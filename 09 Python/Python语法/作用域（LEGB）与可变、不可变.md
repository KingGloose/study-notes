# 作用域（LEGB）与可变、不可变

关联：[[01 Python语法]] | [[Python语法/变量与赋值]] | [[Python语法/函数定义与参数]]

## 前端视角对比

- JS 主要是词法作用域（lexical scope），Python 也是，但有自己的一套查找规则：LEGB
- LEGB：Local -> Enclosing -> Global -> Builtins
- Python 中“在函数体内出现赋值”会让该名字变成局部变量（即使你只是想读全局变量）

## nonlocal / global（对标 JS 的闭包修改）

```py
def outer():
    x = 0

    def inner():
        nonlocal x
        x += 1
        return x

    return inner

inc = outer()
inc()  # 1
inc()  # 2
```

`global` 用于修改模块级变量（一般不推荐大量使用，工程里更倾向显式传参/封装状态）。

## 可变 vs 不可变（和值传递的误解）

Python 不是“按值传递/按引用传递”这么简单，更接近“把对象引用作为参数传入”（和 JS 类似）。

- `int/float/bool/str/tuple` 通常不可变
- `list/dict/set` 可变

```py
def add_one(n: int) -> int:
    n += 1
    return n

def push(xs: list[int]) -> None:
    xs.append(1)
```

## 易踩坑

- 想在函数里读全局变量但又对同名变量赋值，会触发 `UnboundLocalError`；需要 `global` 或换名
