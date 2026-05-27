# Agent Rules

All agents using PaperPilot must follow this behavior contract.

## Default mode

Start in **Plan Mode**.

In Plan Mode the agent may:

- read safe project files;
- summarize existing memory and context;
- ask missing questions;
- propose options;
- create decision packets.

In Plan Mode the agent must not:

- edit files;
- inspect private, licensed, restricted, or confidential raw data;
- run irreversible commands;
- move to the next stage without a human decision.

## Memory-first rule

Before asking the researcher for information, check:

```text
03_Record_Required_Evidence/PROJECT_MEMORY.yml
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/00_Project_Dashboard/PROJECT_DASHBOARD.md
03_Record_Required_Evidence/02_Human_Decisions/
03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/
```

If a stable fact is already recorded, reuse it. If the researcher changes it, update memory and log the change.

## Decision-packet rule

For every major choice, produce:

```text
options
pros and cons
risks
evidence needed
recommended path
files/records to update after approval
```

Wait for human approval before Action Mode.

## Stage-quality rule

Every stage must pass:

```text
Round 1: consistency and missing-input check
Round 2: evidence, data, method, and feasibility check
Round 3: reviewer-risk and next-stage readiness check
```

## Parallel evidence rule

At each stage, update the required evidence track:

```text
AI conversations
human decisions
human time/contribution
data access records
claim/evidence records
stage quality records
parallel documentation tracker
novelty records when relevant
journal-quality score when relevant
```

## Data-safety rule

Never request or inspect raw licensed, restricted, confidential, proprietary, identifiable, referee, or private coauthor material unless explicit permission exists.

Use metadata, toy data, synthetic examples, codebooks, and approved secure environments first.

## Novelty rule

Deviation from the mainstream is not a flaw by itself. Unsupported deviation is a flaw.

If an idea is novel or unusual, preserve the angle and evaluate whether it is justified, testable, and bounded.

## Quality-score rule

Use the quality score to avoid wasting human effort:

```text
idea potential <= 70: normally recommend stop, pivot, or merge
idea potential 95-100: chase if feasible
final paper >= 95 and no hard-stop issue: revision may stop
```

## Agent behavior tests

Use this file when behavior is uncertain:

```text
04_Check_And_Finalize_Paper/Agent_Behavior_Test.md
```


## Multi-agent collaboration rule

If the user wants multiple agent roles, use `05_Coordinate_Multiple_Agents/` as the task-control layer. Before starting a task, check `Agent_Task_Board.csv`, choose the current research role, state missing inputs, and remain in Plan Mode. After the approved action, update `Agent_Status_Log.csv`; if blocked, update `Agent_Blockers_Log.csv`. If the task creates a reusable rule, add it to `Reusable_Lessons_Log.csv`.
