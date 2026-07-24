# 1 基本介绍

1、`ES6`引入了一个新的原始数据类型`Symbol`，表示独一无二的值，它是 JS 的第七种数据类型

![[00 assets/4944232ebb70086edb1810dc73df9b0c_MD5.png]]

2、`Symbol`实例是唯一、不可变的，可以用作**非字符串形式的对象属性**，所以使用他没有属性冲突的危险

![[00 assets/138a72af043c8d9c7b703d706a1bd746_MD5.png]]

# 2 基本使用

## 2.1 Symbol()

1、创建一个`Symbol`实例，这里可以这样理解，`Symbol`是身份证，里面的值是`名字`，`名字`可以一样，但是`身份证`不能一样

2、并且`Symbol`不能实例化，只能使用函数的形式

![[00 assets/5336ce5daae61a67ab2d7fad1d594f0c_MD5.png]]

## 2.2 Symbol.for()

1、如果想在全局的注册表中创建，可以使用`Symbol.for()`来创建`Symbol`，它会对传入的`key`做**幂等操作**，也就是会先检测`全局注册表`，如果没有就创建该实例放入`全局注册表`中，如果有的话就直接返回已经创建好的`Symbol`实例

如果想详细知道幂等操作可以查看下面的链接：[(1 封私信 / 80 条消息) 什么是幂等？如何解决幂等性问题？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/534651475)

![[00 assets/b6694fc4898743d5abc7ac5bc86c973a_MD5.png]]

2、并且直接使用`Symbol.for()`全局注册表中创建的`Symbol`实例和直接使用`Symbol()`创建的`Symbol`实例也不相同

![[00 assets/8fc881d6b382fc7b0ef98e100d410990_MD5.png]]

## 2.3 Symbol.keyFor()

1、使用`Symbol.keyFor()`来在`全局注册表`中查找对应的`key`，否则就返回`undefined`

![[00 assets/d3095b0b9536fd535bd4ccc1a2dcb190_MD5.png]]

# 3 对象属性

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

# 4 遍历 Symbol

![[00 assets/f7fe2f1367124b92c5a0276fd8911ad9_MD5.png]]

# 5 内置 Symbol

## 5.1 Symbol.asyncIterator

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

## 5.2 Symbol.hasInstance

1、检测构造器对象是否认可一个对象是它的实例，一般情况下使用`instanceof`操作符来处理，在`ES6`之后使用`Symbol.hasInstace`来处理

![[00 assets/dccd414cc4a262464b7f72753d42d7b4_MD5.png]]

## 5.3 Symbol.isConcatSpreadable

![[00 assets/48cdee1fa4acb4bad5d3eecd36c7bdfd_MD5.png]]

## 5.4 Symbol.iterator

[[迭代器]]

## 5.5 Symbol.match

1、默认情况下使用`String.match`是使用`Symbol.match`，那么这个也可以改写。而且我们为`match`传输非正则值得话，会导致该值自动转为`RegExp对象`，所以我们可以手动修改该默认模式

![[00 assets/03827aa0a7a9b46abe4eaef71f99df95_MD5.png]]

2、当然我们可以使用`[Symbol.match]`来重写`match`默认模式

![[00 assets/8e29ec95fe3cc912a6e27fda4e02f049_MD5.png]]

## 5.6 Symbol.replace

1、使用`[Symbol.replace]`也可以改变`replace`得默认行为，因为和`Symbol.match`得特性一样，如果为`String.replace`传入非正则表达式，那么就会将该值转为`RegExp对象`

![[00 assets/a1aced0cb36ab886f307e64ef7d2629a_MD5.png]]

## 5.7 Symbol.search

1、整体和`Symbol.match`的特性一致，这里就不赘述了

![[00 assets/e2aec76026bed88e51b3f0b9e70d6f1c_MD5.png]]

## 5.8 Symbol.species

1、`Symbol.species`用于改变内置类型实例方法的返回值暴露实例化派生对象的方法

2、我们来一个一个解析内置类型的实例方法，数组的 `map`、`filter`、`slice` 等方法都会返回一个新的数组。`Symbol.species` 的目的是允许你通过`派生类`来定制这些方法返回的新实例。这就为你提供了一种改变数组方法的默认行为的方式。

3、下图中`personArray`和`animalArray`属于派生类

![[00 assets/7a6ec5e8722d9ba682ca186c14deada8_MD5.png]]

## 5.9 Symbol.split

1、和`Symbol.match`类似，直接参考之前的就行

![[00 assets/2bd4e8c0b2908ffd11462473046e9541_MD5.jpeg]]

## 5.10 Symbol.toPrimitive

1、很多情况下有很多人会将对象转为原始类型，比如如下情况

![[00 assets/c9bc6d3d8185148c7019898f1341037b_MD5.jpeg]]

2、为了改变这样的默认行为，可以使用`Symbol.toPrimitive`

![[00 assets/a1a643db22d94e5a2fd9a3e4bb6beb47_MD5.png]]

## 5.11 Symbol.toStringTag

1、创建对象的默认字符串描述，并且由`Object.toString()`使用

2、按照正常输出模式`Person`为`[Object Object]`，实际却输出了`[Object Person]`，和预期不符合，这里以后可以留意一下

![[00 assets/87db7b0de405f5fb45d2a39a7306dcd6_MD5.png]]
