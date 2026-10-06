"""Certificate preflight and ACME recovery use actual Ansible execution."""
from __future__ import annotations

import copy
import datetime
import json
import os
import pathlib
import subprocess
import sys

import pytest
import yaml
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

ROOT = pathlib.Path(__file__).resolve().parents[2]
TASKS = yaml.safe_load((ROOT / 'tasks/ssl_certificate.yml').read_text())


def run_tasks(tmp_path, tasks, variables, selected_tag=None):
    playbook = tmp_path / 'playbook.yml'
    playbook.write_text(yaml.safe_dump([{
        'name': 'TLS safety regression', 'hosts': 'localhost', 'gather_facts': False,
        'vars': {'ansible_python_interpreter': sys.executable, **variables}, 'tasks': tasks,
    }]))
    environment = {key: value for key, value in os.environ.items() if not key.startswith('ANSIBLE_')}
    environment.update({
        'ANSIBLE_CONFIG': str(ROOT / 'tests/fixtures/ansible.cfg'),
        'ANSIBLE_LOCAL_TEMP': str(tmp_path / 'ansible-tmp'),
        'ANSIBLE_LIBRARY': str(tmp_path / 'library'),
        'ANSIBLE_NOCOLOR': '1',
    })
    command = [sys.executable, '-m', 'ansible.cli.playbook', '-i', 'localhost,', '-c', 'local', str(playbook)]
    if selected_tag:
        command.extend(['--tags', selected_tag])
    return subprocess.run(
        command,
        capture_output=True, text=True, timeout=90, env=environment,
    )


@pytest.mark.parametrize('selected_tag', ['ssl', 'nginx', 'apache', 'webserver'])
def test_tls_preparation_runs_before_selected_webserver_phase(tmp_path, selected_tag):
    phases = yaml.safe_load((ROOT / 'tasks/main.yml').read_text())
    preparation = copy.deepcopy(next(task for task in phases if task['name'] == 'Phase 4 | Prepare and validate the TLS certificate'))
    child = tmp_path / 'certificate-probe.yml'
    child.write_text(yaml.safe_dump([{'name': 'Record validated certificate',
                                    'ansible.builtin.set_fact': {'wordpress_ssl_ready': True}}]))
    preparation['ansible.builtin.include_tasks']['file'] = str(child)
    result = run_tasks(tmp_path, [preparation, {
        'name': 'Require certificate readiness before the selected web server',
        'ansible.builtin.assert': {'that': ['wordpress_ssl_ready | default(false) | bool']},
        'tags': [selected_tag],
    }], {'wordpress_enable_ssl': True}, selected_tag=selected_tag)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize('expired,mismatched,dns_name,hostname,expected', [
    (False, False, 'site.example.test', 'site.example.test', True),
    (True, False, 'site.example.test', 'site.example.test', False),
    (False, True, 'site.example.test', 'site.example.test', False),
    (False, False, 'site.example.test', 'other.example.test', False),
    (False, False, '*.example.test', 'site.example.test', True),
    (False, False, '*.example.test', 'deep.site.example.test', False),
])
def test_certificate_preflight(tmp_path, expired, mismatched, dns_name, hostname, expected):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, dns_name)])
    now = datetime.datetime.now(datetime.timezone.utc)
    certificate = (
        x509.CertificateBuilder().subject_name(subject).issuer_name(subject)
        .public_key(key.public_key()).serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=2))
        .not_valid_after(now + datetime.timedelta(days=-1 if expired else 30))
        .add_extension(x509.SubjectAlternativeName([x509.DNSName(dns_name)]), critical=False)
        .sign(key, hashes.SHA256())
    )
    certificate_path = tmp_path / 'certificate.pem'
    certificate_path.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))
    if mismatched:
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    key_path = tmp_path / 'private.key'
    key_path.write_bytes(key.private_bytes(serialization.Encoding.PEM,
                                         serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    key_path.chmod(0o600)
    names = {'Inspect certificate validity', 'Inspect the private key identity',
             'Read the certificate DNS names', 'Reject expired certificates and mismatched keys before configuration',
             'Record that the validated certificate can be served'}
    tasks = [copy.deepcopy(task) for task in TASKS if task.get('name') in names]
    for task in tasks:
        task['become'] = False
    result = run_tasks(tmp_path, tasks, {
        'wordpress_ssl_certificate': str(certificate_path),
        'wordpress_ssl_certificate_key': str(key_path), 'wordpress_server_name': hostname,
    })
    assert (result.returncode == 0) == expected, result.stdout + result.stderr
    if not expected:
        assert 'The TLS certificate must be valid' in result.stdout
        assert 'Record that the validated certificate can be served' not in result.stdout


@pytest.mark.parametrize('issuance_succeeds', [True, False])
def test_acme_always_restores_the_previous_service(tmp_path, issuance_succeeds):
    library = tmp_path / 'library'
    library.mkdir()
    (library / 'service_probe.py').write_text('''from ansible.module_utils.basic import AnsibleModule
import json
from pathlib import Path
module = AnsibleModule(argument_spec={"event_path": {"required": True}, "state": {"required": True}})
path = Path(module.params["event_path"])
events = json.loads(path.read_text()) if path.exists() else []
events.append(module.params["state"])
path.write_text(json.dumps(events))
module.exit_json(changed=True)
''')
    certbot = tmp_path / 'certbot'
    certbot.write_text('#!/bin/sh\nexit ' + ('0' if issuance_succeeds else '42') + '\n')
    certbot.chmod(0o700)
    event_path = tmp_path / 'events.json'
    block = copy.deepcopy(next(task for task in TASKS if 'block' in task))
    block['become'] = False
    for task in [*block['block'], *block['always']]:
        if 'ansible.builtin.service' in task:
            state = task.pop('ansible.builtin.service')['state']
            task['service_probe'] = {'event_path': str(event_path), 'state': state}
        if 'ansible.builtin.command' in task:
            task['ansible.builtin.command']['argv'][0] = str(certbot)
    result = run_tasks(tmp_path, [block], {
        'wordpress_use_letsencrypt': True, 'wordpress_requested_certificate': {'stat': {'exists': False}},
        'wordpress_acme_restore_service': True, 'wordpress_letsencrypt_email': 'admin@example.test',
        'wordpress_server_name': 'site.example.test', 'wordpress_ssl_certificate': str(tmp_path / 'new.pem'),
    })
    assert (result.returncode == 0) == issuance_succeeds, result.stdout + result.stderr
    assert json.loads(event_path.read_text()) == ['stopped', 'started']
