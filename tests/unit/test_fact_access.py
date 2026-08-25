"""Facts are read through ansible_facts, not the injected bare variables.

ansible-core deprecates the injected ansible_<fact> variables, and they are
absent entirely when inject_facts_as_vars is off. Connection and inventory
variables such as ansible_host are not facts and stay as they are.
"""

from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SEARCH_DIRS = ("tasks", "templates", "handlers", "defaults", "vars", "molecule", "tests")

# setup module facts, which belong under ansible_facts
FACTS = {
    "architecture", "date_time", "default_ipv4", "distribution",
    "distribution_major_version", "distribution_release", "distribution_version",
    "domain", "fqdn", "hostname", "kernel", "memtotal_mb", "mounts",
    "os_family", "processor_vcpus", "selinux",
}

# connection and inventory settings, which do not
NOT_FACTS = {
    "become", "become_method", "become_pass", "become_user", "check_mode",
    "connection", "facts", "host", "loop_var", "managed", "password", "port",
    "python_interpreter", "shell_executable", "ssh_common_args",
    "ssh_extra_args", "ssh_private_key_file", "user", "version",
}

PATTERN = re.compile(r"\bansible_([a-z0-9_]+)")


def _files():
    for directory in SEARCH_DIRS:
        base = ROOT / directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.suffix in {".yml", ".yaml", ".j2", ".cfg"}:
                yield path


@pytest.fixture(scope="module")
def offenders() -> list[str]:
    found = []
    for path in _files():
        for number, line in enumerate(path.read_text(errors="ignore").splitlines(), 1):
            for name in PATTERN.findall(line):
                # Fail closed: anything not known to be a connection setting is
                # treated as a fact and has to be classified deliberately.
                if name not in NOT_FACTS:
                    found.append(f"{path.relative_to(ROOT)}:{number}: ansible_{name}")
    return found


def test_the_corpus_is_not_empty() -> None:
    """A moved directory must fail loudly, not pass on zero inputs."""
    assert len(list(_files())) > 50, "too few files scanned; the layout changed"


def test_the_scanner_detects_an_unlisted_fact(tmp_path) -> None:
    """A fact outside FACTS must still be caught."""
    assert "system" not in NOT_FACTS
    assert PATTERN.findall("when: ansible_system == 'Linux'") == ["system"]


def test_no_bare_fact_variables(offenders: list[str]) -> None:
    assert not offenders, (
        f"{len(offenders)} bare fact references; use ansible_facts['<name>'] instead:\n"
        + "\n".join(offenders[:15])
    )


def test_fact_and_connection_sets_do_not_overlap() -> None:
    assert not (FACTS & NOT_FACTS)
