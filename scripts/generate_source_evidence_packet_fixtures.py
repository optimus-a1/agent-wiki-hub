#!/usr/bin/env python3
"""Generate dry-run fixtures for source evidence packet imports."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
TICKETS_JSON = REGISTRY / "source-refresh-tickets.json"
FIXTURE_DIR = REGISTRY / "source-evidence-fixtures"
DOCS_OUT = ROOT / "docs" / "SOURCE_EVIDENCE_PACKET_FIXTURES.md"
JSON_OUT = REGISTRY / "source-evidence-packet-fixtures.json"


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def doc_link(repo_path: str, label: str | None = None) -> str:
    label = label or Path(repo_path).name
    return f"[{label}](../{repo_path})"


def ticket_records() -> list[dict]:
    return read_json(TICKETS_JSON).get("tickets", [])


def ticket_by_id() -> dict[str, dict]:
    records: dict[str, dict] = {}
    for ticket in ticket_records():
        if ticket.get("ticket_id"):
            records[ticket["ticket_id"]] = ticket
        if ticket.get("task_id"):
            records[ticket["task_id"]] = ticket
    return records


def pending_entry(ticket: dict) -> dict:
    return {"ticket_id": ticket.get("ticket_id", ""), "status": "pending"}


def final_fixture_entry(ticket: dict) -> dict:
    ticket_id = ticket.get("ticket_id", "")
    return {
        "ticket_id": ticket_id,
        "status": "still-needs-source-update",
        "source_title": f"Fixture source note for {ticket_id}",
        "source_publisher": "Fixture Pack",
        "source_url_or_reference": f"fixture-reference:{ticket_id}",
        "source_published_or_updated": "unknown",
        "source_accessed_on": date.today().isoformat(),
        "verified_on": date.today().isoformat(),
        "evidence_summary": "Fixture dry-run entry only; it does not certify any external current fact.",
        "affected_pages": [f"wikis/{ticket.get('wiki', '')}/sources/source-notes.md"],
        "confidence": "low",
        "remaining_uncertainty": "Fixture only; authoritative source verification is still needed.",
        "human_reviewer": "fixture-human-reviewer",
        "follow_up": "Replace fixture fields with real source evidence before import.",
    }


def packet(packet_id: str, entries: list[dict], description: str) -> dict:
    return {
        "packet_id": packet_id,
        "created_on": date.today().isoformat(),
        "created_by": "fixture-generator",
        "description": description,
        "dry_run_only": True,
        "entries": entries,
    }


def fixtures() -> list[dict]:
    tickets = ticket_records()
    by_id = ticket_by_id()
    finance = [ticket for ticket in tickets if ticket.get("wiki") == "finance-agent-wiki"]
    customs = [ticket for ticket in tickets if ticket.get("wiki") == "customs-agent-wiki"]
    t6 = by_id.get("TICKET-SRC-006") or finance[0]

    valid_final = final_fixture_entry(t6)
    missing_human = dict(valid_final)
    missing_human.pop("human_reviewer", None)

    placeholder = dict(valid_final)
    placeholder["source_title"] = "<source title>"
    placeholder["source_publisher"] = "<official publisher or authority>"
    placeholder["source_url_or_reference"] = "<URL or local reference>"

    secret_marker = dict(valid_final)
    secret_marker["source_title"] = "Fixture secret marker api_key=REDACTED"

    duplicate = [pending_entry(t6), pending_entry(t6)]

    return [
        {
            "name": "valid-pending-single.json",
            "kind": "valid",
            "expected_dry_run_pass": True,
            "description": "Minimal pending packet for one ticket; safe because it records no source facts.",
            "packet": packet("valid-pending-single", [pending_entry(t6)], "Minimal pending dry-run packet."),
        },
        {
            "name": "valid-still-needs-source-update-dry-run-only.json",
            "kind": "valid",
            "expected_dry_run_pass": True,
            "description": "Final-status shape for dry-run testing only; replace all fixture fields before real import.",
            "packet": packet("valid-still-needs-source-update-dry-run-only", [valid_final], "Dry-run-only final-status packet."),
        },
        {
            "name": "template-wave-1-p0-pending.json",
            "kind": "template",
            "expected_dry_run_pass": True,
            "description": "Pending packet template for wave-1 P0 finance tickets.",
            "packet": packet("template-wave-1-p0-pending", [pending_entry(ticket) for ticket in finance], "Wave-1 P0 pending template."),
        },
        {
            "name": "template-wave-2-customs-pending.json",
            "kind": "template",
            "expected_dry_run_pass": True,
            "description": "Pending packet template for customs source-refresh tickets.",
            "packet": packet("template-wave-2-customs-pending", [pending_entry(ticket) for ticket in customs], "Customs pending template."),
        },
        {
            "name": "invalid-duplicate-ticket.json",
            "kind": "invalid",
            "expected_dry_run_pass": False,
            "description": "Expected failure: duplicate ticket id in one packet.",
            "packet": packet("invalid-duplicate-ticket", duplicate, "Expected duplicate-ticket failure."),
        },
        {
            "name": "invalid-missing-human-reviewer.json",
            "kind": "invalid",
            "expected_dry_run_pass": False,
            "description": "Expected failure: high-risk final status without human_reviewer.",
            "packet": packet("invalid-missing-human-reviewer", [missing_human], "Expected missing-human-reviewer failure."),
        },
        {
            "name": "invalid-placeholder-source.json",
            "kind": "invalid",
            "expected_dry_run_pass": False,
            "description": "Expected failure: final status still contains placeholder source fields.",
            "packet": packet("invalid-placeholder-source", [placeholder], "Expected placeholder-source failure."),
        },
        {
            "name": "invalid-secret-marker.json",
            "kind": "invalid",
            "expected_dry_run_pass": False,
            "description": "Expected failure: fixture contains a redacted secret marker that must be rejected.",
            "packet": packet("invalid-secret-marker", [secret_marker], "Expected secret-marker failure."),
        },
    ]


def write_fixtures(records: list[dict]) -> None:
    FIXTURE_DIR.mkdir(parents=True, exist_ok=True)
    for record in records:
        path = FIXTURE_DIR / record["name"]
        path.write_text(json.dumps(record["packet"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_importer_fixture(path: Path, allow_duplicate_existing: bool) -> dict:
    args = [
        sys.executable,
        "scripts/import_source_evidence_packet.py",
        "--packet",
        rel(path),
        "--dry-run",
        "--no-post-checks",
    ]
    if allow_duplicate_existing:
        args.append("--allow-duplicate")
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
        "actual_pass": proc.returncode == 0,
    }


def restore_importer_report() -> None:
    subprocess.run(
        [sys.executable, "scripts/import_source_evidence_packet.py"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def validate_fixtures(records: list[dict]) -> list[dict]:
    validations: list[dict] = []
    try:
        for record in records:
            path = FIXTURE_DIR / record["name"]
            # Existing completed evidence is normal in post-import repositories. Keep the
            # duplicate-ticket fixture strict, but let all other fixtures test their
            # intended validation path instead of failing on prior evidence.
            allow_duplicate_existing = record["name"] != "invalid-duplicate-ticket.json"
            result = run_importer_fixture(path, allow_duplicate_existing)
            expected = bool(record["expected_dry_run_pass"])
            validations.append(
                {
                    "fixture": record["name"],
                    "allow_duplicate_existing": allow_duplicate_existing,
                    "expected_pass": expected,
                    "actual_pass": result["actual_pass"],
                    "passed": result["actual_pass"] == expected,
                    "returncode": result["returncode"],
                    "command": result["command"],
                    "output": result["output"],
                }
            )
    finally:
        restore_importer_report()
    return validations


def build_report(records: list[dict], validations: list[dict]) -> dict:
    checks = [
        {
            "name": "ticket registry available",
            "passed": TICKETS_JSON.exists(),
            "detail": rel(TICKETS_JSON) if TICKETS_JSON.exists() else "missing source-refresh-tickets.json",
        },
        {
            "name": "fixtures generated",
            "passed": all((FIXTURE_DIR / record["name"]).exists() for record in records),
            "detail": f"{len(records)} fixtures",
        },
    ]
    checks.extend(
        {
            "name": f"dry-run expectation: {item['fixture']}",
            "passed": item["passed"],
            "detail": f"expected={item['expected_pass']} actual={item['actual_pass']}",
        }
        for item in validations
    )
    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "fixture_dir": rel(FIXTURE_DIR),
        "fixture_count": len(records),
        "valid_fixture_count": sum(1 for record in records if record["kind"] in {"valid", "template"}),
        "invalid_fixture_count": sum(1 for record in records if record["kind"] == "invalid"),
        "fixtures": [
            {
                "name": record["name"],
                "path": rel(FIXTURE_DIR / record["name"]),
                "kind": record["kind"],
                "expected_dry_run_pass": record["expected_dry_run_pass"],
                "description": record["description"],
                "ticket_ids": [entry.get("ticket_id", "") for entry in record["packet"].get("entries", [])],
            }
            for record in records
        ],
        "validations": validations,
        "checks": checks,
    }


def markdown_report(report: dict) -> str:
    lines = [
        "# Source Evidence Packet Fixtures",
        "",
        f"Generated: {report['generated']}",
        "",
        "## Purpose",
        "",
        "These fixtures exercise the source evidence packet importer without verifying or certifying external facts. Use them with `--dry-run`; fill real source evidence before any actual import.",
        "",
        "## Summary",
        "",
        f"- Fixture directory: `{report['fixture_dir']}`",
        f"- Fixtures: {report['fixture_count']}",
        f"- Valid/template fixtures: {report['valid_fixture_count']}",
        f"- Invalid fixtures: {report['invalid_fixture_count']}",
        f"- Passed: {'yes' if report['passed'] else 'no'}",
        "",
        "## Fixtures",
        "",
        "| Fixture | Kind | Expected Dry Run | Ticket IDs | Description |",
        "| --- | --- | --- | --- | --- |",
    ]
    for fixture in report["fixtures"]:
        expected = "pass" if fixture["expected_dry_run_pass"] else "fail"
        tickets = ", ".join(fixture["ticket_ids"]) or "-"
        lines.append(
            f"| {doc_link(fixture['path'], fixture['name'])} | {fixture['kind']} | {expected} | {tickets} | {fixture['description']} |"
        )

    lines.extend(["", "## Dry-Run Validation", "", "| Fixture | Expected | Actual | Result |", "| --- | --- | --- | --- |"])
    for item in report["validations"]:
        expected = "pass" if item["expected_pass"] else "fail"
        actual = "pass" if item["actual_pass"] else "fail"
        result = "PASS" if item["passed"] else "FAIL"
        lines.append(f"| `{item['fixture']}` | {expected} | {actual} | {result} |")

    lines.extend(
        [
            "",
            "## Commands",
            "",
            "```bash",
            "python3 scripts/generate_source_evidence_packet_fixtures.py",
            "python3 scripts/import_source_evidence_packet.py --packet registry/source-evidence-fixtures/valid-pending-single.json --dry-run --no-post-checks",
            "python3 scripts/import_source_evidence_packet.py --packet registry/source-evidence-fixtures/invalid-secret-marker.json --dry-run --no-post-checks",
            "```",
            "",
            "## Safety Boundary",
            "",
            "- Fixtures are for importer tests and packet authoring only.",
            "- Do not import dry-run-only fixtures as evidence for current facts.",
            "- Invalid fixtures intentionally contain placeholders or redacted secret markers to test rejection paths.",
            "- No fixture contains real credentials, private keys, cookies, or verified current facts.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    records = fixtures()
    write_fixtures(records)
    validations = validate_fixtures(records)
    report = build_report(records, validations)
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    DOCS_OUT.write_text(markdown_report(report), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"Wrote {report['fixture_count']} fixtures to {report['fixture_dir']}")
    if not report["passed"]:
        print("SOURCE EVIDENCE PACKET FIXTURES FAILED")
        return 1
    print("SOURCE EVIDENCE PACKET FIXTURES GENERATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
