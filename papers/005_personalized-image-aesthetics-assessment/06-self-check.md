# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 118（文本 78 / 原子 40）|
| 已译文本块 | 78 / 78 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 1 · 已还原 1 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 51 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image aesthetics assessment (IAA) | 图像美学评估（IAA） | 任务总称 |
| generic image aesthetics assessment (GIAA) | 通用图像美学评估（GIAA） | 与 PIAA 对举 |
| personalized image aesthetics assessment (PIAA) | 个性化图像美学评估（PIAA） | 本文核心任务 |
| mean opinion score (MOS) | 平均意见分数（MOS） | GIAA 的真值 |
| aesthetic offset | 美学“偏移” | 残差学习所得的个性化偏移 |
| subject | 被试 | 主观实验参与者，全文统一 |
| annotation | 标注 | 不译作“注释” |
| label system | 标注体系 | |
| image-oriented objective attributes | 面向图像的客观属性 | 9 项 |
| human-oriented subjective attributes | 面向人的主观属性 | 4 项 |
| aesthetics score | 美学分数 | 1–5 |
| quality score | 质量分数 | 1–5 |
| object emphasis | 主体突出 | 二值，指画面中是否存在显著主体 |
| depth of field | 景深 | |
| content preference | 内容偏好 | |
| difficulty of judgement | 判断难度 | 取值 [-1, 0, +1] |
| willingness to share | 分享意愿 | |
| emotion | 情感 | 8 类归为积极/消极/中性三组 |
| Big-Five personality traits | 大五人格特质 | O / C / E / A / N |
| user portrait | 用户画像 | 含 subject portrait，统一译法 |
| desensitized | 脱敏 | 指去除个人身份信息 |
| Pearson Linear Correlation Coefficient (PLCC) | 皮尔逊线性相关系数（PLCC） | |
| Spearman Rank Order Correlation Coefficient (SROCC) | 斯皮尔曼等级秩序相关系数（SROCC） | |
| backbone | 骨干网络 | |
| support set / query set | 支持集 / 查询集 | 少样本评测设置 |
| few-shot | 少样本（few-shot） | |
| control group | 对照组 | 对应 without finetune 组 |
| region of interest (ROI) | 兴趣区域（ROI） | |
| transductive learning | 直推式学习 | |
| scene category | 场景类别 | 9 类 + “其他” |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0007 | IAA 分 GIAA 与 PIAA；MOS 只是“平均意见”；早期工作从多模态、元学习、多任务、强化学习等角度切入 | 图像美学评估（IAA）……可分为通用与个性化两类……平均意见分数（MOS）……多模态协同学习 [17]、元学习 [21]、多任务学习 [7]、深度强化学习 [10]…… | 一致，引用编号与分类未增删 |
| b0014 | 31,220 幅图像、438 名被试、平均 25 人/图、4 主观 + 9 客观属性 | 采集了 31,220 幅图像，每幅平均由 25 名被试标注，被试总数 438；4 项主观 + 9 项客观属性 | 数字全部原样保留 |
| b0032 | 判断难度取值 [-1, 0, +1]，+1 困难 / 0 一般 / -1 容易 | 判断难度为取值于 [-1, 0, +1] 的离散标签……“+1”困难、“0”一般、“-1”容易 | 一致，区间符号未改写 |
| b0067 | 高 N 特质（神经质）被试反应过度；E 特质 PLCC 超 0.8 | 高“N”特质即“神经质”……PLCC 已超过 0.8，属于“强相关” | 一致，0.8 与特质字母原样保留 |
| b0086 | 40 名测试被试（10%）、10/100 张支持集、50 张查询集、重复 10 次 | 随机选取 40 名被试（占被试总数 10%）……10 幅与 100 幅……50 幅……重复 10 次 | 一致，全部数字与抽样规则未改动 |

### 一致性与数字核查

- 已用 Grep 对核心术语全文回扫：`用户画像` 统一 8 处（原先“被试画像”2 处已统一为“用户画像”）；`图像质量评估` 1 处；`条件式 PIAA` / `无条件 PIAA` 采用固定对举译法。
- 数字核查：31,220、438、25、40、10、100、50、446、28,000、3,000、40,000、210、10,000、190、197–222、205、2.0、4.0、0.5、0.8、4 / 2.5 / 3.5 等均与原文逐字一致；区间记号 `(4, 5]`、`[1, 2]`、`(2, 3]`、`(3, 4]`、`[-1, 0, +1]`、`[1, 5]` 原样保留。
- 占位符核查：`b0050` 中的 `⟦SLOT_0⟧` 原样保留，构建脚本报告槽位总数 1、已还原 1、残留 0。
- 编码核查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0。
- 未被翻译的内容：表 1–4、图 1–11 的图形对象、参考文献 [1]–[22] 均按 `t:"keep"` 规则原样保留。
- 原文脚注标记（如 `** * https://www.flickr.com`、`†† † Amazon Mechanical Turk`、`‡‡ ‡`、`§§ §`、`¶¶ ¶`）按原文形态保留，未作删改。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- `b0021` 与 `b0027` 中的脚注符号在 HTML 抽取时已退化为纯文本标记（`** *`、`†† †` 等），含义可辨但排版形态与 PDF 原版略有差异，属上游抽取所致，非翻译问题。
- `object emphasis` 在 AADB 语境下亦有“主体显著性”等译法，本文统一取“主体突出”，以与该词在属性列表中的二值语义一致。


## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0009`、`b0055`、`b0063`、`b0050`、`b0048`、`b0065`（种子 3）；`b0039`、`b0048`、`b0075`、`b0036`、`b0088`、`b0032`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
