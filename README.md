# AI-Stack-Wiki

A Trae-powered, GitHub-native LLM-Wiki：把 `raw/` 原始资料“编译”为可持续积累、相互链接的 Markdown 知识库。

灵感来自 Andrej Karpathy 的 LLM-Wiki 思路：与其每次提问都临时检索（RAG）并重新拼装，不如让知识在仓库里持续沉淀、演进、可追溯。

- 参考：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

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

## 写作约定（面向公开分享）

每个 `wiki/` 页面建议同时覆盖三层读者需求：
- **L0 入门科普**：一句话定义 + 关键点（读完能复述）
- **L1 工程落地**：场景、选型、实践步骤、常见坑（读完能用）
- **L2 研究前沿**：最新方向、关键参考、开放问题、个人判断（读完能跟进）

## 公开仓库注意事项

- `raw/` 目录在公开仓库默认忽略（见 `.gitignore`），避免误提交带版权或隐私的原文资料。
- 建议在 `wiki/` 里沉淀你的总结与结构化理解，并用链接/引用信息标注来源。

## License

默认不包含 License。若你希望鼓励转载传播且保留署名，常见做法是为“内容”采用 CC BY 4.0，并在仓库根目录添加 `LICENSE` 文件进行声明。

