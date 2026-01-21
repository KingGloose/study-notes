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
