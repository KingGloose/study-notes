import { LinkedList } from "./LinkedList";

class Node<T> {
  value: T;
  next: Node<T> | null = null;

  constructor(value: T) {
    this.value = value;
  }
}

class DoublyNode<T> extends Node<T> {
  prev: DoublyNode<T> | null = null;
  next: DoublyNode<T> | null = null;
}
class DoublyLinkedList<T = any> extends LinkedList {
  // 头指针
  protected header: DoublyNode<T> | null = null;
  // 尾指针
  protected footer: DoublyNode<T> | null = null;

  // 从尾部添加元素
  public append(value: any): void {
    const node = new DoublyNode(value);

    if (this.size === 0) {
      this.header = node;
    } else {
      this.footer!.next = node;
      node.prev = this.footer;
    }
    this.footer = node;

    this.size++;
  }

  // 从头部添加元素
  public prepend(value: T) {
    const node = new DoublyNode(value);

    if (!this.header || this.size === 0) {
      this.header = node;
      this.footer = node;
    } else {
      node.next = this.header;
      this.header!.prev = node;
      this.header = node;
    }
    this.size++;
  }

  // 从尾部遍历所有元素
  public postTraverse() {
    let index = 0;
    let arr: T[] = [];

    let current = this.footer;
    while (index++ < this.size && current) {
      arr.push(current!.value);
      current = current?.prev;
    }

    console.log(arr.join(" -> "));
  }

  // 根据索引插入方法
  public insertAt(value: T, position: number) {
    super.checkNodePosition(position);

    if (position === 0) {
      this.prepend(value);
    } else if (position === this.size) {
      this.append(value);
    } else {
      const node = new DoublyNode(value);
      const previous = this.getNode(position - 1) as DoublyNode<T>;
      const current = previous!.next;

      previous!.next = node;
      node.next = current;
      current!.prev = node;
      node.prev = previous;

      this.size++;
    }
  }

  // 根据索引删除元素
  public removeAt(position: number) {
    super.checkNodePosition(position);

    let current = this.header;
    if (position === 0) {
      if (this.size === 1) {
        this.footer = null;
        this.header = null;
      } else {
        this.header = this.header!.next;
        this.header!.prev = null;
      }
    } else if (position === this.size - 1) {
      current = this.footer;
      this.footer = this.footer!.prev;
      this.footer!.next = null;
    } else {
      current = this.getNode(position) as DoublyNode<T>;
      current.next!.prev = current.prev;
      current.prev!.next = current.next;
    }

    this.size--;

    return current?.value ?? null;
  }
}

const doublyLinkedList = new DoublyLinkedList();
doublyLinkedList.append("a");
doublyLinkedList.append("b");
doublyLinkedList.append("c");
doublyLinkedList.append("d");
doublyLinkedList.append("e");

// doublyLinkedList.prepend("f");
doublyLinkedList.removeAt(4);

doublyLinkedList.traverse();
// doublyLinkedList.postTraverse();

export {};
