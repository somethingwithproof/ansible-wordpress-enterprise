# SPDX-FileCopyrightText: 2025 Thomas Vincent
# SPDX-License-Identifier: MIT
"""Best-effort commands must remain observable without breaking idempotence."""

from __future__ import annotations

import pathlib

import yaml
from jinja2 import Environment

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _named_tasks(path: pathlib.Path) -> dict[str, dict]:
    return {
        task["name"]: task
        for task in yaml.safe_load(path.read_text()) or []
        if isinstance(task, dict) and "name" in task
    }


def _evaluate(condition: str | list[str], **variables) -> bool:
    conditions = condition if isinstance(condition, list) else [condition]
    environment = Environment()
    return all(
        bool(environment.compile_expression(expression)(**variables))
        for expression in conditions
    )


def test_failed_cache_flush_dispatches_its_reporter() -> None:
    tasks = _named_tasks(ROOT / "handlers" / "main.yml")
    flush = tasks["Run wp-cli cache flush"]
    report = tasks["Report a failed wp-cli cache flush"]

    assert flush["failed_when"] is False
    assert _evaluate(flush["changed_when"], wordpress_cache_flush={"rc": 1})
    assert _evaluate(flush["changed_when"], wordpress_cache_flush={})
    assert not _evaluate(flush["changed_when"], wordpress_cache_flush={"rc": 0})
    assert flush["notify"] == "Report a failed wp-cli cache flush"
    assert _evaluate(report["when"], wordpress_cache_flush={"rc": 1})
    assert _evaluate(report["when"], wordpress_cache_flush={})
    assert not _evaluate(report["when"], wordpress_cache_flush={"rc": 0})


def test_wpcli_best_effort_failures_have_reachable_reports() -> None:
    tasks = _named_tasks(ROOT / "tasks" / "wpcli.yml")
    completion = tasks["Report a missing WP-CLI bash completion"]["when"]
    core = tasks["Report an unavailable WordPress installation to WP-CLI"]["when"]

    assert _evaluate(completion, wordpress_wpcli_completion={"status_code": 500})
    assert _evaluate(completion, wordpress_wpcli_completion={})
    assert not _evaluate(completion, wordpress_wpcli_completion={"status_code": 200})
    assert not _evaluate(completion, wordpress_wpcli_completion={"status_code": 304})
    assert not _evaluate(completion, wordpress_wpcli_completion={"skipped": True})
    assert _evaluate(core, wp_core_test={"rc": 1})
    assert _evaluate(core, wp_core_test={})
    assert not _evaluate(core, wp_core_test={"rc": 0})
    assert not _evaluate(core, wp_core_test={"skipped": True})
