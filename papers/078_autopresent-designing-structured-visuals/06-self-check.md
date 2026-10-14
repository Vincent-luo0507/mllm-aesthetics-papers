# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 240（文本 163 / 原子 77）|
| 已译文本块 | 163 / 163 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 22 · 已还原 22 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 45 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 13 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| structured visuals | 结构化视觉内容 | 全文统一 |
| presentation slide | 演示幻灯片 | |
| slide deck | 幻灯片组 | |
| natural language (NL) | 自然语言（NL） | 首次出现括注缩写 |
| NL-to-slide generation | 自然语言到幻灯片的生成 | |
| NL-to-code / program generation | 自然语言到代码 / 程序生成 | 与端到端图像生成对照 |
| reference-based metrics | 基于参考的指标 | |
| reference-free metrics | 无参考指标 | |
| executability / execution success rate | 可执行性 / 执行成功率 | |
| element matching | 元素匹配 | |
| content similarity | 内容相似度 | |
| color similarity | 颜色相似度 | |
| position similarity | 位置相似度 | |
| CIEDE2000 | CIEDE2000 | 色差公式名保留 |
| CLIP score | CLIP 分数 | |
| sentence-transformer | sentence-transformer | 库名保留 |
| intraclass correlation coefficient (ICC) | 组内相关系数（ICC） | |
| iterative refinement | 迭代精修 | 与 auto-refinement（自动精修）同源 |
| in-context examples | 上下文示例 | |
| few-shot examples | 少样本示例 | |
| visual programming | 视觉编程 | |
| end-to-end image generation | 端到端图像生成 | |
| Tesseract OCR | Tesseract OCR | 工具名保留 |
| paired t-test | 配对 t 检验 | |
| perceptual evaluation | 感知评测 | |
| canvas | 画布 | |
| large language model (LLM) | 大语言模型（LLM） | |
| vision-language model (VLM) | 视觉语言模型（VLM） | |
| LoRA | LoRA | 参数名保留 |

### 交叉验证记录（抽样 5 块）

| id | 原文要点 | 我的译文 | 语义一致性 |
|---|---|---|---|
| b0007 | SlidesBench 含 7⟦SLOT_0⟧ 训练 / 585 测试示例，源自 10 个领域 310 个幻灯片组；两类指标（基于参考考位置/内容/颜色，无参考考设计质量） | 四个数字与两类指标的定义完整译出，SLOT 占位符按序保留 | 一致，无漏译 |
| b0019 | 10 个领域；每领域全片满足 (i) 结构化布局 (ii) 可提取媒体才可入选；每领域 1 组入测试、其余入训练；共 10 + 300 组，每组平均 20 张；提供 URL 与退出机制 | 两项筛选条件、10/300/20 三个数字与版权处理措施全部保留 | 一致，数字核对无误 |
| b0058 | 程序平均 170 行 → 用 SlidesLib 降至 13 行；4 个基础函数 + 3 个图像函数；遵循视觉编程方法提供文档与两个上下文示例 | 170、13、4、3 四个数字原样保留，方法名与函数类别对应正确 | 一致 |
| b0092 | 小模型开箱即用几乎无法产出可用幻灯片；带图设定下差距 ⟦SLOT_10⟧–⟦SLOT_11⟧ 分，无视觉素材时缩小到 ⟦SLOT_12⟧–⟦SLOT_13⟧ | 两组区间均由 SLOT 承载，因果关系（获取图像是挑战）完整 | 一致 |
| b0118 | 局限：单页生成、单次产出完整代码、未用迭代式工作流；未来方向：整组幻灯片、渐进交互式生成、动画、更多设计原则 | 三点局限与四点方向逐条对应，未增删 | 一致，未添油加醋 |

### 一致性与数字核查

- 术语一致性：全文统一"结构化视觉内容""演示幻灯片""幻灯片组""基于参考/无参考指标""迭代精修""上下文示例"。模型名（AutoPresent、LlaMa、Llama 3.1、LlaVa、DeepseekCoder-7B-v1.5、CodeLlaMa-7B-Instruct、GPT-4o、gpt-4o-mini、Vicuna-7B-v1.5、Stable-Diffusion 2、DALL-E 3）、库名与函数名（SlidesLib、python-pptx、add_title、add_text、add_image、search_image、generate_image、match、all-MiniLM-L6-v2）、方法名（Design2Code、LoRA、Tesseract OCR）、数据集名（SlidesBench）全部原样保留。
- 数字核查：7⟦SLOT_n⟧（7k）、585、310、10、300、20、115.6/118.3/26.6（平均词数）、1.1/0.0/0.0（平均图像数）、170 行、13 行、4+3 个函数、25 与 16 份回答、1–5 与 0–5 量表、0–100 换算、36.3%/20.3%/13.5% 等均未作换算或改写；由 SLOT 承载的数值原样传递。
- 占位符完整性：163 个文本块的 `⟦SLOT_n⟧` 集合与原文逐块比对，零差异；构建脚本 stray = 0。初稿曾误在 b0102（表 5 说明）写入 `⟦SLOT_21⟧`，而该块原文为字面 "t-test"、并无占位符，已修正为"配对 t 检验"后重跑通过。
- 编码检查：`zh.json` 与 `index.html` 中均不含 U+FFFD。

### 遗留问题

- 无图片缺失（`missing_img = 0`），5 张 `<img>` 均指向已下载的 `figures/` 本地文件。
- b0006 与 b0008 原文 "as shown in ." 缺失图号，属原文引用空缺；译文统一作"如图所示"，未臆测具体图号。
- b0027 含原文编辑残留标记 `** *`，已按原文位置保留。
- b0049 含双脚注标记 `†† †`，已按原文位置内联保留，未单独拆块。
- b0218、b0220 等处原文 "down-weighted by the execution success rate" 与 "un-weighted" 在表题中并存，译文统一处理为"按执行成功率降权／未按执行成功率降权"，与 §E 正文表述一致。
- b0202 原文 "Figure 9shows" 缺空格、b0218 原文 "Table 8shows" 缺空格，属 PDF 抽取痕迹；译文按正常语句处理，未保留排版缺陷。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0120、b0228、b0114、b0077、b0084、b0038、b0118、b0216、b0098
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
