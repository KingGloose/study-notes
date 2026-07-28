# 知识索引 · 唤醒地图

> 这份索引的作用是**唤醒**:列出我接触过的知识点关键词,让脑子里"知道这个东西存在"。
> 详细内容大多在 `archive/`(旧笔记归档)。需要细节时,问 AI 或翻 archive 对应文件。
>
> - 通用知识点(AI 能直接答的)也全部保留在这里,因为"知道它存在"本身就是价值。
> - 新沉淀的知识进 `wiki/`,原始资料进 `raw/`。
> - 带 ⭐ 的是近期深度笔记 / 有个人实践上下文的内容,价值更高。
> - **领域不限于技术**。早期旧笔记以技术为主(01~09 沿用旧目录编号),新内容覆盖沟通话术、心理、
>   商业财经、人文历史、健康、生活技艺等一切知识向领域——需要时直接新开一节,不必往技术分类里硬塞。

---

## 01 基础

- **Git**:版本控制原理、集中式vs分布式、基本配置、文件状态、操作流程、分支、远程仓库
- **Linux**:CentOS 安装、网络连接三种方式、虚拟机(克隆/快照/迁移)、vmtools、目录结构、常见命令
- **Docker**:镜像原理、安装部署、制作镜像、volume 挂载、arg/env、cmd/entrypoint、copy/add
- **计算机网络**:子网划分、⭐Clash TUN 模式(与系统代理的区别、使用场景)
- **网络 / 泛域名**(⭐系列,`wiki/网络/`):⭐泛域名/通配符域名/子域名/泛解析/通配符证书概念辨析、⭐DNS 泛解析与查询链路(递归vs迭代、`*` 只匹配一层、精确优先通配兜底、TTL/dig)、⭐通配符 HTTPS 证书(SAN 不认 CN、只覆盖一级、多级需多条 SAN、DNS-01 签发)、⭐nginx 泛域名转发(server_name 匹配优先级、正则捕获子域信息、反代透传 Host/X-Real-IP/X-Forwarded-Proto)、⭐同源策略与 CORS(同源三要素、限读放行用、预检、带凭证不能用`*`、Vary:Origin)、⭐Cookie 跨子域(Domain=父域共享登录态、SameSite 同站≠同源、postMessage 双向 origin 校验)
- **设计模式**:单例模式、工厂模式
- **网络安全**:SRI 子资源完整性、浏览器指纹
- **云服务器**:域名、主机记录

## 02 算法

- 算法练习仓库(study-algorithm)

## 03 前端

### HTML
- 骨架/meta 标签、块元素vs行内元素、全局属性、字符实体、语义化
- 表格(单元格合并)、列表、表单(input/select/textarea/label)、音视频(编解码器 H.264/VP8/AAC)、Emmet

### CSS
- **基础**:引入方式、选择器(简单/属性/关系/伪类/结构伪类)、继承、盒子模型(box-sizing/border-radius/box-shadow)
- **布局**:定位(relative/absolute/fixed/sticky/z-index)、浮动(清除/高度塌陷/clearfix)、Flex、Grid、媒体查询
- **文字字体**:text-shadow/align/overflow、white-space、@font-face 网络字体、字体图标
- **背景动画**:线性/径向渐变、精灵图、background 各属性、transition、animation/@keyframes
- **预处理/框架**:SCSS、TailwindCSS
- **实践**:checkbox 样式重写、password 眼睛显示、单行省略号

### JavaScript
- **变量类型**:数据类型、typeof、类型转换、var/let/const、作用域提升、块级作用域、暂时性死区
- **函数**:箭头函数、默认参数、剩余参数、扩展运算符、IIFE
- **对象**:Object.is/entries/freeze、Proxy、Reflect(Receiver/construct)
- **数据结构**:Set/WeakSet、迭代器(可迭代对象/自定义迭代类)、Map
- **异步**:⭐Promise(工作流程/API/手写)、requestAnimationFrame、requestIdleCallback、MessageChannel、⭐模拟虚拟线程、Atomics、⭐watch/watchEffect 里跑异步(竞态、onCleanup、依赖收集断裂 → wiki/前端)
- **DOM/事件**:解析 DOM 树、addEventListener、handleEvent
- **进阶**:⭐defer/async 深度理解(脚本加载时机、与 Vue 首屏的坑)、⭐Signals(alien-signals、Vue 3.5/3.6 响应式重构)、PerformanceEntry、位运算权限、模板字符串(标签模板)
- **ECMAScript**:ES6(let/const/Symbol/迭代器/生成器)、ES7(includes/指数)、ES8(entries/padding)、ES9(rest/扩展)、ES10(flat/flatmap)、ES11(可选链/??/BigInt/globalThis/私有属性)、ES12(逻辑赋值/WeakRef/FinalizationRegistry)

### 框架 / 运行时
- **Vue**:响应式原理、组件通信、Vuex/Pinia、Vue Router、虚拟DOM、生命周期(详见 archive Vue 全集)
- **React**:hooks、redux 原理、虚拟DOM diff
- **Jquery**、**NodeJS**、**TypeScript**、**微信小程序**
- ⭐**Node.js 子进程管理 spawn**(`wiki/NodeJS/`,蒸馏公众号文章 + 本机实测):exec 的 **maxBuffer 默认 1MiB 上限**(超出直接杀子进程报 ERR_CHILD_PROCESS_STDIO_MAXBUFFER,这才是必须换 spawn 的硬理由)、**`d.toString()` 切坏多字节 UTF-8**(实测 9/10 块中文乱码→用 StringDecoder / setEncoding)、**exit ≠ close**(close 才代表 stdio 收完)、SIGTERM→SIGKILL 两层退出、`kill()` 返回 true 只代表信号已发出(进程可忽略 SIGTERM)、被信号杀时 code 为 null 要看 signal、**孙进程逸逸**(proc.kill() 只杀 shell→孙进程变孤儿;需 detached:true + `process.kill(-pid)` 杀进程组;Windows 无信号/进程组靠 taskkill /T;官方 killTree 提议未落地)、会话管理与并发上限(MAX_SESSIONS 要和 fd 上限一起算,每进程占 3 个 fd)、输出截断(**token×4 只对英文成立,中文低估 3~4 倍**;只留头部会丢异常栈→头尾都留)、PTY(node-pty)与 stdin ready signal
- **Uniapp**:⭐跨平台原理、环境配置(网页/小程序/Android/mumu模拟器)、pages.json/manifest.json、uni-ui/uni-forms、页面通讯(setup传参/事件总线)、⭐网络请求封装(RequestService)、pinia、⭐蘑菇街项目(多端适配/条件编译/图片懒加载/三端发布)、easycom、#ifndef 条件编译
- **NuxtJS**、**NextJS**、**Electron**、**Uniapp**

### 富文本 / 编辑器
- ⭐**QuillJs**:换行 bug、`<br>` 被忽略、单独视频/图片后光标无法定位(文档必须以 `\n` 结尾)、BrBlot workaround vs 数据层归一化、clipboard matcher(→ wiki/前端,学堂系统实践)

### 模块化
- ⭐**JS 模块系统**:模块化历史(NoModule/AMD/CMD)、CommonJS(exports vs module.exports 内存引用、寻址规则、Module 对象本质/compiledWrapper)、ESM(静态分析、live binding、import()、顶层 await、Node .mjs/type:module)、CJS↔ESM 互操作、⭐**模块缓存=单例**(缓存按文件路径 key,React/antd 隐式单例的地基 → wiki/前端)

### 工程化 / 其他
- 工程化、Webpack、Vite、微前端、单元测试、Bun、前端可视化
- ⭐**运行时动态 base / publicPath**(`wiki/前端/`,泛域名系列重头):编译期 base vs 运行时 base、webpack `__webpack_public_path__`→`__webpack_require__.p`、`__webpack_require__.e` 动态建 script 加载 chunk、Vite 三方案(重写 import()/改造构建平台/插件)、vite-plugin-dynamic-base 原理(`/__dynamic_base__/` 靶子 + `window.__dynamic_base__` 运行时拼接 + preloads 数组 + enforce:post + 插件执行顺序)、容易漏的资源(CSS url/legacy/PWA)、一次构建多处部署
- ⭐**依赖冲突**:peerDependencies(对等依赖)、依赖单例(ConfigProvider context/hooks dispatcher)、npm/pnpm/yarn 冲突行为差异、overrides vs resolutions(npm 不认 resolutions)、NormalModuleReplacementPlugin 按来源分流 antd v4/v5(→ wiki/前端,学堂 zant-ui 实践)

## 04 Java

- **Java基础**:四种内部类(局部/匿名/成员/静态)、枚举、注解
- **JavaWeb**:XML(语法/解析)、Web 基础

## 05 数据库

- **MySQL**:数据库/表操作、增删改查、备份恢复
- **MongoDB**:安装、数据库/集合/文档命令
- **Redis**:String/List/Set/Hash/Geo、过期时间

## 06 Rust

- 环境安装、HelloWorld、基础语法

## 07 嵌入式

- ESP8266、UNO

## 08 AI

- **理论**:机器学习(监督/非监督/半监督)、神经网络
- **RAG**:⭐向量表征、向量概念、文本向量、Embedding、余弦相似度/欧氏距离、向量数据库
- **LangChain**、**LangGraph**
- **MCP**:⭐JSON-RPC、通信方式、生命周期、工具发现/调用
- **Skills**:YAML Frontmatter、Markdown instructions、Bundled Resources、各平台支持、渐进式披露(只有 description 常驻上下文)、pi 的 skill 发现规则(递归扫含 SKILL.md 的目录、`disable-model-invocation`)
- ⭐**本库自建摄入体系**(`skills/`,均 `kg-` 前缀,详见 `skills/README.md`):
  - **分层摄入原则**(写进 AGENTS.md):L0 白拿平台现成文字(B站CC/AI字幕、公众号正文、播客shownotes、PDF文字层)→ L1 本地转换(ASR/OCR,一次投入永久复利)→ L2 多模态精准补充(暂不做);为何不用原生多模态当主线(每次付费无复利)
  - **架构**:底层库 `kg-media-to-text`(素材→文字,按类型分流,平台无关) + 上层 `kg-bilibili`/`kg-wechat`/`kg-xiaoyuzhou`/`kg-doc`(各平台适配+沉淀);转换沉底层复用、沉淀归上层
  - **工具选型**:PDF→Docling(版面感知/含RapidOCR) vs MarkItDown(Office);ASR→**Mac 用 mlx-whisper(Metal) / Linux 用 faster-whisper(CUDA)**,因 faster-whisper 不支持 Apple MPS;yt-dlp 是下载层(搬运平台现成字幕≠ASR)
  - **踩坑**:bilibili-api-python 裸装不带 HTTP client(须装 curl_cffi 并 select_client);curl_cffi 的 stream Response 不支持 with;小宇宙官方逐字稿需鉴权且 token 抓取有封号风险;gitignore 对已追踪文件无效(须 git rm --cached)
- **Agent**:Claude Agent、Project Contract、Build/Test、Architecture Boundaries、Coding Conventions
- **Harness**、**DeepAgents**(上下文管理/虚拟文件系统/任务规划/子智能体/异步子智能体)
- ⭐**浏览器自动化调研**:CDP 核心、Puppeteer、Chrome DevTools MCP 深度实践、Playwright/Lightpanda
- ⭐**Chrome DevTools MCP**:架构解析、通信协议选型、连接排查、复用浏览器实例、带登录态启动
- ⭐**Claude Code MCP 调用机制**:Shell 调用 vs 直接 MCP、stdin/stdout 通信、exec 作用
- ⭐**AI Agent 的可验证开发体系**(`wiki/AI/`,蒸馏B站「数字黑魔法」视频):90% 时间耗在手动验证的真痛点(慢/脆/盲三层)、验证的不对称性与 Verifier's Law(Jason Wei;原文用 verifier's *rule*)、生成便宜验证贵才是根因、**把难验证亲手改造成易验证**、芯片验证行业类比(验证人力是设计 2~3 倍、EDA 让写码变便宜后价值转移到验证体系)、面向 AI Agent 开发的三个判据(离开 UI 还跑不跑/中间状态可读/有无给 AI 的接口)、MCP 模拟 UI vs 前后端分离取舍、ACI(Agent-Computer Interface,SWE-agent 论文:Agent 是全新一类用户)、**两层裁判**(确定性 assertion + 干净上下文的 LLM supervisor 做量化打分而非判对错)、借自芯片的 assertion/coverage/scoreboard、happy path 固化+线上捞案例、**每功能配 feature flag 做开关对照归因**、codex 闭环(先设计回归测试→flag→实现→开关双跑→收敛,人只定义什么算对)
- ⭐**AI Native 时代的研发组织**(`wiki/AI/`,详细蒸馏阿里技术许晓斌文章):AI=新协作主体(非工具)、组织双层结构(Harness 层结构化 AI 主导 / Hive Mind 层松散人主导、叠加非替代)、Org Chart→Execution Graph(节点=任务+上下文+权限+工具、reorg 季度→week)、人既是瓶颈也是兑底、新瓶颈=信息形态的人形偏置(人肉中间件/Harness Engineering/AI 友好 5 维度)、管理塔缩非消失、Architect 最高杠杆点、Agent=新员工阶层、Platform 三柱(Agent Platform Group/Domain Teams/Risk & Oversight)、Death of ego 有边界(杀防御性护生产性、AI stateless 做不到创新)、蒸馏焦虑/培养断裂、Harness 与 Execution Graph 双复利
- ⭐**KimiCode Agent 架构演进**(`wiki/AI/`,详细蒸馏知乎文章):Kimi 终端 Agent 从 Python 整体重写为 TypeScript。**分发**:Node.js SEA + postject 做单二进制(tsdown打包→SEA blob→postject注入→codesign→验证五步),打破"TS不适合做CLI"偏见——关键在构建工程不在语言;为何弃 Bun(官方能力更可控/签名友好/Bun 正被 Anthropic 收购重构中)。**TUI**:弃 React 系 Ink 选 pi-tui(Agent界面=流式滚动+固定输入区/浮动弹窗的混合形态、React reconciler diff 在长会话是负担、减依赖利于单二进制体积)、reverse-rpc 解耦 TUI 与核心(可独立测试/换前端/背压控制)。**最重要**:核心抽象跨语言成立 → **Agent 架构模式正在收敛**——kosong(LLM多provider抽象+Zod编译期类型安全,优于Pydantic)、kaos(POSIX-like执行抽象:exec/readText/stat/iterdir→SSH/SFTP原子映射,故能统一操作任何机器)、agent-core分层(loop含run-turn/turn-step/tool-call/tool-scheduler/retry + session/tools/mcp/skill/rpc)、Wire/ACP协议;工具集Python↔TS一一对应说明"重写只换实现不换产品定义"。语言只是实现层,**Agent 的"操作系统化"才是本质**

## 09 Python

- **语法**(⭐前端视角对比系列):变量与赋值(解包/名字绑定)、数据类型(int/float/Decimal/bytes)、运算符(链式比较/短路)、函数(*args/**kwargs/5种参数形态)、类与对象(classmethod/dataclass/类属性坑)、推导式(列表/字典/生成器表达式)、字符串(f-string)、内置函数(zip/enumerate/sorted key)、注释与 docstring
- **环境配置**(⭐):⭐方案对比与选择(三层心智模型)、pyenv、uv、venv 与 pip
- **框架**:pydantic(配置管理/FastAPI)、FastAPI、uvicorn

## 10 沟通 / 话术

- ⭐**深度关系与自我表露**(`wiki/沟通/`,蒸馏《纵横四海》EP81 解读斯坦福 Connect / Touchy-Feely 课,4.5h):深度关系六特征、**两根支柱**(自我表露=门槛 / 反馈与冲突=技能)、**深≠话题高级而=表露自己**(聊不深不是缺话题)、感受>事实>解法(给解法其实是服务自己)、**15% 法则**(三圈模型/降级阶梓/不只看内容还看关系长度)、**软弱≠脆弱**(脆弱=对反应失控的不确定,不看内容正负)、**rawness 流失**("专业"的代价=把人味精修掉)、**幼儿化对方**(过度保护对方感受=不尊重其成年智慧)、情绪价值=真诚的好奇心(非情绪劳动;三条禁令)、共情vs同情(差在**认同**那一步)、"我不会共情"=注意力在自己身上、**刺痛 pinch→剧痛 crunch**(突然爆发的指责往往只是导火线)、消极叙事与大脑自动收集证据、**三层现实 / 跮网**(意图-行为-影响,任何时刻只掌握两层;跮网=指责→防御)、**XYZ 行为反馈**(小孩天生会;职场版 X+Z;被指责时的反向公式)、**"我觉得"→"我认为"判别观点 vs 感受**、用情绪压制情绪(说"别带情绪"的人最有情绪)、**性格难改但行为可改**(先改行为让认知跟上;"P 人的 J 法")、公平感/杀鸡取卵/情感退缩会让渡权力、**逐回合拒绍话术**("那你要跟我交换吗"/"太贵不是你一人说了算")、越界与**为你好≠控制欲**(判据:决策权还给你)、**金缮 kintsugi**、深度关系不进则退、爱情vs友情(**承诺而非意愿**;友情修复窗口更窄)、渐行渐远=不能再分享脆弱、朋友 portfolio 多元、feeling emotionally met、讨好=对自己的深度隐藏、不存在纯粹(对齐诉求而非真心换真心)、**唯一失败案例**(技巧齐全仍可能失败——诉求不匹配)
- ⭐**转移回答的层级**(`wiki/沟通/`,蒸馏B站房石阳明话术解析第48期):不转移**话题**而转移**回答层级**("是不是真的"→"你为什么这么想")、承认推理有依据≠承认结论正确、三种可复用句式(回应对方的在意/判断的依据/问题本身)、元沟通 metacommunication(内容层 vs 元层;视频字幕误作"语言沟通")、**Artful Dodger 实证**(听者默认注意力在"我喜不喜欢你"而非"你答没答";三种被识破条件——被要求判相关性/偏离过大/**问题文字持续可见→书面沟通风险高**;流畅答错问题评价高于结巴答对)、失效后退而不破(不说死)、**真正目标是让两种可能同时存在**而非被相信、天平校正与火力转移、"赢"往往只需不被排在优先处理位

## 99 其他 / 记录 / 求职

- **求职**:⭐八股记录(nextTick/vuex/redux/虚拟DOM/axios/rem适配/防抖等大量面试题)、实习学习、求职指导
- **记录**、**其他**

---

_最后更新:见 log.md。此索引扫描 archive 旧笔记标题生成,后续随 wiki 增长手动维护。_
