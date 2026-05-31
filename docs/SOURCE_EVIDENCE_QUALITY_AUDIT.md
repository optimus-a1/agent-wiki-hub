# Source Evidence Quality Audit

Generated: 2026-05-31

## Purpose

This audit checks quality of completed source evidence entries. It does not verify external sources or certify current facts by itself.

## Summary

- Evidence entries: 13
- Final entries: 0
- Issues: 0
- Warnings: 0
- Audit passed: yes

## Status Counts

| Status | Entries |
| --- | ---: |
| pending | 13 |

## Entries

| Ticket | Wiki | Status | Confidence | Result | Log |
| --- | --- | --- | --- | --- | --- |
| TICKET-SRC-003 | airdrop-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-002 | airdrop-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-001 | airdrop-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-007 | finance-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-006 | finance-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-005 | finance-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-004 | finance-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-009 | health-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-008 | health-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-011 | legal-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-010 | legal-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-013 | security-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md) |
| TICKET-SRC-012 | security-agent-wiki | pending | low | PASS | [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md) |

## Issues

No evidence quality issues found.

## Warnings

No evidence quality warnings found.

## Quality Rules

- Final evidence must include source title, publisher, reference, access date, evidence summary, confidence, and remaining uncertainty.
- High-risk tickets require a human reviewer.
- Dates must use `YYYY-MM-DD` except `source_published_or_updated`, which may be `unknown` when the source does not publish a date.
- Evidence must not include API keys, private keys, cookies, authorization headers, bearer tokens, seed phrases, or mnemonics.
- A `verified` entry does not remove human confirmation requirements for high-risk domains.

## Re-run

```bash
python3 scripts/audit_source_evidence_quality.py
python3 scripts/run_acceptance.py
```
