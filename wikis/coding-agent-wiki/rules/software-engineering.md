---
title: Software Engineering Rules
status: stable
last_updated: 2026-05-26
risk_level: medium
---

# Software Engineering Rules

## Core rules

1. 先读项目 `AGENTS.md`，再改代码。
2. 小步修改，优先保持现有架构一致。
3. 修改行为必须配测试；修复 bug 必须加回归测试。
4. 不把密钥、cookie、token、私钥写入代码或日志。
5. 生产变更必须有回滚方案。
6. 不为通过测试而删除测试或降低断言质量。

## Definition of done

- 代码通过格式化、lint、类型检查和测试。
- README 或文档更新了用户可见变化。
- 错误处理覆盖主要失败路径。
- 安全敏感数据不入库、不回显、不打日志。
