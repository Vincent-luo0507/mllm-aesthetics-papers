# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 379（文本 219 / 原子 160）|
| 已译文本块 | 219 / 219 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 63 · 已还原 63 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 1043 |
| `<img>` 元素 | 10 |
| `<table>` 元素 | 46 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| multimodal judge | 多模态评审器 | 全文统一，不译“裁判” |
| reward model | 奖励模型 | 与 judge 区分，各按原文用词对应 |
| multimodal foundation model (FM) | 多模态基础模型 | 首次出现附缩写 FM |
| text-to-image (generation) | 文本到图像（生成） | |
| text-image alignment | 图文对齐 | 四大视角之一 |
| safety | 安全性 | |
| image quality / artifacts | 图像质量 / 伪影 | 原文两词并存，分别对应 |
| generation bias | 生成偏见 | |
| preference dataset | 偏好数据集 | |
| chosen image / rejected image | 优选图像 / 被拒图像 | 全文统一，不用“正/负样本” |
| score model (SM) | 评分模型 | 与 VLM 评审器相对的一类 |
| single-input VLM / multi-input VLM | 单输入 VLM / 多输入 VLM | |
| Likert scale | Likert 量表 | |
| numerical scale | 数值量表 | |
| win rate | 胜率 | |
| tie threshold | 平局阈值 | |
| hallucination | 幻觉 | |
| chain-of-thought (CoT) | 思维链 | |
| rubric | 评分细则 | |
| inpainting | 图像修复 | |
| distortion / blur | 畸变 / 模糊 | 质量子集的两种负向变换 |
| defocused blur / motion blur | 离焦模糊 / 运动模糊 | |
| demographic group / representation | 人口群体 / 人口统计学表征 | |
| ACC (Accuracy) | ACC（准确率） | 偏见指标，缩写保留 |
| GES (Gini-based Equality Score) | GES（基于基尼系数的平等性分数） | |
| NDS (Normalized Dispersion Score) | NDS（归一化离散分数） | |
| NSFW | NSFW | 保留原文 |
| toxicity | 毒性 | safety 下的子目标 |
| RLAIF / RLHF / DPO / DDPO / PPO | 保留原名 | 算法名不译 |
| Bradley-Terry model | Bradley-Terry 模型 | |
| MJ-Bench | 保留原名 | 基准名 |

### 交叉验证记录（随机抽 5 块）

| id | 原文要点 | 我的译文 | 一致性结论 |
|---|---|---|---|
| b0016 | 有效奖励模型应 100% 选出更准确图像；数据点为三元组，含 4 个槽位 | 我们评价的核心见解是……应当百分之百地选出更准确的那张。为评价这一点，MJ-Bench 中每个数据点是一个三元组 ⟦SLOT_0⟧，由指令 ⟦SLOT_1⟧、优选图像 ⟦SLOT_2⟧ 与被拒图像 ⟦SLOT_3⟧ 构成。 | 一致；槽位顺序 0→3 与原文一致 |
| b0037 | 80 种职业、60 个专业；AGE[3]/RACE[6]/GENDER[3]/NATIONALITY[5]/RELIGION[4]；两个组合数槽位 | 同上中文表述 | 一致；五个维度方括号数值与两个槽位原样保留 |
| b0041 | ACC/GES/NDS 三个偏见指标的定义，含 11 个槽位 | 同上中文表述 | 一致；槽位 10→18 顺序与原文完全一致 |
| b0218 | de-blur 算子，5 个槽位 | 其中 de-blur 表示离焦模糊变换算子，⟦SLOT_38⟧ 表示原始图像…… | 一致；算子名与槽位原样保留 |
| b0378 | 三位作者、每批 100 张图、滤除 17.8% 报告 | 同上中文表述 | 一致；两个数字与百分比未改动 |

### 一致性与数字核查

- 术语统一性：Grep 复核 zh.json，「多模态评审器」「奖励模型」「图文对齐」「优选图像／被拒图像」「评分模型」「Likert 量表」「数值量表」「评分细则」「图像修复」「人口统计学表征」等核心术语全文译法唯一；四大视角（对齐／安全性／图像质量／偏见）在正文与附录各表中完全一致。
- 数字与指标：80、60、3、6、5、4、29、31、42、92、197、177、98、472、350、169、152、100、421、2000、4,200、1,200、2,200、100、[1,6]、[0,5]、[0,10]、[0,100]、17.8%、7b–25b 等全部逐位保留；ACC、GES、NDS、FR、RR、AR、AV、SM、VLM、NSFW、DPO、DDPO、PPO、RLAIF、RLHF 等缩写原样。
- 占位符完整性：219 个文本块的 `⟦SLOT_n⟧` 序列与原文完全一致（mismatch 列表为空），构建脚本 stray=0。
- 编码检查：初稿 b0036 曾混入 3 个 U+FFFD 替换字符（已定位并修正为「表现出生成偏见」）；修正后重跑脚本 mojibake=0，zh.json 与 index.html 均不含乱码，编码为 UTF-8。

### 遗留问题

1. 原文 b0042 与 b0279 中“随机种子下的排序”缩写均写作 FR（应为 RR），属原文本身的不一致；译文按各块原文照译，未擅自更正缩写。
2. 多处脚注编号与正文粘连（如 “Likert scale 11 1”“SDXL-1.0 模型 33 3”“仓库44 4”“NudeNet 66 6”“1010 10”“99 9” 等），属 LaTeX 转 HTML 的排版残留，译文一律原样保留数字与其后的 URL。
3. b0200 中 “under170 the guise” 为原文页码与正文粘连，译文按语义处理为“以……为掩饰”，未保留页码数字。
4. 图片缺失 0，figures/ 资源齐全。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0040`、`b0273`、`b0312`、`b0202`、`b0019`、`b0271`（种子 3）；`b0205`、`b0036`、`b0041`、`b0338`、`b0354`、`b0059`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。

### 其他说明

- `b0047` “7 billion to 25 billion” 译为“70 亿到 250 亿”，单位换算正确。
- `b0200`、`b0205` 中混入的版面页码残字（`under170`、`88 8`）按噪声处理，未译入正文，符合规范。
