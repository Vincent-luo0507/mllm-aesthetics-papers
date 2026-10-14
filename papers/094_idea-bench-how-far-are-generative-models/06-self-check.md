# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 224（文本 126 / 原子 98）|
| 已译文本块 | 126 / 126 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 14 · 已还原 14 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 65 |
| `<img>` 元素 | 14 |
| `<table>` 元素 | 13 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| IDEA-Bench (Intelligent Design Evaluation and Assessment Benchmark) | IDEA-Bench（智能设计评测与评估基准） | 首次出现附全称，后文用 IDEA-Bench |
| Text-to-Image (T2I) | 文本到图像（T2I） | 任务类别名统一 |
| image-to-image | 图像到图像 | |
| images-to-image | 多图到图像 | 与上一项区分 |
| text-to-images | 文本到多图 | |
| image(s)-to-images | 图像/多图到多图 | 保留斜杠与括号写法 |
| IDEA-Bench-mini | IDEA-Bench-mini | 子集名保留 |
| generative model | 生成模型 | |
| universal generative model | 通用生成模型 | |
| multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | |
| prompt rephrasing | 提示改写 | 指用 GPT-4o 把多模态输入改写为 T2I 提示 |
| prompt refinement | 提示精修 | 指对评估问题措辞的迭代修改 |
| hierarchical evaluation | 层级化评估 | 三级评分结构 |
| binary scoring item | 二值评分项 | 0/1 计分 |
| subtask / case | 子任务 / 用例 | 100 个子任务、275 个用例 |
| leaderboard | 排行榜 | |
| in-context learning | 上下文学习 | |
| ID consistency | ID 一致性 | |
| style consistency | 风格一致性 | |
| identity-preserving | 身份保持 | |
| storyboard / storyboarding | 分镜 | 电影分镜 |
| picture book | 绘本 | |
| photo retouching | 照片修图 | |
| font transfer | 字体迁移 | |
| visual effects | 视觉特效 | |
| adapter | 适配器 | ControlNet / T2I-Adapter |
| guidance scale | 引导系数 | 文本/图像引导系数 |
| sampling steps | 采样步数 | |
| collage | 拼图 | 多图拼接输入 |
| failure rate | 失败率 | 评估器未返回 0/1 的比例 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性确认 |
|---|---|---|---|
| b0006 | 5 个类别、100 个子任务、275 个用例、1,650 道层级化评估问题 | 四项数字与结构全部保留 | 数量一致，无增删 |
| b0051 | 形式化定义：数据集 ⟦SLOT_1⟧、子任务 ⟦SLOT_2⟧、大类 ⟦SLOT_3⟧、数据集 ⟦SLOT_4⟧、大类数 ⟦SLOT_5⟧ | 五个占位符按原编号顺序嵌入对应位置 | 占位符编号逐个对应 |
| b0071 | FLUX-1 取得 22.46 最高分；不借助 MLLM 时无模型超过 10 分；Anole 表现不理想 | 保留 22.46 与 10，模型名与因果关系一致 | 数值与结论一致 |
| b0187 | Gemini 1.5 pro 失败率 0.95%，GPT-4o 为 52.84%；每问评估三次 | 两个百分比与「三次评估」规则原样保留 | 数值与判定规则一致 |
| b0176 | 提示平均长度约 139 词；短提示集中在图像到图像与多图到图像 | 保留 139 词与类别归因 | 数值与结论一致 |

### 一致性与数字核查

- 术语统一性：回扫确认「文本到图像/图像到图像/多图到图像/文本到多图/图像（多图）到多图」五类任务译法全文唯一；「提示改写」与「提示精修」分别对应 prompt rephrasing 与 prompt refinement，未混用；「子任务/用例」「二值评分项」「层级化评估」等亦保持一致。
- 数字与指标：100 / 275 / 1,650 / 18 / 11 / 22.46 / 8.98 / 10 / 139 / 50 / 0.95% / 52.84% / 6 / 12 / 2–5 等全部原样保留；模型名 FLUX-1、SD3、Pixart、DALL-E 3、InstructPix2Pix、MagicBrush、Emu2、OmniGen、Anole、GDT、ControlNet、T2I-Adapter、Gemini 1.5 Pro、GPT-4o 与指标名 FID、CLIPScore 均保留原文。
- 摘要中最高分为 22.48（meta 摘要），正文 b0071 为 22.46，二者差异源自原文，译文未作统一改动。
- 占位符：全文共 14 处（b0046 的 SLOT_0、b0051 的 SLOT_1–SLOT_5、b0056 的 SLOT_6、b0066 的 SLOT_7、b0074 的 SLOT_8、b0076 的 SLOT_9、b0078 的 SLOT_10、b0080 的 SLOT_11、b0184 的 SLOT_12、b0190 的 SLOT_13），译文中数量与编号与原文一致；构建脚本 `stray` 为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 未改动 `blocks.json` / `translate_input.json` / `orig.html`。

### 遗留问题

- 原文存在若干拼写/语法瑕疵：`shwon`（b0087）、`anlyses`（b0165）、`adde`（b0024）、`greatly expand`（b0024）、`double explosure`（b0212）。译文按上下文语义处理（如 explosure 按「双重曝光」译出），未改动源文件。
- b0061、b0071、b0072、b0094 等处主谓一致存在语法瑕疵（如「FLUX-1 achieve」「Anole do not achieve」），译文按中文表达规范处理，未逐句机械直译。
- 图片文件引用缺失为 0，无图片下载需求。


## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0043、b0092、b0074、b0009、b0094、b0198、b0015、b0172、b0183
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
