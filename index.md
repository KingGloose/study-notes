# 知识索引 · 唤醒地图

> 这份索引的作用是**唤醒**:列出我接触过的知识点关键词,让脑子里"知道这个东西存在"。
> 详细内容大多在 `archive/`(旧笔记归档)。需要细节时,问 AI 或翻 archive 对应文件。
>
> - 通用知识点(AI 能直接答的)也全部保留在这里,因为"知道它存在"本身就是价值。
> - 新沉淀的知识进 `wiki/`,原始资料进 `raw/`。
> - 带 ⭐ 的是近期深度笔记 / 有个人实践上下文的内容,价值更高。

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
- **Skills**:YAML Frontmatter、Markdown instructions、Bundled Resources、各平台支持
- **Agent**:Claude Agent、Project Contract、Build/Test、Architecture Boundaries、Coding Conventions
- **Harness**、**DeepAgents**(上下文管理/虚拟文件系统/任务规划/子智能体/异步子智能体)
- ⭐**浏览器自动化调研**:CDP 核心、Puppeteer、Chrome DevTools MCP 深度实践、Playwright/Lightpanda
- ⭐**Chrome DevTools MCP**:架构解析、通信协议选型、连接排查、复用浏览器实例、带登录态启动
- ⭐**Claude Code MCP 调用机制**:Shell 调用 vs 直接 MCP、stdin/stdout 通信、exec 作用
- ⭐**AI Native 时代的研发组织**(`wiki/AI/`,详细蒸馏阿里技术许晓斌文章):AI=新协作主体(非工具)、组织双层结构(Harness 层结构化 AI 主导 / Hive Mind 层松散人主导、叠加非替代)、Org Chart→Execution Graph(节点=任务+上下文+权限+工具、reorg 季度→week)、人既是瓶颈也是兑底、新瓶颈=信息形态的人形偏置(人肉中间件/Harness Engineering/AI 友好 5 维度)、管理塔缩非消失、Architect 最高杠杆点、Agent=新员工阶层、Platform 三柱(Agent Platform Group/Domain Teams/Risk & Oversight)、Death of ego 有边界(杀防御性护生产性、AI stateless 做不到创新)、蒸馏焦虑/培养断裂、Harness 与 Execution Graph 双复利

## 09 Python

- **语法**(⭐前端视角对比系列):变量与赋值(解包/名字绑定)、数据类型(int/float/Decimal/bytes)、运算符(链式比较/短路)、函数(*args/**kwargs/5种参数形态)、类与对象(classmethod/dataclass/类属性坑)、推导式(列表/字典/生成器表达式)、字符串(f-string)、内置函数(zip/enumerate/sorted key)、注释与 docstring
- **环境配置**(⭐):⭐方案对比与选择(三层心智模型)、pyenv、uv、venv 与 pip
- **框架**:pydantic(配置管理/FastAPI)、FastAPI、uvicorn

## 99 其他 / 记录 / 求职

- **求职**:⭐八股记录(nextTick/vuex/redux/虚拟DOM/axios/rem适配/防抖等大量面试题)、实习学习、求职指导
- **记录**、**其他**

---

_最后更新:见 log.md。此索引扫描 archive 旧笔记标题生成,后续随 wiki 增长手动维护。_
