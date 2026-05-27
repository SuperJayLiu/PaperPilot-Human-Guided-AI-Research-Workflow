# Skill 09: AFA-Style Documentation and Disclosure Pack

## Purpose

Prepare a documentation package that records initial prompt, full AI conversations, human time, data access, model configuration, workflow decisions, and contribution shares.

## When to use this skill

Use this throughout the project and especially before submission or public release.

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

1. Check that the initial prompt and conversations are saved.
2. Check human time and direct contributions.
3. Check model configuration and tool settings.
4. Check data access records and AI-use boundaries.
5. Generate a disclosure summary and missing-items list.
6. Ask the human to confirm accuracy.

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

- Treating logs as an afterthought.
- Summarizing conversations without preserving full prompts/responses.
- Forgetting human direct contributions outside prompts.
- Overstating the precision of AI-vs-human line shares.

## Verification checklist

- Initial prompt exists.
- Conversation files are complete.
- Human time log is current.
- Data and model configuration are documented.
- Contribution report states assumptions and limitations.

## Outputs and records to update

`03_Record_Required_Evidence/06_Submission_Package/`, `03_Record_Required_Evidence/01_AI_Conversations/`, `03_Record_Required_Evidence/03_Record_Human_Time_And_Contributions/`, `03_Record_Required_Evidence/model_config.yml`




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
Use Skill 09: AFA-Style Documentation and Disclosure Pack. Start in Plan Mode. Check project memory first. Ask only missing questions. Produce a decision packet before any Action Mode work. End with verification checklist and memory updates.
```
