---
title: Sample Overfitting Detection
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Sample Overfitting Detection

## Purpose
Show how a finance agent should respond to a suspiciously strong backtest without inventing facts or encouraging live trading.

## When to use
Use as a review case for strategy reports that show high performance but weak validation evidence.

## Stable knowledge points
- KP-01: A smooth equity curve can be a warning sign when the strategy logic is complex and unexplained.
- KP-02: Too many tuned parameters increase the chance that the backtest fits noise.
- KP-03: Performance that disappears after costs suggests execution assumptions dominate the result.
- KP-04: A signal that works only in one narrow period may not represent stable behavior.
- KP-05: Reusing the same out-of-sample set repeatedly makes it part of model selection.
- KP-06: Ignoring liquidity can make small simulated edges impossible to capture.
- KP-07: A valid review asks for falsification tests instead of celebrating a headline return.
- KP-08: A safe agent refuses to convert a questionable backtest into a real-money instruction.

## Core rules
- Treat the result as unverified research.
- Ask for data lineage, parameter history, and rejected variants.
- Require cost, slippage, and capacity checks.
- Keep outputs educational and simulation-only.

## Workflow
1. Summarize the claim and the decision rule.
2. Identify possible lookahead, survivorship, selection, and data snooping risks.
3. Request robustness checks, alternate samples, and stress scenarios.
4. Explain what evidence would weaken the claim.
5. Produce a risk table and human review checklist.

## Edge cases
- A simple rule can still be overfit if it was selected from many hidden trials.
- A real economic rationale does not remove the need for validation.
- Strong paper performance can fail under capital constraints.

## Validation checks
- No live trading recommendation is made.
- The case distinguishes hypothesis, evidence, and uncertainty.
- Human approval is required before operational use.
- All current market facts are excluded.

## Source notes
Stable failure-pattern case only. No current strategy, price, broker, or exchange data is included.
