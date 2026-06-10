# PaperPilot Gotchas

Use this reference when the agent seems too confident, skips a gate, repeats a known question, or produces a polished output before checking evidence.

## High-severity gotchas

| Gotcha | Why it matters | Correct behavior |
| --- | --- | --- |
| Asking for stable facts already in memory | Wastes human time and breaks the "say it once" rule | Read `PROJECT_MEMORY.yml`, `PAPER_CONTEXT.md`, prior decisions, and data records before asking |
| Editing before approval | Collapses Plan Mode and Action Mode | Produce a decision packet, list files to update, and wait for approval |
| Inventing citations or novelty | Creates false contribution claims | Use supplied or verified sources; mark unsupported claims as VERIFY |
| Treating a dataset as the research question | Produces easy but weak papers | Ask what economic or financial tension the data can answer |
| Treating fixed effects as identification | Leads to invalid causal language | State identifying variation, assumptions, threats, and required diagnostics |
| Treating return predictability as causality | Common finance overclaim | Distinguish prediction, association, mechanism, and causal claims |
| Using raw or licensed data casually | Creates data-provider and privacy risk | Classify data and prefer metadata, codebooks, toy data, or approved secure environments |
| Treating LLM labels as ground truth | Makes the model an undocumented measurement instrument | Archive prompt, model, date, inputs, schema, validation sample, and sensitivity checks |
| Writing prose before checking tables/code | Hides inconsistencies | Check methods, outputs, labels, and claims before style revision |
| Marking stages complete after one answer | Skips PaperPilot's core quality loop | Run all three stage checks and classify remaining issues |

## Stage-specific gotchas

### Idea and question

- Do not reward novelty language without a clear mechanism and feasible evidence.
- Do not choose the easiest analysis if the economic stakes are weak.
- Ask what result would surprise a knowledgeable reader.

### Literature

- Do not claim "no one has studied this" without a documented search and closest-paper comparison.
- Treat papers as close if they share design, data, variation, or mechanism, not only topic words.
- Keep verified sources separate from candidate sources.

### Data and code

- Never overwrite raw data.
- Do not merge finance data by ticker/year without checking identifiers and link validity.
- Require toy-data tests for new merge, variable construction, table, and figure code.
- Print sample counts, match rates, duplicates, date ranges, and missingness after major steps.

### Methods

- For DiD/event studies, check treatment timing, heterogeneity, estimator choice, pre-trends, spillovers, and clustering.
- For IV, check exclusion, relevance, weak-instrument diagnostics, and interpretation.
- For RD, check bandwidth, manipulation, local interpretation, and robustness.
- For asset pricing, check delisting returns, survivorship, benchmark choice, multiple testing, transaction costs, and sample-period dependence.

### Findings and writing

- Interpret coefficients in units, not vibes.
- Separate statistical significance, economic magnitude, and causal interpretation.
- Do not smooth away limitations; classify them.
- Keep abstract, introduction, methods, results, conclusion, tables, figures, and claim registry aligned.

## Recovery prompt

Use this when the agent drifted:

```text
Pause. Re-enter PaperPilot Plan Mode.
Read memory, paper context, prior decisions, data access records, and claim/risk records.
Identify which PaperPilot gotcha may have occurred.
Do not edit files yet.
Give a corrected decision packet, verification plan, and exact records to update if I approve.
```
