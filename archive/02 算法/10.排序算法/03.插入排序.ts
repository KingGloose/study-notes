import { getSingleRuntimeInfo } from "./utils";

// 插入排序
// 时间复杂度 最好情况:O(n) 最坏情况:O(n ^ 2) 平均情况:O(n ^ 2)
// 不适合大规模排序，只适合练手使用，但是在数据都排好的情况表现很好
function insertionSort(arr: number[]): number[] {
  for (let i = 1; i < arr.length; i++) {
    let j = i - 1;
    const data = arr[i];
    while (j >= 0 && data < arr[j]) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = data;
  }
  return arr;
}

getSingleRuntimeInfo(insertionSort);

export {};
