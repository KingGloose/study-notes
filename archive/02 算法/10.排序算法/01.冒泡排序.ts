import { getCountRuntimeInfo, swap } from "./utils";

// 冒泡排序
// 时间复杂度 最好情况:O(n) 最坏情况:O(n ^ 2) 平均情况:O(n ^ 2)
// 不适合大规模排序，只适合练手使用
function bubbleSort(arr: number[]): number[] {
  for (let i = 0; i < arr.length; i++) {
    let sorted = false;

    for (let j = 0; j < arr.length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
        sorted = true;
      }
    }

    if (!sorted) break;
  }

  return arr;
}

getCountRuntimeInfo(bubbleSort, 1, 100000);

export {};
