// leecode: https://leetcode.cn/problems/add-two-numbers/description/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// method1 - 110ms
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let head = l1;
  let next = 0;

  while (l1 || l2) {
    // 01 计算数据
    const l1Val = l1 ? l1.val : 0;
    const l2Val = l2 ? l2.val : 0;
    const value = l1Val + l2Val + next;

    // 02 保留进位
    next = 0;
    if (value >= 10) next = Math.floor(value / 10);

    const newVal = value >= 10 ? value % 10 : value;
    l1!.val = newVal;

    if (!l1!.next && l2?.next) {
      l1!.next = new ListNode(0, undefined);
    }

    l1 = l1 && l1!.next;
    l2 = l2 && l2!.next;
  }

  // 为最后一个数字赋值
  if (next !== 0) {
    l1 = head;
    while (l1?.next) l1 = l1.next;
    l1!.next = new ListNode(next, undefined);
  }

  return head;
}

// 创建 listNode
function create(arr: number[]) {
  let next: ListNode | null = null;
  for (let i = arr.length - 1; i >= 0; i--) {
    const data = arr[i];
    const node: ListNode = new ListNode(data, next);
    next = node;
  }
  return next;
}
const l1 = create([9, 9, 9, 9, 9, 9, 9]);
const l2 = create([9, 9, 9, 9]);

let head = addTwoNumbers(l2, l1);
console.log(head);
let arr = [];
while (head) {
  arr.push(head.val);
  head = head.next;
}
console.log(arr);

export {};
