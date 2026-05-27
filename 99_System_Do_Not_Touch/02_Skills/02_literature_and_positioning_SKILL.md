# Skill 02: Literature and Positioning

## Purpose

Build a source-grounded literature map and position the paper without invented citations or unsupported claims.

## When to use this skill

Use this for literature review, contribution positioning, related-work tables, citation checking, or deciding which literature path the paper should enter.

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

1. Read the chosen question and contribution from memory.
2. Ask for seed papers or approved search scope only if missing.
3. Create a literature map: paper, question, data, method, finding, relation to this project.
4. Separate verified sources from candidate sources.
5. Propose positioning options and reviewer risks.

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

- Inventing papers, results, or citations.
- Summarizing abstracts as if full papers were read.
- Claiming novelty without a comparison set.
- Forgetting to log source version, access date, and search method.

## Verification checklist

- Every cited item has a verifiable source.
- Literature claims are marked verified or needs-check.
- The contribution paragraph does not overclaim.
- Search scope and excluded areas are recorded.

## Outputs and records to update

`02_Build_The_Paper/01_Question_And_Story/`, `03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/claim_registry.csv`, `03_Record_Required_Evidence/02_Human_Decisions/`

## Source checks

Use official journal pages, working paper pages, SSRN/NBER/AEA links, and method-standard references where possible. Do not rely only on model memory.


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
Use Skill 02: Literature and Positioning. Start in Plan Mode. Check project memory first. Ask only missing questions. Produce a decision packet before any Action Mode work. End with verification checklist and memory updates.
```

## Novelty and mainstream-deviation check

If this stage touches the paper's contribution, literature position, method choice, interpretation, or writing emphasis, the agent must apply **Skill 13: Novelty and Mainstream-Deviation Guardrail** before marking the stage complete.

The agent must not erase a non-mainstream idea merely because it is unusual. It must record the mainstream benchmark, proposed deviation, evidence needed, falsification logic, and skeptical referee objections in `03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/`.
