# 1 let/const



# 2 块级作用域

## 2.1 基本介绍

使用`var`可以读取到的，书写块级作用域无效

```javascript
{
  var a = 123;
}
console.log(a);
```

假如你使用`let/const/function/class`的话，就找不到了。但是实际情况是`function`依旧可以获取到，因为做了一个特殊的处理

```javascript
{
  let a = 123;
  function fn() {}
  class Person {}
}
console.log(a, fn, Person);
```

![[00 assets/650e1f12362fe10dffb8e4714012a623_MD5.png]]

## 2.2 使用场景

其中`if/switch/for`可以理解为一个块级作用域，也就是被包裹的语句可以理解为和`{ }(块级作用域)`是一样的

```javascript
if (true) {
  var name = "张三";
}

let color = "red";
switch (color) {
  case "red":
    let name = "李四";
    break;
}

for (let i = 1; i < 10; i++) {
  console.log(i);
}
```

其中`for`对于块级作用域最常见，比如说下面的这个场景，我们获取到元素并且给他添加点击事件。

![[00 assets/5766016fa8bc31270b18a9577e4fced8_MD5.png]]

但是我们在函数内部获取`i`的时候，一直都是`i`的最大值。因为我们定义`var`的时候块级作用域约束不到他，所以他会添加到全局，所以获取到的就是`for循环`加到最大值

![[00 assets/477c9b71362711aa8de4a9b66f30768e_MD5.png]]

假如需要解决的话，就需要使用到函数作用域来处理

![[00 assets/9dbd37f71c7925eb1db627a8c48d2e16_MD5.png]]

或者直接使用`let`来处理也可以，这样处理是最好的

![[00 assets/12d250d4636f7f86296b92de23be6e88_MD5.png]]

## 2.3 for 中的 let

实际上我们在使用`for`来遍历的时候，是创建一个个的块级作用域。假如是`var`的话就是一个`var`，所以每个块级作用域访问的时候都是访问的这个`var`

![[00 assets/7acd4eb6b7341959965ff5f3ea8743ba_MD5.png]]

## 2.4 暂时性死区

![[00 assets/ec767f4dc379930c7451be0ed4665951_MD5.png]]

假如按照`var`来写的变量，在初始的时候会将改该变量写入`GO`中，为`undefined`。所以访问不会报错，但是没有值

![[00 assets/c613060ae00eca24f324b662c1054450_MD5.png]]

假如我们只要块级作用域中使用了`let/const`的话，就会报错了。

![[00 assets/4880667dce0cd2d92c95423bbff1eef2_MD5.png]]



# 4 模板字符串


# 5 对象简化写法

下面为一个简写的形式来编写对象中的属性

```javascript
let name = "张三";
let say = function () {
  console.log("Hello Warld!");
};

const person = {
  // 1. 属性的简写
  name,
  say,

  // 2. 方法的简写
  dothing() {
    // 不是箭头函数的语法糖，所以this是调用者，不是上层作用域
    console.log("Just do it!");
  },

  // 3. 计算属性的简写
  [name + " zs"]: "key可以拼接",

  // 属性和方法以前的写法
  // name:name,
  // say:say,
  // dothing:function(){
  //     console.log('Just do it!');
  // }
};
// 计算属性以前的写法
person[name + " zss"] = "key可以拼接"

console.log(person);
```

![[00 assets/d8251b9e441c51fc91d2ccad267777a8_MD5.jpeg]])


# 10 Symbol


# 11 迭代器


# 12 生成器

^bbfc74

## 12.1 基本介绍

`生成器`就是一个特殊的`迭代器`，使用`yield`是划分代码块的，也就是`分隔符`

![[00 assets/4a6450a3a9eadc2237da20fe1de09266_MD5.png]]

既然是`特殊的迭代器`，那么我们使用`for of`来遍历循环也可以

![[00 assets/b924129e8b1686ba2f62146bbe887038_MD5.png]]

## 12.2 返回值/参数

1、其中`yield`是暂停函数的执行，后面的参数是作为返回值。`return`表示结束函数

![[00 assets/e0c4809a11b501b5813817ffa0d4d4e6_MD5.png]]

2、要给第二段代码中传入参数就需要从第一个`yield`的返回值获取

![[00 assets/09060bc21258524364f694b70824c504_MD5.png]]

3、这里需要强调一个点就是关于给 next() 传递参数的问题，你执行 next() 其实是执行 yield 之上的代码，可以理解为一个指针指向到了 yield 这行，并且这个指针是指向到 "=" 这里，也就是还没执行赋值操作

4、当你执行下一个 next 函数的时候，传递的参数才会进行赋值操作，可以查看下图来理解其中的顺序关系

![[00 assets/2e8c8f962dfc68cc457b76076b3d4f29_MD5.png]]

## 12.3 终止执行

![[00 assets/9f656737ec6ea55e69a5cc70e843d0d5_MD5.png]]

## 12.4 抛出异常

使用`throw()`可以抛出异常，抛出异常的位置在上一个`yield`。假如你是要`try-catch`来包裹的话，依旧会执行第二段代码，也就相当于你使用`throw()`顺便执行了`next()`和`报错`

![[00 assets/25e658971b750a6fde606f43fd089202_MD5.png]]

# 16. Promise

^872c8d

[[Primise]]

# 14 Set


# 15 Map

## 15.1 基本介绍

![[00 assets/7f81ae26d37cd1aa0bc256a63ef9056b_MD5.png]]

```javascript
//set方法就是添加值
let obj1 = { name: "张三" };
let obj2 = { name: "李四" };

let m = new Map();
// 1.可以使用字符串为key
m.set("name", "张三");
m.set("say", function () {
  console.log("hi");
});
console.log(m);

// 2.可以使用对象作为key
m.set(obj1, ["湖北", "上海", "南京"]);
console.log(m);

// 3.也可以使用entries数组来创建
const m1 = new Map([
  [obj1, "赵六"],
  [obj2, "王五"],
  ["name", "张八"],
]);
console.log(m1)
```

![[00 assets/d689898237809c436fe6ff4601e25721_MD5.png]]

## 15.2 常见方法

![[00 assets/8bd288c2ff02f924fb1612798ee92e7f_MD5.png]]

当然 Map 还有其他的一些 API

```javascript
//set方法就是添加值
let m = new Map();
let address = {
	name:'房子',
	num:18
};
m.set('name','张三');		// 1. set添加
m.set('say',function(){
	console.log('hi');
});
m.set(address,['湖北','上海','南京']);
console.log(m);

m.size;				//2. 获取Map键的个数
m.delete(name);		//3. 删除
m.get('say')		//4. 获取
m.clear();			//5. 清空
```

```javascript
let obj1 = { name: "张三" };
let obj2 = { name: "李四" };

const m = new Map();

m.set(obj1, "1");
m.set(obj2, "2");
m.set("name", "赵六");

// 6.遍历
for (let [key, value] of m) {
  console.log(key, value);
}
m.forEach((ele, key) => {
  console.log(key, ele);
});
```

![[00 assets/b0c9990bf559a09b857bfa3aa753c4ff_MD5.png]]

## 15.3 WeakMap

![[00 assets/3b3c34c6170732777ecbe890d835746f_MD5.png]]

因为`WeakMap`没有实现迭代器，所以不能被遍历

```javascript
let obj = {};

let ws = new WeakMap();

ws.set(obj, "张三"); // 1. 添加
console.log(ws.get(obj)); // 2. 获取
console.log(ws.has(obj)); //3. 是否存在
ws.delete(obj); // 4. 删除

console.log(ws);
```

![[00 assets/7dd3d8d07a5db8ce32a182cf5b024107_MD5.png]]

`WeakMap`得应用场景比`WeakSet`好很多，其中就是就是`Vue3`得响应式场景

下面只是表示的只是`Vue3`响应式得数据存储得方式，其主要得存储方式为：`WeakMap => Map => Function`。也就是在`WeakMap`中存储`Map`，在`Map`中存储的对应得对象中每个`Key`存储对应得函数。

但是下面并没有加上响应式得代码。假如想看响应式得代码可以参考`Proxy`得笔记

```javascript
const obj = {
  name: "张三",
  age: 18,
};

function ObjNameFn1() {
  console.log("ObjNameFn1执行");
}
function ObjNameFn2() {
  console.log("ObjNameFn2执行");
}
function ObjAgeFn1() {
  console.log("ObjAgeFn1执行");
}
function ObjAgeFn2() {
  console.log("ObjAgeFn2执行");
}

let ObjWeakMap = new WeakMap();
let ObjMap = new Map();
ObjMap.set("name", [ObjAgeFn1, ObjAgeFn2]);
ObjMap.set("age", [ObjAgeFn1, ObjAgeFn2]);
ObjWeakMap.set(obj, ObjMap);

let ObjNameFnArr = ObjWeakMap.get(obj).get("name");
ObjNameFnArr.forEach((ele) => {
  ele();
});
```

![[00 assets/88a811ee894cee3b376b1174387110e5_MD5.png]]

# 16 class

可以通过 class 来定义类，这个写法只是让对象原型的写法更加清晰、更像面向对象编程的语法

```javascript
//构造函数
function Person(name,age){
	this.name = name;
	this.age = age;
}
//向里面添加方法
Person.prototype.say = function(){
	console.log('你好!');
}

//对象
let p1 = new Person('张三',12);
p1.say();
console.log(p1);
```

上面是 ES5 构造函数的方法，但是在 ES6 里面就不一样了，下面我们就可以使用 class 来实现 constructor 就是构造函数，记住名字不能修改，只能使用这个

```javascript
class Person{
	//构造函数，名字不能修改
	constructor(name,age) {
		this.name = name;
		this.age = age;
	}
	say(){
		console.log('你好');
	}
}
let p1 = new Person('张三',10);
console.log(p1);
```

## 16.1 静态类成员

首先我们需要知道一点，就是函数也是一个函数对象

下面的 name 和 say 是给函数对象 Person 的属性，所以我们实例化的对象就不能没有相应的值

```javascript
function Person(){}
Person.name = '张三';
Person.say = function(){
	console.log('你好!');
}
let p1 = new Person();
console.log(p1.name);
```

但是原型属性是一样的

```javascript
function Person(){}
Person.prototype.name = '张三';
let p1 = new Person();
console.log(p1.name);
```

其实实质就是静态成员，也就是下面的这个方式，我们可以参考 Java 的 class，其实和他基本是一致

```javascript
class Person{
	static name = '张三';
}
let p1 = new Person();
console.log(p1.name);
```

## 16.2 继承

这是 ES5 的继承

```javascript
// 父级构造函数
function Person(name,age){
	this.name = name;
	this.age = age;
}
//父级方法
Person.prototype.say = function(){
	console.log('你好!');
}
//子级构造函数
function boy(name,age,sex,hight){
	Person.call(this,name,age);	//这里的call()是改变了this的指向
	this.sex = sex;
	this.hight = hight;
}

//设置子级构造函数原型
boy.prototype = new Person();
boy.prototype.constructor = boy;

boy.prototype.play = function(){
	console.log('我会玩游戏');
}

let p1 = new boy('张三',18,'男',180);
p1.say();
```

这是 ES6 的继承，其基本结构和 C#也是差不多的

```javascript
class Person{
	constructor(name,age) {
		this.name = name;
		this.age = age;
	}
	say(){
		console.log('Hi!');
	}
}
class boy extends Person{
	constructor(name,age,sex) {
		super(name,age);
		this.sex = sex;
	}
	play(){
		console.log('play');
	}
}
let p1 = new boy('张三',10,'男')
p1.say();
```

## 16.3 子类对父类的重写

最后的结果就是 Hello!，重写就是和父类同名的方法进行独自的编辑

```javascript
class Person{
	constructor(name,age) {
		this.name = name;
		this.age = age;
	}
	say(){
		console.log('Hi!');
	}
}
class boy extends Person{
	constructor(name,age,sex) {
		super(name,age);
		this.sex = sex;
	}
    say(){
        console.log('Hello!');
    }
	play(){
		console.log('play');
	}
}
let p1 = new boy('张三',10,'男')
p1.say();
```

![[00 assets/69381750b28764deed8e7a5a33641cf0_MD5.png]]

## 16.4 getter 和 setter

```javascript
class Person{
	get say(){
		console.log('Hi!');
		return '1';
	}
	set say(a){
		console.log(a);
		console.log(2);
	}
}
let p1 = new Person()
console.log(p1.say);	//当你调用的时候就会触发
//但是要注意是后面没有括号，所以不是单纯的方法调用
p1.say = 12		//当你赋值的时候就会触发
```

# 17. 数值扩展

**Number.EPSILON**，表示 JS 里面最小精度

```javascript
equal = (a,b) => Math.abs(a-b) < Number.EPSILON;
console.log(equal(0.1+0.2,0.3));	//true
console.log(0.1+0.2===0.3);			//false
```

**二进制和八进制**

```javascript
let er = 0b1000;	//二进制0b
let ba = 0o7000;	//八进制0o
let si = 123;		//十进制
let liu = 0xff;		//十六进制0x
```

**检测**

```javascript
console.log(Number.isFinite(100));	//检测是否为有限值
console.log(Number.isNaN(NaN));		//是否为NaN
console.log(Number.isInteger(1));		//是否为整数
console.log(Number.sign(1));		//是否为正数，0，负数
```

**转换**

```javascript
console.log(Number.trace(1.1));
```

# 18. 对象方法扩展

**判断**，这也是和===最大的区别

```javascript
console.log(Object.is(NaN,NaN));	//true
console.log(NaN === NaN);	//false
```

**覆盖**，这里的 p2 会将 p1 覆盖掉，属性名是一样的话就会覆盖，p1 没有的，p2 有的，会添加上去，p1 有的，p2 没有的，也不会消失

```javascript
let p1 = {
	name:'张三',
	age:12,
	say(){
		console.log('1');
	}
}
let p2 = {
	name:'李四',
	age:19,
	add:'四合院'
}
console.log(Object.assign(p1,p2));
```


# 20 Proxy


# 21. Reflect

[[Reflect]]

# 99. 案例

## 99.1 let 实践

我们来看下面的下面的问题出在哪里

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
				border: 1px solid red;
				float: left;
			}
		</style>
	</head>
	<body>
		<div></div>
		<div></div>
		<div></div>
		<script type="text/javascript">
			let divs = document.querySelectorAll('div');
			for(var i=0;i<divs.length;i++){
				divs[i].onclick = function(){
					divs[i].style.background = 'pink';
				}
			}
		</script>
	</body>
</html>
```

其实是 for 循环的问题，其实最后 i 的值会到 3，当你点击方块的话 _divs[i].style.background = 'pink';_ 其中的 i 就是 3，所以会报错

```javascript
{
	//i = 0;
	divs[0].onclick = function(){

	}
}
{
	//i = 1;
	divs[1].onclick = function(){

	}
}
{
	//i = 2;
	divs[2].onclick = function(){

	}
}
```

```
console.log(i);			//查看i的值
```

假如我们修改的话，可以这样修改

```javascript
let divs = document.querySelectorAll('div');
for(let i=0;i<divs.length;i++){
		divs[i].onclick = function(){
		divs[i].style.background = 'pink';
	}
}
```

为什么可以这样修改呢，这是因为 var 的 i 是全局作用域，但是 let 的话是局部作用域，换成 let 的话就是这样的，其中 i 是不会互相影响的，所以没问题

```javascript
{
	let i = 0;
	divs[0].onclick = function(){

	}
}
{
	let i = 1;
	divs[1].onclick = function(){

	}
}
{
	let i = 2;
	divs[2].onclick = function(){

	}
}
```

假如我们不想改 var i 的话可以这样

```javascript
let divs = document.querySelectorAll('div');
for(let i=0;i<divs.length;i++){
		divs[i].onclick = function(){
		this.style.background = 'pink';
	}
}
```

## 99.2 箭头函数实践

我们来看下下面这个为什么不能运行

这是因为这里面的 this 指向的是 window，所以不能成功运行

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.main{
				width: 200px;
				height: 200px;
				background-color: red;
			}
		</style>
	</head>
	<body>
		<div class="main"></div>
		<script type="text/javascript">
			const main = document.querySelector('.main');
			main.onclick = function(){
				setTimeout(function(){
					this.style.background = 'pink';
				},2000);
			}
		</script>
	</body>
</html>
```

解决方法，在前面保存 this 的值就可以了

```javascript
const main = document.querySelector('.main');
main.onclick = function(){
    let _this = this;
	setTimeout(function(){
		_this.style.background = 'pink';
	},2000);
}
```

但是我们学了箭头函数，所以这里我们可以使用箭头函数来完成，这是因为箭头函数是静态的，始终指向函数声明时所在的作用域下的 this 的值

```javascript
const main = document.querySelector('.main');
main.onclick = function(){
	setTimeout(()=>{
		this.style.backgroundColor = 'pink';
	},2000);
}
```

下面是从数组中返回偶数的元素

```javascript
var num = [32, 33, 16, 40];
const result = num.filter(function(item){
	if(item % 2 === 0) return true;
	else return false;
});
console.log(result);
```

但是我们使用箭头函数来表示的话

```javascript
var num = [32, 33, 16, 40];
const result = num.filter(item => item % 2 === 0);
console.log(result);
```

所以我们总结的话，就是箭头函数适合与 this 无关的回调，比如说定时器，数组方法的回调

## 99.3 扩展运算符实践

**数组和并**

```javascript
//使用对象方法
const arr = ['a','b'];
const arr1 = ['c','d'];
const arr_con = arr.concat(arr1);
console.log(arr_con);

//使用扩展运算符
const arr = ['a','b'];
const arr1 = ['c','d'];
const arr_con = [...arr,...arr1];
console.log(arr_con);
```

**数组克隆**，但是注意这个是浅拷贝

```javascript
const arr = ['a','b'];
const arr1 = [...arr];
console.log(arr_con);
```

**伪数组转换**，这就是上面 rest 参数的使用

```javascript
const divs = document.querySelectorAll('.div');
const divs_arr = [...divs];
console.log(divs_arr);
```

## 99.4 生成器函数实践

需求是 1s 后输出 1，2s 后输出 2，3s 后输出 3

我们可以使用这样的方法，但是这样的方法很不好看，而且不好维护，这也被称为回调地狱

```javascript
setTimeout(()=>{
	console.log('1');
	setTimeout(()=>{
		console.log('2');
		setTimeout(()=>{
			console.log('3');
		},3000);
	},2000);
},1000);
```

假如我们使用生成器的话

```javascript
function one(){
	setTimeout(()=>{
		console.log('1');
		Iterator.next();
	},1000)
}
function two(){
	setTimeout(()=>{
		console.log('2');
		Iterator.next();
	},2000)
}
function three(){
	setTimeout(()=>{
		console.log('3');
	},3000)
}
function * fn(){
	yield one();
	yield two();
	yield three();
}
let Iterator = fn();
Iterator.next();
```

假如我们改为订单数据的话，我们要获取里面的值的话，就可以使用 next 方式来传递值

```javascript
function one(){
	setTimeout(()=>{
		let name = '张三'
		Iterator.next(name);
	},1000)
}
function two(){
	setTimeout(()=>{
		let age = 18;
		Iterator.next(age);
	},2000)
}
function three(){
	setTimeout(()=>{
		let sex = '男'
		Iterator.next(sex);
	},3000)
}
function * fn(){
	let name = yield one();
    console.log(name);
	let age = yield two();
    console.log(age);
	let sex = yield three();
    console.log(sex);
}
let Iterator = fn();
Iterator.next();
```

## 99.5 Promise 实践

假如我们使用回调地狱来做的话就是下面这个样子

需求是将 3 个文件依次链接在一起

```javascript
fs.readFile('./1.txt',(err,data1)=>{
	fs.readFile('./1.txt',(err,data2)=>{
		fs.readFile('./1.txt',(err,data3)=>{
			let result = data1 + '\n' + data2 + '\n' + data3;
			console.log(result);
		});
	});
});
```

这个就可以避免回调地狱了，但是说句实话，理解了之后再看的话可能是挺方便的，但是观感确实没有回调地狱好看，可能是我水平不是很够吧

```javascript
const fs = require('fs');

//第一个Promise，读取1.txt
const p = new Promise((resolve, reject) => {
	fs.readFile('./1.txt', (err, data) => {
		resolve(data);	//将1.txt传达then()里面value
	});
});

p.then(value => {	//此时这里的value表示的是1.txt
	return new Promise((resolve, reject) => {
		fs.readFile('./2.txt', (err, data) => {
			resolve([value,data]);
	//这个时候就是一个数组,[1.txt,2.txt],我们将他传给then()
		});
	})
}).then(value => {	//采用链式调用，返回值给了他
	return new Promise((resolve, reject) => {
		fs.readFile('./3.txt', (err, data) => {
			value.push(data);	//将3.txt压进数组里面[1.txt,2.txt,3.txt]
			resolve(value);	//再将数组传出来
		});
	})
}).then(value => {	//数组传到了这个value的值里面
	console.log(value.join('\n'));	//我们将数组连接
});
```

## 99.6 set 实践

**数据去重**

但是这里不是数组去重，而是 set 数据

```javascript
let arr = ['1','2','3','4','5','1'];
let result = new Set(arr);
console.log(result);
```

![[00 assets/994c25a8cf6545479444f3c5fc4d23cc_MD5.png]]

这里我们使用扩展运算符，将数组序列转换为数组

```javascript
let arr = ['1','2','3','4','5','1'];
let result = [...new Set(arr)];
console.log(result);
```

![[00 assets/71a7e5545066aa591ecf835291540435_MD5.png]]

**交集**

```javascript
let arr = [1,2,3,4,5,1];
let arr2 = [2,3,3,4];
let result = [...new Set(arr)].filter(item => {
	let s2 = new Set(arr2);
	if(s2.has(item)){
		return true;
	}else{
		return false;
	}
});
console.log(result);

//当然我们也可以简化一下
let arr = [1,2,3,4,5,1];
let arr2 = [2,3,3,4];
let result = [...new Set(arr)].filter(item => new Set(arr2).has(item));
console.log(result);
```

**并集**

```javascript
let arr = [1,2,3,4,5,1];
let arr2 = [2,3,3,4];
let s = [...new Set([...arr,...arr2])];
console.log(s);
```

**差集**，其实就是交集取反

```javascript
let arr = [1,2,3,4,5,1];
let arr2 = [2,3,3,4];
let result = [...new Set(arr)].filter(item => !(new Set(arr2).has(item)));
console.log(result);
```
