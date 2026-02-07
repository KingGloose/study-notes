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

## 逐行读取：把文件对象当 iterable

很多前端同学会习惯 `read()` 一次性读完；Python 更常逐行：

```py
with open("a.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        print(line)
```

## newline / encoding：跨平台最常见问题

- 文本模式下建议显式 `encoding="utf-8"`
- Windows/Unix 换行差异可以用 `newline` 控制；多数场景不用管，但遇到 CSV/协议文本时要记得它存在

## Path 的常用能力（比字符串拼接安全）

```py
from pathlib import Path

p = Path("data")

# 遍历目录
for child in p.iterdir():
    print(child)

# 递归 glob
for md in p.rglob("*.md"):
    print(md)

# 读写快捷方法（适合小文件）
text = (p / "a.txt").read_text(encoding="utf-8")
(p / "b.txt").write_text(text, encoding="utf-8")
```

> [!warning] read_text/write_text 适合小文件
> 大文件仍建议用 `open()` 流式处理，避免内存暴涨。

## 常见数据格式：JSON（前端很熟悉）

```py
import json
from pathlib import Path

data = {"a": 1}
Path("data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

obj = json.loads(Path("data.json").read_text(encoding="utf-8"))
print(obj["a"])
```

## 小练习

1. 写一个脚本：遍历某目录下所有 `.md` 文件，统计总行数（提示：`Path.rglob` + 逐行读取）。
2. 写一个函数 `read_json(path: Path) -> dict` 和 `write_json(path: Path, obj: dict) -> None`。
3. 写一个“安全写文件”：写到临时文件后再 rename（了解原子替换概念）。

## 对应到 Node

```ts
import { promises as fs } from "node:fs"
import path from "node:path"

const p = path.join("data", "a.txt")
const text = await fs.readFile(p, "utf8")
```
