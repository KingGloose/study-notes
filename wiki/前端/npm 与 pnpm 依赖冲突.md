# 1. npm / pnpm 依赖冲突与 peer dependency

> 项目背景:学堂系统(antd v4)接入 zant-ui 富文本组件(依赖 antd v5),peer dependency 版本冲突。
> 原始资料:[[../../raw/npm依赖冲突问题-原文.md]]
> 底层原理:[[JS 模块系统与模块缓存单例]]

---

## 1.1 为什么会冲突:peer dependency + 单例

### 1.1.1 peer dependency(对等依赖)是什么

`package.json` 三种依赖的区别:

| 字段 | 含义 | 谁来装 |
| --- | --- | --- |
| `dependencies` | 运行时需要,由我自己带来 | 装我时自动装进我的 node_modules |
| `devDependencies` | 只在开发/构建时用 | 别人装我时不带 |
| `peerDependencies` | 我需要它,但要求**宿主项目提供,大家共用一份** | 不自动装,宿主负责装 |

组件库(antd、zant-ui、eslint 插件、webpack loader…)把「必须全局唯一」的宿主级框架声明成 peer,语义是:**「请宿主提供一个 X,我不自己带,免得装出两份。」**

判断法则:**这个依赖是不是「必须全局唯一、由宿主主导版本」的宿主级框架?** 是→peer;否→普通 dependency。

### 1.1.2 为什么必须单例(冲突为什么危险)

peer dependency 的目的是保证「只有一份」。为什么这么重要?因为很多库的功能靠**模块单例**工作(底层原理见 [[JS 模块系统与模块缓存单例]]):

- **React hooks**:靠模块级「当前 dispatcher」全局变量。两份 React → `Invalid hook call`。
- **antd ConfigProvider 主题**:靠 `createContext()` 的 context 对象(模块单例)传递。两份 antd → 两个不同 context → 主题传不过去。
- **antd message/Modal 静态方法**:模块级变量,两份 = 两个实例。
- **antd v5 cssinjs 样式缓存**:模块级 Map,两份 = 重复注入。

### 1.1.3 理论合理,现实卡在「版本不可调和」

peer dependency「共用一份」有个隐含前提:**宿主版本落在库声明的范围内**。而本案例宿主是 antd v4、zant-ui 要 v5,v4→v5 是破坏性升级(API、类名、主题方案全变),**根本不存在一个两边都能用的版本**。

于是 peer dependency 的「共用」走不通,只剩两条路:
- **路 A:让 zant-ui 做 v4/v5 兼容适配** —— 组件库不会为某个宿主跨大版本适配,成本高且无动力,对使用方是死路。
- **路 B:放弃共用,改成隔离共存** —— 宿主继续用 v4,zant-ui 用自己的 v5,两份 antd 在同页面井水不犯河水。**这就是最终方案。**

> 认知:最终方案本质上**违背了 peer dependency 的单例初衷**(它想单例,我们却制造两份并隔离)。这不是钻空子,而是版本无法调和时的合理妥协。前提是 zant-ui 富文本组件「自包含」——不跟宿主共享 antd context。
> peer dependency 是**协商机制不是魔法**;协商不出双方都接受的版本时,机制只负责报错,取舍(适配/隔离/升级)由人来做。

---

## 1.2 三个包管理器的表现差异

| 包管理器 | 冲突时默认行为 | node_modules 结构 |
| --- | --- | --- |
| npm (v7+) | ERESOLVE **报错终止** | 扁平 hoist,冲突版本嵌套 |
| pnpm | 非严格模式**只警告**,靠符号链接+内容寻址隔离,允许多版本共存 | 硬链接到全局 store + symlink |
| yarn | 相对宽松 | 扁平 hoist |

pnpm 的「共存」有坑(本案例正好踩到):**共存 ≠ 每个包都链到自己要的版本**。peer dependency 解析会让 zant-ui 优先用宿主提供的 antd(v4),而不是它自己 node_modules 里的 v5——即原文说的「实际链接还是链到项目根目录的 antd」。原理:模块缓存按路径做 key,peer 被解析回了根目录那份路径。

---

## 1.3 强制版本:resolutions / overrides(含纠错)

> ⚠️ 原文写「用 resolutions(使用 npm)」是**不准确**的,复用时要注意:

- `resolutions` 是 **Yarn** 的字段,**npm 本身不认**。`"a/b/c"` 斜杠路径也是 yarn 语法。
- npm 的等价物是 **`overrides`**(npm v8.3+),用嵌套对象结构。
- pnpm 用 **`pnpm.overrides`**,父子用 `>` 分隔。

正确写法对照:
```jsonc
// yarn: resolutions(斜杠路径)
{ "resolutions": { "@ant-design/pro-components/antd": "^5.27.6" } }

// npm: overrides(嵌套对象)
{ "overrides": { "@ant-design/pro-components": { "antd": "^5.27.6" } } }

// pnpm: pnpm.overrides(> 分隔)
{ "pnpm": { "overrides": { "@ant-design/pro-components>antd": "^5.27.6" } } }
```

> 所以原文最终方案里 `"resolutions": { "@zz-common/zant-ui/antd": "^5.24.0" }` 若项目真用 npm 是不生效的。**待确认:当时项目实际用的哪个包管理器 + 哪个字段真正生效。**

### 方案 1/2 为什么解决不了根本问题(原文也这么标注)

- 方案 1 `strictPeerDependencies: true` 只是让冲突**更早报错**,不是让两版本正确共存。
- 方案 2 `publicHoistPattern: ["*antd*"]` 把 antd 提升到顶层,反而**强化「大家都用同一份」**——顶层若是 v4,zant-ui 更拿不到 v5。原文标注「这可能不会解决根本问题」,判断正确。

---

## 1.4 最终方案:resolutions + NormalModuleReplacementPlugin

单靠版本锁定不够,因为**宿主还要继续用 v4**,不能把全项目 antd 强升到 v5。真正的解法是**按 import 来源分流**:
- 宿主代码 import antd → v4;
- zant-ui 内部 import antd → 重定向到 v5。

```js
const path = require('path')
const zantUiAntdPath = path.resolve(
  __dirname,
  '../node_modules/@zz-common/zant-ui/node_modules/antd'
)
const webpack = require('webpack')
config.plugin('ReplaceZantUiAntd').use(webpack.NormalModuleReplacementPlugin, [
  /^antd(\/.*)?$/,
  (resource) => {
    // 按「谁发起的 import」(resource.context)判断来源,只重写 zant-ui 内部的 antd 引用
    if (resource.context && resource.context.includes('@zz-common/zant-ui')) {
      const match = resource.request.match(/^antd(\/.*)?$/)
      const subPath = match ? match[1] || '' : ''
      resource.request = zantUiAntdPath + subPath
    }
  },
])
```

**巧妙点**:在**构建期**按 `resource.context` 判断 import 来源,只把 zant-ui 目录内的 antd 引用改指向 v5 路径,宿主 antd 不动。绕开了 node_modules hoisting 的不确定性,直接在打包解析层隔离两份 antd。

**隐患**:
- 页面会真的同时加载 antd v4 + v5 两份代码,bundle 变大。
- 若 zant-ui 组件需要跟宿主共享 antd context(同一 ConfigProvider 主题),会对不上。仅当富文本组件相对独立时该方案成立。

---

## 1.5 决策速查

| 真实诉求 | 推荐做法 |
| --- | --- |
| 能调和到一个双方都接受的版本 | overrides / resolutions 锁版本即可 |
| 宿主与库大版本不可调和,但库组件自包含 | 按来源分流(NormalModuleReplacementPlugin),接受两份并存 |
| 库组件必须与宿主共享 antd context | 只能升级宿主 or 换组件库,隔离方案会失效 |

> 以上评估为 AI 建议,最终由主人判断拍板。
