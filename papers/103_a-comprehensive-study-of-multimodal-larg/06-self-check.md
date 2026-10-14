# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 214（文本 120 / 原子 94）|
| 已译文本块 | 120 / 120 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 59 · 已还原 59 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 122 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 7 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Quality Assessment (IQA) | 图像质量评估（IQA） | 首次出现附英文缩写 |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | |
| Human Visual System (HVS) | 人类视觉系统（HVS） | |
| psychophysics | 心理物理学 | |
| single-stimulus method | 单刺激方法 | |
| double-stimulus method | 双刺激方法 | 又称 2AFC / 成对比较 |
| multiple-stimulus method | 多刺激方法 | |
| standard prompting | 标准提示 | |
| in-context prompting | 上下文提示 | 即少样本提示 |
| chain-of-thought prompting | 思维链提示 | |
| Full-Reference (FR) | 全参考（FR） | FR-IQA |
| No-Reference (NR) | 无参考（NR） | NR-IQA |
| SRCC | 斯皮尔曼秩相关系数（SRCC） | |
| PLCC | 皮尔逊线性相关系数（PLCC） | |
| mean squared error (MSE) | 均方误差（MSE） | |
| two-alternative forced choice (2AFC) | 二选一强制选择（2AFC） | |
| Thurstone’s Case V model | Thurstone’s Case V 模型 | 排序聚合模型 |
| maximum a posteriori estimation | 最大后验估计 | |
| Group MAximum Differentiation (gMAD) | 组最大差异化（gMAD） | 困难样本选择方法 |
| point-to-set distance | 点到集合距离 | 多样性度量 |
| variance normalization | 方差归一化 | 不确定性度量 |
| black-box attack | 黑盒攻击 | |
| catastrophic forgetting | 灾难性遗忘 | |
| instruction tuning | 指令微调 | |
| parameter-efficient tuning | 参数高效微调 | |
| model falsification | 模型证伪 | |
| difficult sample selection | 困难样本选择 | |
| expert IQA model | 专家 IQA 模型 | 与 MLLM 相对 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性确认 |
|---|---|---|---|
| b0037 | 双刺激方法：2AFC、提供「质量相当」第三选项、成对偏好矩阵 ⟦SLOT_7⟧、⟦SLOT_8⟧ 记录 ⟦SLOT_9⟧ 优于 ⟦SLOT_10⟧ 的次数（条件 ⟦SLOT_11⟧）、Thurstone Case V、样本复杂度 ⟦SLOT_12⟧ | 12 个占位符按原编号顺序保留，2AFC 与 Thurstone’s Case V 译名一致 | 占位符编号逐个对应，术语一致 |
| b0050 | 优化问题符号说明：⟦SLOT_18⟧–⟦SLOT_31⟧ 共 14 个符号 | 14 个占位符按原编号顺序嵌入对应说明 | 占位符编号逐个对应，无遗漏 |
| b0062 | 样本数与参数设置：⟦SLOT_37⟧–⟦SLOT_49⟧；TOPIQ / DISTS / CDNet / LIQE / Q-Align / LPIPS / MANIQA 的指派关系 | 13 个占位符保留，模型名与数据集名原样保留，指派关系逐项对应 | 数值、模型与数据集一致 |
| b0178 | FR 单刺激标准提示全文，含输出取值 0–100 与 Score 格式 | 提示全文逐句译出，0 到 100 与 Score: [分数] 格式原样保留 | 格式约束与取值一致 |
| b0227 | NR 多刺激上下文提示，八张图像、排序 [first: 0, second: 1, third: 2, fourth: 3] | 保留八张图像与排序取值，输出格式 Score: [第五张: ，第六张: ，第七张: ，…] 原样保留 | 图像数量与排序格式一致 |

### 一致性与数字核查

- 术语统一性：回扫确认「单刺激/双刺激/多刺激方法」与「标准/上下文/思维链提示」两组策略名全文译法唯一；「全参考（FR）/无参考（NR）」「困难样本选择」「专家 IQA 模型」「点到集合距离」等术语保持一致；SRCC 与 PLCC 首次出现给出中文全称并附缩写，后文沿用缩写。
- 数字与指标：九种提示系统、三个开源加一个闭源 MLLM、分数区间 0–100、排序取值 0–3、输出取值 0/1/2、图像张数（两/三/四/五/六/八/十张）、四参数逻辑函数、基金编号 62071407、61991451、9440379、9440390、JCYJ20220818101001004 等全部原样保留；模型名 GPT-4V、LLaVA-v1.6、InternLM-XComposer2-VL、mPLUG-Owl2、Q-Instruct、Kosmos-2、MiniGPT-4、CLIP、VGG 与指标/数据集名 PSNR、SSIM、FSIM、LPIPS、AHIQ、DISTS、NIQE、MUSIQ、MANIQA、LIQE、TOPIQ、CDNet、Q-Align、KADID、TQD、SPCD、SPAQ、AGIQA-3K 均保留原文。
- 占位符：全文共 59 处（SLOT_0 至 SLOT_58），译文中数量与编号与原文完全一致；构建脚本 `stray` 为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 未改动 `blocks.json` / `translate_input.json` / `orig.html`。

### 遗留问题

- 原文存在若干拼写瑕疵：`InernLM2-7B`（b0068）、`generalizablity`（b0082）、`method11 1`（b0034 脚注标记）、`the shown three images,the`（b0187 缺空格）。译文按上下文语义处理（如 InernLM2-7B 按原文保留），未改动源文件。
- b0178、b0181、b0184、b0187、b0190、b0193、b0196、b0199、b0202、b0206、b0209、b0212、b0215、b0218、b0221、b0224、b0227、b0230 为附录中的完整提示词文本，属可执行的英文提示模板；已全文译为中文，同时保留 Score / Description 等格式标记与取值约束，读者如需直接复用模型提示请参照原文英文。
- 图片文件引用缺失为 0，无图片下载需求。


## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0087、b0045、b0012、b0068、b0080、b0168、b0018、b0178、b0190
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
