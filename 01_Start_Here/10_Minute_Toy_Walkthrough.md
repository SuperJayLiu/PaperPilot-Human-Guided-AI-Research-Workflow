# 10 Minute Toy Walkthrough

Use this walkthrough to see PaperPilot behavior without exposing real research material.

## Toy setup

```text
Field: finance
Rough idea: whether annual report language about supply-chain risk predicts future inventory investment.
Data status: public filings only for the toy example; no licensed or private data.
Current stage: idea screening.
Goal: decide whether this is worth turning into a real paper.
```

## Prompt

```text
Use $paperpilot-research-workflow for this toy finance idea.
Start in Plan Mode.
Apply relevant AI-for-economics-and-finance companion skill patterns if helpful.
Do not edit files.
Give a decision packet and the three stage checks.
```

## Expected agent behavior

The agent should:

1. classify the task as idea screening plus research-question/taste routing;
2. ask whether to apply the companion topic-to-tension and strict "so what?" patterns;
3. identify at least two mechanisms that could make different predictions;
4. avoid claiming novelty without verified literature;
5. flag data and measurement risks before any analysis;
6. produce a decision packet with options, risks, evidence needed, and recommendation;
7. run the three checks before saying the stage is ready.

## Example decision packet shape

| Field | Example content |
| --- | --- |
| Decision needed | pursue, refine, or drop the toy idea |
| Option A | descriptive text-measure paper using public filings |
| Option B | mechanism-focused paper linking text to inventory investment |
| Option C | drop or merge into a broader supply-chain disclosure project |
| Key risks | fake novelty, LLM measurement error, look-ahead leakage, weak economic magnitude |
| Evidence needed | closest papers, filing timestamp rules, validation sample, baseline investment measure |
| Recommendation | refine before committing; do not start code yet |
| Files to update if real | `PROJECT_MEMORY.yml`, decision packet, data access record, novelty register |

## Stage checks

Round 1 should catch missing inputs: target audience, closest literature, exact text corpus, outcome timing.

Round 2 should catch evidence and feasibility: public filing access, validation set, timing rule, safe data handling.

Round 3 should catch reviewer risk: whether the text measure is real signal or post-hoc narrative, whether claims are predictive rather than causal, and whether economic magnitude can be shown.

## What success looks like

The agent should not produce a polished introduction or code. It should slow the project down enough to make the first human decision better.
