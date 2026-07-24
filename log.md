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

## [2026-07-25] ingest+query | QuillJs 换行 bug 方案评估

- 讨论 `文档内容/QuillJs换行bug解决方案.doc`(Confluence MHTML 导出)。原文只记了现象 + BrBlot workaround 代码。
- 判断:含个人项目上下文(学堂系统)+ 取舍判断,不是纯通用知识 → 沉淀进 wiki。
- 原始正文清理后存 `raw/QuillJs换行bug解决方案-原文.md`(过滤 base64 图片,保留代码)。
- 新建 `wiki/前端/QuillJs 换行与 embed 光标问题.md`:根因(Quill 用 \n 分块、文档须以 \n 结尾)、原方案 3 个隐患 + create() 漏 return node 的 bug、数据层归一化替代方案(补 \n / clipboard matcher)、选型建议表。
- 顺带把讨论引出的通用知识落成 `wiki/前端/Vue watch 与 Promise 异步.md`(竞态/onCleanup/依赖收集断裂/flush),两页互建双链。
- index.md 新增「富文本/编辑器 · QuillJs」条目,并在 JS 异步条目补 watch 异步关键词。

## [2026-07-25] ingest+upgrade | npm 依赖冲突 + 模块缓存单例(旧笔记升级)

- 讨论 `文档内容/npm依赖冲突问题.doc`(Confluence MHTML)。学堂 antd v4 接入 zant-ui(antd v5)peer dependency 冲突。
- 提取原文 5 张代码截图(A 档知识型)转成文字/代码,存 `raw/npm依赖冲突问题-原文.md`。
- 新建 `wiki/前端/npm 与 pnpm 依赖冲突.md`:peer dependency 原理、理论vs现实(版本不可调和→隔离共存)、三包管理器差异、overrides/resolutions 纠错(npm 不认 resolutions)、NormalModuleReplacementPlugin 按来源分流、决策表。留一个待确认:当时实际用的哪个包管理器。
- 讨论中追到「模块缓存=单例」,发现 archive 旧笔记 `模块化.md` 记过 CJS 缓存机制且正确,但没点破单例结论、缺 ESM 对照。符合 just-in-time 升级条件。
- 升级:蒸馏 `模块化.md`(725行大量截图)为 `wiki/前端/JS 模块系统与模块缓存单例.md`,保留正确的 CJS 机制+补 ESM Module Map/live binding+点破「缓存按路径 key=单例地基」+接到 antd 两份实例案例。旧笔记原文封存不动,升级说明存 `raw/模块化-旧笔记升级说明.md`。
- 两页互建双链(依赖冲突 ↔ 模块单例)。按主人要求,QuillJs 页不建双链(与依赖/模块无关)。
- index.md 新增「JS 模块系统 / 模块缓存=单例」「依赖冲突 / peerDependencies」条目。
