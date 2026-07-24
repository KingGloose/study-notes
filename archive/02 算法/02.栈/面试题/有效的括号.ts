import ArrayStack from "../ArrayStack";

let arrayStack = new ArrayStack<string>();
function matchParenthese(str: string) {
  if (str.length % 2 !== 0) return false;

  for (let i = 0; i < str.length; i++) {
    const par = str[i];
    if (par === "(") {
      arrayStack.push(")");
    } else if (par === "[") {
      arrayStack.push("]");
    } else if (par === "{") {
      arrayStack.push("}");
    } else {
      let c = arrayStack.pop();
      if (par !== c) {
        return false;
      }
    }
  }

  return arrayStack.isEmpty();
}
console.log(matchParenthese("{[]}()"));
// console.log(matchParenthese("()"));
