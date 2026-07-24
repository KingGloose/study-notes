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

// 时间复杂度 O(logn)
console.log(binarySearch([1, 2, 3, 5, 6, 7, 9, 10, 11, 12], 11));

export {};
