"""Exercise the role's HTTPS probes against real trusted and invalid certificates."""

from __future__ import annotations

import copy
import datetime
import http.server
import os
import pathlib
import ssl
import subprocess
import sys
import threading

import pytest
import yaml
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

ROOT = pathlib.Path(__file__).resolve().parents[2]


@pytest.fixture
def tls_endpoint(tmp_path):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
    now = datetime.datetime.now(datetime.timezone.utc)
    certificate = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(subject)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=1))
        .not_valid_after(now + datetime.timedelta(days=1))
        .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(key, hashes.SHA256())
    )
    cert_path, key_path = tmp_path / "ca.pem", tmp_path / "key.pem"
    cert_path.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))
    key_path.write_bytes(key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    ))
    key_path.chmod(0o600)

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_HEAD(self):
            self.send_response(200)
            self.end_headers()

        do_GET = do_HEAD

        def log_message(self, *args):
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(cert_path, key_path)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        yield cert_path, server.server_port
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=5)


@pytest.mark.parametrize("source,name", [
    ("ssl.yml", "Verify SSL configuration"),
    ("verify.yml", "Test HTTPS response (if SSL is enabled)"),
    ("verify.yml", "Test WordPress URL response"),
])
def test_certificate_trust_and_hostname_are_enforced(source, name, tls_endpoint, tmp_path):
    cert_path, port = tls_endpoint
    original = next(task for task in yaml.safe_load((ROOT / "tasks" / source).read_text())
                    if task.get("name") == name)
    cases = [
        ("private CA", "localhost", str(cert_path), False, False, True),
        ("generated development certificate", "localhost", "", True, False, True),
        ("untrusted certificate", "localhost", "", False, False, False),
        ("hostname mismatch", "127.0.0.1", str(cert_path), False, False, False),
        ("Let's Encrypt uses system trust", "localhost", "", True, True, False),
    ]
    tasks = []
    for label, host, ca_path, generated, letsencrypt, expected in cases:
        probe = copy.deepcopy(original)
        probe["name"] = label
        probe["register"] = "probe"
        probe["become"] = False
        probe["ignore_errors"] = True
        probe["vars"] = {
            "wordpress_server_name": host,
            "wordpress_https_port": port,
            "wordpress_enable_ssl": True,
            "wordpress_ssl_ca_path": ca_path,
            "wordpress_ssl_certificate": str(cert_path),
            "wordpress_generate_self_signed_cert": generated,
            "wordpress_use_letsencrypt": letsencrypt,
        }
        # This probe normally starts with HTTP and may redirect to HTTPS.
        # Point it at TLS directly to exercise its certificate policy.
        if name == "Test WordPress URL response":
            probe["ansible.builtin.uri"]["url"] = "https://{{ wordpress_server_name }}:{{ wordpress_https_port }}"
        probe["ansible.builtin.uri"]["use_proxy"] = False
        tasks.append(probe)
        tasks.append({
            "name": f"Check {label}",
            "ansible.builtin.assert": {
                "that": ["probe is succeeded" if expected else "probe is failed"]
                + ([] if expected else ["'CERTIFICATE_VERIFY_FAILED' in probe.msg"]),
            },
        })
    playbook = tmp_path / "verify.yml"
    playbook.write_text(yaml.safe_dump([{
        "name": "Check real TLS behavior", "hosts": "localhost", "gather_facts": False,
        "vars": {"ansible_python_interpreter": sys.executable}, "tasks": tasks,
    }]))
    env = {**os.environ, "ANSIBLE_LOCAL_TEMP": str(tmp_path / "ansible-tmp"),
           "ANSIBLE_NOCOLOR": "1"}
    result = subprocess.run(
        [str(pathlib.Path(sys.executable).with_name("ansible-playbook")),
         "-i", "localhost,", "-c", "local", str(playbook)],
        text=True, capture_output=True, env=env, timeout=90,
    )
    assert result.returncode == 0, result.stdout + result.stderr
