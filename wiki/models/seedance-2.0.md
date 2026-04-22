---
title: "Seedance 2.0"
date: 2026-04-22
tags: ["video-generation", "multimodal", "audio-video", "bytedance-seed"]
aliases: ["Dreamina Seedance 2.0", "Seedance2.0"]
---

## L0 入门科普

Seedance 2.0 是字节跳动 ByteDance Seed 团队发布的多模态音视频生成模型，核心目标是把视频生成从“短片段、弱可控”推进到“强可控、可用于真实创作流程”。

## L1 工程落地

**能力边界（按输入/控制信号）**
- 支持四种输入模态：文本、图像、音频、视频
- 支持多模态参考与编辑：主体控制、运动操控、风格迁移、特效设计、创意生成、视频延展
- 支持单独任务与组合任务（更贴近真实工作流）

**适用场景**
- 需要多源参考（图像/音频/视频参考）并进行局部编辑的创作场景
- 需要“多镜头叙事”与更稳定的跨帧一致性的制作流程

## L2 研究前沿

**范式变化**
- 从“仅评估生成质量”走向“评估可控性与工作流可用性”：强调多模态参考、编辑、延展与组合任务的覆盖

**评测信号**
- 基于 [SeedVideoBench 2.0](../concepts/seedvideobench-2.0.md) 的多维评测框架（含叙事质量子维度）
- 基于 [Arena.AI](../concepts/arena-ai.md) 的真实用户偏好对比（Elo 排行）

## 来源

- 来源：raw/Seedance 2.0.pdf
