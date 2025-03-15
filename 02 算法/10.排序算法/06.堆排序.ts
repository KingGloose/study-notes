// 堆排序
/*
    时间复杂度: O(nlogn)
*/

import { cbtPrint, swap } from "hy-algokit";
import { getSingleRuntimeInfo } from "./utils";

function heapifyDown(arr: number[], length: number, index: number) {
  while (2 * index + 1 < length) {
    let leftChildIndex = 2 * index + 1;
    let rightChildIndex = 2 * index + 2;

    let largeIndex = leftChildIndex;
    if (rightChildIndex < length && arr[leftChildIndex] < arr[rightChildIndex]) {
      largeIndex = rightChildIndex;
    }

    if (arr[index] >= arr[largeIndex]) {
      break;
    }

    swap(arr, index, largeIndex);
    index = largeIndex;
  }
}

function heapSort(arr: number[]): number[] {
  let n = arr.length;

  // 01 对数组进行原地建堆
  const start = Math.floor((n - 2) / 2);
  for (let i = start; i >= 0; i--) {
    heapifyDown(arr, n, i);
  }

  // 03 依次迁移
  for (let i = n - 1; i > 0; i--) {
    swap(arr, 0, i);
    heapifyDown(arr, i, 0);
  }

  return arr;
}

// cbtPrint(heapSort([11, 190, 14, 149, 24, 38, 30, 36, 36, 118, 29, 73, 84, 85, 151, 89, 43, 186, 108, 71]));

getSingleRuntimeInfo(heapSort);

export {};
