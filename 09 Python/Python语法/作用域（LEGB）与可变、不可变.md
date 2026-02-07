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

## LEGB：名字查找的完整路径

当你在函数里写 `x`，Python 会按顺序找：

1. **L**ocal：当前函数局部作用域
2. **E**nclosing：外层函数作用域（闭包）
3. **G**lobal：模块级作用域（当前 .py 文件）
4. **B**uiltins：内置命名空间（`len`, `str`, `list` 等）

理解这一点能解释很多“我明明定义了变量，怎么找不到/怎么变成局部了”。

## global：修改模块级绑定（谨慎用）

```py
count = 0


def inc() -> int:
    global count
    count += 1
    return count
```

工程建议：

- 脚本小工具可以用
- 长生命周期服务（web server）不建议靠 global 维护状态（更难测、更难并发）

## nonlocal：修改闭包外层函数的绑定

你在本页开头已经见过 `nonlocal`，这里强调它解决的是：

- 外层变量不是全局
- 但你又想在内层函数里“重新绑定”它

## 可变对象与“传参”心智模型

和 JS 一样，Python 函数调用更接近“传对象引用的副本”（你可以把它理解为：把引用值按值传递）。

```py
def mutate(xs: list[int]) -> None:
    xs.append(1)


def rebind(xs: list[int]) -> None:
    xs = [99]  # 只是把局部名字 xs 重新绑定到新对象，不影响外部


a = []
mutate(a)
print(a)  # [1]

rebind(a)
print(a)  # [1]
```

## 避免遮蔽 builtins（前端也会踩）

```py
list = [1, 2, 3]
# 之后你就不能再用 list(...) 构造列表了
```

更推荐：

- `items`, `xs`, `arr`, `values` 等名字

## 小练习

1. 写一个闭包 `make_counter()`：每次调用返回递增整数（用 `nonlocal`）。
2. 写一个函数演示 `UnboundLocalError` 的触发条件，然后用 `global` 修复（仅作为理解练习）。
3. 传入一个 list 到函数里，分别测试“原地修改”和“重新绑定”对外部的影响。
