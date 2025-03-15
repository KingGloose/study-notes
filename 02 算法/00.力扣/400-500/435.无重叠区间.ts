// leecode: https://leetcode.cn/problems/non-overlapping-intervals/

// method1 动态规划 + 贪心
/*
    1 - 3
      2 - 4
        3 - 6
*/
function eraseOverlapIntervals(intervals: number[][]): number {
  let nums = 1;

  intervals.sort((a, b) => a[0] - b[0]);

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] >= intervals[i - 1][1]) {
      nums++;
    } else {
      intervals[i][1] = Math.min(intervals[i - 1][1], intervals[i][1]);
    }
  }

  return intervals.length - nums;
}

console.log(
  eraseOverlapIntervals([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
  ])
);

export {};
