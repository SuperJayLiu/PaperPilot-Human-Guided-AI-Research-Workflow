# Parallel AFA Reporting Track

PaperPilot must build the paper and the documentation package **in parallel**. The agent must not leave the AFA-style documentation until the end.

After every stage and every stage-quality round, update this folder plus the relevant record folders.

## What gets updated at every stage

| Reporting item | Record location |
| --- | --- |
| AI conversation transcript | `03_Record_Required_Evidence/01_AI_Conversations/` |
| Human decision packet | `03_Record_Required_Evidence/02_Human_Decisions/` |
| Human time and direct contribution | `03_Record_Required_Evidence/03_Record_Human_Time_And_Contributions/` |
| Data access and permission status | `03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/` |
| Claim, evidence, and limitation status | `03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/` |
| Submission-readiness checklist | `03_Record_Required_Evidence/06_Submission_Package/` |
| Stage quality-cycle status | `03_Record_Required_Evidence/08_Stage_Quality_Cycles/` |
| Current stable facts | `03_Record_Required_Evidence/PROJECT_MEMORY.yml` |

## Do not proceed rule

A stage is not complete until both are true:

1. the stage output has passed three quality rounds or has a human-approved residual issue;
2. the required evidence recording tracker has been updated for that stage.
