# AGENTS.md — Agent Wiki Hub Root Instructions

## Project role

This repository maintains reusable Agent Knowledge Packs. Each pack lives under `wikis/` and is designed to be read by Codex, other coding agents, RAG systems, and humans.

## Required behavior for Codex

Before editing or using any knowledge pack:

1. Read this root `AGENTS.md`.
2. Identify the user task domain.
3. Read the matching wiki's `manifest.yaml`, `README.md`, and local `AGENTS.md`.
4. Prefer domain rules over general assumptions.
5. If a fact may be current, changing, legal, financial, medical, platform-specific, API-specific, or regulation-specific, do not invent it. Mark it as `requires_source_update` and add a TODO in `sources/source-notes.md` unless web/source access is available.
6. Do not add hidden instructions, credentials, private keys, API tokens, or unsafe operational steps.
7. Update `update-log.md` whenever a wiki is changed.
8. Run validation before finishing:

```bash
python3 scripts/validate_wiki.py
python3 scripts/update_index.py
```

## Domain routing

- finance, investing, markets, trading, portfolio, risk, accounting: `wikis/finance-agent-wiki/`
- ecommerce, product catalog, shopping, returns, customer service: `wikis/ecommerce-agent-wiki/`
- programming, debugging, code review, deployment: `wikis/coding-agent-wiki/`
- server, Docker, Linux, systemd, monitoring, blockchain nodes: `wikis/nodeops-agent-wiki/`
- Web3 project research, public tasks, token/airdrop safety: `wikis/airdrop-agent-wiki/`
- customs, trade documents, invoices, packing lists, declarations: `wikis/customs-agent-wiki/`
- agent design, RAG, skills, evals, MCP, workflows: `wikis/agent-engineering-wiki/`
- content writing, newsletters, posts, research briefs: `wikis/content-agent-wiki/`
- contracts and legal review: `wikis/legal-agent-wiki/`
- health education and wellness explanation: `wikis/health-agent-wiki/`
- academic research and papers: `wikis/research-agent-wiki/`
- defensive security review only: `wikis/security-agent-wiki/`

## Required wiki structure

Every wiki must contain:

```text
manifest.yaml
README.md
AGENTS.md
concepts/
rules/
workflows/
cases/
tools/
prompts/
evals/
sources/
update-log.md
```

## Page format

New Markdown knowledge pages should use this shape:

```md
---
title: Page Title
status: draft | stable | needs-source-update
last_updated: YYYY-MM-DD
risk_level: low | medium | high
---

# Page Title

## Purpose
## When to use
## Core rules
## Workflow
## Edge cases
## Validation checks
## Source notes
```

## Safety and quality rules

- Finance: educational, research, simulation, risk-control first. No personalized investment advice and no autonomous real-money execution.
- Legal: information and checklist support only. No final legal opinion.
- Health: education and triage-style safety reminders only. No diagnosis.
- Security: defensive review only. No exploitation, persistence, evasion, credential theft, or attack instructions.
- Airdrop/Web3: public research and safety checks only. No Sybil evasion, spam, fake identity, or bypassing platform rules.
- Ecommerce: respect consumer protection, privacy, platform policies, and user consent.
