#!/usr/bin/env python3
"""Validate SemVer and build the project's archives and native release artifacts."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import tomllib
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROLE_PATHS = ("defaults", "vars", "handlers", "meta", "tasks", "templates", "docs", "examples")
SEMVER_IDENTIFIER = re.compile(r"[A-Za-z\d-]+", re.ASCII)


def valid_numeric_identifier(value: str) -> bool:
    """Require ASCII decimal identifiers with no unnecessary leading zeros."""
    return value.isascii() and value.isdecimal() and (len(value) == 1 or not value.startswith("0"))


def validate_identifiers(value: str) -> None:
    """Reject empty identifiers and characters outside SemVer's ASCII alphabet."""
    if not all(SEMVER_IDENTIFIER.fullmatch(part) for part in value.split(".")):
        raise ValueError("SemVer identifiers must be nonempty ASCII letters, digits or hyphens")


def validate_semver(version: str) -> str:
    """Accept complete SemVer, rejecting leading-zero numeric prerelease fields."""
    release, metadata_separator, metadata = version.partition("+")
    core, prerelease_separator, prerelease = release.partition("-")
    numbers = core.split(".")
    if len(numbers) != 3 or not all(valid_numeric_identifier(part) for part in numbers):
        raise ValueError("Release version must be complete SemVer, such as 1.2.3 or 1.2.3-rc.1")
    if metadata_separator:
        validate_identifiers(metadata)
    if prerelease_separator:
        validate_identifiers(prerelease)
        if any(
            part.isdecimal() and not valid_numeric_identifier(part)
            for part in prerelease.split(".")
        ):
            raise ValueError("Numeric prerelease identifiers must not have leading zeros")
    return version


def declared_version() -> str:
    """Read the role version file or Python project metadata."""
    if (ROOT / "VERSION").is_file():
        return (ROOT / "VERSION").read_text().strip()
    return str(tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"])


def resolve_version(requested: str | None = None) -> str:
    """Require the requested release and source version to agree."""
    declared = declared_version()
    version = validate_semver(requested or declared)
    if (ROOT / "VERSION").is_file():
        agrees = version == declared
    else:
        from packaging.version import Version

        agrees = Version(version) == Version(declared)
    if not agrees:
        raise ValueError(f"Release version {version} differs from source version {declared}")
    return version


def commit_epoch() -> int:
    """Use the source commit timestamp for deterministic artifact metadata."""
    return int(
        subprocess.check_output(
            ["git", "show", "-s", "--format=%ct", "HEAD"], cwd=ROOT, text=True
        ).strip()
    )


def copy_role(payload: Path) -> None:
    """Ship role sources and documentation, excluding development state."""
    destination = payload / "usr/share/ansible/roles/wordpress_enterprise"
    destination.mkdir(parents=True)
    for name in ROLE_PATHS:
        source = ROOT / name
        if source.is_dir():
            shutil.copytree(
                source, destination / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc")
            )
    for name in ("README.md", "LICENSE", "VERSION", "requirements.yml"):
        shutil.copy2(ROOT / name, destination / name)


def role_archive(payload: Path, output: Path, epoch: int) -> None:
    """Create a role-installable archive with stable ownership and timestamps."""
    role = payload / "usr/share/ansible/roles/wordpress_enterprise"
    with (
        output.open("wb") as raw,
        gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=epoch) as compressed,
        tarfile.open(fileobj=compressed, mode="w") as archive,
    ):
        for path in sorted(role.rglob("*")):
            if path.is_symlink():
                raise ValueError("Role release sources must not contain symlinks")
            relative = path.relative_to(role)
            if any(part in {".", ".."} or "\\" in part for part in relative.parts):
                raise ValueError("Role archive member names must be safe relative paths")
            info = tarfile.TarInfo(f"wordpress_enterprise/{relative.as_posix()}")
            info.type = tarfile.DIRTYPE if path.is_dir() else tarfile.REGTYPE
            info.size = 0 if path.is_dir() else path.stat().st_size
            info.uid = info.gid = 0
            info.uname = info.gname = "root"
            info.mtime = epoch
            info.mode = 0o755 if path.is_dir() else 0o644
            if path.is_file():
                with path.open("rb") as stream:
                    archive.addfile(info, stream)
            else:
                archive.addfile(info)


def python_payload(payload: Path, wheel: Path, packager: str) -> None:
    """Bundle hash-locked portable clients and generate distro-specific commands."""
    library = payload / "usr/lib/nagios-plugins-collection"
    library.mkdir(parents=True)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--index-url",
            "https://pypi.org/simple",
            "--target",
            str(library),
            "--no-compile",
            "--only-binary=:all:",
            "--platform",
            "manylinux_2_17_x86_64",
            "--implementation",
            "cp",
            "--abi",
            "cp311",
            "--python-version",
            "3.11",
            "--require-hashes",
            "-r",
            str(ROOT / "packaging/runtime-requirements.txt"),
        ],
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--target",
            str(library),
            "--no-compile",
            "--no-deps",
            "--only-binary=:all:",
            str(wheel),
        ],
        check=True,
    )
    shutil.rmtree(library / "bin", ignore_errors=True)
    # The selected clients have portable Python implementations; native packages
    # use those implementations rather than shipping host-specific accelerators.
    for extension in library.rglob("*"):
        if extension.is_file() and extension.suffix in {".so", ".pyd", ".dylib"}:
            extension.unlink()
    scripts = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["scripts"]
    commands = payload / "usr/lib/nagios/plugins"
    commands.mkdir(parents=True)
    interpreter = "/usr/bin/python3.12" if packager == "rpm" else "/usr/bin/python3"
    for name, reference in scripts.items():
        module, function = reference.split(":")
        if (
            not re.fullmatch(r"check_[a-z0-9_]+", name)
            or not re.fullmatch(r"nagios_plugins[.a-z0-9_]+", module)
            or function != "main"
        ):
            raise ValueError("Unexpected console entry point in package metadata")
        target = commands / name
        target.write_text(
            f"#!{interpreter}\nimport sys\nsys.dont_write_bytecode = True\nsys.path.insert(0, '/usr/lib/nagios-plugins-collection')\nfrom {module} import main\nraise SystemExit(main())\n"
        )
        target.chmod(0o755)
    documents = payload / "usr/share/doc/nagios-plugins-collection"
    documents.mkdir(parents=True)
    for name in ("README.md", "LICENSE"):
        shutil.copy2(ROOT / name, documents / name)
    shutil.copytree(ROOT / "docs/source/_static", documents / "docs/source/_static")


def package_contents(payload: Path) -> list[dict[str, Any]]:
    """Assign root ownership and exact installed paths to generated payload files."""
    contents = []
    for path in sorted(payload.rglob("*")):
        if path.is_symlink():
            raise ValueError("Native payload must not contain unexpected symlinks")
        relative = path.relative_to(payload).as_posix()
        if path.is_dir() and relative in {
            "usr",
            "usr/lib",
            "usr/share",
            "usr/share/doc",
            "usr/share/ansible",
            "usr/share/ansible/roles",
            "usr/lib/nagios",
            "usr/lib/nagios/plugins",
        }:
            continue
        item: dict[str, Any] = {"dst": "/" + relative}
        mode = 0o755 if path.is_dir() or "/nagios/plugins/" in str(path) else 0o644
        item["file_info"] = {"mode": mode, "owner": "root", "group": "root"}
        if path.is_dir():
            item["type"] = "dir"
        else:
            item["src"] = str(path)
        contents.append(item)
    return contents


def build_python_archives(output: Path, environment: dict[str, str]) -> Path:
    """Build and validate first-party archives using the installed locked tools."""
    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--no-isolation",
            "--sdist",
            "--wheel",
            "--outdir",
            str(output),
        ],
        cwd=ROOT,
        check=True,
        env=environment,
    )
    wheels = list(output.glob("*.whl"))
    if len(wheels) != 1:
        raise ValueError("Release must contain exactly one project wheel")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "twine",
            "check",
            str(wheels[0]),
            *map(str, output.glob("*.tar.gz")),
        ],
        check=True,
    )
    chart = ROOT / "charts/nagios-plugins-collection"
    if chart.is_dir():
        chart_metadata = yaml.safe_load((chart / "Chart.yaml").read_text())
        if (
            chart_metadata["version"] != declared_version()
            or chart_metadata["appVersion"] != declared_version()
        ):
            raise ValueError("Helm chart and application versions must match the source version")
        subprocess.run(
            ["helm", "package", str(chart), "--destination", str(output)],
            check=True,
            env=environment,
        )
    return wheels[0]


def prepare_output(version: str) -> Path:
    """Replace only the owned, non-symlink artifact directory for a valid version."""
    validate_semver(version)
    output = ROOT / "dist/release" / version
    if any(path.is_symlink() for path in (ROOT / "dist", ROOT / "dist/release", output)):
        raise ValueError("Release output paths must not be symlinks")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    return output


def build_artifacts(version: str) -> Path:
    """Build complete source, checksum and native artifacts for one source version."""
    output = prepare_output(version)
    config = yaml.safe_load((ROOT / "packaging/nfpm.yaml").read_text())
    role = (ROOT / "VERSION").is_file()
    epoch = commit_epoch()
    environment = {**os.environ, "RELEASE_VERSION": version, "SOURCE_DATE_EPOCH": str(epoch)}
    with tempfile.TemporaryDirectory(prefix="native-release-") as directory:
        workspace = Path(directory)
        if role:
            payload = workspace / "role"
            copy_role(payload)
            role_archive(payload, output / f"ansible-wordpress-enterprise-{version}.tar.gz", epoch)
        else:
            wheel = build_python_archives(output, environment)
        for packager in ("deb", "rpm"):
            if not role:
                payload = workspace / packager
                python_payload(payload, wheel, packager)
            native = {**config, "contents": package_contents(payload)}
            generated = workspace / f"{packager}.json"
            generated.write_text(json.dumps(native))
            suffix = "all.deb" if packager == "deb" else "noarch.rpm"
            destination = output / f"{config['name']}_{version}_{suffix}"
            subprocess.run(
                [
                    "nfpm",
                    "package",
                    "--config",
                    str(generated),
                    "--packager",
                    packager,
                    "--target",
                    str(destination),
                ],
                check=True,
                env=environment,
            )
    metadata = {
        "project": config["name"],
        "version": version,
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "source_date_epoch": epoch,
    }
    (output / "release.json").write_text(json.dumps(metadata, indent=2) + "\n")
    artifacts = sorted(
        path for path in output.iterdir() if path.is_file() and path.name != "SHA256SUMS"
    )
    (output / "SHA256SUMS").write_text(
        "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in artifacts
        )
    )
    return output


def main() -> int:
    """Validate source versions and optionally build their release artifacts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "build"))
    parser.add_argument("--version")
    arguments = parser.parse_args()
    version = resolve_version(arguments.version)
    if target := os.environ.get("GITHUB_OUTPUT"):
        with open(target, "a", encoding="utf-8") as stream:
            stream.write(
                f"version={version}\nprerelease={'true' if '-' in version.split('+')[0] else 'false'}\n"
            )
    if arguments.command == "build":
        print(build_artifacts(version))
    else:
        print(version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
