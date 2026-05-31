#!/usr/bin/env python3
"""Generate per-ticket source review work orders without verifying facts."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
WORK_ORDER_DIR = REGISTRY / "source-review-work-orders"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_WORK_ORDERS.md"
JSON_OUT = REGISTRY / "source-review-work-orders.json"
MANIFEST_OUT = WORK_ORDER_DIR / "manifest.json"

REPORTS = {
    "source_refresh_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "source_review_packet_audit": "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "source_review_packet_rehearsal": "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "source_review_session_plan": "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "source_reviewer_queue": "docs/SOURCE_REVIEWER_QUEUE.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
}

REQUIRED_LOCAL_ARTIFACTS = [
    "registry/source-review-readiness-matrix.json",
    "registry/source-reviewer-queue.json",
    "registry/source-review-session-plan.json",
    "registry/source-review-packet-bundle.json",
]

WORK_ORDER_CHECKLIST = [
    "Read root AGENTS.md, target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.",
    "Collect only authoritative, dated, scoped evidence for the exact ticket topic.",
    "Prefer official primary sources; do not use secondary summaries as the only authority.",
    "Record source title, publisher, URL or local reference, publication/update date, access date, confidence, and uncertainty.",
    "Keep status pending or still-needs-source-update when evidence is missing, stale, conflicting, or out of scope.",
    "Replace every placeholder before any non-dry-run packet import.",
    "Do not record API keys, private keys, cookies, seed phrases, credentials, bearer tokens, or private account data.",
    "Do not write current facts into wiki pages until evidence logs, quality audit, completion audit, acceptance, and package checks pass.",
]

HUMAN_GATE_CHECKLIST = [
    "Name a human reviewer before marking this ticket verified or unchanged.",
    "Keep the relevant high-risk boundary visible in the evidence summary.",
    "Do not use this work order as permission for autonomous finance, legal, medical, security, Web3, or production operations.",
]

COMMANDS = [
    "python3 scripts/audit_source_review_packets.py",
    "python3 scripts/rehearse_source_review_packet_imports.py",
    "python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks",
    "python3 scripts/audit_source_refresh_completion.py",
    "python3 scripts/audit_source_evidence_quality.py",
    "python3 scripts/generate_source_review_readiness_matrix.py",
    "python3 scripts/generate_source_review_work_orders.py",
    "python3 scripts/generate_source_refresh_dashboard.py",
    "python3 scripts/run_acceptance.py",
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


def safe_filename(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "source-review-work-order"


def ticket_sort_key(row: dict) -> tuple:
    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    wave_order = {"wave-1": 0, "wave-2": 1, "wave-3": 2}
    return (
        priority_order.get(row.get("priority", ""), 99),
        wave_order.get(row.get("wave", ""), 99),
        row.get("wiki", ""),
        row.get("ticket_id", ""),
    )


def packet_entries(bundle: dict) -> dict[str, dict]:
    packet_path = bundle.get("packet_json")
    if not packet_path:
        return {}
    data = read_json(ROOT / str(packet_path))
    entries = data.get("entries", []) if isinstance(data, dict) else []
    return {entry.get("ticket_id", ""): entry for entry in entries if entry.get("ticket_id")}


def packet_template_fallback(ticket_id: str, human_gate: bool) -> dict:
    return {
        "ticket_id": ticket_id,
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
        "human_reviewer": "<reviewer>" if human_gate else "",
        "follow_up": "Keep needs-source-update unless evidence is authoritative, dated, scoped, and reviewed.",
    }


def work_order_record(row: dict, review: dict, entry: dict, bundle: dict) -> dict:
    ticket_id = row.get("ticket_id", "")
    work_order_id = f"WORKORDER-{ticket_id}"
    path = WORK_ORDER_DIR / f"{safe_filename(ticket_id)}.md"
    dry_run_commands = list(bundle.get("dry_run_import_commands", []))
    if review.get("dry_run_command"):
        dry_run_commands.insert(0, review["dry_run_command"])
    return {
        "work_order_id": work_order_id,
        "ticket_id": ticket_id,
        "task_id": row.get("task_id", ""),
        "wiki": row.get("wiki", ""),
        "priority": row.get("priority", ""),
        "wave": row.get("wave", ""),
        "risk_level": row.get("risk_level", ""),
        "freshness": row.get("freshness", ""),
        "category": row.get("category", ""),
        "topic": row.get("topic", ""),
        "readiness_stage": row.get("readiness_stage", ""),
        "reviewer_role": row.get("reviewer_role") or review.get("reviewer_role", ""),
        "human_review_gate": bool(row.get("human_review_gate", review.get("human_review_gate", False))),
        "source_notes": row.get("source_notes") or review.get("source_notes", ""),
        "evidence_log": row.get("evidence_log") or review.get("evidence_log", ""),
        "required_reading": review.get("required_reading", []),
        "suggested_sources": review.get("suggested_sources", []),
        "review_checklist": review.get("review_checklist", []),
        "packet_json": bundle.get("packet_json", ""),
        "packet_jsonl": bundle.get("packet_jsonl", ""),
        "packet_checklist": bundle.get("checklist", ""),
        "packet_entry_template": entry or packet_template_fallback(ticket_id, bool(row.get("human_review_gate"))),
        "dry_run_commands": dry_run_commands,
        "record_command_template": review.get("record_command_template", ""),
        "work_order_path": rel(path),
    }


def markdown_list(items: list[str]) -> list[str]:
    return [f"- `{item}`" if item.startswith(("wikis/", "docs/", "registry/", "scripts/", "AGENTS.md")) else f"- {item}" for item in items] or ["- -"]


def work_order_markdown(order: dict) -> str:
    checklist = list(WORK_ORDER_CHECKLIST)
    if order["human_review_gate"]:
        checklist.extend(HUMAN_GATE_CHECKLIST)
    if order.get("review_checklist"):
        checklist.extend(item for item in order["review_checklist"] if item not in checklist)

    lines = [
        f"# Source Review Work Order: {order['ticket_id']}",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Scope",
        "",
        f"- Work order: `{order['work_order_id']}`",
        f"- Ticket: `{order['ticket_id']}`",
        f"- Task: `{order['task_id']}`",
        f"- Wiki: `{order['wiki']}`",
        f"- Priority: `{order['priority']}`",
        f"- Wave: `{order['wave']}`",
        f"- Risk: `{order['risk_level']}`",
        f"- Freshness: `{order['freshness']}`",
        f"- Category: `{order['category']}`",
        f"- Readiness stage: `{order['readiness_stage']}`",
        f"- Reviewer role: `{order['reviewer_role']}`",
        f"- Human review gate: {bool_word(order['human_review_gate'])}",
        f"- Topic: {order['topic']}",
        "",
        "## Required Reading",
        "",
        *markdown_list(order["required_reading"]),
        "",
        "## Source Targets",
        "",
        *markdown_list(order["suggested_sources"]),
        "",
        "## Local Artifacts",
        "",
        f"- Source notes: `{order['source_notes']}`",
        f"- Evidence log: `{order['evidence_log']}`",
        f"- Packet JSON: `{order['packet_json']}`",
        f"- Packet JSONL: `{order['packet_jsonl']}`",
        f"- Packet checklist: `{order['packet_checklist']}`",
        "",
        "## Evidence Fields To Fill",
        "",
        "Replace every placeholder before any real import. Leave `status` as `pending` until source evidence has actually been reviewed.",
        "",
        "```json",
        json.dumps(order["packet_entry_template"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## Collection Checklist",
        "",
    ]
    lines.extend(f"- [ ] {item}" for item in checklist)
    lines.extend(["", "## Commands", "", "Run only dry-run imports until every placeholder is replaced.", "", "```bash"])
    lines.extend(order["dry_run_commands"])
    if order["record_command_template"]:
        lines.append(order["record_command_template"])
    lines.extend(
        [
            "```",
            "",
            "## Safety Boundary",
            "",
            "- This work order is an offline collection aid; it does not verify or certify current facts.",
            "- It does not authorize real-money trading, final legal or medical advice, offensive security activity, wallet signing, or production changes.",
            "- Keep `needs-source-update` in the wiki until authoritative source evidence is recorded and audits pass.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_work_orders() -> dict:
    readiness = read_json(REGISTRY / "source-review-readiness-matrix.json")
    reviewer_queue = read_json(REGISTRY / "source-reviewer-queue.json")
    session_plan = read_json(REGISTRY / "source-review-session-plan.json")
    packet_bundle = read_json(REGISTRY / "source-review-packet-bundle.json")
    packet_map = packet_entries(packet_bundle)

    review_by_ticket = {card.get("ticket_id"): card for card in reviewer_queue.get("review_cards", []) if card.get("ticket_id")}
    selected_by_ticket = {review.get("ticket_id"): review for review in session_plan.get("selected_reviews", []) if review.get("ticket_id")}
    ready_rows = sorted(
        [row for row in readiness.get("rows", []) if row.get("readiness_stage") == "ready-for-source-collection"],
        key=ticket_sort_key,
    )
    selected_rows = [row for row in readiness.get("rows", []) if row.get("selected_for_current_session")]
    selected_finalized_count = sum(1 for row in selected_rows if row.get("finalized"))
    selected_verified_count = sum(1 for row in selected_rows if row.get("verified"))
    post_import_completed = bool(readiness.get("post_import_completed")) or (
        bool(selected_rows) and selected_finalized_count == len(selected_rows)
    )

    work_orders = []
    for row in ready_rows:
        ticket_id = row.get("ticket_id", "")
        review = dict(review_by_ticket.get(ticket_id, {}))
        review.update(selected_by_ticket.get(ticket_id, {}))
        entry = packet_map.get(ticket_id) or packet_template_fallback(ticket_id, bool(row.get("human_review_gate")))
        work_orders.append(work_order_record(row, review, entry, packet_bundle))

    WORK_ORDER_DIR.mkdir(parents=True, exist_ok=True)
    for order in work_orders:
        (ROOT / order["work_order_path"]).write_text(work_order_markdown(order), encoding="utf-8")

    manifest = {
        "generated": date.today().isoformat(),
        "passed": True,
        "work_order_count": len(work_orders),
        "human_review_gate_count": sum(1 for order in work_orders if order["human_review_gate"]),
        "work_order_paths": [order["work_order_path"] for order in work_orders],
    }
    MANIFEST_OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    missing_required = [path for path in REQUIRED_LOCAL_ARTIFACTS if not (ROOT / path).exists()]
    checks = [
        {
            "check": "required local review artifacts exist",
            "passed": not missing_required,
            "detail": ", ".join(missing_required) if missing_required else "all required artifacts present",
        },
        {
            "check": "readiness matrix passed",
            "passed": bool(readiness.get("passed")),
            "detail": f"{readiness.get('ready_for_source_collection_count', 0)} ready rows",
        },
        {
            "check": "ready tickets have reviewer cards",
            "passed": all((order["ticket_id"] in review_by_ticket) for order in work_orders),
            "detail": f"{sum(1 for order in work_orders if order['ticket_id'] in review_by_ticket)}/{len(work_orders)} work orders",
        },
        {
            "check": "ready tickets have packet entries",
            "passed": all((order["ticket_id"] in packet_map) for order in work_orders),
            "detail": f"{sum(1 for order in work_orders if order['ticket_id'] in packet_map)}/{len(work_orders)} work orders",
        },
        {
            "check": "work order files written",
            "passed": all((ROOT / order["work_order_path"]).exists() for order in work_orders) and MANIFEST_OUT.exists(),
            "detail": f"{len(work_orders)} work order files plus manifest",
        },
        {
            "check": "human gates preserved",
            "passed": post_import_completed
            or sum(1 for order in work_orders if order["human_review_gate"]) == int(session_plan.get("selected_human_review_gate_count", sum(1 for order in work_orders if order["human_review_gate"]))),
            "detail": "selected tickets already finalized; no new work orders required"
            if post_import_completed and not work_orders
            else f"{sum(1 for order in work_orders if order['human_review_gate'])} human-gated work orders",
        },
        {
            "check": "current facts remain gated",
            "passed": not bool(readiness.get("current_fact_ready", False)),
            "detail": "current_fact_ready=false while source tickets remain open",
        },
    ]

    manifest["passed"] = all(check["passed"] for check in checks)
    MANIFEST_OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "purpose": "Convert ready source-review tickets into offline work orders for human or connected source reviewers without fetching or certifying facts.",
        "current_fact_ready": bool(readiness.get("current_fact_ready", False)),
        "ticket_count": int(readiness.get("ticket_count", 0)),
        "ready_for_source_collection_count": int(readiness.get("ready_for_source_collection_count", len(work_orders))),
        "selected_finalized_count": selected_finalized_count,
        "selected_verified_count": selected_verified_count,
        "post_import_completed": post_import_completed,
        "source_review_phase": "post-import-completed" if post_import_completed else "pre-import-or-in-progress",
        "work_order_count": len(work_orders),
        "human_review_gate_count": sum(1 for order in work_orders if order["human_review_gate"]),
        "wiki_counts": dict(sorted(Counter(order["wiki"] for order in work_orders).items())),
        "role_counts": dict(sorted(Counter(order["reviewer_role"] for order in work_orders).items())),
        "priority_counts": dict(sorted(Counter(order["priority"] for order in work_orders).items())),
        "wave_counts": dict(sorted(Counter(order["wave"] for order in work_orders).items())),
        "work_order_dir": rel(WORK_ORDER_DIR),
        "manifest": rel(MANIFEST_OUT),
        "reports": REPORTS,
        "commands": COMMANDS,
        "work_orders": work_orders,
        "checks": checks,
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Work Orders",
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
        f"- Source-review tickets: {data['ticket_count']}",
        f"- Ready for source collection: {data['ready_for_source_collection_count']}",
        f"- Selected finalized tickets: {data['selected_finalized_count']}",
        f"- Selected verified tickets: {data['selected_verified_count']}",
        f"- Source review phase: {data['source_review_phase']}",
        f"- Work orders: {data['work_order_count']}",
        f"- Human review gates: {data['human_review_gate_count']}",
        f"- Work order directory: {repo_link(data['work_order_dir'])}",
        f"- Work order manifest: {repo_link(data['manifest'])}",
        "",
        "## Work Orders",
        "",
        "| Work Order | Ticket | Wiki | Priority | Wave | Risk | Human Gate | Reviewer Role | Topic |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for order in data["work_orders"]:
        lines.append(
            f"| {repo_link(order['work_order_path'], order['work_order_id'])} | `{order['ticket_id']}` | "
            f"{repo_link('wikis/' + order['wiki'], order['wiki'])} | {order['priority']} | {order['wave']} | "
            f"{order['risk_level']} | {bool_word(order['human_review_gate'])} | {order['reviewer_role']} | {order['topic']} |"
        )

    lines.extend(["", "## Wiki Counts", ""])
    for wiki, count in data["wiki_counts"].items():
        lines.append(f"- {wiki}: {count}")

    lines.extend(["", "## Reviewer Role Counts", ""])
    for role, count in data["role_counts"].items():
        lines.append(f"- {role}: {count}")

    lines.extend(["", "## Commands", "", "```bash"])
    lines.extend(data["commands"])
    lines.extend(["```", "", "## Related Reports", ""])
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
            "- Work orders are collection templates only; they do not fetch, verify, or certify external facts.",
            "- Zero work orders is acceptable when the selected review tickets are already finalized after evidence import.",
            "- Keep current facts gated until evidence is recorded, human gates are satisfied, and audits pass.",
            "- Do not use these files to store secrets, credentials, cookies, private keys, seed phrases, or private account data.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_work_orders()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"Wrote {MANIFEST_OUT.relative_to(ROOT)}")
    print(
        "SOURCE REVIEW WORK ORDERS "
        f"{'GENERATED' if data['passed'] else 'HAS BLOCKERS'} "
        f"({data['work_order_count']} work orders, {data['human_review_gate_count']} human gates)"
    )
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
