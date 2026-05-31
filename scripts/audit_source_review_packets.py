#!/usr/bin/env python3
"""Audit source-review packet files before import."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
PACKET_DIR = REGISTRY / "source-review-packets"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_PACKET_AUDIT.md"
JSON_OUT = REGISTRY / "source-review-packet-audit.json"
TICKETS_JSON = REGISTRY / "source-refresh-tickets.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}
STATUSES = FINAL_STATUSES | {"pending"}
CONFIDENCE = {"low", "medium", "high"}
PLACEHOLDER_MARKERS = {"<", "YYYY-MM-DD", "unknown", "required"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----", re.I),
    re.compile(r"\b(api[_-]?key|secret[_-]?key|private[_-]?key|access[_-]?token|refresh[_-]?token)\s*[:=]", re.I),
    re.compile(r"\b(cookie|set-cookie|authorization)\s*:", re.I),
    re.compile(r"\bbearer\s+[A-Za-z0-9._~+/=-]{16,}", re.I),
    re.compile(r"\b(seed phrase|mnemonic)\b", re.I),
]

REQUIRED_FINAL_FIELDS = [
    "source_title",
    "source_publisher",
    "source_url_or_reference",
    "source_accessed_on",
    "evidence_summary",
    "confidence",
    "remaining_uncertainty",
]

REPORTS = {
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_review_packet_rehearsal": "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "source_review_packet_bundle": "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
    "source_review_session_plan": "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
}

ADVISORY_PACKET_NAME_PARTS = ("-ai-prefill",)


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def repo_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def bool_word(value: bool) -> str:
    return "yes" if value else "no"


def load_tickets() -> dict[str, dict]:
    data = read_json(TICKETS_JSON)
    records: dict[str, dict] = {}
    for ticket in data.get("tickets", []):
        if ticket.get("ticket_id"):
            records[str(ticket["ticket_id"])] = ticket
        if ticket.get("task_id"):
            records[str(ticket["task_id"])] = ticket
    return records


def packet_paths() -> list[Path]:
    if not PACKET_DIR.exists():
        return []
    return sorted(path for path in PACKET_DIR.iterdir() if path.suffix.lower() in {".json", ".jsonl"} and not path.name.endswith("-manifest.json"))


def packet_manifest(path: Path) -> dict:
    manifest = path.with_name(f"{path.stem}-manifest.json")
    return read_json(manifest)


def packet_metadata(path: Path) -> dict:
    if path.suffix.lower() == ".json":
        try:
            data = read_json(path)
            if isinstance(data, dict):
                return data
        except Exception:
            return {}
    return packet_manifest(path)


def packet_scope(path: Path) -> tuple[bool, str, str]:
    name = path.stem.casefold()
    if any(part in name for part in ADVISORY_PACKET_NAME_PARTS):
        return (
            False,
            "advisory-ai-prefill",
            "AI-prefill packets are historical source-assistance artifacts, not active import packets.",
        )
    metadata = packet_metadata(path)
    if metadata.get("planning_only") or metadata.get("no_current_fact_write"):
        return (
            False,
            "planning-only-pending-packet",
            "Planning-only pending packets are templates for future source review and do not block acceptance.",
        )
    return True, "active-import-packet", ""


def load_packet(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    data = json.loads(text)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("entries"), list):
        return data["entries"]
    if isinstance(data, dict):
        return [data]
    raise ValueError("packet must be a JSON object, object with entries, JSON list, or JSONL")


def value(entry: dict, *names: str) -> str:
    for name in names:
        if name in entry and entry[name] is not None:
            return str(entry[name])
    return ""


def is_placeholder(raw: str | None) -> bool:
    text = (raw or "").strip()
    if not text:
        return True
    lowered = text.casefold()
    return any(marker.casefold() in lowered for marker in PLACEHOLDER_MARKERS)


def has_secret(entry: dict) -> bool:
    text = json.dumps(entry, ensure_ascii=False)
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def duplicate_ticket_ids(entries: list[dict]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for entry in entries:
        ticket_id = value(entry, "ticket_id", "task_id")
        if not ticket_id:
            continue
        if ticket_id in seen:
            duplicates.add(ticket_id)
        seen.add(ticket_id)
    return sorted(duplicates)


def audit_entry(entry: dict, tickets: dict[str, dict], packet_path: Path, index: int) -> dict:
    issues: list[str] = []
    warnings: list[str] = []
    ticket_id = value(entry, "ticket_id", "task_id")
    status = value(entry, "status")
    ticket = tickets.get(ticket_id, {})

    if not ticket_id:
        issues.append("missing ticket_id")
    elif ticket_id not in tickets:
        issues.append("unknown ticket_id")
    if status not in STATUSES:
        issues.append(f"invalid status: {status or '<empty>'}")
    if has_secret(entry):
        issues.append("entry appears to contain a credential, token, cookie, private key, or seed phrase")

    if status == "pending":
        if not any(is_placeholder(value(entry, field)) for field in ["source_title", "source_publisher", "source_url_or_reference"]):
            warnings.append("pending entry has non-placeholder source fields; confirm this is still only a template")
    elif status in FINAL_STATUSES:
        for field in REQUIRED_FINAL_FIELDS:
            if is_placeholder(value(entry, field)):
                issues.append(f"final status requires non-placeholder {field}")
        confidence = value(entry, "confidence")
        if confidence and confidence not in CONFIDENCE:
            issues.append(f"invalid confidence: {confidence}")
        if ticket.get("human_confirmation_required") and is_placeholder(value(entry, "human_reviewer")):
            issues.append("human-gated ticket requires human_reviewer before final status")
    if value(entry, "confidence") and value(entry, "confidence") not in CONFIDENCE:
        issues.append(f"invalid confidence: {value(entry, 'confidence')}")

    return {
        "packet": rel(packet_path),
        "index": index,
        "ticket_id": ticket_id,
        "status": status,
        "wiki": ticket.get("wiki", ""),
        "risk_level": ticket.get("risk_level", ""),
        "human_confirmation_required": bool(ticket.get("human_confirmation_required", False)),
        "issues": issues,
        "warnings": warnings,
        "passed": not issues,
    }


def audit_packet(path: Path, tickets: dict[str, dict]) -> dict:
    blocking, classification, non_blocking_reason = packet_scope(path)
    try:
        entries = load_packet(path)
        duplicates = duplicate_ticket_ids(entries)
        entry_records = [audit_entry(entry, tickets, path, index + 1) for index, entry in enumerate(entries)]
        issues = []
        if duplicates:
            issues.append(f"duplicate ticket ids: {', '.join(duplicates)}")
        issues.extend(f"{record['ticket_id'] or '#'+str(record['index'])}: {issue}" for record in entry_records for issue in record["issues"])
        warnings = [f"{record['ticket_id'] or '#'+str(record['index'])}: {warning}" for record in entry_records for warning in record["warnings"]]
        return {
            "path": rel(path),
            "blocking": blocking,
            "classification": classification,
            "non_blocking_reason": non_blocking_reason,
            "passed": not issues,
            "blocking_passed": (not issues) if blocking else True,
            "entry_count": len(entries),
            "final_entry_count": sum(1 for entry in entries if value(entry, "status") in FINAL_STATUSES),
            "pending_entry_count": sum(1 for entry in entries if value(entry, "status") == "pending"),
            "human_gated_entry_count": sum(1 for record in entry_records if record["human_confirmation_required"]),
            "issues": issues,
            "warnings": warnings,
            "entries": entry_records,
        }
    except Exception as exc:
        return {
            "path": rel(path),
            "blocking": blocking,
            "classification": classification,
            "non_blocking_reason": non_blocking_reason,
            "passed": False,
            "blocking_passed": False if blocking else True,
            "entry_count": 0,
            "final_entry_count": 0,
            "pending_entry_count": 0,
            "human_gated_entry_count": 0,
            "issues": [str(exc)],
            "warnings": [],
            "entries": [],
        }


def build_audit() -> dict:
    tickets = load_tickets()
    paths = packet_paths()
    packets = [audit_packet(path, tickets) for path in paths]
    active_packets = [packet for packet in packets if packet.get("blocking", True)]
    advisory_packets = [packet for packet in packets if not packet.get("blocking", True)]
    planning_packets = [packet for packet in packets if packet.get("classification") == "planning-only-pending-packet"]
    historical_packets = [packet for packet in packets if packet.get("classification") == "advisory-ai-prefill"]
    entry_records = [entry for packet in active_packets for entry in packet.get("entries", [])]
    status_counts = Counter(entry.get("status", "unknown") for entry in entry_records)
    wiki_counts = Counter(entry.get("wiki", "unknown") for entry in entry_records)
    checks = [
        {
            "check": "ticket registry available",
            "passed": TICKETS_JSON.exists() and bool(tickets),
            "detail": rel(TICKETS_JSON) if TICKETS_JSON.exists() else "missing registry/source-refresh-tickets.json",
        },
        {
            "check": "packet directory available",
            "passed": PACKET_DIR.exists(),
            "detail": rel(PACKET_DIR) if PACKET_DIR.exists() else "missing registry/source-review-packets",
        },
        {
            "check": "packet files discovered",
            "passed": bool(paths),
            "detail": f"{len(paths)} discovered packet files",
        },
        {
            "check": "active packet files discovered",
            "passed": bool(active_packets),
            "detail": f"{len(active_packets)} active packet files",
        },
        {
            "check": "active packet files passed",
            "passed": all(packet["blocking_passed"] for packet in active_packets) if active_packets else False,
            "detail": f"{sum(1 for packet in active_packets if packet['blocking_passed'])}/{len(active_packets)} active packets passed",
        },
        {
            "check": "advisory packets do not block acceptance",
            "passed": True,
            "detail": f"{len(advisory_packets)} advisory packet files, {sum(len(packet['issues']) for packet in advisory_packets)} advisory issues",
        },
    ]
    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "purpose": "Audit active source-review packet files before import, while keeping historical AI-prefill packets visible as non-blocking advisory artifacts.",
        "packet_dir": rel(PACKET_DIR),
        "packet_count": len(active_packets),
        "discovered_packet_count": len(packets),
        "advisory_packet_count": len(advisory_packets),
        "planning_packet_count": len(planning_packets),
        "historical_packet_count": len(historical_packets),
        "entry_count": sum(packet["entry_count"] for packet in active_packets),
        "discovered_entry_count": sum(packet["entry_count"] for packet in packets),
        "advisory_entry_count": sum(packet["entry_count"] for packet in advisory_packets),
        "final_entry_count": sum(packet["final_entry_count"] for packet in active_packets),
        "pending_entry_count": sum(packet["pending_entry_count"] for packet in active_packets),
        "issue_count": sum(len(packet["issues"]) for packet in active_packets),
        "advisory_issue_count": sum(len(packet["issues"]) for packet in advisory_packets),
        "warning_count": sum(len(packet["warnings"]) for packet in active_packets),
        "advisory_warning_count": sum(len(packet["warnings"]) for packet in advisory_packets),
        "human_gated_entry_count": sum(packet["human_gated_entry_count"] for packet in active_packets),
        "status_counts": dict(sorted(status_counts.items())),
        "wiki_counts": dict(sorted(wiki_counts.items())),
        "packets": packets,
        "active_packets": active_packets,
        "advisory_packets": advisory_packets,
        "planning_packets": planning_packets,
        "historical_packets": historical_packets,
        "checks": checks,
        "reports": REPORTS,
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Packet Audit",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Purpose",
        "",
        data["purpose"],
        "",
        "## Summary",
        "",
        f"- Passed: {bool_word(data['passed'])}",
        f"- Active packet files: {data['packet_count']}",
        f"- Discovered packet files: {data['discovered_packet_count']}",
        f"- Advisory packet files: {data['advisory_packet_count']}",
        f"- Planning-only packet files: {data['planning_packet_count']}",
        f"- Historical/prefill packet files: {data['historical_packet_count']}",
        f"- Entries: {data['entry_count']}",
        f"- Advisory entries: {data['advisory_entry_count']}",
        f"- Pending entries: {data['pending_entry_count']}",
        f"- Final entries: {data['final_entry_count']}",
        f"- Human-gated entries: {data['human_gated_entry_count']}",
        f"- Issues: {data['issue_count']}",
        f"- Advisory issues: {data['advisory_issue_count']}",
        f"- Warnings: {data['warning_count']}",
        "",
        "## Packets",
        "",
        "| Packet | Scope | Result | Entries | Pending | Final | Human-Gated | Issues | Warnings |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for packet in data["packets"]:
        if packet.get("blocking", True):
            result = "PASS" if packet["passed"] else "FAIL"
        else:
            result = "ADVISORY" if packet["issues"] else "PASS"
        lines.append(
            f"| {repo_link(packet['path'])} | {packet.get('classification', 'active-import-packet')} | {result} | {packet['entry_count']} | {packet['pending_entry_count']} | "
            f"{packet['final_entry_count']} | {packet['human_gated_entry_count']} | {len(packet['issues'])} | {len(packet['warnings'])} |"
        )

    lines.extend(["", "## Status Counts", ""])
    for status, count in data["status_counts"].items():
        lines.append(f"- {status}: {count}")

    lines.extend(["", "## Issues", ""])
    issue_lines = [f"- `{packet['path']}`: {issue}" for packet in data["active_packets"] for issue in packet["issues"]]
    lines.extend(issue_lines or ["No active packet issues found."])

    lines.extend(["", "## Advisory Packet Observations", ""])
    advisory_lines = []
    for packet in data["advisory_packets"]:
        reason = packet.get("non_blocking_reason") or "non-blocking advisory packet"
        if packet["issues"]:
            for issue in packet["issues"]:
                advisory_lines.append(f"- `{packet['path']}`: {reason} Observation: {issue}")
        else:
            advisory_lines.append(f"- `{packet['path']}`: {reason} No issues found.")
    lines.extend(advisory_lines or ["No advisory packet observations."])

    lines.extend(["", "## Warnings", ""])
    warning_lines = [f"- `{packet['path']}`: {warning}" for packet in data["packets"] for warning in packet["warnings"]]
    lines.extend(warning_lines or ["No packet warnings found."])

    lines.extend(["", "## Related Reports", ""])
    for name, path in data["reports"].items():
        lines.append(f"- {name}: {repo_link(path)}")

    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        result = "PASS" if check["passed"] else "FAIL"
        lines.append(f"| {check['check']} | {result} | {check['detail']} |")

    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- This audit does not verify external facts.",
            "- It checks packet structure, final-status readiness, human-review gates, duplicate tickets, and obvious secret patterns.",
            "- Passing this audit does not mean the packet evidence is true or current.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_audit()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"SOURCE REVIEW PACKET AUDIT {'PASSED' if data['passed'] else 'FAILED'} ({data['packet_count']} packets, {data['entry_count']} entries)")
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
