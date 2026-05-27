from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[2]
old_names = [
    'AGENTS.md','CHANGELOG.md','CITATION.cff','CLAUDE.md','CLEANUP_OLD_FOLDERS.md','CODEX.md',
    'DATA_SAFETY_FIRST.md','FULL_PAPER_RUN.md','LICENSE','MASTER_WORKFLOW.md','Makefile',
    'SECURITY.md','START_HERE.md','requirements.txt','.github','PAPER_WORKSPACE','PROJECT_RECORDS','_repo_system',
    'analysis','data','decision_logs','decision_packets','docs','examples','logs','output','project','scripts','skills','submission_documentation','templates'
]
for name in old_names:
    p=ROOT/name
    if p.exists():
        if p.is_dir(): shutil.rmtree(p)
        else: p.unlink()
print('Old root clutter removed. Run check_visible_structure.py next.')
