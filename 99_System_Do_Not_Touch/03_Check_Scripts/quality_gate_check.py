from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

required = [
    'README.md',
    '01_Start_Here/README.md',
    '01_Start_Here/Use_Codex.md',
    '01_Start_Here/Use_Claude_Code.md',
    '01_Start_Here/Run_Full_Paper_Process.md',
    '01_Start_Here/Data_Safety_First.md',
    '01_Start_Here/Use_As_Is_Or_Tailor.md',
    '02_Build_The_Paper/PAPER_CONTEXT.md',
    '03_Record_Required_Evidence/PROJECT_MEMORY.yml',
    '03_Record_Required_Evidence/01_AI_Conversations',
    '03_Record_Required_Evidence/02_Human_Decisions',
    '03_Record_Required_Evidence/09_Parallel_AFA_Documentation',
    '03_Record_Required_Evidence/10_Novelty_And_Mainstream_Deviations',
    '03_Record_Required_Evidence/11_Journal_Quality_Score',
    '04_Check_And_Finalize_Paper/README.md',
    '04_Check_And_Finalize_Paper/Agent_Behavior_Test.md',
    '04_Check_And_Finalize_Paper/Researcher_Readiness_Check.md',
    '05_Coordinate_Multiple_Agents/README.md',
    '05_Coordinate_Multiple_Agents/Agent_Task_Board.csv',
    '05_Coordinate_Multiple_Agents/Agent_Blockers_Log.csv',
    '99_System_Do_Not_Touch/02_Skills/SKILL.md',
    '99_System_Do_Not_Touch/03_Check_Scripts/check_visible_structure.py',
    '99_System_Do_Not_Touch/03_Check_Scripts/check_clear_wording.py',
    '99_System_Do_Not_Touch/03_Check_Scripts/check_agent_behavior.py',
    '99_System_Do_Not_Touch/03_Check_Scripts/check_multi_agent_collaboration.py',
]

missing = [p for p in required if not (ROOT / p).exists()]
score = round((len(required)-len(missing))/len(required)*100, 1)
print(f'Quality gate score: {score}%')
if missing:
    print('Missing required items:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('Quality gate passed.')
