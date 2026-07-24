function sequentSearch(array: number[], num: number) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === num) return i;
  }
  return -1;
}

// 时间复杂度 O(n)
sequentSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3);

export {};
