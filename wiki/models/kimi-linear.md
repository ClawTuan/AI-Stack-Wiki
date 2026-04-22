---
title: "Kimi Linear"
date: 2026-04-22
tags: ["model", "llm", "moe", "transformer", "attention-mechanism"]
aliases: ["Kimi Linear LLM"]
---

## L0：模型概览

Kimi Linear是由Kimi Team开发的大规模混合专家(MoE)Transformer语言模型，采用了先进的注意力机制和残差连接设计，在保持高效训练和推理的同时，实现了优异的下游任务性能。

## L1：架构设计

### 核心架构

Kimi Linear遵循Moonlight/DeepSeek-V3设计理念，主要特点包括：

1. **混合专家结构** (Mixture-of-Experts)
   - 总参数：48B
   - 激活参数：3B
   - 专家数量：256个路由专家 + 1个共享专家
   - 每层使用：8个激活专家

2. **注意力机制**
   - Kimi Delta Attention (KDA)：高效的注意力实现
   - Multi-Head Latent Attention (MLA)：潜在空间注意力
   - 比例：3个KDA层 : 1个MLA层交错排列
   - 无位置编码(NoPE)设计，支持上下文扩展

3. **层结构**
   - 27个Transformer块（共54层）
   - 每层后接MoE前馈网络
   - 集成Attention Residuals (AttnRes)作为残差连接机制

### 训练配置

- 预训练语料：1.4T tokens
- 训练阶段：
  - 第一阶段：1T tokens，4096token上下文窗口
  - 第二阶段：≈400B高质量tokens
  - 扩展阶段：32K token上下文窗口
- 优化器：Muon optimizer
- 学习率调度：WSD (Warmup–Stable–Decay)
- 全局批次大小：8M tokens

## L2：技术创新

### Attention Residuals集成

Kimi Linear创新性地集成了Attention Residuals (AttnRes)机制：

1. **Block AttnRes实现**
   - 每6层分为一个块，共9个块
   - 块级表示+token嵌入作为深度注意力源
   - 每个块内使用标准残差连接
   - 块间使用注意力机制选择性聚合

2. **系统优化**
   - 交叉阶段缓存：减少流水线并行通信
   - 两阶段计算：提升推理效率
   - 内存高效预填充：支持长上下文

3. **训练优势**
   - 控制隐藏状态随深度的增长
   - 使梯度分布更加均匀
   - 解决PreNorm信息稀释问题
   - 提升深度信息交互能力

### 性能改进

集成AttnRes后，Kimi Linear在以下方面表现提升：

| 任务类型 | 代表性基准 | 性能提升 |
|----------|------------|----------|
| 多步推理 | GPQA-Diamond | +7.5 |
| 数学推理 | Math | +3.6 |
| 代码生成 | HumanEval | +3.1 |
| 知识理解 | MMLU | +1.1 |
| 中文理解 | C-Eval | +2.9 |

## 应用场景

- 复杂多步推理任务
- 长上下文建模
- 代码生成与理解
- 数学问题求解
- 多语言理解与生成

## 技术规格

| 参数 | 配置 |
|------|------|
| 总参数 | 48B |
| 激活参数 | 3B |
| Transformer块 | 27个 |
| 总层数 | 54层 |
| 专家数量 | 256个路由专家 + 1个共享专家 |
| 每层激活专家 | 8个 |
| 注意力层比例 | 3个KDA : 1个MLA |
| AttnRes块大小 | 6层/块 |
| 预训练语料 | 1.4T tokens |
| 最大上下文 | 32K tokens |

## 与其他模型对比

- **与标准Transformer对比**：采用MoE结构和AttnRes机制，参数效率更高
- **与DeepSeek-V3对比**：共享基础设计，但集成了AttnRes优化
- **与Moonlight对比**：遵循类似架构理念，但规模更大

## 来源

- 来源：raw/Attention_Residuals.pdf