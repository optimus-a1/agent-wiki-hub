#!/usr/bin/env python3
"""Audit GitHub Actions workflow expectations for Agent Wiki Hub."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "wiki-acceptance.yml"
DOCS_OUT = ROOT / "docs" / "CI_AUDIT.md"
JSON_OUT = ROOT / "registry" / "ci-audit.json"

REQUIRED_SNIPPETS = {
    "trigger:pull_request": "pull_request:",
    "trigger:workflow_dispatch": "workflow_dispatch:",
    "permissions:contents_read": "contents: read",
    "checkout": "actions/checkout@",
    "setup_python": "actions/setup-python@",
    "run_acceptance": "python scripts/run_acceptance.py",
}
FORBIDDEN_PATTERNS = {
    "no_github_secrets": r"\bsecrets\.",
    "no_api_key_literals": r"(?i)(api[_-]?key|private[_-]?key|access[_-]?token|cookie)\s*[:=]",
    "no_write_permissions": r"contents:\s*write",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def add_check(checks: list[dict], check_id: str, passed: bool, evidence: str) -> None:
    checks.append({"check_id": check_id, "passed": passed, "evidence": evidence})


def audit() -> list[dict]:
    checks: list[dict] = []
    text = read_text(WORKFLOW)
    add_check(checks, "workflow_exists", WORKFLOW.exists(), WORKFLOW.relative_to(ROOT).as_posix())
    add_check(checks, "workflow_not_empty", bool(text.strip()), f"{len(text)} characters")

    for check_id, snippet in REQUIRED_SNIPPETS.items():
        add_check(checks, check_id, snippet in text, snippet)
    for check_id, pattern in FORBIDDEN_PATTERNS.items():
        matched = bool(re.search(pattern, text))
        add_check(checks, check_id, not matched, pattern)
    return checks


def markdown_report(checks: list[dict]) -> str:
    failed = [item for item in checks if not item["passed"]]
    lines = [
        "# CI Workflow Audit",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Checks: {len(checks)}",
        f"- Passed: {len(checks) - len(failed)}",
        f"- Failed: {len(failed)}",
        "",
        "## Checks",
        "",
        "| Check | Result | Evidence |",
        "| --- | --- | --- |",
    ]
    for item in checks:
        result = "PASS" if item["passed"] else "FAIL"
        lines.append(f"| {item['check_id']} | {result} | `{item['evidence']}` |")

    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- CI should run the same local acceptance suite that maintainers run manually.",
            "- Keep workflow permissions minimal and do not store secrets in workflow files.",
            "- If this audit fails, fix `.github/workflows/wiki-acceptance.yml` before publishing packages.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    checks = audit()
    failed = [item for item in checks if not item["passed"]]
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(checks), encoding="utf-8")
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if failed:
        print("CI WORKFLOW AUDIT FAILED")
        for item in failed:
            print(f"- {item['check_id']}: {item['evidence']}")
        return 1
    print(f"CI WORKFLOW AUDIT PASSED ({len(checks)} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
