"""No two tasks fight over the same resource.

Ansible applies whichever task runs last, so a second writer to the same
destination silently discards the first. Ownership is a property of the
destination, not of the file the task sits in, so clashes are reported by task
name and intra-file duplicates count.
"""

from __future__ import annotations

import collections
import functools
import pathlib
import re

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
TASKS = sorted((ROOT / "tasks").rglob("*.y*ml"))
EXPECTED_TASK_FILE_COUNT = 27
TEMPLATES = ROOT / "templates"
BASELINE = pathlib.Path(__file__).with_name("missing_templates.yml")
DEFAULT_VALUES = yaml.safe_load((ROOT / "defaults" / "main.yml").read_text())

FEATURE_FLAG = {
    "backups.yml": "wordpress_enable_backups",
    "caching.yml": "wordpress_enable_caching",
    "fail2ban.yml": "wordpress_enable_fail2ban",
    "firewall.yml": "wordpress_configure_firewall",
    "monitoring.yml": "wordpress_enable_monitoring",
    "security.yml": "wordpress_enable_security",
}

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
    "ansible.builtin.lineinfile": ("path", ("regexp",)),
    "ansible.builtin.blockinfile": ("path", ("marker",)),
    "ansible.builtin.replace": ("path", ("regexp",)),
    "community.general.ini_file": ("path", ("section", "option")),
}

WP_CONFIG_WRITERS = {
    "ansible.builtin.file": "path",
    "ansible.builtin.template": "dest",
    "ansible.builtin.copy": "dest",
    "ansible.builtin.get_url": "dest",
    "ansible.builtin.unarchive": "dest",
    "ansible.builtin.lineinfile": "path",
    "ansible.builtin.blockinfile": "path",
    "ansible.builtin.replace": "path",
    "community.general.ini_file": "path",
}

# main.yml includes these under mutually exclusive conditions, so a shared
# destination between them can never be written twice in one run.
EXCLUSIVE_FILES = ({"webserver_apache.yml", "webserver_nginx.yml"},)

# These files are deliberately rendered once and then extended with optional
# settings. Their partial writers use distinct discriminators checked below.
WHOLE_PARTIAL_ALLOWED = {
    "{{expr:'/etc/redis/redis.conf' if ansible_facts.os_family == 'Debian' else '/etc/redis.conf'}}",
    "/etc/fail2ban/jail.local",
    "{{wordpress_install_dir}}/wp-config.php",
}

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
            yield str(path.relative_to(ROOT / "tasks")), task, when


@pytest.fixture(scope="module")
def all_tasks() -> list[tuple[str, dict, tuple]]:
    return list(_tasks())


@pytest.fixture(scope="module")
def security_tasks(all_tasks) -> list[tuple[str, dict, tuple]]:
    handlers = ROOT / "handlers" / "main.yml"
    assert handlers.is_file(), "handlers/main.yml is absent from the security corpus"
    handler_tasks = [
        ("handlers/main.yml", task, when)
        for task, when in _walk(yaml.safe_load(handlers.read_text()) or [])
    ]
    assert handler_tasks, "handlers/main.yml contains no tasks"
    return [*all_tasks, *handler_tasks]


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


def _constraint(cond) -> tuple[str, str, str, str | None] | None:
    m = re.fullmatch(
        r"""\s*([\w.]+)
            (?:\s*\|\s*default\(\s*["']([^"']+)["']\s*\))?
            \s*(==|!=)\s*["']([^"']+)["']\s*""",
        str(cond),
        re.VERBOSE,
    )
    return (m.group(1), m.group(3), m.group(4), m.group(2)) if m else None


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
                found.setdefault(c[0], set()).add((c[1], c[2], c[3]))
        per_writer.append(found)

    variables = set(per_writer[0]) if per_writer else set()
    for writer in per_writer[1:]:
        variables &= set(writer)

    for var in variables:
        constraints = [w[var] for w in per_writer]
        if any(len(c) != 1 for c in constraints):
            continue
        flat = [next(iter(c)) for c in constraints]
        if len({default for _, _, default in flat}) != 1:
            continue
        equalities = [v for op, v, _ in flat if op == "=="]
        if len(equalities) == len(flat) and len(set(equalities)) == len(flat):
            return True
        if len(flat) == 2:
            (op_a, val_a, _), (op_b, val_b, _) = flat
            if {op_a, op_b} == {"==", "!="} and val_a == val_b:
                return True
    return False


def test_the_corpus_is_not_empty(all_tasks) -> None:
    assert TASKS, "no task files found; the glob or the layout changed"
    assert len(TASKS) == EXPECTED_TASK_FILE_COUNT, (
        f"task-file corpus changed from {EXPECTED_TASK_FILE_COUNT} to {len(TASKS)}; "
        "review the new or relocated files and update the pin deliberately"
    )
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
    all_tasks = list(all_tasks)
    owners = collections.defaultdict(list)
    whole_targets = {
        _normalise(task[module][key])
        for _, task, _ in all_tasks
        for module, key in WHOLE_FILE.items()
        if isinstance(task.get(module), dict)
        and isinstance(task[module].get(key), str)
    }
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
            edits = [edit]
            loop = task.get("loop")
            if any("item" in part for part in edit) and isinstance(loop, list):
                edits = []
                for item in loop:
                    rendered = []
                    for part in edit:
                        if isinstance(item, dict):
                            part = re.sub(
                                r"\{\{\s*item\.([A-Za-z_]\w*)\s*\}\}",
                                lambda match: str(item.get(match.group(1))),
                                part,
                            )
                        else:
                            part = re.sub(r"\{\{\s*item\s*\}\}", str(item), part)
                        rendered.append(part)
                    edits.append(tuple(rendered))
            target = _normalise(body[key])
            crosses_whole_writer = (
                target in whole_targets and target not in WHOLE_PARTIAL_ALLOWED
            )
            for resolved_edit in edits:
                owner_key = (
                    target if crosses_whole_writer
                    else f"{target}!{resolved_edit}"
                )
                owners[owner_key].append((label, filename, when))
    return owners


FILE_ATTRIBUTES = ("mode", "owner", "group", "state")
FILE_ATTRIBUTE_TRANSITIONS = {
    # A disposable download workspace is created before extraction and removed
    # after the installation has completed.
    ("/tmp/wordpress-download", "state"): ("directory", "absent"),
}


def _render_loop_item(value, item) -> str:
    rendered = str(value)
    if isinstance(item, dict):
        return re.sub(
            r"\{\{\s*item\.([A-Za-z_]\w*)(?:\s*\|.*?)?\s*\}\}",
            lambda match: str(item.get(match.group(1))),
            rendered,
        )
    return re.sub(r"\{\{\s*item\s*\}\}", str(item), rendered)


def _normalise_file_value(value) -> str:
    rendered = str(value)
    expression = re.fullmatch(r"\{\{\s*([A-Za-z_]\w*)(?:\s*\|.*?)?\s*\}\}", rendered)
    if expression and expression.group(1) in DEFAULT_VALUES:
        return str(DEFAULT_VALUES[expression.group(1)])
    return _normalise(rendered)


@functools.cache
def _starts_with_unconditional_failure(filename: str) -> bool:
    source = ROOT / "tasks" / filename
    source_tasks = yaml.safe_load(source.read_text()) or [] if source.is_file() else []
    first = source_tasks[0] if source_tasks else {}
    return (
        "ansible.builtin.fail" in first
        and "when" not in first
        and not first.get("ignore_errors")
    )


def _file_attribute_writers(all_tasks):
    writers = collections.defaultdict(list)
    for filename, task, when in all_tasks:
        if _starts_with_unconditional_failure(filename):
            continue
        body = task.get("ansible.builtin.file")
        if not isinstance(body, dict) or not isinstance(body.get("path"), str):
            continue
        loop = task.get("loop")
        items = loop if isinstance(loop, list) and "item" in body["path"] else [None]
        for item in items:
            target = _normalise(
                body["path"] if item is None else _render_loop_item(body["path"], item)
            )
            for attribute in FILE_ATTRIBUTES:
                if attribute in body:
                    value = body[attribute]
                    if item is not None:
                        value = _render_loop_item(value, item)
                    writers[(target, attribute)].append(
                        (_normalise_file_value(value), f"{filename}:{task.get('name')}", when)
                    )
    return writers


def test_file_attributes_do_not_conflict(all_tasks) -> None:
    clashes = {}
    for (target, attribute), writers in _file_attribute_writers(all_tasks).items():
        transition = FILE_ATTRIBUTE_TRANSITIONS.get((target, attribute))
        if transition and set(transition) == {value for value, _, _ in writers}:
            continue
        conflicts = []
        for index, (value, label, conditions) in enumerate(writers):
            for other_value, other_label, other_conditions in writers[index + 1:]:
                if value == other_value:
                    continue
                if _exclusive([conditions, other_conditions]):
                    continue
                conflicts.extend((f"{label}={value}", f"{other_label}={other_value}"))
        if conflicts:
            clashes[f"{target}:{attribute}"] = sorted(set(conflicts))
    assert not clashes, f"file attributes have conflicting writers: {clashes}"


def test_allowed_file_transitions_are_ordered(all_tasks) -> None:
    writers = _file_attribute_writers(all_tasks)
    for key, transition in FILE_ATTRIBUTE_TRANSITIONS.items():
        actual = [value for value, _, _ in writers[key]]
        positions = [actual.index(value) for value in transition]
        assert positions == sorted(positions), f"file transition is out of order: {key}"


def _wp_config_modes(all_tasks) -> set[str]:
    all_tasks = list(all_tasks)
    target = "{{wordpress_install_dir}}/wp-config.php"
    install_root = "{{wordpress_install_dir}}"
    install_literal = str(DEFAULT_VALUES["wordpress_install_dir"]).rstrip("/")
    safe_dynamic_file_lists = set()
    for _, task, _ in all_tasks:
        find = task.get("ansible.builtin.find")
        register = task.get("register")
        if not isinstance(find, dict) or not isinstance(register, str):
            continue
        paths = find.get("paths")
        paths = paths if isinstance(paths, list) else [paths]
        normalised = [_normalise(path).rstrip("/") for path in paths if isinstance(path, str)]
        if normalised and all(
            path.startswith(f"{install_root}/")
            and path != target
            and not ({".", ".."} & set(path.split("/")))
            for path in normalised
        ):
            safe_dynamic_file_lists.add(register)
    modes = set()
    for _, task, _ in all_tasks:
        for module, destination in WP_CONFIG_WRITERS.items():
            body = task.get(module)
            if not isinstance(body, dict) or not isinstance(body.get(destination), str):
                continue
            # A nonrecursive directory task cannot chmod a regular wp-config.php:
            # Ansible rejects an existing file when state is directory.
            if (
                module == "ansible.builtin.file"
                and body.get("state") == "directory"
                and body.get("recurse", False) is False
            ):
                continue
            loop = task.get("loop")
            loop_values = " ".join(str(value) for value in body.values())
            dynamic_loop = loop is not None and not isinstance(loop, list) and "item" in loop_values
            loop_is_scoped_below_config = any(
                register in str(loop) for register in safe_dynamic_file_lists
            )
            unresolved_destination = _normalise(body[destination])
            static_prefix = unresolved_destination.split("{{item", 1)[0].rstrip("/")
            item_is_sanitized_below_config = (
                "| basename" in body[destination]
                and static_prefix.startswith(f"{install_root}/")
                and static_prefix != install_root
            )
            destination_is_fixed_outside_install = (
                static_prefix.startswith("/")
                and not static_prefix.startswith(install_literal)
                and not install_literal.startswith(f"{static_prefix}/")
            )
            if (
                dynamic_loop
                and "item" in unresolved_destination
                and not loop_is_scoped_below_config
                and not item_is_sanitized_below_config
                and not destination_is_fixed_outside_install
                and body.get("mode") is not None
            ):
                # An unresolved runtime item could target wp-config.php. Record
                # its mode rather than silently treating the writer as safe.
                modes.add(_normalise_file_value(body["mode"]))
                continue
            items = loop if isinstance(loop, list) and "item" in loop_values else [None]
            for item in items:
                destination_value = body[destination]
                mode = body.get("mode")
                recurse = body.get("recurse", False)
                if item is not None:
                    destination_value = _render_loop_item(destination_value, item)
                    mode = _render_loop_item(mode, item) if mode is not None else None
                    recurse = _render_loop_item(recurse, item)
                destination_symbolic = _normalise(destination_value).rstrip("/")
                destination_literal = _normalise_file_value(destination_value).rstrip("/")
                recurse_is_false = recurse is False or str(recurse).lower() in {
                    "false", "none", "0", ""
                }
                recursively_reaches_config = (
                    module == "ansible.builtin.file"
                    and not recurse_is_false
                    and (
                        destination_symbolic == install_root
                        or install_literal == destination_literal
                        or install_literal.startswith(f"{destination_literal}/")
                    )
                )
                direct_config = (
                    destination_symbolic == target
                    or destination_literal == f"{install_literal}/wp-config.php"
                    or bool(re.fullmatch(
                        r"\{\{wordpress_\w*(?:dir|path)\}\}/wp-config\.php",
                        destination_symbolic,
                    ))
                )
                writes_config = direct_config or recursively_reaches_config
                if writes_config:
                    if mode is not None:
                        modes.add(_normalise_file_value(mode))
                    elif direct_config:
                        modes.add("MISSING")
        for module in ("ansible.builtin.command", "ansible.builtin.shell"):
            command = _command_text(task, module)
            for statement in _command_statements(command):
                if "wp-config.php" not in statement:
                    continue
                if re.search(
                    r"(?:!|-not)\s+-name\s+['\"]?wp-config\.php\*['\"]?",
                    statement,
                ):
                    continue
                chmod_mode = re.search(r"\bchmod\b(?:\s+-\S+)*\s+([0-7]{3,4})\b", statement)
                install_mode = re.search(r"\binstall\b.*?\s-m\s+([0-7]{3,4})\b", statement)
                mode_match = chmod_mode or install_mode
                if mode_match:
                    modes.add(mode_match.group(1).lstrip("0").zfill(4))
                    continue
                variable_mode = re.search(
                    r"\b(?:chmod|install\s+-m)\b.*?\{\{\s*([A-Za-z_]\w*)", statement
                )
                if variable_mode and variable_mode.group(1) in DEFAULT_VALUES:
                    modes.add(_normalise_file_value(f"{{{{ {variable_mode.group(1)} }}}}"))
    return modes


def _command_text(task: dict, module: str) -> str:
    body = task.get(module)
    if isinstance(body, str):
        return body
    if not isinstance(body, dict):
        return ""
    if isinstance(body.get("cmd"), str):
        return body["cmd"]
    if isinstance(body.get("argv"), list):
        return " ".join(str(argument) for argument in body["argv"])
    return ""


def _command_statements(command: str) -> list[str]:
    return re.split(r"\s*(?:(?<!\\);|&&|\|\||\n)\s*", command)


def _unsafe_wp_config_sweeps(all_tasks) -> list[str]:
    unsafe = []
    install_root = str(DEFAULT_VALUES["wordpress_install_dir"])
    for filename, task, _ in all_tasks:
        for module in (
            "ansible.builtin.command",
            "ansible.builtin.shell",
            "ansible.builtin.raw",
            "ansible.builtin.script",
        ):
            command = _command_text(task, module)
            for statement in _command_statements(command):
                recursive_chmod = "chmod" in statement and re.search(
                    r"(?:^|\s)(?:--recursive|-\S*R\S*)(?:\s|$)", statement
                )
                reaches_tree = install_root in statement or re.search(
                    r"\{\{\s*wordpress_\w*(?:dir|path)\b", statement
                )
                find_chmod = "find " in statement and "chmod" in statement
                candidates = [statement]
                if find_chmod and "-type " in statement:
                    branch_source = re.sub(
                        r"(?:!|-not)\s+-type\s+([df])\b",
                        r"__negated_type_\1__",
                        statement,
                    )
                    candidates = re.split(r"(?=-type\s+[df]\b)", branch_source)
                for candidate in candidates:
                    candidate_changes_config = bool(re.search(
                        r"\binstall\b.*?\s-m\s+\S+.*wp-config\.php",
                        candidate,
                    ))
                    candidate_chmods_files = (
                        "chmod" in candidate and "-type d" not in candidate
                    )
                    touches_files = (
                        bool(recursive_chmod)
                        or candidate_chmods_files
                        or candidate_changes_config
                    )
                    excludes_config_family = re.search(
                        r"(?:!|-not)\s+-name\s+['\"]?wp-config\.php\*['\"]?",
                        candidate,
                    )
                    if touches_files and reaches_tree and not excludes_config_family:
                        unsafe.append(f"{filename}:{task.get('name')}")
                        break
    return unsafe


def _wp_config_backup_writers(all_tasks) -> list[str]:
    target = "{{wordpress_install_dir}}/wp-config.php"
    writers = []
    for filename, task, _ in all_tasks:
        for module, destination in WP_CONFIG_WRITERS.items():
            body = task.get(module)
            if (
                isinstance(body, dict)
                and isinstance(body.get(destination), str)
                and _normalise(body[destination]) == target
                and body.get("backup") is True
            ):
                writers.append(f"{filename}:{task.get('name')}")
    return writers


def test_wp_config_modes_are_always_private(security_tasks) -> None:
    modes = _wp_config_modes(security_tasks)
    assert modes, "no task protects wp-config.php"
    assert modes == {"0600"}, f"wp-config.php has unsafe mode writers: {sorted(modes)}"


def test_wp_config_has_no_in_place_backups(security_tasks) -> None:
    backup_writers = _wp_config_backup_writers(security_tasks)
    assert not backup_writers, (
        "wp-config.php backups expose secret-bearing copies in the document root: "
        f"{backup_writers}"
    )


def test_wp_config_is_excluded_from_permission_sweeps(security_tasks) -> None:
    unsafe_sweeps = _unsafe_wp_config_sweeps(security_tasks)
    assert not unsafe_sweeps, f"chmod sweeps include wp-config.php: {unsafe_sweeps}"


def test_wp_config_guard_detects_an_unsafe_template() -> None:
    tasks = _synthetic("""
- name: Unsafe config
  ansible.builtin.template:
    src: wp-config.php.j2
    dest: '{{ wordpress_install_dir }}/wp-config.php'
    mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


@pytest.mark.parametrize(
    "destination",
    ["/var/www/wordpress/wp-config.php", "{{ wordpress_path }}/wp-config.php"],
)
def test_wp_config_guard_detects_config_path_spellings(destination: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe alternate config path
  ansible.builtin.copy:
    content: test
    dest: '{destination}'
    mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


@pytest.mark.parametrize("module", ["ansible.builtin.get_url", "ansible.builtin.unarchive"])
def test_all_whole_file_modules_are_config_mode_writers(module: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe whole-file writer
  {module}:
    src: source
    dest: '{{{{ wordpress_install_dir }}}}/wp-config.php'
    mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_wp_config_writer_map_covers_file_mutation_modules() -> None:
    assert set(WHOLE_FILE) | set(PARTIAL) <= set(WP_CONFIG_WRITERS)


def test_wp_config_guard_rejects_a_mode_less_writer() -> None:
    tasks = _synthetic("""
- name: Mode-less config copy
  ansible.builtin.copy:
    content: test
    dest: '{{ wordpress_install_dir }}/wp-config.php'
""")
    assert _wp_config_modes(tasks) == {"MISSING"}


@pytest.mark.parametrize(
    "module_body",
    [
        "ansible.builtin.shell: chmod -R 0644 {{ wordpress_install_dir }}",
        "ansible.builtin.command: find {{ wordpress_install_dir }} -type f -exec chmod 0644 {} +",
        """ansible.builtin.command:
    argv: [chmod, -R, '0644', '{{ wordpress_install_dir }}']""",
        """ansible.builtin.command:
    cmd: chmod -R 0644 {{ wordpress_install_dir }}""",
        "ansible.builtin.raw: chmod -Rf 0644 {{ wordpress_install_dir }}",
        "ansible.builtin.shell: chmod --recursive 0644 {{ wordpress_install_dir }}",
        "ansible.builtin.command: chmod 0644 -R {{ wordpress_install_dir }}",
        "ansible.builtin.command: chmod -v -R 0644 {{ wordpress_install_dir }}",
        "ansible.builtin.command: find {{ wordpress_install_dir }} -exec chmod 0644 {} +",
        """ansible.builtin.shell: >-
    chmod -R 0644 {{ wordpress_install_dir }};
    echo 'wp-config.php*'""",
    ],
)
def test_wp_config_guard_detects_chmod_sweep_forms(module_body: str) -> None:
    tasks = _synthetic(f"""
- name: Protect config
  ansible.builtin.file:
    path: '{{{{ wordpress_install_dir }}}}/wp-config.php'
    mode: '0600'
- name: Unsafe sweep
  {module_body}
""")
    with pytest.raises(AssertionError, match="Unsafe sweep"):
        test_wp_config_is_excluded_from_permission_sweeps(tasks)


def test_wp_config_guard_detects_recursive_file_mode() -> None:
    tasks = _synthetic("""
- name: Unsafe recursive mode
  ansible.builtin.file:
    path: '{{ wordpress_install_dir }}'
    recurse: true
    mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_wp_config_guard_detects_loop_driven_recursive_mode() -> None:
    tasks = _synthetic("""
- name: Unsafe loop mode
  ansible.builtin.file:
    path: '{{ item.path }}'
    recurse: '{{ item.recurse | default(false) }}'
    mode: '{{ item.mode }}'
  loop:
    - path: '{{ wordpress_install_dir }}'
      recurse: true
      mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


@pytest.mark.parametrize(
    "item_path",
    [
        "{{ item }}",
        "{{ item.path }}",
        "{{ item.dest }}",
        "{{ wordpress_install_dir }}/{{ item }}",
        "{{ wordpress_install_dir }}/{{ item.path }}",
        "{{ wordpress_install_dir }}/{{ item | basename }}",
    ],
)
def test_wp_config_guard_fails_closed_on_dynamic_mode_loop(item_path: str) -> None:
    tasks = _synthetic(f"""
- name: Runtime-discovered mode writer
  ansible.builtin.file:
    path: '{item_path}'
    mode: '0644'
  loop: '{{ discovered.files }}'
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_dynamic_mode_loop_scoped_below_config_is_safe() -> None:
    tasks = _synthetic("""
- name: Discover uploads
  ansible.builtin.find:
    paths: '{{ wordpress_install_dir }}/wp-content/uploads'
    file_type: file
  register: upload_files
- name: Protect uploads
  ansible.builtin.file:
    path: '{{ item.path }}'
    mode: '0644'
  loop: '{{ upload_files.files }}'
""")
    assert _wp_config_modes(tasks) == set()


def test_dynamic_find_scope_cannot_traverse_to_config() -> None:
    tasks = _synthetic("""
- name: Unsafe discovery scope
  ansible.builtin.find:
    paths: '{{ wordpress_install_dir }}/wp-content/..'
    file_type: file
  register: discovered
- name: Unsafe discovered writer
  ansible.builtin.file:
    path: '{{ item.path }}'
    mode: '0644'
  loop: '{{ discovered.files }}'
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_handler_config_writer_is_in_the_mode_corpus() -> None:
    handlers = [
        ("handlers/main.yml", task, when)
        for _, task, when in _synthetic("""
- name: Unsafe handler mode
  ansible.builtin.file:
    path: '{{ wordpress_install_dir }}/wp-config.php'
    mode: '0644'
""")
    ]
    assert _wp_config_modes(handlers) == {"0644"}


def test_handler_config_backup_is_in_the_backup_corpus() -> None:
    handlers = [
        ("handlers/main.yml", task, when)
        for _, task, when in _synthetic("""
- name: Unsafe handler backup
  ansible.builtin.copy:
    dest: '{{ wordpress_install_dir }}/wp-config.php'
    content: test
    backup: true
""")
    ]
    assert _wp_config_backup_writers(handlers) == [
        "handlers/main.yml:Unsafe handler backup"
    ]


@pytest.mark.parametrize("path", ["/var/www/wordpress", "/var/www"])
def test_wp_config_guard_detects_literal_recursive_ancestor(path: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe literal recursive mode
  ansible.builtin.file:
    path: {path}
    recurse: true
    mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


@pytest.mark.parametrize("module", ["lineinfile", "blockinfile", "replace"])
def test_wp_config_guard_detects_unsafe_partial_writer_mode(module: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe partial writer
  ansible.builtin.{module}:
    path: '{{{{ wordpress_install_dir }}}}/wp-config.php'
    mode: '0644'
""")
    assert _wp_config_modes(tasks) == {"0644"}


@pytest.mark.parametrize(
    ("module", "destination"),
    [
        ("ansible.builtin.blockinfile", "path"),
        ("ansible.builtin.copy", "dest"),
        ("community.general.ini_file", "path"),
    ],
)
def test_wp_config_guard_rejects_in_place_backups(module: str, destination: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe backup
  {module}:
    {destination}: '{{{{ wordpress_install_dir }}}}/wp-config.php'
    block: test
    backup: true
""")
    assert _wp_config_backup_writers(tasks) == ["synthetic.yml:Unsafe backup"]


@pytest.mark.parametrize("target", ["{{ wordpress_path }}", "/var/www/wordpress"])
def test_wp_config_guard_detects_sweep_target_aliases(target: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe alternate target
  ansible.builtin.command: find {target} -type f -exec chmod 0644 {{}} +
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Unsafe alternate target"]


def test_exact_name_exclusion_does_not_cover_wp_config_backups() -> None:
    tasks = _synthetic("""
- name: Incomplete exclusion
  ansible.builtin.command: >-
    find {{ wordpress_install_dir }} -type f ! -name wp-config.php
    -exec chmod 0644 {} +
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Incomplete exclusion"]


def test_positive_name_filter_is_not_mistaken_for_an_exclusion() -> None:
    tasks = _synthetic("""
- name: Positive config match
  ansible.builtin.command: >-
    find /var/www/wordpress -type f -name 'wp-config.php*'
    -exec chmod 0666 {} +
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Positive config match"]


def test_combined_find_branches_still_check_the_file_branch() -> None:
    tasks = _synthetic("""
- name: Combined unsafe sweep
  ansible.builtin.command:
    cmd: >-
      find {{ wordpress_install_dir }}
      ( -type d -exec chmod 0755 {} + )
      -o ( -type f -exec chmod 0644 {} + )
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Combined unsafe sweep"]


@pytest.mark.parametrize(
    "command",
    [
        "chmod 0644 {{ wordpress_install_dir }}/wp-config.php",
        "install -m 0644 source {{ wordpress_install_dir }}/wp-config.php",
    ],
)
def test_wp_config_guard_detects_direct_command_modes(command: str) -> None:
    tasks = _synthetic(f"""
- name: Unsafe direct mode
  ansible.builtin.command: {command}
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_wp_config_guard_resolves_direct_command_mode_variable() -> None:
    tasks = _synthetic("""
- name: Variable direct mode
  ansible.builtin.command: >-
    chmod {{ wordpress_file_permissions }}
    {{ wordpress_install_dir }}/wp-config.php
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_exclusion_on_one_shell_line_does_not_exempt_another() -> None:
    tasks = _synthetic("""
- name: Multiline unsafe sweep
  ansible.builtin.shell: |
    find {{ wordpress_install_dir }} -type f ! -name 'wp-config.php*' -exec chmod 0644 {} +
    chmod -R 0666 {{ wordpress_install_dir }}
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Multiline unsafe sweep"]


def test_exclusion_on_one_line_does_not_hide_direct_mode_writer() -> None:
    tasks = _synthetic("""
- name: Multiline direct writer
  ansible.builtin.shell: |
    find {{ wordpress_install_dir }} -type f ! -name 'wp-config.php*' -exec chmod 0644 {} +
    install -m 0644 source {{ wordpress_install_dir }}/wp-config.php
""")
    assert _wp_config_modes(tasks) == {"0644"}


def test_directory_branch_exclusion_does_not_exempt_file_branch() -> None:
    tasks = _synthetic("""
- name: Wrong-branch exclusion
  ansible.builtin.command: >-
    find {{ wordpress_install_dir }}
    ( -type d ! -name 'wp-config.php*' -exec chmod 0755 {} + )
    -o ( -type f -exec chmod 0644 {} + )
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Wrong-branch exclusion"]


@pytest.mark.parametrize("negation", ["!", "-not"])
def test_negated_directory_type_is_treated_as_a_file_sweep(negation: str) -> None:
    tasks = _synthetic(f"""
- name: Negated directory sweep
  ansible.builtin.command: >-
    find {{{{ wordpress_install_dir }}}} {negation} -type d
    -exec chmod 0666 {{}} +
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Negated directory sweep"]


def test_install_mode_writer_is_part_of_the_sweep_guard() -> None:
    tasks = _synthetic("""
- name: Unsafe install mode
  ansible.builtin.command: >-
    install -m 0644 source {{ wordpress_install_dir }}/wp-config.php
""")
    assert _unsafe_wp_config_sweeps(tasks) == ["synthetic.yml:Unsafe install mode"]


def test_written_destinations_are_owned_by_one_task(all_tasks) -> None:
    owners = _destinations(all_tasks)
    clash = {}
    for target, writers in owners.items():
        if len(writers) < 2:
            continue
        files = {f for _, f, _ in writers}
        if len(writers) == len(files) and any(files == pair for pair in EXCLUSIVE_FILES):
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
    recorded = 56
    assert len(baseline) == recorded, (
        f"the baseline changed to {len(baseline)} from {recorded}; update the "
        "ratchet deliberately when missing templates are added or supplied"
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

def test_every_affected_file_is_classified(baseline) -> None:
    """Nothing may fall out of the coverage check by being absent from a map."""
    affected = {entry.split(":", 1)[0] for entry in baseline}
    unclassified = sorted(affected - set(FEATURE_FLAG))
    assert not unclassified, (
        "these files reference missing templates but are not feature-gated: "
        f"{unclassified}"
    )
    stale = sorted(set(FEATURE_FLAG) - affected)
    assert not stale, f"feature files no longer fail closed; remove their guards: {stale}"


def test_fail_closed_file_attribute_exclusions_are_explicit() -> None:
    skipped = {path.name for path in TASKS if _starts_with_unconditional_failure(path.name)}
    assert skipped == set(FEATURE_FLAG), (
        "file-attribute writers are skipped only in reviewed fail-closed features: "
        f"{sorted(skipped)}"
    )


def test_files_with_missing_templates_fail_before_changing_anything(baseline) -> None:
    """A feature that cannot finish must stop first, not halfway."""
    affected = {entry.split(":", 1)[0] for entry in baseline}
    unguarded = []
    for filename in sorted(affected & set(FEATURE_FLAG)):
        tasks = yaml.safe_load((ROOT / "tasks" / filename).read_text()) or []
        first = tasks[0] if tasks else {}
        if (
            "ansible.builtin.fail" not in first
            or "when" in first
            or first.get("ignore_errors")
        ):
            unguarded.append(filename)
    assert not unguarded, (
        "these files reference templates the role does not ship and would abort "
        f"partway through; give them a leading ansible.builtin.fail: {unguarded}"
    )


def test_feature_guards_match_the_main_task_includes() -> None:
    main = yaml.safe_load((ROOT / "tasks" / "main.yml").read_text()) or []
    includes = {}
    for task in main:
        include = task.get("ansible.builtin.include_tasks")
        if not include:
            continue
        filename = include.get("file") if isinstance(include, dict) else include
        includes[filename] = task.get("when")
    drift = {
        filename: flag
        for filename, flag in FEATURE_FLAG.items()
        if flag not in str(includes.get(filename, ""))
    }
    assert not drift, f"feature guards do not match main.yml includes: {drift}"


def _enabled_incomplete_features(node) -> set[str]:
    enabled = set()
    if isinstance(node, list):
        for item in node:
            enabled |= _enabled_incomplete_features(item)
    elif isinstance(node, dict):
        for key, value in node.items():
            if key in FEATURE_FLAG.values() and (
                value is True
                or isinstance(value, str)
                and value.strip().lower() in {"true", "yes", "on", "1"}
            ):
                enabled.add(key)
            enabled |= _enabled_incomplete_features(value)
    return enabled


def test_examples_and_scenarios_do_not_enable_incomplete_features() -> None:
    paths = sorted((ROOT / "examples").rglob("*.yml"))
    paths += sorted((ROOT / "tests" / "scenarios").rglob("*.yml"))
    paths += sorted((ROOT / "molecule").glob("*/converge.yml"))
    enabled = {
        str(path.relative_to(ROOT)): sorted(
            _enabled_incomplete_features(yaml.safe_load(path.read_text()) or [])
        )
        for path in paths
        if _enabled_incomplete_features(yaml.safe_load(path.read_text()) or [])
    }
    assert not enabled, f"incomplete features enabled in shipped playbooks: {enabled}"


@pytest.mark.parametrize("truthy", [True, "true", "True", "yes", "on"])
def test_incomplete_feature_gate_understands_yaml_truthiness(truthy) -> None:
    assert _enabled_incomplete_features({"vars": {"wordpress_enable_backups": truthy}}) == {
        "wordpress_enable_backups"
    }


def test_partial_edit_anchors_do_not_hide_a_clash() -> None:
    line_tasks = _synthetic("""
- name: First line
  ansible.builtin.lineinfile: {path: /x, regexp: '^same', insertafter: '^one', line: same=1}
- name: Second line
  ansible.builtin.lineinfile: {path: /x, regexp: '^same', insertafter: '^two', line: same=2}
""")
    block_tasks = _synthetic("""
- name: First block
  ansible.builtin.blockinfile: {path: /y, insertbefore: '^one', block: one}
- name: Second block
  ansible.builtin.blockinfile: {path: /y, insertbefore: '^two', block: two}
""")
    with pytest.raises(AssertionError, match="synthetic.yml"):
        test_written_destinations_are_owned_by_one_task(line_tasks)
    with pytest.raises(AssertionError, match="synthetic.yml"):
        test_written_destinations_are_owned_by_one_task(block_tasks)


def test_dynamic_file_loop_is_recorded() -> None:
    tasks = _synthetic("""
- name: Dynamic files
  ansible.builtin.file:
    path: '{{ item.path }}'
    mode: '0644'
  loop: '{{ discovered.files }}'
""")
    writers = _file_attribute_writers(tasks)
    assert ("{{item.path}}", "mode") in writers


def test_whole_partial_allowlist_has_no_stale_entries(all_tasks) -> None:
    whole = collections.Counter()
    partial = collections.Counter()
    for _, task, _ in all_tasks:
        for module, key in WHOLE_FILE.items():
            body = task.get(module)
            if isinstance(body, dict) and isinstance(body.get(key), str):
                whole[_normalise(body[key])] += 1
        for module, (key, _) in PARTIAL.items():
            body = task.get(module)
            if isinstance(body, dict) and isinstance(body.get(key), str):
                partial[_normalise(body[key])] += 1
    stale = sorted(
        target
        for target in WHOLE_PARTIAL_ALLOWED
        if not whole[target] or not partial[target]
    )
    assert not stale, f"stale whole/partial ownership exemptions: {stale}"


def test_conflicting_file_modes_are_reported() -> None:
    tasks = _synthetic("""
- name: Loose
  ansible.builtin.file: {path: /secret, mode: '0644'}
- name: Strict
  ansible.builtin.file: {path: /secret, mode: '0600'}
""")
    with pytest.raises(AssertionError, match="/secret:mode"):
        test_file_attributes_do_not_conflict(tasks)


def test_compatible_file_attributes_are_allowed() -> None:
    tasks = _synthetic("""
- name: Own directory
  ansible.builtin.file: {path: /data, owner: app}
- name: Create directory
  ansible.builtin.file: {path: /data, state: directory}
- name: Confirm owner
  ansible.builtin.file: {path: /data, owner: app}
""")
    test_file_attributes_do_not_conflict(tasks)


def test_two_not_equal_conditions_are_not_exclusive() -> None:
    """x != 'a' and x != 'b' are both true for x == 'c'."""
    assert not _exclusive([("web != 'nginx'",), ("web != 'apache'",)])


def test_complementary_conditions_are_exclusive() -> None:
    assert _exclusive([("web == 'nginx'",), ("web != 'nginx'",)])
    assert _exclusive([("web == 'nginx'",), ("web == 'apache'",)])
    assert not _exclusive([("web == 'nginx'",), ("web == 'nginx'",)])


def test_writers_constrained_on_different_variables_are_not_exclusive() -> None:
    assert not _exclusive([("a == 'x'",), ("b == 'y'",)])


def test_filtered_conditions_are_not_assumed_exclusive() -> None:
    assert not _exclusive([("x | lower == 'a'",), ("x == 'A'",)])
    assert not _exclusive([
        ("x | default('a') == 'a'",),
        ("x | default('b') == 'b'",),
    ])


def test_file_pair_exemption_does_not_hide_an_intra_file_clash() -> None:
    tasks = [
        ("webserver_nginx.yml", {"name": "One", "ansible.builtin.copy": {"dest": "/x"}}, ()),
        ("webserver_nginx.yml", {"name": "Two", "ansible.builtin.copy": {"dest": "/x"}}, ()),
        ("webserver_apache.yml", {"name": "Three", "ansible.builtin.copy": {"dest": "/x"}}, ()),
    ]
    with pytest.raises(AssertionError, match="/x"):
        test_written_destinations_are_owned_by_one_task(tasks)


def test_whole_file_and_partial_writers_clash() -> None:
    tasks = _synthetic("""
- name: Whole
  ansible.builtin.template: {src: a.j2, dest: /etc/thing.conf}
- name: Partial
  ansible.builtin.lineinfile: {path: /etc/thing.conf, regexp: '^x', line: 'x=1'}
""")
    with pytest.raises(AssertionError, match="/etc/thing.conf"):
        test_written_destinations_are_owned_by_one_task(tasks)


def test_overlapping_loop_driven_partial_writers_clash() -> None:
    tasks = _synthetic("""
- name: First
  ansible.builtin.lineinfile:
    path: /etc/thing.conf
    regexp: '^{{ item.key }}='
    line: '{{ item.key }}={{ item.value }}'
  loop:
    - {key: shared, value: one}
    - {key: first, value: one}
- name: Second
  ansible.builtin.lineinfile:
    path: /etc/thing.conf
    regexp: '^{{ item.key }}='
    line: '{{ item.key }}={{ item.value }}'
  loop:
    - {value: two, key: shared}
    - {value: two, key: second}
""")
    with pytest.raises(AssertionError, match="shared"):
        test_written_destinations_are_owned_by_one_task(tasks)


def test_cron_guard_reports_duplicate_names() -> None:
    tasks = _synthetic("""
- name: First
  ansible.builtin.cron: {name: duplicate, job: /bin/true}
- name: Second
  ansible.builtin.cron: {name: duplicate, job: /bin/false}
""")
    with pytest.raises(AssertionError, match="duplicate"):
        test_cron_entry_names_are_owned_by_one_task(tasks)


def test_nonrecursive_directory_loops_cannot_chmod_wp_config() -> None:
    tasks = _synthetic("""
- name: Create a missing directory
  ansible.builtin.file:
    path: '{{ item.directory }}'
    state: directory
    mode: '0700'
  loop: '{{ directory_results }}'
""")
    assert _wp_config_modes(tasks) == set()
    tasks[0][1]["ansible.builtin.file"]["recurse"] = True
    assert _wp_config_modes(tasks) == {"0700"}
