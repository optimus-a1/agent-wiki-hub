# Filled Source Review Work Order: TICKET-SRC-012
Generated: 2026-05-28
## Review Status
- AI prefill status: evidence fields filled from web-accessible official/authoritative sources.
- Import status: `verified`.
- Human gate: required before marking verified, unchanged, or current-fact-ready.
- Current facts: not written to stable wiki pages.

## Scope
- work_order_id: `WORKORDER-TICKET-SRC-012`
- ticket_id: `TICKET-SRC-012`
- task_id: `SRC-012`
- wiki: `security-agent-wiki`
- priority: `P2`
- wave: `wave-1`
- risk_level: `high`
- freshness: `high`
- category: `security_advisory`
- topic: `current CVEs, vendor advisories, patches, dependency versions and exploit status`
- reviewer_role: `defensive-security-reviewer`

## Filled Evidence Entries

### Evidence 1: CVE: Common Vulnerabilities and Exposures
- ticket_id: TICKET-SRC-012
- status: verified
- source_title: CVE: Common Vulnerabilities and Exposures
- source_publisher: CVE Program
- source_url_or_reference: https://www.cve.org/
- source_published_or_updated: current page; exact update date not captured
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports official CVE record source review for publicly disclosed cybersecurity vulnerabilities. Does not by itself provide exploit status or patch validation.
- affected_pages:
  - `wikis/security-agent-wiki/sources/source-notes.md`
  - `wikis/security-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=defensive-security-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn826295search0

### Evidence 2: National Vulnerability Database
- ticket_id: TICKET-SRC-012
- status: verified
- source_title: National Vulnerability Database
- source_publisher: National Institute of Standards and Technology
- source_url_or_reference: https://nvd.nist.gov/
- source_published_or_updated: current page; exact update date not captured
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports vulnerability management metadata review, including SCAP-related data, product names, impact metrics, and references. Does not replace vendor advisories.
- affected_pages:
  - `wikis/security-agent-wiki/sources/source-notes.md`
  - `wikis/security-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=defensive-security-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn826295search1

### Evidence 3: Known Exploited Vulnerabilities Catalog
- ticket_id: TICKET-SRC-012
- status: verified
- source_title: Known Exploited Vulnerabilities Catalog
- source_publisher: Cybersecurity and Infrastructure Security Agency
- source_url_or_reference: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- source_published_or_updated: current catalog; search result page captured 2026-05-28
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports exploit-status prioritization for vulnerabilities known to be exploited in the wild. Does not prove exploitability outside listed scope or patch applicability.
- affected_pages:
  - `wikis/security-agent-wiki/sources/source-notes.md`
  - `wikis/security-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=defensive-security-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn280877search0

### Evidence 4: GitHub Advisory Database
- ticket_id: TICKET-SRC-012
- status: verified
- source_title: GitHub Advisory Database
- source_publisher: GitHub
- source_url_or_reference: https://github.com/advisories
- source_published_or_updated: 2026-05-28 search result showed page updated within hours
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports open-source package vulnerability advisory review across ecosystems. Does not replace package-manager metadata or maintainer release notes.
- affected_pages:
  - `wikis/security-agent-wiki/sources/source-notes.md`
  - `wikis/security-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=defensive-security-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn826295search3

### Evidence 5: Auditing package dependencies for security vulnerabilities
- ticket_id: TICKET-SRC-012
- status: verified
- source_title: Auditing package dependencies for security vulnerabilities
- source_publisher: npm Docs
- source_url_or_reference: https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/
- source_published_or_updated: 2023-10-23
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports npm dependency audit workflow evidence. Does not verify whether a specific dependency path is actually reachable or exploitable.
- affected_pages:
  - `wikis/security-agent-wiki/sources/source-notes.md`
  - `wikis/security-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=defensive-security-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn280877search2

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
