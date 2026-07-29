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
- **网络 / 泛域名**(⭐系列 7 篇,`wiki/网络/`):概念辨析(泛域名/泛解析/通配符证书)、DNS 泛解析与查询链路、通配符 HTTPS 证书(SAN/只覆盖一级)、nginx 泛域名转发、同源策略与 CORS、Cookie 跨子域与 postMessage
- **Chrome Cookie 存储与加密**:⭐浏览器 Cookie 本地存储与登录态搬运(磁盘加密/Keychain/AES-128-CBC/32字节host hash前缀/App-Bound Encryption/DBSC终局约束 → wiki/网络)
- **Obsidian webview 登录态注入**:⭐Obsidian webview 的 Electron 源码分析(partition 设计/partition/remote API/注入方案/路径对比/市场现状/设计方案 → wiki/网络)
- **Obsidian 插件开发**:⭐入门实战索引(`wiki/obsidian/`):骨架速查(三件套/生命周期/API/esbuild)+ 实战坑(官方模板与 lint=审核标准/**不能分发原生模块→纯JS+系统命令**/软链+HotReload+watch 调试/@electron/remote 灰色 API/i18n/发版全流程/BRAT)
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
- ⭐**Node.js 子进程管理 spawn**(`wiki/NodeJS/`):spawn vs exec/fork、stdio 三管道与背压、僵尸与孤儿进程、信号语义(SIGTERM/SIGKILL)、进程组与 detached、跨平台差异、CLI 调子进程的踩坑清单
- **Uniapp**:⭐跨平台原理、环境配置(网页/小程序/Android/mumu模拟器)、pages.json/manifest.json、uni-ui/uni-forms、页面通讯(setup传参/事件总线)、⭐网络请求封装(RequestService)、pinia、⭐蘑菇街项目(多端适配/条件编译/图片懒加载/三端发布)、easycom、#ifndef 条件编译
- **NuxtJS**、**NextJS**、**Electron**、**Uniapp**

### 富文本 / 编辑器
- ⭐**QuillJs**:换行 bug、`<br>` 被忽略、单独视频/图片后光标无法定位(文档必须以 `\n` 结尾)、BrBlot workaround vs 数据层归一化、clipboard matcher(→ wiki/前端,学堂系统实践)

### 模块化
- ⭐**JS 模块系统**:模块化历史(NoModule/AMD/CMD)、CommonJS(exports vs module.exports 内存引用、寻址规则、Module 对象本质/compiledWrapper)、ESM(静态分析、live binding、import()、顶层 await、Node .mjs/type:module)、CJS↔ESM 互操作、⭐**模块缓存=单例**(缓存按文件路径 key,React/antd 隐式单例的地基 → wiki/前端)

### 工程化 / 其他
- 工程化、Webpack、Vite、微前端、单元测试、Bun、前端可视化
- ⭐**运行时动态 base / publicPath**(`wiki/前端/`,泛域名系列重头):编译期 vs 运行时 base、webpack `__webpack_public_path__`/`.p`/动态建 script 加载 chunk、Vite 三方案、vite-plugin-dynamic-base 源码级原理、一次构建多处部署
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
- ⭐**AI Agent 的可验证开发体系**(`wiki/AI/`,蒸馏B站视频):验证的不对称性、芯片验证行业类比、先改造系统再写测试、为不确定系统构建回归测试、人退出内环、作者自己的免责声明
- ⭐**Graph Engineering 与多智能体编排**(`wiki/AI/`,蒸馏腾讯技术工程文章+核实 Anthropic 原始数据):**五层演进**(Prompt→Context→Harness→Loop→Graph,层层叠加非取代)、Loop 的**五个结构性缺陷**(上下文腐烂/错误级联/工具过载15~20个后选错/无控制粒度/可观测性差)、**目标失明与古德哈特定律**(客服"工单解决率"涨5个月而流失率翻倍——循环完美运行而成功恰是失败机制)、**G=(V节点,E边,S状态,P策略)**、Graph≠流程图≠知识图谱、三种拓扑(**菱形扇出扇入**/主管Orchestrator-Workers/流水线)、Anthropic **五种工作流模式**(Prompt Chaining/Routing/Parallelization/Orchestrator-Workers/Evaluator-Optimizer)、**核心价值是确定性不是智能体数量**、**Verifier验证器**(职责是推翻而非重写;必须干净上下文)+Router分诊、三种验证打法(对抗式/多视角/评委制)、**让模型判断落在节点、代码可靠性落在边上**、**必须有现实锚点**(否则是"项目管理更好的更大幻觉")、**成本三数字**(多智能体强90.2%但烧15×token、token用量解释80%方差;**换更好模型>翻倍token预算**)、该用的三把尺子(上下文保护/可并行/专业化)、**每天跑的任务值得上图、只跑一次就是纯税**、**工作图快变 vs 角色图慢变**(权限绝不能让模型现场发挥)、LangGraph **持久化执行**(checkpointer/super-step/pending writes/时间旅行/人在回路)、框架 token 差异(图把"对话"变"状态转换")、老工作流vs ReAct vs Graph(**边固定+节点自主**,形似神不似)、**识别技术营销的判据**(新词诞生时有无伴随新能力发布)
- ⭐**AI Native 时代的研发组织**(`wiki/AI/`,详细蒸馏阿里技术文章):AI=新协作主体、Harness层+HiveMind层双层结构、Org Chart→Execution Graph、人既是瓶颈也是兜底、信息形态的人形偏置(人肉中间件)、管理塌缩、Architect 最高杠杆、Platform 三柱、Death of ego 有边界
- ⭐**KimiCode Agent 架构演进**(`wiki/AI/`,详细蒸馏知乎文章):Node.js SEA+postject 单二进制分发(打破"TS不适合做CLI"偏见)、弃 React 系 Ink 选 pi-tui、kosong(LLM抽象)/kaos(POSIX-like执行抽象)跨语言成立 → **Agent 架构正在收敛**。⭐含主人对照本库 skills 体系的原创判断

## 09 Python

- **语法**(⭐前端视角对比系列):变量与赋值(解包/名字绑定)、数据类型(int/float/Decimal/bytes)、运算符(链式比较/短路)、函数(*args/**kwargs/5种参数形态)、类与对象(classmethod/dataclass/类属性坑)、推导式(列表/字典/生成器表达式)、字符串(f-string)、内置函数(zip/enumerate/sorted key)、注释与 docstring
- **环境配置**(⭐):⭐方案对比与选择(三层心智模型)、pyenv、uv、venv 与 pip
- **框架**:pydantic(配置管理/FastAPI)、FastAPI、uvicorn

## 10 沟通 / 话术

- ⭐**深度关系与自我表露**(`wiki/沟通/`,蒸馏B站视频):自我表露的深度层级、互惠性与节奏匹配、脆弱性的门槛效应、关系升温的具体路径、常见误区(过快过深/单向倾倒)
- ⭐**转移回答的层级**(`wiki/沟通/`,蒸馏B站房石阳明话术解析):不想回答时的高阶闪避、层级转移(具体→抽象/个人→普遍)、让对方以为已被回答的机制、素材取自《人狼村之谜》

## 99 其他 / 记录 / 求职

- **求职**:⭐八股记录(nextTick/vuex/redux/虚拟DOM/axios/rem适配/防抖等大量面试题)、实习学习、求职指导
- **记录**、**其他**

---

_最后更新:见 log.md。此索引扫描 archive 旧笔记标题生成,后续随 wiki 增长手动维护。_
