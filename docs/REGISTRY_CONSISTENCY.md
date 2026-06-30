# Registry Consistency Report

Generated: 2026-06-30

## Summary

- Checks: 234
- Passed: 234
- Failed: 0

## Checks

| Check | Result | Evidence |
| --- | --- | --- |
| registry_exists | PASS | registry/wiki-registry.yaml |
| registry_version | PASS | 0.1.0 |
| registry_updated | PASS | 2026-05-27 |
| registry_records | PASS | 12 records |
| registry_unique_ids | PASS | 12 unique ids / 12 records |
| registry_matches_wiki_dirs | PASS | registry=12, directories=12 |
| finance-agent-wiki:path_exists | PASS | wikis/finance-agent-wiki |
| finance-agent-wiki:path_basename_matches_id | PASS | finance-agent-wiki vs finance-agent-wiki |
| finance-agent-wiki:manifest_id | PASS | finance-agent-wiki vs finance-agent-wiki |
| finance-agent-wiki:domain | PASS | finance vs finance |
| finance-agent-wiki:risk_level | PASS | high vs high |
| finance-agent-wiki:freshness | PASS | high vs high |
| finance-agent-wiki:entrypoint:README.md | PASS | README.md |
| finance-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| finance-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| finance-agent-wiki:required_directory:concepts | PASS | concepts |
| finance-agent-wiki:required_directory:rules | PASS | rules |
| finance-agent-wiki:required_directory:workflows | PASS | workflows |
| finance-agent-wiki:required_directory:cases | PASS | cases |
| finance-agent-wiki:required_directory:tools | PASS | tools |
| finance-agent-wiki:required_directory:prompts | PASS | prompts |
| finance-agent-wiki:required_directory:evals | PASS | evals |
| finance-agent-wiki:required_directory:sources | PASS | sources |
| finance-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| finance-agent-wiki:safety_flags | PASS | 3/3 flags |
| customs-agent-wiki:path_exists | PASS | wikis/customs-agent-wiki |
| customs-agent-wiki:path_basename_matches_id | PASS | customs-agent-wiki vs customs-agent-wiki |
| customs-agent-wiki:manifest_id | PASS | customs-agent-wiki vs customs-agent-wiki |
| customs-agent-wiki:domain | PASS | customs_trade_documents vs customs_trade_documents |
| customs-agent-wiki:risk_level | PASS | medium vs medium |
| customs-agent-wiki:freshness | PASS | high vs high |
| customs-agent-wiki:entrypoint:README.md | PASS | README.md |
| customs-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| customs-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| customs-agent-wiki:required_directory:concepts | PASS | concepts |
| customs-agent-wiki:required_directory:rules | PASS | rules |
| customs-agent-wiki:required_directory:workflows | PASS | workflows |
| customs-agent-wiki:required_directory:cases | PASS | cases |
| customs-agent-wiki:required_directory:tools | PASS | tools |
| customs-agent-wiki:required_directory:prompts | PASS | prompts |
| customs-agent-wiki:required_directory:evals | PASS | evals |
| customs-agent-wiki:required_directory:sources | PASS | sources |
| customs-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| customs-agent-wiki:safety_flags | PASS | 3/3 flags |
| coding-agent-wiki:path_exists | PASS | wikis/coding-agent-wiki |
| coding-agent-wiki:path_basename_matches_id | PASS | coding-agent-wiki vs coding-agent-wiki |
| coding-agent-wiki:manifest_id | PASS | coding-agent-wiki vs coding-agent-wiki |
| coding-agent-wiki:domain | PASS | software_engineering vs software_engineering |
| coding-agent-wiki:risk_level | PASS | medium vs medium |
| coding-agent-wiki:freshness | PASS | medium vs medium |
| coding-agent-wiki:entrypoint:README.md | PASS | README.md |
| coding-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| coding-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| coding-agent-wiki:required_directory:concepts | PASS | concepts |
| coding-agent-wiki:required_directory:rules | PASS | rules |
| coding-agent-wiki:required_directory:workflows | PASS | workflows |
| coding-agent-wiki:required_directory:cases | PASS | cases |
| coding-agent-wiki:required_directory:tools | PASS | tools |
| coding-agent-wiki:required_directory:prompts | PASS | prompts |
| coding-agent-wiki:required_directory:evals | PASS | evals |
| coding-agent-wiki:required_directory:sources | PASS | sources |
| coding-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| coding-agent-wiki:safety_flags | PASS | 3/3 flags |
| agent-engineering-wiki:path_exists | PASS | wikis/agent-engineering-wiki |
| agent-engineering-wiki:path_basename_matches_id | PASS | agent-engineering-wiki vs agent-engineering-wiki |
| agent-engineering-wiki:manifest_id | PASS | agent-engineering-wiki vs agent-engineering-wiki |
| agent-engineering-wiki:domain | PASS | ai_agent_engineering vs ai_agent_engineering |
| agent-engineering-wiki:risk_level | PASS | medium vs medium |
| agent-engineering-wiki:freshness | PASS | medium vs medium |
| agent-engineering-wiki:entrypoint:README.md | PASS | README.md |
| agent-engineering-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| agent-engineering-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| agent-engineering-wiki:required_directory:concepts | PASS | concepts |
| agent-engineering-wiki:required_directory:rules | PASS | rules |
| agent-engineering-wiki:required_directory:workflows | PASS | workflows |
| agent-engineering-wiki:required_directory:cases | PASS | cases |
| agent-engineering-wiki:required_directory:tools | PASS | tools |
| agent-engineering-wiki:required_directory:prompts | PASS | prompts |
| agent-engineering-wiki:required_directory:evals | PASS | evals |
| agent-engineering-wiki:required_directory:sources | PASS | sources |
| agent-engineering-wiki:trigger_keywords | PASS | trigger_keywords |
| agent-engineering-wiki:safety_flags | PASS | 3/3 flags |
| ecommerce-agent-wiki:path_exists | PASS | wikis/ecommerce-agent-wiki |
| ecommerce-agent-wiki:path_basename_matches_id | PASS | ecommerce-agent-wiki vs ecommerce-agent-wiki |
| ecommerce-agent-wiki:manifest_id | PASS | ecommerce-agent-wiki vs ecommerce-agent-wiki |
| ecommerce-agent-wiki:domain | PASS | ecommerce vs ecommerce |
| ecommerce-agent-wiki:risk_level | PASS | medium vs medium |
| ecommerce-agent-wiki:freshness | PASS | high vs high |
| ecommerce-agent-wiki:entrypoint:README.md | PASS | README.md |
| ecommerce-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| ecommerce-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| ecommerce-agent-wiki:required_directory:concepts | PASS | concepts |
| ecommerce-agent-wiki:required_directory:rules | PASS | rules |
| ecommerce-agent-wiki:required_directory:workflows | PASS | workflows |
| ecommerce-agent-wiki:required_directory:cases | PASS | cases |
| ecommerce-agent-wiki:required_directory:tools | PASS | tools |
| ecommerce-agent-wiki:required_directory:prompts | PASS | prompts |
| ecommerce-agent-wiki:required_directory:evals | PASS | evals |
| ecommerce-agent-wiki:required_directory:sources | PASS | sources |
| ecommerce-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| ecommerce-agent-wiki:safety_flags | PASS | 3/3 flags |
| nodeops-agent-wiki:path_exists | PASS | wikis/nodeops-agent-wiki |
| nodeops-agent-wiki:path_basename_matches_id | PASS | nodeops-agent-wiki vs nodeops-agent-wiki |
| nodeops-agent-wiki:manifest_id | PASS | nodeops-agent-wiki vs nodeops-agent-wiki |
| nodeops-agent-wiki:domain | PASS | operations vs operations |
| nodeops-agent-wiki:risk_level | PASS | high vs high |
| nodeops-agent-wiki:freshness | PASS | medium vs medium |
| nodeops-agent-wiki:entrypoint:README.md | PASS | README.md |
| nodeops-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| nodeops-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| nodeops-agent-wiki:required_directory:concepts | PASS | concepts |
| nodeops-agent-wiki:required_directory:rules | PASS | rules |
| nodeops-agent-wiki:required_directory:workflows | PASS | workflows |
| nodeops-agent-wiki:required_directory:cases | PASS | cases |
| nodeops-agent-wiki:required_directory:tools | PASS | tools |
| nodeops-agent-wiki:required_directory:prompts | PASS | prompts |
| nodeops-agent-wiki:required_directory:evals | PASS | evals |
| nodeops-agent-wiki:required_directory:sources | PASS | sources |
| nodeops-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| nodeops-agent-wiki:safety_flags | PASS | 3/3 flags |
| airdrop-agent-wiki:path_exists | PASS | wikis/airdrop-agent-wiki |
| airdrop-agent-wiki:path_basename_matches_id | PASS | airdrop-agent-wiki vs airdrop-agent-wiki |
| airdrop-agent-wiki:manifest_id | PASS | airdrop-agent-wiki vs airdrop-agent-wiki |
| airdrop-agent-wiki:domain | PASS | web3_research vs web3_research |
| airdrop-agent-wiki:risk_level | PASS | high vs high |
| airdrop-agent-wiki:freshness | PASS | high vs high |
| airdrop-agent-wiki:entrypoint:README.md | PASS | README.md |
| airdrop-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| airdrop-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| airdrop-agent-wiki:required_directory:concepts | PASS | concepts |
| airdrop-agent-wiki:required_directory:rules | PASS | rules |
| airdrop-agent-wiki:required_directory:workflows | PASS | workflows |
| airdrop-agent-wiki:required_directory:cases | PASS | cases |
| airdrop-agent-wiki:required_directory:tools | PASS | tools |
| airdrop-agent-wiki:required_directory:prompts | PASS | prompts |
| airdrop-agent-wiki:required_directory:evals | PASS | evals |
| airdrop-agent-wiki:required_directory:sources | PASS | sources |
| airdrop-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| airdrop-agent-wiki:safety_flags | PASS | 3/3 flags |
| content-agent-wiki:path_exists | PASS | wikis/content-agent-wiki |
| content-agent-wiki:path_basename_matches_id | PASS | content-agent-wiki vs content-agent-wiki |
| content-agent-wiki:manifest_id | PASS | content-agent-wiki vs content-agent-wiki |
| content-agent-wiki:domain | PASS | content_operations vs content_operations |
| content-agent-wiki:risk_level | PASS | low vs low |
| content-agent-wiki:freshness | PASS | medium vs medium |
| content-agent-wiki:entrypoint:README.md | PASS | README.md |
| content-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| content-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| content-agent-wiki:required_directory:concepts | PASS | concepts |
| content-agent-wiki:required_directory:rules | PASS | rules |
| content-agent-wiki:required_directory:workflows | PASS | workflows |
| content-agent-wiki:required_directory:cases | PASS | cases |
| content-agent-wiki:required_directory:tools | PASS | tools |
| content-agent-wiki:required_directory:prompts | PASS | prompts |
| content-agent-wiki:required_directory:evals | PASS | evals |
| content-agent-wiki:required_directory:sources | PASS | sources |
| content-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| content-agent-wiki:safety_flags | PASS | 3/3 flags |
| legal-agent-wiki:path_exists | PASS | wikis/legal-agent-wiki |
| legal-agent-wiki:path_basename_matches_id | PASS | legal-agent-wiki vs legal-agent-wiki |
| legal-agent-wiki:manifest_id | PASS | legal-agent-wiki vs legal-agent-wiki |
| legal-agent-wiki:domain | PASS | legal_information vs legal_information |
| legal-agent-wiki:risk_level | PASS | high vs high |
| legal-agent-wiki:freshness | PASS | high vs high |
| legal-agent-wiki:entrypoint:README.md | PASS | README.md |
| legal-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| legal-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| legal-agent-wiki:required_directory:concepts | PASS | concepts |
| legal-agent-wiki:required_directory:rules | PASS | rules |
| legal-agent-wiki:required_directory:workflows | PASS | workflows |
| legal-agent-wiki:required_directory:cases | PASS | cases |
| legal-agent-wiki:required_directory:tools | PASS | tools |
| legal-agent-wiki:required_directory:prompts | PASS | prompts |
| legal-agent-wiki:required_directory:evals | PASS | evals |
| legal-agent-wiki:required_directory:sources | PASS | sources |
| legal-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| legal-agent-wiki:safety_flags | PASS | 3/3 flags |
| health-agent-wiki:path_exists | PASS | wikis/health-agent-wiki |
| health-agent-wiki:path_basename_matches_id | PASS | health-agent-wiki vs health-agent-wiki |
| health-agent-wiki:manifest_id | PASS | health-agent-wiki vs health-agent-wiki |
| health-agent-wiki:domain | PASS | health_education vs health_education |
| health-agent-wiki:risk_level | PASS | high vs high |
| health-agent-wiki:freshness | PASS | high vs high |
| health-agent-wiki:entrypoint:README.md | PASS | README.md |
| health-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| health-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| health-agent-wiki:required_directory:concepts | PASS | concepts |
| health-agent-wiki:required_directory:rules | PASS | rules |
| health-agent-wiki:required_directory:workflows | PASS | workflows |
| health-agent-wiki:required_directory:cases | PASS | cases |
| health-agent-wiki:required_directory:tools | PASS | tools |
| health-agent-wiki:required_directory:prompts | PASS | prompts |
| health-agent-wiki:required_directory:evals | PASS | evals |
| health-agent-wiki:required_directory:sources | PASS | sources |
| health-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| health-agent-wiki:safety_flags | PASS | 3/3 flags |
| research-agent-wiki:path_exists | PASS | wikis/research-agent-wiki |
| research-agent-wiki:path_basename_matches_id | PASS | research-agent-wiki vs research-agent-wiki |
| research-agent-wiki:manifest_id | PASS | research-agent-wiki vs research-agent-wiki |
| research-agent-wiki:domain | PASS | research vs research |
| research-agent-wiki:risk_level | PASS | medium vs medium |
| research-agent-wiki:freshness | PASS | high vs high |
| research-agent-wiki:entrypoint:README.md | PASS | README.md |
| research-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| research-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| research-agent-wiki:required_directory:concepts | PASS | concepts |
| research-agent-wiki:required_directory:rules | PASS | rules |
| research-agent-wiki:required_directory:workflows | PASS | workflows |
| research-agent-wiki:required_directory:cases | PASS | cases |
| research-agent-wiki:required_directory:tools | PASS | tools |
| research-agent-wiki:required_directory:prompts | PASS | prompts |
| research-agent-wiki:required_directory:evals | PASS | evals |
| research-agent-wiki:required_directory:sources | PASS | sources |
| research-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| research-agent-wiki:safety_flags | PASS | 3/3 flags |
| security-agent-wiki:path_exists | PASS | wikis/security-agent-wiki |
| security-agent-wiki:path_basename_matches_id | PASS | security-agent-wiki vs security-agent-wiki |
| security-agent-wiki:manifest_id | PASS | security-agent-wiki vs security-agent-wiki |
| security-agent-wiki:domain | PASS | defensive_security vs defensive_security |
| security-agent-wiki:risk_level | PASS | high vs high |
| security-agent-wiki:freshness | PASS | high vs high |
| security-agent-wiki:entrypoint:README.md | PASS | README.md |
| security-agent-wiki:entrypoint:AGENTS.md | PASS | AGENTS.md |
| security-agent-wiki:entrypoint:rules/core-rules.md | PASS | rules/core-rules.md |
| security-agent-wiki:required_directory:concepts | PASS | concepts |
| security-agent-wiki:required_directory:rules | PASS | rules |
| security-agent-wiki:required_directory:workflows | PASS | workflows |
| security-agent-wiki:required_directory:cases | PASS | cases |
| security-agent-wiki:required_directory:tools | PASS | tools |
| security-agent-wiki:required_directory:prompts | PASS | prompts |
| security-agent-wiki:required_directory:evals | PASS | evals |
| security-agent-wiki:required_directory:sources | PASS | sources |
| security-agent-wiki:trigger_keywords | PASS | trigger_keywords |
| security-agent-wiki:safety_flags | PASS | 3/3 flags |

## Usage Notes

- Run this after adding, renaming, or changing a wiki manifest.
- Failed checks usually mean registry, manifest, or directory metadata drifted apart.
- This report does not verify source freshness or safety behavior; use the source queue and safety audit reports for those gates.
