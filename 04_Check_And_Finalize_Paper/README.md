# 04 Check And Finalize Paper

Use this folder to verify whether the workflow, agents, stage outputs, and final paper are ready.

## What to open

| Need | Open |
| --- | --- |
| Check whether Codex/Claude is behaving correctly | `Agent_Behavior_Test.md` |
| Check whether you are ready to start a real project | `Researcher_Readiness_Check.md` |
| Review full paper status | use the quality cycles and score records in `03_Record_Required_Evidence/` |

## What gets checked

1. **Agent behavior:** the agent starts in Plan Mode, reads memory first, asks only missing questions, waits before editing, and updates records.
2. **Stage quality:** every stage passes three rounds of checks before moving on.
3. **Whole-paper consistency:** question, literature, data, methods, results, claims, tables, and writing agree.
4. **Novelty:** unusual ideas are preserved when well justified, not automatically pushed back to mainstream wording.
5. **Journal-style quality:** the paper is scored across 10 quality dimensions.
6. **Submission readiness:** AI-use records, human logs, data access, model configuration, contribution records, and unresolved issues are complete.

## Stop rule

Revision can stop only when remaining issues are one of these:

```text
fixed
accepted limitation
human-approved tradeoff
future work
blocked with documented reason
```

For the final paper, the target is:

```text
journal-quality score >= 95
and no hard-stop issue remains
and required evidence package is complete enough for the intended use
```
