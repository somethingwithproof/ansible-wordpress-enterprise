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

# Task files nothing includes. They never run, so they have no place in the
# ordering and cannot conflict with anything. Recorded rather than ranked so a
# newly orphaned file fails instead of being silently sorted last.
UNREACHABLE = {
    "plugins.yml",      # only reachable if something includes it; nothing does
    "themes.yml",       # same
    "repositories.yml",  # same
    "validate.yml",     # 379 lines of assertions that never run
}

VARIABLE = re.compile(r"\{\{\s*([A-Za-z_][\w.]*)")

# Filled by _destinations(): every writer of a destination, whole-file or partial.
RENDERED = collections.defaultdict(list)


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


def _play_order() -> dict:
    """Where each task file first runs, following includes from main.yml.

    A file included from another task file runs at its parent's position, not
    after everything main.yml lists. Ranking those last put seven of the
    twenty-five files in the wrong order.
    """
    order: dict[str, float] = {"main.yml": -1.0}

    def walk(filename: str, base: float, span: float) -> None:
        path = ROOT / "tasks" / filename
        if not path.is_file():
            return
        tasks = yaml.safe_load(path.read_text()) or []
        includes = [
            t.get("ansible.builtin.include_tasks")
            for t, _ in _walk(tasks)
            if isinstance(t.get("ansible.builtin.include_tasks"), str)
        ]
        for index, target in enumerate(includes):
            position = base + span * (index + 1) / (len(includes) + 1)
            if target in order:
                continue
            order[target] = position
            walk(target, position, span / (len(includes) + 1))

    walk("main.yml", 0.0, 1.0)
    return order


def _tasks():
    for path in TASKS:
        for index, (task, when) in enumerate(
            _walk(yaml.safe_load(path.read_text()) or [])
        ):
            yield path.name, task, when, index


@pytest.fixture(scope="module")
def all_tasks() -> list[tuple[str, dict, tuple, int]]:
    return list(_tasks())


def _resolve_item(part: str, entry) -> str:
    """Substitute one loop entry into an edit discriminator."""
    if isinstance(entry, dict):
        for field, value in entry.items():
            part = part.replace("{{ item.%s }}" % field, str(value))
            part = part.replace("{{item.%s}}" % field, str(value))
    else:
        part = part.replace("{{ item }}", str(entry)).replace("{{item}}", str(entry))
    return part


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
    """Key on the variable *and* its filter chain.

    x | default('a') == 'v' and x == 'v' do not constrain the same expression,
    so treating them as one variable would call two writers exclusive when they
    can both run.
    """
    m = re.fullmatch(
        r"\s*([\w.]+)\s*(\|[^=!]*?)?\s*(==|!=)\s*[\"']([^\"']+)[\"']\s*", str(cond))
    if not m:
        return None
    chain = " ".join((m.group(2) or "").split())
    return (f"{m.group(1)}{chain}", m.group(3), m.group(4))


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
    # A guard that recorded no destinations would pass every ownership check.
    RENDERED.clear()
    owners = _destinations(all_tasks)
    assert len(owners) > 50, f"only {len(owners)} destinations recorded"
    assert len(RENDERED) > 30, f"only {len(RENDERED)} distinct paths recorded"


def test_cron_entry_names_are_owned_by_one_task(all_tasks) -> None:
    owners = collections.defaultdict(list)
    for filename, task, when, position in all_tasks:
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
    for filename, task, when, position in all_tasks:
        label = f"{filename}:{task.get('name')}"
        for module, key in WHOLE_FILE.items():
            body = task.get(module)
            if isinstance(body, dict) and isinstance(body.get(key), str):
                target = _normalise(body[key])
                owners[target].append((label, filename, when))
                body = task.get(module) or {}
                create_only = isinstance(body, dict) and (
                    body.get("force") is False or "creates" in body)
                RENDERED[target].append(
                    ("whole", filename, position, label, when, create_only))
        for module, (key, discriminators) in PARTIAL.items():
            body = task.get(module)
            if not isinstance(body, dict) or not isinstance(body.get(key), str):
                continue
            edit = tuple(str(body.get(d)) for d in discriminators)
            target = _normalise(body[key])
            loop = task.get("loop") or task.get("with_items")
            if any("item" in part for part in edit) and isinstance(loop, list):
                # A literal loop names the options it writes, so two tasks
                # setting the same one collide even from different loops.
                for entry in loop:
                    resolved = tuple(
                        _resolve_item(part, entry) for part in edit
                    )
                    owners[f"{target}!{resolved}"].append((label, filename, when))
            elif any("item" in part for part in edit):
                edit += (str(loop),)
                owners[f"{target}!{edit}"].append((label, filename, when))
            else:
                owners[f"{target}!{edit}"].append((label, filename, when))
            RENDERED[target].append(("partial", filename, position, label, when, False))
    return owners


def test_written_destinations_are_owned_by_one_task(all_tasks) -> None:
    owners = _destinations(all_tasks)
    clash = {}
    for target, writers in owners.items():
        if len(writers) < 2:
            continue
        files = [f for _, f, _ in writers]
        # Only a cross-branch pairing is exempt, and only with one writer per
        # branch: two writers inside one branch are still last-write-wins.
        exempt = any(
            set(files) == pair and len(files) == len(set(files))
            for pair in EXCLUSIVE_FILES
        )
        if exempt or _exclusive([c for _, _, c in writers]):
            continue
        clash[target] = sorted(label for label, _, _ in writers)
    assert not clash, f"destinations written by more than one task: {clash}"


# --- the guards prove they fire -------------------------------------------

def _synthetic(doc: str):
    return [
        ("synthetic.yml", task, when, index)
        for index, (task, when) in enumerate(_walk(yaml.safe_load(doc)))
    ]


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


# These reference a missing template from a task the operator has to opt into,
# so the failure already lands only when the feature is asked for.

def test_two_not_equal_conditions_are_not_exclusive() -> None:
    """x != 'a' and x != 'b' are both true for x == 'c'."""
    assert not _exclusive([("web != 'nginx'",), ("web != 'apache'",)])


def test_complementary_conditions_are_exclusive() -> None:
    assert _exclusive([("web == 'nginx'",), ("web != 'nginx'",)])
    assert _exclusive([("web == 'nginx'",), ("web == 'apache'",)])
    assert not _exclusive([("web == 'nginx'",), ("web == 'nginx'",)])


def test_writers_constrained_on_different_variables_are_not_exclusive() -> None:
    assert not _exclusive([("a == 'x'",), ("b == 'y'",)])


def test_no_destination_is_rendered_by_one_file_and_edited_by_another(
    all_tasks,
) -> None:
    """One file renders it, another edits it: neither owns it.

    Rendering a base file and then tuning lines of it is a normal idiom, and
    whether the tuning survives the next render is a runtime property this
    cannot decide. Within one file that trade-off is visible to whoever reads
    it. Across files it is not: the renderer restores its own output on the
    next converge and silently drops what the other file added, which is how
    .htaccess ended up rewritten and re-appended on every run.
    """
    RENDERED.clear()
    _destinations(all_tasks)
    offenders = {}
    for target, writers in RENDERED.items():
        whole = [w for w in writers if w[0] == "whole" and not w[5]]
        partial = [w for w in writers if w[0] == "partial"]
        if not whole or not partial:
            continue
        if {w[1] for w in whole} | {p[1] for p in partial} == {whole[0][1]}:
            continue
        if _exclusive([w[4] for w in whole] + [p[4] for p in partial]):
            continue
        offenders[target] = sorted(
            [f"renders: {w[3]}" for w in whole] + [f"edits: {p[3]}" for p in partial])
    assert not offenders, (
        "these destinations are rendered by one file and edited by another, so "
        f"the renderer undoes the other file's edit on every run: {offenders}")


def test_a_renderer_and_an_editor_in_different_files_are_reported() -> None:
    """Neither file owns the destination, so the renderer wins by accident."""
    def part(name, doc):
        return [(name, t, w, i) for i, (t, w) in enumerate(_walk(yaml.safe_load(doc)))]
    tasks = part("editor.yml", """
- name: Edit one line
  ansible.builtin.lineinfile: {path: /etc/thing.conf, regexp: '^a', line: 'a=1'}
""") + part("renderer.yml", """
- name: Re-render the whole file
  ansible.builtin.template: {src: thing.j2, dest: /etc/thing.conf}
""")
    with pytest.raises(AssertionError, match="undoes the other"):
        test_no_destination_is_rendered_by_one_file_and_edited_by_another(tasks)


def test_a_renderer_and_an_editor_in_one_file_are_allowed() -> None:
    """Render then tune is a normal idiom and is visible to whoever reads it."""
    tasks = _synthetic("""
- name: Render the whole file
  ansible.builtin.template: {src: thing.j2, dest: /etc/thing.conf}
- name: Adjust one line
  ansible.builtin.lineinfile: {path: /etc/thing.conf, regexp: '^a', line: 'a=1'}
""")
    test_no_destination_is_rendered_by_one_file_and_edited_by_another(tasks)


def test_two_loops_writing_one_option_are_reported() -> None:
    """Different loops that both set the same key are still last-write-wins."""
    tasks = _synthetic("""
- name: First loop
  ansible.builtin.lineinfile:
    path: /etc/php.ini
    regexp: '^{{ item.key }}'
    line: '{{ item.key }} = {{ item.value }}'
  loop:
    - {key: memory_limit, value: '256M'}
- name: Second loop
  ansible.builtin.lineinfile:
    path: /etc/php.ini
    regexp: '^{{ item.key }}'
    line: '{{ item.key }} = {{ item.value }}'
  loop:
    - {key: memory_limit, value: '512M'}
""")
    with pytest.raises(AssertionError, match="synthetic.yml"):
        test_written_destinations_are_owned_by_one_task(tasks)


def test_two_loops_writing_different_options_are_allowed() -> None:
    tasks = _synthetic("""
- name: First loop
  ansible.builtin.lineinfile:
    path: /etc/php.ini
    regexp: '^{{ item.key }}'
    line: '{{ item.key }} = {{ item.value }}'
  loop:
    - {key: memory_limit, value: '256M'}
- name: Second loop
  ansible.builtin.lineinfile:
    path: /etc/php.ini
    regexp: '^{{ item.key }}'
    line: '{{ item.key }} = {{ item.value }}'
  loop:
    - {key: upload_max_filesize, value: '64M'}
""")
    test_written_destinations_are_owned_by_one_task(tasks)


def test_a_filter_chain_is_not_mistaken_for_the_bare_variable() -> None:
    """x | default('a') == 'v' does not constrain the same thing as x == 'v'."""
    assert not _exclusive([("web | default('nginx') == 'nginx'",), ("web == 'apache'",)])
    assert _exclusive([("web == 'nginx'",), ("web == 'apache'",)])
