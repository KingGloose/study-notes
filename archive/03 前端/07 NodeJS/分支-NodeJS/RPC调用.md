## 1. RPC 是什么

RPC，Remote Procedure Call，中文通常叫“远程过程调用”或“远程方法调用”。它的核心思想是：**让一个进程/服务去调用另一个进程/服务里的方法，并尽量把这种调用包装得像本地函数调用一样**。在 gRPC 的官方定义里，客户端可以像调用本地对象的方法一样，去调用另一台机器上服务的方法；JSON-RPC 的规范也把它定义为一种轻量、无状态、与传输层无关的远程调用协议。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

所以，RPC 的重点并不在于“是不是 HTTP”，而在于 **通信抽象**：调用方关心的是 `getUserInfo(1001)` 这种“方法”和“参数”，而不是先去想 URL、资源路径、控制器和路由。这个思维方式与 REST 的“面向资源”不同，RPC 更偏“面向行为 / 面向服务方法”。从 gRPC 的设计来看，它先定义 service 和 rpc method，再由客户端 stub 和服务端实现去完成调用链路，这就是典型的 RPC 思维。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

---

## 2. 在 Node.js 里，RPC 到底意味着什么

Node.js 本身并没有一个叫“RPC”的内建模块；它提供的是做网络通信的基础能力，比如 `node:http`、`node:http2`、`node:net`、`node:tls`。因此更准确地说，**Node.js 不是自带 RPC，而是适合作为 RPC 的实现端或调用端**：你可以基于 HTTP、HTTP/2、TCP、TLS，自己实现协议，或者直接使用 gRPC、JSON-RPC、Thrift、tRPC 这类现成方案。这个结论可以从 Node 官方文档对 `http`、`http2`、`net` 这些基础网络模块的定位，以及 gRPC/Thrift/tRPC 官方文档对其 Node 用法的说明中推出来。([Node.js](https://nodejs.org/api/http.html?utm_source=chatgpt.com "HTTP | Node.js v25.8.1 Documentation"))

站在 Node.js 工程实践里，RPC 通常有三种实现层级：

### 2.1 自己基于 HTTP / HTTP2 / TCP 封一层协议

最底层的做法，是你自己定义一个请求格式，比如：

```json
{
  "service": "UserService",
  "method": "getUserInfo",
  "params": { "userId": 1001 },
  "requestId": "abc123"
}
```

然后用 Node 的 `http`、`http2` 或 `net` 模块把它发出去，对端再解析、分发、执行、回包。Node 官方文档说明了 `node:http` 是低层 HTTP 接口，`node:http2` 是面向 HTTP/2 特性的低层接口，`node:net` 则用于 TCP / IPC 的流式连接；JSON-RPC 规范也明确说明它是“传输无关”的，可以跑在 socket、HTTP 或消息环境之上。([Node.js](https://nodejs.org/api/http.html?utm_source=chatgpt.com "HTTP | Node.js v25.8.1 Documentation"))

这种方式的好处是完全可控，坏处也很明显：**序列化、路由分发、异常码、超时、重试、类型约束、兼容升级、链路追踪** 都要你自己补。小项目里这会很灵活，大项目里往往会越写越像“重新发明一个 RPC 框架”。

### 2.2 用 JSON-RPC

JSON-RPC 是一种很轻的 RPC 协议，规范里定义了 `jsonrpc`、`method`、`params`、`id` 等固定字段。它简单、直观、调试友好，尤其适合内部工具、管理后台、快速联调场景。([jsonrpc.org](https://www.jsonrpc.org/specification "JSON-RPC 2.0 Specification"))

一个典型 JSON-RPC 请求长这样：

```json
{
  "jsonrpc": "2.0",
  "method": "getUserInfo",
  "params": { "userId": 1001 },
  "id": 1
}
```

它的优点是门槛低、跨语言容易；缺点是强类型约束偏弱，接口演进、代码生成、复杂流式通信能力一般，规模一上来通常不如 gRPC 规范。

### 2.3 用 gRPC

这是现代服务间 RPC 最常见、也最“正统”的方案之一。gRPC 官方文档把它定义为高性能、跨语言的 RPC 框架；它支持用 `.proto` 文件同时作为 **接口定义语言（IDL）** 和消息格式定义，客户端和服务端都可以基于同一份协议生成代码。官方资料也明确说明，Node 和 Java 都支持通过 `.proto` 生成对应的 client/server 代码。([gRPC](https://grpc.io/?utm_source=chatgpt.com "gRPC"))

gRPC 的工程价值主要来自三点：第一，**接口契约前置**，先定义 service 和 message；第二，**跨语言一致性**，Node、Java、Go 等都能从同一份协议出代码；第三，**通信语义更完整**，不仅有普通请求响应，还有服务端流、客户端流、双向流，并且官方概念层面直接支持 deadline / timeout、cancel、status code 等分布式调用里很关键的机制。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

---

## 3. Node.js 里如何实现 RPC

如果你从零开始，在 Node.js 里做 RPC，推荐把思路拆成 5 层：
1. **服务定义**：定义有哪些 service、method、请求结构、响应结构。
2. **序列化协议**：JSON、Protobuf、MsgPack 等。
3. **传输层**：HTTP、HTTP/2、TCP。
4. **客户端代理**：让调用端像 `client.getUserInfo()` 一样使用。
5. **服务端分发器**：收到请求后把 `service + method` 分发到真实函数执行。

这套结构本质上就是所有 RPC 框架都在做的事情。gRPC 官方文档里讲得很清楚：从 `.proto` 开始，生成客户端 stub 和服务端基类；客户端调用 stub，服务端实现方法，gRPC 基础设施负责请求解码、执行方法、响应编码。([gRPC](https://grpc.io/docs/what-is-grpc/core-concepts/?utm_source=chatgpt.com "Core concepts, architecture and lifecycle"))

### 3.1 用 gRPC 在 Node.js 实现

gRPC 在 Node 侧的典型流程是：
- 写 `.proto`
- 用 `@grpc/proto-loader` 加载 proto，或用 `protoc` 做静态代码生成
- 用 `@grpc/grpc-js` 创建 server / client
- 服务端注册方法实现
- 客户端拿 stub 直接调用

这不是“民间约定”，而是 gRPC Node 官方教程直接给出的做法：Node 教程展示了两种方式——运行时动态加载 `.proto`，以及通过 `protoc` 静态生成代码；同时给出了 `@grpc/grpc-js` 和 `@grpc/proto-loader` 的使用方式。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

一个最小 proto 可以这样写：

```proto
syntax = "proto3";

package user;

service UserService {
  rpc GetUserInfo (GetUserInfoRequest) returns (GetUserInfoResponse) {}
}

message GetUserInfoRequest {
  int64 userId = 1;
}

message GetUserInfoResponse {
  int64 userId = 1;
  string name = 2;
}
```

Node 服务端示意：

```js
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('./user.proto', {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const proto = grpc.loadPackageDefinition(packageDefinition).user;

function getUserInfo(call, callback) {
  const { userId } = call.request;
  callback(null, {
    userId,
    name: '张三',
  });
}

const server = new grpc.Server();
server.addService(proto.UserService.service, {
  GetUserInfo: getUserInfo,
});

server.bindAsync(
  '0.0.0.0:50051',
  grpc.ServerCredentials.createInsecure(),
  () => server.start()
);
```

Node 客户端示意：

```js
const client = new proto.UserService(
  '127.0.0.1:50051',
  grpc.credentials.createInsecure()
);

client.GetUserInfo({ userId: 1001 }, (err, res) => {
  console.log(err, res);
});
```

这背后的本质是：**你写的不是 URL 调用，而是 service/method 调用；真正的网络细节由 stub 和框架兜底**。这和 Node 教程里展示的加载 proto、拿到 service descriptor、创建 server/client 的思路一致。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

### 3.2 用 JSON-RPC 在 Node.js 实现

如果你不想一上来就上 Protobuf/gRPC，也可以直接用 `node:http` 实现一个 JSON-RPC 服务器。Node 官方文档说明 `http` 模块本身就是低层接口，适合你自己处理 headers、body、流；JSON-RPC 规范则规定了方法名、参数、请求 ID 的结构。([Node.js](https://nodejs.org/api/http.html?utm_source=chatgpt.com "HTTP | Node.js v25.8.1 Documentation"))

服务端大致像这样：

```js
const http = require('node:http');

const handlers = {
  getUserInfo: async ({ userId }) => ({ userId, name: '张三' }),
};

http.createServer(async (req, res) => {
  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', async () => {
    const rpcReq = JSON.parse(body);
    const fn = handlers[rpcReq.method];

    if (!fn) {
      res.end(JSON.stringify({
        jsonrpc: '2.0',
        error: { code: -32601, message: 'Method not found' },
        id: rpcReq.id
      }));
      return;
    }

    const result = await fn(rpcReq.params);
    res.end(JSON.stringify({
      jsonrpc: '2.0',
      result,
      id: rpcReq.id
    }));
  });
}).listen(3000);
```

这类方案适合“先把 RPC 模式跑通”，但要进入正式工程，一般还得补齐鉴权、超时、幂等、traceId、错误码、重试策略等。

### 3.3 tRPC 算不算 RPC

算，但它更像 **TypeScript 生态里的 RPC 风格框架**。tRPC 官方文档强调的是“端到端 typesafe API”，客户端知道有哪些 procedures，以及它们的输入输出类型；同时它也明确说明，tRPC API 本质上仍然可以像普通 HTTP 请求那样被调用。([trpc.io](https://trpc.io/docs/quickstart "Quickstart | tRPC"))

所以，tRPC 特别适合 **Node + TypeScript + React/Next.js** 的一体化项目；但如果你的目标是 **Node 调 Java**，它就不是首选，因为它最强的价值在 TS 类型推导，不在跨语言互通。

---

## 4. 如果要通过 RPC 去调用 Java 中的代码，怎么实现

### 4.1 最推荐：Node 客户端 + Java gRPC 服务端

这是最标准、也最稳的跨语言方案。gRPC 官方文档明确说明，Node 和 Java 都可以基于同一份 `.proto` 文件生成对应的客户端/服务端代码；Java 教程中也直接展示了如何用 `protoc` 生成 Java 的消息类和 `RouteGuideGrpc` 这样的服务基类与 stub。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

它的落地步骤通常是：
1. **定义共享的 `.proto` 接口**  
    这一步是“契约先行”，把 Java 暴露给 Node 的能力收敛成稳定接口。
2. **Java 侧生成代码并实现服务**  
    Java 官方教程说明，`protoc` + gRPC Java 插件会生成消息类和服务基类；服务端只要继承生成的基类并覆写对应方法。([gRPC](https://grpc.io/docs/languages/java/basics/ "Basics tutorial | Java | gRPC"))
3. **Node 侧加载同一份 proto，生成 client stub**  
    Node 官方教程展示了动态加载 proto 和创建客户端 stub 的过程。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))
4. **Node 像本地调用一样调用 Java 方法**  
    例如 `client.GetUserInfo({ userId: 1001 })`，但这次真正执行逻辑的是 Java 服务。

Java 端示意代码：

```java
public class UserServiceImpl extends UserServiceGrpc.UserServiceImplBase {
  @Override
  public void getUserInfo(GetUserInfoRequest request,
                          StreamObserver<GetUserInfoResponse> responseObserver) {
    GetUserInfoResponse response = GetUserInfoResponse.newBuilder()
        .setUserId(request.getUserId())
        .setName("张三")
        .build();

    responseObserver.onNext(response);
    responseObserver.onCompleted();
  }
}
```

Node 端示意代码：

```js
client.GetUserInfo({ userId: 1001 }, (err, res) => {
  console.log(res);
});
```

这是我最推荐你在“Node 调 Java”场景下采用的方式，因为它同时解决了 **跨语言契约、序列化效率、代码生成、接口升级** 这几件最难缠的事。gRPC 官方和 Protobuf 官方都强调了：同一份协议可生成多语言绑定，而 Protobuf 本身是语言无关、平台无关的结构化序列化机制，并且支持向后兼容式演进。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

### 4.2 可选方案：Node + Java 通过 Thrift 通信

Apache Thrift 的官方定位也很明确：先定义数据类型和服务接口，再由编译器生成多语言代码，让客户端和服务端跨语言通信。官方首页甚至直接给了“Java Server + 其他语言 Client”的示例思路。([thrift.apache.org](https://thrift.apache.org/ "Apache Thrift - Home"))

如果你所在公司历史上已经大量使用 Thrift，那它当然可行；但如果你是新项目，通常今天大家更优先想到 gRPC。原因不是 Thrift 不行，而是 gRPC 在现代服务治理、流式语义、生态工具、观测性整合上通常更常见。

### 4.3 最容易起步但约束较弱：JSON-RPC / HTTP

如果 Java 服务已经是一个成熟的 Spring Boot 系统，而你暂时不想引入 Protobuf、代码生成、HTTP/2，那么还有一个很现实的做法：**Java 暴露 JSON-RPC 风格接口，Node 按 JSON-RPC 协议请求它**。JSON-RPC 规范本身就是传输无关、JSON 结构固定；这意味着 Java 和 Node 都很好实现。([jsonrpc.org](https://www.jsonrpc.org/specification "JSON-RPC 2.0 Specification"))

它的问题也很直接：你失去了 gRPC 那种“共享 proto + 自动生成强约束客户端”的硬边界，长期维护容易退化成“披着 RPC 名字的普通 JSON 接口”。

---

## 5. RPC 具体适合哪些场景

### 5.1 微服务 / 服务拆分

当系统被拆成用户服务、订单服务、库存服务、支付服务、营销服务之后，服务与服务之间一定需要通信。RPC 特别适合这种 **内部服务间调用**：调用方关心“调哪个方法”，而不是“拼哪个 URL”。gRPC 官方也把它定位为适合分布式应用与服务的方式。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

### 5.2 跨语言系统集成

这是你现在最关心的点：Node.js 想复用 Java 里的能力，或者 Node 做 BFF / 网关层，后面挂一堆 Java 服务。gRPC 和 Thrift 都是为这种“不同语言但共享一套接口契约”的场景设计的。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

### 5.3 需要流式通信的场景

如果只是最普通的 CRUD，REST 和 RPC 都能干；但如果你需要 **服务端流、客户端流、双向流**，比如日志流、订阅流、实时协作、持续推送、批量上传边传边处理，gRPC 的模型会自然得多。官方文档明确列出了四种调用类型：普通 unary、服务端流、客户端流、双向流。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

### 5.4 高约束的内部平台

比如公司内部中台、统一用户中心、风控服务、计费服务、权限服务。这类能力通常要求接口演进稳、跨团队协作清晰、客户端不要乱写。共享 `.proto` 或 IDL 的 RPC 模式，在这种时候很有优势，因为接口定义天然更“硬”。gRPC 和 Protobuf 官方文档都强调了基于 `.proto` 的定义、代码生成与兼容升级能力。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

---

## 6. RPC 的实际意义

RPC 的实际意义，不是“把 HTTP 换个名字”，而是把 **分布式系统里的调用关系做成一种工程化约束**。

第一层意义是 **把通信抽象成接口契约**。  
以前你可能手写一堆 `axios.post('/xxx')`；而 RPC 更强调“先有 service definition，再有实现和调用”。这会让系统边界更清晰，也更适合多人协作。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

第二层意义是 **把跨语言通信标准化**。  
Node、Java、Go、Python 之间最烦的并不是“怎么发请求”，而是“数据结构怎么统一、升级怎么兼容、谁来保证字段不乱改”。Protobuf 官方文档强调它是语言无关、平台无关的序列化机制，而且支持扩展和兼容演进；gRPC 则把它拿来当接口定义和消息格式的核心。([protobuf.dev](https://protobuf.dev/overview/ "Overview | Protocol Buffers Documentation"))

第三层意义是 **把分布式问题显式化**。  
在单体里你调函数，最多就是 try/catch；但在分布式里你一定会遇到超时、取消、状态码、重试、部分成功、链路追踪这些问题。gRPC 官方概念文档专门把 deadline/timeout、cancellation、status code 当成核心能力讲，这说明成熟 RPC 不是只管“发出去”，而是把“远程调用一定会失败”这件事纳入协议和框架层。([gRPC](https://grpc.io/docs/what-is-grpc/core-concepts/ "Core concepts, architecture and lifecycle | gRPC"))

---

## 7. 为什么需要 RPC 技术

你可以把这个问题理解成：**为什么“普通 HTTP 接口”还不够？**

答案不是“HTTP 不行”，而是 **当系统复杂到一定程度时，单纯的 HTTP + JSON + 手写文档 + 手写 SDK，会开始失控**。你会遇到这些问题：
- 接口文档和真实实现不一致
- 前后端 / 多语言团队各写各的类型定义
- 字段升级靠口头同步
- 服务之间调用风格不统一
- 超时、重试、错误码、流式能力全靠各项目自己补
- 一个 Java 服务改了字段，Node 侧可能几周后才发现

RPC 的价值，就是用 **IDL、代码生成、统一调用模型、统一错误模型、统一超时语义** 去压住这种失控趋势。gRPC 官方文档对 service definition、stub、status、deadline、streaming 的强调，本质上都在服务这个目标。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

换句话说，RPC 不是为了“显得高级”，而是为了在系统规模、团队规模、语言数量、调用链长度上来之后，仍然能保持 **接口稳定、调用一致、协作成本可控**。这也是为什么它在内部微服务里常见，而在简单对外开放 API 或极小项目里未必是第一选择。后者更多是工程判断：从这些官方设计目标可以推断，RPC 更偏向内部系统协作和服务间通信，而不是为了替代所有 REST 场景。([gRPC](https://grpc.io/?utm_source=chatgpt.com "gRPC"))

---

## 8. 你可以怎么理解“Node 调 Java 的最佳落地”

如果你现在是一个 Node.js / 前端出身工程师，要和 Java 系统打通，我给你的结论很直接：

**第一选择：gRPC。**  
原因是它最适合“Node 做调用端，Java 做能力端”的模式：同一份 `.proto` 既是文档，也是类型契约，也是代码生成输入。([gRPC](https://grpc.io/docs/languages/node/basics/ "Basics tutorial | Node | gRPC"))

**第二选择：JSON-RPC over HTTP。**  
适合先快速接入、成本低、调试方便，但中长期治理能力一般。([jsonrpc.org](https://www.jsonrpc.org/specification "JSON-RPC 2.0 Specification"))

**第三选择：Thrift。**  
不是差，而是更看组织历史包袱；如果公司已有 Thrift 体系，就跟着生态走。([thrift.apache.org](https://thrift.apache.org/ "Apache Thrift - Home"))

**不建议把 tRPC 当成 Node ↔ Java 主方案。**  
它在 TypeScript 全栈里非常香，但它最强的“端到端 typesafe”价值主要建立在 TS 生态里，不是跨 Java 生态的通用契约方案。这个判断是根据 tRPC 官方文档强调的 procedure/typesafe client 模型，以及它本身仍可通过普通 HTTP 请求调用这一特点推出来的。([trpc.io](https://trpc.io/docs/quickstart "Quickstart | tRPC"))

---

## 9. 一段总结

RPC，本质上是 **把跨进程、跨机器、跨语言的调用，包装成“像本地方法调用一样”的工程模型**。在 Node.js 里，它可以基于 HTTP、HTTP/2、TCP 自己实现，也可以借助 JSON-RPC、gRPC、Thrift、tRPC 等方案落地；而在 **Node 调 Java** 的场景下，最成熟的主流做法通常是 **共享 `.proto`，Java 提供 gRPC 服务，Node 生成 client stub 去调用**。([gRPC](https://grpc.io/docs/what-is-grpc/introduction/ "Introduction to gRPC | gRPC"))

它真正解决的问题，不是“发一个请求”，而是 **让复杂系统里的服务调用有统一契约、统一类型、统一语义、统一治理方式**。当你的系统开始拆服务、开始跨语言、开始有长调用链、开始需要流式能力和严格接口管理时，RPC 就不再是“可选知识点”，而会慢慢变成一类很实用的基础设施思维。([gRPC](https://grpc.io/docs/what-is-grpc/core-concepts/ "Core concepts, architecture and lifecycle | gRPC"))
