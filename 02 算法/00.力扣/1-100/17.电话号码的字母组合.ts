// leecode: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/

// method1 - 47ms
function letterCombinations(digits: string): string[] {
  const map = new Map([
    ["2", "abc"],
    ["3", "def"],
    ["4", "ghi"],
    ["5", "jkl"],
    ["6", "mno"],
    ["7", "pqrs"],
    ["8", "tuv"],
    ["9", "wxyz"],
  ]);

  if (digits.length === 0) return [];
  let arr: string[] = map.get(digits[0])?.split("")!;
  const length = digits.length;
  for (let i = 1; i < length; i++) {
    const chars = map.get(digits[i])!;
    let newArr = [];
    for (const m of arr) {
      for (const n of chars) newArr.push(m + n);
    }
    arr = newArr;
  }

  return arr;
}

console.log(letterCombinations("23"));

export {};
