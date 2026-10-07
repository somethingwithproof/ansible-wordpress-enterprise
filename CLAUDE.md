<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# ansible-wordpress-enterprise coding guide

Read [AGENTS.md](AGENTS.md) before making changes. It contains the repository's
architecture, canonical commands, supported boundaries and operating rules.
Follow any applicable nested instructions and the checked-out CI configuration.

## Project priorities

Review platform/feature gates, persisted secrets, TLS and path protections, idempotence and supported runtime contracts.

## Verification

Offline unit/SPDX/lint checks; default and TLS Molecule contracts only on disposable Ubuntu/Rocky fixtures.

Separate offline checks from operations that change hosts, databases, firewalls
or published artifacts. State verification limits and preserve existing controls.
Select language runtimes through `mise`; never commit local session state or secrets.
