# Agent Wiki Hub Acceptance Report

Generated: 2026-06-03

## Summary

- Steps: 64
- Passed: 64
- Failed: 0

## Steps

| Step | Result | Command |
| --- | --- | --- |
| validate wiki structure and evals | PASS | `python.exe scripts/validate_wiki.py` |
| check registry consistency | PASS | `python.exe scripts/check_registry_consistency.py` |
| audit CI workflow | PASS | `python.exe scripts/audit_ci_workflow.py` |
| audit page metadata | PASS | `python.exe scripts/audit_page_metadata.py` |
| audit content coverage | PASS | `python.exe scripts/audit_content_coverage.py` |
| check eval files | PASS | `python.exe scripts/check_eval_files.py` |
| update search index | PASS | `python.exe scripts/update_index.py` |
| generate Obsidian vault | PASS | `python.exe scripts/generate_obsidian_vault.py` |
| generate Obsidian canvas | PASS | `python.exe scripts/generate_obsidian_canvas.py` |
| audit Obsidian vault | PASS | `python.exe scripts/audit_obsidian_vault.py` |
| collect dashboard data | PASS | `python.exe dashboard/scripts/collect_dashboard_data.py` |
| audit dashboard | PASS | `python.exe scripts/audit_dashboard.py` |
| generate ingestion report | PASS | `python.exe ingestion/generate_ingestion_report.py` |
| audit ingestion pipeline | PASS | `python.exe scripts/audit_ingestion_pipeline.py` |
| generate crawl report | PASS | `python.exe crawler/generate_crawl_report.py` |
| classify candidate knowledge dry-run | PASS | `python.exe scripts/classify_candidate_knowledge.py --dry-run` |
| promote stable knowledge dry-run | PASS | `python.exe scripts/promote_stable_knowledge.py --dry-run` |
| generate source review from candidates dry-run | PASS | `python.exe scripts/generate_source_review_from_candidates.py --dry-run` |
| audit crawler outputs | PASS | `python.exe scripts/audit_crawler_outputs.py` |
| audit knowledge promotion | PASS | `python.exe scripts/audit_knowledge_promotion.py` |
| audit RAG config | PASS | `python.exe scripts/audit_rag_config.py` |
| audit secret leaks | PASS | `python.exe scripts/audit_secret_leaks.py` |
| report wiki status | PASS | `python.exe scripts/report_wiki_status.py` |
| list source updates | PASS | `python.exe scripts/list_source_updates.py` |
| generate source refresh playbook | PASS | `python.exe scripts/generate_source_refresh_playbook.py` |
| generate source refresh tickets | PASS | `python.exe scripts/generate_source_refresh_tickets.py` |
| dry-run source evidence recorder | PASS | `python.exe scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run --allow-duplicate` |
| generate source evidence packet importer | PASS | `python.exe scripts/import_source_evidence_packet.py` |
| generate source evidence packet fixtures | PASS | `python.exe scripts/generate_source_evidence_packet_fixtures.py` |
| generate source refresh logs | PASS | `python.exe scripts/generate_source_refresh_logs.py` |
| audit source refresh completion | PASS | `python.exe scripts/audit_source_refresh_completion.py` |
| audit source evidence quality | PASS | `python.exe scripts/audit_source_evidence_quality.py` |
| audit safety boundaries | PASS | `python.exe scripts/audit_safety_boundaries.py` |
| generate source refresh wave runner | PASS | `python.exe scripts/generate_source_refresh_wave_runner.py` |
| generate source reviewer queue | PASS | `python.exe scripts/generate_source_reviewer_queue.py` |
| generate source review session plan | PASS | `python.exe scripts/generate_source_review_session_plan.py` |
| generate source review packet bundle | PASS | `python.exe scripts/generate_source_review_packet_bundle.py` |
| generate source review packet classification | PASS | `python.exe scripts/generate_source_review_packet_classification.py` |
| audit source review packets | PASS | `python.exe scripts/audit_source_review_packets.py` |
| rehearse source review packet imports | PASS | `python.exe scripts/rehearse_source_review_packet_imports.py` |
| generate source review readiness matrix | PASS | `python.exe scripts/generate_source_review_readiness_matrix.py` |
| generate source review work orders | PASS | `python.exe scripts/generate_source_review_work_orders.py` |
| dry-run source review packet bundle | PASS | `python.exe scripts/import_source_evidence_packet.py --packet registry/source-review-packets/source-review-session-wave-1-pending.json --dry-run --no-post-checks --allow-duplicate` |
| generate source refresh dashboard | PASS | `python.exe scripts/generate_source_refresh_dashboard.py` |
| pack wikis for navigation | PASS | `python.exe scripts/pack_wikis.py` |
| generate hub navigation | PASS | `python.exe scripts/generate_hub_navigation.py` |
| generate agent routing cards | PASS | `python.exe scripts/generate_agent_routing_cards.py` |
| generate agent handoff | PASS | `python.exe scripts/generate_agent_handoff.py` |
| audit links | PASS | `python.exe scripts/audit_links.py` |
| route query: risk control backtest paper trading | PASS | `python.exe scripts/route_wiki.py --query risk control backtest paper trading --json` |
| route query: field extraction invoice packing list | PASS | `python.exe scripts/route_wiki.py --query field extraction invoice packing list --json` |
| route query: defensive security hardening | PASS | `python.exe scripts/route_wiki.py --query defensive security hardening --json` |
| search finance-agent-wiki: risk control | PASS | `python.exe scripts/search_wiki.py --query risk control --wiki finance-agent-wiki` |
| search customs-agent-wiki: field extraction | PASS | `python.exe scripts/search_wiki.py --query field extraction --wiki customs-agent-wiki` |
| search finance-agent-wiki: paper trading real money | PASS | `python.exe scripts/search_wiki.py --query paper trading real money --wiki finance-agent-wiki` |
| search customs-agent-wiki: INV-EXAMPLE-001 evidence confidence | PASS | `python.exe scripts/search_wiki.py --query INV-EXAMPLE-001 evidence confidence --wiki customs-agent-wiki` |
| search agent-engineering-wiki: needs-source-update topics | PASS | `python.exe scripts/search_wiki.py --query needs-source-update topics --wiki agent-engineering-wiki` |
| search security-agent-wiki: bypass login Authorization header | PASS | `python.exe scripts/search_wiki.py --query bypass login Authorization header --wiki security-agent-wiki` |
| pack wikis | PASS | `python.exe scripts/pack_wikis.py` |
| audit pack integrity | PASS | `python.exe scripts/audit_pack_integrity.py` |
| generate release notes | PASS | `python.exe scripts/generate_release_notes.py` |
| generate change summary | PASS | `python.exe scripts/generate_change_summary.py` |
| pack wikis with acceptance report | PASS | `python.exe scripts/pack_wikis.py` |
| audit final package integrity | PASS | `python.exe scripts/audit_pack_integrity.py` |

## Command Output

### validate wiki structure and evals - PASS

```text
VALIDATION PASSED (137 eval tests)
```

### check registry consistency - PASS

```text
Wrote docs\REGISTRY_CONSISTENCY.md
Wrote registry\registry-consistency.json
REGISTRY CONSISTENCY PASSED (234 checks)
```

### audit CI workflow - PASS

```text
Wrote docs\CI_AUDIT.md
Wrote registry\ci-audit.json
CI WORKFLOW AUDIT PASSED (11 checks)
```

### audit page metadata - PASS

```text
Wrote docs\PAGE_METADATA_AUDIT.md
Wrote registry\page-metadata-audit.json
PAGE METADATA AUDIT PASSED (159 pages)
```

### audit content coverage - PASS

```text
Wrote docs\COVERAGE_AUDIT.md
Wrote registry\coverage-audit.json
CONTENT COVERAGE AUDIT PASSED (51 topics)
```

### check eval files - PASS

```text
EVAL CHECK PASSED (137 tests)
```

### update search index - PASS

```text
Indexed 255 docs -> index\search_index.json
```

### generate Obsidian vault - PASS

```text
OBSIDIAN VAULT GENERATED (12 wikis, 12 MOCs)
```

### generate Obsidian canvas - PASS

```text
OBSIDIAN CANVAS GENERATED (3 files)
```

### audit Obsidian vault - PASS

```text
OBSIDIAN VAULT AUDIT PASSED (13 checks)
```

### collect dashboard data - PASS

```text
DASHBOARD DATA GENERATED (12 wikis, 13 packs)
```

### audit dashboard - PASS

```text
DASHBOARD AUDIT PASSED (10 checks)
```

### generate ingestion report - PASS

```text
INGESTION REPORT GENERATED (warnings only)
```

### audit ingestion pipeline - PASS

```text
INGESTION PIPELINE AUDIT PASSED
```

### generate crawl report - PASS

```text
CRAWL REPORT GENERATED (3 configured sources, 0 collected)
```

### classify candidate knowledge dry-run - PASS

```text
CANDIDATE KNOWLEDGE CLASSIFICATION PASSED (0 records, dry_run=True)
```

### promote stable knowledge dry-run - PASS

```text
KNOWLEDGE PROMOTION PASSED (0 eligible, dry_run=True)
```

### generate source review from candidates dry-run - PASS

```text
AUTO SOURCE REVIEW QUEUE PASSED (0 entries, dry_run=True)
```

### audit crawler outputs - PASS

```text
CRAWLER OUTPUT AUDIT PASSED (0 raw notes)
```

### audit knowledge promotion - PASS

```text
KNOWLEDGE PROMOTION AUDIT PASSED (0 files)
```

### audit RAG config - PASS

```text
RAG CONFIG AUDIT PASSED (1 warnings)
```

### audit secret leaks - PASS

```text
SECRET LEAK AUDIT PASSED (2 findings, 0 blocking)
```

### report wiki status - PASS

```text
Wrote docs\WIKI_STATUS.md
Wrote registry\wiki-status.json
```

### list source updates - PASS

```text
Wrote docs\SOURCE_UPDATE_QUEUE.md
Wrote registry\source-update-queue.json
Queued 35 source-update topics
```

### generate source refresh playbook - PASS

```text
Wrote docs\SOURCE_REFRESH_PLAYBOOK.md
Wrote registry\source-refresh-playbook.json
SOURCE REFRESH PLAYBOOK GENERATED (35 tasks)
```

### generate source refresh tickets - PASS

```text
Wrote docs\SOURCE_REFRESH_TICKETS.md
Wrote registry\source-refresh-tickets.json
SOURCE REFRESH TICKETS GENERATED (35 tickets)
```

### dry-run source evidence recorder - PASS

```text
- task_id: SRC-006
  ticket_id: TICKET-SRC-006
  topic: "current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity"
  status: pending
  verified_on: 2026-06-03
  source_title: ""
  source_publisher: ""
  source_url_or_reference: ""
  source_published_or_updated: "unknown"
  source_accessed_on: 2026-06-03
  evidence_summary: ""
  affected_pages:
    - wikis/finance-agent-wiki/sources/source-notes.md
  confidence: 
  remaining_uncertainty: ""
  human_reviewer: ""
  follow_up: "none"
```

### generate source evidence packet importer - PASS

```text
Wrote docs\SOURCE_EVIDENCE_PACKET_IMPORTER.md
Wrote registry\source-evidence-packet-importer.json
SOURCE EVIDENCE PACKET IMPORTER READY (no packet supplied)
```

### generate source evidence packet fixtures - PASS

```text
Wrote docs\SOURCE_EVIDENCE_PACKET_FIXTURES.md
Wrote registry\source-evidence-packet-fixtures.json
Wrote 8 fixtures to registry/source-evidence-fixtures
SOURCE EVIDENCE PACKET FIXTURES GENERATED
```

### generate source refresh logs - PASS

```text
Wrote docs\SOURCE_REFRESH_LOG_STATUS.md
Wrote registry\source-refresh-log-status.json
SOURCE REFRESH LOGS READY (12 wikis)
```

### audit source refresh completion - PASS

```text
Wrote docs\SOURCE_REFRESH_COMPLETION_AUDIT.md
Wrote registry\source-refresh-completion-audit.json
SOURCE REFRESH COMPLETION AUDIT PASSED (35 open, 0 verified)
```

### audit source evidence quality - PASS

```text
Wrote docs\SOURCE_EVIDENCE_QUALITY_AUDIT.md
Wrote registry\source-evidence-quality-audit.json
SOURCE EVIDENCE QUALITY AUDIT PASSED (13 entries, 0 issues)
```

### audit safety boundaries - PASS

```text
Wrote docs\SAFETY_AUDIT.md
Wrote registry\safety-audit.json
SAFETY AUDIT PASSED (75 required checks)
```

### generate source refresh wave runner - PASS

```text
Wrote docs\SOURCE_REFRESH_WAVE_RUNNER.md
Wrote registry\source-refresh-wave-runner.json
SOURCE REFRESH WAVE RUNNER GENERATED (35 open, 35 selected)
```

### generate source reviewer queue - PASS

```text
Wrote docs\SOURCE_REVIEWER_QUEUE.md
Wrote registry\source-reviewer-queue.json
SOURCE REVIEWER QUEUE GENERATED (35 open, 16 human gates)
```

### generate source review session plan - PASS

```text
Wrote docs\SOURCE_REVIEW_SESSION_PLAN.md
Wrote registry\source-review-session-plan.json
SOURCE REVIEW SESSION PLAN GENERATED (13 selected, 13 human gates)
```

### generate source review packet bundle - PASS

```text
Wrote docs\SOURCE_REVIEW_PACKET_BUNDLE.md
Wrote registry\source-review-packet-bundle.json
Wrote registry/source-review-packets/source-review-session-wave-1-pending.json
Wrote registry/source-review-packets/source-review-session-wave-1-pending.jsonl
Wrote registry/source-review-packets/source-review-session-wave-1-pending-checklist.md
SOURCE REVIEW PACKET BUNDLE GENERATED (13 entries, 13 human gates)
```

### generate source review packet classification - PASS

```text
Wrote docs\SOURCE_REVIEW_PACKET_CLASSIFICATION.md
Wrote registry\source-review-packet-classification.json
SOURCE REVIEW PACKET CLASSIFICATION PASSED (10 packets)
```

### audit source review packets - PASS

```text
Wrote docs\SOURCE_REVIEW_PACKET_AUDIT.md
Wrote registry\source-review-packet-audit.json
SOURCE REVIEW PACKET AUDIT PASSED (2 packets, 26 entries)
```

### rehearse source review packet imports - PASS

```text
Wrote docs\SOURCE_REVIEW_PACKET_REHEARSAL.md
Wrote registry\source-review-packet-rehearsal.json
SOURCE REVIEW PACKET REHEARSAL PASSED (2/2 dry-runs passed)
```

### generate source review readiness matrix - PASS

```text
Wrote docs\SOURCE_REVIEW_READINESS_MATRIX.md
Wrote registry\source-review-readiness-matrix.json
SOURCE REVIEW READINESS MATRIX PASSED (13 ready, 22 queued)
```

### generate source review work orders - PASS

```text
Wrote docs\SOURCE_REVIEW_WORK_ORDERS.md
Wrote registry\source-review-work-orders.json
Wrote registry\source-review-work-orders\manifest.json
SOURCE REVIEW WORK ORDERS GENERATED (13 work orders, 13 human gates)
```

### dry-run source review packet bundle - PASS

```text
Wrote docs\SOURCE_EVIDENCE_PACKET_IMPORTER.md
Wrote registry\source-evidence-packet-importer.json
SOURCE EVIDENCE PACKET DRY RUN (13 entries)
```

### generate source refresh dashboard - PASS

```text
Wrote docs\SOURCE_REFRESH_DASHBOARD.md
Wrote registry\source-refresh-dashboard.json
SOURCE REFRESH DASHBOARD GENERATED (35 open, 0 verified)
```

### pack wikis for navigation - PASS

```text
packed packs\agent-engineering-wiki.zip
packed packs\airdrop-agent-wiki.zip
packed packs\coding-agent-wiki.zip
packed packs\content-agent-wiki.zip
packed packs\customs-agent-wiki.zip
packed packs\ecommerce-agent-wiki.zip
packed packs\finance-agent-wiki.zip
packed packs\health-agent-wiki.zip
packed packs\legal-agent-wiki.zip
packed packs\nodeops-agent-wiki.zip
packed packs\research-agent-wiki.zip
packed packs\security-agent-wiki.zip
packed packs\agent-wiki-hub-all.zip
```

### generate hub navigation - PASS

```text
Wrote docs\HUB_NAVIGATION.md
Wrote registry\hub-navigation.json
HUB NAVIGATION GENERATED (12 wikis)
```

### generate agent routing cards - PASS

```text
Wrote docs\AGENT_ROUTING_CARDS.md
Wrote registry\agent-routing-cards.json
AGENT ROUTING CARDS GENERATED (12 cards)
```

### generate agent handoff - PASS

```text
Wrote docs\AGENT_HANDOFF.md
Wrote registry\agent-handoff.json
AGENT HANDOFF GENERATED
```

### audit links - PASS

```text
Wrote docs\LINK_AUDIT.md
Wrote registry\link-audit.json
LINK AUDIT PASSED (3751 references)
```

### route query: risk control backtest paper trading - PASS

```text
{
  "generated": "2026-06-03",
  "query": "risk control backtest paper trading",
  "top_wiki": "finance-agent-wiki",
  "source_update_required": false,
  "source_update_terms": [],
  "safety_gate_required": true,
  "high_risk_terms": [],
  "matches": [
    {
      "wiki": "finance-agent-wiki",
      "name": "Finance Agent Wiki",
      "score": 58.3,
      "reasons": [
        "alias:backtest",
        "alias:paper trading",
        "alias:risk control",
        "alias:trading",
        "token:backtest",
        "token:control",
        "token:paper",
        "token:risk",
        "token:trading"
      ],
      "priority": "P0",
      "risk_level": "high",
      "freshness_requirement": "high",
      "required_reading_order": [
        "wikis/finance-agent-wiki/AGENTS.md",
        "wikis/finance-agent-wiki/manifest.yaml",
        "wikis/finance-agent-wiki/README.md",
        "wikis/finance-agent-wiki/rules/",
        "wikis/finance-agent-wiki/workflows/"
      ],
      "source_gates": [
        "wikis/finance-agent-wiki/sources/source-notes.md",
        "wikis/finance-agent-wiki/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md"
      ],
      "safety_rules": [
        "Educational, research, and simulation use only.",
        "Do not provide personalized investment advice.",
        "Default to paper trading or human-approved simulation.",
        "Require human confirmation before any high-risk financial action."
      ],
      "prohibited_actions": [
        "Autonomous real-money order placement.",
        "Personalized buy, sell, hold, leverage, or allocation instructions.",
        "Claims about current prices, rates, exchange rules, or market conditions without source refresh."
      ],
      "package": "packs/finance-agent-wiki.zip"
    },
    {
      "wiki": "research-agent-wiki",
      "name": "Research Agent Wiki",
      "score": 14.1,
      "reasons": [
        "alias:paper",
        "token:paper"
      ],
      "priority": "P2",
      "risk_level": "medium",
      "freshness_requirement": "high",
      "required_reading_order": [
        "wikis/research-agent-wiki/AGENTS.md",
        "wikis/research-agent-wiki/manifest.yaml",
        "wikis/research-agent-wiki/README.md",
        "wikis/research-agent-wiki/rules/",
        "wikis/research-agent-wiki/workflows/"
      ],
      "source_gates": [
        "wikis/research-agent-wiki/sources/source-notes.md",
        "wikis/research-agent-wiki/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md"
      ],
      "safety_rules": [
        "Keep citations traceable to source text.",
        "Label speculation, limitations, and unresolved evidence gaps.",
        "Mark newest papers, datasets, leaderboards, and benchmarks as source-update topics."
      ],
      "prohibited_actions": [
        "Fabricating citations, abstracts, datasets, or benchmark results.",
        "Presenting weak or unverified evidence as consensus.",
        "Omitting limitations that affect interpretation."
      ],
      "package": "packs/research-agent-wiki.zip"
    },
    {
      "wiki": "customs-agent-wiki",
      "name": "Customs Document Agent Wiki",
      "score": 2.3,
      "reasons": [
        "token:risk"
      ],
      "priority": "P0",
      "risk_level": "medium",
      "freshness_requirement": "high",
      "required_reading_order": [
        "wikis/customs-agent-wiki/AGENTS.md",
        "wikis/customs-agent-wiki/manifest.yaml",
        "wikis/customs-agent-wiki/README.md",
        "wikis/customs-agent-wiki/rules/",
        "wikis/customs-agent-wiki/workflows/"
      ],
      "source_gates": [
        "wikis/customs-agent-wiki/sources/source-notes.md",
        "wikis/customs-agent-wiki/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md"
      ],
      "safety_rules": [
        "Treat outputs as structured review support, not final customs advice.",
        "Preserve source snippets, confidence, and unresolved fields.",
        "Flag policy, tariff, HS code, and regulatory questions as source-update topics.",
        "Require manual review for medium and high risk discrepancies."
      ],
      "prohibited_actions": [
        "Inventing missing document values.",
        "Presenting current customs policy or legal classification as verified without authoritative sources.",
        "Hiding OCR uncertainty or document conflicts."
      ],
      "package": "packs/customs-agent-wiki.zip"
    }
  ]
}
```

### route query: field extraction invoice packing list - PASS

```text
{
  "generated": "2026-06-03",
  "query": "field extraction invoice packing list",
  "top_wiki": "customs-agent-wiki",
  "source_update_required": false,
  "source_update_terms": [],
  "safety_gate_required": false,
  "high_risk_terms": [],
  "matches": [
    {
      "wiki": "customs-agent-wiki",
      "name": "Customs Document Agent Wiki",
      "score": 44.3,
      "reasons": [
        "alias:invoice",
        "alias:packing list",
        "alias:field extraction",
        "token:extraction",
        "token:field",
        "token:invoice",
        "token:packing"
      ],
      "priority": "P0",
      "risk_level": "medium",
      "freshness_requirement": "high",
      "required_reading_order": [
        "wikis/customs-agent-wiki/AGENTS.md",
        "wikis/customs-agent-wiki/manifest.yaml",
        "wikis/customs-agent-wiki/README.md",
        "wikis/customs-agent-wiki/rules/",
        "wikis/customs-agent-wiki/workflows/"
      ],
      "source_gates": [
        "wikis/customs-agent-wiki/sources/source-notes.md",
        "wikis/customs-agent-wiki/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md"
      ],
      "safety_rules": [
        "Treat outputs as structured review support, not final customs advice.",
        "Preserve source snippets, confidence, and unresolved fields.",
        "Flag policy, tariff, HS code, and regulatory questions as source-update topics.",
        "Require manual review for medium and high risk discrepancies."
      ],
      "prohibited_actions": [
        "Inventing missing document values.",
        "Presenting current customs policy or legal classification as verified without authoritative sources.",
        "Hiding OCR uncertainty or document conflicts."
      ],
      "package": "packs/customs-agent-wiki.zip"
    },
    {
      "wiki": "ecommerce-agent-wiki",
      "name": "Ecommerce Agent Wiki",
      "score": 2.2,
      "reasons": [
        "token:invoice"
      ],
      "priority": "P1",
      "risk_level": "medium",
      "freshness_requirement": "high",
      "required_reading_order": [
        "wikis/ecommerce-agent-wiki/AGENTS.md",
        "wikis/ecommerce-agent-wiki/manifest.yaml",
        "wikis/ecommerce-agent-wiki/README.md",
        "wikis/ecommerce-agent-wiki/rules/",
        "wikis/ecommerce-agent-wiki/workflows/"
      ],
      "source_gates": [
        "wikis/ecommerce-agent-wiki/sources/source-notes.md",
        "wikis/ecommerce-agent-wiki/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md"
      ],
      "safety_rules": [
        "Respect privacy, consent, consumer protection, and platform rules.",
        "Mark fees, return policies, ads policy, and platform rules as source-update topics.",
        "Avoid deceptive claims, fake scarcity, or unsupported product promises."
      ],
      "prohibited_actions": [
        "Inventing product availability, current pricing, or platform policy.",
        "Using private customer data without a clear need and consent basis.",
        "Generating manipulative or misleading sales tactics."
      ],
      "package": "packs/ecommerce-agent-wiki.zip"
    }
  ]
}
```

### route query: defensive security hardening - PASS

```text
{
  "generated": "2026-06-03",
  "query": "defensive security hardening",
  "top_wiki": "security-agent-wiki",
  "source_update_required": false,
  "source_update_terms": [],
  "safety_gate_required": true,
  "high_risk_terms": [],
  "matches": [
    {
      "wiki": "security-agent-wiki",
      "name": "Defensive Security Agent Wiki",
      "score": 47.1,
      "reasons": [
        "alias:security",
        "alias:defensive security",
        "alias:hardening",
        "phrase",
        "token:defensive",
        "token:hardening",
        "token:security"
      ],
      "priority": "P2",
      "risk_level": "high",
      "freshness_requirement": "high",
      "required_reading_order": [
        "wikis/security-agent-wiki/AGENTS.md",
        "wikis/security-agent-wiki/manifest.yaml",
        "wikis/security-agent-wiki/README.md",
        "wikis/security-agent-wiki/rules/",
        "wikis/security-agent-wiki/workflows/"
      ],
      "source_gates": [
        "wikis/security-agent-wiki/sources/source-notes.md",
        "wikis/security-agent-wiki/sources/source-refresh-log.md",
        "docs/SOURCE_UPDATE_QUEUE.md",
        "docs/SOURCE_REFRESH_DASHBOARD.md",
        "docs/SOURCE_REFRESH_PLAYBOOK.md",
        "docs/SOURCE_REFRESH_TICKETS.md",
        "docs/SOURCE_REFRESH_WAVE_RUNNER.md",
        "docs/SOURCE_REVIEWER_QUEUE.md",
        "docs/SOURCE_REVIEW_SESSION_PLAN.md",
        "docs/SOURCE_REVIEW_READINESS_MATRIX.md",
        "docs/SOURCE_REVIEW_WORK_ORDERS.md",
        "docs/SOURCE_REVIEW_PACKET_BUNDLE.md",
        "docs/SOURCE_REVIEW_PACKET_AUDIT.md",
        "docs/SOURCE_REVIEW_PACKET_REHEARSAL.md",
        "docs/SOURCE_EVIDENCE_RECORDER.md",
        "docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md",
        "docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md",
        "docs/SOURCE_REFRESH_COMPLETION_AUDIT.md",
        "docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md"
      ],
      "safety_rules": [
        "Defensive review only.",
        "Focus on risk explanation, detection, mitigation, and verification.",
        "Mark current CVEs, exploit status, dependency versions, and advisories as source-update topics.",
        "Require human approval for production security changes."
      ],
      "prohibited_actions": [
        "Exploitation, persistence, evasion, credential theft, or bypass steps.",
        "Payloads or procedures that enable unauthorized access.",
        "Claims about current vulnerabilities or advisories without source refresh."
      ],
      "package": "packs/security-agent-wiki.zip"
    }
  ]
}
```

### search finance-agent-wiki: risk control - PASS

```text
[11] wikis/finance-agent-wiki/concepts/portfolio-and-risk-metrics.md :: Portfolio And Risk Metrics
    --- title: Portfolio And Risk Metrics status: stable last_updated: 2026-06-01 risk_level: high --- # Portfolio And Risk Metrics ## Purpose Define stable portfolio and risk measurement concepts for educational research, s...
[5] wikis/finance-agent-wiki/rules/risk-control.md :: Finance Risk Control Rules
    --- title: Finance Risk Control Rules status: stable last_updated: 2026-05-27 risk_level: high --- # Finance Risk Control Rules ## Purpose 任何金融 Agent 都必须先做风险控制，再做收益分析。 ## Non-negotiable rules 1. 默认只做教育、研究、模拟盘和风险检查。 2. 不输...
[5] wikis/finance-agent-wiki/update-log.md :: Update Log — Finance Agent Wiki
    # Update Log — Finance Agent Wiki ## 2026-06-01 - Added stable high-density knowledge pages for portfolio risk metrics, model risk and backtest hygiene, portfolio review workflow, and overfitting detection. - Updated REA...
[3] wikis/finance-agent-wiki/workflows/portfolio-review-workflow.md :: Portfolio Review Workflow
    --- title: Portfolio Review Workflow status: stable last_updated: 2026-06-01 risk_level: high --- # Portfolio Review Workflow ## Purpose Offer a stable review workflow for simulated or educational portfolio analysis. ## ...
[2] wikis/finance-agent-wiki/cases/sample-backtest-risk-review.md :: Sample Backtest Risk Review
    --- title: Sample Backtest Risk Review status: stable last_updated: 2026-05-27 risk_level: high --- # Sample Backtest Risk Review ## Purpose 提供一个可复用的回测审查样例，帮助 Agent 判断回测报告是否满足数据、成本、风控和上线边界要求。 ## When to use 用于审查用户提供的策略回测...
[2] wikis/finance-agent-wiki/rules/model-risk-and-backtest-hygiene.md :: Model Risk And Backtest Hygiene
    --- title: Model Risk And Backtest Hygiene status: stable last_updated: 2026-06-01 risk_level: high --- # Model Risk And Backtest Hygiene ## Purpose Provide stable rules for preventing misleading financial models and ove...
[1] wikis/finance-agent-wiki/AGENTS.md :: AGENTS.md — Finance Agent Wiki
    # AGENTS.md — Finance Agent Wiki ## Trigger Use this wiki when the task involves: 金融, 投资, 财报, 估值, 市场数据, 回测, 风控, 交易系统, 资金费率, 套利. ## Reading order 1. `manifest.yaml` 2. `README.md` 3. `rules/` 4. `workflows/` 5. `cases/` 6...
[1] wikis/finance-agent-wiki/cases/sample-overfitting-detection.md :: Sample Overfitting Detection
    --- title: Sample Overfitting Detection status: stable last_updated: 2026-06-01 risk_level: high --- # Sample Overfitting Detection ## Purpose Show how a finance agent should respond to a suspiciously strong backtest wit...
```

### search customs-agent-wiki: field extraction - PASS

```text
[4] wikis/customs-agent-wiki/rules/field-extraction-rules.md :: Customs Field Extraction Rules
    --- title: Customs Field Extraction Rules status: stable last_updated: 2026-05-27 risk_level: medium --- # Customs Field Extraction Rules ## Core fields - shipper / seller / exporter -> 发货人/卖方/出口商 - consignee / buyer / i...
[3] wikis/customs-agent-wiki/update-log.md :: Update Log — Customs Document Agent Wiki
    # Update Log — Customs Document Agent Wiki ## 2026-05-27 - Added source refresh log template for authoritative source verification. - Added sample invoice extraction and document difference cases with expected JSON/table...
[2] wikis/customs-agent-wiki/cases/sample-invoice-extraction.md :: Sample Invoice Extraction
    --- title: Sample Invoice Extraction status: stable last_updated: 2026-05-27 risk_level: medium --- # Sample Invoice Extraction ## Purpose 提供一个合成商业发票字段抽取样例，展示英文表头到标准 JSON 的映射方式。 ## When to use 用于训练或测试 OCR/文本解析到结构化 JSON 的...
[1] wikis/customs-agent-wiki/cases/sample-document-diff.md :: Sample Document Difference Table
    --- title: Sample Document Difference Table status: stable last_updated: 2026-05-27 risk_level: medium --- # Sample Document Difference Table ## Purpose 提供合同、发票和装箱单差异比对样例，展示风险等级和人工复核建议。 ## When to use 用于测试单证差异表输出、金额币种校验、...
[1] wikis/customs-agent-wiki/concepts/document-types.md :: Trade Document Types
    --- title: Trade Document Types status: stable last_updated: 2026-05-27 risk_level: medium --- # Trade Document Types ## Common documents - Contract / Sales Contract: 买卖双方、合同号、签署日期、货物、数量、价格、贸易术语、付款方式、交货条件。 - Commercial I...
[1] wikis/customs-agent-wiki/sources/source-notes.md :: Source Notes — Customs Document Agent Wiki
    # Source Notes — Customs Document Agent Wiki ## Policy 本文件记录需要外部来源、实时核验或权威确认的主题。 ## Needs source update - topic: latest HS codes, customs supervision conditions and declaration elements status: needs-source-update sugges...
[1] wikis/customs-agent-wiki/workflows/difference-comparison.md :: Document Difference Comparison Workflow
    --- title: Document Difference Comparison Workflow status: stable last_updated: 2026-05-27 risk_level: medium --- # Document Difference Comparison Workflow ## Purpose 比较多份单证之间的关键字段一致性，输出差异表、风险等级和人工复核建议。 ## When to use 用于...
[1] wikis/customs-agent-wiki/workflows/document-checking.md :: Customs Document Checking Workflow
    --- title: Customs Document Checking Workflow status: stable last_updated: 2026-05-26 risk_level: medium --- # Customs Document Checking Workflow ## Workflow 1. Identify document types. 2. Extract fields into normalized ...
```

### search finance-agent-wiki: paper trading real money - PASS

```text
[4] wikis/finance-agent-wiki/workflows/paper-trading-system.md :: Paper Trading System Workflow
    --- title: Paper Trading System Workflow status: stable last_updated: 2026-05-26 risk_level: high --- # Paper Trading System Workflow ## Purpose 设计模拟盘系统，验证数据、风控、执行流程和日志，而不是直接投入真实资金。 ## Components - market data adapter - ...
[3] wikis/finance-agent-wiki/cases/sample-overfitting-detection.md :: Sample Overfitting Detection
    --- title: Sample Overfitting Detection status: stable last_updated: 2026-06-01 risk_level: high --- # Sample Overfitting Detection ## Purpose Show how a finance agent should respond to a suspiciously strong backtest wit...
[3] wikis/finance-agent-wiki/update-log.md :: Update Log — Finance Agent Wiki
    # Update Log — Finance Agent Wiki ## 2026-06-01 - Added stable high-density knowledge pages for portfolio risk metrics, model risk and backtest hygiene, portfolio review workflow, and overfitting detection. - Updated REA...
[2] wikis/finance-agent-wiki/rules/trading-system-boundaries.md :: Trading System Boundaries
    --- title: Trading System Boundaries status: stable last_updated: 2026-05-27 risk_level: high --- # Trading System Boundaries ## Purpose 约束金融 Agent 在交易系统设计中的权限、输出和安全边界。 ## When to use 用于模拟盘、回测平台、风险引擎、交易日志、告警、权限控制和人工审批流程设...
[2] wikis/finance-agent-wiki/sources/source-refresh-log.md :: Source Refresh Log
    # Source Refresh Log Wiki: finance-agent-wiki Risk level: high Freshness requirement: high Template initialized: 2026-05-27 ## Purpose Record authoritative source verification work before current facts are written into t...
[1] wikis/finance-agent-wiki/concepts/portfolio-and-risk-metrics.md :: Portfolio And Risk Metrics
    --- title: Portfolio And Risk Metrics status: stable last_updated: 2026-06-01 risk_level: high --- # Portfolio And Risk Metrics ## Purpose Define stable portfolio and risk measurement concepts for educational research, s...
[1] wikis/finance-agent-wiki/README.md :: Finance Agent Wiki
    # Finance Agent Wiki ## Stable Knowledge Expansion (2026-06-01) Added stable, non-current finance knowledge: - `concepts/portfolio-and-risk-metrics.md`: portfolio exposure, drawdown, liquidity, correlation, and risk-adju...
[1] wikis/finance-agent-wiki/sources/source-notes.md :: Source Notes — Finance Agent Wiki
    # Source Notes — Finance Agent Wiki ## Policy 本文件记录需要外部来源、实时核验或权威确认的主题。 ## Needs source update - topic: current market prices, OHLCV feeds, order book snapshots, spread, volume and liquidity status: needs-source-update s...
```

### search customs-agent-wiki: INV-EXAMPLE-001 evidence confidence - PASS

```text
[15] wikis/customs-agent-wiki/cases/sample-invoice-extraction.md :: Sample Invoice Extraction
    --- title: Sample Invoice Extraction status: stable last_updated: 2026-05-27 risk_level: medium --- # Sample Invoice Extraction ## Purpose 提供一个合成商业发票字段抽取样例，展示英文表头到标准 JSON 的映射方式。 ## When to use 用于训练或测试 OCR/文本解析到结构化 JSON 的...
[7] wikis/customs-agent-wiki/rules/field-extraction-rules.md :: Customs Field Extraction Rules
    --- title: Customs Field Extraction Rules status: stable last_updated: 2026-05-27 risk_level: medium --- # Customs Field Extraction Rules ## Core fields - shipper / seller / exporter -> 发货人/卖方/出口商 - consignee / buyer / i...
[5] wikis/customs-agent-wiki/evals/customs-agent-evals.yaml :: customs-agent-evals
    wiki: customs-agent-wiki updated: 2026-05-27 tests: - id: customs-extract-001 question: "从发票中抽取 invoice no、currency、total amount。" expected_behavior: "输出标准 JSON，并保留 evidence。" - id: customs-compare-001 question: "合同和发票金额...
[5] wikis/customs-agent-wiki/sources/source-refresh-log.md :: Source Refresh Log
    # Source Refresh Log Wiki: customs-agent-wiki Risk level: medium Freshness requirement: high Template initialized: 2026-05-27 ## Purpose Record authoritative source verification work before current facts are written into...
[3] wikis/customs-agent-wiki/workflows/ocr-to-json.md :: OCR to Structured JSON Workflow
    --- title: OCR to Structured JSON Workflow status: stable last_updated: 2026-05-27 risk_level: medium --- # OCR to Structured JSON Workflow ## Purpose 把扫描件、图片或 PDF 文本解析为可比对的结构化 JSON，同时保留证据和置信度。 ## When to use 用于合同、商业发票、装...
[2] wikis/customs-agent-wiki/cases/sample-document-diff.md :: Sample Document Difference Table
    --- title: Sample Document Difference Table status: stable last_updated: 2026-05-27 risk_level: medium --- # Sample Document Difference Table ## Purpose 提供合同、发票和装箱单差异比对样例，展示风险等级和人工复核建议。 ## When to use 用于测试单证差异表输出、金额币种校验、...
[2] wikis/customs-agent-wiki/update-log.md :: Update Log — Customs Document Agent Wiki
    # Update Log — Customs Document Agent Wiki ## 2026-05-27 - Added source refresh log template for authoritative source verification. - Added sample invoice extraction and document difference cases with expected JSON/table...
[2] wikis/customs-agent-wiki/workflows/document-checking.md :: Customs Document Checking Workflow
    --- title: Customs Document Checking Workflow status: stable last_updated: 2026-05-26 risk_level: medium --- # Customs Document Checking Workflow ## Workflow 1. Identify document types. 2. Extract fields into normalized ...
```

### search agent-engineering-wiki: needs-source-update topics - PASS

```text
[6] wikis/agent-engineering-wiki/cases/sample-rag-source-grounding.md :: Sample RAG Source Grounding Case
    --- title: Sample RAG Source Grounding Case status: stable last_updated: 2026-05-27 risk_level: medium --- # Sample RAG Source Grounding Case ## Purpose 提供一个合成 RAG 评测样例，验证 Agent 是否会引用来源、识别冲突和标记需要来源更新的信息。 ## When to use 用...
[3] wikis/agent-engineering-wiki/evals/agent-engineering-evals.yaml :: agent-engineering-evals
    wiki: agent-engineering-wiki updated: 2026-05-27 tests: - id: agent-arch-001 question: "Agent 由什么组成？" expected_behavior: "说明模型、工具、知识、工作流、记忆、评测和安全边界。" - id: rag-quality-001 question: "如何评测 RAG？" expected_behavior: "覆盖召回、准...
[3] wikis/agent-engineering-wiki/sources/source-notes.md :: Source Notes — Agent Engineering Wiki
    # Source Notes — Agent Engineering Wiki ## Policy 本文件记录需要外部来源、实时核验或权威确认的主题。 ## Needs source update - topic: current Codex Skill format, plugin behavior and tool capabilities status: needs-source-update suggested_sources:...
[1] wikis/agent-engineering-wiki/concepts/rag-knowledge-pack.md :: RAG and Knowledge Pack Foundations
    --- title: RAG and Knowledge Pack Foundations status: stable last_updated: 2026-05-27 risk_level: medium --- # RAG and Knowledge Pack Foundations ## Purpose 定义可被 Agent、RAG 系统和人类共同使用的知识包标准。 ## When to use 用于设计知识库、RAG 管线、检...
[1] wikis/agent-engineering-wiki/evals/smoke-tests.yaml :: smoke-tests
    wiki: agent-engineering-wiki updated: 2026-05-26 tests: - id: structure-001 question: "这个知识库的使用边界是什么？" expected_behavior: "读取 README.md 和 rules/core-rules.md，说明用途、风险等级和限制。" - id: freshness-001 question: "请给我最新政策/价格/API 规...
[1] wikis/agent-engineering-wiki/manifest.yaml :: manifest
    id: agent-engineering-wiki name: Agent Engineering Wiki version: 0.1.0 language: zh-CN domain: ai_agent_engineering risk_level: medium freshness_requirement: medium description: "Agent 架构、RAG、知识包、Codex Skills、评测与安全边界知识库。...
[1] wikis/agent-engineering-wiki/prompts/default-agent.md :: Default Agent Prompt
    --- title: Default Agent Prompt status: stable last_updated: 2026-05-26 risk_level: medium --- # Default Agent Prompt 你是 `Agent Engineering Wiki`。处理任务时必须： 1. 先读取本知识库的 `manifest.yaml`、`AGENTS.md`、`rules/`。 2. 使用稳定知识回答稳定问题...
[1] wikis/agent-engineering-wiki/README.md :: Agent Engineering Wiki
    # Agent Engineering Wiki ## Stable Knowledge Expansion (2026-06-01) Added stable, non-current agent engineering knowledge: - `concepts/agent-memory-and-context.md`: working memory, long-term memory, retrieval-backed memo...
```

### search security-agent-wiki: bypass login Authorization header - PASS

```text
[9] wikis/security-agent-wiki/cases/sample-login-review.md :: Sample Defensive Login Review
    --- title: Sample Defensive Login Review status: stable last_updated: 2026-05-27 risk_level: high --- # Sample Defensive Login Review ## Purpose 提供一个合成登录接口防御性审查样例，验证 Agent 是否输出修复建议而非攻击步骤。 ## When to use 用于代码安全审查、上线前检查、权限...
[2] wikis/security-agent-wiki/update-log.md :: Update Log — Defensive Security Agent Wiki
    # Update Log — Defensive Security Agent Wiki ## 2026-06-01 - Added stable high-density knowledge pages for security controls, secret handling, defensive triage, and secret exposure review. - Updated README and manifest t...
[2] wikis/security-agent-wiki/workflows/defensive-review-triage.md :: Defensive Review Triage
    --- title: Defensive Review Triage status: stable last_updated: 2026-06-01 risk_level: high --- # Defensive Review Triage ## Purpose Provide a stable workflow for triaging defensive security findings without enabling mis...
[1] wikis/security-agent-wiki/README.md :: Defensive Security Agent Wiki
    # Defensive Security Agent Wiki ## Stable Knowledge Expansion (2026-06-01) Added stable, non-current defensive security knowledge: - `concepts/security-control-model.md`: preventive, detective, corrective controls, least...
[1] wikis/security-agent-wiki/sources/source-refresh-log.md :: Source Refresh Log
    # Source Refresh Log Wiki: security-agent-wiki Risk level: high Freshness requirement: high Template initialized: 2026-05-27 ## Purpose Record authoritative source verification work before current facts are written into ...
[1] wikis/security-agent-wiki/workflows/security-review-checklist.md :: Defensive Security Review Checklist
    --- title: Defensive Security Review Checklist status: stable last_updated: 2026-05-26 risk_level: high --- # Defensive Security Review Checklist ## Checklist - Secrets are not committed. - Environment variables are docu...
```

### pack wikis - PASS

```text
packed packs\agent-engineering-wiki.zip
packed packs\airdrop-agent-wiki.zip
packed packs\coding-agent-wiki.zip
packed packs\content-agent-wiki.zip
packed packs\customs-agent-wiki.zip
packed packs\ecommerce-agent-wiki.zip
packed packs\finance-agent-wiki.zip
packed packs\health-agent-wiki.zip
packed packs\legal-agent-wiki.zip
packed packs\nodeops-agent-wiki.zip
packed packs\research-agent-wiki.zip
packed packs\security-agent-wiki.zip
packed packs\agent-wiki-hub-all.zip
```

### audit pack integrity - PASS

```text
Wrote docs\PACK_AUDIT.md
Wrote registry\pack-audit.json
PACK INTEGRITY PASSED (615 checks)
```

### generate release notes - PASS

```text
Wrote docs\RELEASE_NOTES.md
Wrote registry\release-manifest.json
RELEASE NOTES GENERATED (12 wikis, 13 packages)
```

### generate change summary - PASS

```text
Wrote docs\CHANGE_SUMMARY.md
Wrote registry\change-summary.json
CHANGE SUMMARY GENERATED (12 wikis)
```

### pack wikis with acceptance report - PASS

```text
packed packs\agent-engineering-wiki.zip
packed packs\airdrop-agent-wiki.zip
packed packs\coding-agent-wiki.zip
packed packs\content-agent-wiki.zip
packed packs\customs-agent-wiki.zip
packed packs\ecommerce-agent-wiki.zip
packed packs\finance-agent-wiki.zip
packed packs\health-agent-wiki.zip
packed packs\legal-agent-wiki.zip
packed packs\nodeops-agent-wiki.zip
packed packs\research-agent-wiki.zip
packed packs\security-agent-wiki.zip
packed packs\agent-wiki-hub-all.zip
```

### audit final package integrity - PASS

```text
Wrote docs\PACK_AUDIT.md
Wrote registry\pack-audit.json
PACK INTEGRITY PASSED (615 checks)
```
