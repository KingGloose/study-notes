import { LinkedList } from "./LinkedList";

class CircularLinkedList<T = any> extends LinkedList {
  public append(value: any): void {
    super.append(value);
    this.footer!.next = this.header;
  }

  public insertAt(value: any, position: number): void {
    super.insertAt(value, position);
    if (this.footer && (position === 0 || this.size - 1 === position)) {
      this.footer.next = this.header;
    }
  }

  public removeAt(position: number) {
    const value = super.removeAt(position);
    if (value && this.footer && (position === 0 || this.size === position)) {
      this.footer.next = this.header;
    }
    return value;
  }
}

const circularLinkedList = new CircularLinkedList();
circularLinkedList.append("a");
circularLinkedList.append("b");
circularLinkedList.append("c");
circularLinkedList.append("d");
circularLinkedList.append("a");

console.log(circularLinkedList.indexOf("e"));

circularLinkedList.traverse();

export {};
