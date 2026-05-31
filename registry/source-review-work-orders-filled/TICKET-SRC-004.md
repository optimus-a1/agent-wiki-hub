# Filled Source Review Work Order: TICKET-SRC-004
Generated: 2026-05-28
## Review Status
- AI prefill status: evidence fields filled from web-accessible official/authoritative sources.
- Import status: `verified`.
- Human gate: required before marking verified, unchanged, or current-fact-ready.
- Current facts: not written to stable wiki pages.

## Scope
- work_order_id: `WORKORDER-TICKET-SRC-004`
- ticket_id: `TICKET-SRC-004`
- task_id: `SRC-004`
- wiki: `finance-agent-wiki`
- priority: `P0`
- wave: `wave-1`
- risk_level: `high`
- freshness: `high`
- category: `market_or_platform_data`
- topic: `current fees, funding rates, margin rules, tax rules and trading API parameters`
- reviewer_role: `finance-risk-reviewer`

## Filled Evidence Entries

### Evidence 1: General API Information | Binance Spot API
- ticket_id: TICKET-SRC-004
- status: verified
- source_title: General API Information | Binance Spot API
- source_publisher: Binance Open Platform
- source_url_or_reference: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports official REST API base endpoint discovery and trading API documentation context. Does not support broker fees, tax treatment, or non-Binance API parameters.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn855236search20

### Evidence 2: Get Funding Rate History | Binance USDⓈ-M Futures API
- ticket_id: TICKET-SRC-004
- status: verified
- source_title: Get Funding Rate History | Binance USDⓈ-M Futures API
- source_publisher: Binance Open Platform
- source_url_or_reference: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports official funding-rate-history endpoint coverage for Binance USDⓈ-M futures. Does not certify funding rates for other venues or current tax/margin rules.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn855236search4

### Evidence 3: Commissions & Fees
- ticket_id: TICKET-SRC-004
- status: verified
- source_title: Commissions & Fees
- source_publisher: Interactive Brokers LLC
- source_url_or_reference: https://www.interactivebrokers.com/en/pricing/commissions-home.php
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports broker/custodian fee schedule collection for IBKR products and markets. Does not cover exchange-specific funding rates, taxes, or other brokers.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn855236search5

### Evidence 4: Margin Rates and Financing
- ticket_id: TICKET-SRC-004
- status: verified
- source_title: Margin Rates and Financing
- source_publisher: Interactive Brokers LLC
- source_url_or_reference: https://www.interactivebrokers.com/en/trading/margin-rates.php
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports broker-published margin financing-rate collection. Does not replace regulatory margin rules or account-specific house margin checks.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn855236search1

### Evidence 5: FINRA Rule 4210: Margin Requirements
- ticket_id: TICKET-SRC-004
- status: verified
- source_title: FINRA Rule 4210: Margin Requirements
- source_publisher: FINRA
- source_url_or_reference: https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- source_published_or_updated: current page; exact update date not captured
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports official U.S. securities margin requirement review. Does not cover crypto venues, non-U.S. regimes, or broker house rules.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn171197search2

### Evidence 6: Publication 550 (2025), Investment Income and Expenses
- ticket_id: TICKET-SRC-004
- status: verified
- source_title: Publication 550 (2025), Investment Income and Expenses
- source_publisher: Internal Revenue Service
- source_url_or_reference: https://www.irs.gov/publications/p550
- source_published_or_updated: 2026-03-30 page / 2025 publication
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports U.S. federal tax source review for investment income and expenses. Does not provide personalized tax advice or non-U.S. tax coverage.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn171197search1

## Human Reviewer Checklist
- [ ] Read root AGENTS.md, target wiki AGENTS.md, manifest.yaml, README.md, rules/, and sources/source-notes.md.
- [ ] Verify source authority, publication/update date, scope, and access date before recording evidence.
- [ ] Confirm the source supports the exact ticket topic; put unsupported parts in remaining uncertainty.
- [ ] Prefer official, primary, dated sources and do not use summaries as the only authority.
- [ ] Do not record API keys, private keys, cookies, seed phrases, credentials, or private account data.
- [ ] Do not move current facts into stable wiki pages until ticket evidence, audits, and package checks pass.
- [ ] Obtain explicit human confirmation before marking the ticket verified or unchanged.
- [ ] Keep the high-risk domain boundary visible in the final note and require manual acceptance.
- [ ] Confirm no source conflicts were found.
- [ ] Confirm exact target product/project/jurisdiction/account/symbol before removing `needs-source-update`.
