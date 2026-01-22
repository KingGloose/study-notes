# 循环（for、while）与 range、enumerate

关联：[[01 Python语法]] | [[Python语法/切片（slice）]] | [[Python语法/常用内置函数与惯用法]]

## 前端视角对比

- Python 的 `for` 更像 JS 的 `for...of`：遍历“可迭代对象”（iterable），而不是下标
- `range(n)` 是“生成序列”的工具，常用来做计数循环（类似传统 for）
- `enumerate(xs)` ≈ JS 的 `xs.entries()` 或手写 index

## 常见写法

```py
for i in range(3):
    print(i)

items = ["a", "b", "c"]
for item in items:
    print(item)

for idx, item in enumerate(items):
    print(idx, item)
```

## break/continue 与 for-else

`for ... else` 在“没有被 break 打断”时会执行 `else`：

```py
for x in [1, 2, 3]:
    if x == 4:
        break
else:
    print("not found")
```

这在前端里通常要写一个 flag 或提前 return。

## iterable / iterator：for 到底在遍历什么

Python 的 `for` 依赖“迭代协议”：

- **iterable**：可被 `iter(x)` 取到 iterator 的对象（例如 `list/tuple/dict/set/str/range`）
- **iterator**：有 `__next__()` 的对象，会在耗尽时抛 `StopIteration`

你不需要一开始就写 iterator，但理解它能解释很多行为：

```py
it = iter([1, 2, 3])
next(it)  # 1
next(it)  # 2
```

> [!tip] 工程直觉
> - `for x in f():` 里的 `f()` 只会执行一次，然后消费其迭代结果
> - 很多内置函数（`zip/enumerate/map`）返回的都是“惰性迭代器”，需要 `list(...)` 才会立刻 materialize

## range 的完整用法

```py
range(5)        # 0..4
range(2, 5)     # 2..4
range(0, 10, 2) # 0,2,4,6,8
```

## enumerate 的常用参数 start

```py
items = ["a", "b"]
for idx, item in enumerate(items, start=1):
    print(idx, item)  # 1 a / 2 b
```

## zip：并行遍历（替代手写 index）

```py
names = ["Alice", "Bob"]
ages = [18, 20]

for name, age in zip(names, ages):
    print(name, age)
```

Python 3.10+：`zip(..., strict=True)` 可以在长度不等时报错（更安全）。

## while 的常见模式

```py
while True:
    line = input("cmd> ").strip()
    if line == "quit":
        break
```

## 小练习

1. 用 `enumerate` 实现一个 `find_index(xs, target)`：找不到返回 -1。
2. 用 `zip` 把两个列表拼成 dict（提示：`dict(zip(keys, values))`）。
3. 写一个 `for-else`：在列表里找一个满足条件的元素，找到就 break，否则 else 打印 "not found"。

## 对应到 JS/TS

```ts
for (let i = 0; i < 3; i++) console.log(i)

const items = ["a", "b", "c"]
for (const item of items) console.log(item)

for (const [idx, item] of items.entries()) console.log(idx, item)
```
