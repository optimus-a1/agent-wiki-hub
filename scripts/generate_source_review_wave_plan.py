#!/usr/bin/env python3
"""Generate a planning-only source-review wave work-order plan."""
from __future__ import annotations

from argparse import ArgumentParser
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS = ROOT / "docs"

DEFAULT_DASHBOARD = REGISTRY / "source-refresh-dashboard.json"
DEFAULT_READINESS = REGISTRY / "source-review-readiness-matrix.json"
REVIEWER_QUEUE = REGISTRY / "source-reviewer-queue.json"
SOURCE_TICKETS = REGISTRY / "source-refresh-tickets.json"

REPORTS = {
    "source_refresh_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_refresh_dashboard_json": "registry/source-refresh-dashboard.json",
    "source_reviewer_queue": "registry/source-reviewer-queue.json",
    "source_refresh_tickets": "registry/source-refresh-tickets.json",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
}

RISK_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
WAVE_ORDER = {"wave-1": 0, "wave-2": 1, "wave-3": 2}

PREFLIGHT_CHECKLIST = [
    "Read root AGENTS.md and the target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.",
    "Confirm the ticket topic and scope before opening or recording any source.",
    "Use official, primary, dated sources whenever available.",
    "Record source title, publisher, URL or local reference, publication/update date, access date, confidence, and remaining uncertainty.",
    "Keep status pending or still-needs-source-update when evidence is missing, stale, conflicting, or out of scope.",
    "Do not write current facts into wiki pages from this plan.",
    "Do not record API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.",
]

SAFETY_BOUNDARY = [
    "This plan does not browse, verify, certify, or write current facts.",
    "All entries remain planning-only until authoritative evidence is recorded.",
    "High-risk tickets require named human confirmation before final status.",
    "Node operations tickets do not authorize production changes, wallet actions, live upgrades, firewall changes, or billing-sensitive operations.",
]


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


def safe_slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "source-review-wave-plan"


def wave_display(value: str) -> str:
    match = re.search(r"wave-(\d+)", value)
    if match:
        return f"Wave {match.group(1)}"
    return value


def wave_token(value: str) -> str:
    return safe_slug(value).upper().replace("-", "")


def wave_placement_reason(wave: str, review: dict, ticket: dict) -> str:
    if wave == "wave-1":
        return "Selected for the first active source-review wave because it is highest priority or blocks source-refresh readiness."
    if wave == "wave-2":
        return "Placed after wave-1 active packet handling so high-risk and P0/P1 follow-up topics can be prepared without blocking acceptance."
    if wave == "wave-3":
        return (
            "Placed in wave-3 because wave-1 active packet handling and wave-2 pending planning take precedence; "
            "this topic still needs authoritative evidence before any current-fact use."
        )
    return ticket.get("wave_placement_reason", review.get("wave_placement_reason", "Queued by source-refresh wave assignment."))


def wave_dependencies(wave: str) -> list[str]:
    base = [
        "current_fact_ready must remain false until evidence quality, completion, acceptance, and human gates pass.",
        "Planning-only packet artifacts must not be imported as verified evidence.",
    ]
    if wave == "wave-1":
        return base + ["Wave-1 active packet audit and dry-run rehearsal must pass before any real import."]
    if wave == "wave-2":
        return base + ["Wave-1 active packet state must remain acceptance-compatible before wave-2 evidence collection."]
    if wave == "wave-3":
        return base + [
            "Wave-1 active packet state must remain acceptance-compatible.",
            "Wave-2 planning and pending packet artifacts must remain non-blocking until real evidence is collected.",
        ]
    return base


def sort_key(item: dict) -> tuple:
    return (
        RISK_ORDER.get(str(item.get("risk_level", "")), 99),
        PRIORITY_ORDER.get(str(item.get("priority", "")), 99),
        -int(item.get("priority_score", 0) or 0),
        WAVE_ORDER.get(str(item.get("wave", "")), 99),
        str(item.get("wiki", "")),
        str(item.get("ticket_id", "")),
    )


def open_ticket_records(dashboard: dict, reviewer_by_ticket: dict[str, dict], readiness_by_ticket: dict[str, dict]) -> list[dict]:
    completion = dashboard.get("source_refresh", {}).get("completion", {})
    records = []
    for ticket in completion.get("tickets", []):
        if ticket.get("is_final"):
            continue
        ticket_id = str(ticket.get("ticket_id", ""))
        review = reviewer_by_ticket.get(ticket_id, {})
        readiness = readiness_by_ticket.get(ticket_id, {})
        records.append(
            {
                "ticket_id": ticket_id,
                "task_id": ticket.get("task_id", ""),
                "wiki": ticket.get("wiki", ""),
                "wave": ticket.get("wave", ""),
                "priority": review.get("priority", ""),
                "priority_score": int(ticket.get("priority_score", 0) or 0),
                "risk_level": ticket.get("risk_level", ""),
                "freshness": review.get("freshness", ticket.get("freshness_requirement", "")),
                "category": review.get("category", ticket.get("category", "")),
                "topic": ticket.get("topic", ""),
                "status": ticket.get("status", ""),
                "reviewer_role": review.get("reviewer_role", ""),
                "human_review_gate": bool(review.get("human_review_gate", ticket.get("human_confirmation_required", False))),
                "readiness_stage": readiness.get("readiness_stage", ""),
                "selected_for_current_session": bool(readiness.get("selected_for_current_session", False)),
                "evidence_log": review.get("evidence_log", ticket.get("log_path", "")),
                "source_notes": review.get("source_notes", f"wikis/{ticket.get('wiki', '')}/sources/source-notes.md"),
            }
        )
    return sorted(records, key=sort_key)


def packet_entry(card: dict) -> dict:
    return {
        "ticket_id": card.get("ticket_id", ""),
        "status": "pending",
        "source_title": "<source title>",
        "source_publisher": "<official publisher or authority>",
        "source_url_or_reference": "<URL or local reference>",
        "source_published_or_updated": "YYYY-MM-DD | unknown",
        "source_accessed_on": date.today().isoformat(),
        "verified_on": "",
        "evidence_summary": "<what the source supports and does not support>",
        "affected_pages": [],
        "confidence": "low",
        "remaining_uncertainty": "<remaining uncertainty>",
        "human_reviewer": "<reviewer>" if card.get("human_review_gate") else "",
        "follow_up": "Keep needs-source-update unless authoritative, dated, scoped evidence is recorded and reviewed.",
    }


def compact_review(card: dict, ticket: dict) -> dict:
    wave = card.get("wave", ticket.get("wave", ""))
    return {
        "review_id": card.get("review_id", ""),
        "ticket_id": card.get("ticket_id", ""),
        "task_id": card.get("task_id", ticket.get("task_id", "")),
        "wiki": card.get("wiki", ticket.get("wiki", "")),
        "priority": card.get("priority", ""),
        "wave": wave,
        "risk_level": card.get("risk_level", ticket.get("risk_level", "")),
        "freshness": card.get("freshness", ticket.get("freshness_requirement", "")),
        "category": card.get("category", ticket.get("category", "")),
        "topic": card.get("topic", ticket.get("topic", "")),
        "reviewer_role": card.get("reviewer_role", ""),
        "human_review_gate": bool(card.get("human_review_gate", ticket.get("human_confirmation_required", False))),
        "suggested_sources": card.get("suggested_sources", ticket.get("suggested_sources", [])),
        "required_reading": card.get("required_reading", ticket.get("required_reading", [])),
        "evidence_log": card.get("evidence_log", ticket.get("log_path", "")),
        "source_notes": card.get("source_notes", f"wikis/{ticket.get('wiki', '')}/sources/source-notes.md"),
        "dry_run_command": card.get("dry_run_command", f"python scripts/record_source_evidence.py --ticket-id {card.get('ticket_id', ticket.get('ticket_id', ''))} --status pending --dry-run"),
        "record_command_template": card.get("record_command_template", ""),
        "reason_for_wave_placement": wave_placement_reason(wave, card, ticket),
        "dependencies": wave_dependencies(wave),
    }


def work_order(card: dict, ticket: dict, rank: int) -> dict:
    review = compact_review(card, ticket)
    return {
        "work_order_id": f"{wave_token(review['wave'])}-WORKORDER-{review['ticket_id']}",
        "rank": rank,
        "plan_status": "planned-not-started",
        "no_current_fact_write": True,
        "source_collection_required": True,
        "human_confirmation_required": review["human_review_gate"],
        "review": review,
        "source_policy": ticket.get("source_policy", []),
        "verification_steps": ticket.get("verification_steps", []),
        "acceptance_criteria": ticket.get("acceptance_criteria", []),
        "packet_entry_template": packet_entry(review),
    }


def role_workload(work_orders: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for order in work_orders:
        grouped[order["review"]["reviewer_role"]].append(order)
    records = []
    for role in sorted(grouped):
        items = grouped[role]
        records.append(
            {
                "reviewer_role": role,
                "work_order_count": len(items),
                "high_risk_count": sum(1 for item in items if item["review"]["risk_level"] == "high"),
                "human_gate_count": sum(1 for item in items if item["human_confirmation_required"]),
                "tickets": [item["review"]["ticket_id"] for item in items],
                "wikis": dict(sorted(Counter(item["review"]["wiki"] for item in items).items())),
            }
        )
    return records


def build_plan(wave: str) -> dict:
    dashboard = read_json(DEFAULT_DASHBOARD)
    readiness = read_json(DEFAULT_READINESS)
    reviewer_queue = read_json(REVIEWER_QUEUE)
    source_tickets = read_json(SOURCE_TICKETS)

    reviewer_by_ticket = {card.get("ticket_id"): card for card in reviewer_queue.get("review_cards", []) if card.get("ticket_id")}
    readiness_by_ticket = {row.get("ticket_id"): row for row in readiness.get("rows", []) if row.get("ticket_id")}
    ticket_by_id = {ticket.get("ticket_id"): ticket for ticket in source_tickets.get("tickets", []) if ticket.get("ticket_id")}
    open_topics = open_ticket_records(dashboard, reviewer_by_ticket, readiness_by_ticket)
    selected_topics = [topic for topic in open_topics if topic.get("wave") == wave]

    selected_orders = []
    for rank, topic in enumerate(selected_topics, start=1):
        ticket = ticket_by_id.get(topic["ticket_id"], {})
        card = reviewer_by_ticket.get(topic["ticket_id"], {})
        selected_orders.append(work_order(card, ticket, rank))

    selected_reviews = [order["review"] for order in selected_orders]
    checks = [
        {
            "check": "required dashboard artifacts exist",
            "passed": DEFAULT_DASHBOARD.exists() and DEFAULT_READINESS.exists(),
            "detail": f"{rel(DEFAULT_DASHBOARD)}, {rel(DEFAULT_READINESS)}",
        },
        {
            "check": "open topics loaded",
            "passed": len(open_topics) == int(dashboard.get("source_refresh", {}).get("completion", {}).get("open_ticket_count", len(open_topics))),
            "detail": f"{len(open_topics)} open topics",
        },
        {
            "check": f"{wave} topics selected",
            "passed": bool(selected_orders),
            "detail": f"{len(selected_orders)} planned work orders",
        },
        {
            "check": "reviewer cards available for selected topics",
            "passed": all(order["review"]["reviewer_role"] for order in selected_orders),
            "detail": f"{sum(1 for order in selected_orders if order['review']['reviewer_role'])}/{len(selected_orders)} reviewer roles",
        },
        {
            "check": "current facts remain gated",
            "passed": not bool(dashboard.get("current_fact_ready")),
            "detail": "current_fact_ready=false; plan writes no current facts",
        },
    ]

    return {
        "generated": date.today().isoformat(),
        "session_id": f"source-review-session-{safe_slug(wave)}-{date.today().isoformat()}",
        "wave": wave,
        "purpose": "Plan source-review work orders for one source-refresh wave without browsing, verifying, importing, or writing current facts.",
        "passed": all(check["passed"] for check in checks),
        "current_fact_ready": bool(dashboard.get("current_fact_ready", False)),
        "no_current_fact_write": True,
        "selected_filters": {"wave": wave, "risk_priority_sort": "risk desc, priority asc, priority_score desc"},
        "open_topic_count": len(open_topics),
        "selected_review_count": len(selected_reviews),
        "selected_high_risk_count": sum(1 for review in selected_reviews if review["risk_level"] == "high"),
        "selected_human_review_gate_count": sum(1 for review in selected_reviews if review["human_review_gate"]),
        "open_topics": open_topics,
        "selected_reviews": selected_reviews,
        "planned_work_orders": selected_orders,
        "role_workload": role_workload(selected_orders),
        "risk_counts": dict(sorted(Counter(review["risk_level"] for review in selected_reviews).items())),
        "priority_counts": dict(sorted(Counter(review["priority"] for review in selected_reviews).items())),
        "wiki_counts": dict(sorted(Counter(review["wiki"] for review in selected_reviews).items())),
        "packet_template": {
            "packet_id": f"source-review-session-{safe_slug(wave)}-pending",
            "created_on": date.today().isoformat(),
            "created_by": "<human reviewer or source-refresh agent>",
            "dry_run_first": True,
            "entries": [packet_entry(review) for review in selected_reviews],
        },
        "preflight_checklist": PREFLIGHT_CHECKLIST,
        "safety_boundary": SAFETY_BOUNDARY,
        "next_commands": [
            f"python scripts/generate_source_review_wave_packet_bundle.py --plan registry/source-review-{safe_slug(wave)}-plan.json --stem source-review-session-{safe_slug(wave)}-pending",
            "python scripts/audit_source_review_packets.py",
            "python scripts/rehearse_source_review_packet_imports.py",
            "python scripts/audit_source_refresh_completion.py",
            "python scripts/audit_source_evidence_quality.py",
            "python scripts/run_acceptance.py",
        ],
        "reports": REPORTS,
        "checks": checks,
    }


def topic_table(topics: list[dict]) -> list[str]:
    rows = [
        "| Ticket | Wave | Wiki | Priority | Score | Risk | Human Gate | Status | Topic |",
        "| --- | --- | --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for topic in topics:
        rows.append(
            f"| `{topic['ticket_id']}` | {topic['wave']} | {repo_link('wikis/' + topic['wiki'], topic['wiki'])} | "
            f"{topic['priority'] or '-'} | {topic['priority_score']} | {topic['risk_level']} | "
            f"{bool_word(topic['human_review_gate'])} | {topic['status']} | {topic['topic']} |"
        )
    return rows


def markdown_report(data: dict) -> str:
    display = wave_display(data["wave"])
    lines = [
        f"# Source Review {display} Plan",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Inputs Read",
        "",
        f"- {repo_link('docs/SOURCE_REFRESH_DASHBOARD.md')}",
        f"- {repo_link('docs/SOURCE_REVIEW_READINESS_MATRIX.md')}",
        f"- {repo_link('registry/source-refresh-dashboard.json')}",
        "",
        "## Guardrails",
        "",
    ]
    lines.extend(f"- {item}" for item in data["safety_boundary"])
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Passed: {bool_word(data['passed'])}",
            f"- Current-fact ready: {bool_word(data['current_fact_ready'])}",
            f"- Current facts written by this plan: no",
            f"- Remaining open topics: {data['open_topic_count']}",
            f"- Selected wave: {data['wave']}",
            f"- Planned work orders: {data['selected_review_count']}",
            f"- High-risk work orders: {data['selected_high_risk_count']}",
            f"- Human confirmation gates: {data['selected_human_review_gate_count']}",
            "",
            "## Remaining Open Source Update Topics",
            "",
        ]
    )
    lines.extend(topic_table(data["open_topics"]))
    lines.extend(
        [
            "",
            f"## {display} Work Order Plan",
            "",
            "Sorted by risk first, then wiki priority and priority score. These are planning records only.",
            "",
            "| Rank | Work Order | Ticket | Wiki | Priority | Score | Risk | Reviewer | Human Gate | Topic |",
            "| ---: | --- | --- | --- | --- | ---: | --- | --- | --- | --- |",
        ]
    )
    for order in data["planned_work_orders"]:
        review = order["review"]
        lines.append(
            f"| {order['rank']} | `{order['work_order_id']}` | `{review['ticket_id']}` | "
            f"{repo_link('wikis/' + review['wiki'], review['wiki'])} | {review['priority']} | "
            f"{next((topic['priority_score'] for topic in data['open_topics'] if topic['ticket_id'] == review['ticket_id']), 0)} | "
            f"{review['risk_level']} | `{review['reviewer_role']}` | {bool_word(order['human_confirmation_required'])} | {review['topic']} |"
        )

    lines.extend(["", "## Reviewer Workload", "", "| Reviewer Role | Work Orders | High Risk | Human Gates | Tickets |", "| --- | ---: | ---: | ---: | --- |"])
    for workload in data["role_workload"]:
        lines.append(
            f"| `{workload['reviewer_role']}` | {workload['work_order_count']} | {workload['high_risk_count']} | "
            f"{workload['human_gate_count']} | {', '.join('`' + ticket + '`' for ticket in workload['tickets'])} |"
        )

    lines.extend(["", "## Preflight Checklist", ""])
    lines.extend(f"- [ ] {item}" for item in data["preflight_checklist"])

    lines.extend(["", "## Per-Ticket Source Targets", ""])
    for order in data["planned_work_orders"]:
        review = order["review"]
        source_targets = ", ".join(review.get("suggested_sources", [])) or "-"
        lines.extend(
            [
                f"### {order['rank']}. {review['ticket_id']} - {review['wiki']}",
                "",
                f"- Risk: {review['risk_level']}",
                f"- Reviewer role: `{review['reviewer_role']}`",
                f"- Human confirmation: {bool_word(order['human_confirmation_required'])}",
                f"- Topic: {review['topic']}",
                f"- Reason for wave placement: {review['reason_for_wave_placement']}",
                f"- Dependencies: {'; '.join(review.get('dependencies', []))}",
                f"- Suggested source types: {source_targets}",
                f"- Source notes: {repo_link(review['source_notes'])}",
                f"- Evidence log: {repo_link(review['evidence_log'])}",
                f"- Dry run: `{review['dry_run_command']}`",
                "",
            ]
        )

    lines.extend(["## Packet Skeleton", "", "This is placeholder-only. Replace every placeholder before any real import.", "", "```json"])
    packet_preview = dict(data["packet_template"])
    packet_preview["entries"] = packet_preview["entries"][:3]
    packet_preview["truncated_entries"] = max(data["selected_review_count"] - 3, 0)
    lines.append(json.dumps(packet_preview, ensure_ascii=False, indent=2))
    lines.extend(["```", ""])

    lines.extend(["## Next Commands", "", "```bash"])
    lines.extend(data["next_commands"])
    lines.extend(["```", "", "## Related Reports", ""])
    for name, path in data["reports"].items():
        lines.append(f"- {name}: {repo_link(path)}")

    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        lines.append(f"| {check['check']} | {'PASS' if check['passed'] else 'FAIL'} | {check['detail']} |")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = ArgumentParser(description="Generate a planning-only source-review wave work-order plan.")
    parser.add_argument("--wave", default="wave-2", choices=["wave-1", "wave-2", "wave-3"], help="Source refresh wave to plan.")
    parser.add_argument("--json", action="store_true", help="Print plan JSON after writing outputs.")
    args = parser.parse_args()

    data = build_plan(args.wave)
    stem = f"source-review-{safe_slug(args.wave)}-plan"
    docs_out = DOCS / f"{stem.upper().replace('-', '_')}.md"
    json_out = REGISTRY / f"{stem}.json"
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    docs_out.write_text(markdown_report(data), encoding="utf-8")
    json_out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"Wrote {docs_out.relative_to(ROOT)}")
        print(f"Wrote {json_out.relative_to(ROOT)}")
        print(
            f"SOURCE REVIEW {args.wave.upper()} PLAN GENERATED "
            f"({data['selected_review_count']} work orders, {data['selected_human_review_gate_count']} human gates)"
        )
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
