# Agent Behavior Test

Use this file to check whether Codex or Claude Code is behaving as PaperPilot requires.

## Quick test after the first agent response

Data safety and three-round checks are required throughout the workflow.

The first agent response should do five things:

| Check | Pass condition |
| --- | --- |
| Plan Mode | The agent says it will not edit files yet. |
| Memory first | The agent summarizes what it found in project memory/context. |
| Minimal questions | The agent asks only missing questions needed for the next stage. |
| Decision packet | The agent proposes options, pros/cons, risks, evidence needed, and a recommendation. |
| Evidence plan | The agent says which required records it will update after approval. |

If any item fails, paste the corrective prompt below.

## Corrective prompt

```text
Pause and return to PaperPilot Plan Mode.

Before asking me more questions:
1. read PROJECT_MEMORY.yml and PAPER_CONTEXT.md;
2. summarize what is already known;
3. ask only missing questions;
4. create a decision packet with options, pros/cons, risks, evidence needed, and recommendation;
5. state which required evidence files will be updated after approval.

Do not edit files until I approve the decision packet.
```

## Stage behavior test

At every stage, the agent should pass these tests.

| Desired behavior | What to look for |
| --- | --- |
| Uses stable memory | Does not ask for facts already recorded |
| Protects data | Does not request raw licensed, restricted, confidential, or private data |
| Preserves novelty | Does not flatten a justified novel angle into a generic mainstream extension |
| Runs three checks | Consistency check, evidence/method check, reviewer-risk check |
| Updates records | Conversations, decisions, data access, claims, quality records |
| Gives next action | Tells the human what decision is needed next |

## Codex-specific warning signs

Codex is not behaving correctly if it:

- edits many files before a decision packet is approved;
- treats a first draft as final;
- skips required evidence records;
- ignores data-safety boundaries;
- fails to preserve memory across stages.

## Claude Code-specific warning signs

Claude Code is not behaving correctly if it:

- rewrites local files before approval;
- inspects private/restricted folders without explicit approval;
- makes broad edits outside the approved plan;
- does not run local checks before declaring a stage complete;
- asks the same stable facts repeatedly.

## Final behavior test

Before the paper is called ready, the agent must show:

```text
1. final score across 10 quality dimensions;
2. unresolved issue list;
3. evidence package status;
4. data safety status;
5. contribution record status;
6. final human sign-off needed.
```
