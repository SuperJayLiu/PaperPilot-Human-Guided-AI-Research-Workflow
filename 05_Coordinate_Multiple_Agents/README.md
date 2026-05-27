# 05 Coordinate Multiple Agents

Use this folder only when you want **more than one agent role** helping with the same paper.

You still choose only one tool at the front door, either Codex or Claude Code. Inside that tool, PaperPilot can ask the agent to act as different research roles, for example Idea Screener, Methods Skeptic, Data Safety Officer, Claims Auditor, Referee Simulator, and Evidence Recorder.

The purpose of this folder is simple:

```text
one paper
→ many research roles
→ one task board
→ one memory file
→ one evidence record
→ no repeated questions
```

## When to use this folder

Use it when:

- the paper has several moving parts;
- you want separate rounds of idea, data, method, writing, and referee review;
- one agent is running multiple tasks over time;
- Codex or Claude Code needs a clear task board before editing files;
- you want blockers and human decisions recorded instead of hidden in chat.

Do not start here if you are new. Start with `01_Start_Here/` first.

## The multi-agent loop

```text
1. Check project memory.
2. Check the current task board.
3. Choose the research role for this task.
4. Work in Plan Mode first.
5. Produce a decision packet if human judgment is needed.
6. Wait for approval before Action Mode.
7. Update paper outputs.
8. Update required evidence records.
9. Report status: done, blocked, or needs human.
10. Add a reusable lesson if the task teaches a repeatable rule.
```

## Files in this folder

| File | Use |
| --- | --- |
| `Research_Agent_Roles.md` | explains the roles the agent can temporarily adopt |
| `Agent_Task_Board.csv` | tracks tasks, status, owner role, needed input, output file, evidence file |
| `Agent_Blockers_Log.csv` | records blockers that prevent progress |
| `Agent_Status_Log.csv` | records short status updates after agent work |
| `Reusable_Lessons_Log.csv` | records project-specific lessons that may become custom skills |

## Rule for researchers

You should only need to state a stable fact once. If the agent asks for information already stored in memory, tell it:

```text
Check project memory and the task board before asking me again.
```
