// 2024.4.13 https://leetcode.cn/problems/remove-element/

// method1  - 63ms
function removeElement(nums: number[], val: number): number {
  let i = 0;
  while (i < nums.length) {
    nums[i] === val ? nums.splice(i, 1) : i++;
  }
  return nums.length;
}

// method2 - 快慢指针 - 52ms
function removeElement1(nums: number[], val: number): number {
  let fast = 0;
  let slow = 0;

  while (fast < nums.length) {
    if (nums[fast] !== val) {
      nums[slow++] = nums[fast];
    }
    fast++;
  }

  return slow;
}

let numss = [0, 1, 2, 2, 3, 0, 4, 2];

console.log(numss, removeElement1(numss, 2));
