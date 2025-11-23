# 1. 概览 — 关键结论

- 当执行 `npm i` 时，npm 会对下载到的 tarball 计算哈希并与“期望哈希”比较。若不一致则报错 `EINTEGRITY` 并停止安装。
- **期望哈希从哪里来**：取决于是否存在 `package-lock.json`（或 `npm-shrinkwrap.json`）：
    - 有 lock 文件：优先使用 lock 中的 `integrity` 字段（SRI，通常 `sha512-...`）。
    - 无 lock 文件：使用 registry metadata（`dist.integrity` 或 `dist.shasum`）。
- registry metadata 中常见两个字段：
    - `dist.shasum` —— hex 表示的 SHA-1（历史遗留）
    - `dist.integrity` —— SRI 格式（如 `sha512-<base64>` 或同一字符串里含多个算法）
- `package-lock.json` 中的 `integrity` 通常是 `sha512-<base64>`（Base64 编码的原始 digest bytes）。

## 2. 详细流程（逐步）

1. **读取锁与/或 metadata**
    
    - 如果存在 `package-lock.json`：读取 `resolved` 和 `integrity`（SRI）。
        
    - 否则查询 registry metadata（`npm view pkg@ver --json` 或 `https://registry.npmjs.org/pkg`），取 `dist.integrity` 或 `dist.shasum`。
        
2. **下载 tarball（stream）**
    
    - npm 发起 HTTP GET 去 `dist.tarball`（通常根据 lock 的 `resolved` 字段或 registry 返回的 tarball URL）。
        
3. **流式计算/校验摘要**
    
    - 在下载流上，npm 使用 `ssri`（SRI 处理）和/或 Node `crypto` 来计算摘要：
        
        - `ssri.checkStream(stream, expectedIntegrity)` 可同时支持多算法并在流中校验。
            
        - 同时历史或兼容逻辑可能用 `crypto.createHash('sha1')` 计算 hex shasum 与 `dist.shasum` 对比。
            
4. **比对**
    
    - 若 `expected` 是 SRI（例如 `sha512-...`），用相同算法生成并将 base64 表示与 expected 比较（或直接用 `ssri` 做 check）。
        
    - 若 `expected` 是 hex shasum（sha1），把下载流计算出的 sha1 hex 与 expected 比较。
        
5. **结果**
    
    - 校验通过：写入本地 cache（`cacache`），解压至 `node_modules`，继续安装。
        
    - 校验失败：抛出 `EINTEGRITY`，删除缓存中对应条目（或跳过），安装失败。
        

---

## 3. 摘要数据如何得来（发布端 & 客户端）

- **发布端（npm publish）**：打包 tarball → 计算哈希：
    
    - `shasum` = `sha1(tarball)` → hex 字符串 → 写入 `dist.shasum`。
        
    - `integrity` = `sha512-<base64(sha512_bytes)>`（由 `ssri` 格式化）→ 写入 `dist.integrity`。
        
    - registry 保存 tarball 与 metadata（versions 字段等）。
        
- **客户端（安装时）**：下载 tarball → 重新对 tarball 计算 sha512/sha1 并与 lock/metadata 对比（**从不信任远端的哈希，始终重新计算**）。
    

---

## 4. 数据格式与转换（hex ↔ base64）

- `dist.shasum`：**40 个 hex 字符**，表示 20 字节的 SHA-1（如 `5dc0753acbf8521ca2e0f137b4578b917b10cf24`）。
    
- `package-lock.json` 中的 `sha1-...`：SRI 格式，后接 **Base64** 编码的原始 20 字节哈希（如 `sha1-iHs7qdhDk+h6CgufTLdWGYtTVIo=`）。
    

**转换方法**：

- hex → raw bytes → base64：
    
    - Node.js：`Buffer.from(hex, 'hex').toString('base64')` → 加前缀 `sha1-`。
        
    - openssl：`xxd -r -p <hexfile> | openssl base64`（或用脚本）。
        

示例（Node）：

```js
const hex = '5dc0753acbf8521ca2e0f137b4578b917b10cf24';
console.log('sha1-' + Buffer.from(hex,'hex').toString('base64'));
// => sha1-iHs7qdhDk+h6CgufTLdWGYtTVIo=
```

---

## 5. 常见导致 `EINTEGRITY` 的原因与排查步骤

**常见原因**：

- 本地 `cacache` 损坏或不一致
    
- registry / 镜像的 tarball 与 lock 中记录的 hash 不一致（版本被覆盖、镜像同步问题）
    
- 下载被中间代理或 CDN 篡改（返回 HTML 错误页面等）
    
- 下载不完整或网络错误（截断）
    
- package-lock.json 被篡改或合并错误
    
- npm 客户端版本 bug（极少）
    

**快速排查清单**：

1. `npm i --verbose` 看具体的 expected/actual 哈希与报错堆栈。
    
2. `npm cache clean --force` 再重试。
    
3. `npm view <pkg>@<ver> dist` 或 `curl -L https://registry.npmjs.org/<pkg>/<ver>` 查看官方 metadata。
    
4. 直接下载 tarball：
    
    ```bash
    curl -L <tarball-url> -o pkg.tgz
    openssl dgst -sha512 -binary pkg.tgz | openssl base64 -A
    openssl dgst -sha1 pkg.tgz
    ```
    
    将结果与 lock / registry 对比。
    
5. 切换 registry（例如 `npm config set registry https://registry.npmjs.org/`）并重试。
    
6. 检查是否存在公司代理或 CDN 在流量中替换内容（用 `curl -v` / `wget` 检查 response headers）。
    

---

## 6. 镜像源（例如 npmmirror / 淘宝）为何会产生 metadata/tarball 错位（metadata drift）

> 关键概念：**官方 registry（registry.npmjs.org）遵守“版本不可变（immutable）”规则** —— 已发布版本的 tarball 与 metadata 不会被覆盖。**第三方镜像不一定遵守或在同步策略上做了补偿/重写**，从而导致“版本键（versions['1.8.0']）指向了不同版本的 tarball（1.9.0.tgz）”。

**镜像出现错误的典型原因**：

1. **增量同步策略 & 同步冲突**
    
    - 镜像通常使用 polling / incremental sync 拉取上游变更；在网络波动或并发写入时，metadata 的部分字段（例如 dist）可能被错误写入到错误的版本 key 中。
        
2. **安全 / deprecated 自动重定向策略**
    
    - 为减少用户下载已知不安全版本，某些镜像会对 deprecated 或有安全 advisory 的版本做“重定向”或“指向推荐版本”。这会把旧版本的 `dist.tarball` 指向一个推荐的修复版本。
        
3. **覆盖式修复（replace-on-sync）**
    
    - 镜像为节省空间或简化管理，可能采用“将若干历史版本折叠/映射到同一 tarball”的策略（例如把历史低频版本映射到某个稳定 tarball）。这破坏了官方的 immutable 假设。
        
4. **镜像实现 bug / 数据库写入冲突**
    
    - 实现或脚本错误会把 1.9.0 的 dist 写入 1.8.0 的记录位置，造成“metadata 漂移”。
        
5. **同步延迟导致的数据不一致（eventual consistency）**
    
    - 在“最终一致性”的系统里，query 某一时间点可能得到处于过渡状态的记录。
        

**你遇到的症状（示例）**：

- `versions['1.8.0']._id` 或 `dist.tarball` 指向 `1.9.0.tgz`。
    
- `dist.integrity` / `dist.shasum` 与官方 registry 的值不一致。
    
- `package-lock.json` 里记录的 `integrity`（sha512）与镜像返回的 tarball hash 不匹配 → `EINTEGRITY`。
    

---

## 7. 如何验证镜像是否污染及自动检测思路

**手动验证流程**：

1. 对于某个包版本 `pkg@ver`：
    
    - 官方：`curl -sL https://registry.npmjs.org/pkg/ver | jq .dist`（或 `npm view pkg@ver dist --json`）
        
    - 镜像：`curl -sL https://registry.npmmirror.com/pkg/ver | jq .dist`
        
2. 比较两个 `tarball` URL、`integrity`、`shasum`。
    
3. 直接下载镜像的 `tarball`，计算 `sha512` base64（SRI）与 `shasum`，比对。若不一致说明镜像污染或写错。
    

**脚本化检测（思路）**：

- 读取 `package-lock.json` 或 `package.json` 的依赖列表 → 对每个依赖：
    
    1. 从官方 registry 拿 metadata，记下 `dist.integrity` 和 `dist.tarball`。
        
    2. 从当前 registry（镜像）拿 metadata，比较两个 metadata 是否一致。
        
    3. 若发现差异，下载镜像 tarball 并直接计算哈希以确认问题。
        
- 输出报告：不一致列表 + 建议（切 registry / 手动修复 lock / 提交镜像 issue）。
    

---

## 8. 防护与最佳实践（工程建议）

1. **在 CI 中使用官方 registry 或可信任的内部私服**（尽量避免直接用第三方公共镜像作为生产依赖源）。
    
2. **对关键 pipeline 做二次校验**：CI 在 `npm ci` 之后执行对 `node_modules` 中某些关键包的 SRI / sha1 校验（或对已知高风险包做二次下载校验）。
    
3. **锁定 registry 并记录来源**：项目中记录 `npm config get registry`，并在 README / CONTRIBUTING 中明确要求使用哪个 registry。
    
4. **定期运行镜像一致性检查脚本**（对关键依赖）。
    
5. **若用镜像做镜像加速（cache），配置 fallback 到官方 registry**，并在校验失败时自动 fallback。示例策略：若 `EINTEGRITY` 且 registry 是镜像，自动尝试官方 registry。
    
6. **CI/CD 使用 `npm ci`（严格使用 lock），并在失败时直接切换到官方 registry 重新尝试**。
    

---

## 9. 常用命令与示例（便于复制到终端）

- 查看某版本 metadata（官方）：
    

```bash
curl -sL https://registry.npmjs.org/path-to-regexp/1.8.0 | jq .dist
# 或
npm view path-to-regexp@1.8.0 dist --json
```

- 查看镜像 metadata：
    

```bash
curl -sL https://registry.npmmirror.com/path-to-regexp/1.8.0 | jq .dist
```

- 下载 tarball 并计算 sha512（构造 SRI）：
    

```bash
curl -L 'https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-1.8.0.tgz' -o pkg.tgz
openssl dgst -sha512 -binary pkg.tgz | openssl base64 -A
# 然后拼接： sha512-<base64>
```

- 下载 tarball 并计算 sha1 hex：
    

```bash
openssl dgst -sha1 pkg.tgz
```

- Node 脚本快速生成 SRI：
    

```js
const fs = require('fs');
const ssri = require('ssri');
const data = fs.readFileSync('pkg.tgz');
console.log(ssri.fromData(data).toString());
```

---

## 10. 总结要点（便捷回顾）

- `package-lock.json` 是安装时的单一信任来源（有 lock 时优先使用 lock 的 `integrity`）。
    
- `dist.shasum`（hex sha1）与 `sha1-...`（SRI）是相同哈希，只是编码不同：hex → bytes → base64。
    
- `EINTEGRITY` 多数源于 tarball 与期望哈希不一致：可能是本地缓存、网络、或镜像污染。\
    
- 官方 registry 保证版本不可变；第三方镜像（如 npmmirror）可能因为同步策略、重定向、或实现 bug 导致 metadata/tarball 指向错位。
    
- 最安全的做法是在 CI 使用官方 registry 或受控私服，并在遇到 integrity 异常时回退到官方源做二次验证。
    

---

### 附录：快速 checklist（出现 EINTEGRITY 时）

1. `npm i --verbose` 查看具体报错。\
    
2. `npm cache clean --force`。\
    
3. 验证 registry：`npm config get registry`。\
    
4. 对比官方 metadata：`npm view <pkg>@<ver> dist --json`。\
    
5. 手动下载 tarball 并 `openssl` / `ssri` 验证。\
    
6. 若镜像有问题：切官方 registry 并重试安装。
    

---

如果你希望，我可以：

- 把“检测脚本”直接写成 Node.js 工具（自动检测 package-lock.json 中的每个依赖与官方 registry 的一致性），并输出修复建议；
    
- 或把这份笔记导出成 PDF / 侧边展示样式。
    

你想要哪个？