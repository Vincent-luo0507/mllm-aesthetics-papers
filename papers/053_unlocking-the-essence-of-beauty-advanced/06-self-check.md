# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 203（文本 100 / 原子 103）|
| 已译文本块 | 100 / 100 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 62 · 已还原 62 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 153 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 21 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Aesthetic Assessment (IAA) | 图像美学评估 | 全文统一 |
| Image Quality Assessment (IQA) | 图像质量评估 | |
| Mean Opinion Score (MOS) | 平均意见得分 | 首次出现补英文 |
| PLCC | PLCC（皮尔逊线性相关系数） | 缩写保留 |
| SRCC | SRCC（斯皮尔曼秩相关系数） | 缩写保留 |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型 | 首次出现补英文 |
| Relative-Absolute Policy Optimization (RAPO) | 相对—绝对策略优化 | 算法名 |
| AesCoT | AesCoT | 数据流水线名，保留 |
| cold start / bootstrapping | 冷启动 / 引导 | |
| chain-of-thought (CoT) | 思维链 | |
| supervised fine-tuning (SFT) | 有监督微调 | |
| reinforcement learning (RL) | 强化学习 | |
| policy gradient | 策略梯度 | |
| relative rank reward | 相对排序奖励 | |
| absolute error reward | 绝对误差奖励 | |
| binary reward | 二值奖励 | |
| advantage | 优势 | RL 术语 |
| KL penalty | KL 惩罚 | |
| clipping threshold | 裁剪阈值 | |
| out-of-distribution (OOD) | 分布外 | |
| backbone (model) | 基座模型 | |
| rationale / explanation | 推理依据 / 解释 | |
| critique | 评析 | 含批评性内容 |
| score leakage | 分数泄漏 | 数据过滤项 |
| token entropy | token 熵 | |
| entropy collapse | 熵坍缩 | |
| reward hacking | 奖励破解 | |
| over-appraisal | 过高评价 | |
| calibration | 校准 | 指分数校准 |
| aesthetic dimension | 美学维度 | |
| external expert (model) | 外部专家模型 | |
| ordinal consistency | 序数一致性 | |
| in-domain / cross-task | 域内 / 跨任务 | |

### 交叉验证记录

| id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0011 | AesCoT 五维度数据、RAPO 双目标、仅 15K 数据、PLCC/SRCC 提升 47.9%/34.8% | 逐条对应，数字 15K、47.9%、34.8% 原样保留 | 一致 |
| b0033 | AesCoT 流水线：遮蔽分数 → 五维度分析 → 拼接真实分数 → 过滤；差/中/优三档 0-0.4 / 0.4-0.7 / 0.7-1.0 | 完整译出，保留 ⟦SLOT_16⟧–⟦SLOT_23⟧ 与三档区间数值 | 一致 |
| b0042 | 假设美学分数服从高斯分布，成对比较概率 | 保留 ⟦SLOT_30⟧–⟦SLOT_36⟧ 全部占位符 | 一致 |
| b0076 | 15K 组合集 2:2:1；平均 PLCC 0.6337 / SRCC 0.6186；VisualQuality-R1 SRCC 0.5825、PLCC 0.4429 | 全部数值原样保留 | 一致 |
| b0180 | 超参数：生成数 4、σ 0.1、KL 系数 0.01 与 0.28、全局批 64、小批量 32、最大长度 1024、A100 | 逐项对应，保留 ⟦SLOT_56⟧–⟦SLOT_61⟧ | 一致 |

### 一致性与数字核查

- 术语统一性已用 Grep 复核：图像美学评估、图像质量评估、平均意见得分、基座模型、冷启动、思维链、相对排序奖励、绝对误差奖励、分布外、熵坍缩、奖励破解等译法全文唯一。
- 全部数字原样保留：47.9%/34.8%、15K、2:2:1、0.6337/0.6186、0.5825、0.4429、0.4097/0.4084、0.4847/0.4903、熵 1.609→0.716、AesCoT-3K 各档 1000/1000/1000、AesCoT-10K 2928/3312/3660、9:1 划分、批大小 64/32、长度 1024、KL 系数 0.01/0.28 等均未改动。
- 占位符核查：本文 SLOT 编号 0–61，共 62 处；译文中数量与编号逐一对应。脚本校验 `stray=0`、`missing=0`。
- 编码核查：`zh.json` 与 `index.html` 中不含 `�`（U+FFFD），脚本 `mojibake=0`。

### 遗留问题

- 无。图片文件齐全（`missing_img=0`），公式槽位全部还原。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0042、b0033、b0028、b0180、b0030、b0005、b0058、b0056、b0191
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
