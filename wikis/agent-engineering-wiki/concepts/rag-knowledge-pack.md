---
title: RAG and Knowledge Pack Foundations
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# RAG and Knowledge Pack Foundations

## Purpose

定义可被 Agent、RAG 系统和人类共同使用的知识包标准。

## When to use

用于设计知识库、RAG 管线、检索评测、引用规则和多 Agent 共享知识。

## Core rules

1. 先整理结构化知识，再做索引。
2. 当前事实、平台规则、API 参数和法规政策必须标记 `needs-source-update`。
3. 检索答案必须能追溯到 wiki 文件、段落或外部来源。
4. 高风险领域必须包含规则、人工确认点、拒答边界和评测。

## Workflow

1. 切块：按标题、语义段、表格和任务边界切分，保留层级元数据。
2. 索引：记录路径、标题、更新时间、风险级别、状态和语言。
3. 召回：使用关键词、向量或混合检索，优先命中当前任务领域。
4. 重排：按相关性、风险匹配、更新时间和来源可靠性排序。
5. 引用：输出文件路径、来源说明和不确定性。
6. 评测：使用 golden questions、行为测试、拒答测试和 source-grounding tests。

## Knowledge Pack standard

- `manifest.yaml`: id、domain、risk、freshness、trigger_keywords、entrypoints。
- `AGENTS.md`: 触发条件、读取顺序、必需行为。
- `rules/`: 领域边界、质量规则、安全限制。
- `workflows/`: 输入、步骤、输出、验收标准。
- `evals/`: golden questions、behavior tests、source-grounding tests。
- `sources/`: 当前事实、权威来源、TODO 和更新记录。

## Validation checks

- 是否能被本地脚本验证结构？
- 是否能被搜索索引命中关键任务？
- 是否区分稳定知识和当前事实？
- 是否有高风险人工确认点？

## Source notes

RAG 框架、嵌入模型、向量数据库、平台 API 和评测工具的最新能力均需来源更新。
