# 03 Record Required Evidence

Use this folder to keep the documentation that supports AI-use disclosure and reproducibility.

The goal is simple: **records should be created while the paper is built**, not reconstructed at the end.

## Main records

| Folder or file | What it records |
| --- | --- |
| `00_Project_Dashboard/` | Current stage, next action, and readiness status. |
| `01_AI_Conversations/` | Initial prompt and full AI transcripts or transcript summaries. |
| `02_Human_Decisions/` | Decision packets, pros/cons, selected options, and human rationale. |
| `03_Record_Human_Time_And_Contributions/` | Human time, direct human work, and AI/human contribution estimates. |
| `04_Record_Data_Access_And_Permissions/` | Dataset sources, permissions, access dates, and AI-use boundaries. |
| `05_Record_Claims_Evidence_And_Risks/` | Paper claims, evidence, robustness, limitations, and risks. |
| `06_Submission_Package/` | AFA-style submission checklist and disclosure package. |
| `07_Full_Paper_Quality_Cycles/` | Whole-paper review and revision cycles. |
| `08_Stage_Quality_Cycles/` | Three-round checks for each stage. |
| `09_Parallel_AFA_Documentation/` | Evidence tracker that updates at every stage. |
| `10_Novelty_And_Mainstream_Deviations/` | Non-mainstream ideas, justification, falsification logic, and referee objections. |
| `11_Journal_Quality_Score/` | Journal-style quality score and stop/revise decisions. |
| `PROJECT_MEMORY.yml` | Stable facts the agent should remember. |
| `MEMORY_CHECKLIST.md` | Checklist for the say-it-once rule. |

## Important rule

If the user has already answered a stable question, record it in `PROJECT_MEMORY.yml` and reuse it. Do not ask again unless the answer is missing, unclear, or changed.
