// leecode https://leetcode.cn/problems/maximum-subarray/description/

// method1 - 73ms / 90%
function maxSubArray1(nums: number[]): number {
  let prev = nums[0];
  let max = prev;

  for (let i = 1; i < nums.length; i++) {
    const current = nums[i];
    prev = prev + current > current ? prev + current : current;
    if (prev > max) max = prev;

    console.log(prev);
  }

  return max;
}

// [-2, 1, -2, 4, 3, 5, 6, 1, 5, 6]
console.log(maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]));

export {};
