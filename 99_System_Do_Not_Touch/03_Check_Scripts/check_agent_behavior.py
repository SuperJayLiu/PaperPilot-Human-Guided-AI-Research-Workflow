from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

required = {
    "README.md": [
        "Plan Mode",
        "Check memory before asking",
        "decision packets",
        "Agent_Behavior_Test.md",
    ],
    "01_Start_Here/Use_Codex.md": [
        "Plan Mode",
        "Before asking",
        "decision packet",
        "After approved action",
        "Agent_Behavior_Test.md",
    ],
    "01_Start_Here/Use_Claude_Code.md": [
        "Plan Mode",
        "Before asking",
        "decision packet",
        "After approved action",
        "Agent_Behavior_Test.md",
    ],
    "01_Start_Here/Run_Full_Paper_Process.md": [
        "Round 1",
        "Round 2",
        "Round 3",
        "required evidence",
        "quality score",
    ],
    "04_Check_And_Finalize_Paper/Agent_Behavior_Test.md": [
        "Plan Mode",
        "Memory first",
        "Decision packet",
        "Data safety",
        "three-round",
    ],
    "99_System_Do_Not_Touch/01_Agent_Rules/AGENTS.md": [
        "Memory-first rule",
        "Decision-packet rule",
        "Stage-quality rule",
        "Parallel evidence rule",
    ],
    "99_System_Do_Not_Touch/01_Agent_Rules/MASTER_WORKFLOW.md": [
        "Before every stage",
        "Stage loop",
        "Full-paper loop",
        "Required behavior checks",
    ],
}

problems = []
for rel, phrases in required.items():
    path = ROOT / rel
    if not path.exists():
        problems.append(f"missing file: {rel}")
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for phrase in phrases:
        if phrase not in text:
            problems.append(f"{rel}: missing phrase {phrase!r}")

if problems:
    print("Agent behavior check failed:")
    for p in problems:
        print("-", p)
    raise SystemExit(1)

print("Agent behavior check passed.")
