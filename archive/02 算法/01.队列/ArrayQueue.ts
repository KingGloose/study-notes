interface ListType<T> {
  isEmpty(): boolean;
  size(): number;
}

interface QueueType<T> extends ListType<T> {
  enqueue(ele: T): void;
  dequeue(): T | undefined;
  front(): T | undefined;
}

class ArrayQueue<T> implements QueueType<T> {
  protected data: T[] = [];

  isEmpty(): boolean {
    return this.data.length === 0;
  }

  size(): number {
    return this.data.length;
  }

  // 尾部添加
  enqueue(ele: T): void {
    this.data.push(ele);
  }

  // 头部删除
  dequeue(): T | undefined {
    return this.data.shift();
  }

  // 获取头部数据
  front(): T | undefined {
    return this.data[0];
  }

  // 打印
  print() {
    console.log(this.data.join(" -> "));
  }
}

// const aq = new ArrayQueue();
// aq.enqueue("ls");
// aq.enqueue("zs");
// aq.enqueue("zl");

// console.log(aq.dequeue(), aq.dequeue(), aq.dequeue());

export default ArrayQueue;
