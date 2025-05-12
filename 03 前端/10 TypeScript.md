**视频讲解**：[尚硅谷 TypeScript 教程（李立超老师 TS 新课）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Xy4y1v7S2?spm_id_from=333.337.search-card.all.click)

**视频讲解**：coderwhy - 前端系统课 - TypeScript

**参考文档**1：[ts 保姆级教程，别再说你不会 ts 了 - 掘金 (juejin.cn)](https://juejin.cn/post/7092415149809598500)

**参考文档 2**：[2021 typescript 史上最强学习入门文章(2w 字) - 掘金 (juejin.cn)](https://juejin.cn/post/7018805943710253086)

**练习题**：[semlinker/awesome-typescript: A collection of awesome TypeScript resources for client-side and server-side development (github.com)](https://github.com/semlinker/awesome-typescript)

# 1. 基本介绍

## 1.1 类型缺失

> JavaScript 是一门优秀的编程语言

![[00 assets/e464c161a412c5e3a9e06660000ae092_MD5.png]]

![[00 assets/a50741744c050c742d8bd81b39b38a6d_MD5.png]]

> 类型带来的问题

 ![[00 assets/05f7a9af969d620ac20327be31b5e8aa_MD5.png]]

![[00 assets/005b83a289ce8e4f445c1bf90a49e6da_MD5.png]]

> 前端人员类似思维缺失

![[00 assets/c7f7faad3864c86afd363b4f3bfe2a7e_MD5.png]]

## 1.2 类型校验

![[00 assets/ebecea94ad64b53549fb9de4607424a1_MD5.png]]

## 1.3 认识 TS

![[00 assets/3d32ab11760e16cc52205a1bf1ac1bc2_MD5.png]]

## 1.4 TS 特点

![[00 assets/b03b95cf3fbbfbeee6d0700758174b3d_MD5.png]]

## 1.5 JS/TS 对比

^160a62

![[00 assets/b135c557db5cf5544b15decddf811f0f_MD5.png]]

# 2. 基本使用

## 2.1 开发环境

> 创建`.ts`文件

1. 下载安装`Node.js`

2. 使用`npm`全局安装`TypeScript`

   ```bash
   npm i -g typescript
   ```

3. 安装`ts-node`，用于直接在`Node.js`环境里面运行 ts 文件，这样就不需要通过`webpack`将 ts 文件打包为低版本的 js 文件再执行

   ```bash
   npm i -g ts-node
   ```

4. 创建`tsconfig.json`文件（**可选**，只是 demo 的话就不需要创建）

   ```bash
   tsc --init
   ```

5. 创建`.ts`文件

> 执行 TS 的 2 种方式

1. 将`TypeScript`文件转换为`JavaScript`文件，再去执行

   ```bash
   tsc xxx.ts		//编译单个文件
   tsc xxx.ts -w 	//自动编译单个文件

   tsc				//编译所有文件
   tsc -w 			//自动编译所有文件
   ```

2. 在`node`环境下执行

   ```
   npm i ts-node -g 				// 安装ts-node
   npm i tslib @types/node -g 	// 安装依赖包
   ts-node xxx.ts 		// ts-node环境下执行
   ```

​

## 3.1 类型声明

1、**类型声明**是 TS 非常重要的一个特点，通过类型声明可以指定 TS 中变量（参数、形参）的类型。

2、指定类型后，当为变量赋值时，TS 编译器会自动检查值是否符合类型声明，符合则赋值，否则就报错。

3、下面的`:number`被称为**类型注解**，后续还有一个**类型签名**

![[00 assets/18aa0618f383f780bebd050017c98cb2_MD5.png]]

## 3.2 类型推导

1、TS 拥有**自动的类型判断机制**，当对变量的声明和赋值是同时进行的，TS 编译器会自动判断变量的类型

2、所以如果你的变量的**声明和赋值同时进行**的，可以省略掉类型声明，这个在文档中有明确的提示

3、假如你是使用**let/var**来创建的变量就是按照赋值的类型来的，你使用的是**const**的话就是按照`字面量类型`来推断的

![[00 assets/da5b9324ec7015c6030acaf32dbbe89b_MD5.png]]

4、其中对于**匿名函数**最好的方式就是不去手动的写它们的类型，而是是根据它的**执行上下文**自动判断

![[00 assets/6e54629213b91437afbe85e4885e24ff_MD5.png]]

其中匿名函数执行中得参数为什么会有类型?因为理解为底层使用了下面得方式来进行处理

![[00 assets/55ca32a92c3215d784c2a696ce0b6def_MD5.png]]

## 3.5 任意属性

下面就是任意属性的使用，我们使用`[propName:string]:any`就表示属性名为`string`，值为`any`类型的

![[00 assets/79689402d71fd1fadd827b6d309b3817_MD5.png]]

一旦定义了任意属性，那么**确定属性**和**可选属性**的类型都必须是它的类型的**子集**

下面报错是因为，`number`不是`string`的子类型，所以会报错

![[00 assets/e4ae7052abbbff91f3d01c7ec5e82cf5_MD5.png]]

所以这个时候就需要联合类型来进行

![[00 assets/c15e870b1a1ab65eb918b33c2289c926_MD5.png]]

## 3.6 注意点

### 3.6.1 null 和 undefined

默认情况下 `null` 和 `undefined` 是所有类型的子类型。 就是说你可以把 `null` 和 `undefined` 赋值给其他类型。

```typescript
// null和undefined赋值给string
let str:string = "666";
str = null
str= undefined

// null和undefined赋值给number
let num:number = 666;
num = null
num= undefined

// null和undefined赋值给object
let obj:object ={};
obj = null
obj= undefined

// null和undefined赋值给Symbol
let sym: symbol = Symbol("me");
sym = null
sym= undefined

// null和undefined赋值给boolean
let isDone: boolean = false;
isDone = null
isDone= undefined

// null和undefined赋值给bigint
let big: bigint =  100n;
big = null
big= undefined
```

如果你在 tsconfig.json 指定了`"strictNullChecks":true` ，`null` 和 `undefined` 只能赋值给 `void` 和它们各自的类型。

![[00 assets/dcbd6bffb017904f01d04285a7e03c1e_MD5.png]]

我们一开始配置话会有这个问题

![[00 assets/7ff42bdb46815826a038bcc29ad5a768_MD5.png]]

假如我们需要使用`bigint`类型，我们需要将`tsconfig.json`里面的`target`和`lib`设置为`ES2020`以上

![[00 assets/cba9654b91405a065e86a0802484bfa5_MD5.png]]

### 3.6.2 number 和 bigint

虽然`number`和`bigint`都表示数字，但是这两个类型不兼容。

```typescript
let big: bigint =  100n;
let num: number = 6;
big = num;
num = big;
```

# 3. 相关类型

## 4.1 基本介绍

|  类型   |         例子         |             描述             |
| :-----: | :------------------: | :--------------------------: |
| number  |       1,-2,90        |           任意数字           |
| String  | "hi",'hello',welcome |          任意字符串          |
| boolean |      true,false      |     布尔值 true 或 false     |
| 字面量  |        其本身        | 限制变量的值就是改字面量的值 |
|   any   |          \*          |           任意类型           |
| unknown |          \*          |        类型安全的 any        |
|  void   |   空值(undefined)    |     没有值(或 undefined)     |
|  never  |        没有值        |         不能是任何值         |
| object  |    {name:"张三"}     |         任意 JS 对象         |
|  array  |       [1,2,3]        |         任意 JS 数字         |
|  tuple  |        [4,5]         |  TS 新增类型，固定长度数组   |
|  enum   |      enum{A,B}       |      TS 新增类型，枚举       |

🎉 这里需要注意一个点：**number、string、boolean、symbol** 混淆的首字母大写的 **Number、String、Boolean、Symbol** 类型，其实后者是包装类

## 4.2 常见类型

### 4.1.1 array

1、**类型推导**：自动推导出类型

![[00 assets/7bbcdc3abdd6827b489410f1a2f4ad05_MD5.png]]

2、**类型声明**：可以使用下面的 2 种方式声明

![[00 assets/c47353d2039fd6b04a82656f4af5bc0a_MD5.png]]

3、**数组中添加多种类型**：可以使用`联合类型`配合，这样一个变量就可以传输多种数据类型

![[00 assets/70cb84a4c0e5e6fdd943e3ea08a20838_MD5.png]]

4、**数组中存储对象类型**：我们可以使用`type`或者`interface`

![[00 assets/72117408d5884847acfe200f131bbecc_MD5.png]]

5、**ReadonlyArray**：可以确保数组创建后再也不能被修改。

![[00 assets/3b696d237f688c3a09c83f65d4918cad_MD5.png]]

### 4.1.2 object

#### 4.1.2.1 基本使用

1、**类型声明**

![[00 assets/103620f9dd0fc29a9ebd41c9c58a8406_MD5.png]]

2、**可选类型**：添加上`?`表示可选类型，这样可以选择添加上去，或者不添加上去都可以

![[00 assets/08321d51d71f9e9d1a259208aa7c3d76_MD5.png]]

3、**交叉类型**

![[00 assets/1796a7f713e9288973837c90307b9591_MD5.png]]

4、**类型别名**：这个是经常使用的方式

![[00 assets/6bb2c7824ab574f36ca827a74982557f_MD5.png]]

#### 4.5.2 包装类

**object**（首字母小写，以下称“小 object”）、**Object**（首字母大写，以下称“大 Object”），其实 2 个 object 是不一样的

**小 object** 代表的是所有非原始类型，也就是说我们不能把 **string、boolean、number、bigint、symbol、null 和 undefined**。等 原始类型赋值给 object。在严格模式下，**null 和 undefined** 类型也不能赋给 object。

```typescript
let lowerCaseObject: object;

lowerCaseObject = 1; // ts(2322)
lowerCaseObject = 'a'; // ts(2322)
lowerCaseObject = true; // ts(2322)
lowerCaseObject = null; // ts(2322)
lowerCaseObject = undefined; // ts(2322)
lowerCaseObject = {}; // ok
```

**大 Object** 代表所有拥有 **toString、hasOwnProperty** 方法的类型，所以所有原始类型、非原始类型都可以赋给 Object。同样，在严格模式下，**null 和 undefined** 类型也不能赋给 Object。

```typescript
let upperCaseObject: Object;

upperCaseObject = 1; // ok
upperCaseObject = 'a'; // ok
upperCaseObject = true; // ok
upperCaseObject = null; // ts(2322)
upperCaseObject = undefined; // ts(2322)
upperCaseObject = {}; // ok
```

根据上面的结果，我们可以知道`Object`是`object`的父类，但是实际上，`Object` 不仅是 `object` 的父类型，同时也是`object` 的子类型。

```typescript
type isLowerObjectExtendsUpperObject = object extends Object ? true : false; // true
type isUpperObjectExtendsLowerObject = Object extends object ? true : false; // true
upperCaseObject = lowerCaseObject; // ok
lowerCaseObject = upperCaseObject; // ok
```

尽管官方文档说可以使用`object`代替`Object`，但是我们仍要明白`Object`并不完全等价于`object`。

#### 4.5.3 {}

和`Object`一样，并且在严格模式下，null 和 undefined 也不能赋给 {}

```typescript
let upperCaseObject: Object;
let ObjectLiteral: {};

ObjectLiteral = 1; // ok
ObjectLiteral = "a"; // ok
ObjectLiteral = true; // ok
ObjectLiteral = null; // ts(2322)
ObjectLiteral = undefined; // ts(2322)
ObjectLiteral = {}; // ok

//证明{}和Object是一样的
type isLiteralObjectExtendsUpperObject = {} extends Object ? true : false; // true
type isUpperObjectExtendsLiteralObject = Object extends {} ? true : false; // true
upperCaseObject = ObjectLiteral;//ok
ObjectLiteral = upperCaseObject;//ok
```

**结论**：`{ }`、`Object` 是比`object`更宽泛的类型，`{ } `和大 `Object` 可以互相代替，用来表示**原始类型**（null、undefined 除外）和**非原始类型**；而`object`则表示**非原始类型**。

### 4.1.3 any

![[00 assets/42732f5464a64b97b538a0045ba13bd9_MD5.png]]

对于`any`也不是所有的地方都用`any`，也不要不使用`any`

![[00 assets/3be3c3a863f83494fc45bed17953afe7_MD5.png]]

### 4.3.2 void

1、对于`void`来说，最常见的地方就是在**函数的返回值**中

![[00 assets/0a14d1a1dfe40df1df11c554b39263da_MD5.png]]

2、当为`可变参数args`的时候，可以使用`any[]`来接受处理，因为你不知道传输的数据是多少

3、当函数作为函数参数的时候就可以使用上面的`函数别名`来自己定义一个函数类型

3、`delatTime: number = 1000`当`delayTime`作为一个参数赋值的时候就默认带上了`可选类型？`

![[00 assets/a82bbf15f08066405dd42fd675f226e1_MD5.png]]

4、基于`上下文类型推导的函数`虽然返回值为`void`，即便我们设置返回值也不会报错，但是这种函数中我们写返回值也没什么意义

![[00 assets/0249cc3a07ae4910e7fa036dcdeee785_MD5.png]]

### 4.10 字面量

1、`"this is string"`（这里表示一个字符串字面量类型）类型是 `string`类型（确切地说是 `string` 类型的子类型），而 `string` 类型不一定是 `"this is string"`（这里表示一个字符串字面量类型）类型

`“马”`比喻 `string` 类型，即“黑马”代指 `"this is string"` 类型，“黑马”肯定是“马”，但“马”不一定是“黑马”，它可能还是“白马”“灰马”。因此，'this is string' 字面量类型可以给 string 类型赋值，但是 string 类型不能给 'this is string' 字面量类型赋值

![[00 assets/4f226ffd7700784958666712394db140_MD5.png]]

2、当然我们只是设置自变量类型是没用的，一般和**联合类型**一起使用

![[00 assets/cddffb17c835d09f8b82490f7cba7588_MD5.png]]

3、我们可以设置将**自变量**类型传输给**string**类型，所以这个自变量类型是**string**类型的子类，所以这个自变量类型转换为 string 类型，我们叫做**类型扩展**

![[00 assets/dff82c2a6aeb9832b669c3fb31ee3799_MD5.png]]

4、假如我们按照下面的方式来传递的话就会出现问题，因为`TS`认为`method`为`string`类型

![[00 assets/12d7a4fd6fe0962a61ec921dd9dfb6c8_MD5.png]]

我们可以使用下面的 3 种方式来解决这个问题

![[00 assets/2d6e9b434adeda255b3f448869d778cc_MD5.png]]

### 4.9 function

#### 4.9.1 基本使用

1、其中`(参数列表) => 返回值`表示是一个`函数类型表达式`

![[00 assets/17219edd0fdec5b7cb5461953c29f71b_MD5.png]]

假如我们不按照指定的类型来写的话就会报错

![[00 assets/c706806629953c66b4e893aa1e1961e6_MD5.png]]

2、使用`函数类型表达式`最常见的地方在传递函数的时候

![[00 assets/36321a4fa44226cbcae2a27f89bce68f_MD5.png]]

3、`TS`故意对函数的个数不进行检测。因为对于`JS`来说，`函数`的参数本身就可以不传，这样可以更加灵活的调用函数，假如做了参数校验的话，`TS`反而不方便了

![[00 assets/413c7c894a677e5334e611f912c0e94a_MD5.png]]

当然也并不是完全不做校验，当参数超出的时候也会报错

![[00 assets/6111e0c4c4637abb5561f8abf3e8f63c_MD5.png]]

4、**可选参数、默认参数、剩余参数**

![[00 assets/ddc0ae7a2a63acaf36ca5a4079804843_MD5.png]]

5、如果想对函数添加类型的话，箭头函数按照下面的方式来添加也可以

![[00 assets/5a98810d225ee6716a68c6aa73808c03_MD5.png]]

#### 4.9.2 调用签名

1、`函数`作为一个`对象`，可以存在自己的属性，但是不仅仅是自己的属性。可能还需要调用自身的方法，所以就存在调用签名
2、假如我们想要函数既有自己的属性，而且可以调用自己的方法就要是要`interface`来定义。这是因为使用`type`定义得话语法就是`type myType = { ... }`得形式，这样得话就是定义对象了
3、并且需要使用调用签名`( 参数列表 ): 返回值`。如果只是作为一个函数使用的话，就是要`函数类型表达式((num1: number) => number)`得形式
4、需要区分`调用签名`和`函数类型表达式`的格式
![[00 assets/3ceb4cb07095459b506fe71707a8cdd7_MD5.png]]

5、针对调用签名还存在如下的写法
![[00 assets/d5873a5b0eb728b3391b5148c94d1209_MD5.jpeg]]
6、大致可以理解为传入的泛型的参数是作为 `TState` 来使用的，他返回的函数 `useSelector` 就可以传入泛型 `useSelector<number>` 那么这里的 `number` 就是 `TSelected`，本质是返回的函数的泛型的写法，前面的`<TSelected>`泛型本质是调用是函数类型
![[00 assets/2f6e2f2e469e2749b10b0d10667ceb49_MD5.jpeg]]

#### 4.9.3 构造签名

1、为了通过`new`得方式来调用得话，就可以使用`构造签名`进行描述

2、如果是函数得调用就可以使用`调用签名`，如果是使用`new`得话就可以使用`构造签名`

![[00 assets/08d2ff5492dccc2d1f4206718459abe8_MD5.png]]

3、作为`构造签名`我们也可以书写成下面的形式，作为一个函数的格式来调用

![[00 assets/e3b3ae77e32d25133d2a7eff704ef7a4_MD5.png]]

#### 4.9.3 函数重载

![[00 assets/29e117bb679ff9e5ef730f3846bab264_MD5.png]]

> 联合类型/函数重载实现

在使用**联合类型**可以实现的情况下，最好使用**联合类型**，只有实现不了情况下使用**函数重载**

![[00 assets/97701fb2bc4e2fa9f592b2a52ee246bc_MD5.png]]

## 4.3 不常见类型

### 4.3.1 unknown

1、**unknown**就如它的英文名一样，”**不知道**“，我们一开始赋值的时候其实是不知道它是什么类型的。当我们使用的时候就需要知道它是什么类型，所以就不能进行使用

![[00 assets/cd9d77aed5b8ddc93530bc815a583e25_MD5.png]]

![[00 assets/f2d0326502392123f3f7b3eeff9bfc3d_MD5.png]]

2、对于下面的场景，我们可以使用`if`来进行**类型缩小**

![[00 assets/c84a41b8638b5cea574072eb64314b92_MD5.png]]

3、**类型断言**：使用类型断言也可以改变`unknown`的类型

![[00 assets/bf2ec8d6778f2d9cc46e4eccb4c8e47d_MD5.png]]

### 4.3.2 never

1、`never`表示永远没有返回结果。包含下面的 2 个场景是`never`类型

![[00 assets/7c4cc555e907e988df95e463b57b7a10_MD5.png]]

2、我们平常开发的时候基本是不使用`never`，但是我们封装工具库或者框架的时候会比较常见，比如说：下面的这个案例，我们还可以使用`never`来实现**类型检查**

![[00 assets/40bcb0f70c51ed1294955b69c0dbe849_MD5.png]]

假如给`Foo类型`添加布尔值，但是`controlFlowAnalysisWithNever`这个方法里面还没有布尔类型的判断。这个时候`never`的作用就体现出来了，因为任何类型都不能给`never`赋值，所以就会报错，提醒开发者`boolean`类型没有编写逻辑

![[00 assets/85da8370284d36a90b6cf97d84a6ae7d_MD5.png]]

### 4.3.3 tuple

1、`元组`最重要的特性是可以限制`数组元素的个数和类型`，它是介于`对象`和`数组`之间的类型。当我们想保存不同类型的值，但是不想添加很多的`key`，那么就可以使用`元组`

![[00 assets/479ddc113760430699cfc87ab63fa62f_MD5.png]]

2、`tuple`使用最常见的地方就是作为函数的返回值存在

![[00 assets/4b760d2af1e46e14041589ef873e9dd4_MD5.png]]

但是这里书写`元组`的类型的时候会存在一个问题，我设置为`void`的时候下面元组返回依旧不会报错

![[00 assets/afabdcb186b0080d8a9415b7c7493ac4_MD5.png]]

3、**解构元组**

![[00 assets/8e5aec978881ac0c77a65918a79a6def_MD5.jpeg]]

4、**可选参数；剩余参数**

![[00 assets/710e1be9f63efc754ba7915c9b5348ca_MD5.png]]

### 4.3.4 enum

![[00 assets/d45fb71e608ed3e67304a5d847fdfc0b_MD5.jpeg]]

![[00 assets/ada342ac6e4d0528c5f9cd8e8d830098_MD5.png]]

当然在`枚举`中也有这样的使用，这个是为了二进制中的计算，主要是为了后续做逻辑运算方便

![[00 assets/c987dfcad5e38a0629eecf28f45ed4be_MD5.png]]

## 4.4 高级类型

### 4.4.1 联合类型

1、`联合类型`使用`|`，表示指定的类型中其中一个

![[00 assets/d1337696aa9c526bb31631c270f40e03_MD5.png]]

2、对于联合类型我们一般会搭配使用`缩小类型`

![[00 assets/a3c8209d19d09334b087b1a0d7792887_MD5.png]]

### 4.6 类型别名

#### 4.6.1.1 type

1、我们可以为`一个`或者`一组`类型使用**type**来**取别名**

![[00 assets/f6da799b35956146a2fe991532955581_MD5.png]]

2、我们还可以对`object`类型取别名，其主要是为了提高可读性

![[00 assets/20086281e72627a247e5d1e276586343_MD5.png]]

3、对于`type`来说，我们也可以实现继承。参考`10.7.2 接口继承`的笔记

#### 4.6.1.2 interface

站在**类型别名**的角度来说的话，大多数情况中`interface`和`type`是一样的，但是`type`的使用场景更广一点。但是站在**对象类型的声明**的角度来说`interface`的扩展性是更强的

所以最后总结为：`对象类型`声明最好使用`interface`，`非对象类型`最好使用`type`

![[00 assets/a8239b6c644e6d647724693a4f11757f_MD5.png]]

> type 和 interface 区别

1、**语法格式不同**

```typescript
interface Person {
  name: string;
  age: number;
}

type Car = {
  name: string;
  id: number;
};
```

2、**type 可以接受其他类型**，但是`interface`只能接受`对象类型`

```typescript
// primitive
type Name = string;

// object
type PartialPointX = { x: number };
type PartialPointY = { y: number };

// union
type PartialPoint = PartialPointX | PartialPointY;

// tuple
type Data = [number, string];

// dom
let div = document.createElement("div");
type B = typeof div;
```

3、**接口可以定义多次,类型别名不可以**

```typescript
interface Point {
  x: number;
}
interface Point {
  y: number;
}
// 定义相同的interface最后会汇总在一起
const point: Point = { x: 1, y: 2 };
```

4、对于`interface`来说，我们也可以实现继承。参考`10.7.2 接口继承`的笔记

### 4.3 可选类型

1、在变量的后面添加`?`就是表示**可选类型**

![[00 assets/12dd4b0a5b1f6dfc72af04725c7fd63a_MD5.png]]

2、`可选类型`的本质其实是一个`联合类型`，也就是`xxx | undefined`

![[00 assets/f6ead0a51996cdc251940305137a25f8_MD5.png]]

### 4.5 交叉类型

联合类型和交叉类型区别：[联合类型和交叉类型 #JavaScript #前端开发工程师 #编程 #程序员 #web 前端 - 抖音 (douyin.com)](https://www.douyin.com/video/7369206544199716105)

1、我们可以将不同类型的进行取并集的操作，但是这种方式不是很好

```typescript
type Case = string | number
```

`交叉类型`的真正的使用方式是将不同接口的值合在一起

```typescript
type Person = { age: number } & { name: string };
let p1: Person = { name: "张三", age: 18 };
```

2、当我们按照下面的互斥的方式，最后推算出来的结果为`never`。当然最好还是不要按照下面的方式来写`&`

![[00 assets/9614f4a7f2b2148d3b93e0efa1d9b394_MD5.jpeg]]

### 4.6 类型断言

> 类型断言

1、使用`类型断言`，就是确切的告诉 TypeScript 这个类型我确定，不用去检查。我们使用类型断言是清楚地知道这个实例具有比它现有类型更确切的类型。

其中`greaterThan2`返回值一定是`number`，但是 TypeScript 认为它返回值有`number`或者`undefined`，所以这个时候就需要类型断言

![[00 assets/20e7f9b6c6ff3cb73dbbae782c803315_MD5.png]]

或者我们在获取`DOM`的情况下，可能为`Element | null`所以就需要使用`类型断言`

![[00 assets/9a238f3a3f52c95f8cc73660e889e67e_MD5.png]]

2、我们可以使用下面的 2 种方式来做`类型断言`

![[00 assets/c3ea7ed2821b5781428350b74d89ddad_MD5.png]]

> 非空类型断言

后缀表达式操作符 `!` 可以用于断言操作对象是非 null 和非 undefined 类型。**具体而言，x! 将从 x 值域中排除 null 和 undefined 。**

下面就是 StrNull 可能为 null 或者 undefined，我们使用非空断言，可以直接断言 StrNull 为非空

![[00 assets/bbe53b6c4f63bf84c2dc02fba5ced3d9_MD5.png]]

我们使用非空断言就可以解决了

```typescript
type NumGenerator = () => number;

function myFunc(numGenerator: NumGenerator | undefined) {
  const num1 = numGenerator(); // Error
  const num2 = numGenerator!(); //OK
}
```

> 确定赋值断言

我们没有赋值，可能就默认为空值，但是不是 null 和 undefined

![[00 assets/f7af070fb752d3ebf5baa3dfce7e262a_MD5.png]]

假如我们加上`!`也可以作为确定赋值断言，表示这个值肯定不是空值

![[00 assets/db68f6301ecbf7c816018143c420b35c_MD5.png]]

通过 `let num!: number;` 确定赋值断言，TypeScript 编译器就会知道该属性会被明确地赋值。

### 4.7 类型缩小

![[00 assets/c6f1ecb51e5465aa245a1e60bdd80d5c_MD5.png]]

1、**typeof、平等缩小、instanceof**

![[00 assets/f6fa059f8c42b8f8545835b27d37f8ca_MD5.png]]

2、**in**

![[00 assets/9c7a15163de34824649373d05eaaf3a2_MD5.png]]

### 4.7.4 readonly

```typescript
//TypeScript 3.4 对元组引入新特性readonly，表示只读

let a: readonly [number, string] = [18, "张三"];
a[0] = 20;	//Error 因为我们对元组设置了只读
```

### 4.7.9 条件类型

> 基本使用

![[00 assets/31bf6bf6a7c9167f978a9c8f5a6e47ed_MD5.png]]

1、如果理解的话，就可以理解为：`三元运算符 + 类型`。下面就是一种条件类型，查看`number/boolean`是否继承自`myType`

![[00 assets/a21b77435db84ce08ce785abcdac1419_MD5.png]]

2、其中的一个场景就是优化`函数重载`，但是按照复杂度来说的话，其实没优化多少。但是对于第三方库来说可能存在这样的写法

![[00 assets/941c5db5eae62e3d12a90a889983c24d_MD5.png]]

> 推断条件类型

![[00 assets/973b7670ae3d63c9c057ebc4253b10ad_MD5.png]]

条件类型中推断就是`infer`关键字，但是这个在实际的项目中基本遇不到，大部分都是类型体操中使用

![[00 assets/0979f8eab89434c7fe8771d0c2179d7c_MD5.png]]

> 分发条件类型

![[00 assets/496dc4b0ee0665d87abdd351028f4981_MD5.png]]

# 4. this

## 4.1 基本使用

1、在默认情况下`this`的数据类型一般都是`any类型`

![[00 assets/da5580d808dc773e73c618c6822578f7_MD5.png]]

2、当我们使用`tsc --init`来初始化`typescript`的时候，将`noImplicitThis`配置设置为`true`的话，`ts编辑器`就会详细的追问`this`的类型

![[00 assets/2b2a8bbc60ffaaddadfed3d7e7de4b7e_MD5.png]]

当不确定`this`的指向的时候就会报错，对于明确的`this`就会自动推导出类型

![[00 assets/09e72ad14da481042e52eb6da0d3309d_MD5.png]]

3、假如我们手动来指定`this`的话就需要在函数中第一个参数指定`this`

![[00 assets/1aa46fc1c14d804e1b6baa409d22b1e7_MD5.png]]

## 4.2 内置工具

> ThisParameterType

提取函数中`this`的类型

![[00 assets/2b2c906e70c285b211341db0a50ee186_MD5.png]]

> OmitThisParameter

剔除函数中`this`类型

![[00 assets/8d5ed5c81b17a2385889883d4ab8e3af_MD5.png]]

> ThisType

`ThisType`表示一个上下文中的`this`类型。其实本质就是修改`TS`认为的`this`的指向。比如下面的案例，`调用`的时候已经使用了`call`，但是`TS`还是认为是错的

![[00 assets/a12e99f414b461f54376bb1cdd8694d8_MD5.png]]

所以这个时候就可以使用`ThisType`来改变`TS`对`this`的认识，这样就不会报错。其实这个就是**pinia**中的实现

![[00 assets/ab6c8e648bfd254a105ad25750b2cb7f_MD5.png]]

# 5. 面向对象

## 10.1 基本使用

1、在原生的`JS`中是不需要写`成员属性`的，直接在`constructor`中编写`this.xxx = xxx`即可。但是在`TS`中需要单独写`成员属性`，不然会报错

![[00 assets/08ef0c46373d6041ae78f50cfc2194bd_MD5.png]]

2、使用语法糖来创建，这样会更加方便

![[00 assets/ca3482e6e853a0c7c5165ab386d5a599_MD5.png]]

3、`readonly`也可以对对象中的属性使用，表示只能读取，不能写入

![[00 assets/8496ecced9792e754b547787a54841ed_MD5.png]]

4、`类`可以创建对应的实例对象；`类`本身可以作为这个实例的类型；`类`也可以当作一个有`构造签名的函数`

![[00 assets/be7a8ca30769c1a6deed9cfbac7375ee_MD5.png]]

## 10.2 继承

1、我们使用`extends`来实现继承，其`继承`的特性和原生`JS`是一样的

![[00 assets/7ce6ff933779e792f648473596ec194f_MD5.png]]

2、我们`继承`了父类之后，必须要写调用父类的构造函数，不然会有问题，并且参数不能少

![[00 assets/21f319edb6a592fd627f047f6524f728_MD5.png]]

## 10.3 成员修饰符

![[00 assets/5877b1ac61f5f2796d755ebc947e4ebe_MD5.jpeg]]

![[00 assets/371d899465854b32243eae9cd46c9723_MD5.png]]

## 10.4 getter/setter

> Java 风格

![[00 assets/a775402d6f62bfdfe05c0b2f6dfef446_MD5.png]]

> C#风格

1、一般的情况下在`typescript`中使用`get/set`属性，就是使用的下面的方式来处理的

![[00 assets/b6bbc9e579e1f5640be34ee5528f1e90_MD5.png]]

2、假如存在继承的话，最好将`get/set属性`设置为`protected`修饰符

![[00 assets/d31eaa363e43b39facd022fe9bff8d12_MD5.png]]

3、我们使用`get/set修饰符`看你存在编译为`js`代码的时候报错的情况，这个时候我们指定`es版本`即可

![[00 assets/114a37c1fe556c52d6f012a808ffdb87_MD5.png]]

```bash
tsc index.ts -t es5 	// 编译为es5版本
tsc index.ts -t es6 	// 编译为es6版本
```

## 10.5 抽象类/多态

对于`抽象类`首先要理解`多态`的处理，先看下面的处理方式。我们每写一个`形状`就需要多写一个类型，这样非常麻烦，所以需要一个方式来解决这个问题

![[00 assets/fcfd8a60006b39c05aa5affe969339a5_MD5.jpeg]]

所以我们需要使用到`继承`来处理上面的问题，我们编写一个`shape`父类，作为下面子类集合的抽象。**我们调用的虽然是父类的方法，但是我们传入的是子类的对象，表现出来的也是子类行为**，即一个对象表现出来的不同的行为这个就是**多态**

![[00 assets/1f63507c7ba7e0215d22d650f770b81c_MD5.jpeg]]

但是作为一个父类我们并不需要调用它，而且方法也不需要实现，所以我们就需要使用`abstract`来表示一个抽象类，下面就是对`Shape`进行的抽象处理

![[00 assets/1527b7858c4971b08a9e66da4bf68637_MD5.png]]

## 10.6 索引签名

### 10.6.1 基本使用

1、对于`索引签名`来说，下面就是一个应用的场景。我们对于返回的值不知道是什么类型的，里面包含了什么属性，所以我们可以使用索引签名来进行描述

![[00 assets/650e600f1b15c9d944442bc687465f26_MD5.png]]

我们遍历数组也是一样，也是当作描述来处理的

![[00 assets/d0199b48209a883313b38f845d30d88b_MD5.png]]

2、`索引签名`中`[xxx]: yyy`的`xxx`只能是`string`和`number`类型

### 10.6.2 类型问题

当我们将索引签名改为`[index: string]: number`的时候就会报错，这个很好理解，因为我们取数组的时候一般都是`array[1]...`来取，不符合`索引签名`的标准

![[00 assets/f963ee9b89c5edd1b105554797303ffe_MD5.png]]

但是我们将后面改为`any`的时候就不会有这样的问题。

1、首先来说`string`的问题，在`JS`内部使用`array[1]`本身就会将索引转化为`string`，所以可以理解。

2、再来说`any`的事情，这是因为我们创建一个数组其实本质是创建一个数组对象，里面包含了很多的方法，我们使用`array.map(...)`来调用可以，还可以使用`array["map"]`来获取，所以需要使用`any`

但是这样理解的话上面的`对象的索引签名`就会有问题

![[00 assets/c0468ded5a9f8b7a3c1f61f7ac8a7788_MD5.png]]

假如还有问题的话可以参考文档：[TypeScript: Documentation - Object Types (typescriptlang.org)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures)

### 10.6.3 多个签名

![[00 assets/9014ddac7a4f30645c7a9c0a62f7f7fa_MD5.jpeg]]

> 要求 1

简单来说就是`number`要转化为`string`，所以需要`number`的范围窄一点，而`string`类型宽泛一点

![[00 assets/a7306f697f12e09805ffa7025618d39d_MD5.png]]

> 要求 2

在定义了`索引签名`的`接口`或者`type`中的其他属性，必须是`string索引`的子类

![[00 assets/8398bfae394906234f2dc8df2aa94e21_MD5.png]]

## 10.7 接口

### 10.7.1 基本使用

1、我们创建的接口，使用了`implements`继承了`Person`的话。就必须要实现里面的属性和方法

![[00 assets/64ac4f08818298f090cb19c886520323_MD5.png]]

一个类可以继承多个接口，这个就是和继承`类`的区别。我们使用`extends`继承类的时候只能继承一个，但是我们使用`implements`继承的话能继承多个

![[00 assets/9f251ad26956bd370bed176a9f978afd_MD5.png]]

2、我们在接口里面也可以继续使用**只读属性**

![[00 assets/1fcee0f430a30961686f3e1552913433_MD5.png]]

### 10.7.2 接口继承

```typescript
// 接口扩展接口
interface PointX {
    x: number
}

interface Point extends PointX {
    y: number
}

// 类型扩展类型
type PointX = {
    x: number
}

type Point = PointX & {
    y: number
}

// 接口扩展类型
type PointX = {
    x: number
}
interface Point extends PointX {
    y: number
}

// 类型扩展接口
interface PointX {
    x: number
}
type Point = PointX & {
    y: number
}
```

### 10.7.3 区别

![[00 assets/38c6791b19f736501eff7557bfcf13e3_MD5.jpeg]]

# 6. 泛型

## 6.1 基本介绍

![[00 assets/81df868947b6ce3153233e74868f1ef7_MD5.png]]

1、将`类型参数化`就是泛型，这样我们可以编写更加通用的接口

![[00 assets/7d249291adee0179818c1fd36c1e2c08_MD5.png]]

2、如果我们继承的是`interface`或者`type`的话，就必须是它的子类才可以

![[00 assets/78c7f6eef3144910960e87d8b0f1151e_MD5.png]]

## 6.2 泛型接口

我们可以给`接口`来定义`泛型`

![[00 assets/4e577e5ce85ee1e19e91db1689798d03_MD5.png]]

对于`泛型`我们也可以`赋默认值`

![[00 assets/50cd3a88fabe68978fc7ecdf9734df7a_MD5.png]]

## 6.3 泛型类

对于`类`，我们也可以使用`泛型`

![[00 assets/23fd4dd2349f2270f880fdfb51e12d94_MD5.jpeg]]

## 6.4 泛型约束

1、因为你输入的`arg`本身是`T`类型的，并不清楚是否包含了`size`属性，所以会报错

![[00 assets/00977e09e963732d0186b8a8a92e4689_MD5.png]]

所以就存在`泛型约束`来约束传入参数的类型，这样就约束为只有`size`的参数可以进入

![[00 assets/c11f8bed0b6a950ed2c65c105fc06936_MD5.png]]

2、还有一个作用就是清楚的知道返回的类型，按照下面的方式就会丢失原本的类型

![[00 assets/6e9c13ff5b10bf4f9844e78ef070c1ab_MD5.png]]

我们使用泛型的话就可以解决上面的问题

![[00 assets/729983fd095e6a97d5850f88c1e6d943_MD5.png]]

3、我们可以来看下面的这段代码，很明显是错误的，并不存在这种形式的获取方式

![[00 assets/fa41d39737fb59d1231518109232673f_MD5.png]]

假如我们使用`泛型参数 + 泛型约束`的话就不会存在这个问题，而且有更好的语法提示。其中`keyof`就是获取某种类型的所有`key`

![[00 assets/aeb4fa9d31c1139e25e53ce2e56ef576_MD5.png]]

## 6.5 映射类型

1、我们使用下面的方式来对一个类型进行拷贝

![[00 assets/de92f291394d68c0e5995212c55d7f2f_MD5.png]]

![[00 assets/1e130de0f8eba37c08c1ea7c7b9fa651_MD5.png]]

2、我们可以给映射类型添加修饰符

![[00 assets/5431f52d46e54a40e8e0cc28b1adecea_MD5.png]]

![[00 assets/9988507ac474a0bfdf7e20771cc84228_MD5.png]]

# 7. 额外知识

## 6.1 鸭子类型

`Typescript`对于类型检测的时候使用的**鸭子类型**，`鸭子类型`是指：如果一只鸟，走起来像鸭子游起来像鸭子，看起来像鸭子，那么你可以认为它就是一只鸭子。所以最后表达的意思：**只关心属性和行为，不关心你具体是不是对应的类型**

其实`JavaScript`本身就是一个鸭子类型，比如：`JavaScript高级 迭代器实现`中的`[Symbol.iterator]`的表现。比如说：下面的 2 个传入的对象最后就没有报错

![[00 assets/825e79abc484298097030740ce16be71_MD5.png]]

## 6.2 严格字面量赋值检测

1、假如我们对`对象`字面量赋值，必须要严格遵守`自己定义的类型`

![[00 assets/68f829bec7f1eb93cb0fcd42df4b80f7_MD5.png]]

下面也是和上面一样的

![[00 assets/57dda011d0721c493352fcbdd437a656_MD5.png]]

2、下面就是对于上面问题的解释，其实我们一开始定义的时候是`fresh`，会做严格的类型检测。假如你后续再使用的话就不会做这种严格的类型检测了

![[00 assets/0ef6569e565a3d2d4160c48fb2101b5f_MD5.png]]

# 9. 模块化

## 9.1 基本介绍

![[00 assets/cfc15599e47008ebde4c510f590e2314_MD5.png]]

## 9.2 与 JS 得差异

### 9.2.1 非模块化

如果添加了`export { }`得话，那么就认为这个`.ts`文件就是一个模块。就不会去影响其他得`.ts`文件得命名

![[00 assets/cb49933eaf66ae58e40ddecf0519575a_MD5.png]]

### 9.2.2 内置类型导入

![[00 assets/ed0069e1de7ce5be1f9404d1e7d3fb5c_MD5.png]]

我们按照下面得方式来对类型进行模块化处理

![[00 assets/cf2cf16ce45aa5d34c5a759f8afb9ef0_MD5.png]]

### 9.2.3 命名空间

![[00 assets/454bc26c8bb09775ba72a2058d5ceb21_MD5.png]]

# 10. 类型查找

## 10.1 基本介绍

![[00 assets/6dbca6c3c9d9f4532fd462d0fd7a1354_MD5.png]]

假如我们将原本的声明类型的文件改为`.d.ts`的话就不需要导出类型，会自动匹配

![[00 assets/5eaba4975a5c57f07673bda70654e0e2_MD5.png]]

## 10.2 内置类型

### 10.2.1 基本介绍

![[00 assets/0e04d9b7e584cc1a03d9c1292885f91b_MD5.png]]

我们在内置类型中使用`ctrl + 左键`即可进入到内置类型来查看，我们在全局安装`typescript`的时候也会一起下载下来

![[00 assets/78b8b47fc7594364d092eb9a7f249b89_MD5.png]]

如果需要查看`typescript`拥有得类型可以查看下面得`git仓库`[TypeScript/lib at main · microsoft/TypeScript (github.com)](https://github.com/microsoft/TypeScript/tree/main/lib)

### 10.2.2 内置环境

![[00 assets/3dad049f5985c4ed50d53c40f6e9e0c9_MD5.png]]

内置环境中的`tsconfig.json`中的`target`和`lib`就是配置环境的选项，用于设置内置环境的，但是这种配置方式基本不去配置，而是在框架中已经配置好了

![[00 assets/50c01f3858eecd652b8d14fab36533e9_MD5.png]]

## 10.3 外部定义

### 10.3.1 第三方库

![[00 assets/74a7a585c5a675a88617fde29fe51bf6_MD5.png]]

> 包本身包含类型声明文件

1、对于一些第三方库来说，是自己包含类型声明文件的，比如`axios`就包含，里面包含很多的类型声明

![[00 assets/50aad24ff5eac4a8b741b859ddaf7686_MD5.png]]

到时候我们导入的时候，直接使用即可，所以不需要我们去处理。必要的话也可以导入`axios`编写好的类型

![[00 assets/26029f9af734a98463cc5a9893a80fd9_MD5.png]]

> 在 DefinitelyTyped 库中下载

2、但是对于一些其他的库来说，就不存在这个文件，所以就需要去下载这个库的类型文件

![[00 assets/77f49868bb631586cd0052c08392a130_MD5.png]]

一般情况下是使用`npm i @types/xxx --save-dev`来下载`DefinitelyTyped库`中的类型声明文件。并且会存在在`node_modules/@types`中

![[00 assets/041a0f3784d9867fe6dd71e630322b95_MD5.png]]

> 自己手写声明

3、可能存在你使用的库根本就不存在类型声明文件，所以就需要自己手写声明

![[00 assets/b1d31d950b480d914438e28f31b4be01_MD5.png]]

我们自己创建一个`.d.ts`文件，其中`declare`表示声明，`"lodash"`表示为这个模块编写声明文件。并且这个文件里面只写声明，不写实现

![[00 assets/acf0aaa10e4335d0ee3277fc0098d083_MD5.png]]

### 10.3.2 自定义声明

对于自定义声明存在下面的一个使用场景，我们在`index.html`中编写`script`，并且在里面定义的变量。在使用`webpack`编译之后会引入`bundle.js`，所以按理说应该是不会报错的，但是在`index.ts`中报错了，所以为了避免这样的情况，就需要自定义声明

![[00 assets/8ccd34cc24f890da5ff24199abf199ce_MD5.jpeg]]

所以就需要使用`declare`来声明类型，这样就可以解决上面的问题。并且它可以声明`变量/函数/对象`

![[00 assets/cbda50c385bf291aba6303b915362375_MD5.png]]

## 10.4 declare

> 声明模块

![[00 assets/c563864f0d2d008af42b824a07eaf118_MD5.png]]

> 声明文件

![[00 assets/537b28af4915e7d8d146b05fee5c77eb_MD5.png]]

在开发中`Vue`中帮我们配置好了文件，但是对于其他的文件需要我们自己来引入，比如说图片。既然你不去声明的话就会报错

![[00 assets/2ac120d63aa54dc20c5618e5d3a1edc8_MD5.png]]

我们声明之后就不会存在引入图片报错

![[00 assets/2f7e7fdaab56b75d714f1d56e8e5c5b8_MD5.png]]

> 命名空间

1、对于我们使用`jquery`来说，它在`index.html`中引入。使用`webpack`打包之后是可以实现正常使用的，但是在目前项目的搭建阶段还是会报错

2、因为`jquery`并没有在`index.ts`文件中引入，所以在这样的情况下使用`命名空间`是最合适的

![[00 assets/a5c14a4e496a654c0a447f8692df726d_MD5.png]]

这样的话就不会报错

![[00 assets/91d47b9633ba28d7d1e8b528ccc05722_MD5.png]]

# 11. tsconfig

## 11.1 基本介绍

> 介绍

![[00 assets/4f0049e385a169e7ac96995a11ff7b72_MD5.png]]

> 配置

![[00 assets/e5747be608aa24e15e62d6d1eca23af0_MD5.png]]

> 顶层设计

![[00 assets/d09a3df17247ce245e5ec1e3752b947b_MD5.png]]

## 11.2 compilerOptions

### 11.2.1 全部选项

![[00 assets/0c97391aef8301c0b553703aa022f68b_MD5.png]]

![[00 assets/2ff6f411ccc7cf74e2bbd98edefa1dce_MD5.png]]

![[00 assets/577faa3a8bb8970e21ddefb7edfc9707_MD5.png]]

![[00 assets/3eb797d4f660b7ad7f1fdc620580be2c_MD5.png]]

![[00 assets/a94248077c645c5a45b1b79a7b19d0a8_MD5.png]]

![[00 assets/d58e9ef6e3357dd36ce2ebfe64a565cd_MD5.png]]

### 11.2.2 target

`targe`指定编译的版本，我们可以设置为 ES3 或者 ES6 的编译版本

```json
"compilerOptions": {
    "target":"ES6",
}
```

但是一般在脚手架中的`target`是使用的`exnext`，也就是跟随`ES`的版本来处理。这样会出现兼容问题，但是实际情况是使用`babel`来编译，所以这里写什么都可以

![[00 assets/2363d0b71017cb4a2dc96f96b5812cb0_MD5.png]]

### 11.2.3 module

`module`指定生成的代码的模块化，比如`Common.js`

```json
"compilerOptions": {
   "target": "ES6",
   "module": "exnext"
}
```

### 11.2.4 strict

`strict`表示开启`ts`的严格模式，`strict`为`true`的话四个选项`alwaysStrict`、`noImplicitAny`、`noImplicitThis`、`strictNullChecks`都为`true`

```json
"compilerOptions": {
    "stric": true
}
```

> noEmitOnError

`noEmitOnError`表示当你错误的时候就不去编译生成文件

```json
"compilerOptions": {
   "noEmitOnError": true
}
```

> noImplicitAny

`noImplicitAny`表示不允许隐式 any 的存在，也就是推断为`any`，下面就隐式 any 的一个方式

![[00 assets/a55c56e6bc7f279778931cabfad8e095_MD5.png]]

```json
"compilerOptions": {
   "noImplicitAny": true
}
```

> noImplicitThis

`noImplicitThis`不允许不明确类型的 this

```json
"compilerOptions": {
    "noImplicitThis": true
  }
```

> strictNullChecks

`strictNullChecks`严格检查空值，假如是空值的话就会有问题，比如说下面的这个情况，假如没获得到 DOM 的话就是空值，是空值的话就会报错

![[00 assets/ec8c314394e67ce38d1a3e9d2be6d273_MD5.png]]

```json
"compilerOptions": {
   "strictNullChecks": false
}
```

### 11.2.5 alwaysStrict

开启严格模式，假如文件里面存在`import`或者`export`的话也会默认开启严格模式

```json
"compilerOptions": {
   "alwaysStrict": true
}
```

当然我们也可以手动在 js 文件里面使用严格模式

![[00 assets/b26573adcf364ed4eef99dee47b2f05f_MD5.png]]

### 11.2.6 allowJs

`allowJs`是否允许对 js 文件进行编译

```json
"compilerOptions": {
    "allowJs": false,
}
```

### 11.2.8 importHelpers

会引入`ts`中的`tslib`，也就是`polyfill`工具模块，在一开始的版本每个文件都会默认引入，但是这样的话会导致包的体积变大，所以你可以设置`importHelpers`来关闭引入

![[00 assets/3c9b6db4ed6fdb484029d381518bd04d_MD5.png]]

### 11.2.9 moduleResolution

表示模块的查找规则，一般情况是使用`node`

![[00 assets/c32cdd15d2b87c76971de4ce29ff9701_MD5.png]]

### 11.2.11 rmoveComments

是否移除注释，true 的话就是移除注释，false 就是不移除注释

```json
"compilerOptions": {
    "removeComments": false,
  }
```

### 11.2.10 lib

`lib`指定这个项目要使用库，一般情况是不修改这个的

```json
"compilerOptions": {
   "target": "ES6",
   "module": "ES6",
   "lib": ["DOM"]
}
```

### 11.2.7 jsx

其中`ts`也可以对`jsx`的语法进行转化，比如写`<div></div>`会转化为`React.createElement("div",{})`，假如你使用`preserve`的话就表示保留，在框架中就会交给`babel`来处理

![[00 assets/cb1bc3a5d9db0b0f3d38fbbc43060786_MD5.png]]

# 12. 内置工具

## 12.1 Partial

![[00 assets/bab1627b05b9c3d34513b7b1191ee928_MD5.jpeg]]

## 12.2 Required

![[00 assets/61882c8148fc10e71236efacf7601fb9_MD5.png]]

## 12.3 Readonly

![[00 assets/c3246de9046e9952d7b8c722cb10a40d_MD5.png]]

## 12.4 Record

![[00 assets/07ab09bc7ed232cbed2836d24cf57a70_MD5.png]]

1、对于下面的封装中`MyRecord<K extends keyof any>`中为什么要添加一个`extends keyof any`？因为我们无法确定你传入的类型是否为可遍历的，如果你传入`Boolean`那就是不能遍历，所以就会报错。

2、所以我们使用`keyof any`的话就默认是`number | string | symbol`的联合类型

![[00 assets/3adbe852c46f61359efa8cd6bd86b241_MD5.png]]

## 12.5 Pick

![[00 assets/9464373fded2358375b2cc5897b5f1dd_MD5.png]]

![[00 assets/b0e3e80d60ed0fb7cadae70d79bd0d2e_MD5.png]]

## 12.6 Omit

![[00 assets/a532cd8bf1bc257d2412a08550a51533_MD5.png]]

## 12.7 Exclude

![[00 assets/667536e5947642e42ba603d2678f4310_MD5.png]]

![[00 assets/a50c7ca2cd7cf702b4f1872c07630195_MD5.png]]

## 12.8 Extract

和`Exclude`是相反的，这个是提取里面的类型

![[00 assets/9317d56710cb1426977729298b22d927_MD5.png]]

## 12.9 NonNullable

![[00 assets/2f2c219686dbdd72aa7a93cf9c135ba9_MD5.png]]

## 12.10 ReturnType

![[00 assets/e3d97c86fca7e415cda379510cbff239_MD5.png]]

## 12.11 InstanceType

![[00 assets/1e1cf9e81aa367cc91819668b06c72cc_MD5.png]]

`InstanceType`的内置工具的实现

![[00 assets/18196453eba48c1576592227a011bb2b_MD5.png]]

## 12.12 Parameters

可以取出函数的参数

![[00 assets/c795e5bccf1988e969276676c574c2c3_MD5.png]]

# 12. axios 封装

额外文章参考：[在项目中用 ts 封装 axios，一次封装整个团队受益 😁 - 掘金 (juejin.cn)](https://juejin.cn/post/7071518211392405541#heading-11)

> 请求

![[00 assets/cde728c6d3f2993520984403c64ce3c1_MD5.png]]

```typescript
import axios from "axios";
import type { AxiosInstance } from "axios";
import type { HYRequestConfig } from "./type";

class encapsulationAxios {
  instance: AxiosInstance;

  constructor(config: HYRequestConfig) {
    this.instance = axios.create(config);

    // 全局请求/响应拦截器
    this.instance.interceptors.request.use(
      (config) => {
        console.log("全局请求");
        return config;
      },
      (err) => {
        console.log("全局请求");
        return err;
      }
    );
    this.instance.interceptors.response.use(
      (res) => {
        console.log("全局响应");
        return res.data;
      },
      (err) => {
        console.log("全局响应");
        return err;
      }
    );

    // 局部请求拦截器:一些接口存在自己特殊性的拦截器，比如：token
    this.instance.interceptors.request.use(
      config.interceptors?.requestSuccessFn,
      config.interceptors?.requestFailureFn
    );
    this.instance.interceptors.response.use(
      config.interceptors?.responseSuccessFn,
      config.interceptors?.responseFailureFn
    );
  }
  request<T = any>(config: HYRequestConfig<T>) {
    // 各个请求进行拦截
    if (config.interceptors?.requestSuccessFn) {
      // 不能在this.instance中加入拦截器，这样每条请求都会执行这个拦截器
      config = config.interceptors.requestSuccessFn(config);
    }

    return new Promise<T>((resolve, reject) => {
      this.instance.request<any, T>(config).then(
        (res) => {
          if (config.interceptors?.responseSuccessFn) {
            res = config.interceptors.responseSuccessFn(res);
          }
          resolve(res);
        },
        (rej) => {
          reject(rej);
        }
      );
    });
  }
  get<T = any>(config: HYRequestConfig<T>) {
    return this.request({ ...config, method: "GET" });
  }
  post<T = any>(config: HYRequestConfig<T>) {
    return this.request({ ...config, method: "POST" });
  }
  delete<T = any>(config: HYRequestConfig<T>) {
    return this.request({ ...config, method: "DELETE" });
  }
  patch<T = any>(config: HYRequestConfig<T>) {
    return this.request({ ...config, method: "PATCH" });
  }
}

export default encapsulationAxios;
```

> 类型

![[00 assets/e38a10d1e822960699bcbc6e032599f9_MD5.png]]

```typescript
import type {
  AxiosResponse,
  InternalAxiosRequestConfig,
  AxiosRequestConfig,
} from "axios";

// 针对AxiosRequestConfig配置进行扩展
export interface HYInterceptors<T = AxiosResponse> {
  requestSuccessFn?: (
    config: InternalAxiosRequestConfig | AxiosRequestConfig
  ) => any;
  requestFailureFn?: (err: any) => any;
  responseSuccessFn?: (res: T) => T;
  responseFailureFn?: (err: any) => any;
}

export interface HYRequestConfig<T = AxiosResponse> extends AxiosRequestConfig {
  interceptors?: HYInterceptors<T>;
}
```

> 发送请求

![[00 assets/6e4b1504fc99c15997d1388292011bc7_MD5.png]]

```typescript
import encapsulationAxios from "./request";

const BASE_URL = "http://123.207.32.32:8000";
const TIMEOUT = 10000;

const re = new encapsulationAxios({
  baseURL: BASE_URL,
  timeout: TIMEOUT,
  interceptors: {
    requestSuccessFn(config) {
      console.log("局部请求~");
      return config;
    },
    responseSuccessFn(res) {
      console.log("局部响应~");
      return res;
    },
  },
});

type homeMulidata = {
  banner: any;
  dKeyword: any;
  keywords: any;
  recommend: any;
};

re.request<homeMulidata>({
  url: "/home/multidata",
  interceptors: {
    requestSuccessFn(config) {
      console.log("单个请求的拦截器~");
      return config;
    },
    responseSuccessFn(res) {
      console.log("单个响应的拦截器~");
      return res;
    },
  },
}).then((res) => {
  console.log(res.banner);
});
```

# 13. 练习题

1、类型体操（推荐）：[type-challenges/README.zh-CN.md at main · type-challenges/type-challenges (github.com)](https://github.com/type-challenges/type-challenges/blob/main/README.zh-CN.md)

2、类型解答（推荐）：[Type Challenges Solutions (ghaiklor.github.io)](https://ghaiklor.github.io/type-challenges-solutions/zh/)

3、类型体操：[Issues · semlinker/awesome-typescript (github.com)](https://github.com/semlinker/awesome-typescript/issues)

# 额外

## 7. 绕开额外的检查

### 7.1 鸭式辨型法

上面代码，在参数里写对象就相当于是直接给`labeledObj`赋值，这个对象有严格的类型定义，所以不能多参或少参。而当你在外面将该对象用另一个变量`myObj`接收，`myObj`不会经过额外属性检查，但会根据类型推论为`let myObj: { size: number; label: string } = { size: 10, label: "Size 10 Object" };`，然后将这个`myObj`再赋值给`labeledObj`，此时根据类型的兼容性，两种类型对象，参照**鸭式辨型法**，因为都具有`label`属性，所以被认定为两个相同，故而可以用此法来绕开多余的类型检查。

```typescript
interface LabeledValue {
  label: string;
}
function printLabel(labeledObj: LabeledValue) {
  console.log(labeledObj.label);
}
let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj); // OK



// 这个就不行
interface LabeledValue {
  label: string;
}
function printLabel(labeledObj: LabeledValue) {
  console.log(labeledObj.label);
}
printLabel({ size: 10, label: "Size 10 Object" }); // Error
```

### 7.2 类型断言

告诉检查器它知道，所以这个时候就可以直接绕过了

```typescript
interface Props {
   name: string;
   age: number;
   money?: number;
 }

 let p: Props = {
   name: "兔神",
   age: 25,
   money: -100000,
   girl: false
 } as Props; // OK
```

### 7.3 索引签名

```typescript
interface Props {
  name: string;
  age: number;
  money?: number;
  [key: string]: any;
}


let p: Props = {
  name: "兔神",
  age: 25,
  money: -100000,
  girl: false
}; // OK
```

## 8. 编译选项

### 8.1 自动编译

> 自动编译单个文件

```bash
tsc xxx.ts -w
```

> 自动编译所有文件

使用这个方式的前提是你添加了 tsconfig.json 文件

```bash
tsc -init	//初始化，即添加tsconfig.json
tsc			//编译所有文件
tsc -w 		//自动编译所有文件
```

## 8.2 指定编译文件

tsconfig.json 是 ts 编辑器的配置文件，ts 编辑器可以根据它的信息来对代码进行编译

```json
//一般是下面的格式来书写
{
  "include": ["./src/*", "./src1/**/*"]
}
```

### 8.2.1 include

不是我们可以一键编译所有 ts 文件吗？所以这个就是用来指定那些 ts 文件需要被编译

```json
//其中**表示任意目录，*表示任意文件
"include": ["./src/**/*", "./include/**/*"]
```

### 8.2.2 exclude

这个和 include 正好相反，就是排除目录的文件

```json
//这个路径的所有文件都不编译
"include": ["./src/**/*", "./include/**/*"]
```

### 8.2.3 extends

用来继承 tsconfig.json 文件

```json
"extends": "./config/1.json"
```

### 8.2.4 files

指定被编译的文件

```json
"files": [
	"1.ts",
    "2.ts"
]
```

## 9. webpack 打包 ts

建议去看我的 webpack 的笔记，基本就是 webpack 的基本使用方式

唯一需要我们知道的就是 ts 的使用

> 安装

```
cnpm i ts-loader -save
```

> 使用

使用 ts-loader

![[00 assets/8fe7036b516431de2f429c734e28f724_MD5.png]]

我们使用`resolve`属性里面的`extensions`，这样配置的话，我们使用 import 就不用书写后缀扩展名了

![[00 assets/64b7eedb27024eec87869b72494aabae_MD5.png]]

老师课比较有意思，可以去看看原课程

### 11. 提高编写效率

### 11.1 减少重复代码

```typescript
//这里就写了很多的重复代码
interface Person {
  firstName: string;
  lastName: string;
}

interface PersonWithBirthDate {
  firstName: string;
  lastName: string;
  birth: Date;
}

1.
//使用extends
interface Person {
  firstName: string;
  lastName: string;
}

interface PersonWithBirthDate extends Person {
  birth: Date;
}


2.
//使用&
type PersonWithBirthDate = Person & { birth: Date };
```

有时候你可能还会发现自己想要定义一个类型来匹配一个初始配置对象的「形状」

```typescript
const INIT_OPTIONS = {
  width: 640,
  height: 480,
  color: "#00FF00",
  label: "VGA",
};

interface Options {
  width: number;
  height: number;
  color: string;
  label: string;
}

1.
//使用typeof
type Options = typeof INIT_OPTIONS;
```

在实际的开发过程中，重复的类型并不总是那么容易被发现。有时它们会被语法所掩盖。比如有多个函数拥有相同的类型签名：

```typescript
function get(url: string, opts: Options): Promise<Response> { /* ... */ } 
function post(url: string, opts: Options): Promise<Response> { /* ... */ }


1.
//优化建议
type HTTPFunction = (url: string, opts: Options) => Promise<Response>; 
const get: HTTPFunction = (url, opts) => { /* ... */ };
const post: HTTPFunction = (url, opts) => { /* ... */ };
```

### 11.2 用精确的类型替代字符串类型

```typescript
//原本
interface Album {
  artist: string; // 艺术家
  title: string; // 专辑标题
  releaseDate: string; // 发行日期：YYYY-MM-DD
  recordingType: string; // 录制类型："live" 或 "studio"
}

interface Album {
  artist: string; // 艺术家
  title: string; // 专辑标题
  releaseDate: string; // 发行日期：YYYY-MM-DD
  recordingType: string; // 录制类型："live" 或 "studio"
}



//改进
interface Album {\
  artist: string; // 艺术家
  title: string; // 专辑标题
  releaseDate: Date; // 发行日期：YYYY-MM-DD
  recordingType: "studio" | "live"; // 录制类型："live" 或 "studio"
}

const dangerous: Album = {
  artist: "Michael Jackson",
  title: "Dangerous",
  releaseDate: new Date("1991-11-31"),
  recordingType: "studio",
};
```

### 11.3 定义的类型总是表示有效的状态

原文章：[2021 typescript 史上最强学习入门文章(2w 字) - 掘金 (juejin.cn)](https://juejin.cn/post/7018805943710253086#heading-124)

## 10.6.3 泛型工具

原文章：[2021 typescript 史上最强学习入门文章(2w 字) - 掘金 (juejin.cn)](https://juejin.cn/post/7018805943710253086#heading-75)

### 10.6.3.1 typeof

typeof 的主要用途是在类型上下文中获取变量或者属性的类型

```typescript
1.
interface Person {
  name: string;
  age: number;
}
const sem: Person = { name: "semlinker", age: 30 };
type Sem = typeof sem; // type Sem = Person


2.
const Message = {
    name: "jimmy",
    age: 18,
    address: {
      province: '四川',
      city: '成都'
    }
}
type message = typeof Message;
/*
 type message = {
    name: string;
    age: number;
    address: {
        province: string;
        city: string;
    };
}
*/


3.
function toArray(x: number): Array<number> {
  return [x];
}
type Func = typeof toArray; // -> (x: number) => number[]
```

### 10.6.3.2 keyof

`keyof` 操作符是在 TypeScript 2.1 版本引入的，该操作符可以用于获取某种类型的所有键，其返回类型是联合类型。

```typescript
interface Person {
  name: string;
  age: number;
}

type K1 = keyof Person; // "name" | "age"
type K2 = keyof Person[]; // "length" | "toString" | "pop" | "push" | "concat" | "join"
type K3 = keyof { [x: string]: Person };  // string | number
```

![[00 assets/e3d3080adb80c6a9fe2e3f1f8ce37e2e_MD5.png]]

下面是 keyof 真正的使用方式

我们这样使用 prop 函数其实是有问题的，

![[00 assets/2e031ac945e4ff97995010109ca6a024_MD5.png]]

我们可以使用下面的方式来进行解决，但是并不是一个很好的方式

![[00 assets/e2e15a071ef4f2e29a6a01e5c5b595f9_MD5.png]]

![[00 assets/60b811fe286565fff9cb095812852e80_MD5.png]]

![[00 assets/adddfb86f299ad97e67ff07112023c6f_MD5.png]]

### 10.6.3.3 Pick

Pick 从某个类型中挑出一些属性出来

```typescript
interface Todo {
  title: string;
  description: string;
  completed: boolean;
}

type TodoPreview = Pick<Todo, "title" | "completed">;

const todo: TodoPreview = {
  title: "Clean room",
  completed: false,
};
```
