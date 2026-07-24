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

最初以为每次 CLI 命令都需要传 `--proxyServer` 参数，但实际上：

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

访问内网 OA 系统时，经常遇到未登录的情况。我们设计了一套分层处理策略：

**第一层：持久化 profile 自动保持登录态**

始终使用 `--userDataDir` 启动 daemon，Cookie 保存到磁盘，daemon 重启后登录态自动恢复：

```bash
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"
```

**第二层：检测未登录时自动注入 Cookie**

只有当持久化 profile 中的 Cookie 过期时，才需要重新注入。流程：

1. **检测未登录**：
```bash
chrome-devtools take_snapshot | grep -E "(未登录|403)"
```

2. **从用户日常 Chrome 提取 Cookie**：
```bash
zzcli cookie .zhuanspirit.com --format json
# 输出：[{"name":"sso_uid","value":"629423872","domain":".zhuanspirit.com"}, ...]
```

3. **注入 Cookie 到 chrome-devtools 浏览器**：
```bash
chrome-devtools evaluate_script "() => {
  document.cookie = 'sso_uid=629423872; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  document.cookie = 't_sso_code=xxx; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  document.cookie = 'sso_company_code=0; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  document.cookie = 'kid=xxx; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  return document.cookie;
}"
```

4. **刷新页面使 Cookie 生效**：
```bash
chrome-devtools navigate_page --type reload
```

注入成功后，Cookie 会保存到持久化 profile 中，后续操作无需再次注入。

**第三层：302 重定向引导登录（备选）**

如果 `zzcli cookie` 提取失败（用户日常 Chrome 也未登录），检查网络请求中的 302 重定向，引导用户到 SSO 登录页：

```bash
chrome-devtools list_network_requests --output-format json | grep '"302"'
chrome-devtools get_network_request --reqid <reqid>
# 从 Location header 获取 SSO 登录页 URL
```

**第四层：提醒用户手动登录**

以上方式都失败时，提醒用户手动登录。

#### 疑问 6：Cookie 注入是否有限制？

通过 `document.cookie` 注入 Cookie 有一个限制：**无法设置 HttpOnly 的 Cookie**。

但经过验证，转转 OA 系统的 SSO Cookie（`sso_uid`、`t_sso_code`、`sso_company_code`、`kid`）全部 `is_httponly=0`，可以通过 `document.cookie` 正常读写。

```sql
-- 从 Chrome Cookie 数据库验证
SELECT name, is_httponly FROM cookies WHERE host_key='.zhuanspirit.com';
-- kid|0, sso_uid|0, t_sso_code|0, sso_company_code|0
```

#### 疑问 7：是否每次调用都需要走 Cookie 注入流程？

**不需要。**

使用 `--userDataDir` 持久化 profile 后，Cookie 保存在磁盘上。正常流程是：

1. 启动 daemon（持久化 profile）
2. 导航到页面
3. 检查登录态
4. **已登录** → 直接操作
5. **未登录** → 走 Cookie 注入流程 → 注入后 Cookie 保存到 profile → 后续自动保持

只有 Cookie 过期时才需要重新注入。

## 技术细节

### Node.js 版本要求

chrome-devtools-mcp 的 `engines` 字段：

```json
{ "node": "^20.19.0 || ^22.12.0 || >=23" }
```

最低支持 Node 20.19.0。

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

### Profile 管理

始终使用持久化 profile：

```bash
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"
```

- Cookie、LocalStorage、Session 自动保存到磁盘
- daemon 重启后自动恢复
- 清除登录态：`rm -rf ~/.chrome-devtools-profile`

## 实践案例：OA 系统表单验证

### 需求

验证 OA 系统中，选择"行政"业务方后是否会出现"行政性质"字段。

### 完整流程

```bash
# 1. 启动 daemon（持久化 profile + 代理）
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"

# 2. 导航到目标页面
chrome-devtools navigate_page --url "https://oa.zhuanspirit.com/asset_manage/?#/asset/use/inbound/create"

# 3. 等待页面加载，检查登录态
sleep 3
chrome-devtools take_snapshot | grep -E "(未登录|403)"

# 4. 如果未登录，从用户 Chrome 提取 Cookie 并注入
zzcli cookie .zhuanspirit.com --format json
# 提取到 sso_uid、t_sso_code、sso_company_code、kid

chrome-devtools navigate_page --url "https://oa.zhuanspirit.com"
chrome-devtools evaluate_script "() => {
  document.cookie = 'sso_uid=629423872; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  document.cookie = 't_sso_code=xxx; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  document.cookie = 'sso_company_code=0; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  document.cookie = 'kid=xxx; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
  return document.cookie;
}"
chrome-devtools navigate_page --type reload

# 5. 重新导航到目标页面
chrome-devtools navigate_page --url "https://oa.zhuanspirit.com/asset_manage/?#/asset/use/inbound/create"
sleep 3

# 6. 获取快照，找到"业务方"下拉框
chrome-devtools take_snapshot | grep "combobox.*业务方"
# 输出：uid=3_49 combobox "* 业务方 :" ...

# 7. 点击下拉框
chrome-devtools click "3_49"

# 8. 等待下拉选项出现，找到"行政"
sleep 1
chrome-devtools take_snapshot | grep "行政"
# 输出：uid=4_5 StaticText "行政"

# 9. 点击"行政"
chrome-devtools click "4_5"

# 10. 等待页面更新，验证是否出现"行政性质"
sleep 2
chrome-devtools take_snapshot | grep "行政性质"
# 输出：uid=5_7 StaticText "行政性质"
#       uid=5_8 combobox "* 行政性质 :" ...

# 11. 截图保存结果
chrome-devtools take_screenshot --filePath /tmp/result.png

# 12. 停止 daemon（可选）
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

### CLI 模式（最终方案）

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
- ✅ 持久化 profile 保持登录态
- ❌ 输出是文本，需要解析

## 最佳实践

### 1. 环境准备

```bash
# 全局安装（需要 Node.js ^20.19.0 || ^22.12.0 || >=23）
npm i -g chrome-devtools-mcp@latest

# 验证安装
chrome-devtools --version
chrome-devtools status
```

### 2. 标准启动（始终使用持久化 profile）

```bash
# 开发调试（有界面，便于观察）
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile" \
  --headless false

# 无界面模式（性能更好）
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"
```

### 3. 登录态检查与注入

```bash
# 检查 daemon 状态
chrome-devtools status || chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"

# 导航到目标页面
chrome-devtools navigate_page --url "https://oa.zhuanspirit.com/..."

# 检查登录状态
if chrome-devtools take_snapshot | grep -q "未登录"; then
  # 从用户 Chrome 提取 Cookie
  COOKIES=$(zzcli cookie .zhuanspirit.com --format json)
  
  # 注入 Cookie（根据提取结果构造）
  chrome-devtools navigate_page --url "https://oa.zhuanspirit.com"
  chrome-devtools evaluate_script "() => {
    document.cookie = 'sso_uid=<value>; path=/; domain=.zhuanspirit.com; Secure; SameSite=None';
    // ... 其他 Cookie
    return document.cookie;
  }"
  chrome-devtools navigate_page --type reload
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

# 清除登录态
rm -rf ~/.chrome-devtools-profile
```

## Skill 落地方案

最终采用 **CLI 按需加载 + Skill 封装** 的组合方案：

```
skills/chrome-devtools/
├── SKILL.md                      # 核心使用指南
└── references/
    ├── installation.md           # 安装和环境准备
    ├── examples.md               # 典型工作流程
    └── troubleshooting.md        # 问题排查
```

**设计原则**：
- 不在全局 settings.json 中配置 MCP（零上下文开销）
- 所有命令内联在 SKILL.md 中，无需额外脚本
- 始终使用 `--userDataDir` 持久化 profile
- 只有检测到未登录时才走 Cookie 注入流程
- 完整命令列表通过 `chrome-devtools --help` 查看

## 常见问题

### Q1: daemon 无法启动

```bash
# 检查 Node 版本（需要 ^20.19.0 || ^22.12.0 || >=23）
node -v

# 清理残留 socket 文件
rm -f /tmp/chrome-devtools-mcp-*.sock

# 重新启动
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"
```

### Q2: 命令超时

```bash
# 检查 daemon 是否还在运行
chrome-devtools status

# 重启 daemon
chrome-devtools stop
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"
```

### Q3: Cookie 注入后仍然未登录

可能原因：
- Cookie 已过期：用户需要先在日常 Chrome 中重新登录
- Cookie 域名不匹配：确认注入时使用了正确的 domain
- Cookie 是 HttpOnly：无法通过 `document.cookie` 设置（转转 SSO Cookie 不是 HttpOnly，不会遇到此问题）

### Q4: 代理不生效

```bash
# 检查 Whistle 是否启动
w2 status

# 检查 daemon 启动参数
chrome-devtools status | grep proxy-server

# 重启 daemon 并带上代理参数
chrome-devtools stop
chrome-devtools start \
  --proxyServer http://127.0.0.1:8899 \
  --userDataDir "$HOME/.chrome-devtools-profile"
```

## 性能对比

| 指标 | MCP 模式 | CLI 模式 |
|------|---------|---------|
| 初始上下文占用 | ~15KB | 0 |
| 命令响应速度 | 快（直接调用） | 中（需要 socket 通信） |
| 数据格式 | 结构化 JSON | 文本（需解析） |
| 浏览器启动 | 每次调用时启动 | daemon 启动时启动一次 |
| 状态保持 | 需要手动管理 | daemon + 持久化 profile 自动管理 |
| 登录态 | 需要手动处理 | 持久化 profile + 自动注入 |
| 适用场景 | 频繁调用、需要结构化数据 | 按需使用、节省上下文 |

## 总结

Chrome DevTools MCP 的 CLI 模式通过巧妙的架构设计（Unix socket + daemon），实现了"按需加载、不占上下文"的目标。结合持久化 profile 和 `zzcli cookie` 自动注入，解决了登录态保持的问题。

最终落地方案的核心要点：
- **CLI 模式**：通过 Unix socket 连接 daemon，不会被 Claude Code 识别为 MCP，零上下文开销
- **持久化 profile**：始终使用 `--userDataDir`，Cookie 保存到磁盘，daemon 重启后自动恢复
- **按需注入**：只有检测到未登录时，才通过 `zzcli cookie` 提取 + `evaluate_script` 注入
- **代理配置**：在 daemon 启动时配置一次，后续命令无需重复
- **Skill 封装**：所有命令内联在 SKILL.md 中，无需额外脚本，参考 sentry-cli skill 的模式
