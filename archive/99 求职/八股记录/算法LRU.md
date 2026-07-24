
---
### 🤖 Assistant

**LRU（Least Recently Used）缓存置换算法** 是一种经典的缓存淘汰策略，其核心思想是：**当缓存容量不足时，优先淘汰最久未被访问的数据**。LRU 广泛应用于数据库、操作系统、前端框架（如 Vue 的 `keep-alive` 组件）等场景。

---

### **核心原理**
1. **淘汰规则**  
   - 最新访问（新增或查询）的数据会被标记为“活跃”。
   - 当缓存容量满时，淘汰最久未被访问的数据。

2. **数据结构**  
   为了实现高效的插入、删除和查询操作，LRU 通常结合以下两种数据结构：
   - **双向链表（Doubly Linked List）**  
     按访问时间排序：链表头部是最近访问的数据，尾部是最久未访问的数据。
   - **哈希表（Hash Table）**  
     用于快速定位数据在链表中的位置，保证查询时间复杂度为 O(1)。

---

### **算法实现步骤**
#### **1. 访问数据**
- **命中缓存（数据存在）**  
  1. 通过哈希表快速定位数据节点。
  2. 将该节点移动到双向链表的头部（标记为最近访问）。

- **未命中缓存（数据不存在）**  
  1. 如果缓存已满，删除链表尾部的节点（淘汰最久未访问数据）。
  2. 将新数据插入链表头部，并更新哈希表。

#### **2. 可视化流程**
```
操作顺序: A → B → C → A → D → B → C  
缓存容量: 3

步骤分析:
1. 插入 A → 缓存: [A]
2. 插入 B → 缓存: [B → A]
3. 插入 C → 缓存: [C → B → A]
4. 访问 A → 缓存: [A → C → B]
5. 插入 D → 缓存已满，淘汰 B → 缓存: [D → A → C]
6. 访问 B → 未命中，淘汰 C → 缓存: [B → D → A]
```

---

### **JavaScript 代码实现**
```javascript
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;  // 缓存容量
    this.cache = new Map();    // 使用 Map 保持插入顺序
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    // 将访问的 key 设为最新（先删除再重新插入）
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.cache.has(key)) {
      // 已存在则更新值并设为最新
      this.cache.delete(key);
    } else if (this.cache.size >= this.capacity) {
      // 容量不足时淘汰最久未使用的键（Map 的 keys() 返回插入顺序的迭代器）
      const oldestKey = this.cache.keys().next().value;
      this.cache.delete(oldestKey);
    }
    this.cache.set(key, value);
  }
}

// 使用示例
const lru = new LRUCache(2);
lru.put(1, 'A');    // 缓存: {1='A'}
lru.put(2, 'B');    // 缓存: {1='A', 2='B'}
lru.get(1);         // 返回 'A'，缓存顺序变为 {2='B', 1='A'}
lru.put(3, 'C');    // 淘汰键 2，缓存: {1='A', 3='C'}
```

---

### **性能优化（双向链表 + 哈希表）**
对于更严格的性能场景（如高频操作），可以用双向链表和哈希表结合实现：
```javascript
class LRUNode {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class OptimizedLRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.map = new Map();          // 哈希表：key → Node
    this.head = new LRUNode();     // 虚拟头节点
    this.tail = new LRUNode();     // 虚拟尾节点
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  _moveToHead(node) {
    // 从链表中移除节点
    node.prev.next = node.next;
    node.next.prev = node.prev;
    // 插入到头部
    node.next = this.head.next;
    node.prev = this.head;
    this.head.next.prev = node;
    this.head.next = node;
  }

  get(key) {
    if (!this.map.has(key)) return -1;
    const node = this.map.get(key);
    this._moveToHead(node);  // 移动节点到头部
    return node.value;
  }

  put(key, value) {
    if (this.map.has(key)) {
      const node = this.map.get(key);
      node.value = value;
      this._moveToHead(node);
    } else {
      if (this.map.size >= this.capacity) {
        // 删除尾部节点
        const lastNode = this.tail.prev;
        this.map.delete(lastNode.key);
        lastNode.prev.next = this.tail;
        this.tail.prev = lastNode.prev;
      }
      // 创建新节点并插入头部
      const newNode = new LRUNode(key, value);
      this.map.set(key, newNode);
      newNode.next = this.head.next;
      newNode.prev = this.head;
      this.head.next.prev = newNode;
      this.head.next = newNode;
    }
  }
}
```

---

### **应用场景**
1. **浏览器缓存**：缓存静态资源（如 CSS、JS 文件）。
2. **数据库查询**：缓存高频查询结果。
3. **前端路由**：Vue 的 `keep-alive` 组件按 LRU 规则缓存页面组件。
4. **API 网关**：缓存热点请求的响应数据。

---

### **与其他算法对比**
| 算法   | 特点                                                                 | 适用场景                     |
|--------|----------------------------------------------------------------------|----------------------------|
| **LRU**  | 淘汰最久未访问数据，实现简单高效                                   | 时间局部性强的访问模式       |
| **LFU**  | 淘汰访问频率最低的数据，需维护频率计数器                           | 长期热点数据场景             |
| **FIFO** | 先进先出，不考虑访问时间                                           | 简单的顺序访问场景           |

---

### **总结**
LRU 通过 **哈希表快速定位** + **双向链表维护访问顺序**，在 O(1) 时间复杂度内完成核心操作。其关键在于将“最近使用”等价于“移动到链表头部”，而链表尾部自然成为淘汰候选。