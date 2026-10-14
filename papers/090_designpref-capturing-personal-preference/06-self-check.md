# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 180（文本 96 / 原子 84）|
| 已译文本块 | 96 / 96 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 57 · 已还原 57 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 130 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| user interface (UI) | 用户界面（UI） | 首次出现附缩写，后文用 UI |
| generative UI design | 生成式 UI 设计 | |
| pairwise comparison | 成对比较 | 数据集基本单位 |
| preference rating | 偏好评级 | |
| rater | 评分者 | 指参与标注的设计师 |
| inter-rater disagreement | 评分者间分歧 | 全文统一，不写作"标注者分歧" |
| Krippendorff's alpha | Krippendorff's alpha | 统计量名保留原文 |
| Cohen's kappa | Cohen's kappa | 统计量名保留原文 |
| Likert scale | 李克特量表 | |
| rationale | 理由 | 设计师给出的文字解释 |
| identity-linked | 身份关联 | 指标签绑定评分者 ID |
| strength-aware margin | 强度感知间隔 | margin 首次出现附英文 |
| contrastive loss | 对比损失 | |
| retrieval-augmented generation (RAG) | 检索增强生成（RAG） | 首次出现附缩写 |
| UIClip | UIClip | 模型名保留 |
| UICrit | UICrit | 数据集/框架名保留 |
| decoder-style LMM | 解码器式 LMM | 与双编码器 CLIP 区分 |
| dual-encoder | 双编码器 | |
| pooled | 汇集式 | 非个性化的聚合基线 |
| personalized | 个性化 | 与 pooled 对举 |
| macro-averaging | 宏平均 | |
| Spearman rank correlation coefficient (SRCC) | Spearman 秩相关系数（SRCC） | 指标名与缩写保留 |
| binary accuracy | 二分类准确率 | |
| four-way accuracy | 四分类准确率 | |
| information architecture (IA) | 信息架构（IA） | |
| scannability | 可扫读性 | |
| affordance | 可供性（affordance） | 交互设计术语，首现附英文 |
| call-to-action | 行动召唤元素 | |
| chrome | 界面装饰 | 指非内容性的界面元素 |
| A/B testing | A/B 测试 | |
| zero-shot | 零样本 | |
| few-shot | 少样本 | |
| checkpoint | 检查点 | 模型权重快照 |
| IRB | IRB | 机构审查委员会，保留缩写 |
| screen type | 屏幕类型 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | 12,000 组成对比较、20 位设计师、Krippendorff's alpha = 0.25、28.5% 与 96% | 数字与统计量原样保留，Krippendorff's alpha 未译写 | 一致 |
| b0028 | 四点李克特量表四个选项 A≫B / A>B / B>A / B≫A，含 SLOT_0–SLOT_4 | 四个槽位按原文顺序嵌入对应选项后，15.55 美元与 90 分钟未改动 | 一致 |
| b0035 | 表单类 72.11%、32.71%；列表/拨号/搜索 66%–68%；条款页等 54%–57% | 全部百分比原样保留，SLOT_36 保留 | 一致 |
| b0075 | 前 SLOT_50 检索结果注入提示；单人 RAG 得 SLOT_51 个样本；SLOT_52 位设计师时返回 SLOT_53 个 | 五个槽位序列一致，聚合规则（取平均后四舍五入）表述准确 | 一致 |
| b0091 | 60.16% / 0.217（个性化）对比 55.07% / 0.126（冻结 UIClip）与 46.68% / SLOT_56（CLIP B/32） | 三组数字与槽位一一对应，模型名未改写 | 一致 |

### 一致性与数字核查

- 术语：pairwise comparison 统一为「成对比较」，preference 统一为「偏好」，disagreement 统一为「分歧」，personalized 统一为「个性化」而 pooled 统一为「汇集式」，四个等级标签（A≫B 等）的槽位写法全文一致。
- 数字与指标：12,000、600、400、106、1,378、20、13、7200/2400/360/120、72.11%、32.71%、66%–68%、54%–57%、60.16%、0.217、55.07%、0.126、46.68%、57.70%、58.89%、31.35%、38.53%、15.55 美元等均按原文字面保留；SRCC、CLIP B/32、Qwen3-VL-235B-Thinking 等模型与指标名未改动。
- 占位符：96 个文本块共 56 处 `⟦SLOT_n⟧`，生成前用脚本逐块比对槽位序列，全部一致；脚本校验残留为 0。
- 编码：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0），无不可解析块。
- 原文 b0030 中「⟦SLOT_10⟧ for ⟦SLOT_11⟧」为「取值—统计量名」的倒装结构，中文以括号注明对应关系以同时满足语序与槽位顺序，属已知折中。
- 补充材料 S2 提示集与 S3 标注指南的具体内容以表格/图片形式承载（未列入 text 块），中文仅保留小节标题。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0054`、`b0098`、`b0013`、`b0089`、`b0058`、`b0065`（种子 3）；`b0091`、`b0092`、`b0054`、`b0062`、`b0005`、`b0100`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。

### 其他说明

- `b0009` “12k” 译为“1.2 万”、`b0055` 的 7200/2400/360/120 加千分位写作 7,200/2,400/360/120，数值一致。
