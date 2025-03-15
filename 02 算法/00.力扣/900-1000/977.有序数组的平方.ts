// leecode: https://leetcode.cn/problems/squares-of-a-sorted-array/description/

// method1 暴力解法
function sortedSquares1(nums: number[]): number[] {
  return nums.map((i) => i ** 2).sort((a, b) => a - b);
}

// method2 双指针法
function sortedSquares2(nums: number[]): number[] {
  const lenght = nums.length;

  let left = 0;
  let right = lenght - 1;
  let index = lenght - 1;
  const arr = Array.from<number>({ length: lenght });

  while (left <= right) {
    const leftNums = nums[left] ** 2;
    const rightNums = nums[right] ** 2;

    if (rightNums > leftNums) {
      arr[index] = rightNums;
      right--;
      index--;
    } else {
      arr[index] = leftNums;
      left++;
      index--;
    }
  }

  return arr;
}

console.log(sortedSquares2([-4, -1, 0, 3, 10]));

export {};
