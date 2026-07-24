// leecode: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/**
 Do not return anything, modify root in-place instead. 
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// method1
function flatten(root: TreeNode | null): void {
  if (!root) return;

  const stack = [root];
  let prev: TreeNode | null = null;

  while (stack.length > 0) {
    let current = stack.pop()!;

    if (prev) {
      prev!.right = current;
      prev.left = null;
    }

    if (current?.right) stack.push(current.right);
    if (current?.left) stack.push(current.left);

    prev = current;
  }
}

export {};
