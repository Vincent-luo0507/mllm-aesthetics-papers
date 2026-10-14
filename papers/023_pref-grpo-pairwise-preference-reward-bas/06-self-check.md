# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 222（文本 135 / 原子 87）|
| 已译文本块 | 135 / 135 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 101 · 已还原 101 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 222 |
| `<img>` 元素 | 23 |
| `<table>` 元素 | 28 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| text-to-image (T2I) | 文本到图像（T2I） | 首次括注，后文可用 T2I |
| reinforcement learning (RL) | 强化学习 | |
| GRPO | GRPO | 全称首次出现时补“组相对策略优化” |
| pointwise reward model | 逐点奖励模型 | 与成对奖励对举 |
| Pairwise Preference Reward Model (PPRM) | 成对偏好奖励模型（PPRM） | 首次括注 |
| reward hacking | 奖励破解 | 全文统一，不作“奖励黑客” |
| illusory advantage | 虚假优势（illusory advantage） | 本文核心概念 |
| advantage | 优势 | GRPO 归一化后的量 |
| normalization | 归一化 | 组内分数归一化 |
| rollout group | 回放组 | 一次采样的图像组 |
| policy | 策略 | |
| flow matching | 流匹配 | |
| rectified flow | 整流流 | [27] |
| velocity field | 速度场 | |
| Markov Decision Process (MDP) | 马尔可夫决策过程 | |
| ODE / SDE | ODE / SDE | 保留缩写 |
| Euler-Maruyama | Euler-Maruyama | 离散化方法 |
| Wiener process | 维纳过程 | |
| win rate | 胜率 | 本文的新奖励信号 |
| within-group standard deviation | 组内标准差 | 虚假优势的成因 |
| semantic consistency | 语义一致性 | 评测对象 |
| primary dimension / sub-dimension | 主维度 / 子维度 | 10 / 27 |
| testpoint | 测试点 | 每条提示词 1–5 个 |
| prompt theme / sub-theme | 提示词主题 / 子主题 | 5 / 20 |
| subject category | 主体类别 | |
| MLLM | 多模态大语言模型（MLLM） | 首次括注 |
| over-saturation | 过饱和 | HPSv2 的破解表征 |
| wall-clock (time) | 时钟（时间） | VII-C 小节 |
| macro-F1 | macro-F1 | 保留原文 |
| Cohen's kappa | Cohen's kappa | 保留原文 |
| closed-source / open-source | 闭源 / 开源 | |
| checkpoint | 检查点 | 开源模型获取方式 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性 |
|---|---|---|---|
| b0014 | 虚假优势的两点成因、放大偏差、图 1 与图 2 引用；主维度需细分为子维度 | 两点论断分述，图号引用与因果链完整 | 一致 |
| b0022 | 五项贡献，含 +5.84%、+12.69%、+12.04% 三个提升数字 | 三个百分数原样保留，五项贡献逐条对应 | 一致 |
| b0084 | Attribute / Action / Relationship / Layout 四个维度的子维度分解清单 | 四个维度的子项逐一译出，未合并或遗漏 | 一致 |
| b0109 | 推理：30 步采样、CFG 3.5、⟦SLOT_87⟧ 幅图像、相同提示词与初始噪声 | 数字与占位符均保留 | 一致 |
| b0157 | 默认设置下 3 s→7 s（+4 s）、64→480 请求、5 s→22 s | 六处时间与请求数原样保留，四个占位符顺序一致 | 一致 |

### 一致性与数字核查

- 术语：复核 zh.json，文本到图像、逐点奖励模型、奖励破解、虚假优势、胜率、主维度／子维度、测试点、语义一致性等核心术语全文译法唯一，未出现同义轮换。
- 数字：5.84%、12.69%、12.04%、600、5、20、10、27、1–5、5k、64、25、8、4、30、3.5、400、40、5、0.8、7、3 s、7 s、4 s、64、480、5 s、22 s、160、10% 等均未改动。
- 占位符：脚本逐块比对 `⟦SLOT_0⟧`–`⟦SLOT_100⟧` 共 101 处，修订 b0099、b0154 两处顺序后完全一致，stray=0。
- 编码：zh.json 与 index.html 均不含 U+FFFD。

### 遗留问题

- 无缺失图片（missing_img=0）。
- 原文多处交叉引用被论文标题串替代（如 “Fig. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning”），据上下文统一规范为“图 1”，涉及 b0014、b0016、b0027、b0053、b0143、b0144。
- 基准维度名（Style、World Knowledge、Attribute、Action、Relationship、Layout、Compound、Grammar、Logical Reasoning、Text）为基准中的专有标签，保留英文原名。
- b0126 中 “Keling-Ketu (Kuaishou)” 按官方中文名译为“可灵-可图（快手）”。


## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；23 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0019、b0142、b0011、b0140、b0173、b0016（seed=2）；加抽 b0034、b0120、b0140、b0108（seed=7）
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
