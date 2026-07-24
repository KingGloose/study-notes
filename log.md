# Log · 流水账

> append-only。格式:`## [日期] 类型 | 摘要`
> 类型:setup / ingest / query / upgrade / lint
> 查最近几条:`grep "^## \[" log.md | tail -5`

## [2026-07-25] setup | LLM Wiki 改造初始化

- 将全部旧领域笔记 + `00 assets`(6790张图)整体归档至 `archive/`。
- 新建三层结构:`raw/`(原始资料)、`assets/`(新图片池)、`wiki/`(AI 沉淀知识)。
- 新建三个根文件:`AGENTS.md`(维护契约)、`index.md`(知识点唤醒索引)、`log.md`(本文件)。
- `index.md` 扫描 archive 旧笔记标题生成,覆盖 12 个领域的知识点关键词。
- 资产分析:archive/00 assets 共 6789 张图,其中 189 张(41M)未被引用,决定不清理(占比小)。
- 待办:归档后配置 Obsidian 图谱默认过滤 `-path:archive`。
