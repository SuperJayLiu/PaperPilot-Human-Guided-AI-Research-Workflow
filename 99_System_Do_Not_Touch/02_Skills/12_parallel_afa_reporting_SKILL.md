# Skill 12: Parallel AFA Reporting

## Purpose

Maintain the documentation package required for an AI-assisted paper while the paper is being produced, not after the fact.

## When to use this skill

Use after every stage output, every stage-quality round, every major human decision, every data-access decision, and every whole-paper review cycle.

Also use when the user asks about AFA readiness, disclosure, AI logs, human effort logs, model configuration, or contribution shares.

## Read before asking

Check these first:

- `03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv`
- `03_Record_Required_Evidence/06_Submission_Package/afa_ready_checklist.md`
- `03_Record_Required_Evidence/01_AI_Conversations/`
- `03_Record_Required_Evidence/02_Human_Decisions/`
- `03_Record_Required_Evidence/03_Record_Human_Time_And_Contributions/`
- `03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/`
- `03_Record_Required_Evidence/model_config.yml`
- `03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/`

Ask only for missing documentation, not for facts already recorded.


## Required inputs to check first

- Current stage name.
- Current AI conversation or transcript location.
- Human decision packet location, if any.
- Human time/contribution record for the stage.
- Data-access, model-config, claim, and quality-cycle records that changed.

## Workflow

1. Identify the current paper stage and stage-quality round.
2. Check whether the AI transcript has been saved.
3. Check whether human decisions and human time were logged.
4. Check whether data access, model configuration, claims, and contribution shares need updates.
5. Update `afa_reporting_tracker.csv`.
6. Create or update a reporting packet if the stage has a substantive change.
7. Flag missing items before the agent proceeds.

## Required reporting categories

Each stage should update, where relevant:

- AI conversation transcript.
- Human decision packet.
- Human time and direct contribution.
- Model/tool configuration.
- Data access and permission record.
- Claim/evidence/limitation registry.
- Contribution-line or contribution-file classification.
- Stage-quality cycle status.

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

- Waiting until the end to reconstruct documentation.
- Recording a summary but not the full conversation.
- Logging the AI output but not the human decision.
- Updating the paper but not the data-access record.
- Creating claims without evidence or limitation entries.
- Treating model configuration as fixed when the agent/tool changed.

## Verification checklist

Before a stage is marked complete:

- A reporting row exists for the stage.
- Transcript and decision records are linked or marked missing.
- Data and model status are checked.
- Human time/contribution records are updated or marked pending.
- Claim/evidence records are updated if claims changed.
- Missing items are listed as blockers or pending tasks.

## Outputs and records to update

Update the current stage files, `03_Record_Required_Evidence/PROJECT_MEMORY.yml`, relevant decision packets, and the relevant trackers listed above.

## Copy-ready command

```text
Use Skill 12: Parallel AFA Reporting for the current stage. Check existing records first. Update the required evidence recording tracker, identify missing documentation, and tell me what must be logged before the stage can be considered complete.
```
