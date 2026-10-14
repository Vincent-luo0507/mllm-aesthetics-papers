# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 364（文本 256 / 原子 108）|
| 已译文本块 | 256 / 256 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 149 · 已还原 149 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 400 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 42 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| reward model | 奖励模型 | 全文统一，未与“打分模型”混用 |
| reward signal | 奖励信号 | 含“高保真奖励信号”等搭配 |
| reinforcement learning (RL) | 强化学习 | 首次出现括注 RL |
| online RL | 在线强化学习 | |
| text-to-image (T2I) | 文生图（T2I） | 首次出现括注英文缩写 |
| flow matching | 流匹配（Flow Matching） | 公式语境保留英文 |
| Visual Language Model (VLM) | 视觉语言模型（VLM） | 缩写一律保留 |
| policy model | 策略模型 | 与“基座模型”区分 |
| base model | 基座模型 | 与 backbone 的“骨干”严格区分 |
| backbone | 骨干 | 如 Flux-Kontext-dev 骨干 |
| Prompt Following (PF) | 指令遵循（PF） | 基准三维度之一 |
| Consistency (C) | 一致性（C） | |
| Overall Quality (O) | 总体质量（O） | |
| Semantic Consistency (SC) | 语义一致性（SC） | VIEScore 的两轴之一 |
| Perceptual Quality (PQ) | 感知质量（PQ） | |
| pairwise accuracy | 成对准确率 | 评测指标，未改写 |
| Best-of-N | Best-of-N | 保留原写法，N 为 SLOT 占位符 |
| self-ensemble / inference-time ensembling | 自集成 / 推理时集成 | 同一策略两种表述，实指一致 |
| inference-time scaling | 推理时扩展 | 与“推理时集成”分指整体与具体手段 |
| ground truth | 真值 | |
| inter-annotator agreement | 标注员间一致性 | 含收敛率、一致率两个子指标 |
| Two-Annotator Discussion Protocol | 双标注员讨论协议 | 附录 B 专有名词 |
| tiered ranking | 分层排序 | 与“档位”配套 |
| preference pairs | 偏好对 | |
| reward hacking | 奖励破解 | 保留常用译法 |
| out-of-distribution (OOD) | 分布外（OOD） | |
| chain-of-thought | 思维链 | 首次出现括注英文 |
| score range | 分数区间 | 未译作“分值范围” |
| advantage estimation | 优势估计 | RL 术语 |
| artifact | 伪影 / 瑕疵 | 图像伪影用“伪影”，视觉缺陷用“瑕疵” |
| paired bootstrap test | 配对自助法检验 | 附录 D |

### 交叉验证记录（抽样 5 块）

| id | 原文要点 | 我的译文 | 语义一致性 |
|---|---|---|---|
| b0006 | 在线 RL 用于高分辨率编辑的障碍是缺少奖励函数；GPT-5 太贵，Qwen2.5-VL-72B 也不够准，会导致训练不稳或策略崩溃 | 译文完整覆盖“缺少合适奖励函数”“规模化调用成本高昂”“Qwen2.5-VL-72B 无法提供准确一致信号”“训练不稳甚至策略崩溃”四层意思 | 一致，无漏译、无增补 |
| b0029 | 基准分四类、13 子任务，来源 GEdit-Bench-EN 与 ImgEdit-Bench；四类为 Subject / Appearance / Scene / Advanced | 译文逐项列出四类及其子任务，数据集名与原文一致 | 一致，13 个子任务未删减 |
| b0061 | Qwen2.5-VL-72B 总体准确率仍不足 0.612，一致性判断劣于随机；EditScore-7B 超越十倍规模模型，72B 与 GPT-4.1 打平 | 数字 0.612、0.7–0.75、7B/32B/72B 均原样保留，未改动任何指标 | 一致，数字核对无误 |
| b0105 | GPT-4.1 标注准确率 0.637 对 0.638 略低，但标准差 2.868 对 2.533 更高；策略得分 6.375/6.292、5.834/5.768 两种评测下一致 | 全部六组数字按原文顺序保留，结论“方差而非绝对准确率是主导因素”完整译出 | 一致 |
| b0253 | 附录 F 推导 SDE，OmniGen2 的概率路径从噪声到数据的方向与 Flow-GRPO 相反，导致漂移项不同；推导三步 | 三步 (i)(ii)(iii) 与 SLOT 公式占位符全部按序保留 | 一致，公式占位符无遗漏 |

### 一致性与数字核查

- 术语一致性：已用脚本统计全文词频，`基座模型` 8 次、`基础模型` 0 次；`骨干` 4 次仅对应 backbone；`成对准确率` 8 次、`自集成` 14 次、`标注员` 32 次，未见同义轮换。模型名（OmniGen2、Qwen2.5-VL、GPT-4.1、GPT-5、Gemini-2.5-image-preview 等）、基准名（EditReward-Bench、GEdit-Bench、ImgEdit-Bench、EmuEdit）、算法名（Flow-GRPO、TempFlow-GRPO、GRPO、PPO、LoRA、K-center）全部原样保留。
- 数字核查：逐块核对了准确率（0.612、0.621、0.659、0.680、0.727、0.763、0.284、0.519、0.569、0.571）、标准差（2.868 / 2.533）、分数（6.375 / 6.292、5.834 / 5.768、22/25、0/25）、吞吐量（16.24、9.48、1.60 samples/s）、比例（12.12%、97%、99.55%、18 秒、20%、576 次）等，未作任何换算或改写；单位（TFLOPs、samples/s、H100 卡数、GB）保持原样。
- 占位符完整性：脚本比对显示 256 个文本块的 `⟦SLOT_n⟧` 集合与原文一一对应，零差异；构建脚本报告 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 中均不含 U+FFFD。

### 遗留问题

- 无图片缺失（构建脚本 `missing_img = 0`），5 张 `<img>` 均指向已下载的 `figures/` 本地文件。
- 附录 F 中原文“equation 10 don’t need a reverse SDE”等处句式残缺，已在中文里补足为主谓完整的表达，未改变数学含义。
- b0077 小节标题原文为 `best-of-⟦SLOT_40⟧ection`，即 “selection” 一词被公式占位符切断，属原文排版异常；译文按 “best-of-⟦SLOT_40⟧ 选择” 处理，与正文 b0075、b0014 的译法保持一致。
- `Fokker-Planck` 在原文中两种写法（Fokker-Planck / Fokker–Planck）并存，译文统一作 “Fokker-Planck 方程”（附录 F）与 “Fokker–Planck 方程”（b0253），连字符形式随原文，未强行统一。

## 复核记录（第二轮交叉验证）

抽查块：b0034、b0305、b0050、b0233、b0174、b0229


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
