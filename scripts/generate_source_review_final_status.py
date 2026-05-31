#!/usr/bin/env python3
"""Generate final source-review follow-up status for planning waves."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"

DOCS_OUT = DOCS / "SOURCE_REVIEW_FINAL_STATUS.md"
JSON_OUT = REGISTRY / "source-review-final-status.json"


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


def report_status(path: str, count_key: str | None = None) -> dict:
    data = read_json(ROOT / path)
    record = {
        "path": path,
        "exists": bool(data),
        "passed": data.get("passed") if data else None,
    }
    if count_key and data:
        record[count_key] = data.get(count_key)
    return record


def unique_ticket_count(records: list[dict], wave: str) -> int:
    tickets = {ticket.get("ticket_id") for ticket in records if ticket.get("wave") == wave and ticket.get("ticket_id")}
    return len(tickets)


def build_status() -> dict:
    dashboard = read_json(REGISTRY / "source-refresh-dashboard.json")
    classification = read_json(REGISTRY / "source-review-packet-classification.json")
    wave2 = read_json(REGISTRY / "source-review-wave-2-plan.json")
    wave3 = read_json(REGISTRY / "source-review-wave-3-plan.json")
    wave2_batches = read_json(REGISTRY / "source-review-wave-2-batch-plan.json")
    wave2_packet = read_json(REGISTRY / "source-review-packets" / "source-review-session-wave-2-pending-manifest.json")
    wave3_packet = read_json(REGISTRY / "source-review-packets" / "source-review-session-wave-3-pending-manifest.json")
    acceptance = read_json(REGISTRY / "acceptance-report.json")
    release = read_json(REGISTRY / "release-manifest.json")

    completion = dashboard.get("source_refresh", {}).get("completion", {})
    tickets = completion.get("tickets", [])
    wave_counts = Counter(ticket.get("wave", "") for ticket in tickets if ticket.get("wave"))
    active_packets = [
        record for record in classification.get("records", []) if record.get("classification") == "active-import-packet"
    ]
    planning_packets = [
        record for record in classification.get("records", []) if record.get("classification") == "planning-only-pending-packet"
    ]
    advisory_packets = [
        record for record in classification.get("records", []) if record.get("classification") == "advisory-prefill-artifact"
    ]

    waves = [
        {
            "wave": "wave-1",
            "ticket_count": wave_counts.get("wave-1", 0),
            "status": "active packet retained; evidence quality audits pass, but tickets remain open for current-fact readiness",
            "packet_role": "active-import-packet",
            "planning_only": False,
            "human_gate_count": release.get("source_review_session_human_gate_count", 13),
            "verified_ticket_count": completion.get("verified_ticket_count", 0),
            "current_fact_write": False,
            "artifacts": [record.get("path") for record in active_packets],
        },
        {
            "wave": "wave-2",
            "ticket_count": wave2.get("selected_review_count", unique_ticket_count(tickets, "wave-2")),
            "status": "planning and pending packet generated; evidence collection not performed",
            "packet_role": "planning-only-pending-packet",
            "planning_only": True,
            "human_gate_count": wave2.get("selected_human_review_gate_count", 0),
            "verified_ticket_count": 0,
            "current_fact_write": False,
            "artifacts": [
                "docs/SOURCE_REVIEW_WAVE_2_PLAN.md",
                "docs/SOURCE_REVIEW_WAVE_2_BATCH_PLAN.md",
                "docs/SOURCE_REVIEW_WAVE_2_PACKET_BUNDLE.md",
                "docs/SOURCE_REVIEW_WAVE_2_WORK_ORDERS.md",
                "docs/SOURCE_REVIEW_WAVE_2_SESSION_PLAN.md",
                "registry/source-review-wave-2-plan.json",
                "registry/source-review-wave-2-batch-plan.json",
                "registry/source-review-packets/source-review-session-wave-2-pending.json",
                "registry/source-review-work-orders-wave-2/manifest.json",
            ],
            "batch_count": wave2_batches.get("batch_count", 0),
            "packet_entry_count": wave2_packet.get("entry_count", 0),
        },
        {
            "wave": "wave-3",
            "ticket_count": wave3.get("selected_review_count", unique_ticket_count(tickets, "wave-3")),
            "status": "planning and pending packet generated; evidence collection not performed",
            "packet_role": "planning-only-pending-packet",
            "planning_only": True,
            "human_gate_count": wave3.get("selected_human_review_gate_count", 0),
            "verified_ticket_count": 0,
            "current_fact_write": False,
            "artifacts": [
                "docs/SOURCE_REVIEW_WAVE_3_PLAN.md",
                "docs/SOURCE_REVIEW_WAVE_3_PACKET_BUNDLE.md",
                "docs/SOURCE_REVIEW_WAVE_3_WORK_ORDERS.md",
                "docs/SOURCE_REVIEW_WAVE_3_SESSION_PLAN.md",
                "registry/source-review-wave-3-plan.json",
                "registry/source-review-packets/source-review-session-wave-3-pending.json",
                "registry/source-review-work-orders-wave-3/manifest.json",
            ],
            "packet_entry_count": wave3_packet.get("entry_count", 0),
        },
    ]

    report_checks = [
        report_status("registry/acceptance-report.json"),
        report_status("registry/link-audit.json"),
        report_status("registry/source-review-packet-audit.json", "entry_count"),
        report_status("registry/source-review-packet-rehearsal.json", "packet_count"),
        report_status("registry/source-evidence-quality-audit.json", "entry_count"),
        report_status("registry/source-refresh-completion-audit.json", "ticket_count"),
        report_status("registry/pack-audit.json"),
    ]

    checks = [
        {
            "check": "acceptance passed",
            "passed": bool(acceptance.get("passed")),
            "detail": "registry/acceptance-report.json",
        },
        {
            "check": "current facts remain gated",
            "passed": not bool(dashboard.get("current_fact_ready")),
            "detail": "current_fact_ready=false",
        },
        {
            "check": "no tickets marked verified for current facts",
            "passed": int(completion.get("verified_ticket_count", 0) or 0) == 0,
            "detail": f"{completion.get('verified_ticket_count', 0)} verified tickets",
        },
        {
            "check": "planning packets are non-blocking",
            "passed": all(record.get("acceptance_role") == "non-blocking" for record in planning_packets),
            "detail": f"{len(planning_packets)} planning-only packet files",
        },
    ]

    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "current_fact_ready": bool(dashboard.get("current_fact_ready")),
        "current_facts_written_by_this_run": False,
        "network_verification_performed": False,
        "wave_2_evidence_collection": "wave-2 evidence collection not performed because no connected source verification is available.",
        "wave_3_evidence_collection": "wave-3 evidence collection not performed because no connected source verification is available.",
        "open_topic_count": completion.get("open_ticket_count", 0),
        "verified_ticket_count": completion.get("verified_ticket_count", 0),
        "finalized_ticket_count": completion.get("finalized_ticket_count", 0),
        "wave_counts": dict(sorted(wave_counts.items())),
        "waves": waves,
        "packet_classification": {
            "path": "registry/source-review-packet-classification.json",
            "passed": classification.get("passed"),
            "classification_counts": classification.get("classification_counts", {}),
            "active_packets": active_packets,
            "planning_only_packets": planning_packets,
            "advisory_packets": advisory_packets,
        },
        "human_gates": {
            "wave-1": waves[0]["human_gate_count"],
            "wave-2": waves[1]["human_gate_count"],
            "wave-3": waves[2]["human_gate_count"],
            "total_planned": sum(wave["human_gate_count"] for wave in waves),
        },
        "report_checks": report_checks,
        "checks": checks,
        "next_steps": [
            "Assign named human reviewers for wave-2 high-risk NodeOps tickets before any final status.",
            "Collect authoritative, primary, dated evidence per ticket into packet entries or source-refresh logs.",
            "Dry-run imports, run packet audit, rehearsal, evidence quality, completion audit, and acceptance before importing evidence.",
            "Keep current facts out of stable wiki pages until evidence, quality audits, acceptance, and human gates all pass.",
        ],
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Final Status",
        "",
        f"Generated: {data['generated']}",
        "",
        "## Summary",
        "",
        f"- Passed: {bool_word(data['passed'])}",
        f"- Acceptance passed: {bool_word(next(check['passed'] for check in data['checks'] if check['check'] == 'acceptance passed'))}",
        f"- Open source update topics: {data['open_topic_count']}",
        f"- Verified tickets for current facts: {data['verified_ticket_count']}",
        f"- Finalized tickets: {data['finalized_ticket_count']}",
        f"- Current-fact ready: {bool_word(data['current_fact_ready'])}",
        f"- Current facts written by this run: {bool_word(data['current_facts_written_by_this_run'])}",
        f"- Network/source verification performed: {bool_word(data['network_verification_performed'])}",
        "",
        "## Evidence Collection",
        "",
        f"- {data['wave_2_evidence_collection']}",
        f"- {data['wave_3_evidence_collection']}",
        "- No packet placeholder was imported as verified evidence.",
        "- No source title, publisher, URL, publication date, or verified_on value was fabricated.",
        "",
        "## Wave Status",
        "",
        "| Wave | Tickets | Status | Packet Role | Human Gates | Current Facts Written |",
        "| --- | ---: | --- | --- | ---: | --- |",
    ]
    for wave in data["waves"]:
        lines.append(
            f"| {wave['wave']} | {wave['ticket_count']} | {wave['status']} | "
            f"{wave['packet_role']} | {wave['human_gate_count']} | {bool_word(wave['current_fact_write'])} |"
        )

    lines.extend(["", "## Packet Classification", ""])
    counts = data["packet_classification"]["classification_counts"]
    lines.extend(
        [
            f"- Classification report: {repo_link(data['packet_classification']['path'])}",
            f"- Active import packet files: {counts.get('active-import-packet', 0)}",
            f"- Planning-only pending packet files: {counts.get('planning-only-pending-packet', 0)}",
            f"- Advisory prefill artifacts: {counts.get('advisory-prefill-artifact', 0)}",
            "",
            "### Active Import Packets",
            "",
        ]
    )
    for record in data["packet_classification"]["active_packets"]:
        lines.append(f"- {repo_link(record['path'])}: {record['entry_count']} entries")
    lines.extend(["", "### Planning-Only Packets", ""])
    for record in data["packet_classification"]["planning_only_packets"]:
        lines.append(f"- {repo_link(record['path'])}: {record['entry_count']} entries, non-blocking")

    lines.extend(["", "## Deliverables", ""])
    for wave in data["waves"]:
        lines.extend([f"### {wave['wave']}", ""])
        for artifact in wave["artifacts"]:
            lines.append(f"- {repo_link(artifact)}")
        lines.append("")

    lines.extend(["## Latest Report Checks", "", "| Report | Exists | Passed | Count |", "| --- | --- | --- | --- |"])
    for report in data["report_checks"]:
        count = "-"
        for key in ("entry_count", "packet_count", "ticket_count"):
            if key in report:
                count = f"{key}={report[key]}"
        lines.append(
            f"| {repo_link(report['path'])} | {bool_word(report['exists'])} | "
            f"{bool_word(bool(report['passed'])) if report['passed'] is not None else '-'} | {count} |"
        )

    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        lines.append(f"| {check['check']} | {'PASS' if check['passed'] else 'FAIL'} | {check['detail']} |")

    lines.extend(["", "## Human Gates", ""])
    for wave, count in data["human_gates"].items():
        lines.append(f"- {wave}: {count}")

    lines.extend(["", "## Next Steps", ""])
    lines.extend(f"- {item}" for item in data["next_steps"])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    data = build_status()
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {rel(DOCS_OUT)}")
    print(f"Wrote {rel(JSON_OUT)}")
    print(
        "SOURCE REVIEW FINAL STATUS "
        f"{'PASSED' if data['passed'] else 'FAILED'} "
        f"({data['open_topic_count']} open topics, {data['verified_ticket_count']} verified tickets)"
    )
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
