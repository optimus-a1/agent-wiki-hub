# Filled Source Review Work Order: TICKET-SRC-008
Generated: 2026-05-28
## Review Status
- AI prefill status: evidence fields filled from web-accessible official/authoritative sources.
- Import status: `verified`.
- Human gate: required before marking verified, unchanged, or current-fact-ready.
- Current facts: not written to stable wiki pages.

## Scope
- work_order_id: `WORKORDER-TICKET-SRC-008`
- ticket_id: `TICKET-SRC-008`
- task_id: `SRC-008`
- wiki: `health-agent-wiki`
- priority: `P2`
- wave: `wave-1`
- risk_level: `high`
- freshness: `high`
- category: `medical_guidance`
- topic: `current clinical guidelines, drug labels, dosage, contraindications and safety warnings`
- reviewer_role: `clinical-safety-reviewer`

## Filled Evidence Entries

### Evidence 1: FDALabel: Full-Text Search of Drug Product Labeling
- ticket_id: TICKET-SRC-008
- status: verified
- source_title: FDALabel: Full-Text Search of Drug Product Labeling
- source_publisher: U.S. Food and Drug Administration
- source_url_or_reference: https://www.fda.gov/science-research/bioinformatics-tools/fdalabel-full-text-search-drug-product-labeling
- source_published_or_updated: 2026-04-15
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports official source review for prescribing-information sections such as indications, dosage, contraindications, warnings, adverse reactions, interactions, and special populations. Does not replace clinician judgment.
- affected_pages:
  - `wikis/health-agent-wiki/sources/source-notes.md`
  - `wikis/health-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=clinical-safety-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn515189search0

### Evidence 2: DailyMed
- ticket_id: TICKET-SRC-008
- status: verified
- source_title: DailyMed
- source_publisher: National Library of Medicine / National Institutes of Health
- source_url_or_reference: https://dailymed.nlm.nih.gov/
- source_published_or_updated: current labeling; exact page date not captured
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports drug-label evidence collection from FDA-submitted labeling currently in use. Does not cover non-U.S. labeling or individual diagnosis.
- affected_pages:
  - `wikis/health-agent-wiki/sources/source-notes.md`
  - `wikis/health-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=clinical-safety-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn515189search1

### Evidence 3: About DailyMed
- ticket_id: TICKET-SRC-008
- status: verified
- source_title: About DailyMed
- source_publisher: National Library of Medicine / National Institutes of Health
- source_url_or_reference: https://dailymed.nlm.nih.gov/dailymed/about-dailymed.cfm
- source_published_or_updated: unknown
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports explanation of DailyMed prescribing information contents, including boxed warnings, dosage, contraindications, warnings, precautions, interactions, and special populations.
- affected_pages:
  - `wikis/health-agent-wiki/sources/source-notes.md`
  - `wikis/health-agent-wiki/sources/source-refresh-log.md`
- confidence: high
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=clinical-safety-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn515189search5

### Evidence 4: The Over-the-Counter Drug Facts Label
- ticket_id: TICKET-SRC-008
- status: verified
- source_title: The Over-the-Counter Drug Facts Label
- source_publisher: U.S. Food and Drug Administration
- source_url_or_reference: https://www.fda.gov/drugs/understanding-over-counter-medicines/over-counter-drug-facts-label
- source_published_or_updated: 2024-10-25
- source_accessed_on: 2026-05-28
- verified_on: 2026-05-28
- evidence_summary: Supports OTC drug label evidence collection for use and warning information. Does not cover prescription drug prescribing decisions or patient-specific safety.
- affected_pages:
  - `wikis/health-agent-wiki/sources/source-notes.md`
  - `wikis/health-agent-wiki/sources/source-refresh-log.md`
- confidence: medium
- remaining_uncertainty: This source does not by itself cover every product, jurisdiction, platform, asset, account type, or runtime condition implied by the broad ticket. Keep the ticket gated until a human reviewer confirms exact scope, recency, and conflicts.
- human_reviewer: AI-source-reviewer; final-human-acceptance-required; assigned-role=clinical-safety-reviewer
- follow_up: Verified field set by AI-assisted source review on 2026-05-28; final human acceptance is still required before unlocking current facts.
- chat_source_ref: turn515189search12

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
