# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 161（文本 85 / 原子 76）|
| 已译文本块 | 85 / 85 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 0 · 已还原 0 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 0 |
| `<img>` 元素 | 10 |
| `<table>` 元素 | 3 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Large Multimodal Model (LMM) | 大多模态模型（LMM） | 本文统一用 LMM，与 LLM 对应 |
| Large Language Model (LLM) | 大语言模型（LLM） | — |
| artwork analysis | 艺术品分析 | — |
| formal analysis | 形式分析 | 艺术史专用术语，不作"格式分析" |
| PaintingForm | 同名保留 | 本文提出的数据集 |
| LLM-biased visual hallucination | LLM 偏置的视觉幻觉 | 本文核心概念，保留引号 |
| recognize-then-analyze | 先识别再分析 | 现有 LMM 的失效流程 |
| nameless painting | 无名画作 | 用于避免知识记忆的测试对象 |
| composition | 构图 | 形式分析视角之一 |
| color palette | 配色 | 形式分析视角之一 |
| line quality | 线条质量 | 形式分析视角之一 |
| texture | 质感 | 形式分析视角之一 |
| light and shadow | 光影 | 形式分析视角之一 |
| perspective | 透视 | 形式分析视角之一 |
| form and shape | 形态与形状 | 形式分析视角之一 |
| movement and gesture | 动态与姿态 | 形式分析视角之一 |
| symbolism and iconography | 象征与图像志 | 形式分析视角之一 |
| scale and proportion | 尺度与比例 | 形式分析视角之一 |
| Supervised Fine-Tuning (SFT) | 监督微调（SFT） | — |
| LoRA | LoRA | 保留原名 |
| vision encoder / projector | 视觉编码器 / 投影器 | 模型三组件之二 |
| decoder-only | 仅解码器 | LLM 架构 |
| zero-shot | 零样本 | 下游任务设定 |
| art visual question answering | 艺术视觉问答 | 下游任务 |
| style classification | 风格分类 | 下游任务 |
| SoTA-1 / SoTA-2 | 最先进方法（SoTA-1 / SoTA-2） | 分别表示无 / 有 PLM |
| Pre-trained Language Model (PLM) | 预训练语言模型（PLM） | — |
| AQUA / ArtQuest / ArtQuest-Type / ArtBench / SemArt | 同名保留 | 数据集名 |
| ShareGPT4V / LLaVA / Qwen-VL / GPT-4V / Gemini | 同名保留 | 模型名 |
| image captioning metrics | 图像描述指标 | 形式分析的评测方式 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0028 | 过滤掉 769 幅、保留 18,026 幅；约 150 位艺术家仅一幅画作 | 三个数字与说明原样保留 | 一致 |
| b0036 | 19,295 幅（含 18,795）；过滤后 18,526；测试 5000、训练 13,526；Van Gogh 保留 1458、过滤 225；David 约 100 幅 | 六个数字与艺术家姓名原样保留，版权声明照译 | 一致 |
| b0042 | 输入 336*336，划分 14 个块，得到 576 个输入词元；两层 MLP 投影器 | 三个数字原样保留 | 一致 |
| b0044 | 学习率 2e-5、批量 16、10k 步、80G A100；LoRA 秩 128、alpha 256 | 六个超参数原样保留 | 一致 |
| b0056 | AQUA 训练/验证/测试为 29,568、1,507、1,270；ArtQuest 6414；ArtQuest-Type 1069；ArtBench 采样 1000（共 10000） | 七个数字原样保留 | 一致 |

### 一致性与数字核查

- 术语统一性：`formal analysis` 全文统一为"形式分析"；`LMM` 统一为"大多模态模型"，未与"多模态大语言模型"混用；`painting` 视语境分别作"画作"与"绘画"，在同一语境内保持一致；形式分析十类视角（构图、配色等）在 b0140 与正文 b0038 中译法完全对应。
- 数字核查：19k/50k、19,295/18,795/18,526、5000/13,526、769/18,026、1458/225、48、8、336*336、14、576、2e-5、16、10k、80G、128、256、29,568/1,507/1,270、6414、1069、1000/10000 等数值全部逐字核对，未做换算。
- 占位符核查：本论文 `translate_input.json` 的 text 块中不含 `⟦SLOT_n⟧` 占位符，构建脚本报告 stray = 0，与预期一致。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、算法与图像块按规范跳过未译；参考文献块未译。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文 b0073 首句"with large multimodal models (LLMs)"疑为笔误（括号中应为 LMMs），译文按字面译为"大多模态模型（LLM）"以保留原文表述。
- 原文 b0069 "inncluding"、b0032 "of-the-shelf"、b0036 "easily to accessed"等拼写笔误，译文按语义处理，不影响内容。
- 原文多处脚注以行内"11 1 …"形式嵌入正文，译文统一改写为"（脚注 N：…）"，未删减脚注内容。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0158、b0152、b0140、b0073、b0018、b0022、b0013、b0069、b0056、b0011
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
