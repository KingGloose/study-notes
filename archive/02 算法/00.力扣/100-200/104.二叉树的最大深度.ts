// leecode: https://leetcode.cn/problems/maximum-depth-of-binary-tree/

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

// [left, right]
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;

  let stack = [root];
  let height = 0;
  while (stack.length > 0) {
    let length = stack.length;
    for (let i = 0; i < length; i++) {
      const node = stack.shift();
      if (node!.left) stack.push(node!.left);
      if (node!.right) stack.push(node!.right);
    }
    height++;
  }

  return height;
}

export {};
