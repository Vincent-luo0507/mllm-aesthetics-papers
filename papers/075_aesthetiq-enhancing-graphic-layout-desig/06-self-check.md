# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 190（文本 107 / 原子 83）|
| 已译文本块 | 107 / 107 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 157 · 已还原 157 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 337 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 16 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| graphic layout | 图形版面 | 全文统一，未混用「布局」 |
| layout prediction / generation | 版面预测 / 版面生成 | 两个动作分别固定译法 |
| Aesthetic-Aware Preference Alignment (AAPA) | 美学感知偏好对齐（AAPA） | 论文核心方法名 |
| Direct Preference Optimization (DPO) | 直接偏好优化（DPO） | 标准译法 |
| Multi-modal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现括注缩写 |
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 与 MLLM 区分，分别固定 |
| judge model | 裁判模型 | 全文统一，未写作「评审模型」 |
| win rate | 胜率 | 评测指标，统一译法 |
| Mean Intersection over Union (mIoU) | 平均交并比（mIoU） | 指标名 |
| Boundary Displacement Error (BDE) | 边界位移误差（BDE） | 指标名 |
| bounding box | 边界框 | 标准译法 |
| design element | 设计元素 | 全文统一 |
| canvas | 画布 | 全文统一 |
| position token | 位置词元 | 与视觉/文本「词元」口径一致 |
| binning function | 分箱函数 | 离散化操作 |
| instruction tuning | 指令微调 | 标准译法 |
| cross-entropy loss | 交叉熵损失 | 标准译法 |
| reference model | 参考模型 | DPO/AAPA 中的基准策略 |
| policy | 策略 | RL/DPO 语境标准译法 |
| logit | logit | 保留不译 |
| alignment score / overlap score | 对齐分数 / 重叠分数 | 质量过滤的两个启发式 |
| quality heuristic | 质量启发式 | 全文统一 |
| data filtration / filtering | 数据过滤 | 统一译法 |
| renderer | 渲染器 | 版面渲染模块 |
| salient region | 显著区域 | 视觉显著性区域 |
| classifier-free guidance | 无分类器引导 | 标准译法（未在本篇出现，用于术语对齐） |
| pretraining | 预训练 | 标准译法 |
| warmup ratio | 预热比例 | 学习率调度参数 |
| cosine annealing | 余弦退火 | 标准译法 |
| ablation study | 消融研究 | 标准译法 |
| aspect ratio | 长宽比 | 全文统一 |
| ground truth | 真值 | 全文统一，未写作「标注」 |
| salient / saliency | 显著（性） | 与显著区域保持一致 |
| demographics | 人群特征 | 用户研究中的人口统计维度 |
| template | 模板 | 图形设计模板 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0006 | 交叉熵损失惩罚元素错位，AAPA 偏好微调捕捉美学细微差别 | 图 1 说明文字，逐句对应 | 语义一致，无增补 |
| b0027（keep） | 式 1 的提示模板公式 | 未翻译（keep 块） | 符合不变量 3 |
| b0057 | Crello 23,302 个模板，划分 19,479 / 1,852 / 1,971；WebUI 7 万网页 UI | 三个划分数字与 7 万原样保留 | 数字一致 |
| b0067 | AesthetiQ-8B 的 42.83% / 52.67% / 40.64% 与 17.19% 胜率；LACE 23.18%、LayoutNUWA 25.74% | 全部数字原样保留，含 ⟦SLOT_135⟧ | 数字与占位符均无遗漏 |
| b0158 | IoU 由 38.47%→48.29%，胜率 19.29%→24.48%，并说明补入 2B、4B 变体 | 逐项照译 | 数字一致，语义一致 |
| b0175 | 提示模板说明，含 <image> 词元与 {canvas_height} 占位 | 模板占位符原样保留，含 ⟦SLOT_155⟧ | 占位符完整 |

### 一致性与数字核查

- 术语统一性：已用 Grep 核查「版面」「裁判模型」「胜率」「设计元素」「位置词元」「质量过滤」等核心术语，全文译法唯一；MLLM 与 VLM 分别固定为「多模态大语言模型」与「视觉语言模型」，未混用。
- 数字核查：23,302 / 19,479 / 1,852 / 1,971 / 70k / 80,000 / 20 epochs / 128 / 8×80GB / 42.83% / 52.67% / 40.64% / 23.18% / 25.74% / 17.19% / 48.29% / 24.48% / 38.47% / 19.29% / 32.16% / 15.28% / 15.36% / 4.81% / 17.88% / 5.27% / 30.19% / 14.73% / 2.43% / 37.64% / 40.81% / 4.97% / 2.56% / 78.41% / 19.37% / 2.22% / 78.8% / 88.6% 等全部与原文一致。
- 占位符完整性：原文 157 个 `⟦SLOT_n⟧` 全部按原编号、原顺序保留，构建后 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 均不含 U+FFFD。

### 遗留问题

- 原文 b0068 提到「Table 3」而正文中 WebUI 的完整结果表编号为 Table 3（正文表 2 的扩展版），表格编号在原文中略有交叉，译文按原文照写未作调整。
- 正文 b0067 中「Mean IoU」在三种推理设置（All / Single / Multiple）下的数值与表 1 一致，未发现原文错误。
- 附录第 12 节的提示模板（b0176–b0186）属可直接使用的英文提示词，按要求全部译为中文，但 `<image>`、`{canvas_height}`、`{canvas_width}`、`image_1`、`image_2` 及 JSON 结构 `{"better_layout": "answer"}` 均原样保留，未作改动。
- 无图片缺失，无原文乱码。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0152、b0034、b0159、b0072、b0176、b0006、b0068、b0074、b0143、b0163
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 发现并修正 1 处：
  - b0143（漏译（英文原词残留））：
    - 修正前：参与者的选取覆盖了广泛的 demographics，在年龄、性别、职业与宗教信仰上均有差异
    - 修正后：参与者的选取覆盖了广泛的人口统计学特征，在年龄、性别、职业与宗教信仰上均有差异
- 已回写 `zh.json` 并重跑 `build_index.py`，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 其余抽查块未发现实质错误：无漏译整句、无错译关键结论、数字与指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
