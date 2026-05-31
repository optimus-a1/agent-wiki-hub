# Source Refresh Tickets

Generated: 2026-05-31

## Purpose

These tickets turn source-refresh tasks into executable verification work. They do not verify or certify current facts by themselves.

## Summary

- Tickets: 35
- Playbook: `registry/source-refresh-playbook.json`
- Passed structural check: yes

## How To Execute A Ticket

- Read the required wiki files before searching or editing.
- Collect authoritative dated evidence for the exact topic and scope.
- Decide whether the topic is verified, unchanged, still needs source update, or rejected.
- Record evidence with `scripts/record_source_evidence.py` or manually in the wiki's `sources/source-refresh-log.md`.
- Update only the minimal affected pages, then run the post-update commands.

## Ticket Index

| Ticket | Wave | Wiki | Priority | Category | Human confirmation | Topic |
| --- | --- | --- | ---: | --- | --- | --- |
| TICKET-SRC-001 | wave-1 | airdrop-agent-wiki | 8 | web3_project_status | yes | current contract addresses, wallet warnings, scam reports and signing risks |
| TICKET-SRC-002 | wave-1 | airdrop-agent-wiki | 8 | policy_or_regulation | yes | current project status, official links, task rules, snapshot and eligibility |
| TICKET-SRC-003 | wave-1 | airdrop-agent-wiki | 8 | web3_project_status | yes | current token launch, TGE, funding, exchange listing and airdrop allocation |
| TICKET-SRC-004 | wave-1 | finance-agent-wiki | 8 | market_or_platform_data | yes | current fees, funding rates, margin rules, tax rules and trading API parameters |
| TICKET-SRC-005 | wave-1 | finance-agent-wiki | 8 | policy_or_regulation | yes | current legal, regulatory or suitability requirements for financial products |
| TICKET-SRC-006 | wave-1 | finance-agent-wiki | 8 | market_or_platform_data | yes | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| TICKET-SRC-007 | wave-1 | finance-agent-wiki | 8 | general_current_fact | yes | latest financial statements, filings, restatements and audit opinions |
| TICKET-SRC-008 | wave-1 | health-agent-wiki | 8 | medical_guidance | yes | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| TICKET-SRC-009 | wave-1 | health-agent-wiki | 8 | medical_guidance | yes | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| TICKET-SRC-010 | wave-1 | legal-agent-wiki | 8 | policy_or_regulation | yes | current platform agreements, data processing terms and consumer protection rules |
| TICKET-SRC-011 | wave-1 | legal-agent-wiki | 8 | policy_or_regulation | yes | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| TICKET-SRC-012 | wave-1 | security-agent-wiki | 8 | security_advisory | yes | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| TICKET-SRC-013 | wave-1 | security-agent-wiki | 8 | policy_or_regulation | yes | current security tool rules, detection signatures, cloud defaults and compliance requirements |
| TICKET-SRC-014 | wave-2 | customs-agent-wiki | 7 | market_or_platform_data | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| TICKET-SRC-015 | wave-2 | customs-agent-wiki | 7 | general_current_fact | no | latest HS codes, customs supervision conditions and declaration elements |
| TICKET-SRC-016 | wave-2 | customs-agent-wiki | 7 | policy_or_regulation | no | latest import/export policy, inspection and quarantine requirements |
| TICKET-SRC-017 | wave-2 | customs-agent-wiki | 7 | technical_docs | no | latest platform OCR model parameters and document template behavior |
| TICKET-SRC-018 | wave-2 | ecommerce-agent-wiki | 7 | policy_or_regulation | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| TICKET-SRC-019 | wave-2 | ecommerce-agent-wiki | 7 | general_current_fact | no | current product certification, recall, safety notice and warranty terms |
| TICKET-SRC-020 | wave-2 | ecommerce-agent-wiki | 7 | market_or_platform_data | no | current product price, stock, promotion, shipping fee and delivery ETA |
| TICKET-SRC-021 | wave-2 | nodeops-agent-wiki | 7 | general_current_fact | yes | current OS package, Docker, systemd and kernel behavior |
| TICKET-SRC-022 | wave-2 | nodeops-agent-wiki | 7 | technical_docs | yes | current blockchain node client versions, network parameters and upgrade requirements |
| TICKET-SRC-023 | wave-2 | nodeops-agent-wiki | 7 | general_current_fact | yes | current cloud provider limits, firewall behavior, billing and incident status |
| TICKET-SRC-024 | wave-2 | research-agent-wiki | 7 | technical_docs | no | current dataset availability, license, model weights and code repository status |
| TICKET-SRC-025 | wave-2 | research-agent-wiki | 7 | general_current_fact | no | latest papers, preprints, revisions, citations and benchmark leaderboards |
| TICKET-SRC-026 | wave-3 | agent-engineering-wiki | 6 | technical_docs | no | current Codex Skill format, plugin behavior and tool capabilities |
| TICKET-SRC-027 | wave-3 | agent-engineering-wiki | 6 | technical_docs | no | current RAG frameworks, embedding models, vector databases and rerankers |
| TICKET-SRC-028 | wave-3 | agent-engineering-wiki | 6 | technical_docs | no | current eval harnesses, model APIs and MCP/tool schemas |
| TICKET-SRC-029 | wave-3 | coding-agent-wiki | 6 | general_current_fact | no | current OpenAI, Codex, GitHub or Vercel product behavior |
| TICKET-SRC-030 | wave-3 | coding-agent-wiki | 6 | general_current_fact | no | current cloud platform build, deploy, runtime and pricing behavior |
| TICKET-SRC-031 | wave-3 | coding-agent-wiki | 6 | security_advisory | no | current dependency vulnerabilities and security advisories |
| TICKET-SRC-032 | wave-3 | coding-agent-wiki | 6 | technical_docs | no | current framework, library, CLI and API parameters |
| TICKET-SRC-033 | wave-3 | content-agent-wiki | 5 | general_current_fact | no | current image, chart, dataset and quote licensing |
| TICKET-SRC-034 | wave-3 | content-agent-wiki | 5 | general_current_fact | no | current news, statistics, public quotes and social media claims |
| TICKET-SRC-035 | wave-3 | content-agent-wiki | 5 | policy_or_regulation | no | current publishing platform rules, format limits and content policies |

## Tickets

### wave-1

#### TICKET-SRC-001 - airdrop-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current contract addresses, wallet warnings, scam reports and signing risks
- Category: `web3_project_status`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/airdrop-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/airdrop-agent-wiki/manifest.yaml)
- [README.md](../wikis/airdrop-agent-wiki/README.md)
- [rules](../wikis/airdrop-agent-wiki/rules/)
- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official contract registry, block explorer, wallet security warning.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Never request or store private keys, seed phrases, cookies, or session tokens.
- [ ] Do not add Sybil evasion, fake identity, spam, or platform-rule bypass guidance.
- [ ] Require human review before wallet signing or permission changes.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.

Content targets:

- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/airdrop-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-001",
  "ticket_id": "TICKET-SRC-001",
  "topic": "current contract addresses, wallet warnings, scam reports and signing risks",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/airdrop-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-002 - airdrop-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current project status, official links, task rules, snapshot and eligibility
- Category: `policy_or_regulation`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/airdrop-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/airdrop-agent-wiki/manifest.yaml)
- [README.md](../wikis/airdrop-agent-wiki/README.md)
- [rules](../wikis/airdrop-agent-wiki/rules/)
- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official website, official documentation, official announcement channel.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Never request or store private keys, seed phrases, cookies, or session tokens.
- [ ] Do not add Sybil evasion, fake identity, spam, or platform-rule bypass guidance.
- [ ] Require human review before wallet signing or permission changes.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.

Content targets:

- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/airdrop-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-002",
  "ticket_id": "TICKET-SRC-002",
  "topic": "current project status, official links, task rules, snapshot and eligibility",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/airdrop-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-003 - airdrop-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current token launch, TGE, funding, exchange listing and airdrop allocation
- Category: `web3_project_status`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/airdrop-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/airdrop-agent-wiki/manifest.yaml)
- [README.md](../wikis/airdrop-agent-wiki/README.md)
- [rules](../wikis/airdrop-agent-wiki/rules/)
- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: project announcement, exchange official announcement, primary funding disclosure.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Never request or store private keys, seed phrases, cookies, or session tokens.
- [ ] Do not add Sybil evasion, fake identity, spam, or platform-rule bypass guidance.
- [ ] Require human review before wallet signing or permission changes.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.

Content targets:

- [source-notes.md](../wikis/airdrop-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/airdrop-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/airdrop-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-003",
  "ticket_id": "TICKET-SRC-003",
  "topic": "current token launch, TGE, funding, exchange listing and airdrop allocation",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/airdrop-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-004 - finance-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current fees, funding rates, margin rules, tax rules and trading API parameters
- Category: `market_or_platform_data`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/finance-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/finance-agent-wiki/manifest.yaml)
- [README.md](../wikis/finance-agent-wiki/README.md)
- [rules](../wikis/finance-agent-wiki/rules/)
- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official exchange documentation, regulator announcement, broker or custodian fee schedule.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Keep the output educational, research-oriented, or simulation-oriented.
- [ ] Do not introduce personalized investment advice.
- [ ] Do not introduce autonomous real-money execution.
- [ ] Keep human confirmation before high-risk financial use.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No personalized investment advice or autonomous real-money execution is introduced.

Content targets:

- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/finance-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-004",
  "ticket_id": "TICKET-SRC-004",
  "topic": "current fees, funding rates, margin rules, tax rules and trading API parameters",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/finance-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-005 - finance-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current legal, regulatory or suitability requirements for financial products
- Category: `policy_or_regulation`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/finance-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/finance-agent-wiki/manifest.yaml)
- [README.md](../wikis/finance-agent-wiki/README.md)
- [rules](../wikis/finance-agent-wiki/rules/)
- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: regulator website, licensed professional review, official product documents.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Keep the output educational, research-oriented, or simulation-oriented.
- [ ] Do not introduce personalized investment advice.
- [ ] Do not introduce autonomous real-money execution.
- [ ] Keep human confirmation before high-risk financial use.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No personalized investment advice or autonomous real-money execution is introduced.

Content targets:

- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/finance-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-005",
  "ticket_id": "TICKET-SRC-005",
  "topic": "current legal, regulatory or suitability requirements for financial products",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/finance-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-006 - finance-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity
- Category: `market_or_platform_data`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/finance-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/finance-agent-wiki/manifest.yaml)
- [README.md](../wikis/finance-agent-wiki/README.md)
- [rules](../wikis/finance-agent-wiki/rules/)
- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: primary exchange or market data vendor, official issuer or exchange data portal, timestamped raw dataset.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Keep the output educational, research-oriented, or simulation-oriented.
- [ ] Do not introduce personalized investment advice.
- [ ] Do not introduce autonomous real-money execution.
- [ ] Keep human confirmation before high-risk financial use.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No personalized investment advice or autonomous real-money execution is introduced.

Content targets:

- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/finance-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-006",
  "ticket_id": "TICKET-SRC-006",
  "topic": "current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/finance-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-007 - finance-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: latest financial statements, filings, restatements and audit opinions
- Category: `general_current_fact`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/finance-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/finance-agent-wiki/manifest.yaml)
- [README.md](../wikis/finance-agent-wiki/README.md)
- [rules](../wikis/finance-agent-wiki/rules/)
- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: company investor relations, securities regulator filing system, audited annual or interim report.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Keep the output educational, research-oriented, or simulation-oriented.
- [ ] Do not introduce personalized investment advice.
- [ ] Do not introduce autonomous real-money execution.
- [ ] Keep human confirmation before high-risk financial use.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No personalized investment advice or autonomous real-money execution is introduced.

Content targets:

- [source-notes.md](../wikis/finance-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/finance-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/finance-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-007",
  "ticket_id": "TICKET-SRC-007",
  "topic": "latest financial statements, filings, restatements and audit opinions",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/finance-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-008 - health-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current clinical guidelines, drug labels, dosage, contraindications and safety warnings
- Category: `medical_guidance`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/health-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/health-agent-wiki/manifest.yaml)
- [README.md](../wikis/health-agent-wiki/README.md)
- [rules](../wikis/health-agent-wiki/rules/)
- [source-notes.md](../wikis/health-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official health authority, drug regulator label, professional clinical guideline.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Do not introduce diagnosis, prescription, dosing, or treatment orders.
- [ ] Preserve clinician review and urgent-care escalation points.
- [ ] Keep guidelines, drug labels, contraindications, and safety warnings source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No diagnosis or treatment instruction is introduced; clinician confirmation points remain visible.

Content targets:

- [source-notes.md](../wikis/health-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/health-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-008",
  "ticket_id": "TICKET-SRC-008",
  "topic": "current clinical guidelines, drug labels, dosage, contraindications and safety warnings",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/health-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-009 - health-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current public health guidance, screening recommendations and nutrition/exercise guidelines
- Category: `medical_guidance`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/health-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/health-agent-wiki/manifest.yaml)
- [README.md](../wikis/health-agent-wiki/README.md)
- [rules](../wikis/health-agent-wiki/rules/)
- [source-notes.md](../wikis/health-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: public health authority, professional medical society, licensed clinician review.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Do not introduce diagnosis, prescription, dosing, or treatment orders.
- [ ] Preserve clinician review and urgent-care escalation points.
- [ ] Keep guidelines, drug labels, contraindications, and safety warnings source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No diagnosis or treatment instruction is introduced; clinician confirmation points remain visible.

Content targets:

- [source-notes.md](../wikis/health-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/health-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/health-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-009",
  "ticket_id": "TICKET-SRC-009",
  "topic": "current public health guidance, screening recommendations and nutrition/exercise guidelines",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/health-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-010 - legal-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current platform agreements, data processing terms and consumer protection rules
- Category: `policy_or_regulation`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/legal-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/legal-agent-wiki/manifest.yaml)
- [README.md](../wikis/legal-agent-wiki/README.md)
- [rules](../wikis/legal-agent-wiki/rules/)
- [source-notes.md](../wikis/legal-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official platform terms, regulator guidance, counsel-approved template.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Do not introduce final legal opinions or guaranteed outcomes.
- [ ] Preserve jurisdiction, date, source, and lawyer review points.
- [ ] Keep statutes, cases, regulations, and platform terms source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No final legal opinion is introduced; jurisdiction and lawyer review points remain visible.

Content targets:

- [source-notes.md](../wikis/legal-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/legal-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-010",
  "ticket_id": "TICKET-SRC-010",
  "topic": "current platform agreements, data processing terms and consumer protection rules",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/legal-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-011 - legal-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements
- Category: `policy_or_regulation`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/legal-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/legal-agent-wiki/manifest.yaml)
- [README.md](../wikis/legal-agent-wiki/README.md)
- [rules](../wikis/legal-agent-wiki/rules/)
- [source-notes.md](../wikis/legal-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official legal database, regulator website, licensed lawyer review.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Do not introduce final legal opinions or guaranteed outcomes.
- [ ] Preserve jurisdiction, date, source, and lawyer review points.
- [ ] Keep statutes, cases, regulations, and platform terms source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No final legal opinion is introduced; jurisdiction and lawyer review points remain visible.

Content targets:

- [source-notes.md](../wikis/legal-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/legal-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/legal-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-011",
  "ticket_id": "TICKET-SRC-011",
  "topic": "current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/legal-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-012 - security-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current CVEs, vendor advisories, patches, dependency versions and exploit status
- Category: `security_advisory`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/security-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/security-agent-wiki/manifest.yaml)
- [README.md](../wikis/security-agent-wiki/README.md)
- [rules](../wikis/security-agent-wiki/rules/)
- [source-notes.md](../wikis/security-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: vendor security advisory, official CVE record, package registry advisory.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Defensive review only.
- [ ] Do not add exploitation, persistence, evasion, credential theft, bypass steps, or payloads.
- [ ] Keep CVEs, advisories, patches, dependency versions, and exploit status source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No exploit, persistence, evasion, credential theft, or offensive procedure is introduced.

Content targets:

- [source-notes.md](../wikis/security-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/security-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-012",
  "ticket_id": "TICKET-SRC-012",
  "topic": "current CVEs, vendor advisories, patches, dependency versions and exploit status",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/security-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-013 - security-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current security tool rules, detection signatures, cloud defaults and compliance requirements
- Category: `policy_or_regulation`
- Target window: refresh first; do not use for current-fact answers until verified
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/security-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/security-agent-wiki/manifest.yaml)
- [README.md](../wikis/security-agent-wiki/README.md)
- [rules](../wikis/security-agent-wiki/rules/)
- [source-notes.md](../wikis/security-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official tool documentation, cloud provider security docs, compliance authority or auditor guidance.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Defensive review only.
- [ ] Do not add exploitation, persistence, evasion, credential theft, bypass steps, or payloads.
- [ ] Keep CVEs, advisories, patches, dependency versions, and exploit status source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.
- [ ] No exploit, persistence, evasion, credential theft, or offensive procedure is introduced.

Content targets:

- [source-notes.md](../wikis/security-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/security-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/security-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-013",
  "ticket_id": "TICKET-SRC-013",
  "topic": "current security tool rules, detection signatures, cloud defaults and compliance requirements",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/security-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

### wave-2

#### TICKET-SRC-014 - customs-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: exchange rates, tariff rates, tax rates and destination-specific fees
- Category: `market_or_platform_data`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/customs-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/customs-agent-wiki/manifest.yaml)
- [README.md](../wikis/customs-agent-wiki/README.md)
- [rules](../wikis/customs-agent-wiki/rules/)
- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: central bank or official exchange source, customs tariff system, destination country authority.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent document values or customs classifications.
- [ ] Keep OCR uncertainty, evidence snippets, confidence, and manual review points visible.
- [ ] Treat policy, tariff, HS code, and regulatory claims as source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/customs-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-014",
  "ticket_id": "TICKET-SRC-014",
  "topic": "exchange rates, tariff rates, tax rates and destination-specific fees",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/customs-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-015 - customs-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: latest HS codes, customs supervision conditions and declaration elements
- Category: `general_current_fact`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/customs-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/customs-agent-wiki/manifest.yaml)
- [README.md](../wikis/customs-agent-wiki/README.md)
- [rules](../wikis/customs-agent-wiki/rules/)
- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: customs authority website, official tariff database, licensed customs broker review.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent document values or customs classifications.
- [ ] Keep OCR uncertainty, evidence snippets, confidence, and manual review points visible.
- [ ] Treat policy, tariff, HS code, and regulatory claims as source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/customs-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-015",
  "ticket_id": "TICKET-SRC-015",
  "topic": "latest HS codes, customs supervision conditions and declaration elements",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/customs-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-016 - customs-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: latest import/export policy, inspection and quarantine requirements
- Category: `policy_or_regulation`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/customs-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/customs-agent-wiki/manifest.yaml)
- [README.md](../wikis/customs-agent-wiki/README.md)
- [rules](../wikis/customs-agent-wiki/rules/)
- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: customs and inspection authority announcement, destination country regulator, official trade compliance bulletin.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent document values or customs classifications.
- [ ] Keep OCR uncertainty, evidence snippets, confidence, and manual review points visible.
- [ ] Treat policy, tariff, HS code, and regulatory claims as source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/customs-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-016",
  "ticket_id": "TICKET-SRC-016",
  "topic": "latest import/export policy, inspection and quarantine requirements",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/customs-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-017 - customs-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: latest platform OCR model parameters and document template behavior
- Category: `technical_docs`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/customs-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/customs-agent-wiki/manifest.yaml)
- [README.md](../wikis/customs-agent-wiki/README.md)
- [rules](../wikis/customs-agent-wiki/rules/)
- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: OCR vendor documentation, internal extraction benchmark, manually reviewed sample set.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent document values or customs classifications.
- [ ] Keep OCR uncertainty, evidence snippets, confidence, and manual review points visible.
- [ ] Treat policy, tariff, HS code, and regulatory claims as source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/customs-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/customs-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/customs-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-017",
  "ticket_id": "TICKET-SRC-017",
  "topic": "latest platform OCR model parameters and document template behavior",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/customs-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-018 - ecommerce-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current marketplace policy, return window, category restrictions and consumer protection rules
- Category: `policy_or_regulation`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/ecommerce-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/ecommerce-agent-wiki/manifest.yaml)
- [README.md](../wikis/ecommerce-agent-wiki/README.md)
- [rules](../wikis/ecommerce-agent-wiki/rules/)
- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official marketplace policy center, consumer protection authority, merchant service agreement.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent price, stock, shipping, return policy, or platform policy.
- [ ] Respect privacy, consent, consumer protection, and platform rules.
- [ ] Keep unsupported product claims out of stable pages.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/ecommerce-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-018",
  "ticket_id": "TICKET-SRC-018",
  "topic": "current marketplace policy, return window, category restrictions and consumer protection rules",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/ecommerce-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-019 - ecommerce-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current product certification, recall, safety notice and warranty terms
- Category: `general_current_fact`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/ecommerce-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/ecommerce-agent-wiki/manifest.yaml)
- [README.md](../wikis/ecommerce-agent-wiki/README.md)
- [rules](../wikis/ecommerce-agent-wiki/rules/)
- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: brand official website, regulator recall database, warranty document.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent price, stock, shipping, return policy, or platform policy.
- [ ] Respect privacy, consent, consumer protection, and platform rules.
- [ ] Keep unsupported product claims out of stable pages.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/ecommerce-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-019",
  "ticket_id": "TICKET-SRC-019",
  "topic": "current product certification, recall, safety notice and warranty terms",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/ecommerce-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-020 - ecommerce-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current product price, stock, promotion, shipping fee and delivery ETA
- Category: `market_or_platform_data`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/ecommerce-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/ecommerce-agent-wiki/manifest.yaml)
- [README.md](../wikis/ecommerce-agent-wiki/README.md)
- [rules](../wikis/ecommerce-agent-wiki/rules/)
- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: platform product page, merchant backend, carrier tracking system.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not invent price, stock, shipping, return policy, or platform policy.
- [ ] Respect privacy, consent, consumer protection, and platform rules.
- [ ] Keep unsupported product claims out of stable pages.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/ecommerce-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/ecommerce-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/ecommerce-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-020",
  "ticket_id": "TICKET-SRC-020",
  "topic": "current product price, stock, promotion, shipping fee and delivery ETA",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/ecommerce-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-021 - nodeops-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current OS package, Docker, systemd and kernel behavior
- Category: `general_current_fact`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/nodeops-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/nodeops-agent-wiki/manifest.yaml)
- [README.md](../wikis/nodeops-agent-wiki/README.md)
- [rules](../wikis/nodeops-agent-wiki/rules/)
- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official documentation, local version output, release notes.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Require backup, rollback, and human confirmation for production changes.
- [ ] Do not record infrastructure secrets, node keys, mnemonics, or account tokens.
- [ ] Keep destructive operations out of automated instructions.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/nodeops-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-021",
  "ticket_id": "TICKET-SRC-021",
  "topic": "current OS package, Docker, systemd and kernel behavior",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/nodeops-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-022 - nodeops-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current blockchain node client versions, network parameters and upgrade requirements
- Category: `technical_docs`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/nodeops-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/nodeops-agent-wiki/manifest.yaml)
- [README.md](../wikis/nodeops-agent-wiki/README.md)
- [rules](../wikis/nodeops-agent-wiki/rules/)
- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official client release notes, chain foundation announcement, node logs and version output.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Require backup, rollback, and human confirmation for production changes.
- [ ] Do not record infrastructure secrets, node keys, mnemonics, or account tokens.
- [ ] Keep destructive operations out of automated instructions.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/nodeops-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-022",
  "ticket_id": "TICKET-SRC-022",
  "topic": "current blockchain node client versions, network parameters and upgrade requirements",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/nodeops-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-023 - nodeops-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current cloud provider limits, firewall behavior, billing and incident status
- Category: `general_current_fact`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: yes

Required reading:

- [AGENTS.md](../wikis/nodeops-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/nodeops-agent-wiki/manifest.yaml)
- [README.md](../wikis/nodeops-agent-wiki/README.md)
- [rules](../wikis/nodeops-agent-wiki/rules/)
- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: cloud provider documentation, status page, account console.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.
- [ ] Require human review before moving this ticket to verified.

Safety checks:

- [ ] Require backup, rollback, and human confirmation for production changes.
- [ ] Do not record infrastructure secrets, node keys, mnemonics, or account tokens.
- [ ] Keep destructive operations out of automated instructions.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/nodeops-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/nodeops-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/nodeops-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-023",
  "ticket_id": "TICKET-SRC-023",
  "topic": "current cloud provider limits, firewall behavior, billing and incident status",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/nodeops-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-024 - research-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current dataset availability, license, model weights and code repository status
- Category: `technical_docs`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/research-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/research-agent-wiki/manifest.yaml)
- [README.md](../wikis/research-agent-wiki/README.md)
- [rules](../wikis/research-agent-wiki/rules/)
- [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official dataset page, repository release notes, model card.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not fabricate citations, abstracts, datasets, benchmark results, or model claims.
- [ ] Keep source traceability, limitations, and uncertainty visible.
- [ ] Mark newest papers, datasets, leaderboards, and repositories as source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/research-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-024",
  "ticket_id": "TICKET-SRC-024",
  "topic": "current dataset availability, license, model weights and code repository status",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/research-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-025 - research-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: latest papers, preprints, revisions, citations and benchmark leaderboards
- Category: `general_current_fact`
- Target window: refresh after wave-1 before operational rollout
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/research-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/research-agent-wiki/manifest.yaml)
- [README.md](../wikis/research-agent-wiki/README.md)
- [rules](../wikis/research-agent-wiki/rules/)
- [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: publisher page, arXiv or conference page, official benchmark leaderboard.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not fabricate citations, abstracts, datasets, benchmark results, or model claims.
- [ ] Keep source traceability, limitations, and uncertainty visible.
- [ ] Mark newest papers, datasets, leaderboards, and repositories as source-gated.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/research-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/research-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/research-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-025",
  "ticket_id": "TICKET-SRC-025",
  "topic": "latest papers, preprints, revisions, citations and benchmark leaderboards",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/research-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

### wave-3

#### TICKET-SRC-026 - agent-engineering-wiki

- Status: `open_pending_source_refresh`
- Topic: current Codex Skill format, plugin behavior and tool capabilities
- Category: `technical_docs`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/agent-engineering-wiki/AGENTS.md)
- [manifest.yaml](../wikis/agent-engineering-wiki/manifest.yaml)
- [README.md](../wikis/agent-engineering-wiki/README.md)
- [rules](../wikis/agent-engineering-wiki/rules/)
- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official documentation, product changelog, local plugin manifest.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not add hidden instructions or unreviewed agent authority.
- [ ] Keep model, API, MCP, tool schema, and platform behavior source-gated.
- [ ] Preserve eval and source-grounding requirements.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/agent-engineering-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-026",
  "ticket_id": "TICKET-SRC-026",
  "topic": "current Codex Skill format, plugin behavior and tool capabilities",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/agent-engineering-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-027 - agent-engineering-wiki

- Status: `open_pending_source_refresh`
- Topic: current RAG frameworks, embedding models, vector databases and rerankers
- Category: `technical_docs`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/agent-engineering-wiki/AGENTS.md)
- [manifest.yaml](../wikis/agent-engineering-wiki/manifest.yaml)
- [README.md](../wikis/agent-engineering-wiki/README.md)
- [rules](../wikis/agent-engineering-wiki/rules/)
- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official documentation, release notes, benchmark report with date.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not add hidden instructions or unreviewed agent authority.
- [ ] Keep model, API, MCP, tool schema, and platform behavior source-gated.
- [ ] Preserve eval and source-grounding requirements.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/agent-engineering-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-027",
  "ticket_id": "TICKET-SRC-027",
  "topic": "current RAG frameworks, embedding models, vector databases and rerankers",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/agent-engineering-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-028 - agent-engineering-wiki

- Status: `open_pending_source_refresh`
- Topic: current eval harnesses, model APIs and MCP/tool schemas
- Category: `technical_docs`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/agent-engineering-wiki/AGENTS.md)
- [manifest.yaml](../wikis/agent-engineering-wiki/manifest.yaml)
- [README.md](../wikis/agent-engineering-wiki/README.md)
- [rules](../wikis/agent-engineering-wiki/rules/)
- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official API documentation, tool schema, repository release notes.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not add hidden instructions or unreviewed agent authority.
- [ ] Keep model, API, MCP, tool schema, and platform behavior source-gated.
- [ ] Preserve eval and source-grounding requirements.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/agent-engineering-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/agent-engineering-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/agent-engineering-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-028",
  "ticket_id": "TICKET-SRC-028",
  "topic": "current eval harnesses, model APIs and MCP/tool schemas",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/agent-engineering-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-029 - coding-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current OpenAI, Codex, GitHub or Vercel product behavior
- Category: `general_current_fact`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/coding-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/coding-agent-wiki/manifest.yaml)
- [README.md](../wikis/coding-agent-wiki/README.md)
- [rules](../wikis/coding-agent-wiki/rules/)
- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official product documentation, changelog, repository or API docs.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not record secrets, tokens, cookies, private keys, or private repository data.
- [ ] Keep dependency, API, CLI, platform, and security-advisory claims source-gated.
- [ ] Preserve test and deployment verification commands.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/coding-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-029",
  "ticket_id": "TICKET-SRC-029",
  "topic": "current OpenAI, Codex, GitHub or Vercel product behavior",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/coding-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-030 - coding-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current cloud platform build, deploy, runtime and pricing behavior
- Category: `general_current_fact`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/coding-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/coding-agent-wiki/manifest.yaml)
- [README.md](../wikis/coding-agent-wiki/README.md)
- [rules](../wikis/coding-agent-wiki/rules/)
- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official platform documentation, status page, project deployment logs.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not record secrets, tokens, cookies, private keys, or private repository data.
- [ ] Keep dependency, API, CLI, platform, and security-advisory claims source-gated.
- [ ] Preserve test and deployment verification commands.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/coding-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-030",
  "ticket_id": "TICKET-SRC-030",
  "topic": "current cloud platform build, deploy, runtime and pricing behavior",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/coding-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-031 - coding-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current dependency vulnerabilities and security advisories
- Category: `security_advisory`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/coding-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/coding-agent-wiki/manifest.yaml)
- [README.md](../wikis/coding-agent-wiki/README.md)
- [rules](../wikis/coding-agent-wiki/rules/)
- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official security advisory, package registry advisory, vendor bulletin.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not record secrets, tokens, cookies, private keys, or private repository data.
- [ ] Keep dependency, API, CLI, platform, and security-advisory claims source-gated.
- [ ] Preserve test and deployment verification commands.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/coding-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-031",
  "ticket_id": "TICKET-SRC-031",
  "topic": "current dependency vulnerabilities and security advisories",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/coding-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-032 - coding-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current framework, library, CLI and API parameters
- Category: `technical_docs`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/coding-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/coding-agent-wiki/manifest.yaml)
- [README.md](../wikis/coding-agent-wiki/README.md)
- [rules](../wikis/coding-agent-wiki/rules/)
- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: official documentation, release notes, source repository.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not record secrets, tokens, cookies, private keys, or private repository data.
- [ ] Keep dependency, API, CLI, platform, and security-advisory claims source-gated.
- [ ] Preserve test and deployment verification commands.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/coding-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/coding-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/coding-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-032",
  "ticket_id": "TICKET-SRC-032",
  "topic": "current framework, library, CLI and API parameters",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/coding-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-033 - content-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current image, chart, dataset and quote licensing
- Category: `general_current_fact`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/content-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/content-agent-wiki/manifest.yaml)
- [README.md](../wikis/content-agent-wiki/README.md)
- [rules](../wikis/content-agent-wiki/rules/)
- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: license document, rights holder page, source terms of use.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not fabricate citations, quotes, current events, or statistics.
- [ ] Keep licensing, platform rules, and factual claims source-gated.
- [ ] Separate fact, inference, opinion, and draft language.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/content-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-033",
  "ticket_id": "TICKET-SRC-033",
  "topic": "current image, chart, dataset and quote licensing",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/content-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-034 - content-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current news, statistics, public quotes and social media claims
- Category: `general_current_fact`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/content-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/content-agent-wiki/manifest.yaml)
- [README.md](../wikis/content-agent-wiki/README.md)
- [rules](../wikis/content-agent-wiki/rules/)
- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: primary source, official data release, dated reputable reporting.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not fabricate citations, quotes, current events, or statistics.
- [ ] Keep licensing, platform rules, and factual claims source-gated.
- [ ] Separate fact, inference, opinion, and draft language.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/content-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-034",
  "ticket_id": "TICKET-SRC-034",
  "topic": "current news, statistics, public quotes and social media claims",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/content-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

#### TICKET-SRC-035 - content-agent-wiki

- Status: `open_pending_source_refresh`
- Topic: current publishing platform rules, format limits and content policies
- Category: `policy_or_regulation`
- Target window: batch refresh is acceptable before broad reuse
- Human confirmation required: no

Required reading:

- [AGENTS.md](../wikis/content-agent-wiki/AGENTS.md)
- [manifest.yaml](../wikis/content-agent-wiki/manifest.yaml)
- [README.md](../wikis/content-agent-wiki/README.md)
- [rules](../wikis/content-agent-wiki/rules/)
- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)

Source policy:

- [ ] Prefer official, primary, dated sources.
- [ ] Start from suggested source types: platform policy center, creator documentation, account dashboard notices.
- [ ] Do not use unsourced summaries as the only authority.
- [ ] Record publication/update date and access date.

Safety checks:

- [ ] Do not fabricate citations, quotes, current events, or statistics.
- [ ] Keep licensing, platform rules, and factual claims source-gated.
- [ ] Separate fact, inference, opinion, and draft language.

Acceptance criteria:

- [ ] No current fact is written without a dated source note.
- [ ] No API key, private key, cookie, credential, or private account data is recorded.
- [ ] Any remaining uncertainty is explicitly marked needs-source-update.
- [ ] The relevant update-log.md records the change.

Content targets:

- [source-notes.md](../wikis/content-agent-wiki/sources/source-notes.md)
- [source-refresh-log.md](../wikis/content-agent-wiki/sources/source-refresh-log.md)
- [update-log.md](../wikis/content-agent-wiki/update-log.md)
- `docs/SOURCE_UPDATE_QUEUE.md`
- `registry/source-update-queue.json`

Evidence template:

```json
{
  "task_id": "SRC-035",
  "ticket_id": "TICKET-SRC-035",
  "topic": "current publishing platform rules, format limits and content policies",
  "status": "pending | verified | unchanged | still-needs-source-update | rejected",
  "verified_on": "YYYY-MM-DD",
  "source_title": "<source title>",
  "source_publisher": "<official publisher or authority>",
  "source_url_or_reference": "<URL or local reference>",
  "source_published_or_updated": "YYYY-MM-DD | unknown",
  "source_accessed_on": "YYYY-MM-DD",
  "evidence_summary": "<what the source supports and what it does not support>",
  "affected_pages": [
    "wikis/content-agent-wiki/sources/source-notes.md"
  ],
  "confidence": "low | medium | high",
  "remaining_uncertainty": "<unknown, conflicting, stale, or out-of-scope facts>",
  "human_reviewer": "<required for high-risk tickets>",
  "follow_up": "<next action or none>"
}
```

## Post-Update Commands

```bash
python3 scripts/list_source_updates.py
python3 scripts/generate_source_refresh_playbook.py
python3 scripts/generate_source_refresh_tickets.py
python3 scripts/generate_source_refresh_logs.py
python3 scripts/audit_source_refresh_completion.py
python3 scripts/update_index.py
python3 scripts/run_acceptance.py
```

## Safety Boundary

- Do not write current prices, policies, laws, medical guidance, platform rules, API parameters, CVEs, or Web3 project facts without dated source evidence.
- Do not record API keys, private keys, cookies, credentials, seed phrases, or private account data.
- Keep human confirmation points for high-risk finance, legal, health, security, airdrop, and operations tasks.
