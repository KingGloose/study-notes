# Chrome DevTools MCP 深度实践：从疑问到落地

## 背景

在探索 AI 驱动的浏览器自动化方案时，我们发现了 Chrome DevTools MCP（Model Context Protocol）这个工具。它承诺提供强大的浏览器控制能力，但在实际使用过程中遇到了一系列技术问题和架构疑问。本文记录了从初次接触到最终落地的完整过程，包括技术细节、架构分析和实践经验。

## 初始需求

我们的核心需求是：
1. **按需加载**：不希望在 Claude Code 启动时就加载所有 MCP 工具定义（占用上下文）
2. **代理支持**：需要通过 Whistle 代理访问内网 OA 系统
3. **登录态保持**：避免每次操作都重新登录
4. **灵活调用**：能够通过简单的命令行方式调用浏览器自动化功能

## 技术调研过程

### 第一阶段：MCP vs CLI 的困惑

最初的调研发现 chrome-devtools-mcp 有两种使用方式：
- **MCP 模式**：在 Claude Code 的 settings.json 中配置，工具定义会加载到上下文
- **CLI 模式**：通过命令行直接调用

这引发了第一个核心疑问：**CLI 模式是否真的能节省上下文？**

#### 疑问 1：CLI 的本质是什么？

从官方文档看到：
> A CLI is also provided for use without MCP.

但深入研究后发现，CLI 实际上是通过 Unix socket 连接到后台的 MCP daemon：

```typescript
// src/daemon/client.ts
const socket = net.createConnection({
  path: socketPath,  // Unix socket 路径，如 /tmp/chrome-devtools-mcp-501.sock
});
```

这让我们产生了第二个疑问。

#### 疑问 2：如果 CLI 连接到 MCP daemon，那还算"不占用上下文"吗？

这是最关键的问题。如果 daemon 本质上是 MCP server，那它的工具定义会不会还是被 Claude Code 识别？

**答案：不会。**

原因在于通信协议的差异：

| 维度 | MCP 模式 | CLI 模式 |
|------|---------|---------|
| 配置方式 | settings.json 中显式配置 | 无需配置 |
| 通信协议 | stdio（标准输入输出） | Unix socket |
| Claude Code 可见性 | ✅ 工具定义加载到上下文 | ❌ Claude Code 不知道 daemon 存在 |
| 调用方式 | 直接调用 MCP 工具 | 通过 Bash 工具执行 CLI 命令 |

**关键点**：Claude Code 的 MCP 系统只识别通过 stdio 通信的 server。daemon 通过 Unix socket 监听，对 Claude Code 来说是"隐形"的。

#### 疑问 3：为什么要设计成 daemon 架构？

如果 CLI 只是为了节省上下文，为什么不直接让 CLI 控制浏览器，而要通过 daemon？

**答案：状态保持。**

```bash
# 第一次命令：启动浏览器
chrome-devtools navigate_page --url "https://example.com"

# 第二次命令：复用同一个浏览器实例
chrome-devtools take_screenshot --filePath /tmp/screenshot.png
```

如果没有 daemon，每次 CLI 命令都要：
1. 启动浏览器（慢）
2. 执行操作
3. 关闭浏览器（丢失状态）

有了 daemon：
- 浏览器持续运行
- Cookie、登录态、页面状态都保留
- 多个命令之间无缝衔接

### 第二阶段：代理配置的困惑

#### 疑问 4：代理配置在哪里生效？

最初以为每次 CLI 命令都需要传 `--proxy-server` 参数，但实际上：

```bash
# 启动时配置代理（只需一次）
chrome-devtools start --proxyServer http://127.0.0.1:8899

# 后续命令无需重复传递
chrome-devtools navigate_page --url "https://oa.zhuanspirit.com"
chrome-devtools take_screenshot --filePath /tmp/screenshot.png
```

**原因**：代理是浏览器层面的配置，不是 MCP 命令层面的。daemon 启动浏览器时传入 `--proxy-server` 参数，浏览器的所有请求都会走这个代理。

验证代理是否生效：
```bash
# 检查 daemon 启动参数
chrome-devtools status
# 输出包含：args=["--proxy-server","http://127.0.0.1:8899",...]
```

### 第三阶段：登录态处理

#### 疑问 5：如何自动处理未登录状态？

访问内网 OA 系统时，经常遇到未登录的情况。我们设计了一套自动检测流程：

1. **检测未登录**：
```bash
chrome-devtools take_snapshot | grep -E "(未登录|403|登录)"
```

2. **查找 302 重定向**：
```bash
chrome-devtools list_network_requests --output-format json | grep '"302"'
```

3. **提取 SSO 登录页 URL**：
```bash
chrome-devtools get_network_request --reqid <302请求的reqid>
# 从 Response Headers 的 Location 字段获取
```

4. **自动导航到 SSO 页面**：
```bash
chrome-devtools navigate_page --url "<SSO登录页URL>"
```

5. **检测并点击 SSO 按钮**：
```bash
chrome-devtools take_snapshot | grep "继续.*登录"
# 假设输出：uid=1_5 button "继续在浏览器中登录访问"
chrome-devtools click "1_5"
```

**实际案例**：在测试中发现，有些系统没有 302 重定向，而是直接返回 200 但页面显示未登录。这种情况下，需要直接提醒用户手动登录。

## 技术细节

### CLI 命令格式

从实际测试中总结的命令格式：

```bash
# 页面导航
chrome-devtools navigate_page --url "https://example.com"

# 截图（注意参数是 --filePath 不是 --file-path）
chrome-devtools take_screenshot --filePath /tmp/screenshot.png

# 元素交互（uid 是位置参数，不需要 --uid）
chrome-devtools click "1_47"
chrome-devtools fill "1_59" "测试内容"

# 键盘操作
chrome-devtools press_key "Enter"
chrome-devtools press_key "Control+A"

# 页面快照
chrome-devtools take_snapshot
chrome-devtools take_snapshot --filePath /tmp/snapshot.txt
```

### 网络请求分析

CLI 支持查看网络请求，这对调试非常有用：

```bash
# 列出所有请求
chrome-devtools list_network_requests

# JSON 格式输出（便于解析）
chrome-devtools list_network_requests --output-format json

# 查看特定请求详情
chrome-devtools get_network_request --reqid 193
```

输出示例：
```json
{
  "requestId": 193,
  "method": "GET",
  "url": "https://funiqueauth.zhuanspirit.com/common/login?appCode=asset_manage",
  "status": "200",
  "responseHeaders": {
    "set-cookie": "sso_company_code=0; Max-Age=259200; ..."
  }
}
```

### Profile 管理

登录态保存在 profile 中：

```bash
# 默认 profile（isolated 模式，临时）
~/.cache/chrome-devtools-mcp/chrome-profile-*

# 持久化 profile（推荐）
chrome-devtools start --userDataDir "$HOME/.chrome-debug-profile"
```

**注意**：
- `--isolated` 模式会在浏览器关闭后自动清理 profile
- 不带 `--isolated` 或指定 `--userDataDir` 可以保持登录态

## 实践案例：OA 系统表单验证

### 需求

验证 OA 系统中，选择"行政"业务方后是否会出现"行政性质"字段。

### 完整流程

```bash
# 1. 启动 daemon（带代理和持久化 profile）
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.cache/chrome-devtools-mcp/chrome-profile" \
  --headless false

# 2. 导航到目标页面
chrome-devtools navigate_page --url "https://oa.zhuanspirit.com/asset_manage/?#/asset/use/inbound/create"

# 3. 等待页面加载
sleep 3

# 4. 检查登录状态
chrome-devtools take_snapshot | grep -E "(未登录|403)"

# 如果未登录，引导用户登录（有界面模式下可以手动登录）

# 5. 获取快照，找到"业务方"下拉框
chrome-devtools take_snapshot | grep "combobox.*业务方"
# 输出：uid=3_32 combobox "* 业务方 :" ...

# 6. 点击下拉框
chrome-devtools click "3_32"

# 7. 等待下拉选项出现
sleep 1

# 8. 找到"行政"选项
chrome-devtools take_snapshot | grep "行政"
# 输出：uid=6_5 StaticText "行政"

# 9. 点击"行政"
chrome-devtools click "6_5"

# 10. 等待页面更新
sleep 2

# 11. 验证是否出现"行政性质"
chrome-devtools take_snapshot | grep "行政性质"
# 输出：uid=7_7 StaticText "行政性质"
#       uid=7_8 combobox "* 行政性质 :" ...

# 12. 截图保存结果
chrome-devtools take_screenshot --filePath /tmp/result.png

# 13. 停止 daemon
chrome-devtools stop
```

### 验证结果

✅ 选择"行政"后，页面确实出现了"行政性质"下拉框（带 `*` 必填标记）

## 架构对比

### MCP 模式

```
┌─────────────┐
│ Claude Code │
└──────┬──────┘
       │ stdio (MCP 协议)
       │ 工具定义加载到上下文
       ↓
┌──────────────────┐
│ chrome-devtools  │
│   MCP Server     │
└────────┬─────────┘
         │
         ↓
    ┌────────┐
    │ Chrome │
    └────────┘
```

**特点**：
- ✅ 直接调用 MCP 工具
- ✅ 结构化数据返回
- ❌ 占用初始上下文（~15KB）

### CLI 模式

```
┌─────────────┐
│ Claude Code │
└──────┬──────┘
       │ Bash 工具
       │ 执行 CLI 命令
       ↓
┌──────────────┐
│ chrome-      │
│ devtools CLI │
└──────┬───────┘
       │ Unix socket
       │ /tmp/chrome-devtools-mcp-501.sock
       ↓
┌──────────────────┐
│   daemon         │
│ (MCP Server 实例) │
└────────┬─────────┘
         │
         ↓
    ┌────────┐
    │ Chrome │
    └────────┘
```

**特点**：
- ✅ 不占用 Claude Code 上下文
- ✅ daemon 保持浏览器状态
- ✅ 代理只需配置一次
- ❌ 输出是文本，需要解析
- ❌ 架构相对复杂

## 最佳实践

### 1. 环境准备

```bash
# 全局安装
npm i -g chrome-devtools-mcp@latest

# 验证安装
chrome-devtools --version
chrome-devtools status
```

### 2. 启动配置

```bash
# 开发调试（有界面，便于观察）
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --headless false \
  --userDataDir "$HOME/.chrome-debug-profile"

# 生产环境（无界面，性能更好）
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --headless true \
  --userDataDir "$HOME/.chrome-debug-profile"
```

### 3. 错误处理

```bash
# 检查 daemon 状态
if ! chrome-devtools status | grep -q "running"; then
  echo "daemon 未运行，正在启动..."
  chrome-devtools start --proxyServer http://127.0.0.1:8899
fi

# 检查登录状态
if chrome-devtools take_snapshot | grep -q "未登录"; then
  echo "需要登录，请在浏览器中完成登录"
  exit 1
fi
```

### 4. 等待策略

```bash
# 等待页面加载
sleep 3

# 等待动态内容（循环检查）
for i in {1..10}; do
  if chrome-devtools take_snapshot | grep -q "目标文本"; then
    echo "内容已加载"
    break
  fi
  echo "等待中... ($i/10)"
  sleep 1
done
```

### 5. 清理资源

```bash
# 脚本结束时停止 daemon
trap "chrome-devtools stop" EXIT

# 或者手动停止
chrome-devtools stop
```

## 常见问题

### Q1: daemon 无法启动

```bash
# 检查 Node 版本
node -v  # 需要 >= 20

# 清理残留 socket 文件
rm -f /tmp/chrome-devtools-mcp-*.sock

# 重新启动
chrome-devtools start
```

### Q2: 命令超时

```bash
# 检查 daemon 是否还在运行
chrome-devtools status

# 重启 daemon
chrome-devtools stop
chrome-devtools start --proxyServer http://127.0.0.1:8899
```

### Q3: 登录态丢失

```bash
# 使用持久化 profile（不要用 --isolated）
chrome-devtools start \
  --userDataDir "$HOME/.chrome-debug-profile" \
  --proxyServer http://127.0.0.1:8899
```

### Q4: 代理不生效

```bash
# 检查 Whistle 是否启动
w2 status

# 检查 daemon 启动参数
chrome-devtools status | grep proxy-server

# 重启 daemon 并带上代理参数
chrome-devtools stop
chrome-devtools start --proxyServer http://127.0.0.1:8899
```

## 性能对比

| 指标 | MCP 模式 | CLI 模式 |
|------|---------|---------|
| 初始上下文占用 | ~15KB | 0 |
| 命令响应速度 | 快（直接调用） | 中（需要 socket 通信） |
| 数据格式 | 结构化 JSON | 文本（需解析） |
| 浏览器启动 | 每次调用时启动 | daemon 启动时启动一次 |
| 状态保持 | 需要手动管理 | daemon 自动管理 |
| 适用场景 | 频繁调用、需要结构化数据 | 按需使用、节省上下文 |

## 总结

Chrome DevTools MCP 的 CLI 模式通过巧妙的架构设计（Unix socket + daemon），实现了"按需加载、不占上下文"的目标。虽然架构相对复杂，但在实际使用中表现良好，特别适合以下场景：

1. **按需浏览器自动化**：不希望在 Claude Code 启动时就加载所有工具
2. **需要代理支持**：内网环境或需要抓包调试
3. **需要保持状态**：登录态、Cookie、页面状态需要在多个命令间保持
4. **脚本化操作**：可以将 CLI 命令组合成 shell 脚本

关键要点：
- CLI 通过 Unix socket 连接 daemon，不会被 Claude Code 识别为 MCP
- daemon 保持浏览器运行，实现状态保持
- 代理在 daemon 启动时配置，后续命令无需重复
- 登录态保存在 profile 中，使用 `--userDataDir` 可以持久化

通过这次深度实践，我们不仅解决了技术问题，更重要的是理解了工具的设计思想和架构权衡，为后续的浏览器自动化工作奠定了坚实基础。
