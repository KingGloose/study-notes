// 2024.4.12 - https://leetcode.cn/problems/merge-two-sorted-lists/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// method1 - 68ms
function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  let head = new ListNode();
  let last = head;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      last.next = list1;
      list1.next = list1;
    } else {
      last.next = list2;
      list2.next = list2;
    }

    last = last.next; // 设置完 next 之后，默认让 last 指向表尾
  }

  last.next = list1 ? list1 : list2;

  return head.next;
}

export {};
