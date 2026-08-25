"""No two tasks fight over the same resource.

Ansible applies whichever task runs last, so a second writer to the same
destination silently discards the first. Ownership is a property of the
destination, not of the file the task sits in, so clashes are reported by task
name and intra-file duplicates count.
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
BASELINE = pathlib.Path(__file__).with_name("missing_templates.yml")

# Modules that render a whole file: two of them on one destination conflict.
WHOLE_FILE = {
    "ansible.builtin.template": "dest",
    "ansible.builtin.copy": "dest",
    "ansible.builtin.get_url": "dest",
    "ansible.builtin.unarchive": "dest",
}

# Modules that edit part of a file: several may share a destination as long as
# each targets a different line, block or option.
PARTIAL = {
    # "line" is the value being written, not what identifies the edit: two
    # tasks matching one regexp with different lines is last-write-wins.
    "ansible.builtin.lineinfile": ("path", ("regexp", "insertafter", "insertbefore")),
    "ansible.builtin.blockinfile": ("path", ("marker", "insertafter", "insertbefore")),
    "ansible.builtin.replace": ("path", ("regexp",)),
    "community.general.ini_file": ("path", ("section", "option")),
}

# main.yml includes these under mutually exclusive conditions, so a shared
# destination between them can never be written twice in one run.
EXCLUSIVE_FILES = ({"webserver_apache.yml", "webserver_nginx.yml"},)

VARIABLE = re.compile(r"\{\{\s*([A-Za-z_][\w.]*)")


def _walk(node, when=()):
    """Yield every task with the when conditions inherited from its blocks."""
    if isinstance(node, list):
        for item in node:
            yield from _walk(item, when)
    elif isinstance(node, dict):
        own = node.get("when")
        own = tuple(own) if isinstance(own, list) else ((own,) if own else ())
        inherited = when + own
        yield node, inherited
        for key in ("block", "rescue", "always"):
            if key in node:
                yield from _walk(node[key], inherited)


def _tasks():
    for path in TASKS:
        for task, when in _walk(yaml.safe_load(path.read_text()) or []):
            yield path.name, task, when


@pytest.fixture(scope="module")
def all_tasks() -> list[tuple[str, dict, tuple]]:
    return list(_tasks())


def _normalise(target: str) -> str:
    """Key a destination on its text, with folding and filters flattened.

    A bare {{ var }} collapses to the variable; anything richer keeps its whole
    expression so two different conditionals never compare equal.
    """
    collapsed = " ".join(str(target).split())

    def one(match: re.Match) -> str:
        inner = match.group(0)[2:-2].strip()
        simple = re.fullmatch(r"([A-Za-z_][\w.]*)(\s*\|[^|]*)*", inner)
        if simple:
            return "{{%s}}" % simple.group(1)
        return "{{expr:%s}}" % inner

    return re.sub(r"\{\{.*?\}\}", one, collapsed)


def _constraint(cond) -> tuple[str, str, str] | None:
    m = re.fullmatch(
        r"\s*([\w.]+)\s*(?:\|[^=!]*?)?\s*(==|!=)\s*[\"']([^\"']+)[\"']\s*", str(cond))
    return (m.group(1), m.group(2), m.group(3)) if m else None


def _exclusive(conditions: list[tuple]) -> bool:
    """True only when one variable provably keeps the writers apart.

    Two "!=" tests are not exclusive: x != 'a' and x != 'b' are both true for
    x == 'c'. Disjointness needs equalities on distinct values, or a
    complementary ==/!= pair.
    """
    per_writer = []
    for group in conditions:
        found = {}
        for cond in group:
            c = _constraint(cond)
            if c:
                found.setdefault(c[0], set()).add((c[1], c[2]))
        per_writer.append(found)

    variables = set(per_writer[0]) if per_writer else set()
    for writer in per_writer[1:]:
        variables &= set(writer)

    for var in variables:
        constraints = [w[var] for w in per_writer]
        if any(len(c) != 1 for c in constraints):
            continue
        flat = [next(iter(c)) for c in constraints]
        equalities = [v for op, v in flat if op == "=="]
        if len(equalities) == len(flat) and len(set(equalities)) == len(flat):
            return True
        if len(flat) == 2:
            (op_a, val_a), (op_b, val_b) = flat
            if {op_a, op_b} == {"==", "!="} and val_a == val_b:
                return True
    return False


def test_the_corpus_is_not_empty(all_tasks) -> None:
    assert TASKS, "no task files found; the glob or the layout changed"
    assert len(all_tasks) > 100, f"only {len(all_tasks)} tasks parsed"


def test_cron_entry_names_are_owned_by_one_task(all_tasks) -> None:
    owners = collections.defaultdict(list)
    for filename, task, when in all_tasks:
        cron = task.get("ansible.builtin.cron")
        if isinstance(cron, dict) and "name" in cron:
            owners[cron["name"]].append((f"{filename}:{task.get('name')}", when))
    clash = {
        name: [w for w, _ in writers]
        for name, writers in owners.items()
        if len(writers) > 1 and not _exclusive([c for _, c in writers])
    }
    assert not clash, f"cron entries written by more than one task: {clash}"


def _destinations(all_tasks):
    owners = collections.defaultdict(list)
    for filename, task, when in all_tasks:
        label = f"{filename}:{task.get('name')}"
        for module, key in WHOLE_FILE.items():
            body = task.get(module)
            if isinstance(body, dict) and isinstance(body.get(key), str):
                owners[_normalise(body[key])].append((label, filename, when))
        for module, (key, discriminators) in PARTIAL.items():
            body = task.get(module)
            if not isinstance(body, dict) or not isinstance(body.get(key), str):
                continue
            edit = tuple(str(body.get(d)) for d in discriminators)
            if any("item" in part for part in edit):
                edit += (str(task.get("loop") or task.get("with_items")),)
            owners[f"{_normalise(body[key])}!{edit}"].append((label, filename, when))
    return owners


def test_written_destinations_are_owned_by_one_task(all_tasks) -> None:
    owners = _destinations(all_tasks)
    clash = {}
    for target, writers in owners.items():
        if len(writers) < 2:
            continue
        files = {f for _, f, _ in writers}
        if any(files <= pair for pair in EXCLUSIVE_FILES):
            continue
        if _exclusive([c for _, _, c in writers]):
            continue
        clash[target] = sorted(label for label, _, _ in writers)
    assert not clash, f"destinations written by more than one task: {clash}"


def _missing(all_tasks) -> set[str]:
    return {
        f"{filename}:{task['ansible.builtin.template']['src']}"
        for filename, task, _ in all_tasks
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
        f"tasks reference template sources the role does not ship: {new}. "
        f"Write the template, or add it to {BASELINE.name} with a reason."
    )


def test_the_missing_template_baseline_has_no_stale_entries(all_tasks, baseline) -> None:
    fixed = sorted(baseline - _missing(all_tasks))
    assert not fixed, (
        f"these templates now exist or the task is gone; remove them from "
        f"{BASELINE.name}: {fixed}"
    )


def test_the_missing_template_baseline_never_grows(baseline: set[str]) -> None:
    """The debt is capped at what was recorded when the ratchet went in."""
    recorded = 62
    assert len(baseline) <= recorded, (
        f"the baseline grew to {len(baseline)} from {recorded}; "
        "it is a ratchet, not a bucket"
    )


# --- the guards prove they fire -------------------------------------------

def _synthetic(doc: str):
    return [("synthetic.yml", task, when) for task, when in _walk(yaml.safe_load(doc))]


def test_two_writers_in_one_file_are_reported() -> None:
    tasks = _synthetic("""
- name: First
  ansible.builtin.template: {src: a.j2, dest: /etc/thing.conf}
- name: Second
  ansible.builtin.template: {src: b.j2, dest: /etc/thing.conf}
""")
    with pytest.raises(AssertionError, match="synthetic.yml:First"):
        test_written_destinations_are_owned_by_one_task(tasks)


def test_mutually_exclusive_writers_are_allowed() -> None:
    tasks = _synthetic("""
- name: Pinned
  ansible.builtin.get_url: {url: a, dest: /tmp/x}
  when: wordpress_version != 'latest'
- name: Latest
  ansible.builtin.get_url: {url: b, dest: /tmp/x}
  when: wordpress_version == 'latest'
""")
    test_written_destinations_are_owned_by_one_task(tasks)


def test_folded_and_filtered_destinations_normalise_together() -> None:
    assert _normalise("{{ wordpress_install_dir }}/x") == _normalise(
        "{{ wordpress_install_dir | default('/srv') }}/x"
    )
    assert _normalise("{{ a }}/x\n  ") == _normalise("{{a}}/x")
    assert _normalise("{{ 'a' if x else 'b' }}") != _normalise("{{ 'c' if x else 'd' }}")


def test_partial_edits_to_one_file_do_not_clash() -> None:
    tasks = _synthetic("""
- name: One setting
  ansible.builtin.lineinfile: {path: /etc/php.ini, regexp: '^memory_limit', line: 'memory_limit = 1'}
- name: Another setting
  ansible.builtin.lineinfile: {path: /etc/php.ini, regexp: '^upload_max', line: 'upload_max = 2'}
""")
    test_written_destinations_are_owned_by_one_task(tasks)


def test_the_same_partial_edit_twice_is_reported() -> None:
    tasks = _synthetic("""
- name: One
  ansible.builtin.lineinfile: {path: /etc/php.ini, regexp: '^memory_limit', line: 'memory_limit = 1'}
- name: Two
  ansible.builtin.lineinfile: {path: /etc/php.ini, regexp: '^memory_limit', line: 'memory_limit = 2'}
""")
    with pytest.raises(AssertionError, match="synthetic.yml"):
        test_written_destinations_are_owned_by_one_task(tasks)


# --- a broken feature must stop before it changes anything -----------------

FEATURE_FLAG = {
    "backups.yml": "wordpress_enable_backups",
    "caching.yml": "wordpress_enable_caching",
    "fail2ban.yml": "wordpress_enable_fail2ban",
    "firewall.yml": "wordpress_configure_firewall",
    "monitoring.yml": "wordpress_enable_monitoring",
    "security.yml": "wordpress_enable_security",
    "ssl.yml": "wordpress_enable_ssl",
}


# These reference a missing template from a task the operator has to opt into,
# so the failure already lands only when the feature is asked for.
OPT_IN = {"wpcli.yml", "themes.yml"}


def test_every_affected_file_is_classified(baseline) -> None:
    """Nothing may fall out of the coverage check by being absent from a map."""
    affected = {entry.split(":", 1)[0] for entry in baseline}
    unclassified = sorted(affected - set(FEATURE_FLAG) - OPT_IN)
    assert not unclassified, (
        "these files reference missing templates but are neither feature-gated "
        f"nor recorded as opt-in: {unclassified}"
    )


def test_files_with_missing_templates_fail_before_changing_anything(baseline) -> None:
    """A feature that cannot finish must stop first, not halfway."""
    affected = {entry.split(":", 1)[0] for entry in baseline}
    unguarded = []
    for filename in sorted(affected & set(FEATURE_FLAG)):
        tasks = yaml.safe_load((ROOT / "tasks" / filename).read_text()) or []
        first = tasks[0] if tasks else {}
        if "ansible.builtin.fail" not in first:
            unguarded.append(filename)
    assert not unguarded, (
        "these files reference templates the role does not ship and would abort "
        f"partway through; give them a leading ansible.builtin.fail: {unguarded}"
    )


def test_two_not_equal_conditions_are_not_exclusive() -> None:
    """x != 'a' and x != 'b' are both true for x == 'c'."""
    assert not _exclusive([("web != 'nginx'",), ("web != 'apache'",)])


def test_complementary_conditions_are_exclusive() -> None:
    assert _exclusive([("web == 'nginx'",), ("web != 'nginx'",)])
    assert _exclusive([("web == 'nginx'",), ("web == 'apache'",)])
    assert not _exclusive([("web == 'nginx'",), ("web == 'nginx'",)])


def test_writers_constrained_on_different_variables_are_not_exclusive() -> None:
    assert not _exclusive([("a == 'x'",), ("b == 'y'",)])
