# 切片（slice）

关联：[[01 Python语法]] | [[Python语法/常用容器类型（list、tuple、dict、set）]] | [[Python语法/字符串基础与格式化（f-string）]]

## 前端视角对比

- Python 切片语法是语言级能力：`xs[start:end:step]`
- JS 需要用 `array.slice(start, end)`，而步长（step）要自己写
- Python 支持负数索引：`xs[-1]` 取最后一个（JS 也有 `at(-1)`，但不是老版本默认习惯）

## Python 示例

```py
arr = [0, 1, 2, 3, 4]

arr[1:4]    # [1, 2, 3]
arr[:3]     # [0, 1, 2]
arr[::2]    # [0, 2, 4]
arr[::-1]   # 反转

last = arr[-1]
```

## 对应到 JS/TS

```ts
const arr = [0, 1, 2, 3, 4]
arr.slice(1, 4)
arr.slice(0, 3)
arr.filter((_, i) => i % 2 === 0)
arr.slice().reverse()
arr.at(-1)
```

## 易踩坑

- 切片 `end` 是“开区间”（不包含 end），和 JS `slice` 一样
- 切片会创建新列表；如果你要原地修改，需要用切片赋值（更进阶，用到时再查）

## slice 的通用语法（适用于 list/tuple/str 等序列）

```text
xs[start:end:step]
```

- `start` 默认 0
- `end` 默认 len(xs)
- `step` 默认 1
- 允许负数（从尾部倒数）

## slice 对象：把“切片”当成一个值

当你想复用某个切片规则时，可以显式构造 `slice` 对象：

```py
s = slice(1, 5, 2)
xs = [0, 1, 2, 3, 4, 5]
print(xs[s])  # [1, 3]
```

## 切片赋值：原地替换一段（非常强，但要慎用）

```py
xs = [0, 1, 2, 3, 4]
xs[1:3] = [10, 11, 12]
print(xs)  # [0, 10, 11, 12, 3, 4]
```

这会改变列表长度；如果你来自前端，这个行为类似 JS 的 `splice`。

## 反转与步长

```py
xs = [1, 2, 3, 4]
rev = xs[::-1]

# 每隔一个取一个
odd_idx = xs[::2]
```

## 小练习

1. 写一个函数 `take_last(xs, n)`：返回列表最后 n 个元素（用切片）。
2. 写一个函数 `every_k(xs, k)`：返回每隔 k 个取一个（用 step）。
3. 用切片赋值实现：把列表中间一段替换为另一个列表（类比 JS splice）。
