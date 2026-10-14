# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 195（文本 123 / 原子 72）|
| 已译文本块 | 123 / 123 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 0 · 已还原 0 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 10 |
| `<img>` 元素 | 18 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| large vision–language model (LVLM) | 大视觉语言模型（LVLM） | 首次出现附英文全名与缩写 |
| LVLM judge | LVLM 裁判 | 全篇统一，未用"评判模型""评审器"等异译 |
| text-to-image (T2I) generation | 文本到图像（T2I）生成 | 缩写保留 |
| text–image alignment | 图文对齐 | 全篇统一 |
| visual bias | 视觉偏置 | bias 在评测语境一律译"偏置"，未混用"偏见" |
| image-induced bias | 图像诱发偏置 | 摘要中的提法 |
| meta-evaluation benchmark | 元评测基准 | 指对评测器本身的评测 |
| FRAME (Fine-gRained Assessment of Multi-domain Evaluation) | FRAME（多领域评测的细粒度评估） | 系统名保留不译，首次出现括注全称中文 |
| adversarial visual manipulation | 对抗性视觉操纵 | 未用"恶意篡改"等带价值判断的词 |
| attack success rate | 攻击成功率 | 指标名 |
| Bounding Box Highlighting | 边界框高亮 | 八类偏置之一 |
| Authenticity Overlay | 真实性叠加 | 叠加「Reference Image」字样 |
| Keyword Overlay | 关键词叠加 | 同上 |
| Instruction Overlay | 指令叠加 | 同上 |
| Beauty Filter | 美颜滤镜 | 同上 |
| Brightness Adjustment | 亮度调整 | 同上 |
| Gamma Correction | 伽马校正 | 同上 |
| Black Padding | 黑色填充 | 同上 |
| overlay / padding / bounding box | 叠加 / 填充 / 边界框 | 三个操作动词分别固定译法 |
| prompt-based mitigation | 基于提示的缓解 | 未用"减轻""消除" |
| Chain-of-Thought (CoT) prompting | 思维链（CoT）提示 | 首次出现附中文全称 |
| bias-aware prompt | 偏置感知提示 | 三种提示模板之一 |
| pairwise evaluation | 成对评测 | 与单图评测相对 |
| position bias | 位置偏置 | 成对比较中需控制的干扰 |
| win rate | 胜率 | 成对比较结果 |
| ground-truth | 真值 | 未用"地面真值" |
| reward signal | 奖励信号 | 训练语境 |
| reinforcement learning with human feedback (RLHF) | 人类反馈强化学习（RLHF） | 首次出现附缩写 |
| domain | 领域 | 五个视觉领域 |
| visual concept | 视觉概念 | 基准构建中的元素类别 |
| perturbation | 扰动 | 指对指令概念的受控改动 |
| human annotator | 人工标注者 | 打分人员 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0010 | 定义一组视觉偏置并考察是否抬高分数；列举亮度调整、伽马校正、文字叠加、黑色填充、美颜滤镜、边界框共六类 | 六类偏置按原顺序逐项译出，译名与第 3 节小标题严格对应 | 语义一致，类别数与顺序未变 |
| b0042 | 五个领域（Animals、People、Outdoor、Indoor、Illustrations），每域 100 个实例，共 500 个 | 五个领域名与两个数字原样保留，"evaluation instances"译为"评测实例" | 语义一致，数字未改动 |
| b0051 | 扰动示例：三只火烈鸟/草地 → 四只火烈鸟/热带雨林，说明改动概念越多对齐度越低 | 两句英文指令原样保留未译（属示例原文），论证部分完整译出 | 语义一致，示例指令未被改写 |
| b0074 | 攻击成功率定义；GPT-4o-mini 64.71% 对 GPT-4o 67.65%；Qwen2.5-VL-32B-Instruct 在平均百分比变化上最稳健 | 三个数值与两个模型名原样保留，"model capacity"译为"模型容量" | 语义一致，数值与模型名未改动 |
| b0166 | 偏置配方：缩放因子集合 16 个值、五个叠加位置、字号 30/20、填充厚度 7 个值、GFPGAN 与 makesense.ai 链接 | 两组数值集合与两个 URL 原样保留，字号与位置枚举完整译出 | 语义一致，参数集合未增减 |

### 一致性与数字核查

- 术语核查：用 Grep 复查「LVLM 裁判」「视觉偏置」「图文对齐」「攻击成功率」「成对评测」「偏置感知提示」等核心词，全文译法唯一；八类偏置的译名在第 3 节小标题、正文与表注中完全一致。
- 数字核查：500、100、2.57、2.52、2.66、2.36、2.48、2.84、64.71%、67.65%、2.0/2.1/2.3 等缩放因子、字号 30 与 20、填充厚度集合 [10, 15, 20, 25, 30, 40, 50]，以及表 6 中 +8.4%/+14.0%/+4.3%/+17.1% 等全部数值均与原文一致，未做四舍五入或单位换算。
- 占位符核查：本篇 `translate_input.json` 的文本块中不含 `⟦SLOT_n⟧`（槽位仅出现在公式块内），脚本 `stray` 为 0。
- 编码核查：`zh.json` 与 `index.html` 中均未检出 U+FFFD。
- 表格、公式、图片与参考文献块按规则保留原文未译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文 b0071、b0087、b0088、b0092、b0162 中含脚注编号与正文混排（如 `domains.22 2 Note that...`），系原文排版残留，译文照原样保留在相应位置，未加改写。
- b0164 原文写「pairwise evaluation (Table 3)」，而图注与正文实际指向图 3；译文按原文表述保留「表 3」，未作更正，仅作记录。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；18 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0188、b0008、b0045、b0104、b0079、b0011（seed=2）；加抽 b0042、b0032、b0090（seed=7）
- 另复核短译文块 b0050（331→82 字符，语义完整）。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
