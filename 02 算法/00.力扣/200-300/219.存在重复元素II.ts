// 2024.4.9 https://leetcode.cn/problems/contains-duplicate-ii/description/

function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i])) {
      const index = map.get(nums[i])!;
      if (Math.abs(i - index) <= k) return true;
    }

    map.set(nums[i], i);
  }

  return false;
}

containsNearbyDuplicate([1, 2, 3, 1], 3);
console.log(containsNearbyDuplicate([1, 2, 3, 1], 3));
