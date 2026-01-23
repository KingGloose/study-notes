# pyenv

关联：[[02 环境配置]] | [[环境配置/uv]] | [[环境配置/venv 与 pip]] | [[环境配置/常见问题排查]]

`pyenv` 的定位非常明确：**只做一件事——管理多个 Python 解释器版本**。

前端类比：`pyenv` ≈ `nvm`。

> [!tip] 你真正需要 pyenv 的原因
> - macOS 自带 Python / brew Python / 项目需要的 Python 经常不一致
> - 你需要把项目锁定到一个版本（比如 3.12），保证本地和 CI 一致

## 安装（macOS 推荐 brew）

```bash
brew update
brew install pyenv
```

然后把初始化脚本加到 shell（zsh 举例）：

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

如果你用的是 bash，请改写到 `~/.bashrc` 或 `~/.bash_profile`。

> [!note] 发生了什么
> pyenv 通过“shims（垫片）”把 `python`/`pip` 等命令指向你当前选择的版本。
> 所以 PATH 顺序非常重要；PATH 问题是 pyenv 最常见坑之一（见 [[环境配置/常见问题排查]]）。

## 安装 Python 版本

列出可安装版本：

```bash
pyenv install --list
```

安装某个版本：

```bash
pyenv install 3.12.2
```

如果你在安装时遇到编译依赖问题，基本都能在 [[环境配置/常见问题排查]] 里按思路解决。

## 选择 Python 版本：global / local / shell

### global（全局默认）

```bash
pyenv global 3.12.2
```

### local（项目级，推荐）

在项目目录执行：

```bash
pyenv local 3.12.2
```

它会生成 `.python-version` 文件，把该目录（及子目录）锁定到此版本。

### shell（仅当前终端会话）

```bash
pyenv shell 3.12.2
```

## 验证你到底在用哪个 Python

这一步非常关键，很多“明明装了包却 import 不到”的问题，本质是你在用错解释器。

```bash
which python
python -V

pyenv which python
pyenv version
```

## pyenv 和虚拟环境的关系

你通常会这样组合：

1) 用 pyenv 锁 Python 版本
2) 用 [[环境配置/uv]] 或 [[环境配置/venv 与 pip]] 创建虚拟环境并装依赖

也就是说：

- pyenv 管“解释器”
- uv/venv 管“依赖隔离”

## 和前端工作流的类比

- `.python-version` ≈ `.nvmrc`
- `.venv/` ≈ `node_modules/`（但 Python 的虚拟环境同时包含可执行入口）
- `pyproject.toml` ≈ `package.json`

## 小练习（帮助你把心智模型做实）

1. 安装两个版本（例如 3.11 和 3.12），在两个目录分别 `pyenv local`，观察 `python -V` 是否跟随目录变化。
2. 在某个目录用 `python -m venv .venv` 创建虚拟环境，再切换 pyenv 版本，体会“解释器版本”和“虚拟环境”是两层东西。
