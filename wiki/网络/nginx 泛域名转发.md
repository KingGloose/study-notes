# 1. nginx 泛域名转发

> 泛域名系列(4/7)。上一篇:[[通配符 HTTPS 证书]]。下一篇:[[../前端/前端运行时动态 base 完全指南]]。
>
> DNS 泛解析把 `*.test.zhuanspirit.com` 全指向同一台入口机,通配符证书让它能上 HTTPS。到了这台入口机之后,靠谁来区分「访问的到底是哪个子域、该转给哪个后端」?就是 nginx。这一篇讲 `server_name` 的泛域名匹配、如何从子域名里提取信息做路由、以及把子域名/真实来源透传给后端时最容易翻车的几个 header。

---

## 1.1 请求到 nginx 之前发生了什么

先接上前三篇,把链路补全:

```
浏览器 oa-zhangjiahui04.test.zhuanspirit.com
   │  ① DNS 泛解析:*.test.zhuanspirit.com → 入口机 IP(见系列 2)
   ▼
入口机 nginx :443
   │  ② TLS 握手,用 *.test.zhuanspirit.com 通配符证书(见系列 3)
   │  ③ 读请求头里的 Host: oa-zhangjiahui04.test.zhuanspirit.com
   │  ④ 按 server_name 匹配到对应 server 块,再按规则转发
   ▼
后端服务 / 静态资源目录 / 具体 docker
```

关键点:**DNS 只负责把不同子域都送到同一个 IP,真正「区分是谁」的是 nginx 读 HTTP 请求里的 `Host` 头**。所以泛解析 + nginx 的组合,才是「一个入口、按子域名分流」的完整方案。

---

## 1.2 server_name 的泛域名匹配

nginx 用 `server_name` 决定一个请求命中哪个 `server` 块。它支持三种通配形式:

```nginx
server_name  oa.zhuanspirit.com;        # 精确
server_name  *.test.zhuanspirit.com;    # 前缀通配(泛域名常用)
server_name  zhuanspirit.*;             # 后缀通配
server_name  ~^oa-(?<user>.+)\.test\.zhuanspirit\.com$;  # 正则(能抓变量!)
```

### 1.2.1 匹配优先级(记牢)

同一个请求可能匹配多个 server,nginx 按**固定优先级**选,不是按配置先后:

1. 精确名字(`oa.zhuanspirit.com`)
2. 最长的前缀通配(`*.test.zhuanspirit.com` 优先于 `*.zhuanspirit.com`)
3. 后缀通配(`zhuanspirit.*`)
4. 第一个匹配的正则(`~` 开头,按配置文件出现顺序)

和 DNS「精确优先于通配」的思路一致:**越具体越优先**。正则最灵活但排在最后,且多个正则按书写顺序取第一个命中的。

### 1.2.2 `*` 同样只匹配一层

nginx 的 `*.test.zhuanspirit.com` 也遵守「一层」规则,匹配 `oa-xxx.test.zhuanspirit.com`,但**不匹配** `a.b.test.zhuanspirit.com`。要匹配任意深度得用正则。这条规则从 DNS → 证书 → nginx 一路统一。

---

## 1.3 从子域名里提取信息:正则捕获

泛域名场景常常需要「知道访问者是谁 / 哪台机器」,而这个信息就藏在子域名前缀里(`oa-zhangjiahui04`)。用正则 `server_name` 可以把它捕获成变量:

```nginx
server {
    listen 443 ssl;
    # 捕获 oa- 后面那段作为 $user
    server_name ~^oa-(?<user>[^.]+)\.test\.zhuanspirit\.com$;

    ssl_certificate     /etc/ssl/wildcard.test.fullchain.pem;
    ssl_certificate_key /etc/ssl/wildcard.test.privkey.pem;

    location / {
        # 把捕获到的 user 用作路径 / 上游选择 / 传给后端
        proxy_pass http://backend;
        proxy_set_header X-Env-User $user;   # 例:告诉后端这是谁的环境
    }
}
```

`(?<user>...)` 是命名捕获,匹配到的值存进 `$user`,后面 `proxy_pass`、`root`、`proxy_set_header` 里都能用。这就是「按子域名路由」的核心手法——**子域名不只是名字,它携带了可解析的信息**。

也可以用 `map` 指令把子域名映射到不同上游:

```nginx
map $host $target_backend {
    default                             http://default_pool;
    ~^oa-(?<u>.+)\.test\.               http://test_pool;
    ~^oa\.zhuanspirit\.com$             http://prod_pool;
}
server {
    server_name ~\.zhuanspirit\.com$;
    location / { proxy_pass $target_backend; }
}
```

---

## 1.4 反向代理时,把「真实来源」透传给后端(高频坑区)

一旦 nginx 做反向代理(`proxy_pass`),后端收到的请求是 nginx 发来的,**默认会丢掉客户端的真实信息**。后端如果依赖 `Host`、真实 IP、协议来做逻辑(比如按域名区分租户、生成绝对 URL、判断是否 HTTPS),就会出错。要手动补这几个 header:

```nginx
location / {
    proxy_pass http://backend;

    proxy_set_header Host              $host;              # ① 原始域名,后端靠它区分子域/租户
    proxy_set_header X-Real-IP         $remote_addr;       # ② 客户端真实 IP
    proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;  # ③ 经过的代理链
    proxy_set_header X-Forwarded-Proto $scheme;            # ④ 原始协议 http/https
    proxy_set_header X-Forwarded-Host  $host;              # ⑤ 有些框架认这个
}
```

逐条说明为什么重要:

- **① `Host: $host`**:最关键。不设的话,后端拿到的 Host 可能是 `backend`(上游名)或被改写,导致「按域名区分租户/环境」的逻辑失效。泛域名场景**必须**透传原始 Host,后端才知道访问的是 `oa-zhangjiahui04...` 还是别的。
  - `$host` vs `$http_host` vs `$server_name` 的区别值得记:`$host` 优先取请求行/Host 头里的域名且转小写、更稳;`$http_host` 是原样 Host 头;`$server_name` 是配置里写的名字(用正则时不是实际访问的域名)。透传一般用 `$host`。
- **② `X-Real-IP` / ③ `X-Forwarded-For`**:后端看到的 `remote_addr` 是 nginx 的 IP。要拿客户端真实 IP(日志、风控、限流)必须靠这两个头。`X-Forwarded-For` 会累加整条代理链。
- **④ `X-Forwarded-Proto`**:nginx 终结了 HTTPS,到后端往往是 http。后端若要生成 `https://` 的绝对链接、或判断「是否安全连接」,得靠这个头,否则会生成错的 http 链接、或误判为不安全。

> 经验:反代后「域名不对 / 拿到的是内网 IP / 生成的链接变 http / 重定向到错域名」这一类问题,90% 是上面某个 header 没透传。排查先看后端实际收到的 header。

---

## 1.5 承接系列:两种「后端」形态

引出本系列的内部文档里提到,线下环境的资源分发有个特点:**公共资源不放在一台公共服务器,而是每台申请的机器 docker 里各 copy 一份**。这落到 nginx 上就是两种转发形态:

### 1.5.1 转发到动态资源服务(反向代理)

```nginx
location /api/ {
    proxy_pass http://backend_pool;
    proxy_set_header Host $host;      # 见 §1.4
    # ...
}
```

### 1.5.2 直接吐静态资源(前端产物)

```nginx
location / {
    # 按子域名捕获的 $user 定位到对应机器/目录里的前端产物
    root /data/deploy/$user/dist;
    try_files $uri $uri/ /index.html;   # SPA 兜底到 index.html
}
```

这里埋了一个关键伏笔:静态资源(`index.html` 里引用的 js/css/图片)**用什么前缀去加载**?如果构建时把资源路径写死成某个固定域名,那泛域名访问时资源就会指错地方。这正是重头那篇 [[../前端/前端运行时动态 base 完全指南]] 要解决的核心问题——**让前端资源的 base 在运行时动态确定,而不是编译期写死**。

---

## 1.6 速查

- **DNS 送到同一台机,nginx 靠 `Host` 头区分是哪个子域**,二者配合才是完整的泛域名分流。
- `server_name` 匹配优先级:精确 > 最长前缀通配 > 后缀通配 > 第一个正则;`*` 只匹配一层。
- 用**正则 `server_name` + 命名捕获**从子域名前缀里提取信息(谁/哪台机),再用于路由。
- 反向代理**必须透传** `Host`(区分租户/域名)、`X-Real-IP`/`X-Forwarded-For`(真实 IP)、`X-Forwarded-Proto`(原始协议);少一个都可能出诡异 bug。
- 静态资源直吐时,产物的加载前缀不能编译期写死 → 引出前端运行时动态 base。
