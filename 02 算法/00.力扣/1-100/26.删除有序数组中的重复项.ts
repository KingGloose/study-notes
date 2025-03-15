// 2024.4.12 https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

// method1 72ms
function removeDuplicates(nums: number[]): number {
  const nums_1 = Array.from(new Set(nums));
  nums_1.sort((a, b) => a - b);

  for (let i = 0; i < nums_1.length; i++) {
    nums[i] = nums_1[i];
  }

  return nums_1.length;
}

// method2 - 快慢指针 - 70ms
function removeDuplicates1(nums: number[]): number {
  let slow = 1;
  for (let fast = 1; fast < nums.length; fast++) {
    if (nums[fast] > nums[slow - 1]) {
      nums[slow++] = nums[fast];
    }
  }

  return slow;
}

let nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
console.log(removeDuplicates1(nums));
