---
title: Portfolio Review Workflow
status: stable
last_updated: 2026-06-01
risk_level: high
---

# Portfolio Review Workflow

## Purpose
Offer a stable review workflow for simulated or educational portfolio analysis.

## When to use
Use when an agent must summarize portfolio risk, check assumptions, and prepare a human-readable review without recommending trades.

## Stable knowledge points
- KP-01: A portfolio review starts with objectives and constraints before metrics.
- KP-02: Holdings should be grouped by exposure drivers, not only by instrument names.
- KP-03: Concentration risk can come from common factors even when holdings look diverse.
- KP-04: Liquidity review should consider exit size, market depth, and stress behavior.
- KP-05: Leverage review must include direct borrowing, derivatives, and embedded leverage.
- KP-06: Scenario analysis is useful because historical averages hide path-dependent losses.
- KP-07: Operational controls matter because process errors can create losses independent of market movement.
- KP-08: A review should end with questions for humans, not automatic real-money action.

## Core rules
- Default to simulation and education.
- Do not tell a user what to buy, sell, or hold for their personal situation.
- Mark uncertain inputs and missing constraints.
- Require human confirmation before any financial action.

## Workflow
1. Clarify scope, objective, horizon, constraints, and whether data is simulated.
2. Build exposure tables for positions, sectors, currencies, factors, leverage, and liquidity.
3. Review concentration, drawdown, volatility, correlation, and stress scenarios.
4. Identify data quality problems and assumptions that dominate results.
5. Produce a neutral report with risk notes, open questions, and human review points.

## Edge cases
- Missing cash or margin data can make exposure numbers misleading.
- Options and structured products require payoff-aware review.
- Short positions can create asymmetric loss and recall risk.

## Validation checks
- Report states that it is not individualized investment advice.
- All calculations identify input sources or simulation assumptions.
- No real trade is executed or instructed.
- Human confirmation points are explicit.

## Source notes
Stable workflow only. It does not include current holdings, prices, broker data, or market conditions.
