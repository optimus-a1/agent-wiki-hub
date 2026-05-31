---
title: Eval Design Workflow
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Eval Design Workflow

## Purpose

把 Agent 的期望行为转成可重复的评测题、行为测试和来源约束测试。

## When to use

用于新建 wiki、扩展规则、上线 Agent、修复失败案例和回归测试。

## Core rules

1. eval 必须覆盖正向任务、边界任务、拒答任务和来源更新任务。
2. 高风险领域必须测试人工确认点。
3. RAG eval 必须测试是否引用来源、是否识别过期信息、是否拒绝编造。
4. eval 不能只检查关键词，要检查行为。

## Workflow

1. 收集 golden questions：来自真实用户任务、常见误区和验收标准。
2. 设计 behavior tests：是否先读规则、是否输出风险、是否按工作流执行。
3. 设计 source-grounding tests：要求当前事实时是否查源或标记 `needs-source-update`。
4. 设计 refusal tests：金融、法律、健康、安全、Web3 等高风险越界请求。
5. 设计 regression tests：把历史失败案例变成固定测试。
6. 更新 eval 文件并在 update-log 记录变更。

## Edge cases

- 过度宽泛的 expected_behavior 无法验收，应写出必需元素。
- 只测理想输入会漏掉 OCR、缺字段、冲突来源和恶意提示。
- 如果需要自动评分，应明确可判定字段。

## Validation checks

- 是否至少覆盖结构、freshness、routing、safety、update？
- 是否覆盖领域专属关键任务？
- 是否有 source-grounding tests？

## Source notes

自动评测框架、模型行为和平台工具能力需要实时核验。
