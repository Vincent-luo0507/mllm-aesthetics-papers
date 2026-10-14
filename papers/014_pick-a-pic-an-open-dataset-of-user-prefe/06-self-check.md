# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 140（文本 95 / 原子 45）|
| 已译文本块 | 95 / 95 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 38 · 已还原 38 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 82 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 9 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| text-to-image generation | 文本到图像生成 | 正文首次出现用全称，后文用“文生图” |
| prompt | 提示词 | 全文统一，不作“提示”或“指令” |
| user preference | 用户偏好 | 数据集核心对象 |
| scoring function | 评分函数 | PickScore 的函数形式 |
| reward model | 奖励模型 | InstructGPT 的目标来源 |
| tie | 平局 | 两幅图像无显著优劣 |
| win ratio / win rate | 胜率 | 统一译法，不轮换 |
| lose ratio | 负率 | 与胜率、平局率并列 |
| classifier-free guidance (CFG) scale | 无分类器引导（CFG）尺度 | 首次括注 CFG |
| backbone model | 骨干模型 | Stable Diffusion 系列 |
| crowd worker | 众包标注者 | 与真实用户对举 |
| inter-rater agreement | 标注者间一致性 | 标注策略比较指标 |
| annotator | 标注者 | 专家级标注者 |
| NSFW | NSFW | 保留原文缩写 |
| validation / test / training set | 验证集 / 测试集 / 训练集 | |
| preprocessing | 预处理 | 数据集划分小节 |
| KL-divergence | KL 散度 | 目标函数的距离度量 |
| temperature parameter | 温度参数 | CLIP 的标量参数 |
| in-batch negatives | 批内负样本 | 附录中的替代损失 |
| warmup | 预热 | 学习率调度 |
| checkpoint | 检查点 | 模型选择依据 |
| hyperparameter search | 超参数搜索 | 未开展 |
| Fréchet Inception Distance (FID) | 弗雷歇 inception 距离（FID） | 首次括注 |
| Elo rating | Elo 评分 | 迭代式评分系统 |
| per-instance score | 逐样本分数 | 与 FID 的集合级度量对举 |
| random seed | 随机种子 | |
| prompt template | 提示词模板 | 含空模板 |
| text-alignment | 文本对齐 | CLIP-H 分数含义 |
| weak supervision | 弱监督 | 如 RLHF |
| aesthetics predictor | 美学预测器 | 基线之一 |
| superhuman performance | 超人性能 | 超过专家标注者 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性 |
|---|---|---|---|
| b0008 | 微调 CLIP-H、InstructGPT 式目标、PickScore 70.5% vs 人类 68.0%、CLIP-H 60.8%、美学预测器 56.8%，含脚注给出模型地址 | 四个百分数与脚注 URL 全部保留，语义对应 | 一致 |
| b0024 | 四项质量控制：身份认证、监控封禁、NSFW 词组清单、1000 次交互上限；含脚注说明用户同意与匿名化 | 四项措施与脚注内容均译出 | 一致 |
| b0030 | 968,965 次排序、66,798 提示词、6,394 用户、583,747 训练样本、500/500、37,523 提示词、4,375 用户 | 七个数字原样保留 | 一致，无换算 |
| b0051 | 4,000 步、学习率 3e-6、批大小 128、预热 500 步、8 块 A100、每 100 步验证 | 训练超参数与硬件信息完整保留 | 一致 |
| b0092 | 14,000 条偏好、45 个模型、4 个骨干、Elo 重复 50 次、⟦SLOT_31⟧–⟦SLOT_34⟧ 四个相关系数 | 数字与四个占位符顺序一致 | 一致 |

### 一致性与数字核查

- 术语：复核 zh.json，文本到图像生成、提示词、评分函数、平局、胜率、无分类器引导尺度、众包标注者等核心术语全文译法唯一。
- 数字：500,000、35,000、968,965、66,798、6,394、583,747、500、37,523、4,375、4,000、3e-6、128、500、100、70.5%、68.0%、60.8%、56.8%、0.917、-0.900、14,000、45、50、7.5、5、20、68.5%、90.5%、66.7、61.1、65.2 等均未改动。
- 占位符：以脚本逐块比对 `⟦SLOT_0⟧`–`⟦SLOT_37⟧` 共 38 处，修订 b0046 一处顺序后已完全一致，脚本 stray=0。
- 编码：zh.json 与 index.html 均不含 U+FFFD。

### 遗留问题

- 无缺失图片（missing_img=0）。
- 附录 b0134 / b0135 为数据集提示词原文示例，属于数据内容，按不译原则原样保留，仅译出数据集名前缀。
- 原文 b0102 中 “Pick-a-Pick” 疑为 “Pick-a-Pic” 的笔误，译文按 Pick-a-Pic 处理。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0081、b0008、b0042、b0104、b0057、b0059），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
