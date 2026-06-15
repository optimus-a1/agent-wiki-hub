## Knowledge Density Expansion v2.1

Generated on 2026-06-15 from model-synthesized stable knowledge.

- Scope: long-lived concepts, rules, workflows, cases, prompts, and evals.
- Boundary: no current facts, no authoritative source claims, no evidence auto-verification.
- High-risk/current claims still require source review and human confirmation.

| Area | Added |
| --- | ---: |
| concepts | 12 |
| rules | 8 |
| workflows | 8 |
| cases | 5 |
| prompts | 6 |
| eval tests | 10 |

# Agent Engineering Wiki

## Stable Knowledge Expansion (2026-06-01)

Added stable, non-current agent engineering knowledge:

- `concepts/agent-memory-and-context.md`: working memory, long-term memory, retrieval-backed memory, handoff, and stale-memory risk.
- `rules/tool-use-and-grounding.md`: evidence grounding, tool selection, source support boundaries, and action gates.
- `workflows/agent-eval-loop.md`: golden questions, behavior tests, source-grounding tests, and regression loops.
- `cases/sample-tool-overreach.md`: safe handling of requests that tempt unnecessary or unsafe tool execution.

Expansion boundary: stable agent design principles only. No current model, tool schema, platform capability, or API parameter facts are included.

Agent 架构、RAG、知识包、Codex Skills、评测与安全边界知识库。

## When to use

触发词：Agent, RAG, 知识库, Codex Skill, AGENTS.md, 评测, MCP, 工作流

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
