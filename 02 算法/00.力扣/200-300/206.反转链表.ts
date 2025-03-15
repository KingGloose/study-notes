class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// method1 - 迭代 - 66ms
function reverseList(head: ListNode | null): ListNode | null {
  let prevNode: ListNode | null = null;
  let currNode = head;
  let nextNode = currNode?.next;

  while (currNode) {
    currNode.next = prevNode;

    prevNode = currNode;
    currNode = nextNode!;
    nextNode = nextNode?.next;
  }

  return prevNode;
}

// method2 - 栈结构 - 75ms
function reverseList1(head: ListNode | null): ListNode | null {
  const stack: any[] = [];

  let current = head;
  while (current) {
    stack.push(current.val);
    current = current.next;
  }

  let newHead = head;
  while (stack.length) {
    const val = stack.pop();
    newHead!.val = val;
    newHead = newHead!.next;
  }

  return head;
}

// method3 - 递归 -
