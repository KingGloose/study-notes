# 异常处理（try、except、finally、raise）

关联：[[01 Python语法]] | [[Python语法/上下文管理器（with）]] | [[Python语法/函数定义与参数]]

## 前端视角对比

- `try/except/finally` ≈ JS `try/catch/finally`
- Python 的异常是“类型体系”很清晰（继承自 `BaseException` / `Exception`）
- 支持 `else`：只有在没有异常时才执行（JS 没有这个语法糖）

## 常见写法

```py
try:
    n = int("123")
except ValueError as e:
    raise RuntimeError("bad number") from e
else:
    print("ok", n)
finally:
    print("cleanup")
```

## raise from（错误链）

`raise ... from e` 类似在 JS 里保留 cause：

```ts
throw new Error("bad number", { cause: e as unknown })
```

## 工程建议

- 捕获尽量具体：`except ValueError` 比 `except Exception` 更安全
- 不要“吞掉异常”不处理；至少记录日志或重新抛出

## 异常体系：Exception vs BaseException

你日常写业务几乎只关心 `Exception` 分支：

- `BaseException`：最顶层（包含 `KeyboardInterrupt`, `SystemExit` 等“系统级”异常）
- `Exception`：应用级异常基类（你的业务异常一般继承它）

工程建议：

- 业务捕获通常写 `except Exception` 都已经很宽了；更推荐捕具体异常
- 不要随手捕获 `BaseException`，会把 Ctrl+C 都吞掉

## 自定义异常（写后端/库时很常见）

```py
class UserNotFoundError(Exception):
    pass


def get_user(user_id: int) -> dict:
    raise UserNotFoundError(f"user_id={user_id} not found")
```

## else 的价值：把“正常路径”和“异常路径”分开

```py
try:
    n = int(text)
except ValueError:
    return None
else:
    return n  # 只有成功时才走到这里
```

这能避免把“正常逻辑”塞到 try 里太多导致可读性变差。

## finally：资源释放

你可以手写 `finally`，但更多时候应该用 [[Python语法/上下文管理器（with）]]。

## assert：开发期的约束（不要当业务校验）

```py
def area(w: int, h: int) -> int:
    assert w >= 0 and h >= 0
    return w * h
```

注意：Python 可以在优化模式下禁用 assert（`python -O`），所以它不适合做线上业务校验。

## 小练习

1. 写 `parse_int(text)`：能转返回 int，不能转返回 None（用 try/except/else）。
2. 写一个自定义异常 `ConfigError`，在配置缺失时抛出，并用 `raise ... from e` 包装底层异常。
3. 用 `finally` 保证一个“模拟资源”被关闭（然后再用 `with` 重写一遍）。
