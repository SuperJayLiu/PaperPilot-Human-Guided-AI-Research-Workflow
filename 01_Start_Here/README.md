# 01 Start Here

Use this folder to begin the project. Do not add data or edit paper files until you choose an agent mode and read the data-safety note.

## Start in four steps

| Step | Do this | File |
| --- | --- | --- |
| 1 | Decide whether to use directly or tailor first | `Use_As_Is_Or_Tailor.md` |
| 2 | Choose your agent | `Use_Codex.md` or `Use_Claude_Code.md` |
| 3 | Read data safety before adding materials | `Data_Safety_First.md` |
| 4 | Start the end-to-end paper workflow | `Run_Full_Paper_Process.md` |

## What you need to provide first

You can begin with very little:

```text
1. Broad idea or field
2. Whether you use Codex or Claude Code
3. What materials are safe to share
4. Any known data source or method preference
5. Whether you want to use the repo as-is or tailor it
```

The agent should then check project memory, ask only missing questions, and create the first decision packet.

## What the agent should not do first

The agent should not:

- edit files before a plan is approved;
- ask you to repeat facts already in memory;
- inspect raw private, licensed, or restricted data;
- skip the decision packet;
- skip required evidence records.

## First prompt

Use the first prompt inside the Codex or Claude Code file. For a full paper run, use the prompt in `Run_Full_Paper_Process.md`.


## If you want multiple agent roles

After choosing Codex or Claude Code, you can open:

```text
05_Coordinate_Multiple_Agents/README.md
```

Use it to keep a task board, blocker log, and status log when the agent acts as Idea Screener, Data Safety Officer, Methods Skeptic, Claims Auditor, Referee Simulator, or Evidence Recorder.
