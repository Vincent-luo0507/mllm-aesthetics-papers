# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 269（文本 147 / 原子 122）|
| 已译文本块 | 147 / 147 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 48 · 已还原 48 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 181 |
| `<img>` 元素 | 17 |
| `<table>` 元素 | 20 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Visual Feedback Layout Model (VFLM) | 视觉反馈版式模型（VFLM） | 首次出现给出中英对照，后文用 VFLM |
| visual feedback | 视觉反馈 | 全文核心术语，译法唯一 |
| text layout | 文本版式 | 「layout」统一译「版式」 |
| code-only paradigm | 纯代码范式 | 与本文方法对举 |
| generation, rendering, reflection, refinement | 生成—渲染—反思—优化 | 四步循环，引号内固定写法 |
| reflection / iterative refinement | 反思／迭代优化 | 固定 |
| self-improving | 自改进 | 固定 |
| visual perception gap | 视觉感知缺口 | 固定 |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 固定 |
| Reinforcement Learning (RL) | 强化学习（RL） | 固定 |
| Supervised Fine-Tuning (SFT) | 监督微调（SFT） | 固定 |
| cold-start | 冷启动 | 固定 |
| reward model | 奖励模型 | 固定 |
| reward hacking | 奖励劫持 | 固定 |
| outcome-based reward | 基于结果的奖励 | 与 process-oriented reward 对举 |
| process-oriented reward | 面向过程的奖励 | 固定 |
| Group Relative Policy Optimization (GRPO) | 组相对策略优化（GRPO） | 缩写保留 |
| advantage (function) | 优势（函数） | 固定 |
| PPO / DPO / RLHF | 权近策略优化（PPO）／直接偏好优化（DPO）／RLHF | 首次给出中文全称 |
| KL divergence | KL 散度 | 固定 |
| rollout | rollout | 保留不译，另加「采样」作语境补充 |
| on-policy | 同策略 | 固定 |
| Optical Character Recognition (OCR) | 光学字符识别（OCR） | 固定 |
| trajectory | 轨迹 | 多轮生成—反思序列 |
| distillation / teacher model | 蒸馏／教师模型 | 固定 |
| ground-truth | 真值 | 固定 |
| tool call | 工具调用 | 固定 |
| preference pair | 偏好对 | 固定 |
| quality level (Level-I～IV) | 质量层级（Level-I～IV） | 层级名保留原文 |
| character-level F-measure | 字符级 F 值 | 固定 |
| Text-Background Harmony | 文本—背景协调性 | GPT-4o 评测维度 |
| Text Presentation Quality | 文本呈现质量 | 同上 |
| Meaning Expression Adaptability | 语义表达适配性 | 同上 |
| SOTA | SOTA | 保留不译 |
| True/False Positive (TP/FP) | 真正例／假正例（TP/FP） | 固定 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 结论 |
|---|---|---|---|
| b0011 | 两阶段训练：蒸馏构造轨迹 + SFT；再用 RL；复杂过程奖励会导致奖励劫持，简单结果奖励更有效（反直觉） | 四层信息全部译出，「奖励劫持」与「反直觉地证明」均保留，三个引用 [41, 10, 25] 保留 | 语义一致，无添油加醋 |
| b0078 | 四级分层构造：每提示生成四级，全部成对比较 → 每个问题 6 个偏好对 | 数值「6 个偏好对」与「Level-I～IV」层级名保留，论证链条完整 | 数字与逻辑一致 |
| b0094 | 0.9071（VFLM-step1）vs. 0.8672（Claude 3.7）vs. 0.8481（IGD），最终 0.9376 | 四个数值与模型名逐项对应，未作四舍五入或改写 | 数字零改动 |
| b0105 | 0.5415 高于 0.5332，迭代后提升到 0.6018 | 三个数值原样保留，比较关系（超过／提升）译写准确 | 数字与语义一致 |
| b0226 | 输入复杂度以 token 长度度量；⟦SLOT_40⟧ tokens 时平均 ⟦SLOT_41⟧2.5 轮；>400 tokens 时接近 4 轮上限 | 1,000 样本、400 词元、4 轮上限与两个槽位全部保留 | 数字与占位符零改动 |

### 一致性与数字核查

- **术语统一**：对 `zh.json` 全文检索确认，「视觉反馈」「文本版式」「反思」「迭代优化」「奖励模型」「奖励劫持」「基于结果的奖励／面向过程的奖励」「冷启动」「质量层级」等核心术语在正文与补充材料中译法完全一致，未出现同义词轮换（例如未混用「反思」与「反省」、「版式」与「布局」）。
- **占位符完整性**：逐块比对原文与译文的 `⟦SLOT_n⟧` 集合，48 个槽位（SLOT_0～SLOT_47）数量、编号与顺序全部一致；构建脚本 `stray = 0` 印证。
- **数字与指标**：200K、9.8、84.7、8K、2,359/1,266/2,030/2,537、16 块 H200、64、8、1.0、1e-3、1e-6、1.2M、25K、512、2100、40k、128、1e-5、0.25、0.1、32K、1K、97.4%、0.9071、0.8672、0.8481、0.9376、0.5415、0.5332、0.6018、250 步、100 步、1,000、400、16 名参与者、320 条查询、960 票、4×4090 等全部原样保留；Char-F、RM Score、R_ali、R_ove、R_com、TP/FP/FN、max_pixels 等指标名与变量名未作翻译或改写；Level-I～Level-IV 层级名保留原文。
- **编码检查**：`zh.json` 与 `index.html` 均不含 U+FFFD，构建脚本 `mojibake = 0`。
- **不变量**：表格（20）、代码块、公式（181 个 `<math>`）、图片（17）与参考文献块均为 `t:"keep"`，未翻译；147 个文本块严格一一对应，无合并、拆分或删减。

### 遗留问题

- 无图片缺失（`missing_img = 0`），17 张图片均已在 `figures/` 中命中。
- 补充材料中多处出现「prompt 5」「Figure Fig. 9」「the the」等原文排版残留（如 b0194 两次写 prompt 5、b0226 写「Figure Fig. 9」、b0124 与 b0109 的拼写瑕疵 outcom），译文按字面保留，未作修正。
- b0246「来自奖励模型的版式表现分数（⟦SLOT_42⟧）与两个基于文本准确率的奖励：」为原文残句（后接公式表），译文同样以冒号收尾，未补写内容。
- b0209 中「OCR engine11 1 https://…」为脚注转换残留，按字面保留。


## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0076、b0225、b0122、b0077、b0053、b0021、b0072、b0027、b0100、b0118
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
