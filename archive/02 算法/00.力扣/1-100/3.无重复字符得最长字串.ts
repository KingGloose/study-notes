// leecode: https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/

// method1 82ms
// 思路: 如果存在 abcbdef 那么遇到不对的就使用 splice 截取数据到 cb 然后再依次向下寻找
function lengthOfLongestSubstring1(s: string): number {
  let arr: string[] = [];
  let max: number = 0;

  for (const char of s) {
    const index = arr.indexOf(char);
    if (index !== -1) {
      max = Math.max(arr.length, max);
      arr = arr.splice(index + 1);
    }

    arr.push(char);
  }

  max = Math.max(arr.length, max);

  return max;
}

// method2 双指针 87ms
function lengthOfLongestSubstring2(s: string): number {
  const length = s.length;
  const map = new Map();
  let max = 0;
  let left = 0;
  for (let right = 0; right < length; right++) {
    const data = s[right];
    if (map.has(data) && map.get(data) >= left) {
      left = map.get(data) + 1;
    }

    map.set(data, right);
    max = Math.max(max, right - left + 1);
  }

  return max;
}

console.log(lengthOfLongestSubstring2("abba"));
