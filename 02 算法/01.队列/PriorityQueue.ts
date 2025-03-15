import { BinaryHeap } from "../08.堆/BinaryHeap";

class PriorityNode<T> {
  value: T;
  priority: number;

  constructor(value: T, priority: number) {
    this.value = value;
    this.priority = priority;
  }

  valueOf() {
    return this.priority;
  }
}

// 优先级队列 - 基于堆
class PriorityQueue<T = any> {
  private heap = new BinaryHeap<T>();

  // 插入
  enqueue(value: T, priority: number) {
    const node = new PriorityNode<T>(value, priority);
    this.heap.insert<PriorityNode<T>>(node);
  }

  // 删除
  dequeue() {
    this.heap.delete();
  }
}

export {};
