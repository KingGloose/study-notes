# 1. 前端运行时动态 base 完全指南(webpack vs Vite)

> 泛域名系列(5/7,重头篇)。上一篇:[[../网络/nginx 泛域名转发]]。下一篇:[[../网络/同源策略与 CORS]]。
> 由 `raw/泛域名-新OA接入处理-原文.md`、`raw/泛域名-前端代理思考和分析-原文.md` 引出并大幅展开。
> 相关:[[JS 模块系统与模块缓存单例]](import()/chunk 加载的底层)。
>
> 前四篇把请求送到了机器、由 nginx 按子域名分流,并直吐前端静态产物。这篇解决最后、也是前端唯一要动手的一环:**同一份构建产物,部署/访问在不同域名下时,它引用的 js/css/图片该用什么前缀去加载?** 核心矛盾是——传统 `base` 是**编译期写死**的,而泛域名要求**运行时才知道**该去哪个域名取资源。

---

## 1.1 问题的本质:编译期 base vs 运行时 base

### 1.1.1 什么是 base / publicPath

前端构建工具打包后,`index.html` 里引用资源要带一个前缀:

```html
<script src="/assets/index.abc123.js"></script>
<img src="/assets/logo.03d6d6da.png">
```

这个前缀(`/assets/` 前面那段)就是 **base(Vite)/ publicPath(webpack)**。它决定「运行时去哪里加载后续资源」。可以是:

- 相对根:`/`
- 子路径:`/my-app/`
- 独立 CDN / 静态域名:`https://s1.zhuanstatic.com/proj/`

### 1.1.2 传统方式的死穴:编译期写死

无论 webpack 的 `output.publicPath` 还是 Vite 的 `base`,默认都是**打包那一刻就把前缀固化进产物**。一旦构建完成,产物里的路径就定死了:

```
构建时 base = https://s1.zhuanstatic.com/proj/
→ 产物里所有资源路径都硬编码成 https://s1.zhuanstatic.com/proj/assets/xxx
→ 换个域名访问,资源还是去 s1.zhuanstatic.com 取
```

这在泛域名场景直接崩:`oa-zhangjiahui04.test...` 和 `oa-lisi.test...` 访问的是**同一份产物**,但资源应该分别落到各自机器的 docker 里(见 [[../网络/nginx 泛域名转发]] §1.5)。编译期写死做不到「一份产物、按访问域名动态取资源」。

**目标**:让 base 变成运行时变量——页面加载时才根据当前环境(域名/全局变量)决定资源前缀。这就是「运行时动态 base」,等价于 webpack 的 `__webpack_public_path__` 能力。

---

## 1.2 webpack 是怎么做到的(参照系)

webpack **原生支持**运行时动态 publicPath,理解它是理解 Vite 方案的基础。

### 1.2.1 `__webpack_public_path__` → `__webpack_require__.p`

webpack 暴露一个魔法变量 `__webpack_public_path__`,你在**入口最顶部**给它赋值,就能在运行时改 publicPath:

```js
// 入口文件第一行,必须在任何 import 之前
__webpack_public_path__ = window.dp || '/'
```

打包后,webpack 会把 `__webpack_public_path__` 编译成内部运行时变量 **`__webpack_require__.p`**。产物里所有资源加载都用 `.p` 做前缀拼接。所以给 `__webpack_public_path__` 赋一个运行时才确定的值(如 `window.dp`),就实现了动态 base。

> 术语对齐(原始文档记录):文档里看到的 `__webpack_require__.p = window.dp || ''`,就是这个机制——把运行时全局变量 `window.dp` 作为 publicPath。

### 1.2.2 chunk 加载:`__webpack_require__.e` 就是「重写版 import」

webpack 把代码分割后的动态 `import()` 编译成 `__webpack_require__.e(chunkId)`。它的本质是**动态创建 `<script>` 标签**去加载 chunk,而 `src` 正是用 `.p` 动态拼出来的:

```js
// webpack 运行时(简化)requireEnsure / __webpack_require__.e
__webpack_require__.e = function (chunkId) {
  // 1. 已加载/加载中则复用缓存的 Promise
  // 2. 新建 Promise 缓存到 installedChunks
  var promise = new Promise(function (resolve, reject) {
    installedChunks[chunkId] = [resolve, reject]
  })
  // 3. 创建 script,src 用 .p 前缀动态拼接  ← 关键
  var script = document.createElement('script')
  script.src = __webpack_require__.p + 'static/js/' + chunkId + '.' + hash + '.js'
  // 4. 设置超时和 onload/onerror 回调,失败则 reject
  document.head.appendChild(script)
  return promise
}
```

**为什么这套天然支持动态 base**:因为 chunk 的 URL 是在**运行时**用 `.p` 拼的,而不是编译期写死。只要页面加载时 `__webpack_require__.p` 已经是正确的运行时值,后续所有按需 chunk、图片、字体都会自动带上正确前缀。

这也是 `__webpack_public_path__` 必须在**所有 import 之前**赋值的原因:一旦开始加载 chunk,`.p` 就被读取了,晚赋值就来不及。

---

## 1.3 Vite 的困境:原生不支持

Vite 的 `base` 是**纯编译期**的。生产构建时 `base` 被字符串替换进产物,运行时没有 `__webpack_public_path__` 这种可改的钩子。原因和 Vite 的产物形态有关:

- Vite 生产用**原生 ESM**,`import()` 是浏览器原生的,URL 在打包时就解析确定,没有 webpack 那层「自己重写的 `__webpack_require__.e`」可以插手。
- 资源引用(`new URL('./x.png', import.meta.url)`、css 里的 `url()`)也都是构建期确定。

所以 Vite 要实现运行时动态 base,**只能想办法在产物生成后再改**。原始文档里评估了三种方案。

---

## 1.4 Vite 三种方案对比(来自原始文档的决策)

### 1.4.1 方案一:自己重写 `import()`

**思路**:劫持/包装动态 import,运行时给 chunk URL 加上动态前缀。

- 优点:简单直接、可行。
- 缺点:**只能覆盖 JS**。css 里的静态资源(`background: url(...)`)、`<img>`、字体等不走 import,需要额外处理。覆盖不全是硬伤。

### 1.4.2 方案二:改造 beetle(内部构建平台)读 `.beetle.config.js`

**思路**:让内部构建平台在打包时读项目配置注入部署信息。

- 卡点:**打包时拿不到部署的目标 IP/机器**。要做到就得改造 beetle 的编译流程,让「编译」和「部署」两阶段能通信(编译时就知道要丢到哪台机器)。
- 判断(原文观点):这在架构上其实是好方向——项目能反过来驱动 CI 配置、编译部署合流。但**改造成本大、且改动了大家习惯的工作流**,而且目前 beetle 编译/部署各环节独立、不好合并。**结论:pass。**

> 这是一条有价值的「决策 + 权衡」记录:好的方向 ≠ 现在该做,工作流改造成本和团队习惯是真实约束。

### 1.4.3 方案三:用 `vite-plugin-dynamic-base` 插件(最终选择)

**思路**:社区已有开源插件([chenxch/vite-plugin-dynamic-base](https://github.com/chenxch/vite-plugin-dynamic-base)),专门给 Vite 补上「类 `__webpack_public_path__`」的运行时动态 base 能力,JS/CSS/静态资源全覆盖。**这是落地选择**,下一节详解原理。

参考:掘金原理文章 `juejin.cn/post/7063016723502333989`。

| 方案 | 覆盖范围 | 成本 | 结论 |
| --- | --- | --- | --- |
| 一 重写 import() | 仅 JS,CSS 静态资源要另处理 | 低 | 覆盖不全 |
| 二 改造 beetle | 理论最彻底 | 高(改 CI + 改工作流) | pass |
| 三 dynamic-base 插件 | JS/CSS/静态资源全覆盖 | 低(装插件+配置) | ✅ 采用 |

---

## 1.5 vite-plugin-dynamic-base 原理精读

### 1.5.1 用法与两段配合

```ts
// vite.config.ts
import { dynamicBase } from 'vite-plugin-dynamic-base'

export default defineConfig({
  // ① base 用一个占位符路径,生产构建时才启用
  base: process.env.NODE_ENV === 'production' ? '/__dynamic_base__/' : '/',
  plugins: [
    dynamicBase({
      // ② 运行时动态前缀变量,默认就是 window.__dynamic_base__
      publicPath: 'window.__dynamic_base__',
      // ③ 是否也动态化 index.html 里的资源(默认 false)
      transformIndexHtml: false,
    }),
  ],
})
```

两个占位符要配对理解:

- **`base: '/__dynamic_base__/'`**:让 Vite 正常打包,但把所有资源前缀都固定成一个**特征字符串** `/__dynamic_base__/`。这不是真实路径,是个「靶子」,方便插件之后精确定位替换。
- **`publicPath: 'window.__dynamic_base__'`**:插件把产物里的靶子 `/__dynamic_base__/` 替换成运行时表达式 `window.__dynamic_base__ + ...`。

### 1.5.2 它替换了什么(结合产物)

插件在构建产物里,把硬编码的 base 靶子替换成运行时拼接。对照实际产物(截图所见):

```js
// 替换前(base=/__dynamic_base__/):
//   "/__dynamic_base__/assets/logo.03d6d6da.png"
// 替换后:
const url = window.__dynamic_base__ + "/assets/logo.03d6d6da.png"
```

覆盖的资源类型(这正是它比「方案一重写 import()」强的地方):

1. **JS chunk**:动态 `import("./About.b8c73c63.js")` 的路径跟随动态前缀。
2. **CSS**:样式表本身 + CSS 内 `background-image: url(...)`。
3. **图片等静态资源**:`logo.xxx.png` 之类打包进来的资源。
4. **legacy 产物**:`index-legacy.xxx.js`、`About-legacy.xxx.js` 里的资源路径同样被改写(配合 `@vitejs/plugin-legacy`)。

### 1.5.3 index.html 与 `preloads`(transformIndexHtml)

`index.html` 里首屏直接引用的入口 script/link/preload 是个特殊情况——它们在**任何 JS 执行前**就要加载,没法靠运行时变量拼。插件开启 `transformIndexHtml` 后的做法是:

- 不再用静态 `<script src>`,而是往页面注入一个 **`preloads` 数组**,每项描述一个待加载资源:

```js
// index.html 内联脚本(产物,简化)
var preloads = [
  { parentTagName: "head", tagName: "script",
    attrs: { type: "module", crossorigin: true, src: "/assets/polyfills-modern.a670d618.js" } },
  { parentTagName: "head", tagName: "script",
    attrs: { type: "module", crossorigin: true, src: "/assets/index.320e629c.js" } },
  { parentTagName: "head", tagName: "link",
    attrs: { rel: "stylesheet", href: "/assets/index.326dd81f.css" } },
]
```

- 然后运行时遍历 `preloads`,给每个 `src`/`href` **拼上 `window.__dynamic_base__`**,再 `document.createElement` 动态创建标签插入 `head`/`body`(按 `parentTagName` 分组、`insertBodyAfter` 控制插入位置)。
- 这样连**首屏入口资源**都变成运行时定位——真正做到「产物里没有任何写死的资源域名」。

> 类比 webpack:webpack 靠 `__webpack_require__.e` 动态建 script 加载 chunk;这里靠 `preloads` + 运行时建标签加载首屏入口。思路同构——**都是把「静态引用」改造成「运行时动态创建标签」**。

### 1.5.4 为什么必须 `enforce: 'post'`

这个插件要改的是**最终产物字符串**,所以必须在 Vite 核心和其它构建插件都处理完之后再跑。Vite 插件执行顺序:

```
Alias → 用户 enforce:'pre' 插件 → Vite 核心插件
      → 用户无 enforce 插件 → Vite 构建插件
      → 用户 enforce:'post' 插件 → Vite 后置构建插件(minify / manifest / report)
```

dynamic-base 走 `post`:等 Vite 把 base 都替换成 `/__dynamic_base__/` 靶子、chunk 都生成好之后,它再在 `post` 阶段统一把靶子换成运行时表达式。放早了产物还没定型,替换会漏或错位。

> 实现细节:早期版本用字符串正则替换,后来重构为用 SWC 解析 AST 精确定位包含 base 的字符串再替换(见 PR #23),避免误伤。

### 1.5.5 运行时怎么给 `window.__dynamic_base__` 赋值

产物依赖 `window.__dynamic_base__` 这个全局变量,它必须在入口脚本执行前就位。常见做法:

```html
<!-- index.html 最前面,先于所有模块脚本 -->
<script>
  // 根据当前访问域名/环境算出资源前缀
  window.__dynamic_base__ = location.origin  // 或从注入的配置读
</script>
```

对应泛域名场景:`oa-zhangjiahui04.test...` 访问时,这里算出的前缀指向它自己那台机器的资源目录;换个人访问,自动指向另一台。**一份产物,运行时按域名各取各的资源**——这就是整条链路要的效果。

---

## 1.6 三个容易漏的坑

1. **CSS 里的静态资源**:`background: url()` 不走 JS import,是「方案一」的死角,也是评估任何自研方案时第一个要验证的点。dynamic-base 覆盖了,自己写要特别处理。
2. **legacy / polyfill 产物**:上了 `@vitejs/plugin-legacy` 会额外产出 `*-legacy.js`(SystemJS 格式)和 polyfill。这些产物里的资源路径**也要**被动态化,否则老浏览器加载 legacy chunk 时前缀又错了。dynamic-base 声明兼容 plugin-legacy 正是为此。
3. **PWA(sw.js / manifest)**:上了 `vite-plugin-pwa` 会产出 `sw.js`、`workbox-*.js`、`manifest.webmanifest`。Service Worker 的 scope 和预缓存清单里的资源路径在动态 base 下要格外小心(sw 的作用域受它自身 URL 路径限制)。dynamic-base 声明兼容 pwa,但接入时要实测缓存路径是否正确。

---

## 1.7 一次构建、多处部署:动态 base 的价值

把整篇收束成一句话:**运行时动态 base 让「构建产物」和「部署位置」彻底解耦。**

- 传统编译期 base:环境 × 域名 有几种,就要构建几次(或维护几套配置)。
- 运行时动态 base:**构建一次**,产物里资源前缀是运行时变量,部署到任何机器/域名/CDN,加载时按 `window.__dynamic_base__` 各自定位。

这正是泛域名 `oa-{任意人}.test.zhuanspirit.com` 能共用一份产物、又能各取各机器资源的前端基础。webpack 靠原生 `__webpack_public_path__`,Vite 靠 dynamic-base 插件补齐同等能力。

---

## 1.8 速查

| 维度 | webpack | Vite(原生) | Vite + dynamic-base |
| --- | --- | --- | --- |
| 运行时改 base | ✅ `__webpack_public_path__` | ❌ 编译期写死 | ✅ `window.__dynamic_base__` |
| 机制 | `.p` 拼 chunk URL,`__webpack_require__.e` 动态建 script | 原生 ESM,URL 构建期定 | `post` 阶段把 `/__dynamic_base__/` 靶子换成运行时表达式 |
| 覆盖范围 | JS/CSS/图片全 | — | JS/CSS/图片/legacy 全,index.html 靠 preloads |
| 赋值时机 | 所有 import 之前 | — | 入口脚本前设好 `window.__dynamic_base__` |

**一句话**:动态 base 的本质,是把资源前缀从「打包那一刻的字符串」变成「页面加载那一刻的变量」;webpack 原生给了,Vite 靠 dynamic-base 在 `post` 阶段替换产物补上。

---

## 1.9 相关知识

- [[../Flutter/Flutter 项目初始化与移动端工具链]]：从 Vite/Webpack 的前端工程化心智模型迁移到 Flutter CLI、Gradle 与多平台宿主工程。
