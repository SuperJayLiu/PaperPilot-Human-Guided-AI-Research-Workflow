# PaperPilot Skill Pack

Use this folder as the skill library for one AI-assisted paper.

Before any skill runs, the agent must:

1. read `03_Record_Required_Evidence/PROJECT_MEMORY.yml`;
2. read `02_Build_The_Paper/PAPER_CONTEXT.md`;
3. check prior decisions;
4. ask only missing questions;
5. update memory after stable facts are confirmed.

## Skills

| Stage | Skill |
| --- | --- |
| Full paper run | `00_full_paper_run_SKILL.md` |
| Question and story | `01_research_question_and_story_SKILL.md` |
| Literature | `02_literature_and_positioning_SKILL.md` |
| Data access | `03_data_access_and_onboarding_SKILL.md` |
| Empirical design | `04_empirical_design_SKILL.md` |
| Analysis | `05_analysis_and_outputs_SKILL.md` |
| Findings | `06_findings_and_claims_SKILL.md` |
| Writing | `07_writing_and_revision_SKILL.md` |
| Review | `08_reviewer_stress_test_SKILL.md` |
| Documentation | `09_afa_documentation_SKILL.md` |
| Slides | `10_slides_and_presentations_SKILL.md` |
| Stage quality cycle | `11_stage_quality_cycle_SKILL.md` |
| Parallel required evidence recording | `12_parallel_afa_reporting_SKILL.md` |
| Novelty and mainstream deviation | `13_novelty_and_mainstream_deviation_SKILL.md` |
| Journal-quality scoring | `14_journal_quality_scoring_SKILL.md` |


## After every stage skill

After using any stage skill from 01 to 10, run:

1. `11_stage_quality_cycle_SKILL.md`;
2. `12_parallel_afa_reporting_SKILL.md`.

This means every stage has three local checks and a parallel documentation update.


## Three-round local stage check

Every stage skill must be followed by Skill 11. The required rounds are: Round 1: internal consistency and missing-input check; Round 2: evidence, data, method, and feasibility check; Round 3: reviewer-risk, claim-strength, and next-stage handoff check.


## Novelty and mainstream-deviation guardrail

Run Skill 13 whenever a stage may produce or revise a non-mainstream idea. The agent must preserve promising originality long enough to evaluate it, while requiring justification, falsification logic, and bounded claim wording. This is especially relevant for question, literature, design, findings, writing, reviewer stress tests, and whole-paper review.


## Journal-quality scoring layer

Run Skill 14 at the idea stage, after major stage cycles when helpful, after each whole-paper revision cycle, and before final readiness. Idea-stage potential ceilings around 70/100 should usually be abandoned or pivoted. Final paper revision may stop only when the score is 95/100 or above and no hard-stop issue remains.

Journal-quality score records are stored in:

```text
03_Record_Required_Evidence/11_Journal_Quality_Score/
```
