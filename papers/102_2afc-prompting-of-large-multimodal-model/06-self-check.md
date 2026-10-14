# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 108（文本 55 / 原子 53）|
| 已译文本块 | 55 / 55 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 67 · 已还原 67 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 710 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 10 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| large multimodal model (LMM) | 大型多模态模型（LMM） | 全文主研究对象 |
| large language model (LLM) | 大语言模型（LLM） | 原文在 II-C 与 II-B 中混用 LLM/LMM，译文按原文用词分别译出，未作统一改写 |
| image quality assessment (IQA) | 图像质量评估（IQA） | |
| two-alternative forced choice (2AFC) | 二选一强制选择（2AFC） | 首次出现括注英文 |
| paired comparison | 成对比较 | |
| mean opinion score (MOS) | 平均意见分数（MOS） | |
| maximum a posterior (MAP) estimation | 最大后验（MAP）估计 | |
| maximum likelihood estimation (MLE) | 极大似然估计（MLE） | |
| Thurstone's case V model | Thurstone Case V 模型 | 模型名保留 |
| coarse-grained / fine-grained | 粗粒度 / 细粒度 | |
| consistency / accuracy / correlation | 一致性 / 准确性 / 相关性 | 三项评价指标，符号 κ/α/ρ 以占位符保留 |
| distortion type / distortion level | 失真类型 / 失真等级 | |
| synthetic distortion / realistic distortion | 合成失真 / 真实失真 | |
| presentation order | 呈现顺序 | |
| biased prediction / preference | 偏倚预测 / 偏倚偏好 | |
| no-reference IQA model | 无参考 IQA 模型 | 指 NIQE、DBCNN |
| Pearson linear correlation coefficient (PLCC) | 皮尔逊线性相关系数（PLCC） | |
| global ranking score | 全局排序分数 | |
| quality preference matrix | 质量偏好矩阵 | |
| ridge regularization | 岭正则化 | |
| outlier rejection | 异常值剔除 | |
| single stimulus continuous methodology | 单刺激连续质量标度法 | 主观实验方法名 |
| data contamination | 数据污染 | |
| spatial information / colorfulness | 空间信息量 / 色彩丰富度 | |
| Perron rank method | Perron 排序法 | |
| TrueSkill rating system | TrueSkill 评分系统 | 保留专名 |
| over-fitting | 过拟合 | |
| ground truth quality score | 真值质量分数 | |
| indicator function | 指示函数 | |
| cumulative distribution function (CDF) | 累积分布函数（CDF） | |

### 交叉验证记录（随机抽样 5 块）

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0007 | 图 1 说明：MOS 取值范围（占位符）；人类不受呈现顺序影响；IDEFICS-Instruct 判错；GPT-4V 与人类一致 | 逐项对应，占位符 ⟦SLOT_0⟧ 原样保留 | 语义与专名一致，未增删 |
| b0027 | 三条细粒度配对规则：同内容同类型异等级；同内容同等级异类型；同 MOS 区间的真实失真 | 三条规则分号并列，与图 2 (a)~(f) 对应 | 结构一一对应 |
| b0055 | 五个 LMM 及各自基座（LLaMA-9B / LLaMA-7B / InternLM-7B / LLaVA_v1.5-7B / GPT-4V）；八个数据集分合成与真实两组；主观测试受试者数、ITU-T BT.500 异常值剔除 | 模型名与基座参数、数据集名、方法名全部原样保留 | 数字与专名逐项核对一致 |
| b0056 | 轮数设为占位符；预定义 prompt 模板逐字给出 | 模板正文保持英文原样，仅说明文字译为中文 | 模板未被翻译或改写 |
| b0070 | MAP 与 MLE、Perron 排序法、TrueSkill 对比；MAP 与 TrueSkill 更优；仍选 MAP | 四种方法名称与结论完整保留 | 语义一致 |

### 一致性与数字核查

- 术语统一性：用 Grep 复核「大型多模态模型（LMM）」「图像质量评估（IQA）」「最大后验（MAP）估计」「平均意见分数（MOS）」「粗粒度/细粒度」「失真类型/失真等级」「合成失真/真实失真」等核心术语，确认全文译法唯一。唯一例外是原文自身在 II-B、II-C 中交替使用 LMM 与 LLM，译文按原文用词分别译为「大型多模态模型」与「大语言模型」，未擅自统一。
- 数字核查：数据集采样量、受试者人数、失真类型数（5 类）、失真等级数（5 级）、MOS 区间数（4 个）等均以占位符形式保留，未做任何换算或改写；表内数值属 `keep` 块，未翻译。
- 占位符完整性：67 个 ⟦SLOT_n⟧ 槽位在译文中数量与编号与原文完全一致（曾在 b0029 出现一次重复引用，已修正为与原文一致的单次引用）。
- 编码检查：zh.json 与 index.html 中 U+FFFD 计数均为 0。

### 遗留问题

- 原文第 II 节标题为「Probingg Pipeline」（Probing 多写一个 g），属原文笔误，译文按「探查流程的构成要素」处理，未修改源文件。
- 图 1 说明中出现「mPULG-Owl」，与正文统一的「mPLUG-Owl」拼写不一致，属原文笔误；译文保留原拼写 mPULG-Owl，未作纠正。
- b0042（表 I 标题）与 b0050（表 II 标题）原文句末缺少句号，为源文本截断，译文同原文不作补句。



## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0041、b0056、b0008、b0058、b0059、b0035、b0029、b0042、b0070、b0061
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
