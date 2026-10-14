# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 222（文本 138 / 原子 84）|
| 已译文本块 | 138 / 138 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 103 · 已还原 103 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 225 |
| `<img>` 元素 | 22 |
| `<table>` 元素 | 6 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| visual preference | 视觉偏好 | 全文统一 |
| personalization | 个性化 | |
| visual attribute | 视觉属性 | 20 个类别下的属性词 |
| free-form comments | 自由形式评论 | 指用户不受结构约束的文字评论 |
| Visual Preference Extractor | 视觉偏好提取器 | 微调后的 IDEFICS2-8b |
| agent (simulated individual) | 智能体（即模拟个体） | 首次出现附解释 |
| proxy metric / proxy measure | 代理指标 / 代理度量 | 评价个性化程度的自动指标 |
| text-to-image model | 文本到图像模型 | |
| prompt embedding | 提示词嵌入 | |
| classifier-free guidance | 无分类器引导 | |
| guidance scale | 引导尺度 | |
| personalization degree | 个性化程度 | |
| cross-entropy loss | 交叉熵损失 | |
| Jaccard distance | Jaccard 距离 | |
| identifiability test | 可辨识性检验 | |
| top-one accuracy | top-1 准确率 | |
| confusion matrix | 混淆矩阵 | |
| reward hacking | 奖励黑客 | 括号附原文 reward-hacking |
| denoising U-Net | 去噪 U-Net | |
| Textual Inversion | Textual Inversion | 基线方法名保留 |
| ZO-RankSGD / FABRIC / PickScore | 保留原名 | 基线方法与指标名 |
| Stable Diffusion / Stable Diffusion XL | 保留原名 | |
| IDEFICS2-8b / IDEFICS1-80b / LLaVA / InstructBLIP / GPT-4 / Llama 2 | 保留原名 | 模型名 |
| NSFW | NSFW | 保留原文 |
| seed | 随机种子 | |
| ViPer | 保留原名 | 方法名 |

### 交叉验证记录（随机抽 5 块）

| id | 原文要点 | 我的译文 | 一致性结论 |
|---|---|---|---|
| b0011 | 用评论捕捉通用视觉偏好；转成含视觉属性的结构化表示；无需额外微调即可条件约束 Stable Diffusion | 同上中文表述 | 一致；示例属性列表（超现实、粗犷笔触、单色调）逐项对应 |
| b0025 | 5000 个智能体；平均 50 个喜欢/不喜欢属性；Jaccard 距离最小 85% | 同上中文表述 | 一致；三个数字原样保留 |
| b0063 | Top-1～Top-4 准确率表：86.1/86.7/65.4/71.6/12.5 等 20 个数值 | 同上中文表述 | 一致；20 个数字逐一核对无改动，表头字段名保留英文 |
| b0167 | 1000 个智能体；ViPer vs Prompt Personalization；CLIP 相似度与 PickScore；两段小标题 | 同上中文表述 | 一致；含 4 个槽位，顺序与原文一致 |
| b0206 | 输入图像 0～28 张；100 个智能体；约 18 张后稳定在约 91.1% | 同上中文表述 | 一致；三个数字与百分比未改动 |

### 一致性与数字核查

- 术语统一性：Grep 复核 zh.json，「视觉偏好」「个性化」「视觉属性」「智能体」「代理指标」「提示词嵌入」「无分类器引导」等核心术语全文译法唯一；「评论」不写作「反馈」以免与基线方法中的 feedback 混淆。
- 数字与指标：50、5000、500、20、2000、10、1000、100、8、20、15、12～15、0.2、0～28、0～1、86.1%、86.7%、65.4%、71.6%、12.5%、93.2%、95.8%、82.2%、89.2%、25.0%、98.6%、100.0%、96.6%、98.3%、37.5%、99.0%、99.2%、50.0%、6.89 倍、5.23 倍、91.1%、85%、77 词元 等全部逐位保留；top-1 至 top-4、Rank 1～8、User's Pers. vs No Pers 等记法原样。
- 占位符完整性：138 个文本块的 `⟦SLOT_n⟧` 序列与原文完全一致（mismatch 列表为空），构建脚本 stray=0。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD 乱码字符，编码为 UTF-8。

### 遗留问题

1. 原文 b0023 的 “（see for examples.）” 与 b0024/b0147/b0195 的 “See page for the complete list.” 均为失效的 LaTeX 交叉引用，无具体目标；译文以「（示例见）」「见对应页面」等对等方式处理，未臆造章节号。
2. 表 6（b0221）与 b0177/b0178 的属性名构成受控词表，译文按中文译出，但同一属性在不同块中出现时可能存在个别译法差异（如 Realism 统一为「写实主义」），已在术语表层面保持一致。
3. b0160 与 b0161 中“第 68 行第 69 列”等以槽位表示的矩阵下标无法核验具体数值，译文严格按槽位顺序呈现，未作推测。
4. 图片缺失 0，figures/ 资源齐全。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0024、b0056、b0029、b0185、b0084、b0012、b0057、b0070、b0221、b0206
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
