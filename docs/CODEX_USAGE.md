# How Codex Should Use This Knowledge Base

## Method A: Work inside the hub

```bash
cd ~/agent-wiki-hub
codex
```

Then ask Codex to read `CODEX_BUILD_PROMPT.md`.

## Method B: Link a wiki into a project

```bash
mkdir -p ~/projects/my-project/knowledge
ln -s ~/agent-wiki-hub/wikis/finance-agent-wiki ~/projects/my-project/knowledge/finance-agent-wiki
```

In the target project's `AGENTS.md`, add:

```md
## Knowledge packs

For finance tasks, read `knowledge/finance-agent-wiki/manifest.yaml`, `AGENTS.md`, and `rules/` before editing code.
```

## Method C: Install as a Codex Skill

Copy the skill folder:

```bash
mkdir -p ~/.codex/skills
cp -R codex-skills/agent-wiki-builder ~/.codex/skills/
```

Then invoke it in Codex with a skill mention if your interface supports it, or simply ask Codex to use the `agent-wiki-builder` skill.

## Maintenance checks

```bash
python3 scripts/run_acceptance.py
python3 scripts/check_registry_consistency.py
python3 scripts/audit_ci_workflow.py
python3 scripts/audit_page_metadata.py
python3 scripts/audit_content_coverage.py
python3 scripts/audit_links.py
python3 scripts/audit_pack_integrity.py
python3 scripts/list_source_updates.py
python3 scripts/generate_source_refresh_playbook.py
python3 scripts/generate_source_refresh_tickets.py
python3 scripts/generate_source_refresh_logs.py
python3 scripts/record_source_evidence.py --ticket-id TICKET-SRC-006 --status pending --dry-run
python3 scripts/import_source_evidence_packet.py
python3 scripts/generate_source_evidence_packet_fixtures.py
python3 scripts/audit_source_refresh_completion.py
python3 scripts/audit_source_evidence_quality.py
python3 scripts/generate_source_refresh_dashboard.py
python3 scripts/generate_source_refresh_wave_runner.py
python3 scripts/generate_source_reviewer_queue.py
python3 scripts/generate_source_review_session_plan.py
python3 scripts/generate_source_review_readiness_matrix.py
python3 scripts/generate_source_review_work_orders.py
python3 scripts/generate_source_review_packet_bundle.py
python3 scripts/generate_source_review_packet_classification.py
python3 scripts/generate_source_review_wave_plan.py --wave wave-2
python3 scripts/generate_source_review_wave_2_batch_plan.py
python3 scripts/generate_source_review_wave_3_plan.py
python3 scripts/generate_source_review_wave_packet_bundle.py --plan registry/source-review-wave-3-plan.json --stem source-review-session-wave-3-pending --work-order-dir registry/source-review-work-orders-wave-3
python3 scripts/generate_source_review_final_status.py
python3 scripts/audit_source_review_packets.py
python3 scripts/rehearse_source_review_packet_imports.py
python3 scripts/audit_safety_boundaries.py
python3 scripts/generate_hub_navigation.py
python3 scripts/generate_agent_routing_cards.py
python3 scripts/generate_agent_handoff.py
python3 scripts/generate_release_notes.py
python3 scripts/generate_change_summary.py
python3 scripts/route_wiki.py --query "risk control backtest"
```

Use `docs/ACCEPTANCE_REPORT.md`, `docs/AGENT_HANDOFF.md`, `docs/HUB_NAVIGATION.md`, `docs/AGENT_ROUTING_CARDS.md`, `docs/ROUTING_CLI.md`, `docs/RELEASE_NOTES.md`, `docs/CHANGE_SUMMARY.md`, `docs/WIKI_STATUS.md`, `docs/REGISTRY_CONSISTENCY.md`, `docs/CI_AUDIT.md`, `docs/PAGE_METADATA_AUDIT.md`, `docs/COVERAGE_AUDIT.md`, `docs/LINK_AUDIT.md`, `docs/PACK_AUDIT.md`, `docs/SOURCE_UPDATE_QUEUE.md`, `docs/SOURCE_REFRESH_DASHBOARD.md`, `docs/SOURCE_REFRESH_PLAYBOOK.md`, `docs/SOURCE_REFRESH_TICKETS.md`, `docs/SOURCE_REFRESH_WAVE_RUNNER.md`, `docs/SOURCE_REVIEWER_QUEUE.md`, `docs/SOURCE_REVIEW_SESSION_PLAN.md`, `docs/SOURCE_REVIEW_READINESS_MATRIX.md`, `docs/SOURCE_REVIEW_WORK_ORDERS.md`, `docs/SOURCE_REVIEW_PACKET_BUNDLE.md`, `docs/SOURCE_REVIEW_PACKET_AUDIT.md`, `docs/SOURCE_REVIEW_PACKET_REHEARSAL.md`, `docs/SOURCE_EVIDENCE_RECORDER.md`, `docs/SOURCE_EVIDENCE_PACKET_IMPORTER.md`, `docs/SOURCE_EVIDENCE_PACKET_FIXTURES.md`, `docs/SOURCE_REFRESH_COMPLETION_AUDIT.md`, `docs/SOURCE_EVIDENCE_QUALITY_AUDIT.md`, `docs/SOURCE_REFRESH_LOG_STATUS.md`, and `docs/SAFETY_AUDIT.md` to review readiness, agent handoff, navigation, agent routing, routing CLI usage, release contents, change impact, metadata alignment, CI wiring, page front matter, topic coverage, link integrity, package integrity, source refresh dashboard, source refresh tasks, source refresh tickets, wave-based refresh execution, reviewer-role assignment, review-session planning, per-ticket readiness, source review work orders, review packet templates, review packet auditing, review packet import rehearsal, source evidence recording, packet evidence import, packet import fixtures, source refresh completion, source evidence quality, source refresh log readiness, safety boundaries, and topics that still need authoritative source verification.

## CI

GitHub Actions workflow: `.github/workflows/wiki-acceptance.yml`

It runs `python3 scripts/run_acceptance.py` on pull requests, pushes to `main` or `master`, and manual dispatches. See `docs/CI_USAGE.md` for operating notes.
