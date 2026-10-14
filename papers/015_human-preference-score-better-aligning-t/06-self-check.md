# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 249（文本 180 / 原子 69）|
| 已译文本块 | 180 / 180 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 17 · 已还原 17 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 46 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 7 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Human Preference Score (HPS) | 人类偏好分数（HPS） | 论文核心指标，首次出现括注英文缩写 |
| human preference classifier | 人类偏好分类器 | 全文统一，不写作"偏好分类模型" |
| text-to-image generation | 文本到图像生成 | 全文统一，未采用"文生图" |
| prompt | 提示词 | 全文统一，未混用"提示" |
| Inception Score (IS) | Inception Score（IS） | 指标名不译 |
| Fréchet Inception Distance (FID) | Fréchet Inception Distance（FID） | 指标名不译 |
| CLIP score | CLIP score | 指标名保留英文 |
| Aesthetic Score Predictor | Aesthetic Score Predictor | 工具名保留英文 |
| preference accuracy | 偏好预测准确率 | 表格中 Preference Acc. 译作"人类选择预测准确率" |
| non-preferred image | 非偏好图像 | 全文统一，未写作"负样本图像"（仅在统计处用"负样本"） |
| adapted model | 调整后模型 | 与表 4「Adapted model」对应 |
| regularization image | 正则化图像 | 训练中用于正则化的真实图像 |
| classifier-free guidance | 无分类器引导 | 标准译法 |
| negative prompt | 负提示 | 推理阶段的反向条件 |
| low-rank adaptation (LoRA) | LoRA | 不译 |
| UNet | UNet | 不译 |
| VAE | VAE | 不译 |
| noise scheduler | 噪声调度器 | PNDM 所属的采样调度组件 |
| guidance scale | 引导系数 | 全文统一 |
| user study | 用户研究 | 全文统一，未写作"人工评测" |
| artifact | 瑕疵 | 指生成图像中的形变/伪影 |
| shape artifact | 形状瑕疵 | 与纹理偏向问题对应 |
| domain gap | 域差距 | 标准译法 |
| alignment tax | 对齐税 | 引自 InstructGPT 的概念 |
| NSFW | NSFW | 保留原文缩写，括注中文解释 |
| datasheet | 数据说明书 | 附录 A 标题 |
| instance | 实例 | 数据说明书中的条目单位 |
| cherry-pick | 反复挑选 | 用户需多次筛选才能得到满意的图像 |
| pseudo ground truth | 伪真值 | FID 计算时的替代目标图像 |
| Stable Foundation Discord channel | Stable Foundation Discord 频道 | 数据来源，保留平台专名 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0011 | 98,807 images / 25,205 human choices；IS、FID、CLIP score 均不能完全匹配人类选择 | 数据集包含 98,807 张图像与 25,205 次人类选择；IS、FID 与 CLIP score 都不能完全吻合人类选择 | 数字一致，语义一致，无增补 |
| b0027 | 23,722 条提示词对应四张图像、953 条三张、530 条两张；2,659 位用户，单用户最多 267 次选择 | 逐项照译，五个数字原样保留 | 数字与分组关系完全对应 |
| b0055 | 训练数据取自 DiffusionDB 的 large_first_1m 划分与 LAION-5B 子集；含 ⟦SLOT_3⟧/⟦SLOT_4⟧ | 训练数据来自 DiffusionDB 的「large_first_1m」划分与 LAION-5B 子集；两个占位符原样保留 | 占位符数量与位置一致 |
| b0076 | α=2.0、37,572 / 21,108 张图像、625k 子集、阈值 6.5、200,231 张正则化图像、rank 32、10k 迭代、batch 40、50 步、7.5 | 全部数字原样保留，含 ⟦SLOT_11⟧～⟦SLOT_13⟧ | 数字与占位符均无遗漏 |
| b0087 | 结论三段：指标与偏好不符；CLIP 可微调为偏好分类器；提出简单有效的方法 | 译文按同样三句组织，未添加评价性内容 | 语义一致，无添油加醋 |

### 一致性与数字核查

- 术语统一性：已用 Grep 核查「人类偏好分类器」「提示词」「非偏好图像」「调整后模型」「正则化图像」等核心术语，全文译法唯一，未出现同义轮换；「Fréchet Inception Distance」统一带重音符号原样保留。
- 数字核查：98,807 / 25,205 / 23,722 / 953 / 530 / 2,659 / 267 / 20,205 / 79,167 / 224 / 5 / 10 / 10,000 / 37,572 / 21,108 / 625k / 6.5 / 200,231 / 32 / 10k / 40 / 50 / 7.5 / 398 / 74% / 22% 等全部与原文一致；表 1～表 4 为 keep 块，未作改动。
- 占位符完整性：原文 17 个 `⟦SLOT_n⟧` 全部原样保留，编号未改写，构建后 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 均不含 U+FFFD。

### 遗留问题

- 原文 b0247「See Fig. 11 and Fig. 11」疑为笔误（应为 Fig. 10 与 Fig. 11），按原文直译为「图 11 与图 11」，未作修正。
- 原文 b0079 提到「In Fig. 3, we visualize our result」，与上下文（人工评估结果）应为 Fig. 8，同样按原文直译未改。
- 无图片缺失，无原文乱码。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；11 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0146、b0074、b0143、b0026、b0173、b0043（seed=2）；加抽 b0089、b0028、b0038、b0009（seed=7）
- 另逐块复核短译文块 b0029（259→54 字符，中文压缩所致，两个信息点「第 4 节相关性研究」「第 5 节分类器训练数据」均完整保留）。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
