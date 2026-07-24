# 1 基本使用

1、我们可以使用下面的方式来定义`单个`或者`多个`变量，还可以使用`const`来定义常量，常量不能改变的
![[00 assets/7b5dd863d731c21b93f94ae9064ea180_MD5.jpeg]]

# 2 命令规范

1、关键字`MDN`文档：[词法文法 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/web/javascript/reference/lexical_grammar)
![[00 assets/3099091422573188e4eadf0d89f0e5e6_MD5.jpeg]]

# 3 数据类型

## 3.1 基本介绍

![[00 assets/3035a1c2a3812ea81d53ec53bb33fac7_MD5.png]]

## 3.2 typeof

![[00 assets/c2788ad49b620642c94716f4566c5f83_MD5.jpeg]]

![[00 assets/a0f88d1d2e3f24330d858638bb863555_MD5.png]]

## 3.3 原始类型

### 3.3.1 Number

我们即便使用`typeof`检测`infinity...`都会是`number`类型

![[00 assets/479e497924a491931483778c3cd7c26b_MD5.png]]

![[00 assets/7509df5ea4170a1b36fbbe5b8d6c5d13_MD5.jpeg]]

### 3.3.2 String

![[00 assets/34eb84c404077fd2d49450b480aa1222_MD5.png]]

![[00 assets/ea1953919999783df7ed066e0c731312_MD5.png]]

![[00 assets/b2b51f4aca773ca08629ef50d64089f1_MD5.jpeg]]

### 3.3.3 Boolean

![[00 assets/55d9bc93594063f0861cbeb6d63385dd_MD5.jpeg]]

### 3.3.4 Undefined

![[00 assets/628b9bf648dd08a74d0572571bb60c99_MD5.png]]

### 3.3.5 Object

![[00 assets/e57d5a435928d7358ce47004666295e1_MD5.png]]

### 3.3.6 Null

![[00 assets/37be54127c800dfa848d785eac94362e_MD5.png]]

## 3.4 类型转换

### 3.4.1 转为 String

![[00 assets/097d5d1e0b9be81bda1fe45410745961_MD5.png]]

![[00 assets/f22b48e5f893b6868d9ef3120296184e_MD5.jpeg]]

### 3.4.2 转为 Number

![[00 assets/cd8a1b9e78f122aefbcc67f935f7ca8a_MD5.jpeg]]

![[00 assets/a5ef1148009381a23e33550d6af7bfa0_MD5.jpeg]]

### 3.4.3 转为 Boolean

![[00 assets/56a964019aabd4234c1f746f9ab78bab_MD5.png]]

![[00 assets/da1152bc10798467b2ee01795bb7130b_MD5.jpeg]]


# 4 let

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

# 5 const

```javascript
// 常量一定要赋初始值
const name = "张三";

name = "李四" // 报错，常量不能修改

console.log(name);
```

假如我们要传递引用类型的话。结果是不会报错的，这是因为，我们保存的是`obj`的地址值

![[00 assets/cdafff26c6426c11c54db501a69d8928_MD5.png]]

# 6 作用域提升

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

# 7 window 关系

在以前的`var`声明的对象都会添加到`window`中，因为在`GO`中的`window`指向的是`this`，所以在全局创建的变量都会保存到`GO`中，也就是`window`

![[00 assets/d853e64dde1ff5babc2db101876c4583_MD5.png]]

但是在`ES6`之后，这个可以参考我`JS高级 - 环境`的笔记。

原本的`GO(VO)`是一个对象，保存变量的时候直接就是`GO.name = "张三"`。但是在现在是`VE`，不是一个对象，最后的数据都会保存在`variables_`，他的数据类型是`VariableMap`，他是一个`HashMap`，也就是一个哈希表，底层通过`C++`实现

因为以前都是`window`指向着`GO`，但是现在使用`let/const`就不会保持同步了。

![[00 assets/c704a72f5d0489e063bc6782c80b922d_MD5.png]]

下面为`variables_`的源码，下面的注释就已经写了

![[00 assets/ddcd9e409eaa5e43cdf1dbc10291820f_MD5.png]]


# 8 var/let/const 选择

![[00 assets/204db614c373655d9cf226c2820dfce8_MD5.png]]

# 9 变量的解构赋值

允许按照一定模式从数组和对象中提取值，对变量进行赋值，这被称为解构赋值

## 9.1 数组结构

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

## 9.2 对象结构

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

## 9.3 解构场景

![[00 assets/d1e025428ccf168ace8b4ddcc73b710a_MD5.png]]
