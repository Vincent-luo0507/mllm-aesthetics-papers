#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split orig.html into translatable text blocks + atomic blocks (math/figure/table/code).

Guarantee: math markup, <img>, <svg>, <table>, <pre> are NEVER touched by the
translator — they are lifted into atomic blocks / ⟦SLOT_n⟧ placeholders and
re-inserted verbatim by build_index.py.
"""
import json, os, re, sys
from bs4 import BeautifulSoup, NavigableString, Tag

BLOCK_TAGS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'figcaption',
              'blockquote', 'dt', 'dd', 'caption', 'td', 'th'}
ATOMIC_TAGS = {'img', 'svg', 'math', 'picture', 'iframe', 'object'}
COLLECT = BLOCK_TAGS | ATOMIC_TAGS | {'table', 'pre'}

# Verbose-only regions: kept verbatim, never translated.
# NOTE: \b boundaries are essential — `ltx_authors_1line` must NOT match `ltx_authors`.
KEEP_RE = re.compile(
    r'\b(ltx_biblist|ltx_bibitem|ltx_bibblock|bibitem|ltx_title_document|'
    r'ltx_abstract|ltx_authors|ltx_date|ltx_pubnotes|ltx_affiliation|ltx_contact)\b')


def in_keep(el):
    p = el
    while p is not None and isinstance(p, Tag):
        cls = ' '.join(p.get('class') or [])
        if KEEP_RE.search(cls):
            return True
        p = p.parent
    return False


def content_root(soup):
    for sel in ('article.ltx_document', 'div.ltx_document', 'article', 'div.ltx_page_main', 'main'):
        r = soup.select(sel)
        if r:
            return r[0]
    return soup.body or soup


def collect(root):
    out, seen = [], set()
    for el in root.find_all(lambda t: isinstance(t, Tag) and t.name in COLLECT):
        p = el.parent
        skip = False
        while p is not None and isinstance(p, Tag):
            if p.name in COLLECT:
                skip = True
                break
            p = p.parent
        if skip:
            continue
        if id(el) not in seen:
            seen.add(id(el))
            out.append(el)
    return out


def text_with_slots(el, slots, counter):
    def walk(node):
        parts = []
        for c in node.children:
            if isinstance(c, NavigableString):
                parts.append(str(c))
            elif isinstance(c, Tag):
                if c.name in ('math', 'img', 'svg'):
                    name = f'SLOT_{counter[0]}'
                    counter[0] += 1
                    slots[name] = str(c)
                    parts.append(f'⟦{name}⟧')
                else:
                    parts.append(walk(c))
        return ''.join(parts)
    return re.sub(r'\s+', ' ', walk(el)).strip()


def plain_text(el, limit=None):
    t = re.sub(r'\s+', ' ', el.get_text(' ', strip=True)).strip()
    return t[:limit] if limit else t


def main(orig_path, outdir):
    soup = BeautifulSoup(open(orig_path, encoding='utf-8').read(), 'lxml')
    for t in soup.find_all(['script', 'style', 'noscript']):
        t.decompose()
    root = content_root(soup)

    blocks, counter = [], [0]
    for i, el in enumerate(collect(root)):
        bid = f'b{i:04d}'
        tag = el.name
        if tag in ('img', 'svg', 'math', 'picture', 'iframe', 'object'):
            blocks.append({'id': bid, 'kind': 'atomic', 'what': tag, 'html': str(el), 'preview': ''})
            continue
        if tag in ('table', 'pre') or in_keep(el):
            w = tag if tag in ('table', 'pre') else 'verbatim'
            blocks.append({'id': bid, 'kind': 'atomic', 'what': w, 'html': str(el),
                           'preview': plain_text(el, 200)})
            continue
        slots = {}
        en = text_with_slots(el, slots, counter)
        if not en and not slots:
            continue
        if not re.sub(r'⟦SLOT_\d+⟧', '', en).strip():
            blocks.append({'id': bid, 'kind': 'atomic', 'what': 'equation',
                           'html': str(el), 'preview': ''})
            continue
        blocks.append({'id': bid, 'kind': 'text', 'what': tag,
                       'html': str(el), 'slots': slots, 'en': en})

    os.makedirs(outdir, exist_ok=True)
    json.dump({'blocks': blocks}, open(os.path.join(outdir, 'blocks.json'), 'w'), ensure_ascii=False)
    tin = []
    for b in blocks:
        if b['kind'] == 'text':
            tin.append({'id': b['id'], 't': 'text', 'w': b['what'], 'en': b['en']})
        else:
            tin.append({'id': b['id'], 't': 'keep', 'w': b['what'], 'en': b.get('preview', '')[:200]})
    json.dump({'blocks': tin}, open(os.path.join(outdir, 'translate_input.json'), 'w'),
              ensure_ascii=False, indent=1)
    return (len(blocks), sum(1 for b in blocks if b['kind'] == 'text'),
            sum(len(b.get('slots', {})) for b in blocks if b['kind'] == 'text'),
            sum(1 for b in blocks if b['kind'] == 'atomic'))


if __name__ == '__main__':
    n, nt, ns, na = main(sys.argv[1], sys.argv[2])
    print(f'blocks={n} text={nt} slots={ns} atomic={na}')
