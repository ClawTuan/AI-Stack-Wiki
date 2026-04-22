---
title: "Seedance 2.0：Advancing Video Generation for World Complexity"
date: 2026-04-22
tags: ["paper", "video-generation", "multimodal", "audio-video", "evaluation", "bytedance-seed"]
aliases: ["Seedance 2.0 paper", "Advancing Video Generation for World Complexity"]
---

## 一句话总结

Seedance 2.0 将视频生成从“短视频片段 + 弱可控”推进到“原生多模态（文/图/音/视频）+ 强可控（参考/编辑/延展/组合任务）”，并用结构化基准与真实用户偏好共同验证其在创作工作流中的可用性。

## 核心信息

- 机构：ByteDance Seed
- 发布时间（文中描述）：2026 年 2 月在中国发布
- 模态支持：文本、图像、音频、视频
- 目标：提升生成质量与多模态可控性，面向大规模创作引擎平台

相关实体页：[Seedance 2.0](../models/seedance-2.0.md)

## 评测与结果摘要

### SeedVideoBench 2.0

评测框架见：[SeedVideoBench 2.0](../concepts/seedvideobench-2.0.md)

文中强调两点：
- 评测从“单纯生成质量”扩展到“多模态任务跟随 + 参考/编辑/延展能力覆盖”，并把能力边界显式化
- 版本 2.0 在视频侧增加更细的叙事质量指标（例如镜头语言、情节设计、风格审美一致性）

### Arena.AI（偏好对比，Elo 排行）

平台机制见：[Arena.AI](../concepts/arena-ai.md)

文中给出的结论要点：
- Dreamina Seedance 2.0 720p 在 Arena.AI 的 Text-to-Video 与 Image-to-Video 两个榜单均排名 #1
- Elo：T2V 1450（±15），I2V 1449（±11）

## 可控性能力（文中列举）

- 参考与编辑：主体、运动、风格、特效、音频内容等
- 延展：时间线前向/后向的无缝扩展
- 组合任务：更贴近真实生产流程的“参考 + 编辑”等联动任务

## 来源

- 来源：raw/Seedance 2.0.pdf
