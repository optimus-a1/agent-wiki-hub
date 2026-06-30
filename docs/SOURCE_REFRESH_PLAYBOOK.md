# Source Refresh Playbook

Generated: 2026-06-30

## Purpose

This playbook turns `needs-source-update` topics into source verification tasks. It does not certify any current fact by itself.

## Summary

- Tasks: 35
- Source queue: `registry/source-update-queue.json`

## Waves

| Wave | Tasks | Meaning |
| --- | ---: | --- |
| wave-1 | 22 | Highest risk or freshness pressure; refresh first. |
| wave-2 | 3 | Important operational topics; refresh after wave-1. |
| wave-3 | 10 | Medium cadence topics; batch refresh is acceptable. |

## Task List

| Task | Wave | Wiki | Priority | Category | Human confirmation | Topic |
| --- | --- | --- | ---: | --- | --- | --- |
| SRC-001 | wave-1 | airdrop-agent-wiki | 9 | web3_project_status | yes | current contract addresses, wallet warnings, scam reports and signing risks |
| SRC-002 | wave-1 | airdrop-agent-wiki | 9 | policy_or_regulation | yes | current project status, official links, task rules, snapshot and eligibility |
| SRC-003 | wave-1 | airdrop-agent-wiki | 9 | web3_project_status | yes | current token launch, TGE, funding, exchange listing and airdrop allocation |
| SRC-004 | wave-1 | finance-agent-wiki | 9 | market_or_platform_data | yes | current fees, funding rates, margin rules, tax rules and trading API parameters |
| SRC-005 | wave-1 | finance-agent-wiki | 9 | policy_or_regulation | yes | current legal, regulatory or suitability requirements for financial products |
| SRC-006 | wave-1 | finance-agent-wiki | 9 | market_or_platform_data | yes | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| SRC-007 | wave-1 | finance-agent-wiki | 9 | general_current_fact | yes | latest financial statements, filings, restatements and audit opinions |
| SRC-008 | wave-1 | health-agent-wiki | 9 | medical_guidance | yes | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| SRC-009 | wave-1 | health-agent-wiki | 9 | medical_guidance | yes | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| SRC-010 | wave-1 | legal-agent-wiki | 9 | policy_or_regulation | yes | current platform agreements, data processing terms and consumer protection rules |
| SRC-011 | wave-1 | legal-agent-wiki | 9 | policy_or_regulation | yes | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements |
| SRC-012 | wave-1 | security-agent-wiki | 9 | security_advisory | yes | current CVEs, vendor advisories, patches, dependency versions and exploit status |
| SRC-013 | wave-1 | security-agent-wiki | 9 | policy_or_regulation | yes | current security tool rules, detection signatures, cloud defaults and compliance requirements |
| SRC-014 | wave-1 | customs-agent-wiki | 8 | market_or_platform_data | no | exchange rates, tariff rates, tax rates and destination-specific fees |
| SRC-015 | wave-1 | customs-agent-wiki | 8 | general_current_fact | no | latest HS codes, customs supervision conditions and declaration elements |
| SRC-016 | wave-1 | customs-agent-wiki | 8 | policy_or_regulation | no | latest import/export policy, inspection and quarantine requirements |
| SRC-017 | wave-1 | customs-agent-wiki | 8 | technical_docs | no | latest platform OCR model parameters and document template behavior |
| SRC-018 | wave-1 | ecommerce-agent-wiki | 8 | policy_or_regulation | no | current marketplace policy, return window, category restrictions and consumer protection rules |
| SRC-019 | wave-1 | ecommerce-agent-wiki | 8 | general_current_fact | no | current product certification, recall, safety notice and warranty terms |
| SRC-020 | wave-1 | ecommerce-agent-wiki | 8 | market_or_platform_data | no | current product price, stock, promotion, shipping fee and delivery ETA |
| SRC-021 | wave-1 | research-agent-wiki | 8 | technical_docs | no | current dataset availability, license, model weights and code repository status |
| SRC-022 | wave-1 | research-agent-wiki | 8 | general_current_fact | no | latest papers, preprints, revisions, citations and benchmark leaderboards |
| SRC-023 | wave-2 | nodeops-agent-wiki | 7 | general_current_fact | yes | current OS package, Docker, systemd and kernel behavior |
| SRC-024 | wave-2 | nodeops-agent-wiki | 7 | technical_docs | yes | current blockchain node client versions, network parameters and upgrade requirements |
| SRC-025 | wave-2 | nodeops-agent-wiki | 7 | general_current_fact | yes | current cloud provider limits, firewall behavior, billing and incident status |
| SRC-026 | wave-3 | agent-engineering-wiki | 6 | technical_docs | no | current Codex Skill format, plugin behavior and tool capabilities |
| SRC-027 | wave-3 | agent-engineering-wiki | 6 | technical_docs | no | current RAG frameworks, embedding models, vector databases and rerankers |
| SRC-028 | wave-3 | agent-engineering-wiki | 6 | technical_docs | no | current eval harnesses, model APIs and MCP/tool schemas |
| SRC-029 | wave-3 | coding-agent-wiki | 6 | general_current_fact | no | current OpenAI, Codex, GitHub or Vercel product behavior |
| SRC-030 | wave-3 | coding-agent-wiki | 6 | general_current_fact | no | current cloud platform build, deploy, runtime and pricing behavior |
| SRC-031 | wave-3 | coding-agent-wiki | 6 | security_advisory | no | current dependency vulnerabilities and security advisories |
| SRC-032 | wave-3 | coding-agent-wiki | 6 | technical_docs | no | current framework, library, CLI and API parameters |
| SRC-033 | wave-3 | content-agent-wiki | 5 | general_current_fact | no | current image, chart, dataset and quote licensing |
| SRC-034 | wave-3 | content-agent-wiki | 5 | general_current_fact | no | current news, statistics, public quotes and social media claims |
| SRC-035 | wave-3 | content-agent-wiki | 5 | policy_or_regulation | no | current publishing platform rules, format limits and content policies |

## Wave Details

### wave-1

#### SRC-001 - airdrop-agent-wiki

- Topic: current contract addresses, wallet warnings, scam reports and signing risks
- Category: web3_project_status
- Source notes: `wikis/airdrop-agent-wiki/sources/source-notes.md`
- Suggested sources: official contract registry, block explorer, wallet security warning
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official contract registry, block explorer, wallet security warning.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.

#### SRC-002 - airdrop-agent-wiki

- Topic: current project status, official links, task rules, snapshot and eligibility
- Category: policy_or_regulation
- Source notes: `wikis/airdrop-agent-wiki/sources/source-notes.md`
- Suggested sources: official website, official documentation, official announcement channel
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official website, official documentation, official announcement channel.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.

#### SRC-003 - airdrop-agent-wiki

- Topic: current token launch, TGE, funding, exchange listing and airdrop allocation
- Category: web3_project_status
- Source notes: `wikis/airdrop-agent-wiki/sources/source-notes.md`
- Suggested sources: project announcement, exchange official announcement, primary funding disclosure
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: project announcement, exchange official announcement, primary funding disclosure.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No Sybil evasion, spam, fake identity, or platform-rule bypass guidance is introduced.

#### SRC-004 - finance-agent-wiki

- Topic: current fees, funding rates, margin rules, tax rules and trading API parameters
- Category: market_or_platform_data
- Source notes: `wikis/finance-agent-wiki/sources/source-notes.md`
- Suggested sources: official exchange documentation, regulator announcement, broker or custodian fee schedule
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official exchange documentation, regulator announcement, broker or custodian fee schedule.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No personalized investment advice or autonomous real-money execution is introduced.

#### SRC-005 - finance-agent-wiki

- Topic: current legal, regulatory or suitability requirements for financial products
- Category: policy_or_regulation
- Source notes: `wikis/finance-agent-wiki/sources/source-notes.md`
- Suggested sources: regulator website, licensed professional review, official product documents
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: regulator website, licensed professional review, official product documents.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No personalized investment advice or autonomous real-money execution is introduced.

#### SRC-006 - finance-agent-wiki

- Topic: current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity
- Category: market_or_platform_data
- Source notes: `wikis/finance-agent-wiki/sources/source-notes.md`
- Suggested sources: primary exchange or market data vendor, official issuer or exchange data portal, timestamped raw dataset
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: primary exchange or market data vendor, official issuer or exchange data portal, timestamped raw dataset.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No personalized investment advice or autonomous real-money execution is introduced.

#### SRC-007 - finance-agent-wiki

- Topic: latest financial statements, filings, restatements and audit opinions
- Category: general_current_fact
- Source notes: `wikis/finance-agent-wiki/sources/source-notes.md`
- Suggested sources: company investor relations, securities regulator filing system, audited annual or interim report
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: company investor relations, securities regulator filing system, audited annual or interim report.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No personalized investment advice or autonomous real-money execution is introduced.

#### SRC-008 - health-agent-wiki

- Topic: current clinical guidelines, drug labels, dosage, contraindications and safety warnings
- Category: medical_guidance
- Source notes: `wikis/health-agent-wiki/sources/source-notes.md`
- Suggested sources: official health authority, drug regulator label, professional clinical guideline
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official health authority, drug regulator label, professional clinical guideline.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No diagnosis or treatment instruction is introduced; clinician confirmation points remain visible.

#### SRC-009 - health-agent-wiki

- Topic: current public health guidance, screening recommendations and nutrition/exercise guidelines
- Category: medical_guidance
- Source notes: `wikis/health-agent-wiki/sources/source-notes.md`
- Suggested sources: public health authority, professional medical society, licensed clinician review
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: public health authority, professional medical society, licensed clinician review.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No diagnosis or treatment instruction is introduced; clinician confirmation points remain visible.

#### SRC-010 - legal-agent-wiki

- Topic: current platform agreements, data processing terms and consumer protection rules
- Category: policy_or_regulation
- Source notes: `wikis/legal-agent-wiki/sources/source-notes.md`
- Suggested sources: official platform terms, regulator guidance, counsel-approved template
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official platform terms, regulator guidance, counsel-approved template.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No final legal opinion is introduced; jurisdiction and lawyer review points remain visible.

#### SRC-011 - legal-agent-wiki

- Topic: current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements
- Category: policy_or_regulation
- Source notes: `wikis/legal-agent-wiki/sources/source-notes.md`
- Suggested sources: official legal database, regulator website, licensed lawyer review
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official legal database, regulator website, licensed lawyer review.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No final legal opinion is introduced; jurisdiction and lawyer review points remain visible.

#### SRC-012 - security-agent-wiki

- Topic: current CVEs, vendor advisories, patches, dependency versions and exploit status
- Category: security_advisory
- Source notes: `wikis/security-agent-wiki/sources/source-notes.md`
- Suggested sources: vendor security advisory, official CVE record, package registry advisory
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: vendor security advisory, official CVE record, package registry advisory.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No exploit, persistence, evasion, credential theft, or offensive procedure is introduced.

#### SRC-013 - security-agent-wiki

- Topic: current security tool rules, detection signatures, cloud defaults and compliance requirements
- Category: policy_or_regulation
- Source notes: `wikis/security-agent-wiki/sources/source-notes.md`
- Suggested sources: official tool documentation, cloud provider security docs, compliance authority or auditor guidance
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official tool documentation, cloud provider security docs, compliance authority or auditor guidance.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.
- No exploit, persistence, evasion, credential theft, or offensive procedure is introduced.

#### SRC-014 - customs-agent-wiki

- Topic: exchange rates, tariff rates, tax rates and destination-specific fees
- Category: market_or_platform_data
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- Suggested sources: central bank or official exchange source, customs tariff system, destination country authority
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: central bank or official exchange source, customs tariff system, destination country authority.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-015 - customs-agent-wiki

- Topic: latest HS codes, customs supervision conditions and declaration elements
- Category: general_current_fact
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- Suggested sources: customs authority website, official tariff database, licensed customs broker review
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: customs authority website, official tariff database, licensed customs broker review.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-016 - customs-agent-wiki

- Topic: latest import/export policy, inspection and quarantine requirements
- Category: policy_or_regulation
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- Suggested sources: customs and inspection authority announcement, destination country regulator, official trade compliance bulletin
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: customs and inspection authority announcement, destination country regulator, official trade compliance bulletin.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-017 - customs-agent-wiki

- Topic: latest platform OCR model parameters and document template behavior
- Category: technical_docs
- Source notes: `wikis/customs-agent-wiki/sources/source-notes.md`
- Suggested sources: OCR vendor documentation, internal extraction benchmark, manually reviewed sample set
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: OCR vendor documentation, internal extraction benchmark, manually reviewed sample set.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-018 - ecommerce-agent-wiki

- Topic: current marketplace policy, return window, category restrictions and consumer protection rules
- Category: policy_or_regulation
- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- Suggested sources: official marketplace policy center, consumer protection authority, merchant service agreement
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official marketplace policy center, consumer protection authority, merchant service agreement.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-019 - ecommerce-agent-wiki

- Topic: current product certification, recall, safety notice and warranty terms
- Category: general_current_fact
- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- Suggested sources: brand official website, regulator recall database, warranty document
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: brand official website, regulator recall database, warranty document.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-020 - ecommerce-agent-wiki

- Topic: current product price, stock, promotion, shipping fee and delivery ETA
- Category: market_or_platform_data
- Source notes: `wikis/ecommerce-agent-wiki/sources/source-notes.md`
- Suggested sources: platform product page, merchant backend, carrier tracking system
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: platform product page, merchant backend, carrier tracking system.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-021 - research-agent-wiki

- Topic: current dataset availability, license, model weights and code repository status
- Category: technical_docs
- Source notes: `wikis/research-agent-wiki/sources/source-notes.md`
- Suggested sources: official dataset page, repository release notes, model card
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official dataset page, repository release notes, model card.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-022 - research-agent-wiki

- Topic: latest papers, preprints, revisions, citations and benchmark leaderboards
- Category: general_current_fact
- Source notes: `wikis/research-agent-wiki/sources/source-notes.md`
- Suggested sources: publisher page, arXiv or conference page, official benchmark leaderboard
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: publisher page, arXiv or conference page, official benchmark leaderboard.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

### wave-2

#### SRC-023 - nodeops-agent-wiki

- Topic: current OS package, Docker, systemd and kernel behavior
- Category: general_current_fact
- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- Suggested sources: official documentation, local version output, release notes
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official documentation, local version output, release notes.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-024 - nodeops-agent-wiki

- Topic: current blockchain node client versions, network parameters and upgrade requirements
- Category: technical_docs
- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- Suggested sources: official client release notes, chain foundation announcement, node logs and version output
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: official client release notes, chain foundation announcement, node logs and version output.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-025 - nodeops-agent-wiki

- Topic: current cloud provider limits, firewall behavior, billing and incident status
- Category: general_current_fact
- Source notes: `wikis/nodeops-agent-wiki/sources/source-notes.md`
- Suggested sources: cloud provider documentation, status page, account console
- Human confirmation required: yes

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Because this is a high-risk wiki, read rules/ before workflows/ and require human confirmation before operational use.
- Start with suggested source types: cloud provider documentation, status page, account console.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

### wave-3

#### SRC-026 - agent-engineering-wiki

- Topic: current Codex Skill format, plugin behavior and tool capabilities
- Category: technical_docs
- Source notes: `wikis/agent-engineering-wiki/sources/source-notes.md`
- Suggested sources: official documentation, product changelog, local plugin manifest
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official documentation, product changelog, local plugin manifest.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-027 - agent-engineering-wiki

- Topic: current RAG frameworks, embedding models, vector databases and rerankers
- Category: technical_docs
- Source notes: `wikis/agent-engineering-wiki/sources/source-notes.md`
- Suggested sources: official documentation, release notes, benchmark report with date
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official documentation, release notes, benchmark report with date.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-028 - agent-engineering-wiki

- Topic: current eval harnesses, model APIs and MCP/tool schemas
- Category: technical_docs
- Source notes: `wikis/agent-engineering-wiki/sources/source-notes.md`
- Suggested sources: official API documentation, tool schema, repository release notes
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official API documentation, tool schema, repository release notes.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-029 - coding-agent-wiki

- Topic: current OpenAI, Codex, GitHub or Vercel product behavior
- Category: general_current_fact
- Source notes: `wikis/coding-agent-wiki/sources/source-notes.md`
- Suggested sources: official product documentation, changelog, repository or API docs
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official product documentation, changelog, repository or API docs.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-030 - coding-agent-wiki

- Topic: current cloud platform build, deploy, runtime and pricing behavior
- Category: general_current_fact
- Source notes: `wikis/coding-agent-wiki/sources/source-notes.md`
- Suggested sources: official platform documentation, status page, project deployment logs
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official platform documentation, status page, project deployment logs.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-031 - coding-agent-wiki

- Topic: current dependency vulnerabilities and security advisories
- Category: security_advisory
- Source notes: `wikis/coding-agent-wiki/sources/source-notes.md`
- Suggested sources: official security advisory, package registry advisory, vendor bulletin
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official security advisory, package registry advisory, vendor bulletin.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-032 - coding-agent-wiki

- Topic: current framework, library, CLI and API parameters
- Category: technical_docs
- Source notes: `wikis/coding-agent-wiki/sources/source-notes.md`
- Suggested sources: official documentation, release notes, source repository
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: official documentation, release notes, source repository.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-033 - content-agent-wiki

- Topic: current image, chart, dataset and quote licensing
- Category: general_current_fact
- Source notes: `wikis/content-agent-wiki/sources/source-notes.md`
- Suggested sources: license document, rights holder page, source terms of use
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: license document, rights holder page, source terms of use.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-034 - content-agent-wiki

- Topic: current news, statistics, public quotes and social media claims
- Category: general_current_fact
- Source notes: `wikis/content-agent-wiki/sources/source-notes.md`
- Suggested sources: primary source, official data release, dated reputable reporting
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: primary source, official data release, dated reputable reporting.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

#### SRC-035 - content-agent-wiki

- Topic: current publishing platform rules, format limits and content policies
- Category: policy_or_regulation
- Source notes: `wikis/content-agent-wiki/sources/source-notes.md`
- Suggested sources: platform policy center, creator documentation, account dashboard notices
- Human confirmation required: no

Verification steps:
- Read the wiki manifest, AGENTS.md, rules/, and sources/source-notes.md before updating content.
- Start with suggested source types: platform policy center, creator documentation, account dashboard notices.
- Collect at least one authoritative primary source; use two independent authoritative sources for high-risk claims when available.
- Record source title, publisher, URL or local reference, access date, publication/update date, and any scope limits.
- Compare the source against the existing wiki statement and identify whether the fact should be added, changed, or left as needs-source-update.
- Update only the minimal relevant wiki pages and sources/source-notes.md; keep uncertainty and human confirmation points visible.
- Run validation, source queue generation, search index update, and acceptance checks after edits.

Acceptance criteria:
- No current fact is written without a dated source note.
- No API key, private key, cookie, credential, or private account data is recorded.
- Any remaining uncertainty is explicitly marked needs-source-update.
- The relevant update-log.md records the change.

## Completion Commands

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

- Do not use this playbook to invent current prices, policies, laws, medical guidance, platform rules, API parameters, CVEs, or Web3 project facts.
- Do not write secrets, credentials, cookies, private keys, or private account data into any wiki or report.
- High-risk domains keep human confirmation points even after source refresh is complete.
