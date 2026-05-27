from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
required = [
    '05_Coordinate_Multiple_Agents/README.md',
    '05_Coordinate_Multiple_Agents/Research_Agent_Roles.md',
    '05_Coordinate_Multiple_Agents/Agent_Task_Board.csv',
    '05_Coordinate_Multiple_Agents/Agent_Blockers_Log.csv',
    '05_Coordinate_Multiple_Agents/Agent_Status_Log.csv',
    '05_Coordinate_Multiple_Agents/Reusable_Lessons_Log.csv',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Multi-agent collaboration check failed.')
    for p in missing:
        print('-', p)
    raise SystemExit(1)

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
if '05_Coordinate_Multiple_Agents' not in readme or 'task board' not in readme.lower():
    print('README does not explain the multi-agent collaboration folder.')
    raise SystemExit(1)

print('Multi-agent collaboration check passed.')
