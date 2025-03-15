// 2024.4.9 https://leetcode.cn/problems/two-sum/

function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, any>();

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (map.has(diff)) return [map.get(diff), i];
    map.set(nums[i], i);
  }

  return [];
}

console.log(twoSum([2, 7, 11, 15], 9));
