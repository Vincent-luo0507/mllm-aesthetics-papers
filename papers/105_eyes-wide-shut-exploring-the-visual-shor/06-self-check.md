# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 216（文本 121 / 原子 95）|
| 已译文本块 | 121 / 121 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 8 · 已还原 8 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 20 |
| `<img>` 元素 | 10 |
| `<table>` 元素 | 8 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 固定 |
| Contrastive Language-Image Pre-Training (CLIP) | 对比语言—图像预训练（CLIP） | 首次给出中文全称，后文用 CLIP |
| CLIP-blind pair | CLIP 盲对（CLIP-blind pair） | 核心概念，首次给出中英对照 |
| Multimodal Visual Patterns (MMVP) | 多模态视觉模式（MMVP） | 基准名 |
| MMVP-VLM | MMVP-VLM | 面向 CLIP 类模型的子基准，保留原名 |
| visual grounding | 视觉定位 | 全文统一，不作「视觉接地」 |
| visual encoder | 视觉编码器 | 固定 |
| vision-only self-supervised learning (SSL) | 纯视觉自监督学习（SSL） | 固定 |
| Mixture-of-Features (MoF) | 特征混合（MoF） | 首次给出中英对照 |
| Additive-MoF (A-MoF) | 加性 MoF（A-MoF） | 固定 |
| Interleaved-MoF (I-MoF) | 交错 MoF（I-MoF） | 固定 |
| instruction-following | 指令遵循 | 固定 |
| adapter | 适配器 | 固定 |
| visual token | 视觉词元 | 固定 |
| embedding / cosine similarity | 嵌入／余弦相似度 | 固定 |
| Visual Question Answering (VQA) | 视觉问答（VQA） | 固定 |
| visual pattern | 视觉模式 | 九类模式的统称 |
| Orientation and Direction | 朝向与方向 | 九类模式之一，附录 D 与表 1 统一 |
| Presence of Specific Features | 特定特征的有无 | 同上 |
| State and Condition | 状态与状况 | 同上 |
| Quantity and Count | 数量与计数 | 同上 |
| Positional and Relational Context | 位置与关系语境 | 同上 |
| Color and Appearance | 颜色与外观 | 同上 |
| Structural and Physical Characteristics | 结构与物理特征 | 同上 |
| Text | 文字 | 同上 |
| Viewpoint and Perspective | 视角与透视 | 同上 |
| Pearson Correlation Coefficient | 皮尔逊相关系数 | 固定 |
| zero-shot | 零样本 | 固定 |
| linear probing | 线性探测 | 固定 |
| random guessing | 随机猜测 | 固定 |
| hallucination | 幻觉 | 固定 |
| POPE / MM-Bench / MMBench / GQA / MM-Vet | 保留原名 | 基准名一律不译 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 结论 |
|---|---|---|---|
| b0010 | CLIP 盲对定义：CLIP 嵌入相似而 DINOv2 嵌入不同的图像对；DINOv2 作为纯视觉自监督参照 | 定义、动机（至少一张编码含混）与参照模型作用完整译出 | 语义一致，无增补 |
| b0021 | 阈值：CLIP 余弦相似度 > 0.95，DINOv2 < 0.6；模型名 CLIP-ViT-L-14、DINOv2-ViT-L-14 | 两个阈值与两个模型名原样保留，比较方向（超过／低于）准确 | 数字与条件零改动 |
| b0068 | DINOv2 比例超过 0.75 后优势减弱，且指令遵循明显受损 | 数值 0.75 与两层转折关系完整保留 | 数字与逻辑一致 |
| b0076 | MMVP 提升 10.7%；POPE、MM-Bench、GQA 上的验证；分辨率提升无用、交错才有效 | 10.7% 原样保留，四个基准名保留，因果对照（不是…而是…）按原文语义改写为直陈 | 数字与结论一致 |
| b0175 | 选项交换实验 40.3% vs. 原始 38.7%，说明问题出在视觉编码器而非对齐或 LLM | 两个数值与推论完整保留 | 数字与语义一致 |

### 一致性与数字核查

- **术语统一**：对 `zh.json` 全文检索确认，「视觉定位」「CLIP 盲对」「特征混合」「加性 MoF／交错 MoF」「纯视觉自监督学习」「指令遵循」「视觉模式」等核心术语在正文、图表说明与附录中译法完全一致，未出现同义词轮换（例如未混用「视觉定位」与「视觉对齐」、「视觉编码器」与「视觉骨干」）。
- **占位符完整性**：逐块比对原文与译文的 `⟦SLOT_n⟧` 集合，8 个槽位（SLOT_0～SLOT_7）数量、编号与顺序全部一致；构建脚本 `stray = 0` 印证。
- **数字与指标**：150、300、95.7%、25%、50%、9 类模式、7/9、0.95、0.6、15 个文本—图像对、0.7、87.5%、0.75、10.7%、40.3%、38.7%、37.3%、80、8 块 A100、Vicuna-13b-v1.3／v1.5、CC595k、158k、665k、224²、336²、256/576/512 词元等全部原样保留；MMVP、MMVP-VLM、POPE、MM-Bench、MMBench、GQA、MM-Vet、TextVQA、VQAv2、ImageNet-1k、LAION-Aesthetics、CLIP-ViT-L-14、DINOv2-ViT-L-14、EVA01 ViT-g-14、MAE、MoCoV3、SLIP、Pearson Correlation 等模型名、基准名与指标名一律保留原名。
- **编码检查**：`zh.json` 与 `index.html` 均不含 U+FFFD，构建脚本 `mojibake = 0`。
- **不变量**：表格（8）、代码块、公式（20 个 `<math>`）、图片（10）与参考文献块均为 `t:"keep"`，未翻译；121 个文本块严格一一对应，无合并、拆分或删减。

### 遗留问题

- 无图片缺失（`missing_img = 0`），10 张图片均已在 `figures/` 中命中。
- b0044（九类视觉模式表）与 b0047（表 1 的符号说明）中的模式名以符号占位，译文沿用原文的符号体系，并在表 1 说明中按原文顺序对应九类模式。
- b0168 中「mini-GPT4 [71]、11 1 为规避 mini-GPT4 的回答幻觉，我们在问题前加上前缀……」为脚注插入导致的断句错乱，译文按字面保留。
- b0035 原文末句「struggle with visual details」缺主语，译文补出「模型」以符合中文语法，未改变原意。
- b0079 中 Bard 的引用标为 [30]（应为 [13]），属原文引用编号问题，译文未作改动。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽样 6 块（b0027、b0194、b0056、b0009、b0186、b0020）语义、数字、术语均无误。另对全文做了脚注残留扫描，发现并修正 1 处：

| 块 ID | 问题类型 | 修正前 → 修正后 |
|---|---|---|
| b0168 | 脚注标记残留（且句子被截断） | `访问 mini-GPT4 [71]、11 1 为规避 mini-GPT4 的回答幻觉，…「请只选择一个选项回答下列问题，不要解释：」 LLaVA 与 LLaVA-1.5 [31]。` → `访问 mini-GPT4 [71]、LLaVA 与 LLaVA-1.5 [31]（为规避 mini-GPT4 的回答幻觉，…「请只选择一个选项回答下列问题，不要解释：」）。`|

修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
