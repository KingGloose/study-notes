// leecode: https://leetcode.cn/problems/minimum-size-subarray-sum/description/

// method1 - 滑动窗口
function minSubArrayLen(target: number, nums: number[]): number {
  const length = nums.length;

  let left = 0;
  let right = 0;
  let result = length + 1;
  let sum = 0;

  while (right < length) {
    sum += nums[right];
    if (sum >= target) {
      while (sum - nums[left] >= target) {
        sum -= nums[left++];
      }
      result = Math.min(result, right - left + 1);
    }
    right++;
  }

  return result === length + 1 ? 0 : result;
}

console.log(minSubArrayLen(11, [1, 2, 3, 4, 5]));

export {};
