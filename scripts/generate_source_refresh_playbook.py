#!/usr/bin/env python3
"""Generate an operational playbook for source-update topics."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
QUEUE_JSON = ROOT / "registry" / "source-update-queue.json"
DOCS_OUT = ROOT / "docs" / "SOURCE_REFRESH_PLAYBOOK.md"
JSON_OUT = ROOT / "registry" / "source-refresh-playbook.json"

HIGH_RISK_WIKIS = {
    "finance-agent-wiki",
    "legal-agent-wiki",
    "health-agent-wiki",
    "security-agent-wiki",
    "airdrop-agent-wiki",
    "nodeops-agent-wiki",
}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def source_notes_path(wiki: str) -> str:
    return f"wikis/{wiki}/sources/source-notes.md"


def task_wave(priority_score: int) -> str:
    if priority_score >= 8:
        return "wave-1"
    if priority_score >= 7:
        return "wave-2"
    return "wave-3"


def source_category(topic: str) -> str:
    text = topic.casefold()
    if any(word in text for word in ["price", "ohlcv", "order book", "rate", "fee", "stock", "eta"]):
        return "market_or_platform_data"
    if any(word in text for word in ["law", "legal", "regulation", "regulatory", "statute", "policy", "rule"]):
        return "policy_or_regulation"
    if any(word in text for word in ["cve", "patch", "advisory", "vulnerab", "security"]):
        return "security_advisory"
    if any(word in text for word in ["clinical", "drug", "dosage", "health", "medical"]):
        return "medical_guidance"
    if any(word in text for word in ["tge", "airdrop", "token", "contract", "wallet", "snapshot"]):
        return "web3_project_status"
    if any(word in text for word in ["api", "sdk", "model", "tool", "framework", "cli"]):
        return "technical_docs"
    return "general_current_fact"


def verification_steps(item: dict) -> list[str]:
    sources = item.get("suggested_sources", [])
    steps = [
        "Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.",
        "Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.",
        "Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.",
        "Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.",
        "Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.",
        "Run validation, source queue generation, search index update, and acceptance checks after edits.",
    ]
    if sources:
        steps.insert(1, f"Start with suggested source types: {', '.join(sources)}.")
    if item.get("wiki") in HIGH_RISK_WIKIS:
        steps.insert(1, "Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.")
    return steps


def acceptance_criteria(item: dict) -> list[str]:
    criteria = [
        "No current fact is written without a dated source note.",
        "No API key, private key, cookie, credential, or private account data is recorded.",
        "Any remaining uncertainty is explicitly marked needs-source-update.",
        "The relevant update-log.md records the change.",
    ]
    wiki = item.get("wiki")
    if wiki == "finance-agent-wiki":
        criteria.append("No personalized investment advice or autonomous real-money execution is introduced.")
    elif wiki == "legal-agent-wiki":
        criteria.append("No final legal opinion is introduced; jurisdiction and lawyer review points remain visible.")
    elif wiki == "health-agent-wiki":
        criteria.append("No diagnosis or treatment instruction is introduced; clinician confirmation points remain visible.")
    elif wiki == "security-agent-wiki":
        criteria.append("No exploit, persistence, evasion, credential theft, or offensive procedure is introduced.")
    elif wiki == "airdrop-agent-wiki":
        criteria.append("No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.")
    return criteria


def task_record(index: int, item: dict) -> dict:
    priority = int(item.get("priority_score", 0))
    wiki = item.get("wiki", "")
    return {
        "task_id": f"SRC-{index:03d}",
        "wave": task_wave(priority),
        "wiki": wiki,
        "domain": item.get("domain", ""),
        "risk_level": item.get("risk_level", ""),
        "freshness_requirement": item.get("freshness_requirement", ""),
        "priority_score": priority,
        "category": source_category(item.get("topic", "")),
        "topic": item.get("topic", ""),
        "status": "pending_source_refresh",
        "source_notes_path": source_notes_path(wiki),
        "suggested_sources": item.get("suggested_sources", []),
        "last_checked": item.get("last_checked", ""),
        "human_confirmation_required": item.get("risk_level") == "high" or wiki in HIGH_RISK_WIKIS,
        "verification_steps": verification_steps(item),
        "acceptance_criteria": acceptance_criteria(item),
        "post_update_commands": [
            "python3 scripts/list_source_updates.py",
            "python3 scripts/generate_source_refresh_playbook.py",
            "python3 scripts/generate_source_refresh_tickets.py",
            "python3 scripts/generate_source_refresh_logs.py",
            "python3 scripts/audit_source_refresh_completion.py",
            "python3 scripts/update_index.py",
            "python3 scripts/run_acceptance.py",
        ],
    }


def build_playbook() -> dict:
    queue = read_json(QUEUE_JSON)
    topics = queue.get("topics", [])
    tasks = [task_record(index, item) for index, item in enumerate(topics, start=1)]
    wave_counts = Counter(task["wave"] for task in tasks)
    wiki_counts = Counter(task["wiki"] for task in tasks)
    category_counts = Counter(task["category"] for task in tasks)
    return {
        "generated": date.today().isoformat(),
        "source_queue": QUEUE_JSON.relative_to(ROOT).as_posix(),
        "task_count": len(tasks),
        "wave_counts": dict(sorted(wave_counts.items())),
        "wiki_counts": dict(sorted(wiki_counts.items())),
        "category_counts": dict(sorted(category_counts.items())),
        "tasks": tasks,
    }


def markdown_report(playbook: dict) -> str:
    tasks = playbook["tasks"]
    by_wave: dict[str, list[dict]] = defaultdict(list)
    for task in tasks:
        by_wave[task["wave"]].append(task)

    lines = [
        "# Source Refresh Playbook",
        "",
        f"Generated: {playbook['generated']}",
        "",
        "## Purpose",
        "",
        "This playbook turns `needs-source-update` topics into source verification tasks. It does not certify any current fact by itself.",
        "",
        "## Summary",
        "",
        f"- Tasks: {playbook['task_count']}",
        f"- Source queue: `{playbook['source_queue']}`",
        "",
        "## Waves",
        "",
        "| Wave | Tasks | Meaning |",
        "| --- | ---: | --- |",
        f"| wave-1 | {playbook['wave_counts'].get('wave-1', 0)} | Highest risk or freshness pressure; refresh first. |",
        f"| wave-2 | {playbook['wave_counts'].get('wave-2', 0)} | Important operational topics; refresh after wave-1. |",
        f"| wave-3 | {playbook['wave_counts'].get('wave-3', 0)} | Medium cadence topics; batch refresh is acceptable. |",
        "",
        "## Task List",
        "",
        "| Task | Wave | Wiki | Priority | Category | Human confirmation | Topic |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for task in tasks:
        human = "yes" if task["human_confirmation_required"] else "no"
        lines.append(
            f"| {task['task_id']} | {task['wave']} | {task['wiki']} | {task['priority_score']} | "
            f"{task['category']} | {human} | {task['topic']} |"
        )

    lines.extend(["", "## Wave Details", ""])
    for wave in ["wave-1", "wave-2", "wave-3"]:
        lines.extend([f"### {wave}", ""])
        if not by_wave.get(wave):
            lines.extend(["No tasks in this wave.", ""])
            continue
        for task in by_wave[wave]:
            sources = ", ".join(task["suggested_sources"]) if task["suggested_sources"] else "source needed"
            lines.extend(
                [
                    f"#### {task['task_id']} - {task['wiki']}",
                    "",
                    f"- Topic: {task['topic']}",
                    f"- Category: {task['category']}",
                    f"- Source notes: `{task['source_notes_path']}`",
                    f"- Suggested sources: {sources}",
                    f"- Human confirmation required: {'yes' if task['human_confirmation_required'] else 'no'}",
                    "",
                    "Verification steps:",
                ]
            )
            for step in task["verification_steps"]:
                lines.append(f"- {step}")
            lines.extend(["", "Acceptance criteria:"])
            for criterion in task["acceptance_criteria"]:
                lines.append(f"- {criterion}")
            lines.append("")

    lines.extend(
        [
            "## Completion Commands",
            "",
            "```bash",
            "python3 scripts/list_source_updates.py",
            "python3 scripts/generate_source_refresh_playbook.py",
            "python3 scripts/generate_source_refresh_tickets.py",
            "python3 scripts/generate_source_refresh_logs.py",
            "python3 scripts/audit_source_refresh_completion.py",
            "python3 scripts/update_index.py",
            "python3 scripts/run_acceptance.py",
            "```",
            "",
            "## Safety Boundary",
            "",
            "- Do not use this playbook to invent current prices, policies, laws, medical guidance, platform rules, API parameters, CVEs, or Web3 project facts.",
            "- Do not write secrets, credentials, cookies, private keys, or private account data into any wiki or report.",
            "- High-risk domains keep human confirmation points even after source refresh is complete.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    playbook = build_playbook()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(playbook), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(playbook, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"SOURCE REFRESH PLAYBOOK GENERATED ({playbook['task_count']} tasks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
