#!/usr/bin/env python3
"""Generate a per-ticket readiness matrix across the source-review pipeline."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_READINESS_MATRIX.md"
JSON_OUT = REGISTRY / "source-review-readiness-matrix.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}

REPORTS = {
    "source_refresh_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_review_work_orders": "docs/SOURCE_REVIEW_WORK_ORDERS.md",
    "source_review_packet_rehearsal": "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "source_review_packet_audit": "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "source_review_session_plan": "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "source_reviewer_queue": "docs/SOURCE_REVIEWER_QUEUE.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def repo_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def bool_word(value: bool) -> str:
    return "yes" if value else "no"


def ticket_status(ticket: dict) -> str:
    return str(ticket.get("status") or "open_pending_source_refresh")


def is_final(ticket: dict) -> bool:
    return bool(ticket.get("is_final")) or ticket_status(ticket) in FINAL_STATUSES


def ticket_sort_key(row: dict) -> tuple:
    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    wave_order = {"wave-1": 0, "wave-2": 1, "wave-3": 2}
    return (
        priority_order.get(row.get("priority", ""), 99),
        wave_order.get(row.get("wave", ""), 99),
        row.get("wiki", ""),
        row.get("ticket_id", ""),
    )


def load_packet_entry_map(packet_audit: dict) -> tuple[dict[str, list[dict]], dict[str, bool]]:
    entries_by_ticket: dict[str, list[dict]] = defaultdict(list)
    active_packets = [packet for packet in packet_audit.get("packets", []) if packet.get("blocking", True)]
    packet_passed = {packet.get("path", ""): bool(packet.get("passed")) for packet in active_packets}
    for packet in active_packets:
        for entry in packet.get("entries", []):
            ticket_id = entry.get("ticket_id")
            if ticket_id:
                entries_by_ticket[str(ticket_id)].append(entry)
    return entries_by_ticket, packet_passed


def rehearsal_passed_by_packet(rehearsal: dict) -> dict[str, bool]:
    return {result.get("packet", ""): bool(result.get("passed")) for result in rehearsal.get("results", [])}


def readiness_stage(row: dict) -> str:
    if row["finalized"]:
        return "finalized"
    if not row["has_reviewer_card"]:
        return "needs-reviewer-assignment"
    if not row["selected_for_current_session"]:
        return "queued-not-in-current-session"
    if not row["has_packet_entry"]:
        return "selected-needs-packet-entry"
    if not row["packet_audit_passed"]:
        return "packet-audit-blocked"
    if not row["packet_rehearsal_passed"]:
        return "packet-rehearsal-blocked"
    return "ready-for-source-collection"


def build_matrix() -> dict:
    tickets_data = read_json(REGISTRY / "source-refresh-tickets.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    reviewer_queue = read_json(REGISTRY / "source-reviewer-queue.json")
    session_plan = read_json(REGISTRY / "source-review-session-plan.json")
    packet_bundle = read_json(REGISTRY / "source-review-packet-bundle.json")
    packet_audit = read_json(REGISTRY / "source-review-packet-audit.json")
    rehearsal = read_json(REGISTRY / "source-review-packet-rehearsal.json")
    quality = read_json(REGISTRY / "source-evidence-quality-audit.json")

    completion_by_ticket = {ticket.get("ticket_id"): ticket for ticket in completion.get("tickets", []) if ticket.get("ticket_id")}
    source_tickets = tickets_data.get("tickets") or completion.get("tickets", [])
    review_by_ticket = {card.get("ticket_id"): card for card in reviewer_queue.get("review_cards", []) if card.get("ticket_id")}
    selected_ids = {review.get("ticket_id") for review in session_plan.get("selected_reviews", []) if review.get("ticket_id")}
    entries_by_ticket, packet_passed = load_packet_entry_map(packet_audit)
    packet_rehearsed = rehearsal_passed_by_packet(rehearsal)

    rows = []
    for ticket in source_tickets:
        ticket_id = ticket.get("ticket_id", "")
        completion_ticket = completion_by_ticket.get(ticket_id, {})
        merged = dict(ticket)
        merged.update({key: value for key, value in completion_ticket.items() if value not in (None, "")})
        review = review_by_ticket.get(ticket_id, {})
        packet_entries = entries_by_ticket.get(ticket_id, [])
        packet_paths = sorted({entry.get("packet", "") for entry in packet_entries if entry.get("packet")})
        packet_entry_passed = bool(packet_entries) and all(entry.get("passed") for entry in packet_entries)
        packet_paths_passed = bool(packet_paths) and all(packet_passed.get(path, False) for path in packet_paths)
        rehearsed = bool(packet_paths) and all(packet_rehearsed.get(path, False) for path in packet_paths)
        row = {
            "ticket_id": ticket_id,
            "task_id": merged.get("task_id", ""),
            "wiki": merged.get("wiki", ""),
            "priority": review.get("priority", merged.get("priority", "")),
            "wave": review.get("wave", merged.get("wave", "")),
            "risk_level": review.get("risk_level", merged.get("risk_level", "")),
            "freshness": review.get("freshness", merged.get("freshness", "")),
            "category": review.get("category", merged.get("category", "")),
            "topic": merged.get("topic", ""),
            "status": ticket_status(merged),
            "finalized": is_final(merged),
            "verified": bool(merged.get("is_verified", False)),
            "has_reviewer_card": bool(review),
            "reviewer_role": review.get("reviewer_role", ""),
            "human_review_gate": bool(review.get("human_review_gate", merged.get("human_confirmation_required", False))),
            "selected_for_current_session": ticket_id in selected_ids,
            "has_packet_entry": bool(packet_entries),
            "packet_entry_count": len(packet_entries),
            "packet_paths": packet_paths,
            "packet_audit_passed": packet_entry_passed and packet_paths_passed,
            "packet_rehearsal_passed": rehearsed,
            "evidence_log": review.get("evidence_log", merged.get("log_path", "")),
            "source_notes": review.get("source_notes", f"wikis/{merged.get('wiki', '')}/sources/source-notes.md"),
        }
        row["readiness_stage"] = readiness_stage(row)
        rows.append(row)

    rows = sorted(rows, key=ticket_sort_key)
    stage_counts = Counter(row["readiness_stage"] for row in rows)
    selected_rows = [row for row in rows if row["selected_for_current_session"]]
    selected_finalized_count = sum(1 for row in selected_rows if row["finalized"])
    selected_verified_count = sum(1 for row in selected_rows if row["verified"])
    post_import_completed = bool(selected_rows) and selected_finalized_count == len(selected_rows)
    checks = [
        {
            "check": "required source review artifacts exist",
            "passed": all((ROOT / path).exists() for path in [
                "registry/source-refresh-tickets.json",
                "registry/source-refresh-completion-audit.json",
                "registry/source-reviewer-queue.json",
                "registry/source-review-session-plan.json",
                "registry/source-review-packet-audit.json",
                "registry/source-review-packet-rehearsal.json",
            ]),
            "detail": "core source review registry artifacts",
        },
        {
            "check": "all tickets represented in matrix",
            "passed": len(rows) == int(tickets_data.get("ticket_count", len(rows))),
            "detail": f"{len(rows)} rows for {tickets_data.get('ticket_count', len(rows))} tickets",
        },
        {
            "check": "open tickets have reviewer cards",
            "passed": all(row["has_reviewer_card"] for row in rows if not row["finalized"]),
            "detail": f"{sum(1 for row in rows if row['has_reviewer_card'])}/{len(rows)} rows have reviewer cards",
        },
        {
            "check": "selected reviews have packet entries",
            "passed": all(row["has_packet_entry"] for row in rows if row["selected_for_current_session"]),
            "detail": f"{sum(1 for row in rows if row['selected_for_current_session'] and row['has_packet_entry'])}/{sum(1 for row in rows if row['selected_for_current_session'])} selected rows have packet entries",
        },
        {
            "check": "packet audit passed",
            "passed": bool(packet_audit.get("passed")),
            "detail": f"{packet_audit.get('packet_count', 0)} packets, {packet_audit.get('issue_count', 0)} issues",
        },
        {
            "check": "packet rehearsal passed",
            "passed": bool(rehearsal.get("passed")) or post_import_completed,
            "detail": "selected tickets already finalized; rehearsal is advisory"
            if post_import_completed and not bool(rehearsal.get("passed"))
            else f"{rehearsal.get('passed_dry_run_count', 0)}/{rehearsal.get('dry_run_count', 0)} dry-runs passed",
        },
        {
            "check": "current facts remain gated while open tickets exist",
            "passed": (not bool(reviewer_queue.get("current_fact_ready"))) if any(not row["finalized"] for row in rows) else True,
            "detail": "current_fact_ready=false while open tickets remain",
        },
    ]

    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "purpose": "Show per-ticket readiness across reviewer assignment, session selection, packet coverage, packet audit, rehearsal, and completion state.",
        "current_fact_ready": bool(reviewer_queue.get("current_fact_ready", False)),
        "ticket_count": len(rows),
        "open_ticket_count": sum(1 for row in rows if not row["finalized"]),
        "finalized_ticket_count": sum(1 for row in rows if row["finalized"]),
        "verified_ticket_count": sum(1 for row in rows if row["verified"]),
        "ready_for_source_collection_count": stage_counts.get("ready-for-source-collection", 0),
        "queued_not_in_current_session_count": stage_counts.get("queued-not-in-current-session", 0),
        "selected_review_count": int(session_plan.get("selected_review_count", 0)),
        "selected_finalized_count": selected_finalized_count,
        "selected_verified_count": selected_verified_count,
        "post_import_completed": post_import_completed,
        "source_review_phase": "post-import-completed" if post_import_completed else "pre-import-or-in-progress",
        "packet_entry_ticket_count": sum(1 for row in rows if row["has_packet_entry"]),
        "packet_audit_issue_count": int(packet_audit.get("issue_count", 0)),
        "packet_rehearsal_failed_count": int(rehearsal.get("failed_dry_run_count", 0)),
        "evidence_entry_count": int(quality.get("entry_count", 0)),
        "stage_counts": dict(sorted(stage_counts.items())),
        "wiki_stage_counts": {
            wiki: dict(sorted(Counter(item["readiness_stage"] for item in items).items()))
            for wiki, items in sorted(group_by(rows, "wiki").items())
        },
        "wave_stage_counts": {
            wave: dict(sorted(Counter(item["readiness_stage"] for item in items).items()))
            for wave, items in sorted(group_by(rows, "wave").items())
        },
        "rows": rows,
        "checks": checks,
        "reports": REPORTS,
    }


def group_by(rows: list[dict], key: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, "unknown"))].append(row)
    return grouped


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Readiness Matrix",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Summary",
        "",
        f"- Passed: {bool_word(data['passed'])}",
        f"- Current-fact ready: {bool_word(data['current_fact_ready'])}",
        f"- Tickets: {data['ticket_count']}",
        f"- Open tickets: {data['open_ticket_count']}",
        f"- Finalized tickets: {data['finalized_ticket_count']}",
        f"- Verified tickets: {data['verified_ticket_count']}",
        f"- Ready for source collection: {data['ready_for_source_collection_count']}",
        f"- Queued outside current session: {data['queued_not_in_current_session_count']}",
        f"- Selected finalized tickets: {data['selected_finalized_count']}",
        f"- Selected verified tickets: {data['selected_verified_count']}",
        f"- Source review phase: {data['source_review_phase']}",
        f"- Packet audit issues: {data['packet_audit_issue_count']}",
        f"- Packet rehearsal failures: {data['packet_rehearsal_failed_count']}",
        "",
        "## Stage Counts",
        "",
    ]
    for stage, count in data["stage_counts"].items():
        lines.append(f"- {stage}: {count}")

    lines.extend(
        [
            "",
            "## Matrix",
            "",
            "| Ticket | Wiki | Priority | Wave | Risk | Reviewer | Session | Packet | Audit | Rehearsal | Stage | Topic |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in data["rows"]:
        lines.append(
            f"| `{row['ticket_id']}` | {repo_link('wikis/' + row['wiki'], row['wiki'])} | {row['priority']} | {row['wave']} | "
            f"{row['risk_level']} | {row['reviewer_role'] or '-'} | {bool_word(row['selected_for_current_session'])} | "
            f"{row['packet_entry_count']} | {bool_word(row['packet_audit_passed'])} | {bool_word(row['packet_rehearsal_passed'])} | "
            f"{row['readiness_stage']} | {row['topic']} |"
        )

    lines.extend(["", "## Related Reports", ""])
    for name, path in data["reports"].items():
        lines.append(f"- {name}: {repo_link(path)}")

    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        result = "PASS" if check["passed"] else "FAIL"
        lines.append(f"| {check['check']} | {result} | {check['detail']} |")

    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- This matrix does not fetch, verify, or certify external facts.",
            "- `ready-for-source-collection` means local packet and dry-run gates are ready, not that facts are verified.",
            "- Current facts remain gated until completion and evidence quality audits show all relevant tickets are finalized.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_matrix()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(
        "SOURCE REVIEW READINESS MATRIX "
        f"{'PASSED' if data['passed'] else 'FAILED'} "
        f"({data['ready_for_source_collection_count']} ready, {data['queued_not_in_current_session_count']} queued)"
    )
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
