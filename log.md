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

## [2026-07-25] ingest | 泛域名全链路系列(7 篇)

- 讨论 `文档内容/前端代理、泛域名思考和分析.doc`、`文档内容/新OA接入泛域名处理.doc`(两篇 Confluence MHTML 导出),外加此前几张 webpack/Vite 产物截图(requireEnsure、preloads、window.__dynamic_base__、enforce 顺序)。
- 两篇原文提取清理为纯文字(去 base64 图/Word 噪声),存 `raw/泛域名-前端代理思考和分析-原文.md`、`raw/泛域名-新OA接入处理-原文.md` 留档。
- 主人决策:不聚焦转转内部规范,把偏通用的知识(DNS 泛解析/通配符证书/CORS/Cookie 跨子域等自己了解不多的)也当学习材料写进来;从 26 个候选收敛到 7 篇;前端处理合成一篇长文不拆散;砍掉机器访问链路/后端接入/专题。
- 新建 `wiki/网络/` 领域目录,产出 6 篇:泛域名与相关概念辨析、DNS 泛解析与查询链路、通配符 HTTPS 证书、nginx 泛域名转发、同源策略与 CORS、Cookie 跨子域与跨窗口通信;`wiki/前端/` 产出重头篇「前端运行时动态 base 完全指南」(webpack `__webpack_public_path__`/`.p`/`requireEnsure` vs Vite 三方案 vs vite-plugin-dynamic-base 源码级原理)。
- 联网核对 vite-plugin-dynamic-base(README 默认配置 publicPath/transformIndexHtml、base=/__dynamic_base__/、AST 重构 PR#23、兼容 legacy/pwa)、webpack `__webpack_public_path__`→`.p`、vite plugin-legacy 机制,确保源码细节准确。
- 七篇按系列首尾互建双链(概念→DNS→证书→nginx→前端动态base→CORS→Cookie),动态base 页与 [[JS 模块系统与模块缓存单例]] 建双链。
- index.md:01 基础新增「网络/泛域名系列」条目,03 前端工程化新增「运行时动态 base」条目。
- 定位说明:这些内容多为通用知识,按 AGENTS.md 本该只进 index 唤醒;但主人明确表示想把这些当学习材料细化成页,故成文并注明来源上下文。

## [2026-07-26] setup+ingest | 新建 bilibili-ingest / wechat-ingest skill + 首篇公众号沉淀

- **背景**:主人空余时间少,想借助 AI 消化平时收藏的视频和公众号文章,沉淀进知识库。
- **调研**:B 站生态成熟(bilibili-api-python + yt-dlp + Whisper);公众号单篇公开文章无需登录,难点只在图片防盗链(Referer)。
- **新建 `skills/bilibili-ingest/`**:扫码登录(login.py 生成二维码图片扫)、拉稍后再看/收藏(list_videos.py)、抓 CC/AI 字幕(get_transcript.py,Whisper 兜底暂不做)。跨平台(Mac/WSL/Windows),cookie 走 .env。踩坑:裸装 bilibili-api-python 不带 HTTP client,须装 curl_cffi 并注册。已验证读到稍后再看 604 条、抓到 27060 字 AI 字幕。
- **新建 `skills/wechat-ingest/`**:wechat_to_md.py 抓公众号单篇文章,curl_cffi 抓 HTML + bs4 提正文 + markdownify 转 md + 图片带 Referer 下载本地。踩坑:pi 内置 fetch_content 对公众号提取失败(Readability 没吃下、Gemini 兜底无 key),故需专门脚本;公众号真实名在 nickname=htmlDecode() 而非 og:site_name;原文分隔符渲染出空标题需过滤。
- **首篇沉淀(详细蒸馏)**:《AI Native 时代——研发组织何去何从》(许晓斌,阿里技术,2026-05-08)。
  - 原文抓取存 `raw/wx-2026-05-08-AI-Native时代研发组织.md`(正文 11146 字),4 张图存 `assets/`(架构图 A 档保留,2 张 gif C 档忽略)。
  - 判断:特定作者综合多信源的独特框架+内部案例数据,AI 给不出 → 写 wiki。
  - 新建 `wiki/AI/` 领域目录,产出 `AI Native 时代的研发组织.md`(详细蒸馏:论证脉络 1.2、管理塌缩与三柱 1.3、Death of ego 边界 1.4、三案例、转型代价、开放问题、十条判断、概念速查)。全文标注 [文章观点]/[信源]/[AI 补充] 区分来源,顶部注明"这是别人观点的蒸馏,非主人原创判断"。
  - 架构图转成文字 ASCII 图避免知识困在图里,同时保留 Obsidian `![[assets/...]]` 引用。
  - 双链:AI 领域尚无兄弟页,Harness/DeepAgents 只在 index 有关键词、无独立页,故不建假双链,改文字呼应,留待后续补。
  - index.md 08 AI 新增条目。
