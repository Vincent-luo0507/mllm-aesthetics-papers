# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 253（文本 152 / 原子 101）|
| 已译文本块 | 152 / 152 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 16 · 已还原 16 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 38 |
| `<img>` 元素 | 9 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| user interface (UI) | 用户界面 | 首次出现附 UI |
| UI design quality | UI 设计质量 | |
| design defect / flaw | 设计缺陷 | 全文统一 |
| design suggestion / design tip | 设计建议 / 设计提示 | 按语境区分，提示用于应用名 |
| design relevance | 设计相关性 | |
| jitter function | 扰动函数 | 本文核心术语，全文统一 |
| jittered / non-jittered | 被扰动的 / 未经扰动的 | |
| jitter | 扰动 | 名词义 |
| crawl / crawler | 爬取 / 爬虫 | |
| data augmentation | 数据增强 | |
| screenshot | 截图 | |
| caption | 描述 / 描述文本 | 与 defect 描述区分时写作「描述文本」 |
| CRAP principles | CRAP 原则 | 保留缩写，含对比/重复/对齐/亲密性 |
| contrast / repetition / alignment / proximity | 对比 / 重复 / 对齐 / 亲密性 | CRAP 四项固定译法 |
| large vision-language model (LVLM) | 大型视觉语言模型 | |
| dual-encoder | 双编码器 | |
| vision transformer | 视觉 Transformer | |
| embedding space | 嵌入空间 | |
| dot product | 点积 | |
| minibatch | 小批量 | |
| contrastive objective | 对比目标 | |
| pairwise contrastive objective | 成对对比目标 | |
| cross-entropy loss | 交叉熵损失 | |
| headless browser | 无头浏览器 | |
| sliding window | 滑动窗口 | |
| mean reciprocal rank (MRR) | 平均倒数排名 | 首次出现附 MRR |
| inter-rater reliability (IRR) | 评分者间信度 | |
| best-of-n sampling | best-of-n 采样 | 保留原文 |
| reward model | 奖励模型 | |
| heuristic evaluation | 启发式评估 | |
| macro-averaged F1 | 宏平均 F1 | |
| visual complexity | 视觉复杂度 | |
| color harmony | 色彩和谐 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0008 | 以 CLIP 为基础；通过修改样式与布局属性引入缺陷；生成 230 万对；另收集 1.2K 条设计师评分 | UIClip 基于广为人知的 CLIP 视觉语言模型……通过修改样式与布局属性刻意引入设计缺陷……生成了 230 万对 UI……收集了 1.2K 条专业设计师评分 | 一致，数值与专名未改动 |
| b0060 | 约 1200 条评分、剔除后 892 对、10 个预设配对、Krippendorff's alpha 为 ⟦SLOT_0⟧ | 我们共从所有参与者处收集了约 1200 条评分……最终得到 892 个评分对……同一组 10 个预设配对……Krippendorff's alpha 分数，为 ⟦SLOT_0⟧ | 一致，占位符原样保留 |
| b0081 | 短边缩放到 224；窗口在长边 ⟦SLOT_12⟧ 上滑动，步数 ⟦SLOT_13⟧；嵌入取平均 | 先把输入截图缩放，使其较短边等于 224 像素；随后一个 224x224 的窗口在尺寸为 ⟦SLOT_12⟧ 的长边上滑动，等间距步数等于 ⟦SLOT_13⟧……再把所有嵌入取平均 | 一致，2 个占位符顺序与原文一致 |
| b0112 | GPT-4V 整体 51.58%、约 10% 拒答；LLaVA 54.59% | GPT-4V（整体 51.58%）在约 10% 的样本上拒绝作答……LLaVA……预测准确率 54.59% | 一致 |
| b0152 | 合成屏幕 67.65% vs 真实应用 57.89%；全体模型 56.05% vs 51.50% | UIClip 对合成屏幕的评分准确率（67.65%）远高于对真实应用屏幕的准确率（57.89%）……56.05%）高于……（51.50%） | 一致，四项数值原样保留 |

### 一致性与数字核查

- 术语：全文统一使用「扰动函数」「设计缺陷」「设计质量」「截图」「小批量」「嵌入空间」「成对对比目标」；`UIClip`、`JitterWeb`、`BetterApp`、`CLIP`、`CLIP B/32`、`MetaCLIP H/12`、`GPT-4V`、`LLaVA`、`Qwen-VL-Chat`、`Screen2Words`、`VINS`、`RICO`、`CRAP`、`MRR`、`BLEU`、`ROGUE`、`Meteor`、`FID`、`CLIPScore`、`CLIP-IQA`、`TIFA` 等专名与指标名一律原样保留。
- 数字与指标：2.3 million（230 万）、99.9%、300,000、201、12、20-32、1.5、10、1200、892、618、73、151 million（1.51 亿）、224x224、32x32、512、77、400 million（4 亿）、75.12%、87.1%、73.88%、65.42%、51.58%、54.59%、87.11%、84.57%、49.17%、46.58%、0.3851、0.4085、67.65%、57.89%、56.05%、51.50%、2.5 billion（25 亿）、80%/10%/10%、70%/10%/20% 等数值均按原义保留，未作换算错误。
- 占位符：逐块脚本比对，`⟦SLOT_0⟧`–`⟦SLOT_15⟧` 共 16 处，译文与原文在编号、数量与出现顺序上完全一致；构建脚本 `stray=0`。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD；构建脚本 `mojibake=0`。
- 不变量：表格、公式、参考文献块未翻译；152 个 text 块一一对应，未做合并或拆分。

### 遗留问题

- 无图片缺失（`missing_img=0`）。
- 原文 b0044 含一段脚注（关于 OpenAI、Llama、Claude 服务条款限制），译文中按语义并入正文，未另起脚注，也未改动源文件。
- 原文 b0109 称结果「如图 5 所示」，而同段主题为设计质量（对应图 4），疑为原文笔误；译文按原文保留为「图 5」，未作推测修改。
- 原文 b0118 中的 "choice-adjusted F1" 译为「选择校正 F1」，属本文自创指标，未找到既定译法。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0129、b0014、b0086、b0036、b0038、b0024、b0073、b0110、b0034
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
