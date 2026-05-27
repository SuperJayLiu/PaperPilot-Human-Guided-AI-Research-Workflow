# Skill 11: Stage Quality Cycle

## Purpose

Run the required three-round quality check for any individual research stage before the agent moves to the next stage.

## When to use this skill

Use after the agent creates or revises any stage output: research question, literature map, data plan, empirical design, analysis plan, results, claims, writing, or reviewer response.

Also use it when the user asks: "check this stage," "are we ready to move on," "make sure the question/design/data/writing is good," or "what remains?"

## Read before asking

Read these before asking the user anything:

- `03_Record_Required_Evidence/PROJECT_MEMORY.yml`
- `02_Build_The_Paper/PAPER_CONTEXT.md`
- the current stage output files
- prior decision packets in `03_Record_Required_Evidence/02_Human_Decisions/`
- prior stage issues in `03_Record_Required_Evidence/08_Stage_Quality_Cycles/stage_issue_register.csv`
- the AFA tracker in `03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv`

If a fact is already recorded, do not ask again. Ask only if the record is missing, stale, or contradictory.


## Required inputs to check first

- Current stage name and stage output file.
- Prior decision packets for the same stage.
- Relevant data-access, method, claim, and novelty records.
- Any human-approved tradeoffs already logged.

## Workflow

1. Read project memory, paper context, prior decisions, and current stage output.
2. Run Round 1: internal consistency and missing-input check.
3. Propose fixes and wait for human approval when needed.
4. Run Round 2: evidence, data, method, and feasibility check.
5. Propose fixes and wait for human approval when needed.
6. Run Round 3: reviewer-risk, claim-strength, and next-stage handoff check.
7. Classify every remaining issue.
8. Update stage trackers, issue registers, memory, and required evidence recording.
9. State whether the stage is ready, blocked, or ready only with a logged human-approved tradeoff.

## Three required rounds

### Round 1: internal consistency and missing-input check

Check:

- Does the stage contradict project memory?
- Are key terms, sample, data, variables, or claims undefined?
- Did the agent reopen a rejected path without reason?
- Are there missing human decisions?
- Is the stage output clear enough for the next stage?

### Round 2: evidence, data, method, and feasibility check

Check:

- Are claims grounded in sources, data, code, or clearly marked as hypotheses?
- Are data permissions and privacy constraints respected?
- Is the method feasible with the available data?
- Are software/tool choices realistic?
- Does the output include the evidence needed for the next stage?

### Round 3: reviewer-risk, claim-strength, and handoff check

Check:

- What would a skeptical reviewer challenge first?
- Are the claims too strong for the design?
- Are limitations honestly recorded without weakening the paper unnecessarily?
- Can the next stage proceed without asking repeated questions?
- Are remaining issues classified correctly?

## Issue status values

Every issue must end as one of:

- Fixed
- Accepted limitation
- Human-approved tradeoff
- Blocked
- Future work

## Records to update

- `03_Record_Required_Evidence/08_Stage_Quality_Cycles/stage_quality_cycle_tracker.csv`
- `03_Record_Required_Evidence/08_Stage_Quality_Cycles/stage_issue_register.csv`
- `03_Record_Required_Evidence/PROJECT_MEMORY.yml`
- `02_Build_The_Paper/PAPER_CONTEXT.md`, if stable facts changed
- `03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv`

## Decision packet requirements

If the skill proposes a substantive change, return a decision packet with:

1. the decision required;
2. options;
3. pros, cons, and risks;
4. evidence needed;
5. recommended option;
6. files to change in Action Mode;
7. records to update.

## Common failure modes

- Running only a final paper check and skipping local stage checks.
- Treating "no obvious problem" as a completed three-round cycle.
- Fixing wording while leaving data, method, or claim problems unresolved.
- Asking the user again for facts already in memory.
- Letting blocked stages proceed without a logged human override.

## Verification checklist

Before declaring the stage ready:

- Round 1, 2, and 3 are recorded.
- All issues have statuses.
- No blocker remains, or a human-approved tradeoff is logged.
- required evidence recording tracker is updated.
- Memory is updated for stable facts.
- Next-stage handoff is clear.

## Outputs and records to update

Update the current stage files, `03_Record_Required_Evidence/PROJECT_MEMORY.yml`, relevant decision packets, and the relevant trackers listed above.

## Copy-ready command

```text
Use Skill 11: Stage Quality Cycle on the current stage. Start in Plan Mode. Check memory and prior decisions first. Run Round 1, Round 2, and Round 3. Do not move to the next stage until blockers are fixed or explicitly accepted by me. Update the stage quality tracker and required evidence recording tracker.
```

## Novelty and mainstream-deviation check

If this stage touches the paper's contribution, literature position, method choice, interpretation, or writing emphasis, the agent must apply **Skill 13: Novelty and Mainstream-Deviation Guardrail** before marking the stage complete.

The agent must not erase a non-mainstream idea merely because it is unusual. It must record the mainstream benchmark, proposed deviation, evidence needed, falsification logic, and skeptical referee objections in `03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/`.
