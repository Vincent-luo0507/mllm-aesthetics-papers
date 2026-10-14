# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 182（文本 93 / 原子 89）|
| 已译文本块 | 93 / 93 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 46 · 已还原 46 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 163 |
| `<img>` 元素 | 9 |
| `<table>` 元素 | 8 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image quality assessment (IQA) | 图像质量评价（IQA） | 首次出现括注英文 |
| large multi-modality model (LMM) | 大型多模态模型（LMM） | |
| open-ended / open-range | 开放式 | open-range question 统一译「开放式问题」 |
| visual quality comparison | 视觉质量比较 | |
| comparative setting | 比较式设定 | |
| pairwise choice / listwise ranking | 成对选择 / 列表排序 | |
| instruction tuning | 指令微调 | |
| Co-Instruct | Co-Instruct | 模型与数据集同名，均不译 |
| Collaborative Instruction Tuning from Weak Supervisors | 来自弱监督者的协同指令微调 | 全称首次出现时给出中文 |
| Merge2Compare / Teach2Compare | Merge2Compare / Teach2Compare | 子集名不译，括注中文含义 |
| weak supervisor | 弱监督者 | |
| teacher / student | 教师 / 学生 | GPT-4V 与 Co-Instruct 的关系 |
| pseudo label | 伪标签 | |
| multi-choice question (MCQ) | 多选题（MCQ） | |
| Which question | Which 类问题 | 保留 Which，后缀统一为「类问题」 |
| Yes-or-No question | 是/否类问题 | |
| two-alternative forced choice (2AFC) | 二选一强制选择（2AFC） | |
| MOS | MOS | 不译 |
| Pearson's linear correlation | Pearson 线性相关系数 | |
| visual token | 视觉词元 | |
| visual abstractor | 视觉抽象器 | |
| image-text interleaved format | 图文交错格式 | |
| context window | 上下文窗口 | |
| top-similarity pair removal | 高相似度配对剔除 | |
| dev set / test set | 开发集 / 测试集 | |
| spot check | 抽查 | |
| ground truth | 真值 | |
| Completeness / Precision / Relevance | Completeness / Precision / Relevance | 评测维度名保留原文 |
| in-the-wild | 真实场景 | |
| artificially-distorted | 人工失真 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0013 | 19K 图像 → 100K 组；9K 图像 → 30K 组；整合 Q-Instruct-200K 得 Co-Instruct-562K | 三组数量与子集名逐一对应，数据来源顺序未变 | 一致 |
| b0041 | 剔除后保留 70K 对（86%）、20K 三元组（74%）、10K 四元组（55%） | 三个数量与三个百分比一一对应，未互换 | 一致 |
| b0050 | 9K 图像构成：5.4K 真实场景 + 1.8K 人工失真 + 1.8K AI 生成；编为 18K/6K/6K 组 | 四组数量与三个来源（YFCC-100M、COCO、KADIS-700K、ImageRewardDB）均对应 | 一致 |
| b0077 | 图像缩放至 N、学习率 N-N、批大小 N、两轮、8 张 A100、25 小时 | 数值全部落在 ⟦SLOT_25–28⟧ 内，硬件与耗时原样保留 | 一致 |
| b0084 | 比基线高 64%、比无比较数据变体高 51%、比最优开源高 23%；超 Qwen-VL-Max/Gemini-Pro 21%/33%；超教师 2.7% | 六个百分比与各自比较对象逐一对齐，无一错配 | 一致 |

### 一致性与数字核查

- 术语一致性：用 Grep 在 `zh.json` 中检索「图像质量评价」「大型多模态模型」「开放式」「视觉质量比较」「指令微调」「图文交错格式」「视觉词元」「多选题」「伪标签」「弱监督者」等核心术语，确认全文译法唯一；「开放式」未与「开放域」混用，「图像质量评价」未与「图像质量评估」混用。
- 数字与指标：所有数量（19K、100K、9K、30K、81K、27K、18K、70K、20K、10K、230K、2,000、1,004、996、499、1,999 等）、百分比（86%、74%、55%、96%、72%、94%、64%、51%、23%、21%、33%、2.7%、5.7%、6.4%、57%、59%、31%、55.2%、54.4% 等）、词元数（1,025、65）、上下文长度（2,048、4,096）均原样保留；模型与数据集名（Q-Pathway、Q-Instruct-200K、Q-Bench、Q-Align、mPLUG-Owl2、LLaMA-2、CLIP-ViT-L14、E5-Mistral、GPT-4V、Gemini-Pro、Qwen-VL-Max、LLaVA-v1.5-13B、InternLM-XComposer2、BakLLaVA、EMU2-Chat、A-OKVQA、YFCC-100M、KADIS-700K、ImageRewardDB）未做任何改动。
- 占位符完整性：写入前逐块比对原文与译文的 `⟦SLOT_n⟧` 列表，slot 0–45 全部一一对应；脚本校验 `⟦SLOT⟧` 残留为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 mojibake 计数为 0。
- 不变量：参考文献、表格、图片（`t:"keep"`）一律未翻译；正文块一块对一块，未合并或拆分。

### 遗留问题

- b0014、b0043、b0065 三块包含模型输入/输出格式模板（如 `User: The first image: <img…> … Assistant: <response>`）与提示词模板。这些是格式规范而非自然语言，故模板部分按原文保留，仅把周围的说明性文字译为中文。
- b0041 中原文用英文示例描述（"The quality is acceptable…" / "The clarity is good, but lighting is dark"），译文将其译为中文「质量尚可」「清晰度不错，但光线偏暗」，以便中文读者理解「高相似度剔除」的判据；占位符 ⟨img⟩ 编号未改动。
- 无图片缺失（missing_img = 0）。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0020`、`b0074`、`b0029`、`b0068`、`b0108`、`b0065`（种子 3）；`b0048`、`b0023`、`b0101`、`b0054`、`b0097`、`b0077`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
