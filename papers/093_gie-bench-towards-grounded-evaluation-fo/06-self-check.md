# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 153（文本 96 / 原子 57）|
| 已译文本块 | 96 / 96 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 22 · 已还原 22 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 51 |
| `<img>` 元素 | 8 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| text-guided image editing | 文本引导的图像编辑 | 全篇统一，未用"文本驱动" |
| functional correctness | 功能正确性 | 双轴之一，全篇统一 |
| content preservation | 内容保持 | 双轴之一，未用"内容保留"以免与 preserve 的歧义 |
| preservation score | 保持分数 | 指标名 |
| object-aware masking | 对象感知掩码 | 技术名 |
| object mask | 对象掩码 | 由 SAM 生成的编辑区域掩码 |
| rest-of-image mask | 图像其余部分掩码 | 对象掩码取反所得 |
| VQA-style | VQA 式（视觉问答式） | 首次出现附中文全称 |
| multiple-choice question | 选择题 | 与 binary yes/no question（二元是非题）相对 |
| distractor | 干扰项 | 选择题中的迷惑选项 |
| edit type | 编辑类型 | 九种编辑类别的总称 |
| Color Change | 颜色更改 | 九类编辑之一 |
| Add Object | 添加物体 | 同上 |
| Remove Object | 移除物体 | 同上 |
| Attribute Change | 属性更改 | 同上 |
| Object Replacement | 物体替换 | 同上 |
| Layout Modification | 布局修改 | 同上 |
| Scene/Background Change | 场景/背景更改 | 同上 |
| Size Change | 尺寸更改 | 同上 |
| Textual Edit | 文字编辑 | 同上 |
| ground truth | 真值 | 未用"地面真值" |
| open-vocabulary | 开放词汇 | GroundingDINO 的检测设定 |
| segmentation mask | 分割掩码 | 与 object mask 区分使用 |
| mean squared error (MSE) | 均方误差（MSE） | 指标名保留缩写 |
| SSIM / PSNR / CLIP | SSIM / PSNR / CLIP | 指标名原样保留，不译 |
| min-max normalize | 最小—最大归一化 | 校准化处理 |
| SIFT keypoints | SIFT 关键点 | 算法名保留 |
| FLANN-based matching | 基于 FLANN 的匹配 | 算法名保留 |
| affine transformation | 仿射变换 | 几何对齐手段 |
| Spearman correlation | Spearman 相关系数 | 统计指标名 |
| ground-truth answer / expected answer | 预期答案 | 附录表格表头 |
| annotator | 标注者 | 人工研究参与者 |
| single-turn | 单轮 | 局限性中的设定描述 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0009 | 用 VQA 式协议评估功能正确性；每道题含 2–5 个选项，难度高于 I2E-Bench 的二元是非题，降低猜中概率 | 逐句对译，保留 I2E-Bench 系统名与 2 至 5 个选项的数值范围，并把"reducing the chance of success by guessing"译为"降低猜对的概率" | 语义一致，数值与系统名未改动 |
| b0036 | 指出全局相似度指标的缺陷：模型完全不编辑时会得满分；改用分割掩码取反定义应保持区域 | 完整译出反例论证与"取反"的核心思路，未添加原文没有的评价 | 语义一致，论证链条完整 |
| b0044 | 原始池 6,000 对，人工筛选后保留 1,080 对、856 张不重复图像，9 类编辑各 120 条指令，20 个类别均衡 | 三个数字原样保留，"unique images"译为"不重复图像"，"evenly/carefully balanced"译为"精细均衡" | 语义一致，数字未改动 |
| b0049 | 用 SIFT 关键点、FLANN 匹配与仿射变换对齐，再对 MSE 取反并做最小—最大归一化，得到区间内的校准保持分数 | 三个技术名原样保留，⟦SLOT_15⟧/⟦SLOT_16⟧/⟦SLOT_17⟧ 三处占位符按原文顺序嵌入 | 语义一致，占位符完整 |
| b0078 | 100 个样例、九个模型、四名标注者、4 分制（0 完全失败、1 弱否决、2 弱接受、3 完全成功），并注明 GPT-Image-1 因 API 未发布而未纳入 | 全部数值与等级定义逐项对译，脚注说明照原样保留在正文相应位置 | 语义一致，评分刻度未改动 |

### 一致性与数字核查

- 术语核查：用 Grep 复查「功能正确性」「内容保持」「对象掩码」「编辑类型」「保持分数」「VQA 式」等核心词，全文译法唯一，未出现同义轮换。
- 数字核查：2000、800、100、1000、1080、856、6000、3、9、20、120、17%、25 USD、100 个样例、四名标注者，以及表 2 中 4.17–99.11、表 7 中 6.67%–97.32% 等全部数值均与原文一致，未做四舍五入或单位换算。
- 占位符核查：`⟦SLOT_0⟧`—`⟦SLOT_21⟧` 共 22 处，逐块比对编号与出现次数完全一致，脚本 `stray` 为 0。
- 编码核查：`zh.json` 与 `index.html` 中均未检出 U+FFFD。
- 表格、公式、图片与参考文献块按规则保留原文未译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- b0055 与 b0144 在源文件中被标记为文本块，实为表格数据（各模型在九类编辑上的准确率）。译文保留了全部数值与模型名，仅把表头（编辑类型名）译为中文，并以分号分隔各行，以保证数值零改动。
- b0020、b0021 中的大量 `\cite` 键（如 `xiao2024omnigenunifiedimagegeneration`）按原文原样保留，未作翻译或改写。
- b0008、b0078 含脚注编号与正文混排（如 `GIE-Bench,11 1 short for...`），系原文排版残留，译文照原样保留。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0034、b0018、b0042、b0032、b0036、b0130、b0151、b0145、b0023、b0053
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
