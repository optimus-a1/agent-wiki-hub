# Wiki Routing CLI

## Purpose

`scripts/route_wiki.py` routes a user query to the most relevant Agent Wiki and prints the required reading order, source gates, safety rules, and prohibited actions.

## Usage

```bash
python3 scripts/generate_agent_routing_cards.py
python3 scripts/route_wiki.py --query "risk control backtest paper trading"
python3 scripts/route_wiki.py --query "field extraction invoice packing list" --json
```

## Output Fields

- `top_wiki`: the recommended wiki id.
- `source_update_required`: true when the query appears to ask for current prices, policies, laws, platform rules, APIs, versions, advisories, guidelines, or similar current facts.
- `safety_gate_required`: true when the matched wiki is high risk or the query contains high-risk terms.
- `required_reading_order`: files and directories an agent should read before acting.
- `source_gates`: files and reports to check before writing current facts.
- `safety_rules`: boundary rules to preserve in the answer.
- `prohibited_actions`: actions the agent must not perform.

## Validation Examples

```bash
python3 scripts/route_wiki.py --query "risk control" --json
python3 scripts/route_wiki.py --query "field extraction" --json
python3 scripts/route_wiki.py --query "defensive security hardening" --json
python3 scripts/run_acceptance.py
```

## Safety Notes

- The router is a local heuristic over generated routing cards; it does not verify current facts.
- When `source_update_required` is true, check `docs/SOURCE_UPDATE_QUEUE.md`, the wiki's `sources/source-notes.md`, and `sources/source-refresh-log.md` before writing factual claims.
- For high-risk finance, legal, health, security, airdrop, and operations tasks, keep human confirmation points in the final output.
