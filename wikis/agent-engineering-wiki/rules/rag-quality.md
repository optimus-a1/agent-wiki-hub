---
title: RAG Quality Rules
status: stable
last_updated: 2026-05-26
risk_level: medium
---

# RAG Quality Rules

## Core rules

1. 先结构化知识，再向量化索引。
2. 检索结果必须可追溯到文件路径和段落。
3. 高风险答案必须引用来源或标记不确定。
4. 切块应保留标题、层级、上下文和元数据。
5. 评测必须覆盖：召回、准确性、引用、拒答边界、过期信息识别。

## Common failure modes

- 检索到相似但不相关的段落。
- 旧版本政策覆盖新版本政策。
- Agent 把 examples 当成 rules。
- 缺少引用路径。
- 知识库和代码实现不同步。
