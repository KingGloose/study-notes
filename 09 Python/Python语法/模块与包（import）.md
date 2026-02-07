# 模块与包（import）

关联：[[01 Python语法]] | [[Python语法/文件与路径（open、pathlib）]] | [[Python语法/异常处理（try、except、finally、raise）]]

## 前端视角对比

- Python 的“一个 .py 文件”就是一个模块（module），类似一个 ES module 文件
- 一个目录如果是包（package），通常包含 `__init__.py`（现代 Python 也支持命名空间包，但先不展开）
- `import x` 会执行模块顶层代码一次，并缓存（类似 ESM 的单例模块行为）

## 常见导入方式

```py
import math
from pathlib import Path
from datetime import datetime as dt

print(math.sqrt(9))
```

## 入口判断（类似 Node 的 main）

```py
def main() -> None:
    print("run")


if __name__ == "__main__":
    main()
```

## 工程建议

- 避免 `from x import *`（可读性差、容易污染命名空间）
- 遇到导入循环（circular import）时，优先调整模块边界或把导入放到函数内部（权衡可读性）

## import 到底做了什么

当你执行 `import some_module`：

1. Python 根据 `sys.path` 搜索模块（当前目录、site-packages 等）
2. 找到后执行该模块的顶层代码（只会执行一次）
3. 把模块对象缓存到 `sys.modules`
4. 当前作用域获得一个名字绑定到该模块对象

这就是为什么“模块顶层写副作用代码”会影响导入行为（例如导入就连数据库）。

> [!tip] 工程建议
> 模块顶层尽量只做：常量定义、类型定义、轻量初始化；重的副作用放到 `main()` 或显式函数里。

## 包（package）与 __init__.py

你会看到这种结构：

```text
pkg/
  __init__.py
  api.py
  service.py
```

- 有 `__init__.py` 的目录通常被当成包
- `import pkg` 会执行 `pkg/__init__.py`

> [!note] 现代 Python
> 也存在“命名空间包”（没有 `__init__.py`），但你作为工程入门阶段可以先按“有 __init__.py 才是包”来理解。

## 相对导入（relative import）

在包内部，你可能会看到：

```py
from .service import UserService
from ..common import config
```

相对导入适合包内部重构；但脚本/快速实验时更推荐绝对导入。

## __name__ == "__main__"：脚本入口

你在文件里写：

```py
if __name__ == "__main__":
    main()
```

含义是：

- 当你 `python file.py` 直接运行时，`__name__` 为 `"__main__"`
- 当你被别人 `import file` 时，`__name__` 为模块名（不会执行 main）

## 小练习

1. 写一个 `utils.py`，定义一个函数；再写一个 `main.py` 导入它并运行。
2. 在模块顶层打印一句话，观察“被 import 时是否会打印”（理解 import 的副作用）。
3. 组织一个简单包（目录 + __init__.py），体验绝对导入和相对导入的区别。
