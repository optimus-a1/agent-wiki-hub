## Knowledge Density Expansion v2.1

Generated on 2026-06-15 from model-synthesized stable knowledge.

- Scope: long-lived concepts, rules, workflows, cases, prompts, and evals.
- Boundary: no current facts, no authoritative source claims, no evidence auto-verification.
- High-risk/current claims still require source review and human confirmation.

| Area | Added |
| --- | ---: |
| concepts | 8 |
| rules | 6 |
| workflows | 5 |
| cases | 4 |
| prompts | 4 |
| eval tests | 8 |

# Content Agent Wiki

研究简报、日报、文章、短帖、长帖、标题和发布检查知识库。

## When to use

触发词：内容, 写作, 日报, 公众号, 帖子, 标题, 摘要, 发布

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

风险级别：`low`。高风险任务必须优先读取 `rules/`，并输出不确定性、人工确认点和不可用场景。
