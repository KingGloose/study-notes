// leecode: https://leetcode.cn/problems/median-of-two-sorted-arrays/description/

// method1 - 双指针 - 95ms
// 1 2 3 4 5 6 12 18 19 | 7 15 16 17 19 -> 1 2 3 4 5 6 7 12 15 16 17 18 19
// 1 2 | 1 3 -> 1 1 2 3
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  let total = nums1.length + nums2.length;
  let isOdd = total % 2 !== 0;
  let mid = total / 2;

  let arr: number[] = [];
  let n1Index = 0;
  let n2Index = 0;

  while (arr.length < Math.floor(mid) + 1) {
    const n1Data = nums1[n1Index] === undefined ? Infinity : nums1[n1Index];
    const n2Data = nums2[n2Index] === undefined ? Infinity : nums2[n2Index];

    if (n1Data < n2Data) {
      n1Index++;
      arr.push(n1Data);
    } else if (n1Data === n2Data) {
      n1Index++;
      arr.push(n1Data);
      if (arr.length >= Math.floor(mid) + 1) break;
      n2Index++;
      arr.push(n2Data);
    } else {
      n2Index++;
      arr.push(n2Data);
    }
  }

  if (isOdd) {
    return arr[arr.length - 1];
  } else {
    return (arr[arr.length - 2] + arr[arr.length - 1]) / 2;
  }
}

// 2 2 2 2 4 4 4 4
console.log(findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]));

export {};
