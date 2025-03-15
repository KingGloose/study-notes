// leecode: https://leetcode.cn/problems/binary-tree-inorder-traversal/

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

// method1 - 递归写法 - 59ms
function inorderTraversal1(root: TreeNode | null): number[] {
  const arr: number[] = [];
  function fn(node: TreeNode | null) {
    if (node) {
      fn(node.left);
      arr.push(node.val);
      fn(node.right);
    }
  }
  fn(root);
  return arr;
}

// method2 - 压栈处理
function inorderTraversal2(root: TreeNode | null): number[] {
 
}

export {};
