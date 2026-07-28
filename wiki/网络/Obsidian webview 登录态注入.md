# 1. Obsidian webview 的 Electron 内幕与登录态注入方案

> **来源**:2026-07-28 实拆 Obsidian 1.8.10 asar 文件,逐行读源码 + 检查运行时状态。
> 姊妹页:[[浏览器 Cookie 本地存储与登录态搬运]](Chrome 侧的 cookie 解密)、[[Cookie 跨子域与跨窗口通信]](域名/Cookie 基础)。
> **为什么值得留页**:社区对这个话题有不少猜测(Figma 嵌不进、Google 登不了、Custom Frames 想共享 session)。我把 Obsidian 实际怎么做的全部挖出来了——不是猜的。

---

## 1.1 文件结构和大小

```
/Applications/Obsidian.app/Contents/Resources/
├── obsidian.asar        # 主应用代码(前端,渲染进程,≈3MB)
├── app.asar             # Electron main process 壳(很小,≈12KB)
└── lib/                 # CodeMirror / Moment / Pixi 等第三方库
```

`app.asar` 的作用很单薄:启动更新器 → 选包(本地埋的 `obsidian.asar` 还是下载的新版 `obsidian-X.Y.Z.asar`)→ `require(main)` 启动。更新的包直接放 `~/Library/Application Support/obsidian/` 下面,文件名叫 `obsidian.X.Y.Z.asar`。

`obsidian.asar` 里面才是真东西:
```
app.js     (3,074,224 bytes) ← 整个前端逻辑
main.js    (33,318 bytes)    ← Electron 进程通信层
```

---

## 1.2 Webview 的 partition 是怎么设计的(关键)

### 1.2.1 partition 命名规则

我在 `app.js` 里找到了这行:

```js
App.prototype.getWebviewPartition = function() {
    return "persist:vault-" + this.appId;
};
```

[实测] 我本机 vault 的 appId 是 `3e07e723679e4e4e`,所以 partition 是 `persist:vault-3e07e723679e4e4e`,对应:

```
~/Library/Application Support/obsidian/Partitions/vault-3e07e723679e4e4e/
├── Cookies          # SQLite,明文,20 列(含 CHIPS 字段)
├── Local Storage/
├── Session Storage/
├── ...
```

`persist:` 前缀意味着 cookie 和 localStorage 是**跨重启持久化**的。不带 `persist:` 就是纯内存,关掉就没。这个设计意味着:**从浏览器搬进来的 cookie 只需要写一次,重启 Obsidian 后还在**。

### 1.2.2 Obsidian 主窗口 vs webview 的 session 是隔离的

Obsidian 自己的窗口(渲染 Markdown 的那个)用的是 `defaultSession`。
Web viewer 的 webview 标签用的是 `persist:vault-<appId>` 这个 **独立 partition**。

好处:webview 里的 cookie 不会泄露给插件的主进程(插件跑在 `defaultSession` 的环境)。
坏处:你需要把目标域名的 cookie 写进**两个 session** 里的哪一个,取决于你的使用场景——是给 web viewer 用(写 partition),还是给插件的 fetch 请求用(写 `defaultSession`)。

### 1.2.3 自定义浏览器 session(create-browser-session)

`main.js` 里有一段 IPC handler,插件可以调用:

```js
ipcMain.on("create-browser-session", async (event, partitionKey, adblockOverride) => {
    // 创建 session,挂 adblock、UA 改写、权限
    session.fromPartition(partitionKey);
    session.setUserAgent(...)               // 去掉 "Obsidian" / "Electron" 标识
    session.webRequest.onBeforeSendHeaders  // 对 Google 改 UA 为 "Chrome"
    session.setPermissionCheckHandler       // 放行某些权限
});
```

这解释了 Obsidian 为什么对 Google 账号系统有特殊处理——它自己在 `onBeforeSendHeaders` 里把 `sec-fetch-dest` 和 `sec-ch-ua` 头删了,对 `accounts.google.com` 把 UA 改成了 `"Chrome"`。但即便如此,Google 还是不一定认(见姊妹页 [[浏览器 Cookie 本地存储与登录态搬运#1.5.2 Google 不只是验 cookie]])。

---

## 1.3 插件怎么拿到这个 session:走 `@electron/remote`

### 1.3.1 remote 是可用的

Obsidian 在 `app.asar/main.js` 里全局初始化了:

```js
electron.remote = require('@electron/remote/main');
let {app, protocol, net, remote} = electron;
remote.initialize();
```

渲染进程里(我们写的插件也是渲染进程)通过 `enhance.js` 的 `enhanceElectron` 函数注入:

```js
// enhance.js, key line
e.electron = require('electron');
e.electron.remote = require('@electron/remote');
e.electronWindow = e.electron.remote.getCurrentWindow();
```

所以插件里直接:

```ts
const { remote } = require('electron');  // 这是 @electron/remote v2.1.2
```

这就是方案成立的基础。

### 1.3.2 Obsidian 自己怎么用——清缓存

`app.js` 里找到了现成的用法:

```js
// Obsidian 自己的清缓存功能
electron.remote.session.fromPartition(
    this.app.getWebviewPartition()
).clearStorageData({ storages: ['cookies'] })
```

路径完全一样:`remote.session.fromPartition(getWebviewPartition())`。

---

## 1.4 Cookie 注入方案:两条路径

### 1.4.1 ✅ 推荐:Electron `cookies.set()` API

```ts
import { App } from 'obsidian';

function getWebviewPartition(app: App): string {
    // 实测 Obsidian 1.8.10 可直接用 app.appId
    return `persist:vault-${(app as any).appId}`;
}

async function injectCookie(app: App, cookie: {
    name: string; value: string; domain: string; path: string;
    secure: boolean; httpOnly: boolean; expires_utc: number;
}) {
    const { remote } = require('electron');
    const session = remote.session.fromPartition(getWebviewPartition(app));

    await session.cookies.set({
        url: `https://${cookie.domain.replace(/^\./, 'www.')}/`,
        name: cookie.name,
        value: cookie.value,
        domain: cookie.domain,
        path: cookie.path,
        secure: cookie.secure,
        httpOnly: cookie.httpOnly,
        expirationDate: (cookie.expires_utc / 1000000) - 11644473600, // Chrome epoch → Unix epoch
        sameSite: 'lax',
    });
}
```

关键细节:

1. **`expirationDate` 必须带**。不加的话 Electron 有 bug(#20688)会变成 session cookie,重启 Obsidian 就丢。Chrome SQLite 里的 `expires_utc` 是 Chromium epoch(microseconds since 1601-01-01),要转成 Unix timestamp。
2. **`url` 参数可以随便给**,不要求精确匹配——Electron 用它做 origin 校验,但同一 site 内都能写。注意 `url` 先于 `domain` 被校验,给一个和 domain 匹配的 https URL 就行。
3. **`httpOnly` 能设**。`document.cookie` 做不到这一点,但 Electron API 没问题。这是这个方案相对于纯前端注入的绝对优势。
4. **`sameSite` 要带上**。Chrome SQLite 里有这个字段(值 -1/0/1/2 对应 unspecified/none/lax/strict),需要映射。默认不传可能变 session cookie。

### 1.4.2 ❌ 不推荐:直写 SQLite

**为什么能做但不该做**:
- Partition 下的 `Cookies` 是**明文**,[实测] 无加密,无 keychain 项,可以直接 INSERT
- 但 Chromium 运行时 cookie 缓存在内存里,你写文件它不知道
- 要生效得关掉 Obsidian 再开(做不到插件内一键)
- 不小心写漏字段可能导致整个 cookie 库被 Chromium 判定为损坏,重建后原来登录的站全没了

---

## 1.5 当前市场现状:社区插件和办法

| 插件/方案 | 做什么 | 和"搬 cookie"的关系 |
|---|---|---|
| **Web Viewer**(核心插件,1.8.3+) | 内嵌 webview 打开链接,partition 持久化 | 没有登录态导入,只靠手动登一次自然保存 |
| **Custom Frames** | 内嵌任意网页到侧边栏/面板 | issue #136 正在讨论改为用 webview 的 partition 共享 session(而不是搬外部 cookie) |
| **Obsidian-Surfing** | 全功能浏览器,劫持 file/http/https 协议 | Cloudflare 能过(比 web viewer 强),但同样是手动登录 |
| **Extended Browser** | 自动填表单登录 | 帮你重新登一次,不是搬 cookie |
| **CookieCloud + social-favorites-to-obsidian** | 从浏览器搬内容进 vault | 搬的是**笔记内容**,不是登录态;且手动部署 CookieCloud 很重 |
| **Surfing Cloudflare issue** | 讨论为什么 web viewer 过不了 CF | 有人建议用插件注入 cookie,但没人实现 |

**结论:市场上没有「把浏览器登录态直接注入 Obsidian webview」的现成方案。**

---

## 1.6 如果要做:插件设计方案

MVP 建议按这个优先级:

### 第一阶段(最小可用)

1. **设置面板**
   - 域名白名单(如 `.zhuanspirit.com` `.zhihu.com`),支持通配符
   - 选择源浏览器:Chrome / Edge / Brave / Arc
   - 一个「Sync now」按钮

2. **核心逻辑**
   ```
   用户点「Sync now」
   → cp Chrome Cookies.db 到临时文件(绕过锁)
   → 读 Keychain → PBKDF2 → AES-128-CBC 解密
   → 去掉 32 bytes host hash 前缀
   → 按白名单过滤
   → 映射字段(name/value/domain/path/secure/httpOnly/sameSite/expires_utc → expirationDate)
   → session.cookies.set() 写入 partition
   → 清理临时文件
   ```

3. **UA 对齐**(可选但影响成功率)
   读取所选浏览器的 UA → 对 webview session 设同样的 UA:
   ```ts
   session.setUserAgent(chromeUA);
   ```

### 第二阶段(体验优化)

- 支持通配符域名白名单(`*.zhuanspirit.com`)
- 支持多个源浏览器同时配
- 显示上次同步时间和 cookie 数量
- 一键清除已同步的 cookie

### 明确不做
- **不做全量导入**(安全风险:等于把浏览器全部登录态明文复制进 Obsidian)
- **不做自动后台同步**(同上 + 没必要,持久 cookie 只需写一次)
- **不尝试 Google 账号**(已知无效,不浪费用户时间)
- **不写 SQLite**(只用 Electron API)

### 需要验证的点(优先级)
1. **重启后 cookie 还在不在**(最关键,虽然 electron#15365 2018 年提过丢失,但我查你的 partition 库有 107 条持久 cookie,很可能已修复)
2. Keychain 弹窗的交互体验(首次授权一次 vs 每次都要)
3. macOS versions ≥13 的 Keychain 访问权限变化

---

## 1.7 相关发现:Obsidian webview 的安全特性

`main.js` 的 custom session 配置:

```js
// 权限控制
session.setPermissionCheckHandler((origin, permission) => allowedPermissions.includes(permission));
session.setDevicePermissionHandler(() => false);
```

- **设备权限全禁**:摄像头、麦克风、屏幕录制都不可用
- **地理定位被禁**
- **通知被禁**
- **画中画和全屏可用**(这是 web viewer 能全屏的基础)
- **adblock 默认开启**

---

## 1.8 环境信息(我的实测)

- Obsidian Desktop 1.8.10 (macOS)
- `@electron/remote` v2.1.2
- Web viewer partition:`persist:vault-3e07e723679e4e4e`
- Partition cookie 库:107 条,value 列明文,encrypted_value 列全空
- Chrome cookie 库:469 条,全部 v10(AES-128-CBC + Keychain),无 v20
