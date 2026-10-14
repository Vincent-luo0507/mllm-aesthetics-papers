#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge blocks.json + zh.json into a bilingual HTML (index.html), 04-bilingual.md
and the automated part of 06-self-check.md."""
import json, os, re, sys, html as H

HEAD = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{zh_title} | 双语对照</title>
<script>
window.MathJax={{
  tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']],processEscapes:true}},
  svg:{{fontCache:'global'}},
  options:{{skipHtmlTags:['script','noscript','style','textarea','pre','code']}}
}};
</script>
<script src="../../assets/mathjax/es5/tex-mml-chtml.js" async></script>
<style>
:root{{--fg:#1f2937;--pri:#1e3a8a;--bd:#e2e8f0;--alt:#f8fafc;}}
*{{box-sizing:border-box;}}
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
color:var(--fg);background:#fff;line-height:1.85;font-size:15.5px;}}
.wrap{{max-width:1500px;margin:0 auto;padding:0 20px 80px;}}
header.paperhead{{border-bottom:2px solid var(--pri);padding:24px 0 18px;margin-bottom:18px;}}
.zh-title{{font-size:25px;font-weight:700;color:var(--pri);line-height:1.35;margin:0 0 8px;}}
.en-title{{font-size:16px;color:#4b5563;line-height:1.5;margin:0 0 12px;font-style:italic;}}
.meta{{font-size:13px;color:#4b5563;display:flex;flex-wrap:wrap;gap:14px;}}
.meta a{{color:#2563eb;}}
.toolbar{{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.96);border-bottom:1px solid var(--bd);
padding:9px 0;display:flex;gap:8px;align-items:center;flex-wrap:wrap;backdrop-filter:blur(6px);}}
.toolbar button{{border:1px solid var(--bd);background:#fff;color:var(--pri);border-radius:5px;
padding:5px 13px;font-size:13px;cursor:pointer;font-family:inherit;}}
.toolbar button.on{{background:var(--pri);color:#fff;border-color:var(--pri);}}
.toolbar .sp{{flex:1;}}
.abs{{background:var(--alt);border:1px solid var(--bd);border-radius:6px;padding:14px 18px;margin:16px 0 24px;font-size:14.5px;}}
.abs h4{{margin:0 0 6px;font-size:14px;color:var(--pri);}}
.blk{{display:grid;grid-template-columns:1fr 1fr;gap:0;border-bottom:1px solid #f1f5f9;}}
.blk>div{{padding:10px 16px;}}
.blk>.en{{border-right:1px solid var(--bd);color:#334155;}}
.blk>.zh{{background:#fff;}}
.blk.atomic{{grid-template-columns:1fr;background:var(--alt);}}
.blk.atomic>div{{padding:12px 16px;text-align:center;}}
h1,h2,h3,h4{{color:var(--pri);line-height:1.45;}}
.blk h2{{font-size:19px;margin:16px 0 8px;}}
.blk h3{{font-size:16.5px;margin:12px 0 6px;}}
.blk h4{{font-size:15px;margin:10px 0 5px;}}
p{{margin:0 0 10px;text-align:justify;}}
img{{max-width:100%;height:auto;display:block;margin:10px auto;border:1px solid var(--bd);}}
table{{border-collapse:collapse;margin:10px auto;font-size:13.5px;background:#fff;}}
td,th{{border:1px solid #dbe2ea;padding:5px 9px;}}
figure{{margin:8px 0;}} figcaption{{font-size:13px;color:#4b5563;text-align:center;margin-top:6px;}}
body.view-zh .blk{{grid-template-columns:1fr;}} body.view-zh .blk>.en{{display:none;}}
body.view-en .blk{{grid-template-columns:1fr;}} body.view-en .blk>.zh{{display:none;}}
.mathwarn{{background:#fef2f2;border-left:4px solid #b91c1c;padding:8px 12px;font-size:13px;color:#7f1d1d;}}
</style>
</head><body class="view-both">
<div class="wrap">
<header class="paperhead">
<h1 class="zh-title">{zh_title}</h1>
<p class="en-title">{en_title}</p>
<div class="meta">{meta}</div>
</header>
<div class="toolbar">
<button data-v="view-both" class="on">中英双栏</button>
<button data-v="view-zh">仅中文</button>
<button data-v="view-en">仅英文</button>
<span class="sp"></span>
<a href="../00_index.html" style="font-size:13px;color:#2563eb;">← 返回总目录</a>
</div>
<div class="abs">
<h4>中文摘要</h4><div>{zh_abs}</div>
<h4 style="margin-top:10px;">Abstract (原文)</h4><div style="color:#475569;">{en_abs}</div>
</div>
<div id="body">
"""

TAIL = """
</div></div>
<script>
document.querySelectorAll('.toolbar button').forEach(function(b){{
  b.addEventListener('click',function(){{
    document.querySelectorAll('.toolbar button').forEach(function(x){{x.classList.remove('on');}});
    b.classList.add('on');
    document.body.className=b.dataset.v;
  }});
}});
</script>
</body></html>
"""

SLOT_RE = re.compile(r'⟦(SLOT_\d+)⟧')


def render_zh(b, zhmap):
    zh = zhmap.get(b['id'], {}).get('zh') if isinstance(zhmap.get(b['id']), dict) else zhmap.get(b['id'])
    if not zh:
        return None
    esc = H.escape(zh, quote=False)
    slots = b.get('slots', {})

    def sub(mo):
        return slots.get(mo.group(1), '')
    esc = SLOT_RE.sub(sub, esc)
    tag = b['what'] if b['what'] in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') else 'p'
    return f'<{tag}>{esc}</{tag}>'


def render_en(b):
    return b['html']


def main(pdir, meta):
    blocks = json.load(open(os.path.join(pdir, 'blocks.json')))['blocks']
    zhp = os.path.join(pdir, 'zh.json')
    zhmap = json.load(open(zhp)) if os.path.exists(zhp) else {}
    if 'blocks' in zhmap:
        zhmap = zhmap['blocks']

    # ---- stats
    text_blocks = [b for b in blocks if b['kind'] == 'text']
    atomic_blocks = [b for b in blocks if b['kind'] == 'atomic']
    missing = [b['id'] for b in text_blocks if not zhmap.get(b['id'])]
    slot_total = sum(len(b.get('slots', {})) for b in text_blocks)
    slot_restored = 0
    math_total = 0
    img_total = 0

    parts = []
    for b in blocks:
        if b['kind'] == 'atomic':
            if re.search(r'ltx_title_document|ltx_title_abstract|class="ltx_abstract"', b['html']):
                continue  # already shown in the page header (title + abstract)
            parts.append(f'<div class="blk atomic"><div>{b["html"]}</div></div>')
            continue
        zh_html = render_zh(b, zhmap)
        if zh_html is None:
            zh_html = '<p style="color:#b91c1c;">（本段缺失译文）</p>'
        else:
            slot_restored += len(b.get('slots', {}))
        parts.append(f'<div class="blk"><div class="en">{render_en(b)}</div>'
                     f'<div class="zh">{zh_html}</div></div>')

    body = '\n'.join(parts)
    zh_title = meta.get('zh_title') or meta['title']
    meta_html = ' · '.join(filter(None, [
        f'<span>arXiv:{meta["aid"]}</span>',
        f'<span>作者：{H.escape(meta.get("authors",""))}</span>',
        f'<span>发布：{meta.get("published","")}</span>',
        f'<a href="https://arxiv.org/abs/{meta["aid"]}" target="_blank">arXiv 页面</a>',
        '<a href="paper.pdf" target="_blank">原版 PDF</a>',
        '<a href="orig.html" target="_blank">原文 HTML</a>',
    ]))
    out = HEAD.format(zh_title=H.escape(zh_title), en_title=H.escape(meta['title']),
                      meta=meta_html,
                      zh_abs=H.escape(meta.get('zh_abstract', '')).replace('\n', '<br>'),
                      en_abs=H.escape(meta.get('abstract', ''))) + body + TAIL
    idx = os.path.join(pdir, 'index.html')
    open(idx, 'w', encoding='utf-8').write(out)

    # ---- 04-bilingual.md
    md = [f"# {zh_title}", "", f"> 原标题：{meta['title']}",
          f"> 作者：{meta.get('authors','')} · arXiv:{meta['aid']} · {meta.get('published','')}", ""]
    for b in blocks:
        if b['kind'] == 'atomic':
            md.append(f'<!-- [原子块 · {b["what"]}] {b.get("preview","")} -->')
            md.append('')
            continue
        z = zhmap.get(b['id'])
        zt = z.get('zh') if isinstance(z, dict) else z
        md.append(f'**EN** {b["en"]}')
        md.append('')
        md.append(f'**ZH** {zt if zt else "（缺失译文）"}')
        md.append('')
    open(os.path.join(pdir, '04-bilingual.md'), 'w', encoding='utf-8').write('\n'.join(md))

    # ---- 06-self-check.md (automated part)
    txt = open(idx, encoding='utf-8').read()
    figs_dir = os.path.join(pdir, 'figures')
    have = set(os.listdir(figs_dir)) if os.path.isdir(figs_dir) else set()
    refs = set(re.findall(r'src="figures/([^"]+)"', txt))
    missing_img = sorted(refs - have)
    mojibake = txt.count('\ufffd')
    stray = len(re.findall(r'⟦SLOT_\d+⟧', txt))
    nmath = len(re.findall(r'<math', txt))
    nimg = len(re.findall(r'<img', txt))
    ntbl = len(re.findall(r'<table', txt))
    report = f"""# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | {len(blocks)}（文本 {len(text_blocks)} / 原子 {len(atomic_blocks)}）|
| 已译文本块 | {len(text_blocks)-len(missing)} / {len(text_blocks)} |
| 缺失译文块 | {len(missing)} {('→ ' + ', '.join(missing[:20])) if missing else ''} |
| 内联公式/图片槽位 | 总数 {slot_total} · 已还原 {slot_restored} |
| `⟦SLOT⟧` 残留（应为 0）| {stray} |
| `<math>` 元素 | {nmath} |
| `<img>` 元素 | {nimg} |
| `<table>` 元素 | {ntbl} |
| 图片文件引用缺失 | {len(missing_img)} {('→ ' + ', '.join(missing_img[:10])) if missing_img else ''} |
| 乱码字符 U+FFFD（应为 0）| {mojibake} |
| 文件编码 | UTF-8 |

"""
    prev = ''
    p6 = os.path.join(pdir, '06-self-check.md')
    if os.path.exists(p6):
        prev = open(p6, encoding='utf-8').read()
        if '## 译者补充' in prev:
            prev = prev.split('## 译者补充', 1)[1]
            prev = '## 译者补充' + prev
        else:
            prev = ''
    open(p6, 'w', encoding='utf-8').write(report + prev)
    print(json.dumps({'blocks': len(blocks), 'missing': len(missing), 'math': nmath,
                      'img': nimg, 'table': ntbl, 'stray': stray,
                      'mojibake': mojibake, 'missing_img': len(missing_img)},
                     ensure_ascii=False))


if __name__ == '__main__':
    pdir = sys.argv[1]
    meta = json.load(open(sys.argv[2]))
    main(pdir, meta)
