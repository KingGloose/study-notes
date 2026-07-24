在 Vue 3 里，`toRef` / `toRefs` 的核心价值就一句话：**把“响应式对象的某个属性”包装成一个 `ref`，而不是把值拷贝出来**，从而在解构、传参、watch 时仍然保持和原对象同一条响应式链路。

---

## 1) `toRef` 的原理：给 reactive 的某个 key 做一个“引用壳”

### 你以为你在拿值，其实你在拿“指针”

```js
const state = reactive({ count: 0 })

const r1 = ref(state.count)       // ❌ 拷贝值：r1.value 以后不跟 state.count 同步
const r2 = toRef(state, 'count')  // ✅ 引用属性：r2.value <-> state.count 双向同步
```

### 底层实现长什么样（简化版）

`toRef(obj, 'count')` 返回的不是“独立存储的 ref”，而是一个对象，内部只有 getter/setter：

```js
function toRef(obj, key) {
  return {
    __v_isRef: true,
    get value() { return obj[key] },      // 读的时候读 obj[key]
    set value(v) { obj[key] = v },        // 写的时候写 obj[key]
  }
}
```

关键点在于：**`obj` 如果是 `reactive` 的 Proxy，那么访问 `obj[key]` 会触发 Proxy 的 get/set 拦截，从而走 Vue 的依赖收集(track)与触发(trigger)。**

> 所以 `toRef` 本质上不是“让属性变 ref”，而是“造了一个 ref 外壳，读写都转发给响应式对象的属性”。

---

## 2) `toRefs` 的原理：对对象每个一层 key 批量 `toRef`

`toRefs(state)` 只是帮你把 `state` 的**当前可枚举一层属性**都做一遍 `toRef`：

```js
function toRefs(obj) {
  const res = {}
  for (const key of Object.keys(obj)) {
    res[key] = toRef(obj, key)
  }
  return res
}
```

### 注意点

* **只处理一层（浅层）**：`nested` 还是个 reactive 对象，不会把 `nested.a` 也变成 ref；要单独 `toRef(state.nested, 'a')`
* **只包含调用当下已存在的 key**：后面你给对象新加的属性，`toRefs` 不会自动给你补一个 ref；动态 key 用 `toRef(state, key)` 更合适

---

## 3) 从 `watch` 角度看：`toRef` 为什么“更对味”

### watch 的本质（你可以这样理解）

`watch(source, cb)` 会建立一个响应式 effect，它会**读取一次 source** 来收集依赖：

* source 是 `ref`：读取 `source.value` 收集依赖
* source 是 getter：执行 getter 收集依赖（读取到谁就依赖谁）

### `watch(toRef(state,'count'))` 的依赖链路

```js
const state = reactive({ count: 0 })
const countRef = toRef(state, 'count')

watch(countRef, (nv, ov) => {
  // ...
})
```

依赖收集发生在：

1. watch 内部读取 `countRef.value`
2. `countRef.value` 的 getter 会去读 `state.count`
3. `state` 是 Proxy，读取 `count` 触发 `track(stateRaw, 'count')`
4. 当你修改 `state.count` 或 `countRef.value` 时触发 `trigger(stateRaw, 'count')`
5. watch 的回调执行

所以 `toRef + watch` 的特点是：**只依赖这一条 key，精准、轻量。**

---

## 4) 和其他 watch 写法的对比（非常实用）

### A. `watch(() => state.count, ...)` vs `watch(toRef(state,'count'), ...)`

这俩本质等价：都只依赖 `count` 这一条属性。

差别主要是工程体验：

* `toRef`：适合把属性当作“可传递的 ref”到别处（函数参数、返回值、解构后仍保持响应式）
* getter：写起来最直观，适合就地 watch

### B. `watch(state, ...)`（大坑/重）

```js
watch(state, () => {})
```

当 source 是 **reactive 对象** 时，Vue 会倾向于深度追踪（会遍历/触达内部属性来建立依赖），更容易“牵一发动全身”，性能也更重。

如果你只关心一个字段，优先用：

* `watch(() => state.xxx, ...)` 或
* `watch(toRef(state,'xxx'), ...)`

---

## 5) `toRef` 包装的是对象/数组时，watch 的“深度”问题

```js
const state = reactive({ nested: { a: 1 } })
const nestedRef = toRef(state, 'nested')

// 默认不会因为 nested.a 改变而触发（nested 这个对象引用没变）
watch(nestedRef, () => console.log('changed'))
state.nested.a++ // 很可能不触发
```

你要的是“内部变了也触发”，就：

```js
watch(nestedRef, () => {}, { deep: true })
```

或者更精准：只 watch 你关心的内部字段

```js
watch(() => state.nested.a, () => {})
// 或者
watch(toRef(state.nested, 'a'), () => {})
```

---

## 6) 常见使用场景总结

* **解构不丢响应式**

  ```js
  const state = reactive({ a: 1, b: 2 })
  const { a, b } = toRefs(state)
  watch(a, () => {})
  ```
* **props 解构保持响应式**

  ```js
  const props = defineProps({ foo: String })
  const foo = toRef(props, 'foo')
  watch(foo, () => {})
  ```

  > props 是只读的，所以 `foo.value = ...` 不应该做（会警告/无效）。


