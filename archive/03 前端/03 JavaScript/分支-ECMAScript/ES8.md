
# 1 values/keys

```javascript
let Person = {
  name: "张三",
  say() {
    console.log("Hi!");
  },
  love: ["篮球", "足球", "羽毛球"],
};
console.log(Object.keys(Person)); // 获取对象中所有得keys
console.log(Object.values(Person)); // 获取对象中所有得values
```

![[00 assets/fc3e7d6d418542737fce3c1ccbdcb935_MD5.png]]

当然`values()`也可以来拆分字符串

![[00 assets/65cf1a137366148893615a7cc89ac1a0_MD5.png]]

# 2 entries

将传入得数据转换为`[[keys,value]]`得形式，为了方便遍历得操作

![[00 assets/081dbb657fe76c6d90a08ce131c3607b_MD5.png]]

# 3 padding

对字符串得首尾进行填充，第一个参数为填充之后得字符串得长度，第二个参数是要填充得字符

![[00 assets/bda1ebacddc748e20ce71673908ead21_MD5.png]]

# 4. getOwnPropertyDescriptors

返回指定对象所有自身属性的描述对象

```javascript
let Person ={
	name:'张三',
	say(){
		console.log('Hi!');
	},
	love:['篮球','足球','羽毛球']
}
console.log(Object.getOwnPropertyDescriptors(Person));
```

![[00 assets/77d47b1ff429d8b5ba33bd21b37d17bc_MD5.png]]

