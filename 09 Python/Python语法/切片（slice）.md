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
