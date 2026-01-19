先把版本状态说清楚：**截至 2026-01-19，Vue 3.6 还在 beta 预发布阶段（如 v3.6.0-beta.1 / beta.2）**，npm 上 `vue` 的稳定版仍是 **3.5.x（例如 3.5.26）**。 ([GitHub](https://github.com/vuejs/core/releases "Releases · vuejs/core · GitHub"))

在“响应式（reactivity）”这一块，**3.6 相对 3.5 的区别，核心几乎都在“底层实现/性能与内存”**，而不是你日常写的 `ref/reactive/watch` API 语义大改。

## 1) 底层响应式引擎：3.5 的大重构 vs 3.6 的再重构

**Vue 3.5**

- 官方明确写了：响应式系统做了一次“重大重构”，**性能更好、内存显著下降（-56%），并且“行为无变化”**；还修了 SSR 场景里 computed 可能“挂住”导致的内存问题，以及“陈旧 computed 值”问题。 ([Vue 博客](https://blog.vuejs.org/posts/vue-3-5 "Announcing Vue 3.5 | The Vue Point"))
- 另外对“超大、深层响应式数组”的追踪做了优化，某些操作可到 **10x**。 ([Vue 博客](https://blog.vuejs.org/posts/vue-3-5 "Announcing Vue 3.5 | The Vue Point"))

**Vue 3.6（beta）**

- 发布说明里点名：`@vue/reactivity` 又做了“重大重构”，这次是**基于 alien-signals**，目标同样是 **更好的性能 + 更低的内存占用**。 ([GitHub](https://github.com/vuejs/core/releases "Releases · vuejs/core · GitHub"))
- alien-signals 自己的 README 也写得很直白：它在研究一种 **push-pull（推-拉混合）** 的 signal 算法；并提到 Vue 3.5 走向了更“pull-based（偏拉取）”的算法路线，而它的核心算法已被移植到 **Vue 3.6**（PR 引用也给了）。 ([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

**一句话理解差异**：

- **3.5：**“把旧引擎瘦身 + 修 computed/SSR + 大数组加速”，而且宣称行为不变。 ([Vue 博客](https://blog.vuejs.org/posts/vue-3-5 "Announcing Vue 3.5 | The Vue Point"))
- **3.6：**“把引擎核心算法换成 alien-signals 那套（push-pull signals），继续榨性能/内存”。 ([GitHub](https://github.com/vuejs/core/releases "Releases · vuejs/core · GitHub"))

## 2) 开发者感知更强的“响应式相关变化”：主要发生在 3.5

如果你说的“响应式”包含“写起来像不像响应式”，那 **3.5 的变化更显眼**：

- **Reactive Props Destructure 默认开启**：`<script setup>` 里从 `defineProps()` 解构出来的变量默认变“响应式”（编译器会把 `count` 之类访问改写成 `props.count` 跟踪）。 ([Vue 博客](https://blog.vuejs.org/posts/vue-3-5 "Announcing Vue 3.5 | The Vue Point"))
    
- watch 清理能力（`onWatcherCleanup()`）等也在 3.5 作为重要 DX（开发体验）改进被强调。 ([Vue 博客](https://blog.vuejs.org/posts/vue-3-5 "Announcing Vue 3.5 | The Vue Point"))
    

而 **3.6 的 release note 里，响应式部分几乎只强调“引擎重构 + 性能内存”**。 ([GitHub](https://github.com/vuejs/core/releases "Releases · vuejs/core · GitHub"))

## 3) 对你项目的实际影响怎么判断

- **功能语义层面**：3.5 官方说“无 breaking change、行为无变化”（至少对响应式重构这块是这么宣称的）。 ([Vue 博客](https://blog.vuejs.org/posts/vue-3-5 "Announcing Vue 3.5 | The Vue Point"))
- **性能/内存层面**：3.6 的收益更可能出现在“依赖量巨大、computed/watch 特别多、长链路响应式图谱”的项目里。 ([GitHub](https://github.com/vuejs/core/releases "Releases · vuejs/core · GitHub"))
- **风险层面**：3.6 目前是 beta，建议把它当“可试用但要跑回归”的性能升级，而不是无脑生产直上。 ([GitHub](https://github.com/vuejs/core/releases "Releases · vuejs/core · GitHub"))


先把 **alien-signals** 想成一句话：**一个“signals（信号）式”的响应式内核/小库**，提供 `signal / computed / effect` 这类原语（primitive），用来做**细粒度依赖追踪**和**高效更新传播**，并且它的实现重点是“把运行时开销压到极低”。它明确说自己是在探索一种 **push-pull（推-拉结合）** 的 signals 算法，并且为了性能在算法核心里刻意限制了数据结构与递归。([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

---

## 1) alien-signals 是干什么用的？它能干什么？

### 它提供的“能用来干活”的东西

在官方 README 的 Usage 里，你能直接看到它的核心 API：([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

- **signal**：一个“可变的响应式值源”（source）
    
- **computed**：基于 signal 派生的“带缓存的计算值”
    
- **effect**：副作用（依赖变了就重新执行，比如更新 DOM、打日志、触发请求等）
    
- 还有一些偏工程能力的东西：
    
    - **effectScope**：批量管理 effect 的生命周期（stop 后统一清理）([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))
        
    - **Nested Effects**：effect 里再创建 effect，会自动清理上一轮创建的内层 effect（避免泄漏/重复订阅）([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))
        
    - **trigger**：当你“绕过 setter 直接 mutate 了 signal 内部对象”时，用它手动通知下游更新 ([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))
        

### 最小心智模型（你可以拿这个去对照 Vue 的 ref/computed/watchEffect）

- `signal` ≈ `ref`
    
- `computed` ≈ `computed`
    
- `effect` ≈ `watchEffect`
    
- 自动依赖收集：在 effect/computed 执行期间读到的 signal，会被记为依赖
    

---

## 2) 它在 Vue 3.6 里是什么角色？

alien-signals 的 README 里写得很直白：**“核心算法已经被移植（ported）到 vuejs/core 的 v3.6（对应 PR #12349）”**。([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))  
也就是说：Vue 3.6 并不是把你 API 层面的 `ref/reactive` 全换成 alien-signals 的写法，而更像是 **把响应式系统底层的依赖追踪/传播的核心算法换成了这套更轻的实现**（至少 PR 的目标是这个方向）。

---

## 3) 核心算法是什么？（用“不绕弯”的方式讲清楚）

alien-signals 自己在 README 里给了关键词：**push-pull based signal algorithm**，并且提到它和 Vue 3 的传播算法、Preact 的双向链表做法等有关。([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

### “Push-Pull”到底在说什么？

把一次更新拆成两段：

**A. Push（推）= 写入时只做“标记传播”**  
当你 `set` 一个 signal（值变了），系统沿着依赖图把下游的 computed/effect **标记为 dirty（脏）**，必要时把 effect 放进待执行队列。

> 重点：**此时不急着把所有 computed 都重算一遍**（避免无用功）。

**B. Pull（拉）= 读取时才“按需校验/重算”**  
当你下一次去读某个 computed（或 effect 要运行时），系统会做 dirty 检查：

- 如果依赖没变：直接用缓存
    
- 如果依赖变了：只重算这条链路上真正受影响的 computed
    

这也是 signals 系统常见的“写入轻、读取按需”的设计思路；TC39 signals 提案里也用 **clean/checked/dirty** 这类状态机去描述“何时需要重算 computed”。([GitHub](https://github.com/tc39/proposal-signals "GitHub - tc39/proposal-signals: A proposal to add signals to JavaScript."))

### 为啥它能更快/更省内存？（不神化，只讲机制）

alien-signals README 里明确说它为了性能给算法核心加了约束：

- **不使用 Array/Set/Map**
    
- **算法核心不使用递归**  
    并认为在这些约束下，保持算法简单反而比复杂调度更划算。([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))
    

另一个基于它内核的文档（复用 `createReactiveSystem()` 的实现说明）提到：为了消除递归、提升性能，`propagate` 和 `checkDirty` 这类核心流程用了“记录上一次循环的链表节点 + 回滚逻辑”的迭代写法（代码更难读，但更快）。([npm](https://www.npmjs.com/package/%40substrate-system%2Fsignals "@substrate-system/signals - npm"))

把这些点翻译成人话就是：

- **少分配**：少用 Set/Map 这类结构通常意味着更少的对象/哈希开销、更少 GC 压力
    
- **少调用栈开销**：不用递归 → 少很多函数调用与栈操作
    
- **按需重算**：push 只标脏，pull 才精确重算 → 减少无意义的 computed 重跑
    

---

## 4) 简单案例代码（3 种你一看就能跑的）

### 4.1 官方 README 的最小例子（函数调用风格）

```ts
import { signal, computed, effect } from 'alien-signals';

const count = signal(1);
const doubleCount = computed(() => count() * 2);

effect(() => {
  console.log(`Count is: ${count()}`);
}); // 立刻打印：Count is: 1

console.log(doubleCount()); // 2

count(2);                   // 打印：Count is: 2
console.log(doubleCount()); // 4
```

([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

### 4.2 生命周期管理：effectScope

```ts
import { signal, effect, effectScope } from 'alien-signals';

const count = signal(1);

const stop = effectScope(() => {
  effect(() => console.log('in scope:', count()));
});

count(2); // 会打印
stop();
count(3); // 不再打印
```

([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

### 4.3 直接 mutate 了内部对象？用 trigger 通知下游

```ts
import { signal, computed, trigger } from 'alien-signals';

const arr = signal<number[]>([]);
const length = computed(() => arr().length);

arr().push(1);
console.log(length()); // 仍然可能是旧值（因为没走 setter）

trigger(arr);
console.log(length()); // 更新后的值
```

([GitHub](https://github.com/stackblitz/alien-signals "GitHub - stackblitz/alien-signals:  The lightest signal library"))

---

## 5) 你想自己“造一个 signals API”？（理解 alien-signals 的内核边界）

社区里也有人把 alien-signals 当作“内核”，用 `createReactiveSystem()` 去封装成别的 API 形状（比如 `.get()/.set()` 更像提案/框架的风格）。这类用法在一个 starter 模板里有例子：([GitHub](https://github.com/johnsoncodehk/alien-signals-starter "GitHub - johnsoncodehk/alien-signals-starter"))

```ts
import { signal, computed, effect } from 'alien-signals-starter';

const count = signal(1);
const double = computed(() => count.get() * 2);

effect(() => console.log(count.get()));
count.set(2);
```

([GitHub](https://github.com/johnsoncodehk/alien-signals-starter "GitHub - johnsoncodehk/alien-signals-starter"))

---

如果你愿意，我可以用一张“依赖图 + dirty 标记传播”的小图（配合伪代码）把 **push 阶段 propagate** 和 **pull 阶段 checkDirty** 的执行顺序讲到你能“脑内单步调试”的程度；这玩意儿一旦懂了，你看 Vue 3.6 的响应式优化会非常有“啊哈”感。


在 **JavaScript 语言本体**里，“Signals”目前还**不是**一个已经落地的内建 API（你在浏览器里直接写 `new Signal.State()` 还用不了）。它是 **TC39 的 Stage 1 提案**：计划给 JS 增加一个名为 `Signal` 的内建命名空间，提供一组“响应式原语”，主要给框架/库当底座用，而不是追求给业务代码最顺手的语法。

---

## Signals 在 JS 里“会是什么样的 API”？

提案里 Signals **不是新语法糖**（不是新关键字），而是 **一套普通的 JS 类 + 方法**，挂在全局的 `Signal` 命名空间上：

- `Signal.State`：可写的状态单元（state cell）
    
- `Signal.Computed`：可缓存的派生计算（derived cell）
    
- `Signal.subtle.Watcher`：低层“观察器”，用来让框架实现 effect/调度/批处理（提案刻意不标准化 `effect()`）
    

---

## 具体语法长什么样？

### 1) State / Computed：用 `.get()` 读、用 `.set()` 写

这是提案 README 里的典型例子（也是 polyfill 里给的例子）：

`const counter = new Signal.State(0);  const isEven = new Signal.Computed(() => (counter.get() & 1) === 0); const parity = new Signal.Computed(() => (isEven.get() ? "even" : "odd"));  console.log(parity.get());      // "even" counter.set(counter.get() + 1); console.log(parity.get());      // "odd"`

要点：

- **依赖收集发生在 `.get()`**：在 computed 运行期间读到的 state/computed 会被记录为依赖。
    
- **computed 是“拉（pull）”的**：状态变了不会立刻把 computed 全部算一遍，而是下次 `.get()` 时才按需重算。
    

### 2) “我就想要 `.value` 语法可以吗？”

提案 FAQ 里甚至给了一个“用 Proxy 把 `.get/.set` 包成 `.value`”的示例（说明框架大概率会做包装层）：

`const a = new Signal.State(0); const b = new Proxy(a, {   get(target, prop) {     if (prop === "value") return target.get();   },   set(target, prop, value) {     if (prop === "value") target.set(value);     return true;   }, });  b.value++;       // 本质还是 set/get console.log(b.value);`

---

## 那 “effect / watch” 怎么办？（提案为什么没给 `effect()`）

Signals 提案明确说：**effect、调度、销毁（ownership/disposal）这些高度依赖框架策略，所以不把 `effect()` 标准化**；只提供更底层的 `Watcher` 让框架去实现自己的 effect。

polyfill README 里给了一个“用 `Signal.subtle.Watcher` 拼一个简单 effect”的参考实现（并且强调 subtle API 不是给业务代码直接用的）：

`let needsEnqueue = true;  const w = new Signal.subtle.Watcher(() => {   if (needsEnqueue) {     needsEnqueue = false;     queueMicrotask(processPending);   } });  function processPending() {   needsEnqueue = true;    for (const s of w.getPending()) {     s.get();     // 触发对应 computed 重新计算   }    w.watch();     // 继续 watch 之前的依赖集合 }  function effect(cb) {   const computed = new Signal.Computed(cb);   w.watch(computed);   computed.get(); // 先跑一次   return () => w.unwatch(computed); }`

---

## 现在我能在哪里“用” Signals？

目前要么：

- 在框架里用它们自己的 signals（Vue/Angular/Solid 等）
    
- 或者用提案的 **polyfill** 体验（但它自己也提醒：这是预览实现，API 可能变，不建议生产用）。
    

---

### 你把它类比成 Vue，会更容易：

- `Signal.State` ≈ `ref`
    
- `Signal.Computed` ≈ `computed`
    
- `Watcher + 调度器` ≈ `watchEffect + scheduler/flush策略`（但标准里只给“底层零件”）

