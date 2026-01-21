# 常用容器类型（list、tuple、dict、set）

关联：[[01 Python语法]] | [[Python语法/切片（slice）]] | [[Python语法/推导式（comprehensions）]]

## 前端视角对比

- `list` ≈ JS `Array`（可变、常用）
- `tuple` ≈ TS `readonly` 元组 / 不可变数组（常用于“固定结构的数据”）
- `dict` ≈ JS `Object` 或 `Map`（更像 `Map`：key 可以是多种可哈希类型）
- `set` ≈ JS `Set`（去重、集合运算）

## list

```py
nums = [1, 2, 3]
nums.append(4)
last = nums.pop()   # 4
```

## tuple

```py
point = (10, 20)
x, y = point
```

## dict

```py
user = {"id": 1, "name": "Alice"}
user["name"]
user.get("age", 0)

for k, v in user.items():
    print(k, v)
```

## set

```py
tags = {"py", "web"}
tags.add("backend")

a = {1, 2, 3}
b = {3, 4}
print(a | b)  # 并集 {1,2,3,4}
print(a & b)  # 交集 {3}
```

## 易踩坑

- `dict` 的 key 必须是“可哈希”的（通常是不可变类型，例如 `str/int/tuple`）
- `set` 是无序的；不要依赖输出顺序
