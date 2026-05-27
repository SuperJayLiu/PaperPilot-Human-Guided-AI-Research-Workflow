from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
paths = [
    ROOT/'03_Record_Required_Evidence/PROJECT_MEMORY.yml',
    ROOT/'03_Record_Required_Evidence/MEMORY_CHECKLIST.md',
    ROOT/'02_Build_The_Paper/PAPER_CONTEXT.md',
]
missing = [str(p.relative_to(ROOT)) for p in paths if not p.exists()]
if missing:
    print('Memory protocol missing files:', missing)
    raise SystemExit(1)
text = '\n'.join(p.read_text(encoding='utf-8', errors='ignore') for p in paths)
terms = ['research question','data','method','novelty','model','decision']
missing_terms = [t for t in terms if t.lower() not in text.lower()]
if missing_terms:
    print('Memory protocol may be incomplete; missing terms:', missing_terms)
    raise SystemExit(1)
print('Memory protocol check passed.')
