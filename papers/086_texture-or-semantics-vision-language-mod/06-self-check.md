# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 298（文本 190 / 原子 108）|
| 已译文本块 | 190 / 190 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 7 · 已还原 7 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 15 |
| `<img>` 元素 | 21 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 首次出现附英文缩写，后文用 VLM |
| font recognition | 字体识别 | 全文统一 |
| typography / typographic | 字体排印 | 指排印风格，与 font（字体）区分 |
| typeface | 字型 | 指具体字型外观，与 font（字体）区分 |
| Font Recognition Benchmark (FRB) | 字体识别基准（FRB） | 保留英文缩写 |
| easy version / hard version | 简单版本 / 困难版本 | 不译作「简易版/困难版」以免混淆 |
| Stroop effect | Stroop 效应 | 原文小写 stroop，按专有名词规范统一大写 |
| serif / sans-serif | 衬线 / 无衬线 | |
| Script & Decorative Fonts | 手写体与装饰字体 | 三大字体类别之一 |
| Chain-of-Thought (CoT) | 思维链（CoT） | 保留缩写 |
| few-shot learning | 少样本学习 | 1-shot 至 6-shot 保留原写法 |
| multiple-choice question (MCQ) | 选择题（MCQ） | 表 1 中 M 后缀即指 MCQ |
| zero-shot | 零样本 | |
| attention matrix | 注意力矩阵 | |
| cross-attention layer | 交叉注意力层 | |
| image patch | 图像块 | |
| attention head | 注意力头 | |
| open-weight / closed-source | 开放权重 / 闭源 | 模型分类术语 |
| ground truth | 真值 | |
| indicator function | 指示函数 | |
| string matching | 字符串匹配 | |
| spurious visual cues | 虚假视觉线索 | |
| texture-based perturbation | 基于纹理的扰动 | |
| content-biased misattribution | 内容偏置型误判 | 四类错误之一 |
| Explicit Inability Acknowledgment | 明确承认无能为力 | |
| Indecisive Classification | 犹豫型分类 | |
| Confidently Incorrect Prediction | 自信的错误预测 | |
| small caps | 小型大写字母 | 排版术语 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性确认 |
|---|---|---|---|
| b0033 | 每种字体 10 张图像、每句尽可能涵盖 26 个英文字母，共 ⟦SLOT_0⟧ 张 | 保留 10、26 与 ⟦SLOT_0⟧，统一 Python 脚本、换行/字号/背景一致均译出 | 数字与占位符一致，无增删 |
| b0046 | 表体文本：13 个模型在四类设置下的全部准确率数值 | 表头与分组词（闭源模型/开放权重模型）译出，全部数值与模型名原样保留 | 48 个数值逐一核对一致 |
| b0058 | MCQ 下开放权重模型准确率均接近 6.67%，等于「仅当字体名与样式一致才正确」的期望值 | 保留 6.67% 与推理解释 | 数值与因果解释一致 |
| b0200 | 准确率公式说明：⟦SLOT_3⟧ 指示函数、⟦SLOT_4⟧ 真实标签、⟦SLOT_5⟧ 预测标签、⟦SLOT_6⟧ 样本总数 | 四个占位符按原编号顺序保留 | 占位符编号逐个对应 |
| b0211 | Llama-3.2-90B 在简单版本正确识别 23 个 Pacifico 实例，Llama-3.2-11B 为 0；Arial 与 Times New Roman 相对容易 | 保留 23、0 及字体名与图 11–30 引用 | 数字与模型名一致 |

### 一致性与数字核查

- 术语统一性：回扫确认「字体识别」「字体排印」「简单版本/困难版本」「Stroop 效应」「开放权重/闭源」「注意力矩阵」等核心术语全文译法唯一；衬线/无衬线、手写体与装饰字体的三分法在正文与附录 A 保持一致。
- 数字与指标：60%、5,000 万、15、13、2,400、30%、15%、10、26、52、6.67%、18%、67%、0.0、0.95、bfloat16、A100 80GB、四块 GPU、日期区间等全部原样保留；字体名（Baskerville SC、Georgia、Merriweather、Times New Roman、Roboto Slab、Arial、Calibri、Consola、Helvetica、Monoton、Vera、Great Vibes、Lobster、Pacifico、Satisfy）与模型名（GPT-4o、GPT-4o-mini、Claude-3.5-Sonnet、Gemini-2.0-Flash-001、Qwen2-VL 系列、Llama-3.2 系列、Phi 系列、Idefics 系列）均保留原文。
- 占位符：全文共 7 处（b0033 的 SLOT_0、b0034 的 SLOT_1、b0082 的 SLOT_2、b0200 的 SLOT_3–SLOT_6），译文中数量与编号与原文一致；构建脚本 `stray` 为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 未改动 `blocks.json` / `translate_input.json` / `orig.html`。

### 遗留问题

- 原文若干字体名存在拼写变体：`Baskervville SC`（多一个 v，见 b0078、b0235、b0239、b0243、b0251、b0255、b0259、b0263）与 `Helevetica`（字母换位，见 b0225、b0229）。按不改动原文的要求，译文照原样保留，未统一为 Baskerville SC / Helvetica。
- b0005 与 b0008 为同一段落被分页截断的两半（b0005 末尾停在「数据收集、标注与」，b0008 以「遴选」开头），按块对块原则分别译出，未作合并。
- b0024 中「Unlike ... the VFR dataset ...」一句英文表述存在重复主语的语病，译文按字面结构保留，未作改写。
- 图片文件引用缺失为 0，无图片下载需求。


## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0052、b0086、b0034、b0062、b0267、b0017、b0005、b0072、b0289
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
