# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 283（文本 190 / 原子 93）|
| 已译文本块 | 190 / 190 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 146 · 已还原 146 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 311 |
| `<img>` 元素 | 14 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image quality assessment (IQA) | 图像质量评估 | 全文统一 |
| full-reference (FR) / reduced-reference (RR) / no-reference (NR) | 全参考／半参考／无参考 | |
| blind image quality assessment (BIQA) | 无参考图像质量评估 | NR-IQA 的同义说法，统一译此 |
| mean opinion score (MOS) | 平均意见分 | 缩写保留 MOS |
| subjective user study | 主观用户研究 | |
| ecological validity | 生态效度 | 本文核心概念，不译作「生态有效性」 |
| in-the-wild | 野外 | 指真实场景采集，全文统一 |
| authentic distortions | 真实失真 | 与 artificial distortions（人工失真）相对 |
| pristine image | 原始图像 | 指未劣化的参考图 |
| crowdsourcing | 众包 | |
| crowd worker / contributor | 众包工作者／贡献者 | 前者统一「众包工作者」 |
| quality indicator | 质量指标 | 七项标量指标 |
| content indicator | 内容指标 | 由深度特征聚类得到 |
| diversity sampling | 多样性采样 | |
| near-duplicate | 近似重复 | |
| machine tag | 机器标签 | YFCC100m 元数据 |
| z-score | z 分数 | |
| absolute category rating (ACR) | 绝对类别评分 | 5 级量表 |
| intra-class correlation coefficient (ICC) | 组内相关系数 | |
| line clicker | 直线点击者 | 众包质量控制术语 |
| outlier | 离群者 | |
| test question | 测试题 | |
| SROCC (Spearman rank order correlation coefficient) | 斯皮尔曼秩相关系数 | 缩写保留 |
| PLCC (Pearson linear correlation coefficient) | Pearson 线性相关系数 | 缩写保留 |
| RMSE | 均方根误差 | |
| global average pooling (GAP) | 全局平均池化 | |
| spatial pyramid pooling (SPP) | 空间金字塔池化 | |
| Earth Mover's Distance (EMD) loss | EMD 损失 | 首次给出英文全称 |
| Huber loss | Huber 损失 | |
| transfer learning | 迁移学习 | |
| fine-tuning | 微调 | |
| crop / cropping | 裁剪 | |
| importance map | 重要性图 | |
| bag-of-words (BoW) | 词袋 | |
| natural scene statistics (NSS) | 自然场景统计 | |
| cross-database testing / cross-test | 跨数据库测试／交叉测试 | |
| effective group size | 有效群体规模 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0011 | KonIQ-10k 为最大 IQA 数据库；10,073 幅；选自 1000 万条 YFCC100M 记录；每图 120 个评分；1,459 位工作者 | 数字与来源逐项对应 | 一致 |
| b0045 | 第二阶段：下载、缩放至 ⟦SLOT_5⟧、裁剪、采样 13,000、去重、人工过滤、最终 10,073 | 同上，槽位保留 | 一致 |
| b0106 | 2,302 → 1,459；10,073 幅；至少 120 分／图；超 120 万条判断 | 数字原样保留 | 一致 |
| b0184 | LIVE-itW 交叉测试 0.825 vs KonIQ-10k 0.921；长宽比改变导致退化类型未见过 | 同上 | 数字与因果一致 |
| b0297 | 附录标签采样启发式，含 ⟦SLOT_123⟧–⟦SLOT_148⟧ 大量槽位 | 全部槽位按序原样保留，未翻译占位符内内容 | 一致，槽位数量与编号完全相同 |

### 一致性与数字核查

- 术语：全文统一「图像质量评估／无参考图像质量评估／平均意见分／众包工作者／质量指标／内容指标／生态效度／野外」，未做同义轮换；KonIQ-10k、LIVE-itW、YFCC100m、KonCept512、InceptionResNetV2、NasNetMobile、SROCC、PLCC、ICC、EMD、ACR、MILP、GAP、SPP 等缩写与系统名一律原样保留。
- 占位符：逐块比对 `t:"text"` 块中 `⟦SLOT_n⟧` 集合与译文槽位集合，数量与编号完全一致（覆盖 ⟦SLOT_0⟧–⟦SLOT_148⟧，其中 ⟦SLOT_27⟧、⟦SLOT_36⟧、⟦SLOT_37⟧ 未出现在文本块中）。
- 数字：10,073、9,974,030、4,807,816、13,000、1,459、2,302、1,749、1,648、68、121、1.2 million、0.921、0.825、0.836、0.918、0.973、0.46、11.35、6.63、1265、7,058／1,000／2,015、0.25／0.25／0.5、2,048／1,024／256、1,536、100,000、512x384 等均原样保留。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片与参考文献块一律未翻译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 补充材料中的图 14–19 在正文中以文字引用（如「补充材料图 14」），原文编号形式予以保留。
- b0081、b0082、b0214、b0045 中含原文脚注标记（如「22 2 …」「33 3 …」「44 4 …」「11 1 …」），译文按原位置保留脚注文本。
- 原文 b0218 中 "universally agreed-upon definition" 译为「尚无公认的统一定义」，未添加额外解释。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0069、b0193、b0031、b0139、b0130、b0212、b0197、b0104、b0081、b0129
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
