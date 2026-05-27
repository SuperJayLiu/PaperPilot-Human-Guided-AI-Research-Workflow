# Skill 05: Analysis, Code, Tables, and Figures

## Purpose

Turn the approved data and design plan into reproducible code, tables, figures, and output checks.

## When to use this skill

Use this when choosing Stata/R/Python, writing scripts, generating tables/figures, debugging code, or preparing reproducible output folders.

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

1. Read data permissions and empirical design.
2. Ask for preferred tool only if missing from memory.
3. Draft a run plan: input files, scripts, outputs, checks.
4. Create toy-data tests before real-data execution.
5. Generate code only for approved files.
6. Record output provenance: script, data source, sample, date, limitations.

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

- Running code on real data before testing toy data.
- Manually copying console values into paper tables.
- Letting labels overstate results.
- Ignoring intermediate merge checks, duplicates, sample counts, or missingness.

## Verification checklist

- Raw data not overwritten.
- Toy test exists for key logic.
- Each output has script and data source.
- Tables/figures include sample, variables, date, and limitations.
- Results are reproducible from run order.

## Outputs and records to update

`02_Build_The_Paper/02_Data_And_Code/code/`, `02_Build_The_Paper/03_Build_Results_And_Manuscript/results/`, `03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/claim_registry.csv`




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
Use Skill 05: Analysis, Code, Tables, and Figures. Start in Plan Mode. Check project memory first. Ask only missing questions. Produce a decision packet before any Action Mode work. End with verification checklist and memory updates.
```
