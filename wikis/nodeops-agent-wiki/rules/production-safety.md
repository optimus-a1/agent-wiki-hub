---
title: Production Safety Rules
status: stable
last_updated: 2026-05-26
risk_level: high
---

# Production Safety Rules

## Non-negotiable rules

1. 生产环境操作前先确认目标主机、服务名、数据目录和备份状态。
2. 破坏性命令必须先解释影响，并要求人工确认。
3. 永远不要在不确认路径的情况下执行删除、格式化、覆盖、强制重启等操作。
4. 所有改动都要有回滚步骤。
5. 修改 systemd、Docker、数据库、节点配置后，要检查日志和健康状态。

## Safe operation checklist

- 当前目录确认
- 磁盘空间确认
- 备份确认
- 服务状态确认
- 日志位置确认
- 端口占用确认
- 回滚方案确认
