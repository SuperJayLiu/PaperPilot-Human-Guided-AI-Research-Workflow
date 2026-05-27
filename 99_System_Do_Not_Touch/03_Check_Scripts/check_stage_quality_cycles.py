#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[2]
required = [
    '03_Record_Required_Evidence/08_Stage_Quality_Cycles/README.md',
    '03_Record_Required_Evidence/08_Stage_Quality_Cycles/stage_quality_cycle_tracker.csv',
    '03_Record_Required_Evidence/08_Stage_Quality_Cycles/stage_issue_register.csv',
    '03_Record_Required_Evidence/08_Stage_Quality_Cycles/stage_round_template.md',
    '99_System_Do_Not_Touch/05_workflows/stage_quality_cycle.md',
    '99_System_Do_Not_Touch/02_Skills/11_stage_quality_cycle_SKILL.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing stage quality cycle files:', missing)
    raise SystemExit(1)
texts = [
    root/'README.md',
    root/'01_Start_Here/README.md',
    root/'99_System_Do_Not_Touch/01_Agent_Rules/MASTER_WORKFLOW.md',
    root/'99_System_Do_Not_Touch/02_Skills/SKILL.md',
]
for f in texts:
    s=f.read_text(encoding='utf-8')
    if 'Round 1' not in s or 'Round 2' not in s or 'Round 3' not in s:
        print(f'Missing three-round language in {f}')
        raise SystemExit(1)
for p in sorted((root/'99_System_Do_Not_Touch/02_Skills').glob('*_SKILL.md')):
    s=p.read_text(encoding='utf-8')
    if p.name not in ['11_stage_quality_cycle_SKILL.md','12_parallel_afa_reporting_SKILL.md']:
        if 'Mandatory stage-quality and parallel-reporting requirement' not in s:
            print(f'Missing mandatory stage quality requirement in {p.name}')
            raise SystemExit(1)
print('Stage quality cycle check passed.')
