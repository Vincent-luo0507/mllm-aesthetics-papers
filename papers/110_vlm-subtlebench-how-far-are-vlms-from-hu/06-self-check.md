# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 297（文本 201 / 原子 96）|
| 已译文本块 | 201 / 201 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 31 · 已还原 31 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 67 |
| `<img>` 元素 | 13 |
| `<table>` 元素 | 16 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| vision-language model (VLM) | 视觉-语言模型（VLM） | 首次括注，后文用 VLM |
| subtle comparative reasoning | 细微比较推理 | 全文统一 |
| difference type | 差异类型 | 十种类型的总称 |
| Attribute / State / Emotion | 属性 / 状态 / 情绪 | 差异类型名，首次括注英文 |
| Temporal / Spatial | 时序 / 空间 | 差异类型名 |
| Existence / Quantity | 存在性 / 数量 | 差异类型名 |
| Quality / Viewpoint / Action | 质量 / 视角 / 动作 | 差异类型名 |
| domain | 领域 | natural/game/medical/industry/aerial/synthetic 六个领域 |
| triplet | 三元组 | 「图像对—问题—答案」 |
| visual question answering (VQA) | 视觉问答（VQA） | 首次括注 |
| captioning | 描述生成 | 与差异描述任务对应 |
| multiple-choice question | 选择题 | 与二选一问答区分 |
| cosine similarity score (CSS) | 余弦相似度分数（CSS） | 描述评测指标 |
| LLM-as-a-judge | LLM 作为评判者 | 描述评测指标，保留缩略说法 |
| chain-of-thought (CoT) | 思维链 | 提示策略 |
| two-step reasoning | 两阶段推理 | 提示策略 |
| grid overlay | 网格叠加 | 4×4 网格 |
| concatenated images | 拼接图像 | 水平拼接 |
| overlap images | 叠加图像 | 像素等权混合 |
| subtraction images | 差分图像 | 绝对逐像素差 |
| highlight images | 高亮图像 | 变化区域加框 |
| morphological closing and opening | 形态学闭运算与开运算 | 图像处理操作 |
| connected components | 连通分量 | |
| percentile threshold | 百分位阈值 | |
| in-distribution adaptation | 分布内适应 | 微调的局限 |
| rank correlation | 秩相关 | Spearman 秩相关 |
| random baseline | 随机基线 | 25% 或 50% |
| anomaly detection | 异常检测 | MMAD 下游任务 |
| inpainting | 修复补全 | nano-banana 编辑方式 |
| OKLAB | OKLAB | 色彩空间名，保留 |
| hue / lightness / luminance | 色相 / 明度 / 亮度 | 颜色敏感性分析 |
| exocentric / egocentric | 外部视角 / 自我中心 | 视频运动类型 |
| fine-tuning | 微调 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0013 | 三条发现：闭源模型落后 30 个百分点以上；CoT/网格/叠加收益有限；对尺寸与数量等难度因素高度敏感 | 三条分点译出，30 个百分点、25%/50% 基线等数值未改动 | 一致 |
| b0090 | 属性（颜色）需约 25% 亮度偏移达 70% 以上，5% 则接近随机；存在性超过 32 个物体降至 60% 以下；数量从近 80% 降至近 60%；视角需约 160 像素（图像高度 27%） | 全部数值与百分比原样保留，趋势方向（存在性下降、视角上升）未颠倒 | 一致 |
| b0166 | 800⟦SLOT_3⟧600 白色背景、2–10 个形状、OKLAB 明度通道（⟦SLOT_4⟧）偏移 5%–10%、缩放 15%–20%、三个干扰项 | 两个占位符原样保留，数值范围一致 | 一致 |
| b0233 | ⟦SLOT_16⟧ 经形态学闭/开运算得 ⟦SLOT_17⟧；聚类 ⟦SLOT_18⟧ 按面积排序取前三；仅当面积达最大聚类 50% 才保留；背景用 ⟦SLOT_19⟧ 压暗；绿色边界 | 四个占位符原样保留，50% 阈值与「至多三个」的限制均译出 | 一致 |
| b0281 | 五种颜色（两种绿 + 蓝/红/洋红）；OKLAB 中 ⟦SLOT_25⟧ 编码明度、⟦SLOT_26⟧ 对应绿–洋红与蓝–黄对立轴；为隔离色相效应修改 ⟦SLOT_28⟧ 而保持 ⟦SLOT_29⟧ | 八个占位符顺序与数量完全一致，语义对应 | 一致 |

### 一致性与数字核查

- 术语：Grep 复查「细微比较推理」「差异类型」「描述生成」「叠加图像」「差分图像」「高亮图像」等在 zh.json 中的用法，全文统一；十种差异类型统一采用「中文（English）」的首次呈现方式，后文不再重复英文。
- 数字：13K 三元组、11.7K/1.3K 划分、1,200 个描述样本（10%）、1,000 个人工评测样本、93.1%、43.0、24.3、25%/50% 随机基线、0.2%、0.5%–10%、1%–5%、20%–30%、35 像素、20–40 像素、800×600、20–80 像素、5–20 度、160 像素（27%）、1,277 样本验证集、723 个验证样本、1e-5、批大小 8/32、3 轮、4×A100 80GB 等数值全部逐项核对，未改动。
- 模型名与数据集名（Qwen2.5-VL、LLaVA-NeXT、LLaVA-OneVision、GPT-4o、o3、GPT-5-main、GPT-5-thinking、Claude-sonnet-4、Gemini-2.5-flash/pro、nano-banana、MVTEC-AD、MVTEC-LOCO、COCO、MIMIC-Diff-VQA、MIMIC-CXR、ChangeIt、CREMA-D、RAVDESS、AFEW-VA、DAiSEE、YT8M、VLM4D、LEVIR-MCI、UBC、MegaFruit、UCF-QNRF-ECC、CameraBench、MMAD、QAG-360K、DINOv3）原样保留。
- 占位符：含 ⟦SLOT⟧ 的文本块共 14 个（含 b0281 的 8 个占位符），逐块按出现顺序比对完全一致，脚本 stray=0。
- 未翻译对象：参考文献、公式、表格、图片、附录中的英文提示语原文均按 `t:"keep"` 或未含英文引号的方式处理，未擅自翻译提示模板。

### 遗留问题

- 附录 C.2 中三条给模型的英文提问（Emotion / Existence / Quality）属提示原文，按不变量第 3 条原样保留未译。
- 附录 A.4 与 A.5 中的英文问答模板（如 "Which frame happened first?"）同属模板原文，保留未译。
- 相机运动术语（dolly-in/out、truck-left/right、pan-left/right、tilt-up/down、pedestal-up/down、zoom-in/out）为专用名词，保留原文未加注。
- 图片引用全部命中，missing_img=0，无缺失图片。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0098、b0073、b0164、b0064、b0255、b0188、b0099、b0181、b0175、b0104
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
另注：章节标题 `3 VLM-SubtleBench` 保留英文原题，属专有名词保留，按规范不改。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
