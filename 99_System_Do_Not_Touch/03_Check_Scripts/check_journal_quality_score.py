from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
required = [
    ROOT/'03_Record_Required_Evidence/11_Journal_Quality_Score/README.md',
    ROOT/'99_System_Do_Not_Touch/02_Skills/14_journal_quality_scoring_SKILL.md',
]
missing=[str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    print('Journal quality scoring files missing:', missing)
    raise SystemExit(1)
print('Journal quality score check passed.')
