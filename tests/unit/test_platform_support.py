"""The declared platforms, runtime gates and support policy agree.

meta/platform_support.yml is the source of truth. These tests fail when a
supported release leaves full vendor support, when meta/main.yml drifts from
the policy, or when a supported release is not exercised by a Molecule
scenario. Extended phases (Ubuntu ESM, Debian LTS, EL Maintenance Support) do
not count as supported.
"""

from __future__ import annotations

import datetime
import json
import os
import pathlib
import re
import subprocess
import sys
import warnings

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "meta" / "platform_support.yml"
META = ROOT / "meta" / "main.yml"
MOLECULE = sorted((ROOT / "molecule").glob("*/molecule.yml"))


def _load(path: pathlib.Path) -> dict:
    return yaml.safe_load(path.read_text())


def _supported_runtime_cases() -> list[tuple[dict[str, str], bool, str]]:
    cases = []
    for distribution, releases in _load(POLICY)["runtime_platforms"].items():
        for release in releases:
            cases.append(
                (
                    {
                        "distribution": distribution,
                        "distribution_version": f"{release}.99",
                        "distribution_major_version": release.split(".")[0],
                    },
                    True,
                    "Reject operating systems outside the tested current/LTS contract",
                )
            )
    return cases


@pytest.fixture(scope="module")
def distributions() -> list[dict]:
    return _load(POLICY)["distributions"]


@pytest.fixture(scope="module")
def supported(distributions: list[dict]) -> list[dict]:
    return [d for d in distributions if d["supported"]]


@pytest.fixture(scope="module")
def php_versions() -> list[dict]:
    return _load(POLICY)["php_versions"]


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


def test_release_policy_has_the_required_shape() -> None:
    policy = _load(POLICY)
    assert isinstance(policy.get("runtime_platforms"), dict)
    assert isinstance(policy.get("distributions"), list)
    assert isinstance(policy.get("php_versions"), list)
    assert isinstance(policy.get("ansible_core"), dict)
    assert isinstance(policy.get("ansible_package"), dict)
    for name, releases in policy["runtime_platforms"].items():
        assert isinstance(name, str)
        assert isinstance(releases, list)
        assert releases
        assert all(isinstance(release, str) for release in releases)
    for distribution in policy["distributions"]:
        if distribution.get("supported"):
            assert isinstance(distribution.get("runtime_release"), str)
    for branch in policy["php_versions"]:
        assert {"version", "security_support_ends", "supported"} <= branch.keys()


def test_every_policy_support_date_is_valid(distributions: list[dict]) -> None:
    invalid = []
    for distribution in distributions:
        try:
            datetime.date.fromisoformat(distribution["full_support_ends"])
        except (KeyError, TypeError, ValueError):
            invalid.append(
                f"{distribution.get('meta_name')} {distribution.get('meta_version')}"
            )
    assert not invalid, f"invalid or missing full-support dates: {invalid}"


def _reference_date() -> datetime.date:
    """UTC today, overridable so the check is reproducible on any checkout."""
    override = os.environ.get("PLATFORM_SUPPORT_DATE")
    if override:
        if os.environ.get("CI"):
            raise AssertionError("PLATFORM_SUPPORT_DATE cannot override the support gate in CI")
        warnings.warn(
            f"PLATFORM_SUPPORT_DATE={override} overrides the end-of-life check; "
            "this is for reproducing an old checkout, not for silencing CI",
            stacklevel=2,
        )
        return datetime.date.fromisoformat(override)
    return datetime.datetime.now(datetime.timezone.utc).date()


def test_every_supported_release_still_has_full_vendor_support(
    supported: list[dict],
) -> None:
    """Extended phases do not count: ESM, Debian LTS and EL Maintenance are out."""
    today = _reference_date()
    lapsed = [
        f"{d['meta_name']} {d['meta_version']} (full support ended {d['full_support_ends']})"
        for d in supported
        if datetime.date.fromisoformat(d["full_support_ends"]) <= today
    ]
    assert not lapsed, (
        f"these are supported here but no longer fully supported upstream: {lapsed}"
    )


def test_supported_distributions_are_current_or_lts(supported: list[dict]) -> None:
    offenders = [
        f"{item['meta_name']} {item['meta_version']}"
        for item in supported
        if item.get("release_channel") not in {"current", "lts"}
    ]
    assert not offenders, f"supported releases are neither current nor LTS: {offenders}"


def test_runtime_allowlist_exactly_matches_supported_releases(
    distributions: list[dict],
) -> None:
    policy = _load(POLICY)
    expected: dict[str, list[str]] = {}
    incomplete = []
    for distribution in (item for item in distributions if item["supported"]):
        if not distribution.get("runtime_distributions") or not distribution.get(
            "runtime_release"
        ):
            incomplete.append(
                f"{distribution['meta_name']} {distribution['meta_version']}"
            )
            continue
        for runtime_name in distribution["runtime_distributions"]:
            expected.setdefault(runtime_name, []).append(
                str(distribution["runtime_release"])
            )

    assert not incomplete, f"supported releases lack runtime identities: {incomplete}"
    actual = {
        name: sorted(str(release) for release in releases)
        for name, releases in policy["runtime_platforms"].items()
    }
    expected = {name: sorted(releases) for name, releases in expected.items()}
    assert actual == expected


def test_platform_gate_runs_before_distribution_vars_are_loaded() -> None:
    main_tasks = _load(ROOT / "tasks" / "main.yml")
    main_names = [task["name"] for task in main_tasks]
    include_index = main_names.index("Enforce the managed-node release policy")
    for later_task in (
        "Load operating system variables",
        "Resolve generated credentials once for this run",
        "Phase 1 | Validate inputs and platform",
    ):
        assert include_index < main_names.index(later_task)
    assert main_tasks[include_index]["tags"] == ["always"]
    include = main_tasks[include_index]["ansible.builtin.include_tasks"]
    assert include["file"] == "platform_policy.yml"
    assert include["apply"]["tags"] == ["always"]

    policy_tasks = _load(ROOT / "tasks" / "platform_policy.yml")
    policy_names = [task["name"] for task in policy_tasks]
    assert policy_names == [
        "Require distribution facts for the release gate",
        "Reject operating systems outside the tested current/LTS contract",
        "Reject unsupported PHP release branches",
    ]


@pytest.mark.parametrize(
    ("facts", "accepted", "expected_task"),
    [
        *_supported_runtime_cases(),
        (
            {
                "distribution": "Ubuntu",
                "distribution_version": "24.04",
                "distribution_major_version": "24",
            },
            True,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {
                "distribution": "Ubuntu",
                "distribution_version": "22.04.5",
                "distribution_major_version": "22",
            },
            False,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {
                "distribution": "Ubuntu",
                "distribution_version": "24.10",
                "distribution_major_version": "24",
            },
            False,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {
                "distribution": "Debian",
                "distribution_version": "12.12",
                "distribution_major_version": "12",
            },
            False,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {
                "distribution": "Rocky",
                "distribution_version": "10.1",
                "distribution_major_version": "10",
            },
            False,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {
                "distribution": "CentOS",
                "distribution_version": "9",
                "distribution_major_version": "9",
            },
            False,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {
                "distribution": "Fedora",
                "distribution_version": "40",
                "distribution_major_version": "40",
            },
            False,
            "Reject operating systems outside the tested current/LTS contract",
        ),
        (
            {},
            False,
            "Require distribution facts for the release gate",
        ),
    ],
)
def test_ansible_executes_the_fail_closed_platform_gate(
    tmp_path: pathlib.Path,
    facts: dict[str, str],
    accepted: bool,
    expected_task: str,
) -> None:
    roles = tmp_path / "roles"
    roles.mkdir()
    (roles / "ansible-wordpress-enterprise").symlink_to(ROOT, target_is_directory=True)
    local_tmp = tmp_path / "ansible-tmp"
    local_tmp.mkdir()
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("ANSIBLE_")
    }
    environment.update(
        {
            "ANSIBLE_CONFIG": str(ROOT / "tests" / "fixtures" / "ansible.cfg"),
            "ANSIBLE_LOCAL_TEMP": str(local_tmp),
            "ANSIBLE_ROLES_PATH": str(roles),
            "ANSIBLE_NOCOLOR": "1",
        }
    )
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "ansible.cli.playbook",
            str(ROOT / "tests" / "fixtures" / "platform-policy-playbook.yml"),
            "-i",
            "localhost,",
            "-v",
            "--extra-vars",
            json.dumps(
                {
                    "ansible_facts": facts,
                    "runtime_platforms": {"Debian": ["12"]},
                    "php_versions": [{"version": "8.1", "supported": True}],
                }
            ),
        ],
        check=False,
        capture_output=True,
        cwd=ROOT,
        env=environment,
        text=True,
        timeout=120,
    )
    output = result.stdout + result.stderr
    if accepted:
        assert result.returncode == 0, output
        assert expected_task in output
        assert re.search(r"ok=[1-9]\d*\s+changed=0\s+unreachable=0\s+failed=0", output)
    else:
        assert result.returncode != 0
        assert expected_task in output
        failure_fragment = {
            "Require distribution facts for the release gate": "Distribution facts are required",
            "Reject operating systems outside the tested current/LTS contract": "Unsupported operating system",
        }[expected_task]
        assert failure_fragment in output
        assert "failed=1" in output


@pytest.mark.parametrize(
    ("facts", "php_version", "tag_arguments", "expected_task", "accepted"),
    [
        (
            {
                "distribution": "Debian",
                "distribution_version": "12.12",
                "distribution_major_version": "12",
            },
            "8.3",
            arguments,
            "Reject operating systems outside the tested current/LTS contract",
            False,
        )
        for arguments in ([], ["--tags", "php"], ["--skip-tags", "validate"])
    ]
    + [
        (
            {
                "distribution": "Ubuntu",
                "distribution_version": "24.04.3",
                "distribution_major_version": "24",
                "os_family": "Debian",
            },
            "8.1",
            arguments,
            "Reject unsupported PHP release branches",
            False,
        )
        for arguments in ([], ["--tags", "php"], ["--skip-tags", "validate"])
    ]
    + [
        (
            {
                "distribution": "Ubuntu",
                "distribution_version": "24.04.3",
                "distribution_major_version": "24",
                "os_family": "Debian",
            },
            "8.3",
            ["--tags", "always", "--skip-tags", "validate,prerequisites"],
            "Load operating system variables",
            True,
        ),
        (
            {
                "distribution": "Ubuntu",
                "distribution_version": "24.04",
                "distribution_major_version": "24",
                "os_family": "Debian",
            },
            8.3,
            ["--tags", "php"],
            "Reject unsupported PHP release branches",
            False,
        ),
    ],
)
def test_role_entrypoint_enforces_the_release_gate(
    tmp_path: pathlib.Path,
    facts: dict[str, str],
    php_version: str | float,
    tag_arguments: list[str],
    expected_task: str,
    accepted: bool,
) -> None:
    roles = tmp_path / "roles"
    roles.mkdir()
    (roles / "ansible-wordpress-enterprise").symlink_to(ROOT, target_is_directory=True)
    local_tmp = tmp_path / "ansible-tmp"
    local_tmp.mkdir()
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("ANSIBLE_")
    }
    environment.update(
        {
            "ANSIBLE_CONFIG": str(ROOT / "tests" / "fixtures" / "ansible.cfg"),
            "ANSIBLE_LOCAL_TEMP": str(local_tmp),
            "ANSIBLE_ROLES_PATH": str(roles),
            "ANSIBLE_NOCOLOR": "1",
        }
    )
    command = [
        sys.executable,
        "-m",
        "ansible.cli.playbook",
        str(ROOT / "tests" / "fixtures" / "platform-policy-entrypoint.yml"),
        "-i",
        "localhost,",
        "-v",
        "--extra-vars",
        json.dumps(
            {
                "ansible_facts": facts,
                "wordpress_php_version": php_version,
                **{
                    name: "test-value-with-at-least-32-characters"
                    for name in (
                        "wordpress_db_root_password",
                        "wordpress_db_password",
                        "wordpress_admin_password",
                        "wordpress_auth_key",
                        "wordpress_secure_auth_key",
                        "wordpress_logged_in_key",
                        "wordpress_nonce_key",
                        "wordpress_auth_salt",
                        "wordpress_secure_auth_salt",
                        "wordpress_logged_in_salt",
                        "wordpress_nonce_salt",
                    )
                },
            }
        ),
        *tag_arguments,
    ]
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        cwd=ROOT,
        env=environment,
        text=True,
        timeout=120,
    )
    output = result.stdout + result.stderr
    if accepted:
        assert result.returncode == 0, output
        assert "Reject operating systems outside the tested current/LTS contract" in output
        assert "Reject unsupported PHP release branches" in output
        assert expected_task in output
        assert "failed=0" in output
        for mutating_task in (
            "Update package cache",
            "Create WordPress system group",
            "Create WordPress system user",
        ):
            assert mutating_task not in output
    else:
        assert result.returncode != 0
        assert expected_task in output
        failure_fragment = (
            "Unsupported operating system"
            if expected_task.startswith("Reject operating systems")
            else "end-of-life, or unverified PHP version"
        )
        assert failure_fragment in output
        assert "Load operating system variables" not in output
        assert "failed=1" in output


def test_legacy_platform_images_follow_the_runtime_policy() -> None:
    policy = _load(POLICY)["runtime_platforms"]
    ubuntu = (ROOT / "tests" / "dockerfiles" / "Dockerfile.ubuntu").read_text()
    rocky = (ROOT / "tests" / "dockerfiles" / "Dockerfile.centos").read_text()
    ubuntu_release = re.search(r"^FROM ubuntu:(\d+\.\d+)$", ubuntu, re.MULTILINE)
    rocky_release = re.search(r"^FROM rockylinux:(\d+)$", rocky, re.MULTILINE)
    assert ubuntu_release
    assert ubuntu_release.group(1) in policy["Ubuntu"]
    assert rocky_release
    assert rocky_release.group(1) in policy["Rocky"]


def test_breaking_release_removals_are_documented() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text()
    marker = "## [Unreleased]"
    assert marker in changelog
    remainder = changelog.split(marker, 1)[1]
    next_release = re.search(r"\n## \[", remainder)
    assert next_release, "the changelog has no release heading after Unreleased"
    unreleased = remainder[: next_release.start()]
    for text in (
        "Ubuntu 24.04 LTS",
        "Enterprise Linux 9",
        "PHP 7.4, 8.0, and 8.1",
        "default PHP branch changes from 8.2 to 8.3",
        "breaking changes",
    ):
        assert text in unreleased


def test_supported_php_branches_have_not_reached_eol(
    php_versions: list[dict],
) -> None:
    today = _reference_date()
    invalid_dates = []
    lapsed = []
    for branch in php_versions:
        try:
            end = datetime.date.fromisoformat(branch["security_support_ends"])
        except (KeyError, TypeError, ValueError):
            invalid_dates.append(branch.get("version"))
            continue
        if branch["supported"] and end <= today:
            lapsed.append(f"PHP {branch['version']} ({end})")

    assert not invalid_dates, f"PHP branches have invalid support dates: {invalid_dates}"
    assert not lapsed, f"supported PHP branches have reached end of life: {lapsed}"


def test_php_gate_consumes_the_release_policy() -> None:
    preflight = (ROOT / "tasks" / "platform_policy.yml").read_text()
    assert "role_path ~ '/meta/platform_support.yml'" in preflight
    for obsolete in ("'7.4'", "'8.0'", "'8.1'"):
        assert obsolete not in preflight


def test_default_php_branch_is_supported(php_versions: list[dict]) -> None:
    default = _load(ROOT / "defaults" / "main.yml")["wordpress_php_version"]
    allowed = {item["version"] for item in php_versions if item["supported"]}
    assert default in allowed


def test_repository_examples_use_only_supported_php_branches(
    php_versions: list[dict],
) -> None:
    allowed = {item["version"] for item in php_versions if item["supported"]}
    candidates = sorted(
        path
        for path in ROOT.rglob("*")
        if path.suffix in {".yml", ".yaml", ".md"}
        and path.name != "CHANGELOG.md"
        and "tests/unit" not in str(path.relative_to(ROOT))
        and ".ansible" not in path.parts
        and not {".venv", ".tox", "node_modules"}.intersection(path.parts)
    )
    assert candidates, "no YAML or Markdown policy consumers found"
    patterns = [
        r"wordpress_php_version:\s*[\"']?(\d+\.\d+)[\"']?",
        r"wordpress_php_version=(\d+\.\d+)",
        r"wordpress_php_version\s*\|\s*default\([\"'](\d+\.\d+)[\"']\)",
    ]
    offenders = []
    for path in candidates:
        content = path.read_text()
        versions = [
            version
            for pattern in patterns
            for version in re.findall(pattern, content)
        ]
        offenders.extend(
            f"{path.relative_to(ROOT)}: PHP {version}"
            for version in versions
            if version not in allowed
        )
    assert not offenders, f"examples select unsupported PHP branches: {offenders}"


def test_meta_declares_exactly_the_supported_releases(supported: list[dict]) -> None:
    declared = {
        (platform["name"], str(version))
        for platform in _load(META)["galaxy_info"]["platforms"]
        for version in platform["versions"]
    }
    expected = {(d["meta_name"], str(d["meta_version"])) for d in supported}
    assert declared == expected


def test_meta_declares_the_documented_ansible_floor() -> None:
    requirements = (ROOT / "requirements.txt").read_text()
    match = re.search(r"^ansible-core>=(\d+\.\d+)", requirements, re.MULTILINE)
    assert match, "requirements.txt does not declare an ansible-core lower bound"
    assert _load(META)["galaxy_info"]["min_ansible_version"] == match.group(1)


def test_ansible_core_is_bounded_to_the_current_release_line() -> None:
    requirements = (ROOT / "requirements.txt").read_text()
    core = _load(POLICY)["ansible_core"]
    expected = f"ansible-core>={core['minimum_version']},<{core['next_release']}"
    assert expected in requirements.splitlines()
    assert core["minimum_version"].startswith(f"{core['release_line']}.")
    major, minor = (int(part) for part in core["release_line"].split("."))
    assert core["next_release"] == f"{major}.{minor + 1}.0"


def test_ansible_package_is_bounded_to_the_current_release_line() -> None:
    requirements = (ROOT / "requirements.txt").read_text()
    package = _load(POLICY)["ansible_package"]
    expected = f"ansible>={package['minimum_version']},<{package['next_release']}"
    assert expected in requirements.splitlines()
    major = int(package["release_line"])
    assert package["minimum_version"].startswith(f"{major}.")
    assert package["next_release"] == f"{major + 1}.0.0"


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
    candidates = [
        *sorted((ROOT / ".github").rglob("*.yml")),
        *sorted((ROOT / ".github").rglob("*.yaml")),
        *[ROOT / name for name in
          ("tox.ini", "Makefile", ".env", "pytest.ini", "setup.cfg", "pyproject.toml",
           "docker-compose.yml", "docker-compose.test.yml", "Dockerfile")],
    ]
    users = sorted({
        str(p.relative_to(ROOT)) for p in candidates
        if p.is_file() and "PLATFORM_SUPPORT_DATE" in p.read_text(encoding="utf-8")
    })
    assert not users, f"PLATFORM_SUPPORT_DATE is set in-tree, disabling the gate: {users}"


def test_the_date_override_is_honoured(monkeypatch) -> None:
    monkeypatch.delenv("CI", raising=False)
    monkeypatch.setenv("PLATFORM_SUPPORT_DATE", "2000-01-01")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert _reference_date() == datetime.date(2000, 1, 1)


def test_the_date_override_is_refused_in_ci(monkeypatch) -> None:
    monkeypatch.setenv("PLATFORM_SUPPORT_DATE", "2000-01-01")
    monkeypatch.setenv("CI", "true")
    with pytest.raises(AssertionError, match="cannot override"):
        _reference_date()


def test_reference_date_uses_utc_today_without_an_override(monkeypatch) -> None:
    monkeypatch.delenv("PLATFORM_SUPPORT_DATE", raising=False)
    monkeypatch.delenv("CI", raising=False)
    assert _reference_date() == datetime.datetime.now(datetime.timezone.utc).date()
