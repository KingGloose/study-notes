# 1. 浏览器 Cookie 本地存储与登录态搬运

> **来源**:2026-07-28 和 AI 讨论「能否把本机 Chrome 的登录态注入 Obsidian 内置 webview」时的实测结论。
> 姊妹页:[[Obsidian webview 登录态注入]](Electron/浏览器侧)、[[Cookie 跨子域与跨窗口通信]](Cookie 作用域模型)。
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
前两层再怎么突破,DBSC 一出来,搬 cookie 这件事就从根源上不再适用——而且这是 W3C 标准,不是单个浏览器的实验性功能。

---

## 1.2 磁盘加密:macOS 上的 v10 方案(实测通过)

### 1.2.1 数据在哪

```bash
# Chrome
~/Library/Application Support/Google/Chrome/Default/Cookies

# Edge
~/Library/Application Support/Microsoft Edge/Default/Cookies

# Brave / Opera / Arc / Chromium —— 同样位置,只换目录名
```

这是一个 SQLite 数据库,`cookies` 表中每行的 `encrypted_value` 列是密文,[实测] 我的 Chrome 当前库有 469 条 cookie,全部是 `v10` 前缀。

### 1.2.2 解密链路(KDF + AES-128-CBC)

[实测] 完整流程:

```
Keychain → PBKDF2-SHA1(key, "saltysalt", 1003) × 16 bytes → AES-128-CBC 解密 → 去掉 32 bytes 前缀 → 明文
```

每一步拆开:

**① 从 Keychain 取 key**
```bash
security find-generic-password -w -s "Chrome Safe Storage" -a "Chrome"
```
Chrome 的 service name 是 `"Chrome Safe Storage"`,Edge 是 `"Microsoft Edge Safe Storage"`,[AI 补充] 其他 Chromium 系各不同(Brave 是 `"Brave Safe Storage"`,Arc 也是独立命名)。首次调用会弹系统授权对话框。

**② PBKDF2 派生**
```
Algorithm:  PBKDF2-SHA1
Password:   Keychain 里拿到的原始 key (24 bytes)
Salt:       "saltysalt" (固定,所有 Chromium 都一样)
Iterations: 1003
Output:     16 bytes
```

[AI 补充] 注意 `"saltysalt"` 这个盐是 Chromium 写死在源码里的——它不是安全措施,只是 KDF 必须有一个盐。真正的安全靠 Keychain 的门禁(只有本机已登录用户才能读)。

**③ AES-128-CBC 解密**(以 Node.js 为例)
```js
const crypto = require('crypto');
const decipher = crypto.createDecipheriv(
  'aes-128-cbc',
  derivedKey,                          // 16 bytes from PBKDF2
  Buffer.alloc(16, 32)                 // IV = 16 个空格(ASCII 0x20)
);
let plaintext = Buffer.concat([
  decipher.update(ciphertext),         // ciphertext = encrypted_value 去掉前 3 字节"v10"
  decipher.final()
]);
```

### 1.2.3 坑:32 字节前缀(网上教程普遍没写)

[实测] 解密得到的 plaintext 不是直接就是 cookie 值,前面多了 **32 字节的 host_key SHA-256**:

```
plaintext: [32 bytes SHA-256 of host_key] [actual cookie value]

示例:
host_key = ".zhihu.com"
plaintext = b"\xd1\x90...\xe0v;`" + "pAuKEsbbjLOjDavQXpFt..."
             ^ 32 bytes host hash        ^ 真正 cookie 值
```

[实测] 正确做法:
```js
const cookieValue = plaintext.subarray(32).toString();
// 对于 _xsrf(.zhihu.com): "pAuKEsbbjLOjDavQXpFt1sEGC"
```

2024 年之前的很多教程(和工具库)没这步,直接拿 plaintext 当 cookie 值——他们当时跑的是 Chromium 还没加前缀的版本。[AI 补充] 这是 Chromium 近年引入的 **cookie integrity check**,用来防止跨站污染:同一个 cookie 值被搬到不同 host_key 的域时,32 字节前缀对不上,浏览器能检测到。

---

## 1.3 App-Bound Encryption(v20):为什么 macOS 不受影响

[官方] Chromium 在 2024 年 7 月(Chrome 127)引入了 App-Bound Encryption。日志原文:

> *"On macOS this is the Keychain services. On Windows, Chrome uses the Data Protection API (DPAPI) which does not protect against malicious applications running as the same user. Starting in Chrome 127, we are introducing app-bound encryption to better secure cookies on Windows."* (Google Security Blog, 2024-07-30)

关键点:

- **v20 只加密 Windows 上的 cookie**。macOS 有 Keychain 档着(需要用户密码才能读),Google 认为足够。
- 在 Windows 上,v20 会把 cookie 绑到 Chrome.exe 的数字签名——**只有那一个 exe 能解密**。恶意软件虽然以同一用户身份运行,但它自己的 exe 权限不够。
- [AI 补充] 但半年不到,红队已经绕过了——`kawakatz/macCookies` 支持 `-win` 标志解 v20,`mpelka/get-cookies` 也加了 Windows 支持。v20 提高的不是绝对门槛,而是攻击成本(需要提权或进程注入而不是简单读文件)。

**对"搬 cookie"的影响**:如果你在 macOS 上做,这一层不存在。如果你要为 Windows 用户做插件,需要关注绕过方案的维护——v20 的绕过依赖 Chrome 内部机制,随时可能随 Chrome 版本变化。

---

## 1.3.5 Windows v10 的完整解密链路(实现时补)

> 这一节是 2026-07 真正做 [[Obsidian webview 登录态注入|Session Bridge 插件]] Windows 适配时补的。macOS 走 v10/AES-128-CBC(见 1.2),Windows 的 v10 是**另一套**:AES-256-GCM,而且密钥要先过 DPAPI。

### 密钥来源:Local State + DPAPI

Windows 上 cookie 的 AES key 不在系统凭据库里(没有 macOS 那种 Keychain),而是**加密后存在 `Local State` 文件**里:

```
%LOCALAPPDATA%\Google\Chrome\User Data\Local State   (JSON)
  └─ os_crypt.encrypted_key  (base64)
```

解开它的步骤:
1. base64 解码 `encrypted_key`
2. **去掉开头 5 字节的 `"DPAPI"` 前缀**(标记这是个 DPAPI blob,和 macOS 的 `v10` 前缀是两回事)
3. 剩下的是 DPAPI blob,调 Windows 的 `CryptUnprotectData(CurrentUser)` 解开 → 得到 **32 字节 AES-256 key**

### [实测坑] 不用原生模块也能调 DPAPI:走 PowerShell

DPAPI 是 Windows API,Node 没内置,常规做法是装 `win-dpapi` 原生模块——但 [[Obsidian webview 登录态注入|Obsidian 插件不能分发原生模块]]。绕过办法是**用 PowerShell 调 .NET 的 `ProtectedData.Unprotect`**,零原生依赖:

```powershell
Add-Type -AssemblyName System.Security;
$blob=[Convert]::FromBase64String('<dpapi_blob_b64>');
$key=[System.Security.Cryptography.ProtectedData]::Unprotect(
  $blob,$null,[System.Security.Cryptography.DataProtectionScope]::CurrentUser);
[Convert]::ToBase64String($key)
```

这条路是 codex 相关工具(`Uni-CLI`、`gstack-windows`)的通用做法,算业界共识的"零依赖 DPAPI"方案。

### cookie 值本身:AES-256-GCM(和 macOS 的 CBC 不同)

拿到 32 字节 key 后,解 `encrypted_value`:

```
encrypted_value = "v10"(3B) + nonce(12B) + ciphertext + tag(16B)
算法:AES-256-GCM,key=上面的 32B,iv=nonce,authTag=tag
解出的明文前 32 字节仍是 host hash 前缀,strip 掉(和 macOS 一样)
```

对比一下两个平台的 v10,别混:

| | macOS v10 | Windows v10 |
|---|---|---|
| 密钥来源 | Keychain(直接是 key) | Local State + DPAPI 解 |
| KDF | PBKDF2-SHA1(saltysalt,1003) | 无(DPAPI 直接给 32B) |
| 加密算法 | AES-**128**-CBC | AES-**256**-GCM |
| IV | 16 个空格(0x20) | 密文里的 nonce(12B) |
| 32 字节 host hash 前缀 | 有 | 有 |

### [实测边界] v20 我们不做

Windows 上 Chrome 127+ 新写的 cookie 是 v20(前缀不是 `"v10"`),`encrypted_key` 也没有 `DPAPI` 前缀而是 app-bound 的。绕过 v20 要提权 + 进程注入(属攻击手法),Session Bridge **直接跳过 v20 cookie**,不硬碰。现实影响:随 Chrome 版本推进,Windows 上可用的 cookie 会越来越少(老 v10 逐渐被 v20 替换),这是 Windows 版天然的衰减,macOS 无此问题。

---

## 1.4 DBSC(设备绑定会话凭证):终局约束

[官方] Google 在 2025 年发布了 DBSC(Device Bound Session Credentials),这是一个 **W3C 标准草案**,不只有 Chrome 在做。

核心机制:
1. 登录时,浏览器生成一对公私钥。私钥存在 **TPM**(Windows)或 **Secure Enclave**(macOS)里。
2. 服务器在设 session cookie 的同时,记住对应的公钥。
3. 后续请求时,浏览器用私钥对特定 challenge 签名,服务器验证签名才认这个 session。

**这意味着什么**:

| 传统 session cookie | DBSC 开启后 |
|---|---|
| 搬走 cookie → 登进去了 | 搬走 cookie → 拿不到私钥签名 → 服务器拒收 |
| 本机不同浏览器之间 cookie 互不干扰 | 同也不互通——私钥在 TPM 里,连 Chrome 自己都拿不到明文私钥 |

[AI 补充] 那是不是这条路很快就没用了?

- **现在是窗口期**。DBSC Chrome 146 在 Windows 公开发布,macOS 在后续版本跟上。但最关键的不是浏览器的节奏,是**服务端要不要配**。DBSC 需要服务端改造——设 `Set-Cookie` 的同时发 `Sec-Session-Registration`,每个认证请求验签。大站(Google、GitHub)会第一批上,内网站点和小站很久都不会跟上。
- 所以这条路的实用价值在未来 2-3 年内是**分化的**:对内网 SSO 系统几乎无影响,对 Google/Figma/Notion 等第三方 SaaS 会逐批失效。
- Google 官方说法:"*DBSC is intended to make cookie theft no longer useful for attackers.*" 但"不再有用"需要服务端真的把所有 cookie 都升级成 DBSC——这个迁移可能需要很多年。

---

## 1.5 搬 cookie 的实际限制清单

除去前面的加/解密技术问题,实际搬过去能不能用还取决于:

### 1.5.1 UA 指纹不匹配

[实测] Obsidian 的 webview 对 `accounts.google.com` 会把 UA 改成 `"Chrome"`(我在 `obsidian.asar/main.js` 的 `onBeforeSendHeaders` 里确认了这行代码)。但即使不强制改,webview 的默认 UA 和 Chrome 的也不同,网站能检测出来。

`cf_clearance`(Cloudflare) 是典型的:它绑 IP + UA,UA 变了就触发重新验证。

### 1.5.2 Google 不只是验 cookie

Google 账号系统有设备指纹、环境校验、浏览器特征多层验证。搬 cookie 过去大概率被登出。社区里 Custom Frames(#136 issue)、Surfing(#294 issue)、Extended Browser(官方 FAQ 明确写了"Google 不保证能用")全都有同类问题。

### 1.5.3 分区 cookie(CHIPS)和 SameSite

[实测] Obsidian 的 partition cookie 库(Cloudflare 107 条)里有 20 个字段,包括 `top_frame_site_key` 和 `has_cross_site_ancestor`。Chrome 从 114 开始支持 **CHIPS**(Cookies Having Independent Partitioned State,`Partitioned` 属性)——这些 cookie 不按 domain 全局共享,而是按 **(top-level site, embedded site)** 的 key 来隔离。

如果用 `cookies.set()` 写 cookie,要注意:如果你的插件是从 Chrome `Default/Cookies` 读的(这是「主窗口」的 cookie 库),但目标域名在 Obsidian webview 里是内嵌在某个第三方站里的 iframe——CHIPS 的 partition key 不同,写进去的 cookie 不会被发出。

---

## 1.6 技术链路总结

```
Chrome Cookies.db (加密, ~/Library/Application Support/Google/Chrome/Default/)
  ↓ ① cp 到临时文件(Chrome 运行时锁库)
  ↓ ② security find-generic-password -w -s "Chrome Safe Storage"
  ↓ ③ PBKDF2-SHA1(key, "saltysalt", 1003) → 16 bytes
  ↓ ④ AES-128-CBC 解密(IV = 16 个空格)
  ↓ ⑤ 去掉 32 bytes host hash 前缀 → 明文 cookie 值
  ↓ ⑥ session.fromPartition("persist:vault-<appId>").cookies.set({url, name, value, domain, path, secure, httpOnly, expirationDate, sameSite})
  ↓ ⑦ Chromium 自己落盘 Partitions/Cookies (明文,无加密)
Obsidian webview (下次打开网页自带登录态)
```

> 安全提醒:Obsidian 的 Partition cookie 库 value 列是明文,未加密(没有 `Obsidian Safe Storage` keychain 项)。
> 任何能读你 home 目录的程序都能直接读到 webview 里的全部登录态。Obsidian 本身不做 cookie 加密。
> 这是个值得留意的点——不是说不要用,而是要知道它的安全边界。

---

## 1.7 相关工具和参考

- `chrome-sso-cookie` skill:本库自带的 Chrome → curl cookie 提取工具,走 `browser_cookie3` + Python,代码在 `skills/chrome-sso-cookie/`
- `mpelka/get-cookies`:Node.js CLI,支持 macOS Keychain + Windows
- `kawakatz/macCookies`:penetration testing 工具,支持 v10 和 v20(Windows)
- [Improving the security of Chrome cookies on Windows](https://security.googleblog.com/2024/07/improving-security-of-chrome-cookies-on.html):Google 官方宣布 App-Bound Encryption
- [W3C DBSC 草案](https://www.w3.org/TR/dbsc/):设备绑定会话的协议规范
