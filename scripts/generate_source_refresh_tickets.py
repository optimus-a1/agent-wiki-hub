#!/usr/bin/env python3
"""Generate execution tickets for source refresh tasks."""
from __future__ import annotations

from argparse import ArgumentParser
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK_JSON = ROOT / "registry" / "source-refresh-playbook.json"
DOCS_OUT = ROOT / "docs" / "SOURCE_REFRESH_TICKETS.md"
JSON_OUT = ROOT / "registry" / "source-refresh-tickets.json"

WIKI_SAFETY_CHECKS = {
    "finance-agent-wiki": [
        "Keep the output educational, research-oriented, or simulation-oriented.",
        "Do not introduce personalized investment advice.",
        "Do not introduce autonomous real-money execution.",
        "Keep human confirmation before high-risk financial use.",
    ],
    "customs-agent-wiki": [
        "Do not invent document values or customs classifications.",
        "Keep OCR uncertainty, evidence snippets, confidence, and manual review points visible.",
        "Treat policy, tariff, HS code, and regulatory claims as source-gated.",
    ],
    "coding-agent-wiki": [
        "Do not record secrets, tokens, cookies, private keys, or private repository data.",
        "Keep dependency, API, CLI, platform, and security-advisory claims source-gated.",
        "Preserve test and deployment verification commands.",
    ],
    "agent-engineering-wiki": [
        "Do not add hidden instructions or unreviewed agent authority.",
        "Keep model, API, MCP, tool schema, and platform behavior source-gated.",
        "Preserve eval and source-grounding requirements.",
    ],
    "ecommerce-agent-wiki": [
        "Do not invent price, stock, shipping, return policy, or platform policy.",
        "Respect privacy, consent, consumer protection, and platform rules.",
        "Keep unsupported product claims out of stable pages.",
    ],
    "nodeops-agent-wiki": [
        "Require backup, rollback, and human confirmation for production changes.",
        "Do not record infrastructure secrets, node keys, mnemonics, or account tokens.",
        "Keep destructive operations out of automated instructions.",
    ],
    "airdrop-agent-wiki": [
        "Never request or store private keys, seed phrases, cookies, or session tokens.",
        "Do not add Sybil evasion, fake identity, spam, or platform-rule bypass guidance.",
        "Require human review before wallet signing or permission changes.",
    ],
    "content-agent-wiki": [
        "Do not fabricate citations, quotes, current events, or statistics.",
        "Keep licensing, platform rules, and factual claims source-gated.",
        "Separate fact, inference, opinion, and draft language.",
    ],
    "legal-agent-wiki": [
        "Do not introduce final legal opinions or guaranteed outcomes.",
        "Preserve jurisdiction, date, source, and lawyer review points.",
        "Keep statutes, cases, regulations, and platform terms source-gated.",
    ],
    "health-agent-wiki": [
        "Do not introduce diagnosis, prescription, dosing, or treatment orders.",
        "Preserve clinician review and urgent-care escalation points.",
        "Keep guidelines, drug labels, contraindications, and safety warnings source-gated.",
    ],
    "research-agent-wiki": [
        "Do not fabricate citations, abstracts, datasets, benchmark results, or model claims.",
        "Keep source traceability, limitations, and uncertainty visible.",
        "Mark newest papers, datasets, leaderboards, and repositories as source-gated.",
    ],
    "security-agent-wiki": [
        "Defensive review only.",
        "Do not add exploitation, persistence, evasion, credential theft, bypass steps, or payloads.",
        "Keep CVEs, advisories, patches, dependency versions, and exploit status source-gated.",
    ],
}

EVIDENCE_FIELDS = [
    "task_id",
    "ticket_id",
    "topic",
    "status",
    "verified_on",
    "source_title",
    "source_publisher",
    "source_url_or_reference",
    "source_published_or_updated",
    "source_accessed_on",
    "evidence_summary",
    "affected_pages",
    "confidence",
    "remaining_uncertainty",
    "human_reviewer",
    "follow_up",
]

POST_COMMANDS = [
    "python3 scripts/list_source_updates.py",
    "python3 scripts/generate_source_refresh_playbook.py",
    "python3 scripts/generate_source_refresh_tickets.py",
    "python3 scripts/generate_source_refresh_logs.py",
    "python3 scripts/audit_source_refresh_completion.py",
    "python3 scripts/update_index.py",
    "python3 scripts/run_acceptance.py",
]


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def rel_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def ticket_window(wave: str) -> str:
    if wave == "wave-1":
        return "refresh first; do not use for current-fact answers until verified"
    if wave == "wave-2":
        return "refresh after wave-1 before operational rollout"
    return "batch refresh is acceptable before broad reuse"


def evidence_template(task: dict, ticket_id: str) -> dict:
    return {
        "task_id": task.get("task_id", ""),
        "ticket_id": ticket_id,
        "topic": task.get("topic", ""),
        "status": "pending | verified | unchanged | still-needs-source-update | rejected",
        "verified_on": "YYYY-MM-DD",
        "source_title": "<source title>",
        "source_publisher": "<official publisher or authority>",
        "source_url_or_reference": "<URL or local reference>",
        "source_published_or_updated": "YYYY-MM-DD | unknown",
        "source_accessed_on": "YYYY-MM-DD",
        "evidence_summary": "<what the source supports and what it does not support>",
        "affected_pages": [task.get("source_notes_path", "")],
        "confidence": "low | medium | high",
        "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
        "human_reviewer": "<required for high-risk tickets>",
        "follow_up": "<next action or none>",
    }


def source_policy(task: dict) -> list[str]:
    sources = task.get("suggested_sources", [])
    policy = [
        "Prefer official, primary, dated sources.",
        "Do not use unsourced summaries as the only authority.",
        "Record publication/update date and access date.",
    ]
    if sources:
        policy.insert(1, f"Start from suggested source types: {', '.join(sources)}.")
    if task.get("human_confirmation_required"):
        policy.append("Require human review before moving this ticket to verified.")
    return policy


def content_targets(task: dict) -> list[str]:
    wiki = task.get("wiki", "")
    return [
        task.get("source_notes_path", f"wikis/{wiki}/sources/source-notes.md"),
        f"wikis/{wiki}/sources/source-refresh-log.md",
        f"wikis/{wiki}/update-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "registry/source-update-queue.json",
    ]


def ticket_record(task: dict) -> dict:
    task_id = task.get("task_id", "")
    ticket_id = f"TICKET-{task_id}" if task_id else "TICKET-UNKNOWN"
    wiki = task.get("wiki", "")
    return {
        "ticket_id": ticket_id,
        "task_id": task_id,
        "status": "open_pending_source_refresh",
        "wave": task.get("wave", ""),
        "target_window": ticket_window(task.get("wave", "")),
        "wiki": wiki,
        "domain": task.get("domain", ""),
        "risk_level": task.get("risk_level", ""),
        "freshness_requirement": task.get("freshness_requirement", ""),
        "priority_score": task.get("priority_score", 0),
        "category": task.get("category", ""),
        "topic": task.get("topic", ""),
        "source_policy": source_policy(task),
        "suggested_sources": task.get("suggested_sources", []),
        "required_reading": [
            f"wikis/{wiki}/AGENTS.md",
            f"wikis/{wiki}/manifest.yaml",
            f"wikis/{wiki}/README.md",
            f"wikis/{wiki}/rules/",
            task.get("source_notes_path", f"wikis/{wiki}/sources/source-notes.md"),
        ],
        "content_targets": content_targets(task),
        "verification_steps": task.get("verification_steps", []),
        "acceptance_criteria": task.get("acceptance_criteria", []),
        "safety_checks": WIKI_SAFETY_CHECKS.get(wiki, ["Keep current facts source-gated and preserve human review points."]),
        "evidence_fields": EVIDENCE_FIELDS,
        "evidence_template": evidence_template(task, ticket_id),
        "post_update_commands": POST_COMMANDS,
        "human_confirmation_required": bool(task.get("human_confirmation_required")),
    }


def build_tickets() -> dict:
    playbook = read_json(PLAYBOOK_JSON)
    tasks = playbook.get("tasks", [])
    tickets = [ticket_record(task) for task in tasks]
    missing_required = []
    for ticket in tickets:
        if not ticket["ticket_id"] or not ticket["wiki"] or not ticket["topic"]:
            missing_required.append(ticket.get("ticket_id", "unknown"))
    return {
        "generated": date.today().isoformat(),
        "passed": not missing_required,
        "playbook": PLAYBOOK_JSON.relative_to(ROOT).as_posix(),
        "ticket_count": len(tickets),
        "wave_counts": dict(sorted(Counter(ticket["wave"] for ticket in tickets).items())),
        "wiki_counts": dict(sorted(Counter(ticket["wiki"] for ticket in tickets).items())),
        "category_counts": dict(sorted(Counter(ticket["category"] for ticket in tickets).items())),
        "missing_required": missing_required,
        "tickets": tickets,
    }


def checkbox_list(items: list[str]) -> list[str]:
    if not items:
        return ["- [ ] none"]
    return [f"- [ ] {item}" for item in items]


def bullet_list(items: list[str]) -> list[str]:
    if not items:
        return ["- none"]
    return [f"- {item}" for item in items]


def markdown_report(data: dict) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for ticket in data["tickets"]:
        grouped[ticket["wave"]].append(ticket)

    lines = [
        "# Source Refresh Tickets",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        "These tickets turn source-refresh tasks into executable verification work. They do not verify or certify current facts by themselves.",
        "",
        "## Summary",
        "",
        f"- Tickets: {data['ticket_count']}",
        f"- Playbook: `{data['playbook']}`",
        f"- Passed structural check: {'yes' if data['passed'] else 'no'}",
        "",
        "## How To Execute A Ticket",
        "",
        "- Read the required wiki files before searching or editing.",
        "- Collect authoritative dated evidence for the exact topic and scope.",
        "- Decide whether the topic is verified, unchanged, still needs source update, or rejected.",
        "- Record evidence with `scripts/record_source_evidence.py` or manually in the wiki's `sources/source-refresh-log.md`.",
        "- Update only the minimal affected pages, then run the post-update commands.",
        "",
        "## Ticket Index",
        "",
        "| Ticket | Wave | Wiki | Priority | Category | Human confirmation | Topic |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for ticket in data["tickets"]:
        human = "yes" if ticket["human_confirmation_required"] else "no"
        lines.append(
            f"| {ticket['ticket_id']} | {ticket['wave']} | {ticket['wiki']} | {ticket['priority_score']} | "
            f"{ticket['category']} | {human} | {ticket['topic']} |"
        )

    lines.extend(["", "## Tickets", ""])
    for wave in ["wave-1", "wave-2", "wave-3"]:
        lines.extend([f"### {wave}", ""])
        if not grouped.get(wave):
            lines.extend(["No tickets in this wave.", ""])
            continue
        for ticket in grouped[wave]:
            lines.extend(
                [
                    f"#### {ticket['ticket_id']} - {ticket['wiki']}",
                    "",
                    f"- Status: `{ticket['status']}`",
                    f"- Topic: {ticket['topic']}",
                    f"- Category: `{ticket['category']}`",
                    f"- Target window: {ticket['target_window']}",
                    f"- Human confirmation required: {'yes' if ticket['human_confirmation_required'] else 'no'}",
                    "",
                    "Required reading:",
                    "",
                    *bullet_list([rel_link(path) for path in ticket["required_reading"]]),
                    "",
                    "Source policy:",
                    "",
                    *checkbox_list(ticket["source_policy"]),
                    "",
                    "Safety checks:",
                    "",
                    *checkbox_list(ticket["safety_checks"]),
                    "",
                    "Acceptance criteria:",
                    "",
                    *checkbox_list(ticket["acceptance_criteria"]),
                    "",
                    "Content targets:",
                    "",
                    *bullet_list([rel_link(path) if path.startswith("wikis/") else f"`{path}`" for path in ticket["content_targets"]]),
                    "",
                    "Evidence template:",
                    "",
                    "```json",
                    json.dumps(ticket["evidence_template"], ensure_ascii=False, indent=2),
                    "```",
                    "",
                ]
            )

    lines.extend(
        [
            "## Post-Update Commands",
            "",
            "```bash",
            *POST_COMMANDS,
            "```",
            "",
            "## Safety Boundary",
            "",
            "- Do not write current prices, policies, laws, medical guidance, platform rules, API parameters, CVEs, or Web3 project facts without dated source evidence.",
            "- Do not record API keys, private keys, cookies, credentials, seed phrases, or private account data.",
            "- Keep human confirmation points for high-risk finance, legal, health, security, airdrop, and operations tasks.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(data: dict) -> None:
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def filtered(data: dict, wiki: str | None, wave: str | None, ticket_id: str | None) -> dict:
    tickets = data["tickets"]
    if wiki:
        tickets = [ticket for ticket in tickets if ticket["wiki"] == wiki]
    if wave:
        tickets = [ticket for ticket in tickets if ticket["wave"] == wave]
    if ticket_id:
        tickets = [ticket for ticket in tickets if ticket["ticket_id"] == ticket_id or ticket["task_id"] == ticket_id]
    result = dict(data)
    result["tickets"] = tickets
    result["ticket_count"] = len(tickets)
    return result


def main() -> int:
    parser = ArgumentParser(description="Generate source refresh execution tickets.")
    parser.add_argument("--wiki", help="Print tickets for one wiki after generating outputs.")
    parser.add_argument("--wave", choices=["wave-1", "wave-2", "wave-3"], help="Print tickets for one wave after generating outputs.")
    parser.add_argument("--ticket-id", help="Print one ticket by ticket id or task id after generating outputs.")
    parser.add_argument("--json", action="store_true", help="Print filtered tickets as JSON after generating outputs.")
    args = parser.parse_args()

    data = build_tickets()
    write_outputs(data)
    subset = filtered(data, args.wiki, args.wave, args.ticket_id)

    if args.json:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}", file=sys.stderr)
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}", file=sys.stderr)
        print(f"SOURCE REFRESH TICKETS GENERATED ({data['ticket_count']} tickets)", file=sys.stderr)
        print(json.dumps(subset, ensure_ascii=False, indent=2))
    else:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
        print(f"SOURCE REFRESH TICKETS GENERATED ({data['ticket_count']} tickets)")
        if args.wiki or args.wave or args.ticket_id:
            print(markdown_report(subset))

    if not data["passed"]:
        print(f"Missing required fields: {data['missing_required']}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
