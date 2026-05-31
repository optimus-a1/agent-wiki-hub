---
title: Codex Usage Rules
status: stable
last_updated: 2026-05-27
risk_level: medium
---

# Codex Usage Rules

## Purpose

规范 Codex 在代码仓库中的读取、修改、验证和汇报方式。

## When to use

用于任何由 Codex 执行的代码修改、测试、审查、调试和部署辅助任务。

## Core rules

1. 开始前读取根 AGENTS.md 和相关子目录规则。
2. 搜索优先使用 `rg`，理解局部上下文后再编辑。
3. 不回退用户已有修改，不执行破坏性 git 操作，除非用户明确要求。
4. 手工编辑使用补丁，保持改动范围小且可解释。
5. 完成前运行相关验证；无法运行时说明原因。

## Workflow

1. 识别任务类型：解释、审查、实现、修复、测试、部署。
2. 收集上下文：文件结构、入口、测试、配置和失败日志。
3. 形成最小改动路径并执行。
4. 运行验证命令并记录结果。
5. 输出变更摘要、验证结果、风险和后续建议。

## Edge cases

- 用户只要求分析或计划时，不擅自改代码。
- 如果遇到实时 API 文档问题，优先查官方来源，否则标记 `needs-source-update`。
- 涉及生产、资金、法律、健康、安全操作时保留人工确认点。

## Validation checks

- 是否遵守项目 AGENTS.md？
- 是否保护用户未提交修改？
- 是否运行或说明验证？

## Source notes

Codex、OpenAI API、GitHub、云平台和依赖工具的最新行为必须以官方文档为准。
