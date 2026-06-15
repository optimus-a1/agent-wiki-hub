## Knowledge Density Expansion v2.1

Generated on 2026-06-15 from model-synthesized stable knowledge.

- Scope: long-lived concepts, rules, workflows, cases, prompts, and evals.
- Boundary: no current facts, no authoritative source claims, no evidence auto-verification.
- High-risk/current claims still require source review and human confirmation.

| Area | Added |
| --- | ---: |
| concepts | 12 |
| rules | 10 |
| workflows | 8 |
| cases | 6 |
| prompts | 4 |
| eval tests | 12 |

# Finance Agent Wiki

## Stable Knowledge Expansion (2026-06-01)

Added stable, non-current finance knowledge:

- `concepts/portfolio-and-risk-metrics.md`: portfolio exposure, drawdown, liquidity, correlation, and risk-adjusted interpretation.
- `rules/model-risk-and-backtest-hygiene.md`: lookahead, survivorship, overfitting, costs, capacity, and model governance.
- `workflows/portfolio-review-workflow.md`: simulation-first portfolio review with exposure tables and human confirmation points.
- `cases/sample-overfitting-detection.md`: safe review of suspicious backtests without live trading recommendations.

Expansion boundary: educational and simulated finance principles only. No current prices, regulations, platform rules, broker terms, or personalized investment advice are included.

金融研究、财务分析、市场数据、回测、风控与模拟交易系统知识库。默认用于教育、研究和模拟，不输出个人化投资建议。

## When to use

触发词：金融, 投资, 财报, 估值, 市场数据, 回测, 风控, 交易系统, 资金费率, 套利

## Structure

```text
concepts/   稳定概念
rules/      规则、边界、安全约束
workflows/  操作流程
cases/      案例和常见错误
tools/      工具、API、平台、格式
prompts/    Agent 提示词
evals/      测试题与验收标准
sources/    来源记录和更新计划
```

## Freshness policy

- `stable`: 可长期复用的概念、流程、规则。
- `needs-source-update`: 价格、政策、API、法规、平台规则、项目状态等需要实时来源确认的信息。

## Safety boundary

风险级别：`high`。高风险任务必须优先读取 `rules/`，并输出不确定性、人工确认点和不可用场景。
