# SPDX-FileCopyrightText: 2025 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT
"""A requirement update must refresh the dependency lock used by CI."""

from __future__ import annotations

import pathlib

import pytest

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

ROOT = pathlib.Path(__file__).resolve().parents[2]


@pytest.mark.parametrize(
    ("input_name", "lock_name"),
    [("requirements.txt", "requirements.lock"),
     ("packaging/build-requirements.in", "packaging/build-requirements.txt")],
)
@pytest.mark.parametrize("python_version", ["3.12", "3.13", "3.14"])
def test_locked_versions_satisfy_declared_requirements(input_name, lock_name, python_version):
    environment = {"python_version": python_version, "python_full_version": python_version + ".0"}
    pins = {}
    for line in (ROOT / lock_name).read_text().splitlines():
        if not line or not line[0].isalnum():
            continue
        pin = Requirement(line.removesuffix(" \\"))
        if pin.marker and not pin.marker.evaluate(environment):
            continue
        name = canonicalize_name(pin.name)
        assert name not in pins, f"overlapping pins for {name} on Python {python_version}"
        spec, = pin.specifier
        assert spec.operator == "=="
        pins[name] = spec.version

    requirements = [Requirement(line) for line in (ROOT / input_name).read_text().splitlines()
                    if line.strip() and not line.startswith("#")]
    assert requirements
    selected = set()
    for requirement in requirements:
        if requirement.marker and not requirement.marker.evaluate(environment):
            continue
        name = canonicalize_name(requirement.name)
        assert name not in selected, f"overlapping requirements for {name} on Python {python_version}"
        selected.add(name)
        assert name in pins, f"{name} is missing from {lock_name}"
        assert pins[name] in requirement.specifier, (
            f"{name}=={pins[name]} violates {requirement}; regenerate {lock_name}"
        )
    if input_name == "requirements.txt":
        assert {"ansible", "ansible-core"} <= selected
