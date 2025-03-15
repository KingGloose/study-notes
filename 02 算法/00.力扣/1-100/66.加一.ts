// leecode: https://leetcode.cn/problems/plus-one/

// method1 - 58ms
function plusOne(digits: number[]): number[] {
  let isFix = true;
  let index = digits.length - 1;
  while (index >= 0) {
    if (digits[index] === 9) {
      isFix = false;
      digits[index] = 0;
      index--;
    } else {
      isFix = true;
      digits[index]++;
      break;
    }
  }

  if (!isFix) digits.unshift(1);

  return digits;
}

console.log(plusOne([1, 2]));
