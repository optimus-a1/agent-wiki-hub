# Agent Engineering Wiki

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
