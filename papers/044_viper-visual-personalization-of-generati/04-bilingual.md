# ViPer：通过个体偏好学习实现生成模型的视觉个性化

> 原标题：ViPer: Visual Personalization of Generative Models via Individual Preference Learning
> 作者：Sogand Salehi, Mahdi Shafiei, Teresa Yeo, Roman Bachmann, Amir Zamir · arXiv:2407.17365 · 2024-07-24

<!-- [原子块 · verbatim] ViPer: Visual Personalization of Generative Models via Individual Preference Learning -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Different users find different images generated for the same prompt desirable. This gives rise to personalized image generation which involves creating images aligned with an individual’s visual prefe -->

<!-- [原子块 · verbatim] We propose to personalize the image generation process by first capturing the generic preferences of the user in a one-time process by inviting them to comment on a small selection of images, explaini -->

<!-- [原子块 · verbatim] Our code and model weights are open sourced at https://viper.epfl.ch . -->

<!-- [原子块 · img]  -->

**EN** Figure 1: We introduce ViPer, a method that personalizes the output of generative models to align with different users’ preferences for the same prompt. This is done via a one-time capture of the user’s general preferences and conditioning the generative model on them without the need for engineered detailed prompts. Notice how the results vary for the same prompt for different users based on their visual preferences.

**ZH** 图 1：我们提出 ViPer，一种把生成模型的输出个性化、使其与不同用户对同一提示词的偏好相对齐的方法。该方法通过一次性采集用户的总体偏好，并以此为条件约束生成模型，无需人工设计详尽的提示词。注意对同一提示词，不同用户因其视觉偏好不同而得到各异的结果。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Text-to-image generative models [28, 12] have demonstrated the ability to produce high-fidelity images and exhibit remarkable generalization abilities. This capability has sparked considerable interest regarding their potential applications which include image editing [13, 25, 2, 23], style transfer [9, 3, 30], and generating training data [10, 31, 22, 41].

**ZH** 文本到图像生成模型 [28, 12] 已展现出生成高保真图像的能力与出色的泛化能力。这一能力引发了人们对其潜在应用的广泛兴趣，包括图像编辑 [13, 25, 2, 23]、风格迁移 [9, 3, 30] 以及生成训练数据 [10, 31, 22, 41]。

**EN** These applications generally require guiding the generative model towards certain desired outputs. In this work, we are interested in guiding the generations toward an individual’s preferences in images, or personalization.

**ZH** 这些应用通常要求把生成模型引导至某些期望的输出。本工作关注的是把生成结果引导至个体在图像上的偏好，即个性化。

**EN** Current methods for producing personally desirable images require the users to iteratively refine their prompts until they achieve their preferred outcomes or incorporate sparse feedback. Some forms of this feedback include binary reactions [36], providing images that the individual likes or dislikes [33, 7, 29], or ranking a given set of images [35].

**ZH** 现有生成个性化合意图像的方法，要求用户反复迭代地修改提示词直至获得偏好的结果，或引入稀疏反馈。这类反馈的形式包括二元反应 [36]、提供个体喜欢或不喜欢的图像 [33, 7, 29]，或对给定图像集合排序 [35]。

**EN** We propose to utilize the individuals’ comments on a given set of images for capturing their generic visual preferences. This allows them to express why they like or dislike certain images. We will demonstrate, through user studies, that this increased level of expressivity results in generations better aligned with individual preferences. To incorporate this feedback into a text-to-image model like Stable Diffusion [28, 26], we first transform these comments into a structured representation containing visual attributes, i.e., a set of features they like or dislike in images, e.g., surrealism, rough brushstrokes, monochromatic, etc. We demonstrate that we can condition Stable Diffusion on these visual preferences without any additional fine-tuning. We call our method Visual Personalization of Generative Models via Individual Preference Learning, or ViPer for short.

**ZH** 我们提出利用个体对给定图像集合的评论来捕捉其通用视觉偏好，这使他们能够表达为何喜欢或不喜欢某些图像。我们将通过用户研究证明，这种更高的表达自由度使生成结果与个体偏好的契合度更高。为把这些反馈融入 Stable Diffusion [28, 26] 之类的文本到图像模型，我们首先把这些评论转换为一种包含视觉属性的结构化表示，即他们在图像中喜欢或不喜欢的一组特征，如超现实、粗犷笔触、单色调等。我们证明，可以在不做任何额外微调的情况下，以这些视觉偏好为条件约束 Stable Diffusion。我们把该方法命名为基于个体偏好学习的生成模型视觉个性化，简称 ViPer。

**EN** Our user studies show that users prefer our method over other baselines most of the time. They also strongly favor personalized results tailored to their preferences compared to non-personalized results or results from other users.

**ZH** 我们的用户研究表明，用户在多数情况下更偏好我们的方法而非其他基线；与非个性化结果或其他用户的结果相比，他们也明显更青睐按自身偏好定制的个性化结果。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Aligning image generative models with general human preferences. Generative models such as Stable Diffusion [28] are trained on images from the internet. Thus, their generations may reflect the artifacts of such data e.g., unusual object poses. This is not ideal if the goal is to generate aesthetically pleasing images e.g., high quality images where the object is centered and unoccluded. To align image generative models with these general goals, as opposed to an individual’s preference, these models are often tuned with reinforcement learning from human feedback (RLHF) [37, 4, 27] to maximize scoring metrics [39, 14, 40, 32] and improve image quality. [8, 38] optimize input prompts instead to achieve the same. While these methods enhance the quality of results by making them aesthetically aligned with general human preferences, ViPer focuses on an individual’s preferences and generates personalized images.

**ZH** 让图像生成模型与通用人类偏好相对齐。Stable Diffusion [28] 等生成模型在互联网图像上训练，因此其生成结果可能反映此类数据的瑕疵，例如不寻常的物体姿态。若目标是生成具有美感的图像（如物体居中、无遮挡的高质量图像），这并不理想。为使图像生成模型与这些通用目标（而非个体偏好）相对齐，人们通常用基于人类反馈的强化学习（RLHF）[37, 4, 27] 调优这些模型，以最大化评分指标 [39, 14, 40, 32] 并提升图像质量；[8, 38] 则改为优化输入提示词来达到同样目的。这些方法通过使结果与通用人类偏好在美学上相对齐来提升质量，而 ViPer 聚焦于个体偏好，生成个性化图像。

**EN** Aligning image generative models with individual’s preferences. Personalization methods seek to adapt generative models to specific concepts, such as styles, by leveraging feedback or direct inputs from individuals. Popular examples include [7] and [29], which aim to learn a representative token for desired concepts, and guidance methods [34, 6, 11, 18], which steer sampling towards images that satisfy a desired objective by adding an auxiliary term to the score function. [33] learns a new style by fine-tuning a few trainable parameters from a reference image and improving the quality via iterative training with either human or automated feedback while [36] is a training-free method that incorporates iterative feedback into the generation process of text-to-image models. These methods mostly rely on users to express their preference for a set of images by simply liking or disliking them, or by providing images themselves. In contrast, ViPer allows users to express their detailed opinions about a given set of images to generate personalized results. This is a one-time process and users aren’t required to provide further feedback. In section 4.2, we show that the additional flexibility and expressivity of comments result in generations more aligned with users’ preferences.

**ZH** 让图像生成模型与个体偏好相对齐。个性化方法旨在借助个体的反馈或直接输入，使生成模型适配特定概念（如风格）。代表性工作包括 [7] 与 [29]，它们旨在为期望概念学习一个代表性词元；以及引导类方法 [34, 6, 11, 18]，它们通过在分数函数中加入辅助项，把采样过程导向满足期望目标的图像。[33] 通过微调少量可训练参数从参考图像中学习新风格，并借助人工或自动反馈的迭代训练提升质量；[36] 则是一种免训练方法，把迭代反馈引入文本到图像模型的生成过程。这些方法大多依赖用户通过简单的喜欢/不喜欢，或自行提供图像来表达对一组图像的偏好。相比之下，ViPer 允许用户对给定图像集合表达详尽看法，从而生成个性化结果；这是一个一次性过程，用户无需再提供进一步反馈。在第 4.2 节中，我们证明评论所提供的额外灵活性与表达力使生成结果更贴合用户偏好。

<!-- [原子块 · img]  -->

**EN** Figure 2: (Left) Capturing an individual’s preference from comments. We ask interested individuals to comment on a small set of images. These images are generated such that they have diverse styles (see fig. 7 for visuals and further details). Note that these comments are not required to be of a specific structure. Thus, users can write as much or as little as they like. Obviously, more detailed and expressive comments would lead to better personalization. We show an example of an individual’s comments on two images. Our method allows for such free-form comments as we make use of a language model to extract structured preferences, i.e. a visual preference extractor (⟦SLOT_0⟧). To get the ⟦SLOT_1⟧, we fine-tune IDEFICS2-8b. Converting the user’s free-form comments into structured visual preferences is a one-time process that provides us with a concise representation of the user’s preferences. In this example, ⟦SLOT_2⟧ extracts the individual’s preferences for the color palette, vibe, and lighting from the comments and translates them into attributes like "Rich and Muted Color Palettes", "Gloomy", and "Highlights and Shadows". (Right) Conditioning Stable Diffusion on an individual’s visual preference. The user’s visual preferences are then encoded and added to the prompt embedding (see eq. 1). This allows us to steer the generations towards certain styles. They’re also used in the guidance formula (see eq. 3) directly to guide Stable Diffusion’s results toward the user’s preferences. This step does not require any fine-tuning and can be used directly with the Stable Diffusion model. Note how the generations reflect the user’s preference by generating a "Gloomy" style while avoiding styles like "Contemporary Abstract", "Vibrant Colors", and "Naive Art".

**ZH** 图 2：（左）从评论中捕捉个体偏好。我们请感兴趣的个体对一小批图像发表评论，这些图像在生成时具有多样的风格（可视化与更多细节见图 7）。注意，这些评论不要求采用特定结构，用户可长可短，随其所愿。显然，更详尽、更具表达力的评论会带来更好的个性化效果。我们展示了一位个体对两张图像的评论示例。我们的方法允许此类自由形式的评论，因为我们使用一个语言模型来提取结构化偏好，即视觉偏好提取器（⟦SLOT_0⟧）。为得到 ⟦SLOT_1⟧，我们微调了 IDEFICS2-8b。把用户的自由形式评论转换为结构化视觉偏好是一次性过程，它为我们提供了用户偏好的简洁表示。在该示例中，⟦SLOT_2⟧ 从评论中提取出该个体在色调、氛围与光照上的偏好，并将其转换为“浓郁而柔和的色调”“阴郁”“高光与阴影”等属性。（右）以个体视觉偏好为条件约束 Stable Diffusion。用户的视觉偏好随后被编码并加到提示词嵌入上（见式 1），这使我们可以把生成结果导向特定风格。它们还被直接用于引导公式（见式 3），以把 Stable Diffusion 的结果导向用户偏好。这一步不需要任何微调，可直接在 Stable Diffusion 模型上使用。注意生成结果如何通过生成“阴郁”风格、同时避开“当代抽象”“鲜艳色彩”“稚拙艺术”等风格来反映用户偏好。

**EN** 3 Method

**ZH** 3 方法

**EN** We propose a method to align text-to-image models with an individual’s visual preferences. In section 3.1, we propose an approach for computing a signal that captures an individual’s preferences. In section 3.2, we demonstrate how we can use this signal to adapt a generative model to generate personalized images. Finally, in section 3.3, we introduce a proxy metric to evaluate how well-aligned the personalized images are with the individuals’ preferences. See fig. 2 for an overview of our method.

**ZH** 我们提出一种使文本到图像模型与个体视觉偏好相对齐的方法。在第 3.1 节中，我们提出一种计算捕捉个体偏好的信号的方案；在第 3.2 节中，我们演示如何用该信号调整生成模型以生成个性化图像；最后在第 3.3 节中，我们引入一个代理指标，用于评价个性化图像与个体偏好的契合程度。方法概览见图 2。

**EN** 3.1 Capturing an individual’s visual preferences

**ZH** 3.1 捕捉个体的视觉偏好

**EN** Current methods for capturing preferences include utilizing signals such as whether an individual likes or dislikes a set of images [36], or how they rank each image within the set [35], while some require users to provide a set of representative images [7, 29, 33]. However, these signals are sparse and may only cover some aspects of an individual’s preferences.

**ZH** 现有捕捉偏好的方法使用的信号包括个体是否喜欢一组图像 [36]，或他们如何为集合中的每张图像排序 [35]；有些方法还要求用户提供一组代表性图像 [7, 29, 33]。然而，这些信号是稀疏的，可能只覆盖个体偏好的某些方面。

**EN** Furthermore, our preferences and even the images themselves can be complex, making it challenging for these signals to fully capture the intricacies of an individual’s preferences. Take for example someone who likes cool colors and realistic art and dislikes warm colors and pixel style. In traditional binary choice or ranking methods, when presented with pixel art featuring cool colors, the individual must decide whether they like the image despite the pixel style, or rank how much they like it.

**ZH** 此外，我们的偏好乃至图像本身都可能很复杂，使这些信号难以完整刻画个体偏好的细微之处。举例来说，某人喜欢冷色与写实艺术，不喜欢暖色与像素风格。在传统的二选一或排序方法中，当看到一幅冷色调的像素艺术时，该个体必须决定：尽管是像素风格，自己是否喜欢这幅图，或者要给它排多高的名次。

**EN** Capturing an individual’s preferences with free-form comments. We propose to use comments on a given set of images to capture an individual’s preferences. To do so, we first generate around 50 images with diverse art features such as style (see the fig. 7 for visuals) and ask individuals to select a random subset to comment on. Note that one can also comment on their own provided set of images if they prefer. Individuals are encouraged to discuss why they like or dislike each selected image, their perception of it, and the emotions it evokes. Importantly, individuals are not bound to any specific writing structure when commenting. They can write as much or as little as they prefer since we utilize a language model to extract structured preferences from their free-form comments. Ideally, these comments are descriptive, covering most of the attributes present in the images that are important to the individual. We show that in this case, comments on as few as eight images are enough to get personalized results (see for examples.)

**ZH** 用自由形式评论捕捉个体偏好。我们提出用对给定图像集合的评论来捕捉个体偏好。为此，我们首先生成约 50 张具有多样艺术特征（如风格，可视化见图 7）的图像，并请个体随机选择一个子集加以评论。注意，如果个体愿意，也可以对自己提供的图像集合发表评论。我们鼓励个体讨论自己为何喜欢或不喜欢每张被选中的图像、对它的感知以及它唤起的情绪。重要的是，个体在评论时不受任何特定写作结构的约束，可长可短，随其所愿，因为我们使用语言模型从其自由形式评论中提取结构化偏好。理想情况下，这些评论应具有描述性，覆盖图像中对个体重要的多数属性。我们证明，在这种情况下，对少至八张图像的评论就足以得到个性化结果（示例见）。

**EN** Converting free-form comments to a structured representation of an individual’s preferences. We propose representing an individual’s visual preferences through a set of attributes across 20 categories such as texture and color palette. Each category contains multiple attributes, e.g.within the texture category, attributes include smoothness, roughness, etc. To obtain this, we instructed several language models e.g., GPT-3.5†† † openai.com, Claude 2.1‡‡ ‡ claude.ai, and Llama 2 to output representative art categories and their corresponding attributes. By aggregating their results, we compiled a total of approximately 500 visual attributes. See page for the complete list.

**ZH** 把自由形式评论转换为个体偏好的结构化表示。我们提出用 20 个类别（如纹理、色调）下的一组属性来表示个体的视觉偏好。每个类别包含多个属性，例如在纹理类别中，属性包括平滑、粗糙等。为此，我们指示若干语言模型（如 GPT-3.5†† † openai.com、Claude 2.1‡‡ ‡ claude.ai 与 Llama 2）输出代表性的艺术类别及其对应属性。通过汇总它们的结果，我们共整理出约 500 个视觉属性。完整列表见对应页面。

**EN** To transform the free-form comments into visual preferences, we require a dataset that maps comments and individual preferences. Since such data does not exist to our knowledge, we start by creating 5000 agents, or simulated individuals, who are characterized by their liked and disliked visual attributes. Each agent is randomly allocated an average of 50 liked and disliked attributes from the attributes list mentioned above. To ensure diversity, we generate them such that there is a minimum Jaccard distance of 85% between any two agents’ liked and disliked attributes.

**ZH** 要把自由形式评论转换为视觉偏好，我们需要一个把评论与个体偏好对应起来的数据集。据我们所知此类数据并不存在，因此我们首先创建 5000 个智能体（即模拟个体），每个智能体由其所喜欢与不喜欢的视觉属性刻画。我们从上述属性列表中为每个智能体随机分配平均 50 个喜欢与 50 个不喜欢的属性。为保证多样性，我们生成这些智能体时使任意两个智能体在喜欢与不喜欢的属性之间的 Jaccard 距离至少为 85%。

**EN** Next, we generate comments that each agent would write for various images based on their visual preferences. To keep the comments relevant to visual preferences and informative, we first generate an average of 10 images for each agent, concatenating a random subset of visual attributes they like or dislike in the input prompts. Although the images are still somewhat random since the input prompts are chosen randomly, this set is directly related to each agent’s visual preferences.

**ZH** 接着，我们生成每个智能体会基于自身视觉偏好为各种图像写下的评论。为使评论贴合视觉偏好并具有信息量，我们首先为每个智能体平均生成 10 张图像，在输入提示词中拼接其喜欢或不喜欢的视觉属性的随机子集。尽管由于输入提示词是随机选取的，这些图像仍带有一定的随机性，但该集合与每个智能体的视觉偏好直接相关。

**EN** To generate the agents’ comments on these images, we instruct GPT-4 [24] to create each agent’s comments based on their visual preferences. Typos and sarcasm are randomly allowed to add diversity and make the results more human-like. This process results in a paired dataset of visual attributes and comments for each agent.

**ZH** 为生成智能体对这些图像的评论，我们指示 GPT-4 [24] 依据每个智能体的视觉偏好创作其评论。我们随机允许出现拼写错误与讽刺，以增加多样性并使结果更接近人类。这一过程为每个智能体产生了一份视觉属性与评论配对的数据集。

**EN** To extract an individual’s visual preference from their comments, we fine-tune IDEFICS2-8b [15, 17], an open-sourced vision-language model, on the agents’ paired dataset. We found this model to work best compared to other open-source vision-language models. We demonstrate the shortcomings of our initial experiments with other models in section A.4. We denote the fine-tuned IDEFICS model as the Visual Preference Extractor, or ⟦SLOT_3⟧. Note that the ⟦SLOT_4⟧’s output is not limited to the pre-defined attributes; it can extract attributes mentioned in comments, e.g., recognizing a color mentioned in the comments but not defined in our attribute set.

**ZH** 为从评论中提取个体的视觉偏好，我们在智能体的配对数据集上微调了开源视觉-语言模型 IDEFICS2-8b [15, 17]。我们发现该模型相比其他开源视觉-语言模型效果最好；我们在 A.4 节中展示用其他模型做初期实验时的不足。我们把微调后的 IDEFICS 模型记为视觉偏好提取器，即 ⟦SLOT_3⟧。注意，⟦SLOT_4⟧ 的输出不限于预定义属性，它能提取评论中提及的属性，例如识别出评论中提到但未定义在我们属性集中的某种颜色。

**EN** Instead of converting comments to visual preferences, one might consider directly asking individuals to choose from visual attributes. However, we believe that this process can be tedious due to the large number of attributes (about 500) and certain attributes may be challenging to visualize out-of-context.

**ZH** 有人可能考虑不让用户写评论，而是直接要求他们从视觉属性中选择。但我们认为，由于属性数量庞大（约 500 个），这一过程会很繁琐，而且某些属性脱离语境后难以想象。

**EN** 3.2 Personalizing a generative model based on an individual’s preference

**ZH** 3.2 基于个体偏好个性化生成模型

**EN** In the previous section, we described how we can capture an individual’s visual preference from their comments. Here, we are interested in how we can use these visual preferences to adapt a generative model. In this work, we employ Stable Diffusion [28, 26]. As described previously, each individual’s preferences are described by a set of preferred and disliked attributes, denoted as ⟦SLOT_5⟧ and ⟦SLOT_6⟧ respectively. Encoding these preferences using Stable Diffusion’s text encoder, ⟦SLOT_7⟧, gives us ⟦SLOT_8⟧ and ⟦SLOT_9⟧. We encode the input prompt, ⟦SLOT_10⟧, and modify the resulting embedding, ⟦SLOT_11⟧, with ⟦SLOT_12⟧ and ⟦SLOT_13⟧ to steer the generations towards the individual’s preferences as follows:

**ZH** 上一节描述了如何从评论中捕捉个体的视觉偏好。这里我们关注如何用这些视觉偏好调整生成模型。本工作采用 Stable Diffusion [28, 26]。如前所述，每个个体的偏好由一组喜欢与不喜欢的属性描述，分别记为 ⟦SLOT_5⟧ 与 ⟦SLOT_6⟧。用 Stable Diffusion 的文本编码器 ⟦SLOT_7⟧ 对这些偏好进行编码，得到 ⟦SLOT_8⟧ 与 ⟦SLOT_9⟧。我们对输入提示词 ⟦SLOT_10⟧ 进行编码，得到嵌入 ⟦SLOT_11⟧，再用 ⟦SLOT_12⟧ 与 ⟦SLOT_13⟧ 对其进行修改，从而把生成结果导向个体偏好，如下所示：

<!-- [原子块 · table] 𝐩 = E ⁡ ( p ) + β ⁡ ( E ⁡ ( V ​ P + ) − E ⁡ ( V ​ P − ) ) . \displaystyle\mathbf{p}=E(p)+\beta(E(VP_{+})-E(VP_{-})). (1) -->

**EN** ⟦SLOT_14⟧ can be tuned by the individual to increase or decrease the ‘level’ of personalization according to their preferences. See fig. 5 for examples. We found in our experiments that ⟦SLOT_15⟧ ensures that the generations will be faithful to both the input prompt and visual preferences. To guide the process toward the individual’s preferences along with the prompt even further, we also modify the predicted noise by using classifier-free guidance [11, 21]. (see eq. 3). For a given timestep ⟦SLOT_16⟧,

**ZH** ⟦SLOT_14⟧ 可由个体按自身偏好调节，以增减个性化的“程度”，示例见图 5。我们在实验中发现，⟦SLOT_15⟧ 能保证生成结果同时忠实于输入提示词与视觉偏好。为进一步把这一过程同时导向个体偏好与提示词，我们还利用无分类器引导 [11, 21] 修改预测噪声（见式 3）。对于给定时间步 ⟦SLOT_16⟧，

<!-- [原子块 · table] ϵ v ​ p ​ ( 𝐱 t , t ) \displaystyle\mathbf{\epsilon}_{vp}(\mathbf{x}_{t},t) = ϵ θ ​ ( 𝐱 t , t , E ⁡ ( V ​ P + ) ) − ϵ θ ​ ( 𝐱 t , t , E ⁡ ( V ​ P − ) ) \displaystyle=\mathbf{\epsilon}_{\theta}(\mathbf -->

**EN** where ⟦SLOT_17⟧ is Stable Diffusion’s denoising U-Net and ⟦SLOT_18⟧ is the guidance scale. The changes to the denoising process are shown in algorithm 1.

**ZH** 其中 ⟦SLOT_17⟧ 为 Stable Diffusion 的去噪 U-Net，⟦SLOT_18⟧ 为引导尺度。去噪过程的变化见算法 1。

**EN** Algorithm 1 Personalized image generation with ViPer

**ZH** 算法 1 用 ViPer 生成个性化图像

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

**EN** 3.3 Proxy for evaluating personalized generations

**ZH** 3.3 评价个性化生成的代理指标

**EN** We proposed a method to generate personalized images. To evaluate them, human evaluations are the gold standard, however, they are expensive and not scalable. In this section, we aim to introduce a proxy measure for evaluating these generations, thereby encouraging further research in this domain.

**ZH** 我们提出了一种生成个性化图像的方法。评价这些结果时，人工评价是黄金标准，但成本高且难以扩展。本节旨在引入一个评价这些生成结果的代理度量，以促进该领域的进一步研究。

**EN** This proxy measure would indicate how much an individual would like a given image. To obtain this proxy measure, we combine two sources of training data: one from our agents and another from the Pick-a-Pic dataset [14]. The latter contains the binary preferences of human users on a set of generated images. For the former, we employ two approaches to generate training data. Using the agents’ visual preferences, we produce a small set of personalized images for each agent with ViPer. Additionally, we generate personalized prompts with a language model and create images from them using standard Stable Diffusion XL (see section 4.2 and section C.3 for details). This is to ensure that the proxy measure will not be biased toward the generations from ViPer. Thus, for a given entity (agent or human), we either have a set of their personalized images or a set of several generated images that they like. We denote each image from this set for entity ⟦SLOT_19⟧ as ⟦SLOT_20⟧. An image that is disliked or not personalized is denoted as ⟦SLOT_21⟧. We denote the set of these image pairs as ⟦SLOT_22⟧. We use 5000 sets of image pairs to fine-tune IDEFICS2-8b, denoted by ⟦SLOT_23⟧, to output the probability of an individual liking a given image ⟦SLOT_24⟧, given a set of their liked and disliked images, ⟦SLOT_25⟧, as ⟦SLOT_26⟧. We use the cross-entropy loss for training, ⟦SLOT_27⟧ where ⟦SLOT_28⟧ is the prediction and ⟦SLOT_29⟧ is the label i.e., ⟦SLOT_30⟧. See fig. 3 for the schematics of a fine-tuning step.

**ZH** 该代理度量反映某个体会喜欢给定图像的程度。为获得这一代理度量，我们结合两处训练数据：一处来自我们的智能体，另一处来自 Pick-a-Pic 数据集 [14]。后者包含人类用户对一组生成图像的二元偏好。对于前者，我们采用两种方法生成训练数据：利用智能体的视觉偏好，用 ViPer 为每个智能体生成一小批个性化图像；此外，我们用一个语言模型生成个性化提示词，并用标准 Stable Diffusion XL 据此生成图像（详见 4.2 节与 C.3 节）。这是为了保证该代理度量不会偏向 ViPer 的生成结果。于是，对于给定实体（智能体或人类），我们或者拥有一组其个性化图像，或者拥有一组其喜欢的若干生成图像。我们把该集合中属于实体 ⟦SLOT_19⟧ 的每张图像记为 ⟦SLOT_20⟧；被不喜欢或未经个性化的图像记为 ⟦SLOT_21⟧；把这些图像对的集合记为 ⟦SLOT_22⟧。我们用 5000 组图像对微调 IDEFICS2-8b（记为 ⟦SLOT_23⟧），使其输出个体喜欢给定图像 ⟦SLOT_24⟧ 的概率（条件给定该个体一组喜欢与不喜欢的图像 ⟦SLOT_25⟧），记为 ⟦SLOT_26⟧。训练采用交叉熵损失 ⟦SLOT_27⟧，其中 ⟦SLOT_28⟧ 为预测值，⟦SLOT_29⟧ 为标签，即 ⟦SLOT_30⟧。微调步骤的示意图见图 3。

<!-- [原子块 · img]  -->

**EN** Figure 3: Learning a proxy measure for evaluating personalized generations. We fine-tune IDEFICS2-8b, denoted by ⟦SLOT_31⟧, using both the personalized/liked and non-personalized/disliked set of images, ⟦SLOT_32⟧, of an agent. ⟦SLOT_33⟧ is given the set of images ⟦SLOT_34⟧ from an individual for context and asked to predict if the user will like a given query image. We trained the model with cross-entropy loss.

**ZH** 图 3：学习用于评价个性化生成的代理度量。我们微调 IDEFICS2-8b（记为 ⟦SLOT_31⟧），所用数据为智能体的一组个性化/被喜欢图像与非个性化/被不喜欢图像 ⟦SLOT_32⟧。⟦SLOT_33⟧ 被给定某个体的一组图像 ⟦SLOT_34⟧ 作为上下文，并被要求预测用户是否会喜欢给定的查询图像。我们用交叉熵损失训练该模型。

**EN** 4 Evaluation and Ablations

**ZH** 4 评价与消融实验

**EN** We demonstrate that ViPer is capable of generating images that align with an individual’s preferences (see section 4.1), and when compared to current baselines, it achieves higher levels of user satisfaction (see section 4.2).

**ZH** 我们证明 ViPer 能够生成与个体偏好相对齐的图像（见 4.1 节），并且与现有基线相比能获得更高的用户满意度（见 4.2 节）。

**EN** 4.1 Evaluating the personalized generations

**ZH** 4.1 评价个性化生成结果

**EN** Comparing generation across users. In fig. 4, we display personalized outcomes from seven prompts for four users using ViPer. These results highlight each user’s distinct art preferences, underlining that visual taste is more than just liking a single art style or a color palette; rather it’s shaped by various visual attributes based on individual preferences.

**ZH** 跨用户比较生成结果。图 4 展示了用 ViPer 为四位用户在七个提示词上生成的个性化结果。这些结果凸显了每位用户各异的艺术偏好，说明视觉品味不只是喜欢某一种艺术风格或某一套色调，而是由基于个体偏好的多种视觉属性共同塑造。

**EN** User studies. We assess our approach using user tests. We invited twenty users to our study, conducting two types of tests. Each participant was first asked to comment on 8 to 20 images (flexible and dependent on the user’s choice). Each user was then shown eight images generated from the same prompt, where only one of the eight was personalized for them using ViPer. This was then repeated for 15 prompts.

**ZH** 用户研究。我们通过用户测试评估本文方法，邀请了二十位用户参与研究，进行两类测试。每位参与者首先要对 8 到 20 张图像发表评论（数量灵活，取决于用户自己的选择）。随后向每位用户展示由同一提示词生成的八张图像，其中只有一张是用 ViPer 为其个性化生成的；这一过程对 15 个提示词重复进行。

**EN** In the first test, the other seven images were created using standard Stable Diffusion XL, without personalization (User’s Pers. vs. No Pers in table 1). Our top-one accuracy here is 86.1%, meaning the user’s most preferred images were overwhelmingly generated from their visual preference, surpassing random chance by 6.89 times.

**ZH** 在第一类测试中，其余七张图像用标准 Stable Diffusion XL 生成，不做个性化（表 1 中的 User’s Pers. vs. No Pers）。我们的 top-1 准确率为 86.1%，意味着用户最偏好的图像绝大多数来自其视觉偏好，比随机猜测高出 6.89 倍。

**EN** In the second test, they were generated based on the visual preferences of other users (User’s vs. Other Users’ Pers in table 1). The aim of this test is to showcase how ViPer goes beyond just enhancing general aesthetics and instead focuses on personalization. Our top-one accuracy here is 65.4%, which exceeds random selection by 5.23 times.

**ZH** 在第二类测试中，这些图像基于其他用户的视觉偏好生成（表 1 中的 User’s vs. Other Users’ Pers）。该测试旨在展示 ViPer 不止于提升通用美感，而是聚焦于个性化。我们的 top-1 准确率为 65.4%，比随机选择高出 5.23 倍。

**EN** The lower accuracy in the second test compared to the first one is because some users have similar preferences. Despite our efforts to address this for the sake of demonstration, users may still favor details in others’ results that weren’t explicitly mentioned in their own comments. We discuss this further in section 5. Our proxy metric’s results closely correlate with actual user tests, demonstrating its alignment with user preferences. Additional ablation studies can be found in the appendix C.

**ZH** 第二类测试的准确率低于第一类，是因为部分用户的偏好相近。尽管我们出于演示目的努力缓解这一点，用户仍可能喜欢他人结果中未在自己评论里明确提及的细节。我们在第 5 节进一步讨论。我们的代理指标结果与真实用户测试高度相关，说明它与用户偏好一致。更多消融实验见附录 C。

<!-- [原子块 · img]  -->

**EN** Figure 4: Comparing the personalized generations between users. Each row shows images generated from the same prompt shown on the left. The first column displays generations without any personalization, while the next four columns show personalized generations for users with distinct preferences. Note that the generations are consistent with the input prompts, and each user’s preferences are reflected across prompts. Moreover, while the color palette is a dominating visual attribute and can be noticed at first glance, other visual attributes such as brush strokes, lines, vibe, etc., also have intricate effects (see last row where colors are specified through input prompt). Users’ visual preferences are included in table 6.

**ZH** 图 4：跨用户比较个性化生成结果。每一行显示由左侧所示同一提示词生成的图像。第一列为不做任何个性化的生成结果，其后四列为具有不同偏好的用户的个性化生成结果。注意生成结果与输入提示词保持一致，且每位用户的偏好在不同提示词间都有体现。此外，虽然色调是最直观、第一眼就能注意到的视觉属性，笔触、线条、氛围等其他视觉属性也产生着微妙影响（见最后一行，其颜色由输入提示词指定）。用户的视觉偏好见表 6。

**EN** Table 1: User study results. In the User’s Pers. vs. No Pers test, for a given prompt, each user is shown 8 images, one of which is personalized for them and the others are without any personalization. In the User’s vs. Other Users’ Pers test, each user is shown an image personalized for them and those personalized for 7 other users. In both tests, the users had to rank the images based on how much they appealed to them. This is done for 12-15 prompts per user. The last column shows the accuracy from random guessing. We report the top-1 to 4 accuracy (%), in columns 1 and 3 in the table below. We also show the accuracy from using our proposed proxy metric (see section 3.3). The accuracy from the user and the proxy metric are similar, indicating that the metric can be a proxy for user preferences.

**ZH** 表 1：用户研究结果。在 User’s Pers. vs. No Pers 测试中，对给定提示词，每位用户看到 8 张图像，其中一张为其个性化生成，其余未经任何个性化。在 User’s vs. Other Users’ Pers 测试中，每位用户看到一张为自己个性化的图像，以及为其他 7 位用户个性化的图像。两项测试中，用户都需按图像的吸引力排序；每位用户进行 12～15 个提示词。最后一列给出随机猜测的准确率。我们报告 top-1 至 top-4 准确率（%），见下表第 1 列与第 3 列。我们还给出使用本文代理指标（见 3.3 节）得到的准确率。用户与代理指标的准确率相近，说明该指标可作为用户偏好的代理。

**EN** Accuracy User’s Pers. vs. No Pers User’s vs. Other Users’ Pers Users Proxy metric Users Proxy metric Random Top-1 86.1 86.7 65.4 71.6 12.5 Top-2 93.2 95.8 82.2 89.2 25.0 Top-3 98.6 100.0 96.6 98.3 37.5 Top-4 99.0 100.0 99.0 99.2 50.0

**ZH** 准确率 User’s Pers. vs. No Pers User’s vs. Other Users’ Pers Users 代理指标 Users 代理指标 随机 Top-1 86.1 86.7 65.4 71.6 12.5 Top-2 93.2 95.8 82.2 89.2 25.0 Top-3 98.6 100.0 96.6 98.3 37.5 Top-4 99.0 100.0 99.0 99.2 50.0

**EN** Controlling the degree of personalization. Our approach offers flexibility by letting users adjust the personalization level with a simple slider. fig. 5 depicts how personalization increases for one user gradually. As ⟦SLOT_35⟧ increases from 0 to 1, results become more tailored to user preferences, departing from generic outcomes while keeping the original prompt’s intent.

**ZH** 控制个性化程度。我们的方法提供了灵活性：用户可用一个简单的滑杆调节个性化程度。图 5 描绘了某位用户的个性化程度如何逐步提高。当 ⟦SLOT_35⟧ 从 0 增至 1，结果越来越贴合用户偏好，逐渐脱离通用输出，同时保持原始提示词的意图。

<!-- [原子块 · img]  -->

**EN** Figure 5: Controlling the degree of personalization. Each row displays images generated from the same prompt. The left column is generated without any personalization, i.e., ⟦SLOT_36⟧ in the guidance equation in eq. 3, while the next five columns increase this number by 0.2 consecutively. This user’s preference for soft, simple, dreamy vibes, and pastel colors increases in intensity as ⟦SLOT_37⟧ increases.

**ZH** 图 5：控制个性化程度。每一行显示由同一提示词生成的图像。最左列不做任何个性化，即式 3 引导方程中的 ⟦SLOT_36⟧；其后五列将该数值依次递增 0.2。该用户对柔和、简约、梦幻氛围与柔和色彩的偏好强度随 ⟦SLOT_37⟧ 增大而增强。

**EN** Consistency with input prompts. In our sample runs, results follow the input prompts’ meaning. This is because the influence of visual preference embeddings on the final images can be limited by ⟦SLOT_38⟧, ensuring they never outweigh the input prompt embeddings. In fig. 4’s last row, we display the results of a prompt following specified art features. Despite maintaining personalization, our results adhere to the prompt’s characteristics. Additional examples and experiments are provided in section C.4.

**ZH** 与输入提示词的一致性。在我们的示例运行中，结果遵循输入提示词的含义。这是因为视觉偏好嵌入对最终图像的影响可被 ⟦SLOT_38⟧ 限制，确保其永远不会压过输入提示词嵌入。在图 4 的最后一行，我们展示了一个遵循指定艺术特征的提示词的结果：尽管保留了个性化，我们的结果仍遵循提示词的特征。更多示例与实验见 C.4 节。

**EN** Evaluation through identifiability tests. We conduct two experiments to make sure that there is a significant connection between the agents’ preferences and their comments so that ⟦SLOT_39⟧ is able to extract preferences correctly from user comments.

**ZH** 通过可辨识性检验进行评价。我们进行了两项实验，以确保智能体的偏好与其评论之间存在显著关联，从而使 ⟦SLOT_39⟧ 能正确地从用户评论中提取偏好。

**EN** In the first experiment, which we denote as "Author test" in table 3, we aim to identify the author of a comment given the visual preferences of five agents. We conduct this using 100 random agents, each appearing at least twice as the author. GPT-4 ranks agents by likelihood of being the author and we measure accuracy by whether the true author is among the top ⟦SLOT_40⟧ predictions.

**ZH** 在第一项实验中（我们在表 3 中称之为“作者检验”），我们的目标是在给定五个智能体视觉偏好的情况下识别某条评论的作者。我们用 100 个随机智能体进行该实验，每个智能体至少两次作为作者出现。GPT-4 按成为作者的可能性对智能体排序，我们通过真实作者是否位于前 ⟦SLOT_40⟧ 个预测之列来衡量准确率。

**EN** The second experiment, which we call "VP vs. VP" in table 3, aims to assess how well an agent’s set of comments maintains their original visual preference. To do this, we first use GPT-4 to reconstruct the visual preferences of 50 random agents from all of their comments. Then for each agent, we consider the agent’s reconstructed visual preference (which was generated from the comments), the agent’s original visual preference (which the comments were generated from), and four random agents’ original visual preferences. We instruct GPT-4 to rank the reconstructed visual preference with the original visual preferences based on the likelihood of both belonging to the same agent.

**ZH** 第二项实验（我们在表 3 中称之为“VP vs. VP”）旨在评估一个智能体的评论集合能在多大程度上保持其原始视觉偏好。为此，我们首先用 GPT-4 从 50 个随机智能体的全部评论中重建它们的视觉偏好。然后，对每个智能体，我们考虑：由评论生成的该智能体的重建视觉偏好、评论据以生成的该智能体的原始视觉偏好，以及四个随机智能体的原始视觉偏好。我们指示 GPT-4 按两者同属一个智能体的可能性，把重建的视觉偏好与这些原始视觉偏好一起排序。

**EN** In both experiments, the top-one accuracy exceeds random selection significantly. The accuracy of the second test, VP vs. VP, is overall higher than the first test. This is because the reconstructed visual preferences contain more information than one comment, making the second test easier in general. These results are proof of alignment between our simulated agents’ preferences and their comments, making ⟦SLOT_41⟧’s training data reliable as a source to extract visual preference from comments.

**ZH** 两项实验中，top-1 准确率都显著超过随机选择。第二项测试 VP vs. VP 的准确率总体高于第一项，因为重建的视觉偏好比单条评论包含更多信息，使第二项测试总体上更容易。这些结果证明了我们模拟智能体的偏好与其评论之间的一致性，从而使 ⟦SLOT_41⟧ 的训练数据作为从评论中提取视觉偏好的来源是可信的。

**EN** Table 2: In the Author test, GPT-4 is instructed to identify the author of a comment among five given agents’ visual preferences by ranking them based on the likelihood of being the author. For the VP vs. VP test, we first reconstruct the visual preferences of agents from their comments with GPT-4, and then we instruct it to identify an agent given their reconstructed visual preference and five ground truth visual preferences, with only one belonging to the user. We perform variations of this test using both positive and negative visual preferences, denoted by ⟦SLOT_42⟧, and each separately, denoted by ⟦SLOT_43⟧ and ⟦SLOT_44⟧. The goal of these tests is to ensure alignment between comments and visual preferences so that we’re sure ⟦SLOT_45⟧ which is tuned on this data, can accurately extract visual preferences from comments. Note that the top-k results (%) exceed the random chance of agents being chosen by the language model, demonstrating the link between agents’ comments and their visual preferences. Additionally, it’s worth noting that in the second test, GPT-4 performs more accurately when given either the entire visual preference or its positive aspect.

**ZH** 表 2：在“作者检验”中，我们指示 GPT-4 在给定五个智能体的视觉偏好时，按成为作者的可能性排序以识别某条评论的作者。在“VP vs. VP”测试中，我们首先用 GPT-4 从评论中重建各智能体的视觉偏好，然后指示它根据重建的视觉偏好与五个真实视觉偏好（其中只有一个属于该用户）识别对应智能体。我们用整体视觉偏好（记作 ⟦SLOT_42⟧）以及分别用其正面与负面部分（记作 ⟦SLOT_43⟧ 与 ⟦SLOT_44⟧）进行了该测试的变体。这些测试的目标是确保评论与视觉偏好之间的一致性，从而确信在该数据上调优的 ⟦SLOT_45⟧ 能准确地从评论中提取视觉偏好。注意，top-k 结果（%）超过了语言模型随机选中智能体的概率，说明智能体的评论与其视觉偏好之间存在关联。此外值得注意的是，在第二项测试中，GPT-4 在获得完整视觉偏好或其正面部分时表现更准确。

<!-- [原子块 · table] Accuracy Author test VP vs. VP test Random V ​ P VP V ​ P + VP_{+} V ​ P − VP_{-} Top-1 83.4 89.9 92.4 45.8 20.0 Top-2 89.1 98.1 96.2 72.1 40.0 Top-3 91.2 100.0 96.4 88.3 60.0 -->

**EN** 4.2 Comparison with baselines

**ZH** 4.2 与基线比较

**EN** In this subsection, we compare our approach to existing baselines. We’ll discuss the strengths and weaknesses of these methods and explain the advantages of our approach over them. We evaluate the following baselines and use Stable Diffusion 2 for the experiments:

**ZH** 本节我们把本文方法与现有基线进行比较，讨论这些方法的优缺点，并说明本文方法相对它们的优势。我们评价以下基线，并在实验中使用 Stable Diffusion 2：

**EN** No personalization: These generations are produced with the input prompts using standard Stable Diffusion.

**ZH** 无个性化：这些生成结果由标准 Stable Diffusion 用输入提示词产生。

**EN** ZO-RankSGD [35]: Users are required to rank several images in multiple iterations for each prompt. This algorithm converges to a stationary point based on the feedback received. This approach helps us compare our approach to ranking.

**ZH** ZO-RankSGD [35]：用户需要对多个提示词各自在若干轮迭代中对若干图像排序；该算法基于收到的反馈收敛到一个驻点。该方法帮助我们把本文方法与排序类方法进行比较。

**EN** FABRIC [36]: For each prompt, users are asked to like/dislike the generated images in multiple steps. The diffusion process is conditioned on this set of liked and disliked feedback images. This method helps us understand which one—binary reactions or comments—is more effective in grasping user preferences.

**ZH** FABRIC [36]：对每个提示词，用户在多个步骤中被要求对生成的图像表示喜欢/不喜欢；扩散过程以这组喜欢与不喜欢的反馈图像为条件。该方法帮助我们理解二元反应与评论哪一种更能把握用户偏好。

**EN** Textual Inversion [7]: Users provide two sets of liked and disliked images. Textual Inversion generates special tokens for each. Tokens are incorporated into positive and negative prompts. This approach helps determine whether asking a user to provide their preferred and disliked images, or comment on images is better at capturing user preferences.

**ZH** Textual Inversion [7]：用户提供喜欢与不喜欢的两组图像，Textual Inversion 为每组生成特殊词元，并把词元融入正向与负向提示词。该方法帮助我们判断：让用户提供其喜欢与不喜欢的图像，还是让用户对图像发表评论，更能捕捉用户偏好。

**EN** Fine-tuning Stable Diffusion [7]: We fine-tune Stable Diffusion with one user’s ⟦SLOT_46⟧, using the CLIP similarity score to align Stable Diffusion-generated outputs for each user with their ⟦SLOT_47⟧ to serve as a reward model [40, 4]. The key distinction from ViPer is in the incorporation of visual preferences into Stable Diffusion. This approach demonstrates the effectiveness of using ⟦SLOT_48⟧ embeddings as shown in eq. 1 and eq. 3.

**ZH** 微调 Stable Diffusion [7]：我们用某位用户的 ⟦SLOT_46⟧ 微调 Stable Diffusion，使用 CLIP 相似度分数把 Stable Diffusion 为每个用户生成的输出与其 ⟦SLOT_47⟧ 相对齐，以此作为奖励模型 [40, 4]。与 ViPer 的关键区别在于视觉偏好融入 Stable Diffusion 的方式。该方法证明了使用 ⟦SLOT_48⟧ 嵌入（如式 1 与式 3 所示）的有效性。

**EN** Prompt Personalization: We instruct a language model to directly personalize prompts, based on the user’s visual preferences extracted from their comments by ⟦SLOT_49⟧. The modified prompt is given to standard Stable Diffusion to generate personalized images. The main difference with ViPer lies in how visual preferences are incorporated into Stable Diffusion. Thus, this method demonstrates the efficacy of using ⟦SLOT_50⟧ embeddings in eq. 1 and eq. 3.

**ZH** 提示词个性化：我们指示一个语言模型基于 ⟦SLOT_49⟧ 从用户评论中提取的视觉偏好，直接对提示词进行个性化；修改后的提示词交给标准 Stable Diffusion 生成个性化图像。与 ViPer 的主要区别在于视觉偏好融入 Stable Diffusion 的方式，因此该方法证明了在式 1 与式 3 中使用 ⟦SLOT_50⟧ 嵌入的有效性。

<!-- [原子块 · img]  -->

**EN** Figure 6: Left: Comparing the generations from ViPer versus the baselines for a single user. Each row displays images generated from the same prompt (except Prompt Personalization which manipulates the input prompt). The leftmost column is generated without any personalization, while the next five columns shows the generations from different methods. Note how ZO-RankSGD’s generations are similar to the generations without any personalization. FABRIC tends to generate images that are more realistic or saturated, which is not aligned with this user’s preferences. Textual Inversion’s learned patterns does not align with the user’s taste. Fine-tuning Stable Diffusion results in low-quality generations but there is some degree of personalization. Prompt Personalization generates images that are close to the user’s preferences, however, they are not always consistent with the input prompt (e.g., the first image in the fifth column). Finally, ViPer generates images that are both aligned with the user’s preferences and follow the input prompts. The user consistently preferred ViPer’s results. Our proxy metric’s average score for each method is presented at the bottom of each column. Right: User’s preference info. A user’s visual preference is extracted from their comments. Some of the user’s liked images and disliked images that were used for our metric’s context and Textual Inversion’s input images are shown below. Note how there is an alignment between the user’s visual preference, set of liked and disliked images, and ViPer’s results. The alignment is significantly less obvious in FABRIC and ZO-RankSGD.

**ZH** 图 6：左：对单个用户，比较 ViPer 与各基线的生成结果。每一行显示由同一提示词生成的图像（提示词个性化除外，它会改动输入提示词）。最左列为不做任何个性化的生成结果，其后五列展示不同方法的结果。注意 ZO-RankSGD 的生成结果与无个性化的结果相近；FABRIC 倾向于生成更写实或更饱和的图像，与该用户的偏好不一致；Textual Inversion 学到的模式不符合用户品味；微调 Stable Diffusion 的生成结果质量较低，但有一定程度的个性化；提示词个性化生成的图像接近用户偏好，却并不总与输入提示词一致（如第五列第一张图像）。最后，ViPer 生成的图像既与用户偏好相对齐，又遵循输入提示词。该用户始终更偏好 ViPer 的结果。我们在每列底部给出本文代理指标对各方法的平均分。右：用户偏好信息。从用户评论中提取的视觉偏好。下方展示该用户的部分喜欢图像与不喜欢图像，它们被用作我们指标的上下文以及 Textual Inversion 的输入图像。注意用户的视觉偏好、喜欢与不喜欢的图像集合以及 ViPer 的结果之间存在一致性；而这种一致性在 FABRIC 与 ZO-RankSGD 中显著更弱。

**EN** fig. 6 depicts a comparison of personalized generations with these baselines versus ViPer, for a single user. Textual Inversion struggles when the user’s selected images are too diverse. Furthermore, users are not able to provide feedback on their reasons for liking/disliking the input images. This can be seen in column 4 in fig. 6, where the results contain textures and certain color palettes that are too extreme for the user’s taste. It is also challenging for users to provide a set of images that completely represents their preferences.

**ZH** 图 6 描绘了单个用户下，这些基线的个性化生成结果与 ViPer 的比较。当用户所选图像过于多样时，Textual Inversion 表现不佳；此外，用户无法就喜欢或不喜欢输入图像的原因提供反馈。这可以在图 6 第 4 列中看到：结果包含的纹理与某些色调对用户品味而言过于极端。用户也很难提供一组能完整代表其偏好的图像。

**EN** Prompt Personalization, which is dependent on a language model, may lead to lengthy prompts, parts of visual preferences being disregarded, and can adopt a conversational tone, despite explicit instructions. Additionally, the personalized prompts may also fail to include key concepts from the original prompts (examples in section C.4). The resulting generations can be seen in the fifth column of fig. 6. The results are aligned with the user’s visual preference but overlook the user’s favored attributes like "Retro", "Creepy", and "Horror" due to language models’ inclination towards generating lengthy outputs. Iterative prompt refinement helps, but the computational overhead of using a language model remains a challenge. We provide further examples of these shortcomings in section C.4.

**ZH** 依赖语言模型的提示词个性化可能导致提示词冗长、部分视觉偏好被忽略，并且即便有明确指示也可能采用对话式口吻。此外，个性化后的提示词可能未能包含原始提示词中的关键概念（示例见 C.4 节）。相应生成结果见图 6 第五列：结果与用户的视觉偏好相对齐，却因语言模型倾向于生成冗长输出而忽略了用户偏好的“复古”“惊悚”“恐怖”等属性。迭代式提示词改进有所帮助，但使用语言模型的计算开销仍是难题。我们在 C.4 节给出这些不足的更多示例。

**EN** Fine-tuning Stable Diffusion results in personalized but low-quality outputs. Additionally, it is an expensive and time-consuming method because each user needs to fine-tune Stable Diffusion with their ⟦SLOT_51⟧.

**ZH** 微调 Stable Diffusion 能得到个性化但低质量的输出；此外，由于每个用户都需要用其 ⟦SLOT_51⟧ 微调 Stable Diffusion，该方法昂贵且耗时。

**EN** In our experiments, FABRIC consistently converged towards a more realistic and vibrant style of images. This can be seen in the third column in fig. 6, despite the user’s dislike for "Realism" and "Vibrant Colors". ZO-RankSGD does not deviate much from the unpersonalized results.

**ZH** 在我们的实验中，FABRIC 一致地收敛到更写实、更鲜艳的图像风格，这可见于图 6 第三列，尽管用户并不喜欢“写实主义”与“鲜艳色彩”。ZO-RankSGD 与未个性化结果相差不大。

**EN** Lastly, we use our proxy metric to calculate a personalization score for each of the methods in fig. 6. ViPer has the highest score, followed by Prompt Personalization and Fine-tuning Stable Diffusion. This aligns well with how the users ranked the images based on their preferences (we present the user’s ranking in fig. 21).

**ZH** 最后，我们用代理指标计算图 6 中各方法的个性化分数。ViPer 得分最高，其次是提示词个性化与微调 Stable Diffusion。这与用户按自身偏好对图像排序的结果高度吻合（我们在图 21 中给出用户的排序）。

**EN** 5 Conclusion and Limitations

**ZH** 5 结论与局限性

**EN** We introduced ViPer, a method for personalizing generative models. It extracts and incorporate individuals’ generic preferences into Stable Diffusion. Moreover, we introduced a metric to automatically assess personalization, reducing the need for costly human evaluations of generated images. Our approach is flexible and scalable and can consider a wide range of preferences. We briefly discuss the limitations and potential future work:

**ZH** 我们提出 ViPer，一种个性化生成模型的方法。它提取个体的通用偏好并把其融入 Stable Diffusion。此外，我们提出了一个自动评估个性化程度的指标，减少了对生成图像进行昂贵人工评价的需求。本文方法灵活、可扩展，能考虑范围广泛的偏好。下面简要讨论局限性与可能的未来工作：

**EN** Exploring other ways of extracting user’s preferences. Our method makes use of user’s comments on a given set of images. As discussed in section 3.1, this is more expressive than e.g., ranking images, however, articulating these preferences can still be difficult for some users. An ideal approach could involve accessing human brain signals directly or scalable proxies of it. Another useful angle is engineering the set of commentary images to maximally reveal the users’ preferences with least interactions.

**ZH** 探索提取用户偏好的其他方式。本文方法利用用户对给定图像集合的评论。如 3.1 节所述，这比图像排序等方式更具表达力，但对部分用户而言，清晰表述这些偏好仍有困难。理想的方式可能是直接获取人脑信号或其可扩展的代理。另一个有用的角度是设计评论图像集合，使其以最少的交互次数最大程度地揭示用户偏好。

**EN** Set of visual attributes. We pre-defined a set of structred visual attributes, but despite our best efforts, it may not cover everything. To address this limitation, we explored using more powerful language models like GPT-4, eliminating the need for pre-defined attributes and allowing more flexibility in the interpretation of comments. However, these models are not open-sourced, and using them at a large scale can be expensive.

**ZH** 视觉属性集合。我们预定义了一组结构化视觉属性，但尽管已尽力，它可能仍未覆盖全部。为缓解这一局限，我们探索使用 GPT-4 等更强的语言模型，从而无需预定义属性，并在解读评论时更具灵活性。然而，这些模型并未开源，大规模使用成本高昂。

**EN** Stable Diffusion limitations. Our current implementation relies on Stable Diffusion’s text encoder, which has limitations such as a 77-token restriction and sensitivity to word order, sometimes leading to some preferred attributes being overlooked. Randomization techniques can partially address this issue, but using an encoder without these limitations would be beneficial. Furthermore, if Stable Diffusion cannot grasp a visual attribute due to its training data distribution, it cannot include it in its results.

**ZH** Stable Diffusion 的局限。我们当前的实现依赖 Stable Diffusion 的文本编码器，它有 77 个词元的限制，且对词序敏感，有时会导致某些偏好属性被忽略。随机化技术可部分缓解该问题，但使用没有这些限制的编码器会更有益。此外，若 Stable Diffusion 因其训练数据分布而无法理解某个视觉属性，它就无法把该属性纳入结果。

**EN** Exploring other ways of adapting Stable Diffusion. We attempted to fine-tune the Stable Diffusion by optimizing our proposed proxy introduced in section 3.3. However, the generations suffered in quality. Exploring alternative reward tuning strategies is an interesting future direction.

**ZH** 探索调整 Stable Diffusion 的其他方式。我们尝试通过优化 3.3 节提出的代理指标来微调 Stable Diffusion，但生成结果的质量有所下降。探索其他奖励调优策略是一个有意思的未来方向。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] AI@Meta. Llama 3 model card. 2024. URL https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md . -->

<!-- [原子块 · verbatim] [2] Tim Brooks, Aleksander Holynski, and Alexei A. Efros. Instructpix2pix: Learning to follow image editing instructions, 2023. -->

<!-- [原子块 · verbatim] [3] Jiwoo Chung, Sangeek Hyun, and Jae-Pil Heo. Style injection in diffusion: A training-free approach for adapting large-scale diffusion models for style transfer, 2023. -->

<!-- [原子块 · verbatim] [4] Kevin Clark, Paul Vicol, Kevin Swersky, and David J Fleet. Directly fine-tuning diffusion models on differentiable rewards, 2023. -->

<!-- [原子块 · verbatim] [5] Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven Hoi. Instructblip: Towards general-purpose vision-language models with i -->

<!-- [原子块 · verbatim] [6] Prafulla Dhariwal and Alex Nichol. Diffusion models beat gans on image synthesis, 2021. -->

<!-- [原子块 · verbatim] [7] Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, and Daniel Cohen-Or. An image is worth one word: Personalizing text-to-image generation using textual inversion,  -->

<!-- [原子块 · verbatim] [8] Yaru Hao, Zewen Chi, Li Dong, and Furu Wei. Optimizing prompts for text-to-image generation, 2023. -->

<!-- [原子块 · verbatim] [9] Feihong He, Gang Li, Mengyuan Zhang, Leilei Yan, Lingyu Si, and Fanzhang Li. Freestyle: Free lunch for text-guided style transfer using diffusion models, 2024. -->

<!-- [原子块 · verbatim] [10] Ruifei He, Shuyang Sun, Xin Yu, Chuhui Xue, Wenqing Zhang, Philip Torr, Song Bai, and Xiaojuan Qi. Is synthetic data from generative models ready for image recognition? arXiv preprint arXiv:2210. -->

<!-- [原子块 · verbatim] [11] Jonathan Ho and Tim Salimans. Classifier-free diffusion guidance, 2022. -->

<!-- [原子块 · verbatim] [12] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models, 2020. -->

<!-- [原子块 · verbatim] [13] Bahjat Kawar, Shiran Zada, Oran Lang, Omer Tov, Huiwen Chang, Tali Dekel, Inbar Mosseri, and Michal Irani. Imagic: Text-based real image editing with diffusion models, 2023. -->

<!-- [原子块 · verbatim] [14] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation, 2023. -->

<!-- [原子块 · verbatim] [15] Hugo Laurençon, Lucile Saulnier, Léo Tronchon, Stas Bekman, Amanpreet Singh, Anton Lozhkov, Thomas Wang, Siddharth Karamcheti, Alexander M. Rush, Douwe Kiela, Matthieu Cord, and Victor Sanh. Obel -->

<!-- [原子块 · verbatim] [16] Hugo Laurençon, Lucile Saulnier, Léo Tronchon, Stas Bekman, Amanpreet Singh, Anton Lozhkov, Thomas Wang, Siddharth Karamcheti, Alexander M. Rush, Douwe Kiela, Matthieu Cord, and Victor Sanh. Obel -->

<!-- [原子块 · verbatim] [17] Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh. What matters when building vision-language models?, 2024. -->

<!-- [原子块 · verbatim] [18] Wei Li, Xue Xu, Xinyan Xiao, Jiachen Liu, Hu Yang, Guohao Li, Zhanpeng Wang, Zhifan Feng, Qiaoqiao She, Yajuan Lyu, and Hua Wu. Upainting: Unified text-to-image diffusion generation with cross-mo -->

<!-- [原子块 · verbatim] [19] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023a. -->

<!-- [原子块 · verbatim] [20] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023b. -->

<!-- [原子块 · verbatim] [21] Nan Liu, Shuang Li, Yilun Du, Antonio Torralba, and Joshua B. Tenenbaum. Compositional visual generation with composable diffusion models, 2023c. -->

<!-- [原子块 · verbatim] [22] Erpai Luo, Minsheng Hao, Lei Wei, and Xuegong Zhang. scdiffusion: conditional generation of high-quality single-cell data using diffusion model, 2024. -->

<!-- [原子块 · verbatim] [23] Ron Mokady, Amir Hertz, Kfir Aberman, Yael Pritch, and Daniel Cohen-Or. Null-text inversion for editing real images using guided diffusion models, 2022. -->

<!-- [原子块 · verbatim] [24] OpenAI, :, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin -->

<!-- [原子块 · verbatim] [25] Gaurav Parmar, Krishna Kumar Singh, Richard Zhang, Yijun Li, Jingwan Lu, and Jun-Yan Zhu. Zero-shot image-to-image translation, 2023. -->

<!-- [原子块 · verbatim] [26] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. Sdxl: Improving latent diffusion models for high-resolution image synthesis,  -->

<!-- [原子块 · verbatim] [27] Mihir Prabhudesai, Anirudh Goyal, Deepak Pathak, and Katerina Fragkiadaki. Aligning text-to-image diffusion models with reward backpropagation, 2023. -->

<!-- [原子块 · verbatim] [28] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models, 2022. -->

<!-- [原子块 · verbatim] [29] Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, and Kfir Aberman. Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation, 2023. -->

<!-- [原子块 · verbatim] [30] Dan Ruta, Gemma Canet Tarrés, Andrew Gilbert, Eli Shechtman, Nicholas Kolkin, and John Collomosse. Diff-nst: Diffusion interleaving for deformable neural style transfer, 2023. -->

<!-- [原子块 · verbatim] [31] Mert Bülent Sarıyıldız, Karteek Alahari, Diane Larlus, and Yannis Kalantidis. Fake it till you make it: Learning transferable representations from synthetic imagenet clones. In Proceedings of the -->

<!-- [原子块 · verbatim] [32] Christoph Schuhmann and Romain Beaumont. Laion-aesthetics. URL https://laion.ai/blog/laion-aesthetics . -->

<!-- [原子块 · verbatim] [33] Kihyuk Sohn, Nataniel Ruiz, Kimin Lee, Daniel Castro Chin, Irina Blok, Huiwen Chang, Jarred Barber, Lu Jiang, Glenn Entis, Yuanzhen Li, Yuan Hao, Irfan Essa, Michael Rubinstein, and Dilip Krishna -->

<!-- [原子块 · verbatim] [34] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations, 2021. -->

<!-- [原子块 · verbatim] [35] Zhiwei Tang, Dmitry Rybin, and Tsung-Hui Chang. Zeroth-order optimization meets human feedback: Provable learning via ranking oracles, 2024. -->

<!-- [原子块 · verbatim] [36] Dimitri von Rütte, Elisabetta Fedele, Jonathan Thomm, and Lukas Wolf. Fabric: Personalizing diffusion models with iterative feedback, 2023. -->

<!-- [原子块 · verbatim] [37] Bram Wallace, Meihua Dang, Rafael Rafailov, Linqi Zhou, Aaron Lou, Senthil Purushwalkam, Stefano Ermon, Caiming Xiong, Shafiq Joty, and Nikhil Naik. Diffusion model alignment using direct prefere -->

<!-- [原子块 · verbatim] [38] Yuxin Wen, Neel Jain, John Kirchenbauer, Micah Goldblum, Jonas Geiping, and Tom Goldstein. Hard prompts made easy: Gradient-based discrete optimization for prompt tuning and discovery, 2023. -->

<!-- [原子块 · verbatim] [39] Xiaoshi Wu, Keqiang Sun, Feng Zhu, Rui Zhao, and Hongsheng Li. Human preference score: Better aligning text-to-image models with human preference, 2023. -->

<!-- [原子块 · verbatim] [40] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation, 2023. -->

<!-- [原子块 · verbatim] [41] Teresa Yeo, Andrei Atanov, Harold Benoit, Aleksandr Alekseev, Ruchira Ray, Pooya Esmaeil Akhoondi, and Amir Zamir. Controlled training data generation with diffusion models. arXiv preprint arXiv: -->

**EN** Appendix

**ZH** 附录

**EN** Appendix A Experimental Setup

**ZH** 附录 A 实验设置

**EN** A.1 Visuals of Generated Images Used for Comments

**ZH** A.1 供评论所用生成图像的可视化

<!-- [原子块 · img]  -->

**EN** Figure 7: Query image set: We generate around 50 images with different art styles and concepts. Individuals are encouraged to choose a subset of these images to comment on.

**ZH** 图 7：查询图像集：我们生成约 50 张具有不同艺术风格与概念的图像。我们鼓励个体选择其中一部分加以评论。

**EN** We employ Stable Diffusion XL [28] to generate around 50 images spanning diverse art styles and concepts. To ensure diversity, we first generated approximately 2000 visual attributes using the same method we used for creating our agents’ visual preferences. Next, we used multiple language models, such as Llama 3 [1] and GPT-4 [24], to generate 50 concepts. We then concatenated the visual attributes with these concepts and selected the top 50 unique images generated from them based on CLIP similarity. Finally, we manually included some images that seemed missing from the final set. While acknowledging that art cannot be fully represented by just 50 images, we opted for this smaller set to spare individuals from the burden of choosing from an extensive selection. However, recognizing the limitations in capturing all aspects of art with this limited set, we ask individuals to provide their own images to comment on if our set fails to evoke strong reactions. We show the generated images in fig. 7.

**ZH** 我们用 Stable Diffusion XL [28] 生成约 50 张涵盖多样艺术风格与概念的图像。为保证多样性，我们首先用与创建智能体视觉偏好相同的方法生成了约 2000 个视觉属性；随后用 Llama 3 [1]、GPT-4 [24] 等多个语言模型生成 50 个概念；再把视觉属性与这些概念拼接，并基于 CLIP 相似度从中选出前 50 张互不重复的图像；最后我们手工补充了一些在最终集合中似乎缺失的图像。我们承认区区 50 张图像无法完整表征艺术，但仍选择这一较小集合，以免个体在过多选项中难以抉择。同时，鉴于这一有限集合难以捕捉艺术的所有方面，若我们的集合无法引发强烈反应，我们会请个体提供自己的图像加以评论。生成的图像见图 7。

**EN** A.2 Prompt Templates

**ZH** A.2 提示词模板

**EN** We use the following prompt template to generate comments using GPT4.

**ZH** 我们用以下提示词模板借助 GPT4 生成评论。

**EN** The prompt template for fine-tuning ⟦SLOT_52⟧ is as follows:

**ZH** 用于微调 ⟦SLOT_52⟧ 的提示词模板如下：

**EN** A.3 Visual Attributes

**ZH** A.3 视觉属性

**EN** The full set of visual attributes is presented on page . In this set, we tried to consider the main features that describe and affect the individual’s perception of image. Some categories include subcategories that contain similar visual attributes. We randomly select several of these attributes for each agent, prioritizing more popular categories such as style, color palette, composition, mood, and medium over movement, depth, lines, etc. This prioritization is done by giving a larger weight to popular categories that we observed mentioned frequently in Lexica’s§§ § lexica.art prompts. The results of 10 sample agents are shown in fig. 8.

**ZH** 完整的视觉属性集合见对应页面。在该集合中，我们尽力考虑了描述并影响个体图像感知的主要特征。部分类别包含若干子类别，其中含有相近的视觉属性。我们为每个智能体随机选取其中若干属性，并优先选择更常见的类别，如风格、色调、构图、情绪、媒介，而非运动、纵深、线条等。这种优先级通过给常见类别更大权重实现——我们观察到这些类别在 Lexica§§ § lexica.art 的提示词中被频繁提及。10 个示例智能体的结果见图 8。

<!-- [原子块 · img]  -->

**EN** Figure 8: The personalized generations of 10 agents, generated with 10 different prompts from the same seed, are presented here. These agents’ visual preferences differ not only in color palette and style but also in various attributes such as texture, pattern, vibe, etc. Note how the preference pattern of each agent’s results remains consistent, with some being more extreme than others.

**ZH** 图 8：此处展示 10 个智能体用同一随机种子、10 个不同提示词生成的个性化结果。这些智能体的视觉偏好不仅在色调与风格上不同，在纹理、图案、氛围等各个属性上也各异。注意每个智能体结果的偏好模式保持一致，其中一些比其他更极端。

**EN** A.4 Experiments with Other Models

**ZH** A.4 用其他模型做实验

**EN** We use GPT4 to generate comments since our initial experiments with the open-source vision-language models, such as IDEFICS2-8b [16, 17], IDEFICS1-80b [16], LLaVA [20, 19], and InstructBLIP [5], hallucinated more often than not. We show some samples in fig. 9. We input the image, and the individual’s preferences, ⟦SLOT_53⟧ and ⟦SLOT_54⟧, to the model with the same comment generation template as the one shown in section A.2.

**ZH** 我们用 GPT4 生成评论，因为我们用 IDEFICS2-8b [16, 17]、IDEFICS1-80b [16]、LLaVA [20, 19] 与 InstructBLIP [5] 等开源视觉-语言模型做的初期实验经常产生幻觉。我们在图 9 中给出一些样本。我们把图像与个体偏好 ⟦SLOT_53⟧ 和 ⟦SLOT_54⟧，连同 A.2 节所示相同的评论生成模板一起输入模型。

**EN** The sample results of these vision-language models shown in fig. 9 mostly discard the input image’s semantics, vibe, and details, and sometimes even discard the given visual preference. In some extreme cases, we witnessed that LLaVA and InstructBLIP would write captions for the images rather than comments, or simply repeat some of the attributes of the given visual preferences without further context.

**ZH** 图 9 所示这些视觉-语言模型的样本结果大多丢弃了输入图像的语义、氛围与细节，有时甚至丢弃了给定的视觉偏好。在一些极端情况下，我们看到 LLaVA 与 InstructBLIP 会为图像写描述而非评论，或者只是重复给定视觉偏好中的某些属性而不提供进一步语境。

<!-- [原子块 · img]  -->

**EN** (a) IDEFICS1-80b: I’m not really feeling this artwork. It’s too busy and vibrant for my taste. I prefer minimalist and abstract pieces with subtlety and open spaces. LLaVA: I find the artwork to be unsettling and creepy, which I appreciate. The melancholic atmosphere and psychological depth and extreme details make it a thought-provoking piece. InstructBLIP: I like the artwork because it has a dark and eerie feel to it. It also has a lot of symbolism and meaning behind it, which is why I like it so much.

**ZH** (a) IDEFICS1-80b：我不太喜欢这件作品。它对我来说太繁杂、太鲜艳。我更喜欢带微妙感与留白的极简抽象作品。LLaVA：我觉得这件作品令人不安、令人毛骨悚然，而我喜欢这一点。忧郁的氛围、心理深度与极致细节使它成为一件引人深思的作品。InstructBLIP：我喜欢这件作品，因为它有一种黑暗、阴森的感觉。它背后还有大量象征与含义，这正是我非常喜欢它的原因。

<!-- [原子块 · img]  -->

**EN** (b) IDEFICS1-80b: I’m not sure about this artwork. It seems a bit too dark and gloomy for my taste. I prefer art that is more uplifting and positive, with vibrant colors and details. LLaVA: The sketch lines and dark themes add to the eerie vibe of the painting. The overall mood remains melancholic and psychologically deep. InstructBLIP: the painting of a woman in a field of flowers is not something that I would like to look at.

**ZH** (b) IDEFICS1-80b：我不太确定这件作品。它对我来说似乎过于阴暗、沉闷。我更喜欢更振奋、更积极的作品，色彩鲜艳且有细节。LLaVA：素描线条与黑暗主题强化了这幅画的诡异氛围。整体情绪依然是忧郁而心理深沉的。InstructBLIP：花田中的女性绘画不是我会想看的东西。

**EN** Figure 9: The comments are generated given an image and an individual’s visual preference. We present some shortcomings we witnessed for different individuals. In fig. 9, neither of the generated comments follows the input image’s content. They discard its minimal and contemporary style. In fig. 9, IDEFICS1-80b and LLaVA’s results do not follow the input image’s content, discarding its happy vibe, while InstructBLIP ignores the given visual preference of a user who loved happy and colorful images depicting flowers.

**ZH** 图 9：评论是在给定图像与个体视觉偏好时生成的。我们展示了在不同个体上观察到的一些不足。在图 9 中，生成的评论都没有遵循输入图像的内容，丢弃了它的极简与当代风格。在图 9 中，IDEFICS1-80b 与 LLaVA 的结果没有遵循输入图像的内容，丢弃了它欢快的氛围；而 InstructBLIP 忽略了某位用户给定的视觉偏好——该用户喜欢描绘花卉的快乐、多彩图像。

**EN** Appendix B User and Proxy Metric Alignment

**ZH** 附录 B 用户与代理指标的一致性

<!-- [原子块 · img]  -->

**EN** Figure 10: On the left, we display the results of users, and on the right, we display proxy ⟦SLOT_55⟧’s results from the User’s vs. Other Users’ Pers test for eight users. By providing each user’s preferences (liked and disliked images) to ⟦SLOT_56⟧, we simulate their behavior. Images generated from 15 distinct prompts personalized for the eight users are organized within each matrix according to real user rankings or ⟦SLOT_57⟧’s predictions. A score is assigned to indicate the preference of user ⟦SLOT_58⟧ towards user ⟦SLOT_59⟧’s images, with higher scores reflecting greater preference. The scores are averaged over prompts and the matrices are normalized for analysis. Note how both users and ⟦SLOT_60⟧ preferred the personalized image on average in most cases. It’s crucial to understand that attaining 100% alignment between users and ⟦SLOT_61⟧ is impossible due to the complexity of users’ preferences, which aren’t solely influenced by personalization factors. These variations are intrinsic to Stable Diffusion rather than personalization itself. ⟦SLOT_62⟧ is limited in its ability to accommodate these nuances as it’s tuned solely to recognize users’ preference patterns based on their liked and disliked images.

**ZH** 图 10：左侧展示用户的结果，右侧展示代理 ⟦SLOT_55⟧ 在八位用户的 User’s vs. Other Users’ Pers 测试中的结果。通过把每位用户的偏好（喜欢与不喜欢的图像）提供给 ⟦SLOT_56⟧，我们模拟他们的行为。由 15 个不同提示词为八位用户个性化生成的图像，按真实用户排序或 ⟦SLOT_57⟧ 的预测排布在每个矩阵内。我们赋予一个分数来表示用户 ⟦SLOT_58⟧ 对用户 ⟦SLOT_59⟧ 图像的偏好程度，分数越高表示偏好越强。分数在提示词上取平均，矩阵经归一化以便分析。注意用户与 ⟦SLOT_60⟧ 在多数情况下平均都更偏好个性化图像。关键要理解的是，用户与 ⟦SLOT_61⟧ 之间不可能达到 100% 一致，因为用户偏好十分复杂，并不只受个性化因素影响。这些差异源于 Stable Diffusion 本身，而非个性化本身。⟦SLOT_62⟧ 无法容纳这些细微之处，因为它仅被调优为根据喜欢与不喜欢的图像识别用户的偏好模式。

**EN** To demonstrate the alignment between users and the proxy metric, we closely examine the User’s vs. Other Users’ Pers test for eight users. We emulate each user’s behavior with our metric ⟦SLOT_63⟧ by providing ⟦SLOT_64⟧ with their liked and disliked images. In fig. 10, we present the confusion matrices of the user test alongside the metric’s simulation of the exact same test. Within each confusion matrix, images generated from 15 distinct prompts personalized for the eight users are arranged based on real user rankings, or ⟦SLOT_65⟧’s predictions. Rank 1 indicates that the user (or ⟦SLOT_66⟧) preferred that image over the others, while Rank 8 indicates the user’s (or ⟦SLOT_67⟧’s) least liked image. In most cases, users only ranked from 1 to 4, as they felt indifferent toward the other images present in the test for that prompt. The score in the ⟦SLOT_68⟧th row and ⟦SLOT_69⟧th column indicates how much user ⟦SLOT_70⟧ likes the images of user ⟦SLOT_71⟧: for each row ⟦SLOT_72⟧, a score of ⟦SLOT_73⟧ is added to the element ⟦SLOT_74⟧ if user ⟦SLOT_75⟧ ranks an image of user ⟦SLOT_76⟧ in the ⟦SLOT_77⟧th place (or if ⟦SLOT_78⟧ ranks it for them). These scores are then averaged over the prompts, and each row of the matrices is normalized. Note how the users’ results are aligned with ⟦SLOT_79⟧’s predictions. On average, both users and ⟦SLOT_80⟧ ranked their personalized images as the most preferred. It is important to note that achieving 100% alignment between users and ⟦SLOT_81⟧ is unattainable. This is due to the nuanced nature of users’ choices, which are not solely dependent on personalization factors. For instance, one user selected an image that deviated significantly from their indicated preference. Their rationale for not choosing the personalized image was that "the person in this image is too thin, like she’s starving". These deviations are inherent to Stable Diffusion itself rather than the concept of personalization. ⟦SLOT_82⟧ is unable to account for such deviations as it is solely tuned to discern users’ preference patterns from their favored and disliked images.

**ZH** 为展示用户与代理指标的一致性，我们细致考察了八位用户的 User’s vs. Other Users’ Pers 测试。我们用指标 ⟦SLOT_63⟧，通过向 ⟦SLOT_64⟧ 提供其喜欢与不喜欢的图像来模拟每位用户的行为。图 10 给出了用户测试的混淆矩阵，以及该指标对完全相同测试的模拟结果。在每个混淆矩阵内，由 15 个不同提示词为八位用户个性化生成的图像，按真实用户排序或 ⟦SLOT_65⟧ 的预测排布。第 1 名表示该用户（或 ⟦SLOT_66⟧）相比其他图像更偏好该图像，第 8 名表示该用户（或 ⟦SLOT_67⟧）最不喜欢的图像。多数情况下用户只排到第 1 至第 4 名，因为他们对测试中该提示词下的其余图像并无偏好差异。第 ⟦SLOT_68⟧ 行第 ⟦SLOT_69⟧ 列的分数表示用户 ⟦SLOT_70⟧ 对用户 ⟦SLOT_71⟧ 图像的喜欢程度：对每一行 ⟦SLOT_72⟧，分值 ⟦SLOT_73⟧ 会被加到元素 ⟦SLOT_74⟧ 上，条件是用户 ⟦SLOT_75⟧ 把用户 ⟦SLOT_76⟧ 的一张图像排在第 ⟦SLOT_77⟧ 位（或由 ⟦SLOT_78⟧ 为其排出该名次）。这些分数随后在提示词上取平均，矩阵的每一行做归一化。注意用户的结果与 ⟦SLOT_79⟧ 的预测是一致的：平均而言，用户与 ⟦SLOT_80⟧ 都把自己的个性化图像排在最受偏好的位置。需要说明的是，用户与 ⟦SLOT_81⟧ 之间不可能达到 100% 一致，这源于用户选择本身的微妙性质——它并不只取决于个性化因素。例如，某位用户选了一张与其所表明偏好明显偏离的图像，其未选择个性化图像的理由是“这张图里的人太瘦了，像在挨饿一样”。这类偏离是 Stable Diffusion 本身固有的，而非个性化这一概念所致。⟦SLOT_82⟧ 无法解释此类偏离，因为它仅被调优为从用户喜欢与不喜欢的图像中识别其偏好模式。

<!-- [原子块 · img]  -->

**EN** Figure 11: Each user is represented to ⟦SLOT_83⟧ by the set of images they like. Notice how, given this set of images, ⟦SLOT_84⟧ manages to output a higher score to query images that share the same preferred features and a lower score to those that do not.

**ZH** 图 11：每位用户由其所喜欢的图像集合表示给 ⟦SLOT_83⟧。注意，给定该图像集合后，⟦SLOT_84⟧ 能对具有相同偏好特征的查询图像输出更高分数，对不具这些特征的图像输出更低分数。

**EN** In fig. 11, we demonstrate how a user is represented to ⟦SLOT_85⟧ by the set of images they like (disliked images are not shown for the sake of simplicity). Notice how ⟦SLOT_86⟧ assigns a significantly higher score to query images that share the same visual pattern and vibe as the liked images for each user.

**ZH** 在图 11 中，我们展示一位用户如何通过其所喜欢的图像集合被表示给 ⟦SLOT_85⟧（为简洁起见未展示不喜欢的图像）。注意 ⟦SLOT_86⟧ 对与每位用户所喜欢图像具有相同视觉模式与氛围的查询图像，给出的分数显著更高。

**EN** Appendix C Additional Experiments

**ZH** 附录 C 补充实验

**EN** C.1 Large-scale Automated Evaluation

**ZH** C.1 大规模自动评价

**EN** To compare the performance of ViPer with other personalization methods, we conducted multiple tests on images personalized for 1000 agents using both Prompt Personalization and ViPer. We use ⟦SLOT_87⟧, CLIP similarity, and PickScore [14] to calculate accuracy. Personalized vs. Non-Personalized Comparison In this experiment, we utilize the proxy metrics to distinguish between agents’ personalized images and random non-personalized images. We anticipate these proxies assigning higher scores to personalized images compared to non-personalized ones. Accuracy is measured as the ratio of correct comparisons to the total number of comparisons. To conduct this test with ⟦SLOT_88⟧, for each agent, we input their set of personalized images as liked images and random non-personalized images as disliked images to act as the preference signal. When using CLIP and PickScore, the preference signal becomes the ⟦SLOT_89⟧ text itself. Subsequently, for each agent, we consider two query images: one personalized and one non-personalized. The proxy metrics are then run on all agents, and alignment between preference signals and query images is calculated. The results are outlined in table 3. It’s notable that ViPer consistently outperforms Prompt Personalization across all three metrics. Despite CLIP and PickScore showing lower accuracy as they are not specifically fine-tuned for this task, their evaluations largely align with ⟦SLOT_90⟧’s. Prompt-Image Alignment We evaluate the alignment of base prompts and personalized images to determine which personalization method prioritizes results following the users’ input prompts. For each agent, we consider two query images, both personalized. Then, we run CLIP similarity and PickScore on the initial input prompt and the queries. We anticipate that the score will be higher for the personalized image generated from the input prompt compared to the one that is not generated from that input prompt. The results can be seen in table 4. Note how, once again, ViPer outperforms Prompt Personalization.

**ZH** 为比较 ViPer 与其他个性化方法的性能，我们在用提示词个性化与 ViPer 为 1000 个智能体个性化生成的图像上进行了多项测试。我们用 ⟦SLOT_87⟧、CLIP 相似度与 PickScore [14] 计算准确率。个性化与非个性化的比较 在该实验中，我们利用代理指标区分智能体的个性化图像与随机的非个性化图像，预期这些代理会给个性化图像打更高分。准确率以正确比较数占总比较数的比例衡量。用 ⟦SLOT_88⟧ 进行该测试时，对每个智能体，我们输入其个性化图像集合作为喜欢的图像，输入随机的非个性化图像作为不喜欢的图像，以此充当偏好信号。使用 CLIP 与 PickScore 时，偏好信号则变为 ⟦SLOT_89⟧ 文本本身。随后，对每个智能体考虑两张查询图像：一张个性化、一张非个性化。代理指标在所有智能体上运行，并计算偏好信号与查询图像之间的对齐程度。结果见表 3。值得注意的是，ViPer 在所有三个指标上都一致优于提示词个性化。尽管 CLIP 与 PickScore 因未针对该任务专门微调而准确率较低，它们的评价在很大程度上与 ⟦SLOT_90⟧ 一致。提示词-图像对齐 我们评估基础提示词与个性化图像的对齐程度，以判断哪种个性化方法优先遵循用户的输入提示词。对每个智能体考虑两张查询图像，两者都是个性化的；然后在初始输入提示词与查询上运行 CLIP 相似度与 PickScore。我们预期：由输入提示词生成的个性化图像得分会高于非由该输入提示词生成的图像。结果见表 4。同样可以看到，ViPer 优于提示词个性化。

**EN** Table 3: We use three proxy metrics to differentiate between personalized and non-personalized images of 1000 agent, expecting higher scores for personalized ones. Accuracy is the ratio of correct comparisons to total comparisons. For each agent, their personalized images are compared to random non-personalized ones as the preference signal. With CLIP and PickScore, the preference signal is the VP text. Two query images, one personalized and one non-personalized, are considered per agent. See how ViPer consistently outperforms Prompt Personalization across all metrics. While CLIP and PickScore, not fine-tuned for this task, show lower accuracy, their evaluations largely align with ⟦SLOT_91⟧’s.

**ZH** 表 3：我们用三个代理指标区分 1000 个智能体的个性化与非个性化图像，预期个性化图像得分更高。准确率为正确比较数占总比较数的比例。对每个智能体，将其个性化图像与随机非个性化图像作为偏好信号进行比较；使用 CLIP 与 PickScore 时，偏好信号为视觉偏好文本本身。每个智能体考虑两张查询图像，一张个性化、一张非个性化。可见 ViPer 在所有指标上一致优于提示词个性化。CLIP 与 PickScore 未针对该任务微调，准确率较低，但它们的评价在很大程度上与 ⟦SLOT_91⟧ 一致。

<!-- [原子块 · table] CLIP PickScore M M Prompt Personalization 69.5% 62.4% 83.9% ViPer 73.3% 67.0% 89.1 % -->

**EN** Table 4: We utilize CLIP and PickScore to assess the alignment between personalized images and input prompts, anticipating higher scores for images generated from the input prompt compared to those that are not. Accuracy is measured by the ratio of correct comparisons to total comparisons. Notice how ViPer consistently outperforms Prompt Personalization across both metrics.

**ZH** 表 4：我们用 CLIP 与 PickScore 评估个性化图像与输入提示词的对齐程度，预期由输入提示词生成的图像得分高于非由其生成的图像。准确率以正确比较数占总比较数的比例衡量。注意 ViPer 在两个指标上都一致优于提示词个性化。

<!-- [原子块 · table] CLIP PickScore Prompt Personalization 83.5% 79.6% ViPer 90.3% 87.8% -->

**EN** C.2 Effect of Number of Comments

**ZH** C.2 评论数量的影响

<!-- [原子块 · img]  -->

**EN** Figure 12: Each column is generated from visual preferences extracted from the same set of comments. In the leftmost column, we selected only one random comment, while in the rightmost column, we generated the visual preference from all the user’s provided comments. The prompts are displayed on the left. It is evident that as the number of comments increases, the results become more aligned with the user’s artistic preferences. While the first column only considered attributes such as distaste for "Abstract", "Contemporary", and "Vibrant Colors" along with a preference for "Delicate" and "Detailed" images, the second column included elements regarding color palette and historical vibe. These visual attributes expanded to the complete set presented in fig. 12.

**ZH** 图 12：每一列都由从同一组评论中提取的视觉偏好生成。最左列只随机选取了一条评论，最右列则从用户提供的全部评论中生成视觉偏好。提示词显示在左侧。显然，随着评论数量增加，结果与该用户的艺术偏好越来越一致。第一列只考虑到对“抽象”“当代”“鲜艳色彩”的厌恶以及对“精致”“细节丰富”图像的偏好，第二列则加入了有关色调与历史氛围的元素。这些视觉属性扩展到图 12 所示的完整集合。

**EN** After selecting which images to comment on, individuals are encouraged to discuss their likes or dislikes for each selected image, expressing their perception of it and the emotions it evokes. Importantly, individuals are not bound to any specific writing structure when commenting. They can write as much or as little as they prefer, as we utilize a language model to extract structured preferences from their free-form comments. Ideally, these comments are descriptive, covering most of the attributes present in the images that are important to the individual. We demonstrate that in this case, comments on as few as eight images are enough to obtain personalized results.

**ZH** 在选择要评论的图像之后，我们鼓励个体讨论对每张所选图像的喜欢或不喜欢，表达自己对它的感知以及它唤起的情绪。重要的是，个体在评论时不受任何特定写作结构的约束，可长可短，随其所愿，因为我们使用语言模型从其自由形式评论中提取结构化偏好。理想情况下，这些评论应具有描述性，覆盖图像中对个体重要的多数属性。我们证明，在这种情况下，对少至八张图像的评论就足以获得个性化结果。

**EN** Consider a user who has the following visual preference:

**ZH** 考虑一位具有以下视觉偏好的用户：

**EN** Likes: Transparent Texture, Glassy, Delicate, Detailed, Story-telling, Intricate Lines, Smooth Texture, Muted Earthy Colors, Historical, Realistic Lighting, Classicism, Busy Composition, Neo-classicism, Balanced, Open Space, Matte, Depth, Matching Colors, Renaissance, Blending Colors, Subtle Lighting, Ethereal, Atmospheric Perspective, Illusion of Depth, Oil Painting, Creativity, Soft Texture, Romanticism, Desaturated, Majestic, Watercolor

**ZH** 喜欢：透明质感、玻璃感、精致、细节丰富、叙事性、繁复线条、平滑质感、柔和大地色、历史感、写实光照、古典主义、繁复构图、新古典主义、均衡、留白、哑光、纵深、色彩协调、文艺复兴、色彩融合、微妙光照、空灵、空气透视、纵深错觉、油画、创意、柔和质感、浪漫主义、低饱和、庄严、水彩

**EN** Dislikes: Abstract, Contemporary, Vibrant Colors, Incoherent Shapes, Chaotic Brushstrokes, Simplistic, Blood and Gore, Bright and Blunt Colors, Single-focused, Realism, Flat, Polished, Modern Architecture, Extreme Colors, Monochromatic, Cold Colors, Picasso, Geometric Patterns, Somber, Dark, Dominating Red, Dry Brushstrokes, Monochromatic, Minimalism, Artificial Colors, Color Splash, Photorealistic, Cartoon, Childish

**ZH** 不喜欢：抽象、当代、鲜艳色彩、形状不连贯、笔触混乱、简略、血腥、明亮而生硬的色彩、单一焦点、写实主义、平面、抛光、现代建筑、极端色彩、单色、冷色、毕加索、几何图案、阴郁、暗沉、红色主导、干笔触、单色、极简主义、人工色彩、色彩飞溅、照片写实、卡通、幼稚

**EN** In fig. 12 we randomly select a subset of this user’s comments and extract their visual preferences from them. In the leftmost column, where only one random comment was selected, the results do not exactly align with the user’s preferences in images. As the number of comments increases, they converge towards their general preference for classic art and related visual attributes, and with eight comments, the results are almost perfectly aligned with their taste, though the user still preferred the last column consistently. It is notable that this experiment is also dependent on the random subset chosen. If the user’s selected comment in the first column indicated their extreme preference toward "Classicism", "Renaissance", or "Muted Earthy Colors", etc., the results would have aligned more with their preference. To avoid cases where commenting on an image fails to give us a lot of information about the user, we ask users to provide an average number of eight to ten comments on images that provoke strong reactions from them.

**ZH** 在图 12 中，我们随机选取该用户评论的一个子集，并从中提取其视觉偏好。在最左列中只选取了一条随机评论，结果与用户在图像上的偏好并不完全吻合。随着评论数量增加，结果逐渐收敛到他们对古典艺术及相关视觉属性的总体偏好；到八条评论时，结果几乎与他们的品味完全吻合，尽管用户始终更偏好最后一列。值得注意的是，该实验还依赖于所选的随机子集：若用户在第一列中选到的评论表达了其对“古典主义”“文艺复兴”或“柔和大地色”等的强烈偏好，结果会更贴合其偏好。为避免对某张图像的评论无法提供关于用户的大量信息，我们要求用户平均提供八到十条评论，对象选择能引发其强烈反应的图像。

**EN** C.3 Prompt Personalization

**ZH** C.3 提示词个性化

**EN** This approach involves modifying prompts using language models based on an individual’s visual preference signal. We instruct the language model to adjust a given prompt based on the provided visual preference text. The objective is to obtain a tailored prompt that, when given to a generative model, can produce a personalized image. This approach serves as a baseline to explore another method of utilizing the ⟦SLOT_92⟧ signals aside from ViPer’s approach. The input prompt to the language model is as follows:

**ZH** 该方法用语言模型基于个体的视觉偏好信号修改提示词。我们指示语言模型依据给定的视觉偏好文本调整给定提示词，目标是得到一个定制化提示词，使其在交给生成模型时能产生个性化图像。该方法作为一个基线，用于探索除 ViPer 之外另一种利用 ⟦SLOT_92⟧ 信号的方式。输入语言模型的提示词如下：

**EN** This method has some shortcomings due to being dependent on a language model. This may lead to lengthy prompts, disregarding parts of visual preferences, and adopting a conversational tone, even against explicit instructions. Additionally, the personalized prompts may fail to include key concepts from the original prompts, e.g., the prompt "Paper clouds, brown origami birds" was transformed into "German Expressionism-inspired clouds float gracefully alongside birds in a sky painted with earthy tones and azure hues. The scene is illuminated by the golden hour, casting a surreal glow over the vibrant landscape. The birds soar amidst dynamic, fragmented clouds, creating a pensive yet lively atmosphere" when using ChatGPT. This resulted in the loss of the instructed materials in the prompt, such as paper and the concept of using origami, as well as the color brown, for the sake of incorporating visual attributes the individual prefers.

**ZH** 由于依赖语言模型，该方法存在一些不足：可能导致提示词冗长、忽略部分视觉偏好，并且即便有明确指示也可能采用对话式口吻。此外，个性化后的提示词可能未能包含原始提示词中的关键概念，例如提示词“纸做的云，棕色折纸鸟”在使用 ChatGPT 时被改写成“受德国表现主义启发的云朵优雅地飘浮在天空中，与鸟儿相伴，天空以大地色与蔚蓝色绘就。场景被黄金时刻照亮，为充满活力的风景投下超现实的光辉。鸟儿在动态、碎片化的云朵间翱翔，营造出沉思而生动的氛围”。这导致提示词中指定的材料（如纸）与折纸概念以及棕色被丢失，只为融入个体偏好的视觉属性。

**EN** We show some of these samples in fig. 13. Each row represents a user’s preference. We can see that ViPer considers the input prompts’ consistently. However, depending on the language model in use, Llama 2-70b or ChatGPT, Prompt Personalization either misses the input prompt or the visual preference. Note that one cannot simply rely on appending the visual preference text to the input prompt, as Stable Diffusion would ignore most parts of the visual preference due to the length of the prompt.

**ZH** 我们在图 13 中展示其中一些样本。每一行代表一位用户的偏好。可以看到 ViPer 始终考虑输入提示词；然而，取决于所用的语言模型（Llama 2-70b 或 ChatGPT），提示词个性化要么丢失输入提示词，要么丢失视觉偏好。注意，不能简单地把视觉偏好文本追加到输入提示词上，因为提示词过长会使 Stable Diffusion 忽略视觉偏好的大部分内容。

<!-- [原子块 · img]  -->

**EN** Figure 13: Each row represents a different user and prompt, highlighting the shortcomings of Prompt Personalization. The input prompts are displayed on the left. The leftmost column presents generated responses without any personalization, while the subsequent three columns are personalized using either ViPer or Prompt Personalization with Llama 2 or ChatGPT. While losing the input prompt due to a lengthy personalized prompt is more common, the last row illustrates how ChatGPT completely ignored the user’s visual preference (In this case, the personalized prompt became Solitary figure stands amidst a gathering crowd). In contrast, ViPer personalized the results while still adhering to the instructions provided in the input prompt. It’s also notable that sometimes, the language model gets fixated on a specific visual attribute, leading to extreme results such as Llama 2’s third row, which totally lost the concept of the input prompt by emphasizing minimalism, even though it was one of the many visual attributes present in the user’s preference.

**ZH** 图 13：每一行代表不同的用户与提示词，突出提示词个性化的不足。输入提示词显示在左侧。最左列为不做任何个性化的生成结果，其后三列分别用 ViPer 或用 Llama 2 / ChatGPT 做提示词个性化生成。因个性化提示词过长而丢失输入提示词更为常见；最后一行展示了 ChatGPT 完全忽略用户视觉偏好的情形（此时个性化提示词变成了“孤独的身影立于聚集的人群之中”）。相比之下，ViPer 在个性化结果的同时仍遵循输入提示词给出的指示。同样值得注意的是，语言模型有时会执着于某个特定视觉属性，导致极端结果，如 Llama 2 的第三行通过强调极简主义完全丢失了输入提示词的概念，尽管极简主义只是用户偏好中众多视觉属性之一。

**EN** C.4 Consistency with Input Prompts

**ZH** C.4 与输入提示词的一致性

<!-- [原子块 · img]  -->

**EN** Figure 14: Each column is generated from a user’s preference using ViPer, and the prompts are shown on the left. While the results are still somewhat personalized, they follow the visual attributes defined in the prompts.

**ZH** 图 14：每一列由某位用户的偏好用 ViPer 生成，提示词显示在左侧。虽然结果仍具有一定个性化，但它们遵循提示词中定义的视觉属性。

**EN** In our tests, input prompts dictate results, with visual preference embeddings limited by ⟦SLOT_93⟧ to prevent overshadowing prompt embeddings. In fig. 14, we present the results of seven users for seven prompts that explicitly define the art style, medium, or color palette. We can see that even though the results are still personalized and there is a clear preference pattern in each column, they consistently adhere to the input prompt’s meaning. In fig. 15 we compare the baseline results for a single prompt when the style is specified. Note how ZO-RankSGD’s [35] generations are similar to the generations without any personalization. While FABRIC [36] changes the images, the results are not only not personalized but also sometimes lose the prompt’s original style (see row 2 in column 3). Textual Inversion’s [7] results are too vibrant for the user’s taste and lose the prompt’s specified style as well (see row 3 and 4 in column 4). Prompt Personalization misses the "Van Gogh" style but is mostly aligned with the user’s preference. However, ViPer follows both the input prompt’s style and the user’s visual preference. It’s important to note that since the effect of input prompt is more than visual preferences, due to ⟦SLOT_94⟧’s limitation, individuals can generate images with attributes they dislike by mentioning them in the prompt (see row 5 in column 5).

**ZH** 在我们的测试中，输入提示词决定结果，视觉偏好嵌入受 ⟦SLOT_93⟧ 限制，以免压过提示词嵌入。在图 14 中，我们展示七位用户在七个明确指定艺术风格、媒介或色调的提示词上的结果。可以看到，尽管结果仍具个性化、每列都有清晰的偏好模式，它们始终遵循输入提示词的含义。在图 15 中，我们比较指定风格时单个提示词下各基线的结果。注意 ZO-RankSGD [35] 的生成结果与无个性化的结果相近；FABRIC [36] 虽改变了图像，但结果不仅没有个性化，有时还丢失了提示词的原始风格（见第 3 列第 2 行）；Textual Inversion [7] 的结果对用户品味而言过于鲜艳，同样丢失了提示词指定的风格（见第 4 列第 3、4 行）；提示词个性化遗漏了“梵高”风格，但大体与用户偏好相对齐。而 ViPer 同时遵循输入提示词的风格与用户的视觉偏好。需要注意的是，由于输入提示词的影响大于视觉偏好（受 ⟦SLOT_94⟧ 的限制），个体可以通过在提示词中提及某些属性来生成带有其不喜欢的属性的图像（见第 5 列第 5 行）。

<!-- [原子块 · img]  -->

**EN** Figure 15: For the "Cityscape" prompt, we’re comparing ViPer with baselines with specified styles in prompts. Each row follows the style on the left. The leftmost column has no personalization, while the next five columns show different methods’ generations. ZO-RankSGD’s results resemble those without personalization. FABRIC changes images, but the user doesn’t find them personalized and they sometimes lose the original style (see row 2 in column 3). Textual inversion’s results are too vibrant for the user’s taste and lose the specified style (see row 4 in column 4). Prompt Personalization misses the "Van Gogh" style but aligns well with the user’s preference. ViPer follows both the prompt’s style and the user’s visual preference. Note how the user dislikes "Cubism," yet it appeared in the result (see row 5 in column 5) when specified in the prompt. The user’s visual preference and a small set of images they like and dislike are presented at right.

**ZH** 图 15：对于“城市景观”提示词，我们在提示词中指定风格的情况下比较 ViPer 与各基线。每一行遵循左侧的风格。最左列不做个性化，其后五列展示不同方法的生成结果。ZO-RankSGD 的结果与无个性化的结果相似。FABRIC 改变了图像，但用户并不觉得它们被个性化，且有时丢失了原始风格（见第 3 列第 2 行）。Textual Inversion 的结果对用户品味而言过于鲜艳，并丢失了指定风格（见第 4 列第 4 行）。提示词个性化遗漏了“梵高”风格，但与用户偏好吻合良好。ViPer 同时遵循提示词的风格与用户的视觉偏好。注意该用户不喜欢“立体主义”，但当提示词中指定了它时，结果中仍出现了立体主义（见第 5 列第 5 行）。右侧给出该用户的视觉偏好以及其喜欢与不喜欢的一小组图像。

**EN** C.5 Effect of Visual Attributes

**ZH** C.5 视觉属性的作用

**EN** While visual attributes such as color palette and art style are immediately apparent to the eye upon first glance at images, it’s important to note that other visual attributes also exert a significant effect on the results. To analyze this, we create 100 agents within three categories: those without preferred colors, those without preferred art styles, and those without both colors and styles. We then conduct an identifiability test on these agents, using our proxy metric to observe how distinguishable the results are. In this test, we initially generate images based on each agent’s preferences. We then use these generated images as examples of images the agent likes, while selecting random images from other agents’ preferences to represent images the agent doesn’t like. Our expectation is that our proxy will assign higher scores to the images generated specifically for each agent and lower scores to the random images. We show the results of the test in table 5. It’s evident that defining colors or art styles enhances our proxy’s ability to better distinguish between liked and disliked images; however, other visual attributes are also undoubtedly important in this process. We show an individual’s results in fig. 16. Notice how, even without defining specific colors or art styles, the overall pattern of the images remains consistent and all of the generations are personalized.

**ZH** 虽然色调与艺术风格等视觉属性在第一眼看到图像时就立刻显现，但需要注意的是，其他视觉属性也对结果有显著影响。为分析这一点，我们创建 100 个智能体，分为三类：没有偏好颜色的、没有偏好艺术风格的、以及既无颜色偏好也无风格偏好的。随后我们对这些智能体进行可辨识性检验，用我们的代理指标观察结果的区分度。在该检验中，我们首先依据每个智能体的偏好生成图像；然后把这些生成的图像当作该智能体喜欢的图像示例，并从其他智能体的偏好中随机选取图像代表其不喜欢的图像。我们预期代理会给专门为每个智能体生成的图像更高分数，给随机图像更低分数。检验结果见表 5。可见，定义颜色或艺术风格能增强代理区分喜欢与不喜欢图像的能力，但其他视觉属性在这一过程中无疑也很重要。我们在图 16 中展示一个个体的结果。注意即便没有定义具体颜色或艺术风格，图像的整体模式仍保持一致，且所有生成结果都具有个性化。

<!-- [原子块 · img]  -->

**EN** Figure 16: For an individual with preference for Bold Outlines, Sharpie, High-contrast, Simplified, Color-pencil, Kawaii, Alex Katz Style, Iwona Lifsches Style, Cartoon, Comic, Naive Art, Bright Colors, Playful, Pastel Palette, Paper Texture, Sketch Lines, Gouache, Opaque Watercolor, Nostalgic, Pink, Yellow, Blue, Lilac, in each column we remove either the color palette attributes, art style attributes, or both, to show the effect of the other visual attributes in more detail. See page for the grouping and definition of visual attributes. There are 20 categories of attributes in general. Excluding color palette and art style, these categories include composition, mood, etc. The first column shows the non-personalized generations. Note how in the other columns, the overall pattern of the images remains consistent. This consistency arises because many visual attributes already establish the foundation of the preferred art styles and colors. Clearly, these effects vary for each unique visual preference, depending on the preferred attributes.

**ZH** 图 16：对于一位偏好粗轮廓、马克笔、高对比、简化、彩铅、Kawaii、Alex Katz 风格、Iwona Lifsches 风格、卡通、漫画、稚拙艺术、明亮色彩、俏皮、柔和色调、纸质纹理、素描线条、水粉、不透明水彩、怀旧、粉色、黄色、蓝色、淡紫色的个体，我们在每一列中分别移除色调属性、艺术风格属性或两者，以更详细地展示其他视觉属性的作用。视觉属性的分组与定义见对应页面。属性共有 20 个类别；除色调与艺术风格外，这些类别还包括构图、情绪等。第一列展示非个性化生成结果。注意其余各列中图像的整体模式保持一致。这种一致性源于许多视觉属性已经奠定了偏好艺术风格与色彩的基础。显然，这些作用随每种独特的视觉偏好及其偏好属性而异。

**EN** Table 5: To analyze the effect of different visual attributes, we study 100 agents divided into three groups: without preferred colors, without preferred art styles, and without both colors and styles. Results show that specifying color or art style helps our metric identify liked and disliked images better, but other visual attributes are also significant.

**ZH** 表 5：为分析不同视觉属性的作用，我们研究 100 个智能体，分为三组：无偏好颜色、无偏好艺术风格、以及既无颜色也无风格偏好。结果表明，指定颜色或艺术风格有助于我们的指标更好地识别喜欢与不喜欢的图像，但其他视觉属性同样重要。

<!-- [原子块 · table] No Color - No Style Style Defined Color Defined Both defined Random Accuracy 71.6% 78.8% 83.1% 91.4% 50.0% -->

**EN** C.6 Diversity Concerns

**ZH** C.6 多样性方面的顾虑

**EN** One potential concern is that the proposed system might cause the diversity of outputs to collapse for a particular prompt. To address this, we compared the diversity of outputs from non-personalized and personalized models on the same prompt. ViPer allows users to adjust diversity through the personalization degree, similar to the classifier-free guidance (⟦SLOT_95⟧) scale (see Fig. 5 of the main paper). Non-personalized Stable Diffusion tends to produce similar outputs with high ⟦SLOT_96⟧ scales, indicating a trade-off between prompt-image alignment and diversity. Similarly, ViPer presents a trade-off between diversity and personalization, modifiable by the personalization degree. By adjusting the personalization degree, users can control the balance between the specificity of the personalization and the diversity of the generated outputs. In fig. 17 we show some images generated from different ⟦SLOT_97⟧ scales and personalization degrees. We can see that as we decrease these hyperparameters, the outputs become less similar.

**ZH** 一个潜在的顾虑是，所提出的系统可能导致某个提示词下输出的多样性坍缩。为此，我们比较了非个性化与个性化模型在同一提示词上输出的多样性。ViPer 允许用户通过个性化程度调节多样性，类似于无分类器引导（⟦SLOT_95⟧）尺度（见正文图 5）。非个性化的 Stable Diffusion 在 ⟦SLOT_96⟧ 尺度较高时倾向于产生相似输出，说明提示词-图像对齐与多样性之间存在权衡。类似地，ViPer 在多样性与个性化之间也存在权衡，可通过个性化程度加以调节。通过调节个性化程度，用户可以控制个性化的专一性与生成输出多样性之间的平衡。图 17 展示了以不同 ⟦SLOT_97⟧ 尺度与个性化程度生成的一些图像。可以看到，随着这两个超参数降低，输出之间的相似度下降。

<!-- [原子块 · img]  -->

**EN** Figure 17: We generate multiple images from the same prompt with different ⟦SLOT_98⟧ scales and personalization degrees. Note how the outputs become more similar as the ⟦SLOT_99⟧ scale and personalization degree increase. One can increase the level of diversity by lowering these two hyperparameters.

**ZH** 图 17：我们用不同 ⟦SLOT_98⟧ 尺度与个性化程度，由同一提示词生成多张图像。注意随着 ⟦SLOT_99⟧ 尺度与个性化程度提高，输出变得更为相似。降低这两个超参数即可提升多样性水平。

**EN** C.7 Effect of Number of Images on Proxy

**ZH** C.7 图像数量对代理指标的影响

<!-- [原子块 · img]  -->

**EN** Figure 18: We generate 100 agents and 10 images based on each of their visual preferences. Then, for each agent, we conduct a test with our proxy ⟦SLOT_100⟧ to determine if it can assign a higher score to an agent’s personalized images compared to random images, while varying the number of input images (both personalized and non-personalized). We observe that as the number of images in the context increases, the accuracy of the ⟦SLOT_101⟧ also increases, stabilizing at 91.1% after approximately 18 input images.

**ZH** 图 18：我们生成 100 个智能体，并依据各自的视觉偏好生成 10 张图像。随后对每个智能体用我们的代理 ⟦SLOT_100⟧ 进行检验，判断它能否给智能体的个性化图像打出高于随机图像的分数，同时改变输入图像（个性化与非个性化）的数量。我们观察到，随着上下文中图像数量增加，⟦SLOT_101⟧ 的准确率也随之提高，在约 18 张输入图像后稳定在 91.1%。

**EN** To understand the impact of the number of images (both personalized and non-personalized for each agent) in the input prompt for the proxy, we evaluate the proxy’s ability to distinguish between an agent’s personalized and non-personalized query images. This evaluation involves providing the proxy with a varying number of personalized and non-personalized images (ranging from 0 to 28) as context in the input prompt.

**ZH** 为理解输入提示词中图像数量（每个智能体的个性化与非个性化图像）对代理指标的影响，我们评估代理区分智能体个性化与非个性化查询图像的能力。该评估向代理提供数量不等（从 0 到 28）的个性化与非个性化图像，作为输入提示词中的上下文。

**EN** For each agent, we measure accuracy based on whether the proxy assigns a higher score to the personalized query compared to a non-personalized image. In fig. 18, we depict the relationship between accuracy and the number of input images in the context by testing 100 agents. We can see that with fewer input images, the metric’s predictions are closer to random. However, as we increase the number of images in the input prompt, the proxy’s accuracy improves for both test sets, stabilizing at approximately 91.1% accuracy after around 18 images in the context. This indicates that with more data (i.e., more input images), the proxy gains a better understanding of the agents’ visual preferences, resulting in more reliable outcomes.

**ZH** 对每个智能体，我们依据代理是否给个性化查询图像打出高于非个性化图像的分数来衡量准确率。图 18 通过对 100 个智能体测试，描绘了上下文中输入图像数量与准确率之间的关系。可以看到，输入图像较少时，指标的预测接近随机；然而，随着输入提示词中图像数量增加，代理在两组测试上的准确率都有所提升，在上下文中约有 18 张图像后稳定在约 91.1% 的准确率。这说明随着数据（即输入图像）增多，代理对智能体视觉偏好有更好的理解，结果也更可靠。

**EN** C.8 Fine-Tuning Stable Diffusion with Individual Preferences

**ZH** C.8 用个体偏好微调 Stable Diffusion

**EN** To align Stable Diffusion to users’ visual preferences, we conducted experiments involving fine-tuning the model based on each individual’s preferences. We used the CLIP similarity score in this experiment, comparing Stable Diffusion-generated outputs for each user against their specified visual preference text to serve as a reward model [40, 4]. In fig. 19, we showcase the outcomes of this approach for four distinct agents, with each row depicting personalized images corresponding to an agent’s visual preference (displayed on the right), and each column containing images generated from the same prompt.

**ZH** 为使 Stable Diffusion 与用户的视觉偏好相对齐，我们进行了基于每个个体偏好微调模型的实验。该实验使用 CLIP 相似度分数，把 Stable Diffusion 为每个用户生成的输出与其指定的视觉偏好文本作比较，以此作为奖励模型 [40, 4]。图 19 展示了该方法在四个不同智能体上的结果：每一行对应一个智能体视觉偏好（显示在右侧）的个性化图像，每一列包含由同一提示词生成的图像。

**EN** While the results of this approach were promising, it exhibited several shortcomings compared to ViPer. Notably, this method is quite expensive due to the necessity of tuning Stable Diffusion for each user. Moreover, it’s sensitive to over-optimization (reward-hacking)[4], resulting in loss of diversity and collapsing as training steps increase. In severe instances, the tuned model disregards input prompts entirely, only to output the same high-reward images. In milder cases, it generates the same facial features, textures, or extreme patterns, resulting in lower-quality images. Additionally, this method may lead to certain visual attributes being overlooked in favor of emphasizing those that yield higher scores from the reward model.

**ZH** 虽然该方法的结果颇有前景，但相较 ViPer 仍存在若干不足。显著的一点是，该方法成本高昂，因为必须为每个用户调优 Stable Diffusion；此外，它对过度优化（奖励黑客）[4] 很敏感，会导致多样性丧失，并随训练步数增加而坍缩。在严重情况下，调优后的模型完全无视输入提示词，只输出同样的一批高奖励图像；在较轻的情况下，它生成相同的面部特征、纹理或极端图案，导致图像质量下降。此外，该方法还可能导致某些视觉属性被忽略，转而强调那些能从奖励模型获得更高分数的属性。

<!-- [原子块 · img]  -->

**EN** Figure 19: In this experiment, we fine-tune Stable Diffusion on each agent’s visual preferences using the CLIP similarity score for the generated images at each step and the visual preference texts. Note how, for each agent, the results align with the visual preference texts shown at right.

**ZH** 图 19：在该实验中，我们用每一步生成图像与视觉偏好文本之间的 CLIP 相似度分数，在每个智能体的视觉偏好上微调 Stable Diffusion。注意对每个智能体，结果都与右侧所示的视觉偏好文本相对齐。

**EN** Appendix D Broader Impact

**ZH** 附录 D 更广泛的影响

**EN** Visual preferences vary widely based on personal experiences and backgrounds. However, current generative models often fail to capture this diversity due to limited training data, resulting in generic outputs. For example, prompts like nostalgia may lean towards Western aesthetics, love often depicts heterosexual monogamous couples, religion incorporates Christian symbols, and human may exclude minority races. Our method addresses these limitations by allowing users to express their preferences thoroughly and in various concepts. In our user tests, some participants favored Queer art and depicted gender nonconforming roles, highlighting the need for more inclusive representation in generative models. Our approach easily incorporates these preferences without requiring additional training data or constant prompt tuning from individuals. Some of these samples are shown for different individuals in fig. 20.

**ZH** 视觉偏好因个人经历与背景而差异巨大。然而，当前的生成模型常因训练数据有限而无法捕捉这种多样性，导致输出趋于同质。例如，“怀旧”这类提示词可能偏向西方美学，“爱”常描绘异性恋一夫一妻伴侣，“宗教”融入基督教符号，而“人”可能排除少数族裔。本文方法通过让用户充分表达自己在各种概念上的偏好来化解这些局限。在我们的用户测试中，一些参与者偏爱酷儿艺术，并描绘性别不符常规的角色，凸显了生成模型中更具包容性的表征的必要性。本文方法能轻松纳入这些偏好，无需额外训练数据，也无需个体不断调整提示词。图 20 展示了不同个体的部分此类样本。

<!-- [原子块 · img]  -->

**EN** Figure 20: We present the non-personalized (base) results of standard Stable Diffusion in the top row. The bottom row displays personalized samples generating the same concepts for different users. While standard Stable Diffusion often discards diversity due to its training data, our method provides individuals with the opportunity to express themselves and their experiences, which are reflected in their visual preferences.

**ZH** 图 20：上排展示标准 Stable Diffusion 的非个性化（基线）结果。下排展示为不同用户生成相同概念的个性化样本。标准 Stable Diffusion 常因训练数据而丢失多样性，而我们的方法为个体提供了表达自身与其经历的机会，这些都反映在他们的视觉偏好中。

**EN** Appendix E Human Subjects Data

**ZH** 附录 E 人类受试者数据

<!-- [原子块 · img]  -->

**EN** Figure 21: We present the user’s ranking in Fig. 6 of the main paper. For each prompt, the user ranked the images based on their preference. They consistently preferred ViPer over other baselines. Note how the user’s rankings for different baselines align with the average scores of metric ⟦SLOT_102⟧.

**ZH** 图 21：我们展示正文图 6 中用户的排序。对每个提示词，用户按自身偏好对图像排序，且始终更偏好 ViPer 而非其他基线。注意用户对不同基线的排序与指标 ⟦SLOT_102⟧ 的平均分数一致。

**EN** We only use human subjects to evaluate the accuracy of our method and its alignment with actual human preferences. This data contains no identifiable information, and whenever an annotation or a part of a user’s data was solicited, their consent was requested. In table 6, we show the visual preferences of different individuals shown in Fig. 4 of the main paper. The user’s ranking in Fig. 6 of the main paper is presented in fig. 21.

**ZH** 我们仅用人类受试者来评估本文方法的准确性及其与真实人类偏好的一致性。该数据不含任何可识别信息；每当征集标注或用户数据的一部分时，都征得了其同意。表 6 给出正文图 4 中不同个体的视觉偏好。正文图 6 中用户的排序见图 21。

**EN** Table 6: Visual preferences of different users shown in Fig. 4 of the main paper.

**ZH** 表 6：正文图 4 中不同用户的视觉偏好。

**EN** User Likes Dislikes 1 Dark, Edgy, Detailed, Busy Composition, Eye Symbolism, Eerie, Creepy, Soft Brushstrokes, Raw, Unsettling, Surrealism, Chiaroscuro Lighting, Monochromatic, Ominous, Symbolic, Horror, Grey Colors, Illusory, Distorted Perspective, Dramatic, Theatrical, Fluid Lines, Desaturated, Classic Contemporary Abstraction, Cheerful Colors, Colorful, Cartoonish, Anime, Manga, Basic, Hyper-realistic, Minimalism, Bright, Flat, Cubism, Repetitive Patterns, Pops of Color, Vibrant Hues, Art Deco, De Stijl, Pixel Art 2 Realism, Representational, Vibrant, Lighter Colors, Bright, Light and Vivid Shades, Detailed, Cheerful, Positive, Uplifting, Soft, Natural Elements, Organic, Atmospheric Perspective, Hopeful, Harmony, Figure-Ground Relationship, Open Space Composition, Dynamic, Colored Pencil Melancholic, Gore, Muted Colors, Dark Themes, Monochromatic, Graffiti, Bad Painting, Abstract, Ambiguous, Artificial Hues, Grayscale, Fog Lighting, Collage, Linocut, Woodcut, Cyanotype Photography, Black and White, Harsh Lighting 3 Psychological and Emotional Depth, Queer Art, Sketch Lines, Dark Themes, Magical, Gloomy, Melancholy, Various Color Palettes, Eerie Vibes, Melancholic, Hand-drawn Textures, Dramatic Lighting, Storytelling, Gothic, Surrealism, Expressionism, Fantastical Elements, Somber Colors, Complex Composition, Innovative, Intricacy, Wonder, Fluid, Freehand Lines, Purples and Blues Realism, Cheerful Colors, Vibrant, Minimalism, Contemporary Abstract, Yellow Hues, Direct Lighting, Monochromatic, Black and white, Grayscale, Static, Lyrical Abstraction, Art Informel, Naive, Rough Texture, Strict, Straight and Thin Lines, Photography, 3D 4 Minimalist, Abstract, Simple Compositions, Room for Interpretation, Limited Color Palettes, Flat, Subtlety, Open Spaces, Muted Colors, Desaturated Palettes, Monochromatic, Complementary Colors, Aqueous Texture, Washed Out, Soothing, Subtle Texture, Contemporary Abstraction, Buttercream Hues, Harmonious, Compressed, Measured Detailed, Busy Composition, Vibrant Colors, Realism, Baroque, Neo-Impressionism, Vivid, Complex, Intricate details, Mechanical Lines, High Contrast, Chaotic, Maximalist Juxtaposition

**ZH** 用户 喜欢 不喜欢 1 暗色调、前卫、细节丰富、繁复构图、眼睛符号、诡异、惊悚、柔和笔触、粗粝、不安、超现实主义、明暗对照光照、单色、不祥、象征性、恐怖、灰色调、幻象感、扭曲透视、戏剧性、舞台感、流畅线条、低饱和、古典 当代抽象、明快色彩、多彩、卡通感、动画、漫画、基础、超写实、极简主义、明亮、平面、立体主义、重复图案、点状亮色、鲜艳色调、装饰艺术、风格派、像素艺术 2 写实主义、具象、鲜艳、浅色调、明亮、明快色调、细节丰富、欢快、积极、振奋、柔和、自然元素、有机、空气透视、充满希望、和谐、图形-背景关系、开放空间构图、动态、彩色铅笔 忧郁、血腥、柔和色彩、暗色主题、单色、涂鸦、拙劣绘画、抽象、含混、人工色调、灰度、雾光、拼贴、油毡版画、木刻、蓝晒摄影、黑白、硬光 3 心理与情感深度、酷儿艺术、素描线条、暗色主题、魔幻、阴郁、忧郁、多样色调、诡异氛围、忧郁感、手绘质感、戏剧性光照、叙事性、哥特、超现实主义、表现主义、奇幻元素、阴沉色彩、复杂构图、创新、繁复、奇妙、流畅、徒手线条、紫与蓝 写实主义、明快色彩、鲜艳、极简主义、当代抽象、黄色调、直射光、单色、黑白、灰度、静态、抒情抽象、非定型艺术、稚拙、粗糙质感、严谨、平直细线、摄影、3D 4 极简主义、抽象、简约构图、留有解读空间、有限色调、平面、微妙、留白、柔和色彩、低饱和色调、单色、互补色、水感质感、褪色、舒缓、微妙质感、当代抽象、奶油色调、和谐、紧凑、节制 细节丰富、繁复构图、鲜艳色彩、写实主义、巴洛克、新印象主义、生动、复杂、繁复细节、机械线条、高对比、混乱、极简主义并置
