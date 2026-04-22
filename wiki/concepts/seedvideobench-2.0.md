---
title: "SeedVideoBench 2.0"
date: 2026-04-22
tags: ["evaluation", "benchmark", "video-generation", "multimodal"]
aliases: ["SeedVideoBench2.0", "SeedVideoBench v2"]
---

## L0 入门科普

SeedVideoBench 2.0 是一个面向视频生成/多模态视频编辑能力的评测框架，用来系统衡量“生成质量 + 指令遵循 + 多模态参考/编辑/延展能力”。

## L1 工程落地

**评测拆分**
- 区分客观与主观两条轨道：客观指标（如运动稳定性）可用自动化管线；主观指标（如美学）可用盲测专家评审

**多模态任务覆盖（让能力边界更显式）**
- Reference：主体 / 运动 / 视觉特效 / 风格 参考生成
- Editing：主体 / 风格 / 场景 / 音频内容 编辑
- Extension：剧情续写与无缝延展（时间线前向/后向）
- Combination：组合任务，贴近真实工作流（例如“参考 + 编辑”联动）

**一致性指标（Consistency）**
- Reference alignment：生成内容与参考输入的贴合程度
- Editing consistency：编辑过程中非编辑区域的保真程度

## L2 研究前沿

**叙事质量（Narrative Quality）**
- SeedVideoBench 2.0 在既有维度之外，引入更细的叙事质量相关指标，用于衡量整体叙事是否连贯、镜头语言是否合理、风格审美是否统一等更主观但更贴近“可用成片”的维度

## 相关条目

- [Arena.AI](arena-ai.md)
- [Seedance 2.0](../models/seedance-2.0.md)

## 来源

- 来源：raw/Seedance 2.0.pdf
