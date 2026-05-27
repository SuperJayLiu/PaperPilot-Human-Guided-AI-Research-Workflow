from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALLOWED_ROOT = {
    "README.md",
    ".gitignore",
    "01_Start_Here",
    "02_Build_The_Paper",
    "03_Record_Required_Evidence",
    "04_Check_And_Finalize_Paper",
    "05_Coordinate_Multiple_Agents",
    "99_System_Do_Not_Touch",
}

def main():
    names = {p.name for p in ROOT.iterdir() if p.name != ".git"}
    extra = sorted(names - ALLOWED_ROOT)
    missing = sorted(ALLOWED_ROOT - names)
    if extra or missing:
        print("Visible-structure check failed.")
        if extra:
            print("Unexpected root items:", ", ".join(extra))
        if missing:
            print("Missing root items:", ", ".join(missing))
        raise SystemExit(1)
    print("Visible-structure check passed.")

if __name__ == "__main__":
    main()
