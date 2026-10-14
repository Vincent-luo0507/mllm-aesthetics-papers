# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 217（文本 122 / 原子 95）|
| 已译文本块 | 122 / 122 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 7 · 已还原 7 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 16 |
| `<img>` 元素 | 4 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| generative UI tool | 生成式 UI 工具 | 全文统一 |
| Design Theater | Design Theater | 本文核心概念名，保留原文不译 |
| user-facing design reasoning | 面向用户的设计推理 | 全文统一，不简写为"设计说明" |
| design rationale | 设计理由 | 与 reasoning 区分，指具体陈述 |
| reasoning trace | 推理轨迹 | |
| reasoning element | 推理要素 | TFS 的最小计分单位 |
| Thinking Fidelity Score (TFS) | 思维保真度分数（TFS） | 首现附缩写，后文可用 TFS |
| Principle Adherence Score (PAS) | 原则遵循度分数（PAS） | 同上 |
| Design Homogeneity Index (DHI) | 设计同质化指数（DHI） | 同上 |
| homogenization | 同质化 | 不写作"趋同化" |
| convergence | 趋同 | 描述工具间输出接近 |
| structural / styling / functional tasks | 结构类 / 样式类 / 功能类任务 | 三个层级统一用此译法 |
| tier | 层级 | Tier 1/2/3 → 第一/二/三层级 |
| UX principle | UX 原则 | |
| information architecture | 信息架构 | |
| visual hierarchy | 视觉层次 | |
| accessibility | 无障碍（性） | 名词用"无障碍性" |
| vibe coding | 氛围编程（vibe coding） | 首现附英文 |
| chain-of-thought (CoT) | 思维链（CoT） | |
| faithfulness | 忠实性 | 指理由是否如实反映过程/产物 |
| post-hoc reconstruction | 事后重构 | |
| trust calibration | 信任校准 | |
| stakeholder | 利益相关方 | |
| non-expert | 非专业者 | 名词；形容词用"非专业的" |
| heuristic evaluation | 启发式评估 | |
| WCAG | WCAG | 规范名保留 |
| Nielsen's heuristics | Nielsen 的启发式准则 | 人名保留 |
| bootstrap confidence interval | 自助法置信区间 | |
| Cohen's κ | Cohen's κ | 统计量名保留 |
| inter-rater reliability | 评分者间信度 | |
| Earth Mover's Distance | Earth Mover's Distance（推土机距离） | 首现附中文 |
| CIELCh | CIELCh | 色彩空间名保留 |
| tree edit distance | 树编辑距离 | |
| UIClip / OmniParser | UIClip / OmniParser | 工具名保留 |
| situated design | 情境化设计 | |
| accountability | 问责 | 指设计文档的责任机制 |
| accountability structures | 问责结构 | |
| artifact-centered | 以产物为中心 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | 120 个设计、5 个工具、24 项任务；三层级划分；TFS/PAS/DHI 三项指标 | 数字与缩写全部保留，三个层级的例子（版面与信息架构/色彩字体间距/交互与流程）逐项对应 | 一致 |
| b0054 | ⟦SLOT_0⟧ tools ⟦SLOT_1⟧ ⟦SLOT_2⟧ tasks；固定实现指令仅用 HTML/CSS/JS | 三个槽位按原文顺序嵌入，实现约束表述未增删 | 一致 |
| b0085 | 跨工具 TFS 均值 0.75；四工具 0.74–0.87；Claude 0.87；Firebase 0.53 | 全部数值原样保留，工具名未改写 | 一致 |
| b0099 | 第一层级 0.50–0.94、第二层级 0.38–0.88；四个工具第三层级 ≤0.06；ChatGPT 第三层级 0.38 | 数字区间与工具对应关系准确，Firebase 未实现任何功能原则表述一致 | 一致 |
| b0108 | DHI-Visual 0.119、DHI-Color 20.6、0.151、39.7、DHI-Layout 0.181、0.211；色彩区间 20.6–39.7 | 六个数值与三组工具配对逐一对应，区间描述未改动 | 一致 |

### 一致性与数字核查

- 术语：全文 user-facing design reasoning 统一为「面向用户的设计推理」，rationale 统一为「理由」，homogenization 统一为「同质化」，convergence 统一为「趋同」；三个层级的任务类型（结构类/样式类/功能类）与三个指标缩写（TFS/PAS/DHI）全文写法一致。
- 数字与指标：24、120、5、25%、34%、0.54、6%、0.75、0.87、0.53、0.66、0.79、0.81、0.56（0.36–0.77）、0.29、0.73、14/48、35/48、0.50–0.94、0.38–0.88、0.06、0.38、0.119、20.6、0.151、39.7、0.181、0.211、NSF 2339443 与 2403252 等均按原文字面保留；Cohen's κ、WCAG、CIELCh、DHI-Visual/DHI-Color/DHI-Layout 等指标与子度量名未改写。
- 占位符：122 个文本块共 7 处 `⟦SLOT_n⟧`，生成前用脚本逐块比对槽位序列，全部一致；脚本校验残留为 0。
- 编码：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0），无不可解析块。
- 原文多处段落被 HTML 拆成两块（b0005、b0035、b0102、b0113、b0120、b0123），译文保持各自的截断位置，未做合并。
- Design Theater 为本文提出的核心概念且无通行中译，全文保留英文原名，仅在首现处以同位语说明其含义。
- 原文以「26」「22」等纯数字形式引用文献，译文照原样保留，未做格式调整。

## 复核记录（第二轮交叉验证）

抽查块：b0065、b0044、b0032、b0027、b0031、b0036


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
