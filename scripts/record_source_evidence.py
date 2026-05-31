#!/usr/bin/env python3
"""Append a completed source evidence entry for a source refresh ticket."""
from __future__ import annotations

from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TICKETS_JSON = ROOT / "registry" / "source-refresh-tickets.json"
FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}
STATUSES = sorted(FINAL_STATUSES | {"pending"})
CONFIDENCE = {"low", "medium", "high"}
COMPLETED_MARKER = "## Completed Entries"
PLACEHOLDER_MARKERS = {"<", "YYYY-MM-DD", "unknown", "required"}
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


def load_ticket(ticket_id: str) -> dict:
    data = read_json(TICKETS_JSON)
    for ticket in data.get("tickets", []):
        if ticket.get("ticket_id") == ticket_id or ticket.get("task_id") == ticket_id:
            return ticket
    raise ValueError(f"ticket not found: {ticket_id}")


def is_placeholder(value: str | None) -> bool:
    value = (value or "").strip()
    if not value:
        return True
    lowered = value.casefold()
    return any(marker.casefold() in lowered for marker in PLACEHOLDER_MARKERS)


def ensure_no_secrets(record: dict) -> None:
    text = json.dumps(record, ensure_ascii=False)
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise ValueError("input appears to contain a credential, token, cookie, private key, or seed phrase")


def completed_section(text: str) -> str:
    if COMPLETED_MARKER not in text:
        return ""
    section = text.split(COMPLETED_MARKER, 1)[1]
    next_heading = re.search(r"\n## ", section)
    if next_heading:
        return section[: next_heading.start()]
    return section


def already_recorded(log_text: str, ticket: dict) -> bool:
    section = completed_section(log_text)
    return bool(
        ticket.get("task_id") and ticket["task_id"] in section
        or ticket.get("ticket_id") and ticket["ticket_id"] in section
    )


def yaml_scalar(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return '""'
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def evidence_entry(record: dict) -> str:
    lines = [
        f"- task_id: {record['task_id']}",
        f"  ticket_id: {record['ticket_id']}",
        f"  topic: {yaml_scalar(record['topic'])}",
        f"  status: {record['status']}",
        f"  verified_on: {record['verified_on']}",
        f"  source_title: {yaml_scalar(record['source_title'])}",
        f"  source_publisher: {yaml_scalar(record['source_publisher'])}",
        f"  source_url_or_reference: {yaml_scalar(record['source_url_or_reference'])}",
        f"  source_published_or_updated: {yaml_scalar(record['source_published_or_updated'])}",
        f"  source_accessed_on: {record['source_accessed_on']}",
        f"  evidence_summary: {yaml_scalar(record['evidence_summary'])}",
        "  affected_pages:",
    ]
    lines.extend(f"    - {page}" for page in record["affected_pages"])
    lines.extend(
        [
            f"  confidence: {record['confidence']}",
            f"  remaining_uncertainty: {yaml_scalar(record['remaining_uncertainty'])}",
            f"  human_reviewer: {yaml_scalar(record['human_reviewer'])}",
            f"  follow_up: {yaml_scalar(record['follow_up'])}",
        ]
    )
    return "\n".join(lines) + "\n"


def append_entry(log_text: str, entry: str) -> str:
    if COMPLETED_MARKER not in log_text:
        log_text = log_text.rstrip() + f"\n\n{COMPLETED_MARKER}\n\n"
    marker_index = log_text.index(COMPLETED_MARKER) + len(COMPLETED_MARKER)
    before = log_text[:marker_index]
    after = log_text[marker_index:]
    if "<Add completed evidence entries here." in after:
        after = re.sub(r"\n\n<Add completed evidence entries here\.[^\n]*>\n?", "\n\n", after, count=1)
    insertion = "\n\n" + entry.rstrip() + "\n"
    return before + insertion + after.lstrip("\n")


def update_checkbox(log_text: str, task_id: str) -> str:
    pattern = re.compile(rf"^- \[ \] ({re.escape(task_id)} \| .*)$", re.M)
    return pattern.sub(r"- [x] \1", log_text)


def update_log(wiki: str, message: str) -> None:
    path = ROOT / "wikis" / wiki / "update-log.md"
    text = read_text(path)
    today = date.today().isoformat()
    heading = f"## {today}"
    bullet = f"- {message}"
    if bullet in text:
        return
    if heading in text:
        text = text.replace(heading, f"{heading}\n\n{bullet}", 1)
    else:
        prefix = text.rstrip() + "\n\n" if text.strip() else ""
        text = f"{prefix}{heading}\n\n{bullet}\n"
    path.write_text(text, encoding="utf-8")


def build_record(args, ticket: dict) -> dict:
    affected_pages = args.affected_page or [ticket.get("source_notes_path") or f"wikis/{ticket['wiki']}/sources/source-notes.md"]
    record = {
        "task_id": ticket.get("task_id", ""),
        "ticket_id": ticket.get("ticket_id", ""),
        "topic": ticket.get("topic", ""),
        "status": args.status,
        "verified_on": args.verified_on or date.today().isoformat(),
        "source_title": args.source_title or "",
        "source_publisher": args.source_publisher or "",
        "source_url_or_reference": args.source_url_or_reference or "",
        "source_published_or_updated": args.source_published_or_updated or "unknown",
        "source_accessed_on": args.source_accessed_on or date.today().isoformat(),
        "evidence_summary": args.evidence_summary or "",
        "affected_pages": affected_pages,
        "confidence": args.confidence or "",
        "remaining_uncertainty": args.remaining_uncertainty or "",
        "human_reviewer": args.human_reviewer or "",
        "follow_up": args.follow_up or "none",
    }
    return record


def validate_record(record: dict, ticket: dict) -> None:
    if record["status"] not in STATUSES:
        raise ValueError(f"invalid status: {record['status']}")
    if record["confidence"] and record["confidence"] not in CONFIDENCE:
        raise ValueError(f"invalid confidence: {record['confidence']}")
    if record["status"] in FINAL_STATUSES:
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
            if is_placeholder(str(record.get(field, ""))):
                raise ValueError(f"final evidence requires non-placeholder {field}")
        if ticket.get("human_confirmation_required") and is_placeholder(record.get("human_reviewer", "")):
            raise ValueError("this high-risk ticket requires --human-reviewer")
    ensure_no_secrets(record)


def run_audits() -> int:
    failures = 0
    for script in ["scripts/audit_source_refresh_completion.py", "scripts/audit_source_evidence_quality.py"]:
        proc = subprocess.run(
            [sys.executable, script],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(proc.stdout.strip())
        if proc.returncode != 0:
            failures += 1
    return 1 if failures else 0


def main() -> int:
    parser = ArgumentParser(description="Record source evidence for a source refresh ticket.")
    parser.add_argument("--ticket-id", required=True, help="Ticket id such as TICKET-SRC-006 or task id such as SRC-006.")
    parser.add_argument("--status", choices=STATUSES, required=True)
    parser.add_argument("--source-title")
    parser.add_argument("--source-publisher")
    parser.add_argument("--source-url-or-reference")
    parser.add_argument("--source-published-or-updated")
    parser.add_argument("--source-accessed-on")
    parser.add_argument("--verified-on")
    parser.add_argument("--evidence-summary")
    parser.add_argument("--affected-page", action="append", help="Affected repo path. Can be repeated.")
    parser.add_argument("--confidence", choices=sorted(CONFIDENCE))
    parser.add_argument("--remaining-uncertainty")
    parser.add_argument("--human-reviewer")
    parser.add_argument("--follow-up")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-duplicate", action="store_true")
    parser.add_argument("--no-audit", action="store_true", help="Skip completion audit after writing.")
    args = parser.parse_args()

    try:
        ticket = load_ticket(args.ticket_id)
        record = build_record(args, ticket)
        validate_record(record, ticket)
        entry = evidence_entry(record)
        log_path = ROOT / "wikis" / ticket["wiki"] / "sources" / "source-refresh-log.md"
        log_text = read_text(log_path)
        if not log_path.exists():
            raise ValueError(f"missing source refresh log: {rel(log_path)}")
        if already_recorded(log_text, ticket) and not args.allow_duplicate:
            raise ValueError("completed evidence already exists for this ticket; use --allow-duplicate to append another entry")
        if args.dry_run:
            print(entry.rstrip())
            return 0
        updated = append_entry(log_text, entry)
        updated = update_checkbox(updated, ticket["task_id"])
        log_path.write_text(updated, encoding="utf-8")
        update_log(ticket["wiki"], f"Recorded source evidence for `{ticket['ticket_id']}` with status `{record['status']}`.")
        print(f"Wrote {rel(log_path)}")
        print(f"Recorded {ticket['ticket_id']} as {record['status']}")
        if not args.no_audit:
            return run_audits()
        return 0
    except Exception as exc:
        print(f"record_source_evidence failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
