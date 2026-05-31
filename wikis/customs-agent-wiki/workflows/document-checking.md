---
title: Customs Document Checking Workflow
status: stable
last_updated: 2026-05-26
risk_level: medium
---

# Customs Document Checking Workflow

## Workflow

1. Identify document types.
2. Extract fields into normalized JSON.
3. Keep evidence text and page/table location when available.
4. Compare cross-document consistency.
5. Flag differences by severity: high, medium, low.
6. Output review table for human confirmation.

## Difference table columns

```text
field | document_a_value | document_b_value | evidence | severity | suggestion
```
