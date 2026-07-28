# 1. Node.js 子进程管理(spawn):Agent 执行 shell 的工程细节

> **来源**:公众号「程序员成长指北」《Node.js 子进程管理:我是如何被 spawn 逼疯的》,作者 mCell,2026-04-21。原文见 [[../../raw/wx-2026-04-21-Nodejs子进程spawn管理.md]]。
> **为什么值得留页**:原文给了一条很清楚的**分层脉络**(输出→输入→超时→会话→截断),但它是经验分享,好几处只点到"有坑"没给解法或数字。这页在它的骨架上补了**我本机实测的验证结果**(Node v25.9.0),并补了原文完全没提的两个坑。
> 标注约定:[原文] / [实测] / [AI 补充]。

---

## 1.1 一句话主旨

`spawn` 一行就能启动进程,但要做出"安全、可控、可观测"的子进程管理,真正的工作量在**进程生命周期与资源边界**上:输出怎么收、输入什么时候写、超时怎么杀干净、并发怎么限、输出怎么截断。 [原文]

场景是 Agent 要替用户执行 shell 命令——这也是本库关心的语境([[../AI/AI Agent 的可验证开发体系]] 里"后端能独立跑、全部走命令行"那一步的底层实现)。

---

## 1.2 为什么不能用 exec 一把梭

原文的起点:最简方案是 `child_process.exec`,输入命令拿输出,但功能变复杂后四个问题逼着换 `spawn` [原文]:

- 命令跑太久,想实时看输出
- 超时了想杀掉进程
- 同时跑多个命令怎么管
- 输出太多怎么截断

### 1.2.1 补一个原文没说的硬理由:exec 有 1MiB 缓冲上限 [实测]

这是**必须换 spawn 的真实技术原因**,不只是"不够灵活":

`exec` 会把 stdout/stderr 全缓冲到内存,受 `maxBuffer` 限制(**默认 1024×1024 字节 = 1MiB**),超出会**直接杀掉子进程并报错**。

本机实测(Node v25.9.0,子进程输出 2MB):

```
[1] exec  2MB -> ERR code=ERR_CHILD_PROCESS_STDIO_MAXBUFFER  stdout maxBuffer length exceeded
[2] spawn 2MB -> code=0  total bytes=2097152     # 完整收到
```

含义:用 `exec` 跑 `npm run build`、`git log`、`cat 大文件` 这类输出量不可控的命令,**会在你没预料的时候炸**,而且错误长得像是命令自己失败了,很难定位。
`spawn` 走流、不缓冲,没有这个上限——**代价是输出量由你自己管**(见 1.6 截断)。

> [AI 补充] `execSync` 触发时报的是 `ENOBUFS`,和异步版报的错误码不同,搜索时两个都要试。历史上这个默认值只有 200KB,Node 12 起才提到 1MiB。

---

## 1.3 第一层:获取输出

`spawn` 默认不返回输出,只给流,得自己监听 [原文]:

```js
proc.stdout.on('data', (d) => console.log('stdout:', d.toString()))
proc.stderr.on('data', (d) => console.error('stderr:', d.toString()))
proc.on('close', (code) => console.log('进程退出:', code))
```

原文说"这一步还好,主要是耐心"。**这里其实藏着两个坑,原文都没提。** [AI 补充]

### 1.3.1 坑一:`d.toString()` 会切坏多字节字符 [实测]

流按字节切块,一个 UTF-8 汉字占 3 字节,**边界很可能落在字符中间**。每块单独 `toString()` 就会产生乱码(U+FFFD 替换字符)。

实测(子进程输出 20 万个"中"):

```
[3] 裸 d.toString():           chunks=10   含替换字符的块数=9    # 9/10 都坏了
[4] 用 StringDecoder:          chunks=10   含替换字符的块数=0    # 干净
```

**9 成的块都有乱码**,这在中文输出场景里几乎必踩。正确做法:

```js
const { StringDecoder } = require('string_decoder')
const decoder = new StringDecoder('utf8')
proc.stdout.on('data', (d) => {
  const text = decoder.write(d)   // 不完整的尾字节会留在内部缓冲,等下一块
  if (text) handle(text)
})
proc.on('close', () => { const rest = decoder.end(); if (rest) handle(rest) })
```

或者更省事:`proc.stdout.setEncoding('utf8')`,Node 内部就是用 StringDecoder 实现的。

### 1.3.2 坑二:`exit` 和 `close` 不是一回事 [实测]

```
[1] 事件顺序 = exit:0 -> close:0
```

- `exit`:进程已退出,但**stdio 可能还没读完**。
- `close`:stdio 全部关闭,数据收全了。

**要拿完整输出必须在 `close` 里收尾**,在 `exit` 里就返回可能丢尾巴。原文示例用的是 `close`(正确),但没说为什么——这个区别是"忘了等进程退出"那条教训的真实机制。

---

## 1.4 第二层:输入交互与 timing

有些命令要交互(`sudo`、`ftp`、等输入的 python 脚本),得往 `stdin` 写 [原文]:

```js
proc.stdin.write('hello\n')
proc.stdin.end()
```

**timing 是坑**:命令还没准备好你就写,数据会丢。原文的做法是等特定的 **ready signal** 再写,比如看到 `password:` 提示符才写入。 [原文]

> [AI 补充] 更根本的问题是很多程序(如 `ssh`、`sudo`)检测到 stdin 不是终端(TTY)时会拒绝读密码,或者改变输出的缓冲策略(管道下变成全缓冲,导致你迟迟收不到提示符)。这类场景光靠 pipe 解决不了,需要**伪终端(PTY)**,Node 生态一般用 `node-pty`。原文的 ready-signal 方案只在程序愿意从管道读时成立。

---

## 1.5 第三层:超时与终止(最容易漏)

原文的两层退出机制 [原文]:

```ts
private async terminateForTimeout(session: SessionState) {
  if (session.exited) return
  session.proc.kill('SIGTERM')          // 温和退出,给清理资源的机会
  await waitForExit(session, 200)
  if (!session.exited) {
    session.proc.kill('SIGKILL')        // 还不退就强杀
    await waitForExit(session, 200)
  }
}
```

先 SIGTERM 再 SIGKILL 是对的。补三点原文没讲清的机制:

### 1.5.1 `kill()` 返回 true 不代表进程死了 [实测]

```
[2] kill() 返回 = true       # 只表示"信号已发出"
[2] 忽略 SIGTERM 的进程:  killed=true   exitCode=null   # 仍在跑
```

`killed` 属性只意味着**信号成功发送过**,不是"已被杀死"。程序可以注册 handler 忽略 SIGTERM。所以**两层机制里的 `waitForExit` 不是保险,是必需**。

### 1.5.2 被 SIGKILL 的进程 `code` 是 null,要看 signal [实测]

```
[3] SIGKILL 后 close(code, signal) = null  SIGKILL
```

只判 `code !== 0` 会漏掉"被杀"这种情况(code 是 null)。判断退出原因要同时看第二个参数:

```js
proc.on('close', (code, signal) => {
  if (signal) { /* 被信号终止,如超时强杀 */ }
  else if (code !== 0) { /* 自己失败退出 */ }
})
```

### 1.5.3 原文最大的缺口:`proc.kill()` 杀不掉孙进程 [实测]

原文"血的教训"第 5 条只写了一句"信号传递:Ctrl+C 杀的是父进程,子进程还在后台跑",**没说这在 spawn 里同样发生,也没给解法**。而这是 Agent 场景最疼的一个坑——`shell: true` 或者跑 `npm`/`make`/`bash` 脚本时,真正干活的是**孙进程**。

实测(父 node → sh → node,三层):

```
[A] 普通 spawn + proc.kill()              -> 残留孙进程 = 1   # 逃逸了
[B] detached:true + process.kill(-pid)    -> 残留孙进程 = 0   # 干净
```

原因:`proc.kill()` 只给**直接子进程**(那个 shell)发信号。shell 死了,它 fork 出来的孙进程被**重新挂到 init 下继续跑**,变成孤儿进程。

解法(POSIX):`detached: true` 让子进程成为**新进程组组长**,然后给**进程组**发信号(负 PID):

```js
const proc = spawn(cmd, { shell: true, detached: true })
// 注意是 process.kill 而非 proc.kill,PID 取负号 = 整个进程组
try { process.kill(-proc.pid, 'SIGTERM') } catch (e) { /* 已退出会抛 ESRCH */ }
```

> [AI 补充] 两个必须知道的边界:
> 1. **Windows 上没有 POSIX 信号和进程组**,`process.kill(-pid)` 不适用,通常靠 `taskkill /T /F /PID` 杀树。跨平台代码这里必须分叉。
> 2. Node 官方也认为这是个缺口,社区有 issue 在提议内置跨平台的 `subprocess.killTree()`(nodejs/node#64406),目前**尚未落地**,还得自己处理。

---

## 1.6 第四层:会话管理与并发上限

原文用统一会话管理器 [原文]:

```ts
class UnifiedExecManager {
  private sessions = new Map<number, SessionState>()
  private nextId = 1
  private MAX_SESSIONS = 64
}
```

每个子进程有唯一 ID,可以查状态、发信号、取历史输出;同时限制最大活跃数防资源耗尽。

> [AI 补充] `MAX_SESSIONS = 64` 这个数字要和系统的**文件描述符上限**一起看:每个 spawn 至少占 3 个 fd(stdin/stdout/stderr),macOS 默认 `ulimit -n` 常见是 256,64 个会话就是约 200 个 fd,已经贴着上限。`Map` 里的 session **必须在 close 时删掉**,否则就是原文教训第 4 条的"内存泄漏"——泄的不只是内存,还有 fd。

---

## 1.7 第五层:输出截断(按 token 计费的现实约束)

Agent 按 token 收费,子进程输出不能无限返回 [原文]:

```js
function truncateByTokens(text, maxOutputTokens) {
  const maxChars = (maxOutputTokens || 2000) * 4
  if (text.length <= maxChars) return { output: text, deliveredChars: text.length }
  return { output: text.slice(0, maxChars), deliveredChars: maxChars }
}
```

默认最多 8000 字符(2000 token × 4)。

> [AI 补充] 两点保留意见:
> 1. **`token × 4` 这个估算只对英文成立**。中文 1 个字往往就接近 1 个 token,按 4 倍放行会**低估 3~4 倍**,真实 token 数可能爆预算。中文输出多的场景该改系数或直接上 tokenizer。
> 2. **只留头部会丢掉最有用的部分**。构建失败、异常栈的关键信息几乎总在**尾部**。更实用的是**头尾都留、中间省略**(如头 60% + 尾 40%,中间插 `...[truncated N chars]...`),既保住上下文也保住报错。

---

## 1.8 原文的"血的教训"五条(对照本页机制)

| 原文教训 [原文] | 真实机制(本页对应节) |
|---|---|
| 1. 忘了等进程退出 | `exit` ≠ `close`,要在 close 收尾 → 1.3.2 |
| 2. 没处理 stderr | 流是分开的,只监听 stdout 会静默丢错误 |
| 3. 输入 timing,没等 ready 就写 stdin | 需要 ready signal,或 PTY → 1.4 |
| 4. 内存泄漏,进程退出没清理 | Map 未删 session,泄内存也泄 fd → 1.6 |
| 5. 信号传递,子进程还在后台跑 | **孙进程逃逸,需 detached + kill(-pid)** → 1.5.3 |

---

## 1.9 关联

- [[../AI/AI Agent 的可验证开发体系]]:直接衔接。那页讲"把后端改造成能脱离 UI 独立运行、全部调用走命令行",本页就是那一步的**实现细节**——命令行执行能力做不稳,上面的可验证闭环就跑不起来(超时杀不干净、输出丢尾巴,回归测试的结果都不可信)。
- **本库摄入 skill 的同类问题** [AI 补充]:`skills/` 下的脚本也在跑外部进程(yt-dlp 抽音轨、ffmpeg 转码)。1.5.3 的孙进程逃逸风险同样存在——ASR 转写中途中断时,ffmpeg 可能残留。目前脚本靠 Python `subprocess` 且未 detached,值得哪天体检一下。
- **index 09 Python** 里的 subprocess 相关:概念一一对应(Popen/communicate/timeout/kill),Python 的 `subprocess.run(timeout=)` 内部也是先 kill 后 wait,同样杀不掉孙进程,需要 `start_new_session=True` + `os.killpg`。

---

## 1.10 实测环境与复现说明

- 环境:macOS,Node **v25.9.0**,本机实测,四组探针(exec/spawn 缓冲、UTF-8 切断、事件顺序与信号语义、孙进程逃逸)。
- 结论仅代表该版本 + POSIX 平台;Windows 的信号与进程组行为完全不同(见 1.5.3)。
- 原文全文:[[../../raw/wx-2026-04-21-Nodejs子进程spawn管理.md]]
- 官方文档:https://nodejs.org/api/child_process.html
