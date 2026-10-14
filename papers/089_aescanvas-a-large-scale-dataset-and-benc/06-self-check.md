# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 396（文本 225 / 原子 171）|
| 已译文本块 | 225 / 225 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 87 · 已还原 87 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 266 |
| `<img>` 元素 | 31 |
| `<table>` 元素 | 33 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Aesthetic Assessment (IAA) | 图像美学评估（IAA） | 首次出现括注缩写 |
| aesthetic critique | 美学评论 | 全文统一，未写作「美学批评」 |
| contextual suitability | 上下文适配性 | 论文核心概念，全文统一 |
| contextual aesthetic suitability | 上下文美学适配性 | 与上一条配套，不省略「美学」 |
| aesthetic context bias | 美学上下文偏置 | 论文提出的失效倾向 |
| CritiqueCanvas / ContextCanvas | CritiqueCanvas / ContextCanvas | 两个组件名不译 |
| instruction–response pair | 指令-回答对 | 全文统一 |
| virtual imagery | 虚拟图像 | 与 photography、painting 并列 |
| aesthetic dimension | 美学维度 | 十个共享维度 |
| aesthetic-specific model | 美学专用模型 | 全文统一 |
| open-weight model | 开源权重模型 | 与 closed-source 对应 |
| closed-source frontier model | 闭源前沿模型 | 全文统一 |
| general-purpose MLLM | 通用 MLLM | 全文统一 |
| base–specialist transfer | 基座-专用模型迁移 | 表 S10 与图 4(a) 配套 |
| visual grounding | 视觉定位 | 全文统一，未写作「视觉接地」 |
| decisive cue / decisive evidence | 决定性线索 / 决定性证据 | 前者指视觉线索，后者指判断依据 |
| Evidence-Grounded Accuracy (EGA) | 证据定位准确率（EGA） | 论文定义指标 |
| Unsupported (rate) | 无支撑率 | EGA 审计中的派生指标 |
| Net Correct Update (NCU) | 净正确更新（NCU） | 反事实审计指标 |
| counterfactual pair / variant | 反事实配对 / 变体 | 全文统一 |
| over-acceptance | 过度接受 | 与 over-rejection 对应 |
| gold label / gold Yes rate | 金标签 / 金标准 Yes 率 | 全文统一 |
| exact-match accuracy | 精确匹配准确率 | 标准译法 |
| Macro-F1 | Macro-F1 | 指标名不译 |
| CLIPScore / BERT-F1 / SBERT-Cos | CLIPScore / BERT-F1 / SBERT-Cos | 指标名保留原文 |
| BLEU / ROUGE-L / METEOR | BLEU / ROUGE-L / METEOR | 指标名保留原文 |
| SacreBLEU | SacreBLEU | 工具名保留 |
| bootstrap confidence interval | bootstrap 置信区间 | 保留 bootstrap 不译 |
| McNemar test | McNemar 检验 | 专名保留 |
| Bonferroni correction | Bonferroni 校正 | 专名保留 |
| provenance | 出处 | 图像来源元数据 |
| rationale | 推理依据 | 与 gold label 配套，未写作「理由」 |
| anti-shortcut validity | 反捷径有效性 | 七项保留准则之一 |
| answerability | 可回答性 | 七项保留准则之一 |
| blocking issue | 阻断性问题 | 与非阻断性问题对应 |
| paired-image case | 成对图像案例 | 与单图案例对应 |
| domain prior | 领域先验 | 失效模式之一 |
| cultural-neighbor substitution | 文化近邻替换 | 失败子类型 |
| aesthetic-halo error | 美学光环错误 | 失败子类型 |
| salient-composition myopia | 显著构图短视 | 失败子类型 |
| source-scene anchoring | 源场景锚定 | 反事实审计发现的现象 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0015 | 四项贡献：519,136 组指令-回答对、54,300 张图像、301 个案例、发布清单 | 逐项照译，四项编号与数字原样保留 | 数字与结构完全对应 |
| b0031 | 图像池构成：21,294 张照片、17,939 幅绘画、15,067 张虚拟图像，合计 54,300 | 三个分项数字与合计原样保留 | 数字一致，无增补 |
| b0038 | ContextCanvas 的七项保留准则 | 七条逐项译出，编号 (1)–(7) 保留 | 无遗漏、无合并 |
| b0066 | 闭源模型准确率区间、系列内提升点数，含 ⟦SLOT_6⟧–⟦SLOT_12⟧ | 七个占位符按原编号原顺序保留 | 占位符与语义均一致 |
| b0221 | SacreBLEU 配置：最大阶数四、effective_order=True，四个占位符 | 配置项与占位符顺序均照原文 | 技术细节无改动 |

### 一致性与数字核查

- 术语统一性：已用 Grep 核查「美学评论」「上下文适配性」「视觉定位」「决定性线索」「美学专用模型」「推理依据」等核心术语，全文译法唯一；grounding 一律译为「定位」，未出现「接地/依据」混用。
- 数字核查：519,136 / 54,300 / 301 / 1,060 / 302 / 291 / 10 / 28.40% / 6,000 / 21,294 / 17,939 / 15,067 / 1,000 / 95.3% / 97% / 970 / 953 / 17 / 91.69% / 30% / 38.14% / 59.11–76.98% / 20.96–30.24% / 256 / 320 / 800 / 500 / 512 / 36 / 25.00–30.56 / 27.78 / 9.72 / 2.78 / 97.22% / 72 / 64 / 199.07 / 102.12 / 13.26 / 6.53 / 95.2% / 66.7% / 34.4% / 4.05 / 37.80% / 39.09% / 61% / 28–34 / 52% / 78% / 88% 等全部与原文一致；表 1–表 6、表 S1–表 S10 为 keep 块，未作改动。
- 占位符完整性：原文 87 个 `⟦SLOT_n⟧` 全部按原编号、原顺序保留，构建后 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 均不含 U+FFFD。

### 遗留问题

- 原文 b0081 与 b0084 均写作「As shown in Table 5」，而表 5 是 36 对反事实审计的结果表，表 4 才是人类与 MLLM 评分表；推测原文存在表号引用误差，译文按原文照写为「表 5」，未作修正。
- 原文 b0289（图 S5 图注）为不完整句（以分号结尾），按原文结构照译，未补全。
- 原文 b0010 与 b0013 为被图 2 图注截断的同一段落，译文分别独立成段，语义连贯性已在译文内部保持。
- 无图片缺失，无原文乱码。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；31 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0024、b0018、b0175、b0084、b0059、b0286（seed=2）；加抽 b0294、b0303、b0317（seed=7）
- 另复核短译文块 b0052（213→50 字符，语义完整）。数值 21,294／17,939／15,067、NCU 25.00–30.56、2.78、27.78、9.72、97.22% 等均原样保留。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
