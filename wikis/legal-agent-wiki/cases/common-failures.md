---
title: Common Failure Cases
status: stable
last_updated: 2026-05-26
risk_level: high
---

# Common Failure Cases

## Failure patterns

1. 未读取本地规则就直接回答。
2. 把过期政策、价格、API 或平台规则当成事实。
3. 没有说明假设和不确定性。
4. 缺少人工确认点。
5. 没有把新增知识写入正确目录。

## Correction pattern

```text
发现问题 -> 定位来源 -> 更新规则/案例 -> 增加 eval -> 记录 update-log
```
