import { cbtPrint } from "hy-algokit";

export class BinaryHeap<T = any> {
  private data: T[];
  private length: number = 0;
  private isMaxHeap: boolean; // true为最大堆 / false为最小堆

  constructor(isMaxHeap = true, initArr: T[] = []) {
    this.isMaxHeap = isMaxHeap;
    this.data = initArr;
    this.length = initArr.length + 1;
    this.buildHeap(this.data);
  }

  // 获取最值 isMaxHeap 为 true 那么就是返回最大值，false 反之
  public getExtreme() {
    return this.data[0];
  }

  // 判断数组是否为空
  public isEmpty() {
    return this.length === 0;
  }

  // 修改比较最大堆和最小堆的重要参数
  private compareFn(index1: number, index2: number) {
    if (this.isMaxHeap) {
      return this.data[index1] >= this.data[index2];
    } else {
      return this.data[index1] <= this.data[index2];
    }
  }

  public print() {
    cbtPrint(this.data);
  }

  // 数据交换
  private swap(index1: number, index2: number) {
    [this.data[index1], this.data[index2]] = [this.data[index2], this.data[index1]];
  }

  // 插入数据
  public insert(value: T) {
    this.data.push(value);
    this.length++;

    let currentIndex = this.length - 1;

    while (currentIndex > 0) {
      const newIndex = this.heapifyUp(currentIndex);
      currentIndex = newIndex === currentIndex ? -1 : newIndex;
    }
  }
  // 上滤 - 输入要上滤的索引
  private heapifyUp(index: number) {
    let currentIndex = index;
    let parentIndex = Math.floor((currentIndex - 1) / 2);

    if (this.compareFn(currentIndex, parentIndex)) {
      this.swap(currentIndex, parentIndex);
      currentIndex = parentIndex;
    }

    return currentIndex;
  }

  // 删除数据 - 堆删除的特性: 只能删除最大值
  public delete() {
    // 将堆末尾元素和首部元素交换，在对尾部元素进行下滤操作
    this.swap(this.length - 1, 0);
    this.data.pop();
    this.length--;

    let currentIndex = 0;

    // 结束条件: 该元素的左子节点不存在了
    while (2 * currentIndex + 1 < this.length) {
      const newIndex = this.heapifyDown(currentIndex);
      if (newIndex === -1) break;
      currentIndex = newIndex;
    }

    return this.data[currentIndex];
  }
  // 下滤 - 输入下滤的索引
  private heapifyDown(index: number) {
    let currentIndex = index;

    let leftChildIndex = 2 * currentIndex + 1;
    let rightChildIndex = 2 * currentIndex + 2;
    let largeChildIndex = leftChildIndex;
    if (rightChildIndex < this.length && this.compareFn(rightChildIndex, leftChildIndex)) {
      largeChildIndex = rightChildIndex;
    }

    if (this.compareFn(currentIndex, largeChildIndex)) {
      return -1;
    }

    this.swap(currentIndex, largeChildIndex);
    currentIndex = largeChildIndex;

    return currentIndex;
  }

  // 原地建堆
  private buildHeap(arr: T[]) {
    const length = arr.length - 1;

    // 找到最近的叶子节点 进行下滤操作
    const start = Math.floor((length - 1) / 2);
    for (let i = start; i >= 0; i--) {
      this.heapifyDown(i);
    }
  }
}

const binaryHeap = new BinaryHeap(true, [19, 100, 36, 17, 3, 25, 1, 2, 7]);

// binaryHeap.print();
