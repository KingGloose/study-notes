# 1 let/const

## 1.1 let

其中声明变量这里基本和 var 是一样的，可以支持一次声明多个变量

```javascript
let a = 123 , b = 'wang' , c = {
	name:'zhang',
	age:12
};
```

但是有一个问题和 var 不一样，var 是支持多次声明一样的变量，但是 let 一次只能声明一个，不能重复声明

```javascript
let a = 123;
let a = 12;
```

其中 let 和 var 最大的区别就是不存在变量提升，而且 var 是函数作用域，而 let 是块级作用域

## 1.2 const

```javascript
// 常量一定要赋初始值
const name = "张三";

name = "李四" // 报错，常量不能修改

console.log(name);
```

假如我们要传递引用类型的话。结果是不会报错的，这是因为，我们保存的是`obj`的地址值

![[00 assets/cdafff26c6426c11c54db501a69d8928_MD5.png]]

## 1.3 作用域提升

假如是使用 var 的话是存在变量声明提前的，所以最后的结果是 undefined

```javascript
console.log(a);
var a = 123;

//效果其实是下面的这样

var a;
console.log(a);
a = 123;
```

假如我们使用 let 的话就会报错，这是因为他不存在变量声明提前

```javascript
console.log(a);
let a = 123;
```

但是事实并非如此

![[00 assets/b33cb5c9b3149643467a8205c2d5ba96_MD5.png]]

![[00 assets/ec775425b0fc134497a1b3cacc4901b2_MD5.png]]

## 1.4 和 window 关系

在以前的`var`声明的对象都会添加到`window`中，因为在`GO`中的`window`指向的是`this`，所以在全局创建的变量都会保存到`GO`中，也就是`window`

![[00 assets/d853e64dde1ff5babc2db101876c4583_MD5.png]]

但是在`ES6`之后，这个可以参考我`JS高级 - 环境`的笔记。

原本的`GO(VO)`是一个对象，保存变量的时候直接就是`GO.name = "张三"`。但是在现在是`VE`，不是一个对象，最后的数据都会保存在`variables_`，他的数据类型是`VariableMap`，他是一个`HashMap`，也就是一个哈希表，底层通过`C++`实现

因为以前都是`window`指向着`GO`，但是现在使用`let/const`就不会保持同步了。

![[00 assets/c704a72f5d0489e063bc6782c80b922d_MD5.png]]

下面为`variables_`的源码，下面的注释就已经写了

![[00 assets/ddcd9e409eaa5e43cdf1dbc10291820f_MD5.png]]


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

## 2.5 var/let/const 选择

![[00 assets/204db614c373655d9cf226c2820dfce8_MD5.png]]

# 3 变量的解构赋值

允许按照一定模式从数组和对象中提取值，对变量进行赋值，这被称为解构赋值

## 3.1 数组结构

```javascript
var PersonName = ["张三", "李四", "王五", "赵六"];

// 1. 对数组进行解构，因为数组没有key，所以他的结构是按照顺序的
let [item1, item2, item3, item4] = PersonName;
console.log(item1, item2, item3, item4);

// 2. 解构后面的元素
let [, , , items] = PersonName;
console.log(items);

// 3. 解构出一个元素，后面的元素放在一个新数组中
let [item11, item22, ...itemss] = PersonName;
console.log(item11, item22, itemss);

// 4. 解构的默认值
let [itema, itemb, itemc, itemd, iteme = "老七"] = PersonName;
console.log(itema, itemb, itemc, itemd, iteme);
```

![[00 assets/460f98bbaa6ec8994bc43ad38d42520b_MD5.jpeg]]

对于`解构赋值`得数组形式，还有一个用途就是交换数据，不需要声明第三方变量

![[00 assets/5e1330e0071facf6501b60633583d7a0_MD5.jpeg]]

## 3.2 对象结构

其基本结构和上面的数组结构是一样的，但是一点，里面的名字必须要和对象里面的值要是一样的，其中 say 就是对应的里面的方法

```javascript
const Person = {
  name: "赵本山",
  age: 18,
  say: function () {
    console.log("我会说话");
  },
};
// 1. 对象解构
let { name, age, say } = Person;
console.log(name);

// 2. 对解构的属性进行赋值
let { name: newName } = Person;
console.log(newName);

// 3. 对属性赋默认值
let { address: NewAddress = "北京市" } = Person;
let { address = "北京市" } = Person;
console.log(NewAddress, address);
```

![[00 assets/a759fedf9cc6418add4dedf33ed315e9_MD5.png]]

## 3.3 解构场景

![[00 assets/d1e025428ccf168ace8b4ddcc73b710a_MD5.png]]

# 4 模板字符串

## 4.1 基本使用

1、一个新的声明字符串的方式，也就是 tab 上面的键

```javascript
let a = `Hello Warld!`;
```

以前的 ‘ ’ 和 “ ” 是不能直接出现换行符的，但是模板字符串是可以的，下面这个就不会报错

```javascript
let a = `aaaa
		 bbbb
		 cccc`;
console.log(a);
```

2、还有一个特性就是变量拼接

```javascript
let a = 'aaa';
let b = a + 'bbb';
//变量拼接的方法
let a = 'aaa';
let b = `${a}bbb`;
```

我们书写函数，其返回值也可以编入到模板字符串中

![[00 assets/a1aa93cb2f9347a841a5e57486eb3a11_MD5.png]]

3、并且使用模板字符串会将插入的字符串都使用`toString()`来转为字符串再插入

![[00 assets/20e25ad4ac0c375af059247dd0324536_MD5.jpeg]]

## 4.2 标签模板字符串

我们也可以直接在函数的后面编写**``**，这样可以直接执行该函数。其中第一个参数就是**非变量参数**，后面的就是**${ }**中的值

![[00 assets/c24b7441021f26a8cbb66b9d56d76ac1_MD5.png]]

假如我们在后面编写字符串的话，就会自动切割`${ }`数据和非`${ }`字符串。

![[00 assets/f0d8eae5a3258c55af55108bfd594ac3_MD5.png]]

在`React`中的`styled-components`中是一种比较常用这种模式

![[00 assets/df0365131fab7962101d59ae99d83b76_MD5.png]]

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

# 6 箭头函数

这是箭头函数的创建

```javascript
let fn = (a) =>{
    console.log('这是一个箭头函数'+a);
}
fn(1);

//箭头函数的省略写法
//1.省略小括号 当形参只有一个的时候
let fn = a =>{
    return a * a;
};
fn(2);
//2.省略大括号 当代码体只有一条语句 而且要注意的是return也要省略 其语句执行的结果就是函数的返回值
let fn = a => a * a;
fn(2);
```

**this**是静态的，this 始终指向函数声明时所在的作用域下的 this 的值

其中 fn2 在经过 call()方法的影响下时不会改变的，所以说白了，就是箭头函数里面 this 所指的对象是不会改变的

```javascript
function fn1(){
	console.log(this.name);
}
let fn2 = () =>{
	console.log(this.name);
}
window.name = '张三';
const person = {
	name:'王五'
}
fn1();
fn2();
fn1.call(person);
fn2.call(person);
```

**不能作为实例化**

```javascript
let person = (name,age) =>{
	this.name = name;
	this.age = age;
}
let boy = new person('张三',12);
console.log(boy.name);
//最后的结果是会报错的
```

**不能使用 arguments 变量**，具体的 arguments 的用法可以参考我的 JS 笔记里面记录的

```javascript
let fn = () =>{
	console.log(arguments);
}
fn(1,2,3,4,5);
```

箭头函数不存在`显式`的`arguments`

# 7 函数参数默认值

**形参初始值**，可以设置有默认初始值的参数

```javascript
function fn(a,b,c=10){
	return a + b + c;
}
fn(1,2);

//但是要记住，一般有参数的值要靠到最后，这是因为，1给了a，2给了b，但是c是空的，所以最后算不出来
function fn(a,b=10,c){
	return a + b + c;
}
fn(1,2);
```

**解构赋值结合**，而且假如你在对象里面没写 age 的值的话，也可以写一个初始值

![[00 assets/45757d08a7520b8841ea013abb5f511b_MD5.png]]

或者可以使用这种写法

![[00 assets/ef59fc4fb65e8b38d6039a26572cd896_MD5.jpeg]]

# 8 剩余参数

他们的语法有点像，但是要记住以前的方法是定义为一个对象，但是 rest 参数是定义为一个数组，这样的话就可以使用数组的方法来处理了

```javascript
//ES5的方法，也就是我JS笔记里面
function fn(){
	console.log(arguments);
}
fn('a','b','c');

//ES6的方法，也就是rest参数
function fn1(...args){
	console.log(args);
}
fn1('a','b','c');

//注意一个点，rest参数要放在最后
function fn2(a,b,...args){
    console.log(a + b + args);
}
fn2(1,2,3,4,5,6);
```

# 9 扩展运算符

" ... "扩展运算符能将数组转换为逗号分隔为参数序列

注意这个，他只有一个参数

```javascript
const person = ['张三','李四','王五'];
function fn(){
	console.log(arguments);
}
fn(person);
```

![[00 assets/76a8ccf5ac948805320babf439e72abf_MD5.png]]

但是我们使用扩展运算符的话，就把原本的数组分为三个了，你使用 arguments[0]的话就是张三，假如不使用扩展运算符的话就是数组对象

```javascript
const person = ['张三','李四','王五'];
function fn(){
	console.log(arguments);
}
fn(...person);

//其本质是
function fn(){
	console.log(arguments);
}
fn('张三','李四','王五');
```

![[00 assets/1faff29c480debd0c170bcb2985eb36b_MD5.png]]

# 10 Symbol

## 10.1 基本介绍

1、`ES6`引入了一个新的原始数据类型`Symbol`，表示独一无二的值，它是 JS 的第七种数据类型

![[00 assets/4944232ebb70086edb1810dc73df9b0c_MD5.png]]

2、`Symbol`实例是唯一、不可变的，可以用作**非字符串形式的对象属性**，所以使用他没有属性冲突的危险

![[00 assets/138a72af043c8d9c7b703d706a1bd746_MD5.png]]

## 10.2 基本使用

### 10.2.1 Symbol()

1、创建一个`Symbol`实例，这里可以这样理解，`Symbol`是身份证，里面的值是`名字`，`名字`可以一样，但是`身份证`不能一样

2、并且`Symbol`不能实例化，只能使用函数的形式

![[00 assets/5336ce5daae61a67ab2d7fad1d594f0c_MD5.png]]

### 10.2.2 Symbol.for()

1、如果想在全局的注册表中创建，可以使用`Symbol.for()`来创建`Symbol`，它会对传入的`key`做**幂等操作**，也就是会先检测`全局注册表`，如果没有就创建该实例放入`全局注册表`中，如果有的话就直接返回已经创建好的`Symbol`实例

如果想详细知道幂等操作可以查看下面的链接：[(1 封私信 / 80 条消息) 什么是幂等？如何解决幂等性问题？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/534651475)

![[00 assets/b6694fc4898743d5abc7ac5bc86c973a_MD5.png]]

2、并且直接使用`Symbol.for()`全局注册表中创建的`Symbol`实例和直接使用`Symbol()`创建的`Symbol`实例也不相同

![[00 assets/8fc881d6b382fc7b0ef98e100d410990_MD5.png]]

### 10.2.3 Symbol.keyFor()

1、使用`Symbol.keyFor()`来在`全局注册表`中查找对应的`key`，否则就返回`undefined`

![[00 assets/d3095b0b9536fd535bd4ccc1a2dcb190_MD5.png]]

## 10.3 对象属性

1、一般情况下`Symbol`是为了给对象设置独一无二的属性名的，下面就是其中一个应用场景

2、使用`Object.getOwnPropertyNames`和`Object.getOwnPropertySymbols`可以分别获取`name`和`symbol`名

3、如果想要获取`name`和`symbol`的话，可以使用`Reflect.ownKeys`来获取

![[00 assets/afb24503739ae480fc7b3518917694e0_MD5.png]]

4、使用`Object.getOwnPropertyDescriptors`也可以获取所有的`key`包括`Symbol`，并且获取对应属性的描述

![[00 assets/f07901221c730809f47d19e34254df86_MD5.png]]

5、当然我们可以使用`Object.defineProperty`来为对象创建对应的`Symbol key`

![[00 assets/dce48f17fe3e8b892cb100a4bb42c9e8_MD5.png]]

假如想进一步了解的话可以参考这个网站：[Symbol - ECMAScript 6 入门 (ruanyifeng.com)](https://es6.ruanyifeng.com/#docs/symbol)

**注意**：同时这里有一个小细节，我们使用 `defineProperty` 添加的属性，如果我们后续即便重新覆盖了一遍，依旧会保留该属性值的属性，可以参考下图

![[00 assets/565d1e2b2603ee47469831cab90624ab_MD5.png]]

## 10.4 遍历 Symbol

![[00 assets/f7fe2f1367124b92c5a0276fd8911ad9_MD5.png]]

## 10.5 内置 Symbol

### 10.5.1 Symbol.asyncIterator

1、当然除了普通的同步迭代器，还存在一个异步迭代器，我们使用`Symbol`也是可以模拟出来的，它会根据迭代的方式，一步步按照同步的方式来执行，每隔 3s 就会进行下一步

![[00 assets/3fe37c0e3eb211e13ab8e635c2438cb9_MD5.png]]

2、下面是使用`生成器yield`来实现的异步迭代器

![[00 assets/09b8e6bc58e01cd93c09a9eb75119963_MD5.png]]

下面是`JS高级程序设计`中的异步迭代器，实现的功能基本类似

![[00 assets/b9a0f612f7ae9800bceff121d4311403_MD5.png]]

3、但是我一直挺好奇这个异步迭代器的具体使用场景在那里

4、**注意**：上述我都是自己写了迭代器来使用，如果我不使用迭代器来使用的话，就存在下面的问题。比如我自己写的迭代器，也是按照 JS 高级程序设计中编写的，时间图应该是这样的，所以总共是 9s

![[00 assets/646a41eb242c424f612e4b438f945bc0_MD5.png]]

但是我自己来写一个 Promise 数组的话，时间图是这样的，也就是总时长是 3s，和预期不一样，这就和`Promise.all`是一样的

![[00 assets/3e964a84919385b8d6d2b7e6d769a34d_MD5.png]]

暂时不是很清楚上面代码那里存在问题，如果以后的我看到后可以解答一下

### 10.5.2 Symbol.hasInstance

1、检测构造器对象是否认可一个对象是它的实例，一般情况下使用`instanceof`操作符来处理，在`ES6`之后使用`Symbol.hasInstace`来处理

![[00 assets/dccd414cc4a262464b7f72753d42d7b4_MD5.png]]

### 10.5.3 Symbol.isConcatSpreadable

![[00 assets/48cdee1fa4acb4bad5d3eecd36c7bdfd_MD5.png]]

### 10.5.4 Symbol.iterator

参考 14.迭代器

### 10.5.5 Symbol.match

1、默认情况下使用`String.match`是使用`Symbol.match`，那么这个也可以改写。而且我们为`match`传输非正则值得话，会导致该值自动转为`RegExp对象`，所以我们可以手动修改该默认模式

![[00 assets/03827aa0a7a9b46abe4eaef71f99df95_MD5.png]]

2、当然我们可以使用`[Symbol.match]`来重写`match`默认模式

![[00 assets/8e29ec95fe3cc912a6e27fda4e02f049_MD5.png]]

### 10.5.5 Symbol.replace

1、使用`[Symbol.replace]`也可以改变`replace`得默认行为，因为和`Symbol.match`得特性一样，如果为`String.replace`传入非正则表达式，那么就会将该值转为`RegExp对象`

![[00 assets/a1aced0cb36ab886f307e64ef7d2629a_MD5.png]]

### 10.5.6 Symbol.search

1、整体和`Symbol.match`的特性一致，这里就不赘述了

![[00 assets/e2aec76026bed88e51b3f0b9e70d6f1c_MD5.png]]

### 13.5.7 Symbol.species

1、`Symbol.species`用于改变内置类型实例方法的返回值暴露实例化派生对象的方法

2、我们来一个一个解析内置类型的实例方法，数组的 `map`、`filter`、`slice` 等方法都会返回一个新的数组。`Symbol.species` 的目的是允许你通过`派生类`来定制这些方法返回的新实例。这就为你提供了一种改变数组方法的默认行为的方式。

3、下图中`personArray`和`animalArray`属于派生类

![[00 assets/7a6ec5e8722d9ba682ca186c14deada8_MD5.png]]

### 10.5.8 Symbol.split

1、和`Symbol.match`类似，直接参考之前的就行

![[00 assets/2bd4e8c0b2908ffd11462473046e9541_MD5.jpeg]]

### 10.5.9 Symbol.toPrimitive

1、很多情况下有很多人会将对象转为原始类型，比如如下情况

![[00 assets/c9bc6d3d8185148c7019898f1341037b_MD5.jpeg]]

2、为了改变这样的默认行为，可以使用`Symbol.toPrimitive`

![[00 assets/a1a643db22d94e5a2fd9a3e4bb6beb47_MD5.png]]

### 10.5.10 Symbol.toStringTag

1、创建对象的默认字符串描述，并且由`Object.toString()`使用

2、按照正常输出模式`Person`为`[Object Object]`，实际却输出了`[Object Person]`，和预期不符合，这里以后可以留意一下

![[00 assets/87db7b0de405f5fb45d2a39a7306dcd6_MD5.png]]

# 11 迭代器

## 11.1 基本介绍

下面的`for of`和`for in`本质也是实现了迭代器，来遍历`可迭代对象`

```javascript
// for of
let name = ['张三','李四','王五','赵六'];
for(let i of name){
	console.log(i);
}

// for in
let name = ['张三','李四','王五','赵六'];
for(let i in name){
	console.log(i);
}
```

可以理解为迭代器（Itreator）是一种`接口`，为各种不同数据结构提供统一的访问机制，任何数据结构只要部署了`Itreator`接口，就可以完成遍历操作。其中对于`迭代器`就需要实现`next()方法`

![[00 assets/87a5968c271b1fe7f47b04a52f393c13_MD5.png]]

其中对于`next()`函数的返回值就是按照下面的方式来处理的

![[00 assets/7a81f570250385d82506ff550e10c3f3_MD5.png]]

假如你要简单的实现的话，可以理解为按照下面的方式来处理

![[00 assets/94d539f248e8561f25c50465dad65097_MD5.png]]

## 11.2 可迭代对象

1、先来区分`可迭代对象`和`迭代器`，它们的的英文分别为`iterable protocol`和`iterator protocol`。这里我们改造了`14.1`的`迭代器`，手写了一个`可迭代对象`

![[00 assets/096af217e6dec0fb1733fbd07a4d48ba_MD5.png]]

2、我们使用`for of`来遍历对象，可以发现`obj`并不是一个`可迭代对象`

![[00 assets/ccefea6138c313df50010d51f3d600f2_MD5.png]]

通过`for of`遍历`可迭代对象`可以知道`for of`的原理。取出对象中的`[Symbol.iterator]`，调用`next()`方法，判断`done`的值，取出`value`值

![[00 assets/5b143fbddb8d9f72cf500026f7ab110c_MD5.png]]

## 11.3 内置可迭代对象

![[00 assets/e957aea1c424bf11899e077d27739bdb_MD5.png]]

其实说白了就是内部会内置一个`[Symbol.Iterator]`属性

![[00 assets/8535c05f40438d76ec9c1619cc26c244_MD5.png]]

可迭代对象的应用

![[00 assets/0ab798072b22dfa996e54067609e95ff_MD5.png]]

1、对于`展开语法`本质也是使用的`迭代器`来遍历处理的

![[00 assets/51ffc563ac63be274193e874e42993f5_MD5.png]]

对象使用`展开语法`的本质其实并不是使用的迭代器来处理的，而是`ES9`新增的特性

![[00 assets/e19a6d051e198652e3903b72ab540ec8_MD5.png]]

2、`解构赋值`本身也是实现的`迭代器`

![[00 assets/eff8f316c669f04ec89be342f7cfb738_MD5.png]]

3、当我们给一些构造函数传入数据的时候，内部其实也是使用的`迭代对象`

![[00 assets/ffe7e0dfc44bac265ed61cb96e3adc37_MD5.png]]

4、`Promise.all`本身也存在`迭代对象`

![[00 assets/2bb79e1353510e356796c5f2de34da99_MD5.png]]

## 11.4 自定义迭代类

![[00 assets/ee2cf19a8c9d747f1af510bea2e8a7fe_MD5.png]]

1、使用下面的方式就实现了`自定义迭代类`

![[00 assets/caef2efa95a88f5ea86cbd52f17e6326_MD5.png]]

假如是函数的话就使用下面的方式来自定义迭代器

![[00 assets/706a77cf33178613e5c3254e5a8a2b61_MD5.png]]

2、假如我们想要提前结束迭代器，并且实现监听的话，需要给返回的`[Symbol.iterator]`添加一个`return`函数

![[00 assets/98b74f64833570ea64f9d517f87f52b4_MD5.png]]

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

## 14.1 基本介绍

![[00 assets/cf35f1dcd6598963f7271e84ff06ff90_MD5.png]]

Set 是一种新的数据结构 Set 集合，他类似于数组，但是值是唯一的，并且这个集合实现了 Iterator 接口，所以可以使用 for..of 来遍历

```javascript
let s = new Set(["1", "2", "3", "4", "1"]); // Set的一个功能就是对数组进行去重操作

console.log(s, ...s); // Set也支持扩展运算符(...)
```

![[00 assets/2640d19f6fda960bfe62d9a3c8e8003d_MD5.png]]

假如你传入的是对象的话，就不会去重。因为对象的本质就是一个内存地址，每创建一个对象内存地址都不一样

![[00 assets/51a6a65a3de1a42b42f0b7b8322303f9_MD5.png]]

## 14.2 常用方法

当然他还有一些 API

```javascript
let s = new Set(["1", "2", "3", "4", "1"]);
s.size; //元素的个数
s.add("5"); //增加
s.delete("1"); //删除
s.has("2"); //存在
s.clear(); //清空
//遍历
for (let i of s) {
  console.log(i);
}
s.forEach((ele) => {
  console.log(ele);
});
```

## 14.3 强引用/弱引用

我们创建了这样一个对象。其中`obj`和`obj.friend`就是强引用，假如把它们设置为`null`的话，这样就没有其他引用指向它，那么就会被销毁。

这个时候我们使用`WeakSet`引用的话，就是弱引用。弱引用和强引用的区别就是，弱引用依旧可以使用`info.name`来获取数据，但是`GC`在回收的时候不会管这条引用，依旧会直接销毁该对象

其中`WeakSet`对对象的引用就是一个弱引用

![[00 assets/205d6b6cf90714aca0b316c7e5a54d6e_MD5.jpeg]]

## 14.4 WeakSet

![[00 assets/30626b44550c670536a2127654a6d8bb_MD5.png]]

![[00 assets/fdcb13b99256695ef4aa6e3fc8be51f0_MD5.png]]

```javascript
let ws = new WeakSet();
ws.add({ name: "张三" });
```

当然`WeakSet`的应用场景比较少，下面就是为数不多的几个。下面的应用场景是只**允许对象隐式调用，而不允许对象显示调用**

下面为解释，其中有一个点就是为什么不能使用`Set`。因为`Set`是一个强引用，后期假如要消除对象`p = null`的时候，因为`Set`也强引用了一份，所以并不会删除该对象，还需要`Set`来删除一份，才能消除该对象。

![[00 assets/920b8dea9fa66248ee5c5351c8c2f679_MD5.png]]

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

# 19 模块化

### 22.1 介绍

模块化是将一个大的程序，拆分为许多的小文件，然后将小文件组合起来

![[00 assets/5d3ac69c44c54f270dcd9bcae2fc2743_MD5.png]]

**express**表示规定模块的对外接口

**import**表示用于输入其他模块提供功能

其中 p1 和 say()表示对外暴露的接口，在 HTML 文件里面的 scrip 文件就是引用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
		<script type="module">
			import * as m from "./js/1.js";
			console.log(m)
		</script>
	</body>
</html>
```

```javascript
export let p1 = '张三'
export function say(){
	console.log('Hi!');
}
```

### 22.2 export

```javascript
//统一暴露
let p1 = '张三'
function say(){
	console.log('Hi!');
}
export{p1,say}

//默认暴露
export default {
	name:'1'
}
//假如要调用的话就是 m.default.name
```

### 22.3 import

**解构赋值形式**

```javascript
let p1 = '张三'
function say(){
	console.log('Hi!');
}

export{p1,say}
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script type="module">
			import {p1,say} from "./js/1.js";
			console.log(p1);
		</script>
	</body>
</html>
```

当然也是支持取别名的

```javascript
import {p1 as name,say} from "./js/1.js";
console.log(p1);
```

使用解构赋值的语法来显示默认暴露的情况

```javascript
export default {
	name:'1'
}
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
		<script type="module">
			import {default as f1} from "./js/1.js";
			console.log(f1)
		</script>
	</body>
</html>

```

**简便形式**，这个方式只能针对默认暴露

```javascript
export default {
	name:'1'
}
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
	</head>
	<body>
		<script type="module">
			import f1 from "./js/1.js";
			console.log(f1)
		</script>
	</body>
</html>

```

### 22.4 浏览器使用

这个是另一种方式来时候模块化

```html
//html文件
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="js/open.js" type="module"></script>
	</body>
</html>
```

```javascript
//1.js
export let name = '张三'
export function say(){
	console.log('Hi!');
}
```

```javascript
//2.js
let p1 = '张三'
function say(){
	console.log('Hi!');
}
export{p1,say}
```

```javascript
//3.js
export default {
	name:'1'
}
```

```javascript
//open.js
import * as f1 from "./1.js";
import * as f2 from "./2.js";
import * as f3 from "./3.js";

console.log(f1);
console.log(f2);
console.log(f3);
```

![[00 assets/efe3e592d0f0bd23d9d9bfc17a31360d_MD5.png]]

### 22.5 babel 转换

模块化可能存在兼容性问题，所以我们要将代码进行转换

babel 官网：[Babel 中文网 · Babel - 下一代 JavaScript 语法的编译器 (babeljs.cn)](https://www.babeljs.cn/)

这里我们需要安装 3 个工具：**babel-cli**（babel 命令行工具），**babel-preset-env**（预设工具包），**browseeify**（打包工具）

初始化

```
npm init --yes
```

再来安装

```
npm i babel-cli babel-preset-env browserify -D
```

再来转换，其中 babel 后面的 js 表示转换的文件的目录，-d 后面的是存到哪里去

```
npx babel js -d jso --presets=babel-preset-env
```

再来打包，其中第一个值是要打包的地址，-o 后面的是存入的地址

```
npx browserify jso/open.js -o jso/op.js
```

### 22.6 引入 npm 包

导入 Jquery 的包

```
npm i jquery
```

然后我们再在文件里面写上 JQuery 的代码，再来进行转换和打包就可以了

```
import $ from 'jquery';
$('body').css('background','pink');
```

# 20 Proxy

## 20.1 基本介绍

![[00 assets/bc901b9e5a7d96417f5e8a51921b96c2_MD5.png]]

## 20.2 基本使用

![[00 assets/debfb9de3e5db6d438eb111fba346523_MD5.png]]

下面为基本使用的过程，假如我们需要使用到监听需要使用`proxy`对象来操作

```javascript
let obj = {
  name: "张三",
  age: 18,
};

const objProxy = new Proxy(obj, {
  // 获取值时的捕获器
  get(target, key) {
    console.log(`监听到${key}被获取~`);
    return target[key];
  },

  // 设置值时的捕获器
  set(target, key, newValue) {
    console.log(`监听到${key}被改变~`);
    target[key] = newValue;
  },

  // 监听in的捕获器
  has(target, key) {
    console.log(`监听到${key}的in操作~`);
    return key in target;
  },

  // 监听delete的捕获器
  deleteProperty(target, key) {
    console.log(`监听到${key}的delete操作~`);
    delete target[key];
  },
});

console.log(objProxy.name);
objProxy.name = "李四";
console.log("name" in objProxy);
delete objProxy.name;
```

![[00 assets/e4572afad8bdbbd94698c2374f097a23_MD5.png]]

## 20.3 捕获器

![[00 assets/86b83b8f8ff733fafb0a91a678765842_MD5.png]]

下面时`apply`、`construct`的捕获器的使用案例

![[00 assets/31ca669c8e2b388e9b98493f2820161a_MD5.png]]

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
