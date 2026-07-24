// leecode: https://leetcode.cn/problems/invert-binary-tree/

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

// method1
function invertTree(root: TreeNode | null): TreeNode | null {
  function fn(treeNode: TreeNode) {
    const temp = treeNode.left;
    treeNode.left = treeNode.right;
    treeNode.right = temp;
  }

  if (root) {
    const stack: TreeNode[] = [root];

    while (stack.length > 0) {
      const treeNode = stack.pop()!;
      if (treeNode.left) stack.push(treeNode.left);
      if (treeNode.right) stack.push(treeNode.right);

      fn(treeNode);
    }
  }

  return root;
}

export {};
