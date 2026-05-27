#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[2]
mem = root/'03_Record_Required_Evidence/PROJECT_MEMORY.yml'
txt = mem.read_text(encoding='utf-8')
count = txt.count('NEEDS_USER_INPUT')
print(f'Memory file: {mem.relative_to(root)}')
print(f'NEEDS_USER_INPUT fields remaining: {count}')
if count:
    print('This is expected in a fresh template. During a real paper, the agent should ask once and then update memory.')
