import { btPrint } from "hy-algokit";
import { BSTree } from "./BSTree";

// AVL树
class AVLTreeNode {
  left: AVLTreeNode | null = null;
  value: number;
  right: AVLTreeNode | null = null;

  // 当前节点的父节点
  parent: AVLTreeNode | null = null;

  constructor(value: number) {
    this.value = value;
  }

  // 当前节点是否是父节点的左节点
  get isLeft(): boolean {
    if (!this.parent) {
      console.log(`${this.value} 没有 parent`);
      return false;
    }
    return !!(this.parent.left === this);
  }

  // 当前节点是否是父节点的右节点
  get isRight(): boolean {
    if (!this.parent) {
      console.log(`${this.value} 没有 parent`);
      return false;
    }
    return !!(this.parent.right === this);
  }

  // 获取当前节点的高度
  private getHeight() {
    const leftHeight: number = this.left ? this.left?.getHeight() : 0;
    const rightHeight: number = this.right ? this.right.getHeight() : 0;

    return Math.max(leftHeight, rightHeight) + 1;
  }

  // 获取元素的平衡因子 (|leftHieght - rightHeight|)
  private getBalenceFactor() {
    const leftHeight: number = this.left ? this.left?.getHeight() : 0;
    const rightHeight: number = this.right ? this.right.getHeight() : 0;

    return Math.abs(leftHeight - rightHeight);
  }

  // 获取当前元素高度较高的子元素 (左/右节点)
  public getHigherChild(): AVLTreeNode | null {
    const leftHeight: number = this.left ? this.left?.getHeight() : 0;
    const rightHeight: number = this.right ? this.right.getHeight() : 0;

    if (leftHeight > rightHeight) return this.left;
    if (leftHeight < rightHeight) return this.right;
    return this.isLeft ? this.left : this.right;
  }

  // 如果平衡因子大于 1 的话就不平衡
  get isBalence(): boolean {
    return this.getBalenceFactor() <= 1;
  }

  // 右旋转
  public rightRotation() {
    // 01 获取 povint 节点
    const povint = this.left;
    const root = this;

    const rootIsLeft = root.isLeft;
    const rootIsRight = root.isRight;

    // 02 处理 povint 的右子节点
    root.left = povint!.right;
    if (povint?.right) povint.right.parent = root;

    // 03 处理 当前节点
    povint!.parent = root.parent;
    povint!.right = root;
    root.parent = povint;

    // 04 处理 povint 要挂载到父节点的那个节点
    if (rootIsLeft) povint!.parent!.left = povint;
    else if (rootIsRight) povint!.parent!.right = povint;
    else if (!povint?.parent) povint!.parent = null;

    return povint;
  }

  // 左旋转
  public leftRotation() {
    // 01 获取 povint 节点
    const povint = this.right;
    const root = this;

    const rootIsLeft = root.isLeft;
    const rootIsRight = root.isRight;

    // 02 处理 povint 的左子节点
    root.right = povint!.left;
    if (povint?.left) povint.left.parent = root;

    // 03 处理 当前节点
    povint!.parent = root.parent;
    povint!.left = root;
    root.parent = povint;

    // 04 处理 povint 要挂载到父节点的那个节点
    if (rootIsLeft) povint!.parent!.left = povint;
    else if (rootIsRight) povint!.parent!.right = povint;
    else if (!povint?.parent) povint!.parent = null;

    return povint;
  }
}

class AVLTree extends BSTree {
  protected root: AVLTreeNode | null = null;

  constructor(arr: number[] = []) {
    super();
    arr.forEach((item) => this.add(item));
  }

  // 打印
  public print() {
    btPrint(this.root);
  }

  // 重写父元素的 createNode, 在 insert 就会返回子元素的 AVLTreeNode
  protected createNode(value: number): AVLTreeNode {
    return new AVLTreeNode(value);
  }

  // 新建一个插入方法
  public add(value: number) {
    const newNode = super.insert(value) as AVLTreeNode;
    this.checkBalance(newNode, true);
  }

  // 新建一个删除方法
  public remove(value: number) {
    const delNode = super.delete(value) as AVLTreeNode;
    this.checkBalance(delNode, false);
  }

  // 检查是否平衡
  public checkBalance(node: AVLTreeNode, isAdd = true) {
    let current = node.parent;
    while (current) {
      if (!current.isBalence) {
        this.rebalance(current);

        // 性能优化
        /*
          1、add 情况只需要一次 rebalance 即可
          2、remove 情况则需要多次
        */
        // if (isAdd) break;
      }
      current = current.parent!;
    }
  }

  // 传入不平衡的节点进行平衡操作
  public rebalance(root: AVLTreeNode) {
    const pivot = root.getHigherChild();
    const child = pivot?.getHigherChild();

    let newRoot: AVLTreeNode | null = null;
    if (pivot?.isLeft) {
      if (child?.isLeft) {
        newRoot = root.rightRotation(); // LL
      } else {
        pivot.leftRotation(); // LR
        newRoot = root.rightRotation();
      }
    } else {
      if (child?.isRight) {
        newRoot = root!.leftRotation(); // RR
      } else {
        pivot?.rightRotation(); // RL
        newRoot = root.leftRotation();
      }
    }

    if (!newRoot?.parent) this.root = newRoot;
  }
}

const avlTree = new AVLTree();

// 随机生成数字模拟
function shuffleArray(array: number[]) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
function generateAndSelectRandomNumbers() {
  let numbers = [];
  for (let i = 0; i < 25; i++) numbers.push(Math.floor(Math.random() * 100) + 1);
  let shuffledNumbers = numbers.slice();
  shuffleArray(shuffledNumbers);
  let selectedNumbers = shuffledNumbers.slice(0, 7);
  return [numbers, selectedNumbers];
}
const [ori, del] = generateAndSelectRandomNumbers();
console.log(ori, del);

for (const item of ori) avlTree.add(item);
avlTree.print();

for (const item of del) avlTree.remove(item);
avlTree.print();
