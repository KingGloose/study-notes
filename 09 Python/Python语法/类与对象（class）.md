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
