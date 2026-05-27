# Skill 01: Research Question and Story Path

## Purpose

Help the researcher turn a broad idea into a clear research question, contribution, and story path without letting the AI over-optimize for novelty claims it cannot verify.

## When to use this skill

Use this when starting a paper, revising the question, comparing possible stories, or deciding whether a question is feasible for the available data and methods.

## Read before asking


Before using this skill, the agent must read `03_Record_Required_Evidence/PROJECT_MEMORY.yml` and `02_Build_The_Paper/PAPER_CONTEXT.md`. Ask only for missing or changed information. If the user gives a stable answer, update memory after the approved action.


## Required inputs to check first

| Input | Memory location | Ask user only if missing? |
| --- | --- | --- |
| Current stage | `03_Record_Required_Evidence/PROJECT_MEMORY.yml` | Yes |
| Research question or task | `03_Record_Required_Evidence/PROJECT_MEMORY.yml` and `02_Build_The_Paper/PAPER_CONTEXT.md` | Yes |
| Data status | `03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/data_access.md` | Yes |
| Prior human choices | `03_Record_Required_Evidence/02_Human_Decisions/` | Yes |

## Workflow

1. Summarize known project facts from memory.
2. Generate or refine 3 to 5 candidate questions.
3. For each, identify contribution, data needs, identification needs, and likely reviewer concern.
4. Ask the human to choose, combine, or reject paths.
5. Save the chosen path and rejected paths in memory.

## Decision packet requirements

Every decision packet must include:

1. the choice the human must make;
2. 2 to 4 options;
3. pros, cons, risks, and evidence needed;
4. which existing memory entries were used;
5. the recommended option and why;
6. what files will be changed in Action Mode;
7. what memory will be updated.

## Common failure modes

- Inventing a contribution without checking literature.
- Treating an available dataset as a research question.
- Choosing the easiest analysis rather than the strongest question.
- Asking the user to repeat already recorded project facts.

## Verification checklist

- Question is one sentence and testable.
- Contribution is stated relative to a literature gap, not just a topic.
- Data and identification needs are explicit.
- Rejected paths are recorded so they are not repeatedly reopened.

## Outputs and records to update

`02_Build_The_Paper/01_Question_And_Story/`, `03_Record_Required_Evidence/02_Human_Decisions/`, `03_Record_Required_Evidence/PROJECT_MEMORY.yml`




## Mandatory stage-quality and parallel-reporting requirement

This skill does not complete the stage by itself. After the stage output is drafted or revised, the agent must run:

1. **Skill 11: Stage Quality Cycle** for three local rounds:
   - Round 1: internal consistency and missing-input check;
   - Round 2: evidence, data, method, and feasibility check;
   - Round 3: reviewer-risk, claim-strength, and next-stage handoff check.
2. **Skill 12: Parallel AFA Reporting** to update the stage reporting row, transcript status, human decision record, model/tool record, data-access record if relevant, contribution log, and claim/evidence records.

The agent may not mark the stage complete merely because it produced a good-looking draft. The stage is complete only when remaining issues are fixed, accepted as limitations, logged as human-approved tradeoffs, marked as future work, or blocked pending human action.

## Copy-ready command

```text
Use Skill 01: Research Question and Story Path. Start in Plan Mode. Check project memory first. Ask only missing questions. Produce a decision packet before any Action Mode work. End with verification checklist and memory updates.
```

## Novelty and mainstream-deviation check

If this stage touches the paper's contribution, literature position, method choice, interpretation, or writing emphasis, the agent must apply **Skill 13: Novelty and Mainstream-Deviation Guardrail** before marking the stage complete.

The agent must not erase a non-mainstream idea merely because it is unusual. It must record the mainstream benchmark, proposed deviation, evidence needed, falsification logic, and skeptical referee objections in `03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/`.
