## Knowledge Density Expansion v2.1

Generated on 2026-06-15 from model-synthesized stable knowledge.

- Scope: long-lived concepts, rules, workflows, cases, prompts, and evals.
- Boundary: no current facts, no authoritative source claims, no evidence auto-verification.
- High-risk/current claims still require source review and human confirmation.

| Area | Added |
| --- | ---: |
| concepts | 12 |
| rules | 8 |
| workflows | 8 |
| cases | 6 |
| prompts | 4 |
| eval tests | 10 |

# NodeOps Agent Wiki

## Stable Knowledge Expansion (2026-06-01)

Added stable, non-current operations knowledge:

- `concepts/service-reliability-signals.md`: availability, latency, error rate, saturation, throughput, logs, metrics, traces, and alert quality.
- `rules/backup-restore-and-change-safety.md`: backup validity, restore planning, destructive-operation gates, and rollback safety.
- `workflows/incident-triage-runbook.md`: impact-first incident triage, evidence capture, mitigation, communication, and review.
- `cases/sample-disk-pressure-incident.md`: safe handling of storage pressure without automatic deletion.

Expansion boundary: stable operations principles only. No current provider, OS, node, chain, service version, or live infrastructure facts are included.

Linux、Docker、systemd、监控、日志、备份、故障排查和节点运维知识库。

## When to use

触发词：服务器, Linux, Docker, systemd, 日志, 监控, 节点, RPC, 故障

## Structure

```text
concepts/   稳定概念
rules/      规则、边界、安全约束
workflows/  操作流程
cases/      案例和常见错误
tools/      工具、API、平台、格式
prompts/    Agent 提示词
evals/      测试题与验收标准
sources/    来源记录和更新计划
```

## Freshness policy

- `stable`: 可长期复用的概念、流程、规则。
- `needs-source-update`: 价格、政策、API、法规、平台规则、项目状态等需要实时来源确认的信息。

## Safety boundary

风险级别：`high`。高风险任务必须优先读取 `rules/`，并输出不确定性、人工确认点和不可用场景。
