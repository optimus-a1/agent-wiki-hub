#!/usr/bin/env python3
"""Generate a handoff brief for the next agent working on this hub."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS_OUT = ROOT / "docs" / "AGENT_HANDOFF.md"
JSON_OUT = ROOT / "registry" / "agent-handoff.json"
REGISTRY = ROOT / "registry"

FIRST_READS = [
    "AGENTS.md",
    "docs/SOURCE_REFRESH_DASHBOARD.md",
    "docs/AGENT_ROUTING_CARDS.md",
    "docs/HUB_NAVIGATION.md",
    "docs/SOURCE_REFRESH_TICKETS.md",
    "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
    "docs/SOURCE_REVIEWER_QUEUE.md",
    "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "docs/SOURCE_REVIEW_WORK_ORDERS.md",
    "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
    "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
    "docs/SAFETY_AUDIT.md",
]

HARD_BOUNDARIES = [
    "Do not treat open source-refresh tickets as verified facts.",
    "Do not write current prices, policies, laws, medical guidance, CVEs, API parameters, platform rules, exchange rules, or Web3 project rules without dated evidence.",
    "Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.",
    "Do not generate real-money autonomous trading flows.",
    "Do not produce final legal opinions, medical diagnoses, offensive security steps, Sybil evasion, spam, fake identity, or platform-rule bypass guidance.",
    "For high-risk wikis, read rules/ before workflows/ and preserve human confirmation points.",
]

NEXT_ACTIONS = [
    "If source access is unavailable, keep current-fact tickets open and add only stable concepts, workflows, prompts, evals, and safety boundaries.",
    "If source access is available, start with wave-1 and P0 tickets, then record evidence through scripts/record_source_evidence.py.",
    "After any source update, rerun source completion, evidence quality, dashboard generation, search index, and full acceptance.",
    "Keep affected wiki update-log.md files current whenever wiki content changes.",
]

COMMANDS = [
    'python3 scripts/route_wiki.py --query "risk control backtest"',
    "python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run",
    "python3 scripts/audit_source_refresh_completion.py",
    "python3 scripts/audit_source_evidence_quality.py",
    "python3 scripts/generate_source_refresh_dashboard.py",
    "python3 scripts/generate_source_refresh_wave_runner.py --wave wave-1 --limit 5",
    "python3 scripts/generate_source_reviewer_queue.py",
    "python3 scripts/generate_source_review_session_plan.py --wave wave-1 --limit 5",
    "python3 scripts/generate_source_review_packet_bundle.py",
    "python3 scripts/audit_source_review_packets.py",
    "python3 scripts/rehearse_source_review_packet_imports.py",
    "python3 scripts/generate_source_review_readiness_matrix.py",
    "python3 scripts/generate_source_review_work_orders.py",
    "python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks",
    "python3 scripts/import_source_evidence_packet.py --template --ticket-id TICKET-SRC-006",
    "python3 scripts/generate_source_evidence_packet_fixtures.py",
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


def priority_order(priority: str) -> int:
    match = re.fullmatch(r"P(\d+)", priority or "")
    return int(match.group(1)) if match else 99


def doc_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def repo_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    prefix = "../" if repo_path.startswith("docs/") or repo_path.startswith("registry/") else "../"
    return f"[{label}]({prefix}{repo_path})"


def source_refresh_summary(
    dashboard: dict,
    completion: dict,
    quality: dict,
    release: dict,
    acceptance: dict,
    reviewer_queue: dict,
    session_plan: dict,
    packet_bundle: dict,
    packet_audit: dict,
    packet_rehearsal: dict,
    readiness_matrix: dict,
    work_orders: dict,
) -> dict:
    return {
        "release_ready_for_internal_use": bool(
            dashboard.get("release_ready_for_internal_use", release.get("ready_for_internal_release", False))
        ),
        "current_fact_ready": bool(
            dashboard.get("current_fact_ready", completion.get("completion_ready_for_current_fact_use", False))
        ),
        "requires_source_update_for_current_facts": bool(
            dashboard.get(
                "requires_source_update_for_current_facts",
                release.get("requires_source_update_for_current_facts", True),
            )
        ),
        "ticket_count": int(completion.get("ticket_count", 0)),
        "open_ticket_count": int(completion.get("open_ticket_count", 0)),
        "verified_ticket_count": int(completion.get("verified_ticket_count", 0)),
        "finalized_ticket_count": int(completion.get("finalized_ticket_count", 0)),
        "source_evidence_entry_count": int(quality.get("entry_count", 0)),
        "source_evidence_quality_issue_count": int(quality.get("issue_count", 0)),
        "source_evidence_quality_warning_count": int(quality.get("warning_count", 0)),
        "source_reviewer_queue_open_count": int(reviewer_queue.get("open_ticket_count", 0)),
        "source_reviewer_queue_human_gate_count": int(reviewer_queue.get("human_review_gate_count", 0)),
        "source_review_session_selected_count": int(session_plan.get("selected_review_count", 0)),
        "source_review_session_human_gate_count": int(session_plan.get("selected_human_review_gate_count", 0)),
        "source_review_packet_bundle_entry_count": int(packet_bundle.get("selected_review_count", 0)),
        "source_review_packet_bundle_human_gate_count": int(packet_bundle.get("selected_human_review_gate_count", 0)),
        "source_review_packet_audit_packet_count": int(packet_audit.get("packet_count", 0)),
        "source_review_packet_audit_issue_count": int(packet_audit.get("issue_count", 0)),
        "source_review_packet_rehearsal_dry_run_count": int(packet_rehearsal.get("dry_run_count", 0)),
        "source_review_packet_rehearsal_passed_count": int(packet_rehearsal.get("passed_dry_run_count", 0)),
        "source_review_ready_for_collection_count": int(readiness_matrix.get("ready_for_source_collection_count", 0)),
        "source_review_queued_not_in_session_count": int(readiness_matrix.get("queued_not_in_current_session_count", 0)),
        "source_review_work_order_count": int(work_orders.get("work_order_count", 0)),
        "source_review_work_order_human_gate_count": int(work_orders.get("human_review_gate_count", 0)),
        "acceptance_passed": bool(acceptance.get("passed", False)),
    }


def p0_open_tickets(registry: dict[str, dict], tickets: list[dict]) -> list[dict]:
    p0_wikis = {wiki_id for wiki_id, record in registry.items() if record.get("priority") == "P0"}
    rows: dict[str, dict] = {}
    for wiki_id in sorted(p0_wikis):
        rows[wiki_id] = {
            "wiki": wiki_id,
            "priority": "P0",
            "open_ticket_count": 0,
            "tickets": [],
        }
    for ticket in tickets:
        wiki = ticket.get("wiki", "")
        if wiki in rows and ticket.get("status") == "open_pending_source_refresh":
            rows[wiki]["open_ticket_count"] += 1
            rows[wiki]["tickets"].append(
                {
                    "ticket_id": ticket.get("ticket_id", ""),
                    "topic": ticket.get("topic", ""),
                    "risk_level": ticket.get("risk_level", ""),
                    "wave": ticket.get("wave", ""),
                    "human_confirmation_required": bool(ticket.get("human_confirmation_required", False)),
                }
            )
    return sorted(rows.values(), key=lambda item: item["wiki"])


def top_open_tickets(dashboard: dict, completion: dict, limit: int = 12) -> list[dict]:
    tickets = dashboard.get("top_open_tickets") or completion.get("tickets", [])
    open_tickets = [ticket for ticket in tickets if ticket.get("status") == "open_pending_source_refresh"]
    return [
        {
            "ticket_id": ticket.get("ticket_id", ""),
            "wiki": ticket.get("wiki", ""),
            "wave": ticket.get("wave", ""),
            "priority_score": ticket.get("priority_score", ""),
            "risk_level": ticket.get("risk_level", ""),
            "topic": ticket.get("topic", ""),
            "human_confirmation_required": bool(ticket.get("human_confirmation_required", False)),
        }
        for ticket in open_tickets[:limit]
    ]


def build_handoff() -> dict:
    dashboard = read_json(REGISTRY / "source-refresh-dashboard.json")
    routing_cards = read_json(REGISTRY / "agent-routing-cards.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    quality = read_json(REGISTRY / "source-evidence-quality-audit.json")
    source_tickets = read_json(REGISTRY / "source-refresh-tickets.json")
    release = read_json(REGISTRY / "release-manifest.json")
    acceptance = read_json(REGISTRY / "acceptance-report.json")
    reviewer_queue = read_json(REGISTRY / "source-reviewer-queue.json")
    session_plan = read_json(REGISTRY / "source-review-session-plan.json")
    packet_bundle = read_json(REGISTRY / "source-review-packet-bundle.json")
    packet_audit = read_json(REGISTRY / "source-review-packet-audit.json")
    packet_rehearsal = read_json(REGISTRY / "source-review-packet-rehearsal.json")
    readiness_matrix = read_json(REGISTRY / "source-review-readiness-matrix.json")
    work_orders = read_json(REGISTRY / "source-review-work-orders.json")
    registry = parse_registry(REGISTRY / "wiki-registry.yaml")
    tickets = completion.get("tickets") or source_tickets.get("tickets", [])

    required_paths = FIRST_READS + [
        "registry/source-refresh-dashboard.json",
        "registry/agent-routing-cards.json",
        "registry/source-refresh-completion-audit.json",
        "registry/source-evidence-quality-audit.json",
        "registry/source-refresh-tickets.json",
        "registry/source-refresh-wave-runner.json",
        "registry/source-reviewer-queue.json",
        "registry/source-review-session-plan.json",
        "registry/source-review-readiness-matrix.json",
        "registry/source-review-work-orders.json",
        "registry/source-review-work-orders/manifest.json",
        "registry/source-review-packet-bundle.json",
        "registry/source-review-packet-audit.json",
        "registry/source-review-packet-rehearsal.json",
        "registry/source-review-packets/source-review-session-wave-1-pending.json",
        "registry/source-evidence-packet-importer.json",
        "registry/source-evidence-packet-fixtures.json",
    ]
    missing_required = [path for path in required_paths if not (ROOT / path).exists()]

    p0_rows = p0_open_tickets(registry, tickets)
    ordered_wikis = sorted(
        [
            {
                "wiki": wiki_id,
                "priority": record.get("priority", ""),
                "domain": record.get("domain", ""),
                "risk_level": record.get("risk_level", ""),
                "freshness": record.get("freshness", ""),
            }
            for wiki_id, record in registry.items()
        ],
        key=lambda item: (priority_order(item["priority"]), item["wiki"]),
    )

    data = {
        "generated": date.today().isoformat(),
        "passed": not missing_required,
        "handoff_ready": not missing_required,
        "missing_required": missing_required,
        "purpose": "Give the next agent a safe, source-aware entry point for continuing Agent Wiki Hub work.",
        "source_refresh": source_refresh_summary(
            dashboard,
            completion,
            quality,
            release,
            acceptance,
            reviewer_queue,
            session_plan,
            packet_bundle,
            packet_audit,
            packet_rehearsal,
            readiness_matrix,
            work_orders,
        ),
        "first_reads": FIRST_READS,
        "wiki_order": ordered_wikis,
        "p0_open_tickets": p0_rows,
        "top_open_tickets": top_open_tickets(dashboard, completion),
        "hard_boundaries": HARD_BOUNDARIES,
        "next_actions": NEXT_ACTIONS,
        "commands": COMMANDS,
        "routing_card_count": int(routing_cards.get("card_count", 0)),
    }
    return data


def markdown_report(data: dict) -> str:
    summary = data["source_refresh"]
    release_ready = "yes" if summary["release_ready_for_internal_use"] else "no"
    current_ready = "yes" if summary["current_fact_ready"] else "no"
    acceptance = "yes" if summary["acceptance_passed"] else "no"
    lines = [
        "# Agent Handoff",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Current State",
        "",
        f"- Internal release ready: {release_ready}",
        f"- Current-fact ready: {current_ready}",
        f"- Acceptance passed: {acceptance}",
        f"- Source-refresh tickets: {summary['ticket_count']}",
        f"- Open tickets: {summary['open_ticket_count']}",
        f"- Verified tickets: {summary['verified_ticket_count']}",
        f"- Finalized tickets: {summary['finalized_ticket_count']}",
        f"- Source evidence entries: {summary['source_evidence_entry_count']}",
        f"- Evidence quality issues: {summary['source_evidence_quality_issue_count']}",
        f"- Evidence quality warnings: {summary['source_evidence_quality_warning_count']}",
        f"- Source reviewer queue: {summary['source_reviewer_queue_open_count']} open reviews",
        f"- Source reviewer human gates: {summary['source_reviewer_queue_human_gate_count']}",
        f"- Source review session: {summary['source_review_session_selected_count']} selected reviews",
        f"- Source review session human gates: {summary['source_review_session_human_gate_count']}",
        f"- Source review packet bundle: {summary['source_review_packet_bundle_entry_count']} pending entries",
        f"- Source review packet human gates: {summary['source_review_packet_bundle_human_gate_count']}",
        f"- Source review packet audit: {summary['source_review_packet_audit_packet_count']} packets",
        f"- Source review packet audit issues: {summary['source_review_packet_audit_issue_count']}",
        f"- Source review packet rehearsal: {summary['source_review_packet_rehearsal_passed_count']}/{summary['source_review_packet_rehearsal_dry_run_count']} dry-runs passed",
        f"- Source review ready for collection: {summary['source_review_ready_for_collection_count']}",
        f"- Source review queued outside session: {summary['source_review_queued_not_in_session_count']}",
        f"- Source review work orders: {summary['source_review_work_order_count']}",
        f"- Source review work order human gates: {summary['source_review_work_order_human_gate_count']}",
        "",
        "## First Reads",
        "",
    ]
    lines.extend(f"- {repo_link(path)}" for path in data["first_reads"])

    lines.extend(["", "## Hard Boundaries", ""])
    lines.extend(f"- {item}" for item in data["hard_boundaries"])

    lines.extend(["", "## Next Best Work", ""])
    lines.extend(f"- {item}" for item in data["next_actions"])

    lines.extend(["", "## P0 Open Tickets", "", "| Wiki | Open | Ticket Topics |", "| --- | ---: | --- |"])
    for row in data["p0_open_tickets"]:
        topics = "<br>".join(f"`{ticket['ticket_id']}` {ticket['topic']}" for ticket in row["tickets"]) or "-"
        lines.append(f"| {repo_link('wikis/' + row['wiki'], row['wiki'])} | {row['open_ticket_count']} | {topics} |")

    lines.extend(["", "## Top Open Tickets", "", "| Ticket | Wiki | Wave | Risk | Topic | Human Confirm |", "| --- | --- | --- | --- | --- | --- |"])
    for ticket in data["top_open_tickets"]:
        human = "yes" if ticket["human_confirmation_required"] else "no"
        lines.append(
            f"| `{ticket['ticket_id']}` | {repo_link('wikis/' + ticket['wiki'], ticket['wiki'])} | "
            f"{ticket['wave']} | {ticket['risk_level']} | {ticket['topic']} | {human} |"
        )

    lines.extend(["", "## Wiki Order", "", "| Wiki | Priority | Risk | Freshness | Domain |", "| --- | --- | --- | --- | --- |"])
    for wiki in data["wiki_order"]:
        lines.append(
            f"| {repo_link('wikis/' + wiki['wiki'], wiki['wiki'])} | {wiki['priority']} | "
            f"{wiki['risk_level']} | {wiki['freshness']} | {wiki['domain']} |"
        )

    lines.extend(["", "## Useful Commands", "", "```bash"])
    lines.extend(data["commands"])
    lines.extend(["```", "", "## Notes", ""])
    lines.extend(
        [
            "- This handoff is generated from local registry and audit artifacts.",
            "- It does not verify external facts by itself.",
            "- Treat every open current-fact topic as `needs-source-update` until evidence is recorded and audits are rerun.",
        ]
    )
    if data["missing_required"]:
        lines.extend(["", "## Missing Required Artifacts", ""])
        lines.extend(f"- `{path}`" for path in data["missing_required"])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_handoff()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if not data["passed"]:
        print("AGENT HANDOFF GENERATED WITH MISSING ARTIFACTS")
        return 1
    print("AGENT HANDOFF GENERATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
