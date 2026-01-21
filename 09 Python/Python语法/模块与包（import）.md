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
