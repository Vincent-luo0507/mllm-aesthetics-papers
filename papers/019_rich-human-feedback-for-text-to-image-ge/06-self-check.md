# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 335（文本 185 / 原子 150）|
| 已译文本块 | 185 / 185 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 22 · 已还原 22 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 81 |
| `<img>` 元素 | 74 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Text-to-image generation (T2I) | 文本到图像（T2I）生成 | 首次出现保留英文缩写 |
| artifact | 伪影 | 全文统一，不写作"伪像" |
| implausibility | 不合理性 | 与 plausibility（合理性）对应 |
| plausibility | 合理性 | 四类细粒度评分之一 |
| text-image alignment | 图文对齐度 | 评分名称 |
| misalignment | 不一致 | 指图文不匹配；不作"错位" |
| misaligned keyword | 不一致关键词 | 提示词中被错表征/缺失的词 |
| heatmap | 热力图 | 点标注经圆盘化后得到 |
| fine-grained score | 细粒度评分 | 合理性/对齐度/美学/总体四类 |
| Likert scale | 李克特量表 | 5 点量表 |
| multimodal transformer | 多模态 Transformer | 模型名 RAHF |
| region inpainting | 区域重绘 | 由掩膜触发的局部再生成 |
| Classifier Guidance | 分类器引导 | 保留英文原术语 |
| ground truth (GT) | 真值 | 图注中保留 GT 缩写 |
| majority voting | 多数投票 | 多标注者整合策略 |
| teacher-forcing | 教师强制 | 序列训练方式 |
| augmented prompt | 增强提示 | 模型变体名称 |
| multi-head | 多头 | 模型变体名称 |
| Direct Preference Optimization (DPO) | 直接偏好优化 | 保留英文缩写 |
| PLCC / SRCC | 皮尔逊线性相关系数 / 斯皮尔曼秩相关系数 | 评分预测指标，缩写保留 |
| NSS / KLD / AUC-Judd / SIM / CC | 同名保留 | 显著性热力图指标，不译 |
| saliency | 显著性 | 仅用于显著性热力图 |
| Pick-a-Pic / ImageReward / PickScore | 同名保留 | 数据集与模型名 |
| Muse / PaLI / PaLM 2 / T5X / ViT | 同名保留 | 模型名 |
| Latent Diffusion (LD) | 潜在扩散（LD） | 首次出现给出中文 |
| annotator | 标注者 | 不写作"标注员" |
| effective radius | 有效半径 | 点标注的覆盖半径定义 |
| Institutional Review Board (IRB) | 机构审查委员会（IRB） | 伦理审批机构 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0005 | Pick-a-Pic 中仅有 ⟦SLOT_0⟧10% 图像无伪影/不合理；举例"男子跳河"却生成站立 | 保留 ⟦SLOT_0⟧ 与 10%，举例照译 | 一致，占位符与百分比未改 |
| b0037 | 用公式 ⟦SLOT_2⟧（⟦SLOT_3⟧、⟦SLOT_4⟧）标准化评分 ⟦SLOT_1⟧ 至 [0,1] | 四个槽位逐一保留，区间 [0, 1] 保留 | 一致 |
| b0076 | ⟦SLOT_9⟧ 空热力图，995 个测试样本中 69 个为空；⟦SLOT_10⟧ 非空 | 数字 995、69 原样保留 | 一致 |
| b0105 | 表 5 五级偏好比较，五个槽位 ⟦SLOT_13⟧–⟦SLOT_17⟧，6 名参与者 | 五个槽位全部保留，人数 6 保留 | 一致 |
| b0232 | 超参数：16×16、12 层 12 头、768/3072/2048、三个槽位 ⟦SLOT_19⟧–⟦SLOT_21⟧、输出词元长度 64 | 全部数字原样，三槽位保留 | 一致 |

### 一致性与数字核查

- 术语统一性：全文 `misalignment` 一律译作"不一致"，`implausibility` 一律译作"合理性"的反面"不合理性"，`heatmap` 一律"热力图"，`prompt` 一律"提示词"，未出现同义轮换。
- 数字核查：18K/17K/16K/1K/995/69/144/27/3000/3,000/0.333/0.410 等数值、百分比与阈值 0.8 均逐字核对，未做换算或四舍五入。
- 占位符核查：22 个 `⟦SLOT_n⟧` 槽位（含图注与正文）在译文中数量与编号完全一致，构建脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 图注中的英文提示词（prompt）原文保留，仅翻译说明性文字，以保留原始实验输入的可核对性。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文 b0286 为图 12 的表头行 "Image GT Our model CLIP gradient"，已按四列表头译出，无对应 HTML 表格结构。
- 原文 b0310 含作者自注"This text will be invisible, just to occupy some spaces."，属原文占位文字，已如实译出。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（9 块）：b0307、b0109、b0103、b0035、b0223、b0121、b0206、b0039、b0089
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
