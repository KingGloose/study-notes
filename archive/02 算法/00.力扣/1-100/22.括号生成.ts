// leecode: https://leetcode.cn/problems/generate-parentheses/description/

// method1 - 64ms
function generateParenthesis(n: number): string[] {
  let set = new Set(["()"]);
  for (let i = 2; i <= n; i++) {
    const newSet = new Set<string>();
    for (const s of set) {
      for (let j = 0; j < s.length; j++) {
        newSet.add(s.slice(0, j) + "()" + s.slice(j));
      }
    }
    set = newSet;
  }

  return Array.from(set);
}

console.log(generateParenthesis(2));

export {};
