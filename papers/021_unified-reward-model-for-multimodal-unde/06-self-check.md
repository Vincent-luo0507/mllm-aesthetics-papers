# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 220（文本 126 / 原子 94）|
| 已译文本块 | 126 / 126 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 35 · 已还原 35 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 76 |
| `<img>` 元素 | 9 |
| `<table>` 元素 | 16 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| reward model | 奖励模型 | 全文统一，不译作「回报模型」 |
| human preference alignment | 人类偏好对齐 | 统一译法 |
| pairwise ranking | 成对排序 | 首次出现括注英文 |
| pointwise scoring / point scoring | 逐点打分 | 统一，不轮换为「单点评分」 |
| point sifting | 逐点筛选 | 指数据构建第二阶段 |
| Direct Preference Optimization (DPO) | 直接偏好优化（DPO） | 首次出现括注缩写，后文用 DPO |
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 后文用 VLM |
| Large Multimodal Model (LMM) | 大模态模型（LMM） | 沿用原文 LMM 写法 |
| text-to-video (T2V) | 文生视频（T2V） | 统一 |
| diffusion model | 扩散模型 | |
| backbone | 骨干网络 | 不译「主干网络」 |
| checkpoint | 检查点 | |
| pointwise score | 逐点分数 | |
| chosen / rejected | 选中 / 拒绝 | 偏好对两侧的固定译法 |
| cross-task synergy | 跨任务协同 | |
| multi-task learning | 多任务学习 | |
| macro accuracy | 宏准确率 | 指标名原样对应 |
| budget-matched control | 预算对齐对照 | 指步数对齐的实验控制 |
| group relative policy optimization (GRPO) | 组相对策略优化（GRPO） | |
| noised latent | 带噪潜变量 | |
| signal-to-noise ratio | 信噪比 | |
| gradient accumulation | 梯度累积 | |
| warm-up ratio | 预热比例 | |
| baseline | 基线 | 全文统一，不译「基准方法」 |
| benchmark | 基准 | 与 baseline 区分 |
| ablation | 消融 | |
| qualitative / quantitative | 定性 / 定量 | |
| prompt faithfulness | 提示忠实度 | |
| overfitting | 过拟合 | |
| generalization | 泛化性 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | 两点担忧：奖励模型任务专用；视觉任务相互关联、联合学习互相促进 | 两点问题：模型面向特定任务、缺综合偏好数据；任务互联、联合学习互惠 | 一致，数字与引用标记 [ ] 未改动 |
| b0028 | 整合现有数据集预处理，构建约 236K 样本的统一偏好数据集 | 约 236K 条样本，覆盖图像与视频理解与生成 | 一致，236K 原样保留 |
| b0042 | 三步流程：数据生成、成对排序（N/2 对）、逐点筛选 | 三步流程，N 个输出分为 N/2 对 | 一致，占位符 SLOT_0/1/2 数量与位置一致 |
| b0085 | 图像+视频理解联合训练较单任务整体准确率、宏准确率分别提升 5.3%、8.3% | 分别提升 5.3% 与 8.3% | 一致，数字未改动 |
| b0213 | Pick-a-Pic 剔除约 12% 并列对后约 851k 偏好对、58.9k 提示 | 剔除约 12%，约 851k 条偏好对，涵盖 58.9k 条提示 | 一致 |

### 一致性与数字核查

- 全文术语已统一：reward model→奖励模型、pairwise ranking→成对排序、pointwise scoring→逐点打分、chosen/rejected→选中/拒绝、baseline→基线、benchmark→基准，未出现同义轮换。
- 数字与指标逐一核对：236K、700K、7.4K、40K、73K、25K、10K、17K、4K、182k、37.6K、26.5k、1,250、851k、58.9k、900k、3.4%、5.3%、8.3%、12%、137k、1632、3200、1K 等均原样保留，未做单位换算。
- 模型名与数据集名（UnifiedReward、LLaVA-OneVision、Qwen2.5-VL、SDXL-Turbo、T2V-Turbo、FLUX.1-dev、Pick-a-Pic、EvalMuse、HPD、OIP、ShareGPTVideo、VideoDPO 等）全部保留原文。
- 占位符核查：`⟦SLOT_0⟧`—`⟦SLOT_34⟧` 在译文中逐一原样保留，编号未改写；脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片、参考文献块按规范跳过未译。

### 遗留问题

- 无。图片引用缺失数为 0，公式与表格均正常还原。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0101, b0189, b0032, b0030, b0071, b0044 / b0190, b0071, b0062, b0200, b0058, b0095
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0051, b0053 | 公式占位符顺序校验 | EN 为 ⟦SLOT_9⟧…⟦SLOT_13⟧ 顺次排列，ZH 中将 ⟦SLOT_13⟧（时间步 t）提前；b0053 中 ⟦SLOT_24⟧ 提前 | 经核对 slots 内容：b0051 ZH「在时间步 t 由 x_0^w、x_0^l 得到的带噪潜变量」与 EN 语义一致；b0053 ZH「来自偏好对数据集 D 的偏好回答 y_w」亦一致。合理换位，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
