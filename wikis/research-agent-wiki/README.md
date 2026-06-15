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
| cases | 5 |
| prompts | 4 |
| eval tests | 10 |

# Research Agent Wiki

## Stable Knowledge Expansion (2026-06-01)

Added stable, non-current research knowledge:

- `concepts/evidence-quality-and-bias.md`: validity, bias, confounding, evidence strength, and uncertainty.
- `rules/reproducibility-and-citation-integrity.md`: citation support, reproducibility details, benchmark claim requirements, and unknown fields.
- `workflows/systematic-literature-review.md`: review questions, search strategy, screening, extraction, appraisal, and synthesis.
- `cases/sample-benchmark-claim-review.md`: safe benchmark claim review without inventing rankings or results.

Expansion boundary: stable research methodology only. No current papers, rankings, benchmark results, dataset versions, or literature coverage claims are included.

论文阅读、综述、实验复现、引用管理和研究评测知识库。

## When to use

触发词：论文, 研究, 综述, 实验, 数据集, 引用, benchmark

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
