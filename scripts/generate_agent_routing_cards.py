#!/usr/bin/env python3
"""Generate human and machine readable routing cards for every wiki."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
PACKS = ROOT / "packs"
REGISTRY = ROOT / "registry"
DOCS_OUT = ROOT / "docs" / "AGENT_ROUTING_CARDS.md"
JSON_OUT = REGISTRY / "agent-routing-cards.json"

REPORTS = {
    "agent_handoff": "docs/AGENT_HANDOFF.md",
    "acceptance": "docs/ACCEPTANCE_REPORT.md",
    "hub_navigation": "docs/HUB_NAVIGATION.md",
    "routing_cli": "docs/ROUTING_CLI.md",
    "source_queue": "docs/SOURCE_UPDATE_QUEUE.md",
    "source_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_playbook": "docs/SOURCE_REFRESH_PLAYBOOK.md",
    "source_tickets": "docs/SOURCE_REFRESH_TICKETS.md",
    "source_wave_runner": "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
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
    "source_completion_audit": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
    "source_log_status": "docs/SOURCE_REFRESH_LOG_STATUS.md",
    "safety_audit": "docs/SAFETY_AUDIT.md",
    "pack_audit": "docs/PACK_AUDIT.md",
}

DOMAIN_GUIDANCE = {
    "finance-agent-wiki": {
        "summary": "Finance research, accounting analysis, market data, backtesting, risk control, and simulated trading systems.",
        "example_intents": [
            "Explain OHLCV, spread, order book, volume, and liquidity for research use.",
            "Design a paper-trading backtest with fee, slippage, and out-of-sample checks.",
            "Review a finance answer for personalized-investment-advice or real-money execution risk.",
        ],
        "safety_rules": [
            "Educational, research, and simulation use only.",
            "Do not provide personalized investment advice.",
            "Default to paper trading or human-approved simulation.",
            "Require human confirmation before any high-risk financial action.",
        ],
        "prohibited_actions": [
            "Autonomous real-money order placement.",
            "Personalized buy, sell, hold, leverage, or allocation instructions.",
            "Claims about current prices, rates, exchange rules, or market conditions without source refresh.",
        ],
        "default_query": "risk control",
    },
    "customs-agent-wiki": {
        "summary": "Trade document extraction, invoice and packing-list comparison, field mapping, validation, and review support.",
        "example_intents": [
            "Extract contract, invoice, packing list, inspection, and guarantee fields into JSON.",
            "Map English headers to Chinese document fields with confidence and evidence.",
            "Compare amount, currency, package count, gross weight, net weight, product name, and specification differences.",
        ],
        "safety_rules": [
            "Treat outputs as structured review support, not final customs advice.",
            "Preserve source snippets, confidence, and unresolved fields.",
            "Flag policy, tariff, HS code, and regulatory questions as source-update topics.",
            "Require manual review for medium and high risk discrepancies.",
        ],
        "prohibited_actions": [
            "Inventing missing document values.",
            "Presenting current customs policy or legal classification as verified without authoritative sources.",
            "Hiding OCR uncertainty or document conflicts.",
        ],
        "default_query": "field extraction",
    },
    "coding-agent-wiki": {
        "summary": "Software engineering workflows for clarification, minimal implementation, tests, debugging, deployment, and secure coding.",
        "example_intents": [
            "Clarify requirements and implement the smallest safe code change.",
            "Plan a test-first debugging workflow and regression check.",
            "Review deployment steps, secret handling, and Codex usage rules.",
        ],
        "safety_rules": [
            "Read repository instructions before editing.",
            "Preserve user changes and keep edits scoped.",
            "Protect secrets, tokens, cookies, and private keys.",
            "Run relevant tests or explain why they could not run.",
        ],
        "prohibited_actions": [
            "Writing credentials into source files or logs.",
            "Discarding unrelated user changes.",
            "Skipping safety checks for deployment or destructive operations.",
        ],
        "default_query": "test first debug deployment secrets",
    },
    "agent-engineering-wiki": {
        "summary": "Agent architecture, RAG, Knowledge Packs, Codex Skills, evals, source grounding, and safety boundaries.",
        "example_intents": [
            "Design an agent as model plus tools plus knowledge plus workflow plus memory plus evals plus safety boundary.",
            "Build a RAG workflow with chunking, indexing, recall, reranking, citations, and evals.",
            "Define a Knowledge Pack with manifest, rules, workflows, evals, sources, and update logs.",
        ],
        "safety_rules": [
            "Make instructions explicit and auditable.",
            "Do not add hidden instructions, secrets, or credentials.",
            "Use source-grounding tests for current or externally sourced facts.",
            "Keep evals tied to observable behavior and refusal boundaries.",
        ],
        "prohibited_actions": [
            "Embedding hidden behavior or unreviewed authority into packs.",
            "Claiming current model, API, MCP, or platform facts without source refresh.",
            "Skipping evals for safety-critical agent behavior.",
        ],
        "default_query": "RAG source grounding evals",
    },
    "ecommerce-agent-wiki": {
        "summary": "Product catalog, SKU and SPU operations, customer service, recommendation constraints, returns, privacy, and platform policy gates.",
        "example_intents": [
            "Normalize product catalog attributes and SKU data.",
            "Draft a customer support workflow for returns, refunds, logistics, and invoices.",
            "Review recommendation output for policy, consent, and privacy risk.",
        ],
        "safety_rules": [
            "Respect privacy, consent, consumer protection, and platform rules.",
            "Mark fees, return policies, ads policy, and platform rules as source-update topics.",
            "Avoid deceptive claims, fake scarcity, or unsupported product promises.",
        ],
        "prohibited_actions": [
            "Inventing product availability, current pricing, or platform policy.",
            "Using private customer data without a clear need and consent basis.",
            "Generating manipulative or misleading sales tactics.",
        ],
        "default_query": "customer service returns privacy",
    },
    "nodeops-agent-wiki": {
        "summary": "Linux, Docker, systemd, logs, backups, monitoring, alerts, node operations, incident review, and rollback support.",
        "example_intents": [
            "Build an incident triage checklist using symptoms, logs, resources, network, and dependencies.",
            "Plan a backup and rollback gate before a production change.",
            "Review Docker or systemd operations for destructive-command risk.",
        ],
        "safety_rules": [
            "Require backup and rollback planning before production changes.",
            "Require human confirmation for destructive or irreversible operations.",
            "Prefer read-only diagnostics before changes.",
            "Protect credentials, node keys, and private infrastructure details.",
        ],
        "prohibited_actions": [
            "Running destructive production commands without confirmation.",
            "Exposing private keys, mnemonics, tokens, or infrastructure secrets.",
            "Treating current install commands, versions, or chain rules as stable facts without source refresh.",
        ],
        "default_query": "backup rollback monitoring",
    },
    "airdrop-agent-wiki": {
        "summary": "Web3 project research, public task tracking, token and airdrop safety checks, wallet hygiene, and compliance boundaries.",
        "example_intents": [
            "Research a project using official docs and public ecosystem signals.",
            "Create a wallet-safety checklist before signing a transaction.",
            "Review an airdrop task plan for Sybil, spam, fake identity, or platform-bypass risk.",
        ],
        "safety_rules": [
            "Public research and safety checks only.",
            "Never request or store private keys, seed phrases, cookies, or session tokens.",
            "Flag project funding, TGE, tokenomics, eligibility, and rules as source-update topics.",
            "Require human review before signing or granting wallet permissions.",
        ],
        "prohibited_actions": [
            "Sybil evasion, spam, fake identity, or platform-rule bypass.",
            "Automating wallet actions that risk assets or account bans.",
            "Promising rewards or treating current airdrop rules as verified without source refresh.",
        ],
        "default_query": "wallet safety public tasks",
    },
    "content-agent-wiki": {
        "summary": "Research briefs, newsletters, articles, posts, titles, summaries, style templates, fact checking, and publishing review.",
        "example_intents": [
            "Turn source notes into a research brief with citations and uncertainty labels.",
            "Create a publishing checklist for style, claims, and platform fit.",
            "Review content for plagiarism, missing citations, or unsupported claims.",
        ],
        "safety_rules": [
            "Separate facts, inference, opinion, and draft language.",
            "Cite sources for factual claims and mark current facts for source refresh.",
            "Avoid plagiarism and undisclosed copied text.",
        ],
        "prohibited_actions": [
            "Fabricating citations or current events.",
            "Publishing private, confidential, or copyrighted material without permission.",
            "Treating platform policy or trend claims as stable without source refresh.",
        ],
        "default_query": "fact checking citations",
    },
    "legal-agent-wiki": {
        "summary": "Legal information support, contract review checklists, risk spotting, issue lists, and lawyer handoff preparation.",
        "example_intents": [
            "Extract contract parties, obligations, deadlines, termination, liability, and dispute clauses.",
            "Create a legal-risk checklist for human counsel review.",
            "Summarize unresolved legal questions and source-update needs by jurisdiction.",
        ],
        "safety_rules": [
            "Information and checklist support only.",
            "Do not provide final legal opinions.",
            "Require jurisdiction, date, and authoritative source checks for law or regulation.",
            "Escalate high-risk legal decisions to qualified counsel.",
        ],
        "prohibited_actions": [
            "Final legal advice or guaranteed outcomes.",
            "Inventing statutes, cases, regulatory status, or filing requirements.",
            "Removing attorney review points from high-risk outputs.",
        ],
        "default_query": "contract review human counsel",
    },
    "health-agent-wiki": {
        "summary": "Health education, wellness explanations, triage-style safety reminders, red flags, and clinician handoff support.",
        "example_intents": [
            "Explain a health topic in plain language with red-flag reminders.",
            "Create a question list for a clinician visit.",
            "Review an answer for diagnosis, prescription, or medical-guideline freshness risk.",
        ],
        "safety_rules": [
            "Education and triage-style safety reminders only.",
            "Do not diagnose, prescribe, or replace clinician judgment.",
            "Mark guidelines, drug information, and medical recommendations as source-update topics.",
            "Escalate urgent symptoms or red flags to professional care.",
        ],
        "prohibited_actions": [
            "Diagnosis or treatment orders.",
            "Medication dosing or contraindication claims without authoritative source refresh and clinician review.",
            "Suppressing emergency or clinician escalation advice.",
        ],
        "default_query": "red flags clinician review",
    },
    "research-agent-wiki": {
        "summary": "Academic research workflows, paper reading, source grounding, citation hygiene, synthesis, limitations, and reproducibility.",
        "example_intents": [
            "Summarize a paper with claims, method, evidence, limitations, and citation trail.",
            "Build a literature review workflow with source-grounding checks.",
            "Design evals for citation accuracy and unsupported-claim detection.",
        ],
        "safety_rules": [
            "Keep citations traceable to source text.",
            "Label speculation, limitations, and unresolved evidence gaps.",
            "Mark newest papers, datasets, leaderboards, and benchmarks as source-update topics.",
        ],
        "prohibited_actions": [
            "Fabricating citations, abstracts, datasets, or benchmark results.",
            "Presenting weak or unverified evidence as consensus.",
            "Omitting limitations that affect interpretation.",
        ],
        "default_query": "source grounding citations",
    },
    "security-agent-wiki": {
        "summary": "Defensive security review, hardening, secure code review, incident documentation, and risk triage.",
        "example_intents": [
            "Review code for defensive security weaknesses and remediation priorities.",
            "Create a hardening checklist without exploit steps.",
            "Triage security findings while excluding bypass, theft, persistence, or evasion instructions.",
        ],
        "safety_rules": [
            "Defensive review only.",
            "Focus on risk explanation, detection, mitigation, and verification.",
            "Mark current CVEs, exploit status, dependency versions, and advisories as source-update topics.",
            "Require human approval for production security changes.",
        ],
        "prohibited_actions": [
            "Exploitation, persistence, evasion, credential theft, or bypass steps.",
            "Payloads or procedures that enable unauthorized access.",
            "Claims about current vulnerabilities or advisories without source refresh.",
        ],
        "default_query": "defensive security hardening",
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def doc_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def parse_manifest(path: Path) -> dict:
    data: dict[str, object] = {"entrypoints": [], "required_directories": [], "trigger_keywords": []}
    current_list: str | None = None
    for raw in read_text(path).splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw.startswith("  - ") and current_list:
            data.setdefault(current_list, [])
            data[current_list].append(stripped[2:].strip().strip('"'))
            continue
        current_list = None
        if ":" not in raw or raw.startswith(" "):
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"')
        if key in {"entrypoints", "required_directories"}:
            data[key] = []
            current_list = key
        elif key == "trigger_keywords":
            data[key] = re.findall(r'"([^"]+)"', raw)
        else:
            data[key] = value
    return data


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


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def source_task_counts() -> dict[str, int]:
    playbook = read_json(REGISTRY / "source-refresh-playbook.json")
    counts: dict[str, int] = {}
    for task in playbook.get("tasks", []):
        wiki = task.get("wiki")
        if wiki:
            counts[wiki] = counts.get(wiki, 0) + 1
    return counts


def source_topic_counts() -> dict[str, int]:
    queue = read_json(REGISTRY / "source-update-queue.json")
    counts: dict[str, int] = {}
    for topic in queue.get("topics", []):
        wiki = topic.get("wiki")
        if wiki:
            counts[wiki] = counts.get(wiki, 0) + 1
    return counts


def existing_path(repo_path: str) -> str:
    path = ROOT / repo_path
    return repo_path if path.exists() else ""


def wiki_card(wiki: Path, registry_record: dict, task_counts: dict[str, int], topic_counts: dict[str, int]) -> dict:
    wiki_id = wiki.name
    manifest = parse_manifest(wiki / "manifest.yaml")
    guidance = DOMAIN_GUIDANCE.get(wiki_id, {})
    package = f"packs/{wiki_id}.zip" if (PACKS / f"{wiki_id}.zip").exists() else ""
    read_order = [
        f"wikis/{wiki_id}/AGENTS.md",
        f"wikis/{wiki_id}/manifest.yaml",
        f"wikis/{wiki_id}/README.md",
        f"wikis/{wiki_id}/rules/",
        f"wikis/{wiki_id}/workflows/",
    ]
    source_gates = [
        f"wikis/{wiki_id}/sources/source-notes.md",
        f"wikis/{wiki_id}/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
    ]
    return {
        "id": wiki_id,
        "name": manifest.get("name", wiki_id),
        "domain": manifest.get("domain") or registry_record.get("domain", ""),
        "priority": registry_record.get("priority", ""),
        "risk_level": manifest.get("risk_level") or registry_record.get("risk_level", ""),
        "freshness_requirement": manifest.get("freshness_requirement") or registry_record.get("freshness", ""),
        "summary": guidance.get("summary", str(manifest.get("description", ""))),
        "trigger_keywords": manifest.get("trigger_keywords", []),
        "example_intents": guidance.get("example_intents", []),
        "required_reading_order": [path for path in read_order if existing_path(path)],
        "source_gates": [path for path in source_gates if existing_path(path)],
        "source_update_topic_count": topic_counts.get(wiki_id, 0),
        "source_refresh_task_count": task_counts.get(wiki_id, 0),
        "safety_rules": guidance.get("safety_rules", []),
        "prohibited_actions": guidance.get("prohibited_actions", []),
        "validation_commands": [
            "python3 scripts/validate_wiki.py",
            "python3 scripts/update_index.py",
            f'python3 scripts/search_wiki.py --query "{guidance.get("default_query", "core rules")}" --wiki {wiki_id}',
            "python3 scripts/run_acceptance.py",
        ],
        "package": package,
    }


def build_cards() -> dict:
    registry = parse_registry(REGISTRY / "wiki-registry.yaml")
    task_counts = source_task_counts()
    topic_counts = source_topic_counts()
    ordered_ids = list(registry)
    seen: set[str] = set()
    cards: list[dict] = []
    for wiki_id in ordered_ids:
        wiki = WIKIS / wiki_id
        if wiki.is_dir():
            cards.append(wiki_card(wiki, registry.get(wiki_id, {}), task_counts, topic_counts))
            seen.add(wiki_id)
    for wiki in sorted(WIKIS.iterdir()):
        if wiki.is_dir() and wiki.name not in seen:
            cards.append(wiki_card(wiki, registry.get(wiki.name, {}), task_counts, topic_counts))
    return {
        "generated": date.today().isoformat(),
        "card_count": len(cards),
        "reports": REPORTS,
        "cards": cards,
    }


def bullet_list(items: list[str], empty: str = "-") -> list[str]:
    if not items:
        return [empty]
    return [f"- {item}" for item in items]


def link_list(paths: list[str]) -> str:
    if not paths:
        return "-"
    return ", ".join(doc_link(path) for path in paths)


def markdown_report(data: dict) -> str:
    cards = data["cards"]
    lines = [
        "# Agent Routing Cards",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        "These cards tell an agent which wiki to read, what order to read it in, where current facts are gated, and which actions are outside the allowed boundary.",
        "",
        "## Start Here",
        "",
        f"- Agent handoff: {doc_link(REPORTS['agent_handoff'], 'AGENT_HANDOFF.md')}",
        f"- Hub navigation: {doc_link(REPORTS['hub_navigation'], 'HUB_NAVIGATION.md')}",
        f"- Routing CLI: {doc_link(REPORTS['routing_cli'], 'ROUTING_CLI.md')}",
        f"- Source update queue: {doc_link(REPORTS['source_queue'], 'SOURCE_UPDATE_QUEUE.md')}",
        f"- Source refresh dashboard: {doc_link(REPORTS['source_dashboard'], 'SOURCE_REFRESH_DASHBOARD.md')}",
        f"- Source refresh playbook: {doc_link(REPORTS['source_playbook'], 'SOURCE_REFRESH_PLAYBOOK.md')}",
        f"- Source refresh tickets: {doc_link(REPORTS['source_tickets'], 'SOURCE_REFRESH_TICKETS.md')}",
        f"- Source refresh wave runner: {doc_link(REPORTS['source_wave_runner'], 'SOURCE_REFRESH_WAVE_RUNNER.md')}",
        f"- Source reviewer queue: {doc_link(REPORTS['source_reviewer_queue'], 'SOURCE_REVIEWER_QUEUE.md')}",
        f"- Source review session plan: {doc_link(REPORTS['source_review_session_plan'], 'SOURCE_REVIEW_SESSION_PLAN.md')}",
        f"- Source review readiness matrix: {doc_link(REPORTS['source_review_readiness_matrix'], 'SOURCE_REVIEW_READINESS_MATRIX.md')}",
        f"- Source review work orders: {doc_link(REPORTS['source_review_work_orders'], 'SOURCE_REVIEW_WORK_ORDERS.md')}",
        f"- Source review packet bundle: {doc_link(REPORTS['source_review_packet_bundle'], 'SOURCE_REVIEW_PACKET_BUNDLE.md')}",
        f"- Source review packet audit: {doc_link(REPORTS['source_review_packet_audit'], 'SOURCE_REVIEW_PACKET_AUDIT.md')}",
        f"- Source review packet rehearsal: {doc_link(REPORTS['source_review_packet_rehearsal'], 'SOURCE_REVIEW_PACKET_REHEARSAL.md')}",
        f"- Source evidence recorder: {doc_link(REPORTS['source_evidence_recorder'], 'SOURCE_EVIDENCE_RECORDER.md')}",
        f"- Source evidence packet importer: {doc_link(REPORTS['source_evidence_packet_importer'], 'SOURCE_EVIDENCE_PACKET_IMPORTER.md')}",
        f"- Source evidence packet fixtures: {doc_link(REPORTS['source_evidence_packet_fixtures'], 'SOURCE_EVIDENCE_PACKET_FIXTURES.md')}",
        f"- Source refresh completion audit: {doc_link(REPORTS['source_completion_audit'], 'SOURCE_REFRESH_COMPLETION_AUDIT.md')}",
        f"- Source evidence quality audit: {doc_link(REPORTS['source_evidence_quality'], 'SOURCE_EVIDENCE_QUALITY_AUDIT.md')}",
        f"- Acceptance report: {doc_link(REPORTS['acceptance'], 'ACCEPTANCE_REPORT.md')}",
        f"- Safety audit: {doc_link(REPORTS['safety_audit'], 'SAFETY_AUDIT.md')}",
        "",
        "## Router Table",
        "",
        "| Wiki | Priority | Risk | Freshness | Triggers | Read First |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for card in cards:
        triggers = ", ".join(card["trigger_keywords"]) or "-"
        read_first = link_list(card["required_reading_order"][:3])
        lines.append(
            f"| {doc_link('wikis/' + card['id'], card['id'])} | {card['priority']} | {card['risk_level']} | "
            f"{card['freshness_requirement']} | {triggers} | {read_first} |"
        )

    lines.extend(["", "## Cards", ""])
    for card in cards:
        lines.extend(
            [
                f"### {card['id']}",
                "",
                f"- Domain: `{card['domain']}`",
                f"- Priority: `{card['priority']}`",
                f"- Risk level: `{card['risk_level']}`",
                f"- Freshness requirement: `{card['freshness_requirement']}`",
                f"- Summary: {card['summary']}",
                f"- Source-update topics: {card['source_update_topic_count']}",
                f"- Source-refresh tasks: {card['source_refresh_task_count']}",
                f"- Package: {doc_link(card['package']) if card['package'] else 'missing until package generation runs'}",
                "",
                "Required reading order:",
                "",
                *bullet_list([doc_link(path) for path in card["required_reading_order"]]),
                "",
                "Source gates:",
                "",
                *bullet_list([doc_link(path) for path in card["source_gates"]]),
                "",
                "Example intents:",
                "",
                *bullet_list(card["example_intents"]),
                "",
                "Safety rules:",
                "",
                *bullet_list(card["safety_rules"]),
                "",
                "Do not do:",
                "",
                *bullet_list(card["prohibited_actions"]),
                "",
                "Validation commands:",
                "",
                "```bash",
                *card["validation_commands"],
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "## Global Routing Rules",
            "",
            "- Read root `AGENTS.md` before using or editing any wiki.",
            "- For a specific domain task, read that wiki's `AGENTS.md`, `manifest.yaml`, `README.md`, `rules/`, then `workflows/`.",
            "- For high-risk domains, read `rules/` before `workflows/` and keep human confirmation points in the output.",
            "- Treat current prices, policies, laws, medical guidance, security advisories, platform rules, API parameters, and Web3 project rules as `needs-source-update` unless verified from authoritative sources.",
            "- Do not add credentials, API keys, private keys, cookies, hidden instructions, or unsafe operational steps.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_cards()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"AGENT ROUTING CARDS GENERATED ({data['card_count']} cards)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
