// leecode: https://leetcode.cn/problems/sqrtx/description/

// method1 暴力解法 140ms
function mySqrt1(x: number): number {
  if (x <= 1) return x;
  if (x === 2) return 1;
  for (let i = 0; i < x; i++) {
    const data = i * i;
    if (data === x) return i;
    if (data > x) return i - 1;
  }
  return 1;
}
