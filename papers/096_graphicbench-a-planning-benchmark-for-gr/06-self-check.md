# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 294（文本 159 / 原子 135）|
| 已译文本块 | 159 / 159 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 61 · 已还原 61 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 61 |
| `<img>` 元素 | 263 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| LLM agent | LLM 智能体 | 首现写明"大语言模型（LLM）智能体" |
| graphic design | 平面设计 | 全文统一 |
| planning | 规划 | 指工作流规划 |
| workflow | 工作流 | |
| workflow plan | 工作流方案 | |
| expert agent | 专家智能体 | |
| supervisor | 监督者 | 生成设计提纲的顶层智能体 |
| lead agent / specialized agent | 主导智能体 / 专用智能体 | 层次化结构 |
| action | 动作 | 对应一次鼠标或键盘操作 |
| action retrieval | 动作检索 | |
| design component | 设计要素 | 可含子要素 |
| explicit / implicit constraint | 显式约束 / 隐式约束 | |
| commonsense constraint | 常识约束 | |
| long-horizon | 长时程 | |
| action space | 动作空间 | |
| open-weights / closed-source | 开放权重 / 闭源 | |
| design outline | 设计提纲 | |
| expert recruitment | 专家招募 | |
| dependency (local / global) | 依赖（局部 / 全局） | |
| Delivery Rate | 交付率 | 指标名保留英文 |
| Design Pass Rate | 设计通过率 | |
| Step Efficiency | 步骤效率 | |
| Expert Use Efficiency | 专家使用效率 | |
| Execution Success Rate | 执行成功率 | |
| Fidelity | 保真度 | |
| Content Similarity | 内容相似度 | |
| VQA Pass Rate | VQA 通过率 | |
| Originality / Elaboration | 独创性 / 精细度 | 创造性两轴，保留英文 |
| invalid action / parameters / expert | 无效动作 / 无效参数 / 无效专家 | 错误类型 |
| Photo Editor / Vector Graphic Editor / Layout Designer | 图像编辑师 / 矢量图形编辑师 / 版式设计师 | 三位专家智能体 |
| book cover / business card / postcard / poster | 书籍封面 / 名片 / 明信片 / 海报 | |
| Likert scale | Likert 量表 | |
| Cohen's Kappa | Cohen's Kappa | 保留专名 |
| Kendall's τ | Kendall's τ | 以占位符 ⟦SLOT_1⟧ 呈现 |
| SentenceBERT | SentenceBERT | 不译 |
| CLIPScore | CLIPScore | 不译 |
| template matching | 模板匹配 | |
| dead loop | 死循环 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0014 | 1,079 组查询与图像；训练集每类 5 个共 20 组；测试集 1,059 | 三个数字与划分方式完全对应 | 一致 |
| b0026 | 179K 与 95K 图像 URL—说明文字配对，构成 274K 图像池，检索 top-3 | 数字与检索策略逐项照录 | 一致 |
| b0076 | 保真率低；Gemma-2 27b 内容相似度 20.79、VQA 39.64；创造性均值 1.88 与 1.63 | 四个数值原样保留，未改量纲 | 一致 |
| b0083 | 依赖错误平均占 53.0%；分局部依赖与全局依赖 | 百分比与两类依赖划分均译出 | 一致 |
| b0235 | 最常见顺序图像编辑师 ⟶ 版式设计师，共 4,207 次；其次 504 与 262 | 三个计数与顺序完全一致 | 一致 |

### 一致性与数字核查

- 术语统一：Grep 复核"平面设计""工作流""专家智能体""设计要素""保真度""全局依赖"在 zh.json 中用法唯一；三个专家智能体名称全文统一为"图像编辑师／矢量图形编辑师／版式设计师"，未出现"排版师""照片编辑器"等同义轮换。`agent` 一律译"智能体"，未混入"代理"。
- 数字核查：1,079、1,059、20、46、1,000+（274K/179K/95K）、0.8、0.586、0.671、200、50、25、10 美元、8K、0.947、1.0、2.05、12.2、9.87、7.92、53.0%、5.96%、0.77%、0.17%、20.79、39.64、1.88、1.63、4,207、504、262、9.07/10.0/7.89/8.70、3.05/1.33、2.15/1.00、1.03/1.28、1.99/1.04、[0,360]、[-150,+150] 等全部原样保留。
- 占位符完整性：脚本逐块比对 `⟦SLOT_n⟧` 序列（含 SLOT_0～SLOT_60），159 个文本块全部一致，输出 slot mismatch: []；其中 b0041、b0056 初稿占位符顺序与原文有出入，已按原文序列调整后重新校验通过。
- 编码检查：zh.json 与 index.html 中不含 U+FFFD（构建脚本 mojibake=0）。

### 遗留问题

- 原文多处脚注标记与正文粘连（如"Behance platform22 2 https://..."），按语义断为正文句末加脚注编号与链接，未改动源文件。
- 原文 b0091 有拼写错误"comunicate"（应为 communicate），按语义译为"传达"，未改动源文件。
- 原文 b0222/b0226 中"3 image""the 3 image from 1 to 3"存在单复数笔误，按语义译出，未改动源文件。
- 图片文件全部齐备（missing_img=0）。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽样 6 块（b0228、b0086、b0023、b0004、b0289、b0078）语义、数字、术语均无误。另对全文做了脚注残留扫描，发现 PDF 抽取的脚注序号被原样写进中文正文，共 20 处，已全部修正（改为括号内联脚注内容）：

| 块 ID | 问题类型 | 修正前 → 修正后 |
|---|---|---|
| b0018 | 脚注标记残留 ×2 | `Behance 平台22 2 https://www.behance.net/` → `Behance 平台（https://www.behance.net/）`；`截图。33 3 https://www.adobe.com/creativecloud 以每张` → `截图（Adobe Creative Cloud 参见 https://www.adobe.com/creativecloud）。以每张`|
| b0026 | 脚注标记残留 ×3 | `OpenCLIPArt44 4 https://openclipart.org/` → `OpenCLIPArt（https://openclipart.org/）`；`Vectors55 5 https://publicdomainvectors.org/` → `Vectors（https://publicdomainvectors.org/）`；`前 3 张图像。66 6 我们将以 CC0 许可发布这些图像。` → `前 3 张图像（我们将以 CC0 许可发布这些图像）。`|
| b0028 | 脚注标记残留 ×3 | `GPT-o177 7 https://openai.com/o1/` → `GPT-o1（https://openai.com/o1/）`；`Cohen's Kappa88 8 https://…Cohens_kappa` → `Cohen's Kappa（https://…Cohens_kappa）`；`Kendall's ⟦SLOT_1⟧99 9 https://…Kendall_rank_correlation_coefficient` → `Kendall's ⟦SLOT_1⟧（https://…Kendall_rank_correlation_coefficient）`|
| b0034 | 脚注标记残留 | `（Son et al. 2024; Yuan et al. 2024b）。1010 10 我们选取…` → `（Son et al. 2024; Yuan et al. 2024b）（我们选取…）。`|
| b0035 | 脚注标记残留 | `Adobe Photoshop 的智能体，1111 11 https://…/photoshop 负责` → `Adobe Photoshop 的智能体（https://…/photoshop），负责`|
| b0036 | 脚注标记残留 | `Adobe Illustrator 的智能体，1212 12 https://…/illustrator 专注于` → `Adobe Illustrator 的智能体（https://…/illustrator），专注于`|
| b0037 | 脚注标记残留 | `Adobe InDesign 的智能体，1313 13 https://…/indesign 负责` → `Adobe InDesign 的智能体（https://…/indesign），负责`|
| b0043 | 脚注标记残留 ×3 | `执行。1414 14 Adobe CC 设计工具不支持直接 API 调用。` → `执行（Adobe CC 设计工具不支持直接 API 调用）。`；`对象操作函数。1515 15 我们依据 Adobe 的教学视频…` → `对象操作函数（我们依据 Adobe 的教学视频…）。`；`JavaScript 代码。1616 16 由于当前模型难以直接…` → `JavaScript 代码（由于当前模型难以直接…）。`|
| b0048 | 脚注标记残留 ×2 | `闭源模型：GPT-3.5。1717 17 https://openai.com/index/chatgpt/ 对开放权重模型` → `闭源模型：GPT-3.5（https://openai.com/index/chatgpt/）。对开放权重模型`；`采样温度设为 0.0。1818 18 开放权重模型的 HuggingFace 模型名…` → `采样温度设为 0.0（开放权重模型的 HuggingFace 模型名…）。`|
| b0053 | 脚注标记残留 | `最多 30 步。1919 19 最大步数由人工标注…` → `最多 30 步（最大步数由人工标注…）。`|
| b0061 | 脚注标记残留 | `量化保真度。2020 20 https://docs.opencv.org/…` → `量化保真度（https://docs.opencv.org/…）。`|
| b0063 | 脚注标记残留 | `生成问题。2121 21 平均而言，书籍封面…` → `生成问题（平均而言，书籍封面…）。`|

修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
