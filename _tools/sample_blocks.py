#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print a deterministic sample of EN/ZH block pairs for review."""
import json, os, random, sys

d = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
blocks = json.load(open(os.path.join(d, 'blocks.json')))['blocks']
z = json.load(open(os.path.join(d, 'zh.json')))
zh = z.get('blocks', z)
text = [b for b in blocks if b['kind'] == 'text']
random.Random(seed).shuffle(text)
sel = [b for b in text if len(b['en']) > 80][:n]
for b in sel:
    v = zh.get(b['id'])
    t = v.get('zh') if isinstance(v, dict) else v
    print('=' * 70)
    print('ID:', b['id'], '| kind:', b['what'])
    print('EN:', b['en'][:900])
    print('ZH:', (t or '<<MISSING>>')[:900])
