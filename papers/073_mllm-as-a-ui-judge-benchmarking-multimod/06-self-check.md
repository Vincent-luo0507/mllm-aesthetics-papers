# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 189（文本 108 / 原子 81）|
| 已译文本块 | 108 / 108 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 77 · 已还原 77 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 161 |
| `<img>` 元素 | 8 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| user interface (UI) | 用户界面（UI） | 全文统一，未译作"界面"以外形式 |
| user experience (UX) | 用户体验（UX） | |
| multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | |
| LLM-as-a-judge | LLM 作为评判者 | 保留连字符概念的整体译法 |
| MLLM as a UI judge | MLLM 作为 UI 评判者 | 全文统一 |
| Likert scale | Likert 量表 | 量表类型名保留 |
| pairwise comparison | 成对比较 | |
| absolute score prediction | 绝对分数预测 | 与"排序预测"对照 |
| ranking prediction | 排序预测 | |
| mean squared error (MSE) | 均方误差（MSE） | |
| mean absolute error (MAE) | 平均绝对误差（MAE） | |
| Pearson correlation coefficient | Pearson 相关系数 | |
| Spearman's / Kendall's | Spearman / Kendall | 符号由 SLOT 承载，名字保留 |
| crowdsourcing | 众包 | |
| approval rating | 好评率 | MTurk 参与者筛选条件 |
| standard deviation | 标准差 | |
| ground truth | 真值 | |
| cognitive / perceptual / emotional factors | 认知／感知／情感因素 | 九因素的三主题 |
| Ease of use | 易用性 | 九因素之一，与原文一一对应 |
| Clarity | 清晰度 | |
| Visual Hierarchy | 视觉层级 | |
| Memorable | 记忆度 | |
| Trust / Trustworthy | 信任感 / 可信度 | 正文用"信任感"，表 2 沿用原文 Trustworthy 处译"可信度" |
| Intuitive | 直觉性 | |
| Aesthetic Pleasure | 审美愉悦 | |
| Interesting | 趣味性 | 图表引述时加引号保留原词 |
| Comfort | 舒适感 | |
| cognitive load | 认知负荷 | |
| design heuristics | 设计启发式 | |
| A/B testing | A/B 测试 | |
| RLHF | 基于人类反馈的强化学习（RLHF） | 首次出现括注 |
| chain-of-thought | 思维链 | |
| few-shot learning | 少样本学习 | |
| bin | 分箱 | |
| approximator | 近似器 | 与"替代品（replacement）"对照 |

### 交叉验证记录（抽样 5 块）

| id | 原文要点 | 我的译文 | 语义一致性 |
|---|---|---|---|
| b0008 | 任务 1 的准确率 SLOT_0 得分 >75%，Pearson/Spearman/Kendall tau 呈中等偏强相关；任务 2 在人类分差大时更准；MLLM 应补充而非替代 | 三项统计量与"补充而非替代"的结论完整译出，75% 阈值原样保留 | 一致，无漏译 |
| b0047 | 15,000 份回答、500 名参与者、MTurk、好评率 >98%、至少 500 份经历、30 个 UI、45 秒—1 分钟、每 UI 75 美元、总计 2,250 美元 | 七组数字全部原样保留，未换算币种或时间单位 | 一致，数字核对无误 |
| b0065 | MSE/MAE/准确率/⟦SLOT_29⟧-准确率四项指标的定义与计算范围 | 四项定义逐条对应，"平方的均值""绝对值的均值""四舍五入后的人类分数"等限定均保留 | 一致 |
| b0071 | 趣味性 MSE/MAE 最高但相关性最高；舒适感 MSE/MAE 最低但相关性近零；两类指标视角不同 | 两个对照因素与"高相关≠低误差"的论点完整，未增删因果解释 | 一致，未添油加醋 |
| b0098 | 未来工作：RLHF / 微调、扩展界面与设备、更多模型（Gemini、Qwen、GPT-4o mini）、思维链与少样本、同设计迭代对比 | 五个方向逐条对应，模型名与提示策略名全部原样保留 | 一致 |

### 一致性与数字核查

- 术语一致性：全文统一"用户界面（UI）""多模态大语言模型（MLLM）""Likert 量表""成对比较""近似器／替代品"。九项 UI 因素的译名（易用性、清晰度、视觉层级、记忆度、信任感／可信度、直觉性、审美愉悦、趣味性、舒适感）在正文与图表说明中保持一致。模型名（GPT-4o、Claude 3.5 Sonnet、Llama-3.2-11B-Vision-Instruct、Llama 3.2、Gemini、Qwen）、平台名（Amazon Mechanical Turk）、机构名（Nielsen Norman Group）与指标名（MSE、MAE、Pearson、Spearman、Kendall）均按原文保留。
- 数字核查：15,000、500、98%、30（UI）、24/6、75 美元、2,250 美元、45 秒—1 分钟、9,296、1–7 量表、0.50 Likert 点、MAE 0.53–0.64、MSE 0.44–0.66、Claude 48%、GPT 40%、75%–85% 一致率、55% 提升等均未作换算或改写；由 SLOT 承载的数值原样传递。
- 占位符完整性：108 个文本块的 `⟦SLOT_n⟧` 集合与原文逐块比对，零差异；构建脚本 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 中均不含 U+FFFD。

### 遗留问题

- 无图片缺失（`missing_img = 0`），8 张 `<img>` 均指向已下载的 `figures/` 本地文件。
- b0099 原文存在重复片段："the entirety of both the human and Firstly, the entirety of both the human and MLLMs tasks"，属原文编辑错误；译文按语义只呈现一次（"人类与 MLLM 的全部任务都在静态用户界面上进行"），未把重复片段照搬。
- b0011、b0028 含 PDF 抽取残留的脚注标记（`11 1 ...`、`22 2 ...`），已按原文位置内联保留，未单独拆块。
- b0039 原文末尾缺右括号前的句号，属原文标点不全；译文沿用原文收束方式，未补句号。
- b0028 中数据源 URL（https://reallygoodemails.com/）作为脚注内容原样保留，未作有效性核验。
- 原文 Trust / Trustworthy 两处写法并存，译文分别作"信任感"（第 3.2.2 节因素定义）与"可信度"（表 2、4.1.1 节的指标语境），已在术语表中说明。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0069`、`b0066`、`b0045`、`b0077`、`b0051`、`b0098`（种子 3）；`b0037`、`b0065`、`b0175`、`b0077`、`b0048`、`b0067`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
