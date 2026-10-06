<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Security policy

Security fixes target the latest maintained 2.22.x release. Older project lines
are outside the current support contract; upgrade using the release and migration
documentation. A platform must still receive vendor security updates and belong
to the verified release matrix. Expired support records block CI and publication.

Report sensitive findings through a private GitHub security advisory:
https://github.com/somethingwithproof/ansible-wordpress-enterprise/security/advisories/new

If private reporting is unavailable to your account, contact the maintainer at
the public author address, thomasvincent@gmail.com. Include affected versions,
impact and a minimal redacted reproducer. Do not put passwords, API keys or
private endpoint data in public issues. Response and fix timing depend on the
finding; this policy does not promise an unverified response SLA.

Use verified TLS and explicit private CA trust, least-privilege credentials and
root-owned package files. Store deployment secrets in Ansible Vault or an
appropriate runtime secret store. Third-party dependency installs used for
release builds are hash-locked and wheel-only. Signed/attested artifacts and
SHA256SUMS provide release verification evidence; review the workflow and its
source commit when assessing an artifact.

The supported OS/runtime matrix and its lifecycle sources are documented in
README.md and the project's machine-readable platform policy. Source examples
for undeployed features are not additional platform support guarantees.

Public WordPress source and static assets use the documented WordPress
`0644` file / `0755` directory convention; neither mode permits writes by
other users. Credentials and salts in `wp-config.php` remain owner-only
(`0600`). Logs and cache directories are private to the service owner/group
(`0750`), and private role security files use `0640` or tighter permissions.
Root-owned system metadata and the system WP-CLI executable intentionally
remain readable or executable by their unprivileged callers.

The isolated Docker regression fixtures use HTTP for unauthenticated
connectivity and redirect assertions with fake fixture configuration. The
separate TLS scenario verifies HTTPS, certificate identity and expiration.
These fixtures do not authorize cleartext production administration.

WordPress's permissions guidance:
https://developer.wordpress.org/advanced-administration/server/file-permissions/
