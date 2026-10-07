<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# WordPress Enterprise Ansible role agent instructions

## Project and public contract

This repository is an Ansible role. `tasks/main.yml` is the supported entry point;
its platform and input gates precede package/configuration changes. Public
variables use the `wordpress_` prefix in `defaults/main.yml`; tasks, handlers,
Jinja templates and OS variables implement deployment. Do not bypass validation
with direct `tasks_from` execution of internal phases.

`meta/platform_support.yml` is the support-policy authority. The stable Molecule
contract is Ubuntu 24.04/Nginx and Rocky Linux 9/Apache; other examples are not
proof of supported cloud or OS deployment. Keep policy, metadata and test images
aligned. See `README.md`, `CONTRIBUTING.md` and `TESTING.md`.

## Setup and offline checks

Use maintained controller Python through `mise`; inspect `requirements.lock`,
`requirements.yml`, the Makefile and CI before installing dependencies.

```sh
mise exec python@3.12 -- make install
mise exec python@3.12 -- make galaxy-install
mise exec python@3.12 -- pre-commit run --all-files
mise exec python@3.12 -- pytest tests/unit -q
mise exec python@3.12 -- python scripts/check_spdx.py
```

Keep hashed dependency installation. The local role-resolution hook creates an
ignored relative self-link under `.ansible/roles/`; never commit its generated
lock or replace it with a developer-specific absolute symlink.

Only in explicitly selected disposable Docker hosts:

```sh
mise exec python@3.12 -- molecule test --scenario-name default
mise exec python@3.12 -- molecule test --scenario-name tls
```

Require converge, idempotence and runtime verification on both stable targets;
unit tests and lint alone do not prove a deployment works.

## Feature maturity and security

Monitoring, backups, fail2ban, security, caching and firewall feature groups
have missing template contracts recorded in `tests/unit/missing_templates.yml`.
Keep their default-off and fail-closed validation until implementations and
runtime tests exist. Do not advertise these flags as working just because their
tasks or example variables are present.

Preserve database credentials, generated WordPress secrets, path/symlink guards,
TLS certificate-chain/hostname checks, SELinux/AppArmor and restrictive file
ownership. Treat installation, upgrades, cleanup and restores as host mutations;
do not target production inventory or run global Docker pruning for validation.
Native `.deb`/`.rpm` packages contain role sources and must not deploy during
installation. Preserve exact-tag verification and SHA-256 release checks.

## Working rules

Select required language runtimes through `mise`. Read the checked-out manifests,
lockfiles and GitHub Actions before choosing versions or commands; do not infer
support from an old README example. Keep changes focused and preserve public
interfaces, licenses and existing correctness/security checks.

Keep credentials, customer data, `.omc/`, `.worktrees/` and generated output out
of commits. Never disable checks or suppress findings just to obtain a passing
result. Report the commands run, results and untested environments. Publishing,
deploying, modifying live systems and merging require task authorization.
