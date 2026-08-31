"""Every variable a task reads comes from somewhere Ansible actually loads.

A role auto-loads defaults/main.yml and vars/main.yml only. Anything else under
defaults/ or vars/ has to be included explicitly, and a file nobody includes is
invisible: its variables silently fall back to whatever inline default() filter
happens to sit at each reference, or are undefined and fail the run.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
AUTOLOADED = (ROOT / "defaults" / "main.yml", ROOT / "vars" / "main.yml")

# tasks/main.yml loads these by ansible_os_family.
OS_VARS = ("Debian.yml", "RedHat.yml")

ROLE_VARIABLE = re.compile(r"\bwordpress_[a-z0-9_]+\b")


def _defined_per_family() -> dict[str, set[str]]:
    """What is defined for each OS family, separately.

    Unioning the two would let a variable defined only in Debian.yml read as
    defined on RedHat, which is the failure mode this file exists to catch.
    """
    common: set[str] = set()
    for path in AUTOLOADED:
        if path.is_file():
            common |= set(yaml.safe_load(path.read_text()) or {})
    families = {}
    for name in OS_VARS:
        path = ROOT / "vars" / name
        extra = set(yaml.safe_load(path.read_text()) or {}) if path.is_file() else set()
        families[name] = common | extra
    return families


def _defined() -> set[str]:
    """Names defined for every family; anything else is a per-family gap."""
    families = _defined_per_family()
    return set.intersection(*families.values()) if families else set()


COMPARISON = re.compile(
    r"(?:when:\s*|^\s*-\s*)?\b(wordpress_[a-z0-9_]+)\s*(?:==|!=|>=|<=|>|<)\s*\S"
)


def _unguarded_comparisons(text: str):
    """Yield (line, variable) for comparisons with no default() on that name."""
    for number, line in enumerate(text.splitlines(), 1):
        for match in COMPARISON.finditer(line):
            name = match.group(1)
            # Only a default() on this variable makes the comparison safe; an
            # unrelated filter elsewhere on the line does not.
            if re.search(re.escape(name) + r"\s*\|\s*default\(", line):
                continue
            if re.search(re.escape(name) + r"\s+is\s+(not\s+)?defined", line):
                continue
            yield number, name


def _walk(node, when=()):
    if isinstance(node, list):
        for item in node:
            yield from _walk(item, when)
    elif isinstance(node, dict):
        yield node, when
        for key in ("block", "rescue", "always"):
            if key in node:
                yield from _walk(node[key], when)


def _files() -> list[pathlib.Path]:
    return sorted((ROOT / "tasks").glob("*.yml"))


def _var_files() -> list[pathlib.Path]:
    return sorted(
        p for directory in ("defaults", "vars")
        for p in (ROOT / directory).glob("*.yml")
    )


def test_the_corpus_is_not_empty() -> None:
    assert _defined(), "no variables loaded; the layout changed"
    assert _var_files(), "no variable files found"


INCLUDE_KEYS = ("ansible.builtin.include_vars", "include_vars")


def _include_targets(roots=("tasks", "handlers", "meta")) -> tuple[set[str], bool]:
    """Literal include_vars basenames, and whether any target is templated.

    A substring search over the task text would match "security.yml" from
    `include_tasks: security.yml` and clear defaults/security.yml, which is the
    exact file this guard exists to catch. Both the short and FQCN keys count.
    """
    literal: set[str] = set()
    templated = False
    for root in roots:
        base = ROOT / root
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.yml")):
            for task, _ in _walk(yaml.safe_load(path.read_text()) or []):
                for key in INCLUDE_KEYS:
                    spec = task.get(key)
                    values = []
                    if isinstance(spec, str):
                        values = [spec]
                    elif isinstance(spec, dict):
                        values = [v for k, v in spec.items()
                                  if k in ("file", "name", "dir") and isinstance(v, str)]
                    for value in values:
                        if "{{" in value:
                            templated = True
                        else:
                            literal.add(value.rsplit("/", 1)[-1])
    return literal, templated


def _orphans(var_files, reachable: set[str]) -> list[str]:
    """Pure so the rule can be exercised without editing the repository."""
    return sorted(name for name in var_files if name not in reachable)


def test_no_variable_file_is_unreachable() -> None:
    """A file Ansible never loads is a trap: its values look set and are not."""
    literal, templated = _include_targets()
    # tasks/main.yml loads "{{ ansible_os_family }}.yml"; that can only resolve
    # to the family files, which are already reachable. A templated target is
    # therefore not a reason to switch the guard off.
    assert templated, "expected the os-family include_vars; did it move?"
    reachable = {p.name for p in AUTOLOADED} | set(OS_VARS) | literal
    orphans = _orphans([p.name for p in _var_files()], reachable)
    assert not orphans, (
        "these variable files are never loaded, so everything in them is "
        f"silently ignored: {orphans}"
    )


def test_the_orphan_rule_reports_an_unreferenced_file() -> None:
    """Exercise the rule itself, not just today's tree."""
    reachable = {"main.yml", "Debian.yml", "RedHat.yml"}
    assert _orphans(["main.yml", "security.yml"], reachable) == ["security.yml"]
    assert _orphans(["main.yml"], reachable) == []


def test_include_tasks_is_not_mistaken_for_include_vars() -> None:
    literal, _ = _include_targets()
    assert "security.yml" not in literal, (
        "include_tasks: security.yml must not register as an include_vars target"
    )


def test_variables_compared_directly_are_defined() -> None:
    """A bare comparison fails the run when the variable is not defined.

    `when: wordpress_apparmor_mode == "enforce"` has no default to fall back
    on, so an unloaded definition is a hard failure, not a quiet wrong value.
    """
    defined = _defined()
    offenders = [
        f"{path.relative_to(ROOT)}:{number}: {name}"
        for path in _files()
        for number, name in _unguarded_comparisons(path.read_text())
        if name not in defined
    ]
    assert not offenders, (
        "these variables are compared without a default but are not defined "
        f"for every OS family: {offenders}"
    )


def test_the_guard_reports_an_inline_when_comparison() -> None:
    """The earlier version anchored at column 0 and saw only list-form items."""
    inline = 'when: wordpress_apparmor_mode == "enforce"\n'
    listed = '    - wordpress_apparmor_mode == "enforce"\n'
    assert [n for n, _ in _unguarded_comparisons(inline)] == [1]
    assert [n for n, _ in _unguarded_comparisons(listed)] == [1]


def test_the_guard_accepts_a_default_on_the_same_name() -> None:
    guarded = "when: wordpress_apparmor_mode | default('enforce') == 'enforce'\n"
    assert list(_unguarded_comparisons(guarded)) == []


def test_an_unrelated_filter_does_not_excuse_the_comparison() -> None:
    """`| default()` on another name must not silence this one."""
    line = "when: wordpress_apparmor_mode == (other | default('x'))\n"
    assert [name for _, name in _unguarded_comparisons(line)] == [
        "wordpress_apparmor_mode"
    ]


def test_a_variable_defined_for_only_one_family_is_not_counted() -> None:
    """Unioning the families would let a Debian-only name read as defined."""
    families = _defined_per_family()
    shared = _defined()
    single = set.union(*families.values()) - shared
    assert single, (
        "expected at least one per-family variable; if the files converged, "
        "this guard no longer proves anything"
    )
    for name in single:
        assert name not in shared, f"{name} is family-specific but counted as shared"


def test_the_real_families_are_both_read() -> None:
    families = _defined_per_family()
    assert set(families) == set(OS_VARS), f"read {sorted(families)}"
    for name, names in families.items():
        assert len(names) > 50, f"{name} resolved only {len(names)} variables"


def test_the_default_skip_branch_actually_skips() -> None:
    """Prove the branch runs: the same line without default() must be reported."""
    guarded = "when: wordpress_apparmor_mode | default('enforce') == 'enforce'\n"
    bare = "when: wordpress_apparmor_mode == 'enforce'\n"
    assert list(_unguarded_comparisons(guarded)) == []
    assert [n for n, _ in _unguarded_comparisons(bare)] == [1], (
        "the bare form must be reported, otherwise the guarded case proves nothing"
    )


def test_an_is_defined_guard_is_accepted() -> None:
    line = "when: wordpress_apparmor_mode is defined and wordpress_apparmor_mode == 'enforce'\n"
    assert list(_unguarded_comparisons(line)) == []
