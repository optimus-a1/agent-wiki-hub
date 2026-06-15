#!/usr/bin/env python3
"""Audit v2.1 minimum knowledge density thresholds."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"

TARGETS = {
    "customs-agent-wiki": dict(concepts=10, rules=8, workflows=6, cases=6, prompts=4, eval_tests=10),
    "nodeops-agent-wiki": dict(concepts=12, rules=8, workflows=8, cases=6, prompts=4, eval_tests=10),
    "airdrop-agent-wiki": dict(concepts=10, rules=8, workflows=6, cases=6, prompts=4, eval_tests=10),
    "finance-agent-wiki": dict(concepts=12, rules=10, workflows=8, cases=6, prompts=4, eval_tests=12),
    "coding-agent-wiki": dict(concepts=10, rules=8, workflows=8, cases=5, prompts=4, eval_tests=10),
    "agent-engineering-wiki": dict(concepts=12, rules=8, workflows=8, cases=5, prompts=6, eval_tests=10),
    "security-agent-wiki": dict(concepts=10, rules=10, workflows=8, cases=6, prompts=4, eval_tests=10),
    "research-agent-wiki": dict(concepts=10, rules=8, workflows=6, cases=5, prompts=4, eval_tests=10),
    "ecommerce-agent-wiki": dict(concepts=8, rules=6, workflows=5, cases=4, prompts=3, eval_tests=8),
    "content-agent-wiki": dict(concepts=8, rules=6, workflows=5, cases=4, prompts=4, eval_tests=8),
    "legal-agent-wiki": dict(concepts=6, rules=6, workflows=4, cases=4, prompts=3, eval_tests=6),
    "health-agent-wiki": dict(concepts=6, rules=6, workflows=4, cases=4, prompts=3, eval_tests=6),
}


def ensure_report() -> dict:
    report = REGISTRY / "knowledge-density-report.json"
    if not report.exists():
        subprocess.run([sys.executable, "scripts/generate_knowledge_density_report.py"], cwd=ROOT, check=True)
    return json.loads(report.read_text(encoding="utf-8"))


def main() -> int:
    report = ensure_report()
    records = {record["wiki"]: record for record in report.get("records", [])}
    checks = []
    for wiki, target in TARGETS.items():
        record = records.get(wiki, {})
        counts = record.get("counts", {})
        issues = []
        for area in ["concepts", "rules", "workflows", "cases", "prompts"]:
            actual = int(counts.get(area, 0))
            if actual < target[area]:
                issues.append(f"{area}: {actual} < {target[area]}")
        eval_tests = int(record.get("eval_tests", 0))
        if eval_tests < target["eval_tests"]:
            issues.append(f"eval_tests: {eval_tests} < {target['eval_tests']}")
        checks.append({"wiki": wiki, "passed": not issues, "issues": issues, "target": target, "actual": {**counts, "eval_tests": eval_tests}})
    failed = [check for check in checks if not check["passed"]]
    payload = {"generated": date.today().isoformat(), "passed": not failed, "checks": checks}
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "knowledge-density-audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Knowledge Density Audit", "", f"Generated: {payload['generated']}", "", f"- Passed: {not failed}", "", "| Wiki | Result | Issues |", "| --- | --- | --- |"]
    for check in checks:
        lines.append(f"| {check['wiki']} | {'PASS' if check['passed'] else 'FAIL'} | {'; '.join(check['issues']) or '-'} |")
    (DOCS / "KNOWLEDGE_DENSITY_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"KNOWLEDGE DENSITY AUDIT {'PASSED' if not failed else 'FAILED'} ({len(checks)} wikis)")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
