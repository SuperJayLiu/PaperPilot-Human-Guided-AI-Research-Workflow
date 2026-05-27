#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[2]
required = [
    root/'01_Start_Here/Run_Full_Paper_Process.md',
    root/'99_System_Do_Not_Touch/02_Skills/00_full_paper_run_SKILL.md',
    root/'03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/README.md',
    root/'03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/full_paper_run_status.csv',
    root/'03_Record_Required_Evidence/07_Full_Paper_Quality_Cycles/whole_paper_issue_register.csv',
]
missing = [p.relative_to(root) for p in required if not p.exists()]
if missing:
    print('Missing full-paper-cycle files:')
    for m in missing:
        print(' -', m)
    raise SystemExit(1)
texts = [
    root/'README.md', root/'01_Start_Here/README.md', root/'01_Start_Here/Use_Codex.md', root/'01_Start_Here/Use_Claude_Code.md',
    root/'99_System_Do_Not_Touch/01_Agent_Rules/MASTER_WORKFLOW.md',
    root/'99_System_Do_Not_Touch/02_Skills/SKILL.md',
]
for p in texts:
    txt = p.read_text(encoding='utf-8')
    if '01_Start_Here/Run_Full_Paper_Process.md' not in txt and '00_full_paper_run_SKILL.md' not in txt:
        print('Full paper run not referenced in', p.relative_to(root))
        raise SystemExit(1)
skill = (root/'99_System_Do_Not_Touch/02_Skills/00_full_paper_run_SKILL.md').read_text(encoding='utf-8').lower()
for phrase in ['three whole-paper review', 'consistency', 'reviewer risk', 'final readiness', 'project_memory.yml']:
    if phrase not in skill:
        print('Full paper skill missing phrase:', phrase)
        raise SystemExit(1)
print('Full paper cycle check passed.')
