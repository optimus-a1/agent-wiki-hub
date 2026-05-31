#!/usr/bin/env python3
"""Import a JSON or JSONL packet of source evidence entries."""
from __future__ import annotations

from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
TICKETS_JSON = REGISTRY / "source-refresh-tickets.json"
DOCS_OUT = ROOT / "docs" / "SOURCE_EVIDENCE_PACKET_IMPORTER.md"
JSON_OUT = REGISTRY / "source-evidence-packet-importer.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}
STATUSES = sorted(FINAL_STATUSES | {"pending"})
CONFIDENCE = {"low", "medium", "high"}

PACKET_FIELDS = [
    "ticket_id",
    "status",
    "source_title",
    "source_publisher",
    "source_url_or_reference",
    "source_published_or_updated",
    "source_accessed_on",
    "verified_on",
    "evidence_summary",
    "affected_pages",
    "confidence",
    "remaining_uncertainty",
    "human_reviewer",
    "follow_up",
]

POST_CHECKS = [
    "scripts/audit_source_refresh_completion.py",
    "scripts/audit_source_evidence_quality.py",
    "scripts/generate_source_refresh_wave_runner.py",
    "scripts/generate_source_reviewer_queue.py",
    "scripts/generate_source_review_session_plan.py",
    "scripts/generate_source_review_packet_bundle.py",
    "scripts/audit_source_review_packets.py",
    "scripts/rehearse_source_review_packet_imports.py",
    "scripts/generate_source_review_readiness_matrix.py",
    "scripts/generate_source_review_work_orders.py",
    "scripts/generate_source_refresh_dashboard.py",
    "scripts/generate_agent_handoff.py",
    "scripts/update_index.py",
    "scripts/run_acceptance.py",
]


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def doc_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def load_tickets() -> dict[str, dict]:
    data = read_json(TICKETS_JSON)
    tickets: dict[str, dict] = {}
    for ticket in data.get("tickets", []):
        if ticket.get("ticket_id"):
            tickets[ticket["ticket_id"]] = ticket
        if ticket.get("task_id"):
            tickets[ticket["task_id"]] = ticket
    return tickets


def packet_template(ticket_id: str = "TICKET-SRC-006") -> dict:
    tickets = load_tickets()
    ticket = tickets.get(ticket_id, {})
    return {
        "packet_id": "source-evidence-packet-example",
        "created_on": date.today().isoformat(),
        "created_by": "<human reviewer or source-refresh agent>",
        "entries": [
            {
                "ticket_id": ticket.get("ticket_id", ticket_id),
                "status": "still-needs-source-update",
                "source_title": "<source title>",
                "source_publisher": "<official publisher or authority>",
                "source_url_or_reference": "<URL or local reference>",
                "source_published_or_updated": "YYYY-MM-DD | unknown",
                "source_accessed_on": date.today().isoformat(),
                "verified_on": date.today().isoformat(),
                "evidence_summary": "<what the source supports and what it does not support>",
                "affected_pages": [
                    ticket.get("source_notes_path") or f"wikis/{ticket.get('wiki', 'finance-agent-wiki')}/sources/source-notes.md"
                ],
                "confidence": "low",
                "remaining_uncertainty": "<unknown, stale, conflicting, or out-of-scope facts>",
                "human_reviewer": "<required for high-risk tickets>",
                "follow_up": "none",
            }
        ],
    }


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
    raise ValueError("packet must be a JSON object, a JSON object with entries, a JSON list, or JSONL")


def value(entry: dict, *names: str) -> str | None:
    for name in names:
        if name in entry and entry[name] is not None:
            return str(entry[name])
    return None


def list_value(entry: dict, name: str) -> list[str]:
    raw = entry.get(name)
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(item) for item in raw]
    return [str(raw)]


def entry_command(entry: dict, dry_run: bool, allow_duplicate: bool, no_audit: bool) -> list[str]:
    ticket_id = value(entry, "ticket_id", "task_id")
    if not ticket_id:
        raise ValueError("entry is missing ticket_id")
    status = value(entry, "status")
    if status not in STATUSES:
        raise ValueError(f"{ticket_id}: invalid status {status!r}")

    args = [
        sys.executable,
        "scripts/record_source_evidence.py",
        "--ticket-id",
        ticket_id,
        "--status",
        status,
    ]
    field_flags = [
        ("source_title", "--source-title"),
        ("source_publisher", "--source-publisher"),
        ("source_url_or_reference", "--source-url-or-reference"),
        ("source_published_or_updated", "--source-published-or-updated"),
        ("source_accessed_on", "--source-accessed-on"),
        ("verified_on", "--verified-on"),
        ("evidence_summary", "--evidence-summary"),
        ("confidence", "--confidence"),
        ("remaining_uncertainty", "--remaining-uncertainty"),
        ("human_reviewer", "--human-reviewer"),
        ("follow_up", "--follow-up"),
    ]
    for field, flag in field_flags:
        item = value(entry, field)
        if item:
            args.extend([flag, item])
    for page in list_value(entry, "affected_pages") or list_value(entry, "affected_page"):
        args.extend(["--affected-page", page])
    if dry_run:
        args.append("--dry-run")
    if allow_duplicate:
        args.append("--allow-duplicate")
    if no_audit:
        args.append("--no-audit")
    return args


def duplicate_ticket_ids(entries: list[dict]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for entry in entries:
        ticket_id = value(entry, "ticket_id", "task_id") or ""
        if not ticket_id:
            continue
        if ticket_id in seen:
            duplicates.add(ticket_id)
        seen.add(ticket_id)
    return sorted(duplicates)


def run_command(args: list[str]) -> dict:
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "command": " ".join([Path(args[0]).name, *args[1:]]),
        "returncode": proc.returncode,
        "output": proc.stdout.strip(),
        "passed": proc.returncode == 0,
    }


def preflight_entries(entries: list[dict], allow_duplicate: bool) -> list[dict]:
    if not allow_duplicate:
        duplicates = duplicate_ticket_ids(entries)
        if duplicates:
            return [
                {
                    "phase": "preflight",
                    "ticket_id": ticket_id,
                    "passed": False,
                    "returncode": 1,
                    "output": "duplicate ticket in packet; use --allow-duplicate only when intentional",
                    "command": "<duplicate check>",
                }
                for ticket_id in duplicates
            ]
    results: list[dict] = []
    for entry in entries:
        result = run_command(entry_command(entry, dry_run=True, allow_duplicate=allow_duplicate, no_audit=True))
        result["phase"] = "preflight"
        result["ticket_id"] = value(entry, "ticket_id", "task_id") or ""
        results.append(result)
    return results


def write_entries(entries: list[dict], allow_duplicate: bool) -> list[dict]:
    results: list[dict] = []
    for entry in entries:
        result = run_command(entry_command(entry, dry_run=False, allow_duplicate=allow_duplicate, no_audit=True))
        result["phase"] = "write"
        result["ticket_id"] = value(entry, "ticket_id", "task_id") or ""
        results.append(result)
        if not result["passed"]:
            break
    return results


def run_post_checks(skip_acceptance: bool) -> list[dict]:
    checks = []
    for script in POST_CHECKS:
        if skip_acceptance and script == "scripts/run_acceptance.py":
            continue
        result = run_command([sys.executable, script])
        result["phase"] = "post_check"
        result["script"] = script
        checks.append(result)
        if not result["passed"]:
            break
    return checks


def build_report(results: list[dict], entries: list[dict] | None = None, packet_path: str | None = None) -> dict:
    entries = entries or []
    checks = [
        {
            "name": "ticket registry available",
            "passed": TICKETS_JSON.exists(),
            "detail": rel(TICKETS_JSON) if TICKETS_JSON.exists() else "missing registry/source-refresh-tickets.json",
        },
        {
            "name": "packet supplied",
            "passed": packet_path is not None,
            "detail": packet_path or "no packet supplied; template mode only",
        },
    ]
    if packet_path is None:
        checks[1]["passed"] = True
    return {
        "generated": date.today().isoformat(),
        "passed": all(item.get("passed", False) for item in results) if results else all(check["passed"] for check in checks),
        "packet_path": packet_path,
        "entry_count": len(entries),
        "final_entry_count": sum(1 for entry in entries if value(entry, "status") in FINAL_STATUSES),
        "checks": checks,
        "results": results,
        "template": packet_template(),
    }


def markdown_report(report: dict) -> str:
    lines = [
        "# Source Evidence Packet Importer",
        "",
        f"Generated: {report['generated']}",
        "",
        "## Purpose",
        "",
        "Import human-reviewed source evidence packets into per-wiki source refresh logs. This importer validates the packet through `record_source_evidence.py` before writing and does not fetch or certify external facts by itself.",
        "",
        "## Summary",
        "",
        f"- Packet path: `{report['packet_path'] or 'none'}`",
        f"- Entries: {report['entry_count']}",
        f"- Final entries: {report['final_entry_count']}",
        f"- Passed: {'yes' if report['passed'] else 'no'}",
        "",
        "## Packet Format",
        "",
        "Use JSON, JSON object with `entries`, JSON list, or JSONL. Field names:",
        "",
    ]
    lines.extend(f"- `{field}`" for field in PACKET_FIELDS)
    lines.extend(
        [
            "",
            "Example packet:",
            "",
            "```json",
            json.dumps(report["template"], ensure_ascii=False, indent=2),
            "```",
            "",
            "## Import Flow",
            "",
            "- Preflight every entry with `record_source_evidence.py --dry-run`.",
            "- Reject duplicate ticket ids in the same packet unless `--allow-duplicate` is explicit.",
            "- Write entries only after the whole packet preflight passes.",
            "- Run completion audit, evidence quality audit, dashboard, wave runner, handoff, index update, and acceptance unless skipped.",
            "",
            "## Commands",
            "",
            "```bash",
            "python3 scripts/import_source_evidence_packet.py",
            "python3 scripts/import_source_evidence_packet.py --template --ticket-id TICKET-SRC-006",
            "python3 scripts/generate_source_evidence_packet_fixtures.py",
            "python3 scripts/import_source_evidence_packet.py --packet source-evidence.json --dry-run",
            "python3 scripts/import_source_evidence_packet.py --packet source-evidence.json",
            "```",
            "",
            "## Results",
            "",
        ]
    )
    if report["results"]:
        lines.extend(["| Phase | Ticket/Script | Result | Command |", "| --- | --- | --- | --- |"])
        for result in report["results"]:
            target = result.get("ticket_id") or result.get("script") or "-"
            outcome = "PASS" if result.get("passed") else "FAIL"
            command = result.get("command", "")
            lines.append(f"| {result.get('phase', '-')} | {target} | {outcome} | `{command}` |")
    else:
        lines.append("No packet imported yet. Generate a template, fill it from authoritative source checks, then run dry-run import.")

    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- Do not put API keys, private keys, cookies, bearer tokens, seed phrases, or private account data in packets.",
            "- Do not mark a ticket `verified` without dated authoritative evidence.",
            "- High-risk tickets require `human_reviewer` for final statuses.",
            "- Use `still-needs-source-update` when sources are unavailable, stale, conflicting, or outside the ticket scope.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_report(report: dict) -> None:
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(report), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = ArgumentParser(description="Import source evidence packets.")
    parser.add_argument("--packet", help="Path to a JSON or JSONL evidence packet.")
    parser.add_argument("--dry-run", action="store_true", help="Preflight packet without writing evidence logs.")
    parser.add_argument("--allow-duplicate", action="store_true", help="Allow duplicate tickets in packet and duplicate completed log entries.")
    parser.add_argument("--no-post-checks", action="store_true", help="Skip post-import audits and generated reports.")
    parser.add_argument("--no-acceptance", action="store_true", help="Run post-import checks but skip full acceptance.")
    parser.add_argument("--template", action="store_true", help="Print a packet template.")
    parser.add_argument("--ticket-id", default="TICKET-SRC-006", help="Ticket id to use for --template.")
    args = parser.parse_args()

    if args.template:
        report = build_report([])
        write_report(report)
        print(json.dumps(packet_template(args.ticket_id), ensure_ascii=False, indent=2))
        return 0

    if not args.packet:
        report = build_report([])
        write_report(report)
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
        print("SOURCE EVIDENCE PACKET IMPORTER READY (no packet supplied)")
        return 0 if report["passed"] else 1

    packet_path = Path(args.packet)
    if not packet_path.is_absolute():
        packet_path = ROOT / packet_path
    try:
        entries = load_packet(packet_path)
        results = preflight_entries(entries, args.allow_duplicate)
        if all(result["passed"] for result in results) and not args.dry_run:
            results.extend(write_entries(entries, args.allow_duplicate))
            if all(result["passed"] for result in results) and not args.no_post_checks:
                results.extend(run_post_checks(skip_acceptance=args.no_acceptance))
        report = build_report(results, entries=entries, packet_path=str(packet_path))
        write_report(report)
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
        if args.dry_run:
            print(f"SOURCE EVIDENCE PACKET DRY RUN ({len(entries)} entries)")
        else:
            print(f"SOURCE EVIDENCE PACKET IMPORT ({len(entries)} entries)")
        return 0 if report["passed"] else 1
    except Exception as exc:
        report = build_report(
            [
                {
                    "phase": "load",
                    "ticket_id": "",
                    "passed": False,
                    "returncode": 1,
                    "output": str(exc),
                    "command": f"load packet {args.packet}",
                }
            ],
            packet_path=args.packet,
        )
        write_report(report)
        print(f"import_source_evidence_packet failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
