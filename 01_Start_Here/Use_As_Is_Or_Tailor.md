# Use PaperPilot As-Is or Tailor It

PaperPilot supports two common use cases.

## Option A: Use directly

Use this when you want to start quickly.

```bash
git clone https://github.com/SuperJayLiu/PaperPilot-Human-Guided-AI-Research-Workflow.git
cd PaperPilot-Human-Guided-AI-Research-Workflow
```

Then choose:

```text
01_Start_Here/Use_Codex.md
```

or:

```text
01_Start_Here/Use_Claude_Code.md
```

Paste the first prompt into your agent. The agent should start in Plan Mode, read memory first, and create a decision packet before editing anything.

## Option B: Download and tailor

Use this when you want a copy for one paper, one lab, one class, or one coauthor team.

1. On GitHub, click **Code → Download ZIP**.
2. Unzip the folder.
3. Rename the folder to your paper/project name.
4. Edit these user-facing files first:

```text
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/PROJECT_MEMORY.yml
03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/data_access.md
```

5. Then run Codex or Claude Code using the relevant mode file.

## Should I edit the skill files?

Not at the beginning.

The detailed skill files already exist so the agent knows how to handle stages like research question, literature, data, empirical design, writing, stage quality checks, novelty, and journal-quality scoring.

Only tailor the skills after you know:

```text
paper field or subfield
data type
method family
software plan
journal/conference target
coauthor or institution rules
```

When tailoring, ask the agent to preserve the structure of each skill:

```text
purpose
when to use
required inputs
workflow
decision packet
failure modes
verification checklist
records to update
copy-ready command
```

## How to create a clean project copy

If you want a private working repo for one paper:

```bash
git clone https://github.com/SuperJayLiu/PaperPilot-Human-Guided-AI-Research-Workflow.git My-PaperPilot-Project
cd My-PaperPilot-Project
rm -rf .git
git init
git branch -M main
git add .
git commit -m "init: start PaperPilot project for one paper"
```

Then connect the private repo to GitHub if desired.

## Important

If you update an existing GitHub repo and old folders remain visible, you did not replace the tracked files. Use a clean force push from a fresh folder, or remove old tracked folders with `git rm -r` before committing.
