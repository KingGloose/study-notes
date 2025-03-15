// leecode: https://leetcode.cn/problems/length-of-last-word/description/

function lengthOfLastWord(s: string): number {
  return (
    s
      .split(" ")
      .filter((item) => item !== "")
      .pop()?.length ?? 0
  );
}
