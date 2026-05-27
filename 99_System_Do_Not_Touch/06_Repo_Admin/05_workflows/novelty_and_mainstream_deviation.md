# Novelty and Mainstream-Deviation Workflow

This workflow prevents the agent from overfitting the paper to mainstream literature while still requiring strong justification.

## Principle

```text
Mainstream conformity is not the same as quality.
Deviation is allowed when it is explicit, motivated, testable, and bounded.
```

## Run this workflow at these points

1. Question and story: create at least one mainstream option and one potentially deviating option.
2. Literature: state the mainstream benchmark and the precise gap or disagreement.
3. Data: ask whether a new population, setting, measurement, or source makes deviation plausible.
4. Design: identify tests that could support or falsify the deviation.
5. Findings: prevent overclaiming and prevent the agent from erasing interesting results.
6. Writing: preserve the novel contribution while stating limitations.
7. Reviewer stress test: simulate objections from both mainstream and novelty-friendly reviewers.

## Required output

Each novelty-sensitive stage must update:

```text
03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/
```

The minimum record is one row in either `novelty_positioning_register.csv` or `mainstream_deviation_register.csv`.

## Three-pass novelty check

| Round | Question |
| --- | --- |
| 1. Preservation | Did the agent accidentally normalize away the original idea? |
| 2. Justification | Is the deviation supported by mechanism, data, design, or evidence? |
| 3. Referee discipline | Can the claim survive skeptical mainstream review without overclaiming? |

## Stop rule

Do not mark a non-mainstream claim as ready until it is one of:

```text
well-justified and testable
promising but needs evidence
bounded hypothesis
documented limitation
future work
dropped or merged into standard framing
```
