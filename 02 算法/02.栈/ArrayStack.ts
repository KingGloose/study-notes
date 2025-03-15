// 基于数组的栈

interface ListType<T> {
  isEmpty(): boolean;
  size(): number;
}

interface StackType<T> extends ListType<T> {
  push(ele: T): void;
  pop(): T | undefined;
  peek(): T | undefined;
}

class ArrayStack<T = any> implements StackType<T> {
  private data: T[] = [];

  push(ele: T): void {
    this.data.push(ele);
  }
  pop(): T | undefined {
    return this.data.pop();
  }
  peek(): T | undefined {
    return this.data[this.size() - 1];
  }
  isEmpty(): boolean {
    return this.data.length === 0;
  }
  size(): number {
    return this.data.length;
  }
}

// let arrayStack = new ArrayStack<string>();
// arrayStack.push("aaa");
// arrayStack.push("bbb");

// console.log(arrayStack.peek());
// console.log(arrayStack.pop(), arrayStack.pop(), arrayStack.pop());

export default ArrayStack;
