// 2024.4.11 https://leetcode.cn/problems/longest-common-prefix/

function longestCommonPrefix(strs: string[]): string {
  const ans = strs[0].split("");

  for (let i = 1; i < strs.length; i++) {
    const cur = strs[i].split("");

    let j = 0;
    for (; j < cur.length; j++) {
      if (ans[j] !== cur[j]) {
        ans.splice(j, ans.length - j);
      }
    }

    ans.splice(j, ans.length - j);
  }

  return ans.join("");
}

console.log(longestCommonPrefix(["flower", "fkow"]));
