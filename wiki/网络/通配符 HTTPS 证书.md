# 1. 通配符 HTTPS 证书

> 泛域名系列(3/7)。上一篇:[[DNS 泛解析与查询链路]]。下一篇:[[nginx 泛域名转发]]。
>
> 泛解析让 `*.test.zhuanspirit.com` 能解析到机器,HTTP 就通了。但要上 HTTPS,浏览器会校验证书里的名字和你访问的域名对不对得上。这一篇讲:通配符证书怎么覆盖一整层子域、为什么只能覆盖一级、多级怎么办,以及现在主流的自动签发方式(ACME / DNS-01)。

---

## 1.1 先搞清证书在验什么

HTTPS 握手时,服务器把自己的证书发给浏览器。浏览器要确认两件事:

1. **信任链**:这张证书是不是由受信任的 CA(证书颁发机构)签发的,一层层能回溯到系统内置的根 CA。
2. **域名匹配**:证书里声明的域名,和你地址栏访问的域名**一致**吗?

第 2 点就是通配符证书要解决的核心。域名匹配看的不是老式的 `CN`(Common Name)字段——现代浏览器**只认 SAN**。

---

## 1.2 关键字段:SAN(Subject Alternative Name)

一张证书里真正列出「我对哪些域名有效」的地方是 **SAN 扩展**,它是一个域名列表:

```
Subject Alternative Name:
    DNS:zhuanspirit.com
    DNS:*.zhuanspirit.com
    DNS:api.other.com
```

- 曾经域名放在 `CN` 里,但从 2017 年起主流浏览器(Chrome 58+)**彻底忽略 CN,只校验 SAN**。签证书时 SAN 必须包含目标域名,否则报 `NET::ERR_CERT_COMMON_NAME_INVALID`。
- SAN 可以放多个域名 → 一张证书覆盖多个站点,这就是 **SAN 证书 / 多域名证书(UCC)**。
- SAN 里的某一项可以是通配符 `*.zhuanspirit.com` → 这就是**通配符证书**。

所以「通配符证书」和「多域名证书」不是对立的:一张证书的 SAN 里既能放通配符,也能放多个精确域名,还能放多个不同通配符(`*.a.com` + `*.b.com`)。

---

## 1.3 通配符只覆盖「一级」——为什么

这是本篇最容易踩的点,和前两篇的 DNS `*` 规则同源。

`*.zhuanspirit.com` 这张证书:

| 访问的域名 | 是否被覆盖 | 原因 |
| --- | --- | --- |
| `oa.zhuanspirit.com` | ✅ | `*` 匹配一层 |
| `api.zhuanspirit.com` | ✅ | 同上 |
| `zhuanspirit.com`(裸域) | ❌ | `*` 不匹配父域自身 |
| `a.b.zhuanspirit.com` | ❌ | 这是两层,`*` 只匹配一层 |
| `oa.test.zhuanspirit.com` | ❌ | 同样是两层 |

**两条规则(和证书规范 RFC 6125 一致):**

1. **`*` 只匹配一个标签(一层)**,不跨 `.`。这和 DNS 泛解析、URL 通配的规则是统一的,底层都是「通配符不吃点」。
2. **`*` 不匹配空**,即不覆盖裸域 `zhuanspirit.com`。所以想同时保护裸域和子域,SAN 里要**两条都写**:`zhuanspirit.com` + `*.zhuanspirit.com`(这也是签证书时的常见默认组合)。

### 1.3.1 多级子域怎么办

回到本系列的 `*.test.zhuanspirit.com` 场景——`test.zhuanspirit.com` 下面还有一层(`oa-xxx`)。这时:

- `*.zhuanspirit.com` 的证书**盖不住** `oa-xxx.test.zhuanspirit.com`(两级)。
- 需要**针对那一层单独签**一张 `*.test.zhuanspirit.com` 的通配符证书。
- 如果层级更深、且不确定,可以在 SAN 里叠多条通配符:`*.zhuanspirit.com` + `*.test.zhuanspirit.com` + `*.dev.zhuanspirit.com` …… 每多一层就多一条。

**没有「多级通配符」这种东西**。`*.*.zhuanspirit.com` 是非法的,CA 不会签,浏览器也不认。要覆盖 N 层,就得为每一层各准备一条通配符 SAN。

---

## 1.4 通配符 vs 多个单域名证书:怎么选

| 维度 | 通配符证书 `*.x.com` | 一堆单域名证书 |
| --- | --- | --- |
| 新增子域 | 无需重签,自动覆盖 | 每个都要重新签发部署 |
| 适合场景 | 子域数量多/动态(多租户、泛域名测试环境) | 子域少且固定 |
| 私钥风险 | 一把私钥泄露,整层子域都受影响 | 影响面隔离在单个域名 |
| 成本(商业 CA) | 一张搞定,通常比买 N 张便宜 | 数量多时贵 |
| 层级限制 | 只覆盖一层 | 每张精确,无层级问题 |

泛域名场景**几乎必然选通配符**——因为子域名是动态生成的(`oa-{任意人}`),事先根本不知道有哪些,单域名证书无从签起。

---

## 1.5 怎么签:从手动到 ACME 自动化

### 1.5.1 域名验证(DV)的三种 challenge

CA 签证书前要确认「你确实控制这个域名」。ACME 协议(Let's Encrypt 等免费 CA 用的)有三种验证方式:

- **HTTP-01**:在 `http://域名/.well-known/acme-challenge/xxx` 放一个指定文件,CA 来抓。**不能用于通配符**——因为通配符要证明的是「你控制整个 `*.x.com`」,而不是某一台具体主机。
- **DNS-01**:在 DNS 里加一条指定的 `TXT` 记录,CA 查这条 TXT 来验证。**通配符证书只能用 DNS-01**,因为只有能改 DNS 的人才算「控制整个域」。
- **TLS-ALPN-01**:握手阶段验证,少用。

### 1.5.2 通配符 = 必须 DNS-01

这是一条硬绑定:**想签 `*.zhuanspirit.com`,必须用 DNS-01**,在权威 DNS 加一条:

```
_acme-challenge.zhuanspirit.com.   TXT   "CA给的一串随机值"
```

CA 查到这条 TXT 匹配,就确认你控制该域,签发通配符证书。

痛点:Let's Encrypt 证书有效期短(90 天),通配符又只能 DNS-01,所以**自动续期必须能自动改 DNS**。实践上要么 DNS 服务商提供 API(certbot 用对应插件自动写 TXT),要么把 `_acme-challenge` 用 CNAME 委派到一个能自动化的地方。

### 1.5.3 常用工具

```bash
# certbot + DNS 插件(以 cloudflare 为例)自动签通配符
certbot certonly \
  --dns-cloudflare \
  --dns-cloudflare-credentials ~/.secrets/cf.ini \
  -d 'zhuanspirit.com' -d '*.zhuanspirit.com'
```

- `certbot`:Let's Encrypt 官方客户端,配 DNS 插件实现全自动。
- `acme.sh`:纯 shell,支持极多 DNS 服务商,轻量。
- 企业内网常有自建 CA 或统一证书平台,泛域名证书通常由运维/平台统一签好挂到网关,业务方一般不用自己管。

---

## 1.6 部署到 nginx(承接下一篇)

签好的证书(`fullchain.pem` + `privkey.pem`)挂到 nginx,配合泛域名 `server_name`:

```nginx
server {
    listen 443 ssl;
    server_name *.test.zhuanspirit.com;          # 泛域名

    ssl_certificate     /etc/ssl/wildcard.test.fullchain.pem;   # *.test.zhuanspirit.com 的通配符证书
    ssl_certificate_key /etc/ssl/wildcard.test.privkey.pem;
    # ... 转发规则见下一篇
}
```

注意证书的通配层级要和 `server_name` 对得上:`server_name *.test.zhuanspirit.com` 就得配 `*.test.zhuanspirit.com` 的证书,不能拿 `*.zhuanspirit.com` 的来顶(盖不住那一级)。nginx 按子域名区分并转发到不同后端的具体做法,见 [[nginx 泛域名转发]]。

---

## 1.7 速查

- 浏览器只认 **SAN**,不认 CN(2017 起)。
- `*` **只匹配一层**,**不匹配裸域**;要同时保护裸域和子域,SAN 里两条都写。
- **没有多级通配符**(`*.*` 非法);覆盖多层要为每层各配一条通配符 SAN。
- **通配符证书只能走 DNS-01 验证**;自动续期需要能自动改 DNS(TXT)。
- 动态子域场景(泛域名)几乎必选通配符,代价是一把私钥保护一整层、泄露影响面大。
