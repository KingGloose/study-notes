function generate(numRows: number): number[][] {
  if (numRows === 1) return [[1]];
  if (numRows === 2) return [[1], [1, 1]];

  let arr = [[1], [1, 1]];
  for (let rows = 2; rows < numRows; rows++) {
    arr.push([]);
    for (let cols = 0; cols <= rows; cols++) {
      const curCols = arr[rows];
      if (cols === 0) curCols.push(1);
      else if (cols === rows) curCols.push(1);
      else curCols[cols] = arr[rows - 1][cols - 1] + arr[rows - 1][cols];
    }
  }

  return arr;
}

console.log(generate(4));

export {};
