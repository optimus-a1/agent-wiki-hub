#!/usr/bin/env python3
"""Generate Agent Wiki Hub v2 scaffolding files.

This script writes local-first Obsidian, RAG, ingestion, crawler, dashboard,
classification, promotion, and audit scaffolds. It does not crawl the network,
verify current facts, or promote high-risk/current content.
"""
from __future__ import annotations

from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
    print(f"Wrote {path}")


def main() -> int:
    write(
        "scripts/generate_obsidian_vault.py",
        r'''
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
        ''',
    )

    write(
        "scripts/generate_obsidian_canvas.py",
        r'''
        #!/usr/bin/env python3
        """Generate Obsidian JSON Canvas maps."""
        from __future__ import annotations

        from datetime import date
        from pathlib import Path
        import json

        ROOT = Path(__file__).resolve().parents[1]
        WIKIS = ROOT / "wikis"
        DASH = ROOT / "obsidian-vault" / "05_Dashboard"
        REGISTRY = ROOT / "registry"
        DOCS = ROOT / "docs"


        def rel(path: Path) -> str:
            return path.relative_to(ROOT).as_posix()


        def text_node(node_id: str, text: str, x: int, y: int) -> dict:
            return {"id": node_id, "type": "text", "text": text, "x": x, "y": y, "width": 260, "height": 110}


        def file_node(node_id: str, path: str, x: int, y: int) -> dict:
            return {"id": node_id, "type": "file", "file": path, "x": x, "y": y, "width": 280, "height": 120}


        def edge(edge_id: str, from_id: str, to_id: str) -> dict:
            return {"id": edge_id, "fromNode": from_id, "toNode": to_id}


        def write_canvas(path: Path, nodes: list[dict], edges: list[dict]) -> None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"nodes": nodes, "edges": edges}, indent=2), encoding="utf-8")


        def main() -> int:
            DASH.mkdir(parents=True, exist_ok=True)
            wiki_ids = sorted(p.name for p in WIKIS.iterdir() if p.is_dir())
            hub_nodes = [file_node("wiki-status", "05_Dashboard/Wiki Status.md", 0, 0)]
            hub_edges = []
            x, y = -720, 180
            for idx, wiki in enumerate(wiki_ids):
                node_id = f"wiki-{idx}"
                hub_nodes.append(text_node(node_id, wiki, x + (idx % 4) * 360, y + (idx // 4) * 180))
                hub_edges.append(edge(f"edge-{idx}", "wiki-status", node_id))
            for idx, label in enumerate(["Source Review", "Acceptance", "RAG", "Obsidian Vault", "Dashboard", "Ingestion", "Crawler"]):
                node_id = f"system-{idx}"
                hub_nodes.append(text_node(node_id, label, 820, idx * 150))
                hub_edges.append(edge(f"system-edge-{idx}", "wiki-status", node_id))
            write_canvas(DASH / "Agent Wiki Hub.canvas", hub_nodes, hub_edges)

            wave_nodes = [
                file_node("source-review", "05_Dashboard/Source Review Status.md", 0, 0),
                text_node("wave-1", "Wave-1 active packet", -420, 190),
                text_node("wave-2", "Wave-2 planning-only", 0, 190),
                text_node("wave-3", "Wave-3 planning-only", 420, 190),
                file_node("human-gates", "05_Dashboard/Human Gates.md", 0, 390),
            ]
            wave_edges = [edge("e1", "source-review", "wave-1"), edge("e2", "source-review", "wave-2"), edge("e3", "source-review", "wave-3"), edge("e4", "source-review", "human-gates")]
            write_canvas(DASH / "Source Review Waves.canvas", wave_nodes, wave_edges)

            map_nodes = [file_node("graph", "05_Dashboard/Knowledge Graph Status.md", 0, 0)]
            map_edges = []
            for idx, wiki in enumerate(wiki_ids):
                node_id = f"moc-{idx}"
                map_nodes.append(text_node(node_id, f"{wiki} MOC", -700 + (idx % 3) * 420, 170 + (idx // 3) * 170))
                map_edges.append(edge(f"moc-edge-{idx}", "graph", node_id))
            write_canvas(DASH / "Wiki Knowledge Map.canvas", map_nodes, map_edges)

            manifest = {
                "generated": date.today().isoformat(),
                "passed": True,
                "canvas_files": [rel(DASH / name) for name in ["Agent Wiki Hub.canvas", "Source Review Waves.canvas", "Wiki Knowledge Map.canvas"]],
                "wiki_count": len(wiki_ids),
            }
            REGISTRY.mkdir(parents=True, exist_ok=True)
            DOCS.mkdir(parents=True, exist_ok=True)
            (REGISTRY / "obsidian-canvas-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            (DOCS / "OBSIDIAN_CANVAS_GUIDE.md").write_text(
                "# Obsidian Canvas Guide\n\nGenerated JSON Canvas maps live in `obsidian-vault/05_Dashboard/` and require no external services.\n",
                encoding="utf-8",
            )
            print(f"OBSIDIAN CANVAS GENERATED ({len(manifest['canvas_files'])} files)")
            return 0


        if __name__ == "__main__":
            raise SystemExit(main())
        ''',
    )

    write(
        "scripts/audit_obsidian_vault.py",
        r'''
        #!/usr/bin/env python3
        """Audit generated Obsidian vault structure."""
        from __future__ import annotations

        from datetime import date
        from pathlib import Path
        import json

        ROOT = Path(__file__).resolve().parents[1]
        VAULT = ROOT / "obsidian-vault"
        DOCS = ROOT / "docs"
        REGISTRY = ROOT / "registry"
        REQUIRED = [
            "00_System/README.md", "01_Raw/README.md", "02_Knowledge/README.md", "03_Skills/README.md",
            "04_Output/README.md", "05_Dashboard/Wiki Status.md", "05_Dashboard/Source Review Status.md",
            "05_Dashboard/Acceptance Status.md", "05_Dashboard/Needs Source Update.md", "05_Dashboard/Human Gates.md",
            "05_Dashboard/Knowledge Graph Status.md", "99_Archive/README.md",
        ]

        def rel(path: Path) -> str:
            return path.relative_to(ROOT).as_posix()

        def main() -> int:
            checks = [{"path": item, "passed": (VAULT / item).exists()} for item in REQUIRED]
            mocs = list((VAULT / "02_Knowledge" / "MOCs").glob("*.md")) if VAULT.exists() else []
            checks.append({"path": "02_Knowledge/MOCs", "passed": len(mocs) >= 12})
            failed = [c for c in checks if not c["passed"]]
            DOCS.mkdir(parents=True, exist_ok=True)
            REGISTRY.mkdir(parents=True, exist_ok=True)
            lines = ["# Obsidian Vault Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", f"- MOCs: {len(mocs)}", "", "| Check | Result |", "| --- | --- |"]
            lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
            (DOCS / "OBSIDIAN_VAULT_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
            (REGISTRY / "obsidian-vault-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks, "moc_count": len(mocs)}, indent=2), encoding="utf-8")
            print(f"OBSIDIAN VAULT AUDIT {'PASSED' if not failed else 'FAILED'} ({len(checks)} checks)")
            return 0 if not failed else 1

        if __name__ == "__main__":
            raise SystemExit(main())
        ''',
    )

    write(
        "dashboard/scripts/collect_dashboard_data.py",
        r'''
        #!/usr/bin/env python3
        """Collect static dashboard data from registry and wiki files."""
        from __future__ import annotations

        from collections import Counter
        from datetime import date
        from pathlib import Path
        import json

        ROOT = Path(__file__).resolve().parents[2]
        DATA = ROOT / "dashboard" / "data"
        REGISTRY = ROOT / "registry"
        WIKIS = ROOT / "wikis"
        PACKS = ROOT / "packs"
        DOCS = ROOT / "docs"

        def read_json(path: Path) -> dict:
            if not path.exists():
                return {}
            return json.loads(path.read_text(encoding="utf-8"))

        def main() -> int:
            DATA.mkdir(parents=True, exist_ok=True)
            DOCS.mkdir(parents=True, exist_ok=True)
            acceptance = read_json(REGISTRY / "acceptance-report.json")
            source_refresh = read_json(REGISTRY / "source-refresh-dashboard.json")
            final_status = read_json(REGISTRY / "source-review-final-status.json")
            readiness = read_json(REGISTRY / "source-review-readiness-matrix.json")
            wiki_dirs = sorted(p for p in WIKIS.iterdir() if p.is_dir())
            page_count = sum(1 for p in WIKIS.rglob("*.md") if p.is_file())
            risk_counts = Counter()
            for wiki in wiki_dirs:
                text = (wiki / "manifest.yaml").read_text(encoding="utf-8", errors="ignore")
                for line in text.splitlines():
                    if line.startswith("risk_level:"):
                        risk_counts[line.split(":", 1)[1].strip()] += 1
            packs = sorted(p.name for p in PACKS.glob("*.zip")) if PACKS.exists() else []
            summary = {
                "generated": date.today().isoformat(),
                "passed": True,
                "wiki_count": len(wiki_dirs),
                "page_count": page_count,
                "acceptance_passed": acceptance.get("passed", False),
                "open_source_topics": final_status.get("open_topic_count", source_refresh.get("source_refresh", {}).get("completion", {}).get("open_ticket_count", 0)),
                "verified_tickets": final_status.get("verified_ticket_count", source_refresh.get("source_refresh", {}).get("completion", {}).get("verified_ticket_count", 0)),
                "current_fact_ready": final_status.get("current_fact_ready", source_refresh.get("current_fact_ready", False)),
                "human_gates": final_status.get("human_gates", {}),
                "risk_counts": dict(sorted(risk_counts.items())),
                "pack_count": len(packs),
            }
            files = {
                "dashboard-summary.json": summary,
                "wiki-status.json": {"generated": date.today().isoformat(), "wikis": [p.name for p in wiki_dirs], "risk_counts": summary["risk_counts"]},
                "source-review-status.json": final_status or {"generated": date.today().isoformat(), "waves": []},
                "acceptance-status.json": acceptance or {"generated": date.today().isoformat(), "passed": False},
                "packs.json": {"generated": date.today().isoformat(), "packs": packs},
            }
            for name, payload in files.items():
                (DATA / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")
            (ROOT / "registry" / "dashboard-manifest.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": True, "files": list(files)}, indent=2), encoding="utf-8")
            (DOCS / "DASHBOARD_USAGE.md").write_text("# Dashboard Usage\n\nRun `python dashboard/scripts/collect_dashboard_data.py`, then open `dashboard/index.html` in a browser.\n", encoding="utf-8")
            print(f"DASHBOARD DATA GENERATED ({summary['wiki_count']} wikis, {summary['pack_count']} packs)")
            return 0

        if __name__ == "__main__":
            raise SystemExit(main())
        ''',
    )

    write(
        "scripts/audit_dashboard.py",
        r'''
        #!/usr/bin/env python3
        """Audit local static dashboard files."""
        from __future__ import annotations

        from datetime import date
        from pathlib import Path
        import json

        ROOT = Path(__file__).resolve().parents[1]
        REQUIRED = ["dashboard/README.md", "dashboard/package.json", "dashboard/index.html", "dashboard/src/main.js", "dashboard/src/styles.css", "dashboard/data/dashboard-summary.json", "dashboard/data/wiki-status.json", "dashboard/data/source-review-status.json", "dashboard/data/acceptance-status.json", "dashboard/data/packs.json"]
        DOCS = ROOT / "docs"
        REGISTRY = ROOT / "registry"

        def main() -> int:
            checks = []
            for item in REQUIRED:
                path = ROOT / item
                passed = path.exists()
                if passed and path.suffix == ".json":
                    try:
                        json.loads(path.read_text(encoding="utf-8"))
                    except json.JSONDecodeError:
                        passed = False
                checks.append({"path": item, "passed": passed})
            failed = [c for c in checks if not c["passed"]]
            DOCS.mkdir(parents=True, exist_ok=True)
            REGISTRY.mkdir(parents=True, exist_ok=True)
            lines = ["# Dashboard Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", "", "| Path | Result |", "| --- | --- |"]
            lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
            (DOCS / "DASHBOARD_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
            (REGISTRY / "dashboard-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks}, indent=2), encoding="utf-8")
            print(f"DASHBOARD AUDIT {'PASSED' if not failed else 'FAILED'} ({len(checks)} checks)")
            return 0 if not failed else 1

        if __name__ == "__main__":
            raise SystemExit(main())
        ''',
    )

    write("dashboard/README.md", "# Local Dashboard\n\nStatic local status dashboard. Run `python dashboard/scripts/collect_dashboard_data.py`, then open `index.html`.\n")
    write("dashboard/data/README.md", "# Dashboard Data\n\nGenerated JSON files for the static dashboard.\n")
    write("dashboard/package.json", '{"name":"agent-wiki-hub-dashboard","version":"0.0.0","private":true,"scripts":{"serve":"python -m http.server 8080"}}\n')
    write(
        "dashboard/index.html",
        '''
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Agent Wiki Hub Dashboard</title>
          <link rel="stylesheet" href="src/styles.css">
        </head>
        <body>
          <main>
            <h1>Agent Wiki Hub Dashboard</h1>
            <section id="summary">Loading dashboard data...</section>
            <section><h2>Packs</h2><ul id="packs"></ul></section>
          </main>
          <script src="src/main.js"></script>
        </body>
        </html>
        ''',
    )
    write(
        "dashboard/src/main.js",
        '''
        async function loadJson(path) {
          const response = await fetch(path);
          return response.json();
        }

        async function render() {
          const summary = await loadJson('data/dashboard-summary.json');
          const packs = await loadJson('data/packs.json');
          document.getElementById('summary').innerHTML = `
            <div class="grid">
              <article><span>Wikis</span><strong>${summary.wiki_count}</strong></article>
              <article><span>Pages</span><strong>${summary.page_count}</strong></article>
              <article><span>Acceptance</span><strong>${summary.acceptance_passed ? 'PASS' : 'OPEN'}</strong></article>
              <article><span>Open Topics</span><strong>${summary.open_source_topics}</strong></article>
              <article><span>Verified Tickets</span><strong>${summary.verified_tickets}</strong></article>
              <article><span>Current Fact Ready</span><strong>${summary.current_fact_ready ? 'yes' : 'no'}</strong></article>
            </div>`;
          document.getElementById('packs').innerHTML = packs.packs.map((pack) => `<li>${pack}</li>`).join('');
        }

        render().catch((error) => {
          document.getElementById('summary').textContent = `Unable to load dashboard data: ${error.message}`;
        });
        ''',
    )
    write(
        "dashboard/src/styles.css",
        '''
        :root { color-scheme: light; font-family: Arial, sans-serif; }
        body { margin: 0; background: #f6f7f9; color: #17202a; }
        main { max-width: 1100px; margin: 0 auto; padding: 32px; }
        h1, h2 { margin: 0 0 16px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; }
        article { background: white; border: 1px solid #d9dee7; border-radius: 8px; padding: 16px; }
        article span { display: block; color: #5d6b7c; font-size: 13px; }
        article strong { display: block; font-size: 28px; margin-top: 8px; }
        li { margin: 6px 0; }
        ''',
    )

    write(
        "rag/README.md",
        "# RAG Layer\n\nLocal-first semantic search scaffold. Chroma is optional; keyword fallback works without external dependencies.\n",
    )
    write(
        "rag/rag_config.yaml",
        '''
        chroma_dir: rag/chroma
        embedding_mode: local_optional
        fallback_mode: keyword
        index_sources:
          - wikis
          - docs
          - obsidian-vault/02_Knowledge
          - obsidian-vault/03_Skills
        excluded_paths:
          - .env
          - obsidian-vault/01_Raw/Audio
          - obsidian-vault/01_Raw/Video
          - rag/chroma
          - registry/*backup*
        ''',
    )
    write("rag/requirements-rag.txt", "chromadb\n")
    write("rag/.gitkeep", "")

    rag_common = r'''
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import argparse, json, re, sys

        ROOT = Path(__file__).resolve().parents[1]
        REGISTRY = ROOT / "registry"
        DOCS = ROOT / "docs"
        SOURCES = [ROOT / "wikis", ROOT / "docs", ROOT / "obsidian-vault" / "02_Knowledge", ROOT / "obsidian-vault" / "03_Skills"]

        def docs_to_index():
            for source in SOURCES:
                if source.exists():
                    for path in source.rglob("*.md"):
                        rel = path.relative_to(ROOT).as_posix()
                        if "/01_Raw/Audio/" in rel or "/01_Raw/Video/" in rel or "/rag/chroma/" in rel:
                            continue
                        yield path

        def extract(path):
            text = path.read_text(encoding="utf-8", errors="ignore")
            wiki = ""
            parts = path.relative_to(ROOT).parts
            if len(parts) > 1 and parts[0] == "wikis":
                wiki = parts[1]
            return {"path": path.relative_to(ROOT).as_posix(), "wiki": wiki, "section": "", "doc_type": path.parent.name, "source_status": "mixed", "risk": "", "last_modified": int(path.stat().st_mtime), "text": text[:4000]}
    '''
    write(
        "rag/index_wikis.py",
        "#!/usr/bin/env python3\n" + textwrap.dedent(rag_common) + r'''
        def main():
            records = [extract(p) for p in docs_to_index() if p.as_posix().find('/wikis/') >= 0 or p.relative_to(ROOT).parts[0] == 'wikis']
            REGISTRY.mkdir(parents=True, exist_ok=True)
            (REGISTRY / "rag-index-manifest.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": "wiki-index", "chunk_count": len(records)}, indent=2), encoding="utf-8")
            print(f"RAG WIKI INDEX GENERATED ({len(records)} chunks)")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "rag/index_obsidian.py",
        "#!/usr/bin/env python3\n" + textwrap.dedent(rag_common) + r'''
        def main():
            records = [extract(p) for p in docs_to_index() if "obsidian-vault" in p.relative_to(ROOT).as_posix()]
            REGISTRY.mkdir(parents=True, exist_ok=True)
            (REGISTRY / "rag-index-manifest.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": "obsidian-index", "chunk_count": len(records)}, indent=2), encoding="utf-8")
            print(f"RAG OBSIDIAN INDEX GENERATED ({len(records)} chunks)")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "rag/build_chroma_index.py",
        "#!/usr/bin/env python3\n" + textwrap.dedent(rag_common) + r'''
        def main():
            records = [extract(p) for p in docs_to_index()]
            try:
                import chromadb  # noqa: F401
                mode = "chroma-available"
                warning = ""
            except Exception:
                mode = "keyword-fallback"
                warning = "chromadb missing; persistent semantic index not built"
            REGISTRY.mkdir(parents=True, exist_ok=True)
            (REGISTRY / "rag-index-manifest.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": True, "mode": mode, "warning": warning, "chunk_count": len(records)}, indent=2), encoding="utf-8")
            print(f"RAG INDEX READY ({mode}, {len(records)} chunks)")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "rag/inspect_chroma_index.py",
        "#!/usr/bin/env python3\n" + textwrap.dedent(rag_common) + r'''
        def main():
            manifest = json.loads((REGISTRY / "rag-index-manifest.json").read_text(encoding="utf-8")) if (REGISTRY / "rag-index-manifest.json").exists() else {}
            print(json.dumps(manifest or {"passed": True, "warning": "rag index manifest missing"}, indent=2))
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "rag/search_knowledge.py",
        "#!/usr/bin/env python3\n" + textwrap.dedent(rag_common) + r'''
        def main():
            parser = argparse.ArgumentParser()
            parser.add_argument("--query", required=True)
            parser.add_argument("--top-k", type=int, default=5)
            args = parser.parse_args()
            terms = [t.casefold() for t in re.findall(r"[A-Za-z0-9_-]+", args.query)]
            scored = []
            for path in docs_to_index():
                text = path.read_text(encoding="utf-8", errors="ignore")
                score = sum(text.casefold().count(term) for term in terms)
                if score:
                    scored.append((score, path.relative_to(ROOT).as_posix()))
            for score, path in sorted(scored, reverse=True)[: args.top_k]:
                print(f"{score}\t{path}")
            if not scored:
                print("No keyword fallback results.")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )

    write(
        "scripts/audit_rag_config.py",
        r'''
        #!/usr/bin/env python3
        """Audit RAG configuration and optional Chroma readiness."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json
        ROOT = Path(__file__).resolve().parents[1]
        REQUIRED = ["rag/README.md", "rag/rag_config.yaml", "rag/requirements-rag.txt", "rag/index_wikis.py", "rag/index_obsidian.py", "rag/build_chroma_index.py", "rag/inspect_chroma_index.py", "rag/search_knowledge.py"]
        def main():
            checks = [{"path": item, "passed": (ROOT / item).exists()} for item in REQUIRED]
            warnings = []
            try:
                import chromadb  # noqa: F401
            except Exception:
                warnings.append("chromadb missing; keyword fallback remains available")
            gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8", errors="ignore")
            checks.append({"path": ".gitignore rag/chroma/", "passed": "rag/chroma/" in gitignore})
            failed = [c for c in checks if not c["passed"]]
            (ROOT / "docs").mkdir(exist_ok=True)
            (ROOT / "registry").mkdir(exist_ok=True)
            lines = ["# RAG Config Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", *[f"- Warning: {w}" for w in warnings], "", "| Check | Result |", "| --- | --- |"]
            lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
            (ROOT / "docs" / "RAG_CONFIG_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
            (ROOT / "registry" / "rag-config-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "warnings": warnings, "checks": checks}, indent=2), encoding="utf-8")
            print(f"RAG CONFIG AUDIT {'PASSED' if not failed else 'FAILED'} ({len(warnings)} warnings)")
            return 0 if not failed else 1
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )

    for path, title in {
        "docs/RAG_INTEGRATION.md": "RAG Integration",
        "docs/RAG_USAGE.md": "RAG Usage",
    }.items():
        write(path, f"# {title}\n\nLocal-first RAG scaffold. Chroma is optional; scripts fall back to keyword search when optional dependencies are unavailable.\n\nRun `python rag/search_knowledge.py --query \"source review human gate\" --top-k 5`.\n")
    write("registry/rag-index-manifest.json", '{"generated":"","passed":true,"mode":"not-built-yet","warning":"Run rag/build_chroma_index.py to refresh."}\n')

    write(
        "ingestion/README.md",
        "# Ingestion Pipeline\n\nRaw inputs go to `obsidian-vault/01_Raw/`; candidate knowledge goes to `obsidian-vault/02_Knowledge/Candidates/`. OCR and Whisper are optional placeholders.\n",
    )
    write(
        "ingestion/intake_config.yaml",
        '''
        raw_root: obsidian-vault/01_Raw
        candidate_root: obsidian-vault/02_Knowledge/Candidates
        high_risk_requires_human_review: true
        optional_dependencies:
          ocr: optional
          whisper: optional
        ''',
    )
    simple_ingest = r'''
        #!/usr/bin/env python3
        """Placeholder ingestion utility."""
        from pathlib import Path
        import argparse
        ROOT = Path(__file__).resolve().parents[1]
        def main():
            parser = argparse.ArgumentParser()
            parser.add_argument("source", nargs="?")
            parser.add_argument("--dry-run", action="store_true")
            args = parser.parse_args()
            print("INGESTION PLACEHOLDER PASS" + (" (dry-run)" if args.dry_run else ""))
            return 0
        if __name__ == "__main__": raise SystemExit(main())
    '''
    for name in ["import_markdown.py", "import_webclip.py", "import_pdf_placeholder.py", "import_image_ocr_placeholder.py", "import_audio_whisper_placeholder.py", "import_video_placeholder.py", "process_raw_to_knowledge.py"]:
        write(f"ingestion/{name}", simple_ingest)
    write(
        "ingestion/generate_ingestion_report.py",
        r'''
        #!/usr/bin/env python3
        """Generate ingestion pipeline report."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json
        ROOT = Path(__file__).resolve().parents[1]
        DOCS = ROOT / "docs"
        REGISTRY = ROOT / "registry"
        LOG = ROOT / "obsidian-vault" / "00_System" / "Logs" / "Ingestion Log.md"
        def main():
            LOG.parent.mkdir(parents=True, exist_ok=True)
            if not LOG.exists():
                LOG.write_text("# Ingestion Log\n\nNo raw ingestion has been performed by default.\n", encoding="utf-8")
            DOCS.mkdir(exist_ok=True); REGISTRY.mkdir(exist_ok=True)
            warnings = ["OCR dependency optional and not required", "Whisper dependency optional and not required", "No Raw inputs may be present"]
            manifest = {"generated": date.today().isoformat(), "passed": True, "warnings": warnings, "raw_root": "obsidian-vault/01_Raw", "candidate_root": "obsidian-vault/02_Knowledge/Candidates"}
            (REGISTRY / "ingestion-pipeline-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            for name, title in [("INGESTION_PIPELINE.md","Ingestion Pipeline"),("MULTIMODAL_PROCESSING_GUIDE.md","Multimodal Processing Guide"),("RAW_TO_KNOWLEDGE_WORKFLOW.md","Raw To Knowledge Workflow")]:
                (DOCS / name).write_text(f"# {title}\n\nRaw inputs remain unverified. OCR/Whisper outputs are never treated as verified facts. High-risk materials require human review.\n", encoding="utf-8")
            print("INGESTION REPORT GENERATED (warnings only)")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "scripts/audit_ingestion_pipeline.py",
        r'''
        #!/usr/bin/env python3
        """Audit ingestion pipeline scaffold."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json
        ROOT = Path(__file__).resolve().parents[1]
        REQUIRED = ["ingestion/README.md","ingestion/intake_config.yaml","ingestion/import_markdown.py","ingestion/import_webclip.py","ingestion/import_pdf_placeholder.py","ingestion/import_image_ocr_placeholder.py","ingestion/import_audio_whisper_placeholder.py","ingestion/import_video_placeholder.py","ingestion/process_raw_to_knowledge.py","ingestion/generate_ingestion_report.py","obsidian-vault/00_System/Logs/Ingestion Log.md","registry/ingestion-pipeline-manifest.json"]
        def main():
            checks = [{"path": p, "passed": (ROOT / p).exists()} for p in REQUIRED]
            failed = [c for c in checks if not c["passed"]]
            lines = ["# Ingestion Pipeline Audit", "", f"Generated: {date.today().isoformat()}", "", f"- Passed: {not failed}", "", "| Path | Result |", "| --- | --- |"]
            lines.extend(f"| {c['path']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in checks)
            (ROOT / "docs" / "INGESTION_PIPELINE_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
            (ROOT / "registry" / "ingestion-pipeline-audit.json").write_text(json.dumps({"generated": date.today().isoformat(), "passed": not failed, "checks": checks, "warnings": ["OCR optional", "Whisper optional"]}, indent=2), encoding="utf-8")
            print(f"INGESTION PIPELINE AUDIT {'PASSED' if not failed else 'FAILED'}")
            return 0 if not failed else 1
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )

    write(
        "crawler/README.md",
        "# Controlled Crawler\n\nConservative public-source crawler scaffold. It defaults to dry-run/no-op and never writes directly to `wikis/`.\n",
    )
    write(
        "crawler/sources.yaml",
        '''
        sources:
          - name: arxiv-ai-agents
            type: rss
            url: "https://export.arxiv.org/rss/cs.AI"
            target_wiki: research-agent-wiki
            risk: medium
            schedule: daily
            review_required: true
            allowed_paths: []
            disallowed_paths: []
            max_items_per_run: 10
            rate_limit_seconds: 5
            respect_robots: true
          - name: github-agent-knowledge-base-search
            type: github_search
            query: "AI agent knowledge base"
            target_wiki: agent-engineering-wiki
            risk: medium
            schedule: weekly
            review_required: true
            max_items_per_run: 10
            rate_limit_seconds: 5
            respect_robots: true
          - name: docker-docs-index
            type: docs_index
            url: "https://docs.docker.com/"
            target_wiki: nodeops-agent-wiki
            risk: high
            schedule: weekly
            review_required: true
            max_items_per_run: 10
            rate_limit_seconds: 10
            respect_robots: true
        ''',
    )
    crawler_stub = r'''
        #!/usr/bin/env python3
        """Controlled crawler no-op/dry-run entrypoint."""
        from __future__ import annotations
        import argparse
        def main():
            parser = argparse.ArgumentParser()
            parser.add_argument("--dry-run", action="store_true")
            args = parser.parse_args()
            print("CRAWLER DRY RUN PASS" if args.dry_run else "CRAWLER NO-OP PASS: network collection disabled by default")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
    '''
    for name in ["crawl_rss.py", "crawl_github.py", "crawl_docs.py", "crawl_web_page.py", "crawl_static_url_list.py", "export_to_raw.py", "dedupe_sources.py", "score_sources.py"]:
        write(f"crawler/{name}", crawler_stub)
    write(
        "crawler/generate_crawl_report.py",
        r'''
        #!/usr/bin/env python3
        """Generate controlled crawler report without network access."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json, re
        ROOT = Path(__file__).resolve().parents[1]
        def parse_sources(text: str):
            records, current = [], {}
            for raw in text.splitlines():
                line = raw.strip()
                if line.startswith("- name:"):
                    if current: records.append(current)
                    current = {"name": line.split(":",1)[1].strip()}
                elif ":" in line and current:
                    k,v=line.split(":",1)
                    current[k.strip()] = v.strip().strip('"')
            if current: records.append(current)
            return records
        def main():
            text = (ROOT / "crawler" / "sources.yaml").read_text(encoding="utf-8")
            sources = parse_sources(text)
            warnings = ["network collection not performed by report generator", "crawler writes Raw only and never writes to wikis"]
            payload = {"generated": date.today().isoformat(), "passed": True, "source_count": len(sources), "sources": sources, "warnings": warnings, "collected_count": 0}
            (ROOT / "registry").mkdir(exist_ok=True); (ROOT / "docs").mkdir(exist_ok=True)
            (ROOT / "registry" / "crawler-sources.json").write_text(json.dumps({"generated": date.today().isoformat(), "sources": sources}, indent=2), encoding="utf-8")
            (ROOT / "registry" / "crawl-report.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
            for name, title in [("CONTROLLED_CRAWLER.md","Controlled Crawler"),("CRAWLER_SOURCE_POLICY.md","Crawler Source Policy"),("KNOWLEDGE_INGESTION_REVIEW_FLOW.md","Knowledge Ingestion Review Flow"),("CRAWL_REPORT.md","Crawl Report")]:
                (ROOT / "docs" / name).write_text(f"# {title}\n\nThe crawler is conservative, public-source only, respects configured limits, writes to Raw only, and never marks content verified.\n", encoding="utf-8")
            print(f"CRAWL REPORT GENERATED ({len(sources)} configured sources, 0 collected)")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "scripts/audit_crawler_outputs.py",
        r'''
        #!/usr/bin/env python3
        """Audit crawler Raw outputs."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json, re
        ROOT = Path(__file__).resolve().parents[1]
        RAW = ROOT / "obsidian-vault" / "01_Raw"
        REQUIRED = ["source_url", "content_hash", "crawled_at", "requires_review", "robots_checked"]
        SECRET_RE = re.compile(r"(ghp_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
        def main():
            records=[]; issues=[]
            for path in RAW.rglob("*.md") if RAW.exists() else []:
                text = path.read_text(encoding="utf-8", errors="ignore")
                if "type: raw-source" not in text:
                    continue
                missing=[field for field in REQUIRED if f"{field}:" not in text]
                has_secret=bool(SECRET_RE.search(text))
                record={"path": path.relative_to(ROOT).as_posix(), "missing": missing, "has_secret": has_secret}
                records.append(record)
                if missing or has_secret: issues.append(record)
            passed = not issues
            lines=["# Crawler Output Audit","",f"Generated: {date.today().isoformat()}","",f"- Passed: {passed}",f"- Raw notes checked: {len(records)}",""]
            if not records: lines.append("No Raw source notes found; no-op PASS.")
            (ROOT/"docs"/"CRAWLER_OUTPUT_AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
            (ROOT/"registry"/"crawler-output-audit.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":passed,"records":records,"issues":issues},indent=2),encoding="utf-8")
            print(f"CRAWLER OUTPUT AUDIT {'PASSED' if passed else 'FAILED'} ({len(records)} raw notes)")
            return 0 if passed else 1
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )

    write(
        "scripts/classify_candidate_knowledge.py",
        r'''
        #!/usr/bin/env python3
        """Classify Raw notes into candidate knowledge categories."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import argparse, json, re
        ROOT = Path(__file__).resolve().parents[1]
        RAW = ROOT / "obsidian-vault" / "01_Raw"
        CAND = ROOT / "obsidian-vault" / "02_Knowledge" / "Candidates"
        HIGH_RISK = {"finance-agent-wiki","health-agent-wiki","legal-agent-wiki","security-agent-wiki","nodeops-agent-wiki","customs-agent-wiki","airdrop-agent-wiki"}
        CURRENT_TERMS = ["current", "latest", "price", "policy", "regulation", "version", "vulnerability", "api"]
        def classify(path: Path):
            text = path.read_text(encoding="utf-8", errors="ignore")
            target = ""
            title = path.stem
            source_url = ""
            for line in text.splitlines():
                if line.startswith("target_wiki:"): target = line.split(":",1)[1].strip()
                if line.startswith("source_title:"): title = line.split(":",1)[1].strip() or title
                if line.startswith("source_url:"): source_url = line.split(":",1)[1].strip()
            lower = text.casefold()
            if target in HIGH_RISK:
                cls, reason, review = "high_risk", "target wiki requires human gate", True
            elif any(term in lower for term in CURRENT_TERMS):
                cls, reason, review = "current_fact", "contains current-fact indicators", True
            elif not source_url:
                cls, reason, review = "low_quality", "missing source URL", True
            else:
                cls, reason, review = "stable_knowledge", "appears stable and low risk", False
            return {"path": path.relative_to(ROOT).as_posix(), "classification": cls, "confidence": 0.8 if cls == "stable_knowledge" else 0.5, "reason": reason, "target_wiki": target, "source_url": source_url, "source_title": title, "requires_human_review": review}
        def main():
            parser=argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args=parser.parse_args()
            records=[]
            for path in RAW.rglob("*.md") if RAW.exists() else []:
                text=path.read_text(encoding="utf-8", errors="ignore")
                if "type: raw-source" in text: records.append(classify(path))
            if not args.dry_run:
                CAND.mkdir(parents=True, exist_ok=True)
                for rec in records:
                    out=CAND/(Path(rec["path"]).stem+" Candidate.md")
                    out.write_text("---\ntype: candidate-knowledge\nclassification: {classification}\nconfidence: {confidence}\nreason: {reason}\ntarget_wiki: {target_wiki}\nsuggested_path: \nsource_url: {source_url}\nsource_title: {source_title}\nrequires_human_review: {requires_human_review}\nsource_status: unverified\ngenerated_by: scripts/classify_candidate_knowledge.py\n---\n\n# Candidate: {source_title}\n\n## Extracted stable knowledge\n\n## What this source supports\n\n## What this source does not support\n\n## Risk classification\n{classification}\n\n## Suggested destination\n\n## Required review\n".format(**rec), encoding="utf-8")
            payload={"generated":date.today().isoformat(),"passed":True,"dry_run":args.dry_run,"candidate_count":len(records),"records":records,"warnings":[] if records else ["no Raw inputs"]}
            (ROOT/"registry").mkdir(exist_ok=True); (ROOT/"docs").mkdir(exist_ok=True)
            (ROOT/"registry"/"candidate-knowledge-report.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
            (ROOT/"docs"/"CANDIDATE_KNOWLEDGE_REPORT.md").write_text(f"# Candidate Knowledge Report\n\nGenerated: {date.today().isoformat()}\n\n- Candidates: {len(records)}\n- Dry run: {args.dry_run}\n",encoding="utf-8")
            print(f"CANDIDATE KNOWLEDGE CLASSIFICATION PASSED ({len(records)} records, dry_run={args.dry_run})")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "scripts/promote_stable_knowledge.py",
        r'''
        #!/usr/bin/env python3
        """Promote safe stable candidate knowledge to automation-generated files."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import argparse, json, re
        ROOT = Path(__file__).resolve().parents[1]
        CAND = ROOT / "obsidian-vault" / "02_Knowledge" / "Candidates"
        HIGH_RISK_WIKIS = {"finance-agent-wiki","health-agent-wiki","legal-agent-wiki","security-agent-wiki","nodeops-agent-wiki","customs-agent-wiki","airdrop-agent-wiki"}
        def parse(path):
            fields={}
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                if ":" in line and not line.startswith("#"):
                    k,v=line.split(":",1); fields[k.strip()]=v.strip()
            return fields
        def eligible(fields):
            return fields.get("classification")=="stable_knowledge" and fields.get("requires_human_review","true")=="false" and float(fields.get("confidence","0") or 0)>=0.75 and fields.get("target_wiki") not in HIGH_RISK_WIKIS and fields.get("source_url") and fields.get("source_title")
        def main():
            parser=argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args=parser.parse_args()
            promotions=[]; blocked=[]
            for path in CAND.rglob("*.md") if CAND.exists() else []:
                fields=parse(path)
                if eligible(fields):
                    promotions.append({"candidate": path.relative_to(ROOT).as_posix(), "target_wiki": fields.get("target_wiki"), "source_url": fields.get("source_url"), "source_title": fields.get("source_title")})
                else:
                    blocked.append({"candidate": path.relative_to(ROOT).as_posix(), "reason": "not eligible"})
            if not args.dry_run:
                for item in promotions:
                    out=ROOT/"wikis"/item["target_wiki"]/ "concepts" / "automation-generated-knowledge.md"
                    out.parent.mkdir(parents=True, exist_ok=True)
                    block=f"\n## {item['source_title']}\n\n- source_status: stable\n- generated_from_raw: {item['candidate']}\n- source_url: {item['source_url']}\n- confidence: 0.8\n- promoted_on: {date.today().isoformat()}\n- reviewed_by: automation\n- limitations: Automation-generated low-risk stable candidate; human review recommended before broad reuse.\n\nNo current facts are promoted by this scaffold.\n"
                    out.write_text((out.read_text(encoding="utf-8") if out.exists() else "---\ntitle: Automation Generated Knowledge\nstatus: stable\nlast_updated: "+date.today().isoformat()+"\nrisk_level: medium\n---\n\n# Automation Generated Knowledge\n") + block, encoding="utf-8")
            payload={"generated":date.today().isoformat(),"passed":True,"dry_run":args.dry_run,"promotion_count":len(promotions),"blocked_count":len(blocked),"promotions":promotions,"blocked":blocked}
            (ROOT/"registry").mkdir(exist_ok=True); (ROOT/"docs").mkdir(exist_ok=True)
            (ROOT/"registry"/"knowledge-promotion-report.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
            (ROOT/"docs"/"KNOWLEDGE_PROMOTION_REPORT.md").write_text(f"# Knowledge Promotion Report\n\n- Dry run: {args.dry_run}\n- Promotions: {len(promotions)}\n- Blocked: {len(blocked)}\n",encoding="utf-8")
            print(f"KNOWLEDGE PROMOTION PASSED ({len(promotions)} eligible, dry_run={args.dry_run})")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "scripts/audit_knowledge_promotion.py",
        r'''
        #!/usr/bin/env python3
        """Audit automation-generated knowledge promotion outputs."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json, re
        ROOT = Path(__file__).resolve().parents[1]
        ALLOWED = {"automation-generated-knowledge.md","automation-generated-rules.md","automation-generated-workflows.md","automation-generated-cases.md"}
        BAD = re.compile(r"(classification:\s*current_fact|classification:\s*high_risk|current_fact promoted|high-risk promoted)", re.I)
        SECRET = re.compile(r"(ghp_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
        def main():
            records=[]; issues=[]
            for path in (ROOT/"wikis").rglob("automation-generated-*.md"):
                text=path.read_text(encoding="utf-8", errors="ignore")
                rec={"path":path.relative_to(ROOT).as_posix(),"allowed_name":path.name in ALLOWED,"has_bad_marker":bool(BAD.search(text)),"has_secret":bool(SECRET.search(text)),"source_url_present":"source_url:" in text}
                records.append(rec)
                if not rec["allowed_name"] or rec["has_bad_marker"] or rec["has_secret"] or not rec["source_url_present"]: issues.append(rec)
            passed=not issues
            (ROOT/"docs").mkdir(exist_ok=True); (ROOT/"registry").mkdir(exist_ok=True)
            (ROOT/"docs"/"KNOWLEDGE_PROMOTION_AUDIT.md").write_text(f"# Knowledge Promotion Audit\n\nGenerated: {date.today().isoformat()}\n\n- Passed: {passed}\n- Files checked: {len(records)}\n",encoding="utf-8")
            (ROOT/"registry"/"knowledge-promotion-audit.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":passed,"records":records,"issues":issues},indent=2),encoding="utf-8")
            print(f"KNOWLEDGE PROMOTION AUDIT {'PASSED' if passed else 'FAILED'} ({len(records)} files)")
            return 0 if passed else 1
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )
    write(
        "scripts/generate_source_review_from_candidates.py",
        r'''
        #!/usr/bin/env python3
        """Generate non-blocking source-review queue from current/high-risk candidates."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import argparse, json
        ROOT=Path(__file__).resolve().parents[1]
        CAND=ROOT/"obsidian-vault"/"02_Knowledge"/"Candidates"
        PACKETS=ROOT/"registry"/"source-review-packets"
        def parse(path):
            fields={}
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                if ":" in line and not line.startswith("#"):
                    k,v=line.split(":",1); fields[k.strip()]=v.strip()
            return fields
        def main():
            parser=argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args=parser.parse_args()
            entries=[]
            for idx,path in enumerate(CAND.rglob("*.md") if CAND.exists() else [], start=1):
                fields=parse(path)
                if fields.get("classification") in {"current_fact","high_risk"}:
                    entries.append({"ticket_id":f"AUTO-SRC-{date.today().strftime('%Y%m%d')}-{idx:03d}","status":"pending","source_title":fields.get("source_title","<source title>"),"source_publisher":"<publisher>","source_url_or_reference":fields.get("source_url","<url or local reference>"),"source_published_or_updated":"YYYY-MM-DD | unknown","source_accessed_on":date.today().isoformat(),"verified_on":"","evidence_summary":"<what the source supports and does not support>","affected_pages":[],"confidence":"low","remaining_uncertainty":"<remaining uncertainty>","human_reviewer":"<reviewer>","follow_up":"Keep pending until authoritative, dated, scoped evidence is reviewed."})
            PACKETS.mkdir(parents=True, exist_ok=True); (ROOT/"docs").mkdir(exist_ok=True); (ROOT/"registry").mkdir(exist_ok=True)
            packet={"packet_id":"source-review-session-auto-pending","created_on":date.today().isoformat(),"planning_only":True,"no_current_fact_write":True,"entries":entries}
            if not args.dry_run or not (PACKETS/"source-review-session-auto-pending.json").exists():
                (PACKETS/"source-review-session-auto-pending.json").write_text(json.dumps(packet,indent=2),encoding="utf-8")
                (PACKETS/"source-review-session-auto-pending.jsonl").write_text("\n".join(json.dumps(e) for e in entries)+("\n" if entries else ""),encoding="utf-8")
            (ROOT/"registry"/"knowledge-review-queue.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":True,"dry_run":args.dry_run,"entry_count":len(entries),"entries":entries},indent=2),encoding="utf-8")
            (ROOT/"docs"/"AUTO_SOURCE_REVIEW_QUEUE.md").write_text(f"# Auto Source Review Queue\n\n- Dry run: {args.dry_run}\n- Pending entries: {len(entries)}\n- This queue is planning-only and must not be imported automatically.\n",encoding="utf-8")
            print(f"AUTO SOURCE REVIEW QUEUE PASSED ({len(entries)} entries, dry_run={args.dry_run})")
            return 0
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )

    write(
        "scripts/audit_secret_leaks.py",
        r'''
        #!/usr/bin/env python3
        """Audit tracked/staged files for likely secret leaks without printing values."""
        from __future__ import annotations
        from datetime import date
        from pathlib import Path
        import json, os, re, subprocess
        ROOT=Path(__file__).resolve().parents[1]
        DOCS=ROOT/"docs"; REGISTRY=ROOT/"registry"
        TOKEN_PATTERNS=[
            ("classic_github_token_prefix", re.compile(r"ghp_[A-Za-z0-9_]{20,}")),
            ("fine_grained_github_token_prefix", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
            ("private_key_block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
            ("bearer_secret_like_value", re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{20,}")),
        ]
        ASSIGN=re.compile(r"(?im)^\s*(GITHUB_TOKEN|password|api_key|private_key)\s*=\s*([^\s#]+)?")
        PLACEHOLDERS={"","<token>","<value>","placeholder","redacted","changeme","example","xxx","xxxx"}
        SKIP={".git"}
        BIN={".zip",".png",".jpg",".jpeg",".gif",".pdf",".ico",".pyc"}
        def git_lines(args):
            proc=subprocess.run(["git",*args],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
            return {line.strip().replace("\\","/") for line in proc.stdout.splitlines() if line.strip()}
        def ignored(rel):
            return subprocess.run(["git","check-ignore","-q","--",rel],cwd=ROOT).returncode==0
        def main():
            tracked=git_lines(["ls-files"])
            staged=git_lines(["diff","--cached","--name-only"])
            findings=[]
            for path in ROOT.rglob("*"):
                if path.is_dir() or path.suffix.lower() in BIN: continue
                rel=path.relative_to(ROOT).as_posix()
                if any(part in SKIP for part in Path(rel).parts): continue
                try: text=path.read_text(encoding="utf-8")
                except UnicodeDecodeError: text=path.read_text(encoding="utf-8", errors="ignore")
                except Exception: continue
                path_ignored=ignored(rel)
                path_tracked=rel in tracked
                path_staged=rel in staged
                for name,rx in TOKEN_PATTERNS:
                    for m in rx.finditer(text):
                        findings.append({"path":rel,"line":text.count("\n",0,m.start())+1,"pattern":name,"tracked":path_tracked,"staged":path_staged,"ignored":path_ignored})
                for m in ASSIGN.finditer(text):
                    value=(m.group(2) or "").strip().strip("'\"")
                    if value.lower() not in PLACEHOLDERS:
                        findings.append({"path":rel,"line":text.count("\n",0,m.start())+1,"pattern":m.group(1)+"_non_placeholder_value","tracked":path_tracked,"staged":path_staged,"ignored":path_ignored})
            blocking=[f for f in findings if f["tracked"] or f["staged"]]
            DOCS.mkdir(exist_ok=True); REGISTRY.mkdir(exist_ok=True)
            lines=["# Secret Leak Audit","",f"Generated: {date.today().isoformat()}","",f"- Passed: {not blocking}",f"- Findings: {len(findings)}",f"- Blocking findings: {len(blocking)}","","| Path | Line | Pattern | Tracked | Staged | Ignored |","| --- | ---: | --- | --- | --- | --- |"]
            lines.extend(f"| {f['path']} | {f['line']} | {f['pattern']} | {f['tracked']} | {f['staged']} | {f['ignored']} |" for f in findings)
            (DOCS/"SECRET_LEAK_AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
            (REGISTRY/"secret-leak-audit.json").write_text(json.dumps({"generated":date.today().isoformat(),"passed":not blocking,"findings":findings,"blocking_findings":blocking},indent=2),encoding="utf-8")
            print(f"SECRET LEAK AUDIT {'PASSED' if not blocking else 'FAILED'} ({len(findings)} findings, {len(blocking)} blocking)")
            return 0 if not blocking else 1
        if __name__ == "__main__": raise SystemExit(main())
        ''',
    )

    write(
        ".github/workflows/knowledge-ingestion.yml",
        '''
        name: Knowledge Ingestion

        on:
          workflow_dispatch:
          schedule:
            - cron: "17 2 * * *"

        permissions:
          contents: write
          pull-requests: write

        jobs:
          ingestion:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: actions/setup-python@v5
                with:
                  python-version: "3.x"
              - name: Generate local-first v2 layers
                run: |
                  python scripts/generate_obsidian_vault.py
                  python scripts/generate_obsidian_canvas.py
                  python dashboard/scripts/collect_dashboard_data.py
                  python ingestion/generate_ingestion_report.py
                  python crawler/generate_crawl_report.py
                  python scripts/classify_candidate_knowledge.py --dry-run
                  python scripts/promote_stable_knowledge.py --dry-run
                  python scripts/generate_source_review_from_candidates.py --dry-run
              - name: Audit and acceptance
                run: |
                  python scripts/audit_secret_leaks.py
                  python scripts/run_acceptance.py
              - name: Create pull request
                uses: peter-evans/create-pull-request@v6
                with:
                  commit-message: Automated knowledge ingestion update
                  title: Automated knowledge ingestion update
                  body: |
                    Automated knowledge ingestion update.

                    Includes collected source reports, promoted stable notes if eligible, pending review items, audit status, acceptance status, and source review warnings.
                  branch: automation/knowledge-ingestion
        ''',
    )

    docs = {
        "docs/UPGRADE_V2_OBSIDIAN_RAG_AUTONOMOUS.md": "Agent Wiki Hub v2 adds Obsidian navigation, dashboard data, RAG scaffolding, ingestion and crawler dry-runs, candidate classification, promotion gates, source-review queueing, and audits.",
        "docs/LOCAL_USAGE_GUIDE.md": "Obsidian: open `obsidian-vault/`. Dashboard: run `python dashboard/scripts/collect_dashboard_data.py` and open `dashboard/index.html`. RAG: optionally install `rag/requirements-rag.txt`, then run `python rag/search_knowledge.py --query \"risk control\" --top-k 5`. Crawler: edit `crawler/sources.yaml`, then run dry-runs and review queues.",
        "docs/AUTONOMOUS_KNOWLEDGE_INGESTION.md": "Autonomous ingestion is source-gated. Raw content remains unverified. Stable low-risk candidates may be promoted only through automation-generated files after audits.",
        "docs/KNOWLEDGE_PROMOTION_POLICY.md": "Promotion requires stable_knowledge classification, low risk, no current facts, source_url, source_title, sufficient confidence, no secrets, and automation-generated destinations only.",
    }
    for path, body in docs.items():
        title = Path(path).stem.replace("_", " ").title()
        write(path, f"# {title}\n\n{body}\n")

    print("V2 SCAFFOLD GENERATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
