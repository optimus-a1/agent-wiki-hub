# Agent Wiki Hub Release Notes

Generated: 2026-05-31

## Summary

- Release readiness for internal use: yes
- Blocking audits passed: yes
- Release warnings: 0
- Requires source updates before current-fact use: yes
- Wikis: 12
- Eval tests: 137
- Source-update topics: 35
- Source-refresh tasks: 35
- Source-refresh tickets: 35
- Source-refresh wave runner available: yes
- Source reviewer queue available: yes
- Source reviewer human gates: 16
- Source review session plan available: yes
- Source review session selected reviews: 13
- Source review session human gates: 13
- Source review readiness matrix available: yes
- Source review ready for collection: 13
- Source review queued outside session: 22
- Source review work orders available: yes
- Source review work orders: 13
- Source review work order human gates: 13
- Source review post-import completed: no
- Source review packet bundle available: yes
- Source review packet entries: 13
- Source review packet human gates: 13
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
| acceptance | PASS | 48 | 48 |
| ci | PASS | 11 | 11 |
| registry | PASS | 234 | 234 |
| metadata | PASS | 0 | 0 |
| coverage | PASS | 0 | 0 |
| links | PASS | 0 | 0 |
| packs | PASS | 553 | 553 |
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
| `packs/agent-engineering-wiki.zip` | 19.1 KB | `b0d4f221c3132e10...` |
| `packs/agent-wiki-hub-all.zip` | external final artifact | Self-referential package; compute final size and checksum after packing release-manifest.json. |
| `packs/airdrop-agent-wiki.zip` | 15.3 KB | `8e91fd21578ef392...` |
| `packs/coding-agent-wiki.zip` | 17.6 KB | `93f46c2db1bb2863...` |
| `packs/content-agent-wiki.zip` | 13.8 KB | `c1a22c00f2fb09ed...` |
| `packs/customs-agent-wiki.zip` | 19.6 KB | `ad92e47de711a910...` |
| `packs/ecommerce-agent-wiki.zip` | 15.1 KB | `51be20541132210b...` |
| `packs/finance-agent-wiki.zip` | 21.1 KB | `59aef4ece5950abe...` |
| `packs/health-agent-wiki.zip` | 12.9 KB | `4af05eaa34c6ef23...` |
| `packs/legal-agent-wiki.zip` | 12.7 KB | `a7ca023a8ef71e67...` |
| `packs/nodeops-agent-wiki.zip` | 15.0 KB | `42728b7d52de9c65...` |
| `packs/research-agent-wiki.zip` | 12.6 KB | `3ee4dc0bdd7d7fd3...` |
| `packs/security-agent-wiki.zip` | 14.8 KB | `7aa86c639ddf3425...` |

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
| airdrop-agent-wiki | 8 | current contract addresses, wallet warnings, scam reports and signing risks |
| airdrop-agent-wiki | 8 | current project status, official links, task rules, snapshot and eligibility |
| airdrop-agent-wiki | 8 | current token launch, TGE, funding, exchange listing and airdrop allocation |
| finance-agent-wiki | 8 | current fees, funding rates, margin rules, tax rules and trading API parameters |
| finance-agent-wiki | 8 | current legal, regulatory or suitability requirements for financial products |
| finance-agent-wiki | 8 | current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity |
| finance-agent-wiki | 8 | latest financial statements, filings, restatements and audit opinions |
| health-agent-wiki | 8 | current clinical guidelines, drug labels, dosage, contraindications and safety warnings |
| health-agent-wiki | 8 | current public health guidance, screening recommendations and nutrition/exercise guidelines |
| legal-agent-wiki | 8 | current platform agreements, data processing terms and consumer protection rules |

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
