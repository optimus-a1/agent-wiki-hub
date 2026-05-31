#!/usr/bin/env python3
"""Generate a source-review session plan from the reviewer queue."""
from __future__ import annotations

from argparse import ArgumentParser
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_SESSION_PLAN.md"
JSON_OUT = REGISTRY / "source-review-session-plan.json"

WAVE_ORDER = {"wave-1": 0, "wave-2": 1, "wave-3": 2}
PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
RISK_ORDER = {"high": 0, "medium": 1, "low": 2}

REPORTS = {
    "source_refresh_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_refresh_wave_runner": "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
    "source_reviewer_queue": "docs/SOURCE_REVIEWER_QUEUE.md",
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "source_review_packet_audit": "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "source_review_packet_rehearsal": "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "source_evidence_recorder": "docs/SOURCE_EVIDENCE_RECORDER.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_evidence_packet_fixtures": "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
}

PREFLIGHT_CHECKLIST = [
    "Read root AGENTS.md and the target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.",
    "Confirm the selected ticket scope before opening external sources.",
    "Use official, primary, dated sources whenever available.",
    "Record source title, publisher, URL or reference, publication/update date, access date, confidence, and remaining uncertainty.",
    "Keep human-review-gated tickets open until a human reviewer is named in the evidence log.",
    "Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.",
    "Use still-needs-source-update when source evidence is missing, stale, conflicting, or out of scope.",
]

SESSION_STEPS = [
    "Run the dry-run command for each selected review to confirm ticket and log wiring.",
    "Collect source evidence outside this script; this planner does not browse or verify facts.",
    "Record evidence with record_source_evidence.py or import_source_evidence_packet.py.",
    "Re-run completion, evidence quality, reviewer queue, session plan, dashboard, index, and acceptance.",
    "Only then consider whether any wiki page can move from needs-source-update to stable wording.",
]

STOP_CONDITIONS = [
    "The source is not official, primary, dated, or clearly scoped to the ticket.",
    "Sources conflict and no authoritative resolution is available.",
    "A high-risk topic lacks human confirmation.",
    "A source requires credentials, private account data, cookies, tokens, or private keys.",
    "The evidence would enable unsafe finance, legal, medical, security, Web3, or production operations.",
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


def repo_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def bool_word(value: bool) -> str:
    return "yes" if value else "no"


def sort_key(card: dict) -> tuple:
    return (
        WAVE_ORDER.get(card.get("wave", ""), 99),
        PRIORITY_ORDER.get(card.get("priority", ""), 99),
        RISK_ORDER.get(card.get("risk_level", ""), 99),
        0 if card.get("human_review_gate") else 1,
        card.get("reviewer_role", ""),
        card.get("wiki", ""),
        card.get("ticket_id", ""),
    )


def selected_cards(
    cards: list[dict],
    wave: str | None,
    priority: str | None,
    wiki: str | None,
    reviewer_role: str | None,
    human_only: bool,
    all_open: bool,
    limit: int | None,
) -> tuple[list[dict], dict]:
    default_session = not any([wave, priority, wiki, reviewer_role, human_only, all_open, limit is not None])
    filters = {
        "wave": wave,
        "priority": priority,
        "wiki": wiki,
        "reviewer_role": reviewer_role,
        "human_only": human_only,
        "all_open": all_open,
        "limit": limit,
        "default_session": default_session,
    }
    rows = list(cards)
    if default_session:
        available_waves = sorted(
            {card.get("wave", "") for card in rows if card.get("wave")},
            key=lambda item: WAVE_ORDER.get(item, 99),
        )
        selected_wave = "wave-1" if "wave-1" in available_waves else (available_waves[0] if available_waves else "wave-1")
        rows = [card for card in rows if card.get("wave") == selected_wave]
        filters["wave"] = selected_wave
    elif wave:
        rows = [card for card in rows if card.get("wave") == wave]

    if priority:
        rows = [card for card in rows if card.get("priority") == priority]
    if wiki:
        rows = [card for card in rows if card.get("wiki") == wiki]
    if reviewer_role:
        rows = [card for card in rows if card.get("reviewer_role") == reviewer_role]
    if human_only:
        rows = [card for card in rows if card.get("human_review_gate")]
    rows = sorted(rows, key=sort_key)
    if limit is not None:
        rows = rows[:limit]
    return rows, filters


def compact_review(card: dict) -> dict:
    return {
        "review_id": card.get("review_id", ""),
        "ticket_id": card.get("ticket_id", ""),
        "task_id": card.get("task_id", ""),
        "wiki": card.get("wiki", ""),
        "priority": card.get("priority", ""),
        "wave": card.get("wave", ""),
        "risk_level": card.get("risk_level", ""),
        "freshness": card.get("freshness", ""),
        "category": card.get("category", ""),
        "topic": card.get("topic", ""),
        "reviewer_role": card.get("reviewer_role", ""),
        "human_review_gate": bool(card.get("human_review_gate", False)),
        "suggested_sources": card.get("suggested_sources", []),
        "required_reading": card.get("required_reading", []),
        "evidence_log": card.get("evidence_log", ""),
        "source_notes": card.get("source_notes", ""),
        "packet_template_hint": card.get("packet_template_hint", ""),
        "dry_run_command": card.get("dry_run_command", ""),
        "record_command_template": card.get("record_command_template", ""),
    }


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
        "follow_up": "Keep needs-source-update unless the evidence is authoritative, dated, scoped, and reviewed.",
    }


def packet_template(cards: list[dict]) -> dict:
    return {
        "packet_id": f"source-review-session-{date.today().isoformat()}",
        "created_on": date.today().isoformat(),
        "created_by": "<human reviewer or source-refresh agent>",
        "dry_run_first": True,
        "entries": [packet_entry(card) for card in cards],
    }


def role_workload(cards: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for card in cards:
        grouped[str(card.get("reviewer_role", "unknown"))].append(card)
    records = []
    for role in sorted(grouped):
        items = grouped[role]
        records.append(
            {
                "reviewer_role": role,
                "review_count": len(items),
                "human_review_gate_count": sum(1 for item in items if item.get("human_review_gate")),
                "high_risk_count": sum(1 for item in items if item.get("risk_level") == "high"),
                "wikis": dict(sorted(Counter(item.get("wiki", "") for item in items).items())),
                "ticket_ids": [item.get("ticket_id", "") for item in items],
            }
        )
    return records


def command_examples() -> list[str]:
    return [
        "python3 scripts/generate_source_review_session_plan.py",
        "python3 scripts/generate_source_review_session_plan.py --wave wave-1 --limit 5",
        "python3 scripts/generate_source_review_session_plan.py --reviewer-role finance-risk-reviewer --human-only",
        "python3 scripts/generate_source_review_session_plan.py --wiki customs-agent-wiki --json",
        "python3 scripts/generate_source_review_session_plan.py --all-open",
    ]


def build_plan(
    wave: str | None = None,
    priority: str | None = None,
    wiki: str | None = None,
    reviewer_role: str | None = None,
    human_only: bool = False,
    all_open: bool = False,
    limit: int | None = None,
) -> dict:
    reviewer_queue = read_json(REGISTRY / "source-reviewer-queue.json")
    completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    cards = sorted(reviewer_queue.get("review_cards", []), key=sort_key)
    selected, filters = selected_cards(cards, wave, priority, wiki, reviewer_role, human_only, all_open, limit)

    missing_required = [
        path
        for path in [
            "registry/source-reviewer-queue.json",
            "registry/source-refresh-completion-audit.json",
        ]
        if not (ROOT / path).exists()
    ]
    checks = [
        {
            "check": "required reviewer artifacts exist",
            "passed": not missing_required,
            "detail": ", ".join(missing_required) if missing_required else "all required artifacts present",
        },
        {
            "check": "selected reviews available",
            "passed": bool(selected) or not cards,
            "detail": f"{len(selected)} selected from {len(cards)} open reviews",
        },
        {
            "check": "selected reviews have reviewer roles and commands",
            "passed": all(card.get("reviewer_role") and card.get("dry_run_command") for card in selected),
            "detail": "reviewer role and dry-run command present for every selected review",
        },
        {
            "check": "current facts remain gated while tickets are open",
            "passed": (not bool(reviewer_queue.get("current_fact_ready"))) if cards else True,
            "detail": "current_fact_ready=false while open reviews remain" if cards else "no open reviews",
        },
    ]

    return {
        "generated": date.today().isoformat(),
        "session_id": f"source-review-session-{date.today().isoformat()}",
        "purpose": "Turn reviewer-queue cards into a concrete source-review session plan without fetching or certifying external facts.",
        "passed": all(check["passed"] for check in checks),
        "current_fact_ready": bool(reviewer_queue.get("current_fact_ready", completion.get("completion_ready_for_current_fact_use", False))),
        "open_review_count": len(cards),
        "selected_review_count": len(selected),
        "selected_human_review_gate_count": sum(1 for card in selected if card.get("human_review_gate")),
        "selected_high_risk_count": sum(1 for card in selected if card.get("risk_level") == "high"),
        "selected_filters": filters,
        "role_workload": role_workload(selected),
        "wiki_counts": dict(sorted(Counter(card.get("wiki", "") for card in selected).items())),
        "priority_counts": dict(sorted(Counter(card.get("priority", "") for card in selected).items())),
        "wave_counts": dict(sorted(Counter(card.get("wave", "") for card in selected).items())),
        "selected_reviews": [compact_review(card) for card in selected],
        "packet_template": packet_template(selected),
        "preflight_checklist": PREFLIGHT_CHECKLIST,
        "session_steps": SESSION_STEPS,
        "stop_conditions": STOP_CONDITIONS,
        "post_commands": POST_COMMANDS,
        "command_examples": command_examples(),
        "reports": REPORTS,
        "checks": checks,
    }


def review_rows(cards: list[dict]) -> list[str]:
    if not cards:
        return ["| - | - | - | - | - | - | - | - |"]
    rows = []
    for card in cards:
        rows.append(
            f"| `{card['review_id']}` | `{card['ticket_id']}` | {repo_link('wikis/' + card['wiki'], card['wiki'])} | "
            f"{card['priority']} | {card['wave']} | {card['risk_level']} | {card['reviewer_role']} | "
            f"{bool_word(card['human_review_gate'])} | {card['topic']} |"
        )
    return rows


def markdown_report(data: dict) -> str:
    filters = json.dumps(data["selected_filters"], ensure_ascii=False)
    lines = [
        "# Source Review Session Plan",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Current State",
        "",
        f"- Current-fact ready: {bool_word(data['current_fact_ready'])}",
        f"- Open reviews: {data['open_review_count']}",
        f"- Selected reviews: {data['selected_review_count']}",
        f"- Selected high-risk reviews: {data['selected_high_risk_count']}",
        f"- Selected human review gates: {data['selected_human_review_gate_count']}",
        f"- Filters: `{filters}`",
        "",
        "## Preflight Checklist",
        "",
    ]
    lines.extend(f"- [ ] {item}" for item in data["preflight_checklist"])

    lines.extend(
        [
            "",
            "## Selected Reviews",
            "",
            "| Review | Ticket | Wiki | Priority | Wave | Risk | Reviewer Role | Human Gate | Topic |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *review_rows(data["selected_reviews"]),
            "",
            "## Role Workload",
            "",
            "| Reviewer Role | Reviews | High Risk | Human Gates | Wikis |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for role in data["role_workload"]:
        wikis = ", ".join(f"{wiki}:{count}" for wiki, count in role["wikis"].items())
        lines.append(
            f"| `{role['reviewer_role']}` | {role['review_count']} | {role['high_risk_count']} | "
            f"{role['human_review_gate_count']} | {wikis} |"
        )

    lines.extend(["", "## Session Steps", ""])
    lines.extend(f"- {item}" for item in data["session_steps"])
    lines.extend(["", "## Stop Conditions", ""])
    lines.extend(f"- {item}" for item in data["stop_conditions"])

    lines.extend(["", "## Evidence Packet Skeleton", "", "Use this only as a template. Replace every placeholder before a real import.", "", "```json"])
    packet_preview = dict(data["packet_template"])
    if len(packet_preview["entries"]) > 5:
        packet_preview["entries"] = packet_preview["entries"][:5]
        packet_preview["truncated_entries"] = data["selected_review_count"] - 5
    lines.append(json.dumps(packet_preview, ensure_ascii=False, indent=2))
    lines.extend(["```", ""])

    lines.extend(["## Per-Ticket Dry Runs", ""])
    for review in data["selected_reviews"]:
        lines.extend(
            [
                f"### {review['review_id']}",
                "",
                f"- Ticket: `{review['ticket_id']}`",
                f"- Wiki: {repo_link('wikis/' + review['wiki'], review['wiki'])}",
                f"- Evidence log: {repo_link(review['evidence_log'])}",
                "",
                "```bash",
                review["dry_run_command"],
                "```",
                "",
            ]
        )

    lines.extend(["## Command Examples", "", "```bash"])
    lines.extend(data["command_examples"])
    lines.extend(["```", "", "## Post-Session Commands", "", "```bash"])
    lines.extend(data["post_commands"])
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
            "- This planner does not browse, verify, or certify current facts.",
            "- It is safe to run offline because it only reorganizes existing open review cards and placeholder packet fields.",
            "- Keep high-risk and human-gated tickets open until authoritative evidence and human confirmation are recorded.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = ArgumentParser(description="Generate source-review session plans from reviewer queue cards.")
    parser.add_argument("--wave", choices=["wave-1", "wave-2", "wave-3"], help="Select one source-refresh wave.")
    parser.add_argument("--priority", choices=["P0", "P1", "P2"], help="Select one wiki priority.")
    parser.add_argument("--wiki", help="Select one wiki id.")
    parser.add_argument("--reviewer-role", help="Select one reviewer role.")
    parser.add_argument("--human-only", action="store_true", help="Select only human-review-gated cards.")
    parser.add_argument("--all-open", action="store_true", help="Select all open cards when no wave is supplied.")
    parser.add_argument("--limit", type=int, help="Limit selected review count.")
    parser.add_argument("--json", action="store_true", help="Print selected session plan as JSON after writing outputs.")
    args = parser.parse_args()

    data = build_plan()
    selected = build_plan(args.wave, args.priority, args.wiki, args.reviewer_role, args.human_only, args.all_open, args.limit)
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.json:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}", file=sys.stderr)
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}", file=sys.stderr)
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
        if any([args.wave, args.priority, args.wiki, args.reviewer_role, args.human_only, args.all_open, args.limit is not None]):
            print(f"Selected reviews: {selected['selected_review_count']}")
        print(
            "SOURCE REVIEW SESSION PLAN GENERATED "
            f"({data['selected_review_count']} selected, {data['selected_human_review_gate_count']} human gates)"
        )
    if not data["passed"]:
        failed = [check for check in data["checks"] if not check["passed"]]
        print(f"SOURCE REVIEW SESSION PLAN HAS BLOCKERS: {failed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
