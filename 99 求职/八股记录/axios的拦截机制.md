
---
### 🤖 Assistant

Axios 的拦截器机制是其核心功能之一，它允许开发者在请求发送前和响应返回后插入自定义逻辑。以下从底层实现到实际应用的完整解析：
---
### 一、拦截器设计原理
Axios 的拦截器本质是一个 **Promise 中间件链**，采用 **责任链模式** 实现，具有以下特性：
1. **双向拦截**：支持请求拦截（Request Interceptors）和响应拦截（Response Interceptors）
2. **异步支持**：拦截器函数可返回 Promise 实现异步操作
3. **执行顺序控制**：请求拦截器按添加顺序 **正向执行**，响应拦截器按添加顺序 **逆向执行**
（图示：请求拦截器A → 请求拦截器B → 发送请求 → 响应拦截器C → 响应拦截器D）
---
### 二、拦截器实现源码解析
#### 1. 存储结构
```javascript
// Axios 构造函数内部
function Axios() {
  this.interceptors = {
    request: new InterceptorManager(), // 请求拦截器管理器
    response: new InterceptorManager() // 响应拦截器管理器
  };
}
// 拦截器管理器类
function InterceptorManager() {
  this.handlers = []; // 存储拦截器对象 { fulfilled, rejected }
}
// 添加拦截器
InterceptorManager.prototype.use = function(fulfilled, rejected) {
  this.handlers.push({ fulfilled, rejected });
  return this.handlers.length - 1; // 返回拦截器ID用于移除
};
```
#### 2. 链式执行逻辑
```javascript
// 核心调度代码 (简化版)
Axios.prototype.request = function(config) {
  // 初始化执行链
  const chain = [dispatchRequest, undefined]; // 核心请求方法
  // 插入请求拦截器
  this.interceptors.request.forEach(function unshiftRequestInterceptors(interceptor) {
    chain.unshift(interceptor.fulfilled, interceptor.rejected);
  });
  // 插入响应拦截器
  this.interceptors.response.forEach(function pushResponseInterceptors(interceptor) {
    chain.push(interceptor.fulfilled, interceptor.rejected);
  });
  // 构建Promise链
  let promise = Promise.resolve(config);
  while (chain.length) {
    promise = promise.then(chain.shift(), chain.shift());
  }
  return promise;
};
```
---
### 三、拦截器的完整使用方式
#### 1. 基础用法
```javascript
// 添加请求拦截器
axios.interceptors.request.use(
  config => {
    console.log('请求拦截器1');
    return config; // 必须返回处理后的config
  },
  error => {
    return Promise.reject(error); // 处理错误
  }
);
// 添加响应拦截器
axios.interceptors.response.use(
  response => {
    console.log('响应拦截器1');
    return response; // 必须返回处理后的response
  },
  error => {
    return Promise.reject(error); // 处理错误
  }
);
```
#### 2. 执行顺序控制
```javascript
// 添加顺序：
// 请求拦截器：A → B → C
// 响应拦截器：X → Y → Z
// 实际执行顺序：
// 请求阶段：C → B → A → 发送请求
// 响应阶段：X → Y → Z → 接收响应
```
---
### 四、高级应用场景
#### 1. 身份认证（自动添加Token）
```javascript
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```
#### 2. 请求重试机制
```javascript
axios.interceptors.response.use(null, error => {
  const config = error.config;
  if (!config || !config.retry) return Promise.reject(error);
  config.__retryCount = config.__retryCount || 0;
  if (config.__retryCount >= config.retry) {
    return Promise.reject(error);
  }
  config.__retryCount += 1;
  return new Promise(resolve => {
    setTimeout(() => resolve(axios(config)), config.retryDelay || 1000);
  });
});
// 使用示例
axios.get('/api', { retry: 3, retryDelay: 2000 });
```
#### 3. 全局Loading状态管理
```javascript
let activeRequests = 0;
axios.interceptors.request.use(config => {
  activeRequests++;
  if (activeRequests === 1) showLoading();
  return config;
});
axios.interceptors.response.use(
  response => {
    activeRequests--;
    if (activeRequests === 0) hideLoading();
    return response;
  },
  error => {
    activeRequests--;
    if (activeRequests === 0) hideLoading();
    return Promise.reject(error);
  }
);
```
---
### 五、关键注意事项
#### 1. 必须返回处理对象
- 请求拦截器必须返回 `config` 对象
- 响应拦截器必须返回 `response` 对象
- 错误拦截器必须返回 `Promise.reject(error)`
#### 2. 异步拦截处理
```javascript
// 异步请求拦截器示例
axios.interceptors.request.use(async config => {
  const newToken = await refreshToken();
  config.headers.Authorization = `Bearer ${newToken}`;
  return config;
});
```
#### 3. 拦截器移除
```javascript
const myInterceptor = axios.interceptors.request.use(config => {/*...*/});
axios.interceptors.request.eject(myInterceptor); // 移除拦截器
```
#### 4. 错误冒泡机制
- 请求拦截器抛出错误 → 直接进入响应错误拦截器
- 响应拦截器抛出错误 → 传递给下一个响应错误拦截器
---
### 六、常见问题解决方案
#### 1. 拦截器导致响应数据格式变化
```javascript
// 解决方案：保持响应结构一致性
axios.interceptors.response.use(response => {
  // 不要直接返回 response.data，保持完整响应结构
  return {
    ...response,
    data: transform(response.data) // 数据处理
  };
});
```
#### 2. 多个实例的独立拦截器
```javascript
// 创建独立实例
const instance = axios.create();
instance.interceptors.request.use(/* 独立拦截器 */);
```
#### 3. 拦截器与取消请求的配合
```javascript
// 在拦截器中处理取消逻辑
axios.interceptors.request.use(config => {
  if (config.cancelToken) {
    config.cancelToken.promise.then(cancel => {
      // 执行取消操作
    });
  }
  return config;
});
```
---
### 七、性能优化建议
1. **避免阻塞性操作**：不要在拦截器中执行耗时同步操作
2. **合理使用异步**：异步拦截器要确保错误正确处理
3. **及时清理拦截器**：对于临时拦截器使用后及时移除
4. **优先级控制**：通过调整添加顺序优化关键拦截逻辑
---
### 八、与 Fetch API 的拦截机制对比
| **特性**         | Axios 拦截器                  | Fetch 拦截方案               |
|------------------|-----------------------------|----------------------------|
| 原生支持         | ✅ 内置                      | ❌ 需自行封装               |
| 错误处理         | ✅ 统一错误流                | ❌ 需手动处理               |
| 异步支持         | ✅ Promise 链               | ✅ 但需自行管理            |
| 执行顺序控制     | ✅ 明确的正反序控制          | ❌ 依赖实现方式            |
| 实例隔离         | ✅ 多实例独立配置            | ❌ 全局影响                |
---
通过深入理解 Axios 拦截器机制，开发者可以实现更精细的请求流程控制，建议结合项目需求设计合理的拦截策略，同时注意避免过度使用导致代码复杂度增加。