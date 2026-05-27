# Journal-Quality Score

This folder records the project quality score used by PaperPilot.

The score is a **Journal of Finance-style internal benchmark**, not an official Journal of Finance metric and not a prediction of acceptance. It is a disciplined way to ask whether the project is strong enough to continue, revise, or stop.

## Two score gates

### 1. Idea-stage potential gate

At the idea stage, score both:

- **current idea score**: how strong the idea is now;
- **potential ceiling score**: how strong the idea could become if executed well.

Interpretation:

| Potential ceiling | Decision rule |
| --- | --- |
| 95-100 | Chase. This is the kind of idea worth major effort if data and design are feasible. |
| 85-94 | Promising. Refine the question, data path, or identification before committing. |
| 71-84 | Borderline. Keep only if strategic, unusually feasible, or human author sees value. |
| 70 or below | Give up, pivot, or merge into another project unless the human explicitly overrides. |

The agent must not spend many rounds on ideas whose **maximum plausible score is only about 70**. It should recommend stopping or pivoting.

### 2. Final-paper stop rule

At final-paper review, the paper can stop revision only if:

1. total score is **95/100 or above**;
2. no hard-stop issue remains;
3. remaining issues are classified as documented limitation, future work, not applicable, or accepted human-author judgment;
4. AFA-style reporting records are ready.

A score below 95 does not mean the paper is bad. It means PaperPilot should keep improving or ask the human author whether the remaining gap is acceptable.

## Ten perspectives

The scoring skill uses ten perspectives. Each is scored from 0 to 10. The total is 100.

1. Big question and economic importance.
2. Novel contribution and originality.
3. Literature positioning.
4. Theory, mechanism, or conceptual clarity.
5. Data quality and construction transparency.
6. Identification or empirical-design credibility.
7. Execution, reproducibility, and robustness.
8. Result strength and economic magnitude.
9. Claim discipline, limitations, and referee risk.
10. Writing, tables, figures, and whole-paper coherence.

## Hard-stop issues override the score

Even if the total score is high, the agent must not mark the paper as ready if any hard-stop issue remains:

- unresolved data-permission problem;
- invented or unverified citations;
- unreproducible main result;
- unsupported causal claim;
- contradiction between code, tables, and prose;
- missing AI-use, human-time, model-configuration, or data-access documentation;
- hidden critical limitation;
- referee objection that would likely invalidate the paper and has not been addressed.

## Files in this folder

| File | Purpose |
| --- | --- |
| `idea_quality_scorecard.csv` | idea-stage current score and potential ceiling |
| `final_paper_quality_scorecard.csv` | final-paper quality score across ten perspectives |
| `quality_scoring_rounds.csv` | score history across review rounds |
| `quality_thresholds.md` | interpretation rules |
| `quality_scoring_packet_template.md` | template for agent scoring reports |
| `journal_quality_scorecard.xlsx` | spreadsheet dashboard for scores |
