# Safety Boundary Audit

Generated: 2026-05-31

## Summary

- Wikis scanned: 12
- High/medium risk wikis with required checks: 11
- Required checks: 75
- Failed required checks: 0

## Required Check Results

| Wiki | Risk | Check | Result | Evidence |
| --- | --- | --- | --- | --- |
| agent-engineering-wiki | medium | manifest_safety_flags | PASS | 3/3 safety flags found |
| agent-engineering-wiki | medium | source_notes_queue | PASS | wikis/agent-engineering-wiki/sources/source-notes.md checked |
| agent-engineering-wiki | medium | human_confirmation_points | PASS | matched 1/1 required term groups |
| agent-engineering-wiki | medium | secret_storage_boundary | PASS | matched 1/1 required term groups |
| agent-engineering-wiki | medium | agent_pack_quality_controls | PASS | matched 4/4 required term groups |
| agent-engineering-wiki | medium | agent_high_risk_boundaries | PASS | matched 2/2 required term groups |
| airdrop-agent-wiki | high | manifest_safety_flags | PASS | 3/3 safety flags found |
| airdrop-agent-wiki | high | source_notes_queue | PASS | wikis/airdrop-agent-wiki/sources/source-notes.md checked |
| airdrop-agent-wiki | high | human_confirmation_points | PASS | matched 1/1 required term groups |
| airdrop-agent-wiki | high | secret_storage_boundary | PASS | matched 1/1 required term groups |
| airdrop-agent-wiki | high | high_risk_rules_before_workflows | PASS | rules index=185, workflows index=197 |
| airdrop-agent-wiki | high | airdrop_no_sybil_or_spam | PASS | matched 4/4 required term groups |
| airdrop-agent-wiki | high | airdrop_wallet_secret_protection | PASS | matched 4/4 required term groups |
| airdrop-agent-wiki | high | airdrop_current_rule_freshness | PASS | matched 2/2 required term groups |
| coding-agent-wiki | medium | manifest_safety_flags | PASS | 3/3 safety flags found |
| coding-agent-wiki | medium | source_notes_queue | PASS | wikis/coding-agent-wiki/sources/source-notes.md checked |
| coding-agent-wiki | medium | human_confirmation_points | PASS | matched 1/1 required term groups |
| coding-agent-wiki | medium | secret_storage_boundary | PASS | matched 1/1 required term groups |
| coding-agent-wiki | medium | coding_secret_and_permission_boundary | PASS | matched 3/3 required term groups |
| coding-agent-wiki | medium | coding_deploy_safety | PASS | matched 4/4 required term groups |
| customs-agent-wiki | medium | manifest_safety_flags | PASS | 3/3 safety flags found |
| customs-agent-wiki | medium | source_notes_queue | PASS | wikis/customs-agent-wiki/sources/source-notes.md checked |
| customs-agent-wiki | medium | human_confirmation_points | PASS | matched 1/1 required term groups |
| customs-agent-wiki | medium | secret_storage_boundary | PASS | matched 1/1 required term groups |
| customs-agent-wiki | medium | customs_document_diff_controls | PASS | matched 4/4 required term groups |
| customs-agent-wiki | medium | customs_regulatory_freshness | PASS | matched 2/2 required term groups |
| ecommerce-agent-wiki | medium | manifest_safety_flags | PASS | 3/3 safety flags found |
| ecommerce-agent-wiki | medium | source_notes_queue | PASS | wikis/ecommerce-agent-wiki/sources/source-notes.md checked |
| ecommerce-agent-wiki | medium | human_confirmation_points | PASS | matched 1/1 required term groups |
| ecommerce-agent-wiki | medium | secret_storage_boundary | PASS | matched 1/1 required term groups |
| ecommerce-agent-wiki | medium | ecommerce_policy_and_privacy | PASS | matched 4/4 required term groups |
| finance-agent-wiki | high | manifest_safety_flags | PASS | 3/3 safety flags found |
| finance-agent-wiki | high | source_notes_queue | PASS | wikis/finance-agent-wiki/sources/source-notes.md checked |
| finance-agent-wiki | high | human_confirmation_points | PASS | matched 1/1 required term groups |
| finance-agent-wiki | high | secret_storage_boundary | PASS | matched 1/1 required term groups |
| finance-agent-wiki | high | high_risk_rules_before_workflows | PASS | rules index=187, workflows index=199 |
| finance-agent-wiki | high | finance_no_personalized_advice | PASS | matched 1/1 required term groups |
| finance-agent-wiki | high | finance_no_real_money_autonomy | PASS | matched 2/2 required term groups |
| finance-agent-wiki | high | finance_paper_trading_default | PASS | matched 1/1 required term groups |
| finance-agent-wiki | high | finance_risk_controls | PASS | matched 5/5 required term groups |
| health-agent-wiki | high | manifest_safety_flags | PASS | 3/3 safety flags found |
| health-agent-wiki | high | source_notes_queue | PASS | wikis/health-agent-wiki/sources/source-notes.md checked |
| health-agent-wiki | high | human_confirmation_points | PASS | matched 1/1 required term groups |
| health-agent-wiki | high | secret_storage_boundary | PASS | matched 1/1 required term groups |
| health-agent-wiki | high | high_risk_rules_before_workflows | PASS | rules index=174, workflows index=186 |
| health-agent-wiki | high | health_no_diagnosis_or_prescription | PASS | matched 3/3 required term groups |
| health-agent-wiki | high | health_red_flags_and_care | PASS | matched 2/2 required term groups |
| legal-agent-wiki | high | manifest_safety_flags | PASS | 3/3 safety flags found |
| legal-agent-wiki | high | source_notes_queue | PASS | wikis/legal-agent-wiki/sources/source-notes.md checked |
| legal-agent-wiki | high | human_confirmation_points | PASS | matched 1/1 required term groups |
| legal-agent-wiki | high | secret_storage_boundary | PASS | matched 1/1 required term groups |
| legal-agent-wiki | high | high_risk_rules_before_workflows | PASS | rules index=175, workflows index=187 |
| legal-agent-wiki | high | legal_no_final_opinion | PASS | matched 2/2 required term groups |
| legal-agent-wiki | high | legal_current_law_freshness | PASS | matched 3/3 required term groups |
| nodeops-agent-wiki | high | manifest_safety_flags | PASS | 3/3 safety flags found |
| nodeops-agent-wiki | high | source_notes_queue | PASS | wikis/nodeops-agent-wiki/sources/source-notes.md checked |
| nodeops-agent-wiki | high | human_confirmation_points | PASS | matched 1/1 required term groups |
| nodeops-agent-wiki | high | secret_storage_boundary | PASS | matched 1/1 required term groups |
| nodeops-agent-wiki | high | high_risk_rules_before_workflows | PASS | rules index=191, workflows index=203 |
| nodeops-agent-wiki | high | nodeops_change_safety | PASS | matched 4/4 required term groups |
| nodeops-agent-wiki | high | nodeops_destructive_boundary | PASS | matched 2/2 required term groups |
| research-agent-wiki | medium | manifest_safety_flags | PASS | 3/3 safety flags found |
| research-agent-wiki | medium | source_notes_queue | PASS | wikis/research-agent-wiki/sources/source-notes.md checked |
| research-agent-wiki | medium | human_confirmation_points | PASS | matched 1/1 required term groups |
| research-agent-wiki | medium | secret_storage_boundary | PASS | matched 1/1 required term groups |
| research-agent-wiki | medium | research_source_grounding | PASS | matched 4/4 required term groups |
| security-agent-wiki | high | manifest_safety_flags | PASS | 3/3 safety flags found |
| security-agent-wiki | high | source_notes_queue | PASS | wikis/security-agent-wiki/sources/source-notes.md checked |
| security-agent-wiki | high | human_confirmation_points | PASS | matched 1/1 required term groups |
| security-agent-wiki | high | secret_storage_boundary | PASS | matched 1/1 required term groups |
| security-agent-wiki | high | high_risk_rules_before_workflows | PASS | rules index=182, workflows index=194 |
| security-agent-wiki | high | security_defensive_only | PASS | matched 2/2 required term groups |
| security-agent-wiki | high | security_no_attack_steps | PASS | matched 6/6 required term groups |
| security-agent-wiki | high | security_secret_and_log_boundary | PASS | matched 2/2 required term groups |
| security-agent-wiki | high | security_vulnerability_freshness | PASS | matched 3/3 required term groups |

## Informational Low-Risk Checks

| Wiki | Check | Result |
| --- | --- | --- |
| content-agent-wiki | manifest_safety_flags | PASS |
| content-agent-wiki | source_notes_queue | PASS |
| content-agent-wiki | human_confirmation_points | PASS |
| content-agent-wiki | secret_storage_boundary | PASS |

## Usage Notes

- Treat this as a structural safety audit, not a substitute for legal, medical, financial, security, or compliance review.
- Failed required checks mean the pack needs clearer safety boundaries before it should be used for high-risk workflows.
- Current facts still require authoritative source verification through `docs/SOURCE_UPDATE_QUEUE.md`.
