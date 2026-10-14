# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 247（文本 125 / 原子 122）|
| 已译文本块 | 125 / 125 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 35 · 已还原 35 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 106 |
| `<img>` 元素 | 15 |
| `<table>` 元素 | 20 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| GenAI-Arena / GenAI-Bench / GenAI-Museum | 保留原名 | 平台、基准与数据池名 |
| text-to-image generation | 文本到图像生成 | 三项任务之一，全文统一 |
| text-to-video generation | 文本到视频生成 | |
| text-guided image editing / image edition | 文本引导图像编辑 / 图像编辑 | 依原文用词分别对应 |
| Elo rating (system) | Elo 评分（系统） | Elo 保留原文写法 |
| Bradley–Terry model | Bradley–Terry 模型 | 模型名保留 |
| maximum likelihood estimation (MLE) | 极大似然估计 | |
| logistic regression | 逻辑斯谛回归 | |
| sandwich standard errors | “三明治”标准误 | 统计学术语 |
| confidence interval | 置信区间 | |
| winning fraction / win rate | 胜率 / 平均胜率 | 语义一致时统一为胜率 |
| battle / match | 对战 / 对局 | battle 统一译“对战” |
| leaderboard | 排行榜 | |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现附缩写 |
| vote / voting | 投票 | |
| anonymous battle | 匿名对战 | |
| pre-computation | 预计算 | |
| NSFW filter / detector | NSFW 过滤器 / 检测器 | NSFW 保留 |
| side-by-side comparison | 并排比较 | |
| arena | 竞技场 | 通用名词；专有名 GenAI-Arena 保留 |
| diffusion transformer | 扩散 Transformer | |
| distillation | 蒸馏 | |
| DDIM inversion | DDIM 反演 | |
| plug-and-play | 即插即用 | |
| motion layer | 运动层 | |
| bootstrap | 自举 | 统计术语 |
| error bar | 误差棒 | |
| state-of-the-art (SOTA) | 最优（SOTA） | |

### 交叉验证记录（随机抽 5 块）

| id | 原文要点 | 我的译文 | 一致性结论 |
|---|---|---|---|
| b0009 | 自 2024-02-11 收集超 9000 票；SOTA 为 PlayGround V2.5、MagicBrush、StableVideoDiffusion（截至 2024-10-24）；热力图揭示 Elo 易被 easy/hard games 不均衡带偏 | 同上中文表述 | 一致；日期、票数、模型名全部保留 |
| b0035 | 四个投票选项：左更好 / 右更好 / 平局 / 两者都差，用于计算 Elo | 3. 用户可按偏好投票，选项为：1）左侧更好；2）右侧更好；3）平局；4）两者都差。这四个选项被用于计算 Elo 评分。 | 一致；四选项逐项对应 |
| b0074 | 图像生成 6300 票、Playground V2.5 第一、SDXL 第十三；StableCascade 第六、训练成本为 SD-2.1 的 10%；图像编辑 1154 票；文本到视频 2024 票 | 同上中文表述 | 一致；五个数字与模型排序未改动 |
| b0119 | 86.57% 有效；其中 76.24% 明显合理、93.07% 明显合理或模糊合理 | 同上中文表述 | 一致；三个百分比精确保留 |
| b0126 | 4.3k→1.7k；85.6% 性内容；1.1k→0.9k；87.5% 暴力犯罪、12.5% 性犯罪；1.2k→1.1k；MIT 许可 | 同上中文表述 | 一致；k 记法与百分比原样保留 |

### 一致性与数字核查

- 术语统一性：Grep 复核 zh.json，「文本到图像」「文本到视频」「Elo 评分」「排行榜」「胜率」「MLLM」「对战」「投票」等核心词全文译法唯一；arena 作为通用名词统一为“竞技场”，作为系统名保留 GenAI-Arena。
- 数字与指标：9000、6300、1154、2024、350、303、50、100、1000、1200、1100、120、5、42、10%、80%、60%、86.57%、76.24%、93.07%、4.3k/1.7k/1.1k/0.9k/1.2k、85.6%、87.5%、12.5% 等全部逐位保留；PSNR、SSIM、LPIPS、FID、IS、FVD、CLIPScore、CLIPSIM 等指标名保留。
- 占位符完整性：125 个文本块的 `⟦SLOT_n⟧` 序列与原文完全一致（mismatch 列表为空），构建脚本 stray=0。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD，编码为 UTF-8。

### 遗留问题

1. 原文 b0126 中 “GenAI-Bench11 1” 为脚注编号与正文粘连的排版残留，译文原样保留 “11 1” 并保留其后的 URL。
2. b0106 提到 “T2V-Turbo” 而上下文讨论的是 PlayGround 2.5，疑为原文笔误；为忠实原文未作改写。
3. b0082/b0084/b0086 与 b0076/b0078/b0080 为相同子图标签（a)(b)(c)，分属不同图，译文按各自位置照译。
4. 图片缺失 0，figures/ 资源齐全。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；15 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0010、b0048、b0229、b0019、b0053、b0223（seed=2）；加抽 b0032、b0008、b0227、b0022（seed=7）
- 另复核列表项块 b0036（274→65 字符，为四条投票规则之一，语义完整无漏译）。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
