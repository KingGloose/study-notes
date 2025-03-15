// leecode: https://leetcode.cn/problems/add-strings/description/

function addStrings(num1: string, num2: string): string {
  const maxLength = Math.max(num1.length, num2.length);

  num1 = num1.padStart(maxLength, "0");
  num2 = num2.padStart(maxLength, "0");

  let j = 0; // 进位
  let result = "";
  for (let i = maxLength - 1; i >= 0; i--) {
    const c = parseInt(num1[i]) + parseInt(num2[i]) + j;
    j = Math.floor(c / 10);
    result = `${c % 10}` + result;
  }
  if (j !== 0) result = `${j}` + result;

  return result;
}

console.log(addStrings("456", "77"));

export {};
