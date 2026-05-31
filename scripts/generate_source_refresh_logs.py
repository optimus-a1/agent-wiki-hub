#!/usr/bin/env python3
"""Create and check per-wiki source refresh log templates."""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
PLAYBOOK_JSON = ROOT / "registry" / "source-refresh-playbook.json"
DOCS_OUT = ROOT / "docs" / "SOURCE_REFRESH_LOG_STATUS.md"
JSON_OUT = ROOT / "registry" / "source-refresh-log-status.json"
LOG_NAME = "source-refresh-log.md"

LOG_BULLET = "- Added source refresh log template for authoritative source verification."
REQUIRED_HEADINGS = [
    "# Source Refresh Log",
    "## Purpose",
    "## How To Use",
    "## Refresh Tasks",
    "## Evidence Entry Template",
    "## Safety Notes",
]


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def parse_manifest(path: Path) -> dict:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw in read_text(path).splitlines():
        if ":" not in raw or raw.startswith(" ") or raw.lstrip().startswith("-"):
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def tasks_by_wiki() -> dict[str, list[dict]]:
    playbook = read_json(PLAYBOOK_JSON)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for task in playbook.get("tasks", []):
        grouped[task.get("wiki", "")].append(task)
    return grouped


def task_line(task: dict) -> str:
    human = "yes" if task.get("human_confirmation_required") else "no"
    return (
        f"- [ ] {task.get('task_id')} | wave: {task.get('wave')} | priority: {task.get('priority_score')} | "
        f"human_confirmation: {human} | topic: {task.get('topic')}"
    )


def log_template(wiki_id: str, manifest: dict, tasks: list[dict]) -> str:
    risk = manifest.get("risk_level", "unknown")
    freshness = manifest.get("freshness_requirement", "unknown")
    lines = [
        "# Source Refresh Log",
        "",
        f"Wiki: {wiki_id}",
        f"Risk level: {risk}",
        f"Freshness requirement: {freshness}",
        f"Template initialized: {date.today().isoformat()}",
        "",
        "## Purpose",
        "",
        "Record authoritative source verification work before current facts are written into this wiki.",
        "",
        "## How To Use",
        "",
        "1. Read `manifest.yaml`, `AGENTS.md`, `rules/`, and `sources/source-notes.md` first.",
        "2. Pick a task from `docs/SOURCE_REFRESH_PLAYBOOK.md` or `registry/source-refresh-playbook.json`.",
        "3. Verify the claim from authoritative sources before editing wiki content.",
        "4. Record evidence below, including dates, source scope, confidence, and remaining uncertainty.",
        "5. Update `sources/source-notes.md` and `update-log.md` after any content change.",
        "6. Run validation and acceptance commands before release.",
        "",
        "## Refresh Tasks",
        "",
    ]
    if tasks:
        lines.extend(task_line(task) for task in tasks)
    else:
        lines.append("- [ ] No current source-refresh tasks are queued for this wiki.")

    lines.extend(
        [
            "",
            "## Evidence Entry Template",
            "",
            "```yaml",
            "- task_id: SRC-000",
            "  topic: <copy topic from playbook>",
            "  status: pending | verified | unchanged | still-needs-source-update | rejected",
            "  verified_on: YYYY-MM-DD",
            "  source_title: <source title>",
            "  source_publisher: <official publisher or authority>",
            "  source_url_or_reference: <URL or local reference>",
            "  source_published_or_updated: YYYY-MM-DD | unknown",
            "  source_accessed_on: YYYY-MM-DD",
            "  evidence_summary: <short summary of what the source supports>",
            "  affected_pages:",
            "    - sources/source-notes.md",
            "  confidence: low | medium | high",
            "  remaining_uncertainty: <what is still unknown or scope-limited>",
            "  human_reviewer: <name/role or required>",
            "  follow_up: <next action or none>",
            "```",
            "",
            "## Completed Entries",
            "",
            "<Add completed evidence entries here. Do not record secrets, credentials, cookies, private keys, or private account data.>",
            "",
            "## Safety Notes",
            "",
            "- Do not write current facts into wiki pages without dated source evidence.",
            "- Keep `needs-source-update` when sources are missing, conflicting, stale, or outside scope.",
            "- High-risk domains keep human confirmation points even after source refresh is complete.",
            "- Do not add personalized investment advice, final legal opinions, medical diagnoses, offensive security procedures, or platform-rule bypass guidance.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def ensure_update_log(wiki: Path) -> bool:
    path = wiki / "update-log.md"
    text = read_text(path)
    if LOG_BULLET in text:
        return False
    marker = "## 2026-05-27"
    if marker in text:
        text = text.replace(marker, f"{marker}\n\n{LOG_BULLET}", 1)
    else:
        prefix = text.rstrip() + "\n\n" if text.strip() else ""
        text = f"{prefix}## 2026-05-27\n\n{LOG_BULLET}\n"
    path.write_text(text, encoding="utf-8")
    return True


def ensure_log(wiki: Path, tasks: list[dict]) -> dict:
    manifest = parse_manifest(wiki / "manifest.yaml")
    path = wiki / "sources" / LOG_NAME
    path.parent.mkdir(parents=True, exist_ok=True)
    created = False
    updated = False
    if not path.exists():
        path.write_text(log_template(wiki.name, manifest, tasks), encoding="utf-8")
        created = True
    else:
        text = read_text(path)
        missing_lines = [task_line(task) for task in tasks if task.get("task_id") and task.get("task_id") not in text]
        if missing_lines:
            if "## Refresh Tasks" in text:
                text = text.replace("## Refresh Tasks\n\n", "## Refresh Tasks\n\n" + "\n".join(missing_lines) + "\n", 1)
            else:
                text = text.rstrip() + "\n\n## Refresh Tasks\n\n" + "\n".join(missing_lines) + "\n"
            path.write_text(text, encoding="utf-8")
            updated = True
    update_log_changed = ensure_update_log(wiki)
    text = read_text(path)
    missing_headings = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    missing_tasks = [task.get("task_id") for task in tasks if task.get("task_id") and task.get("task_id") not in text]
    return {
        "wiki": wiki.name,
        "path": path.relative_to(ROOT).as_posix(),
        "created": created,
        "updated": updated,
        "update_log_changed": update_log_changed,
        "task_count": len(tasks),
        "missing_headings": missing_headings,
        "missing_tasks": missing_tasks,
        "passed": not missing_headings and not missing_tasks,
    }


def build_status() -> dict:
    grouped = tasks_by_wiki()
    records = []
    for wiki in sorted(path for path in WIKIS.iterdir() if path.is_dir()):
        records.append(ensure_log(wiki, grouped.get(wiki.name, [])))
    return {
        "generated": date.today().isoformat(),
        "wiki_count": len(records),
        "created": sum(1 for record in records if record["created"]),
        "updated": sum(1 for record in records if record["updated"]),
        "update_logs_changed": sum(1 for record in records if record["update_log_changed"]),
        "passed": all(record["passed"] for record in records),
        "logs": records,
    }


def markdown_report(status: dict) -> str:
    lines = [
        "# Source Refresh Log Status",
        "",
        f"Generated: {status['generated']}",
        "",
        "## Summary",
        "",
        f"- Wikis: {status['wiki_count']}",
        f"- Created logs: {status['created']}",
        f"- Updated logs: {status['updated']}",
        f"- Update logs changed: {status['update_logs_changed']}",
        f"- Passed: {'yes' if status['passed'] else 'no'}",
        "",
        "## Logs",
        "",
        "| Wiki | Tasks | Created | Updated | Passed | Path |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for record in status["logs"]:
        lines.append(
            f"| {record['wiki']} | {record['task_count']} | {record['created']} | "
            f"{record['updated']} | {record['passed']} | `{record['path']}` |"
        )
    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- Use each wiki's `sources/source-refresh-log.md` to record source evidence before writing current facts.",
            "- This status report checks that refresh logs contain required headings and queued task IDs.",
            "- Completed evidence entries should never include secrets, credentials, cookies, private keys, or private account data.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    status = build_status()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(status), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if not status["passed"]:
        print("SOURCE REFRESH LOG STATUS FAILED")
        for record in status["logs"]:
            if not record["passed"]:
                print(f"- {record['wiki']}: missing headings={record['missing_headings']} tasks={record['missing_tasks']}")
        return 1
    print(f"SOURCE REFRESH LOGS READY ({status['wiki_count']} wikis)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
