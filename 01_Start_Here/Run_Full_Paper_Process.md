# Run Full Paper Process

Use this file when you want Codex or Claude Code to guide the whole paper from idea to final draft and required evidence.

## What the full run does

```text
Idea
↓
Question and story
↓
Literature and novelty position
↓
Data and permissions
↓
Design and method
↓
Analysis and outputs
↓
Findings and claims
↓
Writing and revision
↓
Whole-paper review
↓
Final paper and evidence package
```

Each stage must pass three checks before moving on. The final paper also receives three whole-paper improvement passes unless the human stops earlier.

## First prompt for a full paper run

Paste this into Codex or Claude Code:

```text
Use PaperPilot for a Full Paper Run.

Start in Plan Mode.
Read README.md, 01_Start_Here/Run_Full_Paper_Process.md, 02_Build_The_Paper/PAPER_CONTEXT.md, and 03_Record_Required_Evidence/PROJECT_MEMORY.yml.

Before asking anything, summarize what is already known.
Ask only for missing facts needed for the first stage.

Begin with idea screening.
For each stage, use this loop:
1. produce stage output or options;
2. run Round 1: consistency and missing-input check;
3. improve if needed;
4. run Round 2: evidence, data, method, and feasibility check;
5. improve if needed;
6. run Round 3: reviewer-risk and next-stage readiness check;
7. classify remaining issues;
8. update memory and required evidence;
9. ask me whether to continue.

Do not skip the parallel required-evidence records.
Do not force a novel idea back to mainstream literature if the deviation is well justified.
Use the quality score to stop weak ideas early and keep improving strong drafts.
```

## Full-run stage table

| Stage | Human input | Agent output | Stop/check rule |
| --- | --- | --- | --- |
| Idea | rough idea, field, target | current score and potential ceiling | give up/pivot if ceiling is about 70 or below |
| Question | preferred path or constraints | question/story decision packet | must be important, novel, feasible |
| Literature | seed papers/keywords or unknown | source map and gap/deviation choices | no invented citations |
| Novelty | what differs from mainstream | mainstream-deviation justification | deviation must be testable and bounded |
| Data | data source and access status | safety classification and plan | no unsafe data exposure |
| Design | method candidates or setting | design options and assumptions | assumptions must be defensible |
| Analysis | software, variables, outputs | code/table/figure plan | code, tables, and prose must match |
| Findings | results or result summaries | interpretation and limitations | no overclaiming |
| Writing | approved facts and outline | full paper draft | internal consistency required |
| Final review | full draft and records | quality score and final issues | stop only if score >= 95 and no hard-stop issue |

## Required evidence updated in parallel

At each stage, the agent should update:

```text
AI conversations
human decisions
human time/contribution
data access records
claims and evidence
stage quality records
parallel documentation tracker
novelty records
journal-quality score when relevant
```
