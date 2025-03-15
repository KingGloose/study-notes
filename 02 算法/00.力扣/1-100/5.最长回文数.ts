// leecode: https://leetcode.cn/problems/longest-palindromic-substring/description/

// method1 - 82ms
// 本质就是从中心往外边扩散
function longestPalindrome(s: string): string {
  let max = 0;
  let rsLeft = 0;
  let rsRight = 0;

  let i = 0;
  const length = s.length;
  while (i < length) {
    // 01 解决 caac / cbbc 中心2个相同的问题
    let left = i - 1;
    while (left >= 0 && s[left] === s[i]) left--;
    let right = i + 1;
    while (right < length && s[right] === s[i]) right++;

    // 02 向外扩散对比
    while (left >= 0 && right < length && s[left] === s[right]) {
      left--;
      right++;
    }

    const maxLength = right - left - 1;
    if (max < maxLength) {
      max = maxLength;
      rsLeft = left + 1;
      rsRight = right;
    }

    i++;
  }

  return s.substring(rsLeft, rsRight);
}
console.log(longestPalindrome("cbbd"));

export {};
