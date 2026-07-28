# Node.js 子进程管理：我是如何被 spawn 逼疯的

- 作者: mCell
- 公众号: 程序员成长指北
- 发布日期: 2026-04-21
- 原文: https://mp.weixin.qq.com/s/UzIPnaNlovWMMLqD0h4S_w
- 抓取日期: 2026-07-28

---
```
点击上方 程序员成长指北，关注公众号

回复1，加入高级Node交流群
```

# Node.js 子进程管理：我是如何被 spawn 逼疯的

做 agent开发 之前，我对 Node.js 子进程的理解基本等于零。

不就是在代码里调个 `spawn` 跑个命令吗？能有多难。

结果，真正上手才发现——这玩意儿的水比我想的深多了。

## 背景：为什么我需要 spawn

在开发一个 Agent，要替用户干活，核心能力之一就是执行 shell 命令。

最简单的方案是什么？`child_process.exec` 一把梭，输入命令，拿到输出，完事儿。

但随着功能变复杂，问题就来了：

* 命令执行时间太长，想实时看输出怎么办？
* 超时了想杀掉进程，怎么搞？
* 同时跑多个命令，怎么管理？
* 输出太多，怎么截断？

这些问题逼着我去认真看了 `child_process` 的 API，然后发现——原来 spawn 才是真·主角。

## spawn 是什么

简单说，`spawn` 是 Node.js 用来启动子进程的 API：

```
const { spawn } = require('child_process')  
const proc = spawn('ls', ['-la'])
```

但这只是最基础的用法。真正的挑战在于：你怎么管好这个进程。

### 第一层：获取输出

spawn 默认不返回输出，只给你流。你得自己监听：

```
proc.stdout.on('data', (data) => {  
  console.log('stdout:', data.toString())  
})  
proc.stderr.on('data', (data) => {  
  console.error('stderr:', data.toString())  
})  
proc.on('close', (code) => {  
  console.log('进程退出:', code)  
})
```

这一步还好，主要是耐心。

### 第二层：输入交互

更麻烦的是，有些命令需要交互——比如 `sudo`、`ftp`、`python` 脚本等待用户输入。

这时候你得用 `stdin` 写数据进去：

```
proc.stdin.write('hello\n')  
proc.stdin.end()
```

但 timing 很容易出问题：命令还没准备好，你就开始写，数据就丢了。

memo 的做法是等命令输出特定的「ready signal」再写入，比如看到 `password:` 提示符再写。

### 第三层：超时与终止

这是最容易漏的地方。

我一开始写的代码大概是这样：

```
const proc = spawn('npm', ['run', 'build'])  
proc.on('close', () => {  
  /* 处理结果 */  
})
```

看起来没问题，但——如果这个命令跑 10 分钟怎么办？用户等的花儿都谢了。

memo 现在的做法是两层退出机制：

```
private async terminateForTimeout(session: SessionState) {  
  if (session.exited) return  
  session.proc.kill('SIGTERM')  
  await waitForExit(session, 200) // 等 200ms  
  if (!session.exited) {  
    session.proc.kill('SIGKILL') // 还是没退就直接杀了  
    await waitForExit(session, 200)  
  }  
}
```

先 SIGTERM（温和退出，给程序清理资源的机会），再 SIGKILL（强制杀死）。

### 第四层：进程池与会话管理

跑一个命令还好，但如果同时跑几十个呢？

memo 用的方案是统一会话管理器：

```
class UnifiedExecManager {  
  private sessions = new Map<number, SessionState>()  
  private nextId = 1  
  private MAX_SESSIONS = 64  
}
```

每个子进程都有唯一 ID，可以：

* 查询状态
* 发送信号（kill）
* 获取历史输出

同时限制最大活跃数量，防止资源被耗尽。

### 第五层：输出截断

Agent 是按 token 收费的，子进程输出不能无限返回。

memo 做了截断处理：

```
function truncateByTokens(text: string, maxOutputTokens?: number) {  
  const maxChars = (maxOutputTokens || 2000) * 4  
  if (text.length <= maxChars) {  
    return { output: text, deliveredChars: text.length }  
  }  
  return {  
    output: text.slice(0, maxChars),  
    deliveredChars: maxChars,  
  }  
}
```

默认最多返回 8000 字符，不够可以调。

## 血的教训

踩过的坑列几个：

1. 忘了等进程退出：spawn 是异步的，进程可能还在跑，但你以为已经结束了
2. 没处理 stderr：只看 stdout，错误信息全丢了
3. 输入 timing：没等命令 ready 就写 stdin，数据被吞了
4. 内存泄漏：进程退出了但没清理，长时间运行内存慢慢涨
5. 信号传递：Ctrl+C 杀的是父进程，子进程还在后台跑

## 总结

spawn 看起来简单——一行代码就启动了。

但真正做一个「安全、可控、可观测」的子进程管理系统，需要考虑的细节比我想的多得多：

* 输出流处理
* 输入交互
* 超时终止
* 会话管理
* 资源限制
* 内存清理

好消息是，这些坑踩一遍之后就通了。memo 现在跑得很稳，这些经验也值得分享给你。

如果你也在做类似的 Agent 或 CLI 工具，希望这篇文章能帮你少踩几个坑。

---

> 原文地址： Cell Stack（2026-02-15）。
>
> 作者：mCell

Node 社群

```
我组建了一个氛围特别好的 Node.js 社群，里面有很多 Node.js小伙伴，如果你对Node.js学习感兴趣的话（后续有计划也可以），我们可以一起进行Node.js相关的交流、学习、共建。下方加 考拉 好友回复「Node」即可。

> (原文此处为加群二维码,C 档装饰型,按 AGENTS.md 图片规则未入库)

   “分享、点赞、在看” 支持一波👍
```
