# 1. Cookie 跨子域与跨窗口通信

> 泛域名系列(7/7,完结)。上一篇:[[同源策略与 CORS]]。系列开篇:[[泛域名与相关概念辨析]]。
>
> 泛域名下有一堆子域,自然产生两个诉求:① 一次登录,所有子域都认(登录态跨子域共享);② 主页面和子域 iframe / 弹窗之间要通信。前者靠 Cookie 的 `domain` 作用域,后者靠 `postMessage`。这一篇收尾。

---

## 1.1 Cookie 的作用域:`domain` 决定它跟谁走

Cookie 能不能被带到某个请求,由它的 **`domain` + `path`** 属性决定。这套规则和同源策略**不一样**(Cookie 有自己的作用域模型,别用同源直觉套)。

### 1.1.1 不设 domain vs 设了 domain

```
# 服务器 Set-Cookie 时:
Set-Cookie: token=abc                        # 不设 domain
Set-Cookie: token=abc; Domain=zhuanspirit.com  # 设了 domain
```

- **不设 `domain`(host-only)**:Cookie 只属于**当前那个确切主机**。`oa.zhuanspirit.com` 设的,只有访问 `oa.zhuanspirit.com` 才带,`api.zhuanspirit.com` **不带**。
- **设 `Domain=zhuanspirit.com`**:Cookie 对该域**及其所有子域**生效。`oa.`、`api.`、`shop.zhuanspirit.com` 全都会带上。**这就是跨子域共享登录态的核心开关。**

> 注意反直觉点:设 `Domain=zhuanspirit.com` 会**自动包含所有子域**,不需要写成 `.zhuanspirit.com`(老规范里的前导点现在会被忽略,效果一样,覆盖子域)。而**不设** domain 反而是最严格的「仅当前主机」。

### 1.1.2 跨子域共享登录态的标准做法

想让 `oa.` 登录后 `api.`、`shop.` 都认:

```
Set-Cookie: token=abc; Domain=zhuanspirit.com; Path=/; Secure; HttpOnly; SameSite=Lax
```

这样任何 `*.zhuanspirit.com` 的请求都会带上 `token`,后端各子域服务都能校验同一份登录态。SSO(单点登录)最朴素的一种实现就是靠父域 Cookie。

### 1.1.3 关键约束

1. **只能往上设到「可注册域」,不能跨站设**。`oa.zhuanspirit.com` 可以设 `Domain=zhuanspirit.com`,但**不能**设 `Domain=zhuanspirit.com` 之外(比如别人的域),更不能设 `Domain=.com` 这种顶级域(浏览器的公共后缀列表 Public Suffix List 会禁止,否则就能跨所有 `.com` 站点污染 Cookie)。
2. **子域能给父域设,父域 Cookie 子域能读**(HttpOnly 下是「随请求带」而非 JS 读),但**平级子域之间不能直接给对方设**,只能都挂在父域下共享。

---

## 1.3 SameSite:跨站带不带 Cookie

`SameSite` 控制**跨站请求**要不要带这个 Cookie,是 CSRF 防护和第三方 Cookie 治理的关键。三个值:

| 值 | 行为 | 说明 |
| --- | --- | --- |
| `Strict` | 只有同站请求带 | 最严,跨站跳转过来也不带(点外链进来会「未登录」) |
| `Lax`(现代浏览器默认) | 同站带;跨站仅「顶级导航 GET」带 | 平衡点,大部分场景够用 |
| `None` | 跨站也带 | **必须同时 `Secure`(仅 HTTPS)**,否则被拒 |

**「同站(same-site)」≠「同源(same-origin)」**,这是最容易混的:

- 同源:协议+主机+端口全同(见上一篇)。
- 同站:只看**可注册域(eTLD+1)**是否相同。`oa.zhuanspirit.com` 和 `api.zhuanspirit.com` **是同站**(都属于 `zhuanspirit.com`),但**不同源**。

所以对泛域名的多子域:它们**同站不同源**。`SameSite=Lax` 下子域之间的请求算同站、会带 Cookie——这对跨子域登录态是好事。真正需要 `SameSite=None; Secure` 的是**跨站**嵌入(比如你的页面被别的公司域名 iframe 嵌入还要带你的 Cookie)。

### 1.3.1 组合建议

跨子域共享登录态的典型 Cookie:

```
Set-Cookie: token=abc; Domain=zhuanspirit.com; Path=/;
            Secure; HttpOnly; SameSite=Lax
```

- `Domain=zhuanspirit.com`:覆盖所有子域。
- `HttpOnly`:JS 读不到,防 XSS 窃取。
- `Secure`:只在 HTTPS 传。
- `SameSite=Lax`:同站子域间正常带,挡住大部分跨站 CSRF。

---

## 1.4 和 CORS 的配套关系(串上一篇)

跨子域「带着登录态调接口」要**两套机制同时满足**,缺一不可:

1. **Cookie 层**:`Domain=zhuanspirit.com` 让 Cookie 会被带到 `api.zhuanspirit.com`;`SameSite` 允许这种带法。
2. **CORS 层**(见 [[同源策略与 CORS]] §1.3.3):因为 `oa.` 调 `api.` 是**跨源** fetch,前端要 `credentials:'include'`,服务端要 `Allow-Credentials:true` + `Allow-Origin` 具体源。

一句话分工:**Cookie 的 `domain` 决定「浏览器会不会把 Cookie 装进这个跨子域请求」,CORS 决定「这个跨源请求能不能带凭证并读到响应」。** 两个层面各管一段,常见「Cookie 明明设了却没带过去 / 带过去了但响应被拦」就是漏了其中一层。

---

## 1.5 跨窗口通信:postMessage

同源策略禁止直接读跨源窗口/iframe 的内容(上一篇 §1.2.1)。要在**不同源**的窗口间通信,唯一受支持的安全通道是 `window.postMessage`。

### 1.5.1 基本用法

```js
// 发送方:向目标窗口发消息
// 第二个参数 targetOrigin:限定「只有目标是这个源才收得到」,防止发错对象
targetWindow.postMessage({ type: 'login', token: 'abc' }, 'https://oa.zhuanspirit.com')

// 接收方:监听 message
window.addEventListener('message', (event) => {
  // ① 必须校验来源!否则任何页面都能给你发消息
  if (event.origin !== 'https://oa.zhuanspirit.com') return
  // ② 再处理数据
  console.log(event.data)
})
```

### 1.5.2 两条安全铁律

`postMessage` 是跨源开的口子,**安全全靠双向校验**:

1. **发送方指定 `targetOrigin`**,别用 `'*'`(用 `*` 意味着任何劫持了目标窗口的页面都能收到你的敏感数据,如 token)。
2. **接收方校验 `event.origin`**(还可校验 `event.source`)。**不校验 origin = 任何网站都能给你的页面发指令**,是常见漏洞。校验时用**精确匹配**或严格的白名单,别用 `origin.includes('zhuanspirit.com')` 这种松散判断——`zhuanspirit.com.evil.com` 能绕过。

> 泛域名场景:主页面和嵌入的子域 iframe(可能不同源)交换登录态、尺寸、事件,都走 postMessage,且两端都要按上面两条校验对方的 origin。

---

## 1.6 系列收尾:一条完整链路回顾

从「输入一个泛域名」到「页面完整跑起来、还能跨子域共享登录」,整条链路:

1. **命名**:`*.zhuanspirit.com` 泛域名规划一堆子域([[泛域名与相关概念辨析]])。
2. **解析**:DNS 泛解析把任意子域指向入口机([[DNS 泛解析与查询链路]])。
3. **加密**:通配符证书让这一层子域都能上 HTTPS([[通配符 HTTPS 证书]])。
4. **分流**:nginx 按 `Host` 区分子域、透传来源、转发到对应后端/静态目录([[nginx 泛域名转发]])。
5. **资源**:前端运行时动态 base 让一份产物在任意子域下各取各的资源([[../前端/前端运行时动态 base 完全指南]])。
6. **跨域**:子域间接口调用靠 CORS 授权([[同源策略与 CORS]])。
7. **登录态 & 通信**:Cookie `Domain` 共享登录态、`postMessage` 跨窗口通信(本篇)。

---

## 1.7 速查

- Cookie **不设 domain = 仅当前主机**;**设 `Domain=父域` = 覆盖所有子域**(跨子域共享登录态的开关)。
- 不能跨站设 domain,顶级域被 Public Suffix List 禁止。
- **同站 ≠ 同源**:多子域是「同站不同源」;`SameSite=Lax` 下子域间带 Cookie,`None` 必须配 `Secure`。
- 跨子域带登录态调接口 = **Cookie domain(带得过去) + CORS 带凭证(读得到响应)** 两层都要对。
- `postMessage` 是跨源通信唯一安全通道:**发方指定 `targetOrigin`、收方精确校验 `event.origin`**,两条都不能省。
