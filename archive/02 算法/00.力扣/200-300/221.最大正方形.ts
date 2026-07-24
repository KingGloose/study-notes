// leecode: https://leetcode.cn/problems/maximal-square/description/

// method1 - 动态规划 - 107ms
function maximalSquare1(matrix: string[][]): number {
  const rows = matrix.length;
  const cols = matrix[0].length;
  if (rows === 1 && cols === 1 && Number(matrix[0][0]) === 1) return 1;

  let max = 0;
  const dp = Array.from({ length: rows }, () => Array(cols).fill(0));
  for (let i = 0; i < cols; i++) {
    dp[0][i] = Number(matrix[0][i]);
    if (dp[0][i] === 1) max = 1;
  }
  for (let j = 0; j < rows; j++) {
    dp[j][0] = Number(matrix[j][0]);
    if (dp[j][0] === 1) max = 1;
  }

  for (let i = 1; i < rows; i++) {
    for (let j = 1; j < cols; j++) {
      if (Number(matrix[i][j]) === 1) {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1;
      }
      max = Math.max(dp[i][j], max);
    }
  }

  return max * max;
}

// method2 - 动态规划 / 优化版本 - 100ms
function maximalSquare2(matrix: string[][]): number {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const dp = Array.from({ length: rows }, () => Array(cols).fill(0));

  let max = 0;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (matrix[i][j] === "0") {
        dp[i][j] = 0;
      } else {
        if (i === 0 || j === 0) {
          dp[i][j] = 1;
        } else {
          dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1;
        }
      }
      max = Math.max(dp[i][j], max);
    }
  }

  return max * max;
}

console.log(
  maximalSquare2([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
  ])
);

export {};
