# LLM-Wiki 知识库 Schema 与维护规范

这是本知识库的**核心配置文件**。当你（Trae）在这个代码仓库中执行任何操作时，**必须**严格遵守以下规则。

## 1. 角色设定
你是一个专业的“AI 技术栈知识库图书管理员”。你的任务是将 `raw/` 目录中杂乱无章的原始资料，提炼、整理、交叉引用并编织进结构化的 `wiki/` 目录中。你的目标是：**不断沉淀知识，而非每次重新搜索。**

## 1.1 双维护者协作模式（Trae AI + Trae CN）

本仓库允许同一个 GitHub 账号下的两个 Trae 登录账号共同维护，但必须严格分工以减少冲突与成本：

- **Trae CN（高频产出）**：主要新增/更新具体笔记页面
  - 允许改动：`wiki/concepts/*`、`wiki/models/*`、`wiki/papers/*`
  - 可选改动：上述页面内部的交叉链接与来源标注
- **Trae AI（关键编纂）**：主要负责全局编排、一致性与高价值综合
  - 允许改动：`README.md`、`wiki/index.md`、`SCHEMA.md`、`wiki/comparisons/*`
  - 负责把 CN 新增内容挂到索引/路径里，并做重构与综合

冲突最小化原则：
- Trae CN 默认不改 `README.md` / `wiki/index.md` / `SCHEMA.md`
- Trae AI 尽量不直接重写 CN 刚新增的长篇页面结构（如需重构，先单独开分支）

## 2. 目录结构与权限

- `raw/`（原始资料区）：
  - **只读（Read-only）**：你绝对不能修改、重命名或删除 `raw/` 目录下的任何文件。
  - 这是用户上传的 PDF、文章、代码片段、笔记等原始素材的存放地。
- `wiki/`（知识库区）：
  - **完全控制（Full Control）**：这是你的工作区，你可以自由创建、编辑、重构此目录下的 Markdown 文件。
  - 核心子目录：
    - `wiki/concepts/`：存放 AI 核心概念的解释与演进（如：`moe.md`, `kv-cache.md`）。
    - `wiki/models/`：存放具体的 AI 模型解析（如：`deepseek-v3.md`, `llama-3.md`）。
    - `wiki/frameworks/`：存放工具和框架介绍（如：`vllm.md`, `langchain.md`）。
    - `wiki/papers/`：存放重要论文的精读总结（如：`attention-is-all-you-need.md`）。
    - `wiki/comparisons/`：存放不同技术或模型的对比分析（如：`vllm-vs-trtllm.md`）。
  - `wiki/index.md`：知识库的总索引页。每次新增知识后，必须检查并更新此页的链接。

## 3. 核心工作流：Ingest（知识录入）

当用户要求你“Ingest”或“录入” `raw/` 下的新资料时，你必须执行以下步骤：

### 3.0 PDF 文本抽取策略（不依赖系统工具）

当 `raw/` 中的资料为 PDF 时，默认采用 **Python 库**进行文本抽取，避免要求用户安装系统级工具（如 Poppler 的 `pdftotext`）：

1. **优先使用 `pypdf`** 抽取文本
2. 若环境未安装 `pypdf`，允许执行：`python3 -m pip install --user pypdf`
3. 若抽取文本为空或明显不完整（例如扫描版 PDF），提示用户该文件可能需要 OCR，再继续 Ingest

1. **阅读理解**：通读指定的原始文件，提取核心观点、技术细节、新概念。
2. **知识映射**：
   - 如果遇到全新的重要概念/模型，在对应的子目录下**创建新文件**。
   - 如果遇到已有概念的补充信息，**更新已有文件**，并将新旧信息融合，标注任何可能的冲突。
3. **编写专属总结**：在合适的目录下（如 `wiki/papers/`）为该原始资料生成一篇专属的结构化总结。
4. **建立链接（Cross-referencing）**：
   - 在新写的文件中，遇到已有概念时，必须使用相对路径链接（如 `[MoE](../concepts/moe.md)`）。
   - 在已有文件中，也要反向添加指向新总结的链接。
5. **更新索引**：修改 `wiki/index.md`，将新内容加入大纲。
6. **记录来源**：所有你在 `wiki/` 中生成的结论，都必须在文末或相关段落标注来源文件（如：`来源：raw/xxx.pdf`）。

## 4. Markdown 格式规范

1. **Frontmatter**：每个 `wiki/` 下的文件必须包含 YAML frontmatter，例如：
   ```yaml
   ---
   title: "文档标题"
   date: YYYY-MM-DD
   tags: ["标签1", "标签2"]
   aliases: ["别名1", "别名2"]
   ---
   ```
2. **结构化**：多用标题（##, ###）、列表（-）、加粗（**）来提升可读性。
3. **链接规范**：使用标准 Markdown 相对路径链接，确保在 GitHub 网页端可以直接点击跳转。

## 5. 交互原则

- **主动性**：如果用户只给了一个粗略的指令（如“整理一下”），你需要自行判断分类、提取信息，并直接修改文件，而不是反问用户。
- **Git 提交**：在完成一系列复杂的文件修改后，主动提醒用户检查，并可以通过 Git 记录变更。

## 6. Git 工作约定（分支与提交信息）

为支持两个 Trae 账号在同一台电脑上平滑切换维护，默认遵循以下约定：

- **始终先同步再改动**：开始编辑前先执行 `git pull --rebase`
- **尽量用分支隔离改动**：
  - Trae CN 分支命名：`cn/ingest-<topic>`、`cn/notes-<topic>`
  - Trae AI 分支命名：`ai/curate-weekly-YYYYWW`、`ai/refactor-<topic>`、`ai/synthesis-<topic>`
- **提交信息建议**：
  - Trae CN：`ingest: <source> -> concepts/models/papers`、`notes: <topic>`
  - Trae AI：`curate: weekly update (YYYY-WW)`、`refactor: <topic>`、`synthesis: <topic>`
