# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 139（文本 91 / 原子 48）|
| 已译文本块 | 91 / 91 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 1 · 已还原 1 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 6 |
| `<img>` 元素 | 1 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 首次附英文，后文用 VLM |
| Large Vision-Language Model (LVLM) | 大视觉语言模型（LVLM） | 与 VLM 同义处沿用原文表述 |
| spatial attention bias | 空间注意力偏置 | 本文核心概念，全文统一 |
| horizontally concatenated image | 水平拼接图像 | 实验刺激形式 |
| left-positioned / right-positioned content | 左侧／右侧内容 | 全文统一 |
| left-to-right / right-to-left | 从左到右／从右到左 | 扫描方向 |
| Right-to-Left (RTL) | 从右到左（RTL） | 阿拉伯语阅读方向 |
| neutral prompting | 中性提示 | 无方向引导的基线条件 |
| directional prompting | 方向性提示 | 含明确方向指令的条件 |
| structured prompting | 结构化提示 | 要求 JSON 输出 |
| positional embedding | 位置嵌入 | 架构因素之一 |
| RoPE | RoPE | 位置嵌入方案，保留原名 |
| vision encoder | 视觉编码器 | 架构因素之一 |
| cross-modal alignment projector | 跨模态对齐投影器 | 桥接模块 |
| visual instruction tuning | 视觉指令微调 | 训练阶段 |
| direct preference optimization | 直接偏好优化 | 训练阶段 |
| recency bias | 近因偏置 | 相关工作中的概念 |
| lost-in-the-middle | 中部丢失 | 相关工作中的现象 |
| object-centric image | 以物体为中心的图像 | Caltech-101 数据特性 |
| Desktop UI dataset | Desktop UI 数据集 | 自建密集界面数据集 |
| activation patching | 激活修补 | 机制可解释性技术 |
| mechanistic interpretability | 机制可解释性 | 未来方向 |
| attention pattern analysis | 注意力模式分析 | 未来方向 |
| LLM-as-a-Judge | LLM-as-a-Judge | 评测流程，保留原名 |
| top-p sampling | top-p 采样 | 推理配置 |
| bicubic interpolation | 双三次插值 | 图像预处理 |
| character difference | 字符差值 | 偏置度量指标 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | 100 个图像对（50 对＋水平翻转）、七个模型、开源／闭源名单、简单与结构化两种提示 | 数字与七个模型名原样保留，两类提示条件对应完整 | 一致 |
| b0027 | 50 个图像对、原始排布与翻转版本、100 张测试图、512×512、双三次插值 | 数字与尺寸原样保留 | 一致 |
| b0044 | ±60 字符阈值，五项统计量（强左、强右、均衡、平均、极值） | 阈值与五项统计逐项对应 | 一致 |
| b0051 | 两模型均在 97% 情形先描述左图；AIN 阿拉伯语微调仍左先，指向视觉编码器或跨模态对齐 | 数字与因果推断表述完整对应 | 一致 |
| b0071 | InternVL2-8B 结构化提示下强左偏置由 80% 降到 47%，平均差值由 +472.8 降到 +33.8 | 四个数值原样保留 | 一致 |

### 一致性与数字核查

- 术语统一：以 Grep 核对 zh.json，全文统一使用「空间注意力偏置」「水平拼接」「从左到右／从右到左」「中性提示」「方向性提示」「位置嵌入」「视觉编码器」等译法，未出现同义轮换。
- 数字核查：100 / 50 / 512×512 / 10 / 45 / 10C2 / 97% / 67% / +472.8 / +393.5 / +3.3 / +14.0 / −179.7 / −33.9 / −7.6 / 80% / 47% / +33.8 / ±60 / 0.5 / 0.9 等数值均与原文一致，未作换算或改写。
- 占位符完整性：脚本自校验 `⟦SLOT⟧` 残留为 0；另用脚本逐块比对原文与译文的 `⟦SLOT_n⟧` 序列，91 个文本块全部完全一致（含顺序）。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文中的英文提示词（如 b0033、b0035 的 “Describe the image” 等）属于实验刺激而非代码，译文保留英文原文并在括号中给出中文，便于读者对照。
- 原文 b0029 中 “10C2 = 45” 为组合数写法，按原样保留。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0083、b0051、b0008、b0058、b0029、b0047），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
