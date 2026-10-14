# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 179（文本 84 / 原子 95）|
| 已译文本块 | 84 / 84 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 18 · 已还原 18 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 42 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image editing | 图像编辑 | 全文统一 |
| instruction-based image editing | 基于指令的图像编辑 | 与“指令驱动的图像编辑”不混用 |
| Multimedia Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现括注英文与缩写 |
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 与 MLLM 分列，不互换 |
| Diffusion in Transformer (DiT) | DiT | 架构名，不译 |
| reference image | 参考图像 | 未与“输入图像”混用 |
| editing instruction | 编辑指令 | 与 editing prompt（编辑提示）分别对应 |
| target image | 目标图像 | 数据三元组的一端 |
| data pipeline | 数据流水线 | |
| triplet | 三元组 | 源图像—编辑指令—目标图像 |
| connector module | 连接模块 | |
| token refiner | Token Refiner | 模块名保留英文 |
| token concatenation | 词元拼接 | 与 channel concatenation（通道拼接）对照 |
| rectified flow | rectified flow | 保留英文原写法 |
| latent | 潜（latent） | 统一用“潜层/潜特征” |
| inpainting | 图像修复 | |
| depth estimation | 深度估计 | |
| optical flow | 光流 | |
| Semantic Consistency (SQ/SC) | 语义一致性 | 原文标 SQ，按原文保留 |
| Perceptual Quality (PQ) | 感知质量（PQ） | |
| Overall Score (O) | 总体得分（O） | |
| user preference (UP) | 用户偏好（UP） | |
| Intersection Subset | 交集子集 | |
| Full set | 全集 | |
| de-identification | 去标识化 | 隐私保护流程 |
| closed-source / open-source | 闭源 / 开源 | |
| autoregressive (AR) model | 自回归（AR）模型 | |
| style transfer | 风格迁移 | |
| tone transformation | 色调变换 | |
| beautification | 美化 | 人像编辑子任务 |

### 交叉验证记录（抽样 5 块）

| id | 原文要点 | 我的译文 | 语义一致性 |
|---|---|---|---|
| b0006 | 依据常用指令归纳出 N 类编辑任务，构建可扩展数据流水线，产出超过 N 百万条数据，覆盖对象操作、属性修改、布局调整、风格化 | 四项编辑操作逐项译出，两个 SLOT 占位符原样保留，未改写数量级 | 一致，无漏译 |
| b0033 | 生成超过 SLOT_2 百万三元组，经 step-1o 与人工筛选保留 SLOT_3 百万余条；留存比 20:1；与其他数据集并排对比 | “留存比 20:1”“Step1X-Edit-HQ 子集”均按原文保留，模型名 step-1o 未译 | 一致 |
| b0054 | 与 FLUX-Fill 的通道拼接、SeedEdit 的因果自注意力不同，遵循 OminiControl 用词元拼接；VAE 编码后线性投影，沿词元长度维拼接 | 三种方法的对照关系完整，绿色框提示保留，“沿词元长度维度拼接”与原文一致 | 一致，无添油加醋 |
| b0073 | 去标识化协议：跨多引擎反向图像检索找公开替代图；找不到则修改指令以保持与原意图的忠实 | 两层策略与“伦理正当性”结论全部译出，未增补任何隐私政策评论 | 一致 |
| b0080 | VIEScore 三项指标 SQ/PQ/O；交集子集 434 条、全集 606 条；GPT-4o 因安全策略拒答的处理方式 | 数字 434、606 与脚注标记（11、22、33、44）全部保留，两类测试集的定义与排除规则完整 | 一致，数字核对无误 |

### 一致性与数字核查

- 术语一致性：全文统一使用“图像编辑”“编辑指令”“参考图像”“多模态大语言模型（MLLM）”“交集子集/全集”“闭源/开源”。模型名（Step1X-Edit、Qwen-VL、Qwen2.5-VL、GPT-4o、GPT-4.1、Gemini2 Flash、Doubao、OmniGen、ACE++、AnyEdit、Florence-2、SAM-2、ControlNet、Flux-Fill、SD3、FLUX、HiDream-I1、Flex）与基准名（GEdit-Bench、GEdit-Bench-EN/CN）全部原样保留。
- 数字核查：11 个类别、606 条测试样本、434（EN 交集）/ 422（CN 交集）、1K 余条实例、55 名参与者、留存比 20:1、百万级数据量（由 SLOT 占位符承载）等均未作换算；五级量表（最差/较差/一般/良好/优秀）与 SLOT_12–SLOT_16 一一对应，顺序未打乱。
- 占位符完整性：84 个文本块的 `⟦SLOT_n⟧` 集合与原文逐块比对，零差异；构建脚本 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 中均不含 U+FFFD；脚注标记（如 `44 4 API access as of June 2025.`）按原文结构保留。

### 遗留问题

- 无图片缺失（`missing_img = 0`），7 张 `<img>` 均指向已下载的 `figures/` 本地文件。
- b0080 原文含上标脚注与正文混排（如 `GPT-4.1 [37]11 1 The results...`），属原始 PDF 抽取痕迹，已按“正文 + 脚注文字”的顺序直译，未作删改。
- b0101–b0103 为作者名单与通讯作者邮箱，人名、邮箱原样保留，仅译“核心贡献者／贡献者／通讯作者”标签。原文邮箱 `yugang@stepfu n.com` 中含异常空格，疑为 PDF 抽取错误，按原文照录未作修正。
- 原文指标缩写 SQ 与 VIEScore 通行的 SC 不一致，译文遵循原文作“SQ（语义一致性）”，未擅自改为 SC。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0098, b0046, b0073, b0038, b0053, b0016 / b0103, b0050, b0091, b0008, b0034, b0089
- 结论：抽查未发现实质错误。完整性、准确性、数字与符号、`⟦SLOT_n⟧` 占位符、术语一致性、中文表达六项均通过，未做任何修改。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
