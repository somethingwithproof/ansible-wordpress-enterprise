"""Generated credentials survive between runs.

A password lookup pointed at /dev/null generates a new value every time it is
evaluated. The role resets the database user from that value on every run but
only writes wp-config.php on the first, so a second run rotates the database
password out from under the site.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
DEFAULTS = ROOT / "defaults" / "main.yml"
SEARCH_DIRS = ("defaults", "vars", "tasks", "handlers", "templates")

# Ansible spells this several ways: lookup() and query(), either quote style,
# and with or without spaces. Matching one form would let a regression back in
# under another.
LOOKUP_START = re.compile(
    r"\b(?:lookup|query|q)\s*\(\s*['\"]password['\"]\s*,"
)


def _lookups(text: str):
    """Yield each password lookup argument, respecting nested parentheses.

    A regex stopping at the first ")" truncates
    lookup('password', (store | default('/x')) ~ '/db'), which would hide a
    /dev/null hiding inside.
    """
    for match in LOOKUP_START.finditer(text):
        depth, start = 1, match.end()
        for index in range(start, len(text)):
            char = text[index]
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    yield match.start(), text[start:index].strip()
                    break


@pytest.fixture(scope="module")
def defaults() -> dict:
    return yaml.safe_load(DEFAULTS.read_text())


def _walk(node, path=""):
    """Every scalar in a document, keyed by the path that reaches it."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield from _walk(value, f"{path}.{key}" if path else str(key))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _walk(value, f"{path}[{index}]")
    elif isinstance(node, str):
        yield path, node


def _generated(defaults: dict) -> dict[str, str]:
    """Every password lookup anywhere in the role, not just top-level defaults."""
    found = {}
    for directory in SEARCH_DIRS:
        base = ROOT / directory
        if not base.is_dir():
            continue
        for file in sorted(base.rglob("*")):
            if not file.is_file():
                continue
            if file.suffix in {".yml", ".yaml"}:
                document = yaml.safe_load(file.read_text(encoding="utf-8"))
                pairs = _walk(document)
            else:
                pairs = ((f"{file.name}", file.read_text(encoding="utf-8")),)
            for key, value in pairs:
                for offset, argument in _lookups(value):
                    # The offset keeps several lookups in one file distinct;
                    # without it they collapse to the last one found.
                    found[f"{file.relative_to(ROOT)}:{key}@{offset}"] = argument
    return found


def test_the_role_generates_some_credentials(defaults: dict) -> None:
    """Guard the guard: if the lookups move, this file has to be revisited."""
    assert _generated(defaults), (
        f"no password lookups found under {list(SEARCH_DIRS)}; "
        "if the lookups moved, this file has to be revisited"
    )


def test_no_generated_credential_is_discarded(defaults: dict) -> None:
    """/dev/null means the value is never stored, so every run makes a new one."""
    ephemeral = sorted(
        name for name, expr in _generated(defaults).items() if "/dev/null" in expr
    )
    assert not ephemeral, (
        "these credentials are regenerated on every run, so a second run "
        f"invalidates the ones already written to the host: {ephemeral}"
    )


class _Missing:
    """Stands in for Jinja's Undefined so mandatory() can reject it."""


def _environment(home: str = "/home/tester"):
    """A Jinja environment that speaks enough Ansible to render these defaults."""
    from jinja2 import Environment

    def mandatory(value, msg="mandatory variable not defined"):
        if isinstance(value, _Missing):
            raise ValueError(msg)
        return value

    def default(value, fallback="", boolean=False):
        if isinstance(value, _Missing):
            return fallback
        return fallback if boolean and not value else value

    env = Environment()
    env.filters["mandatory"] = mandatory
    env.filters["default"] = default
    env.globals["undef"] = lambda *a, **k: _Missing()
    env.globals["lookup"] = lambda kind, *a, **k: home if kind == "env" else ""
    return env


def _render(expr: str, defaults: dict, hostname: str, home: str = "/home/tester") -> str:
    """Render a lookup argument for one host, so the property can be tested."""
    env = _environment(home)
    store = env.from_string(
        "{{ " + _strip(defaults["wordpress_credential_store"]) + " }}"
    ).render(inventory_hostname=hostname)
    return env.from_string("{{ " + _strip(expr) + " }}").render(
        inventory_hostname=hostname, wordpress_credential_store=store
    )


def _strip(text: str) -> str:
    """Take the expression out of its {{ }} wrapper if it has one."""
    text = " ".join(text.split())
    match = re.fullmatch(r"\{\{(.*)\}\}", text)
    return match.group(1).strip() if match else text


def test_generated_credentials_are_stored_per_host(defaults: dict) -> None:
    """Two hosts must not resolve to one file; test the property, not a spelling."""
    shared = []
    for name, expr in _generated(defaults).items():
        try:
            a = _render(expr, defaults, "hostA")
            b = _render(expr, defaults, "hostB")
        except Exception as error:  # noqa: BLE001 - surfaced as a failure below
            shared.append(f"{name} (cannot render: {error})")
            continue
        if a == b:
            shared.append(f"{name} -> {a}")
    assert not shared, (
        f"these credential paths do not vary by host, so hosts would share a "
        f"password: {shared}"
    )


UNSAFE_HOMES = ("/tmp", "/var/tmp", "/dev/shm")


def test_the_credential_store_is_not_a_shared_temporary_directory(
    defaults: dict,
) -> None:
    """A world-writable home for secrets is worse than no persistence at all.

    Checked on the rendered path, not on how the expression is spelled, so a
    plain literal is caught as readily as a default() fallback.
    """
    # Every credential path, not just the variable they happen to share: one
    # could name a temporary directory directly.
    paths = {"wordpress_credential_store": defaults["wordpress_credential_store"]}
    paths.update(_generated(defaults))

    offenders = []
    for name, expr in paths.items():
        rendered = _render(expr, defaults, "hostA")
        if any(rendered.startswith(unsafe + "/") for unsafe in UNSAFE_HOMES):
            offenders.append(f"{name} -> {rendered}")
        elif rendered.startswith("/.") or rendered.count("/") <= 2:
            offenders.append(f"{name} -> {rendered} (next to the filesystem root)")
    assert not offenders, (
        f"credentials would be written somewhere other users can reach: {offenders}"
    )


def test_each_credential_has_its_own_file(defaults: dict) -> None:
    """Two credentials sharing a file would be the same secret."""
    import collections
    import re as _re

    files = collections.defaultdict(list)
    for name, expr in _generated(defaults).items():
        match = _re.search(r"~\s*'/([^ ']+)", expr)
        assert match, f"cannot read a filename out of {name}: {expr}"
        files[match.group(1)].append(name)
    clash = {f: sorted(n) for f, n in files.items() if len(n) > 1}
    assert not clash, f"credentials sharing one file: {clash}"


def test_an_unset_home_is_rejected_rather_than_silently_relocated(
    defaults: dict,
) -> None:
    """The store must refuse to resolve rather than land at the filesystem root."""
    with pytest.raises(ValueError, match="HOME"):
        _render(
            defaults["wordpress_credential_store"], defaults, "hostA", home=""
        )


def test_the_guard_catches_a_reintroduced_ephemeral_lookup(tmp_path) -> None:
    """Prove the scanner fires: the regression it guards must be detectable."""
    sample = tmp_path / "defaults.yml"
    sample.write_text(
        "good: \"{{ lookup('password', store ~ '/a length=8') }}\"\n"
        "bad: \"{{ lookup('password', '/dev/null length=8') }}\"\n"
    )
    found = dict(
        (key, value)
        for key, value in
        ((f"{sample.name}@{offset}", argument)
         for offset, argument in _lookups(sample.read_text()))
    )
    assert len(found) == 2, f"both lookups must be seen distinctly: {found}"
    assert any("/dev/null" in argument for argument in found.values())


def test_the_scanner_survives_nested_parentheses() -> None:
    """A regex stopping at the first ')' would truncate the /dev/null away."""
    text = "{{ lookup('password', (store | default('/x')) ~ '/dev/null/db') }}"
    arguments = [argument for _, argument in _lookups(text)]
    assert arguments == ["(store | default('/x')) ~ '/dev/null/db'"]
