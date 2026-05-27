# Skill 10: Slides and Presentations

## Purpose

Create or revise seminar slides, especially Beamer decks, while keeping reveals, compile workflow, figures, and speaker narrative consistent with the paper.

## When to use this skill

Use this for slides, seminar decks, presentation scripts, Beamer overlay issues, or propagating a paper change into slides.

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

1. Read the paper context and claim registry.
2. Decide talk audience and time.
3. Build a slide outline before drafting.
4. For Beamer, use reliable overlay patterns, compile twice, and inspect output.
5. Keep slides, paper, and speaker script consistent.

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

- Broken overlay order.
- Always-on trailing notes that should reveal later.
- Overfull slides.
- Slide claims that exceed the paper evidence.
- Paper/slides/script terminology drifting apart.

## Verification checklist

- Slides compile cleanly if using LaTeX.
- Reveal order is visually checked.
- Claims match claim registry.
- Speaker script follows slide order.
- No unsupported result or citation appears on slides.

## Outputs and records to update

`02_Build_The_Paper/03_Build_Results_And_Manuscript/slides/`, `02_Build_The_Paper/03_Build_Results_And_Manuscript/manuscript/`, `03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/`

## Detailed pattern

This skill follows the user-provided Beamer skill pattern: trigger conditions, compile workflow, failure modes, and a final verification checklist.


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
Use Skill 10: Slides and Presentations. Start in Plan Mode. Check project memory first. Ask only missing questions. Produce a decision packet before any Action Mode work. End with verification checklist and memory updates.
```
