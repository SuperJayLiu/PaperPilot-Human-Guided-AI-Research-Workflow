# Memory Checklist

Before the agent asks the user a question, it must check:

1. `03_Record_Required_Evidence/PROJECT_MEMORY.yml`
2. `02_Build_The_Paper/PAPER_CONTEXT.md`
3. `03_Record_Required_Evidence/02_Human_Decisions/`
4. `03_Record_Required_Evidence/04_Record_Data_Access_And_Permissions/data_access.md`
5. `03_Record_Required_Evidence/00_dashboard/PROJECT_DASHBOARD.md`

The agent should ask only if:

- the information is missing;
- the information is contradictory;
- the information may have changed;
- the decision requires fresh human judgment.

Every answer that becomes a stable fact must be copied into `PROJECT_MEMORY.yml`.

## Novelty memory

Before asking the user again about originality or deviation from the literature, check these memory fields:

- mainstream benchmark;
- proposed deviation;
- why the deviation is plausible;
- evidence needed;
- falsification tests;
- skeptical referee objections;
- human risk tolerance.

If any of these were already answered, reuse them. If they changed, update `PROJECT_MEMORY.yml` and log the change.
