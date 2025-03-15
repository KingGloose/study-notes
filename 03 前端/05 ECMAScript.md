# 18. ES6

## 1. 介绍

ES 的全称是**ECMAScript**，是**脚本语言的规范**，其中 Javascript 就是他的一种实现，所以 ES 新特性就是指的 Javascript 的新特性

**ECMA**中文名是欧洲计算机制造商协会，这个协会的目标是评估、开发和认可电信和计算机标准

## 2. let/const

### 2.1 let

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

### 2.2 const

```javascript
// 常量一定要赋初始值
const name = "张三";

name = "李四" // 报错，常量不能修改

console.log(name);
```

假如我们要传递引用类型的话。结果是不会报错的，这是因为，我们保存的是`obj`的地址值

![image-20221017165345908](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317776.png)

### 2.3 作用域提升

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

![image-20221017170224636](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317812.png)

![image-20221017170435412](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317802.png)

### 2.4 和 window 关系

在以前的`var`声明的对象都会添加到`window`中，因为在`GO`中的`window`指向的是`this`，所以在全局创建的变量都会保存到`GO`中，也就是`window`

![image-20221017172254129](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317797.png)

但是在`ES6`之后，这个可以参考我`JS高级 - 环境`的笔记。

原本的`GO(VO)`是一个对象，保存变量的时候直接就是`GO.name = "张三"`。但是在现在是`VE`，不是一个对象，最后的数据都会保存在`variables_`，他的数据类型是`VariableMap`，他是一个`HashMap`，也就是一个哈希表，底层通过`C++`实现

因为以前都是`window`指向着`GO`，但是现在使用`let/const`就不会保持同步了。

![image-20221017191056246](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317800.png)

下面为`variables_`的源码，下面的注释就已经写了

![image-20221017191312802](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317823.png)

## 3. 块级作用域

### 3.1 基本介绍

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

![image-20221017192754720](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317478.png)

### 3.2 使用场景

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

![image-20221019104842403](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317496.png)

但是我们在函数内部获取`i`的时候，一直都是`i`的最大值。因为我们定义`var`的时候块级作用域约束不到他，所以他会添加到全局，所以获取到的就是`for循环`加到最大值

![image-20221019104954084](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317513.png)

假如需要解决的话，就需要使用到函数作用域来处理

![image-20221019105503291](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317528.png)

或者直接使用`let`来处理也可以，这样处理是最好的

![image-20221019105557233](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317546.png)

### 3.3 for 中的 let

实际上我们在使用`for`来遍历的时候，是创建一个个的块级作用域。假如是`var`的话就是一个`var`，所以每个块级作用域访问的时候都是访问的这个`var`

![image-20221019110146294](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317562.png)

### 3.4 暂时性死区

![image-20221019111339398](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317101.png)

假如按照`var`来写的变量，在初始的时候会将改该变量写入`GO`中，为`undefined`。所以访问不会报错，但是没有值

![image-20221019111539474](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317121.png)

假如我们只要块级作用域中使用了`let/const`的话，就会报错了。

![image-20221019112034185](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317139.png)

### 3.5 var/let/const 选择

![image-20221020162831479](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317156.png)

## 4. 变量的解构赋值

允许按照一定模式从数组和对象中提取值，对变量进行赋值，这被称为解构赋值

### 4.1 数组结构

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

![image-20221017162632835](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317176.png)

对于`解构赋值`得数组形式，还有一个用途就是交换数据，不需要声明第三方变量

![image-20230218132508511](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317239.png)

### 4.2 对象结构

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

![image-20221017163054698](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317836.png)

### 4.3 解构场景

![image-20221017163158898](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317855.png)

## 7. 模板字符串

### 7.1 基本使用

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

![image-20221020163346734](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317874.png)

3、并且使用模板字符串会将插入的字符串都使用`toString()`来转为字符串再插入

![image-20231209134904938](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317896.png)

### 7.2 标签模板字符串

我们也可以直接在函数的后面编写**``**，这样可以直接执行该函数。其中第一个参数就是**非变量参数**，后面的就是**${ }**中的值

![image-20221020163857594](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317913.png)

假如我们在后面编写字符串的话，就会自动切割`${ }`数据和非`${ }`字符串。

![image-20221020164437679](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317935.png)

在`React`中的`styled-components`中是一种比较常用这种模式

![image-20221020170103875](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317416.png)

## 8. 对象简化写法

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

![image-20221017161123274](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317436.png)

## 9. 箭头函数

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

## 10. 函数参数默认值

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

![image-20221020170910998](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317460.png)

或者可以使用这种写法

![image-20221020171401352](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317506.png)

## 11. 剩余参数

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

## 12. 扩展运算符

" ... "扩展运算符能将数组转换为逗号分隔为参数序列

注意这个，他只有一个参数

```javascript
const person = ['张三','李四','王五'];
function fn(){
	console.log(arguments);
}
fn(person);
```

![屏幕截图 2022-02-17 173615](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317529.png)

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

![屏幕截图 2022-02-17 173857](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317555.png)

## 13. Symbol

### 13.1 基本介绍

1、`ES6`引入了一个新的原始数据类型`Symbol`，表示独一无二的值，它是 JS 的第七种数据类型

![image-20231209142846199](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317990.png)

2、`Symbol`实例是唯一、不可变的，可以用作**非字符串形式的对象属性**，所以使用他没有属性冲突的危险

![image-20231209170928957](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317019.png)

### 13.2 基本使用

#### 13.2.1 Symbol()

1、创建一个`Symbol`实例，这里可以这样理解，`Symbol`是身份证，里面的值是`名字`，`名字`可以一样，但是`身份证`不能一样

2、并且`Symbol`不能实例化，只能使用函数的形式

![image-20231209171023875](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317051.png)

#### 13.2.2 Symbol.for()

1、如果想在全局的注册表中创建，可以使用`Symbol.for()`来创建`Symbol`，它会对传入的`key`做**幂等操作**，也就是会先检测`全局注册表`，如果没有就创建该实例放入`全局注册表`中，如果有的话就直接返回已经创建好的`Symbol`实例

如果想详细知道幂等操作可以查看下面的链接：[(1 封私信 / 80 条消息) 什么是幂等？如何解决幂等性问题？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/534651475)

![image-20231209171459545](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317105.png)

2、并且直接使用`Symbol.for()`全局注册表中创建的`Symbol`实例和直接使用`Symbol()`创建的`Symbol`实例也不相同

![image-20231209171723301](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317118.png)

#### 13.2.3 Symbol.keyFor()

1、使用`Symbol.keyFor()`来在`全局注册表`中查找对应的`key`，否则就返回`undefined`

![image-20231209172137194](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317135.png)

### 13.3 对象属性

1、一般情况下`Symbol`是为了给对象设置独一无二的属性名的，下面就是其中一个应用场景

2、使用`Object.getOwnPropertyNames`和`Object.getOwnPropertySymbols`可以分别获取`name`和`symbol`名

3、如果想要获取`name`和`symbol`的话，可以使用`Reflect.ownKeys`来获取

![image-20231209172757201](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317584.png)

4、使用`Object.getOwnPropertyDescriptors`也可以获取所有的`key`包括`Symbol`，并且获取对应属性的描述

![image-20231209173210789](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317606.png)

5、当然我们可以使用`Object.defineProperty`来为对象创建对应的`Symbol key`

![image-20221020211236310](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317627.png)

假如想进一步了解的话可以参考这个网站：[Symbol - ECMAScript 6 入门 (ruanyifeng.com)](https://es6.ruanyifeng.com/#docs/symbol)

**注意**：同时这里有一个小细节，我们使用 `defineProperty` 添加的属性，如果我们后续即便重新覆盖了一遍，依旧会保留该属性值的属性，可以参考下图

![image-20240412174226687](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317646.png)

### 13.4 遍历 Symbol

![image-20231209173757139](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317684.png)

### 13.5 内置 Symbol

#### 13.5.1 Symbol.asyncIterator

1、当然除了普通的同步迭代器，还存在一个异步迭代器，我们使用`Symbol`也是可以模拟出来的，它会根据迭代的方式，一步步按照同步的方式来执行，每隔 3s 就会进行下一步

![image-20231209235712265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317716.png)

2、下面是使用`生成器yield`来实现的异步迭代器

![image-20231210132000557](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317591.png)

下面是`JS高级程序设计`中的异步迭代器，实现的功能基本类似

![image-20231210164954664](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317620.png)

3、但是我一直挺好奇这个异步迭代器的具体使用场景在那里

4、**注意**：上述我都是自己写了迭代器来使用，如果我不使用迭代器来使用的话，就存在下面的问题。比如我自己写的迭代器，也是按照 JS 高级程序设计中编写的，时间图应该是这样的，所以总共是 9s

![image-20231210172421609](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317642.png)

但是我自己来写一个 Promise 数组的话，时间图是这样的，也就是总时长是 3s，和预期不一样，这就和`Promise.all`是一样的

![image-20231210172609756](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317663.png)

暂时不是很清楚上面代码那里存在问题，如果以后的我看到后可以解答一下

#### 13.5.2 Symbol.hasInstance

1、检测构造器对象是否认可一个对象是它的实例，一般情况下使用`instanceof`操作符来处理，在`ES6`之后使用`Symbol.hasInstace`来处理

![image-20231210173251143](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317685.png)

#### 13.5.3 Symbol.isConcatSpreadable

![image-20231210173649283](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317703.png)

#### 13.5.4 Symbol.iterator

参考 14.迭代器

#### 13.5.5 Symbol.match

1、默认情况下使用`String.match`是使用`Symbol.match`，那么这个也可以改写。而且我们为`match`传输非正则值得话，会导致该值自动转为`RegExp对象`，所以我们可以手动修改该默认模式

![image-20231210193600573](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317304.png)

2、当然我们可以使用`[Symbol.match]`来重写`match`默认模式

![image-20231210193959717](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317326.png)

#### 13.5.5 Symbol.replace

1、使用`[Symbol.replace]`也可以改变`replace`得默认行为，因为和`Symbol.match`得特性一样，如果为`String.replace`传入非正则表达式，那么就会将该值转为`RegExp对象`

![image-20231210194902834](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317354.png)

#### 13.5.6 Symbol.search

1、整体和`Symbol.match`的特性一致，这里就不赘述了

![image-20231210195420833](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317398.png)

#### 13.5.7 Symbol.species

1、`Symbol.species`用于改变内置类型实例方法的返回值暴露实例化派生对象的方法

2、我们来一个一个解析内置类型的实例方法，数组的 `map`、`filter`、`slice` 等方法都会返回一个新的数组。`Symbol.species` 的目的是允许你通过`派生类`来定制这些方法返回的新实例。这就为你提供了一种改变数组方法的默认行为的方式。

3、下图中`personArray`和`animalArray`属于派生类

![image-20231210201944683](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317439.png)

#### 13.5.8 Symbol.split

1、和`Symbol.match`类似，直接参考之前的就行

![image-20231210203218986](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317479.png)

#### 13.5.9 Symbol.toPrimitive

1、很多情况下有很多人会将对象转为原始类型，比如如下情况

![image-20231210203602149](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317022.png)

2、为了改变这样的默认行为，可以使用`Symbol.toPrimitive`

![image-20231210203934413](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317055.png)

#### 13.5.10 Symbol.toStringTag

1、创建对象的默认字符串描述，并且由`Object.toString()`使用

2、按照正常输出模式`Person`为`[Object Object]`，实际却输出了`[Object Person]`，和预期不符合，这里以后可以留意一下

![image-20231210204534741](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317078.png)

## 14. 迭代器

### 14.1 基本介绍

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

![image-20221128112040431](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317106.png)

其中对于`next()`函数的返回值就是按照下面的方式来处理的

![image-20221128111512602](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317140.png)

假如你要简单的实现的话，可以理解为按照下面的方式来处理

![image-20221128121933649](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317187.png)

### 14.2 可迭代对象

1、先来区分`可迭代对象`和`迭代器`，它们的的英文分别为`iterable protocol`和`iterator protocol`。这里我们改造了`14.1`的`迭代器`，手写了一个`可迭代对象`

![image-20221128121550426](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317763.png)

2、我们使用`for of`来遍历对象，可以发现`obj`并不是一个`可迭代对象`

![image-20221128120916641](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317787.png)

通过`for of`遍历`可迭代对象`可以知道`for of`的原理。取出对象中的`[Symbol.iterator]`，调用`next()`方法，判断`done`的值，取出`value`值

![image-20221128122023988](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317813.png)

### 14.3 内置可迭代对象

![image-20221128141434435](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317847.png)

其实说白了就是内部会内置一个`[Symbol.Iterator]`属性

![image-20221128142407855](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317866.png)

可迭代对象的应用

![image-20221128143209997](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317887.png)

1、对于`展开语法`本质也是使用的`迭代器`来遍历处理的

![image-20221128143932792](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317517.png)

对象使用`展开语法`的本质其实并不是使用的迭代器来处理的，而是`ES9`新增的特性

![image-20221128144216300](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317537.png)

2、`解构赋值`本身也是实现的`迭代器`

![image-20221128150913808](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317558.png)

3、当我们给一些构造函数传入数据的时候，内部其实也是使用的`迭代对象`

![image-20221128151200429](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317594.png)

4、`Promise.all`本身也存在`迭代对象`

![image-20221128151328638](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317634.png)

### 14.4 自定义迭代类

![image-20221128152440548](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317669.png)

1、使用下面的方式就实现了`自定义迭代类`

![image-20221128152855220](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317193.png)

假如是函数的话就使用下面的方式来自定义迭代器

![image-20221128153542340](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317223.png)

2、假如我们想要提前结束迭代器，并且实现监听的话，需要给返回的`[Symbol.iterator]`添加一个`return`函数

![image-20221128153827392](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317242.png)

## 15. 生成器

^bbfc74

### 15.1 基本介绍

`生成器`就是一个特殊的`迭代器`，使用`yield`是划分代码块的，也就是`分隔符`

![image-20221128155140873](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317269.png)

既然是`特殊的迭代器`，那么我们使用`for of`来遍历循环也可以

![image-20221128155331758](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317297.png)

### 15.2 返回值/参数

1、其中`yield`是暂停函数的执行，后面的参数是作为返回值。`return`表示结束函数

![image-20221128160155549](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317352.png)

2、要给第二段代码中传入参数就需要从第一个`yield`的返回值获取

![image-20221128161038641](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317948.png)

3、这里需要强调一个点就是关于给 next() 传递参数的问题，你执行 next() 其实是执行 yield 之上的代码，可以理解为一个指针指向到了 yield 这行，并且这个指针是指向到 "=" 这里，也就是还没执行赋值操作

4、当你执行下一个 next 函数的时候，传递的参数才会进行赋值操作，可以查看下图来理解其中的顺序关系

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202409141726359.png)

### 15.3 终止执行

![image-20221128162650917](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317977.png)

### 15.4 抛出异常

使用`throw()`可以抛出异常，抛出异常的位置在上一个`yield`。假如你是要`try-catch`来包裹的话，依旧会执行第二段代码，也就相当于你使用`throw()`顺便执行了`next()`和`报错`

![image-20221128163011165](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317035.png)

## 16. Promise

^872c8d

参考视频：[尚硅谷 Web 前端 Promise 教程从入门到精通\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1GA411x7z1?p=2&spm_id_from=pageDriver)

### 16.1 初始 Promise

#### 16.1.1 Promise 简介

Promise 是一门新的技术(ES6 规范)，并且是 JS 中`进行异步编程`的新解决方案(旧方案是单纯使用回调函数) ^15cb91

从**语法**上来说: Promise 是一个`构造函数`，从功能上来说: promise 对象用来封装一个异步操作并可以获取其成功/ 失败的结果值

#### 16.1.2 使用 Promise 理由

##### 16.1.2.1 指定回调函数的方式更加灵活

**旧的**: 必须在启动异步任务前指定

**现在**: 启动异步任务 => 返回 promie 对象 => 给 promise 对象绑定回调函数(甚至可以在异步任务结束后指定/多个)

##### 16.1.2.2 支持链式调用, 可以解决回调地狱问题

**1.什么是回调地狱**

回调函数嵌套调用, 外部回调函数异步执行的结果是嵌套的回调执行的条件

![image-20220604231948285](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317072.png)

**2.回调地狱的缺点**

不便于阅读 不便于异常处理

**3.解决方案**

promise `链式调用`，用来解决回调地狱问题，但是`只是简单的改变格式`，并没有彻底解决上面的问题真正要解决上述问题，一定要利用 promise 再加上 await 和 async 关键字实现异步传同步(**promise +async/await**)

##### 16.1.2.3 减少沟通的成本

比如下面的`sendRequest()方法`，对于一些库可能存在不同的调用方式，可能会有很大的学习成本。所以就会存在`Promise`，其中`Promise`就翻译为`承诺`，就是指定一个统一的规范，以后按照`Promise`调用即可。

![image-20221127160558490](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317103.png)

#### 16.1.3 初识 Promise

```html
//普通写法
<body>
 <button class="BtnReward">点击我抽奖</button>
 <script>
   function GetRandom(n, m) {
     return Math.ceil(Math.random() * (n - m + 1)) + m - 1;
   }
   const btn = document.querySelector(".BtnReward");
   btn.addEventListener("click", function () {
     setTimeout(() => {
       let r = GetRandom(1, 100);
       if (r <= 30) {
         alert("恭喜你中奖了");
       } else {
         alert("再接再厉");
       }
     }, 1000);
   });
 </script>
</body>


//Promise写法
<button class="BtnReward">点击我抽奖</button>
<script>
  function GetRandom(n, m) {
    return Math.ceil(Math.random() * (n - m + 1)) + m - 1;
  }
  const btn = document.querySelector(".BtnReward");
  btn.addEventListener("click", function () {
    const p = new Promise((res, rej) => {
      setTimeout(() => {
        let r = GetRandom(1, 100);
        if (r <= 30) {
          res(r);
        } else {
          rej(r);
        }
      }, 1000);
    });
    p.then(
      (value) => {
        alert("恭喜你中奖了，你的号码为" + value);
      },
      (reason) => {
        alert("可惜了你没中奖，你的号码为" + reason);
      }
    );
  });
</script>
```

#### 16.1.4 Promise 实践练习

##### 16.1.4.1 fs 文件读取

```javascript
//普通写法
const fs = require("fs");
fs.readFile("./1.txt", (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});


//Primise写法
const fs = require("fs");
const p = new Promise((res, rej) => {
  fs.readFile("./1.txt", (err, data) => {
    if (err) rej(err);
    res(data);
  });
});
p.then(
  (value) => {
    console.log(value.toString());
  },
  (reason) => {
    console.log(reason);
  }
);


//Primise封装为函数写法
const fs = require("fs");
function mineReadFile(path) {
  return new Promise((res, rej) => {
    fs.readFile(path, (err, data) => {
      if (err) rej(err);
      res(data);
    });
  }).then(
    (value) => {
      console.log(value.toString());
    },
    (reason) => {
      console.log(reason);
    }
  );
}
mineReadFile("./1.txt");


//util.promisify进行Promise化
//使用node.js里面的util.promisify将方法转换为Promise，这样就不用每次都自己手动封装
const util = require("util");
const fs = require("fs");

let mineReadFile = util.promisify(fs.readFile);
mineReadFile("./1.txt").then(
  (value) => {
    console.log(value.toString());
  },
  (reason) => {
    console.log(reason);
  }
);
```

##### 16.1.4.2 AJAX 请求

```html
<button class="BtnGetAJAX">点击AJAX</button>
<script>
  var btn = document.querySelector(".BtnGetAJAX");
  btn.addEventListener("click", () => {
    // 普通写法
    const xhr = new XMLHttpRequest();
    xhr.open(
      "GET",
      "http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList"
    );
    xhr.send();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status >= 200 && xhr.status < 300) {
          console.log(xhr.response);
        } else {
          console.log(xhr.status);
        }
      }
    };

    //Promise写法
    const p = new Promise((res, rej) => {
      const xhr = new XMLHttpRequest();
      xhr.open(
        "GET",
        "http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList"
      );
      xhr.send();
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status >= 200 && xhr.status < 300) {
            res(xhr.response);
          } else {
            rej(xhr.status);
          }
        }
      };
    });
    p.then(
      (value) => {
        console.log(value);
      },
      (reason) => {
        console.log(reason);
      }
    );
  });
</script>


//将Promise封装为函数写法
<body>
  <script>
    function GetAjax(url) {
      return new Promise((res, rej) => {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.send();
        xhr.onreadystatechange = function () {
          if (xhr.readyState === 4) {
            if (xhr.status >= 200 && xhr.status < 300) {
              res(xhr.response);
            } else {
              rej(xhr.status);
            }
          }
        };
      }).then(
        (value) => {
          console.log(value);
        },
        (reason) => {
          console.log(reason);
        }
      );
    }
    GetAjax("http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList");
  </script>
</body>
```

#### 16.1.5 Promise 的值

下面就是 Promise 对象上面的三个值

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202406101029834.png)

##### 16.1.5.1 PromiseState

**pending** 未决定的，**resolved / fullfilled** 成功，**rejected** 失败

**pending** 可以变为 **resolved**和**rejected**，并且状态只能改变一次

##### 16.1.5.2 PromiseResult

```javascript
new Promise((res,rej)=>{
	res(data) //也就是这里传递的data
	rej(data)
})
```

##### 16.1.5.3 Promise 参数

1、传入普通的参数，就是按照正常的处理方式

2、传入另外一个`Promise`，那么该`Promise`的控制就不会被移交给传入的`Promise`

![image-20221127163056404](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317768.png)

3、传入的对象中包含`then方法`，那么就会执行`对象`中的方法

![image-20221127163152769](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317786.png)

#### 16.1.6 Promise 工作流程

![image-20220605152339572](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317803.png)

### 16.2 Promise 的 API

#### 16.2.1. Promise 构造函数

(1) executor 函数：执行器(resolve,reject) => {}

(2) resolve 函数：内部定义成功时我们调用的函数 value => {}

(3) reject 函数：内部定义失败时我们调用的函数 reason => {}

```javascript
new Promise((res,rej)=>{
	if(result) rej(data) //成功调用rej
	elsr res(data) 	//失败调用res
})
```

且 Promise 里面的执行器是同步调用的

```javascript
new Promise((res,rej)=>{
	console.log("aaaa")
})
console.log("bbbb")
```

![image-20220605153142500](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317822.png)

#### 16.2.2 Promise.prototype.then()

(1) onResolved 函数：成功的回调函数(value)=>{}

(2) onRejected 函数：失败的回调函数(reason)=>{}

说明：指定用于得到成功 value 的成功回调和用于得到失败 reason 的失败回调返回一个新的 promise 对象

```javascript
const p = new Promise((res, rej) => {
  res();
  rej();
});
function onResolved(value) {
  console.log("这是成功的回调");
}
function onRejected(reason) {
  console.log("这是失败的回调");
}
p.then(onResolved, onRejected);


//但是我们平常简写
const p = new Promise((res, rej) => {
  res();
  rej();
}).then(
  (value) => {
    console.log("这是成功的回调");
  },
  (reason) => {
    console.log("这是失败的回调");
  }
);
```

说明：这里就观察到一个特点，就是 Promise 只能修改一次状态，这个在上面就说过，我们同时调用了`res`和`rej`但是最后的状态就是`res`

#### 16.2.3.Promise.prototype.catch()

(1) onRejected 函数：失败的回调函数(reason)=>{}

说明：只有失败的回调

```javascript
const p = new Promise((res, rej) => {
  rej();
}).catch(
  (reason) => {
    console.log("这是失败的回调");
  }
);
```

#### 16.2.4 Promise.resolve()

(1) 你传入非 Promise 对象，结果为 fulfilled 表示成功。并且 PromiseResult 的结果就是你传入的数据

(2) 你传入的是 Promise 对象，结果就根据 Promise 参数的处理结果来，假如参数是 rejected，那么外部 Promise 的结果就是 rejected。并且参数是根据回调函数传入的值决定的

```javascript
const p = Promise.resolve(123);
console.log(p);

const p1 = Promise.resolve(
  new Promise((res, rej) => {
    rej("哈哈哈");
  })
);
// 用来解决失败回调，浏览器报错的问题
p1.catch((reason)=>{
   console.log("ERROR")
})
console.log(p1);
```

![image-20220605155632266](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317841.png)

#### 16.2.5 Promise.reject()

(1) 不管你传入什么，都是`reject`，你传入什么，失败的结果就是什么

```javascript
const p = Promise.reject(123);
console.log(p);

const p1 = Promise.reject(
  new Promise((res, rej) => {
    res("哈哈哈");
  })
);
console.log(p1);
```

![image-20220605155913918](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317865.png)

#### 16.2.6 Promise.all()

(1) promises 包含 n 个 promise 的数组

说明：返回一个新的 promise，只有所有的 promise 都成功才成功，只要有一个失败了就直接失败

```javascript
//假如都成功的话，最后的结果就是zhuan'ru
const p1 = Promise.resolve(123);
const p2 = Promise.resolve(
  new Promise((res, rej) => {
    res("哈哈哈");
  })
);
const p3 = new Promise((res, rej) => {
  res("哈哈哈哈哈");
});

const result = Promise.all([p1, p2, p3]);
console.log(result);
```

![image-20220605160403528](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317389.png)

假如里面有一个失败的话，其结果就是失败

```javascript
const p1 = Promise.resolve(123);
const p2 = Promise.resolve(
  new Promise((res, rej) => {
    rej("哈哈哈");
  })
);
const p3 = new Promise((res, rej) => {
  res("哈哈哈哈哈");
});

const result = Promise.all([p1, p2, p3]);
console.log(result);
```

![image-20220605204501160](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317411.png)

#### 16.2.7 Promise.race()

只接受第一个 Promise 的状态的改变，一开始的结果是 reject

但是你给 p1 定时器的话，就让 p2 先执行了，所以结果就是 resolve

```javascript
const p1 = Promise.resolve(
  new Promise((res, rej) => {
    rej("哈哈哈");
  })
);
const p2 = new Promise((res, rej) => {
  res("哈哈哈哈哈");
});

const result = Promise.race([p1, p2]);
console.log(result);

```

![image-20220605204930781](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317430.png)

#### 16.2.8 Promise.allSettled()

[Promise.allSettled() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)

### 16.3 Promise 关键问题

#### 16.3.1 改变 Promise 状态的方式

一共三种方式

```javascript
const p = new Promise((res,rej)=>{
   // 1.调用res函数
   res()
   // 2.调用rej函数
   rej()
   // 3.抛出错误
   throw "ERROR"
})
```

#### 16.3.2 指定多个 then 都会执行吗？

```javascript
const p = new Promise((res,rej)=>{
   res("ok")
})
p.then((value)=>{
   console.log("1:" + value)
})
p.then((value)=>{
   console.log("2：" + value)
})
```

![image-20220605205655828](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317454.png)

#### 16.3.3 改变状态和 then 指定回调那个先？

(1) 都有可能，正常情况下是先指定回调再改变状态，但也可以先改状态再指定回调

(2) 如何先改状态再指定回调？

    1.在执行器中直接调用resolve() / reject()

    2.延迟更长时间才调用then()

(3) 什么时候才能得到数据？

    1.如果先指定的回调，那当状态发生改变时，回调函数就会调用，得到数据

    2.如果先改变的状态，那当指定回调时，回调函数就会调用，得到数据

​
首先要理解指定回调和执行回调的区别，指定可以理解为创建 then 回调，但是执行回调就必须在 Promise 构造函数里面执行 resolve() / reject()才可以执行回调

我们在进行同步任务的时候，可能先改变状态，再去指定回调，然后执行回调

平时我们执行异步任务居多，这样的话就是先指定回调，再改变状态，然后执行回调

```javascript
const p = new Promise((res, rej) => {
  //1. 进行同步任务
  res("ok");
  //2. 进行异步任务
  setTimeout(() => {
    res("ok");
  }, 2000);
});
p.then((value) => {
  console.log(value);
});
console.log(p);
```

#### 16.3.4 then 返回的结果由什么决定?

首先我们来看 then()方法的返回值是什么？结果是一个 Promise 对象

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
let result = p.then((value) => {
  console.log(value);
});
console.log(result);
```

![image-20220605213307875](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317474.png)

这个 Promise 的返回值是由里面的 resolve() / reject()回调函数决定的，其结果和 Promise.resolve()是一样的规律

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
let result = p.then((value) => {
  return "ok"
});
console.log(result);
```

![image-20220605213740579](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317526.png)

假如我们返回 Promise 对象，返回 resolve() 状态的 Promise 的话，结果就是 resolve

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
let result = p.then((value) => {
  return new Promise((res, rej) => {
    rej("Error");
  });
});
console.log(result);
```

![image-20220605223325128](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317819.png)

#### 16.3.5 串联任务

下面就是串联任务的一种

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
p.then((value) => {
  //根据上面一点，then()方法返回的值为resolve，那么就是Promise对象执行后面的then回调
  return new Promise((res, rej) => {
    res("Error");
  });
})
  .then((value) => {	//这里参数为上面的Error
    console.log(value); //Error
  })
  .then((value) => {	//不返回reject的话，就是resolve，并且没返回值，所以这里就是undefined
    console.log(value); //undefined
  });
```

#### 16.3.6 异常穿透

(1) 当使用 promise 的 then 链式调用时，可以在最后指定失败的回调

(2) 前面任何操作出了异常，都会传到最后失败的回调中处理

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
p.then((value) => {
  throw "ERROR"
})
  .then((value) => {
    console.log("111");
  })
  .then((value) => {
    console.log("111");
  })
  .catch((reason) => {
    console.log(reason);
  });

```

![image-20220605224717270](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317896.png)

#### 16.3.7 如何中断 Promide 链？

(1) 当使用 promise 的 then 链式调用时，在中间中断，不再调用后面的回调函数

(2) 办法：在回调函数中返回一个 pendding 状态的 promise 对象

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
p.then((value) => {
  return new Promise(() => {});
})
  .then((value) => {
    console.log("111");
  })
  .then((value) => {
    console.log("111");
  })
  .catch((reason) => {
    console.log(reason);
  });

```

为什么返回一个 Padding 状态的 Promise 对象就可以了，因为你不管是 resolve 和 reject，都会触发 then()方法的回调函数，所以我们直接传递 padding 状态的 Promise 对象就不会再执行后面的操作

### 16.4 自定义封装

#### 16.4.1 初始结构

```javascript
function Promise(executor) {}

Promise.prototype.then = function (onResolved, onRejected) {};
```

#### 16.4.2 resolve 和 reject

```javascript
function Promise(executor) {

  this.PromiseState = "Pending";
  this.PromiseResult = null;
  const _this = this;

  function resolve(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  function reject(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  executor(resolve, reject);
}

Promise.prototype.then = function (onResolved, onRejected) {};
```

#### 16.4.3 throw 抛出异常改变状态

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  function reject(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this)
}

Promise.prototype.then = function (onResolved, onRejected) {};
```

#### 16.4.4 Promise 状态只能修改一次

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this);
}

Promise.prototype.then = function (onResolved, onRejected) {};
```

#### 16.4.5 异步任务回调的执行

下面为运行的代码，这里就是上面的 Promise 关键问题第 3 个的实际场景，`指定回调`和`执行回调`的区别。

我们运行到 Promise 里面的`executor函数`之后，因为是一个定时器，这个时候 JS 就会开启异步任务，将这个定时器纳入队列中。然后执行后面的代码，这个时候就指定了 then 回调，执行 then 回调。但是这个时候 Promise 对象的状态是没有改变的，所以里面的方法一个都不会执行。当定时器结束之后，状态改变，但是 then 回调并不是再去执行一遍。

```javascript
<script>
  let p = new Promise((res, rej) => {
    setTimeout(() => {
      res(123);
    }, 3000);
  });
  p.then(
    (value) => {
      console.log(value);
    },
    (reason) => {
      console.log(reason);
    }
  );
</script>
```

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callback = {};
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      if (_this.callback.onResolved) {
        _this.callback.onResolved(data);
      }
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      if (_this.callback.onRejected) {
        _this.callback.onRejected(data);
      }
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this);
}

Promise.prototype.then = function (onResolved, onRejected) {
  if (this.PromiseState === "resolve") {
    onResolved(this.PromiseResult);
  }
  if (this.PromiseState === "reject") {
    onRejected(this.PromiseResult);
  }
  if (this.PromiseState === "Pending") {
    this.callback = {
      onResolved,
      onRejected,
    };
  }
};
```

#### 16.4.6 指定多个回调

每次调用 then，就将 onResolved、onRejected 存起来就可以了

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
         item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this);
}

Promise.prototype.then = function (onResolved, onRejected) {
  if (this.PromiseState === "resolve") {
    onResolved(this.PromiseResult);
  }
  if (this.PromiseState === "reject") {
    onRejected(this.PromiseResult);
  }
  if (this.PromiseState === "Pending") {
    this.callbacks.push({
      onResolved,
      onRejected,
    });
  }
};

```

#### 16.4.7 then 方法结果返回

#### 16.4.8 异步修改 then 方法结果返回

#### 16.4.9 完善 then 方法

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

```

#### 16.4.10 catch 方法，异常穿透与值传递

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

```

#### 16.4.11 resolve 方法封装

#### 16.4.12 all 方法封装

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};
```

#### 16.4.13 race 方法封装

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};

Promise.race = function (value) {
  return new Promise((res, rej) => {
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") return;
        if (item.PromiseState === "resolve") {
          res(item.PromiseResult);
        }
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        }
      });
    } catch (e) {}
  });
};

```

#### 16.4.14 then 方法异步执行

给 then 里面的回调添加一个定时器，让回调异步执行就可以了

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      setTimeout(() => {
        ChangePending(onResolved);
      });
    }
    if (this.PromiseState === "reject") {
      setTimeout(() => {
        ChangePending(onRejected);
      });
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          setTimeout(() => {
            ChangePending(onResolved);
          });
        },
        onRejected: function () {
          setTimeout(() => {
            ChangePending(onRejected);
          });
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};

Promise.race = function (value) {
  return new Promise((res, rej) => {
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") return;
        if (item.PromiseState === "resolve") {
          res(item.PromiseResult);
        }
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        }
      });
    } catch (e) {}
  });
};

```

#### 16.4.15 class 版本的封装

下面这个是 class 版本的封装

```javascript
class Promise {
  // 构造函数
  constructor(executor) {
    //添加属性
    this.PromiseState = "Pending";
    this.PromiseResult = null;
    this.callbacks = [];
    //将对象自己保存到_this
    const _this = this;

    function resolve(data) {
      if (_this.PromiseState === "Pending") {
        _this.PromiseState = "resolve";
        _this.PromiseResult = data;
        _this.callbacks.forEach((item) => {
          if (item.onResolved) {
            item.onResolved(data);
          }
        });
      }
    }

    function reject(data) {
      if (_this.PromiseState === "Pending") {
        _this.PromiseState = "reject";
        _this.PromiseResult = data;
        _this.callbacks.forEach((item) => {
          if (item.onRejected) {
            item.onRejected(data);
          }
        });
      }
    }

    try {
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  // then方法
  then(onResolved, onRejected) {
    const _this = this;
    if (typeof onRejected !== "function") {
      onRejected = (reason) => {
        throw reason;
      };
    }
    if (typeof onResolved !== "function") {
      onResolved = (value) => value;
    }
    return new Promise((res, rej) => {
      function ChangePending(onChange) {
        try {
          const onResult = onChange(_this.PromiseResult);
          if (onResult instanceof Promise) {
            onResult.then(
              (value) => {
                res(value);
              },
              (reason) => {
                rej(reason);
              }
            );
          } else {
            res(onResult);
          }
        } catch (e) {
          rej(e);
        }
      }
      if (this.PromiseState === "resolve") {
        setTimeout(() => {
          ChangePending(onResolved);
        });
      }
      if (this.PromiseState === "reject") {
        setTimeout(() => {
          ChangePending(onRejected);
        });
      }
      if (this.PromiseState === "Pending") {
        this.callbacks.push({
          onResolved: function () {
            setTimeout(() => {
              ChangePending(onResolved);
            });
          },
          onRejected: function () {
            setTimeout(() => {
              ChangePending(onRejected);
            });
          },
        });
      }
    });
  }

  //catch方法
  catch(onRejected) {
    this.then(undefined, onRejected);
  }

  // resolve方法
  static resolve(value) {
    return new Promise((res, rej) => {
      try {
        if (value instanceof Promise) {
          value.then(
            (data) => {
              res(data);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(value);
        }
      } catch (e) {
        rej(e);
      }
    });
  }

  //reject方法
  static reject(value) {
    return new Promise((res, rej) => {
      rej(value);
    });
  }

  // all方法
  static all(value) {
    return new Promise((res, rej) => {
      const array = [];
      try {
        value.forEach((item) => {
          if (item.PromiseState === "Pending") throw new Error("");
          if (item.PromiseState === "reject") {
            rej(item.PromiseResult);
          } else {
            array.push(item.PromiseResult);
          }
        });
      } catch (e) {
      } finally {
        if (value.length === array.length) {
          res(array);
        }
      }
    });
  }

  // race方法
  static race(value) {
    return new Promise((res, rej) => {
      try {
        value.forEach((item) => {
          if (item.PromiseState === "Pending") return;
          if (item.PromiseState === "resolve") {
            res(item.PromiseResult);
          }
          if (item.PromiseState === "reject") {
            rej(item.PromiseResult);
          }
        });
      } catch (e) {}
    });
  }
}
```

下面这个是使用原型来控制的封装

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      setTimeout(() => {
        ChangePending(onResolved);
      });
    }
    if (this.PromiseState === "reject") {
      setTimeout(() => {
        ChangePending(onRejected);
      });
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          setTimeout(() => {
            ChangePending(onResolved);
          });
        },
        onRejected: function () {
          setTimeout(() => {
            ChangePending(onRejected);
          });
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};

Promise.race = function (value) {
  return new Promise((res, rej) => {
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") return;
        if (item.PromiseState === "resolve") {
          res(item.PromiseResult);
        }
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        }
      });
    } catch (e) {}
  });
};

```

### 16.5 async 和 await 函数

#### 16.5.1 async

返回值未 Promise 类型的对象，其基本和 then 的返回的逻辑是一样的

```javascript
async function fn() {
  // return "ok"
  // throw "Error"
  return new Promise((res, rej) => {
    rej(111);
  });
}
let result = fn();
console.log(result);
```

#### 16.5.2 await

1.await 右侧的表达式一般为 promise 对象，但也可以是其它的值

2.如果表达式是 promise 对象，await 返回的是 promise 成功的值

3.如果表达式是其它值，直接将此值作为 await 的返回值

注意

1.await 必须写在 async 函数中，但 async 函数中可以没有 await

2.如果 await 的 promise 失败了，就会抛出异常，需要通过 try.catch 捕获处理

```javascript
async function fn() {
  const p = new Promise((res, rej) => {
    res(111);
  });
  const result = await p;
  console.log(result);
}
fn();
```

![image-20220607163943022](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317916.png)

#### 16.5.3. async 和 await 实践

##### 16.5.3.1 读取文件

```javascript
const fs = require("fs");
const util = require("util");

const miniReanFile = util.promisify(fs.readFile);

async function main() {
  try {
    let a = await miniReanFile("./1.txt");
    let b = await miniReanFile("./2.txt");
    console.log(a + b);
  } catch (e) {
    console.log(e);
  }
}
main();
```

##### 16.5.3.2 发送 AJAX 请求

```javascript
async function GetAjax(url) {
  const result = await new Promise((res, rej) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.send();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status >= 200 && xhr.status < 300) {
          res(xhr.response);
        } else {
          rej(xhr.status);
        }
      }
    };
  });
  console.log(result);
}
GetAjax("http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList")
```

## 17. Set

### 17.1 基本介绍

![image-20221026191219899](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317938.png)

Set 是一种新的数据结构 Set 集合，他类似于数组，但是值是唯一的，并且这个集合实现了 Iterator 接口，所以可以使用 for..of 来遍历

```javascript
let s = new Set(["1", "2", "3", "4", "1"]); // Set的一个功能就是对数组进行去重操作

console.log(s, ...s); // Set也支持扩展运算符(...)
```

![image-20221026191115688](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317993.png)

假如你传入的是对象的话，就不会去重。因为对象的本质就是一个内存地址，每创建一个对象内存地址都不一样

![image-20221026190657580](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317071.png)

### 17.2 常用方法

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

### 17.3 强引用/弱引用

我们创建了这样一个对象。其中`obj`和`obj.friend`就是强引用，假如把它们设置为`null`的话，这样就没有其他引用指向它，那么就会被销毁。

这个时候我们使用`WeakSet`引用的话，就是弱引用。弱引用和强引用的区别就是，弱引用依旧可以使用`info.name`来获取数据，但是`GC`在回收的时候不会管这条引用，依旧会直接销毁该对象

其中`WeakSet`对对象的引用就是一个弱引用

![image-20221026194830206](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317261.png)

### 17.4 WeakSet

![image-20221026195714972](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317413.png)

![image-20221026195903717](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317436.png)

```javascript
let ws = new WeakSet();
ws.add({ name: "张三" });
```

当然`WeakSet`的应用场景比较少，下面就是为数不多的几个。下面的应用场景是只**允许对象隐式调用，而不允许对象显示调用**

下面为解释，其中有一个点就是为什么不能使用`Set`。因为`Set`是一个强引用，后期假如要消除对象`p = null`的时候，因为`Set`也强引用了一份，所以并不会删除该对象，还需要`Set`来删除一份，才能消除该对象。

![image-20221028083820114](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317459.png)

## 18. Map

### 18.1 基本介绍

![image-20221028091656426](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317506.png)

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

![image-20221028090516235](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317640.png)

### 18.2 常见方法

![image-20221028091744290](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317031.png)

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

![image-20221028091347243](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317054.png)

### 18.3 WeakMap

![image-20221028092734965](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317124.png)

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

![image-20221028093009748](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317150.png)

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

![image-20221028095620864](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317180.png)

## 19. class

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

### 19.1 静态类成员

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

### 19.2 继承

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

### 19.3 子类对父类的重写

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

![屏幕截图 2022-02-18 172550](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317306.png)

### 19.4 getter 和 setter

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

## 20. 数值扩展

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

## 21. 对象方法扩展

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

## 22. 模块化

### 22.1 介绍

模块化是将一个大的程序，拆分为许多的小文件，然后将小文件组合起来

![屏幕截图 2022-02-18 195939](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317643.png)

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

![屏幕截图 2022-02-18 203109](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317662.png)

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

## 23. Proxy

### 23.1 基本介绍

![image-20221031194903880](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317678.png)

### 23.2 基本使用

![image-20221031194917564](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317698.png)

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

![image-20221031195853977](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317755.png)

### 23.3 捕获器

![image-20221031201746183](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317806.png)

下面时`apply`、`construct`的捕获器的使用案例

![image-20221031202508028](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317253.png)

## 24. Reflect

[[Reflect]]

## 50. 案例

### 50.1 let 实践

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

### 50.2 箭头函数实践

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

### 50.3 扩展运算符实践

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

### 50.4 生成器函数实践

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

### 50.5 Promise 实践

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

### 50.6 set 实践

**数据去重**

但是这里不是数组去重，而是 set 数据

```javascript
let arr = ['1','2','3','4','5','1'];
let result = new Set(arr);
console.log(result);
```

![屏幕截图 2022-02-18 160928](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317214.png)

这里我们使用扩展运算符，将数组序列转换为数组

```javascript
let arr = ['1','2','3','4','5','1'];
let result = [...new Set(arr)];
console.log(result);
```

![屏幕截图 2022-02-18 161058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317239.png)

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

# 19. ES7

## 1. includes

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

## 2. 指数运算符

```javascript
// 1. 以前的处理方式
Math.pow(2, 3) // 8

// 2. 使用指数运算符的处理方式
2 ** 3 //8
```

# 20. ES8

## 1 values/keys

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

![image-20221029081809400](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317261.png)

当然`values()`也可以来拆分字符串

![image-20221029081942555](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317279.png)

## 2 entries

将传入得数据转换为`[[keys,value]]`得形式，为了方便遍历得操作

![image-20221029082341248](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317742.png)

## 3 padding

对字符串得首尾进行填充，第一个参数为填充之后得字符串得长度，第二个参数是要填充得字符

![image-20221029082730070](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317762.png)

## 4. getOwnPropertyDescriptors

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

![屏幕截图 2022-02-19 164652](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317796.png)

# 21. ES9

## 1. rest 参数

这个是扩展运算符关于对象的使用

```javascript
function con({name,...other}){
	console.log(name);
	console.log(other);
}
con({
	name:'张三',
	age:12,
	sex:'男'
});
```

![屏幕截图 2022-02-19 165451](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317838.png)

## 2. 扩展运算符

其基本的原理也是 ES 差不多

```javascript
const p1 = {
	name1:'张三',
	age:12
}
const p2 = {
	name2:'李四'
}
const p3 = {
	name3:'王五'
}
const l = {...p1,...p2,...p3};
console.log(l);
```

![屏幕截图 2022-02-19 165849](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317860.png)

# 22. ES10

## 1. formEntries

这个在 ES8 里面的`entries`的逆运算，`entries`是将对象、数组、字符串的属性转换为`二维数组`，而它可以转换为对象形式

![image-20221029091144488](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317896.png)

当然这个`API`也是有自己得应用场景得

![image-20221029092005237](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317314.png)

## 2. trimLeft/trimRight

![image-20221029090616872](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317338.png)

## 3. flat

`flat`是将**高维数组转换为低维数组**。flat 方法里面的参数，表示消除的维数

![image-20221029090525113](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317363.png)

## 4. flatmap

![image-20221029090652052](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317382.png)

下面就是其中得一个应用场景，首先是`item.split()`是将字符切割为一个数组了，最后返回得值为`[[Hello,World],[hello lyh],[my,name,is,coderwhy]]`，但是`flatMap`最后会做一个`flat`得操作。

![image-20221029090912389](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317404.png)

## 4.Symbol 扩展

显示 Symbol 里面的值

```javascript
let s = Symbol('张三');
console.log(s.description);
```

# 23. ES11

## 1. 私有属性

在属性里面前面写上#就是代表为私有属性

```javascript
class Person{
	//公有属性
	name;
	//私有属性
	#age;
	#weight
	constructor(name,age,weight) {
		this.name = name;
		this.#age = age;
		this.#weight = weight;
	}
	say(){
		console.log(name);
		console.log(age);
	}
}
```

## 2. Promise 扩展

allSettled 方法的特点就是即便里面的 2 个 Promise 的返回值是错误的，但是最后的结果依然正确的，这就和 all 不一样，all 是只要有一个错误的就是错误的

```javascript
const p1 = new Promise((resolve,reject)=>{
	reject();
});

const p2 = new Promise((resolve,reject)=>{
	resolve();
});

let ps = Promise.allSettled([p1,p2]);
console.log(ps);

let pa = Promise.all([p1,p2]);
console.log(pa);
```

## 4. 可选链操作符

```javascript
function main(config) {
  let result = config && config.db && config.db.host;
  console.log(result);
}
main({
  db: {
    host: 123,
  },
  cc: {
    id: 200,
  },
});
```

假如`main`里面不传入参数呢？这样就会导致报错

![屏幕截图 2022-02-19 181857](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317467.png)

`?.`是判断前面的有没有，没有的话就返回 undefined，有的话就连接后面的

```javascript
function main(config){
	let result = config?.db?.host;
	console.log(result);
}
main()
```

![image-20221029105746058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317881.png)

## 5. 动态 import

不像以前一样一次性将入口文件里面的 import 全部加载

当你点击按钮的时候，就会加载 hello.js

```html
//html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>

	</head>
	<body>
		<button type="button">按我</button>
		<script src="js/open.js" type="module"></script>
	</body>
</html>
```

```javascript
//open.js
var btn = document.querySelector('button');

btn.onclick = function() {
	import('./hello.js').then(aa => {
		aa.say();
	})
}
```

```javascript
//hello.js
export let name = '张三'
export function say(){
	console.log('Hi!');
}
```

## 6. BigInt 类型

对于`JS`能处理数字最大只有下面的 2 个，其中`MAX_SAFE_INTEGER`表示可以操作的安全数字

![image-20221029092442691](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317905.png)

这是 ES11 新引入的数据类型，用于扩大最大数值

![image-20221029092922583](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317922.png)

## 7. globalThis

绝对全局对象，这样就可以忽略环境直接操作，也就是在`浏览器`下面运行是`Window`，在`Node.js`下面运行的是`global`

![image-20221029110807340](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317940.png)

## 8. ??

MDN 参考文档：[空值合并运算符（??） - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator)

以前对于这种需求都是使用`foo || "hello World!"`的方式来处理的，但是这种处理方式不是很好，因为当`foo`为`0或者""`的时候就会判断为`Hello World!`

![image-20221029093441766](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317988.png)

# 24. ES12

## 1. 大数连接符

可以使用`_`来连接数字，来表达大的数据

![image-20221020173926402](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317022.png)

## 2. FinalizationRegistry

这是一个类，作为`GC`的`Hook`。只要被注册的对象被销毁，就会执行自定义函数

![image-20221029120921813](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317415.png)

![image-20221029120953129](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317433.png)

## 3. WeakRef

这个需要配合上面的`FinalizationRegistry`来阅读。`WeakRef`是用于给传入的对象添加弱引用的

**MDN 文档介绍**：[WeakRef - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)

```javascript
const fr = new FinalizationRegistry((val) => {
  console.log("某一个对象被销毁了~", val);
});

let obj = { name: "张三" };
let info = new WeakRef(obj);

fr.register(obj, "obj");

console.log(info.deref().name); // info.deref()是用于获取原本的对象
obj = null;
```

![image-20221029121829510](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317453.png)

## 4 . 逻辑赋值运算

```javascript
// ||= 逻辑或运算
let message = "";

message = message || "Hello World!";
message ||= "Hello World!";
// ===== 本质和下面的是一样的 ===== //
message = message || "Hello World!"

console.log(message);

// &&= 逻辑与运算
let obj = {
  name: "张三",
  age: 18,
};
let info;
info &&= obj.age;
console.log(info)

// ??= 逻辑空运算
let obj1 = {
  PersonName:'李四'
}
console.log(obj1.name ??= "Hello World!")
```

![image-20221029123641147](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032317479.png)
