#!/usr/bin/env python3
"""Generate a compact status report for all Agent Wiki packs."""
from pathlib import Path
import json
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS_OUT = ROOT / "docs" / "WIKI_STATUS.md"
JSON_OUT = ROOT / "registry" / "wiki-status.json"
PACKS = ROOT / "packs"
CONTENT_SUFFIXES = {".md", ".yaml", ".yml", ".json"}
REQUIRED_DIRS = ["concepts", "rules", "workflows", "cases", "tools", "prompts", "evals", "sources"]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_manifest(path: Path) -> dict:
    data = {}
    if not path.exists():
        return data
    for line in read_text(path).splitlines():
        if ":" not in line or line.startswith(" ") or line.startswith("-"):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def eval_test_count(path: Path) -> int:
    if not path.exists():
        return 0
    return len(re.findall(r"^\s*-\s+id:\s*", read_text(path), flags=re.MULTILINE))


def source_topics(path: Path) -> list[str]:
    if not path.exists():
        return []
    topics = []
    for line in read_text(path).splitlines():
        stripped = line.strip()
        if stripped.startswith("- topic:"):
            topics.append(stripped.split(":", 1)[1].strip())
    return topics


def wiki_summary(wiki: Path) -> dict:
    manifest = parse_manifest(wiki / "manifest.yaml")
    counts = {}
    for name in REQUIRED_DIRS:
        folder = wiki / name
        counts[name] = 0
        if folder.is_dir():
            counts[name] = sum(1 for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in CONTENT_SUFFIXES)

    eval_count = 0
    eval_dir = wiki / "evals"
    if eval_dir.is_dir():
        eval_count = sum(eval_test_count(p) for p in eval_dir.glob("*.y*ml"))

    pack_path = PACKS / f"{wiki.name}.zip"
    return {
        "id": wiki.name,
        "domain": manifest.get("domain", ""),
        "risk_level": manifest.get("risk_level", ""),
        "freshness_requirement": manifest.get("freshness_requirement", ""),
        "content_counts": counts,
        "eval_tests": eval_count,
        "source_update_topics": source_topics(wiki / "sources" / "source-notes.md"),
        "pack_exists": pack_path.exists(),
        "pack_size_bytes": pack_path.stat().st_size if pack_path.exists() else 0,
    }


def markdown_report(summaries: list[dict]) -> str:
    total_docs = sum(sum(item["content_counts"].values()) for item in summaries)
    total_evals = sum(item["eval_tests"] for item in summaries)
    total_topics = sum(len(item["source_update_topics"]) for item in summaries)
    lines = [
        "# Agent Wiki Hub Status",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Wikis: {len(summaries)}",
        f"- Knowledge files in required directories: {total_docs}",
        f"- Eval tests: {total_evals}",
        f"- Needs-source-update topics: {total_topics}",
        "",
        "## Wiki Matrix",
        "",
        "| Wiki | Domain | Risk | Freshness | Cases | Evals | Source topics | Pack |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for item in summaries:
        counts = item["content_counts"]
        pack = f"{item['pack_size_bytes']} bytes" if item["pack_exists"] else "missing"
        lines.append(
            f"| {item['id']} | {item['domain']} | {item['risk_level']} | "
            f"{item['freshness_requirement']} | {counts.get('cases', 0)} | "
            f"{item['eval_tests']} | {len(item['source_update_topics'])} | {pack} |"
        )

    lines.extend(["", "## Needs Source Update Topics", ""])
    for item in summaries:
        lines.append(f"### {item['id']}")
        topics = item["source_update_topics"]
        if not topics:
            lines.append("- none")
        else:
            for topic in topics:
                lines.append(f"- {topic}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    summaries = [wiki_summary(p) for p in sorted(WIKIS.iterdir()) if p.is_dir()]
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps({"generated": date.today().isoformat(), "wikis": summaries}, ensure_ascii=False, indent=2), encoding="utf-8")
    DOCS_OUT.write_text(markdown_report(summaries), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
