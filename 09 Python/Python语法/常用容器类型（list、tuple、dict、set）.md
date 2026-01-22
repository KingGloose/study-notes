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

常用方法速记：

- `append(x)`：尾部追加
- `extend(xs)`：追加多个
- `insert(i, x)`：插入
- `remove(x)`：删除第一个匹配
- `pop(i=-1)`：弹出并返回
- `sort(key=..., reverse=...)`：原地排序（更推荐用 `sorted()` 返回新列表）

> [!tip] 工程心法
> - 只要你想“生成新列表”，优先考虑 [[Python语法/推导式（comprehensions）]] 或 `sorted()`，避免不必要的原地修改。
> - 当你发现自己在 `for` 里频繁 `append`，通常可以用推导式更简洁。

## tuple

```py
point = (10, 20)
x, y = point
```

tuple 的典型使用场景：

- 表示“结构固定的一组值”（例如坐标、RGB、数据库的一行）
- 作为 `dict` 的 key（因为 tuple 通常可哈希）
- 函数返回多个值（本质就是返回一个 tuple 并在调用处解包）

```py
def min_max(xs: list[int]) -> tuple[int, int]:
    return min(xs), max(xs)

lo, hi = min_max([1, 2, 3])
```

## dict

```py
user = {"id": 1, "name": "Alice"}
user["name"]
user.get("age", 0)

for k, v in user.items():
    print(k, v)
```

dict 的常用模式：

```py
# 1) 计数（更推荐 collections.Counter）
counts: dict[str, int] = {}
for word in ["a", "b", "a"]:
    counts[word] = counts.get(word, 0) + 1

# 2) 合并（Python 3.9+）
d1 = {"a": 1}
d2 = {"b": 2}
d3 = d1 | d2

# 3) 安全访问
age = user.get("age")
```

> [!note] dict 的顺序
> 从 Python 3.7 起，`dict` 保证“插入顺序”被保留；但工程上不要依赖它做关键业务逻辑（除非你明确知道自己在利用这个特性）。

## set

```py
tags = {"py", "web"}
tags.add("backend")

a = {1, 2, 3}
b = {3, 4}
print(a | b)  # 并集 {1,2,3,4}
print(a & b)  # 交集 {3}
```

set 的典型用途：

- 去重（`set(xs)`）
- 快速 membership 判断（`x in s`，通常比 `x in list` 快）
- 集合运算表达业务规则（白名单/黑名单/权限集合）

```py
allowed = {"read", "write"}
requested = {"read", "delete"}
missing = requested - allowed
print(missing)  # {'delete'}
```

## 性能直觉（够用就行，但要有大概概念）

- `x in list`：平均 O(n)
- `x in dict` / `x in set`：平均 O(1)
- `list.append`：摊还 O(1)

## 易踩坑（补充）

- `list` 的 `*` 重复会复制引用，不会深拷贝：

```py
xs = [[0]] * 3
xs[0].append(1)
print(xs)  # [[0, 1], [0, 1], [0, 1]]
```

正确姿势：

```py
xs = [[0] for _ in range(3)]
```

## 小练习

1. 给一个整数列表，返回去重后的排序结果（提示：`sorted(set(xs))`）。
2. 写一个“权限检查”函数：给用户权限 set 和需要权限 set，返回缺少的权限。
3. 写一个“按字段分组”的函数：输入用户列表（dict），输出 `dict[str, list[dict]]`（提示：`setdefault` 或 `collections.defaultdict`）。

## 易踩坑

- `dict` 的 key 必须是“可哈希”的（通常是不可变类型，例如 `str/int/tuple`）
- `set` 是无序的；不要依赖输出顺序
