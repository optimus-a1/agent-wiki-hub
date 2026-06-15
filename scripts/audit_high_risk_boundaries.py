#!/usr/bin/env python3
"""Audit human/source gates in high-risk wiki pages."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"
HIGH_RISK = {"finance-agent-wiki", "legal-agent-wiki", "health-agent-wiki", "security-agent-wiki", "nodeops-agent-wiki", "airdrop-agent-wiki", "customs-agent-wiki"}
SCAN_DIRS = ["concepts", "rules", "workflows", "cases", "prompts"]


def main() -> int:
    checks = []
    wiki_checks = []
    warnings = []
    for wiki_id in sorted(HIGH_RISK):
        wiki = WIKIS / wiki_id
        wiki_text = "\n".join(
            (wiki / name).read_text(encoding="utf-8", errors="ignore").casefold()
            for name in ["AGENTS.md", "README.md", "manifest.yaml", "sources/source-notes.md"]
            if (wiki / name).exists()
        )
        wiki_has_human = "human" in wiki_text or "人工" in wiki_text
        wiki_has_source = "needs-source-update" in wiki_text or "source" in wiki_text
        wiki_checks.append({"wiki": wiki_id, "passed": wiki_has_human and wiki_has_source, "has_human_gate": wiki_has_human, "has_source_gate": wiki_has_source})
        for dirname in SCAN_DIRS:
            for path in (wiki / dirname).glob("*.md"):
                raw_text = path.read_text(encoding="utf-8", errors="ignore")
                text = raw_text.casefold()
                has_human = "## human gate" in text and ("human" in text or "clinician" in text or "lawyer" in text)
                has_source = "## source gate" in text and ("source review" in text or "needs-source-update" in text)
                is_v2_1 = "status: stable-general-knowledge" in text and "generated_by: codex" in text
                passed = has_human and has_source
                record = {"path": path.relative_to(ROOT).as_posix(), "wiki": wiki_id, "passed": passed, "has_human_gate": has_human, "has_source_gate": has_source, "v2_1_generated": is_v2_1}
                if is_v2_1:
                    checks.append(record)
                elif not passed:
                    warnings.append(record)
    failed = [check for check in checks if not check["passed"]]
    failed.extend([check for check in wiki_checks if not check["passed"]])
    payload = {"generated": date.today().isoformat(), "passed": not failed, "wiki_checks": wiki_checks, "checks": checks, "legacy_warnings": warnings}
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "high-risk-boundary-audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# High Risk Boundary Audit", "", f"Generated: {payload['generated']}", "", f"- Passed: {not failed}", f"- v2.1 pages checked: {len(checks)}", f"- Wiki-level checks: {len(wiki_checks)}", f"- Legacy warnings: {len(warnings)}", f"- Failed: {len(failed)}", "", "## Wiki-Level Gates", "", "| Wiki | Result | Human Gate | Source Gate |", "| --- | --- | --- | --- |"]
    for check in wiki_checks:
        lines.append(f"| {check['wiki']} | {'PASS' if check['passed'] else 'FAIL'} | {check['has_human_gate']} | {check['has_source_gate']} |")
    lines.extend(["", "## v2.1 Page Gates", "", "| Page | Result | Human Gate | Source Gate |", "| --- | --- | --- | --- |"])
    for check in checks:
        lines.append(f"| {check['path']} | {'PASS' if check['passed'] else 'FAIL'} | {check['has_human_gate']} | {check['has_source_gate']} |")
    lines.extend(["", "## Legacy Warnings", "", "Legacy pages without v2.1 gate headings are warnings. New generated high-risk pages remain blocking if gates are missing."])
    (DOCS / "HIGH_RISK_BOUNDARY_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"HIGH RISK BOUNDARY AUDIT {'PASSED' if not failed else 'FAILED'} ({len(checks)} pages)")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
