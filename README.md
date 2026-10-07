<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

An Ansible role for configuring WordPress hosts with PHP, a web server, and a local or external database. Platform and input validation run before deployment phases, while task boundaries keep installation, configuration, and verification separately reviewable.

## Supported deployment contract

[meta/platform_support.yml](meta/platform_support.yml) is the support-policy authority. The stable Molecule matrix covers Ubuntu 24.04 with Nginx and Rocky Linux 9 with Apache, both using PHP 8.3. Compatibility examples do not expand that matrix.

The policy currently requires ansible-core 2.21.4 or newer in the 2.21 line (Ansible package 14.4.0 or newer in the 14 line), with maintained controller Python 3.12–3.14. Managed-node interpreter requirements are separate. Consult the policy before selecting versions; older platforms and merely upstream-supported PHP versions are not automatically adopted.

## Feature maturity

The core task sequence is defined in [tasks/main.yml](tasks/main.yml). Monitoring, backup, Fail2ban, security, caching, and firewall groups have missing template contracts recorded in [tests/unit/missing_templates.yml](tests/unit/missing_templates.yml). Their flags remain default-off and validation rejects enabling incomplete groups. Task names and example variables must not be presented as working implementations of those features.

TLS, database credentials, generated WordPress secrets, path guards, and OS-specific handling require the documented configuration and runtime checks. No automatic failover, cloud-wide availability SLA, or universal production-readiness claim is made here.

## Quick start

Install the role from its repository source and its collection dependencies:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git
ansible-galaxy collection install -r requirements.yml
```

Run the collection command from this checkout. Review [defaults/main.yml](defaults/main.yml) and [examples](examples/README.md) before deployment. Use the supported entry point rather than calling internal task phases directly.

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_php_version: "8.3"
    wordpress_site_url: "https://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - ansible-wordpress-enterprise
```

Provide the referenced secrets through Ansible Vault or an existing secret manager. Configure certificates and hostname resolution for the target host before running a deployment. Keep incomplete feature groups disabled.

## Development and testing

The [Makefile](Makefile), [CONTRIBUTING.md](CONTRIBUTING.md), and [TESTING.md](TESTING.md) define the hashed dependency setup, lint checks, unit tests, and disposable Docker/Molecule contracts. Unit tests and lint do not establish a successful deployment.

```bash
make lint
```

Use the testing guide for the stable `default` and `tls` scenarios and their prerequisites. Host installation, upgrade, cleanup, and restore tasks mutate the selected machines; use isolated test inventories for validation.

## Versioning and release packages

Project releases use the complete SemVer version in `VERSION`, independently
of `meta/main.yml`'s minimum Ansible version. Push a matching `v2.22.1` tag on main
to trigger Release, or run it manually from main after creating the matching tag.
The workflow validates that the existing tag points to the checked source, runs the full CI
suite (including both Molecule scenarios), and publishes a Galaxy-compatible
role archive, Debian package, RPM, `release.json` and `SHA256SUMS`.
Publishing uses that verified existing tag without overriding the release API's
default target, so a later workflow update on main does not require broader
workflow-write credentials. A missing or mismatched tag fails before testing.

Verify downloads with `sha256sum --check SHA256SUMS`. Install native packages
with `sudo apt install ./ansible-wordpress-enterprise_2.22.1_all.deb` on Ubuntu
24.04 or `sudo dnf install ./ansible-wordpress-enterprise_2.22.1_noarch.rpm` on
Rocky Linux 9. Both install the role under
`/usr/share/ansible/roles/wordpress_enterprise`; supply a supported Ansible
controller and install `requirements.yml` separately. The archive can be
installed with `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz`.
Native packages contain role sources and documentation and run no deployment
scripts during installation. CI installs, checks and removes both formats.

## Security and license

See [SECURITY.md](SECURITY.md) and the [MIT license](LICENSE). Package metadata, platform support policy, and release validation must remain aligned with the shipped role.
