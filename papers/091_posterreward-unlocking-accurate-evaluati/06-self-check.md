# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 311（文本 217 / 原子 94）|
| 已译文本块 | 217 / 217 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 58 · 已还原 58 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 136 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 17 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| reward model | 奖励模型 | 全文统一，不作「回报模型」等变体 |
| pointwise (reward modeling) | 逐点（pointwise） | 首次出现括注英文，后文只用「逐点」 |
| pairwise (reward modeling) | 成对（pairwise） | 与 pointwise 对举，全篇一致 |
| discriminative reward model | 判别式奖励模型 | 与「生成式奖励模型」对举 |
| generative reward model | 生成式奖励模型 | |
| preference data / preference pair | 偏好数据 / 偏好对 | |
| text-to-image (T2I) | 文生图 | |
| graphic design | 平面设计 | 不译作「图形设计」 |
| typography / typographical precision | 字体排印 / 字体排印精度 | 涉及字号、字距、字重等渲染细节时统一用此译法 |
| layout | 版式 | 指元素排布结果；「布局」用于指代布局能力本身 |
| rendering (text rendering) | 渲染（文字渲染） | |
| Chain-of-Thought (CoT) | 思维链（Chain-of-Thought, CoT） | 首次括注，后文用「思维链」或 CoT |
| test-time scaling | 测试时扩展 | |
| rejection sampling fine-tuning (RSFT) | 拒绝采样微调（RSFT） | |
| scoring module / analysis module | 打分模块 / 分析模块 | 两阶段架构的固定部件名 |
| logits | logits | 保留原文，不译 |
| Bradley–Terry loss | Bradley–Terry 损失 | |
| Group Relative Policy Optimization (GRPO) | 组相对策略优化（GRPO） | |
| position bias | 位置偏差 | 不译「位置偏置」 |
| Kendall's Coefficient of Concordance | Kendall 和谐系数 | 文中记号 W 以占位符保留 |
| Best-of-8 (Bo8) | Best-of-8（Bo8） | |
| MLLM-as-a-judge | MLLM 即评判者 | |
| cinematic / non-cinematic | 影视类 / 非影视类 | 数据集两大类目 |
| out-of-distribution (OOD) | 分布外（OOD） | |
| AI artifacts | AI 伪影 | |
| prompt fidelity / adherence | 提示词保真度 / 提示词遵循度 | 按原文两处用词分别对应 |
| creative brief | 创意简报 | 提示词模板中的固定说法 |
| MS-Swift / DeepSpeed | MS-Swift / DeepSpeed | 框架与并行库名原样保留 |
| Levenshtein edit distance | Levenshtein 编辑距离 | |
| chosen / rejected | 选中 / 拒绝 | 偏好对两侧的固定称谓 |
| flow matching | 流匹配 | |

### 交叉验证记录（随机抽样 5 块）

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0009 | 现有评估模型（HPSv3、UnifiedReward）只做通用图像偏好；HPDv3 中设计类仅占 9.9%，人物 29.4%、建筑 18.9%、艺术 18.2%；Flow-GRPO 等方法依赖可靠奖励模型 | 对应译出各模型名、四个百分比数值与三个 RL 方法名 | 数值与专名逐项核对一致，未增删 |
| b0040 | 影视类数据用 HPSv3 打分；Kendall 和谐系数（占位符）量化六轮排序一致性；取 2 万英文 + 1 万中文提示词组；45 万候选对；六轮排序至少五轮一致 → 16.4 万候选对 | 全数保留，占位符 ⟦SLOT_0⟧/⟦SLOT_1⟧ 原样保留 | 数字与占位符完整，语义一致 |
| b0077 | 8 张 A100；SFT/RSFT 全参数微调；第三阶段 LoRA（秩 64）；GRPO 用 8 训练 / 8 rollout / 4 部署奖励模型 | 逐项对应，两个学习率以占位符 ⟦SLOT_14⟧/⟦SLOT_15⟧ 保留 | GPU 数量与训练配置无遗漏 |
| b0196 | SD3.5-M 基座；8 张 A100 训练 + 4 张部署奖励模型；取 350 步模型；原始 CFG=4.5、微调 CFG=1.0；种子固定 0 | 全部数值原样保留 | 数字一致 |
| b0249 | 提示词模板第 3 条「Typographical Precision Analysis」：检查拼写、字族、样式、颜色、字重、大小写，以及字距、行距、对齐、比例 | 译为「字体排印精度分析」，各检查项一一对应 | 模板结构未改动，术语与前文统一 |

### 一致性与数字核查

- 术语统一性：用 Grep 复核了「奖励模型 / 逐点 / 成对 / 判别式 / 生成式 / 平面设计 / 字体排印 / 思维链 / 位置偏差 / 打分模块 / 分析模块」等核心术语，确认全文未出现同义轮换；模板段落（图 15、19、21 的五项评估标准）中重复出现的五条标准采用完全一致的表述。
- 数字核查：数据集规模（70K / 33K / 20K / 1.08M / 1.17M / 1740 / 1223 / 517 / 488 / 250 / 1500 / 600 / 4096 / 350）、准确率（86.5%、86.7%、78.6%、10.7%）与硬件配置（8/4 张 A100、LoRA 秩 64、CFG=4.5/1.0）均逐项比对原文，未作四舍五入或单位换算（原文百分比一律保留「%」）。
- 占位符完整性：58 个 ⟦SLOT_n⟧ 槽位在译文中数量与编号与原文完全一致，未改写、未删除、未在占位符内插入文字。
- 编码检查：zh.json 与生成的 index.html 中 U+FFFD 计数均为 0。

### 遗留问题

- 块 b0232（第 11 节末段）原文在 `translate_input.json` 中即止于「…ensuring that closed-source models adhere」，句子未完结。已按现有内容如实翻译，未做任何补写；未修改源文件。
- 图 5、图 8、图 11 等在原文中以 `object` 形式嵌入，脚本统计图片缺失为 0，无需处理。
- 原文摘要在 HTML 中被切分为两段（b0003、b0004）并标记为 `keep`，中文摘要已按 300～500 字要求写入 `meta.json` 的 `zh_abstract`，两段内容均已覆盖。



## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0000、b0243、b0077、b0240、b0267、b0231、b0052、b0100、b0059、b0025
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
