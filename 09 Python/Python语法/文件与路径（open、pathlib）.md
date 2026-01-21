# 文件与路径（open、pathlib）

关联：[[01 Python语法]] | [[Python语法/上下文管理器（with）]] | [[Python语法/模块与包（import）]]

## 前端视角对比

- `open()` ≈ Node.js 的 `fs.open/readFile/writeFile`（但 Python 更常直接用文件对象）
- `pathlib.Path` ≈ Node.js 的 `path` 模块 + 一点点“面向对象的路径操作”
- Python 工程里非常强调 `encoding`（尤其在跨平台/中文环境）

## open 的常见模式

```py
# 读文本
with open("a.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 写文本
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

模式（mode）速记：

- `r` 读（默认）
- `w` 写（覆盖）
- `a` 追加
- `b` 二进制（`rb/wb`）

## pathlib 速记

```py
from pathlib import Path

p = Path("data") / "a.txt"   # 自动处理分隔符
print(p.exists())

p.parent.mkdir(parents=True, exist_ok=True)
```

## 对应到 Node

```ts
import { promises as fs } from "node:fs"
import path from "node:path"

const p = path.join("data", "a.txt")
const text = await fs.readFile(p, "utf8")
```
