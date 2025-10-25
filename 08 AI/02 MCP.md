# 1 基本介绍

https://refly.ai/share/pages/pag-mgi439nspxd6m0rt4cjkr4ae

简单来讲  MCP 本质是通过 AI 来操作本地的功能


# 2 基本概念

## 2.1 JSON-RPC

1、目前 MCP 本身是基于 JSON-RPC 协议来做参数规范的，具体的 JSON-RPC 的本质可以查看：[JSON-RPC规范详解](https://zhuanlan.zhihu.com/p/708628144)，类似 JSON-RPC 本质其实就是使用类似 JSON 的格式去调用服务器中的函数，并传递参数
![[00 assets/db570664166c9cee326acf298ce09955_MD5.jpeg]]

``` JSON
// 请求
{
  "jsonrpc": "2.0", // 用来声明协议版本，通常是 `"2.0"`
  "method": "getUserInfo", // 希望远程调用的方法名
  "params": {"userId": 123}, // 传递给方法的参数
  "id": 1 // 
}

// 响应
{
  "jsonrpc": "2.0",
  "result": {"name": "Alice", "email": "alice@example.com"}, // 方法执行后的返回结果
  "id": 1 // 与请求中的 id 完全一致
}
```


## 2.2 通信方式

1、针对 MCP 的通信又可以使用 stdio、http。stdio 本身是输入输出流

![[00 assets/321de6c8281840d296374257d15848c6_MD5.jpeg]]

可以使用 process 来使用 stdin、stdout 来使用可读可写流，console.log 底层也是上层封装，在 nodejs 层面使用的 process.stdout.write

![[00 assets/1227bf9ad2f3a2fed56a8f23f121e345_MD5.jpeg]]

## 2.3 生命周期

1、在 MCP 的定义中存在生命周期的概念，大体可以分为：**Initialization**、**Operation**、**Shutdown** 简单理解就是：初始化、使用、结束

![[00 assets/0a0b46eb0b2617e76c95515aaf5592c5_MD5.jpeg]]

2、在前面说了整体传输遵循 JSON-RPC，在初始化的时候有请求（Request）和响应（Response），这里的 `capabilities` 允许生命支持的功能，包括能处理哪些 `primitives`，以及身份交换用于调试和兼容性目的

``` JSON
// request
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {},
      "elicitation": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "title": "Example Client Display Name",
      "version": "1.0.0"
    }
  }
}

// response
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "title": "Example Server Display Name",
      "version": "1.0.0"
    },
    "instructions": "Optional instructions for the client"
  }
}
```

在初始化的最后一个操作就是 notifications 通知一切准备就绪

```JSON
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```


## 2.4 工具发现

1、我们已经初始化了 MCP 服务器，另外一个机制就需要我们告诉我们 MCP 有哪些工具

```JSON
// request
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}

// response
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "calculator_arithmetic",
        "title": "Calculator",
        "description": "Perform mathematical calculations including basic arithmetic, trigonometric functions, and algebraic operations",
        "inputSchema": {
          "type": "object",
          "properties": {
            "expression": {
              "type": "string",
              "description": "Mathematical expression to evaluate (e.g., '2 + 3 * 4', 'sin(30)', 'sqrt(16)')"
            }
          },
          "required": ["expression"]
        }
      },
      {
        "name": "weather_current",
        "title": "Weather Information",
        "description": "Get current weather information for any location worldwide",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name, address, or coordinates (latitude,longitude)"
            },
            "units": {
              "type": "string",
              "enum": ["metric", "imperial", "kelvin"],
              "description": "Temperature units to use in response",
              "default": "metric"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }
}
```

![[00 assets/59f0397b0f09e9b7883da2c936a95994_MD5.jpeg]]

2、下面这是 MCP 官网给的解释，但是为什么针对 AI 来讲，我告诉他有这些工具之后，他就会去使用？目前至少对我来讲这是疑问点

![[00 assets/b45ee14b49e7992f8da80a67581dab18_MD5.jpeg]]

## 2.5 工具调用

```JSON
// request
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "weather_current",
    "arguments": {
      "location": "San Francisco",
      "units": "imperial"
    }
  }
}

// response
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Current weather in San Francisco: 68°F, partly cloudy with light winds from the west at 8 mph. Humidity: 65%"
      }
    ]
  }
}
```

# 3 基本使用

## 3.1 MCP 配置

1、网上很多教程都是按照下面的方式来配置的，其实都是错误的，这个组成最后的结果其实是 `npx -C /Users/zhangjiahui04/测试代码/MCP/03 run src/index.js`，我看网上很多的教材都抄成这样
![[00 assets/f8bcd88c0e01fba8aab9cee862445faf_MD5.jpeg]]

2、如果是针对 NodeJS 执行的话，其实是如下图展示的代码
![[00 assets/9c5dfc336050db07801b176de44993f4_MD5.jpeg]]

3、这就是最终的结果，可以看到已经完成了 `初始化` 和 `工具发现`，在 Cursor 中是可以看到的
![[00 assets/5b9fc619f92d867981318562eafbbfde_MD5.jpeg]]

## 3.2 MCP 调试

调试文档：[https://modelcontextprotocol.io/legacy/tools/inspector](https://modelcontextprotocol.io/legacy/tools/inspector)

1、我们下载 `npm i @modelcontextprotocol/inspector`，再去输入 `npx @modelcontextprotocol/inspector` 就可以看到这个 MCP 的内容
![[00 assets/69e848cb91462afb430ab0defcc718f4_MD5.jpeg]]

## 3.3 代码编写

![[00 assets/477f04d8b57b2a2bc9abcbb7a4ea9c5a_MD5.jpeg]]







