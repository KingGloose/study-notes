# 注释与文档字符串（docstring）

关联：[[01 Python语法]] | [[Python语法/函数定义与参数]] | [[Python语法/类型标注（typing）]]

## 前端视角对比

- `# ...` 注释 ≈ `// ...`
- Python 的 docstring 更像“运行时可读取的 JSDoc”：既给人读，也能被 `help()` / IDE / 文档工具读取
- Type Hints（类型标注）在语义上更接近 TS；docstring 更像补充说明/示例

## 注释

```py
# 单行注释
total = 1 + 2
```

## docstring

写在模块/函数/类的第一段字符串，会成为它们的 `__doc__`：

```py
def add(a: int, b: int) -> int:
    """Return a + b.

    Args:
        a: left operand
        b: right operand
    """
    return a + b

print(add.__doc__)
```

## 实践建议（偏工程化）

- 公共函数/对外 API：写 docstring + 类型标注
- 私有/短函数：类型标注往往比长 docstring 更划算
