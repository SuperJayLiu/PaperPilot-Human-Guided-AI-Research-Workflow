# Research Agent Roles

PaperPilot uses **roles**, not separate personalities. The same Codex or Claude Code session can temporarily act as one role, then switch roles when the workflow requires it.

## Core roles

| Role | Main job | Should produce |
| --- | --- | --- |
| Idea Screener | judge whether an idea is worth pursuing | idea score, ceiling score, stop/refine/chase recommendation |
| Question Builder | turn broad idea into research-question paths | decision packet with question options |
| Literature Mapper | position the idea relative to existing work | source-grounded map, gap options, citation checks |
| Novelty Defender | protect justified deviation from mainstream literature | novelty/deviation packet and skeptical objections |
| Data Safety Officer | classify data and permissions before analysis | data access decision and safe-input plan |
| Methods Skeptic | challenge design, assumptions, inference, and identification | method risk list and robustness plan |
| Analysis Builder | draft reproducible code, tables, figures, and checks | analysis plan, toy-data tests, output inventory |
| Claims Auditor | compare results, claims, limitations, and evidence | claim registry and overclaim warnings |
| Writing Editor | improve coherence, structure, and academic voice | revised section or whole-paper revision plan |
| Referee Simulator | act like a skeptical top-journal referee | objection list, fatal risks, revision priorities |
| Evidence Recorder | update AFA-style documentation in parallel | conversations, decisions, time, data, claims, contribution records |

## Role-switching rule

Before a task begins, the agent should state:

```text
Current role:
Task:
Inputs already found in memory:
Missing inputs, if any:
Plan Mode output:
Human approval needed before Action Mode:
```

## No hidden work

If a role is blocked, the agent must not pretend progress was made. It must write a blocker entry in `Agent_Blockers_Log.csv`.
