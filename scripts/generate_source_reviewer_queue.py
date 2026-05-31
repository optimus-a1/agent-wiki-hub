#!/usr/bin/env python3
"""Generate reviewer-role queues for source-refresh tickets without verifying facts."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEWER_QUEUE.md"
JSON_OUT = REGISTRY / "source-reviewer-queue.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}

REPORTS = {
    "source_refresh_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_refresh_wave_runner": "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
    "source_refresh_tickets": "docs/SOURCE_REFRESH_TICKETS.md",
    "source_evidence_recorder": "docs/SOURCE_EVIDENCE_RECORDER.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_evidence_packet_fixtures": "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
}

REVIEWER_ROLES = {
    "finance-agent-wiki": {
        "role": "finance-risk-reviewer",
        "description": "Checks market, accounting, regulatory, and trading-system evidence while preserving investment-advice and real-money execution boundaries.",
    },
    "customs-agent-wiki": {
        "role": "customs-document-reviewer",
        "description": "Checks trade-document, field-mapping, OCR, discrepancy, and customs-policy evidence while preserving manual review gates.",
    },
    "coding-agent-wiki": {
        "role": "software-maintainer-reviewer",
        "description": "Checks software, dependency, API, deployment, and security-development evidence without recording secrets.",
    },
    "agent-engineering-wiki": {
        "role": "agent-engineering-reviewer",
        "description": "Checks agent architecture, RAG, skills, evals, MCP, and source-grounding evidence.",
    },
    "ecommerce-agent-wiki": {
        "role": "ecommerce-policy-reviewer",
        "description": "Checks product, pricing, customer-service, returns, privacy, ads, and marketplace-policy evidence.",
    },
    "nodeops-agent-wiki": {
        "role": "operations-change-reviewer",
        "description": "Checks infrastructure, deployment, install, monitoring, node, and destructive-operation evidence with rollback gates.",
    },
    "airdrop-agent-wiki": {
        "role": "web3-wallet-safety-reviewer",
        "description": "Checks public Web3 project, token, airdrop, and wallet-safety evidence without Sybil, spam, or signing automation.",
    },
    "content-agent-wiki": {
        "role": "content-fact-check-reviewer",
        "description": "Checks publication, trend, citation, platform, and source-backed claim evidence.",
    },
    "legal-agent-wiki": {
        "role": "legal-counsel-reviewer",
        "description": "Checks jurisdiction, statute, regulation, contract, and legal-process evidence while preserving counsel review.",
    },
    "health-agent-wiki": {
        "role": "clinical-safety-reviewer",
        "description": "Checks guideline, drug, symptom, and health-education evidence while preserving clinician review and red flags.",
    },
    "research-agent-wiki": {
        "role": "research-methods-reviewer",
        "description": "Checks papers, datasets, benchmarks, citations, and reproducibility evidence.",
    },
    "security-agent-wiki": {
        "role": "defensive-security-reviewer",
        "description": "Checks defensive security, advisory, dependency, and hardening evidence without exploit or evasion steps.",
    },
}

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


def bool_word(value: bool) -> str:
    return "yes" if value else "no"


def is_open(ticket: dict) -> bool:
    status = str(ticket.get("status") or "open_pending_source_refresh")
    return status not in FINAL_STATUSES and not bool(ticket.get("is_final"))


def evidence_dry_run_command(ticket: dict) -> str:
    if ticket.get("dry_run_command"):
        return str(ticket["dry_run_command"])
    return f"python3 scripts/record_source_evidence.py --ticket-id {ticket.get('ticket_id')} --status pending --dry-run"


def evidence_record_command(ticket: dict) -> str:
    if ticket.get("record_command_template"):
        return str(ticket["record_command_template"])
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
    if ticket.get("human_confirmation_required") or ticket.get("human_review_gate"):
        command += " --human-reviewer \"<reviewer>\""
    return command


def available_fixture_paths() -> set[str]:
    fixtures = read_json(REGISTRY / "source-evidence-packet-fixtures.json")
    return {str(item.get("path")) for item in fixtures.get("fixtures", []) if item.get("path")}


def packet_hint(ticket: dict, paths: set[str]) -> str:
    customs = "registry/source-evidence-fixtures/template-wave-2-customs-pending.json"
    p0_wave_1 = "registry/source-evidence-fixtures/template-wave-1-p0-pending.json"
    default = "registry/source-evidence-fixtures/valid-pending-single.json"
    if ticket.get("wiki") == "customs-agent-wiki" and customs in paths:
        return customs
    if ticket.get("wave") == "wave-1" and ticket.get("priority") == "P0" and p0_wave_1 in paths:
        return p0_wave_1
    if default in paths:
        return default
    return ""


def review_checklist(ticket: dict) -> list[str]:
    items = [
        "Read root AGENTS.md, target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.",
        "Verify source authority, publication/update date, scope, and access date before recording evidence.",
        "Confirm the source supports the exact ticket topic; put unsupported parts in remaining uncertainty.",
        "Prefer official, primary, dated sources and do not use summaries as the only authority.",
        "Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.",
        "Do not move current facts into stable wiki pages until ticket evidence, audits, and package checks pass.",
    ]
    if ticket.get("human_review_gate"):
        items.append("Obtain explicit human confirmation before marking the ticket verified or unchanged.")
    risk = ticket.get("risk_level", "")
    if risk == "high":
        items.append("Keep the high-risk domain boundary visible in the final note and require manual acceptance.")
    return items


def review_card(ticket: dict, index: int, fixture_paths: set[str]) -> dict:
    wiki = str(ticket.get("wiki", ""))
    role_info = REVIEWER_ROLES.get(wiki, {"role": "source-reviewer", "description": "Checks source evidence and unresolved uncertainty."})
    human_gate = bool(ticket.get("human_review_gate") or ticket.get("human_confirmation_required") or ticket.get("risk_level") == "high")
    enriched = dict(ticket)
    enriched["human_review_gate"] = human_gate
    return {
        "review_id": f"REVIEW-SRC-{index:03d}",
        "ticket_id": ticket.get("ticket_id", ""),
        "task_id": ticket.get("task_id", ""),
        "wiki": wiki,
        "priority": ticket.get("priority", ""),
        "wave": ticket.get("wave", ""),
        "risk_level": ticket.get("risk_level", ""),
        "freshness": ticket.get("freshness", ""),
        "category": ticket.get("category", ""),
        "topic": ticket.get("topic", ""),
        "status": ticket.get("status", "open_pending_source_refresh"),
        "reviewer_role": role_info["role"],
        "reviewer_role_description": role_info["description"],
        "review_state": "unassigned_pending_source_refresh",
        "source_collection_required": True,
        "human_confirmation_required": bool(ticket.get("human_confirmation_required", False)),
        "human_review_gate": human_gate,
        "suggested_sources": ticket.get("suggested_sources", []),
        "required_reading": ticket.get("required_reading", []),
        "evidence_log": ticket.get("log_path") or f"wikis/{wiki}/sources/source-refresh-log.md",
        "source_notes": ticket.get("source_notes_path") or f"wikis/{wiki}/sources/source-notes.md",
        "packet_template_hint": packet_hint(ticket, fixture_paths),
        "dry_run_command": evidence_dry_run_command(ticket),
        "record_command_template": evidence_record_command(enriched),
        "review_checklist": review_checklist(enriched),
    }


def group_cards(cards: list[dict], key: str) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for card in cards:
        grouped[str(card.get(key, "unknown"))].append(card)
    records: list[dict] = []
    for value in sorted(grouped):
        items = grouped[value]
        records.append(
            {
                key: value,
                "review_count": len(items),
                "high_risk_count": sum(1 for item in items if item.get("risk_level") == "high"),
                "human_review_gate_count": sum(1 for item in items if item.get("human_review_gate")),
                "wikis": dict(sorted(Counter(item.get("wiki", "") for item in items).items())),
                "review_ids": [item["review_id"] for item in items],
                "ticket_ids": [item["ticket_id"] for item in items],
            }
        )
    return records


def reviewer_role_records(cards: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for card in cards:
        grouped[card["reviewer_role"]].append(card)
    records = []
    for role in sorted(grouped):
        items = grouped[role]
        records.append(
            {
                "reviewer_role": role,
                "description": items[0].get("reviewer_role_description", ""),
                "review_count": len(items),
                "high_risk_count": sum(1 for item in items if item.get("risk_level") == "high"),
                "human_review_gate_count": sum(1 for item in items if item.get("human_review_gate")),
                "wikis": sorted({item["wiki"] for item in items}),
                "ticket_ids": [item["ticket_id"] for item in items],
            }
        )
    return records


def source_cards_from_inputs() -> list[dict]:
    wave_runner = read_json(REGISTRY / "source-refresh-wave-runner.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    candidates = wave_runner.get("recommended_queue") or completion.get("tickets", [])
    return [ticket for ticket in candidates if is_open(ticket)]


def build_queue() -> dict:
    registry = parse_registry(REGISTRY / "wiki-registry.yaml")
    wave_runner = read_json(REGISTRY / "source-refresh-wave-runner.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    quality = read_json(REGISTRY / "source-evidence-quality-audit.json")
    dashboard = read_json(REGISTRY / "source-refresh-dashboard.json")
    fixture_paths = available_fixture_paths()

    source_cards = source_cards_from_inputs()
    cards = [review_card(ticket, index + 1, fixture_paths) for index, ticket in enumerate(source_cards)]
    human_review_queue = [card for card in cards if card["human_review_gate"]]

    missing_required = [
        path
        for path in [
            "registry/wiki-registry.yaml",
            "registry/source-refresh-wave-runner.json",
            "registry/source-refresh-completion-audit.json",
            "registry/source-evidence-quality-audit.json",
        ]
        if not (ROOT / path).exists()
    ]
    checks = [
        {
            "check": "required source-refresh artifacts exist",
            "passed": not missing_required,
            "detail": ", ".join(missing_required) if missing_required else "all required artifacts present",
        },
        {
            "check": "open tickets have reviewer roles",
            "passed": all(card.get("reviewer_role") for card in cards) and len(cards) == int(wave_runner.get("open_ticket_count", len(cards))),
            "detail": f"{len(cards)} review cards for {wave_runner.get('open_ticket_count', len(cards))} open tickets",
        },
        {
            "check": "human review gates are preserved",
            "passed": sum(1 for card in cards if card["human_review_gate"]) >= sum(1 for ticket in source_cards if ticket.get("human_review_gate")),
            "detail": f"{len(human_review_queue)} human-gated cards",
        },
        {
            "check": "current facts remain gated",
            "passed": (not bool(dashboard.get("current_fact_ready", completion.get("completion_ready_for_current_fact_use", False)))) if cards else True,
            "detail": "current_fact_ready=false while open tickets remain" if cards else "no open tickets",
        },
    ]

    data = {
        "generated": date.today().isoformat(),
        "purpose": "Assign source-refresh tickets to generic reviewer roles while preserving human confirmation and current-fact gates.",
        "passed": all(check["passed"] for check in checks),
        "current_fact_ready": bool(dashboard.get("current_fact_ready", completion.get("completion_ready_for_current_fact_use", False))),
        "ticket_count": int(completion.get("ticket_count", wave_runner.get("ticket_count", len(cards)))),
        "open_ticket_count": len(cards),
        "verified_ticket_count": int(completion.get("verified_ticket_count", 0)),
        "finalized_ticket_count": int(completion.get("finalized_ticket_count", 0)),
        "evidence_entry_count": int(quality.get("entry_count", 0)),
        "evidence_issue_count": int(quality.get("issue_count", 0)),
        "human_review_gate_count": len(human_review_queue),
        "reviewer_role_count": len({card["reviewer_role"] for card in cards}),
        "reports": REPORTS,
        "registry_wiki_count": len(registry),
        "reviewer_roles": reviewer_role_records(cards),
        "queues_by_reviewer": group_cards(cards, "reviewer_role"),
        "queues_by_wave": group_cards(cards, "wave"),
        "queues_by_priority": group_cards(cards, "priority"),
        "queues_by_wiki": group_cards(cards, "wiki"),
        "human_review_queue": human_review_queue,
        "review_cards": cards,
        "checks": checks,
        "post_commands": POST_COMMANDS,
    }
    return data


def card_rows(cards: list[dict], limit: int | None = None) -> list[str]:
    shown = cards[:limit] if limit else cards
    if not shown:
        return ["| - | - | - | - | - | - | - |"]
    rows = []
    for card in shown:
        rows.append(
            f"| `{card['review_id']}` | `{card['ticket_id']}` | {repo_link('wikis/' + card['wiki'], card['wiki'])} | "
            f"{card['priority']} | {card['wave']} | {card['reviewer_role']} | {bool_word(card['human_review_gate'])} | {card['topic']} |"
        )
    if limit and len(cards) > limit:
        rows.append(f"| +{len(cards) - limit} more | - | - | - | - | - | - | - |")
    return rows


def markdown_report(data: dict) -> str:
    current_ready = bool_word(data["current_fact_ready"])
    passed = bool_word(data["passed"])
    lines = [
        "# Source Reviewer Queue",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Current State",
        "",
        f"- Queue generated cleanly: {passed}",
        f"- Current-fact ready: {current_ready}",
        f"- Tickets: {data['ticket_count']}",
        f"- Open tickets: {data['open_ticket_count']}",
        f"- Verified tickets: {data['verified_ticket_count']}",
        f"- Finalized tickets: {data['finalized_ticket_count']}",
        f"- Evidence entries: {data['evidence_entry_count']}",
        f"- Evidence issues: {data['evidence_issue_count']}",
        f"- Reviewer roles: {data['reviewer_role_count']}",
        f"- Human review gates: {data['human_review_gate_count']}",
        "",
        "## Reviewer Roles",
        "",
        "| Reviewer Role | Tickets | High Risk | Human Gates | Wikis | Scope |",
        "| --- | ---: | ---: | ---: | --- | --- |",
    ]
    for role in data["reviewer_roles"]:
        wikis = ", ".join(repo_link("wikis/" + wiki, wiki) for wiki in role["wikis"])
        lines.append(
            f"| `{role['reviewer_role']}` | {role['review_count']} | {role['high_risk_count']} | "
            f"{role['human_review_gate_count']} | {wikis} | {role['description']} |"
        )

    lines.extend(["", "## Wave Summary", "", "| Wave | Reviews | High Risk | Human Gates | Wikis |", "| --- | ---: | ---: | ---: | --- |"])
    for row in data["queues_by_wave"]:
        wiki_summary = ", ".join(f"{wiki}:{count}" for wiki, count in row["wikis"].items())
        lines.append(f"| {row['wave']} | {row['review_count']} | {row['high_risk_count']} | {row['human_review_gate_count']} | {wiki_summary} |")

    lines.extend(["", "## Priority Summary", "", "| Priority | Reviews | High Risk | Human Gates | Wikis |", "| --- | ---: | ---: | ---: | --- |"])
    for row in data["queues_by_priority"]:
        wiki_summary = ", ".join(f"{wiki}:{count}" for wiki, count in row["wikis"].items())
        lines.append(f"| {row['priority']} | {row['review_count']} | {row['high_risk_count']} | {row['human_review_gate_count']} | {wiki_summary} |")

    lines.extend(
        [
            "",
            "## Human Confirmation Queue",
            "",
            "| Review | Ticket | Wiki | Priority | Wave | Reviewer Role | Human Gate | Topic |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *card_rows(data["human_review_queue"]),
            "",
            "## Review Cards",
            "",
            "| Review | Ticket | Wiki | Priority | Wave | Reviewer Role | Human Gate | Topic |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *card_rows(data["review_cards"], 60),
            "",
            "## Reviewer Checklist",
            "",
            "- Read root and wiki-level instructions before collecting sources.",
            "- Use official, primary, dated sources whenever available.",
            "- Record publication or update date, access date, scope, confidence, and uncertainty.",
            "- Keep high-risk finance, legal, health, security, Web3, and operations topics behind human confirmation.",
            "- Do not record secrets, credentials, cookies, private keys, seed phrases, or private account data.",
            "- Keep `needs-source-update` in place until evidence logs and audits support a final status.",
            "",
            "## Useful Commands",
            "",
            "```bash",
            *data["post_commands"],
            "```",
            "",
            "## Related Reports",
            "",
        ]
    )
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
            "- This queue does not fetch, verify, or certify external facts.",
            "- Reviewer roles are generic operating roles, not real people or external authorities.",
            "- A ticket can remain open with `still-needs-source-update` when evidence is missing, stale, conflicting, or outside scope.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_queue()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(
        "SOURCE REVIEWER QUEUE GENERATED "
        f"({data['open_ticket_count']} open, {data['human_review_gate_count']} human gates)"
    )
    if not data["passed"]:
        failed = [check for check in data["checks"] if not check["passed"]]
        print(f"SOURCE REVIEWER QUEUE HAS BLOCKERS: {failed}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
