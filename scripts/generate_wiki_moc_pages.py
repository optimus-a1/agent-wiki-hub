#!/usr/bin/env python3
"""Generate root MOC.md pages for each wiki."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"
AREAS = ["concepts", "rules", "workflows", "cases", "prompts", "evals"]


def title(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"')
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def main() -> int:
    records = []
    for wiki in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        lines = [
            "---",
            f"title: \"{wiki.name} MOC\"",
            f"wiki: \"{wiki.name}\"",
            "type: moc",
            "status: stable-general-knowledge",
            "source_status: model-synthesized-stable",
            "current_fact: false",
            "requires_source_review: false",
            "requires_human_review: false",
            "risk_level: medium",
            "generated_by: codex",
            f"generated_on: {date.today().isoformat()}",
            "agent_use: true",
            "tags:",
            "  - agent-wiki",
            "  - stable-knowledge",
            "---",
            "",
            f"# {wiki.name} MOC",
            "",
            "This root map links stable wiki pages. It does not certify current facts.",
        ]
        counts = {}
        for area in AREAS:
            files = sorted(path for path in (wiki / area).glob("*") if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml"})
            counts[area] = len(files)
            lines.extend(["", f"## {area.title()}", ""])
            for item in files:
                rel = item.relative_to(wiki).as_posix()
                lines.append(f"- [{title(item)}]({rel})")
        out = wiki / "MOC.md"
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        records.append({"wiki": wiki.name, "path": out.relative_to(ROOT).as_posix(), "counts": counts})
    payload = {"generated": date.today().isoformat(), "passed": True, "records": records}
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "wiki-moc-report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Wiki MOC Report", "", f"Generated: {payload['generated']}", "", "| Wiki | MOC | Concepts | Rules | Workflows | Cases | Prompts | Evals |", "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for record in records:
        c = record["counts"]
        lines.append(f"| {record['wiki']} | {record['path']} | {c['concepts']} | {c['rules']} | {c['workflows']} | {c['cases']} | {c['prompts']} | {c['evals']} |")
    (DOCS / "WIKI_MOC_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WIKI MOC PAGES GENERATED ({len(records)} wikis)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
