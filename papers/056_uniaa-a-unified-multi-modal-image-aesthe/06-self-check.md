# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 272（文本 164 / 原子 108）|
| 已译文本块 | 164 / 164 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 8 · 已还原 8 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 33 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 10 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Aesthetic(s) Assessment (IAA) | 图像美学评估（IAA） | 首次出现给出中英对照，后文统一用 IAA |
| Multi-modal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 全文统一，不写作「多模态大模型」 |
| Large Language Model (LLM) | 大语言模型（LLM） | 与 MLLM 严格区分 |
| UNIAA / UNIAA-LLaVA / UNIAA-Bench | 原样保留 | 框架名／模型名／基准名，不译 |
| IAA Datasets Conversion Paradigm (IDCP) | IAA 数据集转换范式（IDCP） | 首次出现括号标注，后文用 IDCP |
| Aesthetic Perception / Description / Assessment | 美学感知／美学描述／美学评价 | 基准三大层级，译法固定 |
| visual instruction tuning | 视觉指令微调 | 固定搭配 |
| aesthetic attribute | 美学属性 | 不译作「审美属性」，避免同义轮换 |
| aesthetic comment | 美学评论 | 与 description（描述）区分 |
| mean opinion score (MOS) | 平均意见分（MOS） | 保留缩写 |
| in-domain / in-the-wild | 域内（In-Domain）／开放场景（In-the-Wild） | 数据集切分，固定对应 |
| vision encoder | 视觉编码器 | 固定 |
| score token | 分数词元 | 评分任务专用 |
| rating-level word | 评分等级词 | bad/poor/fair/good/excellent |
| logits | logits | 保留不译 |
| Spearman's rank correlation coefficient (SRCC) | 斯皮尔曼秩相关系数（SRCC） | 指标名保留缩写 |
| Pearson linear correlation coefficient (PLCC) | 皮尔逊线性相关系数（PLCC） | 指标名保留缩写 |
| Completeness / Preciseness / Relevance | 完整性／准确性／相关性 | UNIAA-Describe 三个评分维度 |
| Content and Theme / Composition / Color / Light / Focus / Sentiment | 内容与主题／构图／色彩／光线／对焦／情感 | 六个美学维度，全表统一 |
| rule of thirds | 三分法 | 构图术语 |
| Yes-or-No / What / How | 原样保留 | 三类问题题型，不做翻译 |
| Junior-level / Senior-level Human | 初级水平人类／资深水平人类 | 人类对照水平 |
| state-of-the-art (SOTA) | 当前最优（SOTA） | 缩写保留 |
| golden description | 黄金描述 | 专家参考描述 |
| AI Generated Content (AIGC) | 人工智能生成内容（AIGC） | 括号内保留缩写 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 结论 |
|---|---|---|---|
| b0010 | 提出 UNIAA，首次把 MLLM 引入 IAA；基线用 LLaVA 架构微调得 UNIAA-LLaVA；美学标注昂贵故提出低成本 IDCP | 译文完整覆盖上述四点，含「图 1」「图 1(a)」引用及 LLaVA 的两条引用 | 语义一致，无漏译、无增补 |
| b0035 | 不使用美学分数的原因：主观性强、跨数据集分数不可比；改用属性与描述获得零样本评分能力；补充实验用视觉编码器做监督训练取得 SOTA | 译文保留「为何不使用美学分数？」设问、第 5.3 节交叉引用与 SOTA 表述 | 语义一致，反问语气与论证结构保留 |
| b0076 | 感知实验结果，含 66.82%、78.48% vs. 74.74%、3.59%、60%、10%、30% 等数字 | 译文逐项保留全部数值与模型名（Qwen-VL、mPLUG-Owl2、ShareGPT-4V、Gemini Pro、GPT-4V） | 数字与专有名词零改动 |
| b0217 | 8 块 V100、16 小时／22 小时、2 epoch、学习率 2e-5、批大小 128 | 译文全部保留，单位与数量级未改动 | 数字一致 |
| b0249 | GPT 评测三维度提示模板，含 [MLLM_DESC]、[GOLDEN_DESC]、Score: 等占位串与 0/1/2 打分档 | 译文保留全部占位串与打分规则，仅译说明文字 | 占位串原样，语义一致 |

### 一致性与数字核查

- **术语统一**：用脚本对 `zh.json` 全文检索确认，「美学属性」「美学评论」「美学感知」「美学描述」「美学评价」「视觉指令微调」「视觉编码器」「域内／开放场景」等核心术语在正文与附录中译法完全一致，未出现同义词轮换（如未混用「审美属性」）。
- **占位符完整性**：逐块比对原文与译文的 `⟦SLOT_n⟧` 集合，8 个槽位（SLOT_0～SLOT_7）数量、编号、位置全部一致；构建脚本 `stray = 0` 印证。
- **数字与指标**：5,354、2,229、3,125、501、151/150/200、278,181、19,928、14,079、3,000、4,737、16/22 小时、2e-5、128、4e-6、32、4096、40 等全部原样保留；PLCC／SRCC、MOS、SOTA、logits、softmax 等指标与算法名未作翻译或改写；Excellent/Good/Fair/Poor/Bad 五个等级词与对应 5/4/3/2/1 分值原样保留。
- **编码检查**：`zh.json` 与 `index.html` 均不含 U+FFFD，构建脚本 `mojibake = 0`。
- **不变量**：表格、代码块、公式、图片与参考文献块均为 `t:"keep"`，未翻译；块与块严格一一对应，164 个文本块无合并、拆分或删减。

### 遗留问题

- 无图片缺失（`missing_img = 0`），8 张图片均已在 `figures/` 中命中。
- 原文 b0052 中出现的 `UNIIAA-QA`（多一个 I）为原文笔误，译文按原文照写为 `UNIIAA-QA`，未作修正。
- 原文 b0249 中「Summarize the rewritten aesthetic comments and your answers in Step2」自称 Step2，疑为 Step1 之笔误；译文按字面译为「你在第二步中的回答」，未擅自改动。


## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；8 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0251、b0030、b0055、b0079、b0023、b0014（seed=2）；加抽 b0055、b0024、b0062、b0054（seed=7）
- 另复核短译文块 b0046（641→158 字符，IDCP 三项优势「低成本／统一性／可扩展性」逐条对应，无漏译）。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
