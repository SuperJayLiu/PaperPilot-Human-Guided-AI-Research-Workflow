# Use Claude Code

Use this file if you run PaperPilot with Claude Code in a local terminal.

## First Claude Code prompt

From the repo folder, start Claude Code and paste:

```text
Use this repository as PaperPilot for one AI-assisted economics or finance research paper.

Start in Plan Mode.

Before asking me questions, read:
- README.md
- 01_Start_Here/README.md
- 01_Start_Here/Use_Claude_Code.md
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

## Claude Code behavior contract

Claude Code has local file access, so the safety bar is higher.

| Behavior | Required action |
| --- | --- |
| Plan Mode first | explain the plan before edits |
| Memory first | read memory/context before asking |
| Minimal questions | ask only missing questions |
| Human approval | do not rewrite files until the user approves |
| Safe filesystem use | do not inspect private, licensed, or restricted raw data unless explicitly approved |
| Small changes | change only files named in the approved plan |
| Stage checks | run three checks before stage completion |
| Required evidence | update records after each approved stage |
| Local checks | run the repository checks before saying a stage is complete |
| Novelty and quality | preserve justified novelty and apply the quality score rules |

## Test Claude Code

After the first Claude response, open:

```text
04_Check_And_Finalize_Paper/Agent_Behavior_Test.md
```

If Claude asks for repeated facts, edits too early, or ignores data safety, paste the corrective prompt from that file.


## Multi-agent collaboration rule

If the user wants multiple agent roles, use `05_Coordinate_Multiple_Agents/` as the task-control layer. Before starting a task, check `Agent_Task_Board.csv`, choose the current research role, state missing inputs, and remain in Plan Mode. After the approved action, update `Agent_Status_Log.csv`; if blocked, update `Agent_Blockers_Log.csv`. If the task creates a reusable rule, add it to `Reusable_Lessons_Log.csv`.
