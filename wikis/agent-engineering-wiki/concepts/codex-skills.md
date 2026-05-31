---
title: Codex Skills Foundations
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Codex Skills Foundations

## Purpose

说明如何把可复用工作流沉淀为 Codex Skill。

## When to use

用于需要跨项目复用的专业流程、脚本、参考资料、模板和资产。

## Core rules

1. Skill 必须有清晰触发条件和适用边界。
2. `SKILL.md` 只写必要流程，长资料放入 `references/`。
3. 可自动化的重复步骤优先放入 `scripts/`，不要让 Agent 重写大段样板。
4. 示例不得包含真实凭据、私钥、cookie 或不可公开数据。

## Workflow

1. 定义触发词和任务边界。
2. 编写 `SKILL.md`：目标、读取顺序、步骤、验证和安全边界。
3. 添加 `scripts/`：可重复运行的校验、转换、生成或测试脚本。
4. 添加 `references/`：规范、格式、示例输入输出和决策表。
5. 添加 `assets/`：模板、图片、示例文件或可复用静态资源。
6. 设计 eval：验证技能是否在该触发时被正确使用。

## Edge cases

- 如果任务依赖最新 API 或平台行为，Skill 应要求官方来源核验。
- 如果脚本会修改文件，应说明输入、输出、备份和验证。
- 如果技能处理高风险领域，应写明拒绝范围和人工确认点。

## Validation checks

- 是否有 `SKILL.md`？
- 是否把长资料放到 references？
- 是否复用 scripts 而不是重复生成大段代码？
- 是否没有隐藏指令和敏感凭据？

## Source notes

Codex 插件、技能格式、工具能力和官方产品行为需要实时核验。
