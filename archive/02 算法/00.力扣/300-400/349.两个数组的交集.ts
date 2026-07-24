// 2024.4.9 https://leetcode.cn/problems/intersection-of-two-arrays/

// method1 67ms
function intersection(nums1: number[], nums2: number[]): number[] {
  nums1.sort((a, b) => a - b);
  nums2.sort((a, b) => a - b);

  let p1 = 0;
  let p2 = 0;

  const arr: number[] = [];

  while (p1 < nums1.length && p2 < nums2.length) {
    const num1 = nums1[p1];
    const num2 = nums2[p2];

    if (num1 < num2) {
      p1++;
    } else if (num1 > num2) {
      p2++;
    } else {
      if (arr.indexOf(num1) == -1) {
        arr.push(num1);
      }

      p1++;
      p2++;
    }
  }

  return arr;
}

// method2 58ms
function intersection1(nums1: number[], nums2: number[]): number[] {
  const set1 = new Set(nums1);
  const set2 = new Set(nums2);
  const result: number[] = [];

  for (const num of set1) {
    if (set2.has(num)) {
      result.push(num);
    }
  }

  return result;
}

console.log(
  intersection(
    [
      61, 24, 20, 58, 95, 53, 17, 32, 45, 85, 70, 20, 83, 62, 35, 89, 5, 95, 12, 86, 58, 77, 30, 64, 46, 13, 5, 92, 67, 40, 20, 38, 31, 18,
      89, 85, 7, 30, 67, 34, 62, 35, 47, 98, 3, 41, 53, 26, 66, 40, 54, 44, 57, 46, 70, 60, 4, 63, 82, 42, 65, 59, 17, 98, 29, 72, 1, 96,
      82, 66, 98, 6, 92, 31, 43, 81, 88, 60, 10, 55, 66, 82, 0, 79, 11, 81,
    ],
    [
      5, 25, 4, 39, 57, 49, 93, 79, 7, 8, 49, 89, 2, 7, 73, 88, 45, 15, 34, 92, 84, 38, 85, 34, 16, 6, 99, 0, 2, 36, 68, 52, 73, 50, 77, 44,
      61, 48,
    ]
  )
);
