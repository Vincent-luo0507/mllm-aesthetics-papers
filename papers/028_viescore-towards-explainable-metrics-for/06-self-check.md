# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 234（文本 124 / 原子 110）|
| 已译文本块 | 124 / 124 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 14 · 已还原 14 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 143 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| conditional image synthesis | 条件图像合成 | 含生成与编辑两大类 |
| VIEScore (Visual Instruction-guided Explainable Score) | VIEScore（视觉指令引导的可解释评分） | 首次出现给出全称 |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 全文统一 |
| Semantic Consistency (SC) | 语义一致性（SC） | 两大评分方面之一 |
| Perceptual Quality (PQ) | 感知质量（PQ） | 两大评分方面之一 |
| Overall (O) | 总体（O） | 由 SC 与 PQ 的几何平均得到 |
| rationale | 评判理由 | 不译作"推理过程"，与分数相对 |
| sub-score | 子分数 | SC/PQ 拆分后的细项 |
| Metric-to-Human (M-H) correlation | 指标—人类（M-H）相关性 | 与 H-H 对应 |
| Human-to-Human (H-H) correlation | 人类—人类（H-H）相关性 | 人类一致性上界 |
| In-Context Learning (ICL) | 上下文学习（ICL） | 保留缩写 |
| Fisher Z-transformation | Fisher Z 变换 | 相关性平均方法 |
| Spearman's footrule / rho | 斯皮尔曼 footrule 距离 / rho | 排序相关性指标 |
| Krippendorff's alpha | Krippendorff's alpha | 评分者间一致性，不译 |
| subject-driven | 主体驱动 | 任务类别名 |
| multi-concept image composition | 多概念图像组合 | 任务类别名 |
| control-guided / mask-guided / text-guided | 控制引导 / 掩膜引导 / 文本引导 | 任务类别名 |
| inpainting | 图像修复 | 掩膜引导编辑 |
| subject fidelity | 主体保真度 | DINO / CLIP-I 所度量 |
| perceptual distance | 感知距离 | LPIPS 所度量 |
| image-text alignment | 图文对齐度 | CLIP-Score 所度量 |
| overediting | 过度编辑 | 编辑任务中的失败模式 |
| auto-metric | 自动指标 | 与人工评估相对 |
| human rater | 人类评分者 | 不写作"打分员" |
| leaderboard | 排行榜 | ImagenHub 排名 |
| marking rubric | 评分细则 | PQ 评分所用标准 |
| zero-shot / one-shot / few-shot | 零样本 / 单样本 / 少样本 | 提示设置 |
| backbone model | 骨干模型 | MLLM 骨干 |
| distillation model | 蒸馏模型 | 未来方向 |
| prompt template | 提示模板 | 附录 A 内容 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0008 | 函数 ⟦SLOT_0⟧ 接收指令 ⟦SLOT_1⟧、图像 ⟦SLOT_2⟧、条件集 ⟦SLOT_3⟧，再依 ⟦SLOT_4⟧ 出分 | 五个槽位逐一保留，条件举例照译 | 一致 |
| b0043 | ⟦SLOT_6⟧ 运算、⟦SLOT_7⟧ 为 SC 子分数、⟦SLOT_8⟧ 为 PQ 子分数；量表 0–10；归一化 [0.0, 1.0] | 三槽位保留，List[0.0, 0.17, 0.33, 0.5, 0.67, 0.83, 1.0] 原样 | 一致 |
| b0054 | Fisher Z 变换估计平均斯皮尔曼相关系数 ⟦SLOT_9⟧ | ⟦SLOT_9⟧ 原样保留 | 一致 |
| b0065 | ⟦SLOT_12⟧ 为 footrule，⟦SLOT_13⟧ 为 rho；首个任务无参考图像故 LPIPS 不适用 | 两槽位保留，原因说明照译 | 一致 |
| b0087 | NVIDIA RTX A6000 GPU；OpenAI API 花费约 500 美元 | 硬件型号与金额原样保留 | 一致 |

### 一致性与数字核查

- 术语统一性：SC/PQ/O 一律保留缩写并配中文全称；`rationale` 全文统一为"评判理由"；`subject-driven`、`control-guided`、`multi-concept` 等任务名全文译法一致；`prompt` 在提示模板语境下译作"提示"/"提示词"，未混用为" Prompt"。
- 数字核查：0.4、0.45、0.5、0.2、0.3、29、30、100–200、[0.25, 0.35]、[0.0, 1.0]、500 美元等数值均未改动；区间与列表原样保留。
- 占位符核查：14 个 `⟦SLOT_n⟧` 槽位在译文中数量与编号完全一致，构建脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 参考文献块、作者块、代码块与表格均按规范跳过，未翻译。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- b0004 为项目主页 URL，按原样保留。
- 原文 b0062 中"See 7 for detailed comparison in Appendix"疑为笔误（应为附录 B.2 或表 7），译文按字面保留为"附录 7"。
- 原文 b0008 "these metrics are agnostic the end task"疑缺介词，已按语义译为"与最终任务无关"。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0031、b0194、b0008、b0220、b0067、b0214、b0192、b0083、b0089
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
