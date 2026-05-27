from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
skills = ROOT/'99_System_Do_Not_Touch/02_Skills'
required_sections = ['when to use', 'required inputs', 'workflow', 'decision', 'common failure', 'verification']
problems=[]
for p in skills.glob('*_SKILL.md'):
    txt=p.read_text(encoding='utf-8', errors='ignore').lower()
    for sec in required_sections:
        if sec not in txt:
            problems.append(f'{p.name}: missing {sec}')
if problems:
    print('Skill quality check found issues:')
    print('\n'.join(problems[:80]))
    raise SystemExit(1)
print('Skill quality check passed.')
