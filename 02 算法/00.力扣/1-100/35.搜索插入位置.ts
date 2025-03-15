// leecode: https://leetcode.cn/problems/search-insert-position/

// method1 -
function searchInsert(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) return mid;
    if (nums[mid] > target) right = mid - 1;
    if (nums[mid] < target) left = mid + 1;
  }

  return left;
}

console.log(searchInsert([1, 3, 5, 6], 7));
