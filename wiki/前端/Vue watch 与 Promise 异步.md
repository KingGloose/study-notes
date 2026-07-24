# 1. Vue watch 里使用 Promise / async 的行为

> 缘起:讨论 QuillJs 回显时,延伸到「watch 里跑异步」的通用坑点。
> 本页为通用知识梳理(AI 补充),留作唤醒 + 速查。个人项目里若踩到具体竞态坑,再往这里补真实案例。

---

## 1.1 async 回调合法,但 Vue 不会「等」它

```js
watch(source, async (val) => {
  const data = await fetch(url)  // Vue 不关心这个 await
  result.value = data
})
```

watch 回调的返回值(包括返回的 Promise)Vue 完全不理会。它只在依赖变化时**触发**回调,不会等 await 完再做别的。async 回调合法,但异步流程要自己管。

## 1.2 最大的坑:竞态(race condition)

source 连续变化会连续触发多次异步请求,而返回顺序不保证,可能旧数据覆盖新数据:

```js
watch(keyword, async (kw) => {
  const res = await search(kw)   // abc 的请求可能比 ab 先发出但后返回
  list.value = res               // ← 最后写入的可能是过期结果
})
```

用 `onCleanup`(选项式回调第三参 / 组合式 `onWatcherCleanup` 或回调第三参)解决,下次触发前会先跑上一次 cleanup:

```js
watch(keyword, async (kw, prev, onCleanup) => {
  let canceled = false
  onCleanup(() => { canceled = true })
  const res = await search(kw)
  if (!canceled) list.value = res    // 过期的丢弃
})
```

配合 `AbortController` 直接取消请求更干净。


## 1.3 async 里依赖收集会「断」(watchEffect 尤其注意)

只有**第一个 await 之前**访问的响应式数据才会被收集为依赖:

```js
watchEffect(async () => {
  console.log(a.value)   // ✅ 被收集
  await something()
  console.log(b.value)   // ❌ 不被收集,b 变化不会重新触发
})
```

原因:依赖收集靠「当前活跃 effect」这个全局状态在同步执行期间完成;await 之后微任务恢复时,活跃 effect 已不是它了。(与 archive 里 ⭐Signals / Vue 3.5-3.6 响应式重构原理一脉相承)

## 1.4 flush 时机 ≠ 异步本身

`flush: 'pre' | 'post' | 'sync'` 只决定回调**何时被调用**(DOM 更新前/后/同步),与回调里 await 什么无关。要在异步里拿到更新后的 DOM:用 `flush: 'post'` 或自己 `await nextTick()`。
