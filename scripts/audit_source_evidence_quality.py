#!/usr/bin/env python3
"""Audit quality of completed source evidence entries."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
TICKETS_JSON = ROOT / "registry" / "source-refresh-tickets.json"
DOCS_OUT = ROOT / "docs" / "SOURCE_EVIDENCE_QUALITY_AUDIT.md"
JSON_OUT = ROOT / "registry" / "source-evidence-quality-audit.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}
OPEN_STATUSES = {"pending"}
VALID_STATUSES = FINAL_STATUSES | OPEN_STATUSES
CONFIDENCE = {"low", "medium", "high"}
COMPLETED_MARKER = "## Completed Entries"
PLACEHOLDER_MARKERS = {"<", "YYYY-MM-DD", "required"}
KNOWN_ROOTS = {"wikis", "docs", "registry", "scripts", "codex-skills", "index", "packs"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----", re.I),
    re.compile(r"\b(api[_-]?key|secret[_-]?key|private[_-]?key|access[_-]?token|refresh[_-]?token)\s*[:=]", re.I),
    re.compile(r"\b(cookie|set-cookie|authorization)\s*:", re.I),
    re.compile(r"\bbearer\s+[A-Za-z0-9._~+/=-]{16,}", re.I),
    re.compile(r"\b(seed phrase|mnemonic)\b", re.I),
]


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def md_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def strip_scalar(value: str) -> str:
    value = (value or "").strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def completed_section(text: str) -> str:
    if COMPLETED_MARKER not in text:
        return ""
    section = text.split(COMPLETED_MARKER, 1)[1]
    next_heading = re.search(r"\n## ", section)
    if next_heading:
        section = section[: next_heading.start()]
    return section


def parse_completed_entries(log_text: str, wiki: str, log_path: Path) -> list[dict]:
    section = completed_section(log_text)
    entries: list[dict] = []
    current: dict[str, object] | None = None
    current_list_key: str | None = None
    for raw in section.splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("<"):
            continue
        if stripped.startswith("- task_id:"):
            if current:
                entries.append(current)
            current = {
                "wiki": wiki,
                "log_path": rel(log_path),
                "task_id": strip_scalar(stripped.split(":", 1)[1].strip()),
                "affected_pages": [],
            }
            current_list_key = None
            continue
        if current is None:
            continue
        if current_list_key and stripped.startswith("- "):
            current.setdefault(current_list_key, [])
            current[current_list_key].append(strip_scalar(stripped[2:].strip()))
            continue
        if ":" in stripped and not stripped.startswith("- "):
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = strip_scalar(value.strip())
            if value:
                current[key] = value
                current_list_key = None
            else:
                current[key] = []
                current_list_key = key
    if current:
        entries.append(current)
    return entries


def load_entries() -> list[dict]:
    entries: list[dict] = []
    for wiki in sorted(path for path in WIKIS.iterdir() if path.is_dir()):
        log_path = wiki / "sources" / "source-refresh-log.md"
        entries.extend(parse_completed_entries(read_text(log_path), wiki.name, log_path))
    return entries


def tickets_by_id() -> dict[str, dict]:
    data = read_json(TICKETS_JSON)
    records: dict[str, dict] = {}
    for ticket in data.get("tickets", []):
        if ticket.get("ticket_id"):
            records[ticket["ticket_id"]] = ticket
        if ticket.get("task_id"):
            records[ticket["task_id"]] = ticket
    return records


def is_placeholder(value: str | None, allow_unknown: bool = False) -> bool:
    value = (value or "").strip()
    if not value:
        return True
    lowered = value.casefold()
    if not allow_unknown and lowered == "unknown":
        return True
    return any(marker.casefold() in lowered for marker in PLACEHOLDER_MARKERS)


def valid_date(value: str | None) -> bool:
    try:
        datetime.strptime((value or "").strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False


def reference_quality(value: str | None) -> tuple[list[str], list[str]]:
    issues: list[str] = []
    warnings: list[str] = []
    value = (value or "").strip()
    if is_placeholder(value):
        issues.append("missing source_url_or_reference")
        return issues, warnings
    lowered = value.casefold()
    if "example.invalid" in lowered or "example.com" in lowered:
        issues.append("source_url_or_reference uses an example domain")
    if value.startswith(("http://", "https://")):
        if " " in value:
            issues.append("source URL contains spaces")
    elif len(value) < 8:
        warnings.append("source reference is short and may be hard to audit")
    return issues, warnings


def affected_page_path(entry: dict, raw_path: str) -> Path:
    raw = raw_path.strip().replace("\\", "/")
    if not raw:
        return ROOT / "__missing__"
    first = raw.split("/", 1)[0]
    if first in KNOWN_ROOTS:
        return ROOT / raw
    return ROOT / "wikis" / str(entry.get("wiki", "")) / raw


def has_secret(entry: dict) -> bool:
    text = json.dumps(entry, ensure_ascii=False)
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def entry_quality(entry: dict, tickets: dict[str, dict]) -> dict:
    ticket = tickets.get(str(entry.get("ticket_id", ""))) or tickets.get(str(entry.get("task_id", "")))
    status = str(entry.get("status", "")).strip()
    issues: list[str] = []
    warnings: list[str] = []

    if not ticket:
        issues.append("entry does not match a known ticket")
    elif ticket.get("wiki") != entry.get("wiki"):
        issues.append("entry wiki does not match ticket wiki")
    if status not in VALID_STATUSES:
        issues.append(f"invalid status: {status or '<missing>'}")
    if has_secret(entry):
        issues.append("entry appears to contain a credential, token, cookie, private key, or seed phrase")

    final = status in FINAL_STATUSES
    if final:
        required = [
            "source_title",
            "source_publisher",
            "source_url_or_reference",
            "source_accessed_on",
            "evidence_summary",
            "confidence",
            "remaining_uncertainty",
        ]
        for field in required:
            if is_placeholder(str(entry.get(field, ""))):
                issues.append(f"missing or placeholder field: {field}")
        if not valid_date(str(entry.get("source_accessed_on", ""))):
            issues.append("source_accessed_on must be YYYY-MM-DD")
        if not valid_date(str(entry.get("verified_on", ""))):
            issues.append("verified_on must be YYYY-MM-DD")
        published = str(entry.get("source_published_or_updated", "")).strip()
        if published and published.casefold() != "unknown" and not valid_date(published):
            warnings.append("source_published_or_updated is not YYYY-MM-DD or unknown")
        if str(entry.get("confidence", "")).strip() not in CONFIDENCE:
            issues.append("confidence must be low, medium, or high")
        if len(str(entry.get("evidence_summary", "")).strip()) < 20:
            issues.append("evidence_summary is too short for auditability")
        if "dry run" in str(entry.get("evidence_summary", "")).casefold():
            issues.append("evidence_summary appears to describe a dry run")
        if ticket and ticket.get("human_confirmation_required") and is_placeholder(str(entry.get("human_reviewer", ""))):
            issues.append("high-risk ticket requires human_reviewer")

    ref_issues, ref_warnings = reference_quality(str(entry.get("source_url_or_reference", "")))
    if final:
        issues.extend(ref_issues)
        warnings.extend(ref_warnings)

    affected_pages = entry.get("affected_pages", [])
    if isinstance(affected_pages, str):
        affected_pages = [affected_pages]
    if final and not affected_pages:
        issues.append("affected_pages is empty")
    for page in affected_pages:
        path = affected_page_path(entry, str(page))
        if not path.exists():
            issues.append(f"affected page does not exist: {page}")

    return {
        "ticket_id": entry.get("ticket_id", ""),
        "task_id": entry.get("task_id", ""),
        "wiki": entry.get("wiki", ""),
        "log_path": entry.get("log_path", ""),
        "status": status,
        "confidence": entry.get("confidence", ""),
        "is_final": final,
        "matched_ticket": bool(ticket),
        "issues": issues,
        "warnings": warnings,
        "passed": not issues,
    }


def build_audit() -> dict:
    entries = load_entries()
    tickets = tickets_by_id()
    results = [entry_quality(entry, tickets) for entry in entries]
    issue_results = [result for result in results if result["issues"]]
    warning_results = [result for result in results if result["warnings"]]
    status_counts = Counter(result["status"] or "missing" for result in results)
    wiki_counts = Counter(result["wiki"] for result in results)
    passed = not issue_results
    return {
        "generated": date.today().isoformat(),
        "passed": passed,
        "entry_count": len(results),
        "final_entry_count": sum(1 for result in results if result["is_final"]),
        "issue_count": sum(len(result["issues"]) for result in results),
        "warning_count": sum(len(result["warnings"]) for result in results),
        "status_counts": dict(sorted(status_counts.items())),
        "wiki_counts": dict(sorted(wiki_counts.items())),
        "entries": results,
        "issues": issue_results,
        "warnings": warning_results,
    }


def markdown_report(audit: dict) -> str:
    lines = [
        "# Source Evidence Quality Audit",
        "",
        f"Generated: {audit['generated']}",
        "",
        "## Purpose",
        "",
        "This audit checks quality of completed source evidence entries. It does not verify external sources or certify current facts by itself.",
        "",
        "## Summary",
        "",
        f"- Evidence entries: {audit['entry_count']}",
        f"- Final entries: {audit['final_entry_count']}",
        f"- Issues: {audit['issue_count']}",
        f"- Warnings: {audit['warning_count']}",
        f"- Audit passed: {'yes' if audit['passed'] else 'no'}",
        "",
    ]
    if audit["entry_count"] == 0:
        lines.extend(
            [
                "No completed evidence entries were found. This is acceptable for an unrefreshed offline pack; source tickets remain open until evidence is recorded.",
                "",
            ]
        )

    lines.extend(["## Status Counts", "", "| Status | Entries |", "| --- | ---: |"])
    if audit["status_counts"]:
        for status, count in audit["status_counts"].items():
            lines.append(f"| {status} | {count} |")
    else:
        lines.append("| none | 0 |")

    lines.extend(["", "## Entries", ""])
    if audit["entries"]:
        lines.extend(["| Ticket | Wiki | Status | Confidence | Result | Log |", "| --- | --- | --- | --- | --- | --- |"])
        for item in audit["entries"]:
            result = "PASS" if item["passed"] else "FAIL"
            lines.append(
                f"| {item['ticket_id'] or item['task_id']} | {item['wiki']} | {item['status']} | "
                f"{item['confidence']} | {result} | {md_link(item['log_path'])} |"
            )
    else:
        lines.append("No entries to list.")

    lines.extend(["", "## Issues", ""])
    if audit["issues"]:
        lines.extend(["| Ticket | Wiki | Issues |", "| --- | --- | --- |"])
        for item in audit["issues"]:
            lines.append(f"| {item['ticket_id'] or item['task_id']} | {item['wiki']} | {'; '.join(item['issues'])} |")
    else:
        lines.append("No evidence quality issues found.")

    lines.extend(["", "## Warnings", ""])
    if audit["warnings"]:
        lines.extend(["| Ticket | Wiki | Warnings |", "| --- | --- | --- |"])
        for item in audit["warnings"]:
            lines.append(f"| {item['ticket_id'] or item['task_id']} | {item['wiki']} | {'; '.join(item['warnings'])} |")
    else:
        lines.append("No evidence quality warnings found.")

    lines.extend(
        [
            "",
            "## Quality Rules",
            "",
            "- Final evidence must include source title, publisher, reference, access date, evidence summary, confidence, and remaining uncertainty.",
            "- High-risk tickets require a human reviewer.",
            "- Dates must use `YYYY-MM-DD` except `source_published_or_updated`, which may be `unknown` when the source does not publish a date.",
            "- Evidence must not include API keys, private keys, cookies, authorization headers, bearer tokens, seed phrases, or mnemonics.",
            "- A `verified` entry does not remove human confirmation requirements for high-risk domains.",
            "",
            "## Re-run",
            "",
            "```bash",
            "python3 scripts/audit_source_evidence_quality.py",
            "python3 scripts/run_acceptance.py",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    audit = build_audit()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(audit), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if not audit["passed"]:
        print("SOURCE EVIDENCE QUALITY AUDIT FAILED")
        return 1
    print(f"SOURCE EVIDENCE QUALITY AUDIT PASSED ({audit['entry_count']} entries, {audit['issue_count']} issues)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
