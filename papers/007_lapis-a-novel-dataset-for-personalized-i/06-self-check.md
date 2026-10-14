# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 170（文本 97 / 原子 73）|
| 已译文本块 | 97 / 97 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 6 · 已还原 6 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 19 |
| `<img>` 元素 | 19 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| computational aesthetics | 计算美学 | 学科名 |
| image aesthetic assessment (IAA) | 图像美学评估 | 总称 |
| generic image aesthetic assessment (GIAA) | 通用图像美学评估 | 预测平均分数 |
| personalized image aesthetic assessment (PIAA) | 个性化图像美学评估 | 逐标注者预测 |
| artistic image aesthetic assessment (AIAA) | 艺术图像美学评估 | |
| annotator / participant / rater | 标注者／参与者／评分者 | 本文统一用「标注者」 |
| personal attributes | 个人属性 | 与 image attributes（图像属性）相对 |
| image attributes | 图像属性 | |
| demographic information | 人口统计信息 | |
| art interest | 艺术兴趣 | VAIAK 分量表 |
| art familiarity | 艺术熟悉度 | |
| art expert / art novice | 艺术专家／艺术新手 | |
| aesthetic appreciation | 美学欣赏 | |
| genre | 题材 | 7 类：抽象、城市景观、花卉画等 |
| style | 风格 | 26 种，另有层级化上位标签 |
| figurative / abstract | 具象／抽象 | 全文统一，不用「写实」 |
| representational / non-representational | 再现性／非再现性 | |
| visual analogue scale | 视觉模拟量表 | 0–100，7 个刻度点 |
| tick point | 刻度点 | |
| stratified sampling | 分层采样 | |
| ablation study | 消融实验 | |
| mean squared error (MSE) | 均方误差 | 缩写保留 MSE |
| SROCC (Spearman rank-order correlation coefficient) | SROCC | 指标名原样保留 |
| Pearson correlation coefficient | Pearson 相关系数 | 人名不译 |
| backbone | 骨干网络 | |
| 4-fold cross-validation | 4 折交叉验证 | |
| unseen users | 未见用户 | |
| failure case | 失败案例 | |
| siamese network | 孪生网络 | |
| graph neural network (GNN) | 图神经网络 | |
| collaborative filtering | 协同过滤 | |
| visual analogue scale tick points | 视觉模拟量表刻度点 | |
| Prolific | Prolific | 众包平台名不译 |
| WikiArt | WikiArt | 数据集／网站名不译 |
| Big Five personality test | 大五人格测验 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0012 | Art under-explored；个体差异艺术图更大 [31,32]；AIAA 挑战；DALL-E；contributions | 艺术在计算美学中未被充分探索；艺术图个体差异更大；AIAA 挑战；DALL-E | 一致，引用编号未改 |
| b0036 | 11,723 幅；26 风格；7 题材；WikiArt | 数字与类别数逐项对应 | 一致 |
| b0054 | 亮度熵／边缘方向熵正相关 ⟦SLOT_5⟧；稀疏性／CNN 对称性负相关 ⟦SLOT_6⟧；颜色通道均值负相关、标准差正相关 | 同上，槽位原样保留 | 一致，结论未增删 |
| b0068 | PIAA-MIR/PIAA-ICI 复现；naive 方案 vs 4 折交叉验证；性能显著下降 | 同上 | 一致 |
| b0074 | 抽象／具象失败案例；MSE 与年龄负相关 ⟦SLOT_7⟧/⟦SLOT_8⟧；年轻标注者占比较高 | 同上 | 一致，数字与因果表述未改动 |

### 一致性与数字核查

- 术语：全文统一「美学评估／美学分数／标注者／个人属性／图像属性／具象／抽象」，未做同义轮换；GIAA、PIAA、AIAA、IAA、LAPIS、PARA、BAID、EVA、PR-AADB、FLICKR-AES、VAIAK、PIAA-MIR、PIAA-ICI 等缩写与系统名一律原样保留。
- 占位符：逐块比对 `t:"text"` 块中 `⟦SLOT_n⟧` 集合与译文中的槽位集合，数量与编号完全一致（⟦SLOT_3⟧–⟦SLOT_8⟧）。
- 数字：11,723、24、552、999、1628、60K、360,000、40K、165、16k、30、30,000、438、25、26、7、1990、7976、3747、0–100、250、70/10/20、4 折、1.2%、21、1,927、2160、5 位参与者等均原样保留。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片、参考文献块一律未翻译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文图 s4、s9、s10、s11 与表 s1 位于补充材料中且编号带 "s" 前缀，译文保留原文编号形式（图 s4、表 s1 等）。
- 原文 b0012 中「Our contributions are as follows:」后接三个 `dd` 块（b0014/b0016/b0018），其间的 equation 块为列表标记，未翻译。
- b0157 中的脚注文本（"88 8 ..."）按原文插入位置保留在句中。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（8 块）：b0065、b0006、b0138、b0036、b0018、b0054、b0033、b0058
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 8 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
