#!/usr/bin/env python3
"""Audit Markdown page metadata for wiki knowledge pages."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS_OUT = ROOT / "docs" / "PAGE_METADATA_AUDIT.md"
JSON_OUT = ROOT / "registry" / "page-metadata-audit.json"

KNOWLEDGE_DIRS = {"concepts", "rules", "workflows", "cases", "tools", "prompts"}
EXEMPT_NAMES = {"README.md", "AGENTS.md", "update-log.md", "source-notes.md"}
REQUIRED_FIELDS = ["title", "status", "last_updated", "risk_level"]
VALID_STATUS = {"draft", "stable", "needs-source-update"}
VALID_RISK_LEVELS = {"low", "medium", "high"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw in read_text(path).splitlines():
        if ":" not in raw or raw.startswith(" ") or raw.lstrip().startswith("-"):
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def parse_front_matter(text: str) -> tuple[dict[str, str], bool, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, False, "missing opening ---"
    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break
    if end_index is None:
        return {}, False, "missing closing ---"

    fields: dict[str, str] = {}
    for raw in lines[1:end_index]:
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    body = "\n".join(lines[end_index + 1 :])
    return fields, True, body


def first_h1(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def knowledge_pages() -> list[Path]:
    pages: list[Path] = []
    if not WIKIS.exists():
        return pages
    for wiki in sorted(path for path in WIKIS.iterdir() if path.is_dir()):
        for dirname in KNOWLEDGE_DIRS:
            folder = wiki / dirname
            if folder.exists():
                pages.extend(sorted(path for path in folder.rglob("*.md") if path.name not in EXEMPT_NAMES))
    return pages


def audit_page(path: Path) -> dict:
    wiki = path.parts[path.parts.index("wikis") + 1]
    dirname = path.parts[path.parts.index(wiki) + 1]
    manifest = parse_manifest(ROOT / "wikis" / wiki / "manifest.yaml")
    wiki_risk = manifest.get("risk_level", "")
    text = read_text(path)
    fields, has_front_matter, body_or_reason = parse_front_matter(text)
    issues: list[str] = []

    if not has_front_matter:
        issues.append(body_or_reason)
        body = text
    else:
        body = body_or_reason

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            issues.append(f"missing {field}")

    if fields.get("status") and fields["status"] not in VALID_STATUS:
        issues.append(f"invalid status {fields['status']!r}")
    if fields.get("risk_level") and fields["risk_level"] not in VALID_RISK_LEVELS:
        issues.append(f"invalid risk_level {fields['risk_level']!r}")
    if fields.get("last_updated") and not valid_date(fields["last_updated"]):
        issues.append(f"invalid last_updated {fields['last_updated']!r}")

    title = fields.get("title", "")
    h1 = first_h1(body)
    if not h1:
        issues.append("missing H1")
    elif title and title.casefold() != h1.casefold():
        issues.append(f"title/H1 mismatch: {title!r} vs {h1!r}")

    if wiki_risk == "high" and fields.get("risk_level") == "low":
        issues.append("high-risk wiki page cannot be low risk")

    return {
        "wiki": wiki,
        "directory": dirname,
        "path": path.relative_to(ROOT).as_posix(),
        "title": title,
        "status": fields.get("status", ""),
        "last_updated": fields.get("last_updated", ""),
        "risk_level": fields.get("risk_level", ""),
        "wiki_risk_level": wiki_risk,
        "h1": h1,
        "passed": not issues,
        "issues": issues,
    }


def markdown_report(records: list[dict]) -> str:
    failed = [record for record in records if not record["passed"]]
    by_wiki = Counter(record["wiki"] for record in records)
    status_counts = Counter(record["status"] or "<missing>" for record in records)
    risk_counts = Counter(record["risk_level"] or "<missing>" for record in records)

    lines = [
        "# Page Metadata Audit",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Knowledge pages checked: {len(records)}",
        f"- Passed: {len(records) - len(failed)}",
        f"- Failed: {len(failed)}",
        "",
        "## Counts By Wiki",
        "",
        "| Wiki | Pages |",
        "| --- | ---: |",
    ]
    for wiki, count in sorted(by_wiki.items()):
        lines.append(f"| {wiki} | {count} |")

    lines.extend(["", "## Status Counts", "", "| Status | Pages |", "| --- | ---: |"])
    for status, count in sorted(status_counts.items()):
        lines.append(f"| {status} | {count} |")

    lines.extend(["", "## Risk Counts", "", "| Risk | Pages |", "| --- | ---: |"])
    for risk, count in sorted(risk_counts.items()):
        lines.append(f"| {risk} | {count} |")

    lines.extend(["", "## Failed Pages", ""])
    if failed:
        lines.extend(["| Page | Issues |", "| --- | --- |"])
        for record in failed:
            lines.append(f"| {record['path']} | {'; '.join(record['issues'])} |")
    else:
        lines.append("No metadata issues found.")

    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- This audit checks knowledge pages in `concepts/`, `rules/`, `workflows/`, `cases/`, `tools/`, and `prompts/`.",
            "- `README.md`, `AGENTS.md`, `update-log.md`, and `sources/source-notes.md` are intentionally exempt because they are entrypoint, routing, log, or source queue files.",
            "- Use `needs-source-update` status only when the page itself contains current facts that must be refreshed before reuse.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    records = [audit_page(path) for path in knowledge_pages()]
    failed = [record for record in records if not record["passed"]]
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(records), encoding="utf-8")
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": not failed, "pages": records}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if failed:
        print("PAGE METADATA AUDIT FAILED")
        for record in failed:
            print(f"- {record['path']}: {'; '.join(record['issues'])}")
        return 1
    print(f"PAGE METADATA AUDIT PASSED ({len(records)} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
