# Use Codex

Use this file if you run PaperPilot with OpenAI Codex.

## First Codex prompt

Paste this into Codex:

```text
Use this repository as PaperPilot for one AI-assisted economics or finance research paper.

Start in Plan Mode.

Before asking me questions, read:
- README.md
- 01_Start_Here/README.md
- 01_Start_Here/Use_Codex.md
- 02_Build_The_Paper/PAPER_CONTEXT.md
- 03_Record_Required_Evidence/PROJECT_MEMORY.yml
- 03_Record_Required_Evidence/00_Project_Dashboard/PROJECT_DASHBOARD.md

If I ask for the end-to-end process, also read:
- 01_Start_Here/Run_Full_Paper_Process.md

First summarize what is already known from memory and context.
Then ask only the missing questions needed for the next stage.
Do not edit files yet.

For every major choice, create a decision packet with:
- options;
- pros and cons;
- risks;
- evidence needed;
- your recommendation;
- what will be updated if I approve.

Wait for my approval before switching to Action Mode.
After approved action, update memory and required evidence so I do not need to repeat stable facts.
```

## Codex behavior contract

Codex should pass these checks.

| Behavior | Required action |
| --- | --- |
| Plan Mode first | propose before editing |
| Memory first | read memory/context before asking |
| Minimal questions | ask only missing questions |
| Decision packets | give options, pros/cons, risks, evidence needed |
| Human approval | edit only after approval |
| Data safety | do not inspect private, licensed, or restricted raw data by default |
| Stage checks | run three checks before stage completion |
| AFA-style evidence | update conversations, decisions, data access, claims, contribution, and quality records |
| Novelty | preserve justified deviations from mainstream literature |
| Quality score | apply idea and final-paper scoring rules |

## Test Codex

After the first Codex response, open:

```text
04_Check_And_Finalize_Paper/Agent_Behavior_Test.md
```

If Codex asks for facts already in memory, edits before approval, or skips records, paste the corrective prompt from that file.


## Multi-agent collaboration rule

If the user wants multiple agent roles, use `05_Coordinate_Multiple_Agents/` as the task-control layer. Before starting a task, check `Agent_Task_Board.csv`, choose the current research role, state missing inputs, and remain in Plan Mode. After the approved action, update `Agent_Status_Log.csv`; if blocked, update `Agent_Blockers_Log.csv`. If the task creates a reusable rule, add it to `Reusable_Lessons_Log.csv`.
