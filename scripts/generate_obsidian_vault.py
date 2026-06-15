#!/usr/bin/env python3
"""Generate an Obsidian vault navigation layer for Agent Wiki Hub."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
VAULT = ROOT / "obsidian-vault"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"

CORE_DIRS = [
    "00_System/Dashboards", "00_System/Templates", "00_System/Prompts", "00_System/Logs", "00_System/Config",
    "01_Raw/WebClips", "01_Raw/PDFs", "01_Raw/Images", "01_Raw/Audio", "01_Raw/Video", "01_Raw/Imports",
    "02_Knowledge/MOCs", "02_Knowledge/Concepts", "02_Knowledge/Rules", "02_Knowledge/Workflows",
    "02_Knowledge/Cases", "02_Knowledge/Candidates", "02_Knowledge/SourceReview",
    "03_Skills/SOPs", "03_Skills/DecisionModels", "03_Skills/PromptTemplates", "03_Skills/AgentPlaybooks",
    "04_Output/Reports", "04_Output/Articles", "04_Output/Briefings", "04_Output/Slides", "04_Output/Mermaid",
    "05_Dashboard", "99_Archive",
]
TOP_READMES = ["00_System", "01_Raw", "02_Knowledge", "03_Skills", "04_Output", "05_Dashboard", "99_Archive"]
KNOWLEDGE_DIRS = ["concepts", "rules", "workflows", "cases", "prompts", "tools", "sources"]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in read_text(path).splitlines():
        if ":" not in raw or raw.startswith(" ") or raw.lstrip().startswith("-"):
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def display_name(wiki_id: str) -> str:
    return " ".join(part.capitalize() for part in wiki_id.replace("-wiki", "").split("-")) + " Wiki"


def slug_title(path: Path) -> str:
    text = read_text(path)
    for line in text.splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"')
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def frontmatter(kind: str, wiki: str, risk: str, tags: list[str], source_status: str = "mixed") -> str:
    tag_lines = "\n".join(f"  - {tag}" for tag in tags)
    return (
        "---\n"
        f"type: {kind}\n"
        f"wiki: {wiki}\n"
        "status: active\n"
        f"source_status: {source_status}\n"
        "agent_use: true\n"
        f"risk: {risk}\n"
        "tags:\n"
        f"{tag_lines}\n"
        "generated_by: scripts/generate_obsidian_vault.py\n"
        f"generated_on: {date.today().isoformat()}\n"
        "---\n\n"
    )


def wiki_records() -> list[dict]:
    records = []
    for wiki in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        manifest = parse_manifest(wiki / "manifest.yaml")
        records.append(
            {
                "id": wiki.name,
                "name": manifest.get("name") or display_name(wiki.name),
                "domain": manifest.get("domain", ""),
                "risk": manifest.get("risk_level", ""),
                "freshness": manifest.get("freshness_requirement", ""),
                "path": rel(wiki),
            }
        )
    return records


def write_readmes() -> None:
    (VAULT / "README.md").write_text(
        "# Agent Wiki Hub Obsidian Vault\n\n"
        "This vault is a generated navigation layer over `wikis/`, `docs/`, and `registry/`.\n"
        "It does not replace the wiki source of truth and does not certify current facts.\n",
        encoding="utf-8",
    )
    for folder in TOP_READMES:
        path = VAULT / folder / "README.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"# {folder}\n\nGenerated Obsidian workspace area for Agent Wiki Hub v2.\n"
            "Use generated dashboards and MOCs for browsing; use `wikis/` for agent execution source of truth.\n",
            encoding="utf-8",
        )


def write_mocs(records: list[dict]) -> list[str]:
    paths = []
    for record in records:
        wiki_dir = ROOT / record["path"]
        lines = [
            frontmatter("moc", record["id"], record["risk"], ["agent-wiki", record["domain"], "source-review"]),
            f"# {record['name']} MOC",
            "",
            f"- Wiki: `{record['id']}`",
            f"- Source: `{record['path']}`",
            f"- Risk: `{record['risk']}`",
            f"- Freshness: `{record['freshness']}`",
            "- Related dashboards: [[Wiki Status]], [[Source Review Status]], [[Acceptance Status]], [[Human Gates]]",
            "",
            "## Knowledge Indexes",
        ]
        for dirname in KNOWLEDGE_DIRS:
            folder = wiki_dir / dirname
            target_note = f"{record['name']} {dirname.title()}"
            lines.append(f"- [[{target_note}]]")
            items = sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".yaml", ".yml"})
            out_dir = VAULT / "02_Knowledge" / dirname.title()
            out_dir.mkdir(parents=True, exist_ok=True)
            body = [
                frontmatter("index", record["id"], record["risk"], ["agent-wiki", dirname], "mixed"),
                f"# {target_note}",
                "",
                f"Generated index for `{record['id']}/{dirname}`.",
                "",
                "| Page | Source path |",
                "| --- | --- |",
            ]
            for item in items:
                body.append(f"| {slug_title(item)} | `{rel(item)}` |")
            (out_dir / f"{target_note}.md").write_text("\n".join(body) + "\n", encoding="utf-8")
        lines.extend(["", "## Source Review", "- [[Source Review Status]]", "- [[Needs Source Update]]"])
        out = VAULT / "02_Knowledge" / "MOCs" / f"{record['name']} MOC.md"
        out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        paths.append(rel(out))
    return paths


def dashboard_table(records: list[dict]) -> str:
    lines = ["| Wiki | Domain | Risk | Freshness | MOC |", "| --- | --- | --- | --- | --- |"]
    for record in records:
        lines.append(
            f"| {record['id']} | {record['domain']} | {record['risk']} | {record['freshness']} | "
            f"[[{record['name']} MOC]] |"
        )
    return "\n".join(lines)


def write_dashboards(records: list[dict]) -> list[str]:
    final_status = json.loads(read_text(REGISTRY / "source-review-final-status.json") or "{}")
    acceptance = json.loads(read_text(REGISTRY / "acceptance-report.json") or "{}")
    source_dashboard = json.loads(read_text(REGISTRY / "source-refresh-dashboard.json") or "{}")
    completion = source_dashboard.get("source_refresh", {}).get("completion", {})
    dashboard_dir = VAULT / "05_Dashboard"
    dashboard_dir.mkdir(parents=True, exist_ok=True)
    pages = {
        "Wiki Status.md": [
            "# Wiki Status",
            "",
            dashboard_table(records),
            "",
            "## Optional Dataview",
            "```dataview",
            "TABLE wiki, risk, source_status FROM \"02_Knowledge/MOCs\"",
            "```",
            "",
            "## Obsidian Bases Notes",
            "Use this table as a manual base view when Bases is available.",
        ],
        "Source Review Status.md": [
            "# Source Review Status",
            "",
            f"- Open topics: {final_status.get('open_topic_count', completion.get('open_ticket_count', 'unknown'))}",
            f"- Verified tickets: {final_status.get('verified_ticket_count', completion.get('verified_ticket_count', 'unknown'))}",
            f"- Current-fact ready: {final_status.get('current_fact_ready', source_dashboard.get('current_fact_ready', False))}",
            "",
            "| Wave | Tickets | Human Gates | Packet Role |",
            "| --- | ---: | ---: | --- |",
            *[
                f"| {wave.get('wave')} | {wave.get('ticket_count')} | {wave.get('human_gate_count')} | {wave.get('packet_role')} |"
                for wave in final_status.get("waves", [])
            ],
            "",
            "## Optional Dataview",
            "```dataview",
            "LIST FROM \"02_Knowledge/SourceReview\"",
            "```",
        ],
        "Acceptance Status.md": [
            "# Acceptance Status",
            "",
            f"- Acceptance passed: {acceptance.get('passed', False)}",
            "- Source: `registry/acceptance-report.json`",
            "",
            "| Status | Value |",
            "| --- | --- |",
            f"| passed | {acceptance.get('passed', False)} |",
        ],
        "Needs Source Update.md": [
            "# Needs Source Update",
            "",
            f"- Open source update topics: {completion.get('open_ticket_count', final_status.get('open_topic_count', 'unknown'))}",
            "- Source: `registry/source-refresh-dashboard.json`",
            "",
            "Current facts remain gated until authoritative evidence and human gates pass.",
        ],
        "Human Gates.md": [
            "# Human Gates",
            "",
            "| Gate | Count |",
            "| --- | ---: |",
            *[f"| {key} | {value} |" for key, value in final_status.get("human_gates", {}).items()],
        ],
        "Knowledge Graph Status.md": [
            "# Knowledge Graph Status",
            "",
            f"- Wiki nodes: {len(records)}",
            "- Generated MOCs: yes",
            "- JSON Canvas maps: generated by `scripts/generate_obsidian_canvas.py`",
            "- RAG layer: local-first scaffold",
        ],
    }
    written = []
    for name, lines in pages.items():
        path = dashboard_dir / name
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        written.append(rel(path))
    return written


def write_docs(records: list[dict], mocs: list[str], dashboards: list[str]) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (DOCS / "OBSIDIAN_INTEGRATION.md").write_text(
        "# Obsidian Integration\n\n"
        "Agent Wiki Hub v2 generates an Obsidian vault as a human browsing layer. "
        "`wikis/` remains the agent source of truth; Obsidian pages are generated navigation notes.\n",
        encoding="utf-8",
    )
    (DOCS / "OBSIDIAN_USAGE.md").write_text(
        "# Obsidian Usage\n\n"
        "Open Obsidian, choose `Open folder as vault`, select `obsidian-vault/`, then start with "
        "`05_Dashboard/Wiki Status.md` or `02_Knowledge/MOCs/`.\n",
        encoding="utf-8",
    )
    (DOCS / "OBSIDIAN_DASHBOARD_GUIDE.md").write_text(
        "# Obsidian Dashboard Guide\n\n"
        "Dashboard files use ordinary Markdown tables and optional Dataview blocks. Dataview and Bases are optional and not required for acceptance.\n",
        encoding="utf-8",
    )
    manifest = {
        "generated": date.today().isoformat(),
        "passed": True,
        "wiki_count": len(records),
        "moc_count": len(mocs),
        "dashboard_count": len(dashboards),
        "mocs": mocs,
        "dashboards": dashboards,
    }
    (REGISTRY / "obsidian-vault-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (REGISTRY / "obsidian-dashboard-manifest.json").write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": True, "dashboards": dashboards}, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    for dirname in CORE_DIRS:
        (VAULT / dirname).mkdir(parents=True, exist_ok=True)
    write_readmes()
    records = wiki_records()
    mocs = write_mocs(records)
    dashboards = write_dashboards(records)
    write_docs(records, mocs, dashboards)
    print(f"OBSIDIAN VAULT GENERATED ({len(records)} wikis, {len(mocs)} MOCs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
