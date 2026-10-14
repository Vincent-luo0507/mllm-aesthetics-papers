# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 354（文本 149 / 原子 205）|
| 已译文本块 | 149 / 149 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 101 · 已还原 101 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 300 |
| `<img>` 元素 | 135 |
| `<table>` 元素 | 10 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| graphic design | 平面设计 | 全文统一译法，不写作"图形设计" |
| multi-layered | 多图层 | 指设计稿的图层结构 |
| layer-wise | 逐图层 | 修饰编辑/生成动作 |
| typography | 排版 | 指字体排印与版面属性 |
| leading / tracking / kerning | 行距 / 字距 / 字偶间距 | 首次出现附英文原词 |
| Large Language Model (LLM) | 大语言模型（LLM） | 首次出现附缩写 |
| Large Multimodal Model (LMM) | 大型多模态模型（LMM） | 与 LLM 区分 |
| diffusion model | 扩散模型 | |
| Design-LLM | Design-LLM | 保留系统名不译 |
| Typography-LMM | Typography-LMM | 保留系统名不译 |
| Reflect-LMM | Reflect-LMM | 自反思模块，保留系统名 |
| intention prompt | 意图提示 | |
| DesignerIntention | DesignerIntention | 基准名保留原文 |
| canvas placeholder | 画布占位 | 指背景图预留元素空间的作用 |
| alpha mask | alpha 掩码 | 控制对象像素透明度 |
| composed image | 合成图像 | 文本到对象模型额外预测的通道 |
| offset noise | 偏移噪声（offset noise） | 首次出现附英文 |
| bin partition | 分箱 | 连续值离散化策略 |
| SVG | SVG | 矢量图形格式，不译 |
| inpainting | 图像修复 | |
| win rate | 胜率 | 用户研究指标 |
| ablation | 消融 | 消融实验 |
| IoU / mIoU / AP25 / AP50 / AP75 | IoU / mIoU / AP25 / AP50 / AP75 | 指标名原样保留 |
| CanvaGPT | CanvaGPT | 商业产品名保留 |
| DALL·E3 | DALL⟦SLOT⟧E3 | 中间点由公式槽位还原 |
| GPT-4V(ision) | GPT-4V(ision) | 保留官方写法 |
| Justinmind | Justinmind | 工具名保留 |
| ground-truth | 真值 | 不写作"地面真值" |
| zero-shot | 零样本 | |
| qualitative results | 定性结果 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0017 | DALL·E3 生成设计图能力强，但存在文本错渲染、不可编辑、需专业提示三点局限；Cole 可由简单意图生成可编辑多图层设计 | DALL⟦SLOT_4⟧E3 能力出众但仍有文本渲染错误、不可编辑、需详尽提示三点问题；Cole 可从简单意图生成多图层可编辑设计 | 一致，三个 SLOT 全部保留 |
| b0035 | DesignerIntention 由 SLOT_14 条专业 + SLOT_15 条创意意图组成；胜率 69.6% 与 70.5% | 保留两个槽位与两个百分比数值，语义一致 | 一致 |
| b0051 | 以 Llama2-13B 为底座构建因果掩码多模态 LLM，用近 SLOT_27 组（意图, JSON）对微调 SLOT_28 轮 | 六个槽位按原文顺序全部保留，模型名与轮次数未改动 | 一致 |
| b0063 | 文本到对象扩散模型需预测 SLOT_41 个通道（对象 SLOT_42、掩码 SLOT_43、合成图 SLOT_44），词元上限 SLOT_45→SLOT_46 | 七处槽位与通道数描述逐项对应 | 一致 |
| b0271 | 用 Sentence-BERT 语义相似度比较真值与 Design-LLM/GPT-3.5/GPT-4 预测，表 4 显示 Design-LLM 显著更优 | 指标名 Sentence-BERT 原样保留，结论方向一致 | 一致 |

### 一致性与数字核查

- 术语：以 Grep 复核 zh.json 全文，graphic design 统一为「平面设计」，typography 统一为「排版」，layer-wise 统一为「逐图层」，alpha mask 统一为「alpha 掩码」，未出现同义轮换。
- 数字与指标：69.6%、70.5%、100,000、+4.5、+6.2 以及 100/64/32/256/8/40 等分箱划分数均与原文字面一致；mIoU、AP25、AP50、AP75、IoU、GPT4-V 等指标名原样保留。
- 占位符：149 个文本块共 101 处 `⟦SLOT_n⟧`，脚本校验已还原 101、残留 0；生成前用脚本逐块比对译文与原文的槽位序列，完全一致。
- 编码：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0），无未解析块。
- 原文 b0245 中 titles / subtitles / headings / subheadings 在中文难以四层区分，译文以「标题（titles）、副标题（subtitles）、大标题（headings）、小标题（subheadings）」并列处理并括注英文，属已知折中。
- b0027 与 b0017 原文重复（HTML 解析所致），译文同样保持一致，未做合并。

## 复核记录（第二轮交叉验证）

抽查块：b0308、b0084、b0050、b0038、b0186、b0102


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
