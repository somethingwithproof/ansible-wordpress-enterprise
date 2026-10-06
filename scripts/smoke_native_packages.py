#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT
"""Install and exercise release packages on the supported Linux distributions."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

PLUGIN_CHECK = """
import importlib
import pathlib
import subprocess
import sys
sys.path.insert(0, '/usr/lib/nagios-plugins-collection')
for name in ('httpx', 'rich', 'boto3', 'dns.resolver', 'kubernetes', 'redis', 'psycopg'):
    importlib.import_module(name)
commands = sorted(pathlib.Path('/usr/lib/nagios/plugins').glob('check_*'))
assert len(commands) == 21, commands
for command in commands:
    result = subprocess.run([str(command), '--help'], capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, (command.name, result.stderr)
    assert 'usage:' in result.stdout.lower(), command
print('All 21 installed checks and runtime clients passed')
"""

ROLE_CHECK = """
import pathlib
import tarfile
role = pathlib.Path('/usr/share/ansible/roles/wordpress_enterprise')
for name in ('tasks/main.yml', 'meta/main.yml', 'defaults/main.yml', 'VERSION', 'LICENSE'):
    path = role / name
    assert path.is_file(), path
    assert path.stat().st_uid == 0, path
archives = list(pathlib.Path('/release').glob('*.tar.gz'))
assert len(archives) == 1
with tarfile.open(archives[0]) as archive:
    names = archive.getnames()
    assert any(name.endswith('/tasks/main.yml') for name in names)
    assert not any('/.git/' in name for name in names)
print('Installed role and Galaxy-compatible archive passed')
"""


def check_distribution(directory: Path, project: str, rpm: bool) -> None:
    """Install a package, validate its commands or role files, then uninstall it."""
    suffix = "*.rpm" if rpm else "*.deb"
    candidates = list(directory.glob(suffix))
    if len(candidates) != 1:
        raise ValueError(f"Expected exactly one {suffix} package")
    package = "/release/" + candidates[0].name
    role = project == "ansible-wordpress-enterprise"
    interpreter = "python3.12" if rpm else "python3"
    if rpm:
        install = ["dnf", "-y", "install", "python3.12", package]
        remove = ["rpm", "-e", project]
        image = "rockylinux:9"
    else:
        install = ["apt-get", "-y", "install", "python3", package]
        remove = ["dpkg", "--remove", project]
        image = "ubuntu:24.04"
    # Arguments are serialized and consumed by Python, never interpolated into shell.
    controller = f"""
import os
import pathlib
import subprocess
os.environ['DEBIAN_FRONTEND'] = 'noninteractive'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
subprocess.run({install!r}, check=True)
subprocess.run([{interpreter!r}, '-c', {(ROLE_CHECK if role else PLUGIN_CHECK)!r}], check=True)
subprocess.run({remove!r}, check=True)
assert not pathlib.Path({("/usr/share/ansible/roles/wordpress_enterprise/tasks/main.yml" if role else "/usr/lib/nagios/plugins/check_website_status")!r}).exists()
"""
    bootstrap = (
        "dnf -y install python3.12" if rpm else "apt-get update && apt-get -y install python3"
    )
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--mount",
            f"type=bind,src={directory},dst=/release,readonly",
            image,
            "bash",
            "-ec",
            bootstrap + f' && exec {interpreter} -c "$1"',
            "--",
            controller,
        ],
        check=True,
    )


def main() -> None:
    """Smoke-test both native formats produced by the release builder."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    directory = parser.parse_args().directory.resolve()
    project = json.loads((directory / "release.json").read_text())["project"]
    if project not in {"ansible-wordpress-enterprise", "nagios-plugins-collection"}:
        raise ValueError("Unexpected release project")
    check_distribution(directory, project, rpm=False)
    check_distribution(directory, project, rpm=True)


if __name__ == "__main__":
    main()
