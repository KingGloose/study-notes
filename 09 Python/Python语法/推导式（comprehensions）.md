# 推导式（comprehensions）

关联：[[01 Python语法]] | [[Python语法/常用容器类型（list、tuple、dict、set）]] | [[Python语法/循环（for、while）与 range、enumerate]]

## 前端视角对比

- 列表推导式 ≈ `map + filter`，但更贴近“声明式构造一个新集合”
- 字典/集合推导式是 Python 的特色；JS 通常要手写循环或用 `reduce`
- 需要“惰性计算”时，可用生成器表达式（类似 JS generator/iterator 思路）

## 列表推导式

```py
squares = [x * x for x in range(10) if x % 2 == 0]
```

## 字典推导式 / 集合推导式

```py
mapping = {x: x * x for x in range(3)}
unique = {c for c in "abca"}
```

## 生成器表达式（惰性）

```py
gen = (x * x for x in range(10))
```

## 推导式的“读法”：先读 for，再读前面的表达式

以列表推导式为例：

```py
result = [transform(x) for x in xs if predicate(x)]
```

读成中文：

1) 对于 `xs` 中的每个 `x`
2) 如果 `predicate(x)` 成立
3) 把 `transform(x)` 放进新列表

## 嵌套推导式（可写，但别写到读不懂）

```py
grid = [(x, y) for x in range(3) for y in range(2)]
```

这相当于双重循环：

```py
grid = []
for x in range(3):
    for y in range(2):
        grid.append((x, y))
```

> [!tip] 可读性建议
> 嵌套超过两层，或者 if 条件复杂时，优先退回显式 for 循环。

## 生成器表达式的典型用法：配合 sum/any/all

```py
xs = [1, 2, 3, 4]

total = sum(x * x for x in xs)          # 不创建中间列表
has_even = any(x % 2 == 0 for x in xs)  # 发现一个就短路
```

## 作用域小细节

在 Python 3 里，推导式有自己的局部作用域（不会“泄漏”循环变量到外层）：

```py
x = 100
_ = [x for x in range(3)]
print(x)  # 100
```

## 小练习

1. 给一个字符串列表，过滤掉空字符串并去两端空白（推导式 + if）。
2. 给一个 dict，构造一个新 dict：只保留 value 为真值的项。
3. 给一个二维列表 matrix，写一个推导式把它 flatten 成一维列表。

## 工程建议

- 一行能读懂就用推导式；读不懂就回退到显式 for 循环（可读性优先）
