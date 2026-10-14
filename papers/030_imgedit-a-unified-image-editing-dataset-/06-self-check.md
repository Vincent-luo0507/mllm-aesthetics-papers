# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 251（文本 129 / 原子 122）|
| 已译文本块 | 129 / 129 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 10 · 已还原 10 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 52 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image editing | 图像编辑 | |
| instruction-guided / instruction-based | 指令引导的 / 指令驱动的 | 随语境选用 |
| edit pair | 编辑对 | 源图与编辑图构成的一对 |
| single-turn / multi-turn | 单轮 / 多轮 | |
| in-painting | 局部重绘 | 亦指基于掩码的修复式生成 |
| grounding | 定位 | 指确定待编辑区域 |
| open-vocabulary detector | 开放词汇检测器 | |
| bounding box | 边界框 | |
| mask | 掩码 | |
| segmentation | 分割 | |
| object extraction | 主体提取 | 把主体分离到干净背景并保持身份一致性 |
| cut-out | 抠图 | 基准中与 object extraction 对应 |
| hybrid edit | 混合编辑 | 一条指令含两种局部操作 |
| alter / attribute alteration | 属性修改 | 颜色/材质/外观改变 |
| motion change | 动作更改 | 针对人物主体的动作编辑 |
| background change | 背景替换 | |
| style transfer | 风格迁移 | |
| visual edit | 视觉编辑 | 借助参考图像编辑，保持对象一致性 |
| identity consistency | 身份一致性 | |
| content memory | 内容记忆 | 多轮三大挑战之一 |
| content understanding | 内容理解 | |
| version backtracking | 版本回溯 | |
| instruction adherence | 指令遵循度 | 三个评测维度之一 |
| editing quality | 编辑质量 | |
| detail preservation | 细节保持 | |
| UGE (Understanding-Grounding-Editing) | 理解-定位-编辑（UGE） | 高难单轮套件 |
| fake score | 伪造分数 | 由取证检测器给出 |
| forensic detector | 取证检测器 | 指 FakeShield |
| aesthetic score | 美学分数 | |
| rubric | 评分细则 | |
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | |
| DiT (Diffusion-in-Transformer) | DiT | 架构名保留 |
| UNet | UNet | 架构名保留 |
| MLP | 多层感知机（MLP） | |
| Mixture-of-Experts (MoE) | 混合专家（MoE） | |
| router | 路由器 | MoE 路由模块 |
| VAE | 变分自编码器（VAE） | |
| test suite | 测试套件 | |
| open-source / closed-source | 开源 / 闭源 | |
| ablation study | 消融研究 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0024 | 1.1M 单轮编辑对覆盖 10 种操作；110,000 多轮样本；UGE 套件含义；ImgEdit-Judge | 最终数据集包含 110 万高质量单轮编辑对，覆盖 10 种编辑操作……数据集还包含 11 万条多轮交互样本……理解-定位-编辑（UGE）套件……我们训练了 ImgEdit-Judge | 一致，数字与四个组件均未增删 |
| b0046 | 短边超过 ⟦SLOT_2⟧、美学分数高于 ⟦SLOT_3⟧、⟦SLOT_4⟧ 子集、⟦SLOT_5⟧ 图像对、背景任务编辑面积 >40% | 只保留短边超过 ⟦SLOT_2⟧ 像素且美学分数 [58] 高于 ⟦SLOT_3⟧ 的图像，得到 ⟦SLOT_4⟧ 的图像子集……收集 ⟦SLOT_5⟧ 个图像对……确保被编辑面积占图像 40% 以上 | 一致，四个占位符与 40% 原样保留 |
| b0067 | 九项任务、六大类各十个概念、734 个测试用例 | 九项常见图像编辑任务……从六个大类……各选取十个代表性概念……最终基准包含 734 个测试用例 | 一致，数字与分类未改动 |
| b0075 | 三维度、GPT-4o 1-5 分、多轮“是/否”、FakeShield 召回率（伪造为正类） | 从三个维度评估模型性能……给出 1-5 分评级……对模型输出作“是/否”判定……用最新的开源取证检测器 FakeShield [75]……评估召回率（以伪造为正类） | 一致，评分范围与方法描述未增删 |
| b0196 | 两阶段训练：冻结全部参数、批大小 128、prodigy、lr 1.0；Siglip v2-SO/16@512；50,000 步 + 10,000 步 | 第一阶段冻结 Qwen2.5-VL 与 FLUX 的全部参数……全局批大小 128……prodigy [50]……学习率设为 1.0……Siglip v2-SO/16@512……50,000 步……10,000 步 | 一致，超参与模型名原样保留 |

### 一致性与数字核查

- 已用 Grep 全文回扫核心术语：`主体提取` 12 处、`混合编辑` 9 处、`属性修改` 11 处、`视觉编辑` 6 处、`局部重绘` 7 处、`内容记忆` 9 处、`版本回溯` 9 处、`指令遵循` 7 处、`细节保持` 6 处，均未出现同义轮换。
- 数字核查：1.2 million、1.1 million、110,000、110k、13、10、1280、8.7k、1,000、40%、47、734、10、5、6、3、60、8k、128、1.0、50,000、10,000、10,000（MagicBrush 编辑对）等均与原文一致；数量级表述（`1.2 million`→120 万、`1.1 million`→110 万、`110,000`→11 万）按中文习惯换算，数值等价。
- 模型与指标名：GPT-4o、GPT-4o-Image、Gemini-2.0-Flash、Qwen2.5-VL-7B、SigLIP/Siglip、FLUX、SDXL、Flux-Redux、CLIPScore、PSNR、SSIM、FakeShield、prodigy、ControlNet、IP-Adapters、LoRA、Canny 均原样保留；`⟦SLOT_0⟧`–`⟦SLOT_9⟧` 原样保留。
- 占位符核查：脚本报告槽位总数 10、已还原 10、残留 0；另用脚本逐块比对 `en` 与 `zh` 中 `⟦SLOT_n⟧` 的集合，129 个文本块全部一致（`slot_mismatch` 为空）。
- 编码核查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0。
- 未翻译内容：表 1–4、图 1–12 的图形对象、参考文献均按 `t:"keep"` 规则原样保留。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 数据集规模在原文中同时以 `1.2 million`（摘要与第 3.4 节）与 `1.1 million` 单轮 + `110,000` 多轮（第 1、2 节）两种口径出现，属原文自身的不一致，译文按各处原文忠实译出，未作统一。
- 基准任务列表中的 `cut-out` 与数据集类型中的 `object extraction` 实为同一任务，译文分别作“抠图”与“主体提取”，以保留原文用词差异。
- `b0201` 与 `b0242` 末尾的 `7`、`4` 为原文图表交叉引用编号在 HTML 抽取中的残留，按原文保留。
- `b0235`–`b0240` 位于“附录 D ImgEdit-Bench 的更多细节”之下，内容实为对比模型的架构说明，与附录标题不完全对应，属原文编排问题，译文未作调整。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0069、b0058、b0024、b0075、b0223、b0227），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
