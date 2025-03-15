// leecode https://leetcode.cn/problems/maximum-subarray/description/

// method1 - 73ms / 90%
function maxSubArray1(nums: number[]): number {
  if (nums.length === 1) return nums[0];

  let prev = nums[0];
  let max = prev;

  for (let i = 1; i < nums.length; i++) {
    const current = nums[i];
    prev = prev + current > current ? prev + current : current;
    if (prev > max) max = prev;
  }

  return max;
}

console.log(maxSubArray1([-1, -2]));

export {};
