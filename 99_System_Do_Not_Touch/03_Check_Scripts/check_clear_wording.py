from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT_EXTS = {".md", ".txt", ".yml", ".yaml", ".csv", ".py", ".sh", ".cff"}

# Phrases are assembled this way so the checker does not match its own source code.
BAD_PHRASES = [
    "AFA" + " Reports",
    "AFA" + " reports",
    "Human" + " Import",
    "Max-Efficient-Human-" + "Import",
    "99_System_Files" + "_Do_Not_Start_Here",
    "01_Set_Up" + "_The_Workflow_Here",
    "02_Work_On" + "_The_Paper_Here",
    "03_Record_AFA" + "_Reports_Here",
    "04_Check_Quality" + "_And_Final_Paper_Here",
]


def main():
    hits = []
    for path in ROOT.rglob("*"):
        if path.name == "check_clear_wording.py":
            continue
        if path.is_file() and path.suffix in TEXT_EXTS:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for phrase in BAD_PHRASES:
                if phrase in text or phrase in str(path):
                    hits.append((str(path.relative_to(ROOT)), phrase))
    if hits:
        print("Clear-wording check failed.")
        for path, phrase in hits[:50]:
            print(f"{path}: {phrase}")
        raise SystemExit(1)
    print("Clear-wording check passed.")

if __name__ == "__main__":
    main()
