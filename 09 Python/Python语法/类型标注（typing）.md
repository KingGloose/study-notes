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

## 类型标注的现实定位

把它当成“给人和工具看的契约”，而不是运行时保证：

- 运行时不会因为你写了类型就自动报错
- 你需要 `pyright` / `mypy` / IDE 来做静态检查

> [!tip] 前端类比
> 类似 TS 的类型系统，但 Python 的类型检查是“可选的、工具驱动的”。

## 常用容器与抽象类型

日常最常用的几类：

```py
from collections.abc import Iterable, Sequence, Mapping


def total(xs: Iterable[int]) -> int:
    return sum(xs)


def head(xs: Sequence[int]) -> int:
    return xs[0]


def get_id(user: Mapping[str, int]) -> int:
    return user["id"]
```

写抽象类型（Iterable/Mapping）通常比写具体类型（list/dict）更灵活。

## TypedDict：描述“字典形状”（很像 TS interface）

```py
from typing import TypedDict


class User(TypedDict):
    id: int
    name: str


def greet(user: User) -> str:
    return f"hi {user['name']}"
```

## Protocol：描述“行为契约”（结构化类型）

当你不关心具体类，只关心“有没有某些方法/属性”时，用 Protocol。

```py
from typing import Protocol


class SupportsClose(Protocol):
    def close(self) -> None: ...


def close_all(xs: list[SupportsClose]) -> None:
    for x in xs:
        x.close()
```

## forward reference 与 annotations

当类型引用自己或后定义的类型时，Python 3.11+ 更顺滑；在较早版本常用：

- `from __future__ import annotations`

（你现在先知道有这回事即可。）

## 小练习

1. 给一个返回 dict 的函数补上 `TypedDict`，让返回结构更明确。
2. 把一个只接受 `list[int]` 的函数改成接受 `Iterable[int]`，体会抽象类型的好处。
3. 用 `Protocol` 写一个 `SupportsLen`，要求有 `__len__`，然后写一个函数只依赖这个协议。
