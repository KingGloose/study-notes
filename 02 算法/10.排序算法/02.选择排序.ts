import { getSingleRuntimeInfo, swap } from "./utils";

// 选择排序
// 不适合大规模排序，只适合练手使用
function selectionSort(arr: number[]): number[] {
  for (let i = 0; i < arr.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) minIndex = j;
    }
    if (i !== minIndex) swap(arr, i, minIndex);
  }

  return arr;
}

// function selectionSort(arr: number[]): number[] {
//   for (let i = 0; i < arr.length - 1; i++) {
//     for (let j = i + 1; j < arr.length; j++) {
//       if (arr[i] > arr[j]) swap(arr, i, j);
//     }
//   }
//   return arr;
// }

getSingleRuntimeInfo(selectionSort);

export {};
