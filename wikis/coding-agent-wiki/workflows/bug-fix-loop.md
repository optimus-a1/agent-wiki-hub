---
title: Bug Fix Loop
status: stable
last_updated: 2026-05-26
risk_level: medium
---

# Bug Fix Loop

## Workflow

1. Reproduce: 找到最小复现步骤。
2. Observe: 收集日志、错误栈、输入输出。
3. Localize: 缩小到模块、函数、数据边界。
4. Fix minimally: 做最小安全改动。
5. Test: 加回归测试，运行相关测试。
6. Review: 检查是否引入新风险。
7. Document: 更新变更说明。

## Anti-patterns

- 没有复现就改代码。
- 大面积重构掩盖小 bug。
- 靠吞异常隐藏问题。
- 删除失败测试。
