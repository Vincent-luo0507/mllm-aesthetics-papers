# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 383（文本 217 / 原子 166）|
| 已译文本块 | 217 / 217 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 94 · 已还原 94 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 207 |
| `<img>` 元素 | 77 |
| `<table>` 元素 | 13 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Vision-Language Model (VLM) | 视觉语言模型 | 首现保留缩写 VLM |
| Color Perception | 颜色感知 | 三大核心维度之一 |
| Color Reasoning | 颜色推理 | |
| Color Robustness | 颜色鲁棒性 | |
| Color Recognition (C'Recog) | 颜色识别 | 任务名，保留缩写 |
| Color Extraction (C'Extra) | 颜色提取 | |
| Object Recognition (O'Recog) | 物体识别 | |
| Color Proportion (C'Prop) | 颜色占比 | |
| Color Comparison (C'Comp) | 颜色比较 | |
| Color Counting (C'Count) | 颜色计数 | |
| Object Counting (O'Count) | 物体计数 | |
| Color Illusion (C'Illu) | 颜色错觉 | |
| Color Mimicry (C'Mimic) | 颜色拟态 | 伪装色的误导作用 |
| Color Blindness (C'Blind) | 色盲 | 受石原测试启发 |
| scaling law | 缩放定律 | |
| vision encoder | 视觉编码器 | |
| language model | 语言模型 | 与 LLM 同义，统一译法 |
| Chain of Thought (CoT) | 思维链（CoT） | 首现给出中文，后文用 CoT |
| slow thinking | 慢思考 | |
| hue / saturation / value | 色相 / 饱和度 / 明度 | HSV 三通道 |
| recoloring | 重着色 | |
| seed image | 种子图像 | |
| segment | 分割区域 | GAM 提取所得 |
| Grounded Segmentation Model (GAM) | Grounded Segmentation Model（GAM） | 保留模型原名 |
| Ishihara test | 石原测试 | 色盲检测图 |
| grayscale | 灰度 | |
| Spearman's rank correlation | Spearman 秩相关 | 保留专名 |
| p-value | p 值 | |
| violin plot / heatmap / scatter plot | 小提琴图 / 热图 / 散点图 | |
| attention map | 注意力图 | |
| instance-level / model-level robustness | 实例级 / 模型级鲁棒性 | |
| LoRA | LoRA | 不译 |
| ablation | 消融 | |
| proprietary / open-source | 闭源 / 开源 | |
| P&R Overall | P&R 总体 | 保留缩写 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0018 | ⟦SLOT_5⟧ 个实例、⟦SLOT_6⟧ 道图文问题、⟦SLOT_7⟧ 个任务；鲁棒性每例 10 题（1 张种子图 + 9 张编辑图） | 数量与构成逐项照录，含 1+9=10 的说明 | 一致 |
| b0049 | C'Prop 最佳仅 ⟦SLOT_51⟧；C'Count 领先第二名 ⟦SLOT_52⟧ 个百分点；O'Count 唯一超 ⟦SLOT_54⟧；C'Illu 落在 ⟦SLOT_55⟧–⟦SLOT_56⟧ | 十个任务缩写与全部数值均保留，未改量纲 | 一致 |
| b0050 | 仅 ⟦SLOT_59⟧ 个模型超 ⟦SLOT_60⟧；InternViT-6B 对比 300–400M；GPT-4o ⟦SLOT_61⟧、Gemini-2 ⟦SLOT_62⟧ | 模型名单、编码器规模与四个数值全部保留 | 一致 |
| b0142 | 色相偏移 ⟦SLOT_87⟧°/⟦SLOT_88⟧°/⟦SLOT_89⟧°；每图 9 个变体；最终 493 张种子图像 | 角度、变体数与筛选后数量均照录 | 一致 |
| b0181 | 人类在多数任务最高，仅 O'Recog、C'Prop、C'Comp 被 GPT-o3 超越；差距小于 ⟦SLOT_91⟧、优势超 ⟦SLOT_92⟧ | 三个任务名与两个数值对应一致 | 一致 |

### 一致性与数字核查

- 术语统一：Grep 复核"颜色感知""颜色推理""颜色鲁棒性""视觉编码器""重着色""种子图像""思维链"在 zh.json 中用法唯一；11 个任务名全文统一（如 Color Extraction 一律"颜色提取"，未混入"色彩抽取"）；`proprietary` 一律译"闭源"，与 `open-source`（开源）对应。
- 数字核查：1,400 余、11、3、32、10、9、493、300–400M、InternViT-6B、70B、A100 80GB×1/×4、50、3、2025-04-16、[0,360] 之外的色相偏移角度，以及 SLOT_50～SLOT_93 所涵盖的全部准确率数值，均原样保留；任务缩写 C'Recog、C'Extra、O'Recog、C'Prop、C'Comp、C'Count、O'Count、C'Illu、C'Mimic、C'Blind、C'Robust 与 P&R Overall 均未改写。
- 占位符完整性：脚本逐块比对 `⟦SLOT_n⟧` 序列（含 SLOT_0～SLOT_93），217 个文本块全部一致，输出 slot mismatch: []；其中 b0037、b0038 初稿占位符顺序与原文有出入，已按原文序列重排后重新校验通过。
- 编码检查：zh.json 与 index.html 中不含 U+FFFD（构建脚本 mojibake=0）。

### 遗留问题

- 原文 b0067 写作"recognize these digits in a button-up pattern"，疑为"bottom-up pattern"笔误，按语义译为"以自底向上的方式识别这些数字"，未改动源文件。
- 原文 b0047 脚注标记与正文粘连（"perform the best11 1 To examine..."），按语义断句处理，未改动源文件。
- 原文 b0233（"Figure 27 to 35"）与其前后图注编号（Figure 26 起）存在轻微不一致，按原文照译，未改动源文件。
- 图片文件全部齐备（missing_img=0）。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0060, b0141, b0267, b0209, b0032, b0182 / b0172, b0050, b0334, b0006, b0060, b0030
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| zh_abstract（meta.json） | 漏译整句（未修正） | EN 摘要末句「Our ColorBench can serve as a foundational tool for advancing the study of human-level color understanding of multimodal AI.」在中文摘要中缺失，ZH 止于「……并强调提升颜色理解能力的必要性。」 | 属摘要漏译，应补「我们的 ColorBench 可作为推进多模态 AI 人类级颜色理解研究的基础工具。」；因中文摘要位于 meta.json（规格书 §C 禁改），未直接改写，在此登记待译者补入。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
