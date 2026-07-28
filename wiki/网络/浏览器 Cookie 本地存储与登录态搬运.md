# 1. 浏览器 Cookie 本地存储与登录态搬运

> **来源**:2026-07-28 和 AI 讨论「能否把本机 Chrome 的登录态注入 Obsidian 内置 webview」时的实测结论。
> 姊妹页:[[Obsidian webview 登录态注入]](Obsidian/Electron 侧)、[[Cookie 跨子域与跨窗口通信]](Cookie 作用域模型)。
> **为什么值得留页**:网上教程写 Chrome cookie 解密的一大片,但**绝大多数都漏了 32 字节前缀**(照抄会拿到乱码然后以为是密钥错了);
> 而 App-Bound Encryption「只在 Windows」和 DBSC 是这条路的**长期天花板**,这两点必须一起看才能判断这类方案值不值得做。
> 标注约定:[实测] = 我在本机 macOS + Chrome 上跑通过 / [官方] = 有官方文档或博客出处 / [AI 补充]。

---

## 1.1 全景:三个安全层级,决定了"搬 cookie"这条路能走多远

| 层级 | 保护什么 | 谁做的 | 对"搬 cookie"的影响 |
|---|---|---|---|
| **磁盘加密**(Keychain / DPAPI) | 别人读不到你的 cookie 文件 | 所有 Chromium 浏览器 | 能绕(本人本机有 Keychain 权限) |
| **App-Bound Encryption**(v20) | 只有 Chrome 本体能解 | Chrome 127+,**仅 Windows** | macOS 不受影响;Windows 上要另想办法 |
| **DBSC**(设备绑定会话) | cookie 搬走也没用 | Chrome 146+,服务端要配合 | **无解**。这是终局约束 |

理解顺序很重要:**前两层是"能不能拿到明文"的问题,第三层是"拿到明文有没有用"的问题**。
前两层再怎么突