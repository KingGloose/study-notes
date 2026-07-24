import ArrayQueue from "./ArrayQueue";

// 双端队列
class ArrayDeque<T = any> extends ArrayQueue<T> {
  // 尾部删除
  deleteBack() {
    return this.data.pop();
  }

  // 头部添加
  addFront(ele: T) {
    this.data.unshift(ele);
  }
}

const arr = [15, 20, 40, 2, 1];
const arrayDeque = new ArrayDeque();
for (const item of arr) {
  arrayDeque.addFront(item);
}
arrayDeque.deleteBack();

arrayDeque.print();
