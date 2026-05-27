# Skill 14: Journal-Quality Scoring Agent

## Purpose

Score ideas, stage outputs, and full paper drafts against a demanding top-finance-journal style benchmark so the agent can decide whether to chase, refine, pivot, give up, continue revision, or stop revision.

Use this skill to score a research idea, a stage output, or a full paper against a demanding top-finance-journal style benchmark. The reference point is **Journal of Finance-level research quality**, but this is an internal heuristic, not an official Journal of Finance score and not an acceptance prediction.

## When to use this skill

Use this skill whenever the user asks whether an idea is worth chasing, whether the paper is good enough, whether revision can stop, or whether the project has top-journal potential. Also use it automatically:

1. at the research-question stage before major effort is spent;
2. after novelty/mainstream-deviation review;
3. after the first full draft;
4. after each whole-paper revision cycle;
5. before the final submission package is marked ready.

If the user says “score the paper,” “compare with Journal of Finance papers,” “is this idea good enough,” “can we stop revision,” “should we give up,” or “is the potential 95,” reach for this skill.

## Read before asking

Before asking the user for information, read:

```text
03_Record_Required_Evidence/PROJECT_MEMORY.yml
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/02_Human_Decisions/
03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/
03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/
03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/
03_Record_Required_Evidence/11_Journal_Quality_Score/
```

Do not ask for facts already recorded. If a recorded fact looks stale or inconsistent, state what you found and ask whether to update memory.

## Core idea

A project can continue only when its potential justifies more human effort. The agent must protect two kinds of human time:

1. avoid spending months on an idea whose realistic ceiling is about 70/100;
2. avoid endless polishing once the final paper is around 95/100 and all remaining issues are acceptable.

## Ten scoring perspectives

Score each perspective from 0 to 10. The total is 100.

1. **Big question and economic importance**: Is the question important enough for a top finance audience?
2. **Novel contribution and originality**: Is the contribution real, not just a small extension or a renamed result?
3. **Literature positioning**: Does the paper know the frontier and state exactly what it adds?
4. **Theory, mechanism, or conceptual clarity**: Is the mechanism coherent and economically meaningful?
5. **Data quality and construction transparency**: Are the data appropriate, correctly handled, and documented?
6. **Identification or empirical-design credibility**: Is the causal or predictive design credible for the claim?
7. **Execution, reproducibility, and robustness**: Can the main result be reproduced and stress-tested?
8. **Result strength and economic magnitude**: Are the findings meaningful, not only statistically convenient?
9. **Claim discipline, limitations, and referee risk**: Are claims bounded and likely objections addressed?
10. **Writing, tables, figures, and whole-paper coherence**: Does the paper read as one coherent object?

## Idea-stage scoring

At the idea stage, give two scores:

```text
current_score = how strong the idea is now
potential_ceiling = how strong the idea could become if executed very well
```

Decision thresholds:

| Potential ceiling | Action |
| --- | --- |
| 95-100 | Chase. Make it a priority if data and design are feasible. |
| 85-94 | Promising. Refine before committing major effort. |
| 71-84 | Borderline. Continue only with a special reason or human override. |
| 70 or below | Give up, pivot, or merge into another project. |

The agent must explicitly say when an idea should be abandoned because its maximum plausible score is only about 70. It should not waste human effort by repeatedly polishing a low-ceiling idea.

## Final-paper scoring

At final-paper stage, give:

```text
current_score = present quality of the paper
remaining_upside = points that could realistically be gained
stop_revision_recommendation = yes/no
```

Revision can stop only if:

1. current score is 95/100 or above;
2. no hard-stop issue remains;
3. remaining issues are documented limitations, future work, not applicable, or accepted human-author judgment;
4. parallel required evidence recording records are complete enough for the project stage.

## Hard-stop issues

A hard-stop issue overrides a high score. Mark the paper not ready if any of these remain:

- data permission or confidentiality boundary unresolved;
- main result unreproducible;
- invented, unverified, or misrepresented citations;
- unsupported causal claim;
- core table, code, and prose inconsistency;
- novelty claim not positioned against literature;
- key robustness or falsification test missing without explanation;
- AI-use, human-time, model-configuration, data-access, or contribution-share records missing.


## Required inputs to check first

- Stage being scored: idea, stage output, full draft, revision round, or final paper.
- Current paper context and project memory.
- Main evidence files: literature map, data plan, method/design record, analysis outputs, claim registry, manuscript draft.
- Known limitations, unresolved issues, and human-approved tradeoffs.

## Workflow

### Step 1. Identify scoring context

Classify the scoring task as:

```text
idea screening / stage output / full draft / revision round / final readiness
```

### Step 2. Build a score table

Return a table with:

```text
perspective | score | evidence | weakness | required improvement | hard-stop flag
```

For idea screening, include both current score and potential ceiling for every perspective.

### Step 3. Make a decision recommendation

For idea stage, recommend one of:

```text
chase / refine / pivot / give up / human override needed
```

For final paper, recommend one of:

```text
stop revision / targeted revision / major revision / redesign / not ready
```

### Step 4. Turn score gaps into revision tasks

Do not only score. Convert the weakest dimensions into specific tasks:

```text
what to fix -> file to edit -> evidence needed -> expected score gain -> human decision needed
```

### Step 5. Update records

Update:

```text
03_Record_Required_Evidence/11_Journal_Quality_Score/idea_quality_scorecard.csv
03_Record_Required_Evidence/11_Journal_Quality_Score/final_paper_quality_scorecard.csv
03_Record_Required_Evidence/11_Journal_Quality_Score/quality_scoring_rounds.csv
03_Record_Required_Evidence/PROJECT_MEMORY.yml
03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv
```

## Decision packet requirements

When this skill produces a decision packet, it must include:

1. the scoring context: idea screening, stage output, full draft, revision round, or final readiness;
2. the ten-perspective score table;
3. current score and, for idea-stage scoring, potential ceiling;
4. hard-stop issues that override the score;
5. a recommendation: chase, refine, pivot, give up, targeted revision, major revision, redesign, or stop revision;
6. the expected score gain from each proposed improvement;
7. the records that will be updated if the human approves.

The human must approve the scoring recommendation before the agent abandons an idea, pivots the paper, or stops revision.

## Common failure modes

- **False precision**: scoring 93.7 vs 94.1 as if the number were objective. Use the score to guide decisions, not to pretend certainty.
- **Generic top-journal language**: saying “needs novelty” without identifying the exact missing contribution.
- **Over-conformity**: penalizing a non-mainstream idea merely because it deviates from the literature. Use Skill 13 before downgrading originality.
- **Ignoring feasibility**: giving a 95 potential score to an idea with no data path or no credible design.
- **Polishing forever**: continuing revision after 95+ with no hard-stop issues.
- **Premature stop**: stopping at 95+ while citations, data access, or AI-use reporting are incomplete.

## Verification checklist

Before finalizing the score, verify:

- [ ] memory and prior decisions were checked;
- [ ] the score table uses all ten perspectives;
- [ ] the idea-stage score includes potential ceiling;
- [ ] the final-paper score checks hard-stop issues;
- [ ] weakest perspectives are converted into concrete revision tasks;
- [ ] the recommendation says chase, refine, pivot, give up, continue revision, or stop revision;
- [ ] records in `03_Record_Required_Evidence/11_Journal_Quality_Score/` are updated;
- [ ] parallel required evidence recording is updated.

## Outputs and records to update

After running this skill, update:

```text
03_Record_Required_Evidence/11_Journal_Quality_Score/idea_quality_scorecard.csv
03_Record_Required_Evidence/11_Journal_Quality_Score/final_paper_quality_scorecard.csv
03_Record_Required_Evidence/11_Journal_Quality_Score/quality_scoring_rounds.csv
03_Record_Required_Evidence/PROJECT_MEMORY.yml
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv
```

If this score affects project direction, also create or update a human decision packet in `03_Record_Required_Evidence/02_Human_Decisions/`.

## Copy-ready command

```text
Use Skill 14: Journal-Quality Scoring Agent.
First read project memory, paper context, decision logs, claim registry, full-paper review records, novelty records, and prior scorecards.
Score this project against the ten Journal of Finance-style perspectives.
If this is the idea stage, give current score and potential ceiling, and say whether to chase, refine, pivot, or give up.
If this is the final paper, give the current score, hard-stop issues, required improvements, and whether revision can stop at 95/100 or above.
Update the quality-score records and the parallel required evidence recording tracker.
```


## Mandatory stage-quality and parallel-reporting requirement

When Skill 14 is used as part of a stage output, follow it with the stage-quality and parallel-reporting requirements: run Skill 11 for Round 1, Round 2, and Round 3 checks if the score changes the stage output, and run Skill 12 to update the parallel required evidence recording tracker.
