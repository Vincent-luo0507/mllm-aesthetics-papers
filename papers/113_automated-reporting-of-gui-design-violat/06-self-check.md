# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 202（文本 136 / 原子 66）|
| 已译文本块 | 136 / 136 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 99 · 已还原 99 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 195 |
| `<img>` 元素 | 2 |
| `<table>` 元素 | 6 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Graphical User Interface (GUI) | 图形用户界面（GUI） | 首次出现括注英文 |
| GUI-component / GUI-widget (GC) | GUI 组件（GC） | 全文统一为「GUI 组件」 |
| Screen (S) | 屏幕（S） | 定义为画布的逻辑构造 |
| mock-up | 设计稿 | 指 Sketch/PhotoShop 制作的像素级精确产物 |
| mock-up driven development | 设计稿驱动的开发 | |
| design violation (DV) | 设计违规（DV） | |
| presentation failure (PF) | 呈现失效（PF） | |
| Gvt (Gui Verification sysTem) | Gvt | 工具名原样保留 |
| computer vision (CV) | 计算机视觉 | |
| Perceptual Image Differencing (PID) | 感知图像差分（PID） | |
| Color Quantization (CQ) | 颜色量化（CQ） | |
| Color Histogram (CH) | 颜色直方图（CH） | |
| B-PID | B-PID（二值色彩空间下的 PID） | 首次出现加括注说明 |
| K-Nearest-Neighbors (KNN) | K 最近邻（KNN） | |
| uiautomator | uiautomator | Android 框架名保留 |
| Marketch | Marketch | Sketch 扩展名保留 |
| bounding box | 边界框 | |
| leaf-level / leaf node | 叶级 / 叶节点 | |
| container | 容器 | |
| threshold | 阈值 | 各类阈值名（布局阈值、差异阈值等）均按原文修饰语直译 |
| precision / recall | 精确率 / 召回率 | |
| detection precision / classification precision | 检测精确率 / 分类精确率 | |
| taxonomy | 分类体系 | 指 DV 分类体系 |
| grounded theory | 扎根理论 | |
| open coding / focused coding / axial coding | 开放性编码 / 聚焦编码 / 轴心编码 | |
| Likert scale | Likert 量表 | |
| SUS usability scale | SUS 可用性量表 | |
| user experience honeycomb | 用户体验蜂巢模型 | |
| Intersection over union (IOU) | 交并比（IOU） | |
| cross browser testing (XBT) | 跨浏览器测试（XBT） | |
| Visual GUI Testing (VGT) | 可视化 GUI 测试（VGT） | |
| internal / construct / external validity | 内部有效性 / 构念有效性 / 外部有效性 | |

### 交叉验证记录（随机抽样 5 块）

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0022 | 定义 1：GC 为离散对象 ⟦SLOT_0⟧，属性 ⟦SLOT_1⟧，四元组（<x,y>, <h,w>, <text>, <image>），各元素含义 | 四元组与全部占位符原样保留，各属性说明逐项对应 | 结构与占位符一致 |
| b0049 | 71 组屏幕对、82 个 DV；布局违规 ⟦SLOT_18⟧、资源违规 ⟦SLOT_19⟧、文本违规 ⟦SLOT_20⟧；5/82（⟦SLOT_21⟧）影响背景或容器 | 各类别占比与 5/82 数值原样保留 | 数字一致 |
| b0084 | 各阈值设定：PID 三参数、GC 匹配阈值、差异阈值、5 像素、颜色阈值等 | 全部以占位符 SLOT_44~57 保留 | 未改写任何参数 |
| b0106 | 200 种 DV、100 个屏幕池、三条注入准则（≤3/每个 GC ≤1/每屏 ≥1）、人工复核 | 三条准则与全部数量逐项对应 | 语义一致 |
| b0130 | 开发者 CP/DP/R 结果、⟦SLOT_93⟧=⟦SLOT_94⟧、四类性能损失原因、与 Gvt 报告对比的结论 | 四类原因分号并列，占位符保留，末句结论完整译出 | 结构一一对应 |

### 一致性与数字核查

- 术语统一性：用 Grep 复核「GUI 组件」「屏幕」「设计稿」「设计违规」「呈现失效」「计算机视觉」「感知图像差分」「颜色量化」「颜色直方图」「边界框」「叶节点」「阈值」「精确率/召回率」等核心术语，确认全文译法唯一；访谈引语（b0136~b0138）中的英文原文照录，中文译文统一使用引号标注。
- 数字核查：屏幕对数 71、DV 数 82、5/82、200 种 DV、100 个屏幕、40 个违规、10/8/33/5 等采样规模、36.8 分钟与 22 秒、20% 尺寸变化、40% 像素扰动、30° 与 180° 色相偏移、5 像素阈值、98%/96% 等均逐项比对原文，未做任何换算或改写；公式与阈值符号以占位符保留。
- 占位符完整性：99 个 ⟦SLOT_n⟧ 槽位在译文中数量与编号与原文完全一致。
- 编码检查：zh.json 与 index.html 中 U+FFFD 计数均为 0。

### 遗留问题

- 参考文献块 b0171（keep 类型）原文含「SchaufelbÃ¼hl」，属 UTF-8 被按 Latin-1 解码产生的既有编码问题；该块为不译块，未作改动，也未写入 zh.json，故不影响译文编码检查。
- b0022 中原文「the first four elements of the tuple describe the location of the top left point」与后续「height and width attributes」表述在计数上存在原文自身的不一致，译文按原文直译，未作修正。
- 原文 b0059、b0083 中的脚注标记（「11 1」「12」）为抽取后的残留编号，译文按原样保留。



## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽样 6 块（b0049、b0150、b0063、b0113、b0146、b0107）语义、数字、术语均无误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，发现并修正 2 处：

| 块 ID | 问题类型 | 修正前 → 修正后 |
|---|---|---|
| b0030 | 公式占位符错位 | `两个屏幕 ⟦SLOT_8⟧ 与 ⟦SLOT_9⟧ 中…组件 ⟦SLOT_6⟧ 与 ⟦SLOT_7⟧`（顺序 8/9/6/7） → `两个对应的叶级…GUI 组件 ⟦SLOT_6⟧ 与 ⟦SLOT_7⟧——它们分别位于两个屏幕 ⟦SLOT_8⟧ 与 ⟦SLOT_9⟧ 中——`（顺序恢复为 6/7/8/9）|
| b0059 | 脚注标记残留 | `并不与 Sketch 或 Marketch 文件紧耦合。11 1 关于设计稿 GC 的类似信息…` → `并不与 Sketch 或 Marketch 文件紧耦合（关于设计稿 GC 的类似信息…）。`|

修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
