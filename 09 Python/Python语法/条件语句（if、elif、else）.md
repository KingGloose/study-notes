# 条件语句（if、elif、else）

关联：[[01 Python语法]] | [[Python语法/运算符]] | [[Python语法/循环（for、while）与 range、enumerate]]

## 前端视角对比

- 没有 `{}`，靠缩进定义代码块（和 Python 的“可读性优先”风格强绑定）
- `elif` ≈ `else if`
- 三元表达式：`a if cond else b` ≈ `cond ? a : b`

## Python 写法

```py
score = 85

if score >= 90:
    level = "A"
elif score >= 60:
    level = "B"
else:
    level = "C"

label = "ok" if score >= 60 else "fail"
```

## Truthy / Falsy（真值）

类似 JS，但规则更“统一”：

- `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None` 都是 False
- 其他大多数对象都为 True

```py
if items:         # 等价于 len(items) > 0
    ...
```

## 工程建议

- 判断空值尽量用 `is None`
- 多分支逻辑可以考虑“字典映射”或 Python 3.10+ 的 `match`（类似更强的 switch）

## 条件判断的“Pythonic”写法

### 1) 直接判断容器是否为空

```py
items: list[int] = []

if items:
    print("not empty")
else:
    print("empty")
```

这通常比 `if len(items) > 0:` 更常见。

### 2) None 的判断

```py
user_id: int | None = None

if user_id is None:
    ...

if user_id is not None:
    ...
```

### 3) 类型判断（替代一部分“鸭子类型误用”）

```py
def normalize(x: object) -> str:
    if isinstance(x, str):
        return x.strip()
    return str(x)
```

## match（Python 3.10+）：结构化分支

当你在前端习惯写 `switch` 或者需要对“结构”做分支时，`match` 很好用。

```py
def http_label(code: int) -> str:
    match code:
        case 200 | 201:
            return "ok"
        case 400:
            return "bad request"
        case 404:
            return "not found"
        case _:
            return "other"
```

> [!tip] 什么时候用 match
> - 分支很多且互斥
> - 分支条件是“值匹配/结构匹配”，不是复杂布尔表达式
> - 你希望替代 `if/elif/elif/elif` 的长链条

## 常见坑：and/or 的返回值不是 bool

在 `if` 里你感觉不出来，但在赋值时会影响结果（见 [[Python语法/运算符]]）：

```py
name = "" or "Anonymous"  # 'Anonymous'
```

## 小练习

1. 写一个函数 `grade(score: int) -> str`：用 `if/elif/else` 给 A/B/C。
2. 写一个函数 `to_bool(x: str) -> bool`：支持 "true/false/1/0/yes/no"（注意大小写、空白）。
3. 用 `match` 写一个简单的命令分发："start"/"stop"/"restart"。
