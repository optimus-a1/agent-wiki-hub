#!/usr/bin/env python3
"""Generate source-refresh execution waves without verifying external facts."""
from __future__ import annotations

from argparse import ArgumentParser
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS_OUT = ROOT / "docs" / "SOURCE_REFRESH_WAVE_RUNNER.md"
JSON_OUT = REGISTRY / "source-refresh-wave-runner.json"

WAVE_ORDER = {"wave-1": 0, "wave-2": 1, "wave-3": 2}
PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}

SESSION_CHECKLIST = [
    "Read root AGENTS.md and the target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.",
    "Confirm the ticket topic and scope before collecting sources.",
    "Prefer official, primary, dated sources and record publication/update date plus access date.",
    "Do not use unsourced summaries as the only authority.",
    "Keep high-risk topics behind human confirmation before marking verified.",
    "Record remaining uncertainty when sources are stale, conflicting, missing, or out of scope.",
    "Do not record credentials, API keys, cookies, private keys, seed phrases, or private account data.",
]

POST_COMMANDS = [
    "python3 scripts/audit_source_refresh_completion.py",
    "python3 scripts/audit_source_evidence_quality.py",
    "python3 scripts/generate_source_refresh_wave_runner.py",
    "python3 scripts/generate_source_reviewer_queue.py",
    "python3 scripts/generate_source_review_session_plan.py",
    "python3 scripts/generate_source_review_packet_bundle.py",
    "python3 scripts/audit_source_review_packets.py",
    "python3 scripts/rehearse_source_review_packet_imports.py",
    "python3 scripts/generate_source_review_readiness_matrix.py",
    "python3 scripts/generate_source_review_work_orders.py",
    "python3 scripts/generate_source_refresh_dashboard.py",
    "python3 scripts/update_index.py",
    "python3 scripts/run_acceptance.py",
]


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


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
                current[key.strip()] = value.strip().strip('"')
            if current.get("id"):
                records[str(current["id"])] = current
            continue
        if raw.startswith("    ") and current is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current[key.strip()] = value.strip().strip('"')
            if current.get("id"):
                records[str(current["id"])] = current
    return records


def repo_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def ticket_status(ticket: dict) -> str:
    return str(ticket.get("status") or "open_pending_source_refresh")


def is_open(ticket: dict) -> bool:
    status = ticket_status(ticket)
    return status not in FINAL_STATUSES and not bool(ticket.get("is_final"))


def enrich_tickets(tickets: list[dict], registry: dict[str, dict]) -> list[dict]:
    records: list[dict] = []
    for ticket in tickets:
        wiki = ticket.get("wiki", "")
        meta = registry.get(wiki, {})
        record = dict(ticket)
        record["priority"] = meta.get("priority", "unknown")
        record["registry_risk_level"] = meta.get("risk_level", ticket.get("risk_level", ""))
        record["freshness"] = meta.get("freshness", ticket.get("freshness_requirement", ""))
        record["open"] = is_open(record)
        records.append(record)
    return records


def sort_key(ticket: dict) -> tuple:
    return (
        WAVE_ORDER.get(ticket.get("wave", ""), 99),
        PRIORITY_ORDER.get(ticket.get("priority", ""), 99),
        -int(ticket.get("priority_score", 0) or 0),
        ticket.get("wiki", ""),
        ticket.get("ticket_id", ""),
    )


def filtered_tickets(tickets: list[dict], wave: str | None, priority: str | None, wiki: str | None, ticket_id: str | None) -> list[dict]:
    rows = [ticket for ticket in tickets if ticket.get("open")]
    if wave:
        rows = [ticket for ticket in rows if ticket.get("wave") == wave]
    if priority:
        rows = [ticket for ticket in rows if ticket.get("priority") == priority]
    if wiki:
        rows = [ticket for ticket in rows if ticket.get("wiki") == wiki]
    if ticket_id:
        rows = [ticket for ticket in rows if ticket.get("ticket_id") == ticket_id or ticket.get("task_id") == ticket_id]
    return sorted(rows, key=sort_key)


def evidence_dry_run_command(ticket: dict) -> str:
    return f"python3 scripts/record_source_evidence.py --ticket-id {ticket.get('ticket_id')} --status pending --dry-run"


def evidence_record_command(ticket: dict) -> str:
    command = (
        "python3 scripts/record_source_evidence.py "
        f"--ticket-id {ticket.get('ticket_id')} "
        "--status still-needs-source-update "
        "--source-title \"<source title>\" "
        "--source-publisher \"<publisher>\" "
        "--source-url-or-reference \"<url or local reference>\" "
        "--source-published-or-updated \"YYYY-MM-DD | unknown\" "
        "--evidence-summary \"<what the source supports and does not support>\" "
        "--confidence low "
        "--remaining-uncertainty \"<remaining uncertainty>\""
    )
    if ticket.get("human_confirmation_required"):
        command += " --human-reviewer \"<reviewer>\""
    return command


def merged_ticket_source(ticket_data: dict, completion: dict) -> list[dict]:
    generated = ticket_data.get("tickets", [])
    status_by_id = {
        ticket.get("ticket_id"): ticket
        for ticket in completion.get("tickets", [])
        if ticket.get("ticket_id")
    }
    if not generated:
        return completion.get("tickets", [])
    merged: list[dict] = []
    status_fields = {
        "status",
        "log_path",
        "log_exists",
        "task_present_in_log",
        "has_completed_evidence",
        "is_final",
        "is_verified",
        "issues",
        "passed",
    }
    for ticket in generated:
        record = dict(ticket)
        status = status_by_id.get(ticket.get("ticket_id"), {})
        for field in status_fields:
            if field in status:
                record[field] = status[field]
        merged.append(record)
    return merged


def ticket_runner_card(ticket: dict) -> dict:
    return {
        "ticket_id": ticket.get("ticket_id", ""),
        "task_id": ticket.get("task_id", ""),
        "wiki": ticket.get("wiki", ""),
        "priority": ticket.get("priority", ""),
        "wave": ticket.get("wave", ""),
        "risk_level": ticket.get("risk_level", ticket.get("registry_risk_level", "")),
        "freshness": ticket.get("freshness", ""),
        "category": ticket.get("category", ""),
        "topic": ticket.get("topic", ""),
        "status": ticket_status(ticket),
        "priority_score": int(ticket.get("priority_score", 0) or 0),
        "human_confirmation_required": bool(ticket.get("human_confirmation_required", False)),
        "suggested_sources": ticket.get("suggested_sources", []),
        "required_reading": ticket.get("required_reading", []),
        "log_path": ticket.get("log_path") or f"wikis/{ticket.get('wiki')}/sources/source-refresh-log.md",
        "source_notes_path": f"wikis/{ticket.get('wiki')}/sources/source-notes.md",
        "dry_run_command": evidence_dry_run_command(ticket),
        "record_command_template": evidence_record_command(ticket),
        "human_review_gate": bool(ticket.get("human_confirmation_required", False))
        or ticket.get("risk_level") == "high"
        or ticket.get("registry_risk_level") == "high",
    }


def batch_record(batch_id: str, title: str, tickets: list[dict], description: str) -> dict:
    cards = [ticket_runner_card(ticket) for ticket in sorted(tickets, key=sort_key)]
    return {
        "batch_id": batch_id,
        "title": title,
        "description": description,
        "ticket_count": len(cards),
        "human_confirmation_count": sum(1 for card in cards if card["human_review_gate"]),
        "wikis": dict(sorted(Counter(card["wiki"] for card in cards).items())),
        "tickets": cards,
    }


def build_batches(open_tickets: list[dict]) -> list[dict]:
    batches: list[dict] = []
    for wave in ["wave-1", "wave-2", "wave-3"]:
        rows = [ticket for ticket in open_tickets if ticket.get("wave") == wave]
        if rows:
            batches.append(
                batch_record(
                    f"batch-{wave}",
                    f"{wave} refresh batch",
                    rows,
                    "Execute these tickets in wave order; keep current facts gated until evidence is recorded.",
                )
            )
    for priority in ["P0", "P1", "P2"]:
        rows = [ticket for ticket in open_tickets if ticket.get("priority") == priority]
        if rows:
            batches.append(
                batch_record(
                    f"batch-{priority.lower()}",
                    f"{priority} priority batch",
                    rows,
                    "Use this view when the next source-refresh session is organized by wiki priority.",
                )
            )
    human_rows = [
        ticket
        for ticket in open_tickets
        if ticket.get("human_confirmation_required")
        or ticket.get("risk_level") == "high"
        or ticket.get("registry_risk_level") == "high"
    ]
    if human_rows:
        batches.append(
            batch_record(
                "batch-human-confirmation",
                "Human confirmation batch",
                human_rows,
                "These tickets need explicit human review before any verified/current-fact use.",
            )
        )
    return batches


def build_runner(wave: str | None = None, priority: str | None = None, wiki: str | None = None, ticket_id: str | None = None, limit: int | None = None) -> dict:
    registry = parse_registry(REGISTRY / "wiki-registry.yaml")
    ticket_data = read_json(REGISTRY / "source-refresh-tickets.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    quality = read_json(REGISTRY / "source-evidence-quality-audit.json")
    dashboard = read_json(REGISTRY / "source-refresh-dashboard.json")
    source = merged_ticket_source(ticket_data, completion)
    tickets = enrich_tickets(source, registry)
    open_tickets = sorted([ticket for ticket in tickets if ticket.get("open")], key=sort_key)
    selection = filtered_tickets(tickets, wave, priority, wiki, ticket_id)
    if limit is not None:
        selection = selection[:limit]

    missing_required = []
    for path in [
        "registry/wiki-registry.yaml",
        "registry/source-refresh-tickets.json",
        "registry/source-refresh-completion-audit.json",
        "registry/source-evidence-quality-audit.json",
    ]:
        if not (ROOT / path).exists():
            missing_required.append(path)

    return {
        "generated": date.today().isoformat(),
        "passed": not missing_required,
        "missing_required": missing_required,
        "purpose": "Plan source-refresh execution waves without certifying current facts.",
        "current_fact_ready": bool(dashboard.get("current_fact_ready", completion.get("completion_ready_for_current_fact_use", False))),
        "ticket_count": len(tickets),
        "open_ticket_count": len(open_tickets),
        "verified_ticket_count": int(completion.get("verified_ticket_count", 0)),
        "finalized_ticket_count": int(completion.get("finalized_ticket_count", 0)),
        "evidence_entry_count": int(quality.get("entry_count", 0)),
        "evidence_issue_count": int(quality.get("issue_count", 0)),
        "wave_counts": dict(sorted(Counter(ticket.get("wave", "unknown") for ticket in open_tickets).items())),
        "priority_counts": dict(sorted(Counter(ticket.get("priority", "unknown") for ticket in open_tickets).items())),
        "wiki_counts": dict(sorted(Counter(ticket.get("wiki", "unknown") for ticket in open_tickets).items())),
        "recommended_queue": [ticket_runner_card(ticket) for ticket in open_tickets],
        "selected_queue": [ticket_runner_card(ticket) for ticket in selection],
        "selected_filters": {
            "wave": wave,
            "priority": priority,
            "wiki": wiki,
            "ticket_id": ticket_id,
            "limit": limit,
        },
        "batches": build_batches(open_tickets),
        "session_checklist": SESSION_CHECKLIST,
        "post_commands": POST_COMMANDS,
    }


def short_table_rows(cards: list[dict]) -> list[str]:
    if not cards:
        return ["| - | - | - | - | - | - | - |"]
    rows = []
    for card in cards:
        human = "yes" if card["human_review_gate"] else "no"
        rows.append(
            f"| `{card['ticket_id']}` | {repo_link('wikis/' + card['wiki'], card['wiki'])} | "
            f"{card['priority']} | {card['wave']} | {card['risk_level']} | {human} | {card['topic']} |"
        )
    return rows


def markdown_report(data: dict) -> str:
    selected = data["selected_queue"]
    queue_preview = data["recommended_queue"][:20]
    current_ready = "yes" if data["current_fact_ready"] else "no"
    lines = [
        "# Source Refresh Wave Runner",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Current State",
        "",
        f"- Current-fact ready: {current_ready}",
        f"- Tickets: {data['ticket_count']}",
        f"- Open tickets: {data['open_ticket_count']}",
        f"- Verified tickets: {data['verified_ticket_count']}",
        f"- Finalized tickets: {data['finalized_ticket_count']}",
        f"- Evidence entries: {data['evidence_entry_count']}",
        f"- Evidence issues: {data['evidence_issue_count']}",
        "",
        "## Session Checklist",
        "",
    ]
    lines.extend(f"- [ ] {item}" for item in data["session_checklist"])

    lines.extend(
        [
            "",
            "## Recommended Queue Preview",
            "",
            "| Ticket | Wiki | Priority | Wave | Risk | Human Review | Topic |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *short_table_rows(queue_preview),
        ]
    )
    if len(data["recommended_queue"]) > len(queue_preview):
        lines.append(f"| +{len(data['recommended_queue']) - len(queue_preview)} more | - | - | - | - | - | - |")

    lines.extend(["", "## Batch Views", ""])
    for batch in data["batches"]:
        lines.extend(
            [
                f"### {batch['batch_id']}",
                "",
                f"- Title: {batch['title']}",
                f"- Tickets: {batch['ticket_count']}",
                f"- Human confirmation gates: {batch['human_confirmation_count']}",
                f"- Description: {batch['description']}",
                "",
                "| Ticket | Wiki | Priority | Wave | Risk | Human Review | Topic |",
                "| --- | --- | --- | --- | --- | --- | --- |",
                *short_table_rows(batch["tickets"]),
                "",
            ]
        )

    lines.extend(["## Selected Queue", ""])
    if any(value is not None for value in data["selected_filters"].values()):
        lines.append(f"Filters: `{json.dumps(data['selected_filters'], ensure_ascii=False)}`")
    else:
        lines.append("No filters supplied; selected queue equals the full recommended open-ticket queue.")
    lines.extend(["", "| Ticket | Wiki | Priority | Wave | Risk | Human Review | Topic |", "| --- | --- | --- | --- | --- | --- | --- |"])
    lines.extend(short_table_rows(selected[:50]))
    if len(selected) > 50:
        lines.append(f"| +{len(selected) - 50} more | - | - | - | - | - | - |")

    lines.extend(["", "## Ticket Commands", ""])
    for card in selected[:20]:
        lines.extend(
            [
                f"### {card['ticket_id']}",
                "",
                f"- Wiki: {repo_link('wikis/' + card['wiki'], card['wiki'])}",
                f"- Topic: {card['topic']}",
                f"- Suggested sources: {', '.join(card['suggested_sources']) if card['suggested_sources'] else '-'}",
                f"- Source log: {repo_link(card['log_path'])}",
                "",
                "Dry-run evidence template:",
                "",
                "```bash",
                card["dry_run_command"],
                "```",
                "",
                "Record command template:",
                "",
                "```bash",
                card["record_command_template"],
                "```",
                "",
            ]
        )

    lines.extend(["## Post-Update Commands", "", "```bash"])
    lines.extend(data["post_commands"])
    lines.extend(
        [
            "```",
            "",
            "## Safety Boundary",
            "",
            "- This runner does not fetch, verify, or certify external facts.",
            "- Use `still-needs-source-update` when evidence is missing, stale, conflicting, or outside scope.",
            "- Do not write current facts into wiki pages until the relevant ticket has dated evidence and audits pass.",
        ]
    )
    if data["missing_required"]:
        lines.extend(["", "## Missing Required Artifacts", ""])
        lines.extend(f"- `{path}`" for path in data["missing_required"])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = ArgumentParser(description="Generate source-refresh wave runner plans.")
    parser.add_argument("--wave", choices=["wave-1", "wave-2", "wave-3"], help="Select one wave for the printed queue.")
    parser.add_argument("--priority", choices=["P0", "P1", "P2"], help="Select one wiki priority for the printed queue.")
    parser.add_argument("--wiki", help="Select one wiki id for the printed queue.")
    parser.add_argument("--ticket-id", help="Select one ticket id or task id for the printed queue.")
    parser.add_argument("--limit", type=int, help="Limit selected queue length.")
    parser.add_argument("--json", action="store_true", help="Print selected queue as JSON after writing outputs.")
    args = parser.parse_args()

    data = build_runner()
    selected = build_runner(args.wave, args.priority, args.wiki, args.ticket_id, args.limit)
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.json:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}", file=sys.stderr)
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}", file=sys.stderr)
        print(json.dumps({"generated": selected["generated"], "selected_queue": selected["selected_queue"]}, ensure_ascii=False, indent=2))
    else:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
        if any([args.wave, args.priority, args.wiki, args.ticket_id, args.limit is not None]):
            print(f"Selected queue: {len(selected['selected_queue'])} tickets")
        print(
            "SOURCE REFRESH WAVE RUNNER GENERATED "
            f"({data['open_ticket_count']} open, {len(data['selected_queue'])} selected)"
        )
    if not data["passed"]:
        print(f"Missing required artifacts: {data['missing_required']}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
