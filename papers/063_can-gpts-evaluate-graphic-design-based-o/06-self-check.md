# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 110（文本 85 / 原子 25）|
| 已译文本块 | 85 / 85 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 3 · 已还原 3 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 6 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 0 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| graphic design | 平面设计 | 亦指具体的设计作品 |
| design principles | 设计原则 | |
| alignment | 对齐 | 三项设计原则之一 |
| overlap | 重叠 | 三项设计原则之一 |
| white space | 留白 | 三项设计原则之一 |
| heuristic evaluation (metrics) | 启发式评估（指标） | 指 O’Donovan 等的手工设计公式 |
| hand-crafted metrics | 手工设计指标 | 与启发式指标同义，随语境选用 |
| Large Multimodal Model (LMM) | 大型多模态模型（LMM） | |
| foundation model | 基础模型 | |
| human annotation | 人工标注 | 指受试者打分 |
| human evaluation | 人工评估 / 人类评估 | 随语境选用 |
| subject / participant | 受试者 / 参与者 | 众包评分人员 |
| crowdsourcing | 众包 | |
| correlation | 相关性 | |
| Pearson correlation coefficient | 皮尔逊相关系数 | |
| perturbation | 扰动 | 指对坐标/字号的改动 |
| perturbation level / range | 扰动水平 / 扰动幅度 | small/medium/large 三档 |
| font size | 字号 | |
| banner / poster | 横幅 / 海报 | |
| template | 模板 | |
| sampling temperature | 采样温度 | |
| standard deviation | 标准差 | |
| scatter plot / box plot | 散点图 / 箱线图 | |
| absolute evaluation | 绝对评估 | |
| pairwise evaluation | 成对评估 | |
| vector-based | 基于矢量 | 指直接读取矢量坐标 |
| canvas | 画布 | |
| border margin | 边框留白 | |
| readability | 可读性 | |
| render and rasterize | 渲染并栅格化 | |
| voting | 投票 | 成对评估五次取多数 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0012 | 人工标注与 GPT 的相关性高于启发式指标，表明一定条件下 GPT 能可靠判断平面设计质量 | 我们发现人工标注与 GPT 之间的相关性高于启发式指标，这表明在一定条件下，GPT 能够对平面设计质量给出可靠的判断 | 一致，因果关系与限定语未增删 |
| b0044 | 100 个模板、600 个扰动样本、700 个样本数据集；两类扰动 ⟦SLOT_0⟧ 坐标与字号；扰动文字位置 ⟦SLOT_1⟧ 坐标 | 从 VistaCreate 随机采样一百个模板……施加两类扰动：⟦SLOT_0⟧ 坐标与字号。我们扰动文字位置的 ⟦SLOT_1⟧ 坐标以评估对齐，扰动文字元素的字号以评估重叠与留白……把 100 个原始样本与 600 个扰动样本合并，构建出一个含 700 个样本的数据集 | 一致，三个计数与两个占位符原样保留 |
| b0045 | 通过众包招募 60 名参与者；每个设计五条标注；1–10 分；取平均分 | 我们通过众包招募了 60 名参与者，为每个平面设计收集五条标注，要求参与者在 1 到 10 的范围内打分……实验中使用五条标注的平均分 | 一致，数字与流程未改动 |
| b0050 | GPT 评估五次取平均；采样温度设为 1（默认）；0.9 会产生更多样输出 | 我们进行五次基于 GPT 的评估，并取其平均分作为 GPT 分数。我们把控制 GPT 随机性的采样温度设为 1（默认值）；更高的温度（如 0.9）会产生更多样的输出 | 一致，两个温度值与次数原样保留 |
| b0105 | GPT-4o 准确率随扰动幅度增大而提高；中/大扰动下与启发式相当；小扰动下对齐与留白表现更差；两条原因 | 在所有指标上，GPT-4o 的准确率随扰动幅度增大而逐步提高；在中等与大扰动下，GPT-4o 的性能与启发式指标相当……然而在对齐与留白的小扰动下，GPT-4o 的表现不如启发式指标。这有两个原因：…… | 一致，趋势描述与两项原因未增删 |

### 一致性与数字核查

- 已用 Grep 全文回扫核心术语：`平面设计` 36 处、`设计原则` 21 处、`留白` 31 处、`重叠` 17 处、`启发式` 28 处、`扰动` 18 处、`相关性` 9 处、`人工标注` 7 处，均未出现同义轮换。
- 数字核查：60、100、600、700、1、0.9、5（次/条）、1 到 10、0 至 1、三档（small/medium/large）、三项设计原则等均与原文一致；`⟦SLOT_0⟧`、`⟦SLOT_1⟧`、`⟦SLOT_2⟧` 原样保留。
- 模型与服务名：GPT-4o、GPT-4、VistaCreate、LMM 均原样保留；URL（`https://openai.com/index/hello-gpt-4o/`、`https://create.vista.com`）与脚注编号（`11 1`、`22 2`）按原文形态保留。
- 提示词模板标记 `[A design principle]`、`[image]` 与“第 A 节”“第 C 节”的交叉引用原样保留。
- 占位符核查：脚本报告槽位总数 3、已还原 3、残留 0；另用脚本逐块比对 `en` 与 `zh` 中 `⟦SLOT_n⟧` 的集合，85 个文本块全部一致（`slot_mismatch` 为空）。
- 编码核查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0。
- 未翻译内容：图 1–11 的图形对象、参考文献均按 `t:"keep"` 规则原样保留。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 多处图注末尾带有 “This is a figure.” / “Overview of our study.” / “Annotation example.” 等上游抽取残留文本，译文按原文忠实地一并译出，未作删改。
- `b0109` 原文称 “GPT-4o scores are more similar to those of a heuristic evaluation”，与正文第 5.1 节“GPT 与人工评估相关性更好”的结论存在张力，疑为原文笔误（“heuristic” 或应为 “human”）；译文按原文照译，未作修正，此处记录备查。
- `b0002` 原文在两个句子之间缺少分隔（“…‘white space.’Overview of our study.”），译文保留了这一形态。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽样 6 块（b0025、b0105、b0008、b0070、b0087、b0109）语义、数字、术语均无误。另对全文做了脚注残留扫描，发现并修正 2 处：

| 块 ID | 问题类型 | 修正前 → 修正后 |
|---|---|---|
| b0042 | 脚注标记残留 | `我们向 GPT-4o 11 1 https://openai.com/index/hello-gpt-4o/ 给出提示词`  → `我们向 GPT-4o（https://openai.com/index/hello-gpt-4o/）给出提示词`|
| b0044 | 脚注标记残留 | `我们从 VistaCreate 22 2 https://create.vista.com 收集平面设计模板`  → `我们从 VistaCreate（https://create.vista.com）收集平面设计模板`|

修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
