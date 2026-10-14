# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 376（文本 196 / 原子 180）|
| 已译文本块 | 196 / 196 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 9 · 已还原 9 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 47 |
| `<img>` 元素 | 80 |
| `<table>` 元素 | 10 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| reward hacking | 奖励黑客（reward hacking） | 首次出现括注英文，后文统一用「奖励黑客」 |
| reinforcement learning (RL) | 强化学习 | 与 RLHF/RLVF 一致 |
| post-training | 后训练 | 不译「训练后处理」 |
| text-to-image (T2I) | 文本到图像（T2I） | 首次括注，后文用 T2I |
| reward function | 奖励函数 | |
| reward model | 奖励模型 | |
| proxy reward | 代理奖励 | 与「真实目标」相对 |
| human preference alignment | 人类偏好对齐 | |
| prompt-image consistency | 提示-图像一致性 | 与「图文对齐」为同一概念，前者用于指标语境 |
| compositionality reward | 组合性奖励 | 基于目标检测的奖励类别 |
| artifact | 伪影 | 全文统一，不作「瑕疵」「 artefacts」 |
| structural artifact | 结构性伪影 | 本文核心失效模式 |
| ArtifactReward | ArtifactReward | 本文方法名，保留原文 |
| automatic prompt optimization (APO) | 自动提示优化（APO） | 首次括注 |
| vision-language encoder | 视觉-语言编码器 | CLIP/BLIP 一类 |
| MLLM (multimodal LLM) | 多模态大语言模型 | 首次括注 |
| backbone | 骨干（模型） | Qwen2.5-VL 作为骨干 |
| regularizer | 正则项 | 说明 ArtifactReward 的作用方式 |
| policy gradient | 策略梯度 | REINFORCE 风格 |
| KL regularization | KL 正则化 | |
| distributional regularization | 分布正则化 | ROCM 的方法 |
| over-saturated | 过饱和 | 色彩层面的奖励黑客表现 |
| grounding accuracy | 定位准确率 | 目标检测类指标 |
| degradation | 退化 | 跨指标性能下降 |
| tie | 同分 | 表 2 中奖励给两图相同分数的情形 |
| faithfulness | 忠实度 | EvalAlign 的评测维度 |
| Perception / Correspondence | Perception / Correspondence | LLM4LLM 两个维度名，保留英文并括注含义 |
| WiScore | WiScore | WISE 基准综合分，保留 |
| normalized probability | 归一化概率 | 用于定义 ArtifactReward 分数 |
| cross-metric mismatch | 跨指标不匹配 | 奖励黑客的直接表征 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0009 | 首次系统分析；两类奖励各自导致奖励黑客；集成只部分缓解；普遍模式为伪影生成；与前人工作区分 | 五项要点全部译出，引用 8; 49; 32; 24 原样保留 | 一致 |
| b0070 | GDino/ORM 上升而 HPS、美学、DeQA 退化；HPS 训练则 grounding、语义一致性下降；PickScore/VQAScore/UnifiedReward 无一致上升；组合仅部分缓解 | 图号 1(a)–1(c)、1(e)–1(f)、1(d)、1(g)、1(h) 对应无误，上升/下降方向未颠倒 | 一致 |
| b0095 | 表 4 标题含 WiScore = 0.7 ⟦SLOT_0⟧ Consistency + 0.2 ⟦SLOT_1⟧ Realism + 0.1 ⟦SLOT_2⟧ Aesthetic | 系数 0.7/0.2/0.1 原样保留，三个 ⟦SLOT⟧ 逐个原样保留且位置对应 | 占位符与数字均一致 |
| b0205 | ⟦SLOT_3⟧ 为真值标签，⟦SLOT_4⟧ 为 yes 词元归一化概率，评分函数 ⟦SLOT_5⟧ 为上述对数似然 | 三个占位符原样保留，语义对应 | 一致 |
| b0278 | EvalAlign 用图像忠实度（视觉内容匹配现实或语义的程度）作为质量维度之一，本文聚焦该指标 | 定义与聚焦理由均译出，方法名 EVALALIGN / EvalAlign 按原文两处写法分别保留 | 一致 |

### 一致性与数字核查

- 术语：Grep 复查「奖励黑客」「伪影」「后训练」「组合性奖励」「文图对齐」等在 zh.json 中的用法，全文统一，未出现「奖励劫持」「瑕疵」等同义替换。
- 数字：约 200 个样本、约 3000 步、前 1200 步、三轮训练、0.7/0.2/0.1 权重、1B 与 7B 规模等数值全部原样保留。
- 模型与基准名（Janus-Pro-1B、Janus-Pro-7B、Qwen2.5-VL-7B-Instruct、Grounding DINO、HPS、PickScore、Aesthetic Score、DeQA、GDino、ORM、VQAScore、UnifiedReward、WISE、LLM4LLM、EvalAlign）原样保留，未翻译。
- 占位符：含 ⟦SLOT⟧ 的文本块共 3 个（b0095、b0205、b0266），逐块比对集合完全相等，脚本 stray=0。
- 未翻译对象：参考文献、公式、表格、算法块、图片均按 `t:"keep"` 跳过。

### 遗留问题

- 原文存在若干拼写瑕疵（"Specificly"、"recognizingunrealistic"、"centural"、"This results expose"、"expect the image to show"），译文按正确语义处理，未加注释，也未改动源文件。
- 原文引用编号以裸数字形式出现（如 "42"、"26"），属转换产物，译文照原样保留。
- 图片引用全部命中，missing_img=0，无缺失图片。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0264`、`b0011`、`b0374`、`b0085`、`b0142`、`b0268`（种子 3）；`b0072`、`b0372`、`b0293`、`b0038`、`b0008`、`b0122`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
