# Master Workflow

This is the internal workflow that Codex or Claude Code should follow.

## Before every stage

1. Start in Plan Mode.
2. Read project memory and paper context.
3. Summarize what is already known.
4. Ask only missing questions.
5. Create a decision packet.
6. Wait for human approval.

## Stage loop

For every stage:

1. Read memory and context.
2. Summarize stable facts already known.
3. Ask only missing questions needed for this stage.
4. Produce the stage output or options.
5. Produce a decision packet with pros, cons, risks, evidence needed, and recommended path.
6. Wait for human choice.
7. Execute only the approved action.
8. Run Stage Quality Round 1: consistency and missing-input check.
9. Apply approved improvements.
10. Run Stage Quality Round 2: evidence, data, method, and feasibility check.
11. Apply approved improvements.
12. Run Stage Quality Round 3: reviewer-risk and next-stage readiness check.
13. Classify remaining issues.
14. Update memory, dashboard, decision records, AI conversation records, and parallel required evidence records.
15. Ask whether to continue to the next stage.

## Full-paper loop

After a full draft exists:

1. Check question-literature-data-method-results-claims-writing consistency.
2. Improve the whole paper once.
3. Check again.
4. Improve the whole paper a second time.
5. Check again.
6. Improve the whole paper a third time.
7. Check again.
8. Classify remaining issues as fixed, accepted limitation, human-approved tradeoff, future work, or blocked.
9. Score the paper across the 10 journal-quality dimensions.
10. Stop revision only if the score is at least 95 and no hard-stop issue remains.

## Required behavior checks

The agent must pass the behavior test in:

```text
04_Check_And_Finalize_Paper/Agent_Behavior_Test.md
```

If it fails, return to Plan Mode and correct the workflow.

## Stage order

```text
idea
question and story
literature and novelty position
data and permissions
design and method
analysis and outputs
findings and claims
writing and revision
whole-paper review
final evidence package
```

## Do not over-normalize novelty

Do not turn every unusual idea into a safe mainstream extension. If the user proposes a novel angle, evaluate whether it can be well justified, not whether it sounds familiar.


## Multi-agent collaboration rule

If the user wants multiple agent roles, use `05_Coordinate_Multiple_Agents/` as the task-control layer. Before starting a task, check `Agent_Task_Board.csv`, choose the current research role, state missing inputs, and remain in Plan Mode. After the approved action, update `Agent_Status_Log.csv`; if blocked, update `Agent_Blockers_Log.csv`. If the task creates a reusable rule, add it to `Reusable_Lessons_Log.csv`.
