# venv 与 pip

关联：[[02 环境配置]] | [[环境配置/pyenv]] | [[环境配置/uv]] | [[Python语法/模块与包（import）]]

这套方案是 Python 官方内置的“最小可用组合”：

- `venv`：创建虚拟环境（隔离依赖）
- `pip`：安装第三方包

即使你最终使用 [[环境配置/uv]] 或 [[环境配置/Conda]]，理解 venv + pip 的机制依然很重要：它们是 Python 工程的地基。

## 1) 创建虚拟环境（项目内 .venv）

在项目目录执行：

```bash
python -m venv .venv
```

> [!tip] 为什么写 python -m venv
> 因为你要确保是“你当前选择的 python 解释器”在创建环境，而不是某个飘忽不定的 venv 命令。

## 2) 激活虚拟环境

macOS / Linux（bash/zsh）：

```bash
source .venv/bin/activate
```

激活后你会看到终端提示符前面出现 `(.venv)`。

退出：

```bash
deactivate
```

## 3) 安装依赖（永远用 python -m pip）

```bash
python -m pip install --upgrade pip
python -m pip install requests
python -m pip list
```

> [!warning] 不要用 sudo pip
> 一旦你在系统环境里 sudo 装包，很容易把 Python 环境搞到不可维护。

## 4) 依赖记录：requirements.txt 的来龙去脉

最朴素的方式：

```bash
python -m pip freeze > requirements.txt
```

然后别人用：

```bash
python -m pip install -r requirements.txt
```

但你要知道它的局限：

- `freeze` 记录的是“当前环境里所有包的精确版本”，容易夹带无关依赖
- 它缺少更强的元数据表达（脚本入口、可选依赖、Python 版本约束等）

所以应用开发更推荐转向 `pyproject.toml`（见 [[环境配置/pyproject.toml 与依赖管理]]），以及像 [[环境配置/uv]] 这样的工具。

## 5) 如何判断你 import 的到底是哪个环境的包

在虚拟环境里运行：

```bash
python -c "import sys; print(sys.executable)"
python -c "import site; print(site.getsitepackages())"
```

这能快速定位“你是不是用错了解释器”。

## 小练习

1. 用 `python -m venv .venv` 创建环境，装 `requests`，然后 `python -c "import requests"` 验证。
2. 故意不激活 `.venv`，再运行 `python -c "import requests"`，观察是否报错（理解隔离的价值）。
