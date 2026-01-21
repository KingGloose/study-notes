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

## 对应到 JS/TS

```ts
for (let i = 0; i < 3; i++) console.log(i)

const items = ["a", "b", "c"]
for (const item of items) console.log(item)

for (const [idx, item] of items.entries()) console.log(idx, item)
```
