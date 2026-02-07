# 1 基本介绍

BullMQ 是一个 **基于 Redis 的 Node.js 任务队列（job queue）库**，用来把任务持久化到 Redis，然后由一个或多个 Worker 异步消费执行，常用于微服务/分布式架构里解耦与削峰。([docs.bullmq.io](https://docs.bullmq.io/ "What is BullMQ | BullMQ"))

你可以把它想成：
- **Queue（队列）**：一个“待办清单”
- **Job（任务）**：一条待办事项（含数据 data、选项 opts）
- **Worker（工人）**：不断从清单里拿任务来干活的执行者

官方对 Queue 的定义非常直白：**Queue 就是一串等待被处理的 jobs**，job 可以很小（像消息 broker），也可以是长任务。([docs.bullmq.io](https://docs.bullmq.io/guide/queues "Queues | BullMQ"))

其本质是把“耗时/不稳定的事”从请求链路里拎出去


# 2 基本使用

最基础的使用就是两段代码：一个“生产者”入队，一个“消费者”执行。

```ts
import { Queue, Worker } from "bullmq";
import IORedis from "ioredis";

const connection = new IORedis(process.env.REDIS_URL!);

// 生产者：把任务塞进队列
const emailQueue = new Queue("email", { connection });
await emailQueue.add("sendWelcomeEmail", { userId: 123 });

// 消费者：从队列取任务执行
const worker = new Worker(
  "email",
  async (job) => {
    // 你的耗时逻辑：发邮件、转码、生成报表……
    return { ok: true };
  },
  { connection, concurrency: 10 }
);
```

Worker 的语义也很明确：它就是“消息接收者”，职责是把 job 跑完；成功就进 **completed**，异常就进 **failed**，并且失败可以配置自动重试。([docs.bullmq.io](https://docs.bullmq.io/guide/workers "Workers | BullMQ"))


# 3 核心原理

## 3.1 状态机

BullMQ 的关键不是“把函数丢给后台跑”这么简单，而是它把每个 job 变成一个 **状态机**，在 Redis 里按状态分区存放/流转。

官方架构文档给了核心状态流转（简化版）
- 入队时可能在：`wait` / `prioritized` / `delayed`（以及 flow 场景的 `waiting-children`）
- Worker 拿到后进入：`active`
- 执行结束进入：`completed` 或 `failed`（失败可能再被移回 `wait` 做重试）([docs.bullmq.io](https://docs.bullmq.io/guide/architecture "Architecture | BullMQ"))

官方 getters 文档把可见状态列得很全：`completed / failed / delayed / active / wait / waiting-children / prioritized / paused / repeat`。([docs.bullmq.io](https://docs.bullmq.io/guide/jobs/getters "Getters | BullMQ"))

**这套状态机的好处**：你能可靠地做延迟、优先级、重试、暂停、统计、可视化、追踪事件……而不是靠内存队列“运气好别挂”。


## 3.2 Redis 交互

BullMQ 之所以可靠，很大一部分来自两类东西：

**A. 原子操作（Redis 原生命令 + Lua 脚本**）

API 文档里明确提到：**全局 pause 是通过原子 RENAME 把 wait 队列改名成 paused**；Worker 因为使用了阻塞式的 **BRPOPLPUSH** 来取任务，所以当 wait 被改名后就不会再取到新 job；而“添加 job”则需要 **Lua 脚本**先检查 paused list 是否存在，决定放进 wait 还是 paused。([api.docs.bullmq.io](https://api.docs.bullmq.io/classes/v5.Queue.html "Queue | bullmq - v5.67.3"))

这段其实已经把 BullMQ 的“可靠队列搬运”讲透了：**取任务、迁移状态、加锁/防重复、写入结果**都需要强一致的原子步骤，否则分布式下很容易重复消费或丢任务。

源码/构建侧也能看到它确实带了一堆 Lua：BullMQ 的 package.json 构建脚本会把 `src/commands/*.lua` 等复制进 dist 包里（`copy:lua` / `copy:includes:lua`）。([UNPKG](https://app.unpkg.com/bullmq%403.6.3/files/package.json "UNPKG"))

社区 issue 里也常见“锁/脚本竞态”的讨论，例如有 issue 解释了某些极快任务在 `moveToDelayed/moveToFinished` 相关 Lua 脚本与锁同步之间出现微妙竞态导致 “missing lock”。([GitHub](https://github.com/taskforcesh/bullmq/issues/3295?utm_source=chatgpt.com "Error: Missing lock for job ... moveToDelayed ..."))  （这类讨论反而说明：它真的在用“锁 + Lua 原子脚本”硬扛分布式一致性问题。）


**B. 事件总线用 Redis Streams（不是普通 pub/sub）**

如果你想在“某个独立服务/进程”里监听所有 worker 的完成/失败事件，BullMQ 提供 `QueueEvents`，并且官方写明它是 **用 Redis Streams 实现**，相对标准 pub/sub 在断线场景下有“事件不易丢”的性质（并且会自动 trim）。([docs.bullmq.io](https://docs.bullmq.io/guide/events "Events | BullMQ"))


## 3.3 Redis 原子操作

就是 Redis 自带的那些基础指令集（不用额外模块）——每条命令本身都是原子执行的，但**多条命令的组合**就不天然原子了。

BullMQ 里你会反复遇到这些典型命令（举例）
- **LIST（列表）**：`LPUSH/RPUSH/LPOP/RPOP/BRPOPLPUSH` —— 用来当“等待队列 wait、执行队列 active”等
- **ZSET（有序集合）**：`ZADD/ZRANGEBYSCORE/ZREM` —— 用来做“延迟队列 delayed（按时间排序）/优先级”等
- **HASH/STRING**：`HSET/HGET/SET` —— 存 job 元数据、锁 token、计数器等
- **RENAME**：把一个 key 原子改名（暂停队列就靠它）BullMQ 文档明确说全局 pause 用的是对 wait key 的 **原子 RENAME**，并且 worker 取任务用 **BRPOPLPUSH** 阻塞等任务，所以一旦 wait 被 rename 成 paused，worker 就“等不到新任务了”。


## 3.4 Lua 扮演的角色

**一句话**：把“需要多条 Redis 命令才能完成的一次状态迁移”，塞进 Redis 服务器端用 Lua 一口气做完，达到：
1. **原子性**：脚本执行期间不会被别的客户端命令插队（等价于“这坨操作要么全发生，要么全不发生”）
2. **一致性**：不会出现“我已经 LPOP 了，但还没来得及 HSET / 加锁 / 发事件就宕机”的半状态
3. **少 RTT**：不需要 Node ↔ Redis 往返 N 次

BullMQ 自己在 API 文档里就直接点名：**加 job 需要 Lua 脚本**，因为要先检查 paused 列表是否存在、再决定是进 wait 还是进 paused。同样地，像 `moveToActive`（把任务从 wait 搬到 active 并加锁）这一类核心迁移，在 `Scripts` API 里也能看到：它调用脚本时必须带 **token**。你可以把 Lua 脚本理解成：**BullMQ 的“状态机事务”**。



# 4 实际落地

你实际落地时最常用的是这些能力：

**自动重试 + Backoff（退避）**：BullMQ 支持失败后按 backoff 策略重试；内置固定/指数退避，也可自定义；没配置 backoff 就会立刻重试。([docs.bullmq.io](https://docs.bullmq.io/guide/retrying-failing-jobs "Retrying failing jobs | BullMQ"))

**延迟任务 / 定时任务（Job Scheduler）**：新版本里，**Job Schedulers 在 v5.16.0+ 用来替代 repeatable jobs**，它像“按规则生产 job 的工厂”，可以按固定间隔、cron 等生成任务。([docs.bullmq.io](https://docs.bullmq.io/guide/job-schedulers "Job Schedulers | BullMQ"))

**卡死（stalled）与延迟队列维护**：历史上（尤其旧版本）有 `QueueScheduler` 做“后台管家”，负责把到期的 delayed job 推回可执行队列，并检查 stalled job。API 说明里甚至写了：需要至少有一个 QueueScheduler 在跑，否则 delays / stalled / retries / repeatable 等可能无法正确工作。([api.docs.bullmq.io](https://api.docs.bullmq.io/classes/v1.QueueScheduler.html "QueueScheduler | bullmq - v5.67.3"))  。另外官方 guide 也提示过 QueueScheduler 在 BullMQ 2.0+ 有弃用/演进（不同版本机制有变化）。([docs.bullmq.io](https://docs.bullmq.io/guide/queuescheduler?utm_source=chatgpt.com "QueueScheduler - BullMQ"))

其中典型场景（做 Node 后端非常常见）：
- **发邮件/短信/站内信/Push**：外部服务不稳定，重试 + 退避很关键
- **图片/视频处理**：转码、压缩、加水印，CPU/IO 重活
- **导入导出/报表生成**：Excel 解析、聚合统计、生成 PDF
- **调用第三方 API 的批处理**：限流（rate limit）、失败重试、并发控制
- **业务工作流编排**：A 完成后触发 B/C（flow / 依赖任务）([docs.bullmq.io](https://docs.bullmq.io/guide/architecture "Architecture | BullMQ"))
- **跨服务可靠通信**：一个服务投递任务，另一个服务消费；生产者/消费者挂了还能恢复（NestJS 队列章节也强调了这种可靠通信与状态保留）。([docs.nestjs.com](https://docs.nestjs.com/techniques/queues?utm_source=chatgpt.com "Queues | NestJS - A progressive Node.js framework"))

