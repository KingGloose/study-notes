\*视频讲解\*\*：CodeWhy 王红元 - 深入了解 JavaScript

视频讲解：[尚硅谷 Web 前端 ES6 教程，涵盖 ES6-ES11\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1uK411H7on/?spm_id_from=333.337.search-card.all.click)

# 1.浏览器工作原理

这个可以参考我以前的笔记

# 2. V8 引擎

^315c55

## 2.1 定义

1.`V8`是 Google 用 `C++` 编写的开源高性能 `JuuavaScript`和`WebAssembly`引擎，它用于`Chrome`和`Node.js`（在`node.js`中就内置了`V8引擎`，所以我们可以使用`Node.js`来执行`JavaScript`代码，`node xxx.js //执行的js文件`）

2.它实现`ECMAScript`和`WebAssembly`，并在 Windows7 或更高版本，macOS10.12+ 和 使用 x64，IA-32ARM 或 MIPS 处理器的 Linux 系统上运行，所以`兼容性`是没什么太大问题的

3.`V8`可以独立运行，也可以嵌入到任何`C++`应用程序中。

## 2.2 解释细节

![[00 assets/f4d82d0901ecf5412501912b0ffbd3b9_MD5.png]]

### 2.2.1 **Parse**

`Scanner`对`JS`进行解析，它分为**词法分析**和**语法分析**，比如说: `const name = "张三";`

这里需要注意的一点，因为只是`Scanner`对`JS`代码的分析，所以并不会去执行`JS`代码

```javascript
/*
	在解析阶段只知道flag为let，并且分析出他的类型和变量名，这个时候jS引擎还不知道flag值为true，
	只有在转换为字节码之后,真正运行的时候才会将true赋值给flag
*/
let flag = true
if(flag){}
```

**词法分析**：首先是对于我们每一行的`JS`代码进行切割，大致可以分为：`const`、`name`、`=`、`"张三"`......，然后会生成一个`token数组`，里面存放的就是我们切割的数据的参数

```json
token = [
    {type:"keyword",value:"const",......}
    {type:"identifier",value:"name",......}
    ......
]
```

**语法分析**：根据词法来进行分析，最后生成**AST**(**抽象语法树**)，这个网站就可以生成并且显示抽象语法树：[AST explorer](https://astexplorer.net/)

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032311484.png" alt="image-20220518121745152" style="zoom:67%;" />

这个抽象语法树不仅仅用于`V8引擎`，还有`Vue`、`Typescript`、`babel`......

`V8`的`Parse`解释的官方文档：https://v8.dev/blog/scanner

### 2.2.2 **Ignition**

可以理解为一个**转换器**，将我们的**抽象语法树**转换为**字节码**，这里为什么需要转换为字节码，因为浏览器天然的兼容性，所以需要在不同的机器上面来运行浏览器。我们直接转换为二进制代码的话会出现问题，比如：每个机器的**CPU 架构**都是不一样的。对于`AMD`，`1100`表示的是打开，但是`Intel`表示关闭。

所以为了**解决跨平台的问题**，就需要将**抽象语法树**转化为**字节码**

当一个`函数`执行多次的时候，会标记该函数为**热点函数**，同时会收集`TurboFan优化`所需要的信息（比如函数参数的类型信息，有了类型才能进行真实的运算），然后将该函数解释为`机器码`存储起来，提高性能。

如果该函数只调用一次的话，`Ignition`会解释为`字节码`，而不是`机器码`。并且`TurboFan`在优化的时候会收集参数类型，所以我们在多次调用函数的时候，运用不同的数据类型，会导致性能变差

`Ignition`的`V8`官方文档：https://v8.dev/blog/ignition-interpreter

### 2.2.3 **TurboFan**

这个是优化的操作，以前是直接将`字节码`转换为`汇编语言`，再转换为`二进制代码`，这样转换会影响性能。所以就会有`TurboFan`。它可以直接将`字节码`转换为`二进制`代码保存起来，提高性能

但是并不是每条语句都保存，而是将重复使用的语句进行保存，比如说下面的

```javascript
//这个就不转换,因为只执行了一次
function fn(){
	console.log("111")
}
fn()

//这个就转换，因为多次使用了，所以TurboFan就会进行优化
function fn1(){
    console.log("123")
}
for(var i = 0;i < 10 ; i++){
    fn1()
}
```

`TurboFan`的`V8`官方文档：https://v8.dev/blog/turbofan-jit

### 2.2.4 **Deoptimization**

每次传给函数的参数都不一样的话，`V8引擎`就会将`机器码`转化为`字节码`，这个就是负优化。所以这里就给了我们一个优化的方式，我们在传入参数的时候，尽量使用相同类型的

```javascript
function fn(a , b){
	return a + b;
}
fn(1 , 2);
fn(2 , 3);
fn("a" , "b"); //类型不同，又转换为字节码了，这个会造成性能损失
```

### 2.2.5 PreParser

![[00 assets/3f970049e1e2fce6d01fcbaa5329c143_MD5.png]]

首先是`Scanner`通过**词法分析**将`JavaScript`每行代码转换为`token数组`。然后再将`token数组`给`Parser`，进行了`语法分析`，接着转换为`AST`树

但是为什么这里多了一个**PreParser**呢？这个是**预解析**，网页打开的时候并不是**每个函数都会执行**。那么对所有的 JavaScript 代码进行解析，必然会影响网页的运行效率。所以**V8 引擎**就实现了**Lazy Parsing(延迟解析)**的方案，它的作用是**将不必要的函数进行预解析**，也就是只解析暂时需要的内容，而**对函数的全量解析是在函数被调用时才会进行**；比如我们在一个函数 outer 内部定义了另外一个函数 inner,那么 inneri 函数就会进行预解析；

```javascript
function Outer(){
	function Inner(){} // 只有在函数执行的时候才会对里面进行解析
}
Inner();
```

## 2.3 执行过程

![[00 assets/3f970049e1e2fce6d01fcbaa5329c143_MD5.png]]

下面是大致的执行过程

1.**Blink**将源码交给**V8 引擎**，**Stream**获取到源码并且进行**编码转换**，如图中的`ASCII`....

2.**Scanne**r 会进行**词法分析**，**词法分析**会将代码转换成**token 数组**。

3.经过**Parser**和**PreParser**，接下来**token 数组**会被转换成**AST 树**

4.经过**Ignition**将**AST 树**转化为**字节码**或者**机器码**，这个函数的调用情况来定

## 2.4 GO

我们在通过**Parse**转化为**AST 树**的时候，会自动创建一个**GlobalObject 对象**，这就是为什么我们可以直接使用 Math、Date、String......方法

```javascript
//这就是为什么我们能直接使用下面的方法的原因
setTimeout(() => {
	console.log("1111")
}, 1000);

console.log("2222")
```

并且**GlobalObject 对象**里面有**window 属性**，它的值就是指向的自己

```javascript
var GlobalObject = {
	String:......,
	Date:......,
	window:this， // 值也可以是GlobalObject
    str:undefined,	//js代码中的值，一开始为undefined
    num1:undefined,
    num2:undefined,
    result:undefined
}
```

**V8 引擎**里面会有一个**执行上下文栈**。但是我们为了执行**全局代码**，所以就会创建一个**全局可执行上下文(GEC)**，里面有一个**可变对象(VO)**，它指向的就是**Parser**阶段创建在**堆**里面的**GlobalObject**。

这个时候才会从上到下执行代码，通过**VO**找到**name**就将值赋值给**GlobalObject**里面的**name**

![[00 assets/722fa03f150780a2f089d1cfc57ebc44_MD5.png]]

假如看懂了上面的流程，就知道下面的原理了。下面这个模式可以叫做**作用域提升**。

首先是创建**GlobalObject**，然后将**a**传入，但是值为**undefined**，执行全局的代码前先创建一个**VO**，它指向的就是**GO**。然后从上到下执行代码，就通过**VO**将值给了**GO**。这个时候**a**的值就是**2**，而不是**undefined**

```javascript
a = 2;
var a;
console.log(a); //输出结果：2
```

假如我们看懂了上面的执行情况之后，再来看下面的内容

```javascript
var a = 2;
console.log(a);
var b = 3;
console.log(c);
var c = 4;
console.log(window);
```

因为`window`的值就是`this`，即指向的就是`GO`。所以可以看到全局中的变量

![[00 assets/86cf384caed721080562400973fb9027_MD5.png]]

# 3. 函数执行

## 3.1 执行过程

✨ 该点是`ECMAScript`以前的方式，具体可以参考`3.3`，略作修改不影响流程

下面就来介绍一下在`JS`中函数执行的过程

![[00 assets/a895d9b12bedb6d1036e18924e3c86e3_MD5.png]]

下面就是执行过程的简要表述

![[00 assets/fb4c9f13e9f7c8ebbf946ada093dc0af_MD5.png]]

1.因为是函数内部存在变量，通过**预解析**处理，并不会在开始就去处理函数内部的执行。并且在**Parser 阶段**解析为**AST 树**的时候创建**GO**。

2.然后**全局执行上下文**中会从上往下来执行代码，遇到变量就会让`VO`转存到`GO`中，当执行到到`var name = 'why'`是先保存到调用栈中，然后再保存到堆中的**GO**，即`GO.name = 'why'`(这个只是形象表示，在**ES5**之前是这样的，但是在**ES6**之后就已经修改了`GO`的形式)

3.当执行到`function foo(num)...`的时候，就会通过`VO`将`foo`的内存地址存到`GO`中

4.这个时候`JS`就会创建一个**存储函数空间**，对于这个内存地址，这个时候`GO`中的`foo`存的该**存储函数空间**的**内存地址**。并且在**存储函数空间**里面还包含了**父级作用域**

5.当要执行这个函数的时候，就会在`ECStack`（调用栈）里面创建一个`函数执行上下文`，这里面会创建一个`VO`，这个和全局执行上下文里面的**VO**执行功能是一样的。

6.当出现了`函数执行上下文`的时候，就会创建该函数的**AO**，并且该**函数执行上下文**的**VO**指向着该**AO**

7.当函数执行完毕就会将`函数执行上下文`销毁掉，其中**VO 对 AO**的引用解除。在没有任何变量引用该内存地址的情况下，内存回收机制就会通过算法将该地址回收掉。

## 3.2 作用域链

✨ 该点是`ESMAScript`以前的方式，具体可以参考`3.3`，略作修改不影响流程

### 3.2.1 单函数模式

在一个函数`AO`中不存在的变量，会到上级函数作用域中去寻找

![[00 assets/b89898c5bb218639ec3db980ad9c3d95_MD5.png]]

当**函数执行上下文**执行到`console.log(name)`的时候会发现自己函数的**AO**中并不存在该变量，就会通过自身存储函数空间的**scope 属性**中找到上级函数的**AO**，通过`函数执行上下文`的**VO**对上级进行寻找。

但是这个是单函数，并不存在函数的嵌套，所以`parent scope`就是`GO`

![[00 assets/fbed062b6b3721e2a9c123eb94bed2bf_MD5.png]]

✨`JavaScript`存在一些特性。当我们在`foo()函数`中写了`var m = 100`的话就会报错该变量**m**找不到。但是按照下面的书写方式就不会报错，而且会把该变量加到`GO`中，所以可以打印出来

![[00 assets/91505a71806b6b1496ec06f3a3bf3a4b_MD5.png]]

### 3.2.2 函数嵌套

下面就是函数嵌套中的作用域链，可以发现他不只是会向上寻找一次，而是找到`GO`为止

![[00 assets/8fb1f3ff7045accb0e5f72843aa23ab7_MD5.png]]

假如出现下面函数嵌套的情况，当**foo**的**函数执行上下文**执行到`bar()`的时候，就会创建**bar**的**存储函数空间**，在 foo 的 AO 中的 bar 指向的就是**bar**的存储函数空间。该空间里面的**scope**指向的就是**foo**的**AO**（这也可以知道 foo 的存储函数空间中的 scope 指向的就是 GO 了）

并且在调用栈里面会创建 bar 的**函数执行上下文**，当该函数执行上下文执行到`console.log(name)`的时候，就会在 bar 的**AO**中去寻找，没有就会跟着**scope 的地址找到 foo 的 AO**来寻找，没有就会跟着**foo 的 scope 的地址找到 GO**，这个时候就可以找到 GO 中的 name

![[00 assets/c4c255f14ef1d526b144d8512fd4c1b3_MD5.png]]

✨ 这里需要知道一个细节：一些浏览器中的`window`中会包含一些属性，比如：`name`...。当根据作用域链来寻找都会找到`window`，所有有些时候你即便在全局不写该变量，我们去调用的时候也不会报错

![[00 assets/0742cfbd93a9c87c49b0492f8cb1bfd1_MD5.png]]

### 3.2.3 函数内调用

因为`function ...`写在`GO`里面，所以其作用域链中的父作用域就是`GO`。所以调用在那个位置不影响它的`作用域链`

![[00 assets/fc2ac50d7a70b9d641b33511f6fcf54f_MD5.png]]

### 3.2.4 面试题

![[00 assets/fb4867eb9ef022478b787c96ec5e8618_MD5.png]]

当函数得参数有默认参数得情况下，会形成一个新得作用域，这个作用域用于保存参数得值。

比如说：`foo()`中得`y`和`x`就是一个全新得`参数作用域`。如果没有`参数默认值`得话，那么就只存在`函数内部作用域`

![[00 assets/7650fc1202f34afe68d44f1121820e39_MD5.png]]

## 3.3 变量环境和记录

> 早期的版本

上面做的笔记都基于`ESMAScript 5`以前的

![[00 assets/9914304f1a103e84d2ae29cb03b30492_MD5.png]]

> 最新的版本

将前面的`GO`和`AO`改成了`变量环境(VE)`，这样的话就可以理解为以前的`GO`和`AO`对象形式改变，在底层可能就不是对象来处理了

原本的`GO(VO)`是一个对象，保存变量的时候直接就是`GO.name = "张三"`。但是在现在是`VE`，不是一个对象，最后的数据都会保存在`variables_`，他的数据类型是`VariableMap`，他是一个`HashMap`，也就是一个哈希表，底层通过`C++`实现

![[00 assets/d7f47096ecb368cc7fe3324b08b433e3_MD5.png]]

# 4. 内存管理

## 4.1 基本介绍

> 内存管理

下面的内容就可以参考`深入了解操作系统`

![[00 assets/01b80e1d07970f8fdbf9e64e3fb5a6a6_MD5.png]]

> JS 中的内存管理

JS 在定义变量的时候就会为我们分配内存空间

![[00 assets/81d1d1ef79b538afcfa9d205be45fa67_MD5.png]]

## 4.2 垃圾回收

参考视频：[垃圾回收与内存泄露【渡一教育】-村头一只鹅鹅-稍后再看-哔哩哔哩视频 (bilibili.com)](https://www.bilibili.com/list/watchlater?bvid=BV1fH4y137Sz&oid=1054179753)

### 4.2.1 基本介绍

![[00 assets/732a2bb82e7b29ea4d5d307ea2e6a3e6_MD5.jpeg]]

### 4.2.2 引用计数

1、当然最常见的就是`引用计数算法`，只要有引用的话就会计数+1，其中一个应用就是`AO`中。当计数为 0 的话就会被清除

![[00 assets/40802a567f49a69e40f0436a64fc2819_MD5.png]]

2、但是这个`计数算法`有一个弊端就是循环引用的话就会有问题，这样会导致内存泄漏，比较早的浏览器就是使用的引用计数的方式来处理的，但是后续都换成引用标记清除了

![[00 assets/19001e6d91a774c4b048d5fd396bff04_MD5.png]]

### 4.2.3 标记清除

![[00 assets/e11ff73adfecaa6161f86de58475e903_MD5.png]]

## 5.3 性能优化

> 尽量使用 const 和 let

1、尽量使用`const和let`来提升性能，因为可以更早的进入内存回收机制

2、并且尽量为不要的对象设置为 null，表示以后不会引用

> 隐藏类和删除操作

[V8 引擎隐藏类的概念 - 掘金 (juejin.cn)](https://juejin.cn/post/7240117931886657593)

[javascript - V8 中的隐藏类（Hidden Classes）和内联缓存（Inline Caching） - 个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000039247203)

1、因为 JS 是动态的，所以不可能一开始就默认固定一个对象的属性和属性值，后续还会继续添加，而且 JS 的属性查找的效率很低，所以就有了隐藏类的使用方式

2、初始化会创建一个初始化隐藏类 C0，然后看到存在`name`属性，所以会创建一个`C1`隐藏类，这个时候会有一个 C0 的指针指向 C1，看到 age 属性类似，最后会有 3 个隐藏类

![[00 assets/b29733eebe682f7334f2964cb0cb5ad6_MD5.png]]

3、因为之前对象的隐藏类是一样的，所以会复用隐藏类

4、但是我们为其中一个实例额外赋一个值，就会额外创建隐藏类，所以导致 V8 不能再复用之前的隐藏类，也就造成了性能损失

![[00 assets/04a0a8196681f9938b2cd0cf210566f0_MD5.png]]

5、所以最好使用下面的方式来编写，这样会让使用的 Person 的隐藏类是一样的，也就可以让 V8 复用隐藏类，达到性能优化

![[00 assets/e671ccb8f4b11724c28e237e16828eea_MD5.png]]

6、当然也存在 delete 的方式来删除属性，这也不是很推荐，因为这也会导致隐藏类不一致，导致不能复用

![[00 assets/16a0486ef17d6e477b3208897faf4b86_MD5.png]]

> 内存泄漏

1、为 window 添加变量，因为 widow 不能清除，所以对应的 name 也不能清除

2、定时器的回调通过闭包也会导致内存泄漏

3、如果使用函数闭包也会导致内存泄漏，下面就是一个例子，创建的`innerFn`就会进行闭包，而且`outerFn`执行之后`sum`并没有被消除，就是因为闭包了，如果想释放这个闭包就需要手动设置为`null`，等待 GC 回收

![[00 assets/7e0a3ef16b41baaed9fed8d10efcb5c9_MD5.jpeg]]

# 5. 高阶函数

## 5.1 基本介绍

**把一个函数如果接受另外一个函数件为参数,或者该函数会返回另外一个函数作为返回信的函数,那么这个函数就称之为是一个高阶函数**

> 函数作为另外一个函数的参数

这个方式就很灵活了。你只需要执行执行一个函数，写入不同的参数就能执行不同的业务

```javascript
function calc(num1, num2, fn) {
  console.log(fn(num1, num2));
}

function addfn(num1, num2) {
  return num1 + num2;
}

function subfn(num1, num2) {
  return num1 - num2;
}

// 这样就很灵活,需要调用那个函数直接传入就可以了
calc(1, 2, addfn);
calc(1, 2, subfn);
```

![[00 assets/a878e693e4b6108b89b34ac1981e8782_MD5.png]]

> 函数作为返回值的使用

这样就不需要重复写第一个参数的值，只需要补充后面的参数

```javascript
function fn1(num1) {
  function fn2(num2) { // 这个函数作为返回值
    return num1 + num2;
  }

  return fn2;
}

//这个也同理,前面的fn1()是一个固定的数字，需要调用的时候传入另外一个参数，这样就使操作更加灵活
const result = fn1(5);
console.log(result(6));
console.log(result(7));
```

## 5.2 内置高阶函数

### 5.2.1 filter

```javascript
const nums = [2, 3, 4, 5, 6, 7, 8];

/*
  回调函数参数
  1.item 每个参数
  2.index 当前参数的索引
  3.arr 原数组
*/
var NewArr = nums.filter(function (item, index, arr) {
  return item % 2 === 0 // 返回布尔值
});

console.log(NewArr);
```

![[00 assets/938d53dec711cd376a1e10d142436f12_MD5.png]]

`filter`对于对象的存储是`浅拷贝`，所以我们去修改里面的值也会改变原本数组中的值

![[00 assets/82feddc2177f2232bed5e4e026c857a4_MD5.png]]

### 5.2.2 map

```javascript
const nums = [2, 3, 4, 5, 6, 7, 8];

/*
  回调函数参数
  1.item 每个参数
  2.index 当前参数的索引
  3.arr 原数组
*/
var NewArr = nums.map(function (item, index, arr) {
  return item * 10; // 返回数值
});

console.log(NewArr);
```

![[00 assets/47c2eaf60b560a8d2b8f6bd6e34aa2d6_MD5.jpeg]]

### 5.2.3 forEach

这个可以参考和上面的`map`的区别，`foreach`没有返回值，但是会遍历数组

```javascript
const nums = [2, 3, 4, 5, 6, 7, 8];

nums.forEach((ele) => {
  console.log(ele); // 无返回值
});
```

![[00 assets/3a69ef9f2f21d07dd9c89e081d526cb4_MD5.png]]

当然`forEach`中也可以设置`this`的绑定

### 5.2.4 find

```javascript
const nums = [2, 3, 4, 5, 6, 7, 8];

/*
  回调函数参数
  1.item 每个参数
  2.index 当前参数的索引
  3.arr 原数组
*/
var NewArr = nums.find(function (item,index,arr) {
  return item % 2 === 0; // 注意这个和filter的区别，他只返回一个值
});

console.log(NewArr);
```

![[00 assets/553ddea6442256c2e2a7cdcafae84c63_MD5.jpeg]]

### 5.2.5 reduce

```javascript
const nums = [2, 3, 4, 5, 6, 7, 8];

/*
  第一个参数:前一个参数,开始遍历数组的时候，默认值为0,这个可以设置preValue初始值
  第二个参数:当前参数
  第三个参数:当前参数的索引
  第四个参数:当前遍历的数组
*/
const result = nums.reduce(function (preValue, curValue, curIndex, arr) {
  return preValue + curValue;
}, 0);

console.log(result);
```

# 6. 闭包

## 6.1 基本介绍

下面都是官方的解释

![[00 assets/0da9026ed08dac479d285872d5a63e47_MD5.png]]

我们来分析下面这段代码中执行的情况

```javascript
function foo() {
    function boo() {
        console.log("张三")
    }

    return boo
}

var fn = foo()
fn()
```

当`var fn = foo()`执行完毕，但是`fn()`还没执行的内存地址图。到这里的分析可以查看`3 函数执行`里面的笔记

![[00 assets/3be2faf752500f849884e0f1dead9cd0_MD5.png]]

当执行到`fn()`的时候的内存图

![[00 assets/8f6b17c5d7282d2948d7432355b33913_MD5.png]]

我们再来看`闭包`的内存执行情况，可以参考下面的代码，这个是最典型的闭包

```javascript
function foo() {
  var msg = "foo" // 这里加上msg

  function boo() {
    console.log(msg);
  }

  return boo;
}

var fn = foo();
fn();
```

![[00 assets/f55e96b7d46df8f0b8e7c49584304f9a_MD5.png]]

因为`boo`的`scope`指向的是`foo`，所以该`foo`不会被销毁。而是继续保留，在寻找作用域链的时候会跟着向上寻找，知道找到`GO`为止

![[00 assets/57a5a1f5bb856a2b5fb02fb014bcb3d9_MD5.png]]

假如你走了上面的流程，你会发现当你执行了`foo()`之后返回的是`boo`的内存地址。但是`foo`已经执行完毕了，所以`foo`的`FEC`和`AO`就会被销毁掉。但是按照上面的执行情况来说，他没有销毁，并且可以正常访问。所以这个叫做**闭包**

我们再来看上面的概念，可以得出闭包是两部分组成的：`函数` + `函数外部访问的自由变量`

![[00 assets/15894ead7e0e36041ce7492c6a796abc_MD5.png]]

首先来一段 JS 函数

```javascript
var message = "Hello World!"

function foo() {
	var name = "张三"
    var age = 18
}

function test() {
    console.log("test")
}

foo()
test()
```

下面就是整体的一个执行情况。

1.在程序加载的时候会优先创建`GO对象`，在里面会包含`Date、String...`，解析到`message...`数据会赋值为`undefined`

2.然后会执行代码，这个时候就会将值给`message`，为`Hello World!`

3.当遇到`function foo(){...}`的时候会创建`foo`，然后会解析里面的`函数体`，并且会在堆里面创建`foo函数对象`，里面会包含`父作用域`和`函数执行体`。并且这里的细节就是`父作用域`是以地址的形式来指向父作用域的`AO`

4.然后执行到`foo()`的时候会创建`函数执行上下文`，里面会包含该函数的`AO`，但是在`堆`中创建该`AO`对象

5.当函数执行完毕之后就会注销掉`函数执行上下文`，这个时候`0x200`的引用会被删掉。当所有的引用都没有的话，就基本等于被删除了

![[00 assets/ed04b4fa1b49b46af231bb7236ddf8a2_MD5.jpeg]]

假如上面的函数执行完毕之后，我们再来看下面的执行情况

```javascript
function fn() {
  let name = "张三";
  let age = 18;

  function bo() {
    console.log(name);
    console.log(age);
  }

  return bo;
}

var to = fn();
to();
```

我们再来看下面的内存地址图，当执行到`var to = fn()`，这个时候`fn()`已经算执行完毕了，所以`foo的函数执行上下文`就会消失，所以对`foo的AO对象`的引用也会消失。

按照没有引用就消失得原则，所以`AO`也会消失。但是`foo`的`AO`不会消失，因为还有`bar`函数对象引用它

![[00 assets/f6f6f3ec4112ac8f9d919a469966861b_MD5.png]]

当执行到`to()`得时候，因为返回值给了`fn`，所以`bar`函数对象也不会消失。函数执行上下文也换成了`bar`，当在该`AO`对象找不到得时候，就会通过作用域链去上级作用域来寻找，`bar`函数对象得上级作用域是`foo得AO`对象

这里就可以扩展一下，因为我们在`bar`中可以找到上级作用域，所以通过该方式还可以向上寻找，最后找到`GO`中

![[00 assets/76e2acd54deded9a6502f382120919c6_MD5.png]]

## 6.2 内存泄漏

我们可以看上面的函数执行的情况，内存泄漏就是该消除的函数执行没有被清理

下面的变量`to`一直指向着`bo`，所以`bo`不能被销毁，`bo`指向着`fn`，所以`fn`也不能被销毁掉。所以就会一直被保存，这个就是**内存泄漏**

```javascript
function fn() {
  var name = "张三";
  var age = 18;

  function bo() {
    console.log(name);
    console.log(age);
  }

  return bo;
}

var to = fn();
to();
```

我们使用下面的方式就可以避免内存泄漏，手动设置为`null`，依靠垃圾回收机制来处理

```javascript
function fn() {
  var name = "张三";
  var age = 18;

  function bo() {
    console.log(name);
    console.log(age);
  }

  return bo;
}

var to = fn();
to();

to = null; // to和fn置空，将引用销毁
fn = null;
```

## 6.3 内存泄漏分析

下面就是一个内存泄漏的案例。我们创建了一个`4 * 1023 * 1023`即`400MB`的内存空间，并且使用闭包来引用了该地址，所以该内存不会被释放

```javascript
function fn() {
  var arr = new Array(1024 * 1024).fill(1);

  return function () {
    console.log(arr.length);
  };
}

let fuArr = [];
for (let i = 0; i <= 100; i++) {
  fuArr.push(fn());
}
```

我们来通过浏览器来调试，因为浏览器本身自己需要加载一些服务，所以会占用`400mb`的内存地址。当过了一会之后，内存会一直增加，直到达到`800mb`才会停止，这一段增加的就是内存泄漏的

![[00 assets/af9dfdebbcca03615d2eb3e737acef43_MD5.png]]

当我们去释放内存的话

```javascript
function fn() {
  var arr = new Array(1024 * 1024).fill(1);

  return function () {
    console.log(arr.length);
  };
}

let fuArr = [];
for (let i = 0; i <= 100; i++) {
  fuArr.push(fn());
}

setTimeout(() => {
  fuArr = null;
}, 2000);
```

先是内存上升到`400mb`，当定时到了之后就会赋值为`null`，并且将内存释放。是有等到一定的时间之后才会进行回收的操作，所以看不到结果的时候可以多进行几次操作

![[00 assets/95403547dcb6b6b7f1c0722018ed4eed_MD5.png]]

## 6.3 自由变量销毁

下面执行的代码中的内存地址已经分析了很多次，可以发现`age`已经加载到了`AO`中，但是没有调用

```javascript
function fn() {
  var name = "张三";
  var age = "18";

  function bar() {
    debugger // 设置断点
    console.log(name);
  }

  return bar;
}

var foo = fn();
foo();
```

这个在`ECMA规范`中是不会被销毁的，但是在`V8引擎`中是会被销毁的，可以看到浏览器调试的结果，可以看到只有`name`，`age`已经被销毁了

![[00 assets/5d2df6fbcc9c26b5b15716d85920b684_MD5.jpeg]]

## 6.5 闭包陷阱

参考`React`中`useCallBack`的笔记

# 7. this

## 7.1 基本介绍

在`JS`的日常开发我们在函数内部直接使用`对象名`也可以直接获取到该对象里面的`属性值`

![[00 assets/ffc507b4785c2ef82aef20660d6c970f_MD5.png]]

但是我们为什么需要使用`this`?假如按照上面的来做，假如`对象名person`修改的话，下面的所有的引用都需要修改，这就造成了开发的不便，所以需要使用到`this`

![[00 assets/2d364ccbee061f656880f282cd5dae66_MD5.png]]

✨ 对于`Node.js`直接在全局执行`this`，会打印出`{ }`。其实`Node.js`将每个文件当作是一个`模块`，编译解析，然后`Node.js`将代码放在一个函数里面，并且该函数最后会使用`apply`强行让全局指向为`{ }`

## 7.2 this 指向

**其实 this 的指向和它所处在的位置没有任何关系，只和那个调用的有关系**

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032312245.png" alt="image-20221006194936587" style="zoom: 67%;" />

### 7.2.1 默认绑定

通过下面的 5 个案例，可以发现结果都是`window`，因为都是直接调用

```javascript
// 案例一
function fn() {
  console.log(this);
}
fn();


// 案例二
function fn1() {
  console.log(this);
}
function fn2() {
  fn1();
  console.log(this);
}
function fn3() {
  fn2();
  console.log(this);
}
fn3();


// 案例三
let obj = {
  name: "张三",
  fn: function () {
    console.log(this);
  },
};
let objfn = obj.fn;
objfn();


// 案例四
function fn() {
  console.log(this);
}
let obj1 = {
  name: "张三",
  fn,
};
let obj1fn = obj.fn;
obj1fn();


// 案例五
function foo() {
  return function () {
    console.log(this);
  };
}
let obj2fn = foo();
obj2fn();
```

![[00 assets/c626294fc2ab3f053e515d12a9de8d77_MD5.png]]

### 7.2.2 隐式绑定

该方式就是通过`对象名.方法名`来调用，最后的结果`this指向`就是该`对象`

```javascript
// 案例一
function foo() {
  console.log(this);
}

let obj = {
  name: "张三",
  foo,
};

obj.foo();

// 案例二
let obj1 = {
  name: "李四",
  eating() {
    console.log(this);
  },
};
obj1.eating();

// 案例三
let obj2 = {
  name: "王五",
  foo() {
    console.log(this);
  },
};
let obj3 = {
  name: "赵六",
  bar: obj2.foo,
};
obj3.bar();

```

![[00 assets/59a67a3529f5bb512748111e3259eda7_MD5.png]]

### 7.2.3 显式绑定

![[00 assets/d26e76ae4d5645d872cf3da2e354b80a_MD5.jpeg]]

> call/apply

这 2 个方法最大的作用就是指定`this`的绑定

```javascript
function fn() {
  console.log(this);
}

let obj = {
  name: "张三",
};

fn.call(obj);
fn.apply(obj);
fn.apply("abc");
```

![[00 assets/8ecc01bf2cf8a6399f1d2c74b1744bdb_MD5.png]]

但是`call`和`apply`的最大的区别就是传递的参数不同

```javascript
function fn(num1, num2) {
  console.log(this);
}

let obj = {
  name: "张三",
};

fn.call(obj, 1, 2);
fn.apply(obj, [1, 2]);
fn.apply("abc");
```

> bind

为了避免上面的形式函数多次调用，所以就有下面的方式

```javascript
function fn(num1, num2) {
  console.log(this);
}

let obj = {
  name: "张三",
};

let BindFn = fn.bind(obj); // 绑定之后的返回值直接调用即可
BindFn();
BindFn();
BindFn();
BindFn();

// 使用call/apply
fn.call(obj, 1, 2);
fn.call(obj, 1, 2);
fn.call(obj, 1, 2);
fn.call(obj, 1, 2);
```

![[00 assets/4fa2fecea832193699d3f11c9b0f408c_MD5.png]]

### 7.2.4 new 绑定

我们使用`new绑定`的时候，`this = 创建出来的对象`

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

let p1 = new Person("张三", 18);
console.log(p1.name, p1.age);
```

![[00 assets/0084f7848dda11e5fccfa7f78448b4bb_MD5.jpeg]]

## 7.3 内置函数指向

> setTimeout

下面是`setTimeout`的调用情况。也就是对应的`默认绑定`

```javascript
setTimeout(function () {
  console.log(this);
}, 2000);


// 可以理解为下面的形式
function SystemSetTimeOut(fn, timeout = 0) {
  fn() // 因为直接调用了该函数，所以this的指向就是Window，settimeout也是大致一样的形式
}

SystemSetTimeOut(function () {
  console.log(this);
}, 1000);


// 这里可以参考严格模式 10.3的内容
function SystemSetTimeOut(fn, timeout = 0) {
  fn.apply(window) // 因为开启了严格模式还是指向的window，所以可以猜测使用apply来指向的window
}
```

> 监听点击

下面绑定了一个`DOM对象`，并且给它了一个绑定事件`onclick`。返回的是这个时候指向的是`DOM对象`

```javascript
const divBox = document.querySelector(".box");
divBox.onclick = function () {
  console.log(this);
};


// 可以类比下面的情况
divBox.onclick() //因为是对象的调用，对应的就是隐式绑定
```

![[00 assets/d377db80808ed398a2a40bc969a28346_MD5.jpeg]]

> forEach / map / filter / find

假如直接调用这些高阶函数的时候`this`默认指向的是`Window`。但是一些`API`可以传入一个`thisArg参数`，来动态的指定`this`的指向

```javascript
const arr = [1, 2, 3];

let obj = {
  name: "张三",
  age: 14,
};

arr.forEach(function (ele) {
  console.log(ele, this);
}, obj);
```

![[00 assets/518d3c7f91af2616e3d8107705420b62_MD5.png]]

## 7.4 规则优先级

最后可以得出结论：**new > 显式绑定 > 隐式绑定 > 默认绑定**

## 7.5 this 规则之外

### 7.5.1 忽略显式绑定

假如我们给`apply / call / bind`传入`null / undefined`的话，就会默认绑定到`Window`上

```javascript
function fn() {
  console.log(this);
}

fn.apply(null);
fn.apply(undefined);

var bar = fn.bind(null);
bar()
```

![[00 assets/08b65b4a606cf9b924f92878cf912022_MD5.jpeg]]

### 7.5.2 间接函数引用

我们使用下面的方式也是指向的`window`

```javascript
var obj1 = {
  name: "张三",
  fn() {
    console.log(this);
  },
};

var obj2 = {
  name: "李四",
};

(obj2.bar = obj1.fn)();
```

![[00 assets/13a0d372d7d57ba507d677fcc8a1f3a7_MD5.png]]

但是这里就涉及到了`JavaScript语法规范`了，平常我们写代码的时候是不会主动加上`;`，这是因为`JS引擎`在解析的时候会自动分析语句的结束，然后自动加上`;`

但是按照我上面的实例代码就必须要手动加上`;`，不然会报错

```javascript
var obj1 = {
  name: "张三",
  fn() {
    console.log(this);
  },
};

var obj2 = {
  name: "李四",
}

(obj2.bar = obj1.fn)();


// 上面的代码其实是下面这样的，所以会导致报错
var obj1 = {
  name: "张三",
  fn() {
    console.log(this);
  },
};

var obj2 = {
  name: "李四",
}(obj2.bar = obj1.fn)();
```

![[00 assets/ef3c6e45172c3f6a70f9adfc6a65e8b3_MD5.png]]

在`《你不知道的JavaScript》`中就记录了和上面一样的模式

```javascript
function fn(ele) {
  console.log(ele);
}

let obj = {
  name: "张三",
}

[1, 2, 3].forEach(fn, obj);

// 其实本质和上面是一样
function fn(ele) {
  console.log(ele);
}

let obj = {
  name: "张三",
}[1, 2, 3].forEach(fn, obj);
```

当然这个就是`JavaScript`的语法规则的问题了，在平常书写的时候尽量避免

```javascript
// 解决方法1
// 假如你修正这种情况也很好说，只需要在对象后面加上;
function fn(ele) {
  console.log(ele);
}

let obj = {
  name: "张三",
};

[1, 2, 3].forEach(fn, obj);

// 解决方法2
// 将数组单独写出来也可以
function fn(ele) {
  console.log(ele, this);
}

let obj = {
  name: "张三",
};

let arr = [1, 2, 3]
arr.forEach(fn, obj);
```

## 7.6 箭头函数

### 7.6.1 基本介绍

可以参考我`ES6~ES11`的笔记

假如我们知道了箭头函数的写法，我们就可以简写下面的操作了

```javascript
// 筛选出数组中的偶数，乘100，再相加

let arr = [2, 3, 4, 5, 6, 7];

let sum = arr
  .filter((item) => item % 2 === 0)
  .map((item) => item * 10)
  .reduce((preValue, curValue) => preValue + curValue);

console.log(sum);
```

![[00 assets/6f25f452e3bb2b4c922b7af498d4e7c1_MD5.png]]

假如我们又想简写又想返回对象呢？我们按照下面的方式来写的话，`JS引擎`就区分不了对象的`{ }`的方法的`{}`，所以就会导致报错

![[00 assets/807f10b25109ce33140140080ae5eee4_MD5.png]]

假如我们要返回对象的话，只能将这个对象当作一个整体来处理

![[00 assets/57bccaf31a39d78d3fab672eb5ef939c_MD5.png]]

箭头函数的`this`默认是按照上层作用域来查找的

这里举例来说：**定时器**，在使用的时候肯定是想要使用对象里面的数据的，但是我们在使用`传统function`的时候会默认绑定到`Window`（这里参考`7.3 内置函数指向`）假如我们需要绑定到该对象的话，有 2 种方式

```javascript
// 解决方法1
// 在内置函数外部写一个let _this = this
var obj = {
  name: "张三",
  fn() {
    let _this = this;
    setTimeout(function () {
      console.log(_this);
    }, 1000);
  },
};

obj.fn();


// 解决方法2
// 使用箭头函数，因为箭头函数默认使用上层作用域来查找，即便你使用了显式绑定也不会改变它的指向
var obj = {
  name: "张三",
  fn() {
    setTimeout(() => {
      console.log(this);
    }, 1000);
  },
};

obj.fn();
```

### 7.6.2 面试题

```javascript
var name = "window";

var person = {
  name: "person",
  fn() {
    console.log(this.name);
  },
};

function sayName() {
  var sss = person.fn;
  sss(); // window,默认绑定
  person.fn(); // person,隐式绑定
  // person,本质和上面的person.fn()是一样的，而下面是进行了赋值的操作，最后执行的是b()
  (person.fn)();
  (b = person.fn)(); // window,这个是独立函数调用
}

sayName();
```

面试题：[前端面试之彻底搞懂 this 指向 (qq.com)](https://mp.weixin.qq.com/s/hYm0JgBI25grNG_2sCRlTA)

## 7.8 实现显式绑定

下面是通过`JS`来实现`call/apply/bind`方法

```javascript
function CallOrApplyOrBind() {}

// call方法
Function.prototype.call = function (thisArg, ...args) {
  // 因为使用的fn.call()来调用的该函数，为隐式绑定，所以this就是fn
  var fn = this;
  /*
    1.Object()可以将number、String...类型转换为Object类型
    2.当传入的是null、undefined的时候返回的是window
  */
  thisArg =
    thisArg !== null || thisArg !== undefined ? Object(thisArg) : window;

  // 给传入的对象中加入this的函数，即fn
  thisArg.fn = fn;
  // 执行该函数，并且传入参数
  var result = thisArg.fn(...args);
  delete thisArg.fn;

  return result;
};

// apply方法
Function.prototype.apply = function (thisArg, args = []) {
  // 和call的区别在于传递的是[]
  var fn = this;

  thisArg =
    thisArg !== null || thisArg !== undefined ? Object(thisArg) : window;

  thisArg.fn = fn;
  var result = thisArg.fn(...args);
  delete thisArg.fn;

  return result;
};

// bind方法
Function.prototype.bind = function (thisArg, ...args) {
  var fn = this;
  thisArg =
    thisArg !== null || thisArg !== undefined ? Object(thisArg) : window;

  return function (...ParmBindArgs) {
    thisArg.fn = fn;
    var result = thisArg.fn(...args, ...ParmBindArgs);
    delete thisArg.fn;

    return result;
  };
};


// 下面为实现的案例
let obj = {
  name: "张三",
};
function fn(a, b, c, d) {
  console.log(this, a, b, c, d);
}
fn.call("123", 1, 2, 3, 4);
fn.apply(obj, [1, 2, 3, 4]);

let result = fn.bind(obj, 1, 2);
result(3, 4);
```

![[00 assets/8309271d1cebd12ce1e8c244c45cabe9_MD5.png]]

## 7.9 arguments

![[00 assets/f03a95d452d55f117b99f0aa51bcbaf2_MD5.png]]

下面为使用`arguments`，在箭头函数中不能使用`arguments`

![[00 assets/5c25ea896e75e61bcf752b7c573003e0_MD5.png]]

因为`argument`中很多的方法都不存在，所以我们需要将`argument`转化为数组来处理

```javascript
function fn() {
  // 方法一
  var newArr = [];
  for (let i = 0; i < arguments.length; i++) {
    newArr.push(arguments[i]);
  }

  // 方法二
  var newArr1 = Array.prototype.slice.call(arguments);

  // 方法三
  var newArr2 = [].slice.call(arguments);

  // 方法四
  var newArr3 = Array.from(arguments);

  // 方法五
  var newArr4 = [...arguments];
}

fn(1, 2, 3, 4, 5);
```

![[00 assets/13a1e587db9c8e6a23af60561d72ed4a_MD5.png]]

# 8. 函数式编程

## 8.1 纯函数

### 8.1.1 基本介绍

![[00 assets/dda1757ed3c62fae873b9fbe689b1d9f_MD5.png]]

### 8.1.2 副作用

![[00 assets/452111517c2a8c58ca1e8ba6ae2dce34_MD5.png]]

### 8.1.3 案例演示

其实就是对应的上面的概念。

`确定的输入可以得到确定的输出`，下面输入确定的`start和end`就可以获取获取到确定的数组。

`不产生副作用`，对外面的数组`arr`不做修改。这个就是纯函数的概念

![[00 assets/ba850aa544fcaa4551006359e3848079_MD5.png]]

下面就是一种纯函数的处理方式，本质就是一种处理的思想。

![[00 assets/1bbeeb2cad2e2beed44606ef1503e981_MD5.png]]

### 8.1.4 纯函数优势

![[00 assets/d655a7aa22302819c32cb66e5d84401d_MD5.png]]

## 8.2 柯里化

### 8.2.1 基本介绍

![[00 assets/eda146b7ea427a17d105a5ef8655a006_MD5.png]]

### 8.2.2 案例演示

下面就是`传递一部分参数来调用它，让它返回一个函数来处理剩余的参数`，就叫做**柯里化**。而这个函数并不叫`柯里化函数`。下面的柯里化过程只有在特定的场景会使用到

```javascript
// 正常函数编程
function fn(a, b, c) {
  return a + b + c;
}

// 柯里化过程
function fn1(a) {
  return function (b) {
    return function (c) {
      return a + b + c;
    };
  };
}

// 柯里化过程简写
var fn2 = (a) => (b) => (c) => a + b + c;

console.log(fn(1, 2, 3), fn1(1)(2)(3), fn2(1)(2)(3));
```

![[00 assets/7d4457c0f64fba3c82cd0d944ecddb48_MD5.png]]

### 8.2.3 柯里化优势

![[00 assets/9d2c128f24cd06a514487834bc9484e5_MD5.jpeg]]

> 函数单一职责

即一个函数只处理一部分，如`a += 2`可以想象实际中就包含了`10+`的代码逻辑，后面也是一样的。这样就做到了`函数单一职责`，同时也做到了逻辑的复用

![[00 assets/83a883f1e372e25c22c01ceddd650649_MD5.png]]

> 逻辑复用

![[00 assets/00bff75a32bdf432cac9f773bf41f44a_MD5.png]]

> 逻辑复用 2

![[00 assets/4510f5d5db8c96cfd2b0ea4d7104d5d6_MD5.jpeg]]

### 8.2.4 柯里化实现

下面就是柯里化的实现，只要将函数传递进去就可以将输出的函数柯里化

```javascript
function curry(fn) {
  let curried = function (...args) {
    if (args.length >= fn.length) {
      return fn.call(this, ...args);
    } else {
      let curriedNotFinsh = function (...RemainArgs) {
        return curried.call(this, ...args, ...RemainArgs);
      };
      return curriedNotFinsh;
    }
  };
  return curried;
}

function sum(num1, num2, num3, num4) {
  return num1 + num2 + num3 + num4;
}
let result = curry(sum);
console.log(result(1)(2)(3)(4));
```

![[00 assets/53d51b8371923421d1a3b4f1884d8d30_MD5.png]]

下面为柯里化实现函数的解释

![[00 assets/c2d0ebfe1a4bcd2044b69f67be142502_MD5.png]]

✨ 注意：需要注意一个点，假如要获取传递给函数参数的个数，可以使用`fn.length`的方式来获取

其中比较难理解的就是递归的部分，这里可以参考阶乘的递归处理。

![[00 assets/4a044db7bcbcca0ff6b46f1fcd080154_MD5.png]]

还有一个迷惑的点就是`result1`的返回值的问题，明明返回的是`curried.call...`，为什么可以在该函数中调用到`curried`。这里是因为闭包的处理，所有可以访问到，遵循着作用域链来查找

![[00 assets/16dbc02e0b34793891967b4d7460b862_MD5.png]]

## 8.3 组合函数

下面就是组合函数的传统的处理方式

```javascript
function fn(a) {
  return a * 2;
}
function fn1(a) {
  return a ** 2;
}

function composeFn(m,n){
   return function(count) {
      return n(m(count))
   }
}

composeFn(fn,fn1)
```

**下面就是组合函数的实现过程，可以依次执行传入的函数。**

这个其实不需要使用递归来处理我们只需要将上一个函数返回的数据传递给下一个函数就可以了

```javascript
function fn(a) {
  return a * 2;
}
function fn1(a) {
  return a ** 2;
}

function composeFn(...fns) {
  var length = fns.length;
  for (let i = 0; i < length; i++) {
    if (typeof fns[i] !== "function") {
      throw new TypeError("传入参数错误");
    }
  }

  let compose = function (...args) {
    let index = 0;
    let result = length ? fns[index].apply(this, args) : null;
    while (++index < length) {
      result = fns[index].call(this, result);
    }
    return result;
  };
  return compose;
}


let result = composeFn(fn, fn1);
console.log(result(2));
```

![[00 assets/26e2f998f3488dc58a40852549518847_MD5.png]]

# 9. with/eval

## 9.1 with

`with`相当于多加一层作用域来访问设定好的对象中的值。但是现在不建议来使用了，因为在`js`的严格模式中已经取消它了

![[00 assets/a8e0afd2aeb29ec4276f7963b5af754d_MD5.png]]

## 9.2 eval

可以传入字符串来执行函数

![[00 assets/b71d095065cc96ff9aa9e56eac25aa1f_MD5.png]]

现在已经不推荐使用了

![[00 assets/9ed01a9542afeb1f775fdfa5cde03041_MD5.png]]

# 10. 严格模式

## 10.1 基本介绍

![[00 assets/ef126d1a2a71b8787c1dc1a870d42569_MD5.png]]

下面 2 个是明显的错误，但是在浏览器是`静默错误`，即浏览器知道是错误的，但是不会执行

![[00 assets/91c34f2575586c418d80560e019db181_MD5.png]]

假如开启了严格模式的话，这些以前不会报错的代码，就会报错

![[00 assets/9e0c1dc8c34aba890f28daf75936e9c2_MD5.png]]

## 10.2 开启严格模式

> 全局开启

![[00 assets/b98b59a5e59181c6656b0ae46d5e274d_MD5.png]]

> 函数开启

![[00 assets/bec4c9a2fd2df7a5f676bb9c4a5e437c_MD5.png]]

## 10.3 严格模式限制

![[00 assets/408390dc48782157f03fd9b28854077c_MD5.png]]

> 1.无法意外的创建全局变量

其中`message`和`age`都会自动抬升为全局变量

![[00 assets/7c12e9bf824db4b5a5520a3e9bbd4f46_MD5.png]]

> 2.不允许函数有相同的参数

![[00 assets/158ef32d3ad183389e80f3bda94b6661_MD5.png]]

> 3.静默错误

![[00 assets/7f70b322dd8c9e7144046bc9fd00b160_MD5.png]]

> 4.不允许八进制

![[00 assets/bcb87be4073e37d6469ad680d79a0f46_MD5.png]]

> 5.with 语句不允许使用

> 6.eval 函数不会向上引用变量

> 7.this 的指向

自执行函数会指向为`undefined`，原本的自指向函数都是指向`Window`

![[00 assets/5d25c929fddc8d435ea744570b50722c_MD5.jpeg]]

同时这个就引出了`setTimeOut`的指向问题，在以前的`this`学习的时候说的`setTimeout`是直接执行，所以按照道理应该是`window`，但是实际情况并不是。所以可以猜测`setTimeout`使用的`apply`来改变指向

![[00 assets/952ee3aaf9889e5b721be43189a9fb47_MD5.png]]

# 11. 面向对象

## 11.1 基本介绍

![[00 assets/f65305dab79489622d226108b610aa60_MD5.png]]

> JavaScript 中的面向对象

![[00 assets/6729ee87f794d79be61771b0c20e8b45_MD5.png]]

下面为`new Object()`和`{ }`创建的方式，其中`{ }字面量`创建是`new Object`的语法糖

![[00 assets/9810ae9dd75da7e795129b72c9b820bb_MD5.png]]

> 获取/修改/删除

![[00 assets/e3cb93d6ce340566d6087555c172be34_MD5.jpeg]]

## 11.2 属性描述符

### 11.2.1 基本使用

下面为属性描述符的基本使用，这个可以在为对象添加属性的时候附加一些特殊的功能

使用`defineProperty`添加的属性是不可枚举的。你可以发现已经使用了`defineProperty`添加了`height`属性。但是在遍历`obj`的时候看不到，要获取只能`对象.属性值`。因为里面的`enumerable`默认被设置为`false`

![[00 assets/64676d88601b300018e5bf19cf985243_MD5.png]]

### 11.2.2 描述符分类

![[00 assets/627a583f25bffd2318c5483167207e76_MD5.png]]

#### 11.2.2.1 数据描述符

![[00 assets/e2802cfd00667bab708d457341a9ab45_MD5.png]]

下面就是

```javascript
// 假如是这种形式定义的configurable，enumerable，writable的默认值都为true
var obj = {
  name: "张三",
  age: 18,
};


// 也可以使用属性描述符来处理
// 1. obj 处理的对象
// 2. prop 要定义或修改的属性名
// 3. desc 要定义或修改的属性描述符
// 4. 被传递给函数的对象，这个不是一个纯函数
Object.defineProperty(obj, "height", {
  configurable: true, // 该属性是否为可配置(删除)，默认值为false
  enumerable: true, // 该属性是否可以被枚举，默认值为false
  writable: true, // 该属性是否可以修改，默认值为false
  value: 1.3, // 默认值为undefined
});


// 测试 configurable
delete obj.height
console.log(obj, obj.height);
// 测试 enumerable
console.log(obj, Object.keys(obj));
// 测试 writable
obj.height = 1.6
console.log(obj, obj.height)
```

![[00 assets/7a4e6f612fceb73edcdff6a79248530d_MD5.png]]

假如你在`defineProperty`中什么都不写的话，默认值为`false`，`value`的默认值为`undefined`

![[00 assets/462ff1192c823e3ee8dc28b6c2cf4670_MD5.png]]

#### 11.2.2.2 存取描述符

如果要看其他的记录可以参考`Vue`

因为里面的`get`就替代`数据描述符`了`value`，因为`get`本身就是获取属性。其中`set`就代替了`writeable`，因为`set`就是修改数据。

一般情况是将存取描述符设置为非`_`的形式，因为在实际的操作中都会去遵循`obj.name`的形式，而不去操作`obj._name`，而对象中定义的原始属性设置为`_name`

```javascript
var obj = {
  _name: "张三",
  age: 18,
};

Object.defineProperty(obj, "name", {
  enumerable: true,
  configurable: true,
  get: function () {
    return this._name;
  },
  set: function (value) {
    console.log("name被修改了");
    this._name = value;
  },
});

obj.name = "李四"; // 如果需要修改的话要使用_name来修改，这样就可以执行里面的操作
console.log(obj.name);
```

![[00 assets/af68f53ac84bd66376fda3c0cd0367fa_MD5.jpeg]]

当然我们也可以不去写`defineProperty`的方法来定义，我们可以直接在对象里面定义`set`和`get`

```javascript
Object.defineProperty(obj, "name", {
  enumerable: true,
  configurable: true,
  get: function () {
    return this._name;
  },
  set: function (value) {
    console.log("name被修改了");
    this._name = value;
  },
});

// 上下2种定义方式是一样的效果，使用下面的方式enumerable和configurable默认为true

var obj = {
  _name: "张三",
  get name() {
    return this._name;
  },
  set name(value) {
    this._name = value;
  },
};

obj.name = "李四"
```

### 11.2.3 定义多个

```javascript
var obj = {
  _age: 18, // 私有属性，这个只是社区中的规定，而不是真的定义为私有属性
  _height: 1.8,
  set height(value) {
    this._height = value;
  },
  get height() {
    return this._height;
  },
};

// 定义多个属性
Object.defineProperties(obj, {
  name: {
    enumerable: true,
    writable: true,
    configurable: true,
    value: "李四",
  },
  age: {
    enumerable: true,
    configurable: true,
    get: function () {
      return this._age;
    },
    set: function (value) {
      this._age = value;
    },
  },
});

obj.age = 18;
obj.height = 1.70
console.log(obj);
```

![[00 assets/fe448a2f6b6912a1f9fcdf3be03e7dc3_MD5.png]]

### 11.2.4 属性方法

```javascript
var obj = {
  name: "张三",
  age: 18,
};

Object.defineProperty(obj, "height", {
  configurable: true,
  enumerable: true
  writable: true,
  value: 1.3,
});

console.log(Object.getOwnPropertyDescriptor(obj, "height")); // 获取对象中单个属性值得属性
console.log(Object.getOwnPropertyDescriptors(obj)); // 获取对象中所有属性值得属性

Object.preventExtensions(obj); // 禁止对象继续添加属性
Object.seal(obj); // 禁止对象配置/删除
Object.freeze(obj); // 禁止对象不可修改
```

![[00 assets/57fa31d7daf77ab45bcf66d101d53dad_MD5.png]]

## 11.3 创建多个对象

假如需要创建多个相似对象得时候，能想到得传统方法就是写多个变量

![[00 assets/9fb46370b9946a16b9c3f24c0638ec26_MD5.png]]

### 11.3.1 工厂模式

```javascript
function createPerson(name, age, height, address) {
  return {
    name,
    age,
    height,
    address,
    eating() {
      console.log("正在吃饭");
    },
    running() {
      console.log("正在跑步");
    },
  };
}

var p1 = createPerson("张三", 18, 1.44, "北京市");
var p2 = createPerson("李四", 20, 1.54, "湖北省");

console.log(p1, p2);
```

![[00 assets/0e3461982437dc16978cef6bb8e545b7_MD5.png]]

但是这个工厂模式并不是很好得处理方式，因为无法区分是那个类。看下图就可以发现，是不是创建出来得对象不一样显示得前缀不一样

![[00 assets/ae488fee5626604ae4346cb8851e620e_MD5.png]]

### 11.3.2 构造函数

![[00 assets/0faba8976ac088465aaf401290f672d2_MD5.png]]

下面就是构造函数得模式，比工厂模式更好

```javascript
function Person(name, age, height, address) {
  this.name = name;
  this.age = age;
  this.height = height;
  this.address = address;
  this.eating = function () {
    console.log("正在吃饭");
  };
  this.running = function () {
    console.log("正在跑步");
  };
}

var p3 = new Person("张三", 18, 1.44, "北京市");
var p4 = new Person("李四", 20, 1.54, "湖北省");
```

![[00 assets/d33c2fc59a46edb28f78a3863420076a_MD5.png]]

但是构造函数还是有一个缺点：**当你创建了一个对象，里面的函数都是重新创建的，并且放置在内存中。**

这个相对来说比较浪费性能，所以对于这种效果基本一样的函数，我们可以放置在原型中

![[00 assets/407922f52c34d3742ece78ef2809a7e0_MD5.png]]

## 11.4 原型

### 11.4.1 基本介绍

每一个对象都存在一个原型属性，即`__proto__`。每个函数都存在一个`prototype`

![[00 assets/4a0aa8448c95453e301c0672bad4432d_MD5.png]]

### 11.4.2 隐式原型

```javascript
let obj = { name: "张三" };
obj.__proto__.age = 18; // 为对象添加原型属性
console.log(obj.age) // 现在对象中查找，随后向原型中查找

console.log(obj.__proto__); // 浏览器提供的隐式原型
console.log(Object.getPrototypeOf(obj)); // ES5之后提供的方法
```

![[00 assets/f16fc26744ed5bd5686301d9145b5e6f_MD5.png]]

### 11.4.3 显式原型

#### 11.4.3.1 基本介绍

因为函数本身就是一个对象，所以函数作为一个对象还具有一个`prototype`的显式原型

```javascript
// 1. 创建函数
function Person(name, age, height, address) {
  this.name = name;
  this.age = age;
  this.height = height;
  this.address = address;
  this.running = function () {
    console.log("正在跑步");
  };
}

// 2. 为函数的显式原型添加eating方法
Person.prototype.eating = function () {
  console.log(`${this.name},正在吃饭`);
};

// 3. 查看函数中的原型属性
console.log(Person.__proto__); // 浏览器提供
console.log(Object.getPrototypeOf(Person)); // ES5之后提供的方法

// 4. 创建对象
let p1 = new Person("张三", 12, 1.55, "北京市");
// 先在对象中查找，如果没有的话就会沿着__proto__在函数原型中查找
p1.eating();

// 5. 在创建对象的时候会默认将函数的显式原型给p1
console.log(p1.__proto__ === Person.prototype); // true


// 6. 根据内存图可以来改function的prototype
p1.__proto__.eating = function () {
  console.log(`${this.name},正在吃饭,修改后~`);
};
```

下面为对象的`__proto__`和函数对象中的`prototype`的内存关系

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032312538.png" alt="image-20221012180837715" style="zoom:67%;" />

#### 11.4.3.2 constructor

其中函数对象中都含有一个`constructor`属性，我们看到不到它是因为`constructor`的`enumerable`为`false`。其中`constructor`指向的是函数自己

```javascript
function Person(name, age, height, address) {
  this.name = name;
  this.age = age;
  this.height = height;
  this.address = address;
  this.running = function () {
    console.log("正在跑步");
  };
}
Person.prototype.eating = function () {
  console.log(`${this.name},正在吃饭`);
};

// 1. Person.prototype.constructor 指向构造函数本身 [function Person]
console.log(Person.prototype.constructor);

// 2. 查看该函数的原型中的属性，可以发现 constructor 的 enumerable 为 false
console.log(Object.getOwnPropertyDescriptors(Person.prototype));
```

![[00 assets/56dbc856a5f577ee030d3201dc9255a8_MD5.png]]

#### 11.4.3.3 批量修改原型属性

```javascript
function Person(name, age, height, address) {
  this.name = name;
  this.age = age;
  this.height = height;
  this.address = address;
  this.running = function () {
    console.log("正在跑步");
  };
}

// 1. 单独为原型添加属性
Person.prototype.name = "张三";
Person.prototype.age = 18;
Person.prototype.height = 1.44;
Person.prototype.eating = function () {
  console.log(`${this.name},正在吃饭`);
};


// 2. 批量添加原型属性，但是里面的constructor会丢失
Person.prototype = {
  name: "张三",
  age: 18,
  height: 1.44,
  eating() {
    console.log(`${this.name},正在吃饭`);
  },
};
// 为 Person 添加 constructor属性
Object.defineProperty(Person.prototype, "constructor", {
  enumerable: false,
  configurable: true,
  writable: true,
  value: Person,
});
console.log(Person.prototype.constructor);
```

![[00 assets/0adccd71bc736296af24976660eeaa14_MD5.png]]

#### 11.4.3.3 函数添加原型

下面的方式就是为函数添加原型的属性，每个用该函数创建的对象都可以获取到该原型属性

![[00 assets/793609ffa54b5da3df41e217fb7ccd08_MD5.png]]

### 11.4.4 原型链

#### 11.4.4.1 基本介绍

![[00 assets/1040f252062cbbf254e977a543d46802_MD5.png]]

其实这里就解释了上面的一个误区，访问的时候是访问`__proto__`，然后沿着原型链向上寻找

而不是先访问`__prtot__`，然后就去寻找`prototype`。这个是需要区分`Object`构建和`函数`构建的区别

```javascript
var obj = {
  name: "张三",
  age: 18,
};

obj.__proto__ = {};

obj.__proto__.__proto__ = {};

obj.__proto__.__proto__.__proto__ = {
  address: "湖北省",
};

console.log(obj.address);
```

![[00 assets/1388dc32d5d47f86c09ccfc58cad6947_MD5.png]]

#### 11.4.4.2 区分构造器和对象构建

这个时候就需要区分`函数`创建和`Object`创建的区别了，其实最主要的区别就是内部创建的对象中的`__proto__`指向的是哪里

> 函数构建

![[00 assets/eb609ac96079296efe43e33b0259d3e9_MD5.png]]

> 对象构建

```javascript
1.var text = { }

2.text.__proto__ = Object.prototype //就是这里的区别

3.this = text

// ============================= //
var obj = new Object()

// 所以obj.__proto__ = Object.prototype
// 其中Object.prototype就是顶层的原型
```

#### 11.4.4.3 Object 的 prototype

![[00 assets/610e5d1dbeb48a8ab37eba003dd917af_MD5.png]]

我们首先来看下`Object`函数的原型中具有那些属性

```javascript
console.log(Object.getOwnPropertyDescriptors(Object.prototype));
```

![[00 assets/eda2c02e1d4c304da5b5a80b5fa2f0ed_MD5.png]]

其实`Object`本质也是一个函数，所以可以使用`new Object()`来创建对象。

![[00 assets/ad83adbde7e2f9555530b8731b2a2ed6_MD5.png]]

`Object`作为顶层的原型，其他的对象都会沿着`__proto__`向上查找，但是`Object`的原型对象中的`__proto__`为`null`，所以就不会向上寻找了

![[00 assets/a28515f5d6ebafaac3c949a4b9b1a7a2_MD5.png]]

这个为整个原型链的流程图。对象首先会从`obj`来寻找，然后再来沿着`__proto__`来寻找下面的对象，直到找到`Object`的原型的`__proto__`就会结束。

其实本质就可以理解为一个名叫`Object`的函数，里面的原型包含了很多的方法，使用方法和平常使用构造器是一样的

![[00 assets/ef95e615b6c3e192099840520a9f2ac1_MD5.png]]

#### 11.4.4.4 构造器的 prototype

其中`Person`的`prototype`的`__proto__`的也是指向着`Object`，所以这个就是继承的`Object`

![[00 assets/16f66ce03e4229165a8b45e9fe2ac8e2_MD5.png]]

### 11.4.5 方法补充

![[00 assets/251bbcb6b4a349921ac4ef2a2eed173b_MD5.png]]

```javascript
var obj = {
  name: "张三",
  age: 18,
};

// 1. Object.create() 其实可以往里面传递参数
var info = Object.create(obj, {
  hobby: {
    value: "北京市",
    enumerable: true,
  },
});
console.log(info); // 可以看到被传递的参数

// 2. 查看自己拥有的属性
console.log(info.hasOwnProperty("name"));
console.log(info.hasOwnProperty("hobby"));

// 3. 查看自己和原型上面的属性
console.log("name" in info);
console.log("hobby" in info);
```

![[00 assets/73262c825ef3b4fbd0281fbc953e2d13_MD5.png]]

![[00 assets/4bccbd072dccd0f606211b86580de6e1_MD5.png]]

```javascript
function inheritPrototype(SubType, SuperType) {
  SubType.prototype = Object.create(SuperType.prototype);
  Object.defineProperty(SubType.prototype, "constructor", {
    enumerable: false,
    configurable: true,
    writable: true,
    value: SubType,
  });
}

function Person() {}

function Boy() {}

inheritPrototype(Boy, Person);

let b1 = new Boy();

// 对象来查找上面的原型链
console.log(b1 instanceof Boy);
console.log(b1 instanceof Person);
console.log(b1 instanceof Object);

console.log(Boy.prototype.isPrototypeOf(b1))
```

![[00 assets/2682e49216a4901d1253b7aeb1f4e43a_MD5.png]]

### 11.4.6 原型关系

这里首先要明确一个关系，在`JS`中`函数`也是一个`对象`

```javascript
function foo() {}

// foo 作为一个对象来说是这样的
var foo = new Function()
```

首先`Foo()函数`的在创建的时候会将`prototype`赋值给`Foo原型对象`，然后`Foo原型对象`里面有一个`constructor`来指向本身的`Foo()函数`，并且`Foo()`本身作为一个对象，它会存在一个`__proto__`来指向`Function原型对象`。因为`Foo()`本身也是`new Function()`来创建的，所以`__proto__`指向构造器的原型对象。

![[00 assets/573b3c239a84a3c18242a3a19a4092e1_MD5.jpeg]]

下面为总的预览图，其中`Foo()`和`Function()`的关系可以参考上面的笔记

因为`Object()`本质也是一个函数，所以它的`__proto__`指向的是`Function原型对象`，而他作为一个函数，他的`prototype`指向的是`Object原型对象`。而`Fnuction`和`Foo`的`原型对象`本身作为一个对象，指向的是`Object原型对象`。

![[00 assets/09019b10ec9b69adbe9fad56841071e6_MD5.jpeg]]

## 11.5 继承

### 11.5.1 基本介绍

![[00 assets/00d3553647024e2595abba9806d1cde6_MD5.jpeg]]

### 11.5.2 继承方法

#### 11.5.2.1 原型链的继承

这中间经过了很长时间的演化，各个方式各有优劣，其中的过程可以参考视频来学习，下面就介绍最后的结果

我们再来看下`Object.create()`的底层实现。即`Object.create()`底层实现的功能和`createObject1()`是类似的，而`setPrototypeof()`的实现本质就和下面的`createObject2()`是差不多的

![[00 assets/7ddb0cd0cd0a6e8c36d493f3ba598267_MD5.png]]

下面为代码的实现

```javascript
function createObject(o) {
  var newObj = {};
  Object.setPrototypeOf(newObj, o);
  return newObj;
}
// 实现继承
function inheritPrototype(SubType, SuperType) {
  SubType.prototype = Object.create(SuperType.prototype);
  Object.defineProperty(SubType.prototype, "constructor", {
    enumerable: false,
    configurable: true,
    writable: true,
    value: SubType,
  });
}

// 创建父类
function father(name, age, hobby) {
  this.name = name;
  this.age = age;
  this.hobby = hobby;
}
father.prototype.say = function () {
  console.log("我是父类");
};

// 创建子类
function son(name, age, address, sex) {
  father.call(this, name, age);
  this.address = address;
  this.sex = sex;
}
son.prototype.watch = function () {
  console.log("我是子类，我在看父类");
};

// 调用继承函数
inheritPrototype(son, father);

var s1 = new son("张三", 18, "北京市", "男");
var f1 = new father("李四", 28);

s1.say();
```

因为`Object.create()`的版本可能比较高，所以可以使用`createObject()`来替换`Object.create()`

![[00 assets/54eb5ce1a30b73e22e34c01953effc11_MD5.png]]

#### 11.5.2.2 class 的继承

![[00 assets/fda1138bd4311848232e063ffa2601d6_MD5.png]]

1、这里需要特别提醒一个点，当我们使用 super 调用父元素的函数时，而这个函数正好使用 this 访问属性，那么这个 this 不是按照 js 之前的显式引入的对象，而是 子类 中的 this
2、比如下方的图，你在 Person 类中使用 super 调用 Animal 的方法时，this 就是 Person，而不是 Animal
![[00 assets/5b569bcf0f92b0b263789132eec50db9_MD5.png]]

### 11.5.3 继承内置类

下面为继承`Array`，这样我们就可以在该类中编写方法，来实现数组的方法

![[00 assets/253c815982936e97114465beadc1e2ce_MD5.png]]

### 11.5.4 类的混入

下面的这个混入的方式本质是继承，只不过是使用了`js`中函数的技巧

![[00 assets/be872cae3d58f3a7217f7acc79eb7cd2_MD5.png]]

假如学过了`react`的话可以参考下面的技巧

![[00 assets/3cb98562f277dbd7e79d252099bae41b_MD5.png]]

## 11.6 class

### 11.6.1 基本介绍

其实本质和原本的构造函数是一样的，只不过是一个语法糖

![[00 assets/fa1c88794d75900648af5c8f64c018f2_MD5.png]]

最后还是会将`Person`的显式原型传递给`p1`，所以本质和以前的原型链是一样的

![[00 assets/de2af937d36e018afed393613188a3ea_MD5.jpeg]]

### 11.6.2 构造函数

![[00 assets/560114c02729c8a8ca16d9010c1f7c10_MD5.png]]

假如要使用的话，可以参考下面的。这里需要注意，一个类中只能存在一个构造函数，**不存在重载**

![[00 assets/d26b29112b4743f48d7dc4fc19db4b54_MD5.png]]

### 11.6.3 定义方法

在`class`中定义的方法，其实最后都会存入到他的原型里面。

![[00 assets/3f7711478babfd8c8d7b275168d87db4_MD5.png]]

### 11.6.4 get/set

1、假如要在类里面的属性定义`get`和`set`的话，可以参考下面的方式

![[00 assets/bb5c435ec55e016e8a58c09d92a9aed2_MD5.png]]

2、如果对`class`中的方法添加了`get`的话，就不需要添加`()`来调用了，直接当作属性使用即可

![[00 assets/0f45348bd4991b27f504a0db9d42a957_MD5.png]]

### 11.6.5 静态方法

创建静态方法

![[00 assets/c604e36f2e58609f2ae1fc168addb3e8_MD5.png]]

### 11.6.6 重写方法

![[00 assets/a5c6b3ef365c096bac18e23d0df7b187_MD5.png]]

### 11.6.7 babel 转换

在线转换：[Babel · The compiler for next generation JavaScript (babeljs.io)](https://babeljs.io/repl/#?browsers=&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=MYGwhgzhAEAKCmAnCB7AdtA3gXyA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=true&fileSize=false&timeTravel=false&sourceType=module&lineWrap=false&presets=es2015%2Creact%2Cstage-2&prettier=true&targets=&version=7.19.5&externalPlugins=&assumptions={})

#### 11.6.7.1 基本介绍

下面是使用`babel`转换之后的代码

```javascript
/* --- 转换前 --- */
class Person { }


/* --- 转换后 --- */
"use strict";

// 3. _defineProperties
// 因为没有传入任何得属性，所以_defineProperties没有被调用
function _defineProperties(target, props) {
  for (var i = 0; i < props.length; i++) {
    var descriptor = props[i];
    descriptor.enumerable = descriptor.enumerable || false;
    descriptor.configurable = true;
    if ("value" in descriptor) descriptor.writable = true;
    Object.defineProperty(target, descriptor.key, descriptor);
  }
}

// 4. _createClass
function _createClass(Constructor, protoProps, staticProps) {
  if (protoProps) _defineProperties(Constructor.prototype, protoProps);
  if (staticProps) _defineProperties(Constructor, staticProps);
  // 为传入得构造函数Person添加prototype属性
  Object.defineProperty(Constructor, "prototype", { writable: false });
  return Constructor;
}

// 2. _classCallCheck
// --- 检测Person是否作为一个函数来调用 --- //
function _classCallCheck(instance, Constructor) {
  if (!_instanceof(instance, Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
}
function _instanceof(left, right) {
  if (
    right != null &&
    typeof Symbol !== "undefined" &&
    right[Symbol.hasInstance]
  ) {
    return !!right[Symbol.hasInstance](left);
  } else {
    return left instanceof right;
  }
}


// 1. /*#__PURE__*/
// /*#__PURE__*/ 该标记为pure,设置为纯函数，因为该函数没有副作用
// 在webpack解析的时候可以使用到tree-shaking技术，更好的对函数进行打包
var Person = /*#__PURE__*/ _createClass(function Person() {
  _classCallCheck(this, Person);
});
```

其中`_classCallCheck`是检测转换之后的类`Person`是否作为一个函数来调用

![[00 assets/98b357c5403a919baa45c8d73a98a7da_MD5.png]]

#### 11.6.7.2 常规使用

假如我们将代码变得更加复杂再来看下

```javascript
/* --- 转换前 --- */
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  eating() {
    console.log(this.name + ",正在吃饭");
  }
}

var b1 = new Person("张三", 18);


/* --- 转换后 --- */
"use strict";

// 1. 检测代码是否被函数调用 - 具体代码可以参考上面
function _instanceof(left, right) { ...... }
function _classCallCheck(instance, Constructor) { ...... }



function _defineProperties(target, props) {
  // target为Person得prototype,props为eating()函数
  for (var i = 0; i < props.length; i++) {
    var descriptor = props[i]; // props[i]为一个对象
    descriptor.enumerable = descriptor.enumerable || false;
    descriptor.configurable = true;
    if ("value" in descriptor) descriptor.writable = true;
    // 将该函数添加到Perosn得原型中
    Object.defineProperty(target, descriptor.key, descriptor);
  }
}

function _createClass(Constructor, protoProps, staticProps) {
  if (protoProps) _defineProperties(Constructor.prototype, protoProps);
  if (staticProps) _defineProperties(Constructor, staticProps);
  return Constructor;
}


var Person = /*#__PURE__*/ (function () {
  function Person(name, age) {
    _classCallCheck(this, Person);

    this.name = name;
    this.age = age;
  }

  // 2.这次protoProps有值，所有就会调用_defineProperties
  _createClass(Person, [
    {
      key: "eating",
      value: function eating() {
        console.log(this.name + ",正在吃饭");
      }
    }
  ]);

  return Person;
})();

var b1 = new Person("张三", 18);
```

#### 11.6.7.3 继承使用

```javascript
/* --- 转换前 --- */
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  eating() {
    console.log(this.name + ",正在吃饭");
  }
}

class Boy extends Person {
  constructor(name, age, address) {
    super(name, age);
    this.address = address;
  }
  running() {
    console.log("正在跑步");
  }
}

var b1 = new Boy("张三", 18, "北京市");
b1.eating();
b1.running();


/* --- 转换后 --- */
"use strict";

function _classCallCheck(instance, Constructor) { ...... }
function _instanceof(left, right) { ...... } // 可以参考上面得代码
function _defineProperties(target, props) { ...... }
function _createClass(Constructor, protoProps, staticProps) { ...... }

function _typeof(obj) {
  "@babel/helpers - typeof";
  return (
    (_typeof =
      "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
        ? function (obj) {
            return typeof obj;
          }
        : function (obj) {
            return obj &&
              "function" == typeof Symbol &&
              obj.constructor === Symbol &&
              obj !== Symbol.prototype
              ? "symbol"
              : typeof obj;
          }),
    _typeof(obj)
  );
}

// 3. _createSuper 因为_classCallCheck的限制，所以需要重新创建一个函数来进行调用
function _createSuper(Derived) {
  // 判断是否存在 Reflect
  var hasNativeReflectConstruct = _isNativeReflectConstruct();

  return function _createSuperInternal() {
    // 获取到Boy的 __proto__,因为在继承的_setPrototypeOf中设置了Boy的__proto__为Person
    // 所以下面的Super为Person
    var Super = _getPrototypeOf(Derived) , result;

    if (hasNativeReflectConstruct) {
      // 因为后续的_super是使用call调用的，所以这里的this是Boy
      var NewTarget = _getPrototypeOf(this).constructor;
      // Super -> Person;arguments -> name,age的值;NewTarget -> Boy
      // 会通过Person创建一个实例，但是这个实例的construct指向着Boy
      result = Reflect.construct(Super, arguments, NewTarget);
    } else {
      result = Super.apply(this, arguments);
    }
    return _possibleConstructorReturn(this, result);
  };
}
// 4. _isNativeReflectConstruct 查看你是否支持 Reflect
function _isNativeReflectConstruct() {
  if (typeof Reflect === "undefined" || !Reflect.construct) return false;
  if (Reflect.construct.sham) return false;
  if (typeof Proxy === "function") return true;
  try {
    Boolean.prototype.valueOf.call(
      Reflect.construct(Boolean, [], function () {})
    );
    return true;
  } catch (e) {
    return false;
  }
}
// 5. _getPrototypeOf 获取__proto__
function _getPrototypeOf(o) {
  _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf:
      function _getPrototypeOf(o) {
        return o.__proto__ || Object.getPrototypeOf(o);
      };
  return _getPrototypeOf(o);
}
// 6. _possibleConstructorReturn
function _possibleConstructorReturn(self, call) {
  if (call && (_typeof(call) === "object" || typeof call === "function")) {
    return call;
  } else if (call !== void 0) {
    throw new TypeError(
      "Derived constructors may only return object or undefined"
    );
  }
  return _assertThisInitialized(self);
}
// 7. _assertThisInitialized
function _assertThisInitialized(self) {
  if (self === void 0) {
    throw new ReferenceError(
      "this hasn't been initialised - super() hasn't been called"
    );
  }
  return self;
}


// 1. _inherits，设置继承
function _inherits(subClass, superClass) {
  // 1.1 这一步主要是让:Boy.prototype = 新对象.__proto__ = Person.prototype
  // 判断传入得父类是否为函数和null，如果不是就报错
  if (typeof superClass !== "function" && superClass !== null) {
    throw new TypeError("Super expression must either be null or a function");
  }

  // 1.2 基本逻辑和我之前实现得差不多，使用Object.create()，并且添加constructor
  subClass.prototype = Object.create(superClass && superClass.prototype, {
    constructor: { value: subClass, writable: true, configurable: true },
  });

  // 1.3 为subClasss得prototyp得writable设置为false
  Object.defineProperty(subClass, "prototype", { writable: false });

  // 1.4 下面得_setPrototypeOf是让Boy.__proto__ = Person，为了让静态方法得继承
  if (superClass) _setPrototypeOf(subClass, superClass);
}

// 2. _setPrototypeOf
// 因为Boy()函数本身就是一个对象，所以会有一个__proto__，当自身不存在属性得时候，按照常规得处理，就会去Function.prototype中去寻找，很显然找不到
// 所以需要单独设置__proto__，即Boy.__proto__ = Person，这样得话就会主动到Person中寻找
function _setPrototypeOf(o, p) {
  // 做兼容性处理
  _setPrototypeOf = Object.setPrototypeOf ||
    function _setPrototypeOf(o, p) {
      o.__proto__ = p;
      return o;
    };
  return _setPrototypeOf(o, p);
}

var Person = /*#__PURE__*/ (function () { ...... })(); // 可以参考上面得代码

var Boy = /*#__PURE__*/ (function (_Person) {
  _inherits(Boy, _Person); // 设置继承

  var _super = _createSuper(Boy); // 因为_classCallCheck得限制，所以需要对super进行处理

  function Boy(name, age, address) {
    var _this;

    _classCallCheck(this, Boy);

    _this = _super.call(this, name, age); // _super返回的是函数
    _this.address = address;
    return _this;
  }

  _createClass(Boy, [
    {
      key: "running",
      value: function running() {
        console.log("正在跑步");
      }
    }
  ]);

  return Boy;
})(Person);

var b1 = new Boy("张三", 18, "北京市");
b1.eating();
b1.running();
```

#### 11.6.7.4 静态方法

其实`静态方法`和前面的为原型添加原型是一样的，只不过它是添加到`函数`的对象上面

![[00 assets/fdc54a0a5cfe87d459412f08ea566881_MD5.png]]

因为`function Person()`虽然是函数，但是本身其实是对象，这个在原型关系里面有介绍。所以静态方法本质也是对对象中的方法进行调用

![[00 assets/992d49899648da73ab724b3f519c53ce_MD5.png]]

#### 11.6.7.5 阅读源码

![[00 assets/07332688b3790647b3930252c8d93ab6_MD5.png]]

## 11.7 多态

> 传统语言对多态的的要求

对于传统语言来说，只有满足下面的 3 个条件才会体现出`多态`

![[00 assets/d390cab05cb5b46fa8a5a4a54212de6c_MD5.png]]

> ts 中对多态的体现

![[00 assets/cee1fa415f9b38e07998b3c9e8a5d96d_MD5.png]]

> js 中对多态的体现

![[00 assets/25c59b62034af4b61243a030ded8625e_MD5.jpeg]]

## 11.8 方法

### 11.8.1 Object.freeze()

1、如果想整个对象都不能被修改可以使用这个方式来冻结整个对象

![[00 assets/3ee8bc594909f6b0378027453682c9c5_MD5.png]]

# 12. AJAX

## 12.1 基本介绍

![[00 assets/a96e960fc8799f74c1628d205ddb405f_MD5.png]]

> 网页渲染过程 - 服务器端渲染

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032312744.png" alt="image-20221110122749621" style="zoom: 67%;" />

> 网页渲染过程 - 前后端渲染

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032312772.png" alt="image-20221110105043179" style="zoom: 80%;" />

## 13.2 HTTP 介绍

### 13.2.1 基本介绍

![[00 assets/1828c10404abc0f492c0b5f213abc0fd_MD5.png]]

![[00 assets/b8e699daeb7970ab1000bc7bed92b7da_MD5.png]]

### 13.2.2 HTTP 组成

![[00 assets/e8eec589deab99439b7f982bc4598c43_MD5.png]]

### 13.2.3 HTTP 版本

![[00 assets/3261fe15bea85dd062147385ac52f6f6_MD5.png]]

### 13.2.4 请求方式

![[00 assets/7d2ae7e40a8552b7722bcb688b4339f9_MD5.png]]

### 13.2.5 请求头

![[00 assets/6a1e56f701d8b14790dbaa003b8e1360_MD5.png]]

![[00 assets/e9029203bf56e16b77a19b7c425eb89f_MD5.png]]

### 13.2.6 响应状态码

![[00 assets/43d82455e3dbacb25da3f5b1be4dea6b_MD5.png]]

## 13.3 网络请求

### 13.3.1 基本使用

![[00 assets/fe2a3bc854a7372f567a8c379a18c98f_MD5.png]]

下面就是基本使用的代码

![[00 assets/ed082cb30ae1e3fbe7a7bee7a8d606e0_MD5.png]]

### 13.3.2 xhr 状态

![[00 assets/2bc8694e7a90a21176415ea2f8634758_MD5.png]]

1、我们通过`xhr.readyState`来获取当前的状态。

2、如果要获取服务器传输过来的数据，可以使用`xhr.response`来查看

![[00 assets/ef52f5615ffb6c5751c8e85409256d0e_MD5.jpeg]]

### 13.3.3 关闭异步

在`xhr`的`open方法`中包含第三个参数，我们设置为`false`的话就会关闭异步请求

![[00 assets/a32bcbea460e80f911c4e92dc08fe821_MD5.png]]

### 13.3.4 事件监听

对于`xhr`还存在下面很多的事件监听

![[00 assets/1f487bd156ef06468d8e8e74c172d0e1_MD5.png]]

> onload

其中`onreadystatechange`只要请求发生了改变的话就会被调用，所以一次正常的请求会被调用`4`次。所以不是很节省资源，我们就可以使用`onload`来获取请求到的数据，因为这个是请求成功完成才被调用

![[00 assets/a07f555b13cea1ed905f047a3b9a9755_MD5.png]]

> onerror

1、如果发生连接错误的话就会执行`onerror`事件。

2、其实这里就要区别`状态码报错`和`连接错误`了，`状态码报错`其实是已经连接上服务器了，但是服务器返回给你的数据告诉你是错误的。但`连接错误`就是你连服务器的连接都没碰到

![[00 assets/d30297f9402d0452457ff049ec2366f8_MD5.png]]

### 13.3.5 响应数据

我们可以使用`responseType`来设置响应的类型

![[00 assets/85b2588582fe94c49cd7cced6a262ddd_MD5.png]]

### 13.3.6 HTTP 状态

其中`status`和`statusText`分别获取`状态码`和`状态描述`

![[00 assets/467944151a64ee763ff8b2acb8550728_MD5.png]]

### 13.3.7 传递参数

![[00 assets/d608d30f25abef5a10f713e48a4c2561_MD5.png]]

> query、x-www-form-urlencoded、json

我们可以使用下面的方式来发送请求

![[00 assets/c55debc8329e1115de489d40ff71d569_MD5.png]]

> formData

![[00 assets/ac59f7f18f108a4e39e29fd747e8d5bd_MD5.png]]

### 13.3.8 超时时间/取消请求

1、我们通过`timeout`来设置`超时时间`

2、我们通过`abort()`函数，就可以取消此次请求

![[00 assets/35463223f1e8ca7285591bd96c084341_MD5.png]]

## 13.4 请求封装

![[00 assets/d40400041fc68ca21dcc8bbd050c84eb_MD5.png]]

下面为实例代码

```javascript
// 普通封装
// function axios({
//   url,
//   method = "get",
//   timeout = "10000",
//   data,
//   success,
//   failure,
// } = {}) {
//   const xhr = new XMLHttpRequest();

//   xhr.onload = function () {
//     if (xhr.status >= 200 && xhr.status <= 300) {
//       success && success(xhr.response);
//     } else {
//       failure && failure(xhr.statusText);
//     }
//   };

//   xhr.responseType = "json";
//   xhr.timeout = timeout;

//   if (method.toUpperCase() === "GET") {
//     // 拼接query参数
//     const queryStrings = [];
//     for (const key in data) {
//       queryStrings.push(`${key}=${data[key]}`);
//     }
//     url = url + "?" + queryStrings.join("&");
//     xhr.open(method, url);
//     xhr.send();
//   } else {
//     xhr.open(method, url);
//     xhr.setRequestHeader("Content-type", "application/json");
//     xhr.send(JSON.stringify(data));
//   }

//   return xhr;
// }

// Promise封装
function axios({ url, method = "get", timeout = "10000", data } = {}) {
  const xhr = new XMLHttpRequest();

  const ResultPromise = new Promise((resolve, reject) => {
    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status <= 300) {
        resolve(xhr.response);
      } else {
        reject(xhr.statusText);
      }
    };

    xhr.responseType = "json";
    xhr.timeout = timeout;

    if (method.toUpperCase() === "GET") {
      // 拼接query参数
      const queryStrings = [];
      for (const key in data) {
        queryStrings.push(`${key}=${data[key]}`);
      }
      url = url + "?" + queryStrings.join("&");
      xhr.open(method, url);
      xhr.send();
    } else {
      xhr.open(method, url);
      xhr.setRequestHeader("Content-type", "application/json");
      xhr.send(JSON.stringify(data));
    }
  });

  ResultPromise.xhr = xhr;

  return ResultPromise;
}

axios({
  url: "http://123.207.32.32:8000/home/multidata",
  success(res) {
    console.log(res);
  },
  failure(rej) {
    console.log(rej);
  },
});

axios({
  url: "http://123.207.32.32:1888/02_param/get",
  data: {
    name: "zs",
    age: 18,
  },
  success(res) {
    console.log(res);
  },
  failure(rej) {
    console.log(rej);
  },
});

axios({
  url: "http://123.207.32.32:1888/02_param/postjson",
  method: "post",
  data: { name: "zs", age: 18 },
  success(res) {
    console.log(res);
  },
  failure(rej) {
    console.log(rej);
  },
});

const promiseXHR = axios({
  url: "http://123.207.32.32:8000/home/multidata",
});
promiseXHR.then((res, rej) => {
  console.log(res);
});
console.log(promiseXHR.xhr);

```

## 13.5 Fetch

### 13.5.1 基本介绍

![[00 assets/702e3f089393537eb564664e62beb4c9_MD5.png]]

![[00 assets/4676d05821eafe8f3a6fe28d61231f24_MD5.png]]

### 13.5.2 基本使用

1、下面就是对于`fetch`的基本使用，我的理解是在`ajax`的基础上进行了一次封装

![[00 assets/a11be8ae5c699f625f1fbd1bc4a67f2d_MD5.png]]

2、如果可以的话也可以使用`async/await`来优化代码

![[00 assets/779b1c9d74353dd46c1b786e03fba094_MD5.png]]

### 13.5.3 传递参数

其基本传递参数的规律基本上是一致的

> json

![[00 assets/df419ca7e5bfaaf563c2aed178d0fbe4_MD5.png]]

> formdata

![[00 assets/531d50fd2ab88762b07c6ea38a46913d_MD5.png]]

## 13.6 文件上传

> ajax

1、其中`ajax`上传文件和`fetch`的一个区别就是`ajax`可以使用`onprogress`来进行监听文件上传进度

![[00 assets/57ba8b5053a86c27f925a24162070fe4_MD5.png]]

> fetch

![[00 assets/666ee877780a0bba3604e5bd39aab6df_MD5.png]]

# 13. 错误处理

对于一些函数中无法解决得问题，我们可以直接使用`throw`来抛出错误

![[00 assets/6494d151847bd6e9805a72628574fe08_MD5.png]]

其中抛出错误得方式有下面得 4 种方式

![[00 assets/4e6f266c9b7c096a860ed25774afdf06_MD5.png]]

# 14. JSON

## 15.1 基本介绍

![[00 assets/dad5606de9acb8fa1e791bee974a9975_MD5.png]]

## 15.2 基本使用

![[00 assets/3b6648423232089c1a7fdf33bc45505e_MD5.png]]

## 15.3 序列化

### 15.3.1 基本使用

![[00 assets/de677fbfc63fe85115259f227c97b8a5_MD5.png]]

### 15.3.2 stringfy

对于`stringfy()`存在下面的 3 个参数的使用

![[00 assets/c01c54aef66ab6569bae952cc4d8cc71_MD5.png]]

我们还可以对`object`中添加一个`toJSON()`的方法，这是因为每次调用`JSON.stringfy`的时候就会调用`object`中存在的方法，所以我们可以自定义该函数`序列化`之后的样子

![[00 assets/0019ff85d73cee6ff73d98074bbd23b0_MD5.png]]

### 15.3.3 parse

![[00 assets/f5921d27d9f52707b7146c1f9e450d85_MD5.png]]

## 15.4 深拷贝

其实`JSON`可以对象进行深拷贝。但是这种方式有一个问题，就是不能对对象中得函数进行转换

![[00 assets/478c516a7093f3cdad224cb88faa1ce7_MD5.png]]

# 15. 数据存储

## 16.1 基本使用

1、`sessionStorage`作为一个会话存储，只要浏览器关闭就会消失，并且在同一个窗口下数据可以共享，假如你开启了一个新页面，该新页面不存在存储得数据

2、`localStorage`生命周期是永远存在，除非手动删除。并且多窗口都是可以使用得

![[00 assets/30a5c3b8cb0ce5c6c6aab458b9b69c2c_MD5.png]]

## 16.2 存储封装

```javascript
class Storage {
    constructor(isLocal = true) {
      this.storage = isLocal ? localStorage : sessionStorage;
    }
    setItem(key, value) {
      if (value) {
        this.storage.setItem(key, JSON.stringify(value));
      }
    }
    getItem(key) {
      const value = this.storage.getItem(key);

      if (value) {
        return JSON.parse(value);
      }
    }
    removeItem(key) {
      this.storage.removeItem(key);
    }
    clear() {
      this.storage.clear();
    }
    key(index) {
      const value = this.storage.key(index);

      if (value) {
        return JSON.parse(value);
      }
    }
  }

  const sessionStorage = new Storage();
  const localStorage = new Storage();

  export { sessionStorage, localStorage };

```

## 16.3 indexedDB

> 基本介绍

![[00 assets/c596dff48c8f7231181e7567fe1055bd_MD5.png]]

> 连接操作

![[00 assets/a8f2d8750906e060d04c1d3830ed3925_MD5.png]]

> 增加

注意：一般是执行完操作之后进行回调。并且连接数据库也是需要消耗时间，而且连接时异步，所以尽量将事务放置在回调中处理，这样避免事务没开启得情况

![[00 assets/482bffd2ab1eb0d0e4634e09c5cec7f5_MD5.png]]

> 查询

![[00 assets/5af070ea84377ac3680789a49b439731_MD5.png]]

> 修改/删除

其实修改和删除得本质是在查询得基础上进行处理，下面得操作获取来得游标

![[00 assets/a09c60a79128dd55055636883ec4a7d5_MD5.png]]

![[00 assets/7e7011b2cb48f829da398dd2f65f6423_MD5.png]]

## 16.4 Cookie

具体得笔记可以参考`Node.js`中`16.2.4.2 Cookie`得笔记

# 16. 浏览器

## 16.1 BOM

### 17.1 基本介绍

![[00 assets/8a14c808c82fb1b31fc9a3ebc10a84d6_MD5.png]]

### 17.2 window

#### 17.2.1 基本介绍

> 作为全局对象

![[00 assets/0f2e2edec082d686a9f91cebcfcac737_MD5.png]]

> 作为浏览器连接得对象

**MDN 网址**：[Window - Web API 接口参考 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/API/Window)

![[00 assets/5033ebd361ec8f298414edd35d0e1664_MD5.png]]

#### 17.2.2 基本使用

下面为`window`中比较常见得属性、方法、事件

![[00 assets/d4e27f62e31694e2aa4d79a13f133727_MD5.png]]

#### 17.2.3 EventTarget

当然`window`继承自`EventTarget`，本质其实是继承下面得 3 个方法

![[00 assets/4564c4413cdac2ac9044e3df9bb67369_MD5.png]]

### 17.3 location

#### 17.3.1 常见属性

下面为`location`常见得属性

![[00 assets/cff304a5c1759af188a8fb956c972d7d_MD5.png]]

下面是`jd`得`location属性`

![[00 assets/918f7985f835a16ddfcd47c1ad0ab5f0_MD5.png]]

#### 17.3.2 常见方法

![[00 assets/41719b4ca17c6947aca1dc0794f0acbd_MD5.png]]

![[00 assets/82c76540861b9acae48a5e6975917cd4_MD5.png]]

### 17.4 navigator

`navigator`包含有关浏览器的信息，它具有很多的属性。其中最常见的就是`useAgent`，该属性可以返回由客户端发送服务器的`user-agent`头部的值

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
	</head>
	<body>
		<button type="button">按我</button>
		<script type="text/javascript">
			if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))){
				console.log("这是手机端的页面");
			}
			else{
				console.log("这是电脑端的页面");
			}

		</script>
	</body>
</html>

```

假如我们看的是电脑端浏览器

![[00 assets/0d9943ca7fcbf1b177096589e463e989_MD5.png]]

假如我们使用手机端浏览器

![[00 assets/44096d95a00ae8e2d5b54f8b724769ee_MD5.png]]

### 17.4 history

![[00 assets/43b24d82a06f686ef031b024c21486d3_MD5.png]]

![[00 assets/61b6711ada8e8eab017145bd8930b15d_MD5.png]]

## 16.2 DOM

### 17.1 基本介绍

对于`DOM`来说就是按照下面得方式来做`架构`，其中`Document`和`Element`是并列关系

![[00 assets/58a22b94f00fae253dbd34c9f4cd700c_MD5.png]]

### 17.2 EventTarget

因为都是继承得`EventTarget`所以可以使用`addEventListener`...方法来对事件进行监听

![[00 assets/d45075bc81b17561f545f450ad8776e6_MD5.png]]

### 17.3 Node

**MDN 网址**：[Node - Web API 接口参考 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/API/Node)

![[00 assets/1b7544ebe6bc22a1e6de5c24e6235999_MD5.png]]

### 17.4 Document

![[00 assets/849703b9fe9f7277c54431bd5559b7d0_MD5.png]]

### 17.5 Element

![[00 assets/6144d3f61e5419811a21b7bf67a5bbdf_MD5.png]]

## 16.3 事件监听

### 16.3.1 基本介绍

![[00 assets/b83dfaa3b8b19aa7d90a56e0ceb5910e_MD5.png]]

![[00 assets/68cd0dd278c8d4d3303893cc69c3a717_MD5.png]]

### 16.3.2 事件流

![[00 assets/e6905020b968b04bd0d09ec3307b6ce2_MD5.png]]

![[00 assets/5cbeae653f29d8a70180e89b9d263d22_MD5.png]]

### 16.3.3 event

**MDN 文档**：[事件参考 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/Events)

![[00 assets/024073bb8c9f3a92aa74f9229ac3ba57_MD5.png]]

# 17.字符串

## 17.1 码元码点

视频教程: https://www.bilibili.com/video/BV1Wp4y1j79w?vd_source=8992a13080c32977bce93a5140823f3b

针对码元码点这一块，其实本质就是有一些文字 emoji 的码元不是一个，而是两个
![[00 assets/2e7e619ae467350719e34750ef5b8e41_MD5.png]]

我们可以使用如下的方式来解决，也可以自己封装
![[00 assets/98f1f0848f07e47bab6260f121ac5145_MD5.png]]


# 18.位运算符

1、因为`ESMAScrip`默认是`IEEE 754 64位格式`存储数据的，但位操作不能使用`64位`，所以会将数据先转为`32位`然后在进行位运算，然后再转为`64位`

2、负值是按照二补数的形式来存储的，下面是负值的存储方式

![[00 assets/14cebc3363b19dd84a3057f5474882a1_MD5.jpeg]]

3、下面就是基本的位运算符

![[00 assets/efdde59fa5c1719ddb207b1ddc88c748_MD5.jpeg]]

![[00 assets/a11440cdced0a894142437a3a3862874_MD5.jpeg]]

但是对于`>> << >>>`存在一些细节，比如`>>>`就是无符号右位移，对于正数来说问题不大，但是对于负数来说就有很大的区别了


