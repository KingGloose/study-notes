import { getCountRuntimeInfo, getSingleRuntimeInfo } from "./utils";

// 归并排序
/*
    时间复杂度：O(logn)
    归并排序属于是一个高效的排序，核心的思想是分治，讲待排序的数组分成若干个子数组进行排序
*/
function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;

  // 拆分
  const mid = Math.floor(arr.length / 2);
  const leftArr = arr.slice(0, mid);
  const rightArr = arr.slice(mid);

  const newLeftArr = mergeSort(leftArr);
  const newRightArr = mergeSort(rightArr);

  // 合并
  const newArr: number[] = [];
  let leftIndex = 0;
  let rightIndex = 0;
  while (leftIndex < newLeftArr.length && rightIndex < newRightArr.length) {
    if (newLeftArr[leftIndex] <= newRightArr[rightIndex]) {
      newArr.push(newLeftArr[leftIndex]);
      leftIndex++;
    } else {
      newArr.push(newRightArr[rightIndex]);
      rightIndex++;
    }
  }

  if (leftIndex < newLeftArr.length) {
    newArr.push(...newLeftArr.slice(leftIndex));
  }
  if (rightIndex < newRightArr.length) {
    newArr.push(...newRightArr.slice(rightIndex));
  }

  return newArr;
}

getSingleRuntimeInfo(mergeSort, 10000);
// getCountRuntimeInfo(mergeSort, 1000, 10000);

export {};
