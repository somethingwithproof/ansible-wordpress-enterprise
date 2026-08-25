"""No two task files fight over the same resource.

Ansible applies whichever include runs last, so a second task writing the same
path, or a second cron entry with the same name, silently discards the first.
Missing template sources fail only at runtime, on the host.
"""

from __future__ import annotations

import collections
import pathlib
import re

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
TASKS = sorted((ROOT / "tasks").glob("*.yml"))
TEMPLATES = ROOT / "templates"

WRITERS = {
    "ansible.builtin.template": ("dest",),
    "ansible.builtin.copy": ("dest",),
    "ansible.builtin.lineinfile": ("path",),
    "ansible.builtin.blockinfile": ("path",),
}


def _walk(node):
    if isinstance(node, list):
        for item in node:
            yield from _walk(item)
    elif isinstance(node, dict):
        yield node
        for key in ("block", "rescue", "always"):
            if key in node:
                yield from _walk(node[key])


def _tasks():
    for path in TASKS:
        for task in _walk(yaml.safe_load(path.read_text()) or []):
            yield path.name, task


@pytest.fixture(scope="module")
def all_tasks() -> list[tuple[str, dict]]:
    return list(_tasks())


def test_the_corpus_is_not_empty(all_tasks) -> None:
    """A guard that scanned nothing must not read as a guard that found nothing."""
    assert TASKS, "no task files found; the glob or the layout changed"
    assert len(all_tasks) > 100, f"only {len(all_tasks)} tasks parsed"


def test_cron_entry_names_are_owned_by_one_file(all_tasks) -> None:
    owners = collections.defaultdict(set)
    for filename, task in all_tasks:
        cron = task.get("ansible.builtin.cron")
        if isinstance(cron, dict) and "name" in cron:
            owners[cron["name"]].add(filename)
    clash = {n: sorted(f) for n, f in owners.items() if len(f) > 1}
    assert not clash, f"cron entries defined in more than one file: {clash}"


def _normalise(target: str) -> str:
    """Compare templated destinations structurally: {{ x }}/a and {{ y }}/a differ."""
    return re.sub(r"\{\{\s*([\w.\[\]'\"]+?)\s*\}\}", r"{{\1}}", target)


def test_written_paths_are_owned_by_one_file(all_tasks) -> None:
    owners = collections.defaultdict(set)
    for filename, task in all_tasks:
        for module, keys in WRITERS.items():
            body = task.get(module)
            if not isinstance(body, dict):
                continue
            for key in keys:
                target = body.get(key)
                if isinstance(target, str):
                    owners[_normalise(target)].add(filename)
    clash = {p: sorted(f) for p, f in owners.items() if len(f) > 1}
    assert not clash, f"paths written from more than one file: {clash}"


BASELINE = pathlib.Path(__file__).with_name("missing_templates.yml")


def _missing(all_tasks) -> set[str]:
    return {
        f"{filename}:{task['ansible.builtin.template']['src']}"
        for filename, task in all_tasks
        if isinstance(task.get("ansible.builtin.template"), dict)
        and "{{" not in task["ansible.builtin.template"].get("src", "{{")
        and not (TEMPLATES / task["ansible.builtin.template"]["src"]).is_file()
    }


@pytest.fixture(scope="module")
def baseline() -> set[str]:
    return set(yaml.safe_load(BASELINE.read_text())["missing_templates"])


def test_no_new_template_is_missing(all_tasks, baseline: set[str]) -> None:
    new = sorted(_missing(all_tasks) - baseline)
    assert not new, (
        "tasks reference template sources the role does not ship: "
        f"{new}. Write the template, or add it to {BASELINE.name} with a reason."
    )


def test_the_missing_template_baseline_has_no_stale_entries(
    all_tasks, baseline: set[str]
) -> None:
    fixed = sorted(baseline - _missing(all_tasks))
    assert not fixed, (
        f"these templates now exist or the task is gone; remove them from "
        f"{BASELINE.name}: {fixed}"
    )
