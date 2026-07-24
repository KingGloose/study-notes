// 2024.9.21 https://leetcode.cn/problems/binary-search/description/

// method1  64ms
function binarySearch(arr: number[], target: number): number {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) return mid;
    if (arr[mid] > target) right = mid - 1;
    if (arr[mid] < target) left = mid + 1;
  }

  return -1;
}
