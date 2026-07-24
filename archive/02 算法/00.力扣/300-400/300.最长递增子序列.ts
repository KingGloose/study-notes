// leecode: https://leetcode.cn/problems/longest-increasing-subsequence/description/

// method1 - 动态规划 - 162ms -> n ^ 2
function lengthOfLIS1(nums: number[]): number {
  let max = 0;
  const dp = Array(nums.length).fill(1);

  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    let dpMax = 0;
    for (let j = i - 1; j >= 0; j--) {
      if (current > nums[j]) dpMax = Math.max(dpMax, dp[j]);
    }
    dp[i] += dpMax;
    max = Math.max(max, dp[i]);
  }

  return max;  
}

// method2 - 贪心算法 + 二分查找 - 74ms -> nlogn
function lengthOfLIS2(nums: number[]): number {
  const length = nums.length;
  const arr: number[] = [];

  for (let i = 0; i < length; i++) {
    const data = nums[i];

    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (arr[mid] < data) left = mid + 1;
      else right = mid - 1;
    }

    if (left === arr.length) {
      arr.push(data);
    } else {
      arr[left] = data;
    }
  }

  return arr.length;
}

console.log(lengthOfLIS2([0, 1, 0, 3, 2, 3]));

export {};
