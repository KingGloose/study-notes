// leecode https://leetcode.cn/problems/evaluate-reverse-polish-notation/

// method1 - 67ms
function evalRPN(tokens: string[]): number {
  function handler(h: string, first: number, last: number) {
    switch (h) {
      case "*": return first * last;
      case "-": return first - last;
      case "+": return first + last;
      case "/": return Math.trunc(first / last); // 只保留整数部分
    }
  }

  const stack: number[] = [];
  const length = tokens.length;
  for (let i = 0; i < length; i++) {
    const current = tokens[i];

    if (["+", "-", "*", "/"].includes(current)) {
      const last = stack.pop()!;
      const first = stack.pop()!;
      const value = handler(current, first, last)!;
      stack.push(value);
    } else {
      stack.push(Number(current));
    }
  }

  return stack[0];
}

console.log(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]));

export {};
