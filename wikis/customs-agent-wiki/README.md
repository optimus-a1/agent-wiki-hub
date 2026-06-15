## Knowledge Density Expansion v2.1

Generated on 2026-06-15 from model-synthesized stable knowledge.

- Scope: long-lived concepts, rules, workflows, cases, prompts, and evals.
- Boundary: no current facts, no authoritative source claims, no evidence auto-verification.
- High-risk/current claims still require source review and human confirmation.

| Area | Added |
| --- | ---: |
| concepts | 10 |
| rules | 8 |
| workflows | 6 |
| cases | 6 |
| prompts | 4 |
| eval tests | 10 |

# Customs Document Agent Wiki

外贸单证、报关报检字段抽取、差异比对、人工复核知识库。政策与监管条件必须实时更新。

## When to use

触发词：报关, 报检, 单证, 发票, 装箱单, 合同, 厂检, HS编码, 字段校对

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

风险级别：`medium`。高风险任务必须优先读取 `rules/`，并输出不确定性、人工确认点和不可用场景。
