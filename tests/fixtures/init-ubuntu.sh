#!/bin/bash
# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT
set -euo pipefail

# Credentials are supplied only to these isolated test containers at runtime.
printf 'root:%s\ntestuser:%s\n' "${TEST_ROOT_PASSWORD:?required}" "${TEST_USER_PASSWORD:?required}" | chpasswd
unset TEST_ROOT_PASSWORD TEST_USER_PASSWORD
ssh-keygen -A
exec /sbin/init --log-level=info --log-target=console
