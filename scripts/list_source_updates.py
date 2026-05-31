#!/usr/bin/env python3
"""Build a queue of topics that require authoritative source updates."""
from pathlib import Path
from datetime import date, datetime
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS_OUT = ROOT / "docs" / "SOURCE_UPDATE_QUEUE.md"
JSON_OUT = ROOT / "registry" / "source-update-queue.json"

RISK_SCORE = {"high": 3, "medium": 2, "low": 1}
FRESHNESS_SCORE = {"high": 3, "medium": 2, "low": 1}
REVIEW_WINDOW_DAYS = {"high": 30, "medium": 90, "low": 180}


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


def parse_date(value: str):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_source_notes(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    current = None
    in_sources = False
    for raw in read_text(path).splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("- topic:"):
            if current:
                records.append(current)
            current = {
                "topic": stripped.split(":", 1)[1].strip(),
                "status": "",
                "suggested_sources": [],
                "last_checked": "",
            }
            in_sources = False
        elif current and stripped.startswith("status:"):
            current["status"] = stripped.split(":", 1)[1].strip()
            in_sources = False
        elif current and stripped.startswith("suggested_sources:"):
            in_sources = True
        elif current and stripped.startswith("last_checked:"):
            current["last_checked"] = stripped.split(":", 1)[1].strip()
            in_sources = False
        elif current and in_sources and stripped.startswith("- "):
            current["suggested_sources"].append(stripped[2:].strip())
    if current:
        records.append(current)
    return records


def queue_items() -> list[dict]:
    today = date.today()
    items = []
    for wiki in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        manifest = parse_manifest(wiki / "manifest.yaml")
        risk = manifest.get("risk_level", "")
        freshness = manifest.get("freshness_requirement", "")
        for record in parse_source_notes(wiki / "sources" / "source-notes.md"):
            last_checked = parse_date(record.get("last_checked", ""))
            age_days = (today - last_checked).days if last_checked else None
            review_window = REVIEW_WINDOW_DAYS.get(freshness, 90)
            is_stale = age_days is None or age_days >= review_window
            priority_score = RISK_SCORE.get(risk, 0) + FRESHNESS_SCORE.get(freshness, 0)
            if record.get("status") == "needs-source-update":
                priority_score += 2
            if is_stale:
                priority_score += 1
            items.append({
                "wiki": wiki.name,
                "domain": manifest.get("domain", ""),
                "risk_level": risk,
                "freshness_requirement": freshness,
                "topic": record.get("topic", ""),
                "status": record.get("status", ""),
                "suggested_sources": record.get("suggested_sources", []),
                "last_checked": record.get("last_checked", ""),
                "age_days": age_days,
                "review_window_days": review_window,
                "is_stale": is_stale,
                "priority_score": priority_score,
            })
    items.sort(key=lambda x: (-x["priority_score"], x["wiki"], x["topic"]))
    return items


def markdown_report(items: list[dict]) -> str:
    high_priority = sum(1 for item in items if item["priority_score"] >= 8)
    stale = sum(1 for item in items if item["is_stale"])
    lines = [
        "# Source Update Queue",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Topics: {len(items)}",
        f"- High-priority topics: {high_priority}",
        f"- Stale or missing last_checked topics: {stale}",
        "",
        "## Queue",
        "",
        "| Priority | Wiki | Risk | Freshness | Topic | Last checked | Suggested sources |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        sources = ", ".join(item["suggested_sources"]) if item["suggested_sources"] else "source needed"
        lines.append(
            f"| {item['priority_score']} | {item['wiki']} | {item['risk_level']} | "
            f"{item['freshness_requirement']} | {item['topic']} | {item['last_checked'] or 'unknown'} | {sources} |"
        )
    lines.extend([
        "",
        "## Usage Notes",
        "",
        "- Treat every row as needing authoritative source verification before writing current facts into a wiki.",
        "- Prefer official documentation, regulator pages, primary datasets, vendor advisories, or licensed professional review as listed.",
        "- After verifying a topic, update the relevant `sources/source-notes.md` with the source, date, and remaining uncertainty.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    items = queue_items()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(items), encoding="utf-8")
    JSON_OUT.write_text(json.dumps({"generated": date.today().isoformat(), "topics": items}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"Queued {len(items)} source-update topics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
