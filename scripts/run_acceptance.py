#!/usr/bin/env python3
"""Run the full local acceptance suite for Agent Wiki Hub."""
from pathlib import Path
from datetime import date
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS_OUT = ROOT / "docs" / "ACCEPTANCE_REPORT.md"
JSON_OUT = ROOT / "registry" / "acceptance-report.json"

SEARCH_CHECKS = [
    ("finance-agent-wiki", "risk control"),
    ("customs-agent-wiki", "field extraction"),
    ("finance-agent-wiki", "paper trading real money"),
    ("customs-agent-wiki", "INV-EXAMPLE-001 evidence confidence"),
    ("agent-engineering-wiki", "needs-source-update topics"),
    ("security-agent-wiki", "bypass login Authorization header"),
]

ROUTE_CHECKS = [
    ("risk control backtest paper trading", "finance-agent-wiki"),
    ("field extraction invoice packing list", "customs-agent-wiki"),
    ("defensive security hardening", "security-agent-wiki"),
]


def run_step(name: str, args: list[str]) -> dict:
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "name": name,
        "command": " ".join([Path(sys.executable).name, *args]),
        "returncode": proc.returncode,
        "output": proc.stdout.strip(),
        "passed": proc.returncode == 0,
    }


def search_step(wiki: str, query: str) -> dict:
    step = run_step(
        f"search {wiki}: {query}",
        ["scripts/search_wiki.py", "--query", query, "--wiki", wiki],
    )
    output = step["output"]
    has_result = bool(output and "No results" not in output)
    step["passed"] = step["passed"] and has_result
    step["has_result"] = has_result
    return step


def route_step(query: str, expected_wiki: str) -> dict:
    step = run_step(
        f"route query: {query}",
        ["scripts/route_wiki.py", "--query", query, "--json"],
    )
    top_wiki = None
    try:
        top_wiki = json.loads(step["output"]).get("top_wiki")
    except json.JSONDecodeError:
        pass
    step["top_wiki"] = top_wiki
    step["expected_wiki"] = expected_wiki
    step["passed"] = step["passed"] and top_wiki == expected_wiki
    return step


def markdown_report(steps: list[dict]) -> str:
    passed = sum(1 for step in steps if step["passed"])
    lines = [
        "# Agent Wiki Hub Acceptance Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Steps: {len(steps)}",
        f"- Passed: {passed}",
        f"- Failed: {len(steps) - passed}",
        "",
        "## Steps",
        "",
        "| Step | Result | Command |",
        "| --- | --- | --- |",
    ]
    for step in steps:
        result = "PASS" if step["passed"] else "FAIL"
        lines.append(f"| {step['name']} | {result} | `{step['command']}` |")

    lines.extend(["", "## Command Output", ""])
    for step in steps:
        result = "PASS" if step["passed"] else "FAIL"
        lines.extend([
            f"### {step['name']} - {result}",
            "",
            "```text",
            step["output"] or "<no output>",
            "```",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    steps = [
        run_step("validate wiki structure and evals", ["scripts/validate_wiki.py"]),
        run_step("check registry consistency", ["scripts/check_registry_consistency.py"]),
        run_step("audit CI workflow", ["scripts/audit_ci_workflow.py"]),
        run_step("audit page metadata", ["scripts/audit_page_metadata.py"]),
        run_step("audit content coverage", ["scripts/audit_content_coverage.py"]),
        run_step("check eval files", ["scripts/check_eval_files.py"]),
        run_step("update search index", ["scripts/update_index.py"]),
        run_step("generate Obsidian vault", ["scripts/generate_obsidian_vault.py"]),
        run_step("generate Obsidian canvas", ["scripts/generate_obsidian_canvas.py"]),
        run_step("audit Obsidian vault", ["scripts/audit_obsidian_vault.py"]),
        run_step("collect dashboard data", ["dashboard/scripts/collect_dashboard_data.py"]),
        run_step("audit dashboard", ["scripts/audit_dashboard.py"]),
        run_step("generate ingestion report", ["ingestion/generate_ingestion_report.py"]),
        run_step("audit ingestion pipeline", ["scripts/audit_ingestion_pipeline.py"]),
        run_step("generate crawl report", ["crawler/generate_crawl_report.py"]),
        run_step("classify candidate knowledge dry-run", ["scripts/classify_candidate_knowledge.py", "--dry-run"]),
        run_step("promote stable knowledge dry-run", ["scripts/promote_stable_knowledge.py", "--dry-run"]),
        run_step("generate source review from candidates dry-run", ["scripts/generate_source_review_from_candidates.py", "--dry-run"]),
        run_step("audit crawler outputs", ["scripts/audit_crawler_outputs.py"]),
        run_step("audit knowledge promotion", ["scripts/audit_knowledge_promotion.py"]),
        run_step("audit RAG config", ["scripts/audit_rag_config.py"]),
        run_step("audit secret leaks", ["scripts/audit_secret_leaks.py"]),
        run_step("report wiki status", ["scripts/report_wiki_status.py"]),
        run_step("list source updates", ["scripts/list_source_updates.py"]),
        run_step("generate source refresh playbook", ["scripts/generate_source_refresh_playbook.py"]),
        run_step("generate source refresh tickets", ["scripts/generate_source_refresh_tickets.py"]),
        run_step("dry-run source evidence recorder", ["scripts/record_source_evidence.py", "--ticket-id", "TICKET-SRC-006", "--status", "pending", "--dry-run", "--allow-duplicate"]),
        run_step("generate source evidence packet importer", ["scripts/import_source_evidence_packet.py"]),
        run_step("generate source evidence packet fixtures", ["scripts/generate_source_evidence_packet_fixtures.py"]),
        run_step("generate source refresh logs", ["scripts/generate_source_refresh_logs.py"]),
        run_step("audit source refresh completion", ["scripts/audit_source_refresh_completion.py"]),
        run_step("audit source evidence quality", ["scripts/audit_source_evidence_quality.py"]),
        run_step("audit safety boundaries", ["scripts/audit_safety_boundaries.py"]),
        run_step("generate source refresh wave runner", ["scripts/generate_source_refresh_wave_runner.py"]),
        run_step("generate source reviewer queue", ["scripts/generate_source_reviewer_queue.py"]),
        run_step("generate source review session plan", ["scripts/generate_source_review_session_plan.py"]),
        run_step("generate source review packet bundle", ["scripts/generate_source_review_packet_bundle.py"]),
        run_step("generate source review packet classification", ["scripts/generate_source_review_packet_classification.py"]),
        run_step("audit source review packets", ["scripts/audit_source_review_packets.py"]),
        run_step("rehearse source review packet imports", ["scripts/rehearse_source_review_packet_imports.py"]),
        run_step("generate source review readiness matrix", ["scripts/generate_source_review_readiness_matrix.py"]),
        run_step("generate source review work orders", ["scripts/generate_source_review_work_orders.py"]),
        run_step(
            "dry-run source review packet bundle",
            [
                "scripts/import_source_evidence_packet.py",
                "--packet",
                "registry/source-review-packets/source-review-session-wave-1-pending.json",
                "--dry-run",
                "--no-post-checks",
                "--allow-duplicate",
            ],
        ),
        run_step("generate source refresh dashboard", ["scripts/generate_source_refresh_dashboard.py"]),
        run_step("pack wikis for navigation", ["scripts/pack_wikis.py"]),
        run_step("generate hub navigation", ["scripts/generate_hub_navigation.py"]),
        run_step("generate agent routing cards", ["scripts/generate_agent_routing_cards.py"]),
        run_step("generate agent handoff", ["scripts/generate_agent_handoff.py"]),
        run_step("audit links", ["scripts/audit_links.py"]),
    ]
    steps.extend(route_step(query, expected) for query, expected in ROUTE_CHECKS)
    steps.extend(search_step(wiki, query) for wiki, query in SEARCH_CHECKS)
    steps.append(run_step("pack wikis", ["scripts/pack_wikis.py"]))
    steps.append(run_step("audit pack integrity", ["scripts/audit_pack_integrity.py"]))
    steps.append(run_step("generate release notes", ["scripts/generate_release_notes.py"]))
    steps.append(run_step("generate change summary", ["scripts/generate_change_summary.py"]))

    passed = all(step["passed"] for step in steps)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": passed, "steps": steps}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    DOCS_OUT.write_text(markdown_report(steps), encoding="utf-8")
    # Refresh packages after writing this report so the all-in-one zip contains it.
    final_pack = run_step("pack wikis with acceptance report", ["scripts/pack_wikis.py"])
    steps.append(final_pack)
    final_pack_audit = run_step("audit final package integrity", ["scripts/audit_pack_integrity.py"])
    steps.append(final_pack_audit)
    passed = all(step["passed"] for step in steps)
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": passed, "steps": steps}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    DOCS_OUT.write_text(markdown_report(steps), encoding="utf-8")
    # Refresh source fixtures, wave runner, handoff, and release notes after the final acceptance report includes the package-refresh step.
    subprocess.run([sys.executable, "scripts/generate_source_evidence_packet_fixtures.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_refresh_wave_runner.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_reviewer_queue.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_review_session_plan.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_review_packet_bundle.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/audit_source_review_packets.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/rehearse_source_review_packet_imports.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_review_readiness_matrix.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_review_work_orders.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_source_refresh_dashboard.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_agent_handoff.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    subprocess.run([sys.executable, "scripts/generate_release_notes.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    # One silent final refresh captures the final report that includes the package-refresh step.
    subprocess.run([sys.executable, "scripts/pack_wikis.py"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print("ACCEPTANCE PASSED" if passed else "ACCEPTANCE FAILED")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
