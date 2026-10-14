# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 187（文本 104 / 原子 83）|
| 已译文本块 | 104 / 104 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 108 · 已还原 108 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 235 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 17 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Personalized Image Aesthetic Assessment (PIAA) | 个性化图像美学评估（PIAA） | |
| Generic Image Aesthetic Assessment (GIAA) | 通用图像美学评估（GIAA） | |
| Image Aesthetic Assessment (IAA) | 图像美学评估（IAA） | |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | |
| aesthetic bias | 美学偏见 | |
| stereotype bias | 刻板印象偏见 | |
| implicit bias | 隐性偏见 | |
| alignment / preference alignment | 对齐 / 偏好对齐 | |
| Aesthetic Perception | 美学感知 | 三个子任务之一 |
| Aesthetic Assessment | 美学评估 | 三个子任务之一 |
| Aesthetic Empathy | 美学共情 | 三个子任务之一 |
| Identity Frequency Disparity (IFD) | 身份频率差异（IFD） | |
| Normalized Representation Disparity (NRD) | 归一化表征差异（NRD） | |
| Aesthetic Alignment Score (AAS) | 美学对齐分数（AAS） | |
| demographic group / identity group | 人口群体 / 身份组 | 前者指人群，后者指形式化变量 |
| demographic parity | 人口均等 | |
| total variation distance | 全变差距离 | |
| Jensen-Shannon divergence (JS) | Jensen-Shannon 散度（JS） | |
| Kullback-Leibler divergence (KL) | Kullback-Leibler 散度（KL） | |
| one-hot encoding | 独热编码 | |
| output format set | 输出格式集合 | |
| rating level | 评分等级 | |
| PARA / LAPIS | PARA / LAPIS | 数据集名保留 |
| concept editing | 概念编辑 | |
| data re-balancing | 数据再平衡 | |
| fairness-aware post-training | 公平性感知的后训练 | |
| personally identifiable information (PII) | 个人身份信息（PII） | |
| Group Relative Policy Optimization (GRPO) | 组相对策略优化（GRPO） | |
| default (non-personalized) prompt | 默认（非个性化）提示 | |

### 交叉验证记录（随机抽样 5 块）

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0010 | 19 个 MLLM；小模型偏见更强、大模型更公平；22–25 岁、大学教育女性；共情任务默认女性、显式性别后转男性 | 各结论与两个年龄区间、教育描述逐项对应；17/19 之外的数字未出现 | 数字与结论一致 |
| b0041 | IFD 公式各符号含义（⟦SLOT_33⟧–⟦SLOT_47⟧）与非负性条件 | 12 个占位符原样保留，符号说明逐项对应 | 占位符与语义一致 |
| b0071 | PARA：31,220 张图像、438 名评分者；三类任务；分数范围 1–5 | 数值与任务名逐项对应 | 数字一致 |
| b0092 | 三项任务均强对齐女性偏好，19 个模型中 17 个；22–25 主导感知与评估，共情转向 18–21；评估任务最一致 | 各数量与年龄段原样保留 | 数字与结论一致 |
| b0185 | LAPIS 上 IFD 随规模下降（2B ⟦SLOT_108⟧ 38B）；Qwen2.5-VL-7B 最高；Q-Insight 有改善但仍中等 | 占位符与三句结论完整译出 | 语义一致 |

### 一致性与数字核查

- 术语统一性：用 Grep 复核「个性化图像美学评估（PIAA）」「刻板印象偏见」「美学偏见」「美学感知/美学评估/美学共情」「身份频率差异（IFD）」「归一化表征差异（NRD）」「美学对齐分数（AAS）」「人口群体」「身份组」「人口均等」等核心术语，确认全文译法唯一。
- 数字核查：31,220 张图像、438 名评分者、11,723 张艺术图像、24 名平均标注者与 552 名参与者、19 个模型、17/19 与 15/14/17 等对齐计数、22–25 与 18–21 年龄段、0–100 量表、1–5 分数范围等均逐项比对原文，未做任何换算或改写；统计量一律以占位符保留。
- 占位符完整性：108 个 ⟦SLOT_n⟧ 槽位在译文中数量与编号与原文完全一致。
- 编码检查：zh.json 与 index.html 中 U+FFFD 计数均为 0。

### 遗留问题

- 原文 b0081 把 IFD 与 NRD 分别展开为「Identity Fairness Deviation」与「Normalized Response Deviation」，与第 3.2 节的「Identity Frequency Disparity」和「Normalized Representation Disparity」不一致。为保持全文术语统一，译文在 b0081 沿用第 3.2 节的译名（身份频率差异 / 归一化表征差异），缩写 IFD、NRD 保持一致。
- 原文 b0112 含拼写错误（「evluates」「indentify」），译文按正确语义译出，未修改源文件。
- 原文 b0094、b0098、b0102（表 1/2/3 内容）为 `keep` 块，未翻译；表 1/2 中的英文组名（female、22_25、University 等）按原文保留在表格内，仅在表题译文中给出中文说明。



## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0113、b0081、b0032、b0031、b0093、b0109、b0058、b0014、b0180
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 发现并修正的问题：
  - **b0081**（指标名与所在块 EN 不一致）：「身份频率差异（IFD）与归一化表征差异（NRD）」 → 「身份公平性偏差（IFD）与归一化响应偏差（NRD）」（本块 EN 为 Identity Fairness Deviation / Normalized Response Deviation；论文 §定义处另作 Identity Frequency Disparity / Normalized Representation Disparity，其余各块 ZH 沿用后者，属原文自身不一致，此处按所在块 EN 直译）
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
