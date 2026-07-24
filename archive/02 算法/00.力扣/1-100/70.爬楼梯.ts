// leecode: https://leetcode.cn/problems/climbing-stairs/

// method1 - 59ms
function climbStairs(n: number): number {
  if (n <= 3) return n;

  let dp = [0, 1, 2, 3];
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

console.log(climbStairs(5));

export {};
