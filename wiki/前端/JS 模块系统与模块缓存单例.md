# 1. JS 模块系统与「模块缓存 = 单例」

> 由旧笔记 `archive/03 前端/07 NodeJS/分支-NodeJS/模块化.md` 蒸馏升级而来(排查 antd 依赖冲突时用到)。
> 升级说明:[[../../raw/模块化-旧笔记升级说明.md]]
> 相关:[[npm 与 pnpm 依赖冲突]]
>
> 核心认知:**JS 里没有显式的「单例模式」代码,单例是模块系统「同一路径只执行一次、结果被缓存复用」这个特性天然给的。** 理解这一点,才能理解 React/antd 为什么要求「只能有一份」,以及依赖冲突为什么危险。

---

## 1.1 一句话结论

> **只要 bundle / 运行时里某个模块的物理文件只有一份,所有 import 它的地方拿到的就是同一个实例——这就是「单例」。反之,同名库出现在两个不同路径,就是两份实例,单例破裂。**

这条结论是后面所有内容的锚点。CommonJS 和 ESM 实现细节不同,但都遵守它。

---

## 1.2 CommonJS(Node `require`)的缓存机制

### 1.2.1 缓存怎么工作

第一次 `require("xxx")` 时没有缓存,Node 会:解析路径 → 读文件 → 包成函数(`compiledWrapper`)→ 执行 → 把结果 `module.exports` 存入缓存。**后续再 require 同一个模块,直接返回缓存里的那份,不再执行第二次。**

```js
// a.js
console.log('模块 a 执行')
module.exports = { count: 0 }

// main.js
const a1 = require('./a')   // 打印「模块 a 执行」
const a2 = require('./a')   // 不打印,直接读缓存
a1.count = 5
console.log(a2.count)       // 5  —— a1 和 a2 是同一个对象
console.log(a1 === a2)      // true
```

`a1 === a2` 为 true 正是单例的体现:两次 require 拿到同一个导出对象。

### 1.2.2 缓存的 key 是「文件绝对路径」(关键)

> 旧笔记原话:「模块缓存**使用文件地址来做判断**」——这句是理解依赖冲突的钥匙。

Node 的缓存挂在 `require.cache` 上,**key 是解析后的文件绝对路径**。这意味着:

- 同一个文件,不管从哪 require、写不写 `.js` 后缀,解析到同一个绝对路径 → 同一份缓存 → 单例。
- **同名库但物理路径不同**(如 `项目/node_modules/antd` 与 `项目/node_modules/zant-ui/node_modules/antd`)→ **两个不同的 key** → 各建一份缓存 → **两份实例**。

这直接解释了 [[npm 与 pnpm 依赖冲突]] 里 antd v4/v5 为什么会变成两份、单例为什么破裂。

### 1.2.3 加载顺序细节(来自旧笔记,核对正确)

- `require` 后被引入的代码会**同步、立即执行一次**;执行顺序是「先跑被引入模块,再回到当前模块」。
- 采用**深度优先**:`a → c → d → e` 走到最深再回溯。
- 每个模块的 `module.loaded` 记录是否已加载;循环依赖时,拿到的是「当前已执行到的、可能不完整的」exports(这是 CJS 循环依赖坑的根源)。

---

## 1.3 ESM(`import`/`export`)的缓存机制

ESM 同样保证单例,但机制和 require 有本质区别。

### 1.3.1 Module Map:ESM 的「缓存表」

宿主(浏览器/Node)维护一张 **Module Map**,key 是模块的**解析后 URL / 绝对路径**,value 是模块记录。一个模块只会被 fetch、parse、evaluate **一次**,之后所有 import 复用同一条记录。所以:

```js
import { x } from './m.js'   // 多处 import './m.js'
// 只要解析到同一个 URL,拿到的就是同一个模块实例(单例)
```

结论和 CJS 一致:**单例的边界 = 解析后的路径是否相同**。

### 1.3.2 live binding(实时绑定)—— 和 CJS 的核心差异

- CJS:`module.exports` 是**值/引用的一次性拷贝**。require 拿到的是「导出那一刻」的那个对象引用。
- ESM:import 进来的是对导出变量的**实时绑定(live binding)**,指向导出模块环境记录里的同一个「格子」。导出方后来改了这个变量,导入方读到的是新值。

```js
// counter.js
export let count = 0
export function inc() { count++ }

// main.js
import { count, inc } from './counter.js'
console.log(count)  // 0
inc()
console.log(count)  // 1  —— live binding,CJS 里这样是拿不到更新的
```

> 注意:live binding 是「变量绑定实时」,不是「深拷贝共享」。对引用类型,CJS 和 ESM 都能通过共享的对象地址看到内部字段变化;区别在于**对导出变量本身重新赋值**时,只有 ESM 能同步。

### 1.3.3 静态 vs 动态

- ESM 的 `import`/`export` 是**语法关键字,在解析阶段(执行前)就确定**,所以能做静态分析(tree-shaking、打包依赖图、eslint 扫描)。因此 `import` 不能写在 `if` 里、路径不能动态拼接。
- CJS 的 `require` 只是个**普通函数**,运行时才执行,可以放在 `if` 下、路径可动态拼接——代价是静态分析工具「看不懂」它。
- 需要运行时按条件加载时,ESM 用 `import()`(动态导入,返回 Promise);CJS 里也能用 `import()` 加载 ESM(因为 require 是同步的,没法直接 require 一个异步的 ESM)。

---

## 1.4 为什么这条认知能撑起「依赖单例」

把 1.1 的结论套到组件库上,就理解了 peer dependency 的意义:

1. **React 的 hooks** 靠模块级的「当前 dispatcher」全局变量工作。两份 React = 两个 dispatcher → `Invalid hook call`。
2. **antd 的 ConfigProvider 主题** 靠 `createContext()` 创建的 context 对象传递,这个对象也是模块单例。两份 antd = 两个不同的 context 对象 → Provider 包不住另一份的组件 → 主题失效。
3. **antd 的 message/Modal 静态方法** 是模块级变量 `messageInstance`,两份 antd = 两个实例。
4. **antd v5 的 cssinjs 样式缓存** 是模块级 Map,两份 = 重复注入。

这些「单例」全都建立在 §1.1 那条地基上。所以 `peerDependencies` 的唯一使命,就是**强制 bundle 里只有一份物理文件**,让上面这一整套隐式单例成立。一旦版本冲突 / hoisting 失败导致出现两份路径,整个单例体系从地基塌起——详见 [[npm 与 pnpm 依赖冲突]]。

---

## 1.5 速查

| 维度         | CommonJS                | ESM                  |
| ---------- | ----------------------- | -------------------- |
| 缓存表        | `require.cache`         | Module Map           |
| 缓存 key     | 文件绝对路径                  | 解析后 URL/路径           |
| 单例边界       | 同路径=同实例                 | 同 URL=同实例            |
| 导出绑定       | 一次性引用拷贝                 | live binding(实时)     |
| 解析时机       | 运行时(函数调用)               | 解析阶段(静态)             |
| 动态加载       | `require()` 本就动态        | `import()`           |
| 单例被破坏的典型原因 | 同名库落在不同 node_modules 路径 | 同上 + 多次打包/多 chunk 重复 |
