# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT
"""Verify SPDX coverage of tracked project files and license metadata consistency."""

import subprocess
from pathlib import Path

import tomllib


def main() -> None:
    """Fail on files missing headers or an explicit REUSE annotation."""
    root = Path(__file__).resolve().parents[1]
    reuse = tomllib.loads((root / "REUSE.toml").read_text())
    annotations = {path: item for item in reuse["annotations"] for path in item["path"]}
    license_id = "MIT"
    files = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    missing = []
    for name in filter(None, files):
        if name.startswith("LICENSES/"):
            continue
        if name in annotations:
            assert annotations[name]["SPDX-License-Identifier"] == license_id, name
            continue
        header = (root / name).read_text()[:1500]
        marker = "SPDX-License-Identifier" + ": " + license_id
        if marker not in header:
            missing.append(name)
    if missing:
        raise ValueError(f"Missing SPDX headers or REUSE annotations: {missing}")
    assert (root / "LICENSE").read_bytes() == (root / "LICENSES" / f"{license_id}.txt").read_bytes()
    assert f"license: {license_id}" in (root / "packaging/nfpm.yaml").read_text()
    print(f"SPDX coverage verified for {len(files) - 1} project files")


if __name__ == "__main__":
    main()
