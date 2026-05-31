---
title: Defensive Security Review Checklist
status: stable
last_updated: 2026-05-26
risk_level: high
---

# Defensive Security Review Checklist

## Checklist

- Secrets are not committed.
- Environment variables are documented but values are absent.
- Authentication and authorization are separated.
- Inputs are validated and outputs encoded.
- Logs avoid tokens, passwords, private keys and personal data.
- Dependencies are reviewed with current vulnerability sources.
- Backups and recovery are tested.
