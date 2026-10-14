# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 306（文本 159 / 原子 147）|
| 已译文本块 | 159 / 159 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 344 · 已还原 344 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 782 |
| `<img>` 元素 | 17 |
| `<table>` 元素 | 17 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| alignment | 对齐 | |
| pluralistic alignment | 多元对齐 | 对应框架名 PAL |
| heterogeneous / homogeneous preference | 异质偏好 / 同质偏好 | 全文中二者成对出现，译法固定 |
| plurality | 多元性 | |
| Bradley-Terry-Luce (BTL) model | Bradley-Terry-Luce（BTL）模型 | |
| ideal point model | 理想点模型（ideal point model） | 由 Coombs 提出 |
| ideal point / preference point | 理想点 / 偏好点 | 指同一对象，随语境选用 |
| metric learning | 度量学习 | |
| Mahalanobis metric | 马氏度量 | |
| mixture modeling | 混合建模 | |
| prototype / prototypical | 原型 / 原型化 | |
| convex combination | 凸组合 | |
| convex hull | 凸包 | |
| link function | 连接函数（link function） | |
| reward model (RM) / reward function | 奖励模型（RM）/ 奖励函数 | |
| foundation model | 基础模型 | |
| penultimate-layer representation | 倒数第二层表示 | |
| supervised fine-tuning (SFT) | 监督微调（SFT） | |
| RLHF / PPO / DPO | 基于人类反馈的强化学习（RLHF）/ 近端策略优化（PPO）/ 直接偏好优化（DPO） | |
| pairwise comparison | 成对比较 | |
| latent space / latent dimension | 潜空间 / 潜维度 | |
| hinge loss / logistic loss | 铰链损失 / 逻辑损失 | |
| seen user / unseen user | 已见用户 / 未见用户 | |
| seen accuracy / unseen accuracy | 已见准确率 / 未见准确率 | |
| few-shot / zero-shot | 少样本 / 零样本 | |
| persona | 人格（persona） | Anthropic Persona 数据集 |
| rubric | 标注细则 | 指标注者被给定的评分规范 |
| labeler | 标注者 | |
| semi-synthetic | 半合成 | |
| mixture ratio | 混合比例 | |
| color filter | 颜色滤镜 | |
| leakage / no-leakage | 泄漏 / 无泄漏 | 指测试集与训练集重叠 |
| state-of-the-art (SoTA) | 当前最优（SoTA） | |
| query complexity | 查询复杂度 | |
| simplex | 单纯形 | |
| dropout / weight decay | dropout / 权重衰减 | |
| residual connection | 残差连接 | |
| triplet query | 三元组查询 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0011 | 用理想点模型 [4] 与度量学习 [39] 的视角重构对齐问题，可借助更丰富的工具箱 | 我们引入理想点模型 [4] 与度量学习 [39] 的视角，重构了从人类偏好出发的对齐问题。这一重构使我们得以借助更丰富的建模与算法工具箱（第 2 节与第 3.1 节） | 一致，引用编号与章节号未增删 |
| b0050 | 省略 ⟦SLOT_100⟧ 上的上标 ⟦SLOT_99⟧；连接函数不必对所有用户相同；算法无需知道连接函数 | 我们省略了 ⟦SLOT_100⟧ 上的上标 ⟦SLOT_99⟧；但需要说明，连接函数不必对所有用户都相同，而且我们在第 3.3 节描述的学习算法无需知道连接函数 | 一致，两个占位符顺序与原文一致 |
| b0079 | 每用户样本不足时学习多样化偏好会损害性能；100 样本/已见用户；固定原型与映射只训新权重 | 若每用户样本不足，学习多样化偏好反而会损害性能……（以每已见用户 100 个样本训练）……保持学到的原型与映射固定，只用少量比较样本训练新用户的权重 | 一致，100 与方法描述未改动 |
| b0101 | 混合比例 1 时 PAL 95.2% vs 同质奖励模型 75.4% | 在混合比例为 1 时，⟦SLOT_250⟧ 达到 95.2% 的测试准确率，而同质奖励模型为 75.4% | 一致，两个百分数原样保留 |
| b0115 | 18391 条测试样本；10587 条泄漏、7804 条无泄漏 | Pick-a-Pic v2 测试集包含 18391 条无偏好并列的样本……其中 10587 条（⟦SLOT_258⟧）……其余 7804 条测试样本（⟦SLOT_259⟧） | 一致，三个计数与两个占位符原样保留 |

### 一致性与数字核查

- 已用 Grep 全文回扫核心术语：`理想点模型` 14 处、`异质` 18 处、`同质` 10 处、`原型` 41 处、`凸组合` 6 处、`已见用户` 16 处、`未见用户` 15 处、`连接函数` 8 处、`混合建模` 6 处，均未出现同义轮换。
- 数字核查：594K、592K、105M、6B、1.7B、1.3B、18391、10587、7804、12487、701、94.38%、1261、1453、95.2%、75.4%、100、50、468/4223、234/468、117、116031、3693、2%、24 GB、16 GB、2 小时、1000 轮、10 轮、10 名工作者、100,000 等均与原文一致；`8⟦SLOT_263⟧A100` 中的 GPU 数量以占位符形式原样保留。
- 数据集与模型名：Pick-a-Pic、Pick-a-Filter、Summary、Anthropic Persona、CLIP-H/14、PickScore、all-mpnet-base-v2、Reddit TL;DR、Archangel、Zephyr、Rewarded soups、DPA 均原样保留。
- 占位符核查：脚本报告槽位总数 344、已还原 344、残留 0；另用脚本逐块比对 `en` 与 `zh` 中 `⟦SLOT_n⟧` 的集合（含重复计数），159 个文本块全部一致（`slot_mismatch` 为空）。
- 编码核查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0。
- 未翻译内容：公式 (1)–(7)、算法 1–2、表 1–6、图 1–15 的图形对象、参考文献均按 `t:"keep"` 规则原样保留。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 摘要中提到的 1.7B 奖励模型（b0269）与表 6 标题中的 1.3B（b0270）在原文中不一致，属原文自身笔误，译文按各处原文忠实译出。
- 脚注标记在正文中的形态为抽取残留（如 b0034 的 `11 1`、b0035 的 `22 2`、b0122 的 `33 3 https://github.com/ContextualAI/HALOs`），按原文保留。
- b0226 以冒号开头（“：由于在 Pick-a-Pic V1……”），系原文在 `Pick-a-Filter` 小标题后直接续写所致，译文保留了这一形态。
- `foundation model` 统一译为“基础模型”，未使用“基座模型”等别名。


## 复核记录（第二轮交叉验证）

抽查块：b0075、b0100、b0270、b0101、b0118、b0221


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
