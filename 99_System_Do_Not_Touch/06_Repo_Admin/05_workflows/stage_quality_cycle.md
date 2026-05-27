# Stage Quality Cycle Workflow

Every stage must pass three local quality rounds before it is treated as ready.

## Applies to these stages

1. Research question and story.
2. Literature and positioning.
3. Data access and onboarding.
4. Empirical design.
5. Analysis and outputs.
6. Findings and claims.
7. Writing and revision.
8. Reviewer stress test and response.

## Three-round rule

For each stage, the agent must run:

### Round 1: internal consistency and missing-input check

Check whether the stage output contradicts project memory, repeats old rejected paths, misses required inputs, or uses undefined terms.

### Round 2: evidence, data, method, and feasibility check

Check whether the stage output is grounded in sources, data permissions, feasible implementation, and relevant economics/finance standards.

### Round 3: reviewer-risk, claim-strength, and handoff check

Check whether a strong reviewer would object, whether claims are too strong, and whether the next stage has enough information to proceed without re-asking already answered questions.

## Improvement logic

Each round must:

1. identify issues;
2. classify severity;
3. propose fixes;
4. wait for human approval when fixes change research substance;
5. implement approved fixes in Action Mode;
6. update memory, stage tracker, issue register, and required evidence recording tracker.

## Stop rule

The agent may proceed only if:

- all blocking issues are fixed; or
- the remaining issue is recorded as an accepted limitation, human-approved tradeoff, or future work.

Blocked stages must not silently proceed.

## Novelty preservation in each stage

Round 3 must include a novelty-preservation question: did the agent over-normalize the project and remove a valuable non-mainstream angle without human approval? If yes, run Skill 13 before the stage can close.
