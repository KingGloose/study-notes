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
