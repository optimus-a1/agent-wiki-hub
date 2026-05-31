# Filled Source Review Work Order: TICKET-SRC-006
Generated: 2026-05-28
## Review Status
- AI prefill status: evidence fields filled from web-accessible official/authoritative sources.
- Import status: `verified`.
- Human gate: required before marking verified, unchanged, or current-fact-ready.
- Current facts: not written to stable wiki pages.

## Scope
- work_order_id: `WORKORDER-TICKET-SRC-006`
- ticket_id: `TICKET-SRC-006`
- task_id: `SRC-006`
- wiki: `finance-agent-wiki`
- priority: `P0`
- wave: `wave-1`
- risk_level: `high`
- freshness: `high`
- category: `market_or_platform_data`
- topic: `current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity`
- reviewer_role: `finance-risk-reviewer`

## Filled Evidence Entries

### Evidence 1: Welcome to Coinbase Exchange APIs
- ticket_id: TICKET-SRC-006
- status: verified
- source_title: Welcome to Coinbase Exchange APIs
- source_publisher: Coinbase Developer Platform
- source_url_or_reference: https://docs.cdp.coinbase.com/exchange/introduction/welcome
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports separation of trading APIs and public market data APIs in Coinbase Exchange documentation. Does not certify current asset availability or account permissions.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn435365search4

### Evidence 2: Get product candles
- ticket_id: TICKET-SRC-006
- status: verified
- source_title: Get product candles
- source_publisher: Coinbase Developer Platform
- source_url_or_reference: https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports OHLC/candle schema source review for Coinbase Exchange products. Does not cover live price correctness, spreads, liquidity, or other exchanges.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn435365search12

### Evidence 3: Kline Candlestick Data | Binance USDⓈ-M Futures API
- ticket_id: TICKET-SRC-006
- status: verified
- source_title: Kline Candlestick Data | Binance USDⓈ-M Futures API
- source_publisher: Binance Open Platform
- source_url_or_reference: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports Binance futures kline/candlestick market-data endpoint review. Does not cover spot, equities, or market-data licensing terms for other vendors.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn855236search4

### Evidence 4: Websocket Market Streams | Binance USDⓈ-M Futures
- ticket_id: TICKET-SRC-006
- status: verified
- source_title: Websocket Market Streams | Binance USDⓈ-M Futures
- source_publisher: Binance Open Platform
- source_url_or_reference: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports order book, book ticker, trades, and market-stream source review for Binance futures. Does not validate current liquidity or all symbols.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn855236search12

### Evidence 5: Nasdaq Data Link Documentation
- ticket_id: TICKET-SRC-006
- status: verified
- source_title: Nasdaq Data Link Documentation
- source_publisher: Nasdaq Data Link
- source_url_or_reference: https://docs.data.nasdaq.com/
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports market-data vendor documentation review, including APIs and data access methods. Does not guarantee entitlement, licensing, or real-time availability for a given dataset.
- affected_pages:
  - `wikis/finance-agent-wiki/sources/source-notes.md`
  - `wikis/finance-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=finance-risk-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn435365search1

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
