export function swap(arr: number[], i: number, j: number) {
  [arr[i], arr[j]] = [arr[j], arr[i]];
}

export function isSorted(arr: number[]): boolean {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) return false;
  }
  return true;
}

function getRuntimeInfo(fn: any, length = 20) {
  const arr = Array.from({ length }, () => Math.floor(Math.random() * 200));
  const cloneArr = arr.map((item) => item);

  // @ts-ignore
  const startTime = process.hrtime();

  const sortedArr = fn(arr);

  // @ts-ignore
  const [seconds, nanoseconds] = process.hrtime(startTime);
  const elapsed = (seconds * 1e3 + nanoseconds * 1e-6).toFixed(3); // 转换为毫秒

  return { oriArr: cloneArr, sortedArr, isSorted: isSorted(sortedArr), elapsed };
}

export function getSingleRuntimeInfo(fn: any, length = 20) {
  const { oriArr, sortedArr, isSorted, elapsed } = getRuntimeInfo(fn, length);

  console.log("原始数组:", oriArr);
  console.log("排序数组:", sortedArr);
  console.log("是否排序:", isSorted);
  console.log("排序时间:", elapsed + "ms");
}

export function getCountRuntimeInfo(fn: any, count = 100, length = 20) {
  const times: number[] = [];
  for (let i = 0; i < count; i++) {
    const { isSorted, elapsed } = getRuntimeInfo(fn, length);
    if (isSorted) times.push(Number(elapsed));
  }

  console.log(`运行${count}次 数组个数${length}个的情况`);
  console.log(`排序成功${times.length}次 排序失败${count - times.length}次`);
  console.log("平均耗时:", times.reduce((acc, cur) => acc + cur, 0).toFixed(3) + "ms");
}
