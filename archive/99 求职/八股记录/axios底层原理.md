
---
### 🤖 Assistant

---

**Axios 的底层原理可拆解为以下核心模块**：

---

### **一、核心架构设计**
Axios 采用 **分层设计**，主要分为：
1. **请求/响应拦截器链**（Interceptor Chain）
2. **适配器层**（Adapter）
3. **配置合并与数据处理**
4. **取消请求机制**

---

### **二、请求/响应拦截器链**
#### **1. 拦截器实现原理**
- **链式执行**：拦截器通过 `Promise` 链式调用，形成一个 **中间件队列**。
- **执行顺序**：请求拦截器 → 发起请求 → 响应拦截器 → 最终结果。

```javascript
// 拦截器存储结构
const interceptors = {
  request: [],
  response: []
};

// 添加拦截器
axios.interceptors.request.use(config => {
  console.log('请求拦截器1');
  return config;
});
axios.interceptors.response.use(response => {
  console.log('响应拦截器1');
  return response;
});

// 执行流程
let chain = [dispatchRequest, undefined]; // 核心请求方法
interceptors.request.forEach(interceptor => {
  chain.unshift(interceptor.fulfilled, interceptor.rejected); // 请求拦截器插入头部
});
interceptors.response.forEach(interceptor => {
  chain.push(interceptor.fulfilled, interceptor.rejected); // 响应拦截器插入尾部
});

// 构建 Promise 链
let promise = Promise.resolve(config);
while (chain.length) {
  promise = promise.then(chain.shift(), chain.shift());
}
```

#### **2. 拦截器特性**
- **可中断性**：在拦截器中抛出错误或返回 `Promise.reject` 会中断后续流程。
- **异步支持**：拦截器可返回 `Promise` 对象，实现异步操作（如 Token 刷新）。

---

### **三、适配器层（Adapter）**
#### **1. 跨平台请求发送**
Axios 根据环境选择适配器：
- **浏览器端**：基于 `XMLHttpRequest` 或 `Fetch API`（需配置）。
- **Node.js 端**：基于 `http`/`https` 模块。

```javascript
// 适配器选择逻辑
function getDefaultAdapter() {
  if (typeof XMLHttpRequest !== 'undefined') {
    return xhrAdapter; // 浏览器
  } else if (typeof process !== 'undefined') {
    return httpAdapter; // Node.js
  }
}
```

#### **2. XMLHttpRequest 封装（浏览器端）**
- **创建 XHR 对象**：初始化请求并绑定事件。
- **处理超时**：通过 `xhr.timeout` 设置。
- **处理进度**：通过 `xhr.upload.onprogress` 和 `xhr.onprogress` 监听。

```javascript
// xhrAdapter 核心代码片段
const xhr = new XMLHttpRequest();
xhr.open(config.method.toUpperCase(), config.url, true);
xhr.timeout = config.timeout;

// 绑定事件
xhr.onreadystatechange = function handleLoad() {
  if (!xhr || xhr.readyState !== 4) return;
  const response = {
    data: xhr.response,
    status: xhr.status,
    headers: parseHeaders(xhr.getAllResponseHeaders())
  };
  settle(resolve, reject, response);
};

// 发送请求
xhr.send(config.data);
```

#### **3. Node.js http 模块封装**
- **处理流式数据**：支持 `stream` 模式传输。
- **处理重定向**：自动跟踪 3xx 状态码。

```javascript
// httpAdapter 核心代码片段
const http = require('http');
const https = require('https');

const adapter = config => {
  return new Promise((resolve, reject) => {
    const transport = config.url.startsWith('https') ? https : http;
    const req = transport.request(config.url, {
      method: config.method,
      headers: config.headers
    }, res => {
      let data = [];
      res.on('data', chunk => data.push(chunk));
      res.on('end', () => {
        resolve({
          data: Buffer.concat(data),
          status: res.statusCode,
          headers: res.headers
        });
      });
    });
    req.on('error', reject);
    req.end(config.data);
  });
};
```

---

### **四、配置合并策略**
#### **1. 优先级规则**
配置按优先级合并：`请求级配置` > `实例级配置` > `全局默认配置`。

```javascript
// 配置合并逻辑
const defaults = {
  timeout: 0,
  headers: { common: { Accept: 'application/json' } }
};

function mergeConfig(config1, config2) {
  return {
    timeout: config2.timeout ?? config1.timeout,
    headers: mergeDeep(config1.headers, config2.headers)
  };
}
```

#### **2. 深度合并策略**
- **特殊字段**：`headers` 使用深度合并（Deep Merge）。
- **常规字段**：直接覆盖（如 `timeout`、`method`）。

---

### **五、取消请求机制**
#### **1. CancelToken 实现（旧版）**
- **发布-订阅模式**：通过 `source.token` 订阅取消事件。
- **流程**：调用 `source.cancel()` 触发取消。

```javascript
function CancelToken(executor) {
  let resolvePromise;
  this.promise = new Promise(resolve => {
    resolvePromise = resolve;
  });
  executor(message => {
    resolvePromise(message); // 触发取消
  });
}

// 使用示例
const source = axios.CancelToken.source();
axios.get('/url', { cancelToken: source.token });
source.cancel('Operation canceled');
```

#### **2. AbortController 支持（新版）**
- **基于 Fetch 标准**：使用 `AbortSignal` 实现。
- **浏览器兼容性**：需兼容处理。

```javascript
const controller = new AbortController();
axios.get('/url', { signal: controller.signal });
controller.abort(); // 取消请求
```

---

### **六、数据处理流程**
#### **1. 请求数据转换**
- **默认行为**：根据 `Content-Type` 自动转换：
  - `application/json` → 序列化 JSON。
  - `application/x-www-form-urlencoded` → URL 编码。

```javascript
// 转换逻辑示例
if (isObject(data) && isJSONHeader(headers)) {
  data = JSON.stringify(data);
  headers['Content-Type'] = 'application/json';
}
```

#### **2. 响应数据转换**
- **自动解析**：根据响应头 `Content-Type` 解析数据：
  - `application/json` → 自动转换为 JavaScript 对象。
  - `text/plain` → 保留原始文本。

---

### **七、错误处理机制**
#### **1. 错误分类**
- **网络错误**：无响应（如 `ECONNABORTED`）。
- **HTTP 错误**：状态码 2xx 之外的响应。
- **自定义错误**：通过 `validateStatus` 配置触发。

```javascript
// 响应状态码验证
function validateStatus(status) {
  return status >= 200 && status < 300; // 默认只接受 2xx
}

if (!validateStatus(response.status)) {
  throw new Error(`Request failed with status code ${response.status}`);
}
```

#### **2. 错误对象结构**
错误对象包含：
- `message`：错误描述。
- `config`：请求配置。
- `code`：错误码（如 `ECONNABORTED`）。
- `response`：完整的响应信息（HTTP 错误时存在）。

---

### **八、总结：Axios 核心优势**
| **特性**         | **实现原理**                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **跨平台**       | 适配器层屏蔽环境差异，统一 API 调用                                          |
| **灵活性**       | 拦截器机制允许在请求生命周期中插入自定义逻辑                                  |
| **可扩展性**     | 支持自定义适配器（如 mock 适配器）                                           |
| **高性能**       | 基于 Promise 实现异步流程，避免回调地狱                                       |
| **健壮性**       | 完善的错误分类与处理机制，提供清晰的错误信息                                  |

**源码学习建议**：  
- 重点阅读 `/lib/core/Axios.js`（核心调度逻辑）。  
- 分析 `/lib/adapters/xhr.js` 和 `/lib/adapters/http.js`（跨平台实现）。  
- 理解 `/lib/cancel/CancelToken.js`（取消请求机制）。