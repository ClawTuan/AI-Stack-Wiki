# AI-Stack-Wiki

A Trae-powered, GitHub-native LLM-Wiki：把 `raw/` 原始资料“编译”为可持续积累、相互链接的 Markdown 知识库。

灵感来自 Andrej Karpathy 的 LLM-Wiki 思路：与其每次提问都临时检索（RAG）并重新拼装，不如让知识在仓库里持续沉淀、演进、可追溯。

- 参考：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## 本周更新

- （模板）建议每周滚动更新本段，保持 5–12 条即可
- **Trae CN（高频笔记产出）**
  - 示例：新增 [Seedance 2.0](./wiki/models/seedance-2.0.md)，补齐 [SeedVideoBench 2.0](./wiki/concepts/seedvideobench-2.0.md) 与 [Arena.AI](./wiki/concepts/arena-ai.md)
- **Trae AI（关键编纂与路径整理）**
  - 示例：将本周新增内容归档到精选路径，并更新 [wiki/index.md](./wiki/index.md)

## 精选路径

- **从 0 到 1：看懂一个多模态生成模型的“能力边界”**
  - [Seedance 2.0（模型页）](./wiki/models/seedance-2.0.md)
  - [SeedVideoBench 2.0（基准与指标）](./wiki/concepts/seedvideobench-2.0.md)
  - [Arena.AI（偏好投票与 Elo）](./wiki/concepts/arena-ai.md)
  - [Seedance 2.0（论文精读）](./wiki/papers/seedance-2.0.md)
- **写作/学习模板：入门→落地→前沿三层结构**
  - 任何页面都建议按 L0/L1/L2 三段组织，细节见 [SCHEMA.md](./SCHEMA.md)

## 推荐阅读

- 入口索引：[wiki/index.md](./wiki/index.md)
- 多模态视频生成样例：
  - [Seedance 2.0（模型）](./wiki/models/seedance-2.0.md)
  - [Seedance 2.0（论文）](./wiki/papers/seedance-2.0.md)
- 评测与基准：
  - [SeedVideoBench 2.0](./wiki/concepts/seedvideobench-2.0.md)
  - [Arena.AI](./wiki/concepts/arena-ai.md)

## 核心理念

- **Raw Sources（只读）**：`raw/` 存放原始资料（论文、文章、报告、笔记等），作为事实来源，不被修改。
- **Wiki（可演进）**：`wiki/` 存放结构化的 Markdown 页面（概念、模型、工具、论文精读、对比），由 Trae 维护并持续更新。
- **Schema（规则）**：用一份明确的规范约束维护方式，保证新增/重构不失控、链接不断裂、来源可追溯。

本仓库的 Schema 文件在：[SCHEMA.md](./SCHEMA.md)  
知识库入口在：[wiki/index.md](./wiki/index.md)

## 目录结构

```
raw/                    # 原始资料（建议仅本地保存/私有，公开仓库默认忽略）
wiki/
  index.md              # 总索引（阅读入口）
  concepts/             # 概念库（术语、机制、指标、基准等）
  models/               # 模型库（架构、能力边界、评测、推理要点等）
  frameworks/           # 框架/工具（训练、推理、部署、Agent 等）
  papers/               # 论文/技术报告精读总结
  comparisons/          # 对比分析（方案选型、路线对照、优缺点）
SCHEMA.md               # 维护规范（Trae 执行准则）
```

## 用 Trae 的工作流（推荐）

### 1) Ingest：录入一份新资料

1. 把文件放到 `raw/`（例如：`raw/some-paper.pdf`）
2. 在 Trae 里对仓库发出指令：  
   - “Ingest `raw/some-paper.pdf`”
   - 或 “录入 `raw/some-paper.pdf`，并更新索引与相关概念页”

Trae 会：
- 生成该资料的结构化总结页（通常在 `wiki/papers/` 或合适的分类目录）
- 发现新概念/新基准时创建概念页，遇到已有条目则融合更新
- 建立双向链接（cross-references）
- 更新 [wiki/index.md](./wiki/index.md)
- 在每个结论附近或文末标注来源（例如：`来源：raw/xxx.pdf`）

### 2) Query / Synthesis：提问与综合

你可以让 Trae 基于 `wiki/` 直接综合，而不是重新上网搜碎片：
- “总结目前视频生成的主流评测基准与各自关注点”
- “对比 vLLM vs TensorRT-LLM：适用场景与坑位”
- “把本仓库里关于 Agent 的内容整理成一条入门→落地→前沿的阅读路径”

### 3) Refactor：重构知识库

当页面太长或结构混乱时：
- “把 `wiki/concepts/xxx.md` 拆分并修复所有引用”
- “统一全库 Frontmatter / tags，并清理重复概念”

## 不限于 Trae：通用 LLM Agent 工作流

这个仓库的关键不是某个特定工具，而是 **“Raw → Wiki → Schema”** 这套可积累的维护范式。只要你的 Agent 能做到“读仓库、改文件、跑 git”，就可以接入（例如 Claude Code、OpenAI Codex 等）。

**通用约束**
- 维护时以 [SCHEMA.md](./SCHEMA.md) 为最高优先级规则：`raw/` 只读；`wiki/` 可重构；结论必须标注来源；链接用相对路径。
- 默认不上传 `raw/`：公开仓库只沉淀 `wiki/` 的结构化总结与交叉引用。

**通用提示词（可直接复制到任意 Agent）**
- “阅读 `SCHEMA.md`，然后 Ingest `raw/xxx.pdf`：生成/更新相关概念页与模型页，更新 `wiki/index.md`，并在页面中标注来源。”
- “基于 `wiki/` 回答：……（要求给出引用到具体页面的链接）”

## 写作约定（面向公开分享）

每个 `wiki/` 页面建议同时覆盖三层读者需求：
- **L0 入门科普**：一句话定义 + 关键点（读完能复述）
- **L1 工程落地**：场景、选型、实践步骤、常见坑（读完能用）
- **L2 研究前沿**：最新方向、关键参考、开放问题、个人判断（读完能跟进）

## 公开仓库注意事项

- `raw/` 目录在公开仓库默认忽略（见 `.gitignore`），避免误提交带版权或隐私的原文资料。
- 建议在 `wiki/` 里沉淀你的总结与结构化理解，并用链接/引用信息标注来源。

## License

本仓库的“内容”（例如 `wiki/` 下的 Markdown 笔记）采用 CC BY 4.0，详见仓库根目录的 [LICENSE](./LICENSE)。
