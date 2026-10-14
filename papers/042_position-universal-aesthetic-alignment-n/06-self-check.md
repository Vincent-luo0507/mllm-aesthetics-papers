# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 160（文本 76 / 原子 84）|
| 已译文本块 | 76 / 76 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 59 · 已还原 59 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 137 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| alignment | 对齐 | 全文统一，不另译“校准” |
| instruction following | 指令遵循 | 对齐两大着力点之一 |
| general preference | 通用偏好 | 与 aesthetics 等同使用 |
| wide-spectrum aesthetics | 广谱美学 | 首次出现附英文原词 |
| anti-aesthetics | 反美学 | 与广谱美学同义，首次出现附英文 |
| reward model | 奖励模型 | 全文统一 |
| reversed alignment | 反向对齐 | 作者提出的核心概念，首次出现附英文 |
| user autonomy | 用户自主性 | 全文统一 |
| expressive agency | 表达能动性 | 全文统一 |
| aesthetic pluralism | 美学多元主义 | 全文统一 |
| pre-emptive governance | 先发式治理 | 政治哲学术语，首次出现附英文 |
| value capture | 价值捕获 | Nguyen 提出的概念，附英文 |
| toxic positivity | 毒性积极 | 首次出现附英文 |
| sanitized reality | 被净化的现实 | 六个关切之一 |
| inherited bias | 继承性偏见 | 六个关切之一 |
| developer-centered | 以开发者为中心 | 与 user-centered（以人为本）相对 |
| prompt adherence / prompt following | 提示遵循度 / 提示遵循 | 分别固定 |
| majoritarianism | 多数主义 | 全文统一 |
| image-to-image editing | 图到图编辑 | 通用术语 |
| open-vocabulary detector | 开放词汇检测器 | 指 LLMDet |
| guidance scale | 引导尺度 | 扩散模型术语 |
| Wilcoxon signed-rank test | Wilcoxon 符号秩检验 | 统计检验名 |
| McNemar’s test | McNemar 检验 | 统计检验名 |
| Cohen’s kappa | Cohen's kappa | 一致性指标保留原文 |
| ROC curve | ROC 曲线 | 指标名保留 |
| F1 score | F1 分数 | 指标名保留 |
| AI sycophant | AI 谄媚者 | 首次出现附英文 |
| hieratic scale | 等级比例 | 艺术史术语，附英文 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0004 | 对齐的两个着力点；普适美学标准的假设；模型对齐到“全体智人平均偏好建模出的抽象的人” | 论点与引用编号完整译出，末句关键论断无删减 | 一致，未添补评论 |
| b0029 | HPSv3 标注者 88.95% 为 18—40 岁、21—30 岁组占 38.65%；80% 一致度门槛；95% 置信度筛选 | 四个数字原样保留，因果链条完整 | 一致 |
| b0046 | 四个分数 ⟦SLOT_18⟧–⟦SLOT_21⟧ 的定义，带 ⟦SLOT_22⟧ / ⟦SLOT_23⟧ 两类分数的分工；BLIP 验证 | 六个占位符原样保留，两类分数职责对应准确 | 一致 |
| b0079 | HPSv3 给干净图像平均高 5.90 分；Analog Degradation 13.2；Intentional Blur 与 Exposure Extremes 约 8；量程 0—15 | 数字与类别名原样保留 | 一致，未换算 |
| b0081 | 真实艺术品 HPSv3 平均 5.86；排行榜 10/12；BLIP 0.996 与打乱后 0.086 | 四个数值原样保留，⟦SLOT_58⟧ 保留 | 一致 |

### 一致性与数字核查

- 术语统一：用 Grep 在 `zh.json` 中检索「广谱美学」「反美学」「对齐」「指令遵循」「通用偏好」「奖励模型」「反向对齐」「用户自主性」「美学多元主义」「毒性积极」「价值捕获」「先发式治理」等核心术语，全文译法唯一；缩写 VLM / LLM / RLHF / HPSv2 / HPSv3 / CLIP / BLIP / MPS / F1 / ROC / GPA 均原样保留；模型名（Flux、SDXL、SD3.5M、Nano Banana、Playground、DanceFlux、PrefFlux、Flux Krea、GPT-5-Chat、Qwen3-VL）一律不译。
- 数字核查：样本量 300、维度数 12、2—4 个维度、300 条基础提示、120 条提示、30 条中性提示、6.27K 与 2,928 张图像、5.90、13.2、约 8、0—15、5.86、10/12、0.996、0.086、88.95%、38.65%、80%、95%、约 64%、0.80、引导尺度 4 均未改动或换算。
- 占位符完整性：脚本统计内联槽位 59、已还原 59；另用脚本逐块比对 76 个文本块的 `⟦SLOT_n⟧` 集合，全部一致。
- 编码检查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0，编码 UTF-8。
- 不变量：表格、公式、图片、参考文献块一律未翻译；未删减、合并或拆分段落，一块对一块。

### 遗留问题

- 原文 b0077 处写作 “five classes” 但随后列出六项（clarity、color、lighting、composition、emotions、subjects），译文按原文照录为“五个类别”并保留全部六项，未作更正，在此记录。
- 原文若干引用缺少年份（如 Tate, ；Mordvintsev et al., ；Stacey Hill, ），属原文形态，译文保留原样。
- 图片引用缺失 0，公式元素 137 个均正常还原，未发现原文乱码或不可解析的块。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（9 块）：b0055、b0041、b0081、b0032、b0083、b0056、b0064、b0080、b0075
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 9 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
