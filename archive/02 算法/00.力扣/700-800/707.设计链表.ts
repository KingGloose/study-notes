class Node<T> {
  value: T;
  next: Node<T> | null = null;

  constructor(value: T) {
    this.value = value;
  }
}

class LinkedList<T = any> {
  private header: Node<T> | null = null; // 头指针

  private footer: Node<T> | null = null; // 尾指针

  private size: number = 0; // 链表长度
  get length(): number {
    return this.size;
  }

  // 遍历链表
  private getNode(position: number): Node<T> | null {
    let index = 0;
    let current = this.header;

    while (index++ < position && current) {
      current = current!.next;
    }

    return current;
  }

  // 检查链表越界问题
  private checkNodePosition(position: number) {
    if (position < 0 || position > this.size) {
      throw new Error("position out of bounds");
    }
  }

  // 查看所有数据
  traverse() {
    let index = 0;
    let arr: T[] = [];

    let current = this.header;
    while (index++ < this.size && current) {
      arr.push(current!.value);
      current = current?.next;
    }

    console.log(arr.join(" -> "));
  }

  // 添加数据
  append(value: T) {
    const node = new Node(value);

    if (this.size === 0) {
      this.header = node;
      this.footer = this.header;
    } else {
      this.footer!.next = node;
      this.footer = node;
    }

    this.size++;
  }

  // 插入数据
  insertAt(value: T, position: number) {
    this.checkNodePosition(position);

    const node = new Node(value);

    if (position === 0) {
      node.next = this.header;
      this.header = node;
    } else {
      const previous = this.getNode(position - 1);
      const current = previous!.next;

      previous!.next = node;
      node.next = current;
    }

    this.size++;
  }

  // 删除数据
  removeAt(position: number) {
    this.checkNodePosition(position);

    if (position === 0) {
      this.header = this.header!.next;
    } else {
      const previous = this.getNode(position - 1);
      const current = previous!.next;

      previous!.next = current!.next;
    }

    this.size--;
  }

  // 获取数据
  getAt(position: number) {
    this.checkNodePosition(position);

    const current = this.getNode(position);
    return current?.value;
  }

  // 更新数据
  updateAt(value: T, position: number) {
    this.checkNodePosition(position);

    const current = this.getNode(position);
    current!.value = value;
  }

  // 获取索引
  indexOf(value: T) {
    let index = 0;
    let current = this.header;

    while (current) {
      if (current?.value === value) return index;

      current = current!.next;
      index++;
    }

    return -1;
  }

  // 删除元素
  remove(value: T) {
    const index = this.indexOf(value);
    this.removeAt(index);
  }

  // 判断是否为空
  isEmpty() {
    return this.size === 0;
  }
}

const linkedList = new LinkedList();
linkedList.append(1);
linkedList.append(2);
linkedList.append(3);
linkedList.append(5);

// linkedList.insertAt(6, 4);

// linkedList.removeAt(0);

// console.log(linkedList.getAt(0));

// linkedList.updateAt("a", 0);

// console.log(linkedList.indexOf(0));

linkedList.remove(3);

linkedList.traverse();

export {};
