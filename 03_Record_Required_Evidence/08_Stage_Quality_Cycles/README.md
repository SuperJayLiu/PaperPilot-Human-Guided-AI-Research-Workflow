# Stage Quality Cycles

Every research stage must pass **three local quality rounds** before the agent treats that stage as ready for the next stage.

This is separate from the final whole-paper review. The final whole-paper review checks the manuscript as a system. This folder checks each stage when it is created or revised.

## Required stage loop

For each stage:

```text
Stage draft or plan
  -> Round 1: internal consistency and missing-input check
  -> revise approved fixes
  -> Round 2: evidence, data, method, and feasibility check
  -> revise approved fixes
  -> Round 3: reviewer-risk, claim-strength, and next-stage handoff check
  -> classify remaining issues
  -> update required evidence recording track
  -> proceed only if human approves
```

## Stage issue status values

Use exactly one of these statuses for every remaining issue:

| Status | Meaning |
| --- | --- |
| Fixed | The issue was resolved and evidence was recorded. |
| Accepted limitation | The issue remains but is explicitly disclosed as a limitation. |
| Human-approved tradeoff | The issue remains because the human chose a tradeoff after seeing pros and cons. |
| Blocked | The stage cannot proceed without missing data, permissions, or a human decision. |
| Future work | The issue is outside the paper's current scope and is recorded for transparency. |

## Required records

- `stage_quality_cycle_tracker.csv` records stage-level progress.
- `stage_issue_register.csv` records every issue found in stage checks.
- `stage_round_template.md` gives agents a copy-ready review format.
