# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 154（文本 67 / 原子 87）|
| 已译文本块 | 67 / 67 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 4 · 已还原 4 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 9 |
| `<img>` 元素 | 4 |
| `<table>` 元素 | 7 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | 首次括注，后文可用 MLLM |
| image aesthetics perception (IAP) | 图像美学感知（IAP） | 全文统一 |
| image aesthetics assessment (IAA) | 图像美学评价（IAA） | IAP 的子任务 |
| aesthetic attribute | 美学属性 | 色彩／光线／构图等 |
| aesthetic emotion | 美学情感 | |
| image aesthetics caption | 图像美学描述 | |
| instruction tuning / fine-tuning | 指令微调 | 全文统一，不作"指令调优" |
| instruction-following data | 指令跟随数据 | |
| aesthetic critique | 美学评论 | AesFeedback 的基本单元 |
| coarse-grained / fine-grained / finer-grained | 粗粒度 / 细粒度 / 更细粒度 | 三级渐进式提问 |
| subjective experiment | 主观实验 | |
| AesFeedback / AesMMIT / AesVQA | AesFeedback / AesMMIT / AesVQA | 数据集名保留 |
| natural / artistic / AI-generated images (NI/AI/AGI) | 自然图像（NI）/ 艺术图像（AI）/ 人工智能生成图像（AGI） | 三类图像源 |
| question types (Yes-or-No / What / How / Why) | Yes-or-No 型 / What 型 / How 型 / Why 型 | 保留英文类型名 |
| multiple-choice | 多选 | 附加题型 |
| visual encoder | 视觉编码器 | |
| cross-modality module | 跨模态模块 | |
| projector | 投影器 | 视觉—语言连接 |
| hallucination | 幻觉 | MLLM 的关键挑战 |
| AesBench | AesBench | 评测基准，保留原名 |
| Aesthetic Perception (AesP) | 美学感知（AesP） | AesBench 四维度之一 |
| Aesthetic Empathy (AesE) | 美学共情（AesE） | 四维度之二 |
| Aesthetic Assessment (AesA) | 美学评价（AesA） | 四维度之三 |
| Aesthetic Interpretation (AesI) | 美学阐释（AesI） | 四维度之四 |
| backbone | 骨干网络 | |
| GPT scoring | GPT 评分 | AesI 的评测方式 |
| long-tail distribution | 长尾分布 | 图像采样问题 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性 |
|---|---|---|---|
| b0009 | 三阶段之阶段 1：渐进式提问三个部分、AesFeedback 含 88K 反馈 / 21,904 幅图像 | 三部分与两个数字均保留 | 一致 |
| b0027 | 图像采集：三类图像源、场景分类模型、1239 幅高美学图像、1944 幅低质量图像、21,904 幅总计 | 五个数字原样保留，数据集名与引用完整 | 一致 |
| b0028 | 被试：五个维度、色盲检测、6 名艺术从业者、9 名研究者、两次培训、48 名被试 | 六个数字与筛选条件逐条对应 | 一致 |
| b0045 | 模型结构三部分：CLIP-ViT-L14、336⟦SLOT_5⟧336、576 token、两层 MLP、Vicuna-v1.5、两个 LLaVA 变体、mPLUG-Owl2 | 结构描述与两处数字、一处占位符均保留 | 一致 |
| b0072 | 美学阐释：精确性提升 41.50%、44.60%、25.90%；LLaVA-1.5-7B 与 mPLUG-Owl2 提升 16.00%、15.40% | 五个百分数原样保留 | 一致 |

### 一致性与数字核查

- 术语：复核 zh.json，图像美学感知、指令微调、指令跟随数据、美学评论、粗／细粒度、美学阐释、幻觉等核心术语全文译法唯一，未出现同义轮换。
- 数字：21,904、88K、409K、21K、48、1239、1944、6、9、2、336、576、2,800、10%、12%、15.72%、15%、41.50%、44.60%、25.90%、16.00%、15.40%、250K、1,455K、100K、1.2M、13、8、80G、2、24G 等均未改动。
- 占位符：脚本逐块比对，`⟦SLOT_0⟧`–`⟦SLOT_5⟧` 共 4 处（含 b0013、b0014、b0015、b0045）数量与顺序完全一致，stray=0。
- 编码：zh.json 与 index.html 均不含 U+FFFD。

### 遗留问题

- 无缺失图片（missing_img=0）。
- 表 3 等表头中的缩写（T. Q.、C. L.、Comp.、Cont.、Emot.、Inte.、Uniq.、Rele.、Prec.）在译文中以中文全称加原缩写的形式给出，便于对照。
- b0048 原文未给出 AesP 与 AesE 的缩写对照，译文沿用表 3 注释中的维度名，未额外增补。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0030、b0031、b0048、b0072、b0023、b0017），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
