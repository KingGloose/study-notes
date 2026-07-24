# 1 命令结构分解：

```bash
arch -x86_64 bash -c "source ~/.nvm/nvm.sh && nvm install 12.22.12"
```

1、**`arch -x86_64`**
   - `arch` 是 macOS 的命令，用于指定运行架构。
   - `-x86_64` 强制后续命令在 **Intel x86 64位模拟环境**（Rosetta 2）下运行，解决 Apple Silicon 芯片对某些 x86 软件的兼容性问题。

2、**`bash -c "..."`**
   - 启动一个新的 Bash 子进程，并执行引号内的命令（`-c` 表示执行字符串命令）。

3、**`source ~/.nvm/nvm.sh`**
   - `source` 加载 `nvm.sh` 脚本到当前 Bash 环境（而非子进程）。
   - `~/.nvm/nvm.sh` 是 Node Version Manager (nvm) 的初始化脚本，启用 `nvm` 命令。

4、**`nvm install 12.22.12`**
   - 调用已激活的 `nvm` 命令，安装 Node.js 的 **v12.22.12** 版本。

# 2 完整执行流程

1、通过 Rosetta 2 模拟 x86_64 环境启动 Bash。

2、在子 Shell 中加载 nvm 环境变量和函数。

3、安装指定版本的 Node.js（该版本将在 x86_64 架构下运行）。
