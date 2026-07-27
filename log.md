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

## [2026-07-27] setup | 摄入架构重构:底层库 media-to-text + 统一 venv + 分层摄入契约

- **动因**:讨论多模态摄入(视频/音频/文档)时主人提出关键架构洞察——「素材→文字」应抽成独立底层库,上层各平台 skill 都是它的调用者;同时发现每 skill 一个 .venv 太重(105MB,依赖重叠)。
- **git 清理**:发现 979 个 `.venv` 文件已被追踪并推到 GitHub(gitignore 写在建 venv 之后,对已追踪文件无效,被 Obsidian 自动备份推走)。用 git-filter-repo 重写 393 个提交移除,强推覆盖 main。备份在 /tmp/xuexi-backup(bundle 886MB)。**确认 `.env` 凭证从未被追踪,无泄露**。附带发现:仓库 874MB 里 905MB 是 `archive/00 assets`(6790 张旧图),`.venv` 只是零头,故体积清完基本没变——属正常,archive 是真实资产不动。
- **统一环境**:`skills/.venv`(uv + Python 3.12,1.5GB 共享)替代各 skill 独立 venv;`requirements/` 按功能+平台分 6 个文件(base/doc/bilibili/wechat/asr-mac/asr-linux);新增 `skills/README.md` 作为唯一环境维护点。删除两个旧 venv 和各自的 requirements/gitignore。
- **新建底层库 `skills/media-to-text/`**(editable 安装,`disable-model-invocation`):detect(类型探测) + router(分流) + types(TextResult 契约) + handlers(document/audio)。对外只暴露 `to_text()`。PDF→Docling(含 RapidOCR)、Office→MarkItDown、音视频→ASR(**Mac 自动选 mlx-whisper / Linux 选 faster-whisper**,因 faster-whisper 不支持 Apple MPS)、txt/md→直读。
- **新建 `doc-ingest`**:薄上层,PDF/csv/xlsx/md 全验证。用主人转正材料 PDF(11页 jsPDF 图片型)实测 8226 字符、标题/表格/链接正确还原,二次 30 秒。
- **新建 `xiaoyuzhou-ingest`**:解析 `__NEXT_DATA__` 拿元信息+shownotes(**无需登录**),可选 `--transcribe` 下音频本地转写。实测《#153 AI编程》(2:10:59)shownotes 含完整时间戳大纲;2分钟片段转写 10.3 秒(约12倍实时)。**安全决策**:小宇宙官方逐字稿 API 需鉴权(401)且社区警告 token 抓取可能封号,故一律走本地 ASR。
- **迁移旧 skill**:bilibili/wechat 接入统一 venv(Python 3.12 下回归通过);**补上 bilibili 之前留的 ASR 兜底坑**——`--asr` 走 yt-dlp `-x` 抽音轨 + 调底层库,实测 3 分钟无字幕视频 25 秒完成、技术术语准确。两份 SKILL.md 环境段改为指向 README。
- **AGENTS.md 新增「分层摄入原则」**:L0 白拿现成文字(平台字幕/shownotes/正文,零成本)→ L1 本地转换(ASR/OCR,一次投入永久复利)→ L2 多模态精准补充(暂不做);说明为何不用原生多模态当主线(每次付费无复利);固化「底层库+上层skill」架构;要求 ASR 结果标注误差、**多人对谈不编造发言归属**(当前不做说话人分离)。禁止事项补 4 条。
- 踩坑记录:① 裸装 bilibili-api-python 不带 HTTP client,须装 curl_cffi 并注册 ② curl_cffi 的 stream Response 不支持 context manager(`with` 会 TypeError),须 try/finally ③ pi 内置 fetch_content 对公众号提取失败,故需专门脚本。

## [2026-07-27] setup | skills 加 kg- 前缀 + 软链到全局

- 需求:让库里的 skill 在任何目录都能用,且加 `kg-` 前缀(kg = KingGloose,主人网名)区分自有 skill。
- **改名**(只改 SKILL.md 的 `name` 字段,目录名不动以免动脚本相对路径):
  `kg-bilibili` / `kg-wechat` / `kg-doc` / `kg-xiaoyuzhou` / `kg-media-to-text` / `kg-knowledge-backfill`。
  按主人要求去掉 `-ingest` 后缀。各 SKILL.md 里 description/正文的交叉引用同步更新,路径引用(`../README.md` 等)保持不变。
- **软链**(方案B,整个目录):`~/.agents/skills/kg -> 学习笔记/skills`。
  依据 pi 文档「directories containing SKILL.md are discovered recursively」,**以后新增 skill 自动生效**,无需逐个补软链。
- 验证:从 `/tmp` 启动 pi,五个 kg-* skill 全部被发现;`kg-media-to-text` 正确未出现(标了 `disable-model-invocation`,底层库只被代码调用)。
- 附带解决:此前 `knowledge-backfill` 在 `~/.agents/skills/` 和库里各有一份且内容不同,存在 pi 同名冲突(规则是保留先找到的、行为不确定)。改名后冲突消除。
- 已知开销:软链使 pi 启动从 5.1s 增至 7.5s(递归扫描 `skills/.venv` 的 1.5GB)。待主人决定是否把 venv 移出扫描范围优化。

## [2026-07-27] setup | skills 目录改名对齐 + 一键安装脚本(Mac/WSL2)

- **目录名统一**:目录名此前与 skill 名不一致(`bilibili-ingest` vs `kg-bilibili`),已全部改为 `kg-*` 与 skill 名一致。
  验证安全性:脚本内用 `Path(__file__).parents[3]` 层级定位库根,**不依赖目录名**,故改名不破坏路径;改后重装 editable 底层库,实测落盘路径仍正确指向 `raw/`。
  README 架构段重写(去掉冗余的"目录名≠skill名"说明,现已一致)。
- **新增 `skills/install.sh`**:一键安装/迁移脚本,幂等可重复运行。
  自动:平台探测(macOS arm64/x86、Linux、**WSL2 识别** via /proc/version)→ 检查 uv/ffmpeg → 建 Python 3.12 venv →
  **按平台自动选 ASR 依赖**(Mac=asr-mac/mlx-whisper,Linux/WSL=asr-linux/faster-whisper)→ 装底层库(editable)→
  软链注册全局 → 6 项自检(底层库导入/类型探测/库根定位/文档依赖/B站依赖)。
  参数:`--minimal`(跳过 Docling 1GB + Whisper 1.5GB)、`--no-link`、`--help`。
  实测:完整安装幂等通过;删掉 venv 模拟新机器,`--minimal` 从零安装 11 秒完成(uv 缓存复用),自检全绿。
  踩坑:`"...（$VAR）"` 中文全角括号紧跟变量导致 bash 在 `set -u` 下报 unbound variable,改用半角分隔符。
- **事故与恢复**:改目录名过程中 `kg-knowledge-backfill/SKILL.md` 意外丢失。git 仍追踪(状态 D)故从 `git show HEAD:` 完整恢复(4414 字节),重新应用 kg- 前缀并同步内部路径引用。**教训:批量 mv 后应立即验证文件完整性**。
- 澄清 `kg-knowledge-backfill` 的定位(主人问及):它是本库最早的 skill(2026-07-25 建),与本周新建的摄入类 skill **方向相反**——摄入类是"外部资料→知识库"(入口),它是"在其他项目里获得的经验→跨目录回填知识库"(出口)。两者互补。
- 遗留:`~/.agents/skills/knowledge-backfill/` 是旧版冗余副本(3871字节,硬编码绝对路径),库里新版已改为相对定位(上两级目录)。待主人确认后删除。

## [2026-07-27] lint | 全面缺陷检查与修复(逐个 skill 过一遍)

主人要求自查项目缺陷。逐个 skill + 文档审查,共修 **15 个真实问题**:

**代码缺陷(会导致资源泄漏/崩溃/误导)**
1. `kg-media-to-text/handlers/audio.py`:视频抽音轨的临时目录**从不清理**(每处理一个视频泄漏一份音轨,可能几十MB)。改为 try/finally + shutil.rmtree,实测清理生效。
2. 同上:ffmpeg 失败时 `check=True, capture_output=True` **吞掉 stderr**,用户只见无信息异常。改为手动检查 returncode 并带出 stderr 末 5 行。
3. 同上:CUDA 失败降级 CPU 时 `except Exception` **静默吞掉原因**,用户不知为何突然变慢。改为记入 `metadata.gpu_fallback_reason`。
4. `handlers/document.py`:docling/markitdown 解析失败时异常**未包装**,上层 `except MediaToTextError` 捕不到 → 裸 traceback。改为包成 MediaToTextError 并给常见原因提示。实测损坏 PDF 现在有友好报错。
5. 同上:`handle_plain` 解码失败抛 `MissingDependencyError`(语义完全错,不是缺依赖)→ 改 MediaToTextError。
6. `router.py`:传目录时报"无法识别的素材类型"(误导)→ 增加 is_dir 判断,明确提示。
7. `kg-wechat/scripts/wechat_to_md.py`:**无效 URL 直接 AttributeError 崩溃**(`soup.title.string` 为 None)→ 改用 get_text() 兜底。实测已修。
8. 同上:`fetch_html` 网络请求无错误处理 → 加友好提示。
9. `kg-xiaoyuzhou/scripts/ingest_episode.py`:音频**下载失败会泄漏临时目录**(finally 只覆盖转写路径)→ 补 try/except + rmtree。
10. 同上:页面请求与 JSON 解析无错误处理 → 加。实测非小宇宙 URL 现在给友好 404 提示。
11. `kg-bilibili/scripts/get_transcript.py`:ASR 失败泄漏临时目录 → 改 finally + rmtree;字幕 JSON 请求无错误处理 → 单分P失败降级为 warn 而非整体崩。
12. `kg-doc/scripts/ingest_doc.py`:补 OSError 兜底(权限/IO 错误不再裸 traceback)。

**文档/配置缺陷(会让人跑不通或误导)**
13. **四份 SKILL.md 的命令照抄跑不通**:环境段写 `cd skills` 但用法段是 `python scripts/xxx.py`(skill 目录相对)→ 实测 No such file。改为 `cd skills && source .venv/bin/activate && cd kg-xxx`,四个逐一验证可跑。
14. `AGENTS.md` 架构块用旧目录名(`skills/media-to-text/`、`skills/*-ingest/` 这个 glob 已匹配不到任何目录)→ 修正为 kg-*。AGENTS.md 是必读契约,路径错会把 AI 引到不存在的目录。
15. `kg-bilibili/SKILL.md` description 说"不负责无字幕视频语音转写",与自身正文的 `--asr` 用法和已验证段**直接矛盾**(description 是模型选路依据,会导致错误放弃)→ 已改。
16. `kg-wechat/SKILL.md`、`kg-knowledge-backfill/SKILL.md` 硬编码 `/Users/zhangjiahui04/...` 绝对路径,与"不依赖绝对路径"的迁移承诺冲突 → 改相对路径。
17. 库根 `README.md` 迁移段整段过期(指向已不存在的 `skills/knowledge-backfill`、且"把库根路径改成新位置"与相对定位矛盾)→ 改为指向 `install.sh`。
18. `skills/.gitignore` **漏了 `*.egg-info/`**(editable 安装产物,一提交就进库)+ 补 build/dist;根 gitignore 补 `.pi-subagents/`。
19. `skills/README.md` 写"6 项自检"实际 5 项 → 修正。
20. `index.md` 缺本库自建 skill 体系的唤醒条目(按契约 index 就该唤醒)→ 补分层摄入原则、架构、工具选型、四条踩坑。

**回归验证**:所有 Python 编译通过;install.sh 语法+幂等通过;底层库三路径(文档/纯文本/视频转写)正常;kg-bilibili/kg-wechat 真实链接回归正常;pi 仍正确发现 5 个 kg-* skill。

## [2026-07-27] setup | 移除 knowledge-backfill(两份)

- 主人决定不再需要"知识回填"能力,删除:
  - `~/.agents/skills/knowledge-backfill/`(旧版全局副本,硬编码绝对路径)
  - `skills/kg-knowledge-backfill/`(库内版本,本库最早的 skill,2026-07-25 建)
- 删除前备份到 `/tmp/kb-deleted-backup/`;库内那份也在 git 历史中,需要时可 `git show` 找回。
- 同步清理文档引用:库根 `README.md` skills 说明段、`skills/README.md` 架构块。
- 影响说明:以后在其他项目里想回填知识,没有专门 skill 指导跨目录写入,但 `AGENTS.md` 的 Ingest 流程和判断标准仍在,AI 读契约即可完成。
- 验证:pi 现发现 4 个 kg-* skill(kg-bilibili/kg-doc/kg-wechat/kg-xiaoyuzhou);install.sh 自检全通过。
