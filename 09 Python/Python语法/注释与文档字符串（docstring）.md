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

## docstring 写什么：对“调用者”最有价值的信息

当你写 docstring 时，可以用这 4 个问题约束内容（非常工程化）：

1. 这个函数/类“做什么”（一句话）？
2. 关键参数的语义是什么（不是类型，而是业务含义/单位/约束）？
3. 返回值的语义是什么？
4. 有哪些异常会抛出/哪些边界条件要注意？

> [!tip] 和 TS 的分工
> - 类型标注（[[Python语法/类型标注（typing）]]）解决“形状/类型”
> - docstring 解决“语义/约束/示例/边界条件”

## 常见风格（挑一种团队统一就行）

Python 社区常见 docstring 风格：

- Google style（可读性强，工程里常用）
- NumPy style（科学计算生态常用）
- reStructuredText / Sphinx style（文档工具链更偏传统）

你现在这份笔记里示例更接近 Google style。

## 模块 docstring / 类 docstring

docstring 不仅能写在函数上：

```py
"""user_service.py

This module contains user-related business logic.
"""


class UserService:
    """High-level user operations."""

    def get_user(self, user_id: int) -> dict:
        """Return user data."""
        return {"id": user_id}
```

## 实战建议（补充）

- 复杂逻辑尽量写“小函数 + 好命名”，比长注释更抗变化
- 注释更适合解释“为什么这么做”（why），而不是“做了什么”（what）
- docstring 尽量给出一个最小可运行示例（对写脚本/工具尤其友好）

## 小练习

1. 给你常写的一个工具函数（例如格式化、解析 query），用 docstring 把“输入约束 / 输出语义 / 示例”补全。
2. 写一个模块级 docstring：描述模块职责、对外 API，以及你期望的使用方式。

## 实践建议（偏工程化）

- 公共函数/对外 API：写 docstring + 类型标注
- 私有/短函数：类型标注往往比长 docstring 更划算
