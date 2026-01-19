# Pydantic 是什么，有什么用

Pydantic 是一个用来做“数据校验 + 类型转换”的 Python 库。你可以把它理解成前端里的“表单校验 + 类型约束 + 自动转换”。它会根据你写的类型标注（type hints）来检查输入数据是否符合要求，不符合就报错；如果能自动转换（比如 "123" -> int），它会帮你转换。

它的核心价值：
- **保证数据可靠**：避免后端收到脏数据。
- **统一数据结构**：让接口输入输出更清晰。
- **自动转换**：减少手动处理字符串、数字、日期的麻烦。
- **提升可读性**：类型标注 + 校验规则，别人一眼能看懂。

## 适合从前端转后端的新手的理解方式

你可以把 Pydantic 想成：
- 前端的 `PropTypes`/`TypeScript` + 表单校验规则
- 在后端，每次收到请求数据，你都需要“确认结构正确 + 类型正确”
- Pydantic 让这件事变成“声明式”

## 最小示例：定义一个数据模型

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

user = User(id="1", name="Alice", age="20")
print(user)
```

输出：
```
id=1 name='Alice' age=20
```

说明：
- 输入是字符串，Pydantic 自动把它转成 `int`
- 如果传入不能转换的值，会直接报错

## 常见场景 1：接口请求数据校验

你可以把它当成“后端的表单校验”。

```python
from pydantic import BaseModel, EmailStr

class RegisterForm(BaseModel):
    username: str
    email: EmailStr
    password: str

# 模拟请求体
payload = {
    "username": "tom",
    "email": "not-an-email",
    "password": "123456"
}

RegisterForm(**payload)  # 会抛出校验错误
```

## 常见场景 2：响应数据结构统一

当你返回数据时，也可以用它统一结构。

```python
class UserResponse(BaseModel):
    id: int
    name: str

user = UserResponse(id=1, name="Bob")
print(user.dict())
```

## 常见校验规则

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)  # 必须大于 0
    stock: int = Field(ge=0)    # 必须 >= 0
```

常用校验参数：
- `gt`: 大于
- `ge`: 大于等于
- `lt`: 小于
- `le`: 小于等于
- `min_length`: 字符串最小长度
- `max_length`: 字符串最大长度

## 总结

如果你是从前端转 Python，Pydantic 可以帮你：
- **避免接口数据乱**（像前端的类型系统）
- **更快写出可靠的后端接口**
- **减少手动判断和转换**

如果你想继续学，我可以按你的学习路径讲：
- 与 FastAPI 的配合使用
- 自定义校验函数
- 复杂嵌套数据结构
- 常见报错和调试思路
