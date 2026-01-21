# 1 基础语法

## 变量与赋值

详见：[[Python语法/变量与赋值]]

```py
x = 1
name = "Alice"
x, y = 1, 2          # 解包赋值
x, y = y, x          # 交换
```

## 基本数据类型

详见：[[Python语法/基本数据类型]]

```py
num = 1          # int
pi = 3.14        # float
ok = True        # bool
empty = None     # NoneType
text = "hi"      # str
```

## 常用容器类型（list、tuple、dict、set）

详见：[[Python语法/常用容器类型（list、tuple、dict、set）]]

```py
nums = [1, 2, 3]                 # list: 可变
point = (10, 20)                 # tuple: 不可变
user = {"id": 1, "name": "A"}  # dict: 键值对
tags = {"py", "web"}            # set: 去重、集合运算
```

## 运算符

详见：[[Python语法/运算符]]

```py
1 + 2, 3 - 1, 2 * 3, 5 / 2, 5 // 2, 5 % 2, 2 ** 3
a and b, a or b, not a
"a" in "cat", 1 in [1, 2, 3]
a is None
```

## 注释与文档字符串（docstring）

详见：[[Python语法/注释与文档字符串（docstring）]]

```py
# 单行注释

def add(a: int, b: int) -> int:
    """返回 a + b。"""
    return a + b
```

## 字符串基础与格式化（f-string）

详见：[[Python语法/字符串基础与格式化（f-string）]]

```py
s = "Hello"
name = "Bob"
msg = f"{s}, {name}!"
```

## 条件语句（if、elif、else）

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

详见：[[Python语法/切片（slice）]]

```py
arr = [0, 1, 2, 3, 4]
arr[1:4]     # [1, 2, 3]
arr[:3]      # [0, 1, 2]
arr[::2]     # [0, 2, 4]
arr[::-1]    # 反转
```

## 推导式（comprehensions）

详见：[[Python语法/推导式（comprehensions）]]

```py
squares = [x * x for x in range(5) if x % 2 == 0]
mapping = {x: x * x for x in range(3)}
unique = {c for c in "abca"}
```

## 函数定义与参数

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

详见：[[Python语法/模块与包（import）]]

```py
import math
from datetime import datetime
from pathlib import Path

print(math.sqrt(9))
```

## 异常处理（try、except、finally、raise）

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

详见：[[Python语法/上下文管理器（with）]]

```py
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

## 文件与路径（open、pathlib）

详见：[[Python语法/文件与路径（open、pathlib）]]

```py
from pathlib import Path

p = Path(".") / "data" / "a.txt"
print(p.exists())
```

## 类与对象（class）

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

详见：[[Python语法/类型标注（typing）]]

```py
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    return None
```

## 常用内置函数与惯用法

详见：[[Python语法/常用内置函数与惯用法]]

```py
len([1, 2, 3])
sorted([3, 1, 2])
sum([1, 2, 3])
any([False, True])
all([True, True])
```
