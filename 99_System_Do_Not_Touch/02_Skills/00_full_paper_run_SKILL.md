# Full Paper Run Skill

## Purpose

Run a complete one-paper workflow from idea to final paper quality checks. This skill is the orchestration layer that connects all other PaperPilot skills.

It should maximize paper quality per unit of human input by making the agent do repeatable work and making the human decide only scarce, high-value choices: question, story, data permission, identification, interpretation, claims, and final responsibility.

## When to use this skill

Use this skill when the user says any of the following:

- "run the whole process";
- "from idea to final paper";
- "full paper run";
- "check the whole paper";
- "improve the whole paper";
- "check consistency";
- "review and improve several rounds";
- "keep checking until remaining issues are fine";
- "make sure I only need to say things once".

Also use it when the project reaches a complete draft and needs whole-paper review rather than section-by-section editing.

## Read before asking

Before asking the user anything, read:

```text
03_Record_Required_Evidence/PROJECT_MEMORY.yml
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/02_Human_Decisions/
03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/
03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/
03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/
```

If a stable fact already appears there, reuse it. Do not ask the user to repeat it. If the fact appears inconsistent or stale, ask: "I found X in memory. Is this still correct?"

## Required inputs to check first

Check whether these are already known:

- broad topic;
- target field: finance / economics / accounting / related;
- paper type: empirical / theory / methods / survey / mixed;
- data status: none yet / public / licensed / restricted / confidential / unknown;
- preferred agent: Codex / Claude Code;
- preferred code environment: Stata / R / Python / LaTeX / mixed / not decided;
- current project stage;
- manuscript path if a draft exists;
- whether human wants the full run from idea or from current stage.

Ask only for missing inputs needed for the next decision packet.

## Workflow

### Phase 0. Memory intake

1. Summarize what the repo already knows.
2. List missing facts.
3. Ask at most five missing questions.
4. Update `03_Record_Required_Evidence/PROJECT_MEMORY.yml` after stable facts are confirmed.

### Phase 1. Generate or refine research question

Use `01_research_question_and_story_SKILL.md`.

Return question/story options with:

- contribution logic;
- feasible data path;
- identification or design path;
- novelty risk;
- likely referee concern;
- human effort required.

### Phase 2. Literature and positioning

Use `02_literature_and_positioning_SKILL.md`.

The output must connect the question to literature, but must not invent citations. Every important citation needs a verification status.

### Phase 3. Data access and data plan

Use `03_data_access_and_onboarding_SKILL.md`.

Classify data before asking for files. Use metadata, schemas, toy rows, and public documentation before raw data.

### Phase 4. Empirical design or theory/method design

Use `04_empirical_design_SKILL.md`.

Return options with identifying assumptions, estimator choices, threats, diagnostics, and what a skeptical reviewer will ask.

### Phase 5. Analysis and outputs

Use `05_analysis_and_outputs_SKILL.md`.

Create run order, code skeletons, output inventory, and validation checks. Use toy data tests before real data whenever possible.

### Phase 6. Findings and claims

Use `06_findings_and_claims_SKILL.md`.

Every finding should enter the claim registry with evidence, limitation, and allowable wording.

### Phase 7. Writing and revision

Use `07_writing_and_revision_SKILL.md`.

Draft the paper in sections, then assemble the full manuscript. Do not polish away uncertainty or limitations.

### Phase 8. Whole-paper review cycle 1: consistency and errors

Read the whole manuscript and records. Check:

- abstract, introduction, methods, results, and conclusion consistency;
- research question and claims alignment;
- data, sample, variable, and timing consistency;
- code/table/prose consistency;
- unsupported claims;
- invented or unverified citations;
- missing documentation.

Create issue register entries. Propose fixes. Wait for approval before editing.

### Phase 9. Whole-paper improvement pass 1

After approval, implement fixes from cycle 1. Then check again and update the issue register.

### Phase 10. Whole-paper review cycle 2: contribution and reviewer risk

Check:

- contribution strength;
- relation to literature;
- economic magnitude;
- causal or interpretive overclaiming;
- missing central robustness checks;
- likely referee objections;
- whether limitations are honest but not self-defeating.

Create issue register entries. Propose fixes. Wait for approval.

### Phase 11. Whole-paper improvement pass 2

Implement approved fixes. Then check again and update the issue register.

### Phase 12. Whole-paper review cycle 3: final readiness

Check:

- final prose, notation, variable names, table and figure references;
- abstract/introduction/conclusion alignment;
- claim registry completeness;
- data access records;
- AI conversation logs;
- human time and contribution logs;
- AFA-style checklist;
- residual issues.

### Phase 13. Whole-paper improvement pass 3

Implement approved final fixes. Then check again.

### Phase 14. Residual issue classification

Classify every remaining issue as one of:

```text
fixed
not applicable
documented limitation
accepted human-author judgment
future work outside this paper
blocked by missing data/access and logged
```

Do not declare the project done while unresolved issues remain outside those categories.

## Decision packet requirements

Every major phase must include a decision packet with:

| Field | Required content |
| --- | --- |
| Decision needed | the choice the human must make |
| Options | usually 2 to 4 choices |
| Pros | why each option helps |
| Cons | why each option may fail |
| Risks | data, identification, literature, code, writing, or disclosure risks |
| Evidence needed | what must be checked before strong claims |
| Agent recommendation | one recommendation with reason |
| Human choice | selected option or revision |
| Files to update | exact paths |

## Common failure modes

- The agent asks for facts already stored in `PROJECT_MEMORY.yml`.
- The agent edits files in Plan Mode.
- The agent improves style without checking data/method/prose consistency.
- The agent treats the first draft as finished.
- The agent fixes local paragraphs but misses paper-level contradictions.
- The agent adds citations or claims that are not verified.
- The agent hides limitations instead of classifying them.
- The agent stops after one review round even though the paper still has material unresolved issues.
- The agent changes conclusions without updating abstract, introduction, tables, and claim registry.

## Verification checklist

Before saying the paper is ready, verify:

- `PROJECT_MEMORY.yml` is updated with stable facts.
- Full AI conversation records are present or summarized according to project rules.
- Human decisions are logged.
- Data access records exist for each dataset.
- Claim registry links claims to evidence.
- All tables/figures are referenced and match the prose.
- Methods match code and data construction.
- Literature claims have verified citations.
- Three whole-paper review cycles are complete or the human explicitly stopped earlier.
- Every remaining issue is fixed, not applicable, documented limitation, accepted human-author judgment, future work, or blocked and logged.

## Outputs and records to update

Update these as the full run progresses:

```text
03_Record_Required_Evidence/PROJECT_MEMORY.yml
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/02_Human_Decisions/
03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/claim_registry.csv
03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/full_paper_run_status.csv
03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/whole_paper_issue_register.csv
03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/review_round_template.md copies
03_Record_Required_Evidence/06_Submission_Package/afa_ready_checklist.md
```


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
Use the Full Paper Run skill.
Start in Plan Mode.
Read existing memory and context first.
Run the whole paper process from the current stage to a final paper.
After a complete draft exists, do three paper-level review and improvement cycles: consistency/errors, contribution/reviewer risk, and final readiness.
Ask only missing questions.
Do not edit files until I approve the decision packet.
Update memory, decision records, issue register, claim registry, and submission checklist after each approved action.
```

## Novelty and mainstream-deviation check

If this stage touches the paper's contribution, literature position, method choice, interpretation, or writing emphasis, the agent must apply **Skill 13: Novelty and Mainstream-Deviation Guardrail** before marking the stage complete.

The agent must not erase a non-mainstream idea merely because it is unusual. It must record the mainstream benchmark, proposed deviation, evidence needed, falsification logic, and skeptical referee objections in `03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/`.
