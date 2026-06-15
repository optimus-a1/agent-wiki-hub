# Defensive Security Agent Wiki

## Stable Knowledge Expansion (2026-06-01)

Added stable, non-current defensive security knowledge:

- `concepts/security-control-model.md`: preventive, detective, corrective controls, least privilege, defense in depth, and risk acceptance.
- `rules/secret-handling-and-log-redaction.md`: secret classification, redaction, placeholders, history checks, and release blocking.
- `workflows/defensive-review-triage.md`: authorized triage, safe evidence, defensive remediation, and residual risk.
- `cases/sample-secret-exposure-review.md`: safe reporting of suspected secrets without revealing values.

Expansion boundary: defensive security principles only. No exploit steps, bypass instructions, current vulnerabilities, signatures, patches, or vendor policies are included.

防御性安全审查、配置检查、代码安全与上线前清单知识库。禁止攻击、绕过、盗取或利用步骤。

## When to use

触发词：安全, 审计, 漏洞, 权限, 密钥, 上线检查, 防御

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
