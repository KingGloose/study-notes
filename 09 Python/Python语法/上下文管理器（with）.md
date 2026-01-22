# 上下文管理器（with）

关联：[[01 Python语法]] | [[Python语法/文件与路径（open、pathlib）]] | [[Python语法/异常处理（try、except、finally、raise）]]

## 前端视角对比

- `with ... as ...:` ≈ “自动帮你写好 try/finally 的资源释放”
- 常见场景：文件、锁、数据库连接、临时目录等
- JS 通常要手写 `try/finally` 或依赖库的 `using`/`dispose` 约定

## 最典型的例子：文件

```py
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

等价的思路（手写 try/finally）：

```py
f = open("demo.txt", "w", encoding="utf-8")
try:
    f.write("hello")
finally:
    f.close()
```

## 进阶：自定义上下文管理器

上下文管理器协议是 `__enter__` / `__exit__`；常用 `contextlib` 快速构造。

进一步可以看：[[Python语法/异常处理（try、except、finally、raise）]]（理解退出时如何处理异常）。

## with 的本质：协议 + try/finally

任何对象只要实现了：

- `__enter__(self)`：进入时调用，返回绑定给 `as ...` 的对象
- `__exit__(self, exc_type, exc, tb)`：退出时调用，负责清理资源；返回 True 可“吞掉异常”（慎用）

就能被 `with` 使用。

## 用 contextlib 快速写一个上下文管理器

```py
from contextlib import contextmanager


@contextmanager
def timer(label: str):
    import time
    start = time.perf_counter()
    try:
        yield
    finally:
        cost = time.perf_counter() - start
        print(label, f"{cost:.3f}s")


with timer("work"):
    _ = sum(range(10_000))
```

> [!tip] 前端类比
> 有点像你自己封装一个 `using` / `dispose` 语义：把资源申请/释放绑定在同一个块结构里。

## ExitStack：动态管理多个资源

当你需要根据条件打开多个文件/多个资源时，`ExitStack` 很好用：

```py
from contextlib import ExitStack


paths = ["a.txt", "b.txt"]
with ExitStack() as stack:
    files = [stack.enter_context(open(p, "w", encoding="utf-8")) for p in paths]
    for f in files:
        f.write("hello\n")
```

## 小练习

1. 用 `@contextmanager` 写一个 `suppress_print()`：进入后临时把 stdout 重定向到空（提示：`contextlib.redirect_stdout`）。
2. 写一个自定义 class 上下文管理器：进入时打印 "enter"，退出时打印 "exit"。
3. 用 `ExitStack` 实现“打开若干个文件并写入”，并确保任意一个打开失败时已打开的也会关闭。
