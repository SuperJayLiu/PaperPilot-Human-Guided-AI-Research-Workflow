---
name: paperpilot-research-workflow
description: Use when a researcher wants to apply, summarize, or onboard to PaperPilot, a human-guided AI workflow for building one serious economics or finance paper from idea screening through final manuscript and required evidence records. Trigger for full-paper research workflows, research question refinement, literature positioning, data permission planning, empirical design, analysis outputs, claims discipline, writing revision, reviewer stress tests, AFA-style documentation, multi-agent research coordination, or journal-quality scoring.
---

# PaperPilot Research Workflow

## Purpose

PaperPilot is a human-guided AI workflow for developing one economics or finance paper from first idea to final manuscript and evidence package. The agent does repeatable research support work; the human remains responsible for scarce, high-value decisions: question, novelty, data permissions, design, interpretation, claim strength, disclosure, and final sign-off.

Use this skill to:

- onboard a user to PaperPilot;
- summarize the workflow and required records;
- run a stage or full-paper process inside a PaperPilot repository;
- adapt the workflow to a new research project;
- diagnose what stage a project is in and what should happen next.

## Start Here

If working inside a cloned PaperPilot repository, read these before asking the user questions:

```text
README.md
01_Start_Here/README.md
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/PROJECT_MEMORY.yml
03_Record_Required_Evidence/00_Project_Dashboard/PROJECT_DASHBOARD.md
```

If the user asks for an end-to-end run, also read:

```text
01_Start_Here/Run_Full_Paper_Process.md
99_System_Do_Not_Touch/01_Agent_Rules/MASTER_WORKFLOW.md
99_System_Do_Not_Touch/02_Skills/SKILL.md
99_System_Do_Not_Touch/02_Skills/00_full_paper_run_SKILL.md
```

If those files are unavailable, apply the workflow from this skill and clearly state which repository records could not be checked.

## Core Contract

Follow this loop for every substantive stage:

1. Start in Plan Mode.
2. Check memory and paper context before asking.
3. Ask only for missing, stale, or contradictory facts.
4. Produce options with pros, cons, risks, evidence needed, and a recommendation.
5. Wait for human approval before editing files or executing the chosen path.
6. Run three checks before marking a stage complete.
7. Update memory, decisions, claims, data access, contribution, and stage records in parallel.

Do not ask the user to repeat stable facts already stored in memory. If a stored fact may be outdated, quote the stored fact briefly and ask whether it is still correct.

## Stage Map

Use this stage order unless the user asks to start from the current project state:

| Stage | Agent output | Human decision |
| --- | --- | --- |
| Idea screening | idea score, potential ceiling, stop/refine/chase recommendation | whether the idea deserves time |
| Question and story | 2 to 4 question/story paths | which path fits taste and constraints |
| Literature and novelty | source-grounded map, positioning choices, mainstream-deviation risks | whether the contribution is credible |
| Data and permissions | data classification, allowed AI access, onboarding plan | what data the agent may inspect |
| Design and method | design options, assumptions, threats, diagnostics | which design is defensible |
| Analysis and outputs | run plan, code/output inventory, reproducibility checks | which outputs to build |
| Findings and claims | claim registry entries, interpretation, limitations | how strong claims may be |
| Writing and revision | outline, draft, revision plan, consistency checks | final voice and claims |
| Whole-paper review | issue register, reviewer risks, quality score | what to fix, disclose, or accept |
| Final package | readiness checklist and evidence package status | final responsibility and disclosure |

## Three Checks

After each stage output or revision, run:

1. **Consistency and missing-input check**: contradictions, undefined concepts, reopened rejected paths, missing decisions.
2. **Evidence, data, method, and feasibility check**: source support, data permissions, feasible design, realistic tools, required next-stage evidence.
3. **Reviewer-risk and handoff check**: likely objections, claim strength, limitations, next-stage readiness.

A stage is complete only when remaining issues are classified as fixed, accepted limitation, human-approved tradeoff, future work, not applicable, or blocked with a documented reason.

## Decision Packets

Every major choice must include:

- decision needed;
- 2 to 4 options;
- pros and cons;
- risks;
- evidence needed;
- agent recommendation;
- human choice placeholder;
- exact files or records to update if approved.

## Data Safety

Default to metadata, schemas, codebooks, toy rows, synthetic data, public URLs, and approved secure environments. Do not inspect, upload, summarize, or transform licensed, restricted, confidential, proprietary, identifiable, referee, private coauthor, or otherwise sensitive raw data unless the user confirms permission and the environment is appropriate.

When data status is unclear, classify it first and defer analysis.

## Novelty Guardrail

Do not flatten every unusual idea into a safe mainstream extension. For non-mainstream claims, separate:

```text
unsupported deviation -> reject or soften
testable non-mainstream idea -> preserve, test, bound, and document
```

State the mainstream benchmark, the proposed deviation, why it may be valuable, why it may be wrong, and what evidence would persuade a skeptical referee.

## Quality Scoring

Use the 10-perspective journal-quality score when screening an idea, reviewing a full draft, or deciding whether revision can stop:

1. big question;
2. novelty;
3. literature positioning;
4. mechanism or conceptual clarity;
5. data quality;
6. design credibility;
7. execution and reproducibility;
8. result strength and magnitude;
9. claim discipline and referee risk;
10. writing and whole-paper coherence.

At the idea stage, distinguish current score from potential ceiling. Ideas with a plausible ceiling around 70/100 should usually be stopped, pivoted, or merged. Final paper revision should stop only when the score is at least 95/100 and no hard-stop issue remains, unless the human explicitly accepts the tradeoff.

## Multi-Agent Mode

If the user asks for multiple agent roles, use `05_Coordinate_Multiple_Agents/` when available. Check the task board, choose the active role, state missing inputs, remain in Plan Mode until approval, then update status, blockers, and reusable lessons after the approved action.

## Common Commands

For a first run:

```text
Use $paperpilot-research-workflow to start PaperPilot for this economics or finance paper. Read memory first, summarize what is known, ask only missing questions, and begin in Plan Mode.
```

For a full run:

```text
Use $paperpilot-research-workflow for a full paper run from the current stage to final manuscript and evidence package. Use decision packets, three stage checks, parallel evidence records, novelty guardrails, and journal-quality scoring.
```

For a summary:

```text
Use $paperpilot-research-workflow to summarize this repository for a new researcher and explain how to start safely.
```
