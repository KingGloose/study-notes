// leecode: https://leetcode.cn/problems/unique-paths/

// method1 - 动态规划 - 67ms
function uniquePaths(m: number, n: number): number {
  const dp: number[][] = Array.from({ length: m }, (val, index) => {
    if (index === 0) return Array(n).fill(1);
    const newArr = Array(n).fill(0);
    newArr[0] = 1;
    return newArr;
  });

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
}

console.log(uniquePaths(7, 3));
