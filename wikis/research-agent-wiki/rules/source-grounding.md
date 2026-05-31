---
title: Research Source Grounding Rules
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Research Source Grounding Rules

## Purpose

保证研究 Agent 在论文、数据集、实验和综述任务中明确来源、证据和不确定性。

## When to use

用于论文阅读、文献综述、实验复现、数据集分析、benchmark 比较和引用管理。

## Core rules

1. 不伪造论文、作者、实验结果、引用、数据集或 benchmark。
2. 最新论文、引用数、排行榜、模型性能和数据集状态必须实时核验。
3. 区分作者结论、实验事实、二次解读和 Agent 推断。
4. 复现实验必须记录代码版本、数据版本、环境和随机种子。

## Workflow

1. 来源识别：论文、预印本、代码库、数据集、项目页、勘误和补充材料。
2. 证据抽取：问题、方法、数据、指标、结果、限制和失败案例。
3. 交叉验证：对照论文、官方代码、复现实验和独立评测。
4. 引用输出：保留标题、作者、年份、链接或本地路径、访问日期。
5. 不确定性：标记未复现、未审稿、样本小、数据缺失和指标不可比。

## Edge cases

- arXiv 版本可能和会议版本不同。
- benchmark 可能因数据泄漏、评测设置或版本不同不可比。
- 引用数和 SOTA 状态变化快，不能离线断言最新。

## Validation checks

- 是否有可追溯来源？
- 是否区分事实、作者观点和 Agent 推断？
- 是否把最新论文和榜单标记为 `needs-source-update`？

## Source notes

论文版本、引用数、排行榜、数据集可用性、模型权重和代码仓库状态均需实时核验。
