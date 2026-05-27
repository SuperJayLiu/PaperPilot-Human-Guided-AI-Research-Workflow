# Skill 03: Data Access and Onboarding

## Purpose

Classify data access, protect restricted material, and create a safe data plan before any analysis.

## When to use this skill

Use this before adding data, designing merge code, using WRDS/CRSP/Compustat/Bloomberg/FactSet/LSEG/TRACE, or deciding what the AI may inspect.

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

1. Identify each data source and provider.
2. Classify as public, licensed, restricted, confidential, or unknown.
3. Decide what AI may inspect: public URLs, metadata, schemas, toy rows, or code only.
4. Create a data source card and data inventory row.
5. Propose a safe folder location and analysis path.
6. Update memory and data access records.

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

- Uploading raw licensed or restricted data to public AI.
- Treating public-use data as upload-anywhere data.
- Failing to record version, vintage, access date, or provider terms.
- Writing merge code before defining identifiers and timing rules.

## Verification checklist

- Data source is classified.
- AI permissions are explicit.
- Forbidden inputs are listed.
- Metadata/toy-data alternative exists.
- Data version, date, and citation are recorded.

## Outputs and records to update

`03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/`, `02_Build_The_Paper/02_Data_And_Code/metadata/`, `02_Build_The_Paper/02_Data_And_Code/toy_data/`, `03_Record_Required_Evidence/PROJECT_MEMORY.yml`

## Data safety rule

Default to metadata, schemas, toy rows, synthetic examples, and approved secure environments. Raw licensed or restricted extracts require explicit permission.


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
Use Skill 03: Data Access and Onboarding. Start in Plan Mode. Check project memory first. Ask only missing questions. Produce a decision packet before any Action Mode work. End with verification checklist and memory updates.
```
