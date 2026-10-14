# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 192（文本 117 / 原子 75）|
| 已译文本块 | 117 / 117 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 97 · 已还原 97 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 208 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 10 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| front-end engineering | 前端工程 | |
| webpage | 网页 | 全文统一 |
| screenshot | 截图 | |
| visual element | 视觉元素 | |
| block (element block) | 区块（元素区块） | 检测模块输出的基本单位 |
| Block-Match | 区块匹配 | 自动指标之一，保留 Block-Match 写法 |
| text-augmented prompting | 文本增强提示 | 三种提示方法之一 |
| self-revision prompting | 自我修订提示 | |
| direct prompting | 直接提示 | |
| bounding box | 边界框 | |
| DOM tree | DOM 树 | |
| high-level visual similarity | 高层视觉相似度 | |
| low-level element matching | 低层元素匹配 | |
| inpainting | 图像修复 | Telea 算法场景 |
| Jonker-Volgenant algorithm | Jonker-Volgenant 算法 | 保留原名 |
| Sørensen-Dice similarity | Sørensen-Dice 相似度 | 保留原名 |
| CIEDE2000 | CIEDE2000 | 色差公式名保留 |
| CLIP embedding | CLIP 嵌入 | |
| top-down processing | 自上而下加工 | 认知科学术语 |
| pairwise model comparison | 成对模型比较 | |
| direct assessment | 直接评估 | |
| Win / Tie / Lose | 胜 / 平 / 负 | 人工评测三类结果 |
| stand-alone | 独立自足 | 指网页不依赖外部文件 |
| placeholder file | 占位文件 | rick.jpg |
| finetune / LoRA rank / warmup | 微调 / LoRA 秩 / 预热 | |
| Fleiss' kappa | Fleiss' kappa | 保留 |
| simulated win rate | 模拟胜率 | |
| dual use | 双重用途 | 伦理章节 |
| reciprocal / proxy difficulty indicator | 代理难度指示量 | |

### 交叉验证记录

| id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0018 | 长度均值 31216（min 784、max 98637、std 23903）、标签总数 158（12/528/100）、DOM 深度 13（4/32/5）、唯一标签 22（8/45/6）、84 种 HTML5 标签 | 全部统计数值与括号内的 min/max/std 原样保留 | 一致 |
| b0024 | 区块检测、Jonker-Volgenant 最优匹配、文本相似度匹配 | 完整译出，保留 ⟦SLOT_5⟧–⟦SLOT_17⟧ 共 13 处占位符 | 一致 |
| b0049 | Prolific 招募、每小时 16 美元、采样 100 个样例、⟦SLOT_40⟧ 名标注者多数投票 | 数值与平台名原样保留 | 一致 |
| b0054 | 49% 可互换、64% 被偏好 GPT-4V 生成的网页 | 两个百分比原样保留 | 一致 |
| b0167 | CogAgent-18B 基座、WebSight 823K 采样 20%、LoRA 秩、批大小、学习率 1e-5、A6000、2 天 | 逐项对应，保留 ⟦SLOT_59⟧–⟦SLOT_66⟧ | 一致 |

### 一致性与数字核查

- 术语统一性已用 Grep 复核：网页、截图、视觉元素、区块匹配、文本增强提示、自我修订提示、直接提示、独立自足、模拟胜率等译法全文唯一。
- 全部数字原样保留：484、80、127.9k、14k、7k、200、31216/784/98637/23903、158/12/528/100、13/4/32/5、22/8/45/6、84 种标签、120 个采样（25%）、100k token、100 个评测样例、16 美元/小时、⟦SLOT_40⟧ 与 5 名标注者、49%、64%、79.9%、4096 token、823K、20%、1e-5、20 个开发集样例、26%、19%、30%–40%、0.25→0.84、0.48→1.00、0.87→0.91、0.85→0.91、2500 份问卷、98% 通过率、60 名参与者、8 个示例等均未改动；模型名（GPT-4o、GPT-4V、Claude 3 Opus、Gemini 1.0 Pro Vision、LLaVA-V1.6-Mixtral-7B、DeepSeek-VL-7B、Idefics2-8B、WebSight VLM-8B、CogAgent-18B、Design2Code-18B）、数据集名（C4、WebSight、Design2Code-HARD）、HTML 标签名与占位文件名 rick.jpg 全部保留原文。
- 占位符核查：本文 SLOT 编号 0–96，共 97 处；译文中逐一原样保留，编号未错位。脚本校验 `stray=0`、`missing=0`。
- 编码核查：`zh.json` 与 `index.html` 中不含 `�`（U+FFFD），脚本 `mojibake=0`。

### 遗留问题

- 无。图片文件齐全（`missing_img=0`），公式槽位全部还原。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0032, b0182, b0064, b0028, b0088, b0144 / b0079, b0025, b0051, b0041, b0071, b0044
- 结论：共记录 2 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0024, b0030, b0159, b0180 | 公式占位符顺序校验 | 多处 ZH 占位符顺序与 EN 不一致 | 逐条核对 slots 内容（如 b0024 的 I_R/I_G 与 R/G 集合、b0180 的 0/0/1 缩放值），ZH 语序与 EN 语义一致，属合理换位，未修改。 |
| b0169 | 数字一致性复核 | EN「2,500」在 ZH 中写作「2500」 | 仅千位分隔符差异，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
