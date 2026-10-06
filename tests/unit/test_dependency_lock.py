# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT
"""A requirement update must refresh the dependency lock used by CI."""

from __future__ import annotations

import pathlib
import re

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

ROOT = pathlib.Path(__file__).resolve().parents[2]


def test_locked_versions_satisfy_declared_requirements():
    locked = {
        canonicalize_name(name): version
        for name, version in re.findall(
            r"^([\w.-]+)==([^\s]+)", (ROOT / "requirements.lock").read_text(), re.MULTILINE
        )
    }
    requirements = [Requirement(line) for line in (ROOT / "requirements.txt").read_text().splitlines()
                    if line.strip() and not line.startswith("#")]
    assert requirements
    for requirement in requirements:
        name = canonicalize_name(requirement.name)
        assert name in locked, f"{name} is missing from requirements.lock"
        assert locked[name] in requirement.specifier, (
            f"{name}=={locked[name]} violates {requirement}; regenerate requirements.lock"
        )
