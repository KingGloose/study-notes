// 快速排序

import { getSingleRuntimeInfo, swap } from "./utils";

/*
    时间复杂度: 最好情况: O(nlogn) 最坏情况: O(n ^ 2) (概率极小)
*/
function quickSort(arr: number[]): number[] {
  // 20 2 9 7 12 15 1 6 8
  function partition(left: number, right: number) {
    if (left >= right) return;

    const pivot = arr[right];
    let i = left; // leftIndex
    let j = right - 1; // rightIndex

    // 将双指针移动到指定位置
    while (i <= j) {
      while (arr[i] < pivot) i++;
      while (arr[j] > pivot) j--;

      if (i <= j) {
        swap(arr, i, j);
        i++;
        j--;
      }
    }

    // 移动完毕，将pivot移动
    swap(arr, i, right);

    // 左右继续遍历
    partition(left, j);
    partition(i + 1, right);
  }

  partition(0, arr.length - 1);

  return arr;
}

getSingleRuntimeInfo(quickSort);

export {};
