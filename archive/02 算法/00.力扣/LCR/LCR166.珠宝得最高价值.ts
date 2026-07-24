// leecode: https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/description/

// method1 - 67ms
function jewelleryValue(frame: number[][]): number {
  const h = frame.length;
  const w = frame[0].length;

  // 初始化值
  const dp = Array.from({ length: h }, () => Array(w).fill(0));
  dp[0][0] = frame[0][0];
  for (let i = 1; i < w; i++) dp[0][i] = frame[0][i] + dp[0][i - 1];
  for (let j = 1; j < h; j++) dp[j][0] = frame[j][0] + dp[j - 1][0];

  for (let i = 1; i < h; i++) {
    for (let j = 1; j < w; j++) {
      dp[i][j] = frame[i][j] + Math.max(dp[i][j - 1], dp[i - 1][j]);
    }
  }

  return dp[h - 1][w - 1];
}

console.log(
  jewelleryValue([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
  ])
);

export {};
