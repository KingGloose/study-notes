# 1 基本介绍

1、简单来讲  MCP 本质是通过 AI 来操作本地的功能

![[00 assets/260c6fe68baa57f4d38592844150299e_MD5.jpeg]]


# 2 基本使用

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

2、针对 MCP 的通信又可以使用 stdio、http。stdio 本身是输入输出流

![[00 assets/321de6c8281840d296374257d15848c6_MD5.jpeg]]

可以使用 process 来使用 stdin、stdout 来使用可读可写流，console.log 底层也是上层封装，在 nodejs 层面使用的 process.stdout.write

![[00 assets/1227bf9ad2f3a2fed56a8f23f121e345_MD5.jpeg]]

3、在 MCP 的定义中存在生命周期的概念，大体可以分为：**Initialization**、**Operation**、**Shutdown** 简单理解就是：初始化、使用、结束

![[00 assets/0a0b46eb0b2617e76c95515aaf5592c5_MD5.jpeg]]

4、在前面说了整体传输遵循 JSON-RPC，在初始化的时候有请求（Request）和响应（Response）










![[00 assets/3f4fea73788810843336b07bd74e08c7_MD5.jpeg]]
![[00 assets/ebbc152857aae44f0e2a8368b11ec593_MD5.jpeg]]

![[00 assets/2566e80fde5e1023d8acc1f3510142c2_MD5.jpeg]]

![[00 assets/5a4354f3e0aa5c2f76ee1cd565fbbed4_MD5.jpeg]]

![[00 assets/e4ab85f4102840894d46d219cb78c5ec_MD5.jpeg]]



![[00 assets/8ee476b7a650fc9b5c025c1f9aa89ed9_MD5.jpeg]]



![[00 assets/1f2e3aa984c330b4eaed5510061898e0_MD5.jpeg]]![[00 assets/9f1a376b2b51361d8f73a501d3885ba7_MD5.jpeg]]

要调试的话，可以使用 console.error 来处理，因为这不是标准输入输出
![[00 assets/ff2a64460719ffadb9d39cada7e1fb86_MD5.jpeg]]


![[00 assets/a708a63cbb42dc7a9eca4e44fc419edb_MD5.jpeg]]