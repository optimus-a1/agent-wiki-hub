# Source Review Packet Checklist

Generated: 2026-06-30

## Packet Files

- JSON packet: `registry/source-review-packets/source-review-session-wave-1-pending.json`
- JSONL packet: `registry/source-review-packets/source-review-session-wave-1-pending.jsonl`

## Safety

- This packet contains placeholders only and does not certify current facts.
- Replace every placeholder before a real import.
- Keep status `pending` until authoritative evidence has been collected.
- High-risk or human-gated tickets need an explicit human reviewer before a final status.
- Do not add API keys, private keys, cookies, bearer tokens, seed phrases, credentials, or private account data.

## Dry Run

```bash
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks
python3 scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.jsonl --dry-run --no-post-checks
```

## Selected Reviews

| Ticket | Wiki | Reviewer Role | Human Gate | Topic | Suggested Sources |
| --- | --- | --- | --- | --- | --- |
| `TICKET-SRC-004` | finance-agent-wiki | finance-risk-reviewer | yes | current fees, funding rates, margin rules, tax rules and trading API parameters | official exchange documentation, regulator announcement, broker or custodian fee schedule |
| `TICKET-SRC-005` | finance-agent-wiki | finance-risk-reviewer | yes | current legal, regulatory or suitability requirements for financial products | regulator website, licensed professional review, official product documents |
| `TICKET-SRC-006` | finance-agent-wiki | finance-risk-reviewer | yes | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity | primary exchange or market data vendor, official issuer or exchange data portal, timestamped raw dataset |
| `TICKET-SRC-007` | finance-agent-wiki | finance-risk-reviewer | yes | latest financial statements, filings, restatements and audit opinions | company investor relations, securities regulator filing system, audited annual or interim report |
| `TICKET-SRC-014` | customs-agent-wiki | customs-document-reviewer | no | exchange rates, tariff rates, tax rates and destination-specific fees | central bank or official exchange source, customs tariff system, destination country authority |
| `TICKET-SRC-015` | customs-agent-wiki | customs-document-reviewer | no | latest HS codes, customs supervision conditions and declaration elements | customs authority website, official tariff database, licensed customs broker review |
| `TICKET-SRC-016` | customs-agent-wiki | customs-document-reviewer | no | latest import/export policy, inspection and quarantine requirements | customs and inspection authority announcement, destination country regulator, official trade compliance bulletin |
| `TICKET-SRC-017` | customs-agent-wiki | customs-document-reviewer | no | latest platform OCR model parameters and document template behavior | OCR vendor documentation, internal extraction benchmark, manually reviewed sample set |
| `TICKET-SRC-001` | airdrop-agent-wiki | web3-wallet-safety-reviewer | yes | current contract addresses, wallet warnings, scam reports and signing risks | official contract registry, block explorer, wallet security warning |
| `TICKET-SRC-002` | airdrop-agent-wiki | web3-wallet-safety-reviewer | yes | current project status, official links, task rules, snapshot and eligibility | official website, official documentation, official announcement channel |
| `TICKET-SRC-003` | airdrop-agent-wiki | web3-wallet-safety-reviewer | yes | current token launch, TGE, funding, exchange listing and airdrop allocation | project announcement, exchange official announcement, primary funding disclosure |
| `TICKET-SRC-018` | ecommerce-agent-wiki | ecommerce-policy-reviewer | no | current marketplace policy, return window, category restrictions and consumer protection rules | official marketplace policy center, consumer protection authority, merchant service agreement |
| `TICKET-SRC-019` | ecommerce-agent-wiki | ecommerce-policy-reviewer | no | current product certification, recall, safety notice and warranty terms | brand official website, regulator recall database, warranty document |
| `TICKET-SRC-020` | ecommerce-agent-wiki | ecommerce-policy-reviewer | no | current product price, stock, promotion, shipping fee and delivery ETA | platform product page, merchant backend, carrier tracking system |
| `TICKET-SRC-008` | health-agent-wiki | clinical-safety-reviewer | yes | current clinical guidelines, drug labels, dosage, contraindications and safety warnings | official health authority, drug regulator label, professional clinical guideline |
| `TICKET-SRC-009` | health-agent-wiki | clinical-safety-reviewer | yes | current public health guidance, screening recommendations and nutrition/exercise guidelines | public health authority, professional medical society, licensed clinician review |
| `TICKET-SRC-012` | security-agent-wiki | defensive-security-reviewer | yes | current CVEs, vendor advisories, patches, dependency versions and exploit status | vendor security advisory, official CVE record, package registry advisory |
| `TICKET-SRC-013` | security-agent-wiki | defensive-security-reviewer | yes | current security tool rules, detection signatures, cloud defaults and compliance requirements | official tool documentation, cloud provider security docs, compliance authority or auditor guidance |
| `TICKET-SRC-010` | legal-agent-wiki | legal-counsel-reviewer | yes | current platform agreements, data processing terms and consumer protection rules | official platform terms, regulator guidance, counsel-approved template |
| `TICKET-SRC-011` | legal-agent-wiki | legal-counsel-reviewer | yes | current statutes, regulations, cases, regulatory guidance and jurisdiction-specific requirements | official legal database, regulator website, licensed lawyer review |
| `TICKET-SRC-021` | research-agent-wiki | research-methods-reviewer | no | current dataset availability, license, model weights and code repository status | official dataset page, repository release notes, model card |
| `TICKET-SRC-022` | research-agent-wiki | research-methods-reviewer | no | latest papers, preprints, revisions, citations and benchmark leaderboards | publisher page, arXiv or conference page, official benchmark leaderboard |
