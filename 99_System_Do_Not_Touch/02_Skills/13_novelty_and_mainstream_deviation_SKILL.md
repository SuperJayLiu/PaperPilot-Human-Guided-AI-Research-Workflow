# Skill 13: Novelty and Mainstream-Deviation Guardrail

## Purpose

Protect genuinely novel ideas from being flattened into generic mainstream framing while forcing any deviation from the literature to be justified, testable, and carefully stated.

This skill is not a license to be contrarian. It is a mechanism for distinguishing:

```text
unsupported deviation  -> should be rejected or softened
non-mainstream but testable idea -> should be preserved, tested, and bounded
```

## When to use this skill

Use this skill whenever the agent is:

- generating or choosing the research question;
- positioning the paper in the literature;
- deciding whether the contribution is incremental or disruptive;
- evaluating an unusual data source, variable, mechanism, or empirical design;
- interpreting results that run against prior literature;
- writing novelty, contribution, limitations, abstract, introduction, or conclusion;
- simulating referee reports.

Also use it when the user says any of:

```text
This is not the mainstream view.
I want a more original angle.
The literature mostly says the opposite.
Do not make it too generic.
How can I justify this unusual idea?
What if referees think this is too far from the literature?
```

## Read before asking

Before asking the user to repeat anything, read:

```text
03_Record_Required_Evidence/PROJECT_MEMORY.yml
02_Build_The_Paper/PAPER_CONTEXT.md
03_Record_Required_Evidence/02_Human_Decisions/
03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/
03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/
```

If the mainstream benchmark, novelty claim, or risk tolerance has already been recorded, reuse it. If it seems stale or contradictory, ask whether to update it.

## Required inputs to check first

| Input | Where to check first | Ask only if missing? |
| --- | --- | --- |
| Proposed novel claim or deviation | `PROJECT_MEMORY.yml`, `PAPER_CONTEXT.md`, novelty records | Yes |
| Mainstream benchmark | literature records and novelty records | Yes |
| Why the deviation may be plausible | novelty register, claim registry | Yes |
| Evidence available or needed | claim registry, data/design records | Yes |
| Human risk tolerance | `PROJECT_MEMORY.yml` | Yes |
| Target audience or session | `PROJECT_MEMORY.yml` | Yes |

## Workflow

1. **State the mainstream benchmark.** What would a standard paper in this literature normally claim, measure, or estimate?
2. **State the proposed deviation.** Is the paper deviating in question, mechanism, data, method, interpretation, or writing emphasis?
3. **Separate novelty from unsupported speculation.** Write what is known, what is hypothesized, and what must be tested.
4. **Build the justification ladder.** Look for conceptual logic, institutional facts, measurement improvement, overlooked setting, testable prediction, falsification test, or boundary condition.
5. **Create options.** The options should include keeping the deviation central, keeping it as a bounded hypothesis, testing it while framing conservatively, or dropping/merging it.
6. **Run the skeptical referee test.** Write the strongest mainstream objection and what evidence would answer it.
7. **Update records.** Add or revise rows in the novelty registers and claim/evidence records.

## Decision packet requirements

Every novelty-sensitive decision packet must include:

1. mainstream benchmark;
2. proposed deviation;
3. why the deviation may be valuable;
4. why it may be wrong;
5. evidence needed to support it;
6. evidence that would falsify it;
7. 2 to 4 options with pros, cons, risks, and recommendation;
8. suggested wording that is original but not overclaimed;
9. record updates required.

## Three novelty checks

After drafting any novelty-sensitive output, run:

### Round 1: originality preservation

- Did the agent turn the idea into a generic literature extension?
- Did the agent remove the surprising part without human approval?
- Did the agent preserve at least one non-mainstream path as an evaluated option?

### Round 2: justification and falsifiability

- Is the deviation supported by mechanism, data, institutional facts, or testable predictions?
- Is there a feasible falsification, placebo, robustness, or boundary test?
- Are claims kept as hypotheses when evidence is not yet available?

### Round 3: mainstream referee stress test

- What would a skeptical mainstream referee object to?
- Which objections are valid and require changes?
- Which objections are taste differences that can be addressed through framing?
- Is the claim strong enough to be interesting but bounded enough to be credible?

## Common failure modes

- Rejecting an idea only because it is not the standard framing.
- Treating novelty as a synonym for importance.
- Hiding the non-mainstream contribution in vague language.
- Overclaiming a surprising result without falsification or mechanism.
- Using mainstream literature as decoration instead of as the benchmark being extended or challenged.
- Allowing the agent to soften every claim until the paper becomes generic.
- Forgetting to update novelty records after changing the question or claim.

## Verification checklist

- The mainstream benchmark is named.
- The exact deviation is named.
- The deviation is justified by at least one mechanism, data feature, or testable prediction.
- Falsification or disconfirming evidence is stated.
- Reviewer objections are recorded.
- The claim is phrased as central contribution, bounded hypothesis, limitation, future work, or dropped.
- Records in `03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/` are updated.

## Outputs and records to update

```text
03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/novelty_positioning_register.csv
03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/mainstream_deviation_register.csv
03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/novelty_referee_objection_log.csv
03_Record_Required_Evidence/05_Record_Claims_Evidence_And_Risks/claim_registry.csv
03_Record_Required_Evidence/PROJECT_MEMORY.yml
```

## Copy-ready command

```text
Use Skill 13: Novelty and Mainstream-Deviation Guardrail. Start in Plan Mode. First state the mainstream benchmark and the proposed deviation. Do not reject the deviation merely because it is non-mainstream. Create a decision packet with pros, cons, risks, evidence needed, falsification tests, and referee objections. Then update the novelty records after I choose.
```

## Mandatory stage-quality and parallel-reporting requirement

This skill does not complete a stage by itself. After a novelty-sensitive stage output is drafted or revised, the agent must run:

1. **Skill 11: Stage Quality Cycle** for three local rounds:
   - Round 1: internal consistency and missing-input check;
   - Round 2: evidence, data, method, and feasibility check;
   - Round 3: reviewer-risk, claim-strength, originality-preservation, and next-stage handoff check.
2. **Skill 12: Parallel AFA Reporting** to update the reporting tracker and note whether a novelty/deviation record was updated.

The agent may not mark a novelty-sensitive stage complete merely because it produced an interesting or polished non-mainstream claim. The stage is complete only when remaining issues are fixed, accepted as limitations, logged as human-approved tradeoffs, marked as future work, or blocked pending human action.
