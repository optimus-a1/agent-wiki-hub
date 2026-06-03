---
title: Model Risk And Backtest Hygiene
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Model Risk And Backtest Hygiene

## Purpose
Provide stable rules for preventing misleading financial models and overconfident backtest conclusions.

## When to use
Use when reviewing quantitative signals, portfolio simulations, screening logic, or performance claims.

## Stable knowledge points
- KP-01: A model is a simplified decision aid, not a complete description of markets or business reality.
- KP-02: Backtests are vulnerable to lookahead bias when future information leaks into past decisions.
- KP-03: Survivorship bias appears when failed, delisted, or unavailable instruments are excluded from the tested universe.
- KP-04: Data snooping occurs when repeated trials are treated as one independent discovery.
- KP-05: Overfitting occurs when rules fit historical noise instead of durable behavior.
- KP-06: Transaction costs include explicit fees and implicit execution costs such as spread and slippage.
- KP-07: Capacity limits appear when simulated trade size is too large for realistic liquidity.
- KP-08: Model governance requires assumptions, parameters, validation results, and change history to be reviewable.

## Core rules
- Treat every impressive result as a hypothesis until falsified by robustness checks.
- Keep training, validation, and out-of-sample review logically separate.
- Record all rejected variants when practical.
- Never imply that simulated returns guarantee future performance.

## Workflow
1. Define the investment hypothesis and decision boundary before testing.
2. Check universe construction, timestamps, corporate actions, missing data, and survivorship.
3. Add fees, spread, slippage, latency, and realistic position sizing.
4. Test robustness across parameter ranges and independent periods.
5. Report limitations, failure modes, and human review gates.

## Edge cases
- A strategy can pass out-of-sample review by chance if many variants were tried.
- A signal can be economically weak even when statistically visible.
- Portfolio-level constraints can invalidate instrument-level backtests.

## Validation checks
- No future data is used in simulated past decisions.
- Costs and liquidity assumptions are explicit.
- Results include drawdown and failure analysis.
- Output remains educational and non-personalized.

## Source notes
Stable modeling hygiene only. No current prices, tax rules, regulations, broker rules, or live execution parameters are included.
