// 2024.4.10 https://leetcode.cn/problems/palindrome-number/description/

// method1 146ms
function isPalindrome(x: number): boolean {
  const str = x + "";

  for (let i = str.length - 1; i >= 0; i--) {
    if (str[i] !== str[str.length - 1 - i]) {
      return false;
    }
  }

  return true;
}

// method2 - 123ms
function isPalindrome1(x: number): boolean {
  if (x < 0) return false;
  if (x === 0) return true;
  if (x % 10 === 0) return false;

  let res = 0;
  let new_x = x;
  while (new_x != 0) {
    res = res * 10 + (new_x % 10);
    new_x = Math.floor(new_x / 10);
  }

  return res === x;
}

// method3 - 142ms
function isPalindrome2(x: number): boolean {
  if (x === 0) return true;
  if (x < 0 || x % 10 === 0) return false;

  const str_x = String(x);
  return str_x === str_x.split("").reverse().join("");
}

console.log("🚀 ~ isPalindrome(121):", isPalindrome2(121));

export {}