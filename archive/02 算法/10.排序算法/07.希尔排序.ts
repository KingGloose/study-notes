// 希尔排序
/*
    时间复杂度: 看情况，一般情况优于 O(n ^ 2)
*/

import { getSingleRuntimeInfo } from "./utils";

/*
    81 94 11 96 12 35 
    17 95 28 58 41 75
    15

    第一层循环: 循环步长 gap
    
    第二层循环: 依据步长找到不同的数列集合进行插入排序
    比如: gap为6,那么就按照6来对81 17 15 进行插入排序
    
    第三层循环: 对数列进行插入排序
    比如: 按照gap为6进行插入排序操作(之前插入可以理解为1)
*/
function shellSort(arr: number[]): number[] {
  const length = arr.length;
  let gap = Math.floor(length / 2);

  while (gap > 0) {
    for (let i = gap; i < length; i++) {
      const data = arr[i];
      let j = i;

      while (j > gap - 1 && data < arr[j - gap]) {
        arr[j] = arr[j - gap];
        j = j - gap;
      }

      arr[j] = data;
    }

    // 重新计算步长
    gap = Math.floor(gap / 2);
  }

  return arr;
}

getSingleRuntimeInfo(shellSort);

export {};
