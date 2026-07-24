// leecode: https://leetcode.cn/problems/majority-element-ii/

// method1 3ms
function majorityElement(nums: number[]): number[] {
  const map = new Map();
  const result: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    const value = nums[i];
    if (map.has(value)) {
      let count = map.get(value);
      map.set(value, ++count);
    } else {
      map.set(value, 1);
    }

    if (map.get(value) > nums.length / 3 && result.indexOf(value) < 0) {
      result.push(value);
    }
  }

  return result;
}

export {};
