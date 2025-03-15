// leecode: https://leetcode.cn/problems/sliding-window-maximum/description/

// method1 - 631ms - 双端队列
function maxSlidingWindow(nums: number[], k: number): number[] {
  const dequeue: number[] = []; // 双端队列，存储得是 nums 得索引值
  const maxArr: number[] = [];

  const length = nums.length;
  for (let i = 0; i < length; i++) {
    while (dequeue.length > 0 && nums[dequeue[dequeue.length - 1]] < nums[i]) dequeue.pop();
    dequeue.push(i);
    if (dequeue[0] < i - k + 1) dequeue.shift();
    if (i >= k - 1) maxArr.push(nums[dequeue[0]]);
  }

  return maxArr;
}

console.log(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3));

// method2 - 动态规划
