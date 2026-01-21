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
