# 类与对象（class）

关联：[[01 Python语法]] | [[Python语法/类型标注（typing）]] | [[Python语法/函数定义与参数]]

## 前端视角对比

- Python 的 `class` 表达能力很强（描述器、装饰器、元类等），但日常你可以先按“和 JS class 类似”来理解
- `self` ≈ JS 的 `this`（但必须显式写出来，减少歧义）
- Python 同时有“实例属性”和“类属性”；类属性容易被误用成共享状态

## 基本写法

```py
class User:
    def __init__(self, name: str):
        self.name = name

    def hello(self) -> str:
        return f"Hi, {self.name}"


u = User("Alice")
u.hello()
```

## classmethod / staticmethod

```py
class App:
    version = "1.0"

    @classmethod
    def from_env(cls):
        return cls()

    @staticmethod
    def util(x: int) -> int:
        return x + 1
```

对比 JS：

- `@classmethod` 更像“拿到类本身作为第一个参数”的工厂方法
- `@staticmethod` 类似 JS 的 `static util()`

## 工程建议

- 数据载体优先考虑 `dataclasses.dataclass`（类似 TS 里写 interface + 简单构造），能减少样板代码

## self：显式 this，减少歧义

Python 的实例方法第一个参数必须是 `self`（名字可以换，但强烈建议别换）。

```py
class User:
    def hello(self) -> str:
        return "hi"
```

这让你在阅读代码时能一眼看出“这个属性/方法来自实例”。

## 实例属性 vs 类属性（共享状态大坑）

```py
class Bad:
    items = []  # 类属性：所有实例共享同一个列表

    def add(self, x):
        self.items.append(x)


a = Bad()
b = Bad()
a.add(1)
print(b.items)  # [1]
```

正确姿势：把可变状态放到实例里：

```py
class Good:
    def __init__(self):
        self.items = []
```

## dataclass：写“数据对象”的首选

```py
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
```

- 自动生成 `__init__`, `__repr__`, `__eq__`
- `frozen=True` 让它更像不可变数据结构（对标前端的 immutable 思路）

## property：用属性语法表达 getter/setter

```py
class Temperature:
    def __init__(self, c: float):
        self._c = c

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._c = value
```

## __repr__ / __str__：调试体验

当你在后端排查问题时，良好的 `__repr__` 会救命。dataclass 会自动帮你生成。

## 小练习

1. 用 dataclass 写一个 `User(id: int, name: str)`，并实现一个方法 `display_name()`。
2. 写一个 class，包含类属性 `version` 和实例属性 `name`，体会访问方式差异。
3. 写一个带 `@property` 的校验属性（例如邮箱/温度），非法值抛异常。
