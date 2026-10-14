# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 530（文本 341 / 原子 189）|
| 已译文本块 | 341 / 341 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 159 · 已还原 159 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 405 |
| `<img>` 元素 | 29 |
| `<table>` 元素 | 57 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | 首次出现附英文，后文用 MLLM |
| Visual Aesthetic Benchmark (VAB) | 视觉审美基准（VAB） | 本文提出的基准名，副标题保留 VAB |
| aesthetic judgment | 审美判断 | 全文统一 |
| scalar score | 标量分数 | 与 score 统一 |
| comparative selection | 比较选择 | 不译作对比筛选 |
| candidate set | 候选集 | 全文统一 |
| matched subject matter | 主体内容一致 | 描述候选集内图片共享主体 |
| frontier model | 前沿模型 | 指当前最强商用/开源模型 |
| reward model | 奖励模型 | 专用视觉质量打分模型 |
| execution quality | 完成质量 | 指技法层面的实现水准 |
| inter-annotator agreement | 标注者间一致性 | 8 位专家之间的一致程度 |
| score-derived ranking | 分数导出排序 | 由绝对分数推得的次序 |
| pointwise scoring | 逐点评分 | 单图独立打分范式 |
| ap@1 | ap@1 | 三次排列评测的平均准确率，保留原名 |
| pass^3 | pass^3 | 三次全部正确的严格指标，保留原名 |
| Top-1 / Bot-1 / TB-1 | Top-1 / Bot-1 / TB-1 | 选最优 / 选最差 / 同时选最优与最差 |
| permutation | 排列 | 候选顺序的随机排列 |
| consensus filter | 共识过滤 | 双阈值真值保留准则 |
| Kendall’s τ | Kendall’s τ | 保真度指标，符号保留 |
| McNemar test | McNemar 检验 | 配对二值检验 |
| Wilcoxon signed-rank test | Wilcoxon 符号秩检验 | 熵比较用 |
| top-1 entropy | top-1 熵 | 可区分度指标 |
| homogeneous-content task | 同质内容任务 | 候选取自同一源任务 |
| heterogeneous-content task | 异质内容任务 | 候选跨源任务重组 |
| fine art / photography / illustration | 美术 / 摄影 / 插画 | 三个视觉领域 |
| Low-Rank Adaptation (LoRA) | 低秩适配（LoRA） | 微调方法 |
| vision tower | 视觉塔 | 被冻结的视觉编码器 |
| multimodal projector | 多模态投影器 | 微调时更新的模块 |
| greedy decoding | 贪心解码 | 温度消融对照项 |
| text-to-image / image-to-image | 文生图 / 图生图 | 生成模型类别 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0010 | VAB 含 400 任务、1,195 图、24 主题、2–6 张候选、10 位专家共识、三次排列、ap@1 与 pass^3 | 译文逐项对应，数字与指标名原样保留 | 一致，无漏译 |
| b0011 | Claude Sonnet 4.6 在 TB-1 pass^3 上 26.5%，人类 68.9%，差 42.4 个百分点；保留 ap@1 的 34–65%；SLOT_0/SLOT_1 两处下降幅度 | 数字与两个槽位原样保留，句式按中文断开 | 一致 |
| b0035 | 排序使三项指标分别提升 42.0、37.0、51.3 个百分点，McNemar 检验 | 数字与检验名原样保留 | 一致 |
| b0082 | 插画最难（19.0%），摄影 o4-mini 30.2%，GLM-4.6V 由 34.1% 降至 11.5% | 数字、模型名原样保留 | 一致 |
| b0237 | 零假设通过概率的穷举推导，含 SLOT_84–SLOT_91 | 8 个槽位顺序与数量完全对应 | 一致 |

### 一致性与数字核查

- 术语统一：以 Grep 核对 zh.json，全文统一使用「审美判断」「候选集」「完成质量」「标注者间一致性」「分数导出排序」「比较选择」「同质／异质内容」等译法，未出现同义轮换。
- 数字核查：400 / 1,195 / 24 / 2–6 / 10 / 20 / 6 / 26.5% / 68.9% / 42.4 / 42.0 / 37.0 / 51.3 / 0.188 / 0.351 / 45.5% / 52.0% / 0.729 / 1.213 / 10.1% / 0.8% / 1,142 / 1,809 / 908 / 2,000 / 35B / 397B 等数值均与原文一致，未作换算或改写。
- 占位符完整性：脚本自校验 `⟦SLOT⟧` 残留为 0，159 个内联槽位全部还原；另用脚本逐块比对原文与译文的 `⟦SLOT_n⟧` 序列，341 个文本块全部完全一致（含顺序）。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- Anime and Manga 与 Comic 两个主题名分别译为「动画与漫画」与「漫画」，中文相近，已在术语表中标注以便区分。
- 表格、代码块、公式与参考文献按规范未翻译，仅对正文中的表题与图题作了中文处理。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0342`、`b0184`、`b0317`、`b0213`、`b0412`、`b0311`（种子 3）；`b0014`、`b0057`、`b0277`、`b0373`、`b0201`、`b0255`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。

### 其他说明

- `b0029`/`b0036` 中 “8 annotators” 译为“八位标注者”、多数一致门槛“5 of 8”译为“至少 5/8”，数字关系正确。
