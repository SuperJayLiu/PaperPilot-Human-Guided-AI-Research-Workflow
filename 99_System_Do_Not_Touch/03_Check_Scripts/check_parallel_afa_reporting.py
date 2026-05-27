#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[2]
required = [
    '03_Record_Required_Evidence/09_Parallel_AFA_Documentation/README.md',
    '03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv',
    '03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_packet_template.md',
    '03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_report_status.md',
    '99_System_Do_Not_Touch/05_workflows/parallel_afa_reporting.md',
    '99_System_Do_Not_Touch/02_Skills/12_parallel_afa_reporting_SKILL.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing parallel required evidence recording files:', missing)
    raise SystemExit(1)
for f in [root/'README.md', root/'01_Start_Here/README.md', root/'99_System_Do_Not_Touch/01_Agent_Rules/MASTER_WORKFLOW.md', root/'99_System_Do_Not_Touch/02_Skills/SKILL.md']:
    s=f.read_text(encoding='utf-8')
    if 'Parallel AFA' not in s and 'parallel AFA' not in s:
        print(f'Missing parallel required evidence recording language in {f}')
        raise SystemExit(1)
tracker = (root/'03_Record_Required_Evidence/09_Parallel_AFA_Documentation/afa_reporting_tracker.csv').read_text(encoding='utf-8')
for col in ['full_conversation_saved','human_decision_saved','human_time_logged','model_config_checked','data_access_checked','contribution_log_updated']:
    if col not in tracker:
        print(f'Missing reporting tracker column: {col}')
        raise SystemExit(1)
print('Parallel required evidence recording check passed.')
