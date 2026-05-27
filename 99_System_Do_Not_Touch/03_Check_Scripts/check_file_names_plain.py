#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[2]
problems=[]
for p in root.rglob('*'):
    rel=str(p.relative_to(root))
    if any(part.startswith('.git') for part in p.parts):
        continue
    if len(p.name) > 80:
        problems.append(f'long name: {rel}')
    if ' ' in p.name:
        problems.append(f'space in name: {rel}')
if problems:
    print('\n'.join(problems)); raise SystemExit(1)
print('File-name clarity check passed.')
