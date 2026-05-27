#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[2]
required = [
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/README.md',
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/novelty_positioning_register.csv',
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/mainstream_deviation_register.csv',
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/novelty_referee_objection_log.csv',
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/originality_preservation_checklist.md',
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations/deviation_packet_template.md',
    '99_System_Do_Not_Touch/02_Skills/13_novelty_and_mainstream_deviation_SKILL.md',
    '99_System_Do_Not_Touch/05_workflows/novelty_and_mainstream_deviation.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing novelty mechanism files:')
    for p in missing: print(' -', p)
    raise SystemExit(1)
texts = [
    root/'README.md',
    root/'01_Start_Here/README.md',
    root/'01_Start_Here/Run_Full_Paper_Process.md',
    root/'01_Start_Here/Use_Codex.md',
    root/'01_Start_Here/Use_Claude_Code.md',
    root/'99_System_Do_Not_Touch/01_Agent_Rules/MASTER_WORKFLOW.md',
    root/'99_System_Do_Not_Touch/02_Skills/SKILL.md',
]
terms = ['mainstream', 'deviation', 'novelty']
problems=[]
for path in texts:
    txt = path.read_text(encoding='utf-8')
    for term in terms:
        if term not in txt.lower():
            problems.append(f'{path.relative_to(root)} missing term: {term}')
if problems:
    print('Novelty mechanism not referenced in key files:')
    for p in problems: print(' -', p)
    raise SystemExit(1)
print('Novelty and mainstream-deviation mechanisms present and referenced.')
