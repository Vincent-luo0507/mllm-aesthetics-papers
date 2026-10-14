# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 595（文本 434 / 原子 161）|
| 已译文本块 | 434 / 434 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 271 · 已还原 271 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 582 |
| `<img>` 元素 | 513 |
| `<table>` 元素 | 65 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| vision-language model (VLM) | 视觉语言模型（VLM） | 首次出现附英文全称；全篇统一 |
| blind / blindness | 「盲」/「失明」 | 标题与正文中的比喻，加引号以区别于字面义 |
| BlindTest | BlindTest | 基准名保留不译 |
| low-level vision task | 低层视觉任务 | 与高层语义任务相对 |
| geometric primitive | 几何图元 | 指直线、圆、正方形、五边形等 |
| visual acuity | 视敏度 | 验光术语 |
| visual encoder (VE) | 视觉编码器（VE） | 首次出现附缩写 |
| projection layer | 投影层 | 连接 VE 与 LLM 的层 |
| late fusion | 后期融合 | 先提视觉特征、后接 LLM 的范式 |
| slow-thinking model | 慢思考模型 | 与常规（非思考）模型相对 |
| linear probing | 线性探测 | 冻结特征 + 线性分类器的检验方法 |
| average-pooling | 平均池化 | 特征聚合操作 |
| frozen features | 冻结特征 | 训练时参数不变的特征 |
| logistic regression | 逻辑回归 | 线性分类器 |
| groundtruth | 真值 | 未用"地面真值" |
| random-baseline accuracy | 随机基线准确率 | 各任务的随机猜测上限 |
| educated guess | 经验性猜测 | 动词短语 make educated guesses 统一译"做出经验性猜测" |
| hallucinate | 产生幻觉 | 指生成图像中不存在的字符 |
| intersection | 交点 | 直线或折线相交处 |
| tangent / overlapping / disjoint | 相切 / 重叠 / 分离 | 两圆的三种关系 |
| nested | 嵌套 | 正方形任务中的关系 |
| row / column | 行 / 列 | 网格任务 |
| circled letter | 被圈住的字母 | 任务 3 |
| Olympic logo | 奥运标志 | 亦作"奥运五环标志" |
| subway map | 地铁图 | 类地铁图（subway-like map）同此译法 |
| depth-first search | 深度优先搜索 | 路径生成算法 |
| line chart / line plot | 折线图 | 任务 1 |
| line width / thickness | 线宽 / 线条粗细 | 同一参数，按语境择一 |
| boundary-to-boundary distance | 边界到边界距离 | 形状间距定义 |
| confusion matrix | 混淆矩阵 | 字母误判分析 |
| 2-shot | 2-shot | 少样本示例设定保留 |
| chain-of-thought | 思维链 | 提示技术 |
| meta-prompting | 元提示 | 提示技术 |
| prompt engineering | 提示工程 | 未用"提示词工程" |
| fine-tuning | 微调 | Bunny 实验 |
| data leakage | 数据泄露 | 相关工作中的问题 |
| out-of-distribution | 分布外 | 第 5 节假说之一 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0013 | 7 项任务平均 58.07%，Sonnet-3.5 最好 77.84%，远低于人类 100%；GPT-4o 在 7 个既有基准上优于 Gemini-1.5 Pro，在 BlindTest 上却更差 | 三个数值与两个模型名原样保留，两句对比关系完整译出，未添加评价 | 语义一致，数值未改动 |
| b0031 | 两圆任务图像参数：直径 ⟦SLOT_28⟧、16 个距离取值、四种朝向、每尺寸 224 张、3 种尺寸共 768 张 | 16 个数值原样保留，3⟦SLOT_36⟧224 = 768 的算式与占位符位置对应原文 | 语义一致，占位符完整 |
| b0079 | 重叠圆、五边形、嵌套正方形平均准确率 39.44%、30.99%、74.99%；嵌套正方形上 GPT-4o 55.83%、Sonnet-3 65.00%、Gemini-1.5 87.08%、Sonnet-3.5 92.08%；重叠圆上 77.71% 对 1.87% | 七个百分数与四款模型名原样保留，"-25 points behind"译为"至少落后……25 个点" | 语义一致，全部数值未改动 |
| b0147 | CLIP 特征线性探测 ⟦SLOT_168⟧ 99.47%；SigLIP 变体 100%；投影层后 ⟦SLOT_172⟧ 99.58%；结论是语言模型未把视觉信息解码为正确输出 | 三个准确率与 1,000 轮训练、权重 1.0 原样保留，结论句完整译出 | 语义一致，占位符完整 |
| b0260 | 2-shot 与元提示不如基线提示；脚注给出元提示原文 "Describe the image in detail first..." | 两种技术名与表 T2 引用原样保留，脚注中的英文提示原文照原样保留未译 | 语义一致，脚注内容未改写 |

### 一致性与数字核查

- 术语核查：用 Grep 复查「视觉语言模型」「几何图元」「视觉编码器」「后期融合」「慢思考」「经验性猜测」「嵌套」「相切」等核心词，全文译法唯一；overlapping/tangent/disjoint 三种关系在各任务小节中译名固定。
- 数字核查：58.07%、77.84%、71.59%、72.75%、24%、33.33%、25%、20%、50%、4.55%、1,800、768、224、180、480、264、11,100、6,300、8880/1110/1110、4410/945/945、99.47%、99.58%、+27.1、+20、+63 等全部数值与原文一致，未做四舍五入或单位换算；模型名（GPT-4o、Gemini-1.5 Pro、Sonnet-3、Sonnet-3.5、LLaVA-OneV、Phi-3.5、InternVL-2、QVQ、Bunny）与基准名（MMMU、AI2D、MathVista、ChartQA、DocVQA、ActivityNet-QA、EgoSchema、ARC）均原样保留。
- 占位符核查：`⟦SLOT_0⟧`—`⟦SLOT_276⟧` 共 277 处，逐块比对编号与出现次数完全一致，脚本 `stray` 为 0；b0589–b0595 中以独立段落形式出现的坐标轴标签占位符也按原文顺序保留。
- 编码核查：`zh.json` 与 `index.html` 中均未检出 U+FFFD。
- 表格、公式、图片与参考文献块按规则保留原文未译；正文中列出的提示语（如 b0281、b0342、b0468）为原文照录，未加翻译，以免改动评测协议内容。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文多处使用模型图标占位（如 b0021 中 GPT-4o 后跟一对空括号、b0064 表注中缺失的模型名），系 HTML 转换时图标被移除所致，译文按原文结构保留，未作补写。
- b0021、b0022、b0023 段首的「4 commercial」「8 open-source」「2 slow-thinking」为 PDF 边注残留，译文以「4 款商用模型：」「8 款开源模型：」「2 款慢思考模型：」的形式并入正文。
- b0109 原文把两种解释假说写成「two hypotheses」后列举了三条，译文按原文照译，未调整编号。
- 附录 0.F.7 中 Bunny 微调实验的 50K 数据集出现只生成结束 token 的异常，译文按原文陈述保留。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；513 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0410、b0505、b0095、b0078、b0044、b0300（seed=2）
- 发现并修正的问题（已直接改写 `zh.json` 并重跑 `build_index.py`）：

| 块 ID | 问题类型 | 修正前 | 修正后 |
|---|---|---|---|
| b0089 | 占位符顺序错位 | 例如对一个 4⟦SLOT_109⟧5 网格，GPT-4o 预测为 4⟦SLOT_107⟧4，Gemini-1.5 预测为 5⟦SLOT_108⟧5 | 例如，GPT-4o 预测为 4⟦SLOT_107⟧4，Gemini-1.5 预测为 5⟦SLOT_108⟧5，而实际网格为 4⟦SLOT_109⟧5（顺序 107→108→109 与 EN 一致） |
| b0283 | 占位符顺序错位 | 若 ⟦SLOT_198⟧，我们认定两圆重叠且相切（⟦SLOT_196⟧、⟦SLOT_197⟧）；若 ⟦SLOT_201⟧…；当 ⟦SLOT_204⟧ 时为不重叠且不相切（⟦SLOT_202⟧、⟦SLOT_203⟧） | 我们把两圆重叠且相切记为（⟦SLOT_196⟧、⟦SLOT_197⟧），其条件为 ⟦SLOT_198⟧；不重叠但相切记为（⟦SLOT_199⟧、⟦SLOT_200⟧），其条件为 ⟦SLOT_201⟧；不重叠且不相切记为（⟦SLOT_202⟧、⟦SLOT_203⟧），其条件为 ⟦SLOT_204⟧（顺序与 EN 完全一致） |

- 其余抽查块：完整性、准确性、数字与符号、公式占位符、术语一致性均通过，未发现实质错误。
- 构建校验：重跑 `build_index.py` 后 `missing` / `stray` / `mojibake` / `missing_img` 四项均为 0。
