#!/usr/bin/env python3
"""Generate wave-2 evidence preparation batches without source verification."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
DOCS = ROOT / "docs"
PLAN_JSON = REGISTRY / "source-review-wave-2-plan.json"
BATCH_DIR = REGISTRY / "source-review-wave-2-batches"
DOCS_OUT = DOCS / "SOURCE_REVIEW_WAVE_2_BATCH_PLAN.md"
JSON_OUT = REGISTRY / "source-review-wave-2-batch-plan.json"

BATCHES = [
    {
        "batch_id": "batch-1-nodeops",
        "title": "Batch 1 - NodeOps High-Risk Review",
        "reviewer_role": "operations-change-reviewer",
        "file": "batch-1-nodeops.md",
        "risk_note": "High-risk operations topics require named human confirmation before any final status.",
    },
    {
        "batch_id": "batch-2-customs",
        "title": "Batch 2 - Customs P0 Review",
        "reviewer_role": "customs-document-reviewer",
        "file": "batch-2-customs.md",
        "risk_note": "Customs topics require official, jurisdiction-specific sources before current facts can be used.",
    },
    {
        "batch_id": "batch-3-ecommerce",
        "title": "Batch 3 - Ecommerce P1 Review",
        "reviewer_role": "ecommerce-policy-reviewer",
        "file": "batch-3-ecommerce.md",
        "risk_note": "Platform and product facts remain time-sensitive and must stay pending until source-scoped.",
    },
    {
        "batch_id": "batch-4-research",
        "title": "Batch 4 - Research P2 Review",
        "reviewer_role": "research-methods-reviewer",
        "file": "batch-4-research.md",
        "risk_note": "Research artifacts require primary pages, repository/model-card evidence, and license checks.",
    },
]

EVIDENCE_FIELDS = [
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

DISALLOWED_SOURCES = [
    "unsourced summaries",
    "marketing copy without dates or scope",
    "scraped snippets without an authoritative source page",
    "private account data, cookies, API keys, private keys, seed phrases, or credentials",
    "outdated, conflicting, or jurisdiction-mismatched sources used as final authority",
]

ACCEPTANCE_COMMANDS = [
    "python scripts\\audit_source_review_packets.py",
    "python scripts\\rehearse_source_review_packet_imports.py",
    "python scripts\\audit_source_evidence_quality.py",
    "python scripts\\audit_source_refresh_completion.py",
    "python scripts\\audit_links.py",
    "python scripts\\run_acceptance.py",
]


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


def markdown_list(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items] or ["- -"]


def ticket_table(orders: list[dict]) -> list[str]:
    rows = [
        "| Ticket | Wiki | Risk | Reviewer Role | Human Gate | Topic | Source Targets |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for order in orders:
        review = order["review"]
        sources = ", ".join(review.get("suggested_sources", [])) or "-"
        rows.append(
            f"| `{review['ticket_id']}` | {repo_link('wikis/' + review['wiki'], review['wiki'])} | {review['risk_level']} | "
            f"`{review['reviewer_role']}` | {bool_word(bool(order['human_confirmation_required']))} | {review['topic']} | {sources} |"
        )
    return rows


def batch_markdown(batch: dict) -> str:
    orders = batch["work_orders"]
    lines = [
        f"# {batch['title']}",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Purpose",
        "",
        "Prepare source evidence collection for this wave-2 batch without browsing, verifying, importing, or writing current facts.",
        "",
        "## Batch Summary",
        "",
        f"- Batch id: `{batch['batch_id']}`",
        f"- Reviewer role: `{batch['reviewer_role']}`",
        f"- Tickets: {len(orders)}",
        f"- High-risk tickets: {sum(1 for order in orders if order['review']['risk_level'] == 'high')}",
        f"- Human gates: {sum(1 for order in orders if order['human_confirmation_required'])}",
        f"- Risk note: {batch['risk_note']}",
        "",
        "## Tickets",
        "",
        *ticket_table(orders),
        "",
        "## Evidence Fields To Fill",
        "",
    ]
    lines.extend(f"- `{field}`" for field in EVIDENCE_FIELDS)
    lines.extend(["", "## Authoritative Source Targets", ""])
    for order in orders:
        review = order["review"]
        lines.extend(
            [
                f"### {review['ticket_id']}",
                "",
                f"- Topic: {review['topic']}",
                f"- Wiki: `{review['wiki']}`",
                f"- Evidence log: `{review['evidence_log']}`",
                f"- Source notes: `{review['source_notes']}`",
            ]
        )
        lines.extend(markdown_list(review.get("suggested_sources", [])))
        lines.append("")
    lines.extend(["## Disallowed Sources", ""])
    lines.extend(markdown_list(DISALLOWED_SOURCES))
    lines.extend(
        [
            "",
            "## Human Gate Notes",
            "",
            "- High-risk tickets require a named human reviewer before any `verified` or `unchanged` status.",
            "- If no reviewer is available, keep the ticket `pending` or `still-needs-source-update`.",
            "- Keep nodeops operational boundaries visible; no production, wallet, firewall, billing, or upgrade action is authorized by this batch.",
            "",
            "## Rollback Notes",
            "",
            "- This batch writes planning artifacts only; rollback is removing generated batch docs/registry entries.",
            "- If future evidence import fails, do not delete source logs blindly; add a corrective evidence entry or keep the ticket pending.",
            "- Do not revert unrelated user changes.",
            "",
            "## Acceptance Commands",
            "",
            "```bash",
            *ACCEPTANCE_COMMANDS,
            "```",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_plan() -> dict:
    plan = read_json(PLAN_JSON)
    orders = plan.get("planned_work_orders", [])
    batches = []
    for spec in BATCHES:
        selected = [order for order in orders if order["review"].get("reviewer_role") == spec["reviewer_role"]]
        path = BATCH_DIR / spec["file"]
        batch = {
            **spec,
            "path": rel(path),
            "ticket_ids": [order["review"]["ticket_id"] for order in selected],
            "wiki_counts": dict(sorted(Counter(order["review"]["wiki"] for order in selected).items())),
            "risk_counts": dict(sorted(Counter(order["review"]["risk_level"] for order in selected).items())),
            "human_gate_count": sum(1 for order in selected if order["human_confirmation_required"]),
            "work_orders": selected,
            "evidence_fields_to_fill": EVIDENCE_FIELDS,
            "disallowed_sources": DISALLOWED_SOURCES,
            "acceptance_commands": ACCEPTANCE_COMMANDS,
            "rollback_notes": [
                "Planning artifacts can be regenerated from registry/source-review-wave-2-plan.json.",
                "Do not delete evidence logs or unrelated files as rollback.",
                "If a source is invalid, keep status pending or still-needs-source-update.",
            ],
            "human_gate_notes": [
                "Named human reviewer required before final status on high-risk tickets.",
                "No production operations or current-fact wiki writes are authorized by this preparation batch.",
            ],
        }
        batches.append(batch)
    checks = [
        {
            "check": "wave-2 plan exists and passed",
            "passed": PLAN_JSON.exists() and bool(plan.get("passed")),
            "detail": rel(PLAN_JSON),
        },
        {
            "check": "all wave-2 tickets assigned to batches",
            "passed": sum(len(batch["ticket_ids"]) for batch in batches) == int(plan.get("selected_review_count", 0)),
            "detail": f"{sum(len(batch['ticket_ids']) for batch in batches)}/{plan.get('selected_review_count', 0)} tickets",
        },
        {
            "check": "no current facts written",
            "passed": True,
            "detail": "planning-only batch preparation",
        },
    ]
    return {
        "generated": date.today().isoformat(),
        "passed": all(check["passed"] for check in checks),
        "purpose": "Prepare wave-2 evidence collection batches without source verification or current-fact writes.",
        "planning_only": True,
        "no_current_fact_write": True,
        "source_review_wave_plan": rel(PLAN_JSON),
        "batch_dir": rel(BATCH_DIR),
        "ticket_count": sum(len(batch["ticket_ids"]) for batch in batches),
        "batch_count": len(batches),
        "high_risk_count": sum(sum(1 for order in batch["work_orders"] if order["review"]["risk_level"] == "high") for batch in batches),
        "human_gate_count": sum(batch["human_gate_count"] for batch in batches),
        "batches": batches,
        "checks": checks,
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Source Review Wave 2 Batch Plan",
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
        f"- Planning only: {bool_word(data['planning_only'])}",
        f"- Current facts written: no",
        f"- Tickets: {data['ticket_count']}",
        f"- Batches: {data['batch_count']}",
        f"- High-risk tickets: {data['high_risk_count']}",
        f"- Human gates: {data['human_gate_count']}",
        f"- Batch directory: {repo_link(data['batch_dir'])}",
        "",
        "## Batches",
        "",
        "| Batch | Reviewer Role | Tickets | High Risk | Human Gates | File |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for batch in data["batches"]:
        high_risk = batch["risk_counts"].get("high", 0)
        lines.append(
            f"| `{batch['batch_id']}` | `{batch['reviewer_role']}` | {len(batch['ticket_ids'])} | "
            f"{high_risk} | {batch['human_gate_count']} | {repo_link(batch['path'])} |"
        )
    lines.extend(["", "## Ticket Overview", ""])
    for batch in data["batches"]:
        lines.extend([f"### {batch['batch_id']}", ""])
        lines.extend(ticket_table(batch["work_orders"]))
        lines.append("")
    lines.extend(["## Checks", "", "| Check | Result | Detail |", "| --- | --- | --- |"])
    for check in data["checks"]:
        lines.append(f"| {check['check']} | {'PASS' if check['passed'] else 'FAIL'} | {check['detail']} |")
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(data: dict) -> None:
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for batch in data["batches"]:
        (ROOT / batch["path"]).write_text(batch_markdown(batch), encoding="utf-8")
    DOCS_OUT.write_text(markdown_report(data), encoding="utf-8")
    JSON_OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    data = build_plan()
    write_outputs(data)
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    for batch in data["batches"]:
        print(f"Wrote {batch['path']}")
    print(f"SOURCE REVIEW WAVE-2 BATCH PLAN {'PASSED' if data['passed'] else 'FAILED'} ({data['ticket_count']} tickets)")
    return 0 if data["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
