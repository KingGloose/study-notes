// 2024.4.11 https://leetcode.cn/problems/roman-to-integer/

//method1 - 94ms
function romanToInt(s: string): number {
  const s_arr = s.split("");

  const find = (c: String) => {
    switch (c) {
      case "I":
        return 1;
      case "V":
        return 5;
      case "X":
        return 10;
      case "L":
        return 50;
      case "C":
        return 100;
      case "D":
        return 500;
      case "M":
        return 1000;
      default:
        return 0;
    }
  };

  let num = 0;
  for (let i = 0; i < s_arr.length; i++) {
    let c = s_arr[i];

    switch (c) {
      case "I":
        if (i !== s_arr.length - 1 && (s_arr[i + 1] === "V" || s_arr[i + 1] === "X")) {
          num += find(s_arr[i + 1]) - find("I");
          i++;
        } else {
          num += find("I");
        }
        break;
      case "V":
        num += find("V");
        break;
      case "X":
        if (i !== s_arr.length - 1 && (s_arr[i + 1] === "L" || s_arr[i + 1] === "C")) {
          num += find(s_arr[i + 1]) - find("X");
          i++;
        } else {
          num += find("X");
        }
        break;
      case "L":
        num += find("L");
        break;
      case "C":
        if (i !== s_arr.length - 1 && (s_arr[i + 1] === "D" || s_arr[i + 1] === "M")) {
          num += find(s_arr[i + 1]) - find("C");
          i++;
        } else {
          num += find("C");
        }
        break;
      case "D":
        num += find("D");
        break;
      case "M":
        num += find("M");
        break;
    }
  }

  return num;
}

// method2 - 113ms
function romanToInt1(s: string): number {
  const which = (ch: String) => {
    switch (ch) {
      case "I":
        return 1;
      case "V":
        return 5;
      case "X":
        return 10;
      case "L":
        return 50;
      case "C":
        return 100;
      case "D":
        return 500;
      case "M":
        return 1000;
      case "a":
        return 4;
      case "b":
        return 9;
      case "c":
        return 40;
      case "d":
        return 90;
      case "e":
        return 400;
      case "f":
        return 900;
      default:
        return 0;
    }
  };

  s = s.replace("IV", "a");
  s = s.replace("IX", "b");
  s = s.replace("XL", "c");
  s = s.replace("XC", "d");
  s = s.replace("CD", "e");
  s = s.replace("CM", "f");

  let num = 0;
  s.split("").forEach((item) => {
    num += which(item);
  });

  return num;
}

// method3 - 107m
function romanToInt2(s: string): number {
  const map = new Map([
    ["I", 1],
    ["V", 5],
    ["X", 10],
    ["L", 50],
    ["C", 100],
    ["D", 500],
    ["M", 1000],
  ]);
  const s_arr = s.split("");

  let sum = 0;
  for (let i = 0; i < s_arr.length; i++) {
    const current = map.get(s_arr[i])!;
    const next = map.get(s_arr[i + 1])!;

    if (current < next) {
      sum = sum + next - current;
      i++;
    } else {
      sum = sum + current;
    }
  }

  return sum;
}

console.log(romanToInt2("MCMXCIV"));
