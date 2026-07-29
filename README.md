# 学习笔记 · LLM Wiki

一个按 Andrej Karpathy 的 **LLM Wiki** 模式运作的个人知识库。

## 结构

- **`AGENTS.md`** — 维护契约(AI 如何维护本库)。开始工作前先读它。
- **`index.md`** — 知识点唤醒索引。快速唤醒"我学过什么"。
- **`log.md`** — 流水账。
- **`raw/`** — 原始资料(只读):B站转写、文章原文、AI 对话存档。
- **`assets/`** — 新库图片池。
- **`wiki/`** — AI 沉淀的知识,按领域分子目录。
- **`archive/`** — 旧笔记整体归档,原样封存,按需唤起。
- **`learning/`** — 学习计划(过程性产物,非沉淀知识)。

> **工具不在本库**:维护工具在独立开源仓库 [kg-wiki-skills](https://github.com/KingGloose/kg-wiki-skills),
> 全局注册后 AI 在任何目录都能调用。本库只放知识。

## 迁移到新电脑

本库只含知识,工具在独立仓库。迁移到新机器后:
1. clone 工具仓库并安装:
   ```bash
   git clone https://github.com/KingGloose/kg-wiki-skills.git ~/个人代码/kg-wiki-skills
   cd ~/个人代码/kg-wiki-skills && bash install.sh
   ```
2. 建软链(**用相对路径**,跨机器更稳,前提是两仓库同级):
   ```bash
   cd <本库> && ln -s ../个人代码/kg-wiki-skills skills
   ```
3. 告诉 skills 本库在哪(任选一种):
   - 写 `~/.config/kg-wiki/config.json`: `{"vault": "/path/to/本库"}`
   - 或 `export KG_VAULT=/path/to/本库`
   - 或在本库目录内执行命令(自动向上查找)

## 理念

AI 时代,知识库的价值是**唤醒**(知道知识点存在,能判断 AI 的回答)+ **沉淀**(只存 AI 给不出的:个人判断、项目上下文、踩坑)。存量整体归档,向前建新库,价值靠使用浮现。

详见 `AGENTS.md`。
