# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 193（文本 131 / 原子 62）|
| 已译文本块 | 131 / 131 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 8 · 已还原 8 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 80 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 11 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| artifact (Artifact) | 制品 | 自包含、可执行的生成单元，首现保留英文 |
| interactive visual artifact | 交互式视觉制品 | 全文统一 |
| visual fidelity | 视觉保真度 | |
| interactive integrity | 交互完整性 | |
| MLLM-as-Judge | 以多模态大语言模型为评审 | 首现保留英文 |
| referee | 评审模型 | 与 judge 统一 |
| checklist | 检查清单 | 十维评分表 |
| staged / temporal screenshot | 分阶段截图 | 交互前/中/后三张 |
| sandbox | 沙箱 | |
| execution harness | 执行环境 | 指 Playwright + 无头 Chromium |
| ranking consistency | 排名一致性 | |
| pairwise agreement (Pair ACC) | 两两一致率 | 指标名保留 Pair ACC |
| Footrule (distance) | Footrule（距离） | 排序距离度量，保留专名 |
| WebDev Arena | WebDev Arena | 不译 |
| generalist / specialist model | 通用模型 / 专用模型 | |
| instruction-tuned | 指令微调 | |
| coder-specialized | 代码专用 | |
| slow thinker | "慢思考"模型 | 长推理模型 |
| vision-oriented / code-oriented | 视觉导向 / 代码导向 | 两类检查维度 |
| difficulty stratification | 难度分层 | Easy/Medium/Hard |
| partial-order constraint | 偏序约束 | 排序关系 |
| version stability | 版本稳定性 | 评审模型版本替换不变性 |
| de-duplication / contamination | 去重 / 污染 | 数据构建环节 |
| MinHash | MinHash | 算法名保留 |
| perceptual hashing | 感知哈希 | |
| provenance | 来源 | 数据溯源 |
| viewport | 视口 | |
| DOM | DOM | 文档对象模型，首现括注 |
| hallucination | 幻觉 | |
| version drift | 版本漂移 | |
| agentic | 智能体式 | 多轮自主迭代 |
| double-blind | 双盲 | 人工评测协议 |
| distillation | 知识蒸馏 | |
| front-end | 前端 | |
| interaction trajectory | 交互轨迹 | |
| SV / MMD / HD / II | 静态视觉 / 轻中度动态 / 高动态 / 强交互 | 表内缩写保留原样 |
| IFLEN | IFLEN | 回答长度指标 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0008 | 1,825 个任务、九个领域、三层复杂度、贡献三方面 | 数字与结构逐项对应 | 一致 |
| b0011 | 30+ LLM、280 实例、两两一致率 90.95%、WebDev Arena 94.4% | 全部数值原样保留 | 一致 |
| b0028 | 难度比例 30%/40%/30%，实际划分 559/611/655，留一族重采样 | 比例与划分数字一致 | 一致 |
| b0080 | Footrule 一致性 94.4% vs WebBench 69.4%；o3-mini 排名略高于人类投票的原因 | 数值与因果表述完整译出，未添加评价 | 一致 |
| b0164 | 五种消融配置 w/o img、w/ img、w/ imgs、w/ caption、only w/ imgs | 配置项英文缩写原样保留并给出中文说明 | 一致 |

### 一致性与数字核查

- 术语统一：Grep 复核"制品""检查清单""评审模型""分阶段截图""视觉保真度""偏序约束"在 zh.json 中用法唯一；`judge` 与 `referee` 统一译为"评审模型"，`artifact` 统一译为"制品"，未出现"工件/构件""裁判/评判"等同义轮换。
- 数字核查：1,825、30+、280、90.95%、94.4%、69.4%、559/611/655、30%/40%/30%、10、5、50、3、5、9、6、10%、280、11 等全部原样保留，未换算或改写；表内英文缩写（AVG、IFLEN、RANK、Pair ACC、SV/MMD/HD/II）保持原样。
- 占位符完整性：脚本逐块比对 `⟦SLOT_n⟧` 序列，131 个文本块，输出 slot mismatch: []，0 处偏差。
- 编码检查：zh.json 与 index.html 中不含 U+FFFD（构建脚本 mojibake=0）。

### 遗留问题

- 原文 b0080 中脚注标记与正文粘连（"consistency11 1 Based on the ⟦SLOT_5⟧ distance"），按语义断句译为"一致性11 1 基于排序向量之间的 ⟦SLOT_5⟧ 距离"，未改动源文件。
- 原文 b0088 标题为 "First Autors"（疑似拼写错误），按语义译为"第一作者"，未改动源文件。
- 图片文件全部齐备（missing_img=0）。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽样 6 块（b0021、b0061、b0177、b0077、b0025、b0008）语义、数字、术语均无误。另对全文做了脚注残留扫描，发现并修正 1 处：

| 块 ID | 问题类型 | 修正前 → 修正后 |
|---|---|---|
| b0080 | 脚注标记残留（且含多余句号） | `94.4% 的归一化 Footrule 一致性11 1 基于排序向量之间的 ⟦SLOT_5⟧ 距离；越接近 1 越好。，而 WebBench` → `94.4% 的归一化 Footrule 一致性（基于排序向量之间的 ⟦SLOT_5⟧ 距离；越接近 1 越好），而 WebBench`|

修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
