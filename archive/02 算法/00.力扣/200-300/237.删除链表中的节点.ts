// 2024.4.14 https://leetcode.cn/problems/delete-node-in-a-linked-list/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function deleteNode(node: ListNode | null): void {
  node!.val = node!.next!.val;
  node!.next = node!.next!.next;
}

export {};
