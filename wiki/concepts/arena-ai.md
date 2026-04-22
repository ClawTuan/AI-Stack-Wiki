---
title: "Arena.AI"
date: 2026-04-22
tags: ["evaluation", "benchmark", "human-preference", "elo"]
aliases: ["Arena", "LMArena (video)"]
---

## L0 入门科普

Arena.AI 是一种基于真实用户偏好投票的评测平台：用户对比两组匿名模型输出，投票更喜欢哪一个，系统据此生成类似 Elo 的排行榜。

## L1 工程落地

**为什么有用**
- 比起单一自动指标，偏好投票能更整体地反映视觉质量、运动真实感、时间一致性、提示词遵循等综合体验

**解读注意**
- Elo 反映的是“相对偏好”，与具体场景分布强相关
- 需要结合结构化基准（如 [SeedVideoBench 2.0](seedvideobench-2.0.md)）一起看，避免只追榜单

## 相关条目

- [Seedance 2.0](../models/seedance-2.0.md)

## 来源

- 来源：raw/Seedance 2.0.pdf
