// 2024.4.14 - https://leetcode.cn/problems/design-linked-list/description/
// 下面是单链表的设计与实现

class Node<T> {
  value: T;
  next: Node<T> | null = null;

  constructor(value: T) {
    this.value = value;
  }
}

export class LinkedList<T = any> {
  // 头指针
  protected header: Node<T> | null = null;
  // 尾指针
  protected footer: Node<T> | null = null;
  // 链表长度
  protected size: number = 0;

  get length(): number {
    return this.size;
  }

  // 遍历链表
  protected getNode(position: number): Node<T> | null {
    let index = 0;
    let current = this.header;

    while (index++ < position && current) {
      current = current!.next;
    }

    return current;
  }

  // 检查链表越界问题
  protected checkNodePosition(position: number) {
    if (position < 0 || position > this.size) {
      throw new Error("position out of bounds");
    }
  }

  // 判断节点是否为最后一个节点
  protected isFooterNode(node: Node<T>) {
    return node === this.footer;
  }

  // 查看所有数据
  public traverse() {
    let index = 0;
    let arr: T[] = [];

    let current = this.header;
    while (index++ < this.size && current) {
      arr.push(current!.value);
      current = current?.next;

      // 循环链表打印
      if (current === this.header) {
        arr.push(`circular(${this.footer?.next?.value})` as any);
        break;
      }
    }

    console.log(arr.join(" -> "));
  }

  // 添加数据
  public append(value: T) {
    const node = new Node(value);

    if (this.size === 0) {
      this.header = node;
    } else {
      this.footer!.next = node;
    }
    this.footer = node;

    this.size++;
  }

  // 插入数据
  public insertAt(value: T, position: number) {
    this.checkNodePosition(position);

    const node = new Node(value);

    if (position === 0) {
      if (this.size !== 0) {
        node.next = this.header;
      } else {
        this.footer = node;
      }
      this.header = node;
    } else {
      const previous = this.getNode(position - 1);
      const current = previous!.next;

      previous!.next = node;
      node.next = current;

      if (position === this.size) {
        this.footer = node;
      }
    }

    this.size++;
  }

  // 删除数据
  public removeAt(position: number): T | null {
    this.checkNodePosition(position);

    let current = this.header;
    if (position === 0) {
      this.header = current!.next;

      if (this.size === 1) {
        this.footer = null;
      }
    } else {
      const previous = this.getNode(position - 1);
      current = previous!.next;

      previous!.next = current!.next;

      if (position === this.size - 1) {
        this.footer = previous;
      }
    }

    this.size--;

    return current?.value ?? null;
  }

  // 获取数据
  public getAt(position: number) {
    this.checkNodePosition(position);

    const current = this.getNode(position);
    return current?.value;
  }

  // 更新数据
  public updateAt(value: T, position: number) {
    this.checkNodePosition(position);

    const current = this.getNode(position);
    current!.value = value;
  }

  // 获取索引
  public indexOf(value: T) {
    let index = 0;
    let current = this.header;

    while (current && index < this.size) {
      if (current?.value === value) return index;

      current = current!.next;
      index++;
    }

    return -1;
  }

  // 删除元素
  public remove(value: T) {
    const index = this.indexOf(value);
    return this.removeAt(index);
  }

  // 判断是否为空
  public isEmpty() {
    return this.size === 0;
  }

  // 反转链表
  public reserve() {
    let prevNode: Node<T> | null = null;
    let currNode = this.header;
    let nextNode = currNode?.next;

    while (currNode) {
      currNode.next = prevNode;

      prevNode = currNode;
      currNode = nextNode!;
      nextNode = nextNode?.next;
    }

    this.footer = this.header;
    this.header = prevNode!;
  }
}

const linkedList = new LinkedList();
linkedList.append(1);
linkedList.append(2);
linkedList.append(3);
linkedList.append(5);
linkedList.append(7);

linkedList.removeAt(4);

// console.log(linkedList.remove(3));

// linkedList.reserve();

// linkedList.insertAt(6, 4);

// linkedList.removeAt(0);

// console.log(linkedList.getAt(0));

// linkedList.updateAt("a", 0);

// console.log(linkedList.indexOf(0));

// linkedList.remove(3);

// linkedList.traverse();

export {};
