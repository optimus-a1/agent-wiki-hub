#!/usr/bin/env python3
"""Generate knowledge density metrics for all wikis."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"
AREAS = ["concepts", "rules", "workflows", "cases", "prompts"]


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if ":" not in raw or raw.startswith(" ") or raw.lstrip().startswith("-"):
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def eval_count(wiki: Path) -> int:
    count = 0
    for path in (wiki / "evals").glob("*.y*ml"):
        count += sum(1 for line in path.read_text(encoding="utf-8", errors="ignore").splitlines() if re.match(r"\s*-\s+id:", line))
    return count


def generated_count(wiki: Path) -> int:
    count = 0
    for area in AREAS:
        for path in (wiki / area).glob("*.md"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "generated_by: codex" in text and "source_status: model-synthesized-stable" in text:
                count += 1
    return count


def density_group(record: dict) -> str:
    total = sum(record["counts"][area] for area in AREAS)
    if total >= 45 and record["eval_tests"] >= 15:
        return "high-density"
    if total >= 28 and record["eval_tests"] >= 8:
        return "medium-density"
    return "low-density"


def main() -> int:
    records = []
    for wiki in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        manifest = parse_manifest(wiki / "manifest.yaml")
        counts = {area: sum(1 for p in (wiki / area).glob("*.md")) for area in AREAS}
        record = {
            "wiki": wiki.name,
            "priority": manifest.get("priority", ""),
            "domain": manifest.get("domain", ""),
            "risk_level": manifest.get("risk_level", ""),
            "counts": counts,
            "eval_tests": eval_count(wiki),
            "generated_stable_pages": generated_count(wiki),
        }
        record["knowledge_density_group"] = density_group(record)
        records.append(record)

    groups = Counter(record["knowledge_density_group"] for record in records)
    payload = {
        "generated": date.today().isoformat(),
        "passed": True,
        "wiki_count": len(records),
        "groups": dict(sorted(groups.items())),
        "records": records,
    }
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "knowledge-density-report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Knowledge Density Report",
        "",
        f"Generated: {payload['generated']}",
        "",
        "| Wiki | Group | Concepts | Rules | Workflows | Cases | Prompts | Eval Tests | Generated Stable Pages |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for record in records:
        c = record["counts"]
        lines.append(
            f"| {record['wiki']} | {record['knowledge_density_group']} | {c['concepts']} | {c['rules']} | "
            f"{c['workflows']} | {c['cases']} | {c['prompts']} | {record['eval_tests']} | {record['generated_stable_pages']} |"
        )
    (DOCS / "KNOWLEDGE_DENSITY_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"KNOWLEDGE DENSITY REPORT GENERATED ({len(records)} wikis)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
