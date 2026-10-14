# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 222（文本 121 / 原子 101）|
| 已译文本块 | 121 / 121 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 136 · 已还原 136 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 309 |
| `<img>` 元素 | 46 |
| `<table>` 元素 | 11 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image aesthetics assessment / analysis | 图像美学评估／分析 | 全文统一用「美学」，不混用「美感」作术语 |
| aesthetic rating | 美学评分 | 指连续分数值 |
| aesthetic ranking | 美学排序 | 指相对次序 |
| ranking loss | 排序损失 | 与 regression loss（回归损失）并列 |
| Siamese network | 孪生网络 | 首次出现括注英文 |
| Euclidean loss | 欧氏损失 | |
| attribute-adaptive model | 属性自适应模型 | |
| content-adaptive model | 内容自适应模型 | |
| rater / worker | 评分者／工作者 | raters 一律「评分者」，AMT workers 视语境用「工作者」 |
| within-rater / cross-rater sampling | 评分者内／评分者间采样 | 全文统一 |
| Aesthetics with Attributes Database (AADB) | 美学与属性数据库（AADB） | 数据集名原样保留缩写 |
| AVA (Aesthetics Visual Analysis) | AVA 数据集 | 首次出现给出英文全称 |
| Spearman's rank correlation (ρ) | 斯皮尔曼秩相关 | 符号 ρ 原样保留 |
| Kendall's τ | Kendall τ | 指标符号原样保留 |
| false discovery rate (FDR) | 错误发现率 | Benjamini-Hochberg 程序，算法名不译 |
| rule of thirds | 三分法 | 摄影构图术语 |
| depth of field | 景深 | |
| motion blur | 运动模糊 | |
| deep supervision | 深度监督 | 引自文献 [13] |
| softmax confidence score | softmax 置信度分数 | |
| content-specific branch | 内容特定分支 | |
| gate (verb) | 门控 | 用于对预测做加权组合 |
| Amazon Mechanical Turk (AMT) | Amazon Mechanical Turk（AMT） | 众包平台名，缩写保留 |
| long tail distribution | 长尾分布 | |
| permutation test | 置换检验 | |
| power rater | 重度评分者 | 指标注量大、一致性高的工作者 |
| transferability | 可迁移性 | 跨数据集泛化能力 |
| state-of-the-art | 最佳（性能） | 中文行文用「最佳性能」 |
| Spatial Pyramid Pooling (SPP) | 空间金字塔池化网络（SPP） | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0011 | Siamese network takes image pairs, predicts relative ranking; side-information: attributes + content | 孪生网络以图像对为输入，直接预测相对排序；旁支信息含美学属性与照片内容 | 一致，数字与引用编号未改动 |
| b0028 | 11 attributes; 10,000 images; 5 raters; split 500/1,000/rest | 十一项属性；10,000 幅图像；五位评分者；验证 500／测试 1,000／其余训练 | 数字逐项一致 |
| b0062 | Spearman's ρ definition, ranks r_i / s_i, range, threshold τ for binary | 斯皮尔曼 ρ 定义、秩记号、取值范围、二值化阈值 | 公式槽位 ⟦SLOT_44⟧–⟦SLOT_57⟧ 全部原样保留 |
| b0071 | Reg 0.4995 vs Reg+Rank 0.5126；Reg+Att 0.5331 vs Reg+Rank+Att 0.5445；within-/cross-rater 采样对比 | 同上，四个数值原样保留；采样策略名称与顺序一致 | 数值与结论一致 |
| b0098 | Conclusion: CNN 融合属性与内容；阈值化即达 SOTA；与「平均 MTurk 工作者」相当但落后于一致性更高的工作者 | 同上 | 一致，未添加原文没有的评价 |

### 一致性与数字核查

- 术语：以 Grep 复核「美学评分／美学排序／评分者／属性自适应／内容自适应／孪生网络／排序损失」等核心术语，全文译法唯一，未做同义轮换。
- 占位符：逐块比对 `translate_input.json` 中 `t:"text"` 块的 `⟦SLOT_n⟧` 集合与 `zh.json` 中对应译文的槽位集合，数量与编号完全一致（含 b0071 的 ⟦SLOT_60⟧–⟦SLOT_72⟧、b0167–b0170 的 Kendall/Spearman 槽位）。
- 数字：10,000 / 8,500 / 500 / 1,000 / 250,000 / 230,000 / 20,000、相关系数 0.4995、0.5126、0.5331、0.5445、0.5336、0.5445、阈值 5、学习率 0.0001、衰减因子 0.1、190 位工作者、2.5 倍等均原样保留，未换算或改写。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 未翻译内容：表格、公式、代码块、图片与参考文献块一律保持原文，未做处理。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文 b0071 段落中「Table 3 and 3」疑为排版笔误（应指表 2 与表 3），译文按原文直述为「表 3 与表 3」，未擅自更正。
- 附录中属性名（如 balancing element、vivid color）保留英文原词并括注中文，避免与正文术语表冲突。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax 已加载；46 处图片 `src` 均为 `figures/` 相对路径，无 http 外链；无 U+FFFD；顶部中文标题与摘要齐备，底部有「返回总目录」链接。
- 抽查块（6 块，seed=2）：b0007、b0049、b0078、b0096、b0010、b0074 —— 语义完整、数字与公式槽位一致、术语统一，未发现实质错误。
- 全量机器复核另发现 3 处公式槽位顺序与 EN 不一致（语义正确但编号顺序错位），已修正：

| 块 ID | 问题类型 | 修正前 | 修正后 |
|---|---|---|---|
| b0062 | 占位符顺序错位 | 记 ⟦SLOT_45⟧ 表示按分数 ⟦SLOT_47⟧ 排序时第 ⟦SLOT_46⟧ 个样本的秩 | 记 ⟦SLOT_45⟧ 表示第 ⟦SLOT_46⟧ 个样本在按分数 ⟦SLOT_47⟧ 排序时的秩（⟦SLOT_45⟧/⟦SLOT_46⟧/⟦SLOT_47⟧ 顺序与 EN 一致） |
| b0071 | 占位符顺序错位 | 对于 AVA 数据集 ⟦SLOT_71⟧ 幅测试图像上算得的、在 ⟦SLOT_70⟧ 附近的 ⟦SLOT_69⟧ 值 | 当 ⟦SLOT_69⟧ 取值在 ⟦SLOT_70⟧ 附近（在 AVA 数据集的 ⟦SLOT_71⟧ 幅测试图像上计算得到）时（顺序 69→70→71→72 与 EN 一致） |
| b0169 | 占位符顺序错位 | 总计 ⟦SLOT_124⟧ 个批次中有 ⟦SLOT_123⟧ 个批次具有显著一致性 | ⟦SLOT_123⟧ 个批次具有显著一致性（全部批次共 ⟦SLOT_124⟧ 个）（顺序 122→123→124 与 EN 一致） |

- 已重跑 `build_index.py`：`missing` 0 / `stray` 0 / `mojibake` 0 / `missing_img` 0。
