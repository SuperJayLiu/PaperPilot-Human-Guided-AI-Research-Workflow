from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OLD = '-'.join(['Max','Efficient','Human','Import','for','AI','Generated','Papers'])
SKIP_SUFFIXES = {'.png','.jpg','.jpeg','.pdf','.xlsx','.zip','.pyc'}
hits=[]
for p in ROOT.rglob('*'):
    rel=str(p.relative_to(ROOT))
    if '.git/' in rel or '__pycache__' in rel:
        continue
    if OLD in rel:
        hits.append(f'PATH: {rel}')
    if p.is_file() and p.suffix.lower() not in SKIP_SUFFIXES:
        try:
            txt=p.read_text(encoding='utf-8')
        except Exception:
            continue
        if OLD in txt:
            hits.append(f'TEXT: {rel}')
if hits:
    print('Old working name found:')
    print('\n'.join(hits[:100]))
    raise SystemExit(1)
print('No old working name found.')
