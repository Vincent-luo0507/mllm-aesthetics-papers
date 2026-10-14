# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 320（文本 164 / 原子 156）|
| 已译文本块 | 164 / 164 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 119 · 已还原 119 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 239 |
| `<img>` 元素 | 100 |
| `<table>` 元素 | 6 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image quality assessment (IQA) | 图像质量评价 | 全文统一，不写作“质量评估” |
| aesthetic assessment | 美学评价 | 与 technical quality assessment 对举 |
| technical quality | 技术质量 | 指噪声/模糊/压缩等低层退化 |
| full-reference / no-reference | 全参考 / 无参考 | 盲评价统一写“无参考” |
| mean opinion score (MOS) | 平均意见分数 | 首次出现括注英文 |
| convolutional neural network (CNN) | 卷积神经网络（CNN） | 首次括注，后文用 CNN |
| earth mover's distance (EMD) | 推土机距离（EMD） | 有序类别损失的度量 |
| probability mass function | 概率质量函数 | 评分分布 p 与 p̂ |
| score bucket | 分数区间 | 1–10 分的离散桶 |
| cumulative distribution function (CDF) | 累积分布函数 | 闭式 EMD 解中使用 |
| linear correlation coefficient (LCC) | 线性相关系数（LCC） | 表 I/II/III 指标 |
| Spearman's rank correlation coefficient (SRCC) | 斯皮尔曼等级相关系数（SRCC） | 原文一处笔误 SROC 已按 SRCC 处理 |
| ordered classes | 有序类别 | 评分区间天然有序 |
| standard deviation | 标准差 | 与 unconventionality 关联 |
| unconventionality | 非常规性 | AVA 中的“见仁见智”程度 |
| baseline network | 基线网络 | ImageNet 预训练骨干 |
| fully-connected layer | 全连接层 | 替换分类器末层 |
| soft-max | softmax | 输出 10 类质量概率 |
| dropout | dropout | 保留英文 |
| exponential decay | 指数衰减 | 学习率调度 |
| stochastic gradient descent (SGD) | 随机梯度下降 | 优化器 |
| data augmentation | 数据增强 | 缩放+随机裁剪+水平翻转 |
| over-fitting | 过拟合 | 小数据集风险 |
| photo ranking | 照片排序 | III-C 应用 |
| multi-layer Laplacian | 多层拉普拉斯 | 色调增强技术 [43] |
| Turbo denoising | Turbo 去噪 | 以域变换为核心 [44] |
| spatial / range smoothing parameter | 空间 / 值域平滑参数 | 去噪器待调参数 |
| signal-to-noise ratio | 信噪比 | 解释纹理图最优参数偏低 |
| inference | 推理 | 表 V 计时场景 |
| AVA / TID2013 / LIVE | AVA / TID2013 / LIVE | 数据集名原样保留 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性 |
|---|---|---|---|
| b0005 | 区分技术质量（噪声/模糊/压缩）与美学（语义层），全参考 vs 无参考，MOS 主观性，CNN 微调范式 | 对应译出四类区别、PSNR/SSIM 举例、ImageNet 初始化后微调 | 一致，无增删 |
| b0023 | 预测评分分布而非二分类或回归均值；采用平方 EMD 损失；可同时预测标准差/非常规性 | 三项贡献逐条对应，EMD 全称“推土机距离” | 一致 |
| b0036 | TID2013 强制选择实验，均值与离散度弱相关，含脚注说明对比度变化趋势不明显 | 正文+脚注内容均译出，图 3(c)、图 4、图 5 引用保留 | 一致 |
| b0094 | 类别按序排列、ℓ 范数距离、EMD 定义为最小搬运代价，⟦SLOT_88⟧–⟦SLOT_94⟧ 共 7 个占位符 | 占位符逐个原样保留，语义与公式说明一致 | 一致 |
| b0192 | Turbo 去噪：噪声 σ=30、50 个随机裁剪平均、(a)(g) 平滑图参数高于 (j)、图 16 欠/过平滑 | 数字 30、50、图号与各子图标签全部保留 | 一致 |

### 一致性与数字核查

- 术语：以 Grep 复核 zh.json，图像质量评价、美学评价、无参考、概率质量函数、推土机距离、标准差、非常规性等核心术语全文译法唯一，未出现同义轮换。
- 数字：255,000、200、900、1–10、5.5、1.4、1.43、3000、25、24、120、9、985、1162、175、0.9、0.75、10、0.95、8:2、250、30、50、6/11/11、726 以及各图注中的分数（6.38/7.16 等）均原样保留，未做单位换算或四舍五入。
- 占位符：以脚本逐块比对，`⟦SLOT_0⟧`–`⟦SLOT_118⟧` 共 119 处在译文中数量与顺序完全一致，脚本 stray=0。
- 编码：zh.json 与 index.html 均不含 U+FFFD。

### 遗留问题

- 无缺失图片（missing_img=0）。
- 表 I/II 表头原文将 SRCC 误写作 SROC，译文统一按 SRCC（斯皮尔曼等级相关系数）处理。
- 部分公式块为独立原子块（未列入文本块），按规范不作翻译。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0103、b0028、b0083、b0113、b0269、b0224），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
