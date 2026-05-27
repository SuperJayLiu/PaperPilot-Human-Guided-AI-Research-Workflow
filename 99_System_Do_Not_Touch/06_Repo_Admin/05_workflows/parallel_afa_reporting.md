# Parallel AFA Reporting Workflow

The paper workflow and the disclosure/reporting workflow must run in parallel.

## Principle

Do not wait until the final paper to reconstruct what happened. After every stage and every quality round, record:

- what prompt or agent task was used;
- what the AI produced;
- what the human decided;
- what files changed;
- what data were used or deliberately not shared;
- what model/tool configuration was used;
- how unresolved issues were classified.

## Stage reporting packet

At the end of each stage, create or update a reporting packet using:

```text
03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_packet_template.md
```

## Required tracker

Update:

```text
03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv
```

A stage is not complete until its reporting row is complete enough for the current stage.

## Final reporting bundle

At the end of the project, the agent uses the tracker to assemble the submission documentation from existing records rather than reconstructing it from memory.
