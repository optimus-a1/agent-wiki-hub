#!/usr/bin/env python3
"""Update Obsidian MOCs and dashboards with v2.1 backlinks."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian-vault"
MOCS = VAULT / "02_Knowledge" / "MOCs"
DASH = VAULT / "05_Dashboard"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def append_section(path: Path, heading: str, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else f"# {path.stem}\n"
    if heading in text:
        text = text.split(heading, 1)[0].rstrip()
    path.write_text(text.rstrip() + "\n\n" + heading + "\n\n" + "\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_dashboard_pages(density: dict, leakage: dict, boundaries: dict) -> list[str]:
    DASH.mkdir(parents=True, exist_ok=True)
    records = density.get("records", [])
    density_lines = [
        "# Knowledge Density",
        "",
        "| Wiki | Group | Concepts | Rules | Workflows | Cases | Prompts | Eval Tests |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for record in records:
        c = record.get("counts", {})
        density_lines.append(f"| {record['wiki']} | {record.get('knowledge_density_group')} | {c.get('concepts',0)} | {c.get('rules',0)} | {c.get('workflows',0)} | {c.get('cases',0)} | {c.get('prompts',0)} | {record.get('eval_tests',0)} |")
    density_lines.extend(["", "## Optional Dataview", "```dataview", "TABLE wiki, risk, source_status FROM \"02_Knowledge/MOCs\"", "```"])
    (DASH / "Knowledge Density.md").write_text("\n".join(density_lines) + "\n", encoding="utf-8")

    current_lines = [
        "# Current Fact Gates",
        "",
        f"- Current-fact leakage audit passed: {leakage.get('passed', False)}",
        f"- Findings: {leakage.get('finding_count', 0)}",
        f"- Blocking findings: {leakage.get('blocking_count', 0)}",
        "",
        "Changing facts remain in source review until authoritative evidence and human gates pass.",
    ]
    (DASH / "Current Fact Gates.md").write_text("\n".join(current_lines) + "\n", encoding="utf-8")

    boundary_lines = [
        "# High Risk Boundaries",
        "",
        f"- Boundary audit passed: {boundaries.get('passed', False)}",
        f"- Pages checked: {len(boundaries.get('checks', []))}",
        "",
        "| Page | Human Gate | Source Gate |",
        "| --- | --- | --- |",
    ]
    for check in boundaries.get("checks", [])[:200]:
        boundary_lines.append(f"| {check['path']} | {check.get('has_human_gate')} | {check.get('has_source_gate')} |")
    (DASH / "High Risk Boundaries.md").write_text("\n".join(boundary_lines) + "\n", encoding="utf-8")

    human_lines = [
        "# Human Review Gates",
        "",
        "Human gates remain active for high-risk domains and current-fact promotion.",
        "",
        "- Finance: real-money or personalized output.",
        "- Legal: jurisdiction-specific or binding legal conclusion.",
        "- Health: diagnosis, dosage, or care decision.",
        "- Security: production control, secrets, or remediation impact.",
        "- NodeOps: production mutation, destructive command, rollback, or firewall change.",
        "- Customs: filing, declaration, classification, or high-risk discrepancy acceptance.",
        "- Airdrop: wallet signing, approvals, identity-sensitive tasks, or rule-sensitive automation.",
    ]
    (DASH / "Human Review Gates.md").write_text("\n".join(human_lines) + "\n", encoding="utf-8")
    return [
        "obsidian-vault/05_Dashboard/Knowledge Density.md",
        "obsidian-vault/05_Dashboard/Current Fact Gates.md",
        "obsidian-vault/05_Dashboard/High Risk Boundaries.md",
        "obsidian-vault/05_Dashboard/Human Review Gates.md",
    ]


def main() -> int:
    density = read_json(REGISTRY / "knowledge-density-report.json")
    leakage = read_json(REGISTRY / "current-fact-leakage-audit.json")
    boundaries = read_json(REGISTRY / "high-risk-boundary-audit.json")
    updated_mocs = []
    for path in sorted(MOCS.glob("*.md")):
        append_section(
            path,
            "## v2.1 Backlinks",
            [
                "- [[Knowledge Density]]",
                "- [[Current Fact Gates]]",
                "- [[Human Review Gates]]",
                "- [[High Risk Boundaries]]",
                "- [[Wiki Status]]",
                "- [[Source Review Status]]",
            ],
        )
        updated_mocs.append(path.relative_to(ROOT).as_posix())
    dashboards = write_dashboard_pages(density, leakage, boundaries)
    payload = {"generated": date.today().isoformat(), "passed": True, "updated_mocs": updated_mocs, "dashboards": dashboards}
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "obsidian-backlink-report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Obsidian Backlink Report", "", f"Generated: {payload['generated']}", "", f"- MOCs updated: {len(updated_mocs)}", f"- Dashboard pages: {len(dashboards)}"]
    (DOCS / "OBSIDIAN_BACKLINK_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OBSIDIAN BACKLINKS GENERATED ({len(updated_mocs)} MOCs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
