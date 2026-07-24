import ArrayStack from "../ArrayStack";

let arrayStack = new ArrayStack<number>();

function BinaryToDecimal(num: number): string {
  while (num > 0) {
    let BinaryData = num % 2;
    arrayStack.push(BinaryData);
    num = (num - BinaryData) / 2;
  }

  let str = "";
  while (!arrayStack.isEmpty()) {
    str += arrayStack.pop();
  }

  return str;
}

console.log(BinaryToDecimal(40));
