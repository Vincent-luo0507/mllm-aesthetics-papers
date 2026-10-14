# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 266（文本 196 / 原子 70）|
| 已译文本块 | 196 / 196 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 69 · 已还原 69 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 138 |
| `<img>` 元素 | 10 |
| `<table>` 元素 | 0 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Visual Minimal-Change Understanding (VisMin) | 视觉最小改动理解（VisMin） | 基准名，首次出现括注英文 |
| vision-language model (VLM) | 视觉—语言模型（VLM） | |
| foundational VLM | 基座型 VLM | 指 CLIP、SigLip、BLIP、Coca 一类对比式模型 |
| multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | 与「基座型 VLM」对举 |
| minimal change | 最小改动 | 全文统一，不轮换为「最小变化」 |
| hard negative | 难负例 | |
| visual hard negative | 视觉难负例 | |
| image-caption match / image-text matching | 图文匹配 | |
| text score / image score / group score | 文本分数 / 图像分数 / 分组分数 | 沿用 Winoground 的 T/I/G 记法 |
| spatial relation | 空间关系 | |
| counting / count | 计数 | |
| attribute | 属性 | |
| edit instruction | 编辑指令 | |
| source caption / edited caption | 源描述 / 编辑后描述 | caption 在此语境统一译「描述」 |
| bounding box | 边界框 | |
| inpainting | 修复 | 指 SDXL 修复模型 |
| layout-based diffusion model | 基于布局的扩散模型 | 指 LMD、GLIGEN |
| end-to-end diffusion model | 端到端扩散模型 | 指 Stable Diffusion |
| photo-realism | 照片真实感 | |
| visual question answering (VQA) | 视觉问答（VQA） | |
| annotator | 标注者 | |
| acceptance rate | 接受率 | |
| Amazon Mechanical Turk (AMT) | Amazon Mechanical Turk（AMT） | 平台名保留 |
| out-of-distribution (OOD) | 分布外（OOD） | |
| zero-shot | 零样本 | |
| QLoRA / LoRa | QLoRA / LoRa | 保留专名 |
| perceiver resampler | perceiver 重采样器 | |
| cosine similarity | 余弦相似度 | |
| ground truth | 真值 | |
| downsample | 下采样 | |

### 交叉验证记录（随机抽样 5 块）

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0021 | LLM（Mistral 47B）生成编辑指令与编辑后描述；COCO/VSR 人工描述作源；每条源生成 5 条；过滤剔除 ⟦SLOT_0⟧；计数与空间关系用合成源描述与规则法；边界框示例 | 各步骤与全部占位符（SLOT_0~5）原样保留，示例描述照译 | 语义、数量与占位符一致 |
| b0024 | 四步人工验证，每步需 5 人中 4 人一致；四步接受率 26%/80%/84%/95% | 四条标准与四个接受率数值逐项对应 | 数字完全一致，未四舍五入 |
| b0026 | 训练集 64,392（37,017/10,352/10,050/6,973），基准 2,084（579/294/589/622）；COCO 2017 训练 118K、验证 5K | 全部数值原样保留 | 数字一致 |
| b0048 | CLIP 小批次构成、加入难负例后的形式、128 总批大小、OpenCLIP 默认超参、训练轮数 | 超参以占位符 SLOT_13~25 保留，说明文字照译 | 占位符与描述一致 |
| b0230 | NeurIPS 检查清单第 8 条指南：计算节点类型、内存与存储、单次与总计算量、是否超出论文报告 | 三条指南逐条对应译出 | 结构与语义一致 |

### 一致性与数字核查

- 术语统一性：用 Grep 复核「视觉—语言模型（VLM）」「基座型 VLM」「多模态大语言模型（MLLM）」「最小改动」「难负例」「图文匹配」「文本分数/图像分数/分组分数」「空间关系」「计数」「属性」等核心术语，确认全文译法唯一；NeurIPS 检查清单中的「[Yes]/[No]/[N/A]」「Guidelines」「Justification」分别统一译为「答案」「指南」「理由」。
- 数字核查：数据集规模（64,392 / 2,084 / 118K / 5K / 65k / 16k / 6.5 万 / 1.6 万）、各基准规模（400 / 150 / 3,000 / 2,306 / 1,232 / 250,612 / 45,400）、参数量（149.62M / 427.62M）与接受率（26% / 80% / 84% / 95% 等）均逐项比对原文，未做任何换算或改写；表内数值属代码块内容，一律照抄未译。
- 占位符完整性：69 个 ⟦SLOT_n⟧ 槽位在译文中数量与编号与原文完全一致。
- 编码检查：zh.json 与 index.html 中 U+FFFD 计数均为 0。

### 遗留问题

- 块 b0052 原文末有一个孤立的字母「W」（疑为句子起始残字），源文件本身即如此；译文保留该字母未作补写，未修改源文件。
- 块 b0032（表 1 正文）原文中「VisMin（Ours）」在 HTML 抽取后呈现为「VisMin (Ours)」，其中括号已含中文排版，译文按「VisMin（ ours）」处理以贴合源文本形态。
- 原文在 b0029 中引用「Appendix15」「Appendix 13」等（编号与章节名粘连），属原文排版问题，译文按原文顺序直译，未做修正。
- 提示模板（b0037 中的英文提示、b0140 的模板示例）按原文保留英文，未翻译，以免改变指令语义。



## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0205、b0021、b0202、b0189、b0008、b0220、b0192、b0250、b0230、b0212
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
