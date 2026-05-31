---
title: Main Workflow
status: stable
last_updated: 2026-05-26
risk_level: high
---

# Main Workflow

## Input

用户任务、相关文件、约束条件、期望输出格式。

## Steps

1. 识别任务意图和风险等级。
2. 读取 `manifest.yaml` 和 `rules/`。
3. 检索相关 `concepts/`、`workflows/`、`cases/`。
4. 判断是否需要最新来源。
5. 生成方案或结果。
6. 用 `evals/` 中的问题检查输出。
7. 标记缺口并更新 `sources/source-notes.md`。

## Output

- 任务理解
- 使用的知识路径
- 结果
- 风险/不确定性
- 需要人工确认的点
