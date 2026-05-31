---
title: Incident Response Workflow
status: stable
last_updated: 2026-05-26
risk_level: high
---

# Incident Response Workflow

## Workflow

1. Define symptom: 服务不可用、同步慢、磁盘满、内存高、端口不通。
2. Check scope: 单机、单服务、网络、依赖、外部 API。
3. Collect evidence: logs、metrics、system status、recent changes。
4. Stabilize: 限流、重启非关键进程、释放空间、切换备用服务。
5. Root cause: 配置、资源、依赖、版本、数据损坏。
6. Fix: 小步修复，保留回滚。
7. Verify: 健康检查、日志、端口、指标、业务请求。
8. Postmortem: 记录原因、影响、修复、预防。
