// leecode: https://leetcode.cn/problems/minimum-time-difference/description/

// method1 - 87ms
function findMinDifference(timePoints: string[]): number {
  // 将时间都转为分钟
  const timeArr = timePoints.map((item) => {
    const [h, m] = item.split(":").map(Number);
    return h * 60 + m;
  });
  timeArr.sort((a, b) => a - b);

  let min = 1440;
  const length = timeArr.length;
  for (let i = 1; i < length; i++) {
    if (timeArr[i] === timeArr[i - 1]) return 0;
    let diff = timeArr[i] - timeArr[i - 1];
    min = Math.min(diff, min);
  }

  return Math.min(min, 1440 + timeArr[0] - timeArr[length - 1]);
}

console.log(findMinDifference(["23:59", "00:00"]));

export {};
