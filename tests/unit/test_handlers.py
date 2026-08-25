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
PUBLIC = {"Restart nginx", "Restart apache", "Restart php-fpm", "Restart mysql",
          "Restart mariadb", "Restart redis", "Restart memcached", "Reload systemd"}


def test_no_handler_is_orphaned(handler_names: set[str]) -> None:
    orphans = sorted(handler_names - _notified() - PUBLIC)
    assert not orphans, (
        f"handlers nothing notifies and that are not part of the public "
        f"interface: {orphans}"
    )


def test_the_public_handlers_all_exist(handler_names: set[str]) -> None:
    missing = sorted(PUBLIC - handler_names)
    assert not missing, (
        f"removing a published handler is a breaking change; restore it or bump "
        f"the major version in meta/main.yml: {missing}"
    )


def test_handler_names_are_unique() -> None:
    names = [h["name"] for h in yaml.safe_load(HANDLERS.read_text()) if "name" in h]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    assert not duplicates, f"duplicate handler names: {duplicates}"
