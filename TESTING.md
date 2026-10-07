<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Testing Guide

This role uses Molecule with Docker for its stable release contract.

## Stable matrix

The single `default` scenario provisions both supported paths from pinned
images:

| Host | Stack |
| --- | --- |
| `ubuntu-24-nginx` | Ubuntu 24.04, PHP 8.3, Nginx |
| `rocky-9-apache` | Rocky Linux 9, PHP 8.3, Apache |

Ubuntu 22.04 and Debian 13 are compatibility targets. Add either to the stable
matrix only after it passes the same end-to-end contract without exceptions.

## Prerequisites

- Docker with permission to run privileged systemd containers
- `mise`
- Git

Install the pinned Python toolchain and Ansible collections:

```bash
mise install python@3.12
mise exec python@3.12 -- python -m pip install --require-hashes --only-binary=:all: -r requirements.lock
mise exec python@3.12 -- ansible-galaxy collection install -r requirements.yml
```

## Release contract

Run the complete lifecycle:

```bash
mise exec python@3.12 -- molecule test --scenario-name default
```

The sequence destroys stale containers, performs syntax validation, creates and
prepares both hosts, converges the role, proves a second convergence reports
zero changes, runs the verifier, and destroys the containers.

The verifier fails closed unless both hosts pass all of these checks:

- expected web server, PHP-FPM, and database services are active;
- Apache or Nginx configuration syntax is valid;
- the requested PHP version is installed;
- WordPress core and its database are valid through WP-CLI;
- `wp-config.php` is mode `0600`;
- the configured HTTP endpoint returns status 200 and dynamic WordPress content;
- no PHP files exist below `wp-content/uploads`.

## Interactive debugging

Keep the environment between individual stages when diagnosing a failure:

```bash
mise exec python@3.12 -- molecule create --scenario-name default
mise exec python@3.12 -- molecule prepare --scenario-name default
mise exec python@3.12 -- molecule converge --scenario-name default
mise exec python@3.12 -- molecule idempotence --scenario-name default
mise exec python@3.12 -- molecule verify --scenario-name default
mise exec python@3.12 -- molecule login --scenario-name default --host ubuntu-24-nginx
mise exec python@3.12 -- molecule destroy --scenario-name default
```

Use `rocky-9-apache` as the login host when investigating the EL9 path.

## Static checks

Run the same fast checks used by CI:

```bash
mise exec python@3.12 -- ansible-lint
mise exec python@3.12 -- pytest -q tests/unit
actionlint .github/workflows/ci.yml .github/workflows/security-tests.yml
```

Core CI uses GitHub-hosted Ubuntu 24.04 for lint, unit tests, both Molecule
scenarios and native package checks. Each job gets an isolated runner with
Docker, so pull requests and releases do not depend on the shared ephemeral
self-hosted queue or compete for identically named containers. The scheduled
`Security Tests` workflow reruns the complete contract daily.

With logging enabled, verification writes `verification-report.txt` in
`wordpress_log_dir`. This snapshot changes only when the observed deployment
state changes; verification checks still execute on every run. It replaces
timestamped reports that made otherwise unchanged deployments non-idempotent.

## Adding platform coverage

Platform support is a tested contract, not a metadata-only declaration. A new
platform must use a pinned image and pass syntax, converge, idempotence, and the
full verifier before it is added to `meta/platform_support.yml` and
`meta/main.yml`.

When adding an independent experiment, place its Molecule files in a distinct
scenario directory and give its containers unique names. Do not weaken or skip
checks in the stable scenario to accommodate a compatibility target.

## Troubleshooting

If a run is interrupted, clean up the named scenario before retrying:

```bash
mise exec python@3.12 -- molecule destroy --scenario-name default
```

For detailed Molecule diagnostics, add `--debug` before the command, for
example `molecule --debug converge --scenario-name default`.

- Molecule documentation: https://molecule.readthedocs.io/
- Ansible documentation: https://docs.ansible.com/
- Issue tracker: https://github.com/somethingwithproof/ansible-wordpress-enterprise/issues
