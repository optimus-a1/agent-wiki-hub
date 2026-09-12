# Agent Wiki Hub Release Notes

Generated: 2026-09-12

## Summary

- Release readiness for internal use: yes
- Blocking audits passed: yes
- Release warnings: 0
- Requires source updates before current-fact use: yes
- Wikis: 12
- Eval tests: 247
- Source-update topics: 35
- Source-refresh tasks: 35
- Source-refresh tickets: 35
- Source-refresh wave runner available: yes
- Source reviewer queue available: yes
- Source reviewer human gates: 16
- Source review session plan available: yes
- Source review session selected reviews: 25
- Source review session human gates: 16
- Source review readiness matrix available: yes
- Source review ready for collection: 25
- Source review queued outside session: 10
- Source review work orders available: yes
- Source review work orders: 25
- Source review work order human gates: 16
- Source review post-import completed: no
- Source review packet bundle available: yes
- Source review packet entries: 25
- Source review packet human gates: 16
- Source review packet audit passed: yes
- Source review packet audit packets: 2
- Source review packet audit issues: 0
- Source review packet rehearsal passed: yes
- Source review packet rehearsal dry-runs: 2/2
- Source evidence packet importer available: yes
- Source evidence packet fixtures: 8
- Source-refresh open tickets: 35
- Source-refresh verified tickets: 0
- Source-refresh completion ready: no
- Source evidence entries: 13
- Source evidence quality issues: 0
- Source evidence quality passed: yes
- Source refresh dashboard available: yes
- Source-refresh logs: 12
- Change summary available: yes
- Hub navigation available: yes
- Agent routing cards available: yes
- Agent handoff available: yes
- Source evidence recorder available: yes
- Packages: 13

## Acceptance Gates

| Gate | Result | Passed | Total |
| --- | --- | ---: | ---: |
| acceptance | PASS | 71 | 71 |
| ci | PASS | 11 | 11 |
| registry | PASS | 234 | 234 |
| metadata | PASS | 0 | 0 |
| coverage | PASS | 0 | 0 |
| links | PASS | 0 | 0 |
| packs | PASS | 656 | 656 |
| safety | PASS | 79 | 79 |
| source_refresh_logs | PASS | 12 | 12 |
| routing_cards | PASS | 0 | 0 |
| source_refresh_tickets | PASS | 35 | 35 |
| source_refresh_wave_runner | PASS | 35 | 35 |
| source_reviewer_queue | PASS | 4 | 4 |
| source_review_session_plan | PASS | 4 | 4 |
| source_review_readiness_matrix | PASS | 7 | 7 |
| source_review_work_orders | PASS | 7 | 7 |
| source_review_packet_bundle | PASS | 7 | 7 |
| source_review_packet_audit | PASS | 6 | 6 |
| source_review_packet_rehearsal | PASS | 4 | 4 |
| source_evidence_packet_importer | PASS | 2 | 2 |
| source_evidence_packet_fixtures | PASS | 10 | 10 |
| source_refresh_completion | PASS | 35 | 35 |
| source_evidence_quality | PASS | 13 | 13 |
| source_refresh_dashboard | PASS | 15 | 16 |
| agent_handoff | PASS | 0 | 0 |

## Release Warnings

No release warnings.

## Packages

| Package | Size | SHA-256 |
| --- | ---: | --- |
| `packs/agent-engineering-wiki.zip` | 92.5 KB | `cff5642d2fd880b9...` |
| `packs/agent-wiki-hub-all.zip` | external final artifact | Self-referential package; compute final size and checksum after packing release-manifest.json. |
| `packs/airdrop-agent-wiki.zip` | 74.7 KB | `cc45e16691d5c896...` |
| `packs/coding-agent-wiki.zip` | 83.1 KB | `e016dc1bd772b57b...` |
| `packs/content-agent-wiki.zip` | 60.1 KB | `d32ec989c1fbb4a0...` |
| `packs/customs-agent-wiki.zip` | 79.5 KB | `5ff22c4636380fa8...` |
| `packs/ecommerce-agent-wiki.zip` | 60.6 KB | `cc092aafeea60ee8...` |
| `packs/finance-agent-wiki.zip` | 98.3 KB | `fed15559ea9b4e35...` |
| `packs/health-agent-wiki.zip` | 51.7 KB | `6334d1987037d5c6...` |
| `packs/legal-agent-wiki.zip` | 53.7 KB | `ca9ddf728fc95802...` |
| `packs/nodeops-agent-wiki.zip` | 87.9 KB | `8b1111c812932be2...` |
| `packs/research-agent-wiki.zip` | 74.8 KB | `16e0e9f6ebe9365e...` |
| `packs/security-agent-wiki.zip` | 86.3 KB | `ce90b81351e27d78...` |

## Wiki Coverage

### Risk Levels

- high: 6
- low: 1
- medium: 5

### Freshness Requirements

- high: 8
- medium: 4

## Source Update Queue

Source refresh playbook tasks: 35

| Wiki | Priority | Topic |
| --- | ---: | --- |
| airdrop-agent-wiki | 9 | current contract addresses, wallet warnings, scam reports and signing risks |
| airdrop-agent-wiki | 9 | current project status, official links, task rules, snapshot and eligibility |
| airdrop-agent-wiki | 9 | current token launch, TGE, funding, exchange listing and airdrop allocation |
| finance-agent-wiki | 9 | current fees, funding rates, margin rules, tax rules and trading API parameters |
| finance-agent-wiki | 9 | current legal, regulatory or suitability requirements for financial products |
| finance-agent-wiki | 9 | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| finance-agent-wiki | 9 | latest financial statements, filings, restatements and audit opinions |
| health-agent-wiki | 9 | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| health-agent-wiki | 9 | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| legal-agent-wiki | 9 | current platform agreements, data processing terms and consumer protection rules |

## Safety Notes

- This release contains stable concepts, reusable workflows, prompts, evals, and safety boundaries.
- It does not certify current prices, policies, laws, medical guidance, platform rules, API parameters, CVEs, or project-specific Web3 facts.
- High-risk finance, legal, health, security, airdrop, and operations tasks retain human confirmation points.
- Do not use this release to execute real-money trades, provide final legal or medical opinions, or run offensive security activity.

## Reproduce

```bash
python3 scripts/run_acceptance.py
python3 scripts/generate_release_notes.py
python3 scripts/pack_wikis.py
```
