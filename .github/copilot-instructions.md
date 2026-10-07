<!--
SPDX-FileCopyrightText: 2025 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# ansible-wordpress-enterprise implementation and review instructions

Read [AGENTS.md](../AGENTS.md) for the complete repository-specific guidance.

## Review priorities

Review platform/feature gates, persisted secrets, TLS and path protections, idempotence and supported runtime contracts.

Require focused regression evidence for changed behavior and preserve existing
correctness/security checks. Offline unit/SPDX/lint checks; default and TLS Molecule contracts only on disposable Ubuntu/Rocky fixtures.

Flag unsupported maturity claims, hidden failures, credentials in code/logs, and
generated output presented as first-party implementation. Review permissions,
immutable Action pins and fork-secret isolation when workflows change. A skipped
check or absent check result is not proof that validation ran.

Keep changes within the requested scope and use `mise` for language runtimes.
