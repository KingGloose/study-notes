// leecode: https://leetcode.cn/problems/spiral-matrix-ii/description/

// 1  2  3  4
// 12 13 14 5
// 11 16 15 6
// 10 9  8  7

// method1
function generateMatrix(n: number): number[][] {
  const arr = Array.from({ length: n }, () => Array(n).fill(0));

  let x = 0;
  let y = 0;
  let i = 1;

  let curr = 0;

  while (i <= n ** 2) {
    arr[y][x] = i;

    if (curr === 0) {
      // right
      if (x === n - 1 || arr[y][x + 1] !== 0) {
        curr = 1;
        y++;
      } else x++;
    } else if (curr === 1) {
      // bottom
      if (y === n - 1 || arr[y + 1][x] !== 0) {
        curr = 2;
        x--;
      } else y++;
    } else if (curr === 2) {
      // left
      if (x === 0 || arr[y][x - 1] !== 0) {
        curr = 3;
        y--;
      } else x--;
    } else if (curr === 3) {
      // top
      if (arr[y - 1][x] !== 0) {
        curr = 0;
        x++;
      } else y--;
    }

    i++;
  }

  return arr;
}

generateMatrix(5);

export {};
