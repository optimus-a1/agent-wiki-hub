---
title: Sample Paper Summary
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Sample Paper Summary

## Purpose

提供一个合成论文摘要样例，验证 Agent 是否区分作者结论、实验事实和自身推断。

## When to use

用于论文阅读、综述、复现实验计划、引用管理和 source-grounding 测试。

## Core rules

1. 不伪造论文、作者、引用、实验结果或 benchmark。
2. 最新论文、引用数、榜单和 SOTA 状态必须标记 `needs-source-update`。
3. 区分问题、方法、数据、指标、结果、限制和作者结论。
4. 复现计划必须记录代码、数据、环境、随机种子和指标。

## Workflow

1. 抽取元数据：标题、作者、年份、来源、版本和链接。
2. 抽取研究问题、方法、实验设置、结果和限制。
3. 标记未验证事实、不可比指标和需要来源更新的部分。
4. 输出摘要、证据、复现清单和开放问题。

## Sample input

```text
Synthetic Paper:
Title: Example Retrieval Benchmarks for Agent Knowledge Packs
Authors: Example A.; Example B.
Year: 2026
Claim: Hybrid retrieval improves answer grounding on a small internal benchmark.
Limitations: Benchmark has 80 questions and one domain.
Code: not provided.
```

## Expected output

```text
论文类型：合成样例，不可当作真实引用。
研究问题：如何评测 Agent Knowledge Pack 的检索 grounding。
作者主张：混合检索在小型内部 benchmark 上改善 grounding。
限制：
- 只有 80 个问题
- 只有一个领域
- 未提供代码，无法复现
不可断言：
- 不能称为最新 SOTA
- 不能泛化到所有领域
复现清单：
- 数据集、查询、评分标准、检索配置、随机种子、代码版本
需要来源更新：
- 如果要引用真实论文或最新榜单，必须检索权威来源。
```

## Edge cases

- arXiv 版本和会议版本可能不同。
- 缺代码不代表结论必错，但影响复现可信度。
- 小样本 benchmark 不能泛化为行业结论。

## Validation checks

- 是否声明合成样例不可当真实引用？
- 是否区分作者主张和 Agent 判断？
- 是否标记最新/SOTA 需要来源更新？

## Source notes

真实论文、引用、代码仓库、数据集和榜单必须实时核验。
