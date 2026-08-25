"""The declared platforms, the Molecule matrix and the support policy agree.

meta/platform_support.yml is the source of truth. These tests fail when a
supported release reaches end of life, when meta/main.yml drifts from the
policy, or when a supported release is not exercised by a Molecule scenario.
"""

from __future__ import annotations

import datetime
import os
import pathlib
import warnings

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "meta" / "platform_support.yml"
META = ROOT / "meta" / "main.yml"
MOLECULE = sorted((ROOT / "molecule").glob("*/molecule.yml"))


def _load(path: pathlib.Path) -> dict:
    return yaml.safe_load(path.read_text())


@pytest.fixture(scope="module")
def distributions() -> list[dict]:
    return _load(POLICY)["distributions"]


@pytest.fixture(scope="module")
def supported(distributions: list[dict]) -> list[dict]:
    return [d for d in distributions if d["supported"]]


@pytest.fixture(scope="module")
def molecule_images() -> set[str]:
    images = set()
    for path in MOLECULE:
        for platform in _load(path).get("platforms") or []:
            images.add(platform["image"].split("@", 1)[0])
    return images


def test_the_corpus_is_not_empty(distributions: list[dict]) -> None:
    """A moved directory must fail loudly, not pass on zero inputs."""
    assert MOLECULE, "no molecule.yml files found; the layout changed"
    assert distributions, "the support policy is empty"


def _reference_date() -> datetime.date:
    """UTC today, overridable so the check is reproducible on any checkout."""
    override = os.environ.get("PLATFORM_SUPPORT_DATE")
    if override:
        warnings.warn(
            f"PLATFORM_SUPPORT_DATE={override} overrides the end-of-life check; "
            "this is for reproducing an old checkout, not for silencing CI",
            stacklevel=2,
        )
        return datetime.date.fromisoformat(override)
    return datetime.datetime.now(datetime.timezone.utc).date()


def test_no_supported_release_is_end_of_life(supported: list[dict]) -> None:
    today = _reference_date()
    lapsed = [
        f"{d['meta_name']} {d['meta_version']} (eol {d['eol']})"
        for d in supported
        if datetime.date.fromisoformat(d["eol"]) <= today
    ]
    assert not lapsed, f"supported releases past end of life: {lapsed}"


def test_meta_declares_exactly_the_supported_releases(supported: list[dict]) -> None:
    declared = {
        (platform["name"], str(version))
        for platform in _load(META)["galaxy_info"]["platforms"]
        for version in platform["versions"]
    }
    expected = {(d["meta_name"], str(d["meta_version"])) for d in supported}
    assert declared == expected


def test_molecule_runs_only_supported_images(
    distributions: list[dict], molecule_images: set[str]
) -> None:
    allowed = {d["image"] for d in distributions if d["supported"]}
    known = {d["image"]: d for d in distributions}
    offenders = {
        f"{image} ({known[image]['meta_name']} {known[image]['meta_version']})"
        if image in known
        else f"{image} (absent from the policy)"
        for image in molecule_images - allowed
    }
    assert not offenders, f"Molecule runs unsupported images: {sorted(offenders)}"


def test_every_supported_release_is_exercised(
    supported: list[dict], molecule_images: set[str]
) -> None:
    missing = [
        f"{d['meta_name']} {d['meta_version']} ({d['image']})"
        for d in supported
        if d["image"] not in molecule_images
    ]
    assert not missing, f"supported releases with no Molecule coverage: {missing}"


def test_molecule_images_are_pinned_by_digest() -> None:
    unpinned = [
        f"{path.parent.name}: {platform['image']}"
        for path in MOLECULE
        for platform in _load(path).get("platforms") or []
        if "@sha256:" not in platform["image"]
    ]
    assert not unpinned, f"Molecule images not pinned by digest: {unpinned}"


def test_the_date_override_is_not_baked_into_ci() -> None:
    """The override must not become a permanent way to silence the gate."""
    workflows = ROOT / ".github" / "workflows"
    users = [
        p.name for p in sorted(workflows.glob("*.yml"))
        if "PLATFORM_SUPPORT_DATE" in p.read_text(encoding="utf-8")
    ]
    assert not users, f"CI sets PLATFORM_SUPPORT_DATE, disabling the gate: {users}"


def test_the_date_override_is_honoured() -> None:
    previous = os.environ.get("PLATFORM_SUPPORT_DATE")
    os.environ["PLATFORM_SUPPORT_DATE"] = "2000-01-01"
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            assert _reference_date() == datetime.date(2000, 1, 1)
    finally:
        if previous is None:
            del os.environ["PLATFORM_SUPPORT_DATE"]
        else:
            os.environ["PLATFORM_SUPPORT_DATE"] = previous
