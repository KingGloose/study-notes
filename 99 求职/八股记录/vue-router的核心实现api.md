
---
### 🤖 Assistant

Vue Router 的核心 API 可以分为以下几个关键部分，每个部分在路由系统中承担不同的职责：

---

### 一、**路由实例创建与配置**
#### 1. `createRouter(options: RouterOptions)`
- **作用**：创建路由实例
- **核心参数**：
  ```javascript
  {
    history: createWebHistory(), // 或 createWebHashHistory()
    routes: [] // 路由配置数组
  }
  ```
- **实现原理**：内部初始化路由匹配器（matcher）、导航守卫队列、历史记录管理器

#### 2. **路由配置对象**
```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [/* 嵌套路由 */],
    name: 'user',
    redirect: '/home',
    meta: { requiresAuth: true },
    beforeEnter: (to, from) => { /* 路由独享守卫 */ }
  }
]
```

---

### 二、**路由实例核心 API**
#### 1. **属性**
- `router.currentRoute`：当前路由对象（响应式）
- `router.options`：原始配置信息

#### 2. **方法**
- `router.addRoute(parentName?: string, route: RouteRecordRaw)`  
  **作用**：动态添加路由  
  **实现原理**：修改内部路由表，重建路由匹配器

- `router.beforeEach(guard)`  
  `router.afterEach(guard)`  
  **作用**：全局导航守卫  
  **实现原理**：维护守卫队列，按顺序执行

- `router.push(to)` / `router.replace(to)`  
  **作用**：编程式导航  
  **实现原理**：调用 history API（如 `history.pushState`）

- `router.resolve(to)`  
  **作用**：解析目标路由位置  
  **实现原理**：通过路由匹配器计算完整路由对象

---

### 三、**路由组件注入 API**
#### 1. `$router`
- 访问路由实例
- **实现原理**：通过 Vue 的 `provide/inject` 机制注入

#### 2. `$route`
- 访问当前路由信息（响应式）
- **实现原理**：通过 `Vue.util.defineReactive` 实现响应式

---

### 四、**路由匹配核心 API**
#### 1. `createWebHistory(base?: string)`
- **作用**：创建 HTML5 History 模式路由
- **实现原理**：基于 `window.history` API

#### 2. `createWebHashHistory()`
- **作用**：创建 Hash 模式路由
- **实现原理**：监听 `hashchange` 事件

---

### 五、**导航守卫体系**
| 类型                | API 形式                          | 执行时机                  |
|---------------------|----------------------------------|-------------------------|
| 全局前置守卫         | `router.beforeEach`             | 导航触发时最早执行        |
| 路由独享守卫         | `beforeEnter`                   | 进入特定路由前            |
| 组件内守卫           | `beforeRouteEnter`              | 组件被复用时              |
| 全局解析守卫         | `router.beforeResolve`          | 所有组件守卫和异步组件解析后 |
| 全局后置钩子         | `router.afterEach`              | 导航完成后               |

---

### 六、**动态路由 API**
#### 1. `router.addRoute()`
- 动态添加路由规则
- **实现原理**：内部维护 `matcher` 对象，调用 `addRoute` 后重建匹配器

#### 2. `router.removeRoute(name)`
- 动态移除路由

---

### 七、**组合式 API**
#### 1. `useRouter()`
```javascript
import { useRouter } from 'vue-router'
const router = useRouter()
```

#### 2. `useRoute()`
```javascript
import { useRoute } from 'vue-router'
const route = useRoute() // 响应式路由对象
```

---

### 八、**路由懒加载实现**
```javascript
const User = () => import('./User.vue')
// 会被编译为 webpack 的代码分割
```

---

### 核心实现机制
1. **路由匹配**：基于路径解析算法（Path-to-RegExp）
2. **响应式更新**：通过 Vue 响应式系统追踪 `$route` 变化
3. **导航流程控制**：
   ```mermaid
   graph TD
   A[导航触发] --> B[调用离开守卫]
   B --> C[调用全局 beforeEach]
   C --> D[调用路由 beforeEnter]
   D --> E[调用组件 beforeRouteEnter]
   E --> F[解析异步组件]
   F --> G[调用全局 beforeResolve]
   G --> H[导航确认]
   H --> I[更新路由]
   I --> J[调用 afterEach]
   ```

---

### 特殊场景 API
- `router.onError(handler)`：捕获导航错误
- `router.isReady()`：等待路由初始化完成
- `router.forward()` / `router.back()`：历史记录操作

这些 API 共同构成了 Vue Router 的核心功能体系，开发者通过这些接口可以实现复杂的路由控制逻辑。理解这些 API 的设计原理（如基于 Promise 的导航守卫链式调用、响应式路由状态管理等），能更好地进行路由层面的性能优化和问题排查。


---
### 🤖 Assistant

Vue Router 的核心 API 可以分为以下几个关键部分，每个部分在路由系统中承担不同的职责：

---

### 一、**路由实例创建与配置**
#### 1. `createRouter(options: RouterOptions)`
- **作用**：创建路由实例
- **核心参数**：
  ```javascript
  {
    history: createWebHistory(), // 或 createWebHashHistory()
    routes: [] // 路由配置数组
  }
  ```
- **实现原理**：内部初始化路由匹配器（matcher）、导航守卫队列、历史记录管理器

#### 2. **路由配置对象**
```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [/* 嵌套路由 */],
    name: 'user',
    redirect: '/home',
    meta: { requiresAuth: true },
    beforeEnter: (to, from) => { /* 路由独享守卫 */ }
  }
]
```

---

### 二、**路由实例核心 API**
#### 1. **属性**
- `router.currentRoute`：当前路由对象（响应式）
- `router.options`：原始配置信息

#### 2. **方法**
- `router.addRoute(parentName?: string, route: RouteRecordRaw)`  
  **作用**：动态添加路由  
  **实现原理**：修改内部路由表，重建路由匹配器

- `router.beforeEach(guard)`  
  `router.afterEach(guard)`  
  **作用**：全局导航守卫  
  **实现原理**：维护守卫队列，按顺序执行

- `router.push(to)` / `router.replace(to)`  
  **作用**：编程式导航  
  **实现原理**：调用 history API（如 `history.pushState`）

- `router.resolve(to)`  
  **作用**：解析目标路由位置  
  **实现原理**：通过路由匹配器计算完整路由对象

---

### 三、**路由组件注入 API**
#### 1. `$router`
- 访问路由实例
- **实现原理**：通过 Vue 的 `provide/inject` 机制注入

#### 2. `$route`
- 访问当前路由信息（响应式）
- **实现原理**：通过 `Vue.util.defineReactive` 实现响应式

---

### 四、**路由匹配核心 API**
#### 1. `createWebHistory(base?: string)`
- **作用**：创建 HTML5 History 模式路由
- **实现原理**：基于 `window.history` API

#### 2. `createWebHashHistory()`
- **作用**：创建 Hash 模式路由
- **实现原理**：监听 `hashchange` 事件

---

### 五、**导航守卫体系**
| 类型                | API 形式                          | 执行时机                  |
|---------------------|----------------------------------|-------------------------|
| 全局前置守卫         | `router.beforeEach`             | 导航触发时最早执行        |
| 路由独享守卫         | `beforeEnter`                   | 进入特定路由前            |
| 组件内守卫           | `beforeRouteEnter`              | 组件被复用时              |
| 全局解析守卫         | `router.beforeResolve`          | 所有组件守卫和异步组件解析后 |
| 全局后置钩子         | `router.afterEach`              | 导航完成后               |

---

### 六、**动态路由 API**
#### 1. `router.addRoute()`
- 动态添加路由规则
- **实现原理**：内部维护 `matcher` 对象，调用 `addRoute` 后重建匹配器

#### 2. `router.removeRoute(name)`
- 动态移除路由

---

### 七、**组合式 API**
#### 1. `useRouter()`
```javascript
import { useRouter } from 'vue-router'
const router = useRouter()
```

#### 2. `useRoute()`
```javascript
import { useRoute } from 'vue-router'
const route = useRoute() // 响应式路由对象
```

---

### 八、**路由懒加载实现**
```javascript
const User = () => import('./User.vue')
// 会被编译为 webpack 的代码分割
```

---

### 核心实现机制
1. **路由匹配**：基于路径解析算法（Path-to-RegExp）
2. **响应式更新**：通过 Vue 响应式系统追踪 `$route` 变化
3. **导航流程控制**：
   ```mermaid
   graph TD
   A[导航触发] --> B[调用离开守卫]
   B --> C[调用全局 beforeEach]
   C --> D[调用路由 beforeEnter]
   D --> E[调用组件 beforeRouteEnter]
   E --> F[解析异步组件]
   F --> G[调用全局 beforeResolve]
   G --> H[导航确认]
   H --> I[更新路由]
   I --> J[调用 afterEach]
   ```

---

### 特殊场景 API
- `router.onError(handler)`：捕获导航错误
- `router.isReady()`：等待路由初始化完成
- `router.forward()` / `router.back()`：历史记录操作

这些 API 共同构成了 Vue Router 的核心功能体系，开发者通过这些接口可以实现复杂的路由控制逻辑。理解这些 API 的设计原理（如基于 Promise 的导航守卫链式调用、响应式路由状态管理等），能更好地进行路由层面的性能优化和问题排查。