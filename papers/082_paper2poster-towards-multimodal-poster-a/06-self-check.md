# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 417（文本 261 / 原子 156）|
| 已译文本块 | 261 / 261 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 80 · 已还原 80 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 231 |
| `<img>` 元素 | 63 |
| `<table>` 元素 | 35 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| academic poster | 学术海报 | 全文统一 |
| paper–poster pair | 论文—海报对 | 基准数据单位 |
| PosterAgent | PosterAgent | 系统名保留 |
| Paper2Poster | Paper2Poster | 基准名保留 |
| Parser | Parser（解析器） | 模块名保留英文，正文首现附中文 |
| Planner | Planner（规划器） | 同上 |
| Painter | Painter（绘制器） | 同上 |
| Commenter | Commenter（评论器） | 同上 |
| asset library | 素材库 | 结构化文本/视觉资源集合 |
| panel | 面板 | 海报中的区块单元 |
| bullet points | 要点 | 面板内的条目化内容 |
| binary-tree layout | 二叉树布局 | 版面策略，首次出现不另行加注 |
| visual-in-the-loop | 视觉在环 | 指渲染反馈参与迭代 |
| Zoom-in | 放大（Zoom-in） | Commenter 的注意力聚焦策略 |
| in-context examples (IC) | 上下文示例（IC） | 消融变体名保留 |
| VLM-as-Judge | VLM-as-Judge | 以视觉语言模型为评判者 |
| PaperQuiz | PaperQuiz | 本文提出的指标名保留 |
| perplexity (PPL) | 困惑度（PPL） | 首次出现附英文与缩写 |
| visual similarity | 视觉相似度 | 指标名 |
| figure relevance | 图片相关性 | 指标名 |
| Engagement | 吸引力 | 六项美学/信息准则之一 |
| Element Quality | 元素质量 | 准则名 |
| Layout Balance | 版面均衡 | 准则名 |
| Content Completeness | 内容完整性 | 准则名 |
| Logical Flow | 逻辑流 | 准则名 |
| density-augmented score | 密度增强分数 | PaperQuiz 的惩罚后指标 |
| verbatim questions | 原文题 | 可直接从文本作答 |
| interpretive questions | 理解性题目 | 需高层理解 |
| oracle | Oracle | 上限参照，保留原词 |
| python-pptx | python-pptx | 库名保留 |
| overflow | 溢出 | 文字超出面板/文本框 |
| token | 词元 | 全文统一，不写作"令牌" |
| backbone | 骨干（模型） | 指底层 LLM/VLM |
| zoom-in region | 放大区域 | 图注用语 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0009 | 四点发现：4o 文本噪声、瓶颈在 Engagement、PaperQuiz 可靠、开源方案词元少 SLOT_0 | 四项发现逐条对应，Engagement 译「吸引力」，槽位保留 | 一致 |
| b0020 | 长度超过 SLOT_1 页至 SLOT_2 页；2022/2023/2024 分别 SLOT_3/4/5；NeurIPS/ICML/ICLR 分别 SLOT_6/7/8 | 八个槽位按原文顺序出现，100 组配对数量未改动 | 一致 |
| b0038 | 惩罚函数三目标，涉及 SLOT_31–SLOT_39 共九处槽位 | 九处槽位序列与原文一致，长度中位数描述准确 | 一致 |
| b0055 | 四类基线：Oracle、端到端（4o-HTML / 4o-Image）、多智能体（OWL / PPTAgent）、PosterAgent-4o 与 -Qwen | 四类划分与全部变体名原样保留，模型版本 Qwen-2.5-7B / Qwen-2.5-VL-7B 未改动 | 一致 |
| b0267 | VLM-as-Judge 3.56–3.72 vs 2.33，视觉相似度 0.75–0.78，原始分 61.33、增强分 121.91，信息分 3.83–3.87、美学分 3.26–3.58 | 全部数字原样保留，SLOT_63 保留 | 一致 |

### 一致性与数字核查

- 术语：全文 poster 统一为「海报」，panel 统一为「面板」，asset 统一为「素材」，overflow 统一为「溢出」，token 统一为「词元」；Parser/Planner/Painter/Commenter 四个模块名一律保留英文不译。
- 数字与指标：100 组论文—海报对、40.7%、69.3%、47.6K/192.0s、255.7K/230.7s、281.48s、158.97s、166.80s、176.69s、54.16s、81.08s、3.56–3.72、0.75–0.78、61.33、121.91、3.83–3.87、3.26–3.58、0.005 美元等均按原文字面保留；PPL、CLIP、AltCLIP、FID、IoU 等指标与模型名未改写。
- 占位符：261 个文本块共 80 处 `⟦SLOT_n⟧`，生成前用脚本逐块比对槽位序列，全部一致；脚本校验残留为 0。
- 编码：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0），无不可解析块。
- 原文 b0057 与 b0060 为一个段落被 HTML 拆成两块，译文保持各自的截断位置，未做合并或重排。
- 附录 F.1 中多处公式体以槽位形式承载（如 SLOT_67–SLOT_74），中文仅描述其语义，公式本身由脚本还原，属预期行为。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0312`、`b0248`、`b0071`、`b0008`、`b0268`、`b0038`（种子 3）；`b0036`、`b0312`、`b0298`、`b0083`、`b0033`、`b0405`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
