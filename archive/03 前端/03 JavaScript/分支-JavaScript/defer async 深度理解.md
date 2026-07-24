# async / defer 与 Vue 首屏请求拦截：一份可读的速查文档

## 背景问题

你在 `index.html` 里额外加了一个脚本（`patch-request.js`）去重写请求处理（比如重写 `fetch/XHR/axios`），并希望它能在 Vue 组件发起请求前生效。  
但你发现：**首次进入页面时，重写并没有影响到最早那一批请求**。

核心原因几乎总是：**脚本执行时序不如你想的那样**，以及/或者 **你 patch 的不是实际请求通道**。

---

## 1. 浏览器到底怎么处理 `<script>`？

浏览器解析 HTML 时，一边解析一边构建 DOM。遇到脚本标签，会触发“下载 + 什么时候执行”的一系列规则。决定顺序的不是“你写在前面”，而是脚本属性与类型。

下面按最常见的几种脚本类型讲清楚。

---

## 2. 普通脚本（无 async / defer）

`<script src="/a.js"></script>`

行为：

- 解析到这里：**停止解析 HTML**
    
- 下载 `a.js`
    
- **立即执行**
    
- 执行完继续解析 HTML
    

特点：

- 执行顺序严格按 HTML 出现顺序
    
- 但会阻塞 HTML 解析（影响首屏）
    

---

## 3. `defer` 脚本

`<script defer src="/patch-request.js"></script>`

行为：

- 解析到这里：**开始下载，但不执行**
    
- HTML 继续解析
    
- 等到 **HTML 解析完成** 后，按它们在页面中出现的顺序执行所有 `defer` 脚本
    
- 执行完 `defer` 队列后，才触发 `DOMContentLoaded`
    

特点：

- **不会阻塞 HTML 解析**
    
- **执行一定发生在 DOM 构建完成后**
    
- **会按顺序执行（相对稳定）**
    
- 但注意：它只保证“HTML 解析完成后才执行”，不保证“比别的脚本更早”
    

一句话：`defer` 是“排队等 DOM 搭好再依次执行”。

---

## 4. `async` 脚本

`<script async src="/vue-app.js"></script>`

行为：

- 解析到这里：**开始下载，但不执行**
    
- HTML 继续解析
    
- **一旦下载完成：立刻执行（会插队）**
    
    - 执行时浏览器会短暂停止 HTML 解析
        
    - 执行完继续解析 HTML
        

特点：

- **不保证顺序**（谁先下载完谁先执行）
    
- **可能在 DOM 还没解析完时就执行**
    
- 适合独立第三方脚本（统计、广告、监控），不适合有严格依赖顺序的启动脚本
    

一句话：`async` 是“下载竞速，谁先到谁先跑”。

---

## 5. `type="module"` 脚本（ESM 模块入口）

`<script type="module" src="/src/main.ts"></script>`

主流浏览器行为近似：

- 类似 `defer`：不会阻塞解析
    
- 一般在 HTML 解析完成后执行（并在 `DOMContentLoaded` 前）
    
- 但模块内部还会加载依赖图（import 的模块）
    

一句话：模块脚本通常是“defer 风格”，但会多一层依赖加载的复杂度。

---

## 6. 你关心的关键组合：`defer patch` + `async Vue`

假设你写的是：

`<script defer src="/patch-request.js"></script> <script async src="/vue-app.js"></script>`

这里会出现“竞速 + 插队”：

### 常见情况（Vue async 先下载完）

- Vue 入口先执行 → Vue 启动 → 请求发出
    
- HTML 解析结束后，`defer patch` 才执行  
    结论：**首波请求拦不住**
    

### 偶发情况（patch 下载快、Vue 下载慢）

- HTML 解析结束 → `defer patch` 执行生效
    
- Vue async 才执行 → 这时请求能被拦住  
    结论：**有时能拦住，有时不行（不稳定）**
    

**所以只要 Vue 入口是 async，你就很难保证 patch 一定先发生。**

---

## 7. “async 会不会在 DOM 没加载完时执行？”

会，而且经常。

这会带来一个实际后果：

- 如果 Vue 入口 async 执行时，`<div id="app"></div>` 还没被解析出来，`mount('#app')` 可能失败（空白/报错）。
    
- 很多人没遇到，是因为 `#app` 通常写在 `<body>` 很靠前的位置。
    

但即便 `#app` 已经存在，Vue 仍然可能在 **DOMContentLoaded 之前**就开始跑逻辑并发请求。

---

## 8. 为什么你“明明把 patch 放在 Vue 前面”，还是不生效？

因为“写在前面”不代表“先执行”。决定先后的是规则：

- `defer`：**等 HTML 解析完**
    
- `async`：**下载完就插队执行**
    
- 普通脚本：**解析到就立即执行**
    

只要你的 Vue 入口脚本是 `async` 或者是普通脚本，而 patch 是 `defer`，就极有可能 Vue 先跑。

---

## 9. 另一个常见坑：你 patch 的不是实际请求通道

就算时序正确，也可能无效：

- 你重写了 `window.fetch`，但项目用的是 XHR（axios 默认很多情况下走 XHR）
    
- 你重写了 XHR，但项目改成 fetch adapter
    
- 项目在更早的地方缓存了引用，例如：
    
    `const rawFetch = window.fetch // 之后一直用 rawFetch，而不是 window.fetch`
    
    这种情况下你后续改 `window.fetch` 也拦不到
    

结论：要确认“请求到底走哪条路”，以及“有没有提前固化引用”。

---

## 10. 最稳妥的工程化方案（按推荐程度排序）

### 方案 A：把 patch 变成入口最早 import（工程最推荐）

在 Vue 入口 `main.ts` 第一行：

`import './boot/patch-request' import { createApp } from 'vue' ...`

这样可以保证它在应用逻辑之前执行（前提是你别在其他模块顶层提前发请求）。

### 方案 B：让 patch 以阻塞脚本形式放在最前（确定性最强）

`<script src="/patch-request.js"></script> <script type="module" src="/src/main.ts"></script>`

patch 通常很小，阻塞成本不高，但确定性拉满。

### 方案 C：避免 Vue 入口使用 async

Vue 入口是启动器，它需要确定的顺序；`async` 天生不保证顺序，不适合当入口。

---

## 11. 一句话总结（可当团队规范）

- **需要顺序**：用 `defer`（并保证关键脚本同为 defer/module）或用阻塞脚本/入口 import
    
- **不需要顺序，只要尽快**：用 `async`（典型：统计、监控、广告脚本）
    
- **“拦首波请求”属于必须有顺序的事情**，所以不要把 Vue 入口搞成 async，让 patch 搞成 defer。
    

---

## 12. 自检小技巧：两行日志看真相

在 patch 顶部：

`console.log('[patch] executed', performance.now());`

在发请求之前：

`console.log('[app] request', performance.now());`

谁的时间小，谁先执行。时序问题一眼判案。

---

这份文档的精髓就是：**defer 是排队，async 是插队**。你要的是“先 patch 再请求”，就别让入口脚本用插队模式。