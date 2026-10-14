# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 240（文本 161 / 原子 79）|
| 已译文本块 | 161 / 161 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 0 · 已还原 0 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 0 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 3 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| heuristic evaluation | 启发式评估 | 全文统一，不译为「启发式评价」 |
| heuristic / heuristics | 启发式准则 | 指具体准则条目时统一用此译法 |
| design guideline | 设计准则 | 与 heuristic 区分，前者偏成文规范 |
| guideline violation | 准则违反项 | 一处违反称「一处违反项」 |
| UI mockup | UI 原型稿 | 全文统一，不作「模型」「样机」 |
| large language model (LLM) | 大语言模型（LLM） | 首次出现括注英文，后文用「大语言模型」 |
| prompt | 提示 | 不译「提示词」，与 prompt chain「提示链」一致 |
| context window | 上下文窗口 | 保留 token 数原样，如 8.1k token |
| few-shot | 少样本 | 与 chain-of-thought「思维链」配套 |
| self-reflection | 自我反思 | 模型对自身错误原因的反思机制 |
| accuracy | 准确性 | 评分维度之一，1–3 分量表 |
| helpfulness | 有用性 | 评分维度之一，1–5 分量表 |
| inter-rater reliability | 评分者间信度 | Fleiss Kappa 即此处计算的指标 |
| Fleiss' Kappa | Fleiss Kappa | 指标名保留英文 |
| precision / recall / F1 | 精确率 / 召回率 / F1 | 指标名统一 |
| ground truth | 真值 | ground truth dataset 译「真值数据集」 |
| grounded theory coding | 扎根理论编码 | 定性分析方法 |
| thematic analysis | 主题分析 | 定性分析方法 |
| Layers panel | 图层面板 | Figma 界面组件 |
| semantic grouping | 语义分组 | Duan 等的 5 条准则，专名大写保留 |
| CrowdCrit | CrowdCrit | Luther 等的视觉设计原则集，保留原文 |
| Nielsen Norman 10 Usability Heuristics | Nielsen Norman 10 条可用性启发式准则 | 机构名保留 |
| Aesthetic and Minimalist Design | 审美与极简设计 | Nielsen 准则条目 |
| Consistency and Standards | 一致性与标准 | Nielsen 准则条目 |
| Recognition rather than Recall | 识别优于回忆 | Nielsen 准则条目 |
| Match Between System and Real World | 系统与现实世界的匹配 | Nielsen 准则条目 |
| Emphasis | 强调 | CrowdCrit 原则条目 |
| Figma plugin | Figma 插件 | 工具形态 |
| UI Snapshot | UI 快照 | 插件中记录评估时刻状态的截图 |
| high-fidelity / low-fidelity | 高保真 / 低保真 | 原型精度 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0009 | LLMs 适合自动化启发式评估的四条理由 + 两条保留意见；引用 OpenAI 2023、Lee 2020、Wang 2023、Lu 2022、Sanh 2022、Lee 2023 | 完整译出规则推理、准则文本化、偏好文本反馈、UI 推理与泛化四点，以及仅接受文本输入、产生幻觉两点；全部引文与年份保留 | 一致，无漏译、无增补 |
| b0092 | 52% / 19% / 29% 准确性分布，49% / 15% / 36% 有用性分布；CrowdCrit 最优、Semantic Grouping 准确性最差、Nielsen Norman 有用性最差 | 六处百分比原样保留，三套准则的优劣关系与原文一致 | 数字一致，比较关系未改动 |
| b0098 | 专家 72 处 → 拆分后 91 处；GPT-4 38 处有用；GPT-4 独有 9、共有 29、人类独有 62；合计 100 | 全部数字逐项对应，9+29+62=100 的关系在译文中同样成立 | 一致 |
| b0119 | 过度套用准则：UI C 线条粗细例子 + P7 引语 + X 与购物袋图标通用惯例 | 例子与引语均译出，未添加评论；Nielsen 准则名照原文语境处理 | 一致 |
| b0157 | 迭代后表现下降的解释：专家修改提升 UI → 剩余违反项减少 → 任务变难 → 检测出错误违反项；图 11 佐证 | 因果链完整保留，图 11 引用保留 | 一致 |

### 一致性与数字核查

- 术语：以 Grep 复查「启发式评估」「准则违反项」「UI 原型稿」「上下文窗口」「有用性」「准确性」等核心术语在 zh.json 中的用法，全文译法统一，未出现同义词轮换（如未混用「启发式评价」「违规」）。
- 数字：5.1、5.2、5.3 各节的百分比与违反项计数（52/19/29、49/15/36、39/26/35、33/16/51、72/91/38/9/29/62/100）、Fleiss Kappa 值（0.112、0.100、0.155、0.085）、上下文窗口（8.1k token）、参数量（1.7 万亿）、参与者规模（3/12/12、51/12/6/3 个 UI）均逐项核对，未改动。
- 模型名与准则名（GPT-4、GPT-3.5-turbo-16k、Claude 2、PaLM 2、Llama 2、GPT-4V、GPT-4-Turbo、CrowdCrit、Nielsen Norman）原样保留。
- 占位符：本文 161 个文本块中不含 `⟦SLOT_n⟧`，脚本 stray=0，与预期一致。
- 未翻译对象：参考文献、表格、代码块、图片均按 `t:"keep"` 跳过。

### 遗留问题

- 原文图注（如 b0002、b0048、b0240）中英文说明与无障碍描述文字（ltx_acm_description）连写在一起，译文按语义分为两句处理，未改动源文件。
- 5.4.8 原文有一处语法瑕疵（"regarding how to fixing the violation"），译文按正确语义处理为「关于如何修复违反项的部分」，未加注释。
- 图片引用全部命中，missing_img=0，无缺失图片。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0051、b0125、b0013、b0155、b0098、b0089），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
