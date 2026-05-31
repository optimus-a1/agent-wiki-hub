#!/usr/bin/env python3
"""Generate planning-only pending packet and work orders for a source-review wave."""
from __future__ import annotations

from argparse import ArgumentParser
from collections import Counter
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS = ROOT / "docs"
PACKET_DIR = REGISTRY / "source-review-packets"


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


def safe_slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "source-review-wave"


def wave_display(value: str) -> str:
    match = re.search(r"wave-(\d+)", value)
    if match:
        return f"Wave {match.group(1)}"
    return value


def wave_token(value: str) -> str:
    return safe_slug(value).upper().replace("-", "")


def wave_doc_token(value: str) -> str:
    return safe_slug(value).upper().replace("-", "_")


def packet_entry(review: dict) -> dict:
    return {
        "ticket_id": review.get("ticket_id", ""),
        "status": "pending",
        "source_title": "<source title>",
        "source_publisher": "<official publisher or authority>",
        "source_url_or_reference": "<URL or local reference>",
        "source_published_or_updated": "YYYY-MM-DD | unknown",
        "source_accessed_on": date.today().isoformat(),
        "verified_on": "",
        "evidence_summary": "<what the source supports and does not support>",
        "affected_pages": [],
        "confidence": "low",
        "remaining_uncertainty": "<remaining uncertainty>",
        "human_reviewer": "<reviewer>",
        "follow_up": "Keep needs-source-update unless authoritative, dated, scoped evidence is recorded and reviewed.",
    }


def write_jsonl(path: Path, entries: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(entry, ensure_ascii=False) for entry in entries) + "\n", encoding="utf-8")


def markdown_list(items: list[str]) -> list[str]:
    if not items:
        return ["- -"]
    return [f"- {item}" for item in items]


def work_order_markdown(order: dict, packet_json: str, packet_jsonl: str, checklist: str, display: str) -> str:
    review = order["review"]
    lines = [
        f"# {display} Source Review Work Order: {review['ticket_id']}",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Scope",
        "",
        f"- Work order: `{order['work_order_id']}`",
        f"- Ticket: `{review['ticket_id']}`",
        f"- Task: `{review['task_id']}`",
        f"- Wiki: `{review['wiki']}`",
        f"- Priority: `{review['priority']}`",
        f"- Wave: `{review['wave']}`",
        f"- Risk: `{review['risk_level']}`",
        f"- Freshness: `{review['freshness']}`",
        f"- Category: `{review['category']}`",
        f"- Reviewer role: `{review['reviewer_role']}`",
        f"- Human confirmation: {bool_word(order['human_confirmation_required'])}",
        f"- Topic: {review['topic']}",
        "",
        "## Required Reading",
        "",
        *markdown_list(review.get("required_reading", [])),
        "",
        "## Suggested Source Types",
        "",
        *markdown_list(review.get("suggested_sources", [])),
        "",
        "## Local Artifacts",
        "",
        f"- Source notes: `{review['source_notes']}`",
        f"- Evidence log: `{review['evidence_log']}`",
        f"- Packet JSON: `{packet_json}`",
        f"- Packet JSONL: `{packet_jsonl}`",
        f"- Packet checklist: `{checklist}`",
        "",
        "## Packet Entry Placeholder",
        "",
        "This is not verified evidence. Replace every placeholder before any real import.",
        "",
        "```json",
        json.dumps(packet_entry(review), ensure_ascii=False, indent=2),
        "```",
        "",
        "## Collection Checklist",
        "",
        "- [ ] Confirm exact ticket scope before collecting sources.",
        "- [ ] Use authoritative, dated, scoped sources only.",
        "- [ ] Record title, publisher, URL or local reference, publication/update date, access date, confidence, and uncertainty.",
        "- [ ] Keep status pending or still-needs-source-update unless evidence has been reviewed.",
        "- [ ] Fill `human_reviewer` before any final status; high-risk nodeops tickets require named human confirmation.",
        "- [ ] Do not write current facts into wiki pages from this work order.",
        "- [ ] Do not record API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.",
        "",
        "## Dry Run",
        "",
        "```bash",
        review.get("dry_run_command", f"python scripts/record_source_evidence.py --ticket-id {review['ticket_id']} --status pending --dry-run"),
        "```",
        "",
        "## Safety Boundary",
        "",
        "- Planning-only work order; it does not browse, verify, certify, import, or write current facts.",
        "- It does not authorize production operations, wallet actions, cloud changes, live upgrades, or billing-sensitive actions.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def packet_checklist_markdown(plan: dict, packet_json: Path, packet_jsonl: Path, entries: list[dict], display: str) -> str:
    lines = [
        f"# Source Review {display} Packet Checklist",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Packet Files",
        "",
        f"- JSON packet: `{rel(packet_json)}`",
        f"- JSONL packet: `{rel(packet_jsonl)}`",
        "",
        "## Safety",
        "",
        "- This packet is planning-only pending evidence.",
        "- It does not verify, certify, import, or write current facts.",
        "- Every entry must remain `status=pending` until a reviewer replaces placeholders with authoritative evidence.",
        "- Do not add API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.",
        "- Do not delete or overwrite wave-1 artifacts.",
        "",
        "## Required Field State",
        "",
        "- `status`: `pending`",
        "- `verified_on`: empty string",
        "- `confidence`: `low`",
        "- `human_reviewer`: `<reviewer>`",
        "- `evidence_summary`: `<what the source supports and does not support>`",
        "",
        "## Dry Run",
        "",
        "```bash",
        f"python scripts/import_source_evidence_packet.py --packet {rel(packet_json)} --dry-run --no-post-checks",
        f"python scripts/import_source_evidence_packet.py --packet {rel(packet_jsonl)} --dry-run --no-post-checks",
        "```",
        "",
        "## Entries",
        "",
        "| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    review_by_ticket = {review["ticket_id"]: review for review in plan.get("selected_reviews", [])}
    for entry in entries:
        review = review_by_ticket.get(entry["ticket_id"], {})
        lines.append(
            f"| `{entry['ticket_id']}` | {review.get('wiki', '-')} | {review.get('risk_level', '-')} | "
            f"`{review.get('reviewer_role', '-')}` | {bool_word(bool(review.get('human_review_gate')))} | {review.get('topic', '-')} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def session_plan_markdown(plan: dict, files: dict, display: str) -> str:
    lines = [
        f"# Source Review {display} Session Plan",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Purpose",
        "",
        f"Prepare {display.lower()} source review packet and work orders without browsing, verifying, importing, or writing current facts.",
        "",
        "## Summary",
        "",
        f"- Current-fact ready: {bool_word(bool(plan.get('current_fact_ready')))}",
        f"- Selected reviews: {plan.get('selected_review_count', 0)}",
        f"- High-risk reviews: {plan.get('selected_high_risk_count', 0)}",
        f"- Human confirmation gates: {plan.get('selected_human_review_gate_count', 0)}",
        f"- Packet JSON: {repo_link(files['packet_json'])}",
        f"- Packet JSONL: {repo_link(files['packet_jsonl'])}",
        f"- Packet checklist: {repo_link(files['packet_checklist'])}",
        f"- Work order directory: {repo_link(files['work_order_dir'])}",
        "",
        "## Selected Reviews",
        "",
        "| Ticket | Wiki | Priority | Risk | Reviewer Role | Human Gate | Topic |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for review in plan.get("selected_reviews", []):
        lines.append(
            f"| `{review['ticket_id']}` | {repo_link('wikis/' + review['wiki'], review['wiki'])} | "
            f"{review['priority']} | {review['risk_level']} | `{review['reviewer_role']}` | "
            f"{bool_word(bool(review['human_review_gate']))} | {review['topic']} |"
        )

    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Packet entries are placeholders only and remain pending.",
            "- Do not use this session plan as verified evidence.",
            "- Do not write current facts into wiki pages.",
            "- Node operations work requires named human confirmation before final status.",
            "",
            "## Next Commands",
            "",
            "```bash",
            "python scripts\\audit_source_review_packets.py",
            "python scripts\\rehearse_source_review_packet_imports.py",
            "python scripts\\audit_links.py",
            "python scripts\\run_acceptance.py",
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def packet_bundle_markdown(plan: dict, manifest: dict, display: str) -> str:
    lines = [
        f"# Source Review {display} Packet Bundle",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Purpose",
        "",
        f"Generate {display.lower()} pending packet artifacts only. No sources are verified, no evidence is imported, and no current facts are written.",
        "",
        "## Summary",
        "",
        f"- Passed: {bool_word(manifest['passed'])}",
        f"- Packet entries: {manifest['entry_count']}",
        f"- High-risk entries: {manifest['high_risk_count']}",
        f"- Human reviewer placeholders: {manifest['human_reviewer_placeholder_count']}",
        f"- JSON packet: {repo_link(manifest['packet_json'])}",
        f"- JSONL packet: {repo_link(manifest['packet_jsonl'])}",
        f"- Checklist: {repo_link(manifest['checklist'])}",
        "",
        "## Entry Field Invariants",
        "",
        "- Every entry has `status=pending`.",
        "- Every entry has `verified_on=\"\"`.",
        "- Every entry has `confidence=low`.",
        "- Every entry has `human_reviewer=\"<reviewer>\"`.",
        "- Every entry has `evidence_summary=\"<what the source supports and does not support>\"`.",
        "- Source title, publisher, URL/reference, and publication date remain placeholders.",
        "",
        "## Tickets",
        "",
        "| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for review in plan.get("selected_reviews", []):
        lines.append(
            f"| `{review['ticket_id']}` | {repo_link('wikis/' + review['wiki'], review['wiki'])} | {review['risk_level']} | "
            f"`{review['reviewer_role']}` | {bool_word(bool(review['human_review_gate']))} | {review['topic']} |"
        )
    lines.extend(["", "## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in manifest["checks"]:
        lines.append(f"| {check['check']} | {'PASS' if check['passed'] else 'FAIL'} | {check['detail']} |")
    return "\n".join(lines).rstrip() + "\n"


def work_orders_report_markdown(plan: dict, manifest: dict, display: str) -> str:
    lines = [
        f"# Source Review {display} Work Orders",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Purpose",
        "",
        f"Provide independent {display.lower()} work orders for source reviewers without verifying, importing, or writing current facts.",
        "",
        "## Summary",
        "",
        f"- Passed: {bool_word(manifest['passed'])}",
        f"- Work orders: {manifest['work_order_count']}",
        f"- High-risk work orders: {manifest['high_risk_count']}",
        f"- Human confirmation gates: {manifest['human_gate_count']}",
        f"- Work order directory: {repo_link(manifest['work_order_dir'])}",
        "",
        "## Work Orders",
        "",
        "| Work Order | Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for order in manifest["work_orders"]:
        review = order["review"]
        lines.append(
            f"| {repo_link(order['work_order_path'], order['work_order_id'])} | `{review['ticket_id']}` | "
            f"{repo_link('wikis/' + review['wiki'], review['wiki'])} | {review['risk_level']} | "
            f"`{review['reviewer_role']}` | {bool_word(bool(order['human_confirmation_required']))} | {review['topic']} |"
        )
    lines.extend(
        [
            "",
            "## Safety Boundary",
            "",
            "- These work orders are planning-only.",
            "- They do not authorize production changes, wallet actions, cloud changes, live upgrades, or billing-sensitive operations.",
            "- They do not certify any source fields; reviewer-filled evidence is still required.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_bundle(plan_path: Path, stem: str, work_order_dir: Path) -> dict:
    plan = read_json(plan_path)
    wave = plan.get("wave", "wave-2")
    display = wave_display(wave)
    doc_token = wave_doc_token(wave)
    entries = [packet_entry(review) for review in plan.get("selected_reviews", [])]
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    work_order_dir.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)

    packet_json = PACKET_DIR / f"{stem}.json"
    packet_jsonl = PACKET_DIR / f"{stem}.jsonl"
    checklist = PACKET_DIR / f"{stem}-checklist.md"
    packet_manifest = PACKET_DIR / f"{stem}-manifest.json"

    packet = {
        "packet_id": stem,
        "created_on": date.today().isoformat(),
        "created_by": "<human reviewer or source-refresh agent>",
        "dry_run_first": True,
        "wave": wave,
        "source_review_session_id": plan.get("session_id", ""),
        "source_review_session_filters": plan.get("selected_filters", {}),
        "planning_only": True,
        "no_current_fact_write": True,
        "entries": entries,
    }
    packet_json.write_text(json.dumps(packet, ensure_ascii=False, indent=2), encoding="utf-8")
    write_jsonl(packet_jsonl, entries)
    checklist.write_text(packet_checklist_markdown(plan, packet_json, packet_jsonl, entries, display), encoding="utf-8")

    work_orders = []
    for order in plan.get("planned_work_orders", []):
        review = order["review"]
        work_order_path = work_order_dir / f"{review['ticket_id']}.md"
        record = {
            "work_order_id": f"{wave_token(wave)}-WORKORDER-{review['ticket_id']}",
            "ticket_id": review["ticket_id"],
            "human_confirmation_required": bool(order.get("human_confirmation_required")),
            "review": review,
            "packet_entry_template": packet_entry(review),
            "work_order_path": rel(work_order_path),
        }
        work_order_path.write_text(work_order_markdown(record, rel(packet_json), rel(packet_jsonl), rel(checklist), display), encoding="utf-8")
        work_orders.append(record)

    work_order_manifest = {
        "generated": date.today().isoformat(),
        "passed": True,
        "wave": wave,
        "planning_only": True,
        "no_current_fact_write": True,
        "work_order_dir": rel(work_order_dir),
        "work_order_count": len(work_orders),
        "high_risk_count": sum(1 for order in work_orders if order["review"]["risk_level"] == "high"),
        "human_gate_count": sum(1 for order in work_orders if order["human_confirmation_required"]),
        "work_order_paths": [order["work_order_path"] for order in work_orders],
        "work_orders": work_orders,
    }
    (work_order_dir / "manifest.json").write_text(json.dumps(work_order_manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    checks = [
        {
            "check": "plan passed",
            "passed": bool(plan.get("passed")),
            "detail": rel(plan_path),
        },
        {
            "check": "entry count matches selected reviews",
            "passed": len(entries) == int(plan.get("selected_review_count", len(entries))),
            "detail": f"{len(entries)} entries for {plan.get('selected_review_count', 0)} selected reviews",
        },
        {
            "check": "entries remain pending",
            "passed": all(entry["status"] == "pending" for entry in entries),
            "detail": "all entries use status=pending",
        },
        {
            "check": "entries keep required placeholder fields",
            "passed": all(
                entry["verified_on"] == ""
                and entry["confidence"] == "low"
                and entry["human_reviewer"] == "<reviewer>"
                and entry["evidence_summary"] == "<what the source supports and does not support>"
                for entry in entries
            ),
            "detail": "verified_on, confidence, human_reviewer, and evidence_summary placeholders checked",
        },
        {
            "check": "work orders written",
            "passed": all((ROOT / order["work_order_path"]).exists() for order in work_orders) and (work_order_dir / "manifest.json").exists(),
            "detail": f"{len(work_orders)} work order files plus manifest",
        },
    ]
    manifest = {
        "generated": date.today().isoformat(),
        "packet_id": stem,
        "wave": wave,
        "passed": all(check["passed"] for check in checks),
        "planning_only": True,
        "no_current_fact_write": True,
        "entry_count": len(entries),
        "high_risk_count": sum(1 for review in plan.get("selected_reviews", []) if review.get("risk_level") == "high"),
        "human_reviewer_placeholder_count": sum(1 for entry in entries if entry["human_reviewer"] == "<reviewer>"),
        "status_counts": dict(sorted(Counter(entry["status"] for entry in entries).items())),
        "packet_json": rel(packet_json),
        "packet_jsonl": rel(packet_jsonl),
        "checklist": rel(checklist),
        "manifest": rel(packet_manifest),
        "work_order_dir": rel(work_order_dir),
        "work_order_manifest": rel(work_order_dir / "manifest.json"),
        "dry_run_import_commands": [
            f"python scripts/import_source_evidence_packet.py --packet {rel(packet_json)} --dry-run --no-post-checks",
            f"python scripts/import_source_evidence_packet.py --packet {rel(packet_jsonl)} --dry-run --no-post-checks",
        ],
        "checks": checks,
    }
    packet_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    files = {
        "packet_json": manifest["packet_json"],
        "packet_jsonl": manifest["packet_jsonl"],
        "packet_checklist": manifest["checklist"],
        "work_order_dir": manifest["work_order_dir"],
    }
    packet_bundle_doc = DOCS / f"SOURCE_REVIEW_{doc_token}_PACKET_BUNDLE.md"
    work_orders_doc = DOCS / f"SOURCE_REVIEW_{doc_token}_WORK_ORDERS.md"
    session_plan_doc = DOCS / f"SOURCE_REVIEW_{doc_token}_SESSION_PLAN.md"
    packet_bundle_doc.write_text(packet_bundle_markdown(plan, manifest, display), encoding="utf-8")
    work_orders_doc.write_text(work_orders_report_markdown(plan, work_order_manifest, display), encoding="utf-8")
    session_plan_doc.write_text(session_plan_markdown(plan, files, display), encoding="utf-8")
    manifest["docs"] = {
        "packet_bundle": rel(packet_bundle_doc),
        "work_orders": rel(work_orders_doc),
        "session_plan": rel(session_plan_doc),
    }
    packet_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "packet_manifest": manifest,
        "work_order_manifest": work_order_manifest,
    }


def main() -> int:
    parser = ArgumentParser(description="Generate planning-only source-review wave packet and work orders.")
    parser.add_argument("--plan", default="registry/source-review-wave-2-plan.json", help="Path to wave plan JSON.")
    parser.add_argument("--stem", default="source-review-session-wave-2-pending", help="Packet file stem.")
    parser.add_argument("--work-order-dir", default="registry/source-review-work-orders-wave-2", help="Independent work order directory.")
    args = parser.parse_args()

    plan_path = Path(args.plan)
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    work_order_dir = Path(args.work_order_dir)
    if not work_order_dir.is_absolute():
        work_order_dir = ROOT / work_order_dir

    result = build_bundle(plan_path, safe_slug(args.stem), work_order_dir)
    manifest = result["packet_manifest"]
    print(f"Wrote {manifest['packet_json']}")
    print(f"Wrote {manifest['packet_jsonl']}")
    print(f"Wrote {manifest['checklist']}")
    print(f"Wrote {manifest['manifest']}")
    print(f"Wrote {manifest['work_order_manifest']}")
    for doc_path in manifest.get("docs", {}).values():
        print(f"Wrote {doc_path}")
    print(
        f"SOURCE REVIEW {manifest.get('wave', 'wave-2').upper()} PENDING PACKET GENERATED "
        f"({manifest['entry_count']} entries, {result['work_order_manifest']['work_order_count']} work orders)"
    )
    return 0 if manifest["passed"] and result["work_order_manifest"]["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
