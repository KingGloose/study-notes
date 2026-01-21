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

## 工程建议

- 一行能读懂就用推导式；读不懂就回退到显式 for 循环（可读性优先）
