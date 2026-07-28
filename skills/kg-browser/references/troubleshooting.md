# kg-browser 排查

## 连接失败

### `Network.enable timed out` / `Timeout waiting for daemon response`

daemon 起来了但连不上 Chrome。最常见原因：**`DevToolsActivePort` 里的 WS UUID 已失效**。

该文件在 `~/Library/Application Support/Google/Chrome/DevToolsActivePort`，两行：
```
53563                                              ← 端口
/devtools/browser/319232b7-4e3b-...                ← WS UUID（Chrome 重启会变）
```

Chrome 重启后 UUID 变了但文件可能没更新（实测遇到过文件是几天前的）。
排查：
```bash
ls -la "$HOME/Library/Application Support/Google/Chrome/DevToolsActivePort"   # 看时间戳
lsof -nP -iTCP:<端口> -sTCP:LISTEN                                            # 确认是 Chrome 在听
```

**修复**：让主人在 `chrome://inspect/#remote-debugging` 勾选 Allow remote debugging，
**彻底退出 Chrome（⌘Q，不是关窗口）**，重新打开。这会重写该文件。

### `未找到 chrome-devtools 命令`

```bash
npm i -g chrome-devtools-mcp@latest
```

### CDP 的 HTTP 接口（`/json/version`）不响应

正常现象，不用管。较新 Chrome 限制了 CDP 的 HTTP 端点，但 **WebSocket 端点仍可用**——
连接脚本走的就是 WS，不依赖 HTTP 接口。别拿 `curl /json/version` 当连通性判据。

### 连上了但 `list_pages` 是空的

大概率连到了**隔离浏览器**而不是用户 Chrome。原因通常是：在 `connect-chrome.sh`
成功之前就执行了 `chrome-devtools` 的页面命令，CLI 隐式启了个干净实例。
`chrome-devtools stop` 后重新跑连接脚本。

## 提取失败

### 正文长度异常小 / 拿不到内容

按顺序排查：
1. **页面真的加载完了吗** —— `evaluate_script "() => document.readyState"` 应为 `complete`
2. **需要登录吗** —— 让主人在可见 Chrome 里看这页是否正常显示。**不要尝试绕过登录**
3. **内容被折叠了吗** —— 知乎回答默认折叠，见 `site-selectors.md`
4. **虚拟滚动/懒加载吗** —— Notion、语雀长文只渲染视口内容，需逐屏滚动
5. **在 iframe 里吗** —— `list_pages` 看有没有子 frame
6. **Shadow DOM 吗** —— 试 `el.shadowRoot.innerHTML`

### 选择器失效（站点改版）

用 SKILL.md 的"探选择器"片段按文字量重新找，找到后**更新 `site-selectors.md`**。

### 输出太大刷屏

用 `--filePath` 写文件：
```bash
chrome-devtools evaluate_script "() => document.querySelector('...').outerHTML" --filePath /tmp/body.html
```

## 跨平台

### macOS

直接可用（本 skill 主要在 macOS 上验证）。

### WSL2 访问 Windows 侧 Chrome

WSL 和 Windows 是不同网络命名空间，需要额外配置：
1. Windows 上以调试端口启动 Chrome：
   `chrome.exe --remote-debugging-port=9222`
2. WSL 里连 Windows 主机：`$(hostname).local:9222` 或从 `/etc/resolv.conf` 拿 nameserver IP
3. Chrome 默认只监听 `127.0.0.1`，跨命名空间可能连不上，可能需要端口转发
   （`netsh interface portproxy`）

**配不通就别硬扛**，用降级方案：
- 主人手动复制正文文字发过来
- 或用浏览器扩展（如 `zhihu-md`）导出 Markdown 文件，再走 `kg-doc` 摄入

两种降级方案都不影响后续的沉淀流程——那部分本来就是 AI 做的。
