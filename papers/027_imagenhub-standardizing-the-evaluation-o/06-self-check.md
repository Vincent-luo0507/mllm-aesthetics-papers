# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 264（文本 173 / 原子 91）|
| 已译文本块 | 173 / 173 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 52 · 已还原 52 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 223 |
| `<img>` 元素 | 22 |
| `<table>` 元素 | 16 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| conditional image generation | 条件图像生成 | 全文统一译法 |
| text-guided image generation | 文本引导图像生成 | 七项任务之一，任务名固定 |
| text-guided image editing | 文本引导图像编辑 | |
| mask-guided image editing | 掩码引导图像编辑 | |
| subject-driven image generation / editing | 主体驱动图像生成 / 编辑 | subject 统一译“主体” |
| multi-concept image composition | 多概念图像组合 | |
| control-guided image generation | 控制引导图像生成 | |
| semantic consistency (SC) | 语义一致性（SC） | 人工评价指标 |
| perceptual quality (PQ) | 感知质量（PQ） | 原文偶作 perceptive quality，统一译作感知质量 |
| rater / worker | 评分员 / 工作者 | Prolific 平台上称 worker，评价语境称评分员 |
| inter-worker agreement / inter-rater reliability | 评分者间一致性 / 评分者间信度 | |
| Fleiss Kappa | Fleiss Kappa | 统计量名保留 |
| Krippendorff's Alpha | Krippendorff's Alpha | 统计量名保留 |
| geometric mean | 几何平均 | |
| leaderboard | 排行榜 | |
| artifacts | 伪影 | |
| unnatural sense | 不自然感 | |
| hyper-parameter tuning | 超参数调优 | |
| prompt engineering | 提示词工程 | |
| inference | 推理 | |
| latent diffusion model | 潜扩散模型 | |
| zero convolution | 零卷积 | ControlNet 术语 |
| textual inversion | Textual Inversion | 方法名保留 |
| standard deviation | 标准差 | |
| Prolific | Prolific | 众包平台名保留 |
| ImagenHub / Imagen Museum | 保留原名 | 系统与可视化工具名 |
| Inception score / FID / LPIPS / DreamSim / CLIP score / BLIP score / ImageReward | 保留原名 | 自动指标名 |

### 交叉验证记录（随机抽 5 块）

| id | 原文要点 | 我的译文 | 一致性结论 |
|---|---|---|---|
| b0010 | 推理阶段需大量超参数调优与提示词工程，调优投入不同导致比较不公平 | • 推理：部分工作需要大量超参数调优与提示词工程才能达到合理性能……由于不同模型在调优上的投入差异显著，其比较可能有失公平。 | 一致；未补入任何原文没有的推断 |
| b0026 | 掩码引导图像编辑的形式化定义，含 5 个槽位 | • 掩码引导图像编辑：⟦SLOT_11⟧……目标是对 ⟦SLOT_14⟧ 在掩码区域内的部分进行修改，使其符合 ⟦SLOT_15⟧。 | 一致；槽位顺序 11→15 与原文一致 |
| b0053 | 默认设置；停用负向提示词；3 名评分员；Fleiss kappa 与 Krippendorff's Alpha 的差别；区间 [-1,1] | 同上中文表述 | 一致；数字 3、-1、1 原样保留 |
| b0066 | 总体分为 SC 与 PR 的几何平均；加权和设定下 Text2Live 反超 CycleDiffusion 但人工检查相反；SC=0 且 PQ=1 | 同上中文表述 | 一致；分数取值与模型名未改动 |
| b0236 | 10 名评分员、15 个 Midjourney 样本；均值约 0.70；Alpha 从 3 人时 0.70 降到 10 人时 0.64；最终取 3 名 | 同上中文表述 | 一致；五个数字逐一核对无改动 |

### 一致性与数字核查

- 术语统一性：已用 Grep 复核 zh.json，「条件图像生成」「语义一致性」「感知质量」「评分员」「伪影」「潜扩散模型」「超参数调优」「几何平均」均为全文唯一译法；七个任务名在正文、附录与图注中完全统一。
- 数字与指标：100-200、7、83%、0.6、0.2、[-1, 1]、[0, 0.5, 1]、[0, 0.5, 1, 2]、150-200、10-20、15、10、3、4、5、0.70、0.64、42、11 美元等数字全部保留；SC/PQ/PR 记法、Output 编号与 [SC, PQ] 分数对均按原文格式书写。
- 占位符完整性：逐块脚本比对，173 个文本块的 `⟦SLOT_n⟧` 序列与原文完全一致（mismatch 列表为空），构建脚本 stray=0。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD，编码为 UTF-8。

### 遗留问题

1. 原文 b0016 中 “ImagenHub library11 1” 为脚注编号排版残留，译文原样保留 “11 1” 标记。
2. 附录评分示例中大量使用 PR（如 “PR=0.5”），而正文指标名为 PQ；原文两处并存，译文未作统一改写，保留各处的原始记法。
3. b0054 与 b0064 中“除主体驱动图像编辑/生成外”的表述与摘要略有出入，属原文自身不一致，译文按各块原文照译。
4. 图片缺失 0，figures/ 资源齐全。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（8 块）：b0008、b0164、b0165、b0053、b0191、b0066、b0060、b0014
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
