<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

<!-- translations:start -->
**Languages:** **English** · [Deutsch](docs/i18n/de/README.md) · [Español](docs/i18n/es/README.md) · [Français](docs/i18n/fr/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Русский](docs/i18n/ru/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [العربية](docs/i18n/ar/README.md) · [हिन्दी](docs/i18n/hi/README.md)

<details>
<summary>All 45 languages (Tier 1, Africa, Asia)</summary>

- **Tier 1:** **English** · [Deutsch](docs/i18n/de/README.md) · [Español](docs/i18n/es/README.md) · [Français](docs/i18n/fr/README.md) · [Italiano](docs/i18n/it/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Nederlands](docs/i18n/nl/README.md) · [Русский](docs/i18n/ru/README.md) · [Українська](docs/i18n/uk/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [繁體中文](docs/i18n/zh-TW/README.md) · [العربية](docs/i18n/ar/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [Polski](docs/i18n/pl/README.md) · [Türkçe](docs/i18n/tr/README.md) · [Svenska](docs/i18n/sv/README.md) · [Tiếng Việt](docs/i18n/vi/README.md) · [Bahasa Indonesia](docs/i18n/id/README.md)
- **Africa:** [Afrikaans](docs/i18n/af-ZA/README.md) · [አማርኛ](docs/i18n/am-ET/README.md) · [العربية (مصر)](docs/i18n/ar-EG/README.md) · [العربية (المغرب)](docs/i18n/ar-MA/README.md) · [Français (Maroc)](docs/i18n/fr-MA/README.md) · [Français (Sénégal)](docs/i18n/fr-SN/README.md) · [Hausa](docs/i18n/ha-NG/README.md) · [Igbo](docs/i18n/ig-NG/README.md) · [Malagasy](docs/i18n/mg-MG/README.md) · [Kinyarwanda](docs/i18n/rw-RW/README.md) · [Soomaali](docs/i18n/so-SO/README.md) · [Kiswahili](docs/i18n/sw-KE/README.md) · [isiXhosa](docs/i18n/xh-ZA/README.md) · [Yorùbá](docs/i18n/yo-NG/README.md) · [isiZulu](docs/i18n/zu-ZA/README.md)
- **Asia:** [বাংলা](docs/i18n/bn/README.md) · [فارسی](docs/i18n/fa/README.md) · [עברית](docs/i18n/he/README.md) · [मराठी](docs/i18n/mr/README.md) · [தமிழ்](docs/i18n/ta/README.md) · [తెలుగు](docs/i18n/te/README.md) · [ไทย](docs/i18n/th/README.md) · [اردو](docs/i18n/ur/README.md) · [Bahasa Melayu](docs/i18n/ms/README.md) · [Filipino](docs/i18n/fil/README.md)

</details>
<!-- translations:end -->

# Ansible WordPress Enterprise

[![CI](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_ansible-wordpress-enterprise&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_ansible-wordpress-enterprise)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/ansible-wordpress-enterprise)](https://github.com/somethingwithproof/ansible-wordpress-enterprise/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/ansible-wordpress-enterprise/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/ansible-wordpress-enterprise)

An Ansible role for configuring WordPress hosts with PHP, a web server, and a local or external database. Platform and input validation run before deployment phases, while task boundaries keep installation, configuration, and verification separately reviewable.

## Supported deployment contract

[meta/platform_support.yml](meta/platform_support.yml) is the support-policy authority. The stable Molecule matrix covers Ubuntu 24.04/PHP 8.3 and Ubuntu 26.04/PHP 8.5 with Nginx, Debian 13/PHP 8.4 with Nginx, and Rocky Linux 9 and 10/PHP 8.3 with Apache. Every path is exercised over HTTP and HTTPS. These are the tested OS/PHP pairs; inventory overrides to untested pairs fail before package changes. EL aliases share the policy, but runtime evidence comes from Rocky Linux containers.

Python 3.12 controllers use Ansible 14.6 or later in the 14.x line with ansible-core 2.21.6 or later in the 2.21 line. Python 3.13 and 3.14 controllers use Ansible 15.x with ansible-core 2.22.x. The hashed requirements lock selects the pair for the controller interpreter. Managed-node interpreter requirements are separate. Consult the policy before selecting versions; older platforms and merely upstream-supported PHP versions are not automatically adopted.

## Feature maturity

The core task sequence is defined in [tasks/main.yml](tasks/main.yml). Monitoring, backup, Fail2ban, security, caching, and firewall groups have missing template contracts recorded in [tests/unit/missing_templates.yml](tests/unit/missing_templates.yml). Their flags remain default-off and validation rejects enabling incomplete groups. Task names and example variables must not be presented as working implementations of those features.

TLS, database credentials, generated WordPress secrets, path guards, and OS-specific handling require the documented configuration and runtime checks. No automatic failover, cloud-wide availability SLA, or universal production-readiness claim is made here.

## Quick start

Install the role from its repository source and its collection dependencies:

```bash
ansible-galaxy role install git+https://github.com/somethingwithproof/ansible-wordpress-enterprise.git,HEAD,wordpress_enterprise
ansible-galaxy collection install -r requirements.yml
```

Run the collection command from this checkout. Review [defaults/main.yml](defaults/main.yml) and [examples](examples/README.md) before deployment. Use the supported entry point rather than calling internal task phases directly.

```yaml
- hosts: wordpress_test_hosts
  become: true
  vars:
    wordpress_web_server: nginx
    wordpress_site_url: "http://wordpress.example.com"
    wordpress_server_name: wordpress.example.com
    wordpress_admin_password: "{{ vault_wordpress_admin_password }}"
    wordpress_db_password: "{{ vault_wordpress_db_password }}"
    wordpress_db_root_password: "{{ vault_wordpress_db_root_password }}"
  roles:
    - wordpress_enterprise
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
suite (including all four Molecule scenarios), and publishes a Galaxy-compatible
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
installed with `ansible-galaxy role install ./ansible-wordpress-enterprise-2.22.1.tar.gz,,wordpress_enterprise`.
Native packages contain role sources and documentation and run no deployment
scripts during installation. CI installs, checks and removes both formats.

## Security and license

See [SECURITY.md](SECURITY.md) and the [MIT license](LICENSE). Package metadata, platform support policy, and release validation must remain aligned with the shipped role.
