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
