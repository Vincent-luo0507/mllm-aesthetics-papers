# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 143（文本 60 / 原子 83）|
| 已译文本块 | 60 / 60 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 24 · 已还原 24 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 49 |
| `<img>` 元素 | 3 |
| `<table>` 元素 | 2 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| large vision-language model (LVLM) | 大型视觉语言模型 | 首次括注缩写 |
| vision-language generative reward model (VL-GenRM) | 视觉语言生成式奖励模型 | 缩写原样保留 |
| LLM-as-a-Judge / LVLM-as-a-judge | 以大语言模型为裁判／以 LVLM 为裁判 | 范式名 |
| preference pair | 偏好对 | |
| chosen / rejected response | 受偏好（被选中）／被拒绝的回复 | |
| visual hallucination | 视觉幻觉 | |
| hallucination-oriented queries | 面向幻觉的查询 | 数据集类别名 |
| multimodal reasoning | 多模态推理 | |
| Best-of-N (BoN) sampling | Best-of-N（BoN）采样 | |
| reinforcement learning from human feedback (RLHF) | 人类反馈强化学习 | |
| ensemble filtering | 集成过滤 | |
| weak judge | 弱裁判 | 指小型模型 |
| difficulty assessment | 难度评估 | |
| human verification | 人工核验 | |
| positional/position bias | 位置偏置 | 全文统一，不混用「顺序偏置」 |
| majority voting | 多数投票 | |
| overall accuracy | 总体准确率 | |
| macro average accuracy | 宏平均准确率 | |
| inference-time scaling | 推理时扩展 | 与 test-time scaling（测试时扩展）同源，按原文分别处理 |
| critic training | 评判训练 | |
| pointwise critic | 逐点评判者 | |
| pairwise critic | 成对评判者 | |
| error type | 错误类型 | |
| existence error | 存在性错误 | |
| recognition error | 识别错误 | |
| counting error | 计数错误 | |
| attribute identification error | 属性识别错误 | |
| Cohen's kappa | Cohen's kappa | 指标名不译 |
| Pearson correlation | Pearson 相关 | 人名不译 |
| inter-annotator agreement | 标注者间一致性 | |
| data curation | 数据策划 | |
| dataset contamination | 数据集污染 | |
| data flywheel | 数据飞轮 | |
| oracle answer | 标准答案 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0009 | 三条准则 (a)(b)(c)；三个应用领域；1,250 样本／7 个数据集 | 逐条对应，数字原样 | 一致 |
| b0012 | GPT-4o 62.4%、Gemini-1.5-Pro 62.5%、Qwen2-VL-72B 43.0%、LLaMA-3.2-90B 53.9%；Pearson r⟦SLOT_0⟧0.9；感知错误 ⟦SLOT_1⟧ 67% vs 推理 41.8%；+14.7% | 六个数值与槽位均保留 | 一致 |
| b0028 | 3,785 → 932；每样本约 65 秒；五类错误 | 数字与分类逐项对应 | 一致 |
| b0036 | 749/59.9%、318/25.4%、183/14.7%；895 中 531/59.3%、184/20.6%、69/7.7%、60/6.7%；Cohen's kappa 0.56–0.90、均值 0.70 | 比例与计数全部保留 | 一致，未换算 |
| b0053 | GPT-4o-mini 存在性 67.9%；Qwen2-VL-7B 识别 80.9%；推理均值 41.8%；7B→72B 计数错误降 18.2 个百分点（74.1%→55.9%）；推理仅降 6.0% | 数字与因果一致 | 一致 |

### 一致性与数字核查

- 术语：全文统一「视觉语言生成式奖励模型／偏好对／位置偏置／宏平均准确率／推理时扩展／评判训练／数据策划」，未做同义轮换；VL-RewardBench、VLFeedback、WildVision、POVID、RLAIF-V、RLHF-V、MMMU-Pro、MMMU、MathVerse、LLaVA-OneVision、LLaVA-Critic、InternVL2、Molmo、Pixtral、NVLM、Gemini-1.5-Pro/Flash、Claude-3.5-Sonnet、GPT-4o/4o-mini、Qwen2-VL、Llama-3.2、BoN、RLHF 等系统名与缩写一律原样保留。
- 占位符：逐块比对 `t:"text"` 块中 `⟦SLOT_n⟧` 集合与译文槽位集合，数量与编号完全一致（覆盖 ⟦SLOT_0⟧–⟦SLOT_23⟧）。
- 数字：1,250、7、681、6,484、1,568、1,546、3,785、932、1,204、318、749、183、895、531、184、69、60、65 秒、0.56–0.90、0.70、16、7B–90B、62.5%/62.4%/53.9%/43.0%、51.1%–70.5%、28.0%–50.8%、42.8%/53.9%、33.9%/43.0%、39.7%/43.7%、44.8%、35.7%→52.5%、67.9%、80.9%、41.8%、18.2 个百分点、74.1%→55.9%、6.0%、K=1–9、60.3%→62.7%、1.7/2.6 个百分点、14.7%、9.2%、52.9%/47.4%、9.1%、60.0%、temperature=0.2、top-p=0.2 等均原样保留。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片与参考文献块一律未翻译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 摘要中报告的 GPT-4o 准确率（65.4%）与正文主要结果表中的宏平均准确率（62.4%）口径不同（前者为总体准确率口径），译文按各自原文数值保留，未统一。
- b0062 含原文脚注标记「11 1 …」，译文按原位置保留脚注文本。
- 表 1 与表 2 的完整数据以表格块形式存在，未翻译。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0059、b0057、b0062、b0030、b0049、b0069、b0028、b0040、b0027、b0055
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
