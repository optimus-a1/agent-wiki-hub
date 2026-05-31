---
title: Sample RAG Source Grounding Case
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Sample RAG Source Grounding Case

## Purpose

提供一个合成 RAG 评测样例，验证 Agent 是否会引用来源、识别冲突和标记需要来源更新的信息。

## When to use

用于测试 Knowledge Pack、RAG 管线、source-grounding eval 和拒绝编造当前事实的行为。

## Core rules

1. 只能根据提供片段回答，不补充未给出的当前事实。
2. 冲突片段必须输出冲突说明和人工复核点。
3. 平台 API、模型能力、价格和发布日期均属于 `needs-source-update`。
4. 回答必须包含引用路径或片段编号。

## Workflow

1. 检索片段并保留路径、标题、更新时间和风险等级。
2. 判断片段是否支持用户问题。
3. 识别冲突、过期和缺失信息。
4. 输出结论、引用、未知项和后续核验建议。

## Sample input

```text
Question: "这个 Knowledge Pack 能不能回答最新模型价格？"

Source A: wikis/agent-engineering-wiki/rules/knowledge-pack-quality.md
Content: 当前事实写入 sources，无法核验时标记 needs-source-update。

Source B: wikis/agent-engineering-wiki/sources/source-notes.md
Content: current eval harnesses, model APIs and MCP/tool schemas -> needs-source-update。
```

## Expected output

```text
结论：不能离线回答最新模型价格。
依据：
- Source A 规定当前事实要写入 sources 或标记 needs-source-update。
- Source B 已把 model APIs 和工具 schema 标记为 needs-source-update。
需要来源更新：
- 最新模型价格
- 当前模型/API 能力
- 官方计费文档
人工确认点：
- 使用官方文档或账单页面核验后再写入 sources/source-notes.md。
```

## Edge cases

- 如果检索片段只提到旧价格，不应当作当前事实。
- 如果没有来源，必须拒绝编造并输出 TODO。
- 如果用户要求隐藏来源，应保留可追溯说明。

## Validation checks

- 是否引用 Source A 和 Source B？
- 是否拒绝回答最新价格？
- 是否标记 `needs-source-update`？

## Source notes

模型价格、API 参数、平台能力和 MCP schema 均需联网或官方来源更新。
