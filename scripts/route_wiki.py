#!/usr/bin/env python3
"""Route a user query to the most relevant Agent Wiki."""
from __future__ import annotations

from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CARDS_PATH = ROOT / "registry" / "agent-routing-cards.json"

DOMAIN_ALIASES = {
    "finance-agent-wiki": [
        "finance",
        "market data",
        "ohlcv",
        "order book",
        "spread",
        "volume",
        "liquidity",
        "financial statements",
        "income statement",
        "balance sheet",
        "cash flow",
        "valuation",
        "backtest",
        "paper trading",
        "risk control",
        "portfolio",
        "leverage",
        "drawdown",
        "investment",
        "trading",
        "金融",
        "投资",
        "风控",
        "回测",
        "模拟盘",
        "财报",
        "估值",
    ],
    "customs-agent-wiki": [
        "customs",
        "trade document",
        "invoice",
        "packing list",
        "contract",
        "factory inspection",
        "guarantee",
        "field extraction",
        "ocr",
        "document diff",
        "amount",
        "currency",
        "gross weight",
        "net weight",
        "hs code",
        "报关",
        "单证",
        "发票",
        "装箱单",
        "字段抽取",
        "差异比对",
        "毛重",
        "净重",
    ],
    "coding-agent-wiki": [
        "coding",
        "programming",
        "software engineering",
        "debug",
        "test first",
        "deployment",
        "secret management",
        "codex",
        "api",
        "database",
        "github",
        "requirements",
        "minimal implementation",
        "代码",
        "编程",
        "调试",
        "测试",
        "部署",
        "密钥",
    ],
    "agent-engineering-wiki": [
        "agent",
        "rag",
        "knowledge pack",
        "codex skill",
        "skill.md",
        "mcp",
        "eval",
        "source grounding",
        "chunking",
        "reranking",
        "workflow",
        "memory",
        "知识包",
        "评测",
        "工作流",
        "引用",
    ],
    "ecommerce-agent-wiki": [
        "ecommerce",
        "product catalog",
        "sku",
        "spu",
        "returns",
        "refund",
        "customer service",
        "recommendation",
        "inventory",
        "shipping",
        "marketplace",
        "电商",
        "商品",
        "客服",
        "退货",
        "物流",
        "库存",
    ],
    "nodeops-agent-wiki": [
        "nodeops",
        "operations",
        "linux",
        "docker",
        "systemd",
        "logs",
        "monitoring",
        "backup",
        "rollback",
        "server",
        "blockchain node",
        "rpc",
        "服务器",
        "节点",
        "日志",
        "监控",
        "备份",
        "回滚",
    ],
    "airdrop-agent-wiki": [
        "airdrop",
        "web3",
        "wallet",
        "signing",
        "token",
        "tge",
        "eligibility",
        "snapshot",
        "sybil",
        "public tasks",
        "空投",
        "钱包",
        "签名",
        "代币",
        "项目研究",
    ],
    "content-agent-wiki": [
        "content",
        "newsletter",
        "post",
        "article",
        "brief",
        "summary",
        "title",
        "citation",
        "fact checking",
        "publishing",
        "内容",
        "写作",
        "文章",
        "标题",
        "摘要",
        "事实核查",
    ],
    "legal-agent-wiki": [
        "legal",
        "contract",
        "clause",
        "agreement",
        "compliance",
        "jurisdiction",
        "lawyer",
        "legal review",
        "法律",
        "合同",
        "条款",
        "法务",
        "合规",
    ],
    "health-agent-wiki": [
        "health",
        "medical",
        "wellness",
        "symptom",
        "drug",
        "clinical",
        "guideline",
        "diagnosis",
        "clinician",
        "red flags",
        "健康",
        "医疗",
        "症状",
        "药品",
        "医生",
        "诊断",
    ],
    "research-agent-wiki": [
        "research",
        "paper",
        "literature review",
        "citation",
        "dataset",
        "benchmark",
        "experiment",
        "method",
        "evidence",
        "论文",
        "研究",
        "综述",
        "引用",
        "数据集",
    ],
    "security-agent-wiki": [
        "security",
        "defensive security",
        "hardening",
        "vulnerability",
        "cve",
        "incident",
        "audit",
        "permission",
        "secret",
        "bypass",
        "exploit",
        "credential",
        "安全",
        "防御",
        "漏洞",
        "审计",
        "权限",
    ],
}

SOURCE_UPDATE_TERMS = [
    "latest",
    "current",
    "today",
    "now",
    "real-time",
    "live",
    "price",
    "rate",
    "fee",
    "policy",
    "law",
    "regulation",
    "rule",
    "api",
    "sdk",
    "version",
    "cve",
    "advisory",
    "patch",
    "guideline",
    "drug",
    "tge",
    "eligibility",
    "snapshot",
    "benchmark",
    "leaderboard",
    "tariff",
    "hs code",
    "最新",
    "当前",
    "今天",
    "实时",
    "价格",
    "费率",
    "政策",
    "法规",
    "规则",
    "版本",
    "漏洞",
    "指南",
    "药品",
]

HIGH_RISK_TERMS = [
    "real money",
    "execute trade",
    "private key",
    "seed phrase",
    "cookie",
    "token",
    "bypass",
    "exploit",
    "steal",
    "credential",
    "diagnose",
    "prescribe",
    "legal opinion",
    "delete production",
    "真实资金",
    "私钥",
    "助记词",
    "绕过",
    "攻击",
    "盗取",
    "诊断",
    "处方",
    "法律意见",
]

TOKEN_STOPWORDS = {
    "and",
    "the",
    "for",
    "with",
    "from",
    "into",
    "list",
    "status",
    "task",
    "tasks",
    "check",
    "review",
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def tokens(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9_.-]+", text.casefold())
        if len(token) >= 3 and token not in TOKEN_STOPWORDS
    ]


def load_cards() -> list[dict]:
    if not CARDS_PATH.exists():
        raise FileNotFoundError(
            "registry/agent-routing-cards.json is missing. Run scripts/generate_agent_routing_cards.py first."
        )
    data = json.loads(CARDS_PATH.read_text(encoding="utf-8"))
    return list(data.get("cards", []))


def card_haystack(card: dict) -> str:
    fields: list[str] = [
        card.get("id", ""),
        card.get("name", ""),
        card.get("domain", ""),
        card.get("summary", ""),
        " ".join(card.get("trigger_keywords", [])),
        " ".join(card.get("example_intents", [])),
        " ".join(card.get("safety_rules", [])),
        " ".join(card.get("prohibited_actions", [])),
        " ".join(DOMAIN_ALIASES.get(card.get("id", ""), [])),
    ]
    return normalize(" ".join(fields))


def priority_bonus(priority: str) -> float:
    return {"P0": 0.3, "P1": 0.2, "P2": 0.1}.get(priority, 0.0)


def matched_terms(query: str, terms: list[str]) -> list[str]:
    q = normalize(query)
    return [term for term in terms if normalize(term) and normalize(term) in q]


def score_card(query: str, card: dict) -> dict:
    q = normalize(query)
    haystack = card_haystack(card)
    score = 0.0
    reasons: list[str] = []

    for alias in DOMAIN_ALIASES.get(card.get("id", ""), []):
        alias_norm = normalize(alias)
        if alias_norm and alias_norm in q:
            score += 12
            reasons.append(f"alias:{alias}")

    for keyword in card.get("trigger_keywords", []):
        keyword_norm = normalize(keyword)
        if keyword_norm and keyword_norm in q:
            score += 10
            reasons.append(f"trigger:{keyword}")

    if len(q) >= 5 and q in haystack:
        score += 5
        reasons.append("phrase")

    for token in sorted(set(tokens(query))):
        if token in haystack:
            score += 2
            reasons.append(f"token:{token}")

    if score > 0:
        score += priority_bonus(str(card.get("priority", "")))

    return {
        "wiki": card.get("id"),
        "name": card.get("name"),
        "score": round(score, 2),
        "reasons": reasons[:10],
        "card": card,
    }


def route(query: str, top_k: int) -> dict:
    cards = load_cards()
    matches = sorted(
        [score_card(query, card) for card in cards],
        key=lambda item: (-item["score"], item["wiki"] or ""),
    )
    matches = [item for item in matches if item["score"] > 0][: max(top_k, 1)]
    source_terms = matched_terms(query, SOURCE_UPDATE_TERMS)
    risk_terms = matched_terms(query, HIGH_RISK_TERMS)
    top = matches[0] if matches else None
    source_update_required = bool(source_terms) or bool(
        top and top["card"].get("freshness_requirement") == "high" and source_terms
    )
    safety_gate_required = bool(risk_terms) or bool(top and top["card"].get("risk_level") == "high")
    return {
        "generated": date.today().isoformat(),
        "query": query,
        "top_wiki": top["wiki"] if top else None,
        "source_update_required": source_update_required,
        "source_update_terms": source_terms,
        "safety_gate_required": safety_gate_required,
        "high_risk_terms": risk_terms,
        "matches": matches,
    }


def slim(result: dict) -> dict:
    slim_matches = []
    for item in result["matches"]:
        card = item["card"]
        slim_matches.append(
            {
                "wiki": item["wiki"],
                "name": item["name"],
                "score": item["score"],
                "reasons": item["reasons"],
                "priority": card.get("priority"),
                "risk_level": card.get("risk_level"),
                "freshness_requirement": card.get("freshness_requirement"),
                "required_reading_order": card.get("required_reading_order", []),
                "source_gates": card.get("source_gates", []),
                "safety_rules": card.get("safety_rules", []),
                "prohibited_actions": card.get("prohibited_actions", []),
                "package": card.get("package", ""),
            }
        )
    return {
        "generated": result["generated"],
        "query": result["query"],
        "top_wiki": result["top_wiki"],
        "source_update_required": result["source_update_required"],
        "source_update_terms": result["source_update_terms"],
        "safety_gate_required": result["safety_gate_required"],
        "high_risk_terms": result["high_risk_terms"],
        "matches": slim_matches,
    }


def markdown_list(items: list[str], limit: int = 6) -> list[str]:
    if not items:
        return ["- none"]
    return [f"- {item}" for item in items[:limit]]


def print_text(result: dict) -> None:
    data = slim(result)
    print(f"Query: {data['query']}")
    if not data["matches"]:
        print("No wiki match found. Read AGENTS.md and inspect registry/wiki-registry.yaml.")
        return
    top = data["matches"][0]
    print(f"Recommended wiki: {top['wiki']} (score {top['score']})")
    print(f"Priority: {top['priority']}; risk: {top['risk_level']}; freshness: {top['freshness_requirement']}")
    print(f"Source update required: {'yes' if data['source_update_required'] else 'no'}")
    if data["source_update_terms"]:
        print(f"Source-update terms: {', '.join(data['source_update_terms'])}")
    print(f"Safety gate required: {'yes' if data['safety_gate_required'] else 'no'}")
    if data["high_risk_terms"]:
        print(f"High-risk terms: {', '.join(data['high_risk_terms'])}")
    print("")
    print("Required reading order:")
    print("\n".join(markdown_list(top["required_reading_order"])))
    print("")
    print("Source gates:")
    print("\n".join(markdown_list(top["source_gates"])))
    print("")
    print("Safety rules:")
    print("\n".join(markdown_list(top["safety_rules"], 4)))
    print("")
    print("Do not do:")
    print("\n".join(markdown_list(top["prohibited_actions"], 4)))
    print("")
    print("Top matches:")
    for item in data["matches"]:
        reasons = ", ".join(item["reasons"]) if item["reasons"] else "priority/default"
        print(f"- {item['wiki']}: {item['score']} ({reasons})")
    print("")
    print("Next command:")
    print(f'python3 scripts/search_wiki.py --query "{data["query"]}" --wiki {top["wiki"]}')


def main() -> int:
    parser = ArgumentParser(description="Route a query to an Agent Wiki.")
    parser.add_argument("--query", required=True, help="User query or task description.")
    parser.add_argument("--top-k", type=int, default=3, help="Number of candidate wikis to return.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    try:
        result = route(args.query, args.top_k)
    except Exception as exc:
        print(f"route_wiki failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(slim(result), ensure_ascii=False, indent=2))
    else:
        print_text(result)
    return 0 if result["matches"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
