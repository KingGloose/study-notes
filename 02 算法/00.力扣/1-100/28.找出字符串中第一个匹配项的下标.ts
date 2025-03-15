// 2024.4.13 https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

// method1 - 59ms
function strStr(haystack: string, needle: string): number {
  return haystack.indexOf(needle);
}

// method2 - 暴力解法
function strStr1(haystack: string, needle: string): number {
  const n = haystack.length;
  const m = needle.length;

  for (let i = 0; i <= n - m; i++) {
    let index = i;
    for (let j = 0; j < m; j++) {
      if (haystack[index++] !== needle[j]) break;
      if (j === m - 1) return i;
    }
  }

  return -1;
}

console.log(strStr("leetcode", "leeto"));
