视频讲解：[【尚硅谷】JavaScript 基础&实战丨 JS 入门到精通全套完整版\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1YW411T7GX?from=search&seid=14804065034274264200)

视频讲解：[JavaScript 基础语法-dom-bom-js-es6 新语法-jQuery-数据可视化 echarts 黑马 pink 老师前端入门基础视频教程(500 多集)持续\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Sy4y1C7ha?p=216&spm_id_from=pageDriver)

视频讲解：coderwhy 前端系统课 - JavaScript 基础课

# 1. 基本介绍

## 1.1 发展历史

> 计算机语言

![[00 assets/0bfea36f3437e9a7958d2cdf739c410e_MD5.png]]

> 编程语言

![[00 assets/c2a0975226300642a666175baf155e4e_MD5.png]]

> 常见的编程语言

![[00 assets/8b1fdf113fdb11046718d6ff7f652139_MD5.png]]

> 机器语言

![[00 assets/d9c32059c78849f0c6429176717513ae_MD5.png]]

> 汇编语言

![[00 assets/d38a6986723e486c869b4846834c2361_MD5.png]]

> 高级语言

![[00 assets/1d477d501905ebc53579bb7a2789e85d_MD5.png]]
![[00 assets/0de5f81071242534b12e3920a43d4a03_MD5.jpeg]]


## 1.2 基本介绍

![[00 assets/511068c9b4371b0448ca882bbba9159e_MD5.jpeg]]

## 1.3 JavaScript 历史

![[00 assets/9086cb82093772ea4dba1e402e268ed4_MD5.png]]

![[00 assets/0cfe558d3a980ff8b373b49f24387a78_MD5.png]]
![[00 assets/d11626723524f13b28dd8574d6df5602_MD5.jpeg]]

![[00 assets/ff925e3e760e0266b8dcb0a14017aab0_MD5.png]]

## 1.4 JavaScript 组成

![[00 assets/92944f53340f331a5cc17b608e20913b_MD5.png]]

## 1.5 JavaScript 运行

![[00 assets/60163df32382a9e2526106b60a083323_MD5.jpeg]]

![[00 assets/7336db4d2f2c38a5ee8266f1c1a764f5_MD5.png]]

![[00 assets/cdb0edeafd93cb4487951d4691613803_MD5.png]]

# 2. 基本概念

## 2.1 编写位置

对于编写的位置存在下面的`3`种方式，和`CSS`是的引入方式是一一对应的。但是最后还是比较推荐使用`外部script`来引入

![[00 assets/5b3f8edb51432838f7c5fa44dfb3c539_MD5.png]]

对于`script`存在下面的几个`注意事项`

![[00 assets/c696ee852f85e7dd87b3f8e8e1b1ea82_MD5.png]]

## 2.2 noscript

对于不支持`JavaScript`的浏览器，我们最好的方式就是使用`noscript`来包裹处理，提示相应文字

![[00 assets/44d600d92d4b2a807a4640cdcc4dc455_MD5.png]]

## 2.3 交互方式

![[00 assets/667c070cfd4bf50056009c07f07160f4_MD5.jpeg]]

> alert()

`alert()`浏览器窗口中弹出一个提示框

![[00 assets/0bdd57f3141e7f6dcc051d10bfec0d21_MD5.png]]

> document.write()

`document.write()`会内容将会被写到`body`标签中，并在页面中显示

![[00 assets/6aeeebfb64cbe2ea4bcc20367297d77f_MD5.png]]

> console.log()

`console.log()`会将内容写到开发者工具的控制台中

![[00 assets/16602be8333f62275ca30a91189b59f9_MD5.jpeg]]

> prompt()

`prompt()`会接受你传入的数据。并且默认输入的字符都是`string类型`的，不管你输入的是什么，即便是`null`也会是`"null"`

![[00 assets/c7a43d7ffed228305598e9e56aa5198a_MD5.png]]

> confirm()

`confirm()`会给你一个选择，返回布尔值

![[00 assets/ac588f045380294c44bf58275301929e_MD5.jpeg]]

## 2.4 代码注释

![[00 assets/6edae4abe14948125622864d9cd8feb4_MD5.png]]

编写文档注释的时候使用`/**`就会生成`文档注释`

1、`第一行`是这个函数的描述

2、`@param`是函数参数，`{ }`是返回值，`name`是参数名，接着的是参数描述。

3、`@returns`是返回值的描述

![[00 assets/b86118f413bf0c0bb320e335f06760df_MD5.png]]

# 3. 变量

# 4. 运算符

## 4.1 基本介绍

> 运算符

![[00 assets/a967eb1b566508a56c64eacec13856be_MD5.png]]

> 运算元

![[00 assets/3db9c0d7dae93bf766716e12c61d64e8_MD5.jpeg]]

## 4.2 算术运算符

![[00 assets/f8e2cf2fa2411a641b383ac7ac11bfbe_MD5.png]]

![[00 assets/811bc48d0846aaaf80e31a4a833fa700_MD5.png]]

![[00 assets/eb20223faec9f7053d24f65f27a3b9e1_MD5.jpeg]]

## 4.3 赋值运算符

![[00 assets/c7482f44f1fe7f984bac7f1755998896_MD5.png]]

![[00 assets/5e60ca9ea84c3c09bef21425195708b4_MD5.jpeg]]

![[00 assets/c42e10512102de751cbb18f51cb8d285_MD5.png]]

## 4.4 比较运算符

![[00 assets/2344e557d13c1cae187c0387988dc707_MD5.png]]

![[00 assets/8c55882bdff3117c2a1117bbba936608_MD5.jpeg]]

## 4.5 条件运算符

![[00 assets/b73f6eec6e923e8fb2c8d645b5a2fb16_MD5.png]]

## 4.6 逻辑运算符

![[00 assets/0e2544783ffacd4231c3f4c895a5bc4d_MD5.jpeg]]

> ||

![[00 assets/0a0136f693536de13339ad4dab8b78e8_MD5.png]]

> &&

![[00 assets/14dbe623d20711d15077b2874a9d4db3_MD5.png]]

> !

![[00 assets/e156dddff6c3f94bcd96e7b6e9f3a861_MD5.png]]

## 4.7 运算优先级

![[00 assets/c24428d1b631df82dcb5eb894e7c2f54_MD5.png]]

# 5. 流程控制

## 5.1 基本介绍

![[00 assets/f2ed6054bfd88d2affd89639d64395e9_MD5.png]]

## 5.2 if

> 单分支语句 if

![[00 assets/aa26deab496a056a96b3121d81bfa9cd_MD5.png]]

> 多分支语句 if...else...

![[00 assets/4750bcad48ae256fe8a41b06441d8d5a_MD5.png]]

> 多分支语句 if...else if ...

![[00 assets/b6d94c1f160d64c2c05423269e115224_MD5.png]]

## 5.3 switch

![[00 assets/4d9f43d59bc9e5ec05218797b64865a8_MD5.png]]

![[00 assets/9c67761687f2f865244096375bc8c6b9_MD5.png]]

## 5.4 while

## 6.2 条件分支语句

### 6.3 循环语句

通过循环语句可以反复执行某些语句多次

#### 6.3.1 while 循环

执行流程：
while 语句在执行时，会先对条件表达式进行求值判断，
如果判断结果为 false，则终止循环
如果判断结果为 true，则执行循环体
循环体执行完毕，继续对条件表达式进行求值判断，依此类推

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var a=0;
			while(a<10){
				a++
				document.write(" "+a);
			}

		</script>
	</head>
	<body>
	</body>
</html>

```

#### 6.3.2 do...while 循环

执行流程
do...while 在执行时，会先执行 do 后的循环体，然后在对条件表达式进行判断，
如果判断判断结果为 false，则终止循环。
如果判断结果为 true，则继续执行循环体，依此类推

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var a=0;
			do{
				a++
				document.write(" "+a);
			}while(a<10)

		</script>
	</head>
	<body>
	</body>
</html>

```

do...while 和 while 的区别：

while：先判断后执行

do...while: 先执行后判断

do...while 可以确保循环体至少执行一次。

#### 6.3.3 for 循环

执行流程：
首先执行 ① 初始化表达式，初始化一个变量，
然后对 ② 条件表达式进行求值判断，如果为 false 则终止循环
如果判断结果为 true，则执行 ③ 循环体
循环体执行完毕，执行 ④ 更新表达式，对变量进行更新。
更新表达式执行完毕重复 ②

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			for(var a =0;a<10;a++){
				document.write(" "+a);
			}

		</script>
	</head>
	<body>
	</body>
</html>

```

#### 6.3.4 死循环

while(true){

}

for(;;){

}

### 6.4 break

可以推出 switch 和循环

### 6.5 continue

结束这一次循环，执行下一次循环

# JavaScript 基础

## 3. Script

### 3.2 async、defer、sync

async 和 sync 分别是异步和同步执行，具体的异步和同步参考后面的文档

下面的加上 async 的作用是异步执行，你看不仅在请求 JS，还在渲染 HTML 页面

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="3.js" type="text/javascript" async="async"></script>
	</head>
	<body>
		<p>Hello Warld!</p>
	</body>
</html>

```

![[00 assets/16b5b9d02f01f144f1a37b41c1e00911_MD5.jpeg]]

我们再来看 sync 的同步请求，是不是就和上面的 async 就有区别了，他是从上到下依次执行的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="3.js" type="text/javascript" sync="sync"></script>
	</head>
	<body>
		<p>Hello Warld!</p>
	</body>
</html>

```

![[00 assets/fab647d2d571eedff98e88ec82598fb5_MD5.jpeg]]

defer 的表现和 async 是基本一样的，defer 属性只有 IE 支持

### 5.5 运算符

运算符也称为操作符，并且可以通过运算符可以对一个或多个值进行运算或操作

#### 5.5.6 Unicode 编码

在 JavaScript 里面是支持十六进制的，但是在我们的 HTML 里面是不支持的，所以我们需要将十六进制转换为十进制，然后才可以运行

下面的 JavaScript 和 css 都可以使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log("\u2620");
		</script>
	</head>
	<body>
		<p style="font-size: 200px;">&#9760</p>
	</body>
</html>

```

![[00 assets/fcd83602c8a772e7841512763c882063_MD5.png]]

## 7. 数组

数组也是一个对象，是一个用来存储数据的对象，和 Object 类似，但是它的存储效率比普通对象要高，在开发中我们经常使用数组来存储数据

数组中保存的内容我们称为元素，数组使用索引（index）来操作元素，索引指由 0 开始的整数

### 7.1 创建、使用数组

**一维数组**

下面是基础的创建数组

```html
<script type="text/javascript">
	var arr = new Array();
	arr[0] = 111;
	arr[1] = 222;
</script>
```

我们也可以使用下面的方式来创建数组

```html
<script type="text/javascript">
    var arr = new Array(1,2,3,4,5,6);
</script>
```

**二维数组**

```
var att = [[],[]];
```

### 7.2 获取数组的长度

下面是获取数组的长度，但是前提是连续的数组，假如下面的例子加一个 a[10]的话，那么输出的长度就是 11，中间多出来的数组就会空出来

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = new Array();
			arr[0]=0;
			arr[1]=1;
			arr[2]=2;

			document.write(arr.length);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/7895208318d71e372074f0ce1be48a11_MD5.png]]

### 7.3 修改数组的长度

如果修改后的 length 大于原长度，则多出的部分会空出来，小于原长度，则原数组中多出的元素会被删除

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = new Array();
			arr.length = 5;
			arr[0]=1;
			arr[1]=2;
			document.write(arr);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/cb85544b42d7df0305607621310a3928_MD5.jpeg]]

假如我们向数组的最后添加元素，并且会扩大数组的长度

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = new Array();
			arr.length = 5;
			arr[0]=1;
			arr[1]=2;
			arr[2]=3;
			arr[3]=4;
			arr[4]=5;
			arr[arr.length]=6;
			document.write(arr);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/fc1d3ac1cfd1058a3a0f234fa75f10e7_MD5.png]]

### 7.4 使用字面量来创建数组

我们还可以使用字面量来创建数组，但是这个赋了初值的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = new Array();

			var sum = [1,2,3,4,5,6];

			document.write(sum[2]);
		</script>
	</head>
	<body>
	</body>
</html>
```

注意下面的写法，并不是只有一个数为 10，而是创建 10 个数据的数组

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = new Array(10);

			var sum = [10];

		</script>
	</head>
	<body>
	</body>
</html>
```

数组里面可以放置所有的数据类型，也可以放置对象

### 7.5 检测数组的两种方式

#### 7.5.1 instanceof

下面检测数组的方法

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [];
			console.log(arr instanceof Array);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/aadb972a2ecc00b341baf663624490d6_MD5.png]]

当然这个不止可以检测数组，还可以检测类

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function create(name,age,gender){
				this.name = name;
				this.age = age;
				this.gender = gender;
				this.sayName = function(){
					document.write(name);
				}
			}

			var obj = new create("张小虎",19,"男");

			console.log(obj instanceof create);
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/aadb972a2ecc00b341baf663624490d6_MD5.png]]

#### 7.5.2 Arreay.isArray()

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [];

			console.log(Array.isArray(arr));
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/aadb972a2ecc00b341baf663624490d6_MD5.png]]

### 7.5 数组的方法

#### 7.5.1 push()

![[00 assets/3c8b0ee3f128f33eeecceeee508c08e8_MD5.png]]

用来向数组的末尾添加一个或多个元素，并返回数组新的长度

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3];
			arr.push(4,5,6,7,8,9);

		</script>
	</head>
	<body>
	</body>
</html>

```

但是下面的这个方式也可以添加数值，并且扩大数组的长度，可能上面的方法是为了添加多个数值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3];
			arr[3]=4;
			document.write(arr[3]);
		</script>
	</head>
	<body>
	</body>
</html>

```

该方法会把新数组的长度作为返回值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3];

			document.write(arr.push(4,5,6));
		</script>
	</head>
	<body>
	</body>
</html>
```

#### 7.5.2 pop()

用来删除数组的最后一个元素，并返回被删除的元素

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3];
			arr.pop();
			document.writeln(arr);
			document.write(arr.pop());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/188cb1cfd741e789190f8ce19f7c3d3a_MD5.png]]

#### 7.5.3 unshift()

向数组的前边添加一个或多个元素，并返回数组的新的长度

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3];
			arr.unshift(0);
			document.writeln(arr);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/95a23955d758bfccbea0d17384a149e7_MD5.png]]

但是你传入的是一个数组的话就会形成一个二维数组

```javascript
let arr = [1,2,3];
let addArr = [4,5,6];
console.log(arr.unshift(addArr));
console.log(arr);
```

![[00 assets/f8b8d318baf27508219904eb20ff646a_MD5.png]]

#### 7.5.4 shift()

删除数组的前边的一个元素，并返回被删除的元素

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3];
			arr.shift();
			document.writeln(arr);
			document.write(arr.shift());
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 7.5.5 slice()

可以从一个数组中截取指定的元素,该方法不会影响原数组，而是将截取到的内容封装为一个新的数组并返回，第二个参数可以省略不写，如果不写则一直截取到最后

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ["张","王","郑","谢"];

			var result = arr.slice(0,2);

			document.write(result);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/4847b68e1f6f16ed3d5a3d63c9fe4b4d_MD5.png]]

参数可以传递一个负值，如果是负值，则从后往前数

#### 7.5.6 splice()

可以用来删除数组中指定元素，并使用新的元素替换，该方法会将删除的元素封装到新数组中返回

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ["张","王","郑","谢"];
			//第一个参数：从那个开始 第二个参数：删除几个
			arr.splice(0,2);

			document.write(arr);
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/de2327072a3e91e331be94007a07e788_MD5.jpeg]]

我们可以插入数据

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ["张","王","郑","谢"];

			arr.splice(0,1,"朱");

			document.write(arr);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/772639098dafff37dbe594e616c8cf20_MD5.png]]

#### 7.5.7 concat()

连接两个或者多个数组，并将新数组返回

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ["张","王","郑","谢"];
			var arr1 = ["牛","褚"];

			var result = arr.concat(arr1);

			document.write(result);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/7c7e82fa6fc9f233ff19b9e5e408cde0_MD5.png]]

#### 7.5.8 join()

该方法可以将数组转换为一个字符串，join()里面的值可以是填入分隔符

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ['a','b','c'];
			console.log(arr.join('-'));
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/9d736077581c2effe0165d970699f68b_MD5.jpeg]]

#### 7.5.9 reverse()

反转数组

#### 7.5.10 sort()

排序数组

```javascript
//假如你sort()没值的话，就按照首字母Unicode来排序
var arr = [10,9,111,2,90,89,91];
console.log(arr.sort());

//假如是第一个-第二个的话就是升序
var arr = [10,9,111,2,90,89,91];
console.log(arr.sort((a,b)=>{
	return a-b;
}));

//假如是第二个-第一个的话就是降序
var arr = [10,9,111,2,90,89,91];
console.log(arr.sort((a,b)=>{
	return b-a;
}));
```

#### 7.5.11 indexOf()

返回数组里面特定的索引号

但是这个只放回第一个满足的索引号，假如找不到元素的话，就返回-1

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3,4,5,6,7,8,9];
			console.log(arr.indexOf(5));
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/fd8fe65cb2cde8175e5e970001994809_MD5.png]]

#### 7.5.12 lastIndexOf()

他是倒着查找的，属性基本和上面的 indexOf 是差不多的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3,4,5,6,7,8,9];
			console.log(arr.lastIndexOf(6));
		</script>
	</head>
	<body>
	</body>
</html>

// 5
```


#### 7.5.13 filter

filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素

首先是数组的方法，用数组对象来引用，使用 filter 的方法，创建一个数组，再来执行里面的 checkAdult(ages)的方法，来排除 16，然后再输入到新创建的数组，不是输入到原本的 ages 数组

也就是为 true 的话就返回到 filter 创建的新数组里面

```javascript
var ages = [32, 33, 16, 40];
function checkAdult(age) {
	return age >= 18;
}
function myFunction() {
	console.log(ages.filter(checkAdult));
}
myFunction();

//当然也可以这样写

var ages = [32, 33, 16, 40];
function myFunction() {
	console.log(ages.filter(function checkAdult(age) {
		return age >= 18;
	}));
}
myFunction();
```

#### 7.5.14 map

#### 7.5.13 Array 案例

只要是 5 以下的就放到新数组里面

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3,4,5,6,7,8,9];
			var arr_new = [];

			for(var i=0;i<arr.length;i++){
				if(arr[i]<5)
					arr_new.push(arr[i]);
			}

			console.log(arr_new);
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/ab736c3973cd828a35b5db467d3d2c88_MD5.jpeg]]

数组去重

这里有一个很精妙的地方，就是关于 indexOf 这里，不用自己来写比对，可以直接使用方法来比较，然后返回的值比较就可以了

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ['a','c','a','d','g','d','g'];
			var arr_distinct = [];

			function distinct(){
				for(var i=0;i<arr.length;i++){
					if(arr_distinct.indexOf(arr[i]) === -1){
						arr_distinct.push(arr[i]);
					}
				}
				return arr_distinct;
			}
			console.log(distinct());
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/8031e46e8e3f23dd0fa2b8bc9572d831_MD5.png]]

### 7.6 遍历数组

#### 7.6.1 for

遍历数组就是将数组中元素都获取

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = [1,2,3,4,5,6];
			for(var i=0;i<arr.length;i++){
				document.write(arr[i]+" ");
			}
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/ddbf3b88ad3a2d7b10fa11dcb0a7248f_MD5.png]]

#### 7.6.2 forEach()

使用 forEach()方法来遍历数组（只支持 IE8 以上的浏览器，这个只不过是由我们创建，但是不由我们来调用，数组中由几次就执行几次，每次调用时，浏览器都会将遍历到的信息以实参的形式传递进来，我们可以定义形参来获取这些信息。

并且会传递三个参数 a:正在遍历的元素、b:index:正在遍历元素的索引、c:obj:被遍历对象

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = ["张","王","郑","谢"];

			arr.forEach(function(a,b,c){
				document.write("  "+a);
			});
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/7cf58fdf54a75e6b07c44505551d7fce_MD5.png]]

## 8. 函数

函数也是一个对象，也具有普通对象的功能

函数中可以封装一些代码，在需要的时候可以去调用函数来执行这些代码

使用 typeof 检查一个函数时会返回 function

### 8.1 创建函数和调用函数

这是一种函数的创建的方式

利用函数关键字自定义函数(命名函数)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(){
				console.log("王小胖");
			}

			fun();
		</script>
	</head>
	<body>
	</body>
</html>

```

这是另一种函数的创建方式

函数表达式(匿名函数)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var fun = function(){
				console.log("王小胖");
            };

			fun();
		</script>
	</head>
	<body>
	</body>
</html>
```

### 8.2 形参和实参

#### 8.2.1 形参

定义函数时，可以在()中定义一个或多个形参，形参之间使用,隔开
定义形参就相当于在函数内声明了对应的变量但是并不赋值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(a){
				console.log(a);
			}

			fun();
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/249c4253444f40811699db2bed5a9b0b_MD5.jpeg]]

形参会在调用时才赋值。

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(a,b){
				console.log(a+b);
			}
			fun(1,2);
		</script>
	</head>
	<body>
	</body>
</html>
```

对象也可以作为形参来使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(obj){
				console.log(obj.age);
				console.log(obj.name);
			}

			var obj = {
				name:"张小虎",
				age:18
			};

			fun(obj);
		</script>
	</head>
	<body>
	</body>
</html>

```

函数也可以作为形参来使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(obj){
				obj();
			}

			function obj(){
				console.log("嘤嘤嘤");
			}

			fun(obj);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/3fc4924919a111d7d8e5a6326bcd3317_MD5.png]]

我们来看下面的这个问题

我们可以总结一个问题

fun2()作为 fun1 的实参，是指的函数的返回值

fun2 作为 fun1 的实参，相当于直接使用的函数对象

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun1(b){
				console.log(b);
			}

			function fun2(sum){
				return sum;
			}

			fun1(fun2(10));
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 8.2.2 实际参数

调用函数时，可以在()传递实参，传递的实参会赋值给对应的形参,
调用函数时 JS 解析器不会检查实参的类型和个数，可以传递任意数据类型的值。
如果实参的数量大于形参，多余实参将不会赋值，
如果实参的数量小于形参，则没有对应实参的形参将会赋值 undefined

### 8.3 函数的返回值

返回值，就是函数执行的结果，使用 return 来设置函数的返回值。

return 后边的代码都不会执行，一旦执行到 return 语句时，函数将会立刻退出。

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(a,b){
				var c= a + b;
				return c;
			}
            var d = fun(1,1);
			console.log(d);
		</script>
	</head>
	<body>
	</body>
</html>

```

return 后可以跟任意类型的值，可以是基本数据类型，也可以是一个对象。

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(a,b){
				var obj = new Object();
				obj.name = "王小胖";
				return obj;
			}
			console.log(fun().name)
		</script>
	</head>
	<body>
	</body>
</html>

```

如果 return 后不跟值，或者是不写 return 则函数默认返回 undefined。

函数的返回值也可以是一个函数，但是这里还是有一个需要注意的那个点，函数名和函数名()的区别

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun1(){
				function fun2(){
					console.log("嘤嘤嘤");
				}
				return fun2();
			}
			fun1();
		</script>
	</head>
	<body>

	</body>
</html>
```

### 8.5 函数的方法

#### 8.5.1 call()和 apply()

当函数调用的时候，函数会执行，这种方式可以指定执行的对象

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(){
				document.write(this.name);
			}

			var obj = {name:"王"};
			var obj2 = {name:"张"};

			fun.apply(obj);
			fun.apply(obj2);
		</script>
	</head>
	<body>
	</body>
</html>
```

#### 8.5.2 arguments

在调用函数的时，每次都会传递两个隐含的参数，this 和封装实参的对象 arguments，只有函数才有 arguments 对象

它是一个类数组对象，它也可以通过索引来操作数组，也可以获取长度

在调用函数的时候，我们所传递的实参都会在其中保存

arguments.length 可以获取实参的长度

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(){
				document.write(arguments.length);
				document.write(arguments[0]);
			}
			fun("啊","英")
		</script>
	</head>
	<body>
	</body>
</html>

```

callee 可以查看当前的函数

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(){
				document.write(arguments.callee);
			}
			fun("啊","英")
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/e771915a775fa7943260be308ca016ba_MD5.png]]

当你不是很确定要输入这个函数的参数的个数，就可以使用 arguments

下面时一个小案例，任意数字求出最大的值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">

			var max = function(){
				var max = arguments[0];
				for(var i=1;i<arguments.length;i++){
					if(max < arguments[i]){
						max = arguments[i];
					}
				}
				return max;
			}
			console.log(max(9,6,4));
			console.log(max(10,2,3));

		</script>
	</head>
	<body>

	</body>
</html>

```

![[00 assets/bf1a3054c1741a486ecb06b3aa6710ea_MD5.jpeg]]

### 8.6 函数调用另一个函数

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function f1(){
				console.log("11");
				f2();
			}
			function f2(){
				console.log("22");
			}

			f1();
		</script>
	</head>
	<body>

	</body>
</html>

```

![[00 assets/e29be6fad1063c6033a9b2e376df2fe6_MD5.png]]

下面有一个案例的例子

这个是一个函数调用的例子，关于闰年时 2 月份的事情

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			// 判断是不是闰年
			function judge(year){
				var flag;
				if(year%4==0&&year%100!=0||year%400==0)
					flag=true;
				else
					flag=false;
				return flag;
			}
			//判断2月份
			function twoyear(){
				if(judge(2001))
					console.log("28天");
				else
					console.log("29天");
			}

			twoyear();
		</script>
	</head>
	<body>

	</body>
</html>

```

### 8.7 立即执行函数

主要的作用就是创建一个独立的作用域

```html
写法:(function(){})()		或者(function(){}())
```

下面就是立即执行函数的 2 种使用的方法，发现没有，这里的立即执行函数的步骤基本前面的调用是一致的，只不过是写法的问题

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<script type="text/javascript">
			function f1(){
				console.log("这不是立即执行函数");
			}
			f1();

			(function(){
				console.log("这就是立即执行函数");
			})()

			(function(){
				console.log("这就是立即执行函数的另一个执行的方式");
			}());
		</script>
	</body>
</html>

```

![[00 assets/0dbb37f5a8de4624d23b150aa63f99e2_MD5.png]]

但是发现，是不是后面有一个报错啊，这是因为，上面的执行函数后面没有写分号，导致的报错，假如我们去掉的话就不会报错了

当然后面的括号也可以作为调用函数来处理，可以往里面传递参数

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<script type="text/javascript">
			function f1(){
				console.log("这不是立即执行函数");
			}
			f1();

			(function(a,b){
				console.log(a + b);
			})(1,2);

			(function(a,b){
				console.log(a + b);
			}(1,2));
		</script>
	</body>
</html>

```

![[00 assets/a36cbf5c052c437c8859d28fa33be022_MD5.png]]

当然我们加上函数名也没有问题

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<script type="text/javascript">
			function f1(){
				console.log("这不是立即执行函数");
			}
			f1();

			(function f2(a,b){
				console.log(a + b);
			})(1,2);

			(function f3(a,b){
				console.log(a + b);
			}(1,2));
		</script>
	</body>
</html>

```

![[00 assets/a36cbf5c052c437c8859d28fa33be022_MD5.png]]

立即执行函数最大的作用就是**独立创建了一个作用域**，虽然名字一样的话，也是不影响的

## 9. 作用域

作用域简单来说就是一个变量的作用范围。

### 9.1 全局作用域

直接在 script 标签中编写的代码都运行在全局作用域中

全局作用域在打开页面时创建，在页面关闭时销毁。

全局作用域中有一个全局对象 window，window 对象由浏览器提供，可以在页面中直接使用，它代表的是整个的浏览器的窗口。

在全局作用域中创建的变量都会作为 window 对象的属性保存

在全局作用域中创建的函数都会作为 window 对象的方法保存

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var a = 10;
			console.log(window.a);
		</script>
	</head>
	<body>
	</body>
</html>

```

在全局作用域中创建的变量和函数可以在页面的任意位置访问。
在函数作用域中也可以访问到全局作用域的变量。

尽量不要在全局中创建变量

### 9.2 函数作用域

函数作用域是函数执行时创建的作用域

每次调用函数都会创建一个新的函数作用域。

函数作用域在函数执行时创建，在函数执行结束时销毁，在函数作用域中创建的变量，不能在全局中访问。

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function fun(){
				var a = 10;
			}
			console.log(a);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/8e1e8d750e495046a6cda6a3a4dc45a1_MD5.jpeg]]

### 9.3 块级作用域

假如是下面的程序，Java 里面是调用不了的

```java
if()
{
    int num = 100
}
```

但是现在 JS 是可以去调用的

### 9.4 全局变量

在全局作用下的变量

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
		<script type="application/javascript">
			var num = 10;
			function f1(){
				console.log(num);
			}
			console.log(num);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/492561de94d7acb1040e7496277aab79_MD5.png]]

### 9.5 局部变量

在局部作用域下的变量，也可以是在函数内部的变量

外部是不允许被使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
		<script type="application/javascript">
			function f1(){
				var num = 10;
				console.log(num);
			}
			console.log(num);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/dfa0a9aba5bc5e4154cfde0cf786dd6e_MD5.jpeg]]

还有一个变量虽然写在局部作用域里面，但是它是全局变量，可以参考变量的声明提前的例子

下面还有一个例子，就是局部变量的，形参也是局部变量

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
		<script type="application/javascript">
			function f1(num2){
				var num = 10;
				console.log(num);
			}
			console.log(num2);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/5f4e89a2bc2f09bf937963494cb298cf_MD5.png]]

这里是从**执行效率**来看全局变量和局部变量

全局变量只有在浏览器关闭的时候才会销毁，比较占内存资源

局部变量当我们程序执行完毕就会销毁，比较节约内存资源

### 9.6 作用域链

当在函数作用域中使用一个变量时，它会先在自身作用域中寻找

如果找到了则直接使用，如果没有找到则到上一级作用域中寻找

如果找到了则使用，找不到则继续向上找

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var a = 11;

			function fun(){
				var a = 10;
				console.log(a);
			}
			fun();
			console.log(a);
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/879a0494baa2c5c8fcc411acf2c2b4e8_MD5.png]]

假如在函数里面要访问全局的变量，可以使用 windows

## 10. 预解析

### 10.1 变量的声明提前

在全局作用域中，使用 var 关键字声明的变量会在所有的代码执行之前被声明，但是不会赋值。

我们来看下面的例子，先执行的是 console 的语句，所以先看的是 a，但是我们没有声明 a，但是程序没有报错，所以这里在 console 的上面浏览器自动加上了一个 var a

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(a);
			var a = 123;

            //其实可以类比为下面这样

            var a;
            console.log(a);
            a = 123;
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/fb70c8e5afe75387275d66edb21bf909_MD5.png]]

在函数作用域中，也具有该特性，使用 var 关键字声明的变量会在函数所有的代码执行前被声明

如果没有使用 var 关键字声明变量，则变量会变成全局变量，因为前面默认会加上一个 windows 来设置为全局变量

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var a = 11;
			function fun(){
				console.log(a);
				a =100;
			}
			fun();
			console.log(a);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/9424ec2bfd47634f7ae1362e4a160545_MD5.png]]

### 10.2 函数的声明提前

在全局作用域中，使用函数声明创建的函数（function fun(){}）,会在所有的代码执行之前被创建，

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			fun();

			function fun(){
				console.log("1");
			}
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/3a91fd8849246854dd646dd718a056b9_MD5.png]]

也就是我们可以在函数声明前去调用函数，但是使用函数表达式(var fun = function(){})创建的函数没有该特性

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			fun();

			var fun = function(){
				console.log("1");
			};
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/d84dd3c0a4c583a0f65088ab2e031845_MD5.png]]

在函数作用域中，使用函数声明创建的函数，会在所有的函数中的代码执行之前就被创建好了

### 10.3 预解析解读

JS 代码是由浏览器的 JS 解析器来执行的，JS 解释器在执行 JS 代码的时候，是按预解析和代码执行 2 步

#### 10.3.1 预解析

预解析:预解析会把 JS 里面所有的 var 和 function 提升在当前作用域的最前面

预解析分为变量预解析、函数预解析

##### 10.3.1.1 变量预解析

变量预解析就是把所有变量声明提升到当前作用域的最前面，但是不提升赋值的操作

这里就可以解释上面的变量的声明提前，但是下面这个解析的方式可能有点不一样，就是为什么会报错了

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			fun();

			var fun = function(){
				console.log("1");
			};

            //JS解析之后就是下面这样的
            var fun;
            fun();
            fun = function(){
                console.log("1");
            }
		</script>
	</head>
	<body>
	</body>
</html>
```

##### 10.3.1.2 函数预解析

函数预解析就是把所有函数声明提升到当前作用域的最前面，但是不调用函数

#### 10.3.2 代码执行

按照代码书写顺序从上到下执行

### 10.4 预解析案例

**案例一**

![[00 assets/309479133e468f3eef6e2c9a6da81c9e_MD5.jpeg]]

假如解析之后就是

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="application/javascript">
			var num
			function fun(){
				var num;
				console.log(num);
				num=20;
			}

			num=10;
			fun();
		</script>
	</head>
	<body>
	</body>
</html>
// undefined
```


**案例二**

![[00 assets/c61f72ac04d14ea4d68d5687de1c4df4_MD5.jpeg]]

假如预解析之后就是

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="application/javascript">
			var num;
            function fn(){
                var num;
                console.log(num)
                num =20;
                console.log(num);
            }
            num =10;
            fn();
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/1509a90241fb4f8e09572c78d441667d_MD5.png]]

**案例三**

![[00 assets/ac53c91513d64583c04bc46f70770fdd_MD5.jpeg]]

假如预解析之后就是

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="application/javascript">
			var a;
			function f1(){
				var b;
				b=9;

				var a;

				console.log(a);
				console.log(b);

				a ='123'
			}
			a=18;
			f1();

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/9fe167a6d39b00cd0ccce56f224c76c3_MD5.png]]

**案例四**

![[00 assets/435dfc1566f7c91bcdb4332ae3501d6e_MD5.png]]

假如预解析之后就是

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="application/javascript">
			// var a=b=c=9;
			// 相当于是var a=9; b=9; c=9;
			// 这个b和c只有值，没有var这个直接当作全局变量看

			function f1(){
				var a;
				a = b =c =9;
				console.log(a);
				console.log(b);
				console.log(c);
			}
			f1();
			console.log(c);
			console.log(b);
			console.log(a);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/f274ec7c15e1705ffccc2503969423e2_MD5.jpeg]]

## 11. 对象

对象是 JS 中的引用数据类型，是一种复合数据类型，在对象中可以保存多个不同数据类型的属性，如果使用 typeof 检查一个对象时，会返回 object

在 JS 中，对象是一组无序的相关属性和方法的集合，所有的事物都是对象，例如字符串、数值、数组、函数

![[00 assets/c85cb89be7f5de25221e4f0a9cfbf4fe_MD5.jpeg]]

![[00 assets/c02f20743f2d05943b8d1e2c1b5c3edd_MD5.png]]

### 11.1 创建对象

#### 11.1.1 使用字面量创建对象

对象字面量就是花括号{}，里面包括了表达这个具体事物(对象)的属性和方法

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj2 = {};//创建了一个空的对象
		</script>
	</head>
	<body>
	</body>
</html>

```

假如说在里面指定属性的话

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = {
				name: '孙悟空',
				age: 21,
				sex: '男',
				sayHi: function(){
					console.log("Hello");
				}
			}
		</script>
	</head>
	<body>
	</body>
</html>

```

我们也可以使用下面的 2 种方式来调用对象里面的值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = {
				name: '孙悟空',
				age: 21,
				sex: '男',
				sayHi: function(){
					console.log("Hello");
				}
			}

			console.log(obj.name);
			console.log(obj['age']);
			console.log(obj['sex']);
			obj.sayHi();
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/29df8f0276e1a3a6c5303b0160dad932_MD5.png]]

#### 11.1.2 new Object 创建对象

这里我们使用 = 来赋值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = new Object();
			obj.name = '孙悟空';
			obj.age = 21;
			obj.sayHi = function(){
				console.log("Hello");
			}

			console.log(obj.name);
			console.log(obj['age']);
			obj.sayHi();
		</script>
	</head>
	<body>
	</body>
</html>

```

假如你要查看的属性值在对象里面没有的话，就会放回 undefined

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = new Object();
			obj.name = '孙悟空';
			obj.age = 21;
			obj.sayHi = function(){
				console.log("Hello");
			}

			console.log(obj.name);
			console.log(obj.uname);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/dc1c1458856b950f325b4037fbffdf1f_MD5.png]]

当然我们也可以将对象赋值给属性值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = new Object();
			var obj_in = new Object();

			obj.name = '孙悟空';
			obj.age = 21;
			obj.in = obj_in;
			obj.sayHi = function(){
				console.log("Hello");
			}

			obj_in.name = '六耳猕猴';

			console.log(obj.name);
			console.log(obj.in.name);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/029443dadff090033070925251223477_MD5.png]]

#### 11.1.3 使用构造函数来构造对象

前面的两种方式一次只能创建一个对象，但是我们想一次创建多个对象的话，就需要使用构造函数创建

构造函数是专门用来创建对象的函数，我们将对象里面一些相同的属性和方法抽象出来封装到函数里面

一般构造函数的首字母需要大写

构造函数不需要 return，就可以返回结果

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function Star(name,age,sex){
				this.name = name;
				this.age = age;
				this.sex = sex;
				this.sayHi = function() {
					console.log("Hello!");
				}
			}
			var swk = new Star('孙悟空',18,'男');
			var zbj = new Star('猪八戒',19,'男');

			console.log(swk.name);
			console.log(swk.age);
			console.log(swk['sex']);
			swk.sayHi();

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/a81ec65cd68074b88460a276d15b4cd1_MD5.png]]

后记：感觉构造函数有点像 JAVA 里面的类

这里记一下**new**关键字**执行的过程**

1.new 构造函数会在内存中创建一个空的对象

2.构造函数里面的 this 就会指向空的对象

3.执行构造函数里面的代码，给空对象添加属性和方法

4.返回这个对象

### 11.2 变量、属性、函数、方法对比

变量和属性是相同的，他们都是用来存储数据的

变量是单独声明并赋值，使用的时候直接写变量名，单独存在

属性在对象里面是不需要声明的，使用的时候是对象.属性

函数和方法都是实现某种功能

函数是单独声明并且调用的

方法是在对象里面的，调用的时候是对象名.方法

### 11.3 遍历对象

#### 11.3.1 for...in

枚举对象中的属性，for...in

for...in 语句的循环体会执行多次，对象中有几个属性就会执行几次，每次都会把对象里里面的属性赋值给下面的变量 n，obj[n]得到的是属性值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = {
				name:"张小胖",
				age:12,
				sayName:function(){
					console.log(obj.name)
				}
			};
			for(var n in obj){
				console.log(n);
			}
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/0cc2bbd18af19ea9df193c659ffa2cbb_MD5.png]]

下面是取出属性值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = {
				name:"张小胖",
				age:12,
				sayName:function(){
					console.log(obj.name)
				}
			};
			for(var n in obj){
				console.log(obj[n]);
			}
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/cb054905f43a72f450190753185d04fa_MD5.jpeg]]

#### 11.3.2 keys()

我们也可以使用 keys 来遍历对象，但是这个是创建一个只有键的数组

```javascript
let p1 = {
	name:'张三',
	age:18
}
var arr = Object.keys(p1);
console.log(arr);
```

![[00 assets/ab9db17694a21cfc7c367489d4cc25d3_MD5.png]]

### 11.4 内置对象

JS 的对象包括自定义对象，内置对象，浏览器对象

内置对象就是 JS 就是指的 JS 自带的一些对象，这个对象可以直接使用，为开发提供方便

#### 11.4.1 Date

在 js 中使用 Data 对象来表示一个时间，也就是系统的时间

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d = new Date();

			document.write(d);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/eeae5cc98c0359387dc7ab288f7e1149_MD5.jpeg]]

我们也可以指定时间的数值，一般的格式是：月/日/年 时:分:秒

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			document.write(d1);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/d6c8319a441e92d725617eec4041b68a_MD5.png]]

这里要注意一个小细节，date 和 Date 是不一样的

##### 11.4.1.1 getDate()

用来获取日期是几日

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			document.write(d1.getDate());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/1862c45a3be490ac55d1140ceb8316b0_MD5.png]]

##### 11.4.1.2 getDay()

获取当前日期的这一天是一个星期的周几

周一到周六就是 1 到 6，但是周日是 0

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			console.log(d1.getDay());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/dc924fa104ce4b019137fe5c3dd34905_MD5.png]]

##### 11.4.1.3 getMonth()

获取当前日期的月份，但是一般都是少 1，因为是从 0 开始的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			console.log(d1.getMonth());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/9e9e9218614edc52c81d4d01ffcfd723_MD5.png]]

##### 11.4.1.4 getFullYear()

获取当前日期的年份，但是一般都是少 1，因为是从 0 开始的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			console.log(d1.getFullYear());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/b8996fdb3d3ccba10cd1a336b7170da3_MD5.png]]

##### 11.4.1.5 getHours()

获取小时数

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			console.log(d1.getHours());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/8049a09241e78851ee506824dfd6defd_MD5.png]]

##### 11.4.1.6 getMinutes()

获取分钟

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			console.log(d1.getMinutes());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/e63f5f1552f20d2968074b77ee188613_MD5.png]]

##### 11.4.1.7 getSeconds()

获取秒

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = new Date("12/03/2016 11:11:20");

			console.log(d1.getSeconds());
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/79cbe18acc0eae59f34b6afe7fbd1285_MD5.png]]

##### 11.4.1.8 getTime()和 valueOf()

获取当前日期对象的时间戳

时间戳是从 1970/1/1 0/0/0 到现在的日期所花费的毫秒数(1s=1000ms)

计算机底层在保存时间时都是使用的时间戳

这里有一个很有意思的小细节，你赋值一个时间为，1/1/1970 0:0:0 的时候，最后显示时间时-28800000，是因为有时差的问题

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var date = new Date();

			console.log(date.getTime());
			console.log(date.valueOf());
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/03cd501ac00927d7aa0868ed93cea56f_MD5.png]]

还有一个简单的写法

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var date = +new Date();

			console.log(date);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/fca5529d3e7aa999e4ba2b6d074d02cf_MD5.png]]

##### 11.4.1.9 now()

获取当前的时间戳，这个是 H5 新增的方法

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var d1 = Date.now();
			document.write(d1);
		</script>
	</head>
	<body>
	</body>
</html>
```

我们可以使用时间戳来测试代码的执行的性能

##### 11.4.1.10 Date 案例

显示时分秒，但是这里主要是在 10 以下的显示，1 的话就是 01，这里主要的实现方式是三元运算符

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var time = new Date("12/03/2016 1:1:2");
			var h = time.getHours();
			h = h<10? '0'+h : h;
			var m = time.getMinutes();
			m = m<10? '0'+m : m;
			var s = time.getSeconds();
			s = s<10? '0'+s : s;
			console.log(h+":"+m+":"+s);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/beb866d429f3faab2d4f252b9c52cdb0_MD5.png]]

倒计时案例

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function countDown(time){
				var date_now = +new Date();
				var date_old = +new Date(time);

				var time = (date_old - date_now)/1000;

				var d = parseInt(time/60/60/24);
				d = d<10? '0'+d : d;
				var h = parseInt(time/60/60%24);
				h = h<10? '0'+h : h;
				var m = parseInt(time/60%60);
				m = m<10? '0'+m : m;
				var s = parseInt(time%60);
				s = s<10? '0'+s : s;
				return d+'天'+h+'时'+m+'分'+s+'秒';
			}

			console.log(countDown('2021-11-25 21:00:00'));
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/8bb3ade07b90fa0ae9ca23a4304ee905_MD5.png]]

#### 11.4.2 Math

只是一个工具类，封装了很多的方法和属性

##### 11.4.2.1 PI

这就是 Π 的数值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.PI);
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.2.2 abs()

可以计算一个数字的绝对值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.abs(-1));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.2.3 ceil()

对数字进行上舍入(就是向上取整，小数值只要有，就自动加 1)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.ceil(1.2));
			console.log(Math.ceil(1.9));
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/a42016a937751efee6d4e43e7f1c476b_MD5.png]]

##### 11.4.2.4 floor()

对数值进行下舍入，就是不要小数的部分

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.floor(1.1));
			console.log(Math.floor(1.9))
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/983368a96e00415dd7e193da49b37292_MD5.png]]

##### 11.4.2.5 round()

对数值进行四舍五入取整

但是注意一个为题，但是.5 的时候，也就是 1.5，2.5 的时候，会往大了取，但是当为-1.5 的时候，-1 就是最大的，所以就不是-2 了

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.round(1.1));
			console.log(Math.round(1.9));
			console.log(Math.round(-1.1));
			console.log(Math.round(-1.5));
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/1e1480b565263803f3a804802327fc98_MD5.png]]

##### 11.4.2.6 random()

可以用来随机返回 0-1 的小数

假如生成 2-10 的随机数的话，就是下面的一个公式

假如生成 x-y 的话，就是 Math.floor(Math.random()\*(y-x))+x

假如你想包含 x 和 y 的话就是 Math.floor(Math.random()\*(y-x+1))+x

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
		for(var i = 0 ; i<100 ;i++){
			console.log(Math.floor(Math.random()*8)+2);
		}
		</script>
	</head>
	<body>
	</body>
</html>
```

##### 11.4.2.7 max()

获取多个数字的最大值，并且不限制

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.max(1,7,9,5));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.2.8 min()

获取最小值

##### 11.4.2.9 pow()

返回 x 的 y 次幂

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(Math.pow(2,2));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.2.10 sqrt()

返回一个数字的开方

##### 11.4.2.11 Math 案例

封装 max 和 min

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var obj = {
				max:function(){
					var max = arguments[0];
					for(var i=0;i<arguments.length;i++)
						if(max < arguments[i])
							max = arguments[i];
					return max;
				},
				min:function(){
					var min = arguments[0];
					for(var i=0;i<arguments.length;i++)
						if(min > arguments[i])
							min = arguments[i];
					return min;
				}
			}

			console.log(obj.max(1,9,10));
			console.log(obj.min(1,9,10));
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/2662dd09441a5f8e04ab85d5dfd7ac31_MD5.png]]

随机生成 1-10 的数字来猜

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			function getRandom(x,y){
				return Math.floor(Math.random()*(y-x+1))+x;
			}
			var rand_num = getRandom(1,10);
			var user_num = prompt("请输入数字"+rand_num);

			if(user_num == rand_num) console.log("对了");
			if(user_num < rand_num) console.log("小了");
			if(user_num > rand_num) console.log("大了");
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/7d615f48ad7608f84d36f8f78f474445_MD5.png]]

![[00 assets/28ac7fd6a58dbeae9fddc26981b2ae35_MD5.png]]

#### 11.4.3 String

在底层一般是字符数组来存储的

String 也就是字符串有不可变性，你看下面的图片，一开始 str 表示的是 andy，但是后面赋值给 str 为 red，这样的话 red 就会再内存空间里面开辟一个新的内存空间，然后指向，不建议向这样来改变，这样会影响电脑性能

![[00 assets/090fa87b5c0c8d806edde17bdda68303_MD5.png]]

##### 11.4.3.1 length

获取字符的长度，后面没有括号，是一个属性

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.length);
			console.log(num[4]);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/cb176fe7bc595fcd94793a138b104fa4_MD5.png]]

这里有没有好奇，为什么是字符串类型，但是可以使用 length 来输出长度，这是因为我们使用了基本包装类型，我们将简单数据类型包装为复杂数据类型，String，number，boolen 就可以被包装，下面是执行的步骤

```html
//1 创建
var temp = new String("aaa");
//2 赋值
str = temp;
//3 销毁
temp = null;
```

##### 11.4.3.2 charAt()

放回指定的值，但是一般很麻烦，直接使用索引就可以了

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.charAt(1));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.3.3 charCodeAt()

返回字符的 ASCII 码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.charCodeAt(1));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.3.4 fromChaeCode()

可以根据字符编码去获取字符

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			console.log(String.fromCharCode(98));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.3.5 concat()

链接两个或多个字符串，不会对原来的字符串有影响

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.concat("NO","don't"));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.3.6 indexof()

检索一个字符串有没有指定的内容

如果有，就会返回第一次出现的索引，如果没有的话，就返回-1

假如你输入的是多个字符的话，一般都是检索的是第一个数值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.indexOf("W"));
		</script>
	</head>
	<body>
	</body>
</html>
```

第二个值规定在字符串中开始检索的位置

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.indexOf("l",1));
		</script>
	</head>
	<body>
	</body>
</html>
```

##### 11.4.3.7 lastIndexOf()

和上面的是一样的，一般是从后面向前面查找

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.lastIndexOf("l"));
		</script>
	</head>
	<body>
	</body>
</html>
```

##### 11.4.3.8 slice()

截取指定的内容，并且返回，不会去影响原数组

第一个，是开始位置的索引(包括开始的位置)

第二个，是结束的位置的索引(不包括结束的位置)

如果省略第二个的话，就是截取后面的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var num = "Hello,Warld!";

			console.log(num.slice(1,4));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.4.3.9 substring()

和 slice()类似，但是不接受负值，并且会自动调整参数的位置

##### 11.4.3.10 substr()

也是截取的字符串

第一个数值是开始的索引，第二个数值是结束的索引

##### 11.4.3.11 replace()

替换字符串，但是只能替换一个

replace('被替换的字符','替换为的字符')

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script type="text/javascript">
			var str = 'afawwfbawafwfaw';

			console.log(str.replace('a','b'));
		</script>
	</head>
	<body>

	</body>
</html>

```

![[00 assets/190dc64debbe8dfb41e89281f0e6d217_MD5.png]]

但是假如我们想要都替换的话

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script type="text/javascript">
			var str = 'afawwfbawafwfaw';
			while(str.indexOf('a') !== -1){
				str = str.replace('a','-');
			}
			console.log(str);
		</script>
	</head>
	<body>

	</body>
</html>

```

![[00 assets/c5d4007ec32aac84d7e7a781f4a82219_MD5.png]]

##### 11.4.3.12 split()

字符转化为数组，split('分隔符')

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script type="text/javascript">
			var str = 'afa,wwf,baw,afw,faw';
			console.log(str.split(','));
		</script>
	</head>
	<body>

	</body>
</html>

```

![[00 assets/7882f8256c82846502f31dc4731638c6_MD5.png]]

##### 11.4.3.11 String 案例

返回字符的位置，及个数

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var arr = "wawawfffffw";
			var index = arr.indexOf('w');
			var num = 0;

			while(index !== -1)
			{
				console.log(index);
				num++;
				index = arr.indexOf("w",index+1);
			}

			console.log("出现的次数:"+num);
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/faee1920c0e7b94372e1c4f1a205dcf9_MD5.png]]

统计字符出现的次数，并且显示出现次数最多的字符

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = 'asifaofifeigweigwaagaege';
			var obj = {};

			for(var i=0;i<str.length;i++){
				var chars = str.charAt(i);
				if(obj[chars]){
					obj[chars]++;
				}
				else{
					obj[chars] = 1;
				}
			}
			console.log(obj);
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/2ae7cfa436da6e322f80c94afc3ee844_MD5.png]]

当然我们也可以求里面的最大值

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = 'asifaofifeigweigwaagaege';
			var obj = {};

			for(var i=0;i<str.length;i++){
				var chars = str.charAt(i);
				if(obj[chars]){
					obj[chars]++;
				}
				else{
					obj[chars] = 1;
				}
			}

			var max = 0;
			var ch;
			for(var k in obj){
				if(obj[k] > max){
					max=obj[k];
					ch = k;
				}
			}

			console.log(obj);
			console.log("最多的字母是:"+ch+" 一共出现了"+max+"次");
		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/c0cd132a65ef53fb253cca5e640422d4_MD5.png]]

#### 11.4.4 Array

参考数组里面的 7.5 数组的方法

## 12. 简单、复杂数据类型

### 12.1 简单类型和复杂类型

简单类型又叫做值类型，也就是 number，string，boolean，undefined，null，在存储的时候变量中存储的是值本身，但是这里有一个小问题，就是 null 虽然是简单数据类型，但是你使用 typedef 来检测的时候，就是对象，这是一个小错误就不用去管了

复杂类型也叫复杂数据类型，在存储时变量中存储的仅仅是地址，也就是通过 new 关键字创建的对象........等等

### 12.2 堆、栈

栈是由操作系统自动分配释放存放函数参数值、局部变量的值，简单数据类型存放在栈里面

堆是存储复杂类型，一般由程序员来分配释放，如果不释放，会有垃圾回收机制回收

![[00 assets/75967a18c59b1d309340d0966dcfdcae_MD5.jpeg]]

### 12.3 传参

#### 12.3.1 简单数据类型传参

基本和 Java 是差不多的

![[00 assets/a429de5ce91b3de679cfe48d6997e42f_MD5.png]]

#### 12.3.2 复杂数据类型传参

也基本和 Java 是差不多的

![[00 assets/f402109a0c7630a54ddee0056c590097_MD5.png]]

## 13. 原型对象

其实就是下面的图，我先来解释一下 Myclass 是一个函数，你在创建一个函数的时候，就会有一个 prototype，其中地址值指向的是原型对象，我们在创建 MyClass 对象的时候就会有一个属性** proto **也有原型对象的地址值，你在原型对象里面创建的值是公有的，你通过 MyClass 创建的对象都可以访问里面的值，但是什么时候是被迫访问呢？其实就是对象里面没这个值的时候就会访问原型对象里面的值，但是原型对象也是一个对象，所以 MyClass 的原型对象也有一个原型对象

![[00 assets/99ee1c47458e013d9ecb2c51079d372a_MD5.png]]

下面就是代码演示

下面这个就证明其实指的是一个位置

```javascript
function fn(){}

let p1 = new fn();
console.log(p1.__proto__ === fn.prototype);
//结果为true
```

我们再来给原型对象创建属性值

```javascript
function fn(){}
fn.prototype.val = 10;

let p1 = new fn();
console.log(p1.val);
//结果为10
```

事实证明其实对象是先查找自己的属性值的，假如没有的话就查找原型对象的值

```javascript
function fn(){}
fn.prototype.val = 10;

let p1 = new fn();
p1.val = 18;
console.log(p1.val + ' '+fn.prototype.val);
//结果为18 10
```

当然原型对象也是对象，所以你添加方法也是没问题的

```javascript
function fn(){}
fn.prototype.val = 10;
fn.prototype.say = function(){
	console.log('Hi!')
}

let p1 = new fn();
p1.say();
//结果为Hi!
```

in 不仅会找对象里面是否含有这个值，而且还会寻找他的原型对象是否有这个值，hasOwnProperty 只会找本身是否有这个值

你想下 p1.hasOwnProperty()，其中的 hasOwnProperty 是怎么来的

```javascript
function fn(){}
fn.prototype.val = 10;

let p1 = new fn();
console.log("val" in p1);
console.log(p1.hasOwnProperty("val"));
//结果
//true
//false
```

其实 hasOwnProperty 在对象的原型对象的原型对象里面

```javascript
function fn(){}
let p1 = new fn();
console.log(p1.__proto__.__proto__.hasOwnProperty("hasOwnProperty"));
//结果为true
```

# JavaScript WebAPIs

![[00 assets/daaf89eac7ae3a266590222efac8d14d_MD5.png]]

API 就是应用程序编程接口

![[00 assets/99e036978005f2f1b7e84072abeae45c_MD5.png]]

![[00 assets/d3aed2b3b18800da3ea7207e497cf56e_MD5.png]]

## 11. 正则表达式

正则用来定义一些字符串的规则，程序可以根据这些规则来判断一个字符串是否符合规则，也可以将一个字符串中符合规则的内容提取出来。

### 11.1 创建正则表达式

#### 11.1.1 第一个方式

var reg = new RegExp("正则","匹配模式");
var reg = /正则表达式/匹配模式

正则表达式是一个对象

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = new RegExp("Hello,Warld");
		</script>
	</head>
	<body>
	</body>
</html>

```

第二个数值可以为:

i:忽略大小写

g:全局匹配模式

设置匹配模式时，可以都不设置，也可以设置 1 个，也可以全设置，设置时没有顺序要求

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = new RegExp("a","i");

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.1.2 第二个方式

和上面的基本是一样的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			reg = /a/i;

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

### 11.2 正则语法

#### 11.2.1 |

如果我们判断或者的话，就是这个

```html
/*检查表示有o或i*/
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			reg = /o|i/i;

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>
```

#### 11.2.2 []

可以设置一个范围

[ a-z ] 小写字母
[ A-Z ] 大写字母
[ A-z ] 任意字母
[ 0-9 ] 任意数字

```html
/*检查表示有a-z只要有的话*/
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			reg = /[a-e]/i;

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

假如是下面的这个情况的话

```html
/*检查表示有abc,adc,aec只要有的话*/
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			reg = /a[bde]c/i;

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.2.3 [^]

表示除了这个，都可以

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			reg = /[^no]/;

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

假如是一个范围的话，就是下面的方式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			reg = /[^0-9]/;

			var number = "123";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

### 11.3 方法

#### 11.3.1 text()

可以用来检查一个字符串是否符合正则表达式

如果符合返回 true，否则返回 false

并且要注意这个是严格区分大小写的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = new RegExp("Hello,Warld");

			var number = "NO,warld";

			console.log(reg.test(number))
		</script>
	</head>
	<body>
	</body>
</html>

```

### 11.4 字符串的方法

#### 11.4.1 split

可以将字符串拆分为一个数组

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.split("b");

			console.log(result.length);
			console.log(result)

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/8819f5e3df8d7c88c4d6fb19035ea222_MD5.png]]

这个可以传递一个正则表达式，这样就可以和正则表达式一起合作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.split(/[A-z]/);

			console.log(result)

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/3539fe6396ffa2f9233b58b2846b64f5_MD5.png]]

#### 11.4.2 search()

用来搜索字符串中是否有指定的内容

如果搜索到了话，就返回第一次出现的索引，假如说没搜索到的话，就返回-1

search 只会设置第一个，即便设置看全局的模式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.search("2b");

			console.log(result);

		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/7d6b234d9ca04c5c8d7af35e2aabe4a1_MD5.png]]

这个也可以和正则表达式来整合

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "111 abc 222 adc 333 aec";

			var result = str.search(/a[bde]c/);

			console.log(result);

		</script>
	</head>
	<body>
	</body>
</html>
```

![[00 assets/d79d797e167dea7bdc7f3b8d4b2b2aff_MD5.png]]

#### 11.4.3 match()

可以根据正则表达式，从一个字符串中将符合条件的内容提取出来

我们来看下面的，要提取这个字符串里面的所有的字母，但是只能提取一个，我们这里可以打开全局模式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.match(/[A-z]/);

			console.log(result);

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/b92083fd25648befbd0f0f6f4121f68b_MD5.png]]

下面就是打开全局模式的效果

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.match(/[A-z]/g);

			console.log(result);

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/f1f1be2b4e40ec82161d187f3437dce3_MD5.jpeg]]

假如是两种全局模式的话，就是下面的一个模式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.match(/[A-z]/gi);

			console.log(result);

		</script>
	</head>
	<body>
	</body>
</html>
```

match()会将匹配到的内容封装到一个数组返回

#### 11.4.4 replace()

可以将字符串中指定的内容替换为新的内容

参数 1：被替换的内容，参数 2：新的内容

但是默认只能替换一个

假如说我想替换所有的字母的话，就可以使用正则表达式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "1a2b3c4d5e";

			var result = str.replace(/[a-z]/g,"英");

			console.log(result);

		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/53418487ba91aa5cdba9aee07550e050_MD5.png]]

### 11.5 正则表达式语法

#### 11.5.1 量词

##### 11.5.1.1 {}

通过设置一个量词表示一个内容的出现次数

{n}，表示正好出现的次数

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "aaaeee";

			var reg = /a{3}/;

			console.log(reg.test(str));

		</script>
	</head>
	<body>
	</body>
</html>
```

假如说要检查 ababab 的话

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "ababab";

			var reg = /(ab){3}/;

			console.log(reg.test(str));

		</script>
	</head>
	<body>
	</body>
</html>

```

假如说检查 abbbc 的话

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "abbbc";

			var reg = /ab{3}c/;

			console.log(reg.test(str));

		</script>
	</head>
	<body>
	</body>
</html>
```

这里我们还可以设置一个范围

假如你不知道 b 的出现次数，我们可以设置一个 1-3 的范围

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "abbc";

			var reg = /ab{1,3}c/;

			console.log(reg.test(str));

		</script>
	</head>
	<body>
	</body>
</html>

```

假如设置一个 3 次以上的话

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var str = "abbbbc";

			var reg = /ab{3,}c/;

			console.log(reg.test(str));

		</script>
	</head>
	<body>
	</body>
</html>
```

##### 11.5.1.2 +

表示至少有一个，意思就是说，b 至少有一个，相当于{1,}

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /ab+c/;

			console.log(reg.test("abbbbbc"));
		</script>
	</head>
	<body>
	</body>
</html>
```

##### 11.5.1.3 \*

0 个或多个，相当于{0,}

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /ab*c/;

			console.log(reg.test("abbbbbc"));
		</script>
	</head>
	<body>
	</body>
</html>

```

##### 11.5.1.4 ？

表示 0 个或 1 个，相当于{0,1}

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /ab?c/;

			console.log(reg.test("abbbbbc"));
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.5.2 ^

表示开头

我们来检查一个字符串中是否以 a 开头

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /^a/;

			console.log(reg.test("abbbbbc"));
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.5.3 $

表示结尾

我们来检查一个字符串中是否以 c 结尾

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /c$/;

			console.log(reg.test("abbbbbc"));
		</script>
	</head>
	<body>
	</body>
</html>

```

如果在正则表达式中使用^或$的话，就只能是这个字符

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /^a$/;

			console.log(reg.test("a"));
		</script>
	</head>
	<body>
	</body>
</html>
```

假如说我们来判断一个电话号码的话

这里注意设置正则的语法的时候不能设置空格

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /^1[3-9][0-9]{9}$/

			console.log(reg.test("18345478912"));
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.5.4 .

.表示的是任意字符

假如说，我们要表示“.”的话，就必须加上\，所以这样推的话，要表示\的话，就必须是\\

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /\./

			console.log(reg.test(".123"));
		</script>
	</head>
	<body>
	</body>
</html>

```

假如说使用的正则的第一个方式的话，就必须使用 2 个\ \，因为它是一个字符串

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = new RegExp("\\.");

			console.log(reg.test(".123"));
		</script>
	</head>
	<body>
	</body>
</html>
```

#### 11.5.5 \w 和\W

\w 表示任意字母、数字和下划线

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /\w/

			console.log(reg.test(".123"));
		</script>
	</head>
	<body>
	</body>
</html>

```

\W 表示除了字母、数字和下划线

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /\W/

			console.log(reg.test(".123"));
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.5.6 \d 和\D

\d 表示任意数字

\D 表示除了数字

#### 11.5.7 \s 和\S

\s 表示空格

\S 表示除了空格

去除前面的空格，和后面的空格

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg  = prompt("输入名字:");
			reg = reg.replace(/^\s*|\s*$/g,"");
			console.log(reg);
		</script>
	</head>
	<body>
	</body>
</html>

```

#### 11.5.8 \b 和\B

\b 表示单词边界，表示是一个独立的单词，就是设置单词的界限的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var reg = /\bchild\b/

			console.log(reg.test("hello child boy"));
		</script>
	</head>
	<body>
	</body>
</html>

```

\B 表示除了单词边界

### 11.6 邮箱的正则

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<script type="text/javascript">
			var email  = prompt("输入名字:");
			var reg = /^\w{3,}(\.\w+)*@[A-z0-9]+(\.[A-z]{2,5}){1,2}$/;

			console.log(reg.test(email));
		</script>
	</head>
	<body>
	</body>
</html>
```

### 11.7 常用的正则表达式

![[00 assets/010ad1b088fc2dcf828ecb1ed153bc2c_MD5.png]]

![[00 assets/c1acf1f3dacaaf07793777137f224eb1_MD5.png]]

## 12. DOM

### 12.1 DOM 简介

文档对象模型，通过 DOM(Document Object Model)可以来任意来修改网页中各个内容，也就是接口

**文档**:文档指的是网页，一个网页就是一个文档

**对象**:对象指将网页中的每一个节点都转换为对象，转换完对象以后，就可以以一种纯面向对象的形式来操作网页了

**模型**:模型用来表示节点和节点之间的关系，方便操作页面

**节点**(Node):节点是构成网页的最基本的单元，网页中的每一个部分都可以称为是一个节点
虽然都是节点，但是节点的类型却是不同的

**常用的节点**
文档节点 （Document），代表整个网页
元素节点（Element），代表网页中的标签
属性节点（Attribute），代表标签中的属性
文本节点（Text），代表网页中的文本内容

![[00 assets/68cf0418f77c6379c400d190469a0fee_MD5.png]]

**节点的属性**

![[00 assets/da18db026851bf5737ae4117f6b3c0cc_MD5.png]]

### 12.2 文档的加载

我们来看下面的代码，有没有一个疑惑，以前的 script 是放在 head 里面，但是这个是放在 button 的下面

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<button id="one">点我</button>

		<script type="text/javascript">
			var btn = document.getElementById("one");

			btn.onclick = function(){
				alert("点我干什么");
			};
		</script>
	</body>
</html>

```

原因是因为文档是上到下的，假如把 script 放在上面的话，就没有 btn 的代码，所以就不可以执行，并且报错

### 12.3 获取元素

#### 12.3.1 获取元素节点

通过下面得都是通过 document 来调用的

##### 12.3.1.1 getElementById()

通过 id 属性获取一个元素节点对象

getElementById()返回一个匹配特定 ID 得元素

下面的代码实现的使点击按钮，来实现查找北京，onclick 是点击的时候执行，innerHTML 是获取里面的字

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
				background-color: cornflowerblue;
				/* 设置水平居中 */
				text-align: center;
				/* 设置垂直居中 */
				display: table-cell;
				vertical-align: middle;

				border: 1px solid green;
			}
		</style>
	</head>
	<body>
		<div id="bj">北京</div>
		<div id="nj">南京</div>


		<button id="one">点我</button>
		<script type="text/javascript">
			// 为id为one的按钮绑定一个单击函数
			var one_bj = document.getElementById("one");

			//具体实现
			one_bj.onclick = function(){
				// 再获取id为bj的节点
				var bj = document.getElementById("bj");
				alert(bj.innerHTML);
			};
		</script>
	</body>
</html>
```

![[00 assets/a4c1cf70fdebaa56ccd4e8c2b39f0533_MD5.png]]

后记：首先我们要获取按钮吧！假如你不获取按钮得话，是不是你点击按钮就没什么用，所以我们首先先通过 getElementById 来获取按钮得信息，然后这个按钮点击之后要有相应得反应，也就是函数，当然在对象里面才叫方法，我们就要获取北京得相关信息，然后再读取北京得信息来返回给浏览器

假如你不使用 innerHTML 的话，就会返回整个标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="bj">北京</div>
		<script type="text/javascript">
			var el = document.getElementById("bj");
			console.log(el);
		</script>
	</body>
</html>
```

![[00 assets/29dc82e76b346607062549b2e6cf1920_MD5.png]]

当然也不是放回整个标签，这只是显示，其实真正返回得是 element 对象，如果没有得话就返回 null

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="bj">北京</div>
		<script type="text/javascript">
			var el = document.getElementById("bj");
			console.log(el);
			console.log(typeof el);
		</script>
	</body>
</html>
```

![[00 assets/2c06c01b527f2306e55f4512affcc563_MD5.png]]

我们也可以使用 dir 来显示整个标签完整得信息

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="bj">北京</div>
		<script type="text/javascript">
			var el = document.getElementById("bj");
			console.log(el);
			console.log(typeof el);
			console.dir(el);
		</script>
	</body>
</html>
```

![[00 assets/802ac440744d102d37379bb757e95b37_MD5.png]]

##### 12.3.1.2 getElementsByTagName()

通过标签名获取一组元素节点对象

下面是直接获取“北京”、"南京"

这个是将获取到的返回一个类数组对象，所以查询到的都会封装到对象中，即使元素只有一个，也会封装到数组中

假如里面没有这个元素的话，就会返回一个空的伪数组

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
				background-color: cornflowerblue;
				/* 设置水平居中 */
				text-align: center;
				/* 设置垂直居中 */
				display: table-cell;
				vertical-align: middle;

				border: 1px solid green;
			}
		</style>
	</head>
	<body>
		<!-- 查找背景 -->
		<div id="bj">北京</div>
		<div id="nj">南京</div>


		<button id="one">点我</button>

		<script type="text/javascript">
			// 为id为one的按钮绑定一个单击函数
			var one = document.getElementById("one");

			//具体实现
			one.onclick = function(){

				// 再获取div的节点
				var div = document.getElementsByTagName("div");

				for(var i=0 ; i<div.length ; i++){
					alert(div[i].innerHTML);
				}
			};
		</script>
	</body>
</html>

```

下面就是用伪数组来存储，而且存储得是动态得，假如你改变了标签里面存储得是不会改变的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="bj">北京</div>
		<div id="nj">南京</div>

		<script type="text/javascript">
			var div = document.getElementsByTagName('div');
			console.log(div);
		</script>
	</body>
</html>

```

![[00 assets/6946e364f599085ba5c8deb9271439ce_MD5.png]]

假如是下面的情况的话，根据标签名来获取的话

下面有一个注意的点，父元素必须是单个对象，也就是下面的 ol[0]这里的问题

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
		</ul>

		<ol>
			<li>啥啥啥啥</li>
			<li>啥啥啥啥</li>
			<li>啥啥啥啥</li>
			<li>啥啥啥啥</li>
		</ol>

		<script type="text/javascript">
			var ol = document.getElementsByTagName('ol');
			var lis = ol[0].getElementsByTagName('li');

			console.log(lis);
		</script>
	</body>
</html>

```

![[00 assets/0168d04d4878f67f0e6349970229fc2b_MD5.png]]

也可以使用 id 来使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
		</ul>

		<ol id="one">
			<li>啥啥啥啥</li>
			<li>啥啥啥啥</li>
			<li>啥啥啥啥</li>
			<li>啥啥啥啥</li>
		</ol>

		<script type="text/javascript">
			var ol = document.getElementById('one');
			var lis = ol.getElementsByTagName('li');

			console.log(lis);
		</script>
	</body>
</html>

```

![[00 assets/740a9f26a13568f9cc7e9d59de3bac20_MD5.png]]

##### 12.3.1.3 getElementsByName()

通过 name 属性获取一组元素节点对象

下面是读取 name，这里注意一个问题

innerHTML 是读取元素内部的 HTML 代码

但是你要读取属性的值的话,就是元素.属性名

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<input type="radio" name="gender" value="male" />
		Male
		<input type="radio" name="gender" value="Female" />
		Female

		<button id="one">点我</button>
		<script type="text/javascript">
			var one = document.getElementById("one");

			one.onclick = function(){
				var gender = document.getElementsByName("gender");

				for(var i=0 ; i<gender.length ; i++){
					alert(gender[i].value);
				}
			}
		</script>
	</body>
</html>

```

但是唯独 class 不能采用，只能使用 classNAME 才可以使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<input type="radio" name="gender" value="male" class="two"/>
		Male
		<input type="radio" name="gender" value="Female" class="two"/>
		Female

		<button id="one">点我</button>
		<script type="text/javascript">
			var one = document.getElementById("one");

			one.onclick = function(){
				var gender = document.getElementsByName("gender");

				for(var i=0 ; i<gender.length ; i++){
					alert(gender[i].className);
				}
			}
		</script>
	</body>
</html>

```

##### 12.3.1.4 getElementsByClassName()

根据类名来获取元素，基本和 getElementsByTagName()差不多

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul class="one">
			<li>这是一个啥</li>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
			<li>这是一个啥</li>
		</ul>

		<script type="text/javascript">
			var ul = document.getElementsByClassName('one');
			var lis = ul[0].getElementsByTagName('li');
			console.log(lis);
		</script>
	</body>
</html>

```

![[00 assets/28ac7fd6a58dbeae9fddc26981b2ae35_MD5.png]]

##### 12.3.1.5 querySelector()

可以根据 css 选择器来查询一个元素节点对象

虽然上面查询 class 不支持 ie8，我们就可以使用这个

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<div class="div1">
			<div>我是div1里面的div</div>
		</div>

		<script type="text/javascript">
			var b_all = document.querySelector(".div1 div");

			console.log(b_all.innerHTML)
		</script>
	</body>
</html>
```

![[00 assets/9e301cd409706e9d880d246704396e92_MD5.png]]

使用该方法总会返回唯一的一个元素,也就是返回第一个元素

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<div class="div1">
			<div>我是div1里面的div</div>
			<div>我是div1里面的div二号</div>
		</div>

		<script type="text/javascript">
			var div =document.querySelector('.div1 div');
			console.log(div)
		</script>
	</body>
</html>
```

![[00 assets/ee7f887896f948b97b9c932815156c9b_MD5.png]]

##### 12.3.1.6 querySelectorAll()

会返回指定选择器的所有元素对象的集合，可以获取多个，会封装到数组里面

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<div class="div1">
			<div>我是div1里面的第一个div</div>
			<div>我是div1里面的第二个div</div>
		</div>

		<script type="text/javascript">
			var b_all = document.querySelectorAll(".div1 div");
			console.log(b_all);
			console.log(b_all[0].innerHTML)
		</script>
	</body>
</html>
```

![[00 assets/874ed4ed353021cb7d22163170e60ebf_MD5.jpeg]]

##### 12.3.1.7 获取 body

获取 body，返回的是一个元素对象

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<div>
			这是一个div标签
		</div>
		<script type="text/javascript">
			var b_all = document.body;

			console.log(b_all);
		</script>
	</body>
</html>

```

![[00 assets/93f4a1f3d8cbac511604a583c6622e3e_MD5.png]]

##### 12.3.1.8 获取 html

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div>
			这是一个div标签
		</div>

		<script type="text/javascript">
			var b_all = document.documentElement;

			console.log(b_all)
		</script>
	</body>
</html>

```

![[00 assets/28fc88bcdbfbfc50faca692113c1f28d_MD5.png]]

##### 12.3.1.9 根据自定义属性获取

![[00 assets/9f7f7a9d05e06352477a46deffc176ae_MD5.png]]

#### 12.3.2 获取元素节点的子节点

通过具体的元素节点调用

当然假如使用上面的获取元素节点的方法不仅逻辑性不强，而且繁琐，所有我们就要学习节点操作

一般的，节点至少拥有 nodeType(节点类型),nodeName(节点名称),nodeValue(节点值)

其中元素节点的 nodeType 为 1，属性节点为 2，文本节点为 3，其中包含文字，空格，换行

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p id="three">北京</p>
			<p>南京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			console.dir(div_t);
		</script>
	</body>
</html>
```

![[00 assets/49d621949679f5bb4f09cda5230a19b8_MD5.png]]

##### 12.3.2.2 childNodes

childNodes 属性会获取包括文本在内的所有节点，注意这里是包括文本在内，所以在开发的时候不是很提倡

我们来看下面的代码

我们思考一下，为什么最后的值是 5 呢，因为根据 DOM 标签间空白也会当成文本节点，也就是从< div id="two" >后面的换行也算

注意 IE8 一下的浏览器中，不会将空白文本当成子节点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p id="three">北京</p>
			<p>南京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			var div_w = div_t.childNodes;
			console.log(div_w)
		</script>
	</body>
</html>
```

![[00 assets/826e5486403d7a49043eb47831b6ce4c_MD5.png]]

##### 12.3.2.3 children

childrens 是获取当前元素的所有子元素，但是不会获取文本节点

它不是一个标准的函数，但是它得到了大部分浏览器的支持，基本可以随便使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p id="three">北京</p>
			<p>南京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			var p_s = div_t.children;
			console.log(p_s);
		</script>
	</body>
</html>
```

![[00 assets/f697fcf3d76ca4771240cf742244a1c9_MD5.png]]

##### 12.3.2.4 firstElementChild

这是获取第一个子节点，但是不包括文本节点，但是注意一个问题，这有兼容性问题

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p>北京</p>
			<p>南京</p>
			<p>吴京</p>
			<p>西京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			var p_s = div_t.firstElementChild;
			console.log(p_s);
		</script>
	</body>
</html>
```

![[00 assets/8bf38597fb4ece4fe9b9791e374ee080_MD5.png]]

但是考虑到兼容性问题，我们在实际中就使用下面的写法，也就是使用 children，这样不仅可以获取第一个，还可以获取最后一个节点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p>北京</p>
			<p>南京</p>
			<p>吴京</p>
			<p>西京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			console.log(div_t.children[0]);
			console.log(div_t.children[3]);
		</script>
	</body>
</html>
```

![[00 assets/48645f54e27a5519c61d32a9d0cd04f7_MD5.png]]

##### 12.3.2.5 lastElementChild

这是获取最后一个个子节点，不包括文本节点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p>北京</p>
			<p>南京</p>
			<p>吴京</p>
			<p>西京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			var p_s = div_t.lastElementChild;
			console.log(p_s);
		</script>
	</body>
</html>
```

![[00 assets/f146724395f41d14a24e37fc2dc7a01a_MD5.png]]

##### 12.3.2.6 firstChild

获取第一个子节点，但是和 childNodes 是一样的，会获取文本节点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p>北京</p>
			<p>南京</p>
			<p>吴京</p>
			<p>西京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			var p_s = div_t.firstChild;
			console.log(p_s);
		</script>
	</body>
</html>
```

![[00 assets/29c960939f7b49589325deadf94e603b_MD5.png]]

##### 12.3.2.7 lastChild

获取最后个子节点，但是和 childNodes 是一样的，会获取文本节点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p>北京</p>
			<p>南京</p>
			<p>吴京</p>
			<p>西京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('two');
			var p_s = div_t.lastChild;
			console.log(p_s);
		</script>
	</body>
</html>
```

![[00 assets/dbc328a558e6da59b264335d9698bc9e_MD5.png]]

#### 12.3.3 获取父节点和兄弟节点

这里是一个思想，每当有重复的代码的时候，就可以这样想，设置一个方法，

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			div{
				width: 200px;
				height: 140px;

				margin: 0 auto;
				background-color: chocolate;
				text-align: center;
			}
			p{
				padding: 20px 0;
				border: 2px solid blueviolet;
			}
			#one{
				margin-left: 740px;
				margin-top: 20px;
			}
		</style>
	</head>
	<body>
		<div id="two">
			<p>北京</p>
			<p>南京</p>
		</div>
		<button id="one">点我</button>

		<script type="text/javascript">
			function myClick(idStr , fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			}

			myClick("one",function(){
				alert("hello");
			});
		</script>
	</body>
</html>

```

![[00 assets/6e8fed2835ae8327b75506b046d82a0b_MD5.png]]

##### 12.3.3.1 parentNode

表示当前节点的父节点，可以看下面的显示的控制台，就是获取到了父节点

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="two">
			<p id="three">北京</p>
			<p>南京</p>
		</div>

		<script type="text/javascript">
			var div_t = document.getElementById('three');
			var div_w = div_t.parentNode;
			console.log(div_w)
		</script>
	</body>
</html>
```

![[00 assets/acc8a4500ba9f140c22b4e72861f1032_MD5.png]]

但是要注意一个问题，这是获取离这最近的父节点

假如你想获的父亲的父亲的节点，就可以在后面再加上一个 parentNode

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="one">
			<div id="two">
				<p id="three">北京</p>
				<p>南京</p>
			</div>
		</div>

		<script type="text/javascript">
			var div_one = document.getElementById('three');
			var div_two = div_one.parentNode;
			var div_three = div_one.parentNode.parentNode;
			console.log(div_two);
			console.log(div_three);
		</script>
	</body>
</html>
```

![[00 assets/9975993ee5d50f8452ca5d44da07c4a5_MD5.png]]

##### 12.3.3.4 nextSibling

获取的下一个节点，但是要注意，它也会获取文本节点，找不到的话就会返回 null

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
		<div>这是第一个兄弟</div>
		<span>这是第二个兄弟</span>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			var spans = divs.nextSibling;
			console.dir(spans);
		</script>
	</body>
</html>

```

![[00 assets/0e25e01258203a3b418fba0ab60442a0_MD5.png]]

##### 12.3.3.2 previousSibling

这个是获取上一个节点，也会获取文本节点，找不到的话就会返回 null

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
		<div>这是第一个兄弟</div>
		<span>这是第二个兄弟</span>
		<script type="text/javascript">
			var spans = document.querySelector('span');
			var divs = spans.previousSibling;
			console.dir(divs);
		</script>
	</body>
</html>

```

![[00 assets/8928694c5c80cfdbac3b32ad512958af_MD5.jpeg]]

##### 12.3.3.5 nextElementSibling

获取下一个节点的元素

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
		<div>这是第一个兄弟</div>
		<span>这是第二个兄弟</span>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			var spans = divs.nextElementSibling;
			console.dir(spans);
		</script>
	</body>
</html>

```

![[00 assets/b4fdf7fb9ccec9ce017a7ecf140600f6_MD5.png]]

在实际中会因为兼容性问题，导致无法正常使用，但是我们可以使用自己封装的函数来解决

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
		<div>这是第一个兄弟</div>
		<span>这是第二个兄弟</span>
		<script type="text/javascript">
			function getNextElementSibling(element){
				var el = element;
				while(el = el.nextSibling){
					if(el.nodeType === 1){
						return el;
					}
				}
				return null;
			}

			var divs = document.querySelector('div');
			var spans = getNextElementSibling(divs);
			console.log(spans);
		</script>
	</body>
</html>

```

![[00 assets/854d9c28a1aea5e7a423fa2c458db4d0_MD5.png]]

##### 12.3.3.3 previousElementSibling

获取前一个兄弟元素，IE8 不支持

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
		<div>这是第一个兄弟</div>
		<span>这是第二个兄弟</span>
		<script type="text/javascript">
			var spans = document.querySelector('span');
			var divs = spans.previousElementSibling;
			console.dir(divs);
		</script>
	</body>
</html>

```

![[00 assets/3bdc7c52c7532d4a483f4a0761b65942_MD5.png]]

### 12.4 DOM 增删改

#### 12.4.1 增

##### 12.4.1.1 createElement

创建一个元素节点，后面是写需要创建的标签。因为原本的元素是不存在的，是根据我们的需求动态生成的，所以我，1 也称为动态创建元素节点

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
		<ul></ul>
		<script type="text/javascript">
			var li = document.createElement('li');
		</script>
	</body>
</html>

```

但是创建节点是不够的

##### 12.4.1.3 appendChild

添加一个节点

node.sppendChild(Child)，其中 node 是父级,child 是子级

你看下面的代码，是不是已经成功添加上去了

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
		<ul></ul>
		<script type="text/javascript">
			var li = document.createElement('li');
			var ul = document.querySelector('ul');
			ul.appendChild(li);
		</script>
	</body>
</html>

```

![[00 assets/ddaf1ff3d04c55588dca59d4944793b2_MD5.jpeg]]

但是它是将一个节点添加到指定父节点的子节点列表的末尾

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
		<ul>
			<li>1</li>
		</ul>
		<script type="text/javascript">
			var li = document.createElement('li');
			var ul = document.querySelector('ul');
			ul.appendChild(li);
		</script>
	</body>
</html>

```

![[00 assets/99388ef6c6d50e11cd5d07e14905d7d0_MD5.png]]

##### 12.4.1.2 createTextNode

再创建一个文本节点

##### 12.4.1.5 insertBefore

将节点插入到指定父节点的子节点的前面

node.insertBefore(child，指定节点)

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
		<ul>
			<li>1</li>
		</ul>
		<script type="text/javascript">
			var li = document.createElement('li');
			var ul = document.querySelector('ul');
			ul.insertBefore(li,ul.children[0]);
		</script>
	</body>
</html>
```

![[00 assets/48914bcb44fc9e77d928788469769972_MD5.jpeg]]

##### 12.4.1.4 创建的基本步骤

这里提供的是一个思想

首先我们想在 div 里面添加子元素需要什么，是不是先创建一个 p 的标签，这里就需要 createElement 来创建，我们之后需要什么，是不是需要一个文本，这个时候就需要使用 createTextNode，但是这个时候是只是 p 标签+文本内容，这个时候就需要把文本放到 p 标签里面，但是这个时候你按按钮还是不会添加，是不是还不知道往那里添加啊，这个时候就需要获取父节点 content，然后往这里面添加

```html
//创建一个东京节点
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			#content{
				width: 200px;
				height: 150px;
				border: 1px solid red;

				text-align: center;
			}
			p{
				border: 1px solid red;

				background-color: cornflowerblue;
			}
		</style>

	</head>
	<body>
		<div id="content">
			<p id="p_all">北京</p>
			<p>南京</p>
		</div>
		<button id="btn">按钮</button>

		<script type="application/javascript">
			function myClick(idStr,fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			};

			myClick("btn",function(){
				//先创建一个li元素的节点
				var c_li = document.createElement("li");
				//再创建一个文本节点
				var c_text = document.createTextNode("东京");
				//将文本节点作为li节点的子节点
				c_li.appendChild(c_text);
				//获取父节点
				var content = document.getElementById("content");
				//再将li添加到父节点里面去
				content.appendChild(c_li);
			});
		</script>

	</body>
</html>

```

![[00 assets/e0aef89ecebf419b3da004adebac9c41_MD5.png]]

我们也可以使用 innerHTML 来添加子节点，这个明显简单一点但是还是有一些区别的，你使用这个方式，也就是只改变一个，但是你使用上面的方式的话，就是把原本所有的删除再添加的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			#content{
				width: 200px;
				height: 150px;
				border: 1px solid red;

				text-align: center;
			}
			p{
				border: 1px solid red;

				background-color: cornflowerblue;
			}
		</style>

	</head>
	<body>
		<div id="content">
			<p id="p_all">北京</p>
			<p>南京</p>
		</div>
		<button id="btn">按钮</button>

		<script type="application/javascript">
			function myClick(idStr,fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			};

			myClick("btn",function(){
				//获取北京的节点
				var content = document.getElementById("content");

				content.innerHTML += "<p>东京</p>"
			});
		</script>

	</body>
</html>
```

但是还是比较推荐下面的这个方式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			#content{
				width: 200px;
				height: 150px;
				border: 1px solid red;

				text-align: center;
			}
			p{
				border: 1px solid red;

				background-color: cornflowerblue;
			}
		</style>

	</head>
	<body>
		<div id="content">
			<p id="p_all">北京</p>
			<p>南京</p>
		</div>
		<button id="btn">按钮</button>

		<script type="application/javascript">
			function myClick(idStr,fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			};

			myClick("btn",function(){
				var content = document.getElementById("content");
				var p = document.createElement("p");
				p.innerHTML = '广州';
				content.appendChild(p);
			});
		</script>

	</body>
</html>

```

##### 12.4.1.6 cloneNode

复制节点

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			var li = ul.children[0].cloneNode();
			ul.appendChild(li);
		</script>
	</body>
</html>

```

![[00 assets/0770da478cc18a33fd777f0e48648d42_MD5.png]]

但是发现没是不是没复制文本，这里就是 cloneNode 里面值得问题，默认是 false，就是浅拷贝，只复制节点，但是不复制节点里面得东西，true 就是深拷贝

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			var li = ul.children[0].cloneNode(true);
			ul.appendChild(li);
		</script>
	</body>
</html>

```

![[00 assets/83c6d8875522cdce123643473cf6ca97_MD5.jpeg]]

#### 12.4.2 删

##### 12.4.2.1 removeChild

这个是删除一个节点，并且返回删除的节点

基本语法：父节点.removeChild(子节点)

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>
		<script type="text/javascript">
			var ul = document.querySelector('ul');
			ul.removeChild(ul.children[0]);
		</script>
	</body>
</html>

```

![[00 assets/0e0f151feb3fbba5f85f213d4056a10c_MD5.png]]

#### 12.4.3 改

##### 12.4.3.1 replaceChild

可以使用指定的子节点替换已经有的子节点

这个的思路基本是一样的，先创建一个节点，然后再获取你要替换的节点，再获取父节点，使用父节点的方法替换就可以了

基本的语法是：父节点.replaceChild(新节点，旧节点)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			#content{
				width: 200px;
				height: 150px;
				border: 1px solid red;

				text-align: center;
			}
			p{
				border: 1px solid red;

				background-color: cornflowerblue;
			}
		</style>

	</head>
	<body>
		<div id="content">
			<p id="p_all">北京</p>
			<p>南京</p>
		</div>
		<button id="btn">按钮</button>

		<script type="application/javascript">
			function myClick(idStr,fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			};

			myClick("btn",function(){
				//先创建一个li元素的节点
				var c_li = document.createElement("p");
				//再创建一个文本节点
				var c_text = document.createTextNode("东京");
				//将文本节点作为li节点的子节点
				c_li.appendChild(c_text);
				//获取北京的节点
				var p_all = document.getElementById("p_all");
				//获取父节点
				var content = document.getElementById("content");
				//把新节点放到老节点前面
				content.replaceChild(c_li,p_all);
			});
		</script>

	</body>
</html>

```

##### 12.4.3.2 innerHTML

innerHTML 和 innerText 是差不多的，都是修改内容

innerHTML 从起始位置到终止位置的内容，空格和换行不会去掉，是 W3C 规定的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<div id="text">
			这是外面的哦
			<span>这是里面的哦</span>
		</div>
		<b></b>
		<script type="application/javascript">
			var text = document.getElementById('text');
			console.log(text.innerHTML);
		</script>
	</body>
</html>

```

![[00 assets/b801c514b559201810541c85ded5cb82_MD5.png]]

innerHTML 是识别 html 标签的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<div id="text"></div>
		<b></b>
		<script type="application/javascript">
			var text = document.getElementById('text');
			text.innerHTML = '<b>这是一个</b>在div的文字'
		</script>
	</body>
</html>

```

![[00 assets/2e61ae419e09df714721bd2c9855d1db_MD5.png]]

当然我们还可以通过 innerHTML 来设置一写高级的操作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<div id="time">时间</div>
		<button id="btn">按钮</button>

		<script type="application/javascript">
			var btn = document.getElementById('btn');
			var time = document.getElementById('time');

			btn.onclick = function() {
				time.innerHTML = countDown();
			}

			function countDown() {
				var date = new Date();
				var year = date.getFullYear();
				var month = date.getMonth();
				var day = date.getDay();
				return year + '年' + month + '月' + day + '日';
			}
		</script>
	</body>
</html>

```

![[00 assets/6c1ab47c9660befa5babb6a904ff036b_MD5.png]]

假如你不想设置点击获取时间的话，也可以不设置事件，直接通过网页来刷新获取

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<div id="time">时间</div>
		<button id="btn">按钮</button>

		<script type="application/javascript">
			var btn = document.getElementById('btn');
			var time = document.getElementById('time');

			function countDown() {
				var date = new Date();
				var year = date.getFullYear();
				var month = date.getMonth();
				var day = date.getDay();
				return year + '年' + month + '月' + day + '日';
			}

			time.innerHTML = countDown();
		</script>
	</body>
</html>

```

##### 12.4.3.3 innerText

innerText 从起始位置到终止位置的内容，但是它去除 html 内容，同时空格和换行都会去掉，并且不是标准的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<div id="text">
			这是外面的哦
			<span>这是里面的哦</span>
		</div>
		<b></b>
		<script type="application/javascript">
			var text = document.getElementById('text');
			console.log(text.innerText);
		</script>
	</body>
</html>

```

![[00 assets/638c106412f643130f4566324e8460e2_MD5.png]]

并且是不识别 html 标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<div id="text"></div>
		<b></b>
		<script type="application/javascript">
			var text = document.getElementById('text');
			text.innerText = '<b>这是一个</b>在div的文字'
		</script>
	</body>
</html>

```

![[00 assets/c1148d13dbc3bdcb2a8b1cd966d88574_MD5.png]]

innerHTML 和 innerText 是可读写的

##### 12.4.3.4 元素.属性

下面就是点击那个按钮就改变图片

这里主要的 img.src 就是改变 img 元素里面 src 的值，注意这里的 img 是设置的元素的名称，而不是上面的 img 标签

当然我们也可以改变路径 href，基本都是一样的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			img{
				width: 20%;
				height: 20%;
			}
		</style>
	</head>
	<body>
		<button id="one">火车</button>
		<button id="two">农村</button>
		<img src="img/pic1.jpg" >
		<script type="application/javascript">
			var one = document.getElementById('one');
			var two = document.getElementById('two');
			var img = document.querySelector('img');

			one.onclick = function(){
				img.src = 'img/pic1.jpg';
			}
			two.onclick = function(){
				img.src = 'img/pic2.jpg';
			}

		</script>
	</body>
</html>

```

![[00 assets/49525627525a71629b7e143a5924876a_MD5.png]]

下面是获取 input 里面的值

这里你写的是多少就是获取的多少

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<input type="text" value="abcde" id="usename" />
		<button id="one">点我</button>

		<script type="text/javascript">
			function myClick(idStr , fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			}

			myClick("one",function(){
				var usename = document.getElementById("usename");

				alert(usename.value);
			});
		</script>
	</body>
</html>
```

![[00 assets/a8ce4f60b3446edb6bb89b4abdce7d81_MD5.png]]

下面是修改里面的值，当你点击按钮的时候，values 的值会改变

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<input type="text" value="abcde" id="usename" />
		<button id="one">点我</button>

		<script type="text/javascript">
			function myClick(idStr , fun){
				var btn = document.getElementById(idStr);
				btn.onclick = fun;
			}

			myClick("one",function(){
				var usename = document.getElementById("usename");

				usename.value = "input修改之后的语句"
			});
		</script>
	</body>
</html>
```

![[00 assets/d31841ddb1136d80cbb02f2cf7778b82_MD5.png]]

##### 12.4.3.5 表单操作

innerHTML 是改变普通盒子里面的值，比如说：div

操作基本和上面的元素.属性

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>

	</head>
	<body>
		<button id="btn">按钮</button>
		<input type="text" value="输入文字" />

		<script type="application/javascript">
			var btn = document.getElementById('btn');
			var text = document.querySelector('input');

			btn.onclick = function(){
				text.value = '你点我干啥';
			}
		</script>

	</body>
</html>

```

![[00 assets/feea01c55ae4a889e66c649c5e6b1a1a_MD5.png]]

当然我们也可以改变里面的属性值

当你点击了按钮的时候，会禁用这个按钮

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>

	</head>
	<body>
		<button id="btn">按钮</button>
		<input type="text" value="输入文字" />

		<script type="application/javascript">
			var btn = document.getElementById('btn');
			var text = document.querySelector('input');

			btn.onclick = function(){
				text.value = '你点我干啥';
				btn.disabled = true;
			}
		</script>

	</body>
</html>

```

![[00 assets/6bcd70db5ad7e691d6c05ec7c91a5685_MD5.png]]

##### 12.4.3.6 write

它会在标签中写入内容

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
		<div>1</div>
		<script type="text/javascript">
			document.write('<div>2</div>')
		</script>
	</body>
</html>

```

![[00 assets/cd6b0f226c95d0c78d974340301204be_MD5.png]]

但是它有一个特点，就是文档流结束之后，在调用这句话得话，就会重绘文档流

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
		<div>1</div>
		<button type="button">按我</button>
		<script type="text/javascript">
			var btn = document.querySelector('button');
			btn.onclick = function(){
				document.write('<div>2</div>');
			}
		</script>
	</body>
</html>

```

原本是这样得

![[00 assets/297851db67388907c6090f3b84f79914_MD5.png]]

在点击得按钮之后，发现没文档流被重绘了

![[00 assets/ef996b2f87f085dd310dc90151b40522_MD5.jpeg]]

##### 12.4.3.7 innerHTML 和 createElement 得区别

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
		<div id="one"></div>
		<script type="text/javascript">
			var one = document.getElementById('one');
			// innerHTML创建
			one.innerHTML = '<div></div>';

			//createElement创建
			one.appendChild(document.createElement('div'));
		</script>
	</body>
</html>

```

![[00 assets/8f81e4f22f3600de08152662df3324d4_MD5.png]]

他们都能很快得创建完毕，但是我们不知道创建得效率是多少

下面是记录 innerHTML 创建时间得代码

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
		<div id="one"></div>
		<script type="text/javascript">
			function time(){
				var d1 =+ new Date();
				for(var i=0;i<3000;i++){
					document.body.innerHTML += '<div></div>';
				}
				var d2 =+ new Date();
				console.log(d2-d1);
			}
			time();
		</script>
	</body>
</html>

```

![[00 assets/2e5c900134ec87352b0cde6ac21855b1_MD5.png]]

使用 createElement 创建 50000 次也只需要 42ms，但是上面得创建 3000 次就需要 3064ms 了，可以看出 createElement 得效率很高，但是有没有效率更加高得方法呢

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
		<div id="one"></div>
		<script type="text/javascript">
			function time(){
				var d1 =+ new Date();
				for(var i=0;i<50000;i++){
					one.appendChild(document.createElement('div'));
				}
				var d2 =+ new Date();
				console.log(d2-d1);
			}
			time();
		</script>
	</body>
</html>

```

![[00 assets/edff754a15283c20c8f2b33e5df11a28_MD5.png]]

就是使用 innerHTML 来拼接数组里面得字符串

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
		<div id="one"></div>
		<script type="text/javascript">
			function time(){
				var d1 =+ new Date();
				var arr = [];
				for(var i=0;i<50000;i++){
					arr.push('<div></div>');
				}
				document.body.innerHTML = arr.join('');
				var d2 =+ new Date();
				console.log(d2-d1);
			}
			time();
		</script>
	</body>
</html>

```

![[00 assets/c86d4f4a3a019bf4b83cc660be8cb3c2_MD5.png]]

最后根据结果可以知道，用数组拼接得话，效率是最高得，但是这个方式结构不是很清晰

createElement 得效率虽然不是很高，但是它得结构很清晰

### 12.5 操作元素

我们可以通过 JS 修改元素的大小，颜色，位置

#### 12.5.1 元素.style

行内样式操作

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
				width: 200px;
				height: 200px;
				background-color: blueviolet;
			}
		</style>
	</head>
	<body>
		<div></div>
		<script type="text/javascript">
			var div = document.querySelector('div');
			div.onclick = function(){
				div.style.backgroundColor = 'pink';
				div.style.width = '500px';
			}
		</script>
	</body>
</html>

```

原本的样式

![[00 assets/6ac41a61c9d6c2d5787f7ac8c7476317_MD5.jpeg]]

点击之后的样式

![[00 assets/b3cbd50858083c1595ffee977c9ed845_MD5.png]]

注意这是修改的是行内样式，权重是比较高的

![[00 assets/8521c633bfee2a4b752ed928ad7686ac_MD5.jpeg]]

#### 12.5.2 元素.className

类名样式操作，就是将这个元素的类名改变或添加

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
				background-color: blueviolet;
			}
			.change{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div></div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			divs.onclick = function(){
				divs.className = 'change';
			}
		</script>
	</body>
</html>

```

原本

![[00 assets/5a363478f7e42a0055d2453bec0cbf2c_MD5.png]]

点击之后

![[00 assets/09f73c0f9fd8210cb6a335445eaf246e_MD5.png]]

使用这个的好处，假如有很多的样式设置的话，就是一排元素.style，这样非常不好看，我们就可以使用 className

假如你使用的话，就会覆盖以前的类名

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.yuan{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
				margin-left: 100px;
			}
			.change{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="yuan"></div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			divs.onclick = function(){
				divs.className = 'change';
			}
		</script>
	</body>
</html>

```

![[00 assets/ddd42b395dd561a092242a5d92e1e6d1_MD5.png]]

你看代码，是不是 class 改变为 change 了

![[00 assets/2e72e7d2d2781d5886daa0548d6424d9_MD5.jpeg]]

但是我们也可以使用一个方式来保留原本的类名

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.yuan{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
				margin-left: 100px;
			}
			.change{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="yuan"></div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			divs.onclick = function(){
				divs.className = 'yuan change';
			}
		</script>
	</body>
</html>

```

看见为样式就叠加了

![[00 assets/b28ef0f12c7a529e990da4358339ab65_MD5.jpeg]]

我们来看代码是不是就变成了 2 个 class 类名

![[00 assets/0a9f5b6bc506cfa9d6abcb464faba823_MD5.png]]

### 12.6 排他思想(算法)

假如做下面的按钮的话，不可能为每个小按钮绑定一个事件

![[00 assets/095a1b5f4ed099623a8fa48dba4da41e_MD5.png]]

就在这里就有一个思想，就可以直接链接下面的按钮

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
		<button>1</button>
		<button>2</button>
		<button>3</button>
		<button>4</button>
		<button>5</button>

		<script type="text/javascript">
			var btns = document.getElementsByTagName('button');

			for(var i =0 ; i<btns.length ; i++){
				btns[i].onclick = function(){
					for(var j = 0;j<btns.length ;j++){
						btns[j].style.backgroundColor = '';
					}
					this.style.backgroundColor = 'red';
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/e5b819c043772a2fcbb5543505a0901e_MD5.png]]

如果同一组元素，我们想要一个元素实现某种样式，需要用到循环打排他思想

1.所有元素全部清除样式

2.给当前元素设置样式

3.注意顺序不能颠倒，再设置自己

### 12.7 自定义属性值

#### 12.7.1 自定义属性值

自定义属性的目的是为了保存并使用数据，这样这些数据就不用保存到数据库里面了，可以直接使用

在 H5 的规范里面自定义属性直接使用 data-type 来设置自定义属性

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
		<div id="" data-index = "20">

		</div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			console.log(divs.getAttribute('data-index'))
		</script>
	</body>
</html>

```

![[00 assets/568c8d935e262670e9aba2073fefeb61_MD5.png]]

不仅可以使用下面的方法来获取自定义属性值，还可以通过 H5 新增的方法来获取

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
		<div id="" data-index = "20">

		</div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			console.log(divs.dataset.index);
		</script>
	</body>
</html>

```

![[00 assets/568c8d935e262670e9aba2073fefeb61_MD5.png]]

可以看下面的图片，不是在 divs.setAttribute 里面的 data-time 的值也是可以去出来，即便它不在 div 里面，而且我们也可以使用 dataset 来获取所有的 data 的值

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
		<div id="" data-index = "20"></div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			divs.setAttribute('data-time',2);
			console.log(divs.dataset.index);
			console.log(divs.dataset.time);
			console.log(divs.dataset);
		</script>
	</body>
</html>

```

![[00 assets/98fd1b66f00e9818b96282f665901757_MD5.png]]

当然我们也可以使用下面的方法来获取值，ie11 才支持 dataset，注意这一点

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
		<div id="" data-index = "20"></div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			divs.setAttribute('data-time',2);
			console.log(divs.dataset.index);
			console.log(divs.dataset.time);
			console.log(divs.dataset['index']);
			console.log(divs.dataset['time']);
			console.log(divs.dataset);
		</script>
	</body>
</html>

```

![[00 assets/873cb33cca583be8f87492ad800a7e67_MD5.png]]

当然假如我们使用多个-来连接的话，后面的名字就需要使用驼峰命名法

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
		<div id="" data-index = "20" data-list-one = "30"></div>
		<script type="text/javascript">
			var divs = document.querySelector('div');
			divs.setAttribute('data-time',2);
			console.log(divs.dataset.listOne);
			console.log(divs.dataset['listOne']);
			console.log(divs.dataset);
		</script>
	</body>
</html>

```

![[00 assets/7ee325d7bf6cd27bbfb4bdfe8044cd29_MD5.png]]

#### 12.7.1 获取自定义属性值

##### 12.7.1.1 元素.属性

当然我们也可以直接使用元素.属性来获取里面的属性值

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
		<div id="one">

		</div>

		<script type="text/javascript">
			var one_js = document.getElementById('one');
			console.log(one_js.id);
		</script>
	</body>
</html>

```

![[00 assets/6cdf0d97438944e706b189e616e2910f_MD5.png]]

##### 12.7.1.2 元素.getAttribute

当然我们也可以使用这个来获取属性值

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
		<div id="one" index='1'>

		</div>

		<script type="text/javascript">
			var one_js = document.getElementById('one');
			console.log(one_js.getAttribute('id'));
			console.log(one_js.getAttribute('index'));
		</script>
	</body>
</html>

```

![[00 assets/2e5fd2267c504a017122d4c3d8b4ed68_MD5.png]]

但是他个上一种方法肯定是有区别的，上面一种办法只能获取内置属性值，但是后面 getAttribute 是可以获取自定义属性，就是上面的 index，这是程序员自己设置的属性值

#### 12.7.2 设置自定义属性值

##### 12.7.2.1 元素.属性

这里可以参考，上面的 dom 的增删改->改

##### 12.7.2.2 元素.setAttribute

当然这个不仅和设置内置属性值，还可以设置自定义属性值

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
		<div id="one" index='1'>

		</div>

		<script type="text/javascript">
			var one_js = document.getElementById('one');
			one_js.setAttribute('id','two');
			one_js.setAttribute('index',2);
			console.log(one_js.getAttribute('id'));
			console.log(one_js.getAttribute('index'));
		</script>
	</body>
</html>

```

![[00 assets/e08a83531494ed2804b03ad70dc45d80_MD5.png]]

#### 12.7.3 移除自定义属性值

##### 12.7.3.1 元素.removeAttribute

当然他不仅可以删除内置属性值，还可以删除自定义属性值

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
		<div id="one" index='1'>

		</div>

		<script type="text/javascript">
			var one_js = document.getElementById('one');
			one_js.removeAttribute('id');
			one_js.removeAttribute('index');
			console.log(one_js.getAttribute('id'));
			console.log(one_js.getAttribute('index'));
		</script>
	</body>
</html>

```

![[00 assets/34d4afa275fe00bc0ee917355a6721c1_MD5.jpeg]]

### 12.5 DOM 案例

#### 12.5.1 图片的轮播

下面是设置图片轮播的代码

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			div{
				width: 280px;
				height: 402px;
				border: 10px solid darkslateblue;
				border-bottom: 35px solid darkslateblue;
				background-color: chocolate;
				/* 设置方块的居中 */
				margin: 0 auto;
				/* 设置按钮的居中 */
				text-align: center;
			}
		</style>
		<script>
			window.onload = function(){
				//先获取按钮的信息
				var left = document.getElementById("left");
				var right = document.getElementById("right");
				// 再获取图像的信息，方便修改
				var img = document.getElementsByTagName("img")[0];
				// 将图像的信息存储到数组中
				var imgArr = ["img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png"]
				var index = 0;
				// 当点击left的按钮的时候，进行的方法
				left.onclick = function(){
					index--;
					// 设置循环轮播的判断语句
					if(index < 0){
						index = imgArr.length - 1;
					}
					// 修改html里面的img1的值
					img.src = imgArr[index];
					// 设置提示文字
					info.innerHTML = "一共"+imgArr.length+"张图片,"+"当前是第"+(index+1)+"张图片"
				};

				right.onclick = function(){
					index++;

					if(index > imgArr.length - 1){
						index = 0;
					}

					img.src = imgArr[index];

					info.innerHTML = "一共"+imgArr.length+"张图片,"+"当前是第"+(index+1)+"张图片"
				};

				var info = document.getElementById("info");
				info.innerHTML = "一共"+imgArr.length+"张图片,"+"当前是第"+(index+1)+"张图片"
			}
		</script>
	</head>
	<body>
		<div>
			<p id="info">当前第5张</p>

			<img src="img/1.png" />

			<input type="button" id="left"value="上一个"/>
			<input type="button" id="right" value="下一个"/>
		</div>
	</body>
</html>
```

![[00 assets/f4dac6a61f93e11c865c31e1d1cd384b_MD5.jpeg]]

#### 12.5.2 分时显示图片

根据时间来显示不同的照片，同时显示不同的问候语

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>

		</style>
	</head>
	<body>
		<img src="img/1.png" >
		<div id="one">现在是美好的早上，来学习c语言吧</div>
		<div id="two">现在的时间</div>
		<script type="application/javascript">
			var img = document.querySelector('img');
			var div_one = document.getElementById('one');
			var div_two = document.getElementById('two');

			function getDate(){
				var time = new Date('2019-1-1 9:00:00');

				var h = time.getHours();
				var m = time.getMinutes();
				var s = time.getSeconds();

				if(h>=0&&h<11){
					div_one.innerHTML = '现在是美好的早上，来学习c语言吧';
					img.src = "img/1.png";
				}
				if(h>=11&&h<18){
					div_one.innerHTML = '现在是干活的中午，来学习c++吧';
					img.src = "img/2.png";
				}
				if(h>=18&&h<24){
					div_one.innerHTML = '现在是睡觉的晚上，来学习Java吧';
					img.src = "img/3.png";
				}

				div_two.innerHTML = h+'时'+m+'分'+s+"秒";
			}

			getDate();
		</script>
	</body>
</html>

```

![[00 assets/69a1413fe4fc5100aacf74b0abc5dae3_MD5.png]]

#### 12.5.3 仿京东显示隐藏密码

当然这只是一个思路，我们可以添加很多的效果

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			#pass{
				outline: none;
				border: 0px;
				border-bottom: 1px solid black;
			}
		</style>

	</head>
	<body>
		<input type="password" id="pass"/>
		<button id="btn">隐藏密码</button>
		<script type="application/javascript">
			var btn = document.getElementById('btn');
			var text = document.querySelector('input');
			var flag = 1;

			btn.onclick = function(){
				if(flag === 1){
					flag = 0;
					btn.innerHTML = '显示密码';
					text.type = "text";
				}
				else{
					flag = 1;
					btn.innerHTML = '隐藏密码';
					text.type = "password";
				}
			}
		</script>

	</body>
</html>

```

当你输入密码的话，是隐藏的

![[00 assets/d320388744d93475b3bb043fcfba692e_MD5.png]]

当你显示密码的话

![[00 assets/e5e010c4308d825e04353839af0b444f_MD5.png]]

#### 12.6.4 仿淘宝二维码样式

当你点击旁边的叉号就关闭二维码，下面的代码是简化的，但是思路是没有问题的

![[00 assets/53366f2b89b8f00f5386a252e31a61ea_MD5.png]]

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div id="imgs">
			<img src="img/1.png" >
		</div>
		<button id="btn">关闭</button>
		<script type="text/javascript">
			var btn = document.getElementById('btn');
			var imgs = document.getElementById('imgs');

			btn.onclick = function(){
				imgs.style.display = 'none';
				btn.style.display = 'none';
			}
		</script>
	</body>
</html>

```

原本的

![[00 assets/61a2342ad01176fc6f0c642977e65aab_MD5.png]]

假如你点击的话

![[00 assets/f34e54cee48ea411cbd7cc7e8a9579bf_MD5.png]]

#### 12.6.5 循环精灵图

![[00 assets/00f667f72af10b4afb1f70fc0afe2a14_MD5.png]]

以前用 css 来设置的话

![[00 assets/7db1f13cc6397f1e82eea11c8f773154_MD5.png]]

就要写一排代码

![[00 assets/5ac140a3564e6cfd8cec323316024d4d_MD5.png]]

但是现在就可以使用 JS 来简化

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#imgs{
				display: flex;
			}
			#imgs div{
				width: 64px;
				height: 64px;
				margin-left: 20px;
				background: url(./img/localnav_bg.png) no-repeat;
			}
		</style>
	</head>
	<body>
		<div id="imgs">
			<div></div>
			<div></div>
			<div></div>
			<div></div>
			<div></div>
		</div>
		<script type="text/javascript">
			var imgs = document.querySelectorAll('div');
			for(var i = 0;i<imgs.length;i++){
				var index = i * 64 - 64;
				imgs[i].style.backgroundPosition = '0px -'+index+'px';
			}
		</script>
	</body>
</html>

```

![[00 assets/8353da8f12304becc5c3029bab35deb6_MD5.png]]

#### 12.6.6 显示隐藏文本框内容

假如你点击搜索框的时候，里面的文本消失，假如你不点击的话，就会显示出来

![[00 assets/7c7e82fa6fc9f233ff19b9e5e408cde0_MD5.png]]

这里表单有 2 个新事件，获得焦点 onfocus，失去焦点 onblur

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			input{
				color: #999;
			}
		</style>
	</head>
	<body>
		<input type="text" value="输入" />
		<script type="text/javascript">
			var text = document.querySelector('input');
			text.onfocus = function(){
				if(text.value === '输入'){
					text.value = '';
				}
				text.style.color = '#333';
			}
			text.onblur = function(){
				if(text.value === ''){
					text.value = '输入';
				}
				text.style.color = '#999';
			}
		</script>
	</body>
</html>

```

当你有焦点的时候，也就是点击了输入文本框

![[00 assets/205819b1104283a0a8e9caad5231d316_MD5.png]]

当你没有焦点的时候，当不点击文本框

![[00 assets/3fae799b94a7f76e31c9fb87e753ca84_MD5.png]]

#### 12.6.7 文本框格式提示信息

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			#in {
				width: 400px;
				height: 23px;
				display: flex;
			}

			.divs {
				color: #999;
				margin-left: 10px;
			}

			#in input {
				color: #999;
			}

			.error {
				color: red;
				margin-left: 10px;
			}
		</style>
	</head>
	<body>
		<div id="in">
			<input type="text" value="账号" />
			<div class="divs">请输入6-16位字符</div>
		</div>

		<script type="text/javascript">
			var inp = document.querySelector('input');
			var divs = document.querySelector('.divs');

			inp.onfocus = function(){
				if(inp.value === '账号'){
					inp.value = '';
				}
			}

			inp.onblur = function() {

				if (inp.value.length <= 5 || inp.value.length >= 17) {
					divs.innerText = '你输入的是错误的';
					divs.className = 'error';
				}
				else{
					divs.innerText = '请输入的是正确的';
					divs.className = 'divs';
				}
			}
		</script>
	</body>
</html>

```

假如你输入的数字是小于 6 的话

![[00 assets/abda708326d223bd001d7f5e7bad3c2d_MD5.png]]

假如你输入的数字在范围内的话

![[00 assets/ffdc9c582af514a29bf05ff2a682e036_MD5.png]]

#### 12.7.8 百度换肤

这里是对于上面的排他思想的案例，下面点击按钮切换到相应的图片

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			body{
				background: url(img/bg1.jpg) no-repeat;
				background-size: 100%;
			}
		</style>
	</head>
	<body>
		<button>1</button>
		<button>2</button>
		<button>3</button>
		<button>4</button>
		<button>5</button>

		<script type="text/javascript">
			var btns = document.getElementsByTagName('button');
			for(var i =0 ; i<btns.length ; i++){
				btns[i].onclick = function(){
					for(var j = 0;j<btns.length ;j++){
						btns[j].style.backgroundColor = '';
					}
					this.style.backgroundColor = '#888';
					document.body.style.backgroundImage = 'url(img/bg'+ this.innerHTML +'.jpg)';
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/31de1b056283ff3a850c0f04ae9c3dc3_MD5.png]]

同时在做这个案例的时候发现一些问题，不要以为是 for 循环循环向下走，到了你点击的 onclick 的按钮，就执行下面的 function，结果不是这样的，你再输入 i 的值话就是 5，也就是长度，也可能对于这个理解错了，而且在这里 btn[i]也失效了，到时候有时间了看下

#### 12.7.9 表格隔行变色

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			table{
				border: 1px solid #999;
				width: 400px;
				border-collapse: collapse;
			}
			table tr{border-bottom: 1px solid #999;}
			table td{text-align: center;}
		</style>
	</head>
	<body>
		<table>
			<tr>
				<th>代号</th>
				<th>人物</th>
				<th>年龄</th>
				<th>性别</th>
			</tr>
			<tr>
				<td>001</td>
				<td>孙悟空</td>
				<td>18</td>
				<td>男</td>
			</tr>
			<tr>
				<td>002</td>
				<td>八戒</td>
				<td>20</td>
				<td>男</td>
			</tr>
			<tr>
				<td>003</td>
				<td>沙和尚</td>
				<td>30</td>
				<td>男</td>
			</tr>
			<tr>
				<td>004</td>
				<td>唐僧</td>
				<td>20</td>
				<td>男</td>
			</tr>
		</table>

		<script type="text/javascript">
			var trs = document.getElementsByTagName('tr');
			for(var i=0;i<trs.length;i++){
				trs[i].onmouseover = function(){
					this.style.backgroundColor = 'pink';
				}
				trs[i].onmouseout = function(){
					this.style.backgroundColor = '';
				}
			}
		</script>
	</body>
</html>

```

鼠标放在那里，那里就变色

![[00 assets/926963b45001823437504e809d0f1a42_MD5.png]]

#### 12.7.10 表格全选

下面也包含了上面的表格变色的部分

首先有一个对于上面的理解，我一直以为是 for 循环检查 input 有没有按过，按过就检查后面的函数，但是其实不是，这里是通过 for 循环给按钮绑定了函数，但是不检查 onclick，就相当于写 5 个 onclick 的函数

然后就是下面因为我设置 ins 和 trss 的问题，trss 是有 ins 的，所有在第三个会有点问题，因为 ins 也就是 trss[0]也绑定了全选的函数，所有也会纳入检查的范围，这时你就会发现，你点击不了全选，其实你已经点击了，但是在后面的检查发现还有没点的，就默认为 false，所有全选就会失效

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			table{
				border: 1px solid #999;
				width: 400px;
				border-collapse: collapse;
			}
			table tr{border-bottom: 1px solid #999;}
			table td{text-align: center;}
		</style>
	</head>
	<body>
		<table>
			<tr>
				<th>代号</th>
				<th>人物</th>
				<th>年龄</th>
				<th>性别</th>
				<td>
					<input type="checkbox"/>
				</td>
			</tr>
			<tr>
				<td>001</td>
				<td>孙悟空</td>
				<td>18</td>
				<td>男</td>
				<td>
					<input type="checkbox" />
				</td>
			</tr>
			<tr>
				<td>002</td>
				<td>八戒</td>
				<td>20</td>
				<td>男</td>
				<td>
					<input type="checkbox" />
				</td>
			</tr>
			<tr>
				<td>003</td>
				<td>沙和尚</td>
				<td>30</td>
				<td>男</td>
				<td>
					<input type="checkbox" />
				</td>
			</tr>
			<tr>
				<td>004</td>
				<td>唐僧</td>
				<td>20</td>
				<td>男</td>
				<td>
					<input type="checkbox" />
				</td>
			</tr>
		</table>

		<script type="text/javascript">
			var trs = document.getElementsByTagName('tr');
			for(var i=1;i<trs.length;i++){
				trs[i].onmouseover = function(){
					this.style.backgroundColor = 'pink';
				}
				trs[i].onmouseout = function(){
					this.style.backgroundColor = '';
				}
			}

			var ins = document.querySelector('tr td input:nth-child(1)');
			var trss = document.querySelectorAll('tr input');
			ins.onclick = function(){
				console.log(this.checked)
				for(var i=1;i<trs.length;i++){
					trss[i].checked = this.checked;
				}
			}

			for(var i=1;i<trss.length;i++){
				trss[i].onclick = function(){
					var flag = true;
					for(var i=1;i<trss.length;i++){
						if(!trss[i].checked){
							flag = false;
							break;
						}
					}
					ins.checked = flag;
				}
			}
		</script>
	</body>
</html>

```

#### 12.7.11 tab 栏切换布局

这是一个很重要的一个 JS 案例，就是你点击一个按钮的话，就会显示相应的内容，这个案例主要的是使用自定义函数 index，然后再使用 getAttribute 来获取 index 的值，然后再更改相应的内容的 display 的值

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#tab{
				width: 70%;
				height: 40px;
				border: 1px solid red;
				display: flex;
				justify-content: space-around;
			}
			#tab div{
				height: 40px;
				background-color: burlywood;
				line-height: 40px;
			}
			.content div{
				display: none;
			}
			#curr_two{
				display: block;
			}
		</style>
	</head>
	<body>
		<div id="main">
			<div id="tab">
				<div class="curr_one" index='0'>商品介绍</div>
				<div index='1'>规格和包装</div>
				<div index='2'>售后保障</div>
				<div index='3'>商品评价</div>
				<div index='4'>手机社区</div>
			</div>
			<div class="content">
				<div id="curr_two" index='0'>这是一个好东西</div>
				<div index='1'>它好重啊</div>
				<div index='2'>保障一生</div>
				<div index='3'>这很好</div>
				<div index='4'>别买，这是什么东西，都别买</div>
			</div>
		</div>
		<script type="text/javascript">
			var tabs = document.querySelectorAll('#tab div');
			var cons = document.querySelectorAll('.content div');
			for(var i=0;i<tabs.length;i++){
				tabs[i].onclick = function(){
					for(var i=0;i<tabs.length;i++){
						tabs[i].style.backgroundColor = '';
					}
					this.style.backgroundColor = 'red';

					var flag = this.getAttribute('index');
					for(var i=0;i<tabs.length;i++){
						cons[i].style.display = 'none';
					}
					cons[flag].style.display = 'block';
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/dccf11896543ff4e3b3f4927cb1710d3_MD5.png]]

#### 12.7.12 新浪下拉菜单

当你的鼠标悬浮在一个标记上面的时候，就会显示下面的内容

下面的样式不是很好看，但是思路就是这样的

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.one {
				display: flex;
				justify-content: space-around;
			}
			.two ul li {list-style: none;}
			.two {list-style: none;}
			.two a {margin-left: 45px;}
			a {
				text-decoration: none;
				color: black;
				background-color: burlywood;
			}
			a:link {text-decoration: none;}
			a:visited {text-decoration: none;}
			a:hover {text-decoration: none;}
			a:active {text-decoration: none;}

		</style>
	</head>
	<body>
		<ul class="one">
			<li class="two">
				<a href="#">点击</a>
				<ul>
					<li>这是第一个哦</li>
					<li>这不是第一个哦</li>
					<li>这肯定是第一个哦</li>
				</ul>
			</li>

			<li class="two">
				<a href="#">点击</a>
				<ul>
					<li>这是第一个哦</li>
					<li>这不是第一个哦</li>
					<li>这肯定是第一个哦</li>
				</ul>
			</li>

			<li class="two">
				<a href="#">点击</a>
				<ul>
					<li>这是第一个哦</li>
					<li>这不是第一个哦</li>
					<li>这肯定是第一个哦</li>
				</ul>
			</li>
		</ul>

		<script type="text/javascript">
			var nav = document.querySelector('.one');
			var lis = nav.children;
			for(var i=0;i<lis.length;i++){
				lis[i].onmouseover = function(){
					this.children[1].style.display = 'block';
				}
				lis[i].onmouseout = function(){
					this.children[1].style.display = 'none';
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/9f648ae893ffcf21d68d98a894d68b4e_MD5.png]]

#### 12.7.13 简单版的发布留言

下面是一个简单的发布留言的代码，你在文本框输入字符，再发布的话就会在下面显示

下面有 2 个版本，一个是发布在前面的，一个是发布在后面的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			input{
				width: 300px;
				height: 300px;
			}
		</style>
	</head>
	<body>
		<input type="text" />
		<button>提交</button>
		<ul></ul>
		<script type="text/javascript">
			var btn = document.querySelector('button');
			var inp = btn.previousElementSibling;
			var ul = btn.nextElementSibling;

			btn.onclick = function(){
				var str = inp.value;
				var li = document.createElement('li');
				li.innerHTML = str;
				// ul.insertBefore(li,ul.children[0]);
				ul.appendChild(li);
			}

		</script>
	</body>
</html>

```

![[00 assets/8bb3ade07b90fa0ae9ca23a4304ee905_MD5.png]]

#### 12.7.14 删除留言

这个也是承接上面的发布留言的代码

但是这里有一个很关键的点 ul.removeChild(this.parentNode); 就是这个代码，首先是 ul 为父节点，然后 a 标签的父节点是 li，这样的话就找到了要删除的那个 li

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			input{
				width: 300px;
				height: 300px;
			}
		</style>
	</head>
	<body>
		<input type="text" />
		<button>提交</button>
		<ul></ul>
		<script type="text/javascript">
			var btn = document.querySelector('button');
			var inp = btn.previousElementSibling;
			var ul = btn.nextElementSibling;

			btn.onclick = function(){
				var str = inp.value;
				var li = document.createElement('li');
				li.innerHTML = str + '<a href="javascript:;">删除</a>';
				ul.appendChild(li);
				var as = document.querySelectorAll('a');
				for(var i =0;i<as.length;i++){
					as[i].onclick = function(){
						ul.removeChild(this.parentNode);
					}
				}
			}
		</script>
	</body>
</html>

```

后记：为啥我把删除的代码移动到 onclick 外面的话就会失效

因为放在外面的话就会被优先执行，新生成的 a 就不能绑定事件了，就删除不掉

#### 12.7.15 动态生成表格

第一步中，下面有 2 个方式来创建对象，一个是使用字面量创建，一个是使用构造函数创建，并且作为 data 得数组，我下面使用得是构造函数生成

还有就是在创建得时候要注意逻辑顺序

在这个得第六步里面，得逻辑关系不是很好，在实际开发中要准确得去获取 a 得标签

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			table {width: 300px;}
			a {
				text-decoration: none;
				color: blueviolet;
			}
			a:link {text-decoration: none;}
			a:visited {text-decoration: none;}
			a:hover {text-decoration: none;}
			a:active {text-decoration: none;}
		</style>
	</head>
	<body>
		<table border="1px" cellspacing="0px" cellpadding="0px">
			<thead>
				<tr id="thead">
					<th>姓名</th>
					<th>科目</th>
					<th>成绩</th>
					<th>操作</th>
				</tr>
			</thead>
			<tbody></tbody>
		</table>

		<script type="text/javascript">
			//第一步 创建数据
			function newobj(name, subject, score) {
				this.name = name;
				this.subject = subject;
				this.score = score;
			}
			var obj1 = new newobj('张三', 'c语言', 98)
			var obj2 = new newobj('李四', 'c++语言', 78)
			var obj3 = new newobj('王五', 'c#语言', 88)
			var obj4 = new newobj('老六', 'c语言', 99)
			var data = [obj1, obj2, obj3, obj4];

			//第二步 创建行
			var tbody = document.querySelector('tbody');
			for (var i = 0; i < data.length; i++) {
				var trs = document.createElement('tr');
				tbody.appendChild(trs);

				//第三步 创建单元格
				for (var k in data[i]) {
					var tds = document.createElement('td');
					trs.appendChild(tds);

					//第四步 插入数据
					tds.innerHTML = data[i][k];
				}
				//第五步 删除节点得设置
				var deltd = document.createElement('td');
				deltd.innerHTML = '<a href="javascript:;">删除</a>'
				trs.appendChild(deltd);
			}
			//第六步 设置删除节点
			var as = document.querySelectorAll('a');
			for(var i =0;i<as.length;i++){
					as[i].onclick = function(){
					tbody.removeChild(this.parentNode.parentNode);
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/56889dc55fd0a06e0658bc1a125778d2_MD5.png]]

## 13. 事件

### 13.1 事件的三要素

事件是有三个部分组成，事件源、事件类型、事件处理程序

**事件源**：事件被触发的对象

```html
var btn = document.getElementById("one");
```

**事件类型：**如何触发，比如：鼠标点击，鼠标经过，键盘按下

**事件处理程序：**通过一个函数来处理

下面是就是一个事件的基础的三个元素

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<button id="one">点我</button>

		<script type="text/javascript">
			var btn = document.getElementById("one");

			btn.onclick = function(){
				alert("点我干什么");
			};
		</script>
	</body>
</html>
```

当然假如我们想要创建一个事件的话

1.获取事件源

2.注册事件

3.添加事件处理程序

### 13.3 注册事件得两种方式

#### 13.3.1 传统方式

![[00 assets/49d789bd91dabed952028070091dc6ae_MD5.jpeg]]

这里得事件得唯一性就是只能使用一个处理函数，一般都是选择后定义得

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
			var btn = document.querySelector('button');
			btn.onclick = function(){
				alert("1");
			}
			btn.onclick = function(){
				alert("2");
			}
		</script>
	</body>
</html>

```

![[00 assets/df720a48304ecebbcde640401181b9de_MD5.png]]

#### 13.3.2 方法监听注册方式

##### 13.3.2.1 addEventListener

同一个元素得同一个事件可以注册多个监听器，会按注册依次处理

![[00 assets/31682b0e941cc2fa86fdf2dcd0d7be39_MD5.png]]

下面是使用监听得方式来创建，但是这个方式只有 IE9 以上才支持

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
			var btn = document.querySelector('button');
			btn.addEventListener('click',function(){
				alert('1');
			})
			btn.addEventListener('click',function(){
				alert('2');
			})
		</script>
	</body>
</html>

```

![[00 assets/477531154235fee7c41e25fd2a07a170_MD5.png]]

![[00 assets/3e6c731fb0abdaa9721d02457ea4c089_MD5.png]]

但是这个方法的兼容性不是很好，所以就有下面的兼容性的解决办法

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
		<script type="text/javascript">
			function addEventListener(element,eventName,fn){
				if(element.addEventListener){
					element.addEventListener(eventName,fn);
				}
				else if(element.attachEvent){
					element.attachEvent('on'+eventName,fn);
				}
				else{
					element['on'+eventName] = fn;
				}
			}
		</script>
	</body>
</html>

```

##### 13.3.2.1 attachEvent

这个 IE9 以下版本支持，而且这个不是标准的，尽量不去使用，因为现在大部分浏览器都支持上面的方法，实在不行就使用传统方法来解决

![[00 assets/723befab24f3b3dc7f4045777c4c9629_MD5.png]]

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
			var btn = document.querySelector('button');
			btn.attachEvent('onclick',function(){
				alert('1');
			})
			btn.attachEvent('onclick',function(){
				alert('2');
			})
		</script>
	</body>
</html>

```

![[00 assets/0934877a891cabbadbd7243c5521096f_MD5.png]]

### 13.3 删除事件

#### 13.3.1 传统解绑方式

就是将事件的设置为 null 就可以了，下面的代码指的是你只能点击一次，你点击第二次的话就没有对话框了

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>

		<script type="text/javascript">
			var divs = document.querySelectorAll('div');
			for(var i=0;i<divs.length;i++){
				divs[i].onclick = function(){
					alert(this.innerHTML);
					this.onclick = null;
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/393ca42644bdcfb0693323490f9d9187_MD5.png]]

#### 13.3.2 方法监听解绑方式

##### 13.3.2.1 removeEventListener

这个是监听解绑，这里有一个要注意的点，既然要删除一个事件，是不是要知道要删除那个函数，但是我们以前用的都是匿名函数，所以以前的方式是不行的，这里就在外面设置一个有名的函数

但是这里还有一个要注意的点，使用的时候必须使用函数名，但是并不是调用它，我们删除只需要知道它的名字就可以了，不需要知道它是干什么的

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>

		<script type="text/javascript">
			var divs = document.querySelectorAll('div');
			for(var i=0;i<divs.length;i++){
				divs[i].addEventListener('click',fn);
				function fn(){
					alert(this.innerHTML);
					this.removeEventListener('click',fn);
				}
			}
		</script>
	</body>
</html>

```

![[00 assets/5144e489d3c032be9fdc6575b7f97c8f_MD5.png]]

##### 13.3.2.2 detachEvent

假如你使用的是 attachEvent 的话，就要使用这个方式来解绑

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>

		<script type="text/javascript">
			var divs = document.querySelectorAll('div');
			for(var i=0;i<divs.length;i++){
				divs[i].addEventListener('click',fn);
				function fn(){
					alert(this.innerHTML);
					this.removeEventListener('click',fn);
				}
			}
		</script>
	</body>
</html>

```

### 13.4 DOM 事件流

事件流描述的是页面中接收事件的顺序

事件发生时会在元素节点之间按照特定的顺序传播，这个传播过程就是 DOM 事件流

![[00 assets/13f205afea60b0074b1994b84f5e05d0_MD5.png]]

![[00 assets/7c5d637b69c2ed9b752fc1cb07abbc00_MD5.png]]

JS 代码只能执行捕获或者冒泡其中一个阶段，并且 onclick 和 attachEvent 只能得到冒泡阶段，但是 onblur、onfocus、onmouseenter、onmouseleave 就没有事件冒泡

addEventListener 的第三个参数如果时 true 的话，表示事件处于捕获阶段调用事件处理程序，如果时 false 的话，表示事件冒泡阶段调用事件处理程序

下面代码演示的是**捕获阶段**，假如你点击的是父元素的话，就是显示的是 father 的提示，假如你点击的是子元素的话，就会显示的是 son 的提示，这是因为事件的捕获，首先是检查 document，html，body，father，son，当检查到 father 的时候就会因为执行点击的事件，然后再检查子元素，子元素就会执行点击事件

并且要注意的是要子元素和父元素都设置 true 才可以，不然还是冒泡阶段

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#father{
				width: 200px;
				height: 200px;
				background-color: burlywood;
			}
			#son{
				width: 100px;
				height: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div id="father">
			<div id="son"></div>
		</div>

		<script type="text/javascript">
			var son = document.querySelector('#son');
			var father = son.parentNode;
			son.addEventListener('click',function(){
				alert('son');
			},true);
			father.addEventListener('click',function(){
				alert('father')
			},true);
		</script>
	</body>
</html>

```

![[00 assets/c1bb0caf4ac69842c80346831da4301c_MD5.jpeg]]

下面演示的是冒泡阶段，你点击之后就从子元素冒泡到 document，并且我们再实际开发时候很少使用事件捕获，我们更加关注事件冒泡

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#father{
				width: 200px;
				height: 200px;
				background-color: burlywood;
			}
			#son{
				width: 100px;
				height: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div id="father">
			<div id="son"></div>
		</div>

		<script type="text/javascript">
			var son = document.querySelector('#son');
			var father = son.parentNode;
			son.addEventListener('click',function(){
				alert('son');
			});
			father.addEventListener('click',function(){
				alert('father')
			});
		</script>
	</body>
</html>
```

![[00 assets/d357860c71817af46d33a88e5042de26_MD5.png]]

![[00 assets/c437a1e7dc397525b22bc1c6bf25d495_MD5.png]]

### 13.5 事件对象

当事件响应函数被触发的时候，浏览器每次都会将一个事件作为实参传递进响应函数，并且是系统给我们自动创建的

在事件对象中封装了当前事件相关的一切信息，比如：鼠标的坐标，键盘按下那个键，鼠标滚轮方向......

下面的 event 就是事件对象

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div>123</div>

		<script type="text/javascript">
			var div = document.querySelector('div');
			div.onclick = function(event){
				console.log(event);
			}
		</script>
	</body>
</html>
```

![[00 assets/6638a10530514e928ae0632b0a3f9438_MD5.png]]

事件对象也是有兼容性问题，在 IE678 只知道 window.event，这里我们就可以使用兼容性写法

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div>123</div>

		<script type="text/javascript">
			var div = document.querySelector('div');
			div.onclick = function(event){
				console.log(event||window.event);
			}
		</script>
	</body>
</html>

```

#### 13.5.1 事件对象的属性

![[00 assets/9f0a609d0438b4637069b84d22368d04_MD5.png]]

##### 13.5.1.1 target

返回触发事件的对象，标准

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div>123</div>

		<script type="text/javascript">
			var div = document.querySelector('div');
			div.addEventListener('click',function(e){
				console.log(e.target);
			})
		</script>
	</body>
</html>

```

![[00 assets/85a542efe089888200c5591ef4e14bc6_MD5.png]]

这里会发现，是不是和 this 很像，但是 targrt 是返回触发事件的对象，this 放回的是绑定事件的对象

下面演示的我都是点击的是标签 1，来显示的结果

下面是 target 的演示

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			var lis = ul.children;

			ul.addEventListener('click',function(e){
				console.log(e.target);
			})
		</script>
	</body>
</html>

```

![[00 assets/5c93921dc358145bb9d4b5f3a76f941a_MD5.png]]

下面是 this 的显示

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			var lis = ul.children;

			ul.addEventListener('click',function(e){
				console.log(this);
			})
		</script>
	</body>
</html>

```

![[00 assets/d6dbacbed904abea54d1bef47e33cb32_MD5.png]]

发现没，这就是 this 和 target 的区别，target 是点击那个就是那个，this 就是返回绑定的那个

##### 13.5.1.2 currentTarget

这个和上面显示的 this 是差不多的，也是执行事件之后就返回绑定的那个，但是存在兼容性问题，ie678 是不支持的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			var lis = ul.children;

			ul.addEventListener('click',function(e){
				console.log(e.currentTarget);
			})
		</script>
	</body>
</html>
```

![[00 assets/de5a149c1e68c113b6b8699d0744713d_MD5.png]]

##### 13.5.1.3 type

返回事件类型

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			var lis = ul.children;

			ul.addEventListener('click',function(e){
				console.log(e.type);
			})
		</script>
	</body>
</html>

```

![[00 assets/64de9835456b6510c9a7e0421851a707_MD5.jpeg]]

#### 13.5.2 事件对象的方法

##### 13.5.2.1 组织默认行为

组织默认行为，就是让事件不跳转或者不提交

下面的代码就不会跳转到百度，假如你把 preventDefault()去掉的话，在点击按钮的话就会跳转

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<form action="http://www.baidu.com" method="post">
			<input type="submit" value="提交"/>
		</form>

		<script type="text/javascript">
			var inp = document.querySelector('input');
			inp.addEventListener('click',function(e){
				e.preventDefault();
			})
		</script>
	</body>
</html>

```

![[00 assets/ff229e6e449c84c7c66566ef694164c7_MD5.png]]

下面是一个兼容性的写法，支持 IE678，下面要注意的一个问题，第一个是方法，第二个是属性

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<form action="http://www.baidu.com" method="post">
			<input type="submit" value="提交"/>
		</form>

		<script type="text/javascript">
			var inp = document.querySelector('input');
			inp.onclick = function(e){
				e.preventDefault();
				e.returnValue;
			}
		</script>
	</body>
</html>

```

但是我们还有一个兼容所有浏览器的方法，但是这个方式有一个毛病，就是 return 后面的语句都不会执行

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<form action="http://www.baidu.com" method="post">
			<input type="submit" value="提交"/>
		</form>

		<script type="text/javascript">
			var inp = document.querySelector('input');
			inp.onclick = function(e){
				return false;
			}
		</script>
	</body>
</html>
```

##### 13.5.2.2 阻止事件冒泡

这个方法是阻止冒泡

但是这里设置传播的不一样，传播时都设置为 true 才可以，但是这个只要设置起始的冒泡就可以了，直接切断的时源头，所以就不会向上冒泡

并且要注意一个问题，你使用传统方法来来创建的话，就不能正常使用 stopPropagation()，但是假如你使用广播的方式话，就可以

并且 ie678 不支持

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#father{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
			#son{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
	</head>
	<body>
		<div id="father">
			<div id="son"></div>
		</div>

		<script type="text/javascript">
			var father = document.querySelector('#father');
			var son = document.querySelector('#son');
			son.addEventListener('click',function(e){
				e.stopPropagation();
				alert('son');
			})
			father.addEventListener('click',function(e){
				alert('father');
			})
			document.addEventListener('click',function(){
				alert('document');
			})
		</script>
	</body>
</html>

```

![[00 assets/1712ceca8d5d679715dd6f0119a1749f_MD5.png]]

假如你想考虑兼容性的话，就要使用 cancelBubble

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#father{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
			#son{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
	</head>
	<body>
		<div id="father">
			<div id="son"></div>
		</div>

		<script type="text/javascript">
			var father = document.querySelector('#father');
			var son = document.querySelector('#son');
			son.onclick = function(e){
				alert('son');
				if(e&&e.stopPropagation){
					e.stopPropagation();
				}
				else{
					window.event.cancelBubble = true;
				}
			}
			father.onclick = function(){
				alert('father');
			}
			document.onclick = function(){
				alert('document');
			}
		</script>
	</body>
</html>

```

![[00 assets/1f1176a6df93f10b6613f35ed59e136c_MD5.png]]

#### 13.3.1 常见的鼠标事件

![[00 assets/5433d642d55f2156c3da72e96f7da662_MD5.png]]

##### 13.3.1.1 contextmenu

是设置右键开关的

下面就的代码就是设置右键开关的关闭

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div>你右键不了我哦</div>

		<script type="text/javascript">
			document.addEventListener('contextmenu',function(e){
				e.preventDefault();
			})
		</script>
	</body>
</html>

```

![[00 assets/e3b4a1961caa59ebf95a0e3163120c33_MD5.png]]

##### 13.3.1.2 selectstart

下面是禁止鼠标选中的代码

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<div>你选中不了我哦</div>

		<script type="text/javascript">
			document.addEventListener('selectstart',function(e){
				e.preventDefault();
			})
		</script>
	</body>
</html>

```

![[00 assets/6292625a6d82489e76099542e4a2d39f_MD5.png]]

##### 13.3.1.3 鼠标在页面中的值

![[00 assets/a2cd033835999d7db2770deff61677dc_MD5.png]]

下面就是显示鼠标点击之后返回的值

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<script type="text/javascript">
			document.addEventListener('click',function(e){
				console.log(e);
			})
		</script>
	</body>
</html>

```

![[00 assets/2eb312cb42b0215d4f1fad20fb89bf36_MD5.png]]

并且要注意的是 clientX 和 clientY 是可视区的的值，红线左边的就是可视区

![[00 assets/fa41e82b8faa6ed2543f93e5d7bd9aee_MD5.png]]

但是我们有的页面是很长的，所有就是 pageX 和 pageY 来获取

##### 13.3.1.4 mouseenter 和 mouseover

![[00 assets/4c74b1cfb584e976d293e427878e418f_MD5.png]]

其实本质是 mouseover 不会冒泡

我们来看下面案例，你从左边移动到右边的话，是不是执行了 2 次语句输出

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.father{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
			.son{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>

		<script type="text/javascript">
			var father = document.querySelector('.father');
			father.addEventListener('mouseover',function(){
				console.log('滑动过去了');
			})
		</script>
	</body>
</html>

```

![[00 assets/cadda16428b122ff4d337d1a805f0f61_MD5.png]]

我们再来看下面的案例，一样的滑动，是不是最后只有一次显示

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.father{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
			.son{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>

		<script type="text/javascript">
			var father = document.querySelector('.father');
			father.addEventListener('mouseenter',function(){
				console.log('滑动过去了');
			})
		</script>
	</body>
</html>

```

![[00 assets/8a1351b1550111a6868831db3ffd79b0_MD5.png]]

#### 13.3.1 常见的键盘事件

![[00 assets/1801d2c34a19d0b82da44b2e3a13b176_MD5.png]]

下面就是常见的键盘事件，当你点击按下后松开就触发，还有一个是按下就触发

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div></div>
		<script type="text/javascript">
			var div = document.querySelector('div');
			document.addEventListener('keyup',function(e){
				div.style.backgroundColor = 'red';
			})
			document.addEventListener('keydown',function(e){
				div.style.backgroundColor = 'blue';
			})
		</script>
	</body>
</html>

```

![[00 assets/79cbe18acc0eae59f34b6afe7fbd1285_MD5.png]]

但是这里是不是要怀疑，为什么会设置 2 个键呢，这是因为 keypress 是不能识别功能键的

还有一个问题，就是永远优先执行的是 keydown，不管是不是在前面

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>

		<script type="text/javascript">
			document.addEventListener('keyup',function(e){
				console.log('keyup');
			})
			document.addEventListener('keypress',function(e){
				console.log('keypress');
			})
			document.addEventListener('keydown',function(e){
				console.log('keydown');
			})
		</script>
	</body>
</html>

```

![[00 assets/dc15ffebce345d76df334d7a1e9d56c7_MD5.png]]

还有一个区别，就是 keyup 和 keydown 是不区分大小写的，keypress 是区分大小写，可以参考下面

##### 13.3.1.1 keyCode

这个就是获得相应的 ASCII 码值

下面就是点击了键盘上面的 a，但是返回的是 65，也就是 A 的 ASCII 码的值，这是因为 keyup 和 keydown

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>

		<script type="text/javascript">
			document.addEventListener('keyup',function(e){
				console.log(e.keyCode);
			})
		</script>
	</body>
</html>

```

![[00 assets/fb40f0ca8f2ee62848e6a27d7b0d08c6_MD5.png]]

但是 keyperss 是区分大小写的，下面就是按下的是 a

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>

		<script type="text/javascript">
			document.addEventListener('keypress',function(e){
				console.log(e.keyCode);
			})
		</script>
	</body>
</html>

```

![[00 assets/6cab1db6151975024b702d8941eca1ca_MD5.png]]

### 13.6 事件的委派

事件冒泡会带来坏处，同时也可以带来好处，生活中的场景如下

![[00 assets/c8383949d6358324b0bd57539bc15a5b_MD5.png]]

当然在程序里面场景如下

![[00 assets/28a4e1e684f2124dfe2a6f4f4efa4f73_MD5.png]]

事件委托也称为事件代理，在 jQuery 里面称为事件委派

**事件委托的原理**(很重要，要能口述出来)

不是每个子节点单独设置事件监听器，而是将事件监听器设置到父节点上，然后利用冒泡原理影响设置每个子节点

刚刚的案例，给 ul 注册点击事件，然后利用事件对象的 targrt 来找到当前点击的 li，因为点击 li，事件会冒泡到 ul 上，ul 有注册事件，就会触发事件监听器

我们只操作了一次 DOM，程序的性能提高了很多

我们来解释一下下面的代码，我们没有设置 li，但是我们还是操作了 li，这就是因为事件委托，你点击了 li 之后，就会从 li 往上面冒泡，因为 li 没设置 onclick 的点击事件，所以不会执行，但是父元素 ul 会执行点击事件，然后再使用 e.target 来准确到那个 li，然后再对这个 li 进行操作

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#father{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
			#son{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
	</head>
	<body>
		<ul>
			<li>这是第1个li</li>
			<li>这是第2个li</li>
			<li>这是第3个li</li>
		</ul>

		<script type="text/javascript">
			var ul = document.querySelector('ul');
			ul.addEventListener('click',function(e){
				alert(e.target.innerHTML);
				e.target.style.backgroundColor = 'pink';
			})
		</script>
	</body>
</html>

```

![[00 assets/03ba4c1105cea18b82d278cfb7b3a8cd_MD5.png]]

![[00 assets/4ba44db55ec1a4690cdab18445ffd538_MD5.png]]

### 13.8 事件案例

#### 13.8.1 跟随鼠标

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
				background-color: pink;
				position: absolute;
				top: 0px;
				left: 0px;
			}
		</style>
	</head>
	<body>
		<div></div>
		<script type="text/javascript">
			var div = document.querySelector('div');
			div.addEventListener('mousemove',function(e){
				var x = e.pageX;
				var y = e.pageY;
				this.style.top = x - 50 + 'px';
				this.style.left = y - 50 + 'px';
			})
		</script>
	</body>
</html>

```

![[00 assets/4ceddc4768ec0fdeba6e785173e7f387_MD5.png]]

#### 13.8.2 按键输入案例

当你点击 s 的时候，就把光标定位到搜索框

这里有一个小细节，不能使用 keydown，这是因为，你看下后就执行，然后就会执行聚焦，然后 s 就会将 s 输入打搜索框

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<input type="text" />
		<script type="text/javascript">
			var inp = document.querySelector('input');
			document.addEventListener('keyup',function(e){
				if(e.keyCode === 83){
					inp.focus();
				}
			})
		</script>
	</body>
</html>

```

![[00 assets/a34f6818d774aa207e7ecc440a6df5c7_MD5.png]]

#### 13.8.3 模拟快递单号

输入单号之后就会在上面显示一个放大版本

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.big{
				font-size: 20px;
				width: 170px;
				height: 40px;
				background-color: pink;
				line-height: 40px;

				display: none;
			}
			.big::before{
				content: '';
				width: 0px;
				height: 0px;
				position: absolute;
				top: 48px;
				left: 30px;
				border: 8px solid #FFC0CB;
				border-style: solid dashed dashed;
				border-color: #FFC0CB transparent transparent;
			}
			input{
				margin-top: 10px;
			}
		</style>
	</head>
	<body>
		<div class="big"></div>
		<input type="text" placeholder="请输入你的快递单号"/>
		<script type="text/javascript">
			var inp = document.querySelector('input');
			var div = document.querySelector('.big');
			inp.addEventListener('keyup',function(){
				if(this.value == ''){
					div.style.display = 'none';
				}
				else{
					div.style.display = 'block';
					div.innerText = this.value;
				}
			})
			inp.addEventListener('blur',function(){
				div.style.display = 'none';
			})
			inp.addEventListener('focus',function(){
				if(this.value !== ''){
					div.style.display = 'block';
				}
			})
		</script>
	</body>
</html>

```

![[00 assets/d17dbca848ace22d953410b6afefa759_MD5.png]]

但是有没有疑问，**为什么不去使用 keydown 和 keypress**

这是因为键盘上面的字是键盘弹起之后才输入的，但是 keydown 和 keypress 是按下之后就执行这个函数，字还没进去，所以就会有一个词的差距

## 14. BOM

### 14.1 BOM 概述

#### 14.1.1 BOM

BOM 就是浏览器对象模型，它是独立于内容而与浏览器窗口进行交互的对象，其核心对象就是 window

BOM 是由一系列相关的对象构成，并且每个对象都提供了很多方法和属性

但是有一个问题，BOM 缺乏标准，JS 的语法标准是 ECMA，DOM 标准是 W3C，但是 BOM 最初是网景公司标准的一部分

![[00 assets/a8f2ddc4e2a69af4a47809e615c0e864_MD5.png]]

#### 14.1.2 BOM 的构成

![[00 assets/3ed1975c847991a52d2d127f7d4dc6da_MD5.png]]

window 对象是浏览器的顶级对象，它不仅是 JS 访问浏览器窗口的一个**接口**，而且它是一个全局变量，定义在全局作用域中的变量、函数都会变成 window 对象的**属性和方法**

但是我们可以省略，而且前面的 alert()，prompt()都是 BOM 的一部分

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>

		<script type="text/javascript">
			var w1 = 100;
			console.log('我没写window:'+w1);
			console.log('我写了window:'+window.w1);

			function f1(){
				console.log('200');
			}
			f1();
			window.f1();
		</script>
	</body>
</html>

```

![[00 assets/1512a37da57827bd9cb4c79e5fe7e870_MD5.png]]

但是注意一个问题，最好不要使用 name，因为 name 是 window 下面的一个属性

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>

		<script type="text/javascript">
			console.log(window.name);
		</script>
	</body>
</html>

```

![[00 assets/df2733fa98fc3ae31d24788440feb9d7_MD5.png]]

### 14.2 window 对象的事件

#### 14.2.1 窗口加载事件

window.onload 是窗口加载事件，当文档内容完全加载完全会触发该事件，然后执行后面的处理函数

这里就解决了为 JS 一直要写在 HTML 的后面，因为要等 HTML 执行完毕之后才可以获取里面的值

下面是使用传统的方式来注册，但是有一个问题，传统的注册事件只能写一次

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			window.onload = function(){
				var btn = document.querySelector('button');
				btn.onclick = function(){
					alert('你点击了我');
				}
			}
		</script>
	</head>
	<body>
		<button type="button">点我</button>
	</body>
</html>

```

![[00 assets/cb91547f19a5b7fb3b660a1854469b51_MD5.png]]

所有我们就可以使用监听来写

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			window.addEventListener('load',function(){
				var btn = document.querySelector('button');
				btn.onclick = function(){
					alert('你点击了我');
				}
			})
		</script>
	</head>
	<body>
		<button type="button">点我</button>
	</body>
</html>

```

![[00 assets/b798ba56206d77b188b010e918f54c80_MD5.png]]

但是我们还有一个事件来处理加载页面，就是 DOMContentLoaded

这和上面的 load 是有区别的，假如你加载大量的图片的时候，load 是等待图片加载完毕之后在执行我们的 JS，这就非常的慢，而且体验会非常的不好，这个时候就需要使用这个事件

因为这个事件是加载完标签之后就执行 JS，虽然图片没有加载出来，但是又一个具体的框架，可以提升用户的使用体验

下面代码 DOMContentLoaded 虽然在下面，也是优先执行

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				alert('我是laod');
			})
			window.addEventListener('DOMContentLoaded', function() {
				alert('我是DOM的那个');
			})
		</script>
	</head>
	<body>
		<button type="button">点我</button>
	</body>
</html>

```

![[00 assets/afac1fe08e5ccd5721ac90a096dad316_MD5.png]]

但是在相同的事件下还是 load 优先执行

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				var btn = document.querySelector('button');
				btn.onclick = function() {
					alert('我是load');
				}
			})
			window.addEventListener('DOMContentLoaded', function() {
				var btn = document.querySelector('button');
				btn.onclick = function() {
					alert('我是DOM的那个');
				}
			})
		</script>
	</head>
	<body>
		<button type="button">点我</button>
	</body>
</html>

```

![[00 assets/6d9dbc7e009300cef1c36dfbb5551d64_MD5.png]]

后记：这个没有具体来测试

#### 14.2.2 调整窗口大小事件

window.onresize 是调整窗口大小加载事件，当触发的时候就调用我们的处理函数

下面的代码是只要窗口变化了就执行后面的函数

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			window.addEventListener('resize', function() {
				console.log('变化了');
			})
		</script>
	</head>
	<body>

	</body>
</html>

```

![[00 assets/eeaef2b30046f1a76bfb79cef3518352_MD5.png]]

但是这个事件我们一般用来响应式布局里面，这里就需要一个新的属性，window.innerWidth 来处理

下面就是小于 800 的时候就隐藏盒子

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			div {
				width: 100px;
				height: 100px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				var div = document.querySelector('div');
				window.addEventListener('resize', function() {
					if (window.innerWidth <= 800) {
						div.style.display = 'none'
					} else {
						div.style.display = 'block';
					}
				})
			})
		</script>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/ddd892be396c181543da8bebcba0b24e_MD5.png]]

#### 14.2.3 定时器

##### 14.2.3.1 setTimeout()

window.setTimeout()，就是用于设置一个定时器，该定时器到期后执行调用函数

下面就是一个基础的定时器的使用

这里有 2 个注意的点，window 可以省略不去写，并且延迟事件是毫秒，假如省略的话就默认为 0

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			setTimeout(function(){
				console.log('2秒钟哦');
			},2000);
		</script>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/a3dbeb6eda94fe94c7501f8508f67af9_MD5.png]]

但是里面也可以接收函数名，有 2 种写法，但是后一种方式不是很提倡，只作为了解就可以了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			function f1(){
				console.log('5秒钟了哦');
			}
			setTimeout(f1,5000);
			setTimeout('f1()',5000);
		</script>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/af5a89035b861dd4bad9ae222380e221_MD5.png]]

当然我们也可以给定时器取一个名字

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			function f1(){
				console.log('5秒钟了哦');
			}
			function f2(){
				console.log('3秒钟了哦');
			}
			var s1 = setTimeout(f2,3000);
			var s2 =  setTimeout('f1()',5000);
		</script>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/1a3a5a7a847490b495372887fd54a855_MD5.png]]

这里就有一个名词，就是**回调函数**

因为普通函数都是按照代码顺序来执行的，而这个函数是等待一段时间之后再来回头来调用这个函数，就是回调函数，上面使用的定时器和以前使用的 onclick 都是回调函数

下面就是一个小的案例，就是 5 秒之后就隐藏起来

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
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			window.addEventListener('load',function(){
				var div = document.querySelector('div');
				function hide(){
					div.style.display = 'none';
					console.log("这个方块就留5秒哦");
				}
				var div_hide = setTimeout(hide,5000);
			})
		</script>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/25e7978d5365ab2bc3e7c7ad390d04db_MD5.png]]

当然我们也可以停止定时器

##### 14.2.3.2 clearTimeout()

就是 clearTimeout(定时器的名字)

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
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			window.addEventListener('load',function(){
				var div = document.querySelector('div');
				var btn = document.querySelector('button');
				function hide(){
					div.style.display = 'none';
					console.log("这个方块就留3秒哦");
				}
				var div_hide = setTimeout(hide,3000);
				btn.addEventListener('click',function(){
					clearTimeout(div_hide);
				})
			})
		</script>
	</head>
	<body>
		<button>点击我这个方块就不会消失</button>
		<div></div>
	</body>
</html>

```

![[00 assets/7ff862c4720040babba28ed5105d773a_MD5.png]]

##### 14.2.3.3 setInterval()

当然我们还有其它的定时器 setInterval

这个定时器和上面的 setTimeOut 是一样的用法，但是它和 setTimeOut 有本质的区别，就是 setTimeOut 是只执行一次，但是 setInterval 是持续执行，每隔后面的时间结束就执行一次

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			setInterval(function(){
				console.log("我出现了");
			},1000);
		</script>
	</head>
	<body>
	</body>
</html>

```

![[00 assets/50118fe0fe09e332646af00a843377b6_MD5.png]]

##### 14.2.3.4 clearInterval()

这是清除上面的定时器的

但是这里有一个要注意的点，就是 x_time 这里要设置一个全局变量，这样就可以停止通过全局变量来停止定时器

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				var begin = document.getElementById('begin');
				var stop = document.getElementById('stop');
				var x_time = null;

				begin.addEventListener('click', function() {
					x_time = setInterval(function time() {
						console.log("开始循环了");
					}, 1000);
				})
				stop.addEventListener('click', function() {
					clearInterval(x_time);
					console.log('停止循环了');
				})
			})
		</script>
	</head>
	<body>
		<button type="button" id="begin">开始定时</button>
		<button type="button" id="stop">停止定时</button>
	</body>
</html>

```

### 14.3 this

一般情况下 this 就是指向的那个调用的对象

#### 14.3.1 全局作用域中

在全局作用域中，普通函数，定时器都是指的 window

下面代码的 f1()，指的是 window.f1()，定时器也是差不多的

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
		<script type="text/javascript">
			console.log(this);
			function f1(){
				console.log(this);
			}
			f1();
			setTimeout(function(){
				console.log(this);
			},1000);
		</script>
	</body>
</html>

```

![[00 assets/488ed5c9703b286af6c2f64f751fd757_MD5.png]]

#### 14.2.2 方法调用中

这里帮忙回忆一下，在对象里面的函数叫做方法

是那个对象调用的这个方法，this 就是指的那个对象

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
		<script type="text/javascript">
			var a = {
				say:function(){
					console.log(this);
				}
			}
			a.say();
		</script>
	</body>
</html>

```

![[00 assets/f2d8240936e924fe04625a88251d2c3b_MD5.png]]

后记：为什么最后输出的是 f

但是我们使用事件来调用的 this，就是指的调用的对象，即便使用广播来创建的话也是和下面的结果是一样的

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
			var btn = document.querySelector('button');
			btn.onclick = function(){
				console.log(this);
			}
		</script>
	</body>
</html>

```

![[00 assets/b8c0432044601e641a85e6d5ab4747b7_MD5.png]]

#### 14.2.3 在构造函数中

指的是 fun 的实例化对象

记得实例化的顺序吗，来回忆一下

这里记一下**new**关键字**执行的过程**

1.new 构造函数会在内存中创建一个空的对象

2.构造函数里面的 this 就会指向空的对象

3.执行构造函数里面的代码，给空对象添加属性和方法

4.返回这个对象

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
		<script type="text/javascript">
			function f1(){
				console.log(this);
			}
            var fun = new f1();
		</script>
	</body>
</html>

```

![[00 assets/4efb3c524c9a8c7066f6e666687bbce5_MD5.png]]

### 14.4 JS 执行机制

JS 的一大特点，就是单线程，就是同一时间只能做一件事，这是因为 JS 这门脚本语言诞生的原因所致，JS 是处理页面中用户的交互，我们对一个元素的获取，删除，操作不能同时进行

当然为了解决这个问题，我们就需要使用 CPU 的计算能力，HTML5 提出了 Web Worker 标准，允许 JS 脚本构建多个线程，所以这个时候就出现了同步和异步

#### 14.4.1 同步

也就是上面的单线程的做法，前一个任务结束后执行后一个任务，程序执行的顺序和任务的排列顺序是一致的，同步的

#### 14.4.2 异步

在做一件事的同时，可以去处理其他事情

看见下面的代码没，是不是最后的执行的顺序不是从上到下，先执行的定时器后面的程序，这就是异步带来的变化，后面的代码没必要等着定时器里面的函数来执行，所以就优先执行定时器后面的代码

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
		<script type="text/javascript">
			console.log('第一个出来了');
			setTimeout(function(){
				console.log('第二个出来了');
			},1000);
			console.log('第三个出来了');
		</script>
	</body>
</html>

```

![[00 assets/c4ed67d89863613b7f2ae5f79a577913_MD5.png]]

有人说是因为定时器后面设置了时间导致的，假如说我们不去设置时间的话

看到没，最后的运行的结果是一样的

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
		<script type="text/javascript">
			console.log('第一个出来了');
			setTimeout(function(){
				console.log('第二个出来了');
			},0);
			console.log('第三个出来了');
		</script>
	</body>
</html>

```

![[00 assets/0b57e8c5de7758e5f455f1295e8bda64_MD5.png]]

#### 14.4.3 执行顺序

**同步任务**在主线程上面执行，就是一个执行栈

**异步任务**是通过回调函数来实现的

![[00 assets/c437a1e7dc397525b22bc1c6bf25d495_MD5.png]]

这个时候我们来看上面的案例，也就是 14.4.2 里面的案例

![[00 assets/e534aecee2871e022a6103f174abc426_MD5.png]]

所以根据上面的可以知道，先执行同步任务，遇到异步任务就放在任务队列里面，等到同步任务在执行栈里面执行完毕，系统就会将任务队列里面的异步任务放到执行栈中，开始执行

当然假如一个程序里面包含了多个异步任务的时候，也就是下面代码的情况

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
		<script type="text/javascript">
			console.log("我是第一个执行的");
			document.onclick = function(){
				console.log("我是click的函数");
			}
            console.log("我是第二个执行的");
			setTimeout(function(){
				console.log("我是定时器的函数");
			},3000);
		</script>
	</body>
</html>

```

我们来解释一下上面代码的执行情况

首先先执行同步任务，遇到了 document 的点击事件，这个时候就需要异步进程处理，来判断有没有点击，假如你点击的话就进入异步任务，这个时候我们就不点击了，然后就执行后面的同步任务，输出”我是第二个执行的“，然后再向下来执行，这个时候遇到了定时器，我们将这个定时器里面的函数给异步进程处理来判断，假如时间超过了 3s，就把函数给异步任务，这个时候再来执行同步任务，同步任务已经执行完毕了，就来检查异步任务，这个时候因为我们没有点击，所以异步任务里面只有一个定时器的函数，JS 就会将这个函数给同步任务，同步任务来执行

随后我们点击鼠标，点击的函数就会通过异步进程处理给异步任务，同步任务再检查异步任务，将点击函数拿出来到同步任务里面执行

这个时候我们有没有发现一个问题，为什么程序结束了，同步任务还是会去异步任务看看，这是因为事件循环，会来回循环

![[00 assets/b96268439d3c1da483592739767d3633_MD5.png]]

当然还有一个比较复杂的图

![[00 assets/a9e39aadf03c5dd7d19f8deb9927d4dd_MD5.png]]

### 14.5 BOM 案例

#### 14.5.1 倒计时

这里要注意一个问题，就是要调用一次这个函数，不然每次进网页的时候都有 1s 的延迟，因为定时器是 1s 之后开始调用函数，这个时候函数里面是 123，所以需要在开始的时候就调用一次

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			#time div {
				float: left;
				width: 50px;
				height: 50px;
				background-color: burlywood;
				margin: 5px;
				line-height: 50px;
				text-align: center;
			}
		</style>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				var hour = document.querySelector('#time div:nth-child(1)');
				var min = document.querySelector('#time div:nth-child(2)');
				var sec = document.querySelector('#time div:nth-child(3)');
				var inTime = +new Date('2021-12-7 21:45:00');
				setInterval(getTime,1000);
				function getTime() {
					var nowTime = +new Date();
					var time = (inTime - nowTime) / 1000;

					var h = parseInt(time / 60 / 60 % 24);
					h = h < 10 ? '0' + h : h;
					hour.innerHTML = h;

					var m = parseInt(time / 60 % 60);
					m = m < 10 ? '0' + m : m;
					min.innerHTML = m;

					var s = parseInt(time % 60);
					s = s < 10 ? '0' + s : s;
					sec.innerHTML = s;
				}
				getTime();
			})
		</script>
	</head>
	<body>
		<div id="time">
			<div>1</div>
			<div>2</div>
			<div>3</div>
		</div>
	</body>
</html>

```

![[00 assets/c72e1ccef698b42862e3da431a7ad17c_MD5.png]]

#### 14.5.2 发送短信验证码

下面有 2 个代码

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				var text = document.querySelector('input');
				var btn = document.querySelector('button');
				var i = 5;
				btn.addEventListener('click',function(){
					if(text.value === ''){alert('请输入号码');}
					else{
						btn.disabled = true;
						function time(){
							if(i === 0){
								clearInterval(gtime);
								btn.disabled = false;
								btn.innerHTML = '发送验证码';
								i = 5;
							}
							btn.innerHTML = '还剩下'+i+'秒';
							i--;
						}
						time();
						var gtime = setInterval(time,1000);
					}
				})
			})
		</script>
	</head>
	<body>
		<input type="text"/>
		<button type="button">发送验证码</button>
	</body>
</html>

```

![[00 assets/1da960047e5436d99ddba6f4412523eb_MD5.jpeg]]

但是我们还有一个方式来写这个代码，因为上面的代码有点杂乱了

下面代码有 2 个关键的点

第一个就是作用域的问题，这里要强调一点，作用域是包括前面的前置代码的，比如说下面的 timer 里面，按理说是属于上面的一段代码的作用域，但是最后还是可以在里面使用

第二个就是代码整洁度的问题，有的代码一看条理就很清晰，是因为本事的思路就是就是一看就知道，但是我上面的代码就有一点逻辑上面的问题，一眼看着不是很明白，有很多的前置条件，并且函数的调用也不是很好，但是后面的这个代码就在思路上面非常的清晰

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script type="text/javascript">
			window.addEventListener('load', function() {
				var text = document.querySelector('input');
				var btn = document.querySelector('button');
				var i = 5;
				btn.addEventListener('click',function(){
					if(text.value === ''){alert('请输入号码');}
					else{
						btn.disabled = true;
						var timer = setInterval(function(){
							if(i === 0){
								clearInterval(timer);
								btn.disabled = false;
								btn.innerHTML = '发送验证码';
								i = 5;
							}
							else{
								btn.innerHTML = '还剩下'+i+'秒';
								i--;
							}
						},1000);
					}
				})
			})
		</script>
	</head>
	<body>
		<input type="text"/>
		<button type="button">发送验证码</button>
	</body>
</html>

```

#### 14.5.3 5S 之后跳转页面

下面就是 5s 跳转的代码

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
		<div></div>
		<script type="text/javascript">
			var d = document.querySelector('div');
			var time = 5;
			setInterval(function(){
				if(time == 0){
					location.href = "http://www.baidu.com";
				}
				else{
					d.innerHTML = "您还有"+time+"秒之后跳转";
					time--;
				}
			},1000)
		</script>
	</body>
</html>

```

![[00 assets/a54dc1eac1399d8d048e23dcc5c53a66_MD5.png]]

#### 14.5.4 获取 url 参数

这里需要 2 个页面，也就是 search 传递其他参数，可以参考上面的 location 对象里面的属性

我们先来看下网页的参数传递

index.html

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
		<form action="index1.html">
			用户名:<input type="text" name="uname" />
			<input type="submit" value="登录" />
		</form>
		<script type="text/javascript">

		</script>
	</body>
</html>

```

index1.html

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

	</body>
</html>

```

这个是一开始传递的值，注意这个要是 submit 类型的才可以，不能是 button

我们这里点击了提交，就会变成下面的值

![[00 assets/d6111797014792d8dd27b72bfd48a15b_MD5.png]]

看到网页 url 的值没，是不是发生了变化，并且网页跳转到了 index1.html，后面的 uname 就是其他参数，也就是 search 的值

![[00 assets/77948d01f812fcc7647282e1cfe940de_MD5.png]]

假如将 index1.html 改成下面的样子，就会将用户名更改过来

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
		<div></div>
		<script type="text/javascript">
			var div = document.querySelector('div');
			var p = location.search.substr(1);
			var arr = p.split('=');
			div.innerHTML = arr[1]+"欢迎来这里";
		</script>
	</body>
</html>

```

![[00 assets/d89203b2ee2cfdcdc14b097d9ab04b65_MD5.png]]

## 15. 网页特效

### 15.1 offset

offset 就是偏移量的意思，我们使用 offset 就可以动态的获取元素的位置，大小，但是返回的值是不带单位的

![[00 assets/8a13118804e39dbf0f4a0919ba23a687_MD5.png]]

#### 15.1.1 offsetTop 和 offsetLeft

下面就是父元素不加定位之后子元素的偏移信息，并且这个子元素是获取的和 body 的距离

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				margin-left: 100px;
				background-color: pink;
				overflow: hidden;
			}
			.son{
				width: 50px;
				height: 50px;
				margin-top: 50px;
				margin-left: 50px;
				background-color: burlywood;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
		<script type="text/javascript">
			var fa = document.querySelector('.father');
			var so = document.querySelector('.son');

			console.log("父元素的距离上面的距离"+fa.offsetTop);
			console.log("父元素的距离左面的距离"+fa.offsetLeft);
			console.log("子元素的距离上面的距离"+so.offsetTop);
			console.log("子元素的距离左面的距离"+so.offsetLeft);
		</script>
	</body>
</html>

```

![[00 assets/92e6464f21ea2671a928180419fa2ca4_MD5.png]]

假如给父元素加一个定位的话，就会改变这样的状况，子元素就会按照父元素为起点来写 margin 的值，并且是父元素开启什么定位都可以

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				margin-left: 100px;
				background-color: pink;
				overflow: hidden;
				position: absolute;
			}
			.son{
				width: 50px;
				height: 50px;
				margin-top: 50px;
				margin-left: 50px;
				background-color: burlywood;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
		<script type="text/javascript">
			var fa = document.querySelector('.father');
			var so = document.querySelector('.son');

			console.log("父元素的距离上面的距离"+fa.offsetTop);
			console.log("父元素的距离左面的距离"+fa.offsetLeft);
			console.log("子元素的距离上面的距离"+so.offsetTop);
			console.log("子元素的距离左面的距离"+so.offsetLeft);
		</script>
	</body>
</html>

```

![[00 assets/078abd866a87f27128e828040ed5e130_MD5.png]]

#### 15.1.2 offsetWidth 和 offsetHeight

它是计算 padding+border+width 的值，但是不计算 margin 的值

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.one{
				width: 100px;
				height: 100px;
				background-color: pink;
				/* margin的值改变，值不改变 */
				margin-top: 100px;
				margin-left: 100px;
				/* padding的值改变，值改变 */
				padding-top: 50px;
				padding-left: 50px;
				/* border的值改变，值改变 */
				border-top: 5px solid burlywood;
				border-left: 5px solid burlywood;
			}
		</style>
	</head>
	<body>
		<div class="one"></div>
		<script type="text/javascript">
			var fa = document.querySelector('.one');

			console.log("上面的距离"+fa.offsetHeight);
			console.log("左面的距离"+fa.offsetWidth);
		</script>
	</body>
</html>

```

![[00 assets/990f5d5289364f40d20de19766861312_MD5.png]]

但是有人想问，这个口算的计算的出来，为什么需要这个属性呢，这是因为你不加 width 的话，就会自动获取盒子的 width 值

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.one{
				height: 100px;
				background-color: pink;
				/* padding的值改变，值改变 */
				padding-top: 50px;
				padding-left: 50px;
				/* border的值改变，值改变 */
				border-top: 5px solid burlywood;
				border-left: 5px solid burlywood;
			}
		</style>
	</head>
	<body>
		<div class="one"></div>
		<script type="text/javascript">
			var fa = document.querySelector('.one');

			console.log("左面的距离"+fa.offsetWidth);
		</script>
	</body>
</html>

```

![[00 assets/6bd0360bcf863395d2e003801187fcfe_MD5.png]]

#### 15.1.3 offsetParent

返回带有定位的父元素，注意是带有定位的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				margin-left: 100px;
				background-color: pink;
				overflow: hidden;
                position: absolute;
			}
			.son{
				width: 50px;
				height: 50px;
				margin-top: 50px;
				margin-left: 50px;
				background-color: burlywood;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
		<script type="text/javascript">
			var fa = document.querySelector('.father');
			var so = document.querySelector('.son');

			console.log(so.offsetParent);
		</script>
	</body>
</html>

```

![[00 assets/77a83f41c04093cd20f1eeabf8c8ed73_MD5.png]]

假如你的父元素没开启定位的话，就是返回的 body

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 100px;
				height: 100px;
				margin-top: 100px;
				margin-left: 100px;
				background-color: pink;
				overflow: hidden;
			}
			.son{
				width: 50px;
				height: 50px;
				margin-top: 50px;
				margin-left: 50px;
				background-color: burlywood;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
		<script type="text/javascript">
			var fa = document.querySelector('.father');
			var so = document.querySelector('.son');

			console.log(so.offsetParent);
		</script>
	</body>
</html>

```

![[00 assets/9df4dff0247ff2fbb65fe322c6c718b3_MD5.png]]

但是我们回忆一下前面的 DOM 标记，是不是有一个 parentNode，这也是返回父元素的，但是要注意这个和 offsetParent 的区别，parentNode 是返回最近的一级的父元素，但是 offsetParent 是返回开启定位的最近的父元素

#### 15.1.4 offset 和 style 的区别

![[00 assets/39bb8617a92df4a98830795e2ed279e2_MD5.png]]

首先是获取元素的值

offset 不管 css 在那里都可以获取，但是 style 是不可以的，style 只能获取行内样式表里面的值

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 100px;
				height: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="father"></div>
		<script type="text/javascript">
			var fa = document.querySelector('.father');

			console.log(fa.style.width);
			console.log(fa.offsetWidth);
		</script>
	</body>
</html>

```

![[00 assets/4ac6716cec9e4edb9b734f6f23a7e753_MD5.png]]

style 获取过来的是有单位的，但是 offset 获取过来的是没有单位的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 100px;
				height: 100px;
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="father" style="width: 200px;"></div>
		<script type="text/javascript">
			var fa = document.querySelector('.father');

			console.log(fa.style.width);
			console.log(fa.offsetWidth);
		</script>
	</body>
</html>

```

![[00 assets/b8b6703aebdd1bf1aed58a065f2cb392_MD5.png]]

这个是最主要的区别，就是 offset 属性是只读属性，只能获取不能赋值，也就是不能改变，但是 style 是可读写的，不仅可以读还可以写

### 15.2 client

![[00 assets/da5a67e16d356ae3dcc7ca7a48a34b0f_MD5.png]]

client 和 offsetWidth 最大的区别就是 client 是不包含边框的

我们来看下面的代码的解析，第一个和第二个就是不包含边框，只是单纯包含宽度，但是后面两个就是指计算边框，这就是和 offsetWigth 和 offsetHeight 和区别

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
				border: 20px solid pink;
				background-color: burlywood;
			}
		</style>
	</head>
	<body>
		<div class="main"></div>
		<script type="text/javascript">
			var main = document.querySelector('.main');

			console.log(main.clientWidth);
			console.log(main.clientHeight);
			console.log(main.clientLeft);
			console.log(main.clientTop);
		</script>
	</body>
</html>

```

![[00 assets/b01446b51bacd7bd908298f2832feac8_MD5.png]]

### 15.4 scroll

![[00 assets/ce4b159212582927fecc9176026fe6f7_MD5.jpeg]]

这个就和上面又都不一样，这个是不包含边框，但是包含 padding 的值

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

				border: 20px solid pink;
				padding: 100px 0px;
			}
		</style>
	</head>
	<body>
		<div class="main"></div>
		<script type="text/javascript">
			var div = document.querySelector('.main');
			console.log(div.scrollWidth);
			console.log(div.scrollHeight);
		</script>
	</body>
</html>

```

![[00 assets/981e853eea3225a045cc168fdae442be_MD5.png]]

但是它还有一个特性，假如文字特别多的时候，width 的值也是会增加，因为它是记录实际高度和宽度得值

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="main">
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
		</div>
		<script type="text/javascript">
			var div = document.querySelector('.main');
			console.log(div.scrollWidth);
			console.log(div.scrollHeight);
		</script>
	</body>
</html>

```

![[00 assets/ba8027f9e94d9b87c7829a85ced53230_MD5.png]]

当然我们有的时候也使用 scrollTop 来记录

这里就可以使用 onscroll 得事件

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
				background-color: pink;
				overflow: auto;
			}
		</style>
	</head>
	<body>
		<div class="main">
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
			这是一个语句这是一个语句这是一个语句这是一个语句
		</div>
		<script type="text/javascript">
			var div = document.querySelector('.main');
			div.addEventListener('scroll',function(){
				console.log(div.scrollTop);
			})
		</script>
	</body>
</html>

```

![[00 assets/f435d6c406293b52578cf5f3ab997725_MD5.png]]

### 15.5 总结

![[00 assets/519ff6290347ab7ed47689ee58dc6a59_MD5.png]]

![[00 assets/e3a0a9eb8fbfe6dc6144f5b46f034789_MD5.png]]

### 15.6 案例

#### 15.6.1 获取鼠标在盒子里面的坐标

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.father{
				width: 300px;
				height: 300px;
				background-color: pink;
				margin: 50px;
			}
		</style>
	</head>
	<body>
		<div class="father"></div>

		<script type="text/javascript">
			var fa = document.querySelector('.father');
			fa.addEventListener('click',function(e){
				console.log(e.pageY-fa.offsetLeft);
				console.log(e.pageX-fa.offsetTop);
			})
		</script>
	</body>
</html>

```

![[00 assets/435ec9a363ad1b693af7f690df8bd5cd_MD5.png]]

#### 15.6.2 拖动模态框

下面的代码只是一个模拟，大体的框架是这样的，我们也可以写出更加好看的页面

当然这个案例的最主要的就是鼠标拖拽的地方的代码

我来描述一下代码，首先点击登录框的时候，获取的是相对于这个框左上角的距离，我们移动的话，是可以获取鼠标的相对于页面的距离，当我们松开鼠标的话就会删除移动的鼠标事件，停止移动

我们来看下面的图，假如你删除了移动事件里面的 x 和 y 的话，登录框的左上角就会到红色标指的位置，假如获取一开始鼠标相对于框的距离的话，再减去的话，就不会出现这样的问题

![[00 assets/e6fe8353a363a98b5ad719eebfea3b35_MD5.png]]

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.login{
				width: 200px;
				height: 200px;
				background-color: #999;
				text-align: center;
				color: #fff;

				position: absolute;
				top: 60px;
				left: 60px;
				z-index: 3;

				display: none;
			}
			.login>*{
				margin-top: 30px;
			}
			.guan{
				width: 100%;
				height: 100%;
				background-color: #eee;

				position: absolute;
				top: 0px;
				left: 0px;
				z-index: 2;

				display: none;
			}
		</style>
	</head>
	<body>
		<!-- 按钮 -->
		<button type="button">按住我</button>

		<div class="login">
			<button>关闭</button>
			<div class="main">
				欢迎来到这里
			</div>
		</div>

		<div class="guan"></div>

		<script type="text/javascript">
			var btn = document.querySelector('button');
			var btn_z = document.querySelector('.login button');
			var lo = document.querySelector('.login');
			var gu = document.querySelector('.guan');

			btn.addEventListener('click',function(){
				lo.style.display = 'block';
				gu.style.display = 'block';
			})
			btn_z.addEventListener('click',function(){
				lo.style.display = 'none';
				gu.style.display = 'none';
			})
			lo.addEventListener('mousedown',function(e){
				var x = e.pageX - lo.offsetLeft;
				var y = e.pageY - lo.offsetTop;

				document.addEventListener('mousemove',m)
				function m(e){
					lo.style.left = e.pageX - x + 'px';
					lo.style.top = e.pageY - y + 'px';
				}

				document.addEventListener('mouseup',function(){
					document.removeEventListener('mousemove',m)
				})
			})
		</script>
	</body>
</html>
```

你点击下面的按钮的话，就会出现后面的菜单

![[00 assets/a49cba5216909be495ea057461466c3f_MD5.png]]

然后我们就可以拖动这个菜单框了

![[00 assets/8c3cd885264f29fcc178f7980b157fd1_MD5.png]]

#### 15.6.3 仿京东放大镜

这个既是京东仿放大镜的部分代码，这里主要的问题是和上面的拖动拟态框是一样的，计算好距离就可以了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			* {
				margin: 0px;
				padding: 0px;
			}

			.back_img {
				margin: 50px 50px;
				position: relative;
				top: 0px;
				left: 0px;
			}

			.back_img img {
				width: 400px;
				height: 400px;
			}

			.mask {
				width: 200px;
				height: 200px;
				position: absolute;
				top: 0px;
				left: 0px;
				background-color: burlywood;
				opacity: 0.5;
				display: none;
			}

			.main {
				display: flex;
			}

			.text {
				margin-top: 50px;
			}
			.big_img {
				margin-top: 50px;
				color: pink;
				font-size: 20px;
				display: none;
			}
		</style>
	</head>
	<body>
		<div class="main">
			<div class="back_img">
				<img src="img/bg1.jpg" />
				<div class="mask">1</div>
			</div>
			<div class="text">
				这是一个介绍哦!就是为了显示js的消失的效果
			</div>
			<div class="big_img">
				我没有高清大图，我就用文字代替一下,但是我们也可以直接遮盖在上面
			</div>
		</div>

		<script type="text/javascript">
			var mask = document.querySelector('.mask');
			var back_img = document.querySelector('.back_img');
			var text = document.querySelector('.text');
			var big_img = document.querySelector('.big_img');

			back_img.addEventListener('mouseover',function(){
				mask.style.display = 'block';
				text.style.display = 'none';
				big_img.style.display = 'block';
			})
			back_img.addEventListener('mouseout',function(){
				mask.style.display = 'none';
				text.style.display = 'block';
				big_img.style.display = 'none';
			})
			back_img.addEventListener('mousemove',function(e){
				var x = e.pageX - this.offsetLeft;
				var y = e.pageY - this.offsetTop;

				var maskX = x - mask.offsetWidth/2;
				var maskY = y - mask.offsetHeight/2;

				if(maskX <= 0){
					maskX = 0;
				}else if(maskX >= back_img.offsetWidth - mask.offsetWidth){
					maskX = back_img.offsetWidth - mask.offsetWidth;
				}
				if(maskY <= 0 ){
					maskY = 0;
				}else if(maskY >= back_img.offsetHeight - mask.offsetHeight){
					maskY = back_img.offsetHeight - mask.offsetHeight;
				}

				mask.style.top = maskY + 'px';
				mask.style.left = maskX + 'px';
			})
		</script>
	</body>
</html>

```

![[00 assets/eeaae7cbbd407bf982006be51787a7a7_MD5.png]]

#### 15.6.4 淘宝 flexibleJS 源码分析

建议去观看 302 集，这里只做源码分析的记录

**1.**

首先我们来看第五行代码的解析

![[00 assets/8a2d192ed6117f57f7669f49ec183d99_MD5.png]]

这里是设置物理像素比的，移动端的像素和 pc 端的是不一样的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
	</head>
	<body>
		<script type="text/javascript">
			console.log(window.devicePixelRatio);
		</script>
	</body>
</html>

```

电脑端

![[00 assets/8d9829c02236faa15bf312d805ce211b_MD5.png]]

手机端

![[00 assets/3410ec5a05f51378b884cbb349b645fb_MD5.png]]

**2.**

我们再来看后面的调整字体大小的代码，这就是按照上面获取的物理像素比来动态调整

![[00 assets/cb176fe7bc595fcd94793a138b104fa4_MD5.png]]

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			var dpr = window.devicePixelRatio || 1;

			function setBodyFontSize(){
				if(document.body){
					document.body.style.fontSize = (12 * dpr) + 'px';
				}else{
					document.addEventListener('DOMContentLoaded',setBodyFontSize);
				}
			}
			setBodyFontSize();
		</script>
	</head>
	<body>
		<div class="text">
			这是一个文字
		</div>
	</body>
</html>

```

pc 端

![[00 assets/f2cd29db11a1b52701c9725e715a2096_MD5.png]]

移动端

![[00 assets/f089f611d257ee47ce2e2866aeb76b48_MD5.png]]

**3.**

这里就是 rem 的实现

![[00 assets/10120cfc7a00b5ec03ce93834cde4033_MD5.png]]

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			var docHtml = document.documentElement;

			function setRem(){
				var rem = docHtml.clientWidth/10;
				docHtml.style.fontSize = rem + 'px';
			}
			setRem();
		</script>
	</head>
	<body>
		<div class="text">
			这是一个文字
		</div>
	</body>
</html>

```

PC 端

![[00 assets/86bd4054d6e1e65f444feb73c33ffc75_MD5.png]]

移动端

![[00 assets/d11c4f580e43fc1acbe6bc3e443734bd_MD5.png]]

**4.**

这个就是当页面发生变化的时候的代码，你拉动浏览器窗口的大小的时候，字体也需要一起变化

![[00 assets/98069e3d4924279583fcb6b456f63c51_MD5.png]]

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">

		</style>
		<script type="text/javascript">
			var docHtml = document.documentElement;
			var dpr = window.devicePixelRatio || 1;

			// function setBodyFontSize() {
			// 	if (document.body) {
			// 		document.body.style.fontSize = (12 * dpr) + 'px';
			// 	} else {
			// 		document.addEventListener('DOMContentLoaded', setBodyFontSize);
			// 	}
			// }
			// setBodyFontSize();

			function setRem() {
				var rem = docHtml.clientWidth / 10;
				docHtml.style.fontSize = rem + 'px';
			}
			setRem();


			window.addEventListener('resize',setRem); //尺寸变化的时候调用
			window.addEventListener('pageshow',function(e){ //重新加载页面
				if(e.persisted){
					setRem();
				}
			})
		</script>
	</head>
	<body>
		<div class="text">
			这是一个文字
		</div>
	</body>
</html>
```

![[00 assets/09a9b7195889033a6f1b1a3401c22261_MD5.png]]

但是有没有怀疑，为什么不使用 load 来处理

![[00 assets/43389ccbce198da26f50e7b782396dd9_MD5.png]]

**5.**

当然下面就是设置移动端

![[00 assets/2a8695cc4d92af0cba15a671af0226cb_MD5.png]]

#### 15.6.5 仿淘宝固定定位

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			* {
				margin: 0px;
				padding: 0px;
			}

			.header {
				width: 90%;
				height: 200px;
				background-color: brown;
			}

			.banner {
				width: 90%;
				height: 1500px;
				background-color: cadetblue;
			}

			.content {
				width: 90%;
				height: 500px;
				background-color: cornflowerblue;
			}

			.bar {
				width: 10%;
				height: 80px;
				background-color: crimson;
				line-height: 80px;
				text-align: center;

				position: absolute;
				top: 100px;
				left: 90%;
			}
		</style>
	</head>
	<body>
		<div class="main">
			<div class="bar">
				<span>回到顶部</span>
			</div>
			<div class="header">头部信息</div>
			<div class="banner">主体内容</div>
			<div class="content">尾部内容</div>
		</div>
		<script type="text/javascript">
			var bar = document.querySelector('.bar');
			var banner = document.querySelector('.banner');
			var bar_text = document.querySelector('.bar span');
			var bannerTop = banner.offsetTop;

			document.addEventListener('scroll', function() {
				console.log(window.pageYOffset);

				if(window.pageYOffset > bannerTop){
					bar.style.position = 'fixed';
					bar_text.innerHTML = '回到顶部';
				}else{
					bar.style.position = 'absolute';
					bar_text.innerHTML = '';
				}
			})
		</script>
	</body>
</html>

```

## 16. 动画

### 16.1 动画实现的原理

核心原理：通过定时器 setlnterval() 不断移动盒子位置

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.son{
				width: 100px;
				height: 100px;
				background-color: blueviolet;

				position: absolute;
				left: 0px;
			}
		</style>
	</head>
	<body>
		<div class="son"></div>

		<script type="text/javascript">
			var box = document.querySelector('.son');

			var move = setInterval(function(){
				if(box.offsetLeft > 200){
					clearInterval(move);
				}else{
					box.style.left = box.offsetLeft + 5 + 'px';
				}
			},100);
		</script>
	</body>
</html>

```

![[00 assets/726e46c0f0a246537aa59e051c5f0d92_MD5.gif]]

### 16.2 简单动画函数封装

为了多个目标元素的使用，这个时候就需要使用函数的封装，免的多次重写函数，下面就是一个简单动画函数封装

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}
			.son1{background-color: blueviolet;}
			.son2{background-color: brown;}
			.son3{background-color: cadetblue;}
		</style>
	</head>
	<body>
		<div class="box son1"></div>
		<div class="box son2"></div>
		<div class="box son3"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				var move = setInterval(function() {
					if (obj.offsetLeft > target) {
						clearInterval(move);
					} else {
						obj.style.left = obj.offsetLeft + 5 + 'px';
					}
				}, 60);
			}

			var son1 = document.querySelector('.son1');
			var son2 = document.querySelector('.son2');
			var son3 = document.querySelector('.son3');

			animate(son1,200);
			animate(son2,400);
			animate(son3,600);

		</script>
	</body>
</html>

```

![[00 assets/92847fae9e0a32f42f6eb83095fa47f1_MD5.gif]]

但是我们发现了一个问题没，上面的你只要调用一次封装好的动画函数，我们就需要在内存里面开辟内存空间，假如你要调用 100 个，就需要在内存中创建 100 个，这非常吃性能，所以在这里我们使用下面的写法，来优化性能

我们将调用的函数作为 obj 对象的属性来调用，这样就完成了性能优化

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}
			.son1{background-color: blueviolet;}
			.son2{background-color: brown;}
			.son3{background-color: cadetblue;}
		</style>
	</head>
	<body>
		<div class="box son1"></div>
		<div class="box son2"></div>
		<div class="box son3"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				obj.move = setInterval(function() {
					if (obj.offsetLeft > target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + 5 + 'px';
					}
				}, 60);
			}

			var son1 = document.querySelector('.son1');
			var son2 = document.querySelector('.son2');
			var son3 = document.querySelector('.son3');

			animate(son1,200);
			animate(son2,400);
			animate(son3,600);

		</script>
	</body>
</html>
```

我们再来思考一下，假如我们使用一个按钮，来开启动画

是不是发现，问题了，这是因为你点击一次按钮，就会给这个盒子加一个定时器，第一次点击的定时器加 5px，你再点击一次定时器，又增加 5px，这样一直点击的话，就会一直往前面走

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}
			.son1{background-color: blueviolet;}
			.son2{background-color: brown;}
			.son3{background-color: cadetblue;}
		</style>
	</head>
	<body>
		<button type="button" class="btn">点击我</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				obj.move = setInterval(function() {
					if (obj.offsetLeft > target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + 5 + 'px';
					}
				}, 60);
			}

			var son1 = document.querySelector('.son1');
			var son2 = document.querySelector('.son2');

			var btn = document.querySelector('.btn');
			btn.addEventListener('click',function(){
				animate(son2,400);
			})
			animate(son1,200);
		</script>
	</body>
</html>

```

![[00 assets/97af1c5be5681ac6ded9324826256ae9_MD5.gif]]

下面是优化的方法

我们只要清楚前面的定时器就可以了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}
			.son1{background-color: blueviolet;}
			.son2{background-color: brown;}
		</style>
	</head>
	<body>
		<button type="button" class="btn">点击我</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					if (obj.offsetLeft > target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + 5 + 'px';
					}
				}, 60);
			}

			var son1 = document.querySelector('.son1');
			var son2 = document.querySelector('.son2');

			var btn = document.querySelector('.btn');
			btn.addEventListener('click',function(){
				animate(son2,400);
			})
			animate(son1,200);
		</script>
	</body>
</html>
```

### 16.3 缓动动画原理

缓动动画就是让元素运动速度有所变化，最常见的是让速度慢慢停下来

![[00 assets/158f85a24f4e542ef7731cc7446f4b50_MD5.png]]

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}

			.son2 {
				background-color: brown;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn">点击我</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					if (obj.offsetLeft > target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + (target - obj.offsetLeft) / 10 + 'px';
					}
				}, 60);
			}

			var son2 = document.querySelector('.son2');

			var btn = document.querySelector('.btn');
			btn.addEventListener('click', function() {
				animate(son2, 200);
			})
		</script>
	</body>
</html>

```

![[00 assets/559b972546e168e9ce1c667844a528b0_MD5.gif]]

但是我们可以发现，是不是最后达不到 500px，这是因为公式的原因

这里为了优化这个问题，我们可以是 math 来解决，我们直接取整就可以了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}

			.son2 {
				background-color: brown;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn">点击我</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					if (obj.offsetLeft > target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + Math.ceil((target - obj.offsetLeft) / 10) + 'px';
					}
				}, 15);
			}

			var son2 = document.querySelector('.son2');

			var btn = document.querySelector('.btn');
			btn.addEventListener('click', function() {
				animate(son2, 200);
			})
		</script>
	</body>
</html>
```

这里我们多加几个按钮，来实现下面的效果

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}

			.son2 {
				background-color: brown;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn200">点击我到200</button>
		<button type="button" class="btn300">点击我到300</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					if (obj.offsetLeft == target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + Math.ceil((target - obj.offsetLeft) / 10) + 'px';
					}
				}, 15);
			}

			var son2 = document.querySelector('.son2');

			var btn200 = document.querySelector('.btn200');
			var btn300 = document.querySelector('.btn300');

			btn200.addEventListener('click', function() {
				animate(son2, 200);
			})
			btn300.addEventListener('click', function() {
				animate(son2, 300);
			})
		</script>
	</body>
</html>

```

![[00 assets/c1272ecce5237fbdec19e4c058f745c1_MD5.gif]]

但是我们想下就知道，下面的值肯定会有一些问题，最后的距离并没有回到原先的位置

![[00 assets/023c151b1c0b0f02754e13fb4709a1ef_MD5.png]]

我们再做下面的修改，就可以改正上面的错误了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}

			.son2 {
				background-color: brown;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn200">点击我到200</button>
		<button type="button" class="btn300">点击我到300</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target) {
				clearInterval(obj.move);
				console.log(son2.offsetLeft);
				obj.move = setInterval(function() {
					var step = (target - obj.offsetLeft) / 10;
					step = step > 0 ? Math.ceil(step) : Math.floor(step);

					if (obj.offsetLeft == target) {
						clearInterval(obj.move);
					} else {
						obj.style.left = obj.offsetLeft + step + 'px';
					}
				}, 15);
			}

			var son2 = document.querySelector('.son2');

			var btn200 = document.querySelector('.btn200');
			var btn300 = document.querySelector('.btn300');

			btn200.addEventListener('click', function() {
				animate(son2, 200);
			})
			btn300.addEventListener('click', function() {
				animate(son2, 300);
			})
		</script>
	</body>
</html>

```

### 16.4 缓冲动画添加回调函数

回调函数原理：函数可以作为一个参数，将这个函数作为参数传到另一个函数里面，当那个函数执行完毕之后，再执行传进去的这个函数，这个过程就叫做回调

所以这个时候就将回调函数写在定时器结束里面

也就是下面封装函数的 callback，这个 callback 的本质是 callback = function()，这样的话你要调用函数的话，就使用的是 callback()

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}

			.son2 {
				background-color: #787878;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn200">点击我到200</button>
		<button type="button" class="btn300">点击我到300</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target, callback) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					var step = (target - obj.offsetLeft) / 10;
					step = step > 0 ? Math.ceil(step) : Math.floor(step);

					if (obj.offsetLeft == target) {
						clearInterval(obj.move);
						if(callback){
							callback();
						}
					} else {
						obj.style.left = obj.offsetLeft + step + 'px';
					}
				}, 15);
			}

			function color_animate(obj) {
				obj.style.backgroundColor = 'pink';
			}

			var son2 = document.querySelector('.son2');
			var btn200 = document.querySelector('.btn200');
			var btn300 = document.querySelector('.btn300');

			btn200.addEventListener('click', function() {
				animate(son2, 200, color_animate(son2));
			})
			btn300.addEventListener('click', function() {
				animate(son2, 300, color_animate(son2));
			})
		</script>
	</body>
</html>

```

![[00 assets/6a4bc96715a13f162b8b3b5c57466b0e_MD5.gif]]

但是发现没，是不是最后好像没有完全实现回调函数

这是因为你在外面写的 color_animate 函数，你直接在动画函数里面写函数名的话，就会直接调用 color_animate 函数，所以没有完全实现，这个时候我们就需要改变写法

发现没，是不是等动画函数结束之后再调用的回调函数

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			.box {
				width: 100px;
				height: 100px;

				position: absolute;
				left: 0px;
			}

			.son2 {
				background-color: #787878;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn200">点击我到200</button>
		<button type="button" class="btn300">点击我到300</button>
		<div class="box son1"></div>
		<div class="box son2"></div>

		<script type="text/javascript">
			function animate(obj, target, callback) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					var step = (target - obj.offsetLeft) / 10;
					step = step > 0 ? Math.ceil(step) : Math.floor(step);

					if (obj.offsetLeft == target) {
						clearInterval(obj.move);
						if(callback){
							callback();
						}
					} else {
						obj.style.left = obj.offsetLeft + step + 'px';
					}
				}, 15);
			}

			var son2 = document.querySelector('.son2');
			var btn200 = document.querySelector('.btn200');
			var btn300 = document.querySelector('.btn300');

			btn200.addEventListener('click', function() {
				animate(son2, 200, function(){
					son2.style.backgroundColor = 'pink';
				});
			})
			btn300.addEventListener('click', function() {
				animate(son2, 300, function(){
					son2.style.backgroundColor = 'pink';
				});
			})
		</script>
	</body>
</html>

```

![[00 assets/5845c6183fc57fd376434178cf2fe07b_MD5.gif]]

### 16.5 节流阀

防止轮播图按钮连续点击造成的播放太快

节流阀的目的就是当上一个函数动画内容执行完毕，再去执行一下函数动画，让时间无法连续触发

其核心思路就是利用回调函数，调用一个变量控制，解锁和锁住函数

这里我们截图轮播图部分 JS 代码来解释，下面就是一个典型的案例，首先 flag 的值是 true，可以执行后面的点击事件后面的代码，然后将 flag 变为 false，这个时候你再点击按钮是不会变化的，当你执行了回调函数的时候，也就是 animate 的时候，就会执行后面 flag=true，这个时候你再点击按钮就会有变化了，这个再实际使用中的情况是，你点击了按钮，当移动完全之后再点击才有效果，不然没效果

```javascript
var flag = true;	//节流阀的使用
c.addEventListener('click',function(){
		if(flag){
			flag = false;
			// 当到了第一张图片，点击左按钮移动到最后一张，然后执行动画函数
			if(num == 0){
				num = ul_b.children.length-1;
				ul_b.style.left = -num * 350 + 'px';
			}
			num--;
			animate(ul_b, -num * 350,function(){
				flag = true;
			});

			cir--;
			cir = cir < 0 ? cir = ul_b.children.length - 2 : cir;

			cir_change();
		}
	})
```

### 16.5 案例

#### 16.5.1 滑动条

下面使用了我们的动画实现，缓冲动画，以及回调函数，函数的封装

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			*{
				margin: 0px;
				padding: 0px;
			}
			.main{
				margin-left: 200px;

				width: 40px;
				height: 40px;
			}
			.icon{
				width: 40px;
				height: 40px;
				background-color: pink;
				line-height: 40px;
				text-align: center;
			}
			.text{
				width: 200px;
				height: 40px;
				background-color: brown;
				line-height: 40px;
				text-align: center;
				color: aliceblue;

				position: absolute;
				top: 0px;
				z-index: -1;
			}
		</style>
	</head>
	<body>
		<div class="main">
			<div class="icon">⬅</div>
			<div class="text">我出现了</div>
		</div>

		<script type="text/javascript">
			function animate(obj, target, callback) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					var step = (target - obj.offsetLeft) / 10;
					step = step > 0 ? Math.ceil(step) : Math.floor(step);

					if (obj.offsetLeft == target) {
						clearInterval(obj.move);
						if(callback){
							callback();
						}
					} else {
						obj.style.left = obj.offsetLeft + step + 'px';
					}
				}, 15);
			}

			var main = document.querySelector('.main');
			var text = document.querySelector('.text');
			var icon = document.querySelector('.icon');

			main.addEventListener('mouseenter',function(){
				animate(text,20,function(){
					icon.innerHTML = '➡';
				});
			});
			main.addEventListener('mouseleave',function(){
				animate(text,200,function(){
					icon.innerHTML = '⬅';
				});
			});
		</script>
	</body>
</html>

```

![[00 assets/2f026352b945f60ac59039f81d0618d0_MD5.gif]]

#### 16.5.2 网页轮播图

首先来看下我们要实现什么样的功能

1. 左右滑动
2. 小圆圈的点击及跟随
3. 鼠标移动到上面左右按钮显示
4. 鼠标悬浮关闭定时器，鼠标离开打开定时器

![[00 assets/94c08f5da1c3c9de27975d46342e3a7f_MD5.gif]]

我先放 html 和 css 的代码

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Document</title>
		<link rel="stylesheet" type="text/css" href="index.css"/>
		<script src="index.js" type="text/javascript" charset="utf-8"></script>
	</head>
	<body>
		<!-- 轮播图 -->
		<div class="admin">
			<!-- 中间图片部分 -->
			<div class="a">
				<ul class="a_ul">
					<li class="b"><img src="1.gif"></li>
					<li class="b"><img src="2.gif"></li>
					<li class="b"><img src="3.gif"></li>
					<li class="b"><img src="1.gif"></li>
				</ul>
			</div>
			<!-- 左边按钮 -->
			<div class="c"><</div>
			<!-- 右边按钮 -->
			<div class="d">></div>
			<!-- 底部圆圈 -->
			<ul class="e1">
				<li data-x="0" class="e ee"></li>
				<li data-x="1" class="e"></li>
				<li data-x="2" class="e"></li>
			</ul>
		</div>
	</body>
</html>

```

```css
* {
	padding: 0;
	margin: 0;
}

body {
	background-color: rgb(39, 35, 35);
	display: flex;
	justify-content: center;
	align-items: center;
}

.admin {
	width: 350px;
	height: 542px;
	position: relative;
	top: 60px;
}
.a{
	position: relative;
	left: 0px;
	overflow: hidden;
}
.a ul{
	width: 1500px;
	overflow: hidden;
	position: relative;
	left: 0px;
}
li {
	list-style: none;
}
.b {
	float: left;
	position: relative;
	left: 0px;
}
.b img{
	width: 350px;
	height: 550px;
}

.c,
.d {
	width: 70px;
	height: 550px;
	background: rgba(207, 90, 211, .2);
	position: absolute;
	top: 0;
	line-height: 550px;
	text-align: center;
	font-size: 70px;
	color: blueviolet;
	cursor: pointer;
	user-select: none;
	transition: .3s;
}

.c:hover,
.d:hover {
	background-color: rgba(255, 255, 255, .6);
	color: #000;
}

.c {
	left: -70px;
}

.d {
	right: -70px;
}

.c,
.d {
	display: none;
}

.e1 {
	width: 95%;
	height: 30px;
	display: flex;
	justify-content: space-around;
	align-items: center;
	position: absolute;
	left: 0;
	right: 0;
	bottom: 10px;
	margin: auto;
}

.e {
	border-radius: 50%;
	border: #000 solid 5px;
	width: 15px;
	height: 15px;
	opacity: .7;
	cursor: pointer;
	transition: .4s;
}

.e:hover {
	opacity: 1;
	background-color: rgba(162, 59, 202, 0.7);
}

.e.ee {
	opacity: 1;
	background-color: rgb(46, 33, 158);
}

```

我们再分别来看下轮播图的部分

```javascript
window.addEventListener('load',function(){
	var admin = document.querySelector('.admin');
	var left_button = document.querySelector('.c');
	var right_button = document.querySelector('.d');

	// 鼠标经过轮播图
	admin.addEventListener('mouseenter',function(){
		// 鼠标经过显示左右按钮
		left_button.style.display = 'block';
		right_button.style.display = 'block';
		// 鼠标经过停止定时器
		clearInterval(timer);
		timer = null;
	})
	admin.addEventListener('mouseleave',function(){
		// 鼠标离开左右按钮消失
		left_button.style.display = 'none';
		right_button.style.display = 'none';
		// 鼠标离开开启定时器
		timer = setInterval(function(){
			d.click();
		},2000);
	})

	var uls = document.querySelector('.e1');
	var lis = uls.getElementsByTagName('li');
	var ul_b = document.querySelector('.a ul');

	//滑动效果函数
	function animate(obj, target, callback) {
		clearInterval(obj.move);
		obj.move = setInterval(function() {
			var step = (target - obj.offsetLeft) / 10;
			step = step > 0 ? Math.ceil(step) : Math.floor(step);
			if (obj.offsetLeft == target) {
				clearInterval(obj.move);
				//这里的判断也可以换成callback && callback()
				if(callback){
					callback();
				}
			} else {
				obj.style.left = obj.offsetLeft + step + 'px';
			}
		}, 15);
	}

	var c = document.querySelector('.c');	//左边按钮
	var d = document.querySelector('.d');	//右边按钮
	var num = 0;	//记录按钮点击次数
	var cir = 0;	//记录小圆点

	for(var i = 0;i < lis.length;i++){
		lis[i].addEventListener('click',function(){
			// 使用排他思想实现的小圆点点击
			for(var j=0;j<lis.length;j++){
				lis[j].className = 'e';
			}
			this.className = 'e ee';

			var index = this.getAttribute('data-x');	//记录自定义函数
			// 记录点击小圆圈的值,以免你再点击左右按钮时错位
			num = index;
			// 记录小圆圈的值，让小圆圈跟着你的图片动
			cir = index;
			animate(ul_b,-index * 350);
		})
	}

	//排他思想实现小圆圈的显示
	var cir_change = function(){
		for(var i=0;i<lis.length;i++){
			lis[i].className = 'e';
		}
		lis[cir].className = 'e ee';
	}

	var flag = true;	//节流阀的使用

	// 右按钮功能实现
	d.addEventListener('click',function(){
		// 节流阀的使用
		if(flag){
			flag = false;
			// 当到了最后一页的时候,因为我们多一张图片(为了动画效果)
			// 当到了最后一张图片，将左右按钮记录值归零，并且将图片移动到0，再执行动画函数运行到第二张
			if(num == ul_b.children.length-1){
				ul_b.style.left = 0;
				num = 0;
			}
			num++;
			animate(ul_b, -num * 350 , function(){
				flag = true;
			});
			cir++;
			//如果移动到最后一张图片，就返回到第一张
			cir = cir == 3 ? cir =0 : cir;

			cir_change();
		}
	})

	// 左按钮功能实现
	c.addEventListener('click',function(){
		if(flag){
			flag = false;
			// 当到了第一张图片，点击左按钮移动到最后一张，然后执行动画函数
			if(num == 0){
				num = ul_b.children.length-1;
				ul_b.style.left = -num * 350 + 'px';
			}
			num--;
			animate(ul_b, -num * 350,function(){
				flag = true;
			});

			cir--;
			cir = cir < 0 ? cir = ul_b.children.length - 2 : cir;

			cir_change();
		}
	})

	//轮播图自动播放
	var timer = setInterval(function(){
		d.click();
	},2000);
})
```

这里有一个小技巧，当你使用的回调函数的时候，判断回调函数存在时可以使用下面的表达式

这是为什么呢？这是因为&&，当前面为 true 的时候就执行后面的 callback()，假如是 false 的时候就不执行，这不是和我们这里 if 的判断模式很像

```html
if(callback){
	callback();
}
//可以换成下面的形式
callback && callback();
```

#### 16.5.3 回到顶部

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
				width: 50%;
				height: 1000px;
				background-color: pink;
			}
			.nav{
				width: 100px;
				height: 50px;
				background-color: blueviolet;
				line-height: 50px;
				text-align: center;
				cursor: pointer;
				position: absolute;
				left: 60%;
				top: 900px
			}
		</style>
	</head>
	<body>
		<div class="main"></div>
		<div class="nav">回到顶部</div>

		<script type="text/javascript">
			var nav = document.querySelector('.nav');

			nav.addEventListener('click',function(){
				animate(window,0);
			})

			function animate(obj, target, callback) {
				clearInterval(obj.move);
				obj.move = setInterval(function() {
					var step = (target - window.pageYOffset) / 10;
					step = step > 0 ? Math.ceil(step) : Math.floor(step);

					if (window.pageYOffset == target) {
						clearInterval(obj.move);
						if(callback){
							callback();
						}
					} else {
						window.scroll(0,window.pageYOffset + step);
					}
				}, 15);
			}
		</script>
	</body>
</html>

```

![[00 assets/b3d28546fca7b246c2bc17da0ca6c482_MD5.gif]]

## 17. 移动端网页特效

### 17.1 触屏事件

移动端浏览器的兼容性比较好，我们不需要考虑 JS 的兼容性问题，所有我们卡哇伊使用原生 JS 的书写效果，但是移动端也有自己独特的地方，比如说触屏事件 touch

![[00 assets/87099ccb169bed803e8f44f730d4a162_MD5.png]]

下面演示的是上面的触屏事件 s

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="main"></div>
		<script type="text/javascript">
			var main = document.querySelector('.main');

			main.addEventListener('touchstart',function(){
				main.style.backgroundColor = 'red';
			})

			main.addEventListener('touchmove',function(){
				main.style.backgroundColor = 'blue';
			})

			main.addEventListener('touchend',function(){
				main.style.backgroundColor = 'cadetblue';
			})
		</script>
	</body>
</html>

```

![[00 assets/3d9eac69e9d21a68e024ba75afde7fb6_MD5.gif]]

### 17.2 触摸事件对象

触摸事件是一类描述手指再触摸平面的状态变化的事件，这类事件用于描述一个或多个触电，使开发者可以检测触电的移动，触电的增加和减少，上面提到的，touchstart，touchmove，touchead 三个事件都会有各自的事件对象

我们先来看 touchstart 的事件对象

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
				background-color: pink;
			}
		</style>
	</head>
	<body>
		<div class="main"></div>
		<script type="text/javascript">
			var main = document.querySelector('.main');

			main.addEventListener('touchstart',function(e){
				console.log(e);
			})

		</script>
	</body>
</html>

```

![[00 assets/63f04b7eb7b316ec69392e9fecb20851_MD5.png]]

这几个是最重要的

![[00 assets/03e1b371399f788e287a2d6b0c303669_MD5.png]]

当然这 3 个最重要的触摸列表中最重要的是 changedTouches

我们使用 targetTouches[0]就可以得到触摸 dom 元素的第一个手指的相关信息

### 17.3 移动端拖动元素

移动端拖动的原理：手指移动时，计算出手指移动的距离，然后用盒子原来的位置+手指移动的位置就可以了

拖动元素的三步：1)触摸元素 touchstart：获取手指初始坐标，同时获得盒子原来的位置 2)移动手指 touchmove：计算手指的滑动距离，并且移动盒子 3)离开手指 touchend

假如说你要阻止默认的屏幕滚动的话，就使用 e.prevevtDefault();

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
				background-color: pink;
				position: absolute;
				left: 0px;
				top: 0px;
			}
		</style>
	</head>
	<body>
		<div class="main"></div>

		<script type="text/javascript">
			var main = document.querySelector('.main');

			var startX = 0;	//获取手指初始坐标
			var startY = 0;
			var x = 0;	//获取盒子原来的位置
			var y = 0;

			main.addEventListener('touchstart',function(e){
				//获取手指的初始位置
				startX = e.targetTouches[0].pageX;
				startY = e.targetTouches[0].pageY;
				x = this.offsetLeft;
				y = this.offsetTop;
			});

			main.addEventListener('touchmove',function(e){
				//获取手指的移动位置
				var moveX = e.targetTouches[0].pageX - startX;
				var moveY = e.targetTouches[0].pageY - startY;
				this.style.left = x + moveX + 'px';
				this.style.top = y + moveY + 'px';

				//阻止默认的屏幕滚动
				e.preventDefault();
			});
		</script>
	</body>
</html>
```

![[00 assets/c65dcda7a9fff4adcfeb2e02e9073282_MD5.gif]]

### 17.4 移动端 click 事件 300ms 延时问题解决

为什么会有这个问题，这时因为移动端屏幕双击会缩放页面，设置这个 300ms 的延迟是为了双击缩放的准确性

P345，P346

### 17.5 插件的使用

> Swiper：https://www.swiper.com.cn/

这是一个专门写轮播图的网站，相关的引用可以参考 bootstrap，在我本地文件 JS 里面有 swiper-7.4.1

> SuperSlide：http://www.superslide2.com/index.html

> iScroll 5：http://caibaojian.com/iscroll-5/

### 17.6 框架的使用

也就是 bootstrap，vue，react 等

### 17.4 案例

#### 17.4.1 移动端轮播图

还没写，记得 P335-P343

#### 17.4.2 回到顶部

P344

#### 17.4.3 记住用户名

P357

# 补充

## 1. CodePointAt()

下面是输出字符串的编码数字

```javascript
let val = 'a';
console.log(val.codePointAt());
//97
```

## 2. 输出 99 乘法表

这个主要是标签的创建

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			td {
				border: 1px solid black;
				background-color: blue;
			}
		</style>
	</head>
	<body>
		<button type="button" class="btn">点击我变换颜色</button>
		<script type="text/javascript">
			var bg = "<table>";
			for (var i = 1; i <= 9; i++) {
				bg += "<tr>";
				for (var j = 1; j <= i; j++) {
					bg += "<td>" + i + "*" + j + "=" + i * j + "</td>";
				}
				bg += "</tr>";
			}
			bg += "</table>";
			document.write(bg);

			let btn = document.querySelector('.btn');
			let td = document.querySelectorAll('td');
			console.log(td);

			function randomColor() {
				var hex = Math.floor(Math.random() * 16777216).toString(16);
				while (hex.length < 6) {
					hex = '0' + hex;
				}
				return '#' + hex;
			}
			btn.onclick = function(){
				for(let i = 0;i<td.length;i++)
					td[i].style.backgroundColor = randomColor();
			}
		</script>
	</body>
</html>

```

![[00 assets/3ebd64b2eedc6e677aed82e1a80bf9f2_MD5.png]]

## 3. 优化冒泡排序

这个优化的部分就是你判断已经排好了，也就是说前一个一直比后一个大，就是排序完成，就直接跳出外部循环

```javascript
var arr = [1, 8, 4, 5, 7, 23, 3, 76, 7, 34, 6, 3],
	t = 0;
var n = 0,
	m = 0;
var flag;
for (var i = 0; i < arr.length - 1; i++) {
	flag = true;
	for (var j = 0; j < arr.length - i - 1; j++) {
		m++
		if (arr[j + 1] > arr[j]) {
			flag = false;
			t = arr[j];
			arr[j] = arr[j + 1];
			arr[j + 1] = t;
		}
	}
	if (flag) break;
	n++;
}
console.log(arr);
console.log(m + ' ' + n);
```

## 4. 三级城市联动

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
		<select class="first">
			<option>请选择</option>
		</select>
		<select class="second">
			<option>请选择</option>
		</select>
		<select class="third">
			<option>请选择</option>
		</select>
		<script type="text/javascript">
            //数组
			var first_con = ['上海', '江苏'];
			var second_con = [
				['上海市'],
				['苏州市', '南京市']
			];
			var third_con = [
				[
					['黄浦区', '静安区']
				],
				[
					['虎丘区', '吴中区'],
					['玄武区', '秦淮区']
				]
			];
			//获取元素
			var first = document.querySelector('.first');
			var second = document.querySelector('.second');
			var third = document.querySelector('.third');

            //构造option的方法
			function Create(obj, data) {
				for (let i in data) {
                    //这里的Option实例的
					var option = new Option(data[i], i);
					obj.options.add(option);
				}
			}

            //创建第一个option的
			Create(first, first_con);

            //创建第二个
			first.onchange = function() {
				second.options.length = 0;
				Create(second, second_con[first.value]);
                //onchange只要你的选项改变了就触发事件，但是上海只有一个上海市，所以就触发不了，这个时候就需要手动触发一次
				if(second.value >= 0) second.onchange();
				//并且要注意长度赋值为0，不然的话就叠加了
                else third.options.length = 0;
			}

            //创建第三个
			second.onchange = function() {
				third.options.length = 0;
				Create(third, third_con[first.value][second.value]);
			}
		</script>
	</body>
</html>

```

## 5. 猴子数大王

这个其本质就是 1 2 3 ，然后变为 2 3 1，然后再 3 1 2，然后依次循环再减去，和 c 语言不一样，c 是使用链表的，但是 js 可以直接使用数组的方法

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script type="text/javascript">
			var total = prompt('请输入猴子的总数');
			var num = prompt('请输入踢掉第几个猴子');
			var monkey = [];
			let flag = 0;

			for (let i = 1; i <= total; i++) monkey.push(i);

			while (monkey.length > 1) {
				flag++;
				head = monkey.shift();
				if (flag % num != 0) {
					monkey.push(head);
				}
			}
			console.log(monkey);
		</script>
	</body>
</html>

```

## 6. 拷贝

深拷贝和浅拷贝只是针对 Object 和 Array 这样的引用数据类型的。

**浅拷贝**： 将原对象或原数组的引用直接赋给新对象，新数组，新对象／数组只是原对象的一个引用

**深拷贝**： 创建一个新的对象和数组，将原对象的各项属性的“值”（数组的所有元素）拷贝过来，是“值”而不是“引用”

**赋值和浅拷贝的区别**

当我们把一个对象赋值给一个新的变量时，赋的其实是该对象在栈中的地址，而不是堆中的数据。也就是两个对象指向的是同一个存储空间，无论哪个对象发生改变，其实都是改变的存储空间的内容，因此两个对象是联动。

浅拷贝是按位拷贝对象，它会创建一个新对象，这个对象有着原始对象属性值的一份精确拷贝。如果属性是基本类型，拷贝的就是基本类型的值；如果属性是内存地址(引用类型)，拷贝的就是内存地址，因此如果其实一个对象改变了这个地址，就会影响到另一个对象，即默认拷贝构造函数只是对对象进行浅拷贝赋值(逐个成员依次拷贝)，即只复制对象空间而不复制资源。

下面就是只是将地址给了它，所以就有了联动的效果，你想修改 Student 的 name，但是最后还是修改了 Person

```javascript
let Person = {
	name:'张三',
	age:18,
	hobby:['吃饭','游戏'],
	RecPerson:{
		p1:{id:001},
		p2:{id:002}
	}
}

let Student = Person;
Student.name = '李四'
Student.hobby[0] = '打牌'
Student.RecPerson.p1 = {id:003}

console.log(Student)
```

![[00 assets/289707711c2ecbbea1354aa88d3a11f3_MD5.png]]

```javascript
let Person = {
	name:'张三',
	age:18,
	hobby:['吃饭','游戏'],
	RecPerson:{
		p1:{id:001},
		p2:{id:002}
	}
}

function Copy(Obj){
	let data = {}
	for(let prop in Obj){
		if(Obj.hasOwnProperty(prop)){
			data[prop] = Obj[prop]
		}
	}
	return data;
}

let Student = Copy(Person);

Student.name = '李四'
Student.hobby[0] = '打牌'
Student.RecPerson.p1 = {id:003}

console.log(Student)
console.log(Person)
```

![[00 assets/1a4845a361a23ac663a72502faba725a_MD5.png]]

![[00 assets/e6bfb1c44e69e5547d93c6e248dd4847_MD5.png]]

**浅拷贝**

1.**...**

```
let Person = {
	name:'张三',
	RecPerson:{
		p1:{id:001}
	}
}
let Student = {...Person}
console.log(Student)
```

**深拷贝**

1.JSON.parse(JSON.stringify())

```javascript
let Person = {
	name:'张三',
	RecPerson:{
		p1:{id:001}
	}
}
let Student = JSON.parse(JSON.stringify(Person))
console.log(Student)
```

2.使用原生的方法

```javascript
let copy = function(){
	var temp = {}
	for(var k in this){
		if(typeof this[k] === 'object'){
			temp[k] = this[k].copy();
		}else{
			temp[k] = this[k]
		}
	}
	return temp
}

let Student = {
	sex:'男',
}
let Person = {
	name:'张三',
	age :18,
	Student,
}
Student.copy = copy;
Person.copy = copy;

let NewPerson = Person.copy();
```

## 7. url 获取

```javascript
console.log(location.href)	//结果：http://127.0.0.1:5500/about.html
console.log(location.host)	//结果：127.0.0.1:5500
//还有其他相应的url获取的方式
```

## 8. classList.XXX

[(42 条消息) 原生 js—classList.add()、classList.remove()、classList.contains()、classList.toggle()、\_男孩子小杨的博客-CSDN 博客\_classlist.add](https://blog.csdn.net/qq_43495629/article/details/87867005)

```html
<div class="main"></div>
```

```javascript
var div = document.querySelector(".main")
div.classList.remove("main")
```

这个 API 可以对这个元素的 class 属性进行操作，其他的 API 可以查看上面网址里面的使用方式

## 9. eventPhase 属性

[Event.eventPhase - Web API 接口参考 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/eventPhase)

这个 API 可以获取当前事件的状态

## 10. in

```javascript
var obj = {name:'张三'}
console.log('name' in obj)
//true
//用于检测一个对象里面有没有这个属性
```

## 11. 无法事件冒泡的事件

[JavaScript 中那些不会冒泡的事件 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/164844013)

## 12. 文档高度宽度理解

[javascript 中的各种 width,height 属性整理 - 工程师 wyy - 博客园 (cnblogs.com)](https://www.cnblogs.com/w-y-y/p/7083119.html)

## 13. 不加分号的后果

参考文档：[代码结构 (javascript.info)](https://zh.javascript.info/structure)

因为 JavaScript 里面没有特别强调分号，但是不加上的话还是会有问题

```javascript
alert("这是一个alert语句")
[1,2].forEach(element => {console.log(element)});
```

会报错，这是为什么呢？

![[00 assets/2abc1979fc15e404924c3baaa0f5dccc_MD5.png]]

其实 JS 吧这 2 句当作是一句话了，所以就会报错

![[00 assets/cf18554dae60fde02fb3358f312014e9_MD5.png]]

假如我们加上分号的话就没问题了

## 14. 现代模式，"use strict"

参考模式：[现代模式，"use strict" (javascript.info)](https://zh.javascript.info/strict-mode)

因为 JS 的很多 API 其实设计的不是很好，但是又不能去修改，所以就有了这个模式

但是你写了这个模式，和不写这个模式有什么区别吗？是有的，我们在日常的 js 里面是可以写的

![[00 assets/d06675607abb8e7d5715c71f07c8eb1f_MD5.png]]

但是我们开启现代模式的话，就会有问题

![[00 assets/6c8c191959c6a0fa715138a9a929260d_MD5.png]]

## 15. bind

bind 官方文档：[Function.prototype.bind() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
