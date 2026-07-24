function forceStringMatch(text: string, pattern: string): number {
  const n = text.length;
  const m = pattern.length;

  for (let i = 0; i <= n - m; i++) {
    let index = i;
    for (let j = 0; j < m; j++) {
      if (text[index++] !== pattern[j]) break;
      if (j === m - 1) return i;
    }
  }

  return -1;
}

console.log(forceStringMatch("Hello, world!", "world"));

export {};
