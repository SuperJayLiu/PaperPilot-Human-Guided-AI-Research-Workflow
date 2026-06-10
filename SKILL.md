---
name: paperpilot-research-workflow
description: Use when a researcher wants to apply, summarize, or onboard to PaperPilot, a human-guided AI workflow for building one serious economics or finance paper from idea screening through final manuscript and required evidence records. Trigger for full-paper workflows, research question refinement, literature positioning, data permission planning, empirical design, analysis outputs, claims discipline, writing revision, reviewer stress tests, AFA-style documentation, multi-agent research coordination, journal-quality scoring, or routing to relevant AI-for-economics-and-finance research skills.
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

## Progressive Disclosure Map

Keep this root skill as the router. Load deeper context only when the task calls for it:

| Need | Read |
| --- | --- |
| repeated agent failure, odd behavior, or unclear guardrail | `references/paperpilot-gotchas.md` |
| citation, code, coefficient, data, model, text-as-data, or disclosure verification | `references/verification-playbook.md` |
| full internal PaperPilot stage library | `99_System_Do_Not_Touch/02_Skills/SKILL.md` |
| full paper orchestration | `99_System_Do_Not_Touch/02_Skills/00_full_paper_run_SKILL.md` |
| evidence record templates | `99_System_Do_Not_Touch/04_Templates/` |
| deterministic repository checks | `99_System_Do_Not_Touch/03_Check_Scripts/` |

## Intake Rule

If the user has not stated a specific task, first ask what they want to do, their field or subfield, current paper stage, what materials are safe to share, and the desired output format. Ask at most five missing questions.

For long outputs, file-producing tasks, code, slides, methods sections, literature reviews, referee responses, or agentic workflows, first return `Proposed structure and assumptions` and wait for confirmation.

## First Response Protocol

When invoked at the start of a PaperPilot session:

1. Say which PaperPilot records were read and which were unavailable.
2. Summarize stable facts already known from memory and context.
3. Identify the current stage and recommended next stage.
4. State whether any companion AI-for-Economics-and-Finance Research skill pattern is relevant, and ask whether to apply it if the user has not already approved it.
5. Ask only the missing questions needed for the next decision packet.
6. Do not edit files until the user approves a proposed action.

## Operating Modes

Ask the user to choose a mode if the scope is unclear:

| Mode | Use when | Required records |
| --- | --- | --- |
| Lite | quick idea, question, or draft guidance without a full evidence package | memory/context notes and final verification list |
| Standard | one serious paper with repeated stage checks | memory, decision packets, data access, claim/risk records, stage checks |
| AFA-ready | paper may need detailed AI-use and contribution documentation | all Standard records plus conversation, contribution, model config, parallel AFA tracker, final package |

Default to Standard for serious paper work unless the user asks for Lite or AFA-ready.

## Task Router

Map common user requests to the smallest useful workflow:

| User says | Route to |
| --- | --- |
| "I have an idea" or "is this worth it?" | idea screening, journal-quality scoring, companion topic-to-tension pattern |
| "help me frame the question" | question/story path, "so what?" test, two-mechanism competition |
| "position this in the literature" | literature map, closest-paper table, fake novelty risk check |
| "can I use this data?" | data access classification before analysis |
| "what method should I use?" | empirical design decision packet and identification pre-mortem |
| "write code" or "build tables" | analysis/output plan, toy-data verification, data pipeline checks |
| "interpret these results" | findings/claims stage, coefficient/magnitude verification, claim registry |
| "revise this section" | writing/revision stage, claim-to-evidence check before prose polishing |
| "review the whole paper" | whole-paper review cycle, reviewer stress test, journal-quality scoring |
| "prepare disclosure" | AFA documentation and AI-use reproducibility packet |

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

End substantial outputs with:

- what was produced;
- what was not changed;
- what the human must verify;
- questions for the user, if any.

## Stop Conditions

Pause and ask for human direction when any of these occur:

- data status is private, licensed, restricted, confidential, identifiable, referee-related, coauthor-private, or unknown;
- the user asks the agent to edit files before approving a plan;
- a citation, literature claim, data fact, coefficient, equation, or method claim cannot be verified from supplied or accessible evidence;
- the proposed empirical design cannot support the requested causal or economic claim;
- code would touch raw, private, licensed, or restricted data without explicit permission;
- an LLM-generated variable lacks a prompt/model/archive/validation plan;
- a final-ready claim is requested while unresolved hard-stop issues remain.

## Gotchas

If the agent is about to proceed after a smooth answer, first check for common PaperPilot failures:

- asking again for facts already in memory;
- producing polished prose before checking claim support;
- inventing or over-broadening citation claims;
- treating data availability as a research question;
- treating fixed effects, controls, or backtests as identification;
- ignoring timing, leakage, delisting, survivorship, or prompt/model drift;
- marking a stage complete before the three checks and evidence updates.

For the full gotcha list and the expected correction, read `references/paperpilot-gotchas.md`.

## Companion Skill Routing

PaperPilot can learn from and apply relevant task skills from:

```text
https://github.com/SuperJayLiu/AI-for-Economics-and-Finance-Research
```

Treat that repository as read-only source material. Do not modify or push to it while working on PaperPilot.

When a task matches one of the companion skills below, ask the user whether to apply the relevant AI-for-Economics-and-Finance Research skill before proceeding, unless the user already asked for it explicitly. Name the specific skill or page you intend to use, then apply only the relevant part.

| PaperPilot need | Companion skill pattern to apply |
| --- | --- |
| first setup, agent rules, collaboration | one paper = one AI project + one Git repo + one AI-use log; approval gates for context, plan, edit, run, and publish |
| broad topic or weak question | topic-to-tension builder, two-mechanism competition builder, closest-paper positioning, strict "so what?" test |
| literature and contribution | source-grounded literature map, closest-paper table, fake novelty risk check, claim-to-source check |
| economics empirical design | methods draft/audit, identification pre-mortem, methods-to-code consistency check |
| finance empirical design | finance methods audit, timing and data-leakage checks, asset-pricing/factor-mining guardrails, event-study design checks |
| data construction and outputs | reproducible data pipeline, WRDS/CRSP/Compustat merge plan, variable dictionary, toy-data code verification |
| text-as-data or LLM-generated variables | LLM-as-measurement protocol, human validation sample, prompt/model sensitivity, leakage audit, archive fields |
| verification and disclosure | verification method selector, citation/claim check, code/data-operation check, coefficient magnitude check, AI-use reproducibility packet |
| whole-paper review or referee response | staged self-review, reviewer-risk triage, journal referee response planner |

If the companion repository or linked files are not accessible, ask the user to paste the relevant skill block or proceed from this skill's compact summary while stating the limitation.

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

For data, code, or generated variables, require a verification method matched to the object: toy-data tests for code, source checks for citations, timing checks for coefficients and variables, model/prompt logs for LLM-generated measures, and disclosure records for AI-assisted outputs.

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
