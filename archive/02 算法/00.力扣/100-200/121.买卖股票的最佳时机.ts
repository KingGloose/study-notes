// leecode https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/

// method1 暴力解法 - 超时
function maxProfit1(prices: number[]): number {
  let max = -Infinity;

  const length1 = prices.length;
  for (let i = 0; i < length1 - 1; i++) {
    const start = prices[i];
    for (let j = i + 1; j < length1; j++) {
      const end = prices[j];
      if (start > end) continue;

      const price = end - start;

      if (price <= 0) continue;
      if (price > 0 && price > max) max = price;
    }
  }

  if (max === -Infinity) return 0;

  return max;
}

// method2 动态规划 - 83ms
function maxProfit2(prices: number[]): number {
  if (prices.length <= 1) return 0;

  let prevValue = 0;
  let minPrice = prices[0];

  for (let i = 1; i < prices.length; i++) {
    prevValue = Math.max(prevValue, prices[i] - minPrice);
    minPrice = Math.min(minPrice, prices[i]);
  }

  return prevValue;
}

console.log(maxProfit2([7, 1, 5, 3, 6, 4]));

export {};
