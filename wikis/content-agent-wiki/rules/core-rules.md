---
title: Core Rules
status: stable
last_updated: 2026-05-26
risk_level: low
---

# Core Rules

## General rules

1. 先判断任务是否属于本知识库范围。
2. 高风险任务先读取 `rules/`，再读取 `workflows/`。
3. 当前事实必须来源核验；无法核验时标记 `needs-source-update`。
4. 输出必须说明假设、不确定性和人工确认点。
5. 不保存敏感凭据，不执行未经确认的高风险操作。

## Quality rules

- 输出要可追溯到文件路径或来源记录。
- 新增规则要配至少一个案例或评测题。
- 工作流必须有输入、步骤、输出和验收标准。
