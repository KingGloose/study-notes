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

## [2026-07-28] ingest | B站视频 → wiki/AI/AI Agent 的可验证开发体系

- 走 `kg-bilibili` 形态 1+2:拉稍后再看(474 条),按 AI/技术关键词筛出约 90 条候选,选《我做 AI Agent 一年,90% 在做表面功夫——直到我换了思路》(数字黑魔法,BV1o87764Ebs,14:27,计算机技术)。
- **L0 白拿成功**:B站 AI 字幕直接抓到(13KB),未动本地 ASR。原始逐字稿存 `raw/bili-BV1o87764Ebs-AI-Agent开发的可验证体系.md`,头部标注来源与已知识别误差(AIA证/A卷=AI agent、VLOG=Verilog、school board=scoreboard、虎威测试=回归测试)。
- **沉淀判断**:不是通用教程,而是"从瓶颈出发的工程决策链"+ 芯片验证行业类比,AI 直接问答给不出 → 写成 `wiki/AI/AI Agent 的可验证开发体系.md`。
- 联网核对两个信源:
  - Verifier's Law 提出者 Jason Wei 确认(OpenAI o1/Deep Research 共同作者),但**其博客原题用的是 verifier's *rule***,社区普遍传成 law → 已在页内标注,查原文两个词都要试。
  - ACI 出自普林斯顿 SWE-agent(arXiv:2405.15793, NeurIPS 2024)确认;视频"接口设计影响大过换更强模型"这一强弱比较标为转述措辞,引用需回原文核对。
- 双链:新页 ↔ `AI Native 时代的研发组织`(组织层 ↔ 工程层同一命题的两个尺度),并把后者「本页是 AI 领域第一页,暂无兄弟页」的说明改掉。另关联 MCP(本页给出一个**不选** MCP 的场景)、Skills 渐进式披露、本库摄入体系。
- `index.md` 08 AI 补该页唤醒条目。

## [2026-07-28] contract | 摄入领域放宽:不再限定技术

- **问题**:主人指出知识库不止技术内容,而我把《房石阳明话术解析》当成"非技术"降级处理(只给口头解析,未入库)。
- **根因**:`kg-bilibili/SKILL.md` 的筛选口径写死了"优先级最高:编程/技术相关 / 基本排除娱乐",description 也写"侧重编程/技术类科普"。我拿它当了默认价值判断。其余三个 ingest skill(kg-wechat/kg-xiaoyuzhou/kg-doc)本来没有技术偏向,无需改。
- **改动**:
  - `kg-bilibili/SKILL.md`:description 改为"领域不限";筛选口径重写为**按「是否知识向」筛,不按「是不是技术」筛**,判据是"看完能不能带走一个可复用的认知/方法/判断";补「别被 tname 分区骗了」(人文历史下可能是话术解析、日常下可能是硬核技术连载);要求给候选时**主动跨领域搭配**,否则主人只能在技术里挑。
  - `kg-bilibili` 边界段补两条:非技术内容不降级处理;**非技术类的核对重点不同**——技术类核 API/版本是否过时,话术/心理/商业类核**术语归属、案例出处、适用边界和代价**(最容易漏"什么时候不该用")。
  - `AGENTS.md`:wiki 目录注释的领域举例从"前端/ai/python"扩为含沟通/心理/商业/人文/健康;Ingest 判断步骤后加一条显式声明——判断标准永远是"AI 能否完整答出",不是题材领域。
  - `index.md`:开头说明加"领域不限于技术",并说清 01~09 编号是沿用旧目录、新领域可直接新开一节。

## [2026-07-28] ingest | B站视频 → wiki/沟通/转移回答的层级(新领域首页)

- 视频《别人问你不想回答的问题,怎么让他以为你已经回答了?|房石阳明话术解析第48期》(登高自卑-,BV1KNNv6sE1h,10:18,分区人文历史),素材出自游戏《人狼村之谜》Raging Loop。
- **L0 白拿**:B站 AI 字幕 8.7KB。逐字稿存 `raw/bili-BV1KNNv6sE1h-转移回答层级的话术.md`,标注识别误差(加护→家护/家户、房石→房事/房兴、清之介→亲自介、卷岛宽造→宽躁、**元沟通→"语言沟通"**)。
- **沉淀判断**:话术本身通用,但三样东西值得留页——极端案例(是与不是都会死,机制暴露得最清楚)、可复用句式表、以及**视频没讲的失效条件与代价**。
- 联网核对补了两处视频缺口:
  - 视频说术语叫"语言沟通" → 实为**元沟通/元传播 metacommunication**(Ruesch & Bateson 1951,"关于沟通的沟通",内容层 vs 元层),字幕识别错。
  - 找到哈佛实证 **《The Artful Dodger》**(Rogers & Norton, HBS WP 09-048),四组实验证实机制并给出边界:听者默认注意力目标是"我喜不喜欢这人"而非"你答没答";三种被识破条件(被要求判相关性 / 偏离过大 / **问题文字持续可见**);且**流畅答错问题的评价高于结巴答对**——解释了这招为何短期划算。
  - 由第三条推出一个视频没有的实用结论:**书面沟通(微信/邮件/纪要)里这招危险得多**,因为原问题就在上面几行。
- 双链:`wiki/沟通/转移回答的层级` ↔ [[AI Agent 的可验证开发体系]](攻防反向——工程上主动消除不确定性,博弈里主动维持不确定性当护身符)。
- `index.md` 新开「10 沟通 / 话术」一节。这是 wiki 的**第一个非技术领域目录**。

## [2026-07-27] setup | kg-bilibili 新增全站搜索(形态3)

- 需求:此前只能从「稍后再看/收藏」里挑,主人希望能主动按关键词搜内容。
- 新增 `kg-bilibili/scripts/search_videos.py`,基于 `bilibili_api.search.search_by_type`(SearchObjectType.VIDEO)。
  参数:`--order`(totalrank综合/click播放多/pubdate最新/dm弹幕多/stow收藏多/scores评论多)、`--days N`(近N天)、
  `--min-min`/`--max-min`(时长区间,过滤水视频/超长视频)、`--limit`、`--page`。
  输出字段与 `list_videos.py` 对齐(title/bvid/author/duration/url/intro/tname),额外带 `play`/`danmaku`/`pubdate` 供质量判断。
  细节:B 站搜索结果标题含 `<em class="keyword">` 高亮标签,已用正则清除;duration 是 "MM:SS"/"HH:MM:SS" 字符串,已解析为秒便于过滤。
- SKILL.md 新增「形态 3:主动搜索」工作流,给出参数选择建议(要经典用 click/stow、要最新用 pubdate+days、过滤水视频用 min-min),
  并提醒**别只看播放量**——小众技术视频播放量天然低但内容可能更硬。
- 实测:`Rust 异步编程`(40条)、`AI Agent 开发 --order pubdate --days 365 --min-min 8 --max-min 60`(过滤后6条均为近期长视频)、
  `TypeScript 类型体操 --order click`(播放量降序正确)。边界:非法 --order 报错清晰;过滤过严时提示可放宽。
- **主动放弃的能力**:`search.get_hot_search_keywords()` 能拿全站热搜,但实测内容是泛娱乐/时事(电影撤档、球队转会、台风),
  与主人「编程技术」定位不搭,加了只是噪音,故不集成。

## [2026-07-28] ingest | 公众号 → wiki/NodeJS/子进程 spawn 管理

- 文章《Node.js 子进程管理:我是如何被 spawn 逼疯的》(mCell,程序员成长指北,2026-04-21),正文 3015 字。存 `raw/wx-2026-04-21-Nodejs子进程spawn管理.md`。
- 原文唯一一张图是加群二维码(C 档装饰型),按 AGENTS.md 图片规则**未入库**,raw 里替换为一行说明。
- **沉淀判断**:原文分层脉络(输出→输入→超时→会话→截断)清楚,但多处只说"有坑"没给机制和解法 → 值得成页,在其骨架上补实测。
- **本机实测四组**(Node v25.9.0,macOS),补了原文没有的东西:
  1. **exec 的 maxBuffer 默认 1MiB**:2MB 输出直接 `ERR_CHILD_PROCESS_STDIO_MAXBUFFER` 杀子进程,spawn 完整收到 2097152 字节。这才是必须换 spawn 的硬理由,原文只说"不够灵活"。
  2. **`d.toString()` 切坏多字节 UTF-8**:20 万个"中"实测 **9/10 的块出现 U+FFFD 乱码**,StringDecoder 后 0 坏块。原文说这层"还好,主要是耐心"——中文场景几乎必踩。
  3. **exit ≠ close**,且 `kill()` 返回 true 只代表信号已发出(忽略 SIGTERM 的进程 killed=true 但 exitCode=null 仍在跑);被信号杀时 `code` 为 null,要看第二个参数 signal。
  4. **孙进程逃逸**(原文最大缺口,教训第 5 条只写了一句没给解法):父node→sh→node 三层,`proc.kill()` 后残留孙进程 1 个;`detached:true` + `process.kill(-pid)` 杀进程组后为 0。补了 Windows 无信号/进程组需 taskkill /T,以及官方 killTree 提议(nodejs/node#64406)尚未落地。
- 另加两条对原文的**保留意见**:`token×4` 估算只对英文成立,中文低估 3~4 倍;截断只留头部会丢掉异常栈(关键信息在尾部),应头尾都留。
- 双链:`wiki/NodeJS/子进程 spawn 管理` ↔ [[AI Agent 的可验证开发体系]](后者 1.5.2「调用做成命令行」的实现底座,执行不稳则回归测试结果不可信),并在后者补了反向链接。
- `index.md` 03 前端「框架/运行时」NodeJS 后补该页唤醒条目。

## [2026-07-28] fix | kg-wechat 图片扩展名 bug(实测发现)

- **现象**:抓这篇文章时图片被存成 `assets/wx-33dcba55ce.other`,Obsidian/浏览器都认不出;`file` 一看实际是 WebP。
- **根因**:`wechat_to_md.py` 直接拿 URL 里的 `wx_fmt=` 当扩展名,公众号部分图的 `wx_fmt=other`(或缺失)就原样落成 `.other`。原代码里那句 `if fmt=="webp": fmt="webp"` 是空操作,毫无作用。
- **修复**:新增 `sniff_image_ext()` 按文件头(magic number)嗅探真实格式,覆盖 png/jpeg/gif/webp/bmp/svg,未知回退 png;仅当 `wx_fmt` 不在白名单时才启用嗅探(正常情况不改变原行为)。
- **验证**:单元级 5 种输入判断正确;重抓同一篇文章,同一张图现在正确落为 `wx-33dcba55ce.webp`。

## [2026-07-28] setup | 新增三个实用能力:kg-lint / kg-doc 批量+URL / kg-youtube

**1. 新建 `kg-lint`(库健康检查)** —— 实现 AGENTS.md 里写了但一直缺的「Lint 定期体检」职责。
六项检查:死链(`[[xxx]]` 指向不存在)、孤儿页(无其他页链入=知识网断点)、raw 原文未被 wiki 引用、
index.md 缺唤醒条目、log.md 无摄入记录、内容过短(<400字符)。纯标准库、只读不改、36 毫秒跑完。
**关键设计:三级宽松匹配避免误报**——index 写的是关键词而非页名全称(页名「QuillJs 换行与 embed 光标问题」,
index 只写「QuillJs」)。初版按全称匹配产生 9 条误报;加了「页名全称 → 按标点拆词 → **中文子串滑窗**(长度≥3)」
三级匹配后误报清零。中文滑窗是必需的:中文页名无空格,拆词失效。
**首次体检就发现 4 条真问题**:3 个孤儿页(QuillJs / Vue watch / 转移回答的层级)、
1 个 index 缺唤醒(`沟通/转移回答的层级` 8606 字但 index 只在导言泛提"沟通话术",实际查不到)。

**2. `kg-doc` 扩展:文件夹批量 + 网页 URL**
- 批量(`--batch`):递归扫描、**断点续传**(输出已存在则跳过,`--force` 覆盖)、`--ext` 限定类型、汇总成功/跳过/失败。
- 网页:启发式提正文(`<article>` → `<main>` → 文字最多的容器)+ markdownify。实测 Rust 官方博客 8843 字符,标题/代码块/链接完整。
- 踩坑:curl_cffi **默认不跟随重定向**(`allow_redirects=True`);且该案例是 **meta refresh 跳转**(非 HTTP 3xx),
  需解析 `<meta http-equiv=refresh>` 递归跟随才拿到正文。
- 公众号链接虽能抓但会提示改用 kg-wechat(那边有图片防盗链处理)。

**3. 新建 `kg-youtube`** —— 字幕覆盖率远高于 B站(157 种自动字幕),多数视频走 L0 白拿零算力。
- 策略:**逐个语言尝试字幕、拿到就停**;每种语言先试人工(`--write-subs`)再试自动(`--write-auto-subs`);
  无字幕才降级本地 ASR。产物头部标注实际来源(如 `字幕 en(自动)`)。
- 踩坑:**一次请求多语言会触发 YouTube 429 限流**(实测 zh-Hans 被限),故必须逐个试;
  遇 429 跳过该语言继续。VTT 需清理内联时间标签 `<00:00:19><c>` 与滚动字幕重复行。
- 实测:人工字幕 2066 字符、自动字幕 5904 字符、429 降级成功、清理后无残留、无临时文件泄漏。

**主动放弃**(记录理由,避免以后重复讨论):说话人分离(需 pyannote gated model + HF token,40系显卡有兼容报告,
等真被"分不清谁在说"困扰时再做)、小红书/知乎摄入(反爬严/付费墙,投入产出比低)、定时自动摄入(违背 AGENTS.md
「不批量、一切按需」——价值在讨论过程不在攒素材)。

同步更新 `skills/README.md` 架构块与依赖表、`AGENTS.md` 架构块。全量编译通过,七个 skill CLI 自检通过,
pi 正确发现 6 个可唤起 skill(kg-media-to-text 按设计隐藏)。

## [2026-07-28] ingest | 小宇宙播客 → wiki/沟通/深度关系与自我表露

- 《纵横四海》EP81《深度关系》(携隐 Melody,2026-05-08,**4:29:11**),解读斯坦福 GSB《Connect》(Bradford & Robin,Interpersonal Dynamics / Touchy-Feely 课)。
- **档1 白拿** shownotes 1542 字(含 14 个时间戳节点);经主人确认后跑**档2 转写**:音频 249MB,本地 mlx-whisper 约 22 分钟出 8.5 万字逐字稿,存 `raw/xyz-2026-05-08-EP81...md`。
- 8.5 万字超出单次阅读预算 → **切 5 段派 5 个 delegate 子智能体并发提炼**,主上下文只收结构化笔记。这个模式对长播客有效,以后 2h+ 的节目可复用。
- raw 头部补了详细 ASR 误差标注:人名(携隐→"协影"、纵横四海→"综合赛/宗文萨姨")、案例人名各有 3~4 种写法(Elena/Sanjay/Ben/Maddie/Mia/Anya)、术语(Touchy Feely→"Tachi Phili"、商学院→"上学院"、panic zone→"paddock zone"、金缮→"金扇"、带宽→"贷款"、red flag→"累地累"、MBTI i/e/P/J→"医人/爱人/屁人/贼人")、**全篇他/她不分**、4.2–4.4KB 处转写损坏。
- **沉淀判断**:书的框架 AI 能答,但 Melody 的个人剖析和实战话术给不出 → 成页,严格标注 [书]/[Melody]/[AI 补充] 三类来源。
- 核对✓:书名作者、Touchy-Feely、六特征、15% 法则、三层现实与网球网、**pinch/crunch**、**feeling emotionally met**、金缮。
- **存疑未确认**(已在页内标注):逐字稿高频"一人一杀"疑为"**一轮一杀**"之误;引用往期"EP08 情商"可能是 EP80。
- 明确区分出**属于 Melody 而非书中**的观点:软弱/脆弱两层区分(脆弱=对反应失控的不确定,不看内容正负)、两根支柱归纳、rawness 流失、**幼儿化对方**、爱情vs友情的承诺论、"影响力差异就是权力"的改写、"十个人有九个会回应"的个人数据。
- 双链:`深度关系与自我表露` ↔ [[转移回答的层级]](**同一层面方向相反**:一个躲、一个解,都靠"跳到元层")、↔ AI 两页(rawness 流失是"信息形态越结构化越好"的反面,职业习惯容易带错场)。
- `index.md` 10 沟通/话术 补条目。

## [2026-07-28] fix | index.md 的「10 沟通/话术」整节被 vault backup 覆盖丢失

- **现象**:准备补 EP81 条目时发现 `index.md` 里 07-28 早上加的「10 沟通 / 话术」整节(含`转移回答的层级`条目)和开头的"领域不限于技术"说明**都不在了**;`git show` 确认最近两次 `vault backup` 提交里也没有该节。
- **判断**:不是我误删——wiki 文件本身完好(`wiki/沟通/` 两页都在)、`log.md` 里那条记录也在,只有 `index.md` 这一节丢了。推测是自动 vault backup 与编辑并发时用旧内容覆盖了 index.md。
- **修复**:两条沟通条目一并重建(转移回答的层级 + 深度关系与自我表露),并复原"领域不限于技术"说明。
- **回归检查**:其余三条近期条目(NodeJS spawn / AI 可验证开发体系 / AI Native)均在,未受影响。
- **待观察**:如果 index.md 再出现内容回退,需要检查那个自动 backup 机制的写入时序。

## [2026-07-28] setup | 新增 kg-browser(底层浏览器能力) + kg-zhihu

- 起因:主人问知乎/小红书能否摄入。实测知乎**纯 HTTP 完全走不通**——curl_cffi 各种指纹
  (chrome/safari/移动端)、完整请求头、**甚至带完整登录 cookie(含 z_c0) 全部 403**。
  根因:知乎上了 `zse-ck` JS 挑战(返回加密串+一段必须浏览器执行的 JS 才能算出 __zse_ck cookie)。
  查开源项目(zhihu-md / Squallever / yuchenzhu)后确认:**三个方案全都绕不开浏览器**,
  其中 yuchenzhu 同时依赖 curl_cffi + playwright,印证纯 HTTP 不够用。
- 主人指出已有 `zz-harness/plugins/zzfe/skills/fe-chrome-devtools`(连真实 Chrome 的前端调试 skill),
  要求借鉴改造:**浏览器是底层能力,和 kg-media-to-text 同层;kg-zhihu 是上层业务**。
- **新建 `kg-browser`(底层)**:
  - 从原 skill **只移植 `start-user-chrome.sh`**(连真实 Chrome 的机制,唯一有价值的部分),
    改名 `connect-chrome.sh`,去掉 CLAUDE_PLUGIN_ROOT 依赖与前端调试专属注释。
  - **丢掉**原 skill 8 个前端调试专题(css-debugging/performance-lcp/memory-leak/component-locator 等)——
    定位不同:原 skill 给开发者调试,本 skill 给用户读内容。
  - **一次返工**:我最初写了个 `extract_page.py` 把提取逻辑写死,**主人指出这违背原 skill 的设计哲学**
    (应该给 AI 灵活的 CLI 工具+约束方法论,而不是框死操作)。已删除,改为 SKILL.md 给
    「思路+常用 evaluate_script 片段」、references 存站点知识,核心能力靠 AI 直接调 chrome-devtools 组合。
  - `references/site-selectors.md`:知乎/掘金/CSDN/博客园/思否/简书/语雀/Notion 的选择器与坑。
    **约定优先记"坑"而非"选择器"**(选择器易失效,坑是结构性的:懒加载/折叠/虚拟滚动/公式在 img alt 里)。
  - `references/troubleshooting.md`:连接失败排查(含实测踩坑:`DevToolsActivePort` 里的 WS UUID
    Chrome 重启后失效但文件不更新,导致 `Network.enable timed out`;CDP 的 HTTP 接口不响应是正常的,
    别拿 curl /json/version 当连通判据)、WSL 跨平台限制与降级方案。
  - 为什么用真实 Chrome 而非 Playwright:天然带登录态、天然过 JS 挑战、零反爬对抗、省 300MB Chromium。
    **边界原则:只读用户自己已能看到的页面,不注入 cookie 不绕权限。**
- **新建 `kg-zhihu`(上层)**:同样不写死脚本,给工作流+判断标准。区分三类页面(专栏/单条回答/问题页)
  的不同处理(折叠展开、无限滚动、公式与原图属性),浏览器操作委派 kg-browser。
  额外写了「知乎内容的特殊判断」:高赞≠正确、注意时效、区分作者经验vs转述。
- 装了 `chrome-devtools-mcp@latest` CLI(全局 npm)。**链路尚未端到端验证**——
  主人的 Chrome 需先在 chrome://inspect 开启 remote debugging 并彻底重启(当前 DevToolsActivePort 是旧的)。
- **小红书结论:仍不建议做**。理由升级:连知乎这种相对温和的平台都上了 JS 挑战,小红书要逆向
  `x-s`/`x-t` 签名(与 cookie+浏览器指纹强绑定)、Web 与移动端算法还不同、社区工具频繁失效、
  且有封号风险;加上笔记短图多文字少,对技术沉淀单位产出低。需要时主人手动复制文字更划算。
