#!/usr/bin/env python3
"""Audit completion status for source refresh tickets."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TICKETS_JSON = ROOT / "registry" / "source-refresh-tickets.json"
DOCS_OUT = ROOT / "docs" / "SOURCE_REFRESH_COMPLETION_AUDIT.md"
JSON_OUT = ROOT / "registry" / "source-refresh-completion-audit.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}
OPEN_STATUSES = {"open_pending_source_refresh", "pending", ""}
VALID_STATUSES = FINAL_STATUSES | OPEN_STATUSES
REQUIRED_EVIDENCE_FIELDS = [
    "status",
    "verified_on",
    "source_title",
    "source_publisher",
    "source_url_or_reference",
    "source_accessed_on",
    "evidence_summary",
    "confidence",
    "remaining_uncertainty",
]
PLACEHOLDER_MARKERS = {"<", "YYYY-MM-DD", "unknown", "required"}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def md_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def completed_section(text: str) -> str:
    marker = "## Completed Entries"
    if marker not in text:
        return ""
    section = text.split(marker, 1)[1]
    next_heading = re.search(r"\n## ", section)
    if next_heading:
        section = section[: next_heading.start()]
    return section


def parse_completed_entries(text: str) -> list[dict]:
    section = completed_section(text)
    entries: list[dict] = []
    current: dict[str, str] | None = None
    for raw in section.splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("<"):
            continue
        if stripped.startswith("- task_id:"):
            if current:
                entries.append(current)
            current = {"task_id": stripped.split(":", 1)[1].strip()}
            continue
        if current and ":" in stripped and not stripped.startswith("- "):
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip()
        elif current and stripped.startswith("- ") and "affected_pages" in current:
            current["affected_pages"] = (current.get("affected_pages", "") + " " + stripped[2:].strip()).strip()
    if current:
        entries.append(current)
    return entries


def is_placeholder(value: str) -> bool:
    value = (value or "").strip()
    if not value:
        return True
    lowered = value.casefold()
    return any(marker.casefold() in lowered for marker in PLACEHOLDER_MARKERS)


def evidence_by_task(log_text: str) -> dict[str, dict]:
    records: dict[str, dict] = {}
    for entry in parse_completed_entries(log_text):
        task_id = entry.get("task_id", "").strip()
        ticket_id = entry.get("ticket_id", "").strip()
        if task_id and task_id != "SRC-000":
            records.setdefault(task_id, entry)
        if ticket_id:
            records.setdefault(ticket_id, entry)
    return records


def evidence_status(entry: dict | None) -> str:
    if not entry:
        return "open_pending_source_refresh"
    status = entry.get("status", "").strip()
    if not status or "|" in status:
        return "pending"
    return status


def evidence_issues(ticket: dict, entry: dict | None) -> list[str]:
    status = evidence_status(entry)
    issues: list[str] = []
    if status not in VALID_STATUSES:
        issues.append(f"unknown status: {status}")
    if status not in FINAL_STATUSES:
        return issues
    if not entry:
        issues.append("missing completed evidence entry")
        return issues
    for field in REQUIRED_EVIDENCE_FIELDS:
        if is_placeholder(entry.get(field, "")):
            issues.append(f"missing or placeholder field: {field}")
    if ticket.get("human_confirmation_required") and is_placeholder(entry.get("human_reviewer", "")):
        issues.append("missing human reviewer for high-risk ticket")
    return issues


def ticket_result(ticket: dict) -> dict:
    wiki = ticket.get("wiki", "")
    log_path = ROOT / "wikis" / wiki / "sources" / "source-refresh-log.md"
    log_text = read_text(log_path)
    entries = evidence_by_task(log_text)
    entry = entries.get(ticket.get("task_id", "")) or entries.get(ticket.get("ticket_id", ""))
    status = evidence_status(entry)
    issues = evidence_issues(ticket, entry)
    task_present = bool(ticket.get("task_id") and ticket.get("task_id") in log_text)
    log_exists = log_path.exists()
    structural_passed = log_exists and task_present and not issues
    return {
        "ticket_id": ticket.get("ticket_id", ""),
        "task_id": ticket.get("task_id", ""),
        "wiki": wiki,
        "wave": ticket.get("wave", ""),
        "priority_score": ticket.get("priority_score", 0),
        "risk_level": ticket.get("risk_level", ""),
        "topic": ticket.get("topic", ""),
        "human_confirmation_required": bool(ticket.get("human_confirmation_required")),
        "log_path": rel(log_path) if log_path.exists() else f"wikis/{wiki}/sources/source-refresh-log.md",
        "log_exists": log_exists,
        "task_present_in_log": task_present,
        "has_completed_evidence": bool(entry),
        "status": status,
        "is_final": status in FINAL_STATUSES,
        "is_verified": status == "verified",
        "issues": issues,
        "passed": structural_passed,
    }


def build_audit() -> dict:
    tickets_data = read_json(TICKETS_JSON)
    tickets = tickets_data.get("tickets", [])
    results = [ticket_result(ticket) for ticket in tickets]
    status_counts = Counter(result["status"] for result in results)
    wiki_counts = Counter(result["wiki"] for result in results)
    open_results = [result for result in results if not result["is_final"]]
    issue_results = [result for result in results if result["issues"] or not result["log_exists"] or not result["task_present_in_log"]]
    passed = all(result["passed"] for result in results)
    completion_ready = bool(results) and all(result["is_final"] for result in results)
    return {
        "generated": date.today().isoformat(),
        "passed": passed,
        "completion_ready_for_current_fact_use": completion_ready,
        "ticket_count": len(results),
        "finalized_ticket_count": sum(1 for result in results if result["is_final"]),
        "verified_ticket_count": sum(1 for result in results if result["is_verified"]),
        "open_ticket_count": len(open_results),
        "issue_count": len(issue_results),
        "status_counts": dict(sorted(status_counts.items())),
        "wiki_counts": dict(sorted(wiki_counts.items())),
        "tickets": results,
        "open_tickets": open_results,
        "issues": issue_results,
    }


def markdown_report(audit: dict) -> str:
    by_wiki: dict[str, list[dict]] = defaultdict(list)
    for result in audit["tickets"]:
        by_wiki[result["wiki"]].append(result)

    lines = [
        "# Source Refresh Completion Audit",
        "",
        f"Generated: {audit['generated']}",
        "",
        "## Purpose",
        "",
        "This audit checks whether source refresh tickets have matching refresh-log tasks and completed evidence entries. It does not verify any external source by itself.",
        "",
        "## Summary",
        "",
        f"- Tickets: {audit['ticket_count']}",
        f"- Finalized tickets: {audit['finalized_ticket_count']}",
        f"- Verified tickets: {audit['verified_ticket_count']}",
        f"- Open tickets: {audit['open_ticket_count']}",
        f"- Structural issues: {audit['issue_count']}",
        f"- Completion ready for current-fact use: {'yes' if audit['completion_ready_for_current_fact_use'] else 'no'}",
        f"- Audit passed: {'yes' if audit['passed'] else 'no'}",
        "",
        "## Status Counts",
        "",
        "| Status | Tickets |",
        "| --- | ---: |",
    ]
    for status, count in audit["status_counts"].items():
        lines.append(f"| {status} | {count} |")

    lines.extend(["", "## Wiki Completion", "", "| Wiki | Tickets | Finalized | Verified | Open | Issues |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for wiki, items in sorted(by_wiki.items()):
        finalized = sum(1 for item in items if item["is_final"])
        verified = sum(1 for item in items if item["is_verified"])
        open_count = sum(1 for item in items if not item["is_final"])
        issues = sum(1 for item in items if item["issues"] or not item["log_exists"] or not item["task_present_in_log"])
        lines.append(f"| {wiki} | {len(items)} | {finalized} | {verified} | {open_count} | {issues} |")

    lines.extend(["", "## Open Tickets", "", "| Ticket | Wiki | Wave | Topic | Log |", "| --- | --- | --- | --- | --- |"])
    for item in audit["open_tickets"]:
        lines.append(f"| {item['ticket_id']} | {item['wiki']} | {item['wave']} | {item['topic']} | {md_link(item['log_path'])} |")

    lines.extend(["", "## Issues", ""])
    if audit["issues"]:
        lines.extend(["| Ticket | Wiki | Issue |", "| --- | --- | --- |"])
        for item in audit["issues"]:
            issue_text = "; ".join(item["issues"])
            if not item["log_exists"]:
                issue_text = (issue_text + "; " if issue_text else "") + "missing source-refresh-log.md"
            if not item["task_present_in_log"]:
                issue_text = (issue_text + "; " if issue_text else "") + "task id missing from refresh log"
            lines.append(f"| {item['ticket_id']} | {item['wiki']} | {issue_text} |")
    else:
        lines.append("No structural issues found. Open tickets still require source verification before current facts are written.")

    lines.extend(
        [
            "",
            "## Completion Rules",
            "",
            "- A ticket is open until `sources/source-refresh-log.md` contains a completed evidence entry with its task id.",
            "- Final statuses are `verified`, `unchanged`, `still-needs-source-update`, and `rejected`.",
            "- `verified` means the source evidence supports a safe update; it does not remove high-risk human confirmation requirements.",
            "- `still-needs-source-update` is a valid final audit status only when the evidence entry explains why sources were insufficient.",
            "- Do not mark tickets verified without dated authoritative evidence.",
            "",
            "## Re-run",
            "",
            "```bash",
            "python3 scripts/audit_source_refresh_completion.py",
            "python3 scripts/run_acceptance.py",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    audit = build_audit()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(audit), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if not audit["passed"]:
        print("SOURCE REFRESH COMPLETION AUDIT FAILED")
        return 1
    print(
        "SOURCE REFRESH COMPLETION AUDIT PASSED "
        f"({audit['open_ticket_count']} open, {audit['verified_ticket_count']} verified)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
