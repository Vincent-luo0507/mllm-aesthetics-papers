# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 418（文本 244 / 原子 174）|
| 已译文本块 | 244 / 244 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 110 · 已还原 110 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 251 |
| `<img>` 元素 | 9 |
| `<table>` 元素 | 40 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| leaderboard | 排行榜 | 全文统一 |
| Chatbot Arena / LMArena | Chatbot Arena / LMArena | 平台名保留原文 |
| provider / model provider | 提供方 / 模型提供方 | 全文统一 |
| proprietary model | 专有模型 | |
| open-weight model | 开放权重模型 | 全文统一，不写作「开源权重」 |
| open-source model | 开源模型 | |
| battle | 对战 | Arena 基本单位，全文统一 |
| Arena Score | Arena 分数 | |
| Bradley-Terry (BT) model | Bradley-Terry（BT）模型 | |
| private variant / private testing | 私有变体 / 私有测试 | |
| best-of-N (submission) | best-of-N（提交） | 保留原文 |
| selective disclosure / retraction | 选择性披露 / 撤回 | |
| sampling rate | 采样率 | |
| deprecation / silent deprecation | 下架 / 静默下架 | 全文统一 |
| data asymmetry / data access | 数据不对称 / 数据访问 | |
| overfitting | 过拟合 | |
| win rate | 胜率 | |
| prompt | 提示 | |
| checkpoint | 检查点 | |
| seed / initialization | 训练种子 / 初始化 | |
| unbiased sampling assumption | 无偏采样假设 | BT 模型假设名 |
| transitivity | 传递性 | |
| comparison graph / network | 比较图 / 比较网络 | |
| disconnected / sparse graph | 不连通 / 稀疏的图 | |
| maximum likelihood estimate | 极大似然估计 | |
| Fisher information | Fisher 信息 | |
| order statistics | 次序统计 | |
| bootstrap confidence interval | 自助置信区间 | |
| LM-as-a-judge | 以语言模型充当裁判 | |
| adversarial voting | 对抗性投票 | |
| Goodhart's Law | 古德哈特定律 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0016 | Meta 在 Llama 4 发布前一个月有多达 27 个模型被私下测试；从 ⟦SLOT_0⟧ 个模型中选最高分可系统性博弈评分 | 在 Llama 4 发布前的一个月内，我们观察到 Meta 有多达 27 个模型在 Chatbot Arena 上被私下测试……从 ⟦SLOT_0⟧ 个模型中选择得分最高变体的能力，使系统性博弈 Arena 评分成为可能 | 一致，占位符原样保留 |
| b0054 | 提交 ⟦SLOT_2⟧ 个变体，每个 ⟦SLOT_3⟧ 有潜在技能 ⟦SLOT_4⟧，中心为 ⟦SLOT_5⟧，随 ⟦SLOT_6⟧ 上升，观测技能 ⟦SLOT_7⟧ | 假设某提供方提交 ⟦SLOT_2⟧ 个模型变体，每个变体 ⟦SLOT_3⟧ 都有一个真实的潜在技能参数 ⟦SLOT_4⟧，采样自以某个基础技能水平 ⟦SLOT_5⟧ 为中心的分布……随提交数量 ⟦SLOT_6⟧ 的增加而上升……被观测到的技能为：⟦SLOT_7⟧ | 一致，6 个占位符顺序与原文一致 |
| b0095 | 胜率 23.5% / 42.7% / 49.9%；相对增益 81.7% / 112.3%；MMLU 66.5%→64.4%→65.9% | 变体 0_arena 的胜率为 23.5%，30_arena 为 42.7%……70_arena……为 49.9%……30_arena 上为 81.7%，在 70_arena 上为 112.3%……从 66.5%（0_arena）略微下降至 64.4%（30_arena）与 65.9%（70_arena） | 一致，七项数值原样保留 |
| b0140 | 下架政策原文条款（3000 票、同系列两个更新模型、超过 3 家提供方更便宜或同价且更好） | 当前标准表述为「模型在获得 3000 票后可能被退役，如果同系列中有两个更新的模型，和/或如果有超过 3 家提供方提供更便宜或同价且（按整体 Arena 分数）明显更好的模型」 | 一致，条款内容完整未增删 |
| b0308 | 爬取 5864 场对战、约每天 150 场；先问身份使对战自动失效；每天少量抓取且只投平局 | 我们在 2025 年 1 月至 2025 年 3 月间通过爬取 Chatbot Arena 收集了 5864 场对战（约每天 150 场）……我们首先询问模型的身份……我们每天只抓取少量样本，且只对模型之间的平局投票 | 一致 |

### 一致性与数字核查

- 术语：全文统一使用「提供方」「对战」「下架」「静默下架」「采样率」「开放权重」「过拟合」「Arena 分数」；`Chatbot Arena`、`LMArena`、`LMSYS`、`FastChat`、`ArenaHard`、`MMLU`、`Open LLM Leaderboard`、`OpenCompass`、`SuperGLUE`、`best-of-N`、`BT`、`Elo`、`command-r`、`aya-expanse`、`aya-vision`、`command-a`、`Llama-3.1-8B-Instruct` 等平台名、基准名与模型名一律原样保留。
- 数字与指标：2M、243、42、27、10、16、43、47、205、64%、19.2%、20.4%、8.9%、41、61.4%、54.3%、70.1%、62.8%、68、34%、3.3%、22.0%、17.9%、5.9%、19.4%、23.5%、42.7%、49.9%、81.7%、112.3%、66.5%、64.4%、65.9%、98.6%、1200、12000、197,217、567,319、43,729、14.3K、5864、5.8K、30%、3000、86.6%、87.8%、89%、80%、2.4% 等数值均按原义保留，未作换算错误。
- 占位符：逐块脚本比对，`⟦SLOT_0⟧`–`⟦SLOT_109⟧` 共 110 处，译文与原文在编号、数量与出现顺序上完全一致；构建脚本 `stray=0`。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD；构建脚本 `mojibake=0`。
- 不变量：表格、公式、SVG/object 图形与参考文献块未翻译；244 个 text 块一一对应，未做合并或拆分。

### 遗留问题

- 无图片缺失（`missing_img=0`）。
- 原文多处正文内嵌脚注编号与 URL（如 b0009、b0016、b0019、b0024、b0045、b0048 等），译文按原文顺序保留编号与链接文本，未另起脚注，也未改动源文件。
- 原文 b0061 中「This allows provider A to evaluate multiple models on the Chatbot Arena distribution and select the best-performing model」一句重复出现两次，译文合并表达一次，未改变语义。
- 原文 b0133 中「followed by Chatbot Arena 26」等引用编号处，译文按原文保留指代，未作推断。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0057、b0054、b0155、b0319、b0335、b0134、b0060、b0145、b0015
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
