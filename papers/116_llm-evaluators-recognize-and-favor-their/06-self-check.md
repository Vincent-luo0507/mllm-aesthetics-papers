# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 189（文本 112 / 原子 77）|
| 已译文本块 | 112 / 112 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 10 · 已还原 10 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 20 |
| `<img>` 元素 | 1 |
| `<table>` 元素 | 20 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| self-evaluation | 自我评估 | 全文统一 |
| self-preference | 自我偏好 | 核心概念，统一 |
| self-recognition | 自我识别 | 核心概念，统一 |
| evaluator / evaluatee | 评估者 / 被评估方 | 角色名，统一 |
| generator | 生成器 | 三种角色之一，统一 |
| authorship identifier | 作者身份识别器 | 统一 |
| out-of-the-box | 未微调时 / 开箱即用 | 小节标题统一「未微调时」，行文用「未经微调」 |
| reward modeling | 奖励建模 | 统一 |
| constitutional AI | 宪法 AI | 保留英文原名的常见译法，统一 |
| self-refinement | 自我精修 | 统一 |
| model-based benchmark | 基于模型的基准 | 统一 |
| pairwise measurement | 成对测量 | 与 individual measurement 相对，统一 |
| individual measurement | 单独测量 | 统一 |
| Likert scale | 李克特量表 | 统一 |
| ordering bias | 顺序偏差 | 统一 |
| confounder / confounding | 混杂因素 / 混杂 | 统一 |
| control task | 对照任务 | 统一 |
| prediction confidence | 预测置信度 | 统一 |
| logit-based | 基于 logit 的 | 统一 |
| ambiguous / unambiguous | 不明确 / 明确 | 与原文标记对应，统一 |
| inverse causal relationship | 反向因果关系 | 统一 |
| example level / capability level | 样例层面 / 能力层面 | 统一 |
| situational awareness | 情境意识 | 统一 |
| self-awareness | 自我意识 | 统一 |
| calibration | 校准 | 统一 |
| verbalized uncertainty | 言语化不确定性 | 统一 |
| introspective capability | 内省能力 | 统一 |
| perplexity | 困惑度 | 统一 |
| reward hacking | 奖励劫持 | 统一 |
| authorship obfuscation | 作者身份混淆 | 统一 |
| white-box / black-box | 白盒 / 黑盒 | 统一 |
| Flesh-Kincaid readability | Flesh-Kincaid 可读性 | 保留专名 |
| Kendall’s τ | Kendall ⟦SLOT⟧ | 公式占位符原样保留 |
| prosaic / intentional interpretation | 平实 / 意向性解读 | 哲学语境术语，首次括注英文 |
| disproportionate self-preference | 过度的自我偏好 | 统一 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性 |
|---|---|---|---|
| b0019 | prosaic 与 intentional 解读之分；自我偏好可独立于自我识别存在 | 对这两个定义，我们采取平实（prosaic）而非意向性（intentional）的解读……一个 LLM 可以偏爱自己生成的文本，却并未意识到那些文本事实上由它自己生成 | 关键哲学区分与例证完整，未添补解释 |
| b0026 | 成对测量流程：两段文本、来源不透露、置信度归一化 | 向 LLM 呈现两段文本……备选来源的身份不会透露给评估者。我们通过归一化与两个选项相关联的 token 输出概率来计算预测置信度 | 语义一致，测量条件无遗漏 |
| b0050 | 顺序偏差反转率 GPT-4 25%、GPT-3.5 58%、Llama 89% | 当选项顺序被反转时，GPT-4、GPT-3.5 与 Llama 反转其成对偏好的比例分别为 25%、58% 与 89% | 三个数值与模型一一对应 |
| b0058 | 500 训练文章 / 500 评测 / 8 比特量化 / Adam / 学习率 ⟦SLOT_4⟧ | 我们使用 500 篇训练文章……剩余 500 篇文章及其关联摘要用作评测数据集……量化为 8 比特，并用 Adam 优化器以 ⟦SLOT_4⟧ 的学习率微调一个轮次 | 数字与超参数完整，SLOT_4 原样保留 |
| b0072 | 平均偏好 0.46；仅 22% 配对偏好大于 ⟦SLOT_9⟧ | 对微调模型生成文本的平均偏好为 0.46……只有 22% 的评估者—域配对显示出对微调模型生成文本大于 ⟦SLOT_9⟧ 的偏好 | 数值与结论一致，负面偏好的语义未颠倒 |

### 一致性与数字核查

- **术语统一**：已检索 `zh.json`，「自我评估 / 自我偏好 / 自我识别 / 评估者 / 成对测量 / 单独测量 / 顺序偏差 / 混杂因素」等核心术语译法唯一；「out-of-the-box」在小节标题与行文中分别译为「未微调时」与「未经微调」，语义一致。
- **数字核查**：核对了 1,000 篇、500 训练 / 500 评测、8 比特、25%、58%、89%、0.46、22%、三个数据集（XSUM、CNN/DailyMail、BIG-bench）、八个微调模型、NSF 资助号（1850208、1922658、2046556、#2138259、#2138286、#2138307、#2137603、#2138296）与分配号 CIS230057 等全部数值，未作改动；模型名（GPT-3.5 Turbo、GPT-4、Llama-2-7b-chat、Claude-2、BERT、T5）与数据集名（XSUM、CNN/DailyMail、BIG-bench、Mementos 不适用）原样保留。
- **占位符完整性**：112 个文本块逐块比对 `⟦SLOT_n⟧` 集合，源文与译文完全一致（差异 0）。
- **编码检查**：`zh.json` 与 `index.html` 中 U+FFFD 计数为 0。
- **不变量**：表格、公式、图片与参考文献块按 `t:"keep"` 跳过；段落一一对应，未删减或合并。

### 遗留问题

- 原文 b0046 结尾括号未闭合（"（Figure 4."），属原文排版问题，译文保留「（图 4。」的对应形态。
- 原文 b0081 中 "As we discussed The larger capability gap..." 存在断句问题，译文按语义补全为「正如我们所讨论的，这些模型之间的能力差距……」。
- 原文 b0101 中 "self-recognitiono" 为拼写笔误，译文按「自我识别」处理。
- 原文 b0023 与 b0058 中的脚注编号（11、22、33 等）按其出现位置原样保留。
- `missing_img` 为 0，无需补图。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（9 块）：b0061、b0081、b0037、b0074、b0063、b0050、b0036、b0032、b0082
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 9 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
