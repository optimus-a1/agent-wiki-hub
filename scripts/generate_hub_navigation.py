#!/usr/bin/env python3
"""Generate a one-page navigation map for Agent Wiki Hub."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
PACKS = ROOT / "packs"
DOCS_OUT = ROOT / "docs" / "HUB_NAVIGATION.md"
JSON_OUT = ROOT / "registry" / "hub-navigation.json"

NAV_DIRS = ["rules", "workflows", "evals", "sources"]
ENTRYPOINTS = ["manifest.yaml", "README.md", "AGENTS.md"]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def parse_manifest(path: Path) -> dict:
    data: dict[str, object] = {"entrypoints": [], "trigger_keywords": []}
    lines = read_text(path).splitlines()
    current_list: str | None = None
    for raw in lines:
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
            data[key] = re.findall(r'"([^"]+)"', value)
        else:
            data[key] = value
    return data


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_link(path: str, label: str | None = None) -> str:
    label = label or Path(path).name
    return f"[{label}](../{path})" if path.startswith("wikis/") or path.startswith("packs/") else f"[{label}](../{path})"


def files_in(wiki: Path, dirname: str) -> list[str]:
    folder = wiki / dirname
    if not folder.exists():
        return []
    suffixes = {".md", ".yaml", ".yml", ".json"}
    return [rel(path) for path in sorted(folder.rglob("*")) if path.is_file() and path.suffix.lower() in suffixes]


def source_task_count(wiki_id: str) -> int:
    path = ROOT / "registry" / "source-refresh-playbook.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    return sum(1 for task in data.get("tasks", []) if task.get("wiki") == wiki_id)


def wiki_record(wiki: Path) -> dict:
    manifest = parse_manifest(wiki / "manifest.yaml")
    wiki_id = wiki.name
    files = {dirname: files_in(wiki, dirname) for dirname in NAV_DIRS}
    pack = PACKS / f"{wiki_id}.zip"
    return {
        "id": wiki_id,
        "name": manifest.get("name", wiki_id),
        "domain": manifest.get("domain", ""),
        "risk_level": manifest.get("risk_level", ""),
        "freshness_requirement": manifest.get("freshness_requirement", ""),
        "trigger_keywords": manifest.get("trigger_keywords", []),
        "entrypoints": [rel(wiki / name) for name in ENTRYPOINTS if (wiki / name).exists()],
        "core_rules": files["rules"],
        "workflows": files["workflows"],
        "evals": files["evals"],
        "source_notes": rel(wiki / "sources" / "source-notes.md") if (wiki / "sources" / "source-notes.md").exists() else "",
        "source_refresh_log": rel(wiki / "sources" / "source-refresh-log.md")
        if (wiki / "sources" / "source-refresh-log.md").exists()
        else "",
        "source_refresh_tasks": source_task_count(wiki_id),
        "pack": rel(pack) if pack.exists() else "",
    }


def build_navigation() -> dict:
    records = [wiki_record(path) for path in sorted(WIKIS.iterdir()) if path.is_dir()]
    return {
        "generated": date.today().isoformat(),
        "wiki_count": len(records),
        "reports": {
            "acceptance": "docs/ACCEPTANCE_REPORT.md",
            "agent_handoff": "docs/AGENT_HANDOFF.md",
            "release_notes": "docs/RELEASE_NOTES.md",
            "change_summary": "docs/CHANGE_SUMMARY.md",
            "routing_cards": "docs/AGENT_ROUTING_CARDS.md",
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
        },
        "wikis": records,
    }


def link_list(paths: list[str], limit: int | None = None) -> str:
    shown = paths[:limit] if limit else paths
    if not shown:
        return "-"
    links = [markdown_link(path) for path in shown]
    if limit and len(paths) > limit:
        links.append(f"+{len(paths) - limit} more")
    return ", ".join(links)


def markdown_report(nav: dict) -> str:
    lines = [
        "# Agent Wiki Hub Navigation",
        "",
        f"Generated: {nav['generated']}",
        "",
        "## Start Here",
        "",
        f"- Agent handoff: {markdown_link(nav['reports']['agent_handoff'], 'AGENT_HANDOFF.md')}",
        f"- Acceptance: {markdown_link(nav['reports']['acceptance'], 'ACCEPTANCE_REPORT.md')}",
        f"- Release notes: {markdown_link(nav['reports']['release_notes'], 'RELEASE_NOTES.md')}",
        f"- Change summary: {markdown_link(nav['reports']['change_summary'], 'CHANGE_SUMMARY.md')}",
        f"- Agent routing cards: {markdown_link(nav['reports']['routing_cards'], 'AGENT_ROUTING_CARDS.md')}",
        f"- Routing CLI: {markdown_link(nav['reports']['routing_cli'], 'ROUTING_CLI.md')}",
        f"- Source update queue: {markdown_link(nav['reports']['source_queue'], 'SOURCE_UPDATE_QUEUE.md')}",
        f"- Source refresh dashboard: {markdown_link(nav['reports']['source_dashboard'], 'SOURCE_REFRESH_DASHBOARD.md')}",
        f"- Source refresh playbook: {markdown_link(nav['reports']['source_playbook'], 'SOURCE_REFRESH_PLAYBOOK.md')}",
        f"- Source refresh tickets: {markdown_link(nav['reports']['source_tickets'], 'SOURCE_REFRESH_TICKETS.md')}",
        f"- Source refresh wave runner: {markdown_link(nav['reports']['source_wave_runner'], 'SOURCE_REFRESH_WAVE_RUNNER.md')}",
        f"- Source reviewer queue: {markdown_link(nav['reports']['source_reviewer_queue'], 'SOURCE_REVIEWER_QUEUE.md')}",
        f"- Source review session plan: {markdown_link(nav['reports']['source_review_session_plan'], 'SOURCE_REVIEW_SESSION_PLAN.md')}",
        f"- Source review readiness matrix: {markdown_link(nav['reports']['source_review_readiness_matrix'], 'SOURCE_REVIEW_READINESS_MATRIX.md')}",
        f"- Source review work orders: {markdown_link(nav['reports']['source_review_work_orders'], 'SOURCE_REVIEW_WORK_ORDERS.md')}",
        f"- Source review packet bundle: {markdown_link(nav['reports']['source_review_packet_bundle'], 'SOURCE_REVIEW_PACKET_BUNDLE.md')}",
        f"- Source review packet audit: {markdown_link(nav['reports']['source_review_packet_audit'], 'SOURCE_REVIEW_PACKET_AUDIT.md')}",
        f"- Source review packet rehearsal: {markdown_link(nav['reports']['source_review_packet_rehearsal'], 'SOURCE_REVIEW_PACKET_REHEARSAL.md')}",
        f"- Source evidence recorder: {markdown_link(nav['reports']['source_evidence_recorder'], 'SOURCE_EVIDENCE_RECORDER.md')}",
        f"- Source evidence packet importer: {markdown_link(nav['reports']['source_evidence_packet_importer'], 'SOURCE_EVIDENCE_PACKET_IMPORTER.md')}",
        f"- Source evidence packet fixtures: {markdown_link(nav['reports']['source_evidence_packet_fixtures'], 'SOURCE_EVIDENCE_PACKET_FIXTURES.md')}",
        f"- Source refresh completion audit: {markdown_link(nav['reports']['source_completion_audit'], 'SOURCE_REFRESH_COMPLETION_AUDIT.md')}",
        f"- Source evidence quality audit: {markdown_link(nav['reports']['source_evidence_quality'], 'SOURCE_EVIDENCE_QUALITY_AUDIT.md')}",
        f"- Source refresh log status: {markdown_link(nav['reports']['source_log_status'], 'SOURCE_REFRESH_LOG_STATUS.md')}",
        f"- Safety audit: {markdown_link(nav['reports']['safety_audit'], 'SAFETY_AUDIT.md')}",
        f"- Package audit: {markdown_link(nav['reports']['pack_audit'], 'PACK_AUDIT.md')}",
        "",
        "## Wiki Matrix",
        "",
        "| Wiki | Domain | Risk | Freshness | Entry Points | Rules | Workflows | Evals | Sources | Pack |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for wiki in nav["wikis"]:
        sources = []
        if wiki["source_notes"]:
            sources.append(markdown_link(wiki["source_notes"], "source-notes"))
        if wiki["source_refresh_log"]:
            sources.append(markdown_link(wiki["source_refresh_log"], "source-refresh-log"))
        if wiki["source_refresh_tasks"]:
            sources.append(f"{wiki['source_refresh_tasks']} refresh tasks")
        lines.append(
            f"| {wiki['id']} | {wiki['domain']} | {wiki['risk_level']} | {wiki['freshness_requirement']} | "
            f"{link_list(wiki['entrypoints'])} | {link_list(wiki['core_rules'], 4)} | "
            f"{link_list(wiki['workflows'], 4)} | {link_list(wiki['evals'])} | "
            f"{'<br>'.join(sources) if sources else '-'} | {markdown_link(wiki['pack']) if wiki['pack'] else 'missing'} |"
        )

    lines.extend(["", "## Domain Routing", ""])
    for wiki in nav["wikis"]:
        keywords = ", ".join(wiki.get("trigger_keywords", [])) or "-"
        lines.append(f"- `{wiki['id']}`: {wiki['domain']}; triggers: {keywords}")

    lines.extend(
        [
            "",
            "## Reading Rules",
            "",
            "- For any wiki task, read `manifest.yaml`, `README.md`, `AGENTS.md`, then `rules/` before workflows.",
            "- For high-risk wiki tasks, preserve human confirmation points and avoid autonomous high-risk execution.",
            "- Current facts remain gated by `sources/source-notes.md`, `docs/SOURCE_UPDATE_QUEUE.md`, and source refresh logs.",
            "- Do not record secrets, credentials, cookies, private keys, or private account data.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    nav = build_navigation()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(nav), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(nav, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"HUB NAVIGATION GENERATED ({nav['wiki_count']} wikis)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
