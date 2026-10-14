# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 297（文本 218 / 原子 79）|
| 已译文本块 | 218 / 218 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 59 · 已还原 59 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 126 |
| `<img>` 元素 | 46 |
| `<table>` 元素 | 22 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Aesthetic Assessment (IAA) | 图像美学评估（IAA） | 首次出现附英文缩写，后文统一用中文或 IAA |
| Aesthetic Critique Captioning | 美学评论生成 | 与 AIC 视为同一任务的两种说法 |
| Aesthetic Image Captioning (AIC) | 美学图像描述（AIC） | 同上 |
| photo critique | 摄影评论 | 全文统一，不译作"照片点评" |
| Reddit Photo Critique Dataset (RPCD) | Reddit 摄影评论数据集（RPCD） | 数据集名保留英文缩写 |
| Photo Critique Captioning Dataset (PCCD) | PCCD | 数据集名不译 |
| sentiment polarity | 情感极性 | 全文统一 |
| sentiment score | 情感分数 | 与 aesthetic score（美学分数）严格区分 |
| aesthetic score | 美学分数 | 全文统一 |
| Vision Transformer (ViT) | Vision Transformer（ViT） | 按术语库不译 |
| Data-efficient image Transformer (DeiT) | DeiT | 模型名保留 |
| AestheticViT | AestheticViT | 作者自命名模型，不译 |
| linear probe | 线性探针 | 保持"ViT + 线性探针"写法一致 |
| shot scale | 景别 | 摄影专业术语，含极特写/特写/中景/全景/远景 |
| composition rule | 构图规则 | 三分法等九类的统称 |
| Rule of Thirds (RoT) | 三分法（RoT） | 首次出现附缩写 |
| SRCC (Spearman's Rank Correlation Coefficient) | 斯皮尔曼秩相关系数（SRCC） | 首次出现附英文全称 |
| PLCC / LCC (Pearson's Linear Correlation Coefficient) | 皮尔逊线性相关系数（PLCC / LCC） | 原文混用 PLCC 与 LCC，均按此处理 |
| informativeness score | 信息量分数 | 全文统一 |
| Earth Mover's Distance (EMD) | Earth Mover's Distance（EMD） | 度量名保留 |
| subreddit | 子版块 | 首次出现附 subreddit 原词 |
| top level comment | 顶层评论 | 与"一级评论"统一为顶层评论 |
| topic modeling | 主题建模 | BERTopic 所用方法 |
| NSFW | NSFW | 原样保留 |
| datasheet | 数据说明书 | 首次出现附 datasheet 原词 |
| UltraHD / FullHD | 超高清（UltraHD）/ 全高清（FullHD） | 分辨率档位名 |
| weakly-supervised labeling | 弱监督标注 | 通用术语 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0005 | IAA 因数字摄影增长受关注；单一数值分数的三点局限；Flickr/Photo.net/Instagram 评论比评分信息量更大 | 逐条对应译出三项局限与三个平台名，示例评论原文照录并附中文 | 一致，数字与引用编号未改动 |
| b0027 | 给定图像 ⟦SLOT_19⟧ 与 ⟦SLOT_20⟧ 条评论，对每条评论 ⟦SLOT_21⟧ 做情感极性分析定义美学分数 ⟦SLOT_22⟧ | 占位符 19–25 全部原样保留，语义与原文逐句对应 | 一致，7 个占位符数量对齐 |
| b0039 | 73,965 张图像、219,790 条评论、平均 49.1 词、标准差 55.5、最长 1286 词、每张平均 2.9 条评论、标准差 3.7 | 全部数字原样保留，含千分位写法 | 一致，未做任何换算或四舍五入 |
| b0067 | ViT Large（AestheticViT）在 AVA 上比 [14] 高 4%；准确率以分数 >5 定义高质量；支持 Hosu 等人的相关性指标主张 | 4%、阈值 5、引用编号 [14] 均原样保留 | 一致，未添补解释 |
| b0192 | ViT-B/32 SRCC 0.446 vs ViT-B/16 0.759；ViT-T/16 0.725 vs ViT-L/16 0.793；ImageNet-21k 预训练提升约 0.02 | 四个小数与模型编号原样保留，patch 大小用 ⟦SLOT_49⟧/⟦SLOT_50⟧ 还原 | 一致，占位符对齐 |

### 一致性与数字核查

- 术语统一：用 Grep 在 `zh.json` 中检索"图像美学评估""美学评论生成""情感分数""情感极性""景别""构图规则""信息量分数""线性探针"等核心术语，全文译法唯一，未出现同义词轮换（如"美学评分"与"美学分数"、"照片评论"与"摄影评论"均已统一）。
- 数字核查：数据规模（74K / 220K / 73,965 / 219,790 / 216K / 8K）、相关系数（0.6418、0.6424、0.6066、0.6499、0.446、0.759、0.725、0.793）、百分比（51.20%、89.07%、4%、0.35%、61%、48%、64%、29%、7%）、准确率（87.08%、33.36%、99.72%）与超参数（学习率、批大小、轮数）均未改动或换算。
- 占位符完整性：脚本统计内联槽位总数 59、已还原 59；另用脚本逐块比对原文与译文的 `⟦SLOT_n⟧` 集合，218 个文本块全部一致，无遗漏、无改写编号、无新增。
- 编码检查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0，文件编码 UTF-8。
- 不变量：表格、代码块、公式、图片、参考文献块一律未翻译；未删减、合并或拆分任何段落，一块对一块。

### 遗留问题

- 无。图片引用缺失 0，公式渲染元素 126 个均正常还原，未发现原文乱码或不可解析的块。

## 复核记录（第二轮交叉验证）

抽查块：b0030、b0291、b0058、b0208、b0067、b0246


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
