
---
### 🤖 Assistant

要实现一个符合 **Promises/A+ 规范** 的 `Promise`，需要深入理解其核心机制。以下是分步骤的详细实现过程，包含关键代码和原理说明：

---

### **一、基础框架：状态管理与构造函数**
#### 1. 定义三种状态
```javascript
const PENDING = 'pending'
const FULFILLED = 'fulfilled'
const REJECTED = 'rejected'
```

#### 2. 构造函数
```javascript
class MyPromise {
  constructor(executor) {
    this.state = PENDING   // 初始状态
    this.value = undefined // 成功值
    this.reason = undefined // 失败原因
    this.onFulfilledCallbacks = [] // 成功回调队列
    this.onRejectedCallbacks = []  // 失败回调队列

    // 定义 resolve 和 reject 函数
    const resolve = (value) => {
      if (this.state === PENDING) {
        this.state = FULFILLED
        this.value = value
        this.onFulfilledCallbacks.forEach(fn => fn()) // 触发回调
      }
    }

    const reject = (reason) => {
      if (this.state === PENDING) {
        this.state = REJECTED
        this.reason = reason
        this.onRejectedCallbacks.forEach(fn => fn()) // 触发回调
      }
    }

    // 执行 executor
    try {
      executor(resolve, reject) // 同步执行
    } catch (err) {
      reject(err) // 捕获同步错误
    }
  }
}
```

---

### **二、实现 `then` 方法（核心）**
#### 1. 方法签名
```javascript
then(onFulfilled, onRejected) {
  // 实现值穿透（符合 Promises/A+ 规范）
  onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : value => value
  onRejected = typeof onRejected === 'function' ? onRejected : reason => { throw reason }

  // 返回新 Promise 以实现链式调用
  const promise2 = new MyPromise((resolve, reject) => {
    // 统一处理回调
    const handleCallback = (callback, value) => {
      setTimeout(() => { // 确保异步执行（规范要求）
        try {
          const x = callback(value)
          resolvePromise(promise2, x, resolve, reject)
        } catch (err) {
          reject(err)
        }
      }, 0)
    }

    if (this.state === FULFILLED) {
      handleCallback(onFulfilled, this.value)
    } else if (this.state === REJECTED) {
      handleCallback(onRejected, this.reason)
    } else { // PENDING 状态时暂存回调
      this.onFulfilledCallbacks.push(() => {
        handleCallback(onFulfilled, this.value)
      })
      this.onRejectedCallbacks.push(() => {
        handleCallback(onRejected, this.reason)
      })
    }
  })

  return promise2
}
```

#### 2. 解析回调返回值（关键）
```javascript
function resolvePromise(promise2, x, resolve, reject) {
  if (promise2 === x) { // 禁止循环引用
    return reject(new TypeError('Chaining cycle detected'))
  }

  // 处理 thenable 对象或 Promise
  if ((typeof x === 'object' && x !== null) || typeof x === 'function') {
    let then
    try {
      then = x.then // 可能抛出错误（如属性访问器）
    } catch (err) {
      return reject(err)
    }

    if (typeof then === 'function') {
      let called = false // 防止多次调用
      try {
        then.call(
          x,
          y => {
            if (called) return
            called = true
            resolvePromise(promise2, y, resolve, reject) // 递归解析
          },
          r => {
            if (called) return
            called = true
            reject(r)
          }
        )
      } catch (err) {
        if (!called) reject(err)
      }
    } else {
      resolve(x) // 普通对象
    }
  } else {
    resolve(x) // 基础类型值
  }
}
```

---

### **三、实现其他关键方法**
#### 1. `catch` 方法
```javascript
catch(onRejected) {
  return this.then(null, onRejected)
}
```

#### 2. `finally` 方法
```javascript
finally(callback) {
  return this.then(
    value => MyPromise.resolve(callback()).then(() => value),
    reason => MyPromise.resolve(callback()).then(() => { throw reason })
  )
}
```

#### 3. 静态方法
```javascript
static resolve(value) {
  if (value instanceof MyPromise) return value
  return new MyPromise(resolve => resolve(value))
}

static reject(reason) {
  return new MyPromise((_, reject) => reject(reason))
}

static all(promises) {
  return new MyPromise((resolve, reject) => {
    const result = []
    let count = 0
    promises.forEach((p, i) => {
      MyPromise.resolve(p).then(
        value => {
          result[i] = value
          if (++count === promises.length) resolve(result)
        },
        reject // 任意一个失败则整体失败
      )
    })
  })
}

static race(promises) {
  return new MyPromise((resolve, reject) => {
    promises.forEach(p => {
      MyPromise.resolve(p).then(resolve, reject)
    })
  })
}
```

---

### **四、关键机制解析**
| **机制**            | **实现原理**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **状态不可逆**      | 通过 `state` 变量控制，只能在 `pending` 时转换状态                          |
| **链式调用**        | `then` 返回新的 Promise，形成调用链                                        |
| **异步执行**        | 使用 `setTimeout` 模拟微任务（原生 Promise 使用微任务队列）                |
| **值穿透**          | 当 `then` 的参数非函数时，创建默认函数传递值                               |
| **错误冒泡**        | 在 `then` 和 `resolvePromise` 中捕获错误并传递给下一个 Promise             |
| **处理 thenable**   | 递归解析可能返回的 Promise 或 thenable 对象                                |

---

### **五、测试用例验证**
```javascript
// 测试链式调用
new MyPromise((resolve) => resolve(1))
  .then(val => val + 2)
  .then(val => console.log(val)) // 输出 3

// 测试异步
new MyPromise((resolve) => setTimeout(() => resolve('async'), 100))
  .then(val => console.log(val)) // 1秒后输出 "async"

// 测试错误处理
new MyPromise((_, reject) => reject('error'))
  .catch(err => console.log(err)) // 输出 "error"

// 测试静态方法
MyPromise.all([
  MyPromise.resolve(1),
  new MyPromise(resolve => setTimeout(() => resolve(2), 100))
]).then(values => console.log(values)) // [1, 2]
```

---

### **六、与原生的差异**
| **特性**              | **原生 Promise**               | **此实现**                      |
|-----------------------|--------------------------------|---------------------------------|
| 微任务队列            | 使用引擎微任务（如 MutationObserver） | 用 `setTimeout` 模拟宏任务      |
| 性能                  | 更高                           | 较低（因宏任务延迟）            |
| 完整规范支持          | 完全符合 Promises/A+           | 简化实现，部分边界情况未处理    |

---

### **七、实现总结**
1. **状态机模型**：通过状态转移控制 Promise 生命周期
2. **回调队列**：管理异步回调的执行顺序
3. **递归解析**：处理嵌套 Promise 和 thenable 对象
4. **错误冒泡**：自动将错误传递到链式调用的末端
5. **异步调度**：模拟微任务机制（实际开发中可用 `queueMicrotask` 改进）

通过这个实现，可以深入理解 Promise 的 **链式调用**、**异步处理** 和 **错误传播** 机制。实际应用中建议直接使用原生 Promise，此实现主要用于学习原理。