# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 250（文本 150 / 原子 100）|
| 已译文本块 | 150 / 150 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 51 · 已还原 51 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 102 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 10 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现附英文缩写，其后统一用 MLLM |
| front-end engineering | 前端工程 | 全篇统一 |
| UI code generation | UI 代码生成 | 未写作"界面代码生成" |
| design-to-code | 设计到代码 | 保留连字符概念，首次出现附英文 |
| framework | 框架 | React / Vue / Angular 均不译 |
| vanilla HTML/CSS | 原生 HTML/CSS | 表格中 Vanilla 一词同此译法 |
| Design Generation | 设计生成 | 三项任务名首字母大写，全篇统一 |
| Design Edit | 设计编辑 | 同上 |
| Design Repair | 设计修复 | 同上 |
| UI Mockup | UI 设计稿 | 未使用"原型图"以免与 prototyping tool 混淆 |
| Compilation Success Rate (CSR) | 编译成功率（CSR） | 指标名保留缩写 |
| Code Modification Location Similarity (CMLS) | 代码修改位置相似度（CMLS） | 同上 |
| Code Modification Content Similarity (CMCS) | 代码修改内容相似度（CMCS） | 同上 |
| MLLM-as-Judge | MLLM 即裁判 | 评分指标名 |
| Abstract Syntax Tree (AST) | 抽象语法树（AST） | 首次出现附缩写 |
| Jaccard similarity | Jaccard 相似度 | 专有名词不译 |
| CodeBLEU | CodeBLEU | 指标名原样保留 |
| Kappa score | Kappa 系数 | 一致性指标 |
| component-based design | 组件化设计 | 全篇统一，未用"基于组件的设计" |
| occlusion | 遮挡 | 六类 UI 问题之一 |
| crowding | 拥挤 | 同上 |
| text overlap | 文字重叠 | 同上 |
| alignment | 对齐 | 同上 |
| color and contrast | 颜色与对比度 | 同上 |
| overflow | 溢出 | 同上 |
| code localization | 代码定位 | 未译作"代码本地化" |
| input context | 输入上下文 | 指 image-only / code-only / both 三种输入 |
| issue severity | 问题严重程度 | 难度分级依据之一 |
| prompt | 提示 | 未用"提示词""提示语"等异译 |
| annotator | 标注者 | 指五名博士生评审 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0014 | 三项发现：框架层面短板（JSX 解析、模板语法、TypeScript 架构、组件化范式利用率低）；任务瓶颈（生成受渲染/编译所困，编辑与修复受代码定位与问题识别所困）；条件波动（大图、复杂指令、严重问题），且 code-only 优于 image-only，多模态增益微小 | 完整译出三条发现，保留 0.6024 一类数值、React/Vue/Angular 系统名，并保留"纯代码输入始终优于纯图像输入"的结论 | 语义一致，数字与结论未改动 |
| b0054 | 编辑标注的两个维度：操作类型 Add/Change/Delete 与 UI 属性类型 text/color/position/size/shape/component-level，难度取决于元素数量、依赖复杂度与级联改动范围 | 逐项对译，六类属性名保留英文原词并加中文注释，难度三因素完整保留 | 语义一致，术语与分类数未增减 |
| b0091 | 三个代码指标：CSR 定义为 S/N；CMLS 用 Jaccard 相似度比较 AST 上的增删改操作集合；CMCS 用 CodeBLEU 计算匹配操作的内容相似度，未匹配记零 | 三个指标定义逐句对译，⟦SLOT_36⟧—⟦SLOT_44⟧ 共 9 个占位符位置与原文一一对应 | 语义一致，公式占位符完整 |
| b0131 | 表 6 的难度规律：生成由 0.79-0.83 降至 0.69-0.73；编辑由 8.64-9.05 降至 7.51-8.19；修复由 6.93-7.21 降至 4.19-6.93，小模型灾难性失败 | 三组数值区间原样保留，"灾难性失败"对应 catastrophic failures，"最陡峭的性能壁垒"对应 steepest performance barriers | 语义一致，全部数值区间未改动 |
| b0187 | 面向开发者的三条建议：提供代码修改位置、明确说明修复问题、拆分复杂指令与大型设计稿 | 三条建议以 (i)(ii)(iii) 顺序译出，未添加原文没有的操作细节 | 语义一致，建议条目数一致 |

### 一致性与数字核查

- 已用 Grep 逐项核对核心术语：MLLM、设计生成/设计编辑/设计修复、框架、组件化设计、代码定位、编译成功率、输入上下文，全文译法唯一，未出现同义轮换。
- 数值核查：摘要与正文中的 900、430、359、111、152、158、120、541、1,349、146、25%、39.5%/15.4%/17.1%、0.53、0.8648、0.8428、95.54%、91.89%、52 美元、49/29/25 秒，以及 CLIP（0.5963-0.8319）、CMLS（0.5089-0.7696）、CMCS（0.3924-0.7080）等区间均与原文一致，未做四舍五入或单位换算。
- 占位符核查：逐块比对了 `⟦SLOT_0⟧`—`⟦SLOT_50⟧`，译文与原文的槽位编号、出现次数完全一致，共 51 处全部还原，脚本 `stray` 为 0。
- 编码核查：`zh.json` 与 `index.html` 中均未检出 U+FFFD。
- 表格、代码块、公式、图片与参考文献块均按规则保留原文，未译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文 b0084 自述"六款先进模型"，而表 4 实际列出九款（六个系列九个规格），译文按原文表述保留"六款"，未作改动，仅作记录。
- b0045、b0049、b0092、b0172 中含有脚注编号与 URL 混排（如 `here11 1 https://...`），系原文排版残留，译文照原样保留未加改写。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；6 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0057、b0096、b0025、b0015、b0181、b0098（seed=2）；加抽 b0127、b0106、b0183（seed=7）
- 发现并修正的问题（已直接改写 `zh.json` 并重跑 `build_index.py`）：

| 块 ID | 问题类型 | 修正前 | 修正后 |
|---|---|---|---|
| b0042 | 占位符顺序错位 | 最后用 selenium（Selenium，2025）截图，构造任务 ⟦SLOT_25⟧ 的输入设计图像 ⟦SLOT_24⟧。 | 最后用 selenium（Selenium，2025）截图，构造出输入设计图像 ⟦SLOT_24⟧，供任务 ⟦SLOT_25⟧ 使用。（顺序 24→25 与 EN 一致） |

- 其余抽查块：完整性、准确性、数字与符号、公式占位符、术语一致性均通过，未发现实质错误。
- 构建校验：重跑 `build_index.py` 后 `missing` / `stray` / `mojibake` / `missing_img` 四项均为 0。
