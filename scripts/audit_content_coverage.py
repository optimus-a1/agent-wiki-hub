#!/usr/bin/env python3
"""Audit required topic coverage for each Agent Wiki."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / "wikis"
DOCS_OUT = ROOT / "docs" / "COVERAGE_AUDIT.md"
JSON_OUT = ROOT / "registry" / "coverage-audit.json"

TOP_FILES = ("manifest.yaml", "README.md", "AGENTS.md")
SCAN_DIRS = ("concepts", "rules", "workflows", "cases", "tools", "prompts", "evals", "sources")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}


def topic(priority: str, topic_id: str, description: str, groups: list[list[str]]) -> dict:
    return {"priority": priority, "topic_id": topic_id, "description": description, "groups": groups}


COVERAGE = {
    "finance-agent-wiki": [
        topic("P0", "market_data_foundations", "OHLCV, order book, spread, volume, and liquidity.", [["OHLCV"], ["order book", "盘口"], ["spread", "价差"], ["volume", "成交量"], ["liquidity", "流动性"]]),
        topic("P0", "financial_analysis_foundations", "Income statement, balance sheet, cash flow, and valuation analysis.", [["利润表", "income statement"], ["资产负债表", "balance sheet"], ["现金流", "cash flow"], ["估值", "valuation"]]),
        topic("P0", "risk_control_framework", "Position, drawdown, leverage, liquidity, and operational risk.", [["position", "仓位"], ["drawdown", "回撤"], ["leverage", "杠杆"], ["liquidity", "流动性"], ["operational risk", "操作风险"]]),
        topic("P0", "backtesting_workflow", "Data quality, fees, slippage, out-of-sample tests, and overfitting checks.", [["data quality", "数据质量"], ["fees", "手续费"], ["slippage", "滑点"], ["out-of-sample", "样本外"], ["overfitting", "过拟合"]]),
        topic("P0", "trading_system_boundaries", "Paper trading defaults, human confirmation, logs, circuit breakers, and permissions.", [["paper trading", "模拟盘"], ["human confirmation", "人工确认"], ["logs", "日志"], ["circuit breaker", "熔断"], ["permission", "权限"]]),
        topic("P0", "finance_output_boundaries", "No personalized investment advice and no autonomous real-money execution.", [["personalized investment advice", "个人化投资建议"], ["real money", "真实资金"], ["autonomous", "自动执行", "默认执行"]]),
    ],
    "customs-agent-wiki": [
        topic("P0", "trade_document_types", "Contracts, invoices, packing lists, factory inspection sheets, and conformity/quality guarantees.", [["Contract", "合同"], ["Invoice", "发票"], ["Packing List", "装箱单"], ["Factory Inspection", "厂检"], ["Certificate of Conformity", "Quality Guarantee", "合格保证"]]),
        topic("P0", "field_mapping_rules", "English headers map to normalized Chinese/customs fields.", [["shipper", "seller", "exporter"], ["consignee", "buyer", "importer"], ["invoice no"], ["currency"], ["gross weight", "net weight"]]),
        topic("P0", "ocr_to_json", "OCR/text parsing into structured JSON with evidence and confidence.", [["OCR"], ["JSON"], ["evidence"], ["confidence", "置信度"]]),
        topic("P0", "document_difference_comparison", "Cross-document comparison outputs differences, risk levels, and manual review suggestions.", [["difference", "差异"], ["risk_level", "risk level", "风险等级"], ["review_suggestion", "人工复核", "manual review"]]),
        topic("P0", "customs_validation_rules", "Amount, currency, packages, gross/net weight, goods name, and specifications.", [["amount", "金额"], ["currency", "币制"], ["packages", "件数"], ["gross_weight", "gross weight", "毛重"], ["net_weight", "net weight", "净重"], ["description of goods", "品名"], ["specification", "规格"]]),
    ],
    "coding-agent-wiki": [
        topic("P0", "implementation_lifecycle", "Requirement clarification, minimal implementation, and testing-first workflow.", [["requirement clarification", "需求澄清"], ["minimal implementation", "最小实现"], ["testing-first", "测试先行"]]),
        topic("P0", "debug_flow", "Reproduce, observe, locate, minimally fix, test, and prevent regression.", [["Reproduce", "复现"], ["Locate", "定位"], ["Fix minimally", "最小修复"], ["regression", "回归"]]),
        topic("P0", "deployment_flow", "Deployment preflight, environment variables, health checks, monitoring, and rollback.", [["deployment", "部署"], ["environment", "环境变量"], ["health check", "健康检查"], ["monitoring", "监控"], ["rollback", "回滚"]]),
        topic("P0", "secure_development", "Secrets, permissions, input validation, logging, and dependency risk.", [["secret", "密钥"], ["permission", "权限"], ["input validation", "输入校验"], ["logging", "日志"], ["dependency", "依赖"]]),
        topic("P0", "codex_usage_rules", "Codex reads AGENTS.md, preserves user changes, scopes edits, and verifies.", [["Codex"], ["AGENTS.md"], ["user changes", "用户"], ["scoped edits", "最小改动"], ["verification", "验证"]]),
    ],
    "agent-engineering-wiki": [
        topic("P0", "agent_architecture", "Agent is model, tools, knowledge, workflow, memory, evals, and safety boundaries.", [["Model"], ["Tools"], ["Knowledge"], ["Workflow"], ["Memory"], ["Evals"], ["Safety"]]),
        topic("P0", "rag_pipeline", "RAG chunking, indexing, recall, reranking, citations, and evals.", [["chunk", "切块"], ["index", "索引"], ["recall", "召回"], ["rerank", "重排"], ["citation", "引用"], ["eval", "评测"]]),
        topic("P0", "knowledge_pack_standard", "Knowledge Pack includes manifest, rules, workflows, evals, sources, and update logs.", [["manifest"], ["rules"], ["workflows"], ["evals"], ["sources"], ["update-log"]]),
        topic("P0", "codex_skills", "Codex Skills cover SKILL.md, scripts, references, and assets.", [["SKILL.md"], ["scripts"], ["references"], ["assets"]]),
        topic("P0", "eval_design", "Evals include golden questions, behavior tests, and source-grounding tests.", [["golden questions"], ["behavior tests"], ["source-grounding"]]),
    ],
    "ecommerce-agent-wiki": [
        topic("P1", "product_catalog", "Product catalog, SKU, SPU, attributes, inventory, and price.", [["SKU"], ["SPU"], ["attribute", "属性"], ["inventory", "库存"], ["price", "价格"]]),
        topic("P1", "customer_service_returns", "Customer service, returns, refunds, logistics, and invoices.", [["customer service", "客服"], ["return", "退货"], ["refund", "退款"], ["logistics", "物流"], ["invoice", "发票"]]),
        topic("P1", "recommendation_rules", "Need clarification, constraint matching, comparison, and risk reminders.", [["recommend", "推荐"], ["需求", "need"], ["constraint", "约束"], ["compare", "对比"], ["risk", "风险"]]),
        topic("P1", "policy_privacy_freshness", "Platform policy, privacy, consumer protection, and current fact source updates.", [["platform policy", "平台政策"], ["privacy", "隐私"], ["consumer", "消费者"], ["needs-source-update"]]),
    ],
    "nodeops-agent-wiki": [
        topic("P1", "ops_domains", "Linux, Docker, systemd, logs, backup, monitoring, and alerts.", [["Linux"], ["Docker"], ["systemd"], ["logs", "日志"], ["backup", "备份"], ["monitor", "监控"], ["alert", "告警"]]),
        topic("P1", "production_change_safety", "Production changes require backup, human confirmation, rollback, and monitoring.", [["production", "生产"], ["backup", "备份"], ["human confirmation", "人工确认"], ["rollback", "回滚"], ["monitoring", "监控"]]),
        topic("P1", "incident_response", "Incident response uses symptoms, logs, resources, network, dependencies, and rollback.", [["incident", "故障"], ["symptom", "症状"], ["logs", "日志"], ["resource", "资源"], ["network", "网络"], ["dependency", "依赖"], ["rollback", "回滚"]]),
        topic("P1", "destructive_command_boundary", "Destructive operations are blocked until paths, backups, and confirmation are clear.", [["destructive", "破坏性"], ["delete", "删除"], ["backup", "备份"], ["confirmation", "确认"]]),
    ],
    "airdrop-agent-wiki": [
        topic("P1", "project_research", "Project research covers official links, docs, team, funding, ecosystem, and risk.", [["official", "官方"], ["documentation", "文档"], ["team", "团队"], ["funding", "融资"], ["ecosystem", "生态"], ["risk", "风险"]]),
        topic("P1", "wallet_safety", "Wallet safety includes signatures, authorization, phishing, permissions, and secret protection.", [["wallet", "钱包"], ["signature", "签名"], ["authorization", "授权"], ["phishing", "钓鱼"], ["permission", "权限"], ["private key", "私钥", "助记词"]]),
        topic("P1", "compliance_boundaries", "Refuses Sybil evasion, spam, fake identities, and platform-rule bypass.", [["Sybil", "女巫"], ["spam", "刷量"], ["fake identity", "假身份"], ["bypass", "绕平台规则", "规避"]]),
        topic("P1", "airdrop_freshness", "TGE, snapshot, eligibility, task rules, and project status require source updates.", [["TGE"], ["snapshot", "快照"], ["eligibility", "资格"], ["task rules", "任务规则"], ["needs-source-update"]]),
    ],
    "content-agent-wiki": [
        topic("P1", "content_formats", "Research briefs, reports, articles, long posts, short posts, titles, and summaries.", [["brief", "简报"], ["report", "日报"], ["article", "文章"], ["long", "长帖"], ["short", "短帖"], ["title", "标题"], ["summary", "摘要"]]),
        topic("P1", "fact_checking", "Fact checking, citations, no plagiarism, and current claims source updates.", [["fact", "事实"], ["citation", "引用"], ["plagiarism", "抄袭"], ["needs-source-update"]]),
        topic("P1", "publishing_checklist", "Style templates and publishing checklist with title, summary, tags, images, and citations.", [["style", "风格"], ["publish", "发布"], ["title", "标题"], ["tags"], ["images"], ["citations"]]),
    ],
    "legal-agent-wiki": [
        topic("P2", "contract_review", "Contract review covers parties, commercial terms, risk clauses, operations, and missing information.", [["contract", "合同"], ["parties", "主体"], ["commercial terms", "商业"], ["risk", "风险"], ["missing", "缺失"]]),
        topic("P2", "legal_boundaries", "No final legal opinion; lawyer or legal review is required.", [["final legal opinion", "最终法律意见"], ["lawyer", "律师"], ["legal review", "法务"]]),
        topic("P2", "current_law_freshness", "Jurisdiction, statutes, regulations, cases, and guidance require source updates.", [["jurisdiction", "司法辖区"], ["statutes", "法律条文"], ["regulations", "监管"], ["cases", "判例"], ["needs-source-update"]]),
        topic("P2", "privacy_data_terms", "Privacy, data processing, platform agreements, and consumer protection are covered.", [["privacy", "隐私"], ["data", "数据"], ["platform", "平台"], ["consumer", "消费者"]]),
    ],
    "health-agent-wiki": [
        topic("P2", "health_education_boundary", "Health education only; no diagnosis, no prescription, no doctor replacement.", [["health education", "健康科普"], ["diagnosis", "诊断"], ["prescription", "处方", "开药"], ["doctor", "医生"]]),
        topic("P2", "triage_red_flags", "Triage screens red flags, emergency risks, context, uncertainty, and care-seeking guidance.", [["triage", "分诊"], ["red flag", "红旗"], ["emergency", "急诊"], ["uncertainty", "不确定"], ["doctor", "医生"]]),
        topic("P2", "report_explanation", "Lab/report explanation includes indicators, factors, recheck, and clinician confirmation.", [["lab", "报告"], ["indicator", "指标"], ["factor", "因素"], ["recheck", "复查"], ["doctor", "医生"]]),
        topic("P2", "medical_freshness", "Guidelines, drug labels, dosage, contraindications, and public health advice require source updates.", [["guideline", "指南"], ["drug", "药品"], ["dosage", "剂量"], ["contraindication", "禁忌"], ["needs-source-update"]]),
    ],
    "research-agent-wiki": [
        topic("P2", "source_grounding", "Research claims need citations, traceability, datasets, experiments, and source updates.", [["citation", "引用"], ["traceability", "溯源"], ["dataset", "数据集"], ["experiment", "实验"], ["needs-source-update"]]),
        topic("P2", "paper_summary", "Paper summaries cover claims, methods, evidence, limitations, and reproducibility.", [["paper", "论文"], ["claim", "主张"], ["method", "方法"], ["limitation", "局限"], ["reproduc", "复现"]]),
        topic("P2", "benchmark_freshness", "Latest papers, citations, leaderboards, benchmark status, repositories, and licenses require source updates.", [["latest", "最新"], ["citation", "引用"], ["leaderboard", "榜单"], ["benchmark"], ["repository", "仓库"], ["license", "许可"]]),
    ],
    "security-agent-wiki": [
        topic("P2", "defensive_boundary", "Security wiki is defensive and authorization-scoped.", [["defensive", "防御"], ["authorization", "授权"], ["review", "审查"]]),
        topic("P2", "no_attack_steps", "Refuses exploit, payload, bypass, credential theft, persistence, and evasion steps.", [["exploit"], ["payload"], ["bypass", "绕过"], ["credential", "凭据"], ["persistence", "持久化"], ["evasion", "规避"]]),
        topic("P2", "threat_model_review", "Threat models cover assets, boundaries, data flows, risks, controls, and verification.", [["asset", "资产"], ["boundary", "边界"], ["data flow", "数据流"], ["risk", "风险"], ["control", "控制"], ["verification", "验证"]]),
        topic("P2", "security_freshness", "CVEs, advisories, patches, detection rules, dependency versions, and cloud defaults require source updates.", [["CVE"], ["advisory", "公告"], ["patch", "补丁"], ["detection", "检测"], ["dependency", "依赖"], ["needs-source-update"]]),
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def collect_files(wiki: Path) -> list[tuple[Path, str]]:
    files: list[Path] = []
    for name in TOP_FILES:
        path = wiki / name
        if path.exists():
            files.append(path)
    for dirname in SCAN_DIRS:
        folder = wiki / dirname
        if folder.exists():
            files.extend(sorted(path for path in folder.rglob("*") if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES))
    return [(path, read_text(path).casefold()) for path in sorted(set(files))]


def find_group(files: list[tuple[Path, str]], terms: list[str]) -> dict:
    lowered_terms = [(term, term.casefold()) for term in terms]
    for path, text in files:
        for original, lowered in lowered_terms:
            if lowered in text:
                return {"passed": True, "term": original, "path": path.relative_to(ROOT).as_posix()}
    return {"passed": False, "term": "", "path": "", "expected_any": terms}


def audit_topic(wiki_id: str, files: list[tuple[Path, str]], requirement: dict) -> dict:
    group_results = [find_group(files, group) for group in requirement["groups"]]
    missing = [result for result in group_results if not result["passed"]]
    return {
        "wiki": wiki_id,
        "priority": requirement["priority"],
        "topic_id": requirement["topic_id"],
        "description": requirement["description"],
        "passed": not missing,
        "groups": group_results,
        "missing_groups": missing,
    }


def audit() -> list[dict]:
    results: list[dict] = []
    for wiki_id, requirements in COVERAGE.items():
        wiki = WIKIS / wiki_id
        files = collect_files(wiki) if wiki.exists() else []
        for requirement in requirements:
            if not files:
                results.append({
                    "wiki": wiki_id,
                    "priority": requirement["priority"],
                    "topic_id": requirement["topic_id"],
                    "description": requirement["description"],
                    "passed": False,
                    "groups": [],
                    "missing_groups": [{"passed": False, "expected_any": ["wiki directory exists"], "term": "", "path": ""}],
                })
            else:
                results.append(audit_topic(wiki_id, files, requirement))
    return results


def evidence_summary(groups: list[dict]) -> str:
    hits = []
    for group in groups:
        if group["passed"]:
            hits.append(f"{group['term']} @ {group['path']}")
    return "<br>".join(hits) if hits else "-"


def missing_summary(groups: list[dict]) -> str:
    missing = []
    for group in groups:
        if not group["passed"]:
            missing.append(" / ".join(group.get("expected_any", [])))
    return "<br>".join(missing) if missing else "-"


def markdown_report(results: list[dict]) -> str:
    failed = [result for result in results if not result["passed"]]
    by_wiki = Counter(result["wiki"] for result in results)
    by_priority = Counter(result["priority"] for result in results)
    pass_by_priority = Counter(result["priority"] for result in results if result["passed"])

    lines = [
        "# Content Coverage Audit",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Required topics: {len(results)}",
        f"- Passed: {len(results) - len(failed)}",
        f"- Failed: {len(failed)}",
        "",
        "## Priority Summary",
        "",
        "| Priority | Passed | Total |",
        "| --- | ---: | ---: |",
    ]
    for priority in sorted(by_priority):
        lines.append(f"| {priority} | {pass_by_priority[priority]} | {by_priority[priority]} |")

    lines.extend(["", "## Wiki Summary", "", "| Wiki | Passed | Total |", "| --- | ---: | ---: |"])
    passed_by_wiki = Counter(result["wiki"] for result in results if result["passed"])
    for wiki in sorted(by_wiki):
        lines.append(f"| {wiki} | {passed_by_wiki[wiki]} | {by_wiki[wiki]} |")

    lines.extend([
        "",
        "## Topic Results",
        "",
        "| Wiki | Priority | Topic | Result | Evidence | Missing |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(
            f"| {result['wiki']} | {result['priority']} | {result['topic_id']} | {status} | "
            f"{evidence_summary(result['groups'])} | {missing_summary(result['groups'])} |"
        )
    lines.extend(
        [
            "",
            "## Usage Notes",
            "",
            "- This audit checks whether each wiki has searchable coverage for its required stable topics.",
            "- It is a keyword coverage gate, not a semantic guarantee; reviewers should still read the referenced pages for quality.",
            "- Current facts remain gated by `docs/SOURCE_UPDATE_QUEUE.md` and should not be filled in without authoritative verification.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    results = audit()
    failed = [result for result in results if not result["passed"]]
    DOCS_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUT.write_text(markdown_report(results), encoding="utf-8")
    JSON_OUT.write_text(
        json.dumps({"generated": date.today().isoformat(), "passed": not failed, "topics": results}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {DOCS_OUT.relative_to(ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    if failed:
        print("CONTENT COVERAGE AUDIT FAILED")
        for result in failed:
            print(f"- {result['wiki']}:{result['topic_id']} missing {missing_summary(result['groups']).replace('<br>', '; ')}")
        return 1
    print(f"CONTENT COVERAGE AUDIT PASSED ({len(results)} topics)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
