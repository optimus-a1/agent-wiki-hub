---
title: Production Change Management Workflow
status: stable
last_updated: 2026-05-27
risk_level: high
---

# Production Change Management Workflow

## Purpose

把生产运维变更拆成可审批、可回滚、可审计的步骤。

## When to use

用于部署、重启、升级、配置修改、证书轮换、扩容、迁移和节点维护。

## Core rules

1. 生产变更必须有人类确认和明确窗口。
2. 先观察和备份，再执行最小变更。
3. 变更后必须验证服务、日志、指标和用户路径。
4. 如果无法回滚，应升级为高风险人工评审。

## Workflow

1. 变更申请：目标、影响范围、执行人、时间窗口、成功标准。
2. 预检查：磁盘、内存、CPU、网络、依赖、备份、告警和访问权限。
3. 执行计划：逐步命令、预期输出、检查点和暂停条件。
4. 回滚计划：版本、配置、数据恢复点、DNS 或流量切换方案。
5. 监控验证：错误率、延迟、资源、队列、日志和业务指标。
6. 复盘记录：结果、问题、后续修复和知识库更新。

## Edge cases

- 数据迁移和 schema 变更要单独验证向前/向后兼容。
- 证书、DNS 和防火墙变更需要考虑缓存和传播时间。
- 节点升级要记录客户端版本、网络高度和共识状态。

## Validation checks

- 是否有成功标准、暂停条件和回滚路径？
- 是否有备份和监控？
- 是否列出需要实时核验的版本和平台规则？

## Source notes

云厂商限制、系统包版本、节点客户端版本、链网络参数和 API 兼容性均为 `needs-source-update`。
