# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 227（文本 131 / 原子 96）|
| 已译文本块 | 131 / 131 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 2 · 已还原 2 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 173 |
| `<img>` 元素 | 12 |
| `<table>` 元素 | 13 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| low-level visual perception / understanding | 底层视觉感知 / 理解 | 与 high-level（高层）严格对应 |
| low-level visual attribute | 底层视觉属性 | 如噪声、模糊、清晰度 |
| low-level visual dimension | 底层视觉维度 | 如色彩、亮度 |
| image quality assessment (IQA) | 图像质量评价（IQA） | 首次出现括注缩写 |
| multi-modality large language model (MLLM) | 多模态大语言模型（MLLM） | |
| foundation model | 基座模型 | 未与“基础模型”混用 |
| instruction tuning | 指令微调 | |
| pathway feedback | pathway 反馈 | 作者定义的专有标注格式，保留 pathway |
| human subject | 受试者 | 主观实验参与者；与“参与者”（participant）分用 |
| subjective study | 主观实验 | |
| mean opinion score (MOS) | 平均意见分（MOS） | |
| visual question answering (VQA) | 视觉问答（VQA） | |
| multi-choice question (MCQ) | 多选题（MCQ） | |
| extended conversation | 扩展对话 | Q-Instruct 第三子集 |
| distortion | 失真 | 与 artifact（伪影）区分 |
| in-the-wild | 真实场景（in-the-wild） | 首次出现括注英文 |
| image captioning | 图像描述 | |
| mix strategy / after strategy | 混合策略 / 后置策略 | 第 5 节两种训练策略 |
| high-level awareness | 高层认知 | |
| joint training | 联合训练 | 与 task-separate tuning（分任务微调）对照 |
| softmax pooling | softmax 池化 | |
| SRCC / PLCC | SRCC / PLCC | 指标名保留 |
| greedy search | 贪心搜索 | |
| visual backbone | 视觉骨干 | |
| wordcloud | 词云 | |

### 交叉验证记录（抽样 5 块）

| id | 原文要点 | 我的译文 | 语义一致性 |
|---|---|---|---|
| b0012 | 每条反馈两部分：详细的底层属性描述（含内容/位置上下文）+ 总体质量结论；Q-Pathway 含 18,973 张图上 58K 条反馈，每图至少三条，平均 46.4 词 | 两部分结构与四个数字全部保留，"pathway 反馈"命名沿用 | 一致，无漏译 |
| b0031 | 图像来源：4 个真实场景 IQA 数据集 + 2 个 AI 生成图像数据集；imagecorruptions 变体随机破坏 COCO 中 1,012 张图，15 种失真；共 18,973 张 | 数据集数量、1,012、15、18,973 全部原样保留 | 一致，数字核对无误 |
| b0045 | GPT 参与流水线把反馈转为 76K 问题（how 用观点形容词、what 用属性/上下文名词）；57K 是非问题平衡到 1:1；沿用 A-OKVQA 构造 MCQ 干扰项 | 76K、57K、1:1 与三类问题形式的区分完整译出，粉色框提示保留 | 一致，未添油加醋 |
| b0075 | softmax 池化抽质量分；"mostly seen" 上表现优秀且训练未用 MOS 数值；"never seen" 三数据集 [66, 13, 28] 上 +0.243 平均 SRCC 增益 | +0.243 与三个数据集编号保留，"数值监督""域差异"的表述与原文一致 | 一致 |
| b0221 | 三项局限：通用任务性能下降；68%–71% 对普通人类约 74%；数据集以自然真实场景图像为主 | 三组数字（68%–71%、74%）与三点局限逐条对应，未遗漏 | 一致 |

### 一致性与数字核查

- 术语一致性：全文统一“底层视觉”（未出现“低层/低级视觉”）、“基座模型”（未出现“基础模型”）、“图像质量评价（IQA）”、“pathway 反馈”、“受试者”。模型名（LLaVA-v1.5、mPLUG-Owl-2、InternLM-XComposer-VL、GPT-4V、GPT-4、CLIP、NIQE、Vicuna、LLaMA-2）、数据集名（Q-Pathway、Q-Instruct、COCO、COCO-VQA、A-OKVQA、KoNViD-1k、LLVisionQA-dev/test）、指标名（SRCC、PLCC、MOS）全部原样保留。
- 数字核查：58K、200K、18,973、46.4 词、20–100 词、39 名受试者、30/50 张疲劳阈值、1,012 张、15 种失真、76K、57K、12K、+0.31/+0.17/+0.04、+0.243、68%–71%、约 74%、A100 卡数（8/32）与训练时长（16/22/8/13 小时）等均未作换算或改写。
- 占位符完整性：131 个文本块的 `⟦SLOT_n⟧` 集合与原文逐块比对，零差异；构建脚本 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 中均不含 U+FFFD；附录中的 `<image>`、`<QUESTION>`、`<CHOICEA>`、`$DESC` 等提示模板标记在生成页面中已正确转义，未破坏结构。

### 遗留问题

- 无图片缺失（`missing_img = 0`），12 张 `<img>` 均指向已下载的 `figures/` 本地文件。
- b0039 中原文含脚注标记 `†† ... Fig. 3(d).`，属 PDF 抽取残留，已按原文位置保留，未单独拆为脚注块。
- b0171、b0174、b0177 为 GPT 提示词原文，属可直接复用的模板文本；翻译后仅作阅读参考，实际使用时仍应以英文原模板为准，已在译文中保留 `$DESC` 等占位变量与 JSON 键名。
- b0200、b0202、b0204 为各模型的推理提示模板，其中 `USER:`、`ASSISTANT:`、`<|User|>`、`<|Bot|>` 等控制标记原样保留未译。
- 原文 Fig. 2 处写作 `Q-pathway`（小写 p），正文一律写作 `Q-Pathway`；译文统一为 “Q-Pathway”，未区分大小写差异。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0023、b0010、b0065、b0198、b0168、b0189），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
