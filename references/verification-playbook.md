# PaperPilot Verification Playbook

Use this reference when an AI-assisted output needs to be checked before it enters a paper, codebase, evidence record, or disclosure package.

Verification is object-specific. Do not accept "looks plausible" as verification.

## Verification selector

| Object | Minimum check | Stronger check |
| --- | --- | --- |
| citation | source exists and metadata are correct | sentence-level support from original source, version, DOI/URL, correction/retraction check |
| literature claim | supplied or verified source supports exact sentence | closest-paper table and claim-to-source map |
| research question | one-sentence testable question and mechanism | topic-to-tension test, two competing mechanisms, strict "so what?" test |
| data permission | source classified by access and sensitivity | data source card, provider rules, allowed AI access, forbidden materials |
| merge or cleaning code | toy input with known answer | real pipeline with logs, match rates, duplicates, missingness, date ranges |
| variable construction | formula, source fields, timing, unit, missing rule | variable dictionary plus code/table/prose consistency check |
| coefficient interpretation | unit, transformation, baseline, uncertainty | magnitude calculation, table/code check, causal-language audit |
| empirical design | identifying variation and assumptions stated | pre-mortem with threats, diagnostics, inference, and failure conditions |
| LLM-generated measure | prompt/model/date/schema archived | human validation set, sensitivity tests, leakage audit, drift check |
| paragraph rewrite | no unsupported claims added | claim registry and table/figure consistency check |
| whole-paper readiness | issue register and quality score | three whole-paper cycles plus final evidence package audit |
| AI disclosure | tasks and tools listed | reproducibility packet with model config, logs, human decisions, and contribution records |

## Required verification output

For non-trivial outputs, return:

```text
Verification method:
Evidence checked:
Fast check result:
Submission-quality check needed:
Stop conditions:
Record updated or to update:
Residual risk:
```

## Stop conditions

Stop and ask the human before proceeding if:

- the original source, code, data, or method details are unavailable;
- the output depends on private, licensed, restricted, confidential, or identifiable material;
- the claim is stronger than the design supports;
- the result cannot be interpreted without units, transformations, baseline, or uncertainty;
- an LLM-generated variable lacks validation and archive fields;
- the verification would require a tool, dataset, or permission the agent does not have.

## AI-use record fields

For substantive AI assistance, update or propose an entry with:

```text
date:
tool_or_model:
task:
input_materials:
data_sensitivity:
output_accepted:
human_checks:
files_changed:
claims_affected:
remaining_uncertainty:
```

## Fast recovery prompt

```text
Select the right PaperPilot verification method for this output.
Do not improve the output yet.
First tell me what evidence is needed, what can be checked now, what cannot be checked, and what would stop this from entering the paper.
```
