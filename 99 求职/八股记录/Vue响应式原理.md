
---
### 🤖 Assistant

Vue 的响应式原理主要通过 **数据劫持** 和 **依赖收集** 实现，其核心逻辑可以分为以下几个关键步骤：

---

### 一、核心流程（以 Vue 3 的 Proxy 实现为例）
1. **创建响应式对象**  
   使用 `reactive()` 或 `ref()` 包装原始数据，通过 **Proxy** 代理对象，拦截属性的 **读取（get）** 和 **修改（set）** 操作。

2. **依赖收集（Track）**  
   当组件渲染或计算属性被访问时，会执行副作用函数（如渲染函数）。在函数执行期间，**任何对响应式数据的访问** 都会触发 Proxy 的 `get` 陷阱。此时：
   - Vue 会记录当前正在运行的副作用函数（称为 `effect`）。
   - 将 `effect` 与当前访问的属性建立关联，存储在全局的 **依赖映射（WeakMap）** 中。

3. **触发更新（Trigger）**  
   当响应式数据的属性被修改时，Proxy 的 `set` 陷阱会检测到变化：
   - 根据被修改的属性，从依赖映射中找到所有关联的 `effect`。
   - 重新执行这些 `effect`（如重新渲染组件、更新计算属性）。

---

### 二、关键实现细节
#### 1. 依赖存储结构
Vue 使用 **树形结构的依赖映射** 来高效管理依赖关系：
```javascript
// 伪代码结构
WeakMap<Target, Map<Key, Set<Effect>>>
```
- **WeakMap**：键是响应式对象（避免内存泄漏），值是一个 `Map`。
- **Map**：键是对象的属性名，值是一个 `Set`。
- **Set**：存储所有与该属性关联的副作用函数（`effect`）。

#### 2. 副作用函数（Effect）
副作用函数是响应式系统的核心单元，代表需要响应数据变化的任务（如组件渲染、`watch` 回调）：
```javascript
// 伪代码：定义一个副作用函数
const effect = () => {
  currentEffect = effect;  // 标记当前运行的 effect
  renderComponent();       // 执行实际逻辑（如渲染）
  currentEffect = null;    // 重置
};
```

#### 3. Proxy 拦截逻辑
- **GET 拦截（依赖收集）**  
  ```javascript
  function get(target, key, receiver) {
    track(target, key);       // 记录当前 effect 到依赖映射
    return Reflect.get(...);  // 返回原始值
  }
  ```
- **SET 拦截（触发更新）**  
  ```javascript
  function set(target, key, value, receiver) {
    const result = Reflect.set(...);  // 修改原始值
    trigger(target, key);             // 触发关联 effect 重新执行
    return result;
  }
  ```

---

### 三、Vue 2 与 Vue 3 的差异
| 特性                | Vue 2 (Object.defineProperty)       | Vue 3 (Proxy)                     |
|---------------------|------------------------------------|-----------------------------------|
| 数据劫持方式         | 递归遍历属性逐个劫持               | 直接代理整个对象                 |
| 新增属性监听         | 需手动调用 `Vue.set`               | 自动监听                         |
| 数组监听            | 重写数组方法（如 `push`）          | 直接监听索引变化                 |
| 性能                | 初始化时递归遍历，性能较差         | 按需收集依赖，性能更优           |

---

### 四、示例：依赖收集过程
假设有以下代码：
```javascript
const state = reactive({ count: 0 });

effect(() => {
  console.log(state.count);  // 访问响应式属性
});
```

1. **首次执行 `effect`**  
   - `state.count` 的 `get` 陷阱被触发。
   - 将当前 `effect` 关联到 `state.count` 的依赖集合中。

2. **修改 `state.count`**  
   ```javascript
   state.count = 1;  // 触发 `set` 陷阱
   ```
   - 找到 `state.count` 关联的所有 `effect`。
   - 重新执行这些 `effect`，输出最新值。

---

### 五、总结
Vue 的响应式系统通过 **代理对象拦截操作** + **依赖收集/触发机制**，实现了数据变化到视图更新的自动化。其核心思想是：
- **谁用到了数据，就关注数据的变化**（依赖收集）。
- **数据变化时，通知所有关注者**（触发更新）。

这种设计使得开发者只需声明数据与视图的关系，而无需手动处理更新逻辑。