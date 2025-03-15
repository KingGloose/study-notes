// leecode: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// method1 - 63ms
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let slow = head;
  let fast = head;

  // 快慢指针保持 n 格距离
  for (let i = 0; i < n; i++) fast = fast!.next;

  // 如果此时 fast 指针为 null 那么就是删除第一个
  if (!fast) return (head = head!.next);

  // 否则就依次进行移动
  while (fast.next) {
    slow = slow!.next;
    fast = fast.next;
  }

  slow!.next = slow!.next!.next;

  return head;
}

export {};
