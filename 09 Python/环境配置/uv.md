# uv

关联：[[02 环境配置]] | [[环境配置/pyenv]] | [[环境配置/pyproject.toml 与依赖管理]] | [[环境配置/VS Code 开发体验]]

`uv` 是目前非常适合“应用开发”的一套现代工具：

- 依赖安装很快（体验上接近前端的 pnpm）
- 能管理虚拟环境（通常放在项目内 `.venv`）
- 围绕 `pyproject.toml` 工作，工程化程度高

> [!tip] 前端类比
> - `uv add xxx` ≈ `pnpm add xxx`
> - `uv sync` ≈ `pnpm install`（把环境同步到 lock 的状态）
> - `uv run ...` ≈ `pnpm run ...`（在正确的虚拟环境里执行命令）

## 安装（macOS）

```bash
brew install uv
uv --version
```

（其他平台安装方式以 `uv` 官方说明为准；你只需要记住：**先装 uv，再用 uv 管项目**。）

## 一个标准项目的推荐工作流

### 1) 初始化项目

在新目录：

```bash
uv init
```

它会生成 `pyproject.toml`（以及可能的其他项目文件）。

### 2) 选择 Python（可选，但强烈推荐明确版本）

如果你用 [[环境配置/pyenv]] 锁了版本，这一步通常就自然对齐了。

你要做的核心是：项目必须有一个明确的 Python 版本基线（例如 3.12）。

### 3) 创建虚拟环境

```bash
uv venv
```

通常会创建项目内的 `.venv/`。

### 4) 添加依赖

```bash
uv add requests
uv add --dev pytest
```

这会更新 `pyproject.toml`，并把依赖解析结果记录到 lock（具体文件名取决于 uv 版本）。

### 5) 同步环境（最常用命令之一）

```bash
uv sync
```

它会把你的 `.venv` 精确同步到 lock 描述的状态。

### 6) 运行命令（不要手动激活也能跑）

```bash
uv run python -V
uv run pytest
uv run python -m your_package
```

> [!tip] 为什么推荐 uv run
> 因为它能确保你运行的一定是“这个项目的解释器 + 这个项目的依赖”。
> 这能消灭大量“我本地能跑，你那不能跑”的环境问题。

## uv pip：把 uv 当成更快的 pip

如果你临时要执行类似 pip 的行为：

```bash
uv pip install rich
uv pip list
```

工程上仍建议优先用 `uv add/sync` 维护依赖状态（见 [[环境配置/pyproject.toml 与依赖管理]]）。

## 项目结构建议（应用开发）

一个非常常见、好维护的结构：

```text
project/
  pyproject.toml
  .python-version        # 如果你用 pyenv
  .venv/                 # uv venv
  src/your_app/
  tests/
```

## 常见坑（你提前知道会省很多时间）

### 1) 你以为你装到了项目里，其实装到了全局

解决：

- 尽量用 `uv add` / `uv sync`
- 运行用 `uv run ...`

### 2) VS Code 选错解释器

解决：在 VS Code 里显式选择项目的 `.venv`（见 [[环境配置/VS Code 开发体验]]）。

### 3) lockfile 没进 git

解决：把 lockfile 当成 `pnpm-lock.yaml` 一样对待：

- 应用项目：建议提交 lockfile
- 库项目：是否提交看团队规范（但你要懂它的价值）

## 小练习

1. 新建一个目录，用 `uv init` + `uv add requests` + `uv run python -c "import requests"` 验证链路。
2. 在 `pyproject.toml` 里加一个 `dev` 依赖（例如 pytest），用 `uv run pytest --version` 验证。
