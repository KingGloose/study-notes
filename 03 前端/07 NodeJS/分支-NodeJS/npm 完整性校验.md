# 1、基本介绍

- 当你执行 `npm i` 时，npm 会先从 registry 拉取包的 _元数据_（metadata），里面包含两类与完整性相关的信息：
    - `dist.shasum` —— 这是 **SHA-1 的 hex 摘要**（历史兼容字段）。
    - `dist.integrity` —— 这是 **SRI 格式**（subresource integrity，通常包含 `sha512-<base64>`，也可能包含其它算法）；新版本 npm/registry 优先使用此字段。
- npm 在下载 tarball（.tgz）时会对流/文件实时计算摘要（通常是 sha512，同时历史上也会计算 sha1），下载完后把计算出的摘要与 registry 给出的期望值做比较。若不匹配就抛出 `EINTEGRITY` 并停止安装/索引缓存。
- 实际实现里 npm 使用的关键库是 `ssri`（处理 SRI 格式）和 `cacache`（本地缓存），下载时以流方式用 `ssri` 或 `crypto` 计算摘要并验证。
下面把各部分拆开详细讲：流程 → 摘要如何产生 → 如何校验 → 如何手动验证 / 排查。

# 一、npm 下载与完整性校验的完整流程（逐步）

1. **获取 package metadata**  
    客户端向 registry 请求 package 的 metadata（例如 `GET /package-name` 或 `GET /package-name/-/package-name-1.2.3.tgz` 之前会拿到 metadata）。metadata 中常见字段：
    
    - `dist.shasum`（hex sha1）
        
    - `dist.tarball`（tarball 的 URL）
        
    - `dist.integrity`（SRI 字符串，常见为 `sha512-<base64>`）
        
2. **决定期望值**
    
    - 如果 metadata 含有 `dist.integrity`（SRI），npm 优先使用 SRI（通常含 sha512）。
        
    - 否则回退使用 `dist.shasum`（hex sha1）。一些客户端会同时保留两个做兼容检查（先比 sha512，再对照 shasum）。
        
3. **请求 tarball（实际下载）**  
    npm 发起 HTTP GET 去拿 tarball。下载过程通常是流（stream）式的，数据一边写入 cacache（磁盘缓存）一边被传给 `ssri`/`crypto` 来计算摘要。
    
4. **流式计算摘要**
    
    - 当使用 `ssri` 时，可用 `ssri.integrityStream()` 或 `ssri.checkStream()` 对 incoming stream 进行计算/校验。`ssri` 会为支持的算法（如 sha512）计算 base64 摘要并格式化成 SRI（`sha512-...`）。
        
    - 同时历史代码/兼容逻辑会用 `crypto.createHash('sha1')` 计算 hex shasum（并与 `dist.shasum` 对比）。
        
5. **比对**
    
    - 若期望为 `dist.integrity`（SRI），用 `ssri.checkStream()` 或 `ssri.checkData()` 把下载得到的 digest 与 `dist.integrity` 做对比（SRI 支持多算法/多值）。
        
    - 若期望为 `dist.shasum`，把实际计算出来的 sha1 hex 与 `dist.shasum` 字符串做简单等号比较。
        
    - 若任一比较失败，npm 抛出 `EINTEGRITY`（并常会删除该缓存条目），并停止安装这个包。
        
6. **成功后写入 cache / 继续安装**
    
    - 校验通过后，写入 `cacache`，然后解压并把 package 放到 `node_modules`（或后续安装步骤）。
        

---

# 二、`sha1` 与 `sha512` 是如何“得来”的（发布端 & 客户端）

## 发布端（`npm publish` 时）

- 当包被发布到 npm registry 时，发布流程会：
    
    1. 把 package 打成 tarball（例如 `package-name-1.2.3.tgz`）。
        
    2. 对这个 tarball 计算摘要：`sha1`（hex）会写入 `dist.shasum`，并生成 SRI 字段（通常是 `sha512-<base64>`）写入 `dist.integrity`。这些字段被写入 registry 的 metadata（`/package` 的 JSON）。
        
    3. registry 保存 tarball并把 metadata 对外提供。
        

生成计算方式（伪步骤）：

- `shasum = sha1(tarball) --> hex string` → 存 `dist.shasum`
    
- `sri = "sha512-" + base64(sha512_binary(tarball))` → 存 `dist.integrity`
    

> 注意：`dist.shasum` 保留为 hex（人们习惯的 hex 表示），而 SRI（ssri）用 base64 表示 digest bytes 并带上算法前缀。

## 客户端（你的 npm）

- npm 在下载 tarball 时 **重新计算**这些摘要（而不是直接信任 registry 的文件）。计算方式与发布端相同的算法：
    
    - 使用 SHA-512 得出原始二进制摘要，再用 Base64 编码得到 `sha512-<base64>`。
        
    - 使用 SHA-1 得到 hex 字符串用于与 `dist.shasum` 比较（如果需要）。
        

---

# 三、如何用命令 / 代码手动验证（实操）

下面给出几种实际方法 —— 用 `openssl`、Node、以及 `ssri`。

## 1) 用 `openssl`（shell）

假设你已经下载了 `package-name-1.2.3.tgz` 到当前目录：

- 计算 sha1 hex（与 `dist.shasum` 比较）：
    

```bash
# 输出示例： SHA1(filename)= <hex>
openssl dgst -sha1 package-name-1.2.3.tgz
# 或只要 hex：
openssl dgst -sha1 -hex package-name-1.2.3.tgz
```

- 计算 sha512 并输出 base64（用于构造 SRI `sha512-<base64>`）：
    

```bash
openssl dgst -sha512 -binary package-name-1.2.3.tgz | openssl base64 -A
# 然后把结果前面加上 "sha512-"
# e.g. sha512-<the-base64-string>
```

`-binary` 把 digest 以二进制形式输出，这样 `base64` 才是对 digest bytes 编码（SRI 的要求）。

## 2) 用 Node.js 原生 `crypto`

```js
const fs = require('fs');
const crypto = require('crypto');

const file = fs.readFileSync('package-name-1.2.3.tgz');

// sha1 hex
const shasum = crypto.createHash('sha1').update(file).digest('hex');
console.log('sha1 hex:', shasum);

// sha512 base64 (SRI)
const sha512base64 = crypto.createHash('sha512').update(file).digest('base64');
console.log('sha512 sri:', 'sha512-' + sha512base64);
```

## 3) 用 `ssri`（node 包，用来解析/生成 SRI 字符串）

你可以 `npm i -g ssri` 或用 `npx ssri`。示例（Node）：

```js
const fs = require('fs');
const ssri = require('ssri');

const data = fs.readFileSync('package-name-1.2.3.tgz');

// 生成 SRI（默认会优先用 sha512）
const integrity = ssri.fromData(data, { algorithms: ['sha512', 'sha1'] });
console.log('integrity:', integrity.toString()); // e.g. "sha512-... sha1-..."

// 检查（预期值 exampleIntegrity 来自 registry.dist.integrity）
const ok = ssri.checkData(data, 'sha512-<base64-from-registry>');
console.log('checkData OK?', !!ok);
```

`ssri.fromData` 会返回一个 `Integrity` 对象，可以输出多算法的 SRI 表示（例如同时包含 sha512 和 sha1 的表示）。

---

# 四、SRI 格式与 `dist.shasum` 的差异（关键易混点）

- `dist.shasum`（registry metadata）：**hex 表示的 SHA-1**（例如 `a94a8fe5ccb19ba61c4c0873d391e987982fbbd3`）。这是历史遗留的字段，很多工具仍用它兼容性检查。
    
- `dist.integrity`（registry metadata）：**SRI 字符串**，例如 `sha512-<base64>`（也可以同时包含多个算法，用空格分隔）。SRI 使用 base64 来表示 digest bytes，并带算法前缀（`sha512-...`、`sha1-...` 等）。
    
- 当客户端使用 SRI (`sha512-...`) 时不要用 hex 去对比 —— 必须用二进制 digest -> base64 的流程或用 `ssri` 库做转换/比较。换句话说：hex(sha1) ≠ base64(sha1_bytes)；如果需要把 hex 转成 base64，需要把 hex 解析成 bytes 再 base64 编码。
    

---

# 五、`EINTEGRITY` 常见原因与排查步骤

## 常见原因

1. **网络中间件/代理篡改**：公司代理、缓存服务器或 CDN 在传输过程中出了问题（或错误的缓存）。
    
2. **registry metadata 与 tarball 不一致**：包被重发布但 metadata 没更新（罕见，但可能）。
    
3. **缓存损坏**：本地 `cacache` 内容损坏或磁盘错误。
    
4. **镜像源不同步**（例如使用了私有镜像或第三方镜像与 npm 官方 registry 不一致）。
    
5. **下载被截断或传输错误**（不完整文件会导致摘要不同）。
    
6. **npm 版本 bug**（极少见，但存在历史案例）。
    

## 排查步骤（从快到慢）

1. **查看完整的错误日志**：`npm i --verbose`，查看是哪个包、期望值是什么、实际计算值是什么（npm 的 verbose 会打印比对信息）。
    
2. **清理本地缓存重试**：
    
    ```bash
    npm cache clean --force
    npm i
    ```
    
3. **直接用 curl / wget 下载 tarball 再手动比对**：
    
    - 先从 metadata 拿 `dist.tarball`、`dist.integrity`、`dist.shasum`（用 `npm view <pkg>@<ver> dist` 或 `npm pack <pkg>@<ver>` 获取）。
        
    - `curl -L <tarball-url> -o pkg.tgz`，然后用上面的 `openssl` 或 Node 方式计算，和 metadata 的值比较。
        
4. **切换 registry（检查镜像同步问题）**：暂时切回官方 `https://registry.npmjs.org/` 或换用其他源试试（可通过 `npm set registry`）。
    
5. **检查代理/公司网络**：绕过公司代理/代理服务器测试，或在不同网络（如手机热点）重试。
    
6. **确认 npm 版本**：`npm -v`，如果版本较旧或已知 bug，尝试升级 npm（`npm i -g npm` 或使用 node 的包管理器）。
    
7. **查看是否是某个具体包有问题**：尝试安装这个包单独 `npm i <pkg>@<ver>`，或用 `npm pack` 下载并验证。
    
8. **如果怀疑 registry 问题**：在 npm registry 的网页或包管理页面查看发布时间及元数据，或联系包维护者 / registry。
    

---

# 六、实战示例：完整一步步排查（命令合集）

1. 打印 metadata：
    

```bash
npm view left-pad@1.3.0 dist
# 输出示例：
# { tarball: 'https://registry.npmjs.org/left-pad/-/left-pad-1.3.0.tgz',
#   shasum: 'b5a0b...hex...',
#   integrity: 'sha512-Base64...' }
```

2. 下载 tarball：
    

```bash
curl -L 'https://registry.npmjs.org/left-pad/-/left-pad-1.3.0.tgz' -o left-pad-1.3.0.tgz
```

3. 本地验证：
    

```bash
# sha1 hex
openssl dgst -sha1 left-pad-1.3.0.tgz

# sha512 base64 -> 构成 SRI
openssl dgst -sha512 -binary left-pad-1.3.0.tgz | openssl base64 -A
# 得到 base64 后在前面加 "sha512-"
```

4. 或用 Node + ssri：
    

```js
// verify.js
const fs = require('fs');
const ssri = require('ssri');
const data = fs.readFileSync('left-pad-1.3.0.tgz');

const generated = ssri.fromData(data, { algorithms: ['sha512', 'sha1'] });
console.log('generated SRI:', generated.toString());

const expected = 'sha512-...'; // 从 npm view 拿到
console.log('checkData:', !!ssri.checkData(data, expected));

// 也打印 sha1 hex
const crypto = require('crypto');
console.log('sha1 hex:', crypto.createHash('sha1').update(data).digest('hex'));
```

运行 `node verify.js` 对比输出结果。

---

# 七、关于为什么同时存在 sha1 和 sha512（以及优先级）

- **历史原因**：早期 npm 只用 `shasum`（sha1 hex），随时间进化引入 SRI（sha512）来增强安全性（sha1 已不被认为足够强）。但为了兼容性仍保留 `shasum` 字段。
    
- **客户端行为**：现代 npm 优先使用 `dist.integrity`（sha512 SRI）。`shasum` 仍然用于兼容或作为额外的检查。某些老工具或镜像只提供 `shasum`。
    

---

# 八、小结（你需要知道的关键命令 / API）

- registry metadata：`npm view <pkg>@<ver> dist`
    
- 清缓存：`npm cache clean --force`
    
- 下载 tarball：`curl -L <tarball-url> -o pkg.tgz`
    
- 快速验证：`openssl dgst -sha1 pkg.tgz`（hex）与 `openssl dgst -sha512 -binary pkg.tgz | openssl base64 -A`（得到 SRI 的 base64）
    
- Node 验证（示例）用 `crypto` 或 `ssri`（推荐 `ssri` 去处理 SRI 的解析/比对）
    
- 常见修复：清 cache / 切 registry / 检查代理 / 直接手动比对 tarball 与 metadata
    

---

如果你愿意，我可以：

- 根据你当前出现 `EINTEGRITY` 的日志（把报错片段贴过来），我可以直接帮你解析“期望值/实际值/在哪一步失败”的具体原因；或者
    
- 把上面的 Node `verify.js` 做成一个更完整的脚本，自动从 `npm view` 取 `dist` 字段、下载 tarball、并输出比对结果 —— 你想要哪一种？（如果要脚本，把包名和版本直接给我，我就直接写好脚本）