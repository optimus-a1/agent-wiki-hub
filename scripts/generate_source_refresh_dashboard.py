#!/usr/bin/env python3
"""Generate a one-page dashboard for source refresh readiness."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS_OUT = ROOT / "docs" / "SOURCE_REFRESH_DASHBOARD.md"
JSON_OUT = REGISTRY / "source-refresh-dashboard.json"

REPORT_PATHS = {
    "source_update_queue": "docs/SOURCE_UPDATE_QUEUE.md",
    "source_refresh_playbook": "docs/SOURCE_REFRESH_PLAYBOOK.md",
    "source_refresh_tickets": "docs/SOURCE_REFRESH_TICKETS.md",
    "source_refresh_wave_runner": "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
    "source_reviewer_queue": "docs/SOURCE_REVIEWER_QUEUE.md",
    "source_review_session_plan": "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_review_work_orders": "docs/SOURCE_REVIEW_WORK_ORDERS.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "source_review_packet_audit": "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "source_review_packet_rehearsal": "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "source_evidence_recorder": "docs/SOURCE_EVIDENCE_RECORDER.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_evidence_packet_fixtures": "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
    "source_refresh_log_status": "docs/SOURCE_REFRESH_LOG_STATUS.md",
    "safety_audit": "docs/SAFETY_AUDIT.md",
    "acceptance": "docs/ACCEPTANCE_REPORT.md",
    "release_notes": "docs/RELEASE_NOTES.md",
}

NON_BLOCKING_GATES = {"current-fact completion ready", "acceptance passed"}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def doc_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def parse_registry(path: Path) -> dict[str, dict]:
    records: dict[str, dict] = {}
    current: dict | None = None
    for raw in read_text(path).splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw.startswith("  - "):
            current = {}
            item = stripped[2:]
            if ":" in item:
                key, value = item.split(":", 1)
                current[key.strip()] = value.strip()
            if current.get("id"):
                records[str(current["id"])] = current
            continue
        if raw.startswith("    ") and current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip()
            if current.get("id"):
                records[str(current["id"])] = current
    return records


def audit_passed(path: str) -> bool:
    data = read_json(ROOT / path)
    if not data:
        return False
    return bool(data.get("passed"))


def gate_records(dashboard: dict) -> list[dict]:
    completion = dashboard["source_refresh"]["completion"]
    quality = dashboard["source_refresh"]["quality"]
    return [
        {
            "gate": "source tickets generated",
            "passed": dashboard["source_refresh"]["ticket_count"] > 0,
            "detail": f"{dashboard['source_refresh']['ticket_count']} tickets",
        },
        {
            "gate": "source refresh logs ready",
            "passed": audit_passed("registry/source-refresh-log-status.json"),
            "detail": f"{dashboard['source_refresh']['log_count']} wiki logs",
        },
        {
            "gate": "completion audit structurally passed",
            "passed": bool(completion.get("passed")),
            "detail": f"{completion.get('open_ticket_count', 0)} open, {completion.get('verified_ticket_count', 0)} verified",
        },
        {
            "gate": "evidence quality passed",
            "passed": bool(quality.get("passed", True)),
            "detail": f"{quality.get('entry_count', 0)} entries, {quality.get('issue_count', 0)} issues",
        },
        {
            "gate": "source reviewer queue generated",
            "passed": audit_passed("registry/source-reviewer-queue.json"),
            "detail": "reviewer roles and human gates assigned",
        },
        {
            "gate": "source review session plan generated",
            "passed": audit_passed("registry/source-review-session-plan.json"),
            "detail": "next source-review session selected",
        },
        {
            "gate": "source review packet bundle generated",
            "passed": audit_passed("registry/source-review-packet-bundle.json"),
            "detail": "pending packet templates ready for dry-run import",
        },
        {
            "gate": "source review packet audit passed",
            "passed": audit_passed("registry/source-review-packet-audit.json"),
            "detail": "packet templates checked before import",
        },
        {
            "gate": "source review packet rehearsal passed",
            "passed": audit_passed("registry/source-review-packet-rehearsal.json"),
            "detail": "packet templates dry-run through importer",
        },
        {
            "gate": "source review readiness matrix generated",
            "passed": audit_passed("registry/source-review-readiness-matrix.json"),
            "detail": "per-ticket readiness summarized",
        },
        {
            "gate": "source review work orders generated",
            "passed": audit_passed("registry/source-review-work-orders.json"),
            "detail": "ready tickets have offline work orders",
        },
        {
            "gate": "current-fact completion ready",
            "passed": bool(completion.get("completion_ready_for_current_fact_use")),
            "detail": "requires all tickets finalized before current-fact use",
        },
        {
            "gate": "safety audit passed",
            "passed": audit_passed("registry/safety-audit.json"),
            "detail": "high-risk boundaries checked",
        },
        {
            "gate": "acceptance passed",
            "passed": audit_passed("registry/acceptance-report.json"),
            "detail": "full local acceptance suite",
        },
        {
            "gate": "package audit passed",
            "passed": audit_passed("registry/pack-audit.json"),
            "detail": "zip package integrity",
        },
        {
            "gate": "link audit passed",
            "passed": audit_passed("registry/link-audit.json"),
            "detail": "local references checked",
        },
    ]


def priority_progress(tickets: list[dict], registry: dict[str, dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for ticket in tickets:
        priority = registry.get(ticket.get("wiki", ""), {}).get("priority", "unknown")
        grouped[priority].append(ticket)
    records = []
    for priority in ["P0", "P1", "P2", "unknown"]:
        items = grouped.get(priority, [])
        if not items:
            continue
        records.append(
            {
                "priority": priority,
                "tickets": len(items),
                "open": sum(1 for item in items if not item.get("is_final")),
                "finalized": sum(1 for item in items if item.get("is_final")),
                "verified": sum(1 for item in items if item.get("is_verified")),
                "issues": sum(1 for item in items if item.get("issues")),
            }
        )
    return records


def wiki_progress(tickets: list[dict], registry: dict[str, dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for ticket in tickets:
        grouped[ticket.get("wiki", "")].append(ticket)
    records = []
    for wiki in sorted(grouped):
        items = grouped[wiki]
        meta = registry.get(wiki, {})
        records.append(
            {
                "wiki": wiki,
                "priority": meta.get("priority", "unknown"),
                "risk_level": meta.get("risk_level", ""),
                "freshness": meta.get("freshness", ""),
                "tickets": len(items),
                "open": sum(1 for item in items if not item.get("is_final")),
                "finalized": sum(1 for item in items if item.get("is_final")),
                "verified": sum(1 for item in items if item.get("is_verified")),
                "human_confirmation_required": sum(1 for item in items if item.get("human_confirmation_required")),
                "issues": sum(1 for item in items if item.get("issues")),
            }
        )
    return sorted(records, key=lambda item: (item["priority"], item["wiki"]))


def wave_progress(tickets: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for ticket in tickets:
        grouped[ticket.get("wave", "unknown")].append(ticket)
    records = []
    for wave in ["wave-1", "wave-2", "wave-3", "unknown"]:
        items = grouped.get(wave, [])
        if not items:
            continue
        records.append(
            {
                "wave": wave,
                "tickets": len(items),
                "open": sum(1 for item in items if not item.get("is_final")),
                "finalized": sum(1 for item in items if item.get("is_final")),
                "verified": sum(1 for item in items if item.get("is_verified")),
                "human_confirmation_required": sum(1 for item in items if item.get("human_confirmation_required")),
            }
        )
    return records


def build_dashboard() -> dict:
    registry = parse_registry(REGISTRY / "wiki-registry.yaml")
    queue = read_json(REGISTRY / "source-update-queue.json")
    playbook = read_json(REGISTRY / "source-refresh-playbook.json")
    tickets_data = read_json(REGISTRY / "source-refresh-tickets.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    quality = read_json(REGISTRY / "source-evidence-quality-audit.json")
    log_status = read_json(REGISTRY / "source-refresh-log-status.json")
    release = read_json(REGISTRY / "release-manifest.json")
    reviewer_queue = read_json(REGISTRY / "source-reviewer-queue.json")
    session_plan = read_json(REGISTRY / "source-review-session-plan.json")
    packet_bundle = read_json(REGISTRY / "source-review-packet-bundle.json")
    packet_audit = read_json(REGISTRY / "source-review-packet-audit.json")
    packet_rehearsal = read_json(REGISTRY / "source-review-packet-rehearsal.json")
    readiness_matrix = read_json(REGISTRY / "source-review-readiness-matrix.json")
    work_orders = read_json(REGISTRY / "source-review-work-orders.json")

    tickets = completion.get("tickets") or tickets_data.get("tickets", [])
    open_tickets = [ticket for ticket in tickets if not ticket.get("is_final")]
    dashboard = {
        "generated": date.today().isoformat(),
        "current_fact_ready": bool(completion.get("completion_ready_for_current_fact_use")),
        "release_ready_for_internal_use": bool(release.get("ready_for_internal_release")),
        "requires_source_update_for_current_facts": bool(queue.get("topics")),
        "reports": REPORT_PATHS,
        "source_refresh": {
            "topic_count": len(queue.get("topics", [])),
            "task_count": int(playbook.get("task_count", 0)),
            "ticket_count": int(tickets_data.get("ticket_count", 0)),
            "log_count": int(log_status.get("wiki_count", 0)),
            "completion": completion,
            "quality": quality,
            "reviewer_queue": reviewer_queue,
            "session_plan": session_plan,
            "packet_bundle": packet_bundle,
            "packet_audit": packet_audit,
            "packet_rehearsal": packet_rehearsal,
            "readiness_matrix": readiness_matrix,
            "work_orders": work_orders,
            "wave_counts": playbook.get("wave_counts", {}),
        },
        "priority_progress": priority_progress(tickets, registry),
        "wiki_progress": wiki_progress(tickets, registry),
        "wave_progress": wave_progress(tickets),
        "status_counts": completion.get("status_counts", {}),
        "top_open_tickets": sorted(
            open_tickets,
            key=lambda item: (-int(item.get("priority_score", 0)), item.get("wave", ""), item.get("wiki", ""), item.get("ticket_id", "")),
        )[:12],
    }
    dashboard["gates"] = gate_records(dashboard)
    dashboard["passed"] = all(gate["passed"] for gate in dashboard["gates"] if gate["gate"] not in NON_BLOCKING_GATES)
    return dashboard


def bool_word(value: bool) -> str:
    return "yes" if value else "no"


def markdown_report(data: dict) -> str:
    source = data["source_refresh"]
    completion = source["completion"]
    quality = source["quality"]
    lines = [
        "# Source Refresh Dashboard",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Summary",
        "",
        f"- Release ready for internal use: {bool_word(data['release_ready_for_internal_use'])}",
        f"- Current-fact ready: {bool_word(data['current_fact_ready'])}",
        f"- Requires source update for current facts: {bool_word(data['requires_source_update_for_current_facts'])}",
        f"- Source-update topics: {source['topic_count']}",
        f"- Source-refresh tasks: {source['task_count']}",
        f"- Source-refresh tickets: {source['ticket_count']}",
        f"- Source reviewer queue: {source['reviewer_queue'].get('open_ticket_count', 0)} open reviews, {source['reviewer_queue'].get('human_review_gate_count', 0)} human gates",
        f"- Source review session plan: {source['session_plan'].get('selected_review_count', 0)} selected reviews, {source['session_plan'].get('selected_human_review_gate_count', 0)} human gates",
        f"- Source review packet bundle: {source['packet_bundle'].get('selected_review_count', 0)} pending entries",
        f"- Source review packet audit: {source['packet_audit'].get('packet_count', 0)} packets, {source['packet_audit'].get('issue_count', 0)} issues",
        f"- Source review packet rehearsal: {source['packet_rehearsal'].get('passed_dry_run_count', 0)}/{source['packet_rehearsal'].get('dry_run_count', 0)} dry-runs passed",
        f"- Source review readiness matrix: {source['readiness_matrix'].get('ready_for_source_collection_count', 0)} ready, {source['readiness_matrix'].get('queued_not_in_current_session_count', 0)} queued",
        f"- Source review work orders: {source['work_orders'].get('work_order_count', 0)} work orders, {source['work_orders'].get('human_review_gate_count', 0)} human gates",
        f"- Open tickets: {completion.get('open_ticket_count', 0)}",
        f"- Verified tickets: {completion.get('verified_ticket_count', 0)}",
        f"- Evidence entries: {quality.get('entry_count', 0)}",
        f"- Evidence quality issues: {quality.get('issue_count', 0)}",
        "",
        "## Quick Links",
        "",
    ]
    for key, path in data["reports"].items():
        lines.append(f"- {key}: {doc_link(path)}")

    lines.extend(["", "## Readiness Gates", "", "| Gate | Result | Detail |", "| --- | --- | --- |"])
    for gate in data["gates"]:
        lines.append(f"| {gate['gate']} | {'PASS' if gate['passed'] else 'OPEN'} | {gate['detail']} |")

    lines.extend(["", "## Priority Progress", "", "| Priority | Tickets | Open | Finalized | Verified | Issues |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for item in data["priority_progress"]:
        lines.append(
            f"| {item['priority']} | {item['tickets']} | {item['open']} | "
            f"{item['finalized']} | {item['verified']} | {item['issues']} |"
        )

    lines.extend(["", "## Wave Progress", "", "| Wave | Tickets | Open | Finalized | Verified | Human Confirmation |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for item in data["wave_progress"]:
        lines.append(
            f"| {item['wave']} | {item['tickets']} | {item['open']} | "
            f"{item['finalized']} | {item['verified']} | {item['human_confirmation_required']} |"
        )

    lines.extend(["", "## Wiki Progress", "", "| Wiki | Priority | Risk | Freshness | Tickets | Open | Finalized | Verified | Human Confirmation | Issues |", "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for item in data["wiki_progress"]:
        lines.append(
            f"| {item['wiki']} | {item['priority']} | {item['risk_level']} | {item['freshness']} | "
            f"{item['tickets']} | {item['open']} | {item['finalized']} | {item['verified']} | "
            f"{item['human_confirmation_required']} | {item['issues']} |"
        )

    lines.extend(["", "## Top Open Tickets", ""])
    if data["top_open_tickets"]:
        lines.extend(["| Ticket | Wave | Wiki | Priority | Topic | Log |", "| --- | --- | --- | ---: | --- | --- |"])
        for ticket in data["top_open_tickets"]:
            log = ticket.get("log_path", "")
            lines.append(
                f"| {ticket.get('ticket_id')} | {ticket.get('wave')} | {ticket.get('wiki')} | "
                f"{ticket.get('priority_score')} | {ticket.get('topic')} | {doc_link(log) if log else '-'} |"
            )
    else:
        lines.append("No open tickets remain.")

    lines.extend(
        [
            "",
            "## Next Actions",
            "",
            "- Refresh wave-1 tickets first, especially high-risk finance, legal, health, security, airdrop, and operations topics.",
            "- Use `scripts/record_source_evidence.py` only after authoritative source evidence has been checked.",
            "- Keep `still-needs-source-update` when sources are missing, stale, conflicting, or outside scope.",
            "- Run completion and quality audits after recording evidence.",
            "- Do not write current facts into wiki pages until the relevant ticket has dated evidence.",
            "",
            "## Commands",
            "",
            "```bash",
            "python3 scripts/generate_source_refresh_dashboard.py",
            "python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run",
            "python3 scripts/audit_source_refresh_completion.py",
            "python3 scripts/audit_source_evidence_quality.py",
            "python3 scripts/run_acceptance.py",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    dashboard = build_dashboard()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(dashboard), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(
        "SOURCE REFRESH DASHBOARD GENERATED "
        f"({dashboard['source_refresh']['completion'].get('open_ticket_count', 0)} open, "
        f"{dashboard['source_refresh']['completion'].get('verified_ticket_count', 0)} verified)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
