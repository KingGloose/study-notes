// leecode: https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/description/

// method1 - 使用2个栈模拟队列
class CQueue {
  one: number[] = [];
  two: number[] = [];

  constructor() {}

  appendTail(value: number): void {
    this.one.push(value);
  }

  deleteHead(): number {
    if (this.two.length > 0) {
      return this.two.pop()!;
    } else if (this.one.length > 0) {
      while (this.one.length > 0) {
        const data = this.one.pop()!;
        this.two.push(data);
      }
      return this.two.pop()!;
    } else {
      return -1;
    }
  }
}
