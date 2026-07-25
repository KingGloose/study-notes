# 1. 同源策略与 CORS

> 泛域名系列(6/7)。上一篇:[[../前端/前端运行时动态 base 完全指南]]。下一篇:[[Cookie 跨子域与跨窗口通信]]。
>
> 泛域名让你有一堆子域(`a.zhuanspirit.com`、`api.zhuanspirit.com`……)。这些子域之间、以及和外部域名之间,浏览器怎么判定「同不同源」、什么能跨、什么不能跨,就是同源策略和 CORS 的地盘。这一篇讲清楚:同源到底比什么、它限制什么放行什么、以及 CORS 怎么在受控前提下打开跨域。

---

## 1.1 同源策略:比的是「协议 + 域名 + 端口」

**同源(same-origin)= 协议、主机名、端口三者完全相同。** 少一个都不算同源。

以 `https://oa.zhuanspirit.com` 为基准:

| URL | 是否同源 | 差在哪 |
| --- | --- | --- |
| `https://oa.zhuanspirit.com/a` | ✅ | 只是路径不同,路径不参与判断 |
| `http://oa.zhuanspirit.com` | ❌ | 协议不同(http vs https) |
| `https://api.zhuanspirit.com` | ❌ | 主机名不同(子域不同也算跨源) |
| `https://oa.zhuanspirit.com:8443` | ❌ | 端口不同 |
| `https://zhuanspirit.com` | ❌ | 主机名不同(裸域 vs 子域) |

**关键认知(泛域名场景最容易误会的一点)**:同一个注册域下的不同子域,`oa.` 和 `api.`,在同源策略眼里是**跨源**的。泛域名给你一堆子域,但它们互相之间默认受同源策略限制——这就是为什么多子域架构几乎一定要面对 CORS(接口跨子域)和 Cookie 作用域(下一篇)问题。

---

## 1.2 同源策略限制什么、放行什么

同源策略不是「跨源啥都不让」,它是有选择地限制**读取**,而对某些操作放行。分清这点很重要。

### 1.2.1 受限(跨源被拦)

- **`fetch` / `XMLHttpRequest` 读响应**:请求可能发得出去,但**读不到响应**(除非 CORS 放行)。这是 CORS 要解决的主战场。
- **读跨源 iframe 的 DOM / 内容**:`iframe.contentWindow.document` 跨源直接抛错。
- **读跨源窗口的大部分属性**:只能用受限的 `postMessage`(下一篇)。
- **Canvas 画了跨源图片后 `toDataURL()`**:会「污染」画布,读像素被拒。
- **读跨源的 Cookie / localStorage / IndexedDB**:存储按源隔离。

### 1.2.2 放行(跨源允许)

- **`<img src>`、`<link>` css、`<script src>`、`<video>`**:可以跨源**加载**(但脚本能不能读到内容另说,比如跨源 script 报错细节被屏蔽)。这也是 CDN 能工作的原因。
- **`<form>` 跨源提交**:能提交(CSRF 的根源之一)。
- **跨源跳转、`<a>` 链接**:随便跳。

一句话概括:**能「用」跨源资源(加载、显示、提交),但默认不能「读」跨源的数据。** CORS 就是一套「在服务端明确授权下,让浏览器允许读跨源响应」的协议。

---

## 1.3 CORS:服务端授权的跨源读取

CORS(Cross-Origin Resource Sharing)的核心:**决定权在被请求的服务器**。浏览器发跨源请求时带上来源信息,服务器用响应头声明「我允许谁读」,浏览器据此放行或拦截。

注意分工:**CORS 是浏览器强制执行的**。服务器只是给指示,真正「拦截」发生在浏览器里(所以 Postman / curl 没有 CORS 问题——它们不是浏览器,不执行这套)。

### 1.3.1 简单请求:直接发,看响应头

满足全部条件的算「简单请求」,浏览器直接发,不预检:

- 方法是 `GET` / `POST` / `HEAD`;
- 只用安全头(`Accept`、`Content-Type` 等),且 `Content-Type` 仅限 `text/plain`、`multipart/form-data`、`application/x-www-form-urlencoded`。

请求自动带 `Origin` 头,服务器在响应里回:

```
Access-Control-Allow-Origin: https://oa.zhuanspirit.com
```

浏览器检查这个头包不包含当前源,不匹配就拦掉响应(请求其实已经到服务器了,副作用可能已发生——所以「简单请求」不适合有副作用的写操作)。

### 1.3.2 预检请求(preflight):先 OPTIONS 问一遍

不满足简单请求条件的(如 `PUT`/`DELETE`、`Content-Type: application/json`、带自定义头),浏览器**先发一个 `OPTIONS` 预检**,问服务器「我接下来想这么请求,行不行」:

```
# 浏览器自动发的预检
OPTIONS /api/data
Origin: https://oa.zhuanspirit.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type, authorization
```

服务器答复允许的范围:

```
Access-Control-Allow-Origin: https://oa.zhuanspirit.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 600          # 预检结果缓存 600s,期间同类请求不再预检
```

预检通过后,才发真正的请求。`Access-Control-Max-Age` 能缓存预检结果,减少「每个请求前都 OPTIONS 一遍」的开销。

### 1.3.3 带凭证(Cookie)的跨源请求:最容易踩

默认情况下,跨源 `fetch` **不带 Cookie**。要带上必须两边配合:

```js
// 前端:显式声明要带凭证
fetch('https://api.zhuanspirit.com/me', { credentials: 'include' })
```

```
# 服务端:必须同时满足
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://oa.zhuanspirit.com   # 不能是 *
```

两条硬规则(高频踩坑):

1. **带凭证时 `Access-Control-Allow-Origin` 不能是 `*`**,必须是**具体的源**。所以服务端通常要维护一个「允许来源白名单」,按请求的 `Origin` 动态回显匹配到的那一个。
2. **`Access-Control-Allow-Credentials: true` 必须显式设**,否则即使前端 `credentials: 'include'`,浏览器也会拦掉响应。

泛域名场景很常见这种需求:主站 `oa.zhuanspirit.com` 调 `api.zhuanspirit.com` 且要带登录 Cookie → 必须走「白名单回显 Origin + Allow-Credentials」这套,不能图省事用 `*`。

---

## 1.4 CORS 响应头速查

| 响应头 | 作用 |
| --- | --- |
| `Access-Control-Allow-Origin` | 允许的源;带凭证时必须是具体源不能是 `*` |
| `Access-Control-Allow-Methods` | 预检:允许的方法 |
| `Access-Control-Allow-Headers` | 预检:允许的自定义请求头 |
| `Access-Control-Allow-Credentials` | 是否允许带 Cookie 等凭证 |
| `Access-Control-Max-Age` | 预检结果缓存秒数 |
| `Access-Control-Expose-Headers` | 允许前端 JS 读取的响应头(默认只能读少数几个) |
| `Vary: Origin` | 白名单回显 Origin 时**务必加**,否则 CDN/缓存会把某个源的 CORS 响应错发给别的源 |

> `Vary: Origin` 是个隐蔽但重要的点:当你按请求的 Origin 动态回显 `Allow-Origin` 时,响应内容就随 Origin 变化了。不加 `Vary: Origin`,中间缓存可能把「允许 A 源」的响应缓存下来发给 B 源,导致时灵时不灵的诡异 CORS 报错。

---

## 1.5 和泛域名/系列的关系

- 泛域名带来大量子域,**子域之间默认跨源**,接口调用普遍需要 CORS。
- 需要跨子域带登录态时,CORS 的「带凭证」规则和下一篇的 Cookie `domain` 作用域是**配套**的:CORS 决定「跨源请求能不能带 Cookie 并读响应」,Cookie `domain` 决定「这个 Cookie 会不会被带到那个子域」。两者都对了,跨子域登录态才通。
- 跨窗口/iframe 通信绕不开同源限制,只能用 `postMessage`——见 [[Cookie 跨子域与跨窗口通信]]。

---

## 1.6 速查

- **同源 = 协议 + 主机 + 端口全同**;子域不同 = 跨源。
- 同源策略**限制「读」跨源数据,放行「用」跨源资源**(加载/显示/提交)。
- CORS 由**浏览器执行、服务器授权**;非浏览器工具没有 CORS 问题。
- 非简单请求先 **OPTIONS 预检**;`Max-Age` 缓存预检结果。
- 带凭证:前端 `credentials:'include'` + 服务端 `Allow-Credentials:true` + `Allow-Origin` 为**具体源**(不能 `*`),并加 `Vary: Origin`。
