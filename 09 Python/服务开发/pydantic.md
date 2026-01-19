# Pydantic 学习笔记

## 1、介绍

Pydantic 是一个用来做“数据校验 + 类型转换”的 Python 库。它会根据你写的类型标注（type hints）检查输入数据是否符合要求，不符合就报错；如果可以自动转换（比如 "123" -> int），它会帮你转换。

核心价值：
- **保证数据可靠**：避免后端收到脏数据
- **统一数据结构**：接口输入输出更清晰
- **自动转换**：减少手动处理字符串、数字、日期的麻烦
- **提升可读性**：类型标注 + 校验规则，一眼能看懂

## 2、使用

最小示例：定义模型与自动转换

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
- 输入是字符串，Pydantic 自动转成 `int`
- 如果传入不能转换的值，会直接报错

## 3、配置管理

`pydantic_settings` 是 Pydantic v2 推荐的“配置管理”方式，用来读取环境变量、`.env` 文件、系统参数，并把它们转换成强类型配置对象。

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "my-app"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
print(settings.database_url)
```

要点：
- 环境变量会自动填充配置
- 类型会自动转换，比如 `"true"` -> `True`
- `.env` 适合本地开发

`ConfigDict` 用来控制模型行为（Pydantic v2 新写法）：

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    id: int
    name: str
```

说明：
- `extra="forbid"`：不允许传入多余字段
- `strict=True`：类型必须严格匹配，不做自动转换

## 4、FastAPI 配置

FastAPI 底层使用 Pydantic 来做请求/响应数据校验，你只要写模型即可。

请求体校验：

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CreateUser(BaseModel):
    username: str
    age: int

@app.post("/users")
def create_user(payload: CreateUser):
    return {"ok": True, "data": payload}
```

响应结构统一：

```python
class UserOut(BaseModel):
    id: int
    username: str

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    return {"id": user_id, "username": "tom"}
```

配置管理配合 FastAPI：

```python
from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    database_url: str

settings = Settings()
app = FastAPI()

@app.get("/health")
def health():
    return {"debug": settings.debug}
```

## 5、总结

- Pydantic 负责“数据校验 + 类型转换”
- `pydantic_settings` 负责“配置管理 + 环境变量读取”
- `ConfigDict` 负责“模型行为控制”
- FastAPI 会自动用 Pydantic 做请求/响应校验
