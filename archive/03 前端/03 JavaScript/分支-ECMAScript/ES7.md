
# 1. includes

`includes`是用来检测数组中是否包含某个元素

```javascript
const num = [1, 2, 3, 4, 5, NaN];
// 1.以前的处理方式
if (num.indexOf(1) !== -1) {
  console.log("该数字存在~");
}

// 2.使用includes的处理方式
// 第一个参数 查找的值
// 第二个参数 从第几个索引开始
if (num.includes(2, 1)) {
  console.log("该数字存在~");
}
// 它比indexOf好的地方在于它可以判断NaN
console.log(num.includes(NaN));
```

# 2. 指数运算符

```javascript
// 1. 以前的处理方式
Math.pow(2, 3) // 8

// 2. 使用指数运算符的处理方式
2 ** 3 //8
```
