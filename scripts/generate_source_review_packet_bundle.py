#!/usr/bin/env python3
"""Export source-review session packets with placeholders only."""
from __future__ import annotations

from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
PACKET_DIR = REGISTRY / "source-review-packets"
DOCS_OUT = ROOT / "docs" / "SOURCE_REVIEW_PACKET_BUNDLE.md"
JSON_OUT = REGISTRY / "source-review-packet-bundle.json"
DEFAULT_PLAN = REGISTRY / "source-review-session-plan.json"

FINAL_STATUSES = {"verified", "unchanged", "still-needs-source-update", "rejected"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----", re.I),
    re.compile(r"\b(api[_-]?key|secret[_-]?key|private[_-]?key|access[_-]?token|refresh[_-]?token)\s*[:=]", re.I),
    re.compile(r"\b(cookie|set-cookie|authorization)\s*:", re.I),
    re.compile(r"\bbearer\s+[A-Za-z0-9._~+/=-]{16,}", re.I),
    re.compile(r"\b(seed phrase|mnemonic)\b", re.I),
]

REPORTS = {
    "source_review_readiness_matrix": "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
    "source_review_packet_audit": "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
    "source_review_packet_rehearsal": "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
    "source_review_session_plan": "docs/SOURCE_REVIEW_SESSION_PLAN.md",
    "source_reviewer_queue": "docs/SOURCE_REVIEWER_QUEUE.md",
    "source_refresh_dashboard": "docs/SOURCE_REFRESH_DASHBOARD.md",
    "source_evidence_packet_importer": "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
    "source_evidence_quality": "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md",
    "source_refresh_completion": "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
}


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
    return value or "source-review-session"


def default_stem(plan: dict) -> str:
    filters = plan.get("selected_filters", {})
    if filters.get("wave"):
        return f"source-review-session-{safe_slug(filters['wave'])}-pending"
    if filters.get("wiki"):
        return f"source-review-session-{safe_slug(filters['wiki'])}-pending"
    if filters.get("reviewer_role"):
        return f"source-review-session-{safe_slug(filters['reviewer_role'])}-pending"
    return f"{safe_slug(plan.get('session_id', 'source-review-session'))}-pending"


def has_secret(entry: dict) -> bool:
    text = json.dumps(entry, ensure_ascii=False)
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def packet_from_plan(plan: dict, stem: str) -> dict:
    packet = dict(plan.get("packet_template") or {})
    packet["packet_id"] = stem
    packet["created_on"] = date.today().isoformat()
    packet["created_by"] = "<human reviewer or source-refresh agent>"
    packet["dry_run_first"] = True
    packet["source_review_session_id"] = plan.get("session_id", "")
    packet["source_review_session_filters"] = plan.get("selected_filters", {})
    entries = []
    for entry in packet.get("entries", []):
        item = dict(entry)
        item["status"] = "pending"
        item["verified_on"] = ""
        entries.append(item)
    packet["entries"] = entries
    return packet


def checklist_markdown(plan: dict, packet: dict, json_path: Path, jsonl_path: Path) -> str:
    reviews = plan.get("selected_reviews", [])
    lines = [
        "# Source Review Packet Checklist",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Packet Files",
        "",
        f"- JSON packet: `{rel(json_path)}`",
        f"- JSONL packet: `{rel(jsonl_path)}`",
        "",
        "## Safety",
        "",
        "- This packet contains placeholders only and does not certify current facts.",
        "- Replace every placeholder before a real import.",
        "- Keep status `pending` until authoritative evidence has been collected.",
        "- High-risk or human-gated tickets need an explicit human reviewer before a final status.",
        "- Do not add API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.",
        "",
        "## Dry Run",
        "",
        "```bash",
        f"python3 scripts/import_source_evidence_packet.py --packet {rel(json_path)} --dry-run --no-post-checks",
        f"python3 scripts/import_source_evidence_packet.py --packet {rel(jsonl_path)} --dry-run --no-post-checks",
        "```",
        "",
        "## Selected Reviews",
        "",
        "| Ticket | Wiki | Reviewer Role | Human Gate | Topic | Suggested Sources |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    review_by_ticket = {review.get("ticket_id"): review for review in reviews}
    for entry in packet.get("entries", []):
        review = review_by_ticket.get(entry.get("ticket_id"), {})
        suggested = ", ".join(review.get("suggested_sources", [])) or "-"
        lines.append(
            f"| `{entry.get('ticket_id')}` | {review.get('wiki', '-')} | {review.get('reviewer_role', '-')} | "
            f"{bool_word(bool(review.get('human_review_gate')))} | {review.get('topic', '-')} | {suggested} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def write_jsonl(path: Path, entries: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(entry, ensure_ascii=False) for entry in entries) + "\n", encoding="utf-8")


def build_bundle(plan_path: Path, out_dir: Path, stem: str | None = None) -> dict:
    plan = read_json(plan_path)
    stem = safe_slug(stem or default_stem(plan))
    packet = packet_from_plan(plan, stem)
    entries = packet.get("entries", [])
    json_path = out_dir / f"{stem}.json"
    jsonl_path = out_dir / f"{stem}.jsonl"
    checklist_path = out_dir / f"{stem}-checklist.md"
    manifest_path = out_dir / f"{stem}-manifest.json"

    out_dir.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2), encoding="utf-8")
    write_jsonl(jsonl_path, entries)
    checklist_path.write_text(checklist_markdown(plan, packet, json_path, jsonl_path), encoding="utf-8")

    checks = [
        {
            "check": "source review session plan exists",
            "passed": plan_path.exists() and bool(plan),
            "detail": rel(plan_path) if plan_path.exists() else f"missing {rel(plan_path)}",
        },
        {
            "check": "source review session plan passed",
            "passed": bool(plan.get("passed")),
            "detail": f"selected reviews: {plan.get('selected_review_count', 0)}",
        },
        {
            "check": "packet entry count matches selected reviews",
            "passed": len(entries) == int(plan.get("selected_review_count", len(entries))),
            "detail": f"{len(entries)} packet entries for {plan.get('selected_review_count', 0)} selected reviews",
        },
        {
            "check": "packet keeps entries pending",
            "passed": all(entry.get("status") == "pending" for entry in entries),
            "detail": "all generated entries use pending status",
        },
        {
            "check": "packet contains no final statuses",
            "passed": not any(entry.get("status") in FINAL_STATUSES for entry in entries),
            "detail": "generated bundle cannot mark evidence verified",
        },
        {
            "check": "packet contains no detected secrets",
            "passed": not any(has_secret(entry) for entry in entries),
            "detail": "secret scan over generated packet entries",
        },
        {
            "check": "bundle files written",
            "passed": all(path.exists() for path in [json_path, jsonl_path, checklist_path]),
            "detail": ", ".join(rel(path) for path in [json_path, jsonl_path, checklist_path]),
        },
    ]

    manifest = {
        "generated": date.today().isoformat(),
        "packet_id": stem,
        "passed": all(check["passed"] for check in checks),
        "purpose": "Provide offline-safe source evidence packet templates for the current source-review session.",
        "current_fact_ready": bool(plan.get("current_fact_ready", False)),
        "selected_review_count": int(plan.get("selected_review_count", len(entries))),
        "selected_human_review_gate_count": int(plan.get("selected_human_review_gate_count", 0)),
        "selected_high_risk_count": int(plan.get("selected_high_risk_count", 0)),
        "source_review_session_plan": rel(plan_path),
        "packet_json": rel(json_path),
        "packet_jsonl": rel(jsonl_path),
        "checklist": rel(checklist_path),
        "manifest": rel(manifest_path),
        "dry_run_import_commands": [
            f"python3 scripts/import_source_evidence_packet.py --packet {rel(json_path)} --dry-run --no-post-checks",
            f"python3 scripts/import_source_evidence_packet.py --packet {rel(jsonl_path)} --dry-run --no-post-checks",
        ],
        "real_import_warning": "Replace placeholders with authoritative, dated evidence before any non-dry-run import.",
        "reports": REPORTS,
        "checks": checks,
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest["checks"][-1]["passed"] = all(path.exists() for path in [json_path, jsonl_path, checklist_path, manifest_path])
    manifest["checks"][-1]["detail"] = ", ".join(rel(path) for path in [json_path, jsonl_path, checklist_path, manifest_path])
    manifest["passed"] = all(check["passed"] for check in manifest["checks"])
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Packet Bundle",
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
        f"- Current-fact ready: {bool_word(data['current_fact_ready'])}",
        f"- Selected reviews: {data['selected_review_count']}",
        f"- Human review gates: {data['selected_human_review_gate_count']}",
        f"- High-risk reviews: {data['selected_high_risk_count']}",
        f"- JSON packet: {repo_link(data['packet_json'])}",
        f"- JSONL packet: {repo_link(data['packet_jsonl'])}",
        f"- Checklist: {repo_link(data['checklist'])}",
        "",
        "## Dry-Run Commands",
        "",
        "```bash",
        *data["dry_run_import_commands"],
        "```",
        "",
        "## Real Import Warning",
        "",
        data["real_import_warning"],
        "",
        "## Related Reports",
        "",
    ]
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
            "- This bundle is a template bundle only.",
            "- It does not fetch, verify, or certify external facts.",
            "- It intentionally keeps every entry at `pending` status.",
            "- Do not use a non-dry-run import until every placeholder has been replaced with authoritative source evidence.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = ArgumentParser(description="Generate source-review packet bundles from a session plan.")
    parser.add_argument("--session-plan", default=str(DEFAULT_PLAN.relative_to(ROOT)), help="Path to source-review-session-plan.json.")
    parser.add_argument("--out-dir", default=str(PACKET_DIR.relative_to(ROOT)), help="Directory for generated packet files.")
    parser.add_argument("--stem", help="File stem for generated packet files.")
    parser.add_argument("--json", action="store_true", help="Print bundle manifest JSON after writing outputs.")
    args = parser.parse_args()

    plan_path = Path(args.session_plan)
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir

    data = build_bundle(plan_path, out_dir, args.stem)
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
        print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
        print(f"Wrote {data['packet_json']}")
        print(f"Wrote {data['packet_jsonl']}")
        print(f"Wrote {data['checklist']}")
        print(
            "SOURCE REVIEW PACKET BUNDLE GENERATED "
            f"({data['selected_review_count']} entries, {data['selected_human_review_gate_count']} human gates)"
        )
    if not data["passed"]:
        failed = [check for check in data["checks"] if not check["passed"]]
        print(f"SOURCE REVIEW PACKET BUNDLE HAS BLOCKERS: {failed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
