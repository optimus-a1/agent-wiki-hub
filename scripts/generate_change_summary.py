#!/usr/bin/env python3
"""Generate a current-impact and delta summary for Agent Wiki Hub."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DOCS_OUT = ROOT / "docs" / "CHANGE_SUMMARY.md"
JSON_OUT = ROOT / "registry" / "change-summary.json"
REGISTRY = ROOT / "registry"
PACKS = ROOT / "packs"

AUDIT_REPORTS = {
    "acceptance": REGISTRY / "acceptance-report.json",
    "ci": REGISTRY / "ci-audit.json",
    "registry": REGISTRY / "registry-consistency.json",
    "metadata": REGISTRY / "page-metadata-audit.json",
    "coverage": REGISTRY / "coverage-audit.json",
    "links": REGISTRY / "link-audit.json",
    "packs": REGISTRY / "pack-audit.json",
    "safety": REGISTRY / "safety-audit.json",
    "source_refresh_logs": REGISTRY / "source-refresh-log-status.json",
}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def audit_summary(name: str, data: dict) -> dict:
    checks = data.get("checks", [])
    steps = data.get("steps", [])
    logs = data.get("logs", [])
    total = len(checks) or len(steps) or len(logs)
    if checks:
        passed = sum(1 for item in checks if item.get("passed"))
    elif steps:
        passed = sum(1 for item in steps if item.get("passed"))
    elif logs:
        passed = sum(1 for item in logs if item.get("passed"))
    else:
        passed = total if data.get("passed") else 0
    return {
        "name": name,
        "passed": bool(data.get("passed", total == passed)),
        "passed_count": passed,
        "total": total,
        "failed_count": max(total - passed, 0),
    }


def package_records() -> list[dict]:
    records: list[dict] = []
    if not PACKS.exists():
        return records
    for path in sorted(PACKS.glob("*.zip")):
        records.append(
            {
                "name": path.name,
                "path": path.relative_to(ROOT).as_posix(),
                "size_bytes": path.stat().st_size,
            }
        )
    return records


def playbook_counts() -> Counter:
    playbook = read_json(REGISTRY / "source-refresh-playbook.json")
    return Counter(task.get("wiki", "") for task in playbook.get("tasks", []))


def log_ready_map() -> dict[str, bool]:
    status = read_json(REGISTRY / "source-refresh-log-status.json")
    return {record.get("wiki", ""): bool(record.get("passed")) for record in status.get("logs", [])}


def wiki_records() -> list[dict]:
    status = read_json(REGISTRY / "wiki-status.json")
    task_counts = playbook_counts()
    log_ready = log_ready_map()
    records: list[dict] = []
    for wiki in status.get("wikis", []):
        content_counts = wiki.get("content_counts", {})
        knowledge_files = sum(int(value) for value in content_counts.values())
        records.append(
            {
                "id": wiki.get("id", ""),
                "domain": wiki.get("domain", ""),
                "risk_level": wiki.get("risk_level", ""),
                "freshness_requirement": wiki.get("freshness_requirement", ""),
                "knowledge_files": knowledge_files,
                "eval_tests": int(wiki.get("eval_tests", 0)),
                "source_update_topics": len(wiki.get("source_update_topics", [])),
                "source_refresh_tasks": int(task_counts.get(wiki.get("id", ""), 0)),
                "source_refresh_log_ready": bool(log_ready.get(wiki.get("id", ""), False)),
                "pack_size_bytes": int(wiki.get("pack_size_bytes", 0)),
            }
        )
    return records


def build_snapshot() -> dict:
    wikis = wiki_records()
    packages = package_records()
    audits = [audit_summary(name, read_json(path)) for name, path in AUDIT_REPORTS.items() if path.exists()]
    risk_counts = Counter(wiki["risk_level"] for wiki in wikis)
    freshness_counts = Counter(wiki["freshness_requirement"] for wiki in wikis)
    source_queue = read_json(REGISTRY / "source-update-queue.json")
    playbook = read_json(REGISTRY / "source-refresh-playbook.json")

    return {
        "generated": date.today().isoformat(),
        "metrics": {
            "wiki_count": len(wikis),
            "knowledge_files": sum(wiki["knowledge_files"] for wiki in wikis),
            "eval_tests": sum(wiki["eval_tests"] for wiki in wikis),
            "source_update_topics": len(source_queue.get("topics", [])),
            "source_refresh_tasks": int(playbook.get("task_count", 0)),
            "source_refresh_logs": sum(1 for wiki in wikis if wiki["source_refresh_log_ready"]),
            "package_count": len(packages),
            "package_bytes": sum(package["size_bytes"] for package in packages),
            "audit_gates": len(audits),
            "audit_failures": sum(1 for audit in audits if not audit["passed"]),
        },
        "risk_counts": dict(sorted(risk_counts.items())),
        "freshness_counts": dict(sorted(freshness_counts.items())),
        "wikis": wikis,
        "packages": packages,
        "audits": audits,
    }


def delta_number(current: int, previous: int | None) -> int | None:
    if previous is None:
        return None
    return current - previous


def build_deltas(current: dict, previous: dict | None) -> dict:
    if not previous:
        return {"has_previous": False, "metrics": {}, "wikis": []}
    previous_metrics = previous.get("metrics", {})
    metrics = {
        key: delta_number(int(value), int(previous_metrics[key])) if key in previous_metrics else None
        for key, value in current.get("metrics", {}).items()
    }
    previous_wikis = {wiki.get("id"): wiki for wiki in previous.get("wikis", [])}
    wiki_deltas = []
    for wiki in current.get("wikis", []):
        old = previous_wikis.get(wiki["id"], {})
        wiki_deltas.append(
            {
                "id": wiki["id"],
                "knowledge_files": delta_number(wiki["knowledge_files"], old.get("knowledge_files")) if old else None,
                "eval_tests": delta_number(wiki["eval_tests"], old.get("eval_tests")) if old else None,
                "source_update_topics": delta_number(wiki["source_update_topics"], old.get("source_update_topics")) if old else None,
                "source_refresh_tasks": delta_number(wiki["source_refresh_tasks"], old.get("source_refresh_tasks")) if old else None,
                "pack_size_bytes": delta_number(wiki["pack_size_bytes"], old.get("pack_size_bytes")) if old else None,
            }
        )
    return {"has_previous": True, "metrics": metrics, "wikis": wiki_deltas}


def fmt_delta(value: int | None) -> str:
    if value is None:
        return "n/a"
    if value > 0:
        return f"+{value}"
    return str(value)


def fmt_size(size: int) -> str:
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"
    if size >= 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size} B"


def markdown_report(current: dict, deltas: dict) -> str:
    metrics = current["metrics"]
    delta_metrics = deltas.get("metrics", {})
    lines = [
        "# Change Summary",
        "",
        f"Generated: {current['generated']}",
        "",
        "## Summary",
        "",
        "| Metric | Current | Delta |",
        "| --- | ---: | ---: |",
    ]
    for key in [
        "wiki_count",
        "knowledge_files",
        "eval_tests",
        "source_update_topics",
        "source_refresh_tasks",
        "source_refresh_logs",
        "package_count",
        "package_bytes",
        "audit_gates",
        "audit_failures",
    ]:
        value = metrics[key]
        display = fmt_size(value) if key == "package_bytes" else str(value)
        delta = delta_metrics.get(key)
        delta_display = fmt_delta(delta)
        if key == "package_bytes" and isinstance(delta, int):
            delta_display = fmt_delta(delta)
        lines.append(f"| {key} | {display} | {delta_display} |")

    if not deltas.get("has_previous"):
        lines.extend(["", "No previous change summary baseline was available; deltas start after this run."])

    lines.extend(["", "## Audit Gates", "", "| Gate | Result | Passed | Total |", "| --- | --- | ---: | ---: |"])
    for audit in current["audits"]:
        result = "PASS" if audit["passed"] else "FAIL"
        lines.append(f"| {audit['name']} | {result} | {audit['passed_count']} | {audit['total']} |")

    wiki_delta_map = {item["id"]: item for item in deltas.get("wikis", [])}
    lines.extend(
        [
            "",
            "## Wiki Impact Matrix",
            "",
            "| Wiki | Risk | Freshness | Files | Files Delta | Evals | Source Topics | Refresh Tasks | Log Ready | Pack Size |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for wiki in current["wikis"]:
        delta = wiki_delta_map.get(wiki["id"], {})
        lines.append(
            f"| {wiki['id']} | {wiki['risk_level']} | {wiki['freshness_requirement']} | "
            f"{wiki['knowledge_files']} | {fmt_delta(delta.get('knowledge_files'))} | "
            f"{wiki['eval_tests']} | {wiki['source_update_topics']} | {wiki['source_refresh_tasks']} | "
            f"{'yes' if wiki['source_refresh_log_ready'] else 'no'} | {fmt_size(wiki['pack_size_bytes'])} |"
        )

    lines.extend(["", "## Packages", "", "| Package | Size |", "| --- | ---: |"])
    for package in current["packages"]:
        lines.append(f"| `{package['path']}` | {fmt_size(package['size_bytes'])} |")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Positive file deltas usually mean wiki content, source templates, or generated support files were added.",
            "- Source-update topics are not failures; they are current-fact gates that must be verified before use.",
            "- Audit failures should block release until fixed.",
            "- High-risk wiki changes still require human confirmation points, even when all local audits pass.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    old = read_json(JSON_OUT)
    previous = old.get("current") if old else None
    current = build_snapshot()
    deltas = build_deltas(current, previous)
    output = {
        "generated": current["generated"],
        "current": current,
        "previous": previous,
        "deltas": deltas,
    }
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    DOCS_OUT.write_text(markdown_report(current, deltas), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"CHANGE SUMMARY GENERATED ({current['metrics']['wiki_count']} wikis)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
