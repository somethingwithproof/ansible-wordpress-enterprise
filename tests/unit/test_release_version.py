"""Reject ambiguous versions before release workflows can publish packages."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "release_artifacts", Path(__file__).resolve().parents[2] / "scripts/release_artifacts.py"
)
assert spec is not None
assert spec.loader is not None
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


@pytest.mark.parametrize(
    "version", ["1.2", "01.2.3", "1.2.3-01", "1.2.3-a..b", "1.2.3+..", "1.2.3\n", "v1.2.3"]
)
def test_invalid_release_versions(version: str) -> None:
    with pytest.raises(ValueError):
        release.validate_semver(version)


@pytest.mark.parametrize("version", ["0.1.0", "2.0.0", "2.0.0-rc.1", "2.0.0+build.01"])
def test_complete_semver(version: str) -> None:
    assert release.validate_semver(version) == version


def test_release_must_match_source_version() -> None:
    with pytest.raises(ValueError, match="differs from source"):
        release.resolve_version("999.0.0")


def test_rebuild_does_not_include_stale_artifacts(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(release, "ROOT", tmp_path)
    output = release.prepare_output("2.0.0")
    (output / "stale.whl").write_text("old source")
    assert release.prepare_output("2.0.0") == output
    assert list(output.iterdir()) == []


def test_release_cleanup_refuses_symlinked_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(release, "ROOT", tmp_path)
    outside = tmp_path / "unrelated"
    outside.mkdir()
    protected = outside / "keep.txt"
    protected.write_text("keep")
    (tmp_path / "dist").mkdir()
    (tmp_path / "dist/release").symlink_to(outside)
    with pytest.raises(ValueError, match="symlinks"):
        release.prepare_output("2.0.0")
    assert protected.read_text() == "keep"
