// leecode https://leetcode.cn/problems/container-with-most-water/

// 双指针 一个开头一个结尾 此时底是最大的
function maxArea(height: number[]): number {
  let start = 0;
  let end = height.length - 1;
  let max = 0;

  while (start < end) {
    const startHeight = height[start];
    const endHeight = height[end];

    const minHeight = Math.min(startHeight, endHeight);
    const area = minHeight * (end - start);
    if (max < area) max = area;

    if (startHeight < endHeight) {
      start++;
    } else {
      end--;
    }
  }

  return max;
}

console.log(maxArea([8, 7, 2, 1]));

export {};
