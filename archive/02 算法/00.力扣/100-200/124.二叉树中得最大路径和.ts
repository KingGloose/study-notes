// leecode: https://leetcode.cn/problems/binary-tree-maximum-path-sum/

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

// method1 - 72ms
function maxPathSum(root: TreeNode | null): number {
  let max = -Infinity;
  function fn(node: TreeNode | null): number {
    if (!node) return 0;

    const lefeSum = Math.max(fn(node.left), 0);
    const rightSum = Math.max(fn(node.right), 0);

    const sum = node!.val + lefeSum + rightSum;
    max = Math.max(sum, max);

    return node!.val + Math.max(lefeSum, rightSum);
  }
  fn(root);

  return max;
}

export {};
