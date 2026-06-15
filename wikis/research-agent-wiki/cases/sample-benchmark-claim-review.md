---
title: Sample Benchmark Claim Review
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Sample Benchmark Claim Review

## Purpose
Show how a research agent should evaluate a benchmark claim without inventing results or rankings.

## When to use
Use as a case pattern when a paper or project claims strong benchmark performance.

## Stable knowledge points
- KP-01: Benchmark claims require task, dataset, metric, baseline, and evaluation protocol.
- KP-02: A single aggregate score can hide subgroup failures.
- KP-03: Data leakage can make benchmark performance misleading.
- KP-04: Hyperparameter tuning on the test set invalidates the comparison.
- KP-05: Inconsistent preprocessing can make methods incomparable.
- KP-06: Statistical uncertainty matters when differences are small.
- KP-07: Efficiency, robustness, and failure behavior can matter beyond headline score.
- KP-08: A safe summary reports what the provided evidence supports and what remains unknown.

## Core rules
- Do not create or update rankings without current authoritative evidence.
- Do not infer missing baselines.
- Distinguish reported results from independently reproduced results.
- Flag missing evaluation details.

## Workflow
1. Extract the exact benchmark claim.
2. Identify task, dataset, split, metric, baseline, and protocol.
3. Check for leakage, comparability, uncertainty, and missing details.
4. Summarize supported findings and limitations.
5. Recommend reproducibility review before relying on the claim.

## Edge cases
- A benchmark can be saturated and no longer discriminate well.
- A method can optimize the metric while harming practical usefulness.
- A result can be strong on one task and weak on adjacent tasks.

## Validation checks
- No unsourced current ranking is stated.
- Evidence and uncertainty are separated.
- Missing details are marked unknown.
- The final answer does not fabricate citations.

## Source notes
Stable benchmark review case only. No current leaderboard, model version, dataset version, or paper result is included.
