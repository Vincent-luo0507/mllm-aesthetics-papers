# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 226（文本 94 / 原子 132）|
| 已译文本块 | 94 / 94 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 44 · 已还原 44 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 110 |
| `<img>` 元素 | 14 |
| `<table>` 元素 | 21 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 固定，不混用「多模态大语言模型」 |
| Visual Question Answering (VQA) | 视觉问答（VQA） | 固定 |
| natural adversarial sample | 自然对抗样本 | 核心概念，固定 |
| NaturalBench / NaturalBench-Retrieval | NaturalBench／NaturalBench-Retrieval | 基准名保留 |
| confounding pair | 混淆（样本）对 | 指被判别式 VLM 错配的图文对 |
| mismatched / mismatch | 错配 | 固定 |
| blind solution / blind model | 盲解法／盲模型 | 指不看图像、仅凭语言先验作答的模型 |
| vision-centric | 以视觉为中心 | 固定 |
| balanced evaluation protocol | 均衡评测协议 | 固定 |
| question accuracy (Q-Acc) | 问题准确率（Q-Acc） | 三个指标之一 |
| image accuracy (I-Acc) | 图像准确率（I-Acc） | 同上 |
| group accuracy (G-Acc) | 分组准确率（G-Acc） | 同上 |
| compositionality | 组合性 | 固定 |
| skill tag / skill taxonomy | 技能标签／技能分类体系 | 固定 |
| attribute binding | 属性绑定 | 固定 |
| spatial / action / part relation | 空间／动作／部件关系 | 固定 |
| bias / debiasing | 偏置／去偏置 | 固定，不写作「偏见」 |
| sample-level / global-level debiasing | 样本级／全局级去偏置 | 固定 |
| post-hoc debiasing | 事后去偏置 | 固定 |
| hallucination | 幻觉 | 固定 |
| dynamic evaluation | 动态评测 | 固定 |
| data leakage | 数据泄漏 | 固定 |
| yes-or-no / multiple-choice | 是非题／选择题 | 固定 |
| generative likelihood | 生成似然 | 固定 |
| VQAScore | VQAScore | 指标名保留 |
| stochastic decoding | 随机解码 | 固定 |
| Unanswerable | 无法回答 | 标注选项 |
| MTurk annotator | MTurk 标注者 | 保留平台名 |
| MMMU / MME / MMBench / MMStar / MMVP / ScienceQA / AI2D / MM-Vet / Seed-Bench / Winoground / ARO | 保留原名 | 基准名一律不译 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 结论 |
|---|---|---|---|
| b0012 | 初始基准 5,800 个是非题 + 1,800 个选择题；规模超过 MMVP、MMStar（300～1,500）；人类 >90%；LLaVA、mPLUG-Owl 略好于随机；GPT-4o、GPT-4Vision 落后 50% 以上 | 全部数值与基准名原样保留，比较关系准确 | 数字零改动 |
| b0022 | MME 中 97.5%／100%；MMStar 中「Sad」是「Happy」的三倍、「White/Black」是「Purple」的十倍；VQAv1 中 87% | 三个百分比与三处倍数关系完整保留 | 数字与语义一致 |
| b0033 | 1,200 个 Flickr30K 图像对 → 2,600 是非题 + 1,000 选择题；DOCCI 补充 3,200 + 800；正文合计 7,600 | 五个数值与重采样上限「最多三次」全部保留 | 数字与条件一致 |
| b0047 | 技能分类：8 类物体、8 类属性、3 类关系（空间再分 4 子类）、5 类推理；MMVP 为 8 类单一标签 | 全部计数与 MMVP 对照保留，示例词（helpful、facing、near、to the right 等）保留原文 | 数字与示例零改动 |
| b0225 | 全局最优与事后去偏置明显差于样本最优；Bunny、InterVL-Chat-V1.2、GPT-4o 上性能下降 | 三个模型名与三层比较关系完整保留 | 语义与名称一致 |

### 一致性与数字核查

- **术语统一**：对 `zh.json` 全文检索确认，「视觉语言模型」「自然对抗样本」「盲解法」「以视觉为中心」「混淆对／错配」「偏置／去偏置」「组合性」「技能标签」「动态评测」等核心术语在正文与附录中译法完全一致，未出现同义词轮换（例如未混用「偏见」与「偏置」、「盲模型」与「无视觉模型」）。
- **占位符完整性**：逐块比对原文与译文的 `⟦SLOT_n⟧` 集合，44 个槽位（SLOT_0～SLOT_43）数量、编号与顺序全部一致；构建脚本 `stray = 0` 印证。
- **数字与指标**：10,000、5,800、1,800、7,600、2,600、1,000、3,200、800、2,000、1,200、53、55、27、8、3、4、5、90%、50%、30%、55%～70%、5%～20%、20.2%、35%～40%、87%、97.5%、100%、24、230、500、14、2e-5、16、10 等全部原样保留；Q-Acc、I-Acc、G-Acc、VQAScore、Winoground 的文本／图像／分组分数等指标名与基准名一律保留原名；「是」「否」「B」等答案选项与 `MTurk`、`MTurk 标注者` 等专有名保留。
- **编码检查**：`zh.json` 与 `index.html` 均不含 U+FFFD，构建脚本 `mojibake = 0`。
- **不变量**：表格（21）、代码块、公式（110 个 `<math>`）、图片（14）与参考文献块均为 `t:"keep"`，未翻译；94 个文本块严格一一对应，无合并、拆分或删减。

### 遗留问题

- 无图片缺失（`missing_img = 0`），14 张图片均已在 `figures/` 中命中。
- b0040 中「对 LLaVA-1.5 与 GPT-4o 做视觉微调 11 1 由于成本高昂……」为脚注插入导致的断句错乱，译文按字面保留。
- b0022 中 MMMU 示例问句「Which artist belonging to the Bloomsbury group was Gertler in a relationship with?」在译文中保留英文原句未译（原文即以此作为待答问题示例），其余说明文字已译。
- b0012 与 b0041 中模型数量分别写作「超过 50 个」与「55 个」，b0013 提到 27 项技能，均按原文照写，未统一。
- 表 1、表 2 等表格中的原始数值未被翻译（属 `t:"keep"`），未作改动。


## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0059`、`b0021`、`b0061`、`b0171`、`b0047`、`b0018`（种子 3）；`b0061`、`b0005`、`b0053`、`b0203`、`b0173`、`b0195`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
