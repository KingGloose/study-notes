// leecode: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

// method1 - 78ms
function deleteDuplicates1(head: ListNode | null): ListNode | null {
  const set = new Set();

  let curr = head;
  let prev: ListNode | null = null;
  if (!curr?.next) return head; // 只有一条数据的情况
  while (curr) {
    if (!set.has(curr.val)) {
      set.add(curr.val);
      prev = curr;
      curr = curr.next;
    } else {
      prev!.next = curr.next;
      curr = prev!.next;
    }
  }

  return head;
}

// method2 - 优化版本(因为是已经排序的链表) - 70ms
function deleteDuplicates2(head: ListNode | null): ListNode | null {
  let curr = head;
  while (curr && curr.next) {
    if (curr.val === curr.next.val) {
      curr.next = curr.next.next;
    } else {
      curr = curr.next;
    }
  }
  return head;
}
