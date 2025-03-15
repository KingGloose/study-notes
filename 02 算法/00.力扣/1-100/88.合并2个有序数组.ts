// leecode: https://leetcode.cn/problems/merge-sorted-array/

// method1 - 使用jsapi - 64ms
function merge1(nums1: number[], m: number, nums2: number[], n: number): void {
  nums1.splice(m, nums1.length - m, ...nums2);
  nums1.sort((a, b) => a - b);
}

// method2 - 倒序三指针 - 59ms
function merge2(nums1: number[], m: number, nums2: number[], n: number): void {
  let i = nums1.length - 1;

  while (n > 0) {
    if (m > 0 && nums1[m - 1] > nums2[n - 1]) {
      nums1[i] = nums1[m - 1];
      i--;
      m--;
    } else {
      nums1[i] = nums2[n - 1];
      i--;
      n--;
    }
  }

  console.log(nums1);
}

merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3);

export {};
