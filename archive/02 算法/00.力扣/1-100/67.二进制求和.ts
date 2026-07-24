// leecode: https://leetcode.cn/problems/add-binary/

// method1 - 51ms 不推荐
function addBinary1(a: string, b: string): string {
  // @ts-ignore
  return (BigInt("0b" + a) + BigInt("0b" + b)).toString(2);
}

// method2 -
function addBinary2(a: string, b: string): string {
  let aLength = a.length - 1;
  let bLength = b.length - 1;

  let prev = 0;
  const str = [];

  // 计算共同都有的部分
  while (aLength >= 0 && bLength >= 0) {
    let sum = prev;
    sum += parseInt(a.charAt(aLength--));
    sum += parseInt(b.charAt(bLength--));
    prev = Math.floor(sum / 2);
    str.unshift(sum % 2);
  }

  // 02 处理多出来的部分
  while (aLength >= 0) {
    let sum = prev;
    sum += parseInt(a.charAt(aLength--));
    prev = Math.floor(sum / 2);
    str.unshift(sum % 2);
  }
  while (bLength >= 0) {
    let sum = prev;
    sum += parseInt(b.charAt(bLength--));
    prev = Math.floor(sum / 2);
    str.unshift(sum % 2);
  }
  if (prev === 1) {
    str.unshift(1);
  }

  return str.join("");
}

addBinary2("111", "11");
