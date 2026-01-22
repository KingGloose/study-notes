# 字符串基础与格式化（f-string）

关联：[[01 Python语法]] | [[Python语法/基本数据类型]] | [[Python语法/切片（slice）]]

## 前端视角对比

- Python `str` ≈ JS `string`（不可变）
- f-string ≈ JS 模板字符串（`` `${name}` ``），但支持更强的格式化规格
- 多行字符串常用三引号 `"""..."""`（JS 用模板字符串或 `\n`）

## 常见操作

```py
name = "Alice"
age = 18

msg = f"name={name}, age={age}"
pad = f"{age:04d}"       # 0018
pi = 3.14159
fmt = f"{pi:.2f}"        # 3.14

text = "hello world"
parts = text.split(" ")
joined = "-".join(parts)
```

## 字符串的“不可变”带来的写法差异

和 JS 一样，Python 的字符串不可变：

- 任何“修改”都会创建新字符串
- 循环拼接时会频繁分配新对象

当你需要拼接很多段字符串时，优先用 `"".join(...)`：

```py
chunks = ["a", "b", "c"]
s = "".join(chunks)
```

## f-string 进阶：格式化规格、调试输出

```py
pi = 3.14159
print(f"{pi:.2f}")        # 3.14

n = 42
print(f"{n:08d}")         # 00000042

name = "Alice"
print(f"{name=!r}")       # name='Alice'  （Python 3.8+ 的调试语法）
```

常用格式化规格（最常用的就这些）：

- `.2f`：保留 2 位小数
- `04d`：整数补零到 4 位
- `,`：千分位分隔（`f"{n:,}"`）

## 常用 API 速查（写业务很频繁）

```py
s = "  Hello World  "
s.strip()                 # 去两端空白
s.lower(), s.upper()       # 大小写
s.startswith("  H")
s.replace("World", "Python")

"a,b,c".split(",")
"-".join(["a", "b", "c"])
```

## 原始字符串 r"..."：正则/路径的救星

```py
pattern = r"\d+\.\d+"  # 不用写成 "\\d+\\.\\d+"
```

## 文本 vs 二进制（再次强调）

你会在 [[Python语法/文件与路径（open、pathlib）]] 里反复碰到：

- `open(..., "r", encoding="utf-8")` 读出来是 `str`
- `open(..., "rb")` 读出来是 `bytes`

不要混用：

```py
"hi" + b"!"  # TypeError
```

## 小练习

1. 给一个浮点数列表，打印成两位小数并对齐（用 f-string 格式化）。
2. 写一个函数 `slugify(s: str) -> str`：去两端空白、小写、把空格替换为 `-`。
3. 写一个正则 pattern 用 `r"..."` 表达一个简单的邮箱规则（只做练习，不追求完美）。

## 对应到 JS/TS

```ts
const name = "Alice"
const age = 18

const msg = `name=${name}, age=${age}`
const pad = String(age).padStart(4, "0")
const pi = 3.14159
const fmt = pi.toFixed(2)
```

## 易踩坑

- 字符串不可变：频繁拼接建议用 `"".join(...)`（类似 JS 用数组 join 来拼接）
- 原始字符串 `r"..."` 在处理正则/Windows 路径时很常用（减少转义）
