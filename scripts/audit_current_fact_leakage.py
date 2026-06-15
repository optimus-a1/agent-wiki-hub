#!/usr/bin/env python3
"""Audit stable wiki pages for unsafe current-fact leakage."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS = ROOT / "docs"
REGISTRY = ROOT / "registry"
SCAN_DIRS = ["concepts", "rules", "workflows", "cases", "prompts"]
HIGH_RISK = {"finance-agent-wiki", "legal-agent-wiki", "health-agent-wiki", "security-agent-wiki", "nodeops-agent-wiki", "airdrop-agent-wiki", "customs-agent-wiki"}
RISK_PATTERNS = [
    "current version", "latest price", "current fee", "current law", "current regulation",
    "live market", "today's", "now available", "newly released", "cve currently",
    "exchange listing", "tge date", "airdrop snapshot", "current hs code", "current tax rate",
]
GATE_TERMS = ["source review", "source gate", "requires source review", "needs-source-update", "do not", "not write", "no current facts"]


def frontmatter(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return fields
    parts = text.split("---", 2)
    if len(parts) < 3:
        return fields
    for raw in parts[1].splitlines():
        if ":" in raw:
            key, value = raw.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def gated_context(text: str, index: int) -> bool:
    start = max(0, index - 180)
    end = min(len(text), index + 220)
    window = text[start:end].casefold()
    return any(term in window for term in GATE_TERMS)


def main() -> int:
    findings = []
    blocking = []
    for wiki in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        for dirname in SCAN_DIRS:
            for path in (wiki / dirname).glob("*.md"):
                text = path.read_text(encoding="utf-8", errors="ignore")
                lower = text.casefold()
                fields = frontmatter(text)
                page_findings = []
                for pattern in RISK_PATTERNS:
                    idx = lower.find(pattern)
                    if idx >= 0:
                        gated = gated_context(lower, idx) or fields.get("requires_source_review") == "true"
                        item = {"pattern": pattern, "gated": gated}
                        page_findings.append(item)
                        if wiki.name in HIGH_RISK and not gated:
                            blocking.append({"path": path.relative_to(ROOT).as_posix(), **item})
                if page_findings:
                    findings.append({"path": path.relative_to(ROOT).as_posix(), "findings": page_findings})
                if fields.get("current_fact", "").casefold() == "true" and fields.get("source_status") != "verified":
                    blocking.append({"path": path.relative_to(ROOT).as_posix(), "pattern": "current_fact true without verified source", "gated": False})
    payload = {"generated": date.today().isoformat(), "passed": not blocking, "finding_count": len(findings), "blocking_count": len(blocking), "findings": findings, "blocking": blocking}
    DOCS.mkdir(parents=True, exist_ok=True)
    REGISTRY.mkdir(parents=True, exist_ok=True)
    (REGISTRY / "current-fact-leakage-audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Current Fact Leakage Audit", "", f"Generated: {payload['generated']}", "", f"- Passed: {not blocking}", f"- Findings: {len(findings)}", f"- Blocking: {len(blocking)}", "", "| Path | Patterns |", "| --- | --- |"]
    for finding in findings[:200]:
        patterns = ", ".join(f"{x['pattern']} ({'gated' if x['gated'] else 'ungated'})" for x in finding["findings"])
        lines.append(f"| {finding['path']} | {patterns} |")
    (DOCS / "CURRENT_FACT_LEAKAGE_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"CURRENT FACT LEAKAGE AUDIT {'PASSED' if not blocking else 'FAILED'} ({len(findings)} findings, {len(blocking)} blocking)")
    return 0 if not blocking else 1


if __name__ == "__main__":
    raise SystemExit(main())
