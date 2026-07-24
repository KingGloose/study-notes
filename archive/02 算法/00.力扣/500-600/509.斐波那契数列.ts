// leecode: https://leetcode.cn/problems/fibonacci-number/description/
// example: 0 1 1 2 3 5 8 13 21 34 55

// method1 递归 + 缓存求法 - 64ms / 40.43%
function fib1(n: number): number {
  const map = new Map();

  function fn(n: number): number {
    if (n <= 1) return n;

    let a = map.get(n - 1) ?? fn(n - 1);
    let b = map.get(n - 2) ?? fn(n - 2);

    map.set(n - 1, a);
    map.set(n - 2, b);

    return (a + b) % 1000000007;
  }

  return fn(n);
}

// method2 递归 + 缓存求法(优化版) - 58ms / 76.60%
function fib2(n: number): number {
  const map = new Map();

  function fn(n: number): number {
    if (n <= 1) return n;
    if (map.has(n)) return map.get(n);

    let a = fn(n - 1);
    let b = fn(n - 2);

    map.set(n, (a + b) % 1000000007);
    return map.get(n);
  }

  return fn(n);
}

// method3 动态规划 - 42ms / 100%
function fib3(n: number): number {
  /*
    1.定义状态
        1.1 dp保留斐波那契数列中每一个位置对应的值(状态)
        1.2 dp[x]表示的就是x位置对应的值(状态)
    2.状态转移方程: dp[i] = dp[i-1] + dp[i-2]
        2.1 状态转移方程一般情况都是写在循环(for/while)中
    3.设置初始化状态: dp[0] / dp[1] 初始化状态
    4.计算最终的结果
  */
  let dp: number[] = [0, 1];
  for (let i = 2; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007;
  }
  return dp[n];
}

// method4 动态规划(空间优化版 - 状态压缩)
function fib4(n: number): number {
  if (n <= 1) return n;

  let prev = 0;
  let cur = 1;
  for (let i = 2; i <= n; i++) {
    const newValue = (prev + cur) % 1000000007;
    prev = cur;
    cur = newValue;
  }

  return cur;
}

export {};
