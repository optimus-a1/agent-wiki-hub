---
title: Knowledge Pack Quality Rules
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Knowledge Pack Quality Rules

## Purpose

保证每个 Agent Knowledge Pack 可读、可检索、可验证、可更新。

## When to use

用于创建、扩展、审查或打包 wiki。

## Core rules

1. 每个 wiki 必须有 manifest、README、AGENTS、rules、workflows、evals 和 sources。
2. 新 Markdown 页面必须包含标题、状态、更新时间和风险级别。
3. 稳定知识写入 concepts/rules/workflows；当前事实写入 sources。
4. 高风险 wiki 必须先读 rules 再读 workflows。
5. 每次变更必须更新 `update-log.md`。

## Workflow

1. 检查结构：目录、入口文件、知识文件是否齐全。
2. 检查路由：trigger_keywords 是否覆盖真实任务语言。
3. 检查边界：是否有拒绝范围、人工确认点和安全说明。
4. 检查评测：是否覆盖成功、失败、拒答、来源更新和边界案例。
5. 检查索引：搜索关键任务词是否命中对应页面。

## Edge cases

- 不能把示例当规则。
- 不能把过期事实写成稳定知识。
- 不能用空泛安全声明替代具体操作边界。

## Validation checks

- `python3 scripts/validate_wiki.py`
- `python3 scripts/update_index.py`
- 关键 query 能搜索到目标 wiki。

## Source notes

知识包 schema、Codex Skill 规范、RAG 框架和工具接口的最新版本需要来源更新。
