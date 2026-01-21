# 类型标注（typing）

关联：[[01 Python语法]] | [[Python语法/函数定义与参数]] | [[Python语法/类与对象（class）]]

## 前端视角对比

- TS 是“编译期强制”，Python 类型标注默认不强制执行（需要 mypy/pyright 等工具检查）
- 但类型标注对 IDE 补全、重构、团队协作非常有帮助，推荐从早期就养成习惯

## 常见写法

```py
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    return None

xs: list[int] = [1, 2, 3]
user: dict[str, int] = {"id": 1}
```

## Optional / Union 的心智模型

- `Optional[T]` 等价于 `T | None`（Python 3.10+ 语法）

```py
def f(x: int | None) -> int:
    return 0 if x is None else x
```

对比 TS：

```ts
function f(x: number | null | undefined): number {
  return x == null ? 0 : x
}
```

## 工程建议

- 优先写“函数边界”的类型（入参/返回值），收益最大
- 遇到动态结构（类似 JS 的任意对象）时，可以用 `TypedDict` / `Protocol`（更进阶，用到再学）
