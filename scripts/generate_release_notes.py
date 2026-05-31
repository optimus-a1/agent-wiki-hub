#!/usr/bin/env python3
"""Generate release notes and a machine-readable release manifest."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DOCS_OUT = ROOT / "docs" / "RELEASE_NOTES.md"
JSON_OUT = ROOT / "registry" / "release-manifest.json"
PACKS = ROOT / "packs"
REGISTRY = ROOT / "registry"

REPORTS = {
    "acceptance": REGISTRY / "acceptance-report.json",
    "ci": REGISTRY / "ci-audit.json",
    "registry": REGISTRY / "registry-consistency.json",
    "metadata": REGISTRY / "page-metadata-audit.json",
    "coverage": REGISTRY / "coverage-audit.json",
    "links": REGISTRY / "link-audit.json",
    "packs": REGISTRY / "pack-audit.json",
    "safety": REGISTRY / "safety-audit.json",
    "source_refresh_logs": REGISTRY / "source-refresh-log-status.json",
    "routing_cards": REGISTRY / "agent-routing-cards.json",
    "source_refresh_tickets": REGISTRY / "source-refresh-tickets.json",
    "source_refresh_wave_runner": REGISTRY / "source-refresh-wave-runner.json",
    "source_reviewer_queue": REGISTRY / "source-reviewer-queue.json",
    "source_review_session_plan": REGISTRY / "source-review-session-plan.json",
    "source_review_readiness_matrix": REGISTRY / "source-review-readiness-matrix.json",
    "source_review_work_orders": REGISTRY / "source-review-work-orders.json",
    "source_review_packet_bundle": REGISTRY / "source-review-packet-bundle.json",
    "source_review_packet_audit": REGISTRY / "source-review-packet-audit.json",
    "source_review_packet_rehearsal": REGISTRY / "source-review-packet-rehearsal.json",
    "source_evidence_packet_importer": REGISTRY / "source-evidence-packet-importer.json",
    "source_evidence_packet_fixtures": REGISTRY / "source-evidence-packet-fixtures.json",
    "source_refresh_completion": REGISTRY / "source-refresh-completion-audit.json",
    "source_evidence_quality": REGISTRY / "source-evidence-quality-audit.json",
    "source_refresh_dashboard": REGISTRY / "source-refresh-dashboard.json",
    "agent_handoff": REGISTRY / "agent-handoff.json",
}

ADVISORY_AUDITS = {"acceptance"}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_records() -> list[dict]:
    records: list[dict] = []
    if not PACKS.exists():
        return records
    for path in sorted(PACKS.glob("*.zip")):
        if path.name == "agent-wiki-hub-all.zip":
            records.append(
                {
                    "name": path.name,
                    "path": path.relative_to(ROOT).as_posix(),
                    "size_bytes": None,
                    "sha256": None,
                    "note": "Self-referential package; compute final size and checksum after packing release-manifest.json.",
                }
            )
            continue
        records.append(
            {
                "name": path.name,
                "path": path.relative_to(ROOT).as_posix(),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return records


def audit_summary(name: str, data: dict) -> dict:
    checks = data.get("checks", [])
    steps = data.get("steps", [])
    gates = data.get("gates", [])
    total = len(checks) or len(steps) or len(gates)
    if checks:
        passed = sum(1 for item in checks if item.get("passed"))
    elif steps:
        passed = sum(1 for item in steps if item.get("passed"))
    elif gates:
        passed = sum(1 for item in gates if item.get("passed"))
    elif data.get("logs"):
        total = len(data.get("logs", []))
        passed = sum(1 for item in data.get("logs", []) if item.get("passed"))
    elif data.get("tickets"):
        total = len(data.get("tickets", []))
        if any("passed" in item for item in data.get("tickets", [])):
            passed = sum(1 for item in data.get("tickets", []) if item.get("passed"))
        else:
            passed = total if data.get("passed") else 0
    elif data.get("entries"):
        total = len(data.get("entries", []))
        if any("passed" in item for item in data.get("entries", [])):
            passed = sum(1 for item in data.get("entries", []) if item.get("passed"))
        else:
            passed = total if data.get("passed") else 0
    elif data.get("ticket_count"):
        total = int(data.get("ticket_count", 0))
        passed = total if data.get("passed") else 0
    else:
        passed = total if data.get("passed") else 0
    return {
        "name": name,
        "passed": bool(data.get("passed", total == passed)),
        "total": total,
        "passed_count": passed,
        "failed_count": max(total - passed, 0),
    }


def build_manifest() -> dict:
    wiki_status = read_json(REGISTRY / "wiki-status.json")
    source_queue = read_json(REGISTRY / "source-update-queue.json")
    source_playbook = read_json(REGISTRY / "source-refresh-playbook.json")
    source_tickets = read_json(REGISTRY / "source-refresh-tickets.json")
    source_wave_runner = read_json(REGISTRY / "source-refresh-wave-runner.json")
    source_reviewer_queue = read_json(REGISTRY / "source-reviewer-queue.json")
    source_review_session_plan = read_json(REGISTRY / "source-review-session-plan.json")
    source_review_readiness_matrix = read_json(REGISTRY / "source-review-readiness-matrix.json")
    source_review_work_orders = read_json(REGISTRY / "source-review-work-orders.json")
    source_review_packet_bundle = read_json(REGISTRY / "source-review-packet-bundle.json")
    source_review_packet_audit = read_json(REGISTRY / "source-review-packet-audit.json")
    source_review_packet_rehearsal = read_json(REGISTRY / "source-review-packet-rehearsal.json")
    source_packet_importer = read_json(REGISTRY / "source-evidence-packet-importer.json")
    source_packet_fixtures = read_json(REGISTRY / "source-evidence-packet-fixtures.json")
    source_completion = read_json(REGISTRY / "source-refresh-completion-audit.json")
    source_evidence_quality = read_json(REGISTRY / "source-evidence-quality-audit.json")
    source_dashboard = read_json(REGISTRY / "source-refresh-dashboard.json")
    source_log_status = read_json(REGISTRY / "source-refresh-log-status.json")
    change_summary = read_json(REGISTRY / "change-summary.json")
    hub_navigation = read_json(REGISTRY / "hub-navigation.json")
    routing_cards = read_json(REGISTRY / "agent-routing-cards.json")
    agent_handoff = read_json(REGISTRY / "agent-handoff.json")
    reports = {name: read_json(path) for name, path in REPORTS.items()}
    packages = package_records()

    wikis = wiki_status.get("wikis", [])
    topics = source_queue.get("topics", [])
    risk_counts = Counter(wiki.get("risk_level", "unknown") for wiki in wikis)
    freshness_counts = Counter(wiki.get("freshness_requirement", "unknown") for wiki in wikis)
    topic_priority_counts = Counter(str(topic.get("priority_score", "unknown")) for topic in topics)

    audit_summaries = [audit_summary(name, data) for name, data in reports.items() if data]
    blocking_audits = [item for item in audit_summaries if item["name"] not in ADVISORY_AUDITS]
    advisory_audits = [item for item in audit_summaries if item["name"] in ADVISORY_AUDITS]
    all_blocking_audits_passed = all(item["passed"] for item in blocking_audits) if blocking_audits else False
    release_warnings = [
        f"{item['name']} is not passing yet; this is advisory while release notes are generated inside acceptance."
        for item in advisory_audits
        if not item["passed"]
    ]

    return {
        "generated": date.today().isoformat(),
        "release_name": "Agent Wiki Hub Knowledge Pack Release",
        "ready_for_internal_release": all_blocking_audits_passed and bool(packages),
        "blocking_audits_passed": all_blocking_audits_passed,
        "advisory_audit_count": len(advisory_audits),
        "release_warning_count": len(release_warnings),
        "release_warnings": release_warnings,
        "requires_source_update_for_current_facts": bool(topics),
        "wiki_count": len(wikis),
        "risk_counts": dict(sorted(risk_counts.items())),
        "freshness_counts": dict(sorted(freshness_counts.items())),
        "total_eval_tests": sum(int(wiki.get("eval_tests", 0)) for wiki in wikis),
        "source_update_topic_count": len(topics),
        "source_refresh_task_count": int(source_playbook.get("task_count", 0)),
        "source_refresh_ticket_count": int(source_tickets.get("ticket_count", 0)),
        "source_refresh_wave_runner_available": bool(source_wave_runner.get("recommended_queue")),
        "source_reviewer_queue_available": bool(source_reviewer_queue.get("review_cards")),
        "source_reviewer_queue_human_gate_count": int(source_reviewer_queue.get("human_review_gate_count", 0)),
        "source_review_session_plan_available": bool(source_review_session_plan.get("selected_reviews")),
        "source_review_session_selected_count": int(source_review_session_plan.get("selected_review_count", 0)),
        "source_review_session_human_gate_count": int(source_review_session_plan.get("selected_human_review_gate_count", 0)),
        "source_review_readiness_matrix_available": bool(source_review_readiness_matrix.get("rows")),
        "source_review_readiness_ready_count": int(source_review_readiness_matrix.get("ready_for_source_collection_count", 0)),
        "source_review_readiness_queued_count": int(source_review_readiness_matrix.get("queued_not_in_current_session_count", 0)),
        "source_review_work_orders_available": bool(source_review_work_orders.get("passed")),
        "source_review_work_order_count": int(source_review_work_orders.get("work_order_count", 0)),
        "source_review_work_order_human_gate_count": int(source_review_work_orders.get("human_review_gate_count", 0)),
        "source_review_post_import_completed": bool(
            source_review_work_orders.get("post_import_completed")
            or source_review_readiness_matrix.get("post_import_completed")
        ),
        "source_review_packet_bundle_available": bool(source_review_packet_bundle.get("packet_json")),
        "source_review_packet_bundle_entry_count": int(source_review_packet_bundle.get("selected_review_count", 0)),
        "source_review_packet_bundle_human_gate_count": int(source_review_packet_bundle.get("selected_human_review_gate_count", 0)),
        "source_review_packet_audit_passed": bool(source_review_packet_audit.get("passed", False)),
        "source_review_packet_audit_packet_count": int(source_review_packet_audit.get("packet_count", 0)),
        "source_review_packet_audit_issue_count": int(source_review_packet_audit.get("issue_count", 0)),
        "source_review_packet_rehearsal_passed": bool(source_review_packet_rehearsal.get("passed", False)),
        "source_review_packet_rehearsal_dry_run_count": int(source_review_packet_rehearsal.get("dry_run_count", 0)),
        "source_review_packet_rehearsal_passed_count": int(source_review_packet_rehearsal.get("passed_dry_run_count", 0)),
        "source_evidence_packet_importer_available": bool(source_packet_importer.get("template")),
        "source_evidence_packet_fixture_count": int(source_packet_fixtures.get("fixture_count", 0)),
        "source_refresh_open_ticket_count": int(source_completion.get("open_ticket_count", 0)),
        "source_refresh_verified_ticket_count": int(source_completion.get("verified_ticket_count", 0)),
        "source_refresh_completion_ready": bool(source_completion.get("completion_ready_for_current_fact_use")),
        "source_evidence_entry_count": int(source_evidence_quality.get("entry_count", 0)),
        "source_evidence_quality_issue_count": int(source_evidence_quality.get("issue_count", 0)),
        "source_evidence_quality_passed": bool(source_evidence_quality.get("passed", True)),
        "source_refresh_dashboard_available": bool(source_dashboard.get("source_refresh")),
        "source_refresh_wave_counts": source_playbook.get("wave_counts", {}),
        "source_refresh_log_count": int(source_log_status.get("wiki_count", 0)),
        "change_summary_available": bool(change_summary.get("current")),
        "hub_navigation_available": bool(hub_navigation.get("wikis")),
        "agent_routing_cards_available": bool(routing_cards.get("cards")),
        "agent_handoff_available": bool(agent_handoff.get("first_reads")),
        "source_evidence_recorder_available": (ROOT / "scripts" / "record_source_evidence.py").exists(),
        "source_update_priority_counts": dict(sorted(topic_priority_counts.items())),
        "top_source_update_topics": topics[:10],
        "audits": audit_summaries,
        "packages": packages,
    }


def fmt_size(size: int) -> str:
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"
    if size >= 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size} B"


def markdown_report(manifest: dict) -> str:
    ready = "yes" if manifest["ready_for_internal_release"] else "no"
    needs_sources = "yes" if manifest["requires_source_update_for_current_facts"] else "no"
    lines = [
        "# Agent Wiki Hub Release Notes",
        "",
        f"Generated: {manifest['generated']}",
        "",
        "## Summary",
        "",
        f"- Release readiness for internal use: {ready}",
        f"- Blocking audits passed: {'yes' if manifest['blocking_audits_passed'] else 'no'}",
        f"- Release warnings: {manifest['release_warning_count']}",
        f"- Requires source updates before current-fact use: {needs_sources}",
        f"- Wikis: {manifest['wiki_count']}",
        f"- Eval tests: {manifest['total_eval_tests']}",
        f"- Source-update topics: {manifest['source_update_topic_count']}",
        f"- Source-refresh tasks: {manifest['source_refresh_task_count']}",
        f"- Source-refresh tickets: {manifest['source_refresh_ticket_count']}",
        f"- Source-refresh wave runner available: {'yes' if manifest['source_refresh_wave_runner_available'] else 'no'}",
        f"- Source reviewer queue available: {'yes' if manifest['source_reviewer_queue_available'] else 'no'}",
        f"- Source reviewer human gates: {manifest['source_reviewer_queue_human_gate_count']}",
        f"- Source review session plan available: {'yes' if manifest['source_review_session_plan_available'] else 'no'}",
        f"- Source review session selected reviews: {manifest['source_review_session_selected_count']}",
        f"- Source review session human gates: {manifest['source_review_session_human_gate_count']}",
        f"- Source review readiness matrix available: {'yes' if manifest['source_review_readiness_matrix_available'] else 'no'}",
        f"- Source review ready for collection: {manifest['source_review_readiness_ready_count']}",
        f"- Source review queued outside session: {manifest['source_review_readiness_queued_count']}",
        f"- Source review work orders available: {'yes' if manifest['source_review_work_orders_available'] else 'no'}",
        f"- Source review work orders: {manifest['source_review_work_order_count']}",
        f"- Source review work order human gates: {manifest['source_review_work_order_human_gate_count']}",
        f"- Source review post-import completed: {'yes' if manifest['source_review_post_import_completed'] else 'no'}",
        f"- Source review packet bundle available: {'yes' if manifest['source_review_packet_bundle_available'] else 'no'}",
        f"- Source review packet entries: {manifest['source_review_packet_bundle_entry_count']}",
        f"- Source review packet human gates: {manifest['source_review_packet_bundle_human_gate_count']}",
        f"- Source review packet audit passed: {'yes' if manifest['source_review_packet_audit_passed'] else 'no'}",
        f"- Source review packet audit packets: {manifest['source_review_packet_audit_packet_count']}",
        f"- Source review packet audit issues: {manifest['source_review_packet_audit_issue_count']}",
        f"- Source review packet rehearsal passed: {'yes' if manifest['source_review_packet_rehearsal_passed'] else 'no'}",
        f"- Source review packet rehearsal dry-runs: {manifest['source_review_packet_rehearsal_passed_count']}/{manifest['source_review_packet_rehearsal_dry_run_count']}",
        f"- Source evidence packet importer available: {'yes' if manifest['source_evidence_packet_importer_available'] else 'no'}",
        f"- Source evidence packet fixtures: {manifest['source_evidence_packet_fixture_count']}",
        f"- Source-refresh open tickets: {manifest['source_refresh_open_ticket_count']}",
        f"- Source-refresh verified tickets: {manifest['source_refresh_verified_ticket_count']}",
        f"- Source-refresh completion ready: {'yes' if manifest['source_refresh_completion_ready'] else 'no'}",
        f"- Source evidence entries: {manifest['source_evidence_entry_count']}",
        f"- Source evidence quality issues: {manifest['source_evidence_quality_issue_count']}",
        f"- Source evidence quality passed: {'yes' if manifest['source_evidence_quality_passed'] else 'no'}",
        f"- Source refresh dashboard available: {'yes' if manifest['source_refresh_dashboard_available'] else 'no'}",
        f"- Source-refresh logs: {manifest['source_refresh_log_count']}",
        f"- Change summary available: {'yes' if manifest['change_summary_available'] else 'no'}",
        f"- Hub navigation available: {'yes' if manifest['hub_navigation_available'] else 'no'}",
        f"- Agent routing cards available: {'yes' if manifest['agent_routing_cards_available'] else 'no'}",
        f"- Agent handoff available: {'yes' if manifest['agent_handoff_available'] else 'no'}",
        f"- Source evidence recorder available: {'yes' if manifest['source_evidence_recorder_available'] else 'no'}",
        f"- Packages: {len(manifest['packages'])}",
        "",
        "## Acceptance Gates",
        "",
        "| Gate | Result | Passed | Total |",
        "| --- | --- | ---: | ---: |",
    ]
    for audit in manifest["audits"]:
        result = "PASS" if audit["passed"] else "FAIL"
        lines.append(f"| {audit['name']} | {result} | {audit['passed_count']} | {audit['total']} |")

    lines.extend(["", "## Release Warnings", ""])
    if manifest["release_warnings"]:
        lines.extend(f"- {warning}" for warning in manifest["release_warnings"])
    else:
        lines.append("No release warnings.")

    lines.extend(["", "## Packages", "", "| Package | Size | SHA-256 |", "| --- | ---: | --- |"])
    for package in manifest["packages"]:
        if package.get("sha256"):
            size = fmt_size(package["size_bytes"])
            checksum = f"`{package['sha256'][:16]}...`"
        else:
            size = "external final artifact"
            checksum = package.get("note", "compute after final packaging")
        lines.append(f"| `{package['path']}` | {size} | {checksum} |")

    lines.extend(["", "## Wiki Coverage", "", "### Risk Levels", ""])
    for risk, count in manifest["risk_counts"].items():
        lines.append(f"- {risk}: {count}")
    lines.extend(["", "### Freshness Requirements", ""])
    for freshness, count in manifest["freshness_counts"].items():
        lines.append(f"- {freshness}: {count}")

    lines.extend(["", "## Source Update Queue", ""])
    lines.append(f"Source refresh playbook tasks: {manifest['source_refresh_task_count']}")
    lines.append("")
    if manifest["top_source_update_topics"]:
        lines.extend(["| Wiki | Priority | Topic |", "| --- | ---: | --- |"])
        for topic in manifest["top_source_update_topics"]:
            lines.append(f"| {topic.get('wiki')} | {topic.get('priority_score')} | {topic.get('topic')} |")
    else:
        lines.append("No source-update topics are currently queued.")

    lines.extend(
        [
            "",
            "## Safety Notes",
            "",
            "- This release contains stable concepts, reusable workflows, prompts, evals, and safety boundaries.",
            "- It does not certify current prices, policies, laws, medical guidance, platform rules, API parameters, CVEs, or project-specific Web3 facts.",
            "- High-risk finance, legal, health, security, airdrop, and operations tasks retain human confirmation points.",
            "- Do not use this release to execute real-money trades, provide final legal or medical opinions, or run offensive security activity.",
            "",
            "## Reproduce",
            "",
            "```bash",
            "python3 scripts/run_acceptance.py",
            "python3 scripts/generate_release_notes.py",
            "python3 scripts/pack_wikis.py",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    manifest = build_manifest()
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    DOCS_OUT.write_text(markdown_report(manifest), encoding="utf-8")
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if not manifest["ready_for_internal_release"]:
        print("RELEASE NOTES GENERATED WITH BLOCKERS")
        return 1
    print(f"RELEASE NOTES GENERATED ({manifest['wiki_count']} wikis, {len(manifest['packages'])} packages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
