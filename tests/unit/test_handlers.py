"""Every notify names a handler that exists.

Ansible fails a play on an unknown handler only at runtime, and a handler that
no task notifies is dead weight. Both drift silently, so pin them here.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
HANDLERS = ROOT / "handlers" / "main.yml"
VALIDATE = ROOT / "tasks" / "validate.yml"
TASK_DIRS = ("tasks", "handlers")


def _choices() -> dict[str, list[str]]:
    """The values tasks/validate.yml admits, so notify templates can expand."""
    pattern = re.compile(r"- (\w+) in \[([^\]]+)\]")
    return {
        name: re.findall(r"'([^']+)'", values)
        for name, values in pattern.findall(VALIDATE.read_text())
    }


def _expand(name: str) -> set[str]:
    """A notify may name a handler through a variable; cover every value."""
    match = re.fullmatch(r"(.*)\{\{\s*(\w+)\s*\}\}(.*)", name)
    if not match:
        return {name}
    head, variable, tail = match.groups()
    values = _choices().get(variable)
    if not values:
        raise AssertionError(f"notify {name!r} uses {variable}, which validate.yml does not constrain")
    return {f"{head}{value}{tail}" for value in values}


def _tasks(node):
    """Walk every task, including the ones nested in block/rescue/always."""
    if isinstance(node, list):
        for item in node:
            yield from _tasks(item)
    elif isinstance(node, dict):
        yield node
        for key in ("block", "rescue", "always"):
            if key in node:
                yield from _tasks(node[key])


def _notified() -> set[str]:
    names = set()
    for directory in TASK_DIRS:
        for path in sorted((ROOT / directory).glob("*.yml")):
            for task in _tasks(yaml.safe_load(path.read_text()) or []):
                notify = task.get("notify")
                if isinstance(notify, str):
                    notify = [notify]
                for entry in notify or []:
                    if isinstance(entry, str):
                        names |= _expand(entry)
    return names


@pytest.fixture(scope="module")
def handler_names() -> set[str]:
    return {h["name"] for h in yaml.safe_load(HANDLERS.read_text()) if "name" in h}


def test_the_corpus_is_not_empty(handler_names: set[str]) -> None:
    """A moved directory must fail loudly, not pass on zero inputs."""
    assert handler_names, "no handlers parsed; the layout changed"
    assert _notified(), "no notify targets found; the layout changed"


def test_every_notify_resolves_to_a_handler(handler_names: set[str]) -> None:
    missing = sorted(_notified() - handler_names)
    assert not missing, f"notify targets with no handler: {missing}"


# Handler names are part of the published interface, so a handler no task here
# notifies is not necessarily unused. These are kept for downstream playbooks;
# removing one is a breaking change and needs a major version in meta/main.yml.
PUBLIC = {
    # Every handler name main already publishes. A downstream playbook may
    # notify any of them, so this repo having no notify for one is not
    # evidence it is unused. Removing one is a breaking change.
    "Reload apache", "Reload firewalld", "Reload nginx", "Reload apparmor",
    "Reload systemd", "Restart apache", "Restart auditd", "Restart fail2ban",
    "Restart mariadb", "Restart memcached", "Restart mysql", "Restart nginx",
    "Restart php-fpm", "Restart redis", "Restart sshd", "Restart yum-cron",
    "Reboot system", "Reload sysctl",
}


def test_no_handler_is_orphaned(handler_names: set[str]) -> None:
    orphans = sorted(handler_names - _notified() - PUBLIC)
    assert not orphans, (
        f"handlers nothing notifies and that are not part of the public "
        f"interface: {orphans}"
    )


# Dropped deliberately. Both name a PHP version rather than reading
# wordpress_php_fpm_service, so they only ever worked on a host running that
# exact stream; "Restart php-fpm" supersedes both. Removing a published name is
# a breaking change, recorded here so it is a decision and not an accident.
REMOVED = {"Restart php8.1-fpm", "Restart php8.2-fpm"}


def test_removed_handlers_are_recorded_not_forgotten(handler_names: set[str]) -> None:
    assert not (REMOVED & handler_names), (
        f"these are listed as removed but still defined: {sorted(REMOVED & handler_names)}"
    )
    assert not (REMOVED & PUBLIC), "a name cannot be both published and removed"


def test_the_public_handlers_all_exist(handler_names: set[str]) -> None:
    missing = sorted(PUBLIC - handler_names)
    assert not missing, (
        f"removing a published handler is a breaking change; restore it or bump "
        f"the major version in meta/main.yml: {missing}"
    )


def test_handlers_live_only_where_ansible_loads_them() -> None:
    """A role auto-loads handlers/main.yml and nothing else.

    A second file under handlers/ looks like it defines handlers and does not:
    every name in it is silently unreachable, which is how a duplicate of a
    live handler can sit in the tree looking authoritative.
    """
    stray = sorted(
        p.name for p in (ROOT / "handlers").glob("*.yml") if p.name != "main.yml"
    )
    assert not stray, (
        "these handler files are never loaded, so everything in them is "
        f"ignored: {stray}"
    )


def test_handler_names_are_unique() -> None:
    names = [h["name"] for h in yaml.safe_load(HANDLERS.read_text()) if "name" in h]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    assert not duplicates, f"duplicate handler names: {duplicates}"
