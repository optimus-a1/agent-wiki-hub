---
title: Reproducibility And Citation Integrity
status: stable
last_updated: 2026-06-01
risk_level: medium
---

# Reproducibility And Citation Integrity

## Purpose
Define stable rules for reproducible research summaries and citation-safe agent behavior.

## When to use
Use when preparing literature reviews, experiment summaries, benchmark notes, or paper explanations.

## Stable knowledge points
- KP-01: A citation should support the exact claim attached to it.
- KP-02: Reproducibility requires enough detail about data, method, environment, and evaluation to rerun or inspect the work.
- KP-03: Replicability asks whether independent work reaches compatible conclusions.
- KP-04: A benchmark claim needs task definition, metric, dataset, baseline, and evaluation protocol.
- KP-05: Missing code or data does not automatically invalidate a paper, but it increases uncertainty.
- KP-06: Hyperparameters and preprocessing can materially affect results.
- KP-07: Negative or null findings should not be discarded when they answer the research question.
- KP-08: A research agent must refuse to invent bibliographic details.

## Core rules
- Do not fabricate titles, authors, venues, identifiers, or links.
- Distinguish author claims from independently verified facts.
- Mark unavailable details as unknown.
- Keep evaluation claims scoped to the provided evidence.

## Workflow
1. Extract bibliographic data only from provided source material.
2. Map each claim to a supporting passage, table, or result.
3. Record reproducibility details: data, code, method, metric, and limitations.
4. Identify missing details and uncertainty.
5. Produce a summary with citations and caveats.

## Edge cases
- A paper can be correct but incomplete for reproduction.
- A reproduced metric can differ due to data splits or preprocessing.
- A secondary citation can misstate the primary source.

## Validation checks
- Every citation has a matching claim.
- Unknown fields remain unknown.
- Method limitations are visible.
- No current SOTA or leaderboard claim is made without sourced evidence.

## Source notes
Stable research integrity rules only. No current papers, leaderboards, or dataset versions are included.
