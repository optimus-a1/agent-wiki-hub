#!/usr/bin/env python3
"""Audit safety boundaries for Agent Wiki Hub knowledge packs."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS_OUT = ROOT / "docs" / "SAFETY_AUDIT.md"
JSON_OUT = ROOT / "registry" / "safety-audit.json"

TOP_FILES = ("manifest.yaml", "README.md", "AGENTS.md", "update-log.md")
SCAN_DIRS = (
    "concepts",
    "rules",
    "workflows",
    "cases",
    "tools",
    "prompts",
    "evals",
    "sources",
)
HIGH_AND_MEDIUM = {"high", "medium"}

CN = {
    "human_confirmation": "\u4eba\u5de5\u786e\u8ba4",
    "human_review": "\u4eba\u5de5\u590d\u6838",
    "lawyer_confirmation": "\u5f8b\u5e08\u786e\u8ba4",
    "doctor_confirmation": "\u533b\u751f\u786e\u8ba4",
    "pharmacist_confirmation": "\u836f\u5e08\u786e\u8ba4",
    "no_sensitive_credentials": "\u4e0d\u4fdd\u5b58\u654f\u611f\u51ed\u636e",
    "secret": "\u5bc6\u94a5",
    "private_key": "\u79c1\u94a5",
    "credential": "\u51ed\u636e",
    "personalized_investment_advice": "\u4e2a\u4eba\u5316\u6295\u8d44\u5efa\u8bae",
    "real_money": "\u771f\u5b9e\u8d44\u91d1",
    "real_trade": "\u771f\u5b9e\u4ea4\u6613",
    "paper_trading": "\u6a21\u62df\u76d8",
    "position": "\u4ed3\u4f4d",
    "drawdown": "\u56de\u64a4",
    "leverage": "\u6760\u6746",
    "liquidity": "\u6d41\u52a8\u6027",
    "circuit_breaker": "\u7194\u65ad",
    "backup": "\u5907\u4efd",
    "rollback": "\u56de\u6eda",
    "delete": "\u5220\u9664",
    "format": "\u683c\u5f0f\u5316",
    "drop_database": "\u6e05\u5e93",
    "destructive": "\u7834\u574f\u6027",
    "unconfirmed": "\u672a\u786e\u8ba4",
    "sybil_cn": "\u5973\u5deb",
    "spam_volume": "\u5237\u91cf",
    "bulk_accounts": "\u6279\u91cf\u53f7",
    "fake_identity": "\u5047\u8eab\u4efd",
    "platform_bypass": "\u7ed5\u5e73\u53f0\u89c4\u5219",
    "avoidance": "\u89c4\u907f",
    "mnemonic": "\u52a9\u8bb0\u8bcd",
    "verification_code": "\u9a8c\u8bc1\u7801",
    "airdrop": "\u7a7a\u6295",
    "snapshot": "\u5feb\u7167",
    "final_legal_opinion": "\u6700\u7ec8\u6cd5\u5f8b\u610f\u89c1",
    "not_final": "\u4e0d\u505a\u6700\u7ec8",
    "jurisdiction": "\u53f8\u6cd5\u8f96\u533a",
    "legal_text": "\u6cd5\u5f8b\u6761\u6587",
    "precedent": "\u5224\u4f8b",
    "no_diagnosis": "\u4e0d\u8bca\u65ad",
    "no_prescribing": "\u4e0d\u5f00\u836f",
    "prescription": "\u5904\u65b9",
    "red_flag": "\u7ea2\u65d7",
    "emergency": "\u6025\u8bca",
    "seek_care": "\u5c31\u533b",
    "defense": "\u9632\u5fa1",
    "authorization": "\u6388\u6743",
    "attack": "\u653b\u51fb",
    "bypass": "\u7ed5\u8fc7",
    "theft": "\u76d7\u53d6",
    "exploit_steps": "\u5229\u7528\u6b65\u9aa4",
    "persistence": "\u6301\u4e45\u5316",
    "evasion": "\u89c4\u907f\u68c0\u6d4b",
    "credential_theft": "\u51ed\u636e\u76d7\u53d6",
    "log": "\u65e5\u5fd7",
    "vulnerability": "\u6f0f\u6d1e",
    "patch": "\u8865\u4e01",
    "regulation": "\u76d1\u7ba1",
    "document": "\u5355\u8bc1",
    "difference": "\u5dee\u5f02",
    "risk_level": "\u98ce\u9669\u7b49\u7ea7",
    "env_var": "\u73af\u5883\u53d8\u91cf",
    "test": "\u6d4b\u8bd5",
    "deploy": "\u90e8\u7f72",
    "permission": "\u6743\u9650",
    "knowledge_pack": "\u77e5\u8bc6\u5305",
    "citation": "\u5f15\u7528",
    "eval": "\u8bc4\u6d4b",
    "source": "\u6765\u6e90",
    "privacy": "\u9690\u79c1",
    "consumer": "\u6d88\u8d39\u8005",
    "platform_policy": "\u5e73\u53f0\u653f\u7b56",
    "paper": "\u8bba\u6587",
    "citation_count": "\u5f15\u7528\u6570",
    "traceability": "\u6eaf\u6e90",
}

HUMAN_TERMS = [
    "human confirmation",
    "human review",
    "manual review",
    CN["human_confirmation"],
    CN["human_review"],
    CN["lawyer_confirmation"],
    CN["doctor_confirmation"],
    CN["pharmacist_confirmation"],
]

SECRET_TERMS = [
    "no_secret_storage",
    "secret",
    "api key",
    "private key",
    "cookie",
    "token",
    "credential",
    CN["no_sensitive_credentials"],
    CN["secret"],
    CN["private_key"],
    CN["credential"],
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw in read_text(path).splitlines():
        if ":" not in raw or raw.startswith(" ") or raw.lstrip().startswith("-"):
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def collect_text(wiki: Path) -> str:
    parts: list[str] = []
    for name in TOP_FILES:
        path = wiki / name
        if path.exists():
            parts.append(read_text(path))
    for dirname in SCAN_DIRS:
        folder = wiki / dirname
        if folder.exists():
            for path in sorted(p for p in folder.rglob("*") if p.is_file()):
                if path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".txt"}:
                    parts.append(read_text(path))
    return "\n".join(parts).casefold()


def has_any(text: str, terms: list[str]) -> bool:
    return any(term.casefold() in text for term in terms)


def matched_group_count(text: str, groups: list[list[str]]) -> int:
    return sum(1 for group in groups if has_any(text, group))


def text_check(
    wiki_id: str,
    risk: str,
    check_id: str,
    description: str,
    text: str,
    groups: list[list[str]],
    required: bool = True,
) -> dict:
    matched = matched_group_count(text, groups)
    return {
        "wiki": wiki_id,
        "risk_level": risk,
        "check_id": check_id,
        "description": description,
        "required": required,
        "passed": matched == len(groups),
        "evidence": f"matched {matched}/{len(groups)} required term groups",
    }


def boolean_check(
    wiki_id: str,
    risk: str,
    check_id: str,
    description: str,
    passed: bool,
    evidence: str,
    required: bool = True,
) -> dict:
    return {
        "wiki": wiki_id,
        "risk_level": risk,
        "check_id": check_id,
        "description": description,
        "required": required,
        "passed": passed,
        "evidence": evidence,
    }


def rules_before_workflows(agents_text: str) -> tuple[bool, str]:
    text = agents_text.casefold()
    rules_idx = text.find("rules/")
    workflows_idx = text.find("workflows/")
    passed = rules_idx >= 0 and workflows_idx >= 0 and rules_idx < workflows_idx
    return passed, f"rules index={rules_idx}, workflows index={workflows_idx}"


def domain_checks(wiki_id: str) -> list[tuple[str, str, list[list[str]]]]:
    checks = {
        "finance-agent-wiki": [
            (
                "finance_no_personalized_advice",
                "Refuses personalized investment advice.",
                [["personalized investment advice", CN["personalized_investment_advice"]]],
            ),
            (
                "finance_no_real_money_autonomy",
                "Blocks autonomous real-money trading.",
                [[CN["real_money"], "real-money"], [CN["real_trade"], "live trading", "autonomous"]],
            ),
            (
                "finance_paper_trading_default",
                "Uses paper trading or simulation as the default.",
                [[CN["paper_trading"], "paper trading", "simulation"]],
            ),
            (
                "finance_risk_controls",
                "Covers position, drawdown, leverage, liquidity, and circuit breakers.",
                [
                    [CN["position"], "position"],
                    [CN["drawdown"], "drawdown"],
                    [CN["leverage"], "leverage"],
                    [CN["liquidity"], "liquidity"],
                    [CN["circuit_breaker"], "circuit breaker"],
                ],
            ),
        ],
        "customs-agent-wiki": [
            (
                "customs_document_diff_controls",
                "Covers document extraction, differences, risk levels, and manual review.",
                [
                    [CN["document"], "invoice", "packing list"],
                    [CN["difference"], "diff"],
                    [CN["risk_level"], "risk level"],
                    [CN["human_review"], "manual review"],
                ],
            ),
            (
                "customs_regulatory_freshness",
                "Marks trade policy, HS code, and regulatory facts for source updates.",
                [["hs", CN["regulation"], "regulatory"], ["needs-source-update"]],
            ),
        ],
        "coding-agent-wiki": [
            (
                "coding_secret_and_permission_boundary",
                "Covers secrets, environment variables, and least privilege.",
                [
                    SECRET_TERMS,
                    [CN["env_var"], "environment variable"],
                    [CN["permission"], "permission", "least privilege"],
                ],
            ),
            (
                "coding_deploy_safety",
                "Requires tests, deployment checks, rollback, and human confirmation.",
                [
                    [CN["test"], "test"],
                    [CN["deploy"], "deploy"],
                    [CN["rollback"], "rollback"],
                    HUMAN_TERMS,
                ],
            ),
        ],
        "agent-engineering-wiki": [
            (
                "agent_pack_quality_controls",
                "Covers knowledge pack structure, sources, evals, and citations.",
                [
                    [CN["knowledge_pack"], "knowledge pack", "manifest"],
                    [CN["source"], "source"],
                    [CN["eval"], "eval"],
                    [CN["citation"], "citation"],
                ],
            ),
            (
                "agent_high_risk_boundaries",
                "Requires human confirmation and refusal boundaries for high-risk packs.",
                [HUMAN_TERMS, ["boundary", "refusal", "no_autonomous_high_risk_execution"]],
            ),
        ],
        "ecommerce-agent-wiki": [
            (
                "ecommerce_policy_and_privacy",
                "Covers platform policy freshness, privacy, consumer protection, and review.",
                [
                    [CN["platform_policy"], "platform policy", "policy"],
                    [CN["privacy"], "privacy"],
                    [CN["consumer"], "consumer"],
                    HUMAN_TERMS,
                ],
            ),
        ],
        "nodeops-agent-wiki": [
            (
                "nodeops_change_safety",
                "Requires backup, rollback, monitoring, and human confirmation for production changes.",
                [
                    [CN["backup"], "backup"],
                    [CN["rollback"], "rollback"],
                    ["monitor", "alert"],
                    HUMAN_TERMS,
                ],
            ),
            (
                "nodeops_destructive_boundary",
                "Blocks unconfirmed destructive operations.",
                [
                    [CN["delete"], CN["format"], CN["drop_database"], CN["destructive"], "destructive"],
                    [CN["unconfirmed"], "unconfirmed", "without confirmation"],
                ],
            ),
        ],
        "airdrop-agent-wiki": [
            (
                "airdrop_no_sybil_or_spam",
                "Refuses Sybil evasion, spam, fake identity, and platform-rule bypass.",
                [
                    ["sybil", CN["sybil_cn"]],
                    [CN["spam_volume"], "spam"],
                    [CN["fake_identity"], "fake identity"],
                    [CN["platform_bypass"], CN["avoidance"], "bypass"],
                ],
            ),
            (
                "airdrop_wallet_secret_protection",
                "Protects wallet secrets and requires user confirmation before signatures.",
                [
                    [CN["private_key"], "private key"],
                    [CN["mnemonic"], "seed phrase"],
                    ["cookie", CN["verification_code"]],
                    HUMAN_TERMS,
                ],
            ),
            (
                "airdrop_current_rule_freshness",
                "Marks TGE, snapshot, task, and eligibility facts as source-update topics.",
                [["tge", CN["airdrop"], CN["snapshot"]], ["needs-source-update"]],
            ),
        ],
        "legal-agent-wiki": [
            (
                "legal_no_final_opinion",
                "Avoids final legal opinions and requires lawyer or legal review.",
                [
                    [CN["final_legal_opinion"], CN["not_final"], "final legal opinion"],
                    [CN["lawyer_confirmation"], "lawyer", "legal review"],
                ],
            ),
            (
                "legal_current_law_freshness",
                "Marks jurisdiction, statutes, cases, and regulations for source updates.",
                [
                    [CN["jurisdiction"], "jurisdiction"],
                    [CN["legal_text"], "statute", CN["precedent"]],
                    ["needs-source-update"],
                ],
            ),
        ],
        "health-agent-wiki": [
            (
                "health_no_diagnosis_or_prescription",
                "Avoids diagnosis and prescribing; requires clinician confirmation.",
                [
                    [CN["no_diagnosis"], "no diagnosis", "diagnosis"],
                    [CN["no_prescribing"], CN["prescription"], "prescription"],
                    [CN["doctor_confirmation"], CN["pharmacist_confirmation"], "doctor", "pharmacist"],
                ],
            ),
            (
                "health_red_flags_and_care",
                "Covers red flags and care-seeking guidance.",
                [[CN["red_flag"], "red flag"], [CN["seek_care"], CN["emergency"], "emergency"]],
            ),
        ],
        "research-agent-wiki": [
            (
                "research_source_grounding",
                "Requires citation, traceability, and source updates for current research claims.",
                [
                    [CN["citation"], "citation"],
                    [CN["traceability"], "trace"],
                    [CN["paper"], "paper"],
                    ["needs-source-update"],
                ],
            ),
        ],
        "security-agent-wiki": [
            (
                "security_defensive_only",
                "Keeps the pack defensive and authorization-scoped.",
                [[CN["defense"], "defensive"], [CN["authorization"], "authorization", "authorized"]],
            ),
            (
                "security_no_attack_steps",
                "Refuses exploit, bypass, theft, persistence, and evasion steps.",
                [
                    [CN["attack"], "attack"],
                    [CN["bypass"], "bypass"],
                    [CN["theft"], CN["credential_theft"], "theft"],
                    [CN["exploit_steps"], "exploit"],
                    [CN["persistence"], "persistence"],
                    [CN["evasion"], "evasion"],
                ],
            ),
            (
                "security_secret_and_log_boundary",
                "Protects secrets and logs from credential leakage.",
                [SECRET_TERMS, [CN["log"], "log"]],
            ),
            (
                "security_vulnerability_freshness",
                "Marks vulnerability, CVE, patch, and detection facts for source updates.",
                [[CN["vulnerability"], "cve", "vulnerability"], [CN["patch"], "patch"], ["needs-source-update"]],
            ),
        ],
    }
    return checks.get(wiki_id, [])


def audit_wiki(wiki: Path) -> list[dict]:
    manifest = parse_manifest(wiki / "manifest.yaml")
    wiki_id = manifest.get("id", wiki.name)
    risk = manifest.get("risk_level", "unknown")
    text = collect_text(wiki)
    manifest_raw = read_text(wiki / "manifest.yaml").casefold() if (wiki / "manifest.yaml").exists() else ""
    agents_text = read_text(wiki / "AGENTS.md") if (wiki / "AGENTS.md").exists() else ""
    source_notes = wiki / "sources" / "source-notes.md"

    required = risk in HIGH_AND_MEDIUM
    checks: list[dict] = []
    safety_flags = [
        "require_human_confirmation_for_high_risk: true",
        "no_secret_storage: true",
        "no_autonomous_high_risk_execution: true",
    ]
    flags_present = all(flag in manifest_raw for flag in safety_flags)
    checks.append(
        boolean_check(
            wiki_id,
            risk,
            "manifest_safety_flags",
            "Manifest declares human confirmation, no secret storage, and no autonomous high-risk execution.",
            flags_present,
            f"{sum(1 for flag in safety_flags if flag in manifest_raw)}/{len(safety_flags)} safety flags found",
            required=required,
        )
    )
    checks.append(
        boolean_check(
            wiki_id,
            risk,
            "source_notes_queue",
            "Source notes record current facts as needs-source-update.",
            source_notes.exists() and "needs-source-update" in read_text(source_notes).casefold(),
            f"{source_notes.relative_to(ROOT).as_posix()} checked",
            required=required,
        )
    )
    checks.append(
        text_check(
            wiki_id,
            risk,
            "human_confirmation_points",
            "Wiki text includes human confirmation or manual review points.",
            text,
            [HUMAN_TERMS],
            required=required,
        )
    )
    checks.append(
        text_check(
            wiki_id,
            risk,
            "secret_storage_boundary",
            "Wiki text includes a boundary for secrets, credentials, tokens, or private keys.",
            text,
            [SECRET_TERMS],
            required=required,
        )
    )
    if risk == "high":
        passed, evidence = rules_before_workflows(agents_text)
        checks.append(
            boolean_check(
                wiki_id,
                risk,
                "high_risk_rules_before_workflows",
                "High-risk AGENTS.md reads rules/ before workflows/.",
                passed,
                evidence,
            )
        )
    for check_id, description, groups in domain_checks(wiki_id):
        checks.append(text_check(wiki_id, risk, check_id, description, text, groups, required=required))
    return checks


def markdown_report(checks: list[dict]) -> str:
    required_checks = [check for check in checks if check["required"]]
    failed = [check for check in required_checks if not check["passed"]]
    audited_wikis = sorted({check["wiki"] for check in checks})
    high_medium_wikis = sorted({check["wiki"] for check in required_checks})
    lines = [
        "# Safety Boundary Audit",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Wikis scanned: {len(audited_wikis)}",
        f"- High/medium risk wikis with required checks: {len(high_medium_wikis)}",
        f"- Required checks: {len(required_checks)}",
        f"- Failed required checks: {len(failed)}",
        "",
        "## Required Check Results",
        "",
        "| Wiki | Risk | Check | Result | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for check in required_checks:
        result = "PASS" if check["passed"] else "FAIL"
        lines.append(
            f"| {check['wiki']} | {check['risk_level']} | {check['check_id']} | "
            f"{result} | {check['evidence']} |"
        )
    low_risk_checks = [check for check in checks if not check["required"]]
    if low_risk_checks:
        lines.extend(["", "## Informational Low-Risk Checks", "", "| Wiki | Check | Result |", "| --- | --- | --- |"])
        for check in low_risk_checks:
            result = "PASS" if check["passed"] else "INFO"
            lines.append(f"| {check['wiki']} | {check['check_id']} | {result} |")
    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- Treat this as a structural safety audit, not a substitute for legal, medical, financial, security, or compliance review.",
            "- Failed required checks mean the pack needs clearer safety boundaries before it should be used for high-risk workflows.",
            "- Current facts still require authoritative source verification through `docs/SOURCE_UPDATE_QUEUE.md`.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    if not WIKIS.exists():
        print("SAFETY AUDIT FAILED")
        print("- Missing wikis/ directory")
        return 1

    checks: list[dict] = []
    for wiki in sorted(p for p in WIKIS.iterdir() if p.is_dir()):
        checks.extend(audit_wiki(wiki))

    required_checks = [check for check in checks if check["required"]]
    failed = [check for check in required_checks if not check["passed"]]

    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(checks), encoding="utf-8")
    JSON_OUT.write_text(
        json.dumps(
            {
                "generated": date.today().isoformat(),
                "passed": not failed,
                "checks": checks,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if failed:
        print("SAFETY AUDIT FAILED")
        for check in failed:
            print(f"- {check['wiki']}: {check['check_id']} ({check['evidence']})")
        return 1
    print(f"SAFETY AUDIT PASSED ({len(required_checks)} required checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
