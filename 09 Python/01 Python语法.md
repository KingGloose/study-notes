# 1 基础语法

这份笔记是面向“前端开发工程师 → Python 开发”的语法地图：你已经知道每一章大概讲什么，我会补齐“为什么这样设计 / 日常怎么写 / 容易踩的坑 / 跟 JS/TS 的关键差异”。

> [!tip] 建议的学习方式（非常重要）
> - 每节先看本页的“要点 + 例子”，再点进对应的双链做深入。
> - 写 Python 时优先追求：可读性（PEP 8）> 正确性 > 性能；等你写顺手后再做性能优化。
> - 默认以 Python 3.10+ 作为语法基线（例如 `T | None`、`match` 等）。

> [!note] 一句话心智模型（前端最该先建立的差异）
> Python 的“变量”更像 JS 里的“引用名”：赋值是把名字绑定到对象；可变对象会被共享。

## 变量与赋值

你需要掌握的点：

- 赋值是“名字绑定（name binding）”，不是“拷贝”；这会影响列表/字典等可变对象的使用
- 解包赋值（unpacking）几乎是 Python 的核心语法糖：交换、拆分返回值、遍历 `dict.items()`
- Python 没有 `const`，但可以用“不可变类型 + 约定”达到类似效果

详见：[[Python语法/变量与赋值]]

```py
x = 1
name = "Alice"
x, y = 1, 2          # 解包赋值
x, y = y, x          # 交换
```

## 基本数据类型

你需要掌握的点：

- `int` 默认任意精度；`float` 依然是 IEEE 754（仍会有精度问题）
- `None` 统一表达“空/缺失”，判断用 `is None`
- `str` 是 Unicode；二进制用 `bytes`（这点在文件、网络、加密里非常关键）

详见：[[Python语法/基本数据类型]]

```py
num = 1          # int
pi = 3.14        # float
ok = True        # bool
empty = None     # NoneType
text = "hi"      # str
```

## 常用容器类型（list、tuple、dict、set）

你需要掌握的点：

- `list`（可变序列）/ `tuple`（不可变序列）/ `dict`（映射）/ `set`（集合）分别擅长的场景
- Python 的 `dict` 是“语言级核心结构”（非常常用）；遍历、查找、合并有大量惯用法
- `set` 的集合运算（并/交/差）非常实用，写业务逻辑会比手写循环清晰

详见：[[Python语法/常用容器类型（list、tuple、dict、set）]]

```py
nums = [1, 2, 3]                 # list: 可变
point = (10, 20)                 # tuple: 不可变
user = {"id": 1, "name": "A"}  # dict: 键值对
tags = {"py", "web"}            # set: 去重、集合运算
```

## 运算符

你需要掌握的点：

- `==`（值相等） vs `is`（同一对象）；判断 `None` 永远用 `is None`
- `and/or` 会返回操作数本身（短路求值），不仅仅返回 True/False（这点和 JS 类似）
- Python 支持“链式比较”：`0 < x < 10` 可读性很强

详见：[[Python语法/运算符]]

```py
1 + 2, 3 - 1, 2 * 3, 5 / 2, 5 // 2, 5 % 2, 2 ** 3
a and b, a or b, not a
"a" in "cat", 1 in [1, 2, 3]
a is None
```

## 注释与文档字符串（docstring）

你需要掌握的点：

- docstring 是“运行时可读取的说明”，类似可被工具消费的 JSDoc
- 工程里：对外 API 写 docstring；内部逻辑优先靠“清晰命名 + 类型标注 + 小函数”

详见：[[Python语法/注释与文档字符串（docstring）]]

```py
# 单行注释

def add(a: int, b: int) -> int:
    """返回 a + b。"""
    return a + b
```

## 字符串基础与格式化（f-string）

你需要掌握的点：

- f-string 是最推荐的格式化方式（可读性强、功能强）
- 字符串不可变；大量拼接用 `"".join(...)`
- 文本（`str`） vs 二进制（`bytes`）要分清；文件/网络常见 bug 都出在这里

详见：[[Python语法/字符串基础与格式化（f-string）]]

```py
s = "Hello"
name = "Bob"
msg = f"{s}, {name}!"
```

## 条件语句（if、elif、else）

你需要掌握的点：

- 缩进就是语法（别和编辑器“自动缩进”对着干）
- Truthy/Falsy 规则统一：空容器/0/空字符串/None 都为 False
- Python 3.10+ 的 `match` 可以写更强的分支匹配（用到再学，不用一开始硬背）

详见：[[Python语法/条件语句（if、elif、else）]]

```py
score = 85
if score >= 90:
    level = "A"
elif score >= 60:
    level = "B"
else:
    level = "C"
```

## 循环（for、while）与 range、enumerate

你需要掌握的点：

- `for` 遍历 iterable（更像 JS `for...of`），`range` 只是常见的计数器
- `enumerate(xs)` 是“带索引遍历”的惯用法
- `for ... else` 的语义要理解：没有被 `break` 打断才执行 `else`

详见：[[Python语法/循环（for、while）与 range、enumerate]]

```py
for i in range(3):
    print(i)

items = ["a", "b", "c"]
for idx, item in enumerate(items):
    print(idx, item)

n = 3
while n > 0:
    n -= 1
```

## 切片（slice）

你需要掌握的点：

- `xs[start:end:step]` 是语言级能力；负数索引/负步长很实用
- 切片会生成新序列（浅拷贝）；需要原地修改可以用“切片赋值”

详见：[[Python语法/切片（slice）]]

```py
arr = [0, 1, 2, 3, 4]
arr[1:4]     # [1, 2, 3]
arr[:3]      # [0, 1, 2]
arr[::2]     # [0, 2, 4]
arr[::-1]    # 反转
```

## 推导式（comprehensions）

你需要掌握的点：

- 推导式是写 Python 的高频“表达式级循环”
- 列表/字典/集合推导式都很常用；需要惰性计算用生成器表达式
- 可读性优先：一行读不懂就退回 for 循环

详见：[[Python语法/推导式（comprehensions）]]

```py
squares = [x * x for x in range(5) if x % 2 == 0]
mapping = {x: x * x for x in range(3)}
unique = {c for c in "abca"}
```

## 函数定义与参数

你需要掌握的点：

- 关键字参数（named arguments）是 Python 的强项：可读性极强
- `*args/**kwargs` 与解包调用（`f(*xs, **d)`）非常常见
- 默认参数只求值一次（可变默认值是经典大坑）

详见：[[Python语法/函数定义与参数]]

```py
def greet(name, prefix="Hi"):
    return f"{prefix}, {name}"

def f(*args, **kwargs):
    return args, kwargs

greet("Alice")
greet(name="Bob", prefix="Hello")
```

## 作用域（LEGB）与可变、不可变

你需要掌握的点：

- LEGB 查找规则：Local → Enclosing → Global → Builtins
- `nonlocal/global` 是“修改外层绑定”的显式语法
- 可变对象共享是 Python 代码里 80% 的“诡异 bug”来源

详见：[[Python语法/作用域（LEGB）与可变、不可变]]

```py
x = 10

def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
        return x
    return inner
```

## 模块与包（import）

你需要掌握的点：

- `.py` 文件就是模块；目录通常通过 `__init__.py` 组织成包
- `import` 会执行模块顶层代码一次并缓存（类似 ESM 单例）
- 工程里避免 `from x import *`，也要注意循环导入

详见：[[Python语法/模块与包（import）]]

```py
import math
from datetime import datetime
from pathlib import Path

print(math.sqrt(9))
```

## 异常处理（try、except、finally、raise）

你需要掌握的点：

- 捕获要具体，不要随手 `except Exception`
- `raise ... from e` 用于保留错误链（排查问题非常有用）
- `try/except/else/finally` 的分工要清晰

详见：[[Python语法/异常处理（try、except、finally、raise）]]

```py
try:
    n = int("123")
except ValueError as e:
    raise RuntimeError("bad number") from e
finally:
    pass
```

## 上下文管理器（with）

你需要掌握的点：

- `with` = 自动帮你写好 try/finally 的资源释放
- 文件、锁、数据库连接、临时目录等都适合用 `with`

详见：[[Python语法/上下文管理器（with）]]

```py
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

## 文件与路径（open、pathlib）

你需要掌握的点：

- 永远显式处理 `encoding`（文本文件）
- 路径处理优先用 `pathlib.Path`（比字符串拼路径可靠）
- 读写文件几乎总是和 `with` 一起出现

详见：[[Python语法/文件与路径（open、pathlib）]]

```py
from pathlib import Path

p = Path(".") / "data" / "a.txt"
print(p.exists())
```

## 类与对象（class）

你需要掌握的点：

- `self` 必须显式写：减少 this 的歧义
- 区分实例属性 vs 类属性；共享状态要非常谨慎
- 数据类（`dataclasses`）能大幅减少样板代码

详见：[[Python语法/类与对象（class）]]

```py
class User:
    def __init__(self, name: str):
        self.name = name

    def hello(self) -> str:
        return f"Hi, {self.name}"

u = User("Alice")
u.hello()
```

## 类型标注（typing）

你需要掌握的点：

- Python 类型标注默认不强制执行，但对工程质量帮助极大
- 先从“函数边界”的类型标注开始（入参/返回值）
- `T | None` / `Optional[T]` 的可空建模是最常见需求

详见：[[Python语法/类型标注（typing）]]

```py
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    return None
```

## 常用内置函数与惯用法

你需要掌握的点：

- `len/sorted/sum/any/all/zip/enumerate` 会让代码更短更清晰
- 解包（`*` / `**`）和推导式一起，是 Python 日常写法的核心
- 多用 key 函数（`sorted(xs, key=...)`）少写复杂比较逻辑

详见：[[Python语法/常用内置函数与惯用法]]

```py
len([1, 2, 3])
sorted([3, 1, 2])
sum([1, 2, 3])
any([False, True])
all([True, True])
```
