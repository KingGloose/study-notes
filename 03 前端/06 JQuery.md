# JQuery

## 1. JQuery 概述

### 1.1 JavaScript 库

即 library，是一个封装好的特定的集合（方法和函数），这些经过原生 JS 封装好的就叫做 JS 库，这是为了更加高效的使用这些封装好的功能

常见的 JS 库：Jquery，Prototype，YUI，Dojo，Ext JS 等等

### 1.2 JQuery

J 就是 JavaScript，Query 就是查询，把 JS 中的 DOM 操作做了封装，我们可以快速查询里面的功能

优化了 DOM 操作、事件处理、动画设计、Ajax 交互

学习 JQuery 的本质就是学习调用这些函数（方法）

### 1.3 JQuery 下载

下载网址：https://jquery.com/download/

production 是工程的 Jquery，这个是经过压缩的文件

development 是开发的 jQuery，里面还保留了相关的注释

![[00 assets/22785ccd5482300e8e8996bf6de80ce3_MD5.png]]

## 2. JQuery 基本语法

### 2.1 入口函数

也就是原生 JS 的 load 的加载事件

下面是第一种写法

$('div').hide()是隐藏元素

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			$(document).ready(function(){
				$('div').hide();
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

下面是第二种写法

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			$(function(){
				$('div').hide();
			})
		</script>
	</head>
	<body>
		<div class="main"></div>

	</body>
</html>

```

1. 等着 DOM 结构渲染完毕既可执行内部代码，不必等到所有外部资源加载完成，JQuery 帮我们完成了封装
2. 相当于原生 JS 里面的 DOMContentLoaded
3. 不同原生 JS 中的 load 事件是等页面结构、外部 JS、css、图片加载完毕才执行

### 2.2 顶级对象$

其实$符号和Jquery是一样的，但是为了方便，通常直接使用$

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main{
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			jQuery(function(){
				jQuery('div').hide();
			})

			// $(function(){
			// 	$('div').hide();
			// })
		</script>
	</head>
	<body>
		<div class="main"></div>

	</body>
</html>

```

$相当于原生 JS 中的 window

### 2.3 JQuery 对象和 DOM 对象

Jquery 对象和 DOM 对象获取的方式是不一样的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			$(function() {
                //原生JS获取的方式
				var divs = document.querySelector('div');
				//JQuery获取的方式
				$('div');
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

并且获取来的信息也是不一样的，很明显原生 JS 获取来的信息更加多

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			$(function() {
				var divs = document.querySelector('div');
				console.dir(divs);

				$('div');
				console.dir($('div'))
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/371e7d51d8facfdfec26af65da7a97fb_MD5.png]]

其实 Jquery 对象的本质是利用$对 DOM 对象包装后产生的对象，只不过是采用伪数组来存储的

要记住的是原生 JS 获取的 DOM 对象，只能使用原生 JS 的语法，不能使用 jQuery 的语法，JQuery 对象只能使用 JQuery 的方法

DOM 对象和 JQuery 对象之间是可以相互转换的，因为原生 JS 比 JQuery 更加大，原生的一些属性和方法 JQuery 没给我们封装进去，要想使用原生的 JS，就需要将 JQuery 对象转换为 DOM 对象才能使用

**DOM 对象转换为 JQuery 对象**

注意转换的格式问题，将 DOM 对象转换为 JQuery 对象是不用加引号的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			$(function() {
                //直接获取Jquery对象
				$('.main');
				console.dir($('.main'));

                //将DOM对象转换为JQuery对象
				var JQuery_main = document.querySelector('.main');
				$(JQuery_main);
				console.dir($(JQuery_main));
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

**JQuery 对象转换为 DOM 对象**

$('获取的值')[index]

$('获取的值').get(index)

这两种方式都是可以转换的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script type="text/javascript">
			$(function() {
				$('.main')[0].style.backgroundColor = 'red';
				// $('.main')get(0).style.backgroundColor = 'red';
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

## 3. JQuery 的常见 API

### 3.1 JQuery 选择器

#### 3.1.1 JQuery 各种选择器

原生 JS 获取元素的方式很多很杂，而且兼容性不同，因此 JQuery 给我们做了封装，使得获取元素统一标准

```
$('选择器')
```

![[00 assets/2b3778843ed6110cacfe1ea376df25f4_MD5.png]]

![[00 assets/35a6c4ec4cd0af4aa05ba2b328b31b72_MD5.png]]

下面就是关于 JQuery 选择器的使用，下面的代码证明后代选择器也是可以的，相应的伪类选择器也是可以生效的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
			.small{
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
		<script type="text/javascript">
			$(function() {
				$('.main .small')[0].style.backgroundColor = 'red';
				console.dir($('.main .small'));
			})
		</script>
	</head>
	<body>
		<div class="main">
			<span>123</span>
			<div class="small">123</div>
		</div>
	</body>
</html>

```

![[00 assets/11af4a11148f1072a317deb34d1a9112_MD5.png]]

#### 3.1.2 隐式迭代

遍历内部 DOM 元素（伪数组形式存储）的过程就叫做隐式迭代

是将匹配到的所有元素内部进行遍历循环，而不是自己写

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
			}
		</style>
		<script type="text/javascript">
			$(function() {
				$('div').css('background-color','pink');
			})
		</script>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>
		<div>4</div>
	</body>
</html>

```

![[00 assets/88599a73204b3cc71b1bda49c41973f7_MD5.png]]

我们这边可以查看一下 JQuery 获取来的元素，其实就是伪数组里面 4 个 div

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
			}
		</style>
		<script type="text/javascript">
			$(function() {
				$('div').css('background-color','pink');
				console.dir($('div'));
			})
		</script>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>
		<div>4</div>
	</body>
</html>

```

![[00 assets/f2e718ee579c9fa9052d3fac5121c520_MD5.png]]

#### 3.1.3 JQuery 筛选选择器

![[00 assets/c1ce5c15253403efe1c7f8567ab96160_MD5.png]]

#### 3.1.4 JQuery 筛选方法

下面图有一个错误，prevAll，没有 t

![[00 assets/46c03d2a1c256619b13e89d28f23b048_MD5.png]]

其本质基本和 DOM 操作，CSS 选择是一样的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			div{
				width: 100px;
				height: 100px;
			}
		</style>
		<script type="text/javascript">
			$(function() {
				console.dir($('.son').parent());
				console.dir($('.father').children('li'));
				console.dir($('.father').find('li'));
				console.dir($('.son').siblings('li'));
				console.dir($('.son').nextAll('li'));
				console.dir($('.son').prevAll('li'));
				console.dir($('.father li').hasClass('bro1'));
				console.dir($('.father li').eq(2));
			})
		</script>
	</head>
	<body>
		<ul class="father">
			<li class="bro1">1</li>
			<li class="bro2">2</li>
			<li class="son">3</li>
			<li class="bro3">4</li>
			<li class="bro4">
				5
				<ul>
					<li class="bro5"></li>
					<li class="bro6"></li>
					<li class="bro7"></li>
				</ul>
			</li>
		</ul>
	</body>
</html>

```

![[00 assets/c0724b28b30137342b1d87602b5ae617_MD5.png]]

其中 siblings 可以作为排他思想来使用

### 3.2 链式编程

下面这段代码是案例里面排他思想的一段代码

我们可以发现在写 JQuery 排他思想的时候，核心代码有两段是一样的，代码是不允许一样的代码出现多次，这里就出现了我们的 JQuery 的链式编程

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.nav{
				width: 500px;
				list-style: none;
				display: flex;
				justify-content: space-around;
			}
			.nav li{
				color: pink;
				font-size: 25px;
				cursor: pointer;
			}
		</style>
		<script type="text/javascript">
			$(function(){
				$('.nav').children('li').mouseover(function(){
					$(this).css('color','red');
					$(this).siblings('li').css('color','');
				})
			})
		</script>
	</head>
	<body>
		<ul class="nav">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
		</ul>
	</body>
</html>

```

下面就是链式编程的写法，代替上面的两段代码

```html
$(this).css('color','red').siblings('li').css('color','');
```

我们还可以换一个案例来实现链式编程，在案例 3.8.3 淘宝服饰就可以改为链式编程

```html
$('.main_img img').eq(index).show().siblings('img').hide();
```

这样可以节省很多代码量，让编写更加优雅

### 3.3 JQuery 样式操作

#### 3.3.1 CSS 操作

查看 CSS 样式的属性值的话，你只在 css()方法里面写属性名就可以了，返回值就是属性值

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				console.log($('.main').css('width'));
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/a942039cd2f99e8b8c030d70add873c4_MD5.png]]

当然我们也可以去修改 css 的值

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main').css('background-color','red');
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/843736f5b651dad2b114d74a55cd0b42_MD5.png]]

参数也可以是对象的形式，设置多个 css 样式值，记得里面还有一个括号

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main').css({
					'background-color':'red',
					'width':'400px'
				});
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/70869d2407de981df2b0f2568ba13553_MD5.png]]

#### 3.3.2 设置类样式方法

addClass('类名')，添加类

removeClass('类名')，删除类

toggleClass('类名')，切换类，假如你有的话就删除，假如你没有的话就添加

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
			}
			.main_col{
				background-color: pink;
			}
			.main_text_col{
				color: cadetblue;
				font-size: 30px;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main').addClass('main_col');
				$('.main').removeClass('main_text_col');
				$('.main').toggleClass('main_col');
			})
		</script>
	</head>
	<body>
		<div class="main main_text_col">这是一个可爱的语句</div>
	</body>
</html>

```

![[00 assets/5725b7ef99d1dcc9bac4258920539c1f_MD5.png]]

在原生的 JS 和 JQuery 的类名操作有一些区别，原生 JS 的 className 会覆盖掉原先里面的类名，但是 JQuery 里面类的操作只是对指定类进行操作，不会影响原先的类名，和原生 JS 的 classlist 是基本一样的

我们先来看原生 JS 的操作

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			window.addEventListener('load',function(){
				var main = document.querySelector('.main');
				main.className = 'nav';
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/e7a1fdfdc7a9088bfeecbea2818e34f9_MD5.png]]

但是在我们的 JQuery 里面是不影响的

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main').addClass('nav');
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/98d615f23653e22f5e54afb64f4f87b8_MD5.png]]

### 3.4 JQuery 效果

JQuery 封装了很多的动画效果

![[00 assets/3bf40b01a8847b148499c5128cba4ece_MD5.png]]

#### 3.4.1 显示和隐藏

![[00 assets/8b93018ea8dec9186330c8f252c6c013_MD5.png]]

当然我们还有隐藏的方法

![[00 assets/96ffc03e23ee5a4e1601ff409a0fe5c2_MD5.png]]

toggle 的语法格式是和上面一样的，但是 toggle 是只要隐藏了就显示，显示了就隐藏

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				$('.xian').click(function() {
					$('.main').show(1000, 'linear', function() {
						alert('你显示了哦!');
					})
				})

				$('.ying').click(function() {
					$('.main').hide(1000, 'linear', function() {
						alert('你隐藏了哦!');
					})
				})

				$('.qie').click(function(){
					$('.main').toggle(1000,'linear',function(){
						alert('你切换了哦');
					})
				})
			})
		</script>
	</head>
	<body>
		<button type="button" class="xian">显示</button>
		<button type="button" class="ying">隐藏</button>
		<button type="button" class="qie">切换</button>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/55d6274cd302cd054e8cc40a31461503_MD5.gif]]

#### 3.4.2 滑动

其实和上面的语法格式是一样的，所以这里就不再赘述了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				$('.xian').click(function() {
					$('.main').slideDown(1000, 'linear', function() {
						alert('你显示了哦!');
					})
				})

				$('.ying').click(function() {
					$('.main').slideUp(1000, 'linear', function() {
						alert('你隐藏了哦!');
					})
				})

				$('.qie').click(function(){
					$('.main').slideToggle(1000,'linear',function(){
						alert('你切换了哦');
					})
				})
			})
		</script>
	</head>
	<body>
		<button type="button" class="xian">显示</button>
		<button type="button" class="ying">隐藏</button>
		<button type="button" class="qie">切换</button>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/637b79f96bce599c652a8a316713580b_MD5.gif]]

#### 3.4.3 事件切换

我们在案例 3.8.1 的下拉菜单中就使用了鼠标经过和移开，这里我们介绍另一个，这个也可以进行鼠标的经过和移开，这个更加简单，更加高效

使用 hover 方法就可以了，houver(1,2)，其中 1 表示 mouseenter，也就是鼠标移入的意思，其中 2 就是 mouseleave，也就是鼠标移出的意思

```html
$(function() {
	$(".nav>li").hover(
		function(){
			$(this).children('ul').slideDown(200);
		},function() {
			$(this).children('ul').slideUp(200);
		}
	);
})
```

当然我们也可以更加简单，假如你在 hover 里面只写一个的话，就是你鼠标移入执行这个函数，鼠标移开也移动这个函数

我们只要将上面的写法改成这样下面的就可以了

```html
$(function() {
	$('.nav>li').hover(function(){
		$(this).children('ul').slideToggle(200);
	});
})
```

#### 3.4.5 停止动画排队

假如我们按照上面的写法来写的话，就会有一些小问题，我们将鼠标快速滑动的时候就会有这样的问题

![[00 assets/0380ec41f8a4b10decb5d8ed264034e4_MD5.gif]]

这个时候我们就需要动画停止函数，也就是 stop()，这个使用有一个注意的点，就是要写在动画的前面，不然不能阻止上面的问题，当然我们也可以写在其他的地方

假如我们要修正的话，就要写成下面这个样子

```html
$(function() {
	$('.nav>li').hover(function(){
		$(this).children('ul').stop().slideToggle(200);
	});
})
```

#### 3.4.6 淡入淡出

淡入 fadeTo，淡出 fadeOut，切换 fadeToggle，还有透明度切换 fadeTo，其中语法格式基本和上面都是一样的，除了 fadeTo(speed,opacity,easing,fn)是这样的语法格式

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.main {
				width: 200px;
				height: 200px;
				background-color: pink;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				$('.ru').click(function() {
					$('.main').fadeIn(1000, 'linear', function() {
						alert('这是淡入哦');
					})
				})

				$('.chu').click(function() {
					$('.main').fadeOut(1000, 'linear', function() {
						alert('这是淡出哦');
					})
				})

				$('.qie').click(function(){
					$('.main').fadeToggle(1000,'linear',function(){
						alert('这是淡入淡出切换哦');
					})
				})

				$('.tou').click(function(){
					$('.main').fadeTo(1000,0.5,function(){
						alert('渐进方式调整');
					})
				})
			})
		</script>
	</head>
	<body>
		<button type="button" class="ru">淡入</button>
		<button type="button" class="chu">淡出</button>
		<button type="button" class="qie">淡入淡出切换</button>
		<button type="button" class="tou">修改透明度</button>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/74db03fe1c1a68edfabff54b8be4218c_MD5.gif]]

#### 3.4.7 自定义动画

![[00 assets/f0ebb051e13202f9fa8498253953660b_MD5.png]]

其实这个本质和 CSS3 的动画格式是差不多的，其中 params 是按照对象的格式来写的

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.ani{
				width: 200px;
				height: 200px;
				background-color: pink;
				position: absolute;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('button').click(function(){
					$('.ani').animate({
						left:100,
						top:100,
						opacity:.5,
						height:300,
						width:300
					},500)
				});
			})
		</script>
	</head>
	<body>
		<button type="button">动画效果</button>
		<div class="ani"></div>
	</body>
</html>

```

![[00 assets/38bd48d92f8313b982d38dccacdf16eb_MD5.gif]]

### 3.5 JQuery 属性操作

#### 3.5.1 固有属性值 prop()

固有属性值就是元素本身自带的属性，比如说 a 元素里面 href，input 里面的 type

获取的语法格式是 prop('属性名')

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				console.log($('a').prop("href"));
			})
		</script>
	</head>
	<body>
		<a href="www.baidu.com">点击链接</a>
	</body>
</html>

```

![[00 assets/9d5e71aaefe57403f157d20d9f456dcf_MD5.png]]

当然我们还可以修改属性值，其语法格式是 prop('属性名','属性值')

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				console.log($('a').prop("href",'www.bilibili.com'));
			})
		</script>
	</head>
	<body>
		<a href="www.baidu.com">点击链接</a>
	</body>
</html>

```

当然我们还可以看到 input 的 checked 的属性

change()方法是，只要你改变就会触发里面的函数

当你点击了复选框的话，就会检查 checked

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('input').change(function(){
					console.log($(this).prop('checked'));
				})
			})
		</script>
	</head>
	<body>
		<input type="checkbox" name="" id="" value="" checked="checked"/>
	</body>
</html>

```

![[00 assets/35035fcbcec57131a0401f7482f17396_MD5.png]]

#### 3.5.2 自定义属性 attr()

语法格式基本和上面的 prop()是一样的

![[00 assets/7681518af09ab004d3fb866029e387f1_MD5.png]]

#### 3.5.3 数据缓存

![[00 assets/80d290cd9abc02715fcb345fcecf08ad_MD5.png]]

这个是存在我们的内存里面，只要你刷新页面的话，就会丢失

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('div').data('uname','zhang');
				console.log($('div').data('uname'));
			})
		</script>
	</head>
	<body>
		<div index="1"></div>
	</body>
</html>

```

![[00 assets/9679cd9d40784649fdf15823f96c0c07_MD5.png]]

但是在我们的 H5 里面还有一个 data-index

我们在元素上面写上 data-index 的话，在 JQuery 里面用 attr 查看，和用 data 查看是不一样的，attr 查看的是自定义属性，也就是把 data-index 当作为自定义属性值了，但是使用 data()的话，就是直接获取的 H5 里面的 data-index 的值，再各个方法里面填入的属性值也是不一样的

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				console.log($('div').attr('data-index'));
				console.log($('div').data('index'));
			})
		</script>
	</head>
	<body>
		<div index="1" data-index="2"></div>
	</body>
</html>

```

![[00 assets/24ca8d7eea01513c074ed64d53ddf97e_MD5.png]]

### 3.6 JQuery 内容文本值

#### 3.6.1 普通内容

![[00 assets/8ef6ebb9ab771f27845868c6e7faf71c_MD5.png]]

大体是一样的，其中的差别就是 Innerhtml 和 innertext 是差不多的

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				console.log($('.main').html());
				$('.main').html('这是一个被html改变的语句');
				console.log($('.main').html());

				console.log('-----------');

				console.log($('.no').text());
				$('.no').text('这是一个被text改变的语句');
				console.log($('.no').text());
			})
		</script>
	</head>
	<body>
		<div class="main">这是一个可爱的语句</div>
		<div class="no">这不是一个可爱的语句</div>
	</body>
</html>

```

![[00 assets/9931745b5a37c7ef9c08629b4daa06d8_MD5.png]]

#### 3.6.2 表单内容

表单的话，可以使用 val()方法来表示和修改

但是要注意 val()里面的值，要修改的话，必须使用双引号 " " ，不然会导致无法修改

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				console.log($('input').val());
				$('input').val("我被修改了");
				console.log($('input').val());
			})
		</script>
	</head>
	<body>
		<input type="text" id="" value="这是一个寂寞的输入框" />
	</body>
</html>

```

![[00 assets/a04113db13136de3c53f60e7c13cec59_MD5.png]]

### 3.7 JQuery 遍历

![[00 assets/2a70a95cb4a9f3fd2e0647832250ad62_MD5.png]]

我们来看下面的代码

each 就很像前面的 foreach，就是一个个循环，其中回调函数里面的 index 是表示的序号，从上到下依次是 0,1,2，这个是自动编好的，domEle 是表示的 dom 对象，注意这里是 dom 对象，不是 JQuery 的对象，所以在这里要将 DOM 对象转换为 JQuery 对象，这个在前面有写

随后就是执行 css 方法，然后转回来继续循环

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				var color = ["blue","green","pink"];
				$('div').each(function(index,domEle){
					console.log(index + ' ' + domEle);
					console.log(domEle);

					$(domEle).css('color',color[index]);
				});
			})
		</script>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>
	</body>
</html>

```

![[00 assets/05674b07701d1476973fc3c59e6ac455_MD5.jpeg]]

在 JQuery 里面还有一个遍历的方式，这个是可以遍历任何对象

![[00 assets/1db9db21785785468894fa9ce4684e9b_MD5.png]]

而且输出的东西和上面是一样的，但是我们来看下面的遍历的东西，这个是可以遍历任何对象的

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				var color = ["blue","green","pink"];
				$.each(color,function(index,ele){
					console.log(index);
					console.log(ele);
				});
			})
		</script>
	</head>
	<body>
		<div>1</div>
		<div>2</div>
		<div>3</div>
	</body>
</html>

```

![[00 assets/96e6bc6226459f60eeada6a84ef64042_MD5.png]]

### 3.8 JQuery 尺寸、位置

#### 3.8.1 JQuery 尺寸

假如你要修改的话，就在里面添加数字，就可以修改

![[00 assets/4f9e2cf5af09b5ab0b28c7aa47528c67_MD5.png]]

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

				border: 50px solid blue;
				margin: 50px;
				padding: 50px;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				console.log($('.main').width());
				console.log($('.main').innerWidth());
				console.log($('.main').outerWidth());
				console.log($('.main').outerWidth(true));
			})
		</script>
	</head>
	<body>
		<div class="main">这是一个可爱的语句</div>
	</body>
</html>

```

![[00 assets/4aa4abdef08d3f6ba89b3552b5cc7599_MD5.png]]

#### 3.8.2 JQuery 位置

##### 3.8.2.1 offset()

![[00 assets/65d30706b5d7d7e27e5f3816ccace28e_MD5.png]]

offset()是查看元素距离文档的位置，假如我们单纯查看的话，就是返回的对象，对象里面的值有 left 和 top 值，假如我们要查看的话，就在后面写上.top 和.left 就可以查看相应的值了

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.father {
				width: 200px;
				height: 200px;
				background-color: pink;
				margin: 100px;
			}

			.son {
				width: 100px;
				height: 100px;
				background-color: blueviolet;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				console.log($('.son').offset());
				console.log($('.son').offset().left);
			})
		</script>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
	</body>
</html>

```

![[00 assets/40c72b9c3a3610411b7ff737f1eb73e3_MD5.png]]

当然我们也可以去修改里面的值，并且这是关于文档的距离，和父元素没关系

```html
$(function() {
	$('.son').offset({
		left:200,
		top:200
	});
})
```

##### 3.8.2.2 position()

![[00 assets/58017d92c3bbe3369b7c5fd0ac47ec3d_MD5.png]]

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

			.father {
				width: 200px;
				height: 200px;
				background-color: pink;
				margin: 100px;
				position: relative;
			}

			.son {
				width: 100px;
				height: 100px;
				background-color: blueviolet;
				position: absolute;
				left: 100px;
				top: 100px;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				console.log($('.son').position());
			})
		</script>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
	</body>
</html>

```

![[00 assets/71423694c50fce5bd232b04c17d2e53d_MD5.png]]

##### 3.8.2.3 被卷去的头部

下面代码写的是文档被卷曲的部分，在 JQuery 里面可以用 scrollTop()来是实现

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.father{
				width: 500px;
				height: 2000px;
				background-color: pink;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				$(window).scroll(function(){
					console.log($(document).scrollTop());
				})
			})
		</script>
	</head>
	<body>
		<div class="father"></div>
	</body>
</html>

```

![[00 assets/6e7131d522ead0c77d5ff8f115fd8da6_MD5.png]]

### 3.9 JQuery 事件

#### 3.9.1 事件注册

基本和上面的格式是一样的

![[00 assets/3da0d3ac39065e0207873e1d0b0d81fb_MD5.png]]

#### 3.9.2 事件处理

这个就可以注册多个事件

![[00 assets/dd6b149d7d8bb106dfb5ac2fd7a5f554_MD5.png]]

下面就是使用 on 来绑定事件

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('div').on({
					mouseenter:function(){
						$(this).css('background-color','red');
					},
					click:function(){
						$(this).css('background-color','blue');
					}
				})
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

![[00 assets/3e90747a9fd73b21c48812d6b5ce2d6f_MD5.gif]]

假如你多个处理的函数是一样的话，就可以变成下面这个样子

```html
$(function(){
	$('div').on("mouseenter click",function(){
		$(this).css('background-color','blue');
	});
})
```

事件的处理的优点

可以直接处理多个事件，并且可以实现事件委派的操作

下面代码就是事件委派的代码，第一个是原生事件委派的操作，父元素委派到子元素 li 上面

第二个是使用 on 的委派，是绑定在 ul 上，但是触发的对象是 li

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('ul li').click(function(){

				});	//事件委托实现的
				$('ul').on("click","li",function(){

				});
			})
		</script>
	</head>
	<body>
		<ul>
			<li></li>
			<li></li>
			<li></li>
		</ul>
	</body>
</html>

```

还有一个优点就是可以为动态创建的节点添加事件

这里有一个要注意的点，假如按照下面的方式来创建并且绑定是没有任何问题的

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				var li = $("<li>这是一个可爱的语句</li>");
				$('ol').append(li);
				$('ol li').click(function(){
					alert("没有出来了哦");
				});
				// $('ul').on("click",'li',function(){
				// 	alert("出来了哦");
				// });
			})
		</script>
	</head>
	<body>
		<ol>

		</ol>
	</body>
</html>

```

但是你按照下面的方式来创建的话就不行了，这是因为 click 不能绑定未来创建的 li，也就是说在创建之前绑定，假如我们使用 on 的话就没有任何问题

```html
$('ol li').click(function(){
	alert("没有出来了哦");
});
// $('ul').on("click",'li',function(){
// 	alert("出来了哦");
// });
var li = $("<li>这是一个可爱的语句</li>");
$('ol').append(li);
```

#### 3.9.3 事件解绑

使用 off()方法来解绑事件

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main').on({
					click:function(){
						console.log("我点击了");
					},
					mouseover:function(){
						console.log("我经过了");
					}
				});
				// $('.main').off();	//全部解绑
				$('.main').off('click');	//解绑鼠标点击事件
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

假如说我们要接触事件委托的话

```html
$('ul').off('click',"li");
```

#### 3.8.4 one()

用法和 on 是一样的，但是这个方法绑定的事件只能触发一次

#### 3.8.5 自动触发事件

自动触发事件，就是不去执行事件的操作也可以自动执行这个事件，比如说轮播图的右按钮点击

下面的三种方法都是可以触发自动事件的，最后一个 triggerHandler 和上面 2 个区别就是不会触发元素的默认行为，比如：input 的光标

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
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main').click(function(){
					console.log('我点击了');
				})
				// $('.main').click();
				// $('.main').trigger('click');
				// $('.main').triggerHandler('click');
			})
		</script>
	</head>
	<body>
		<div class="main"></div>
	</body>
</html>

```

#### 3.8.6 JQuery 事件对象

语法基本和原生 JS 是一样的

```
$('.main').click(function(e){
	console.log(e);
});
```

![[00 assets/30487ede2bbb67595771b7b339eb4b78_MD5.png]]

### 3.10 JQuery 其他方法

#### 3.10.1 JQuery 对象拷贝

这个东西不是很重要，记录一下留一个印象

基础的格式是$.extend(被拷贝的对象，拷贝的对象);

首先我们来看结果，将 p2 所有的数据都拷给了 p1，再来看，如果属性名是一样的话，就会覆盖

```javascript
$(function(){
	var p1 = {
		id:1
	};
	var p2 = {
		id:2,
		name:"ai",
		p3:{
			age:19
		}
	};
	$.extend(p1,p2);
	console.dir(p1);
})
```

![[00 assets/485c1aa881ae90eb0bbf4fc8b1df2322_MD5.png]]

extend 默认的是浅拷贝

![[00 assets/5f0a8c7eb9f27ffc52a01d08b927014a_MD5.png]]

如果是深拷贝的话就直接将原对象所有东西直接拷贝给被拷贝的对象，没有浅拷贝里面影响被拷贝对象

#### 3.10.2 多库共存

下面就是将原本的$改为 sc 了，这样的话，以后写 JQuery 的代码就是使用的 sc 来使用，但是原本的是可以使用的

```javascript
var sc = $.noConflict();
```

这个就是多库共存的问题，以免你写的$的方法和 jQuery 不兼容

### 3.8 案例

#### 3.8.1 下拉菜单

我们使用 JQuery 的语法就会简单很多

这里使用 JQuery 的话还有一些注意的地方，首先是选择器，我们获取过来的是.nav 下面的 li，这有 4 个，按照原生 JS 的写法，就必须一个个绑定鼠标移动的事件，但是 JQuery 有隐式迭代，就不用写那么多语法格式了，另外，Jquery 绑定事件也是一样的，直接在后面 .事件 就可以了，里面直接写函数，$(this)在 JQuery 里面代表的是 this

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.nav{
				width: 500px;
				list-style: none;
				display: flex;
				justify-content: space-around;
			}
			.nav li a{
				text-decoration: none;
				color: pink;
				font-size: 20px;
			}
			.nav li ul{
				list-style: none;
				margin-left: -30px;
				margin-top: 10px;
				display: none;
			}
		</style>
		<script type="text/javascript">
			$(function(){
				$('.nav>li').mouseover(function(){
					$(this).children("ul").show();
				})

				$('.nav>li').mouseout(function(){
					$(this).children("ul").hide();
				})
			})
		</script>
	</head>
	<body>
		<ul class="nav">
			<li>
				<a href="#">下拉</a>
				<ul>
					<li>1</li>
					<li>2</li>
					<li>3</li>
				</ul>
			</li>
			<li>
				<a href="#">下拉</a>
				<ul>
					<li>1</li>
					<li>2</li>
					<li>3</li>
				</ul>
			</li>
			<li>
				<a href="#">下拉</a>
				<ul>
					<li>1</li>
					<li>2</li>
					<li>3</li>
				</ul>
			</li>
			<li>
				<a href="#">下拉</a>
				<ul>
					<li>1</li>
					<li>2</li>
					<li>3</li>
				</ul>
			</li>
		</ul>
	</body>
</html>

```

![[00 assets/fc01454ab2f6b323a29c6fce7f10ba67_MD5.png]]

#### 3.8.2 排他思想

JQuery 的排他思想是很好做的，下面就是语法格式

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<style type="text/css">
			.nav{
				width: 500px;
				list-style: none;
				display: flex;
				justify-content: space-around;
			}
			.nav li{
				color: pink;
				font-size: 25px;
				cursor: pointer;
			}
		</style>
		<script type="text/javascript">
			$(function(){
				$('.nav').children('li').mouseover(function(){
					$(this).css('color','red');
					$(this).siblings('li').css('color','');
				})
			})
		</script>
	</head>
	<body>
		<ul class="nav">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
		</ul>
	</body>
</html>

```

![[00 assets/9dcd1e3dda0b1f9839424eeb7bf945a5_MD5.gif]]

#### 3.8.3 淘宝服饰

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
				display: flex;
				justify-content: center;
			}
			.main_ul li{
				list-style: none;
				width: 20px;
				height: 20px;
				background-color: pink;
				margin-top: 30px;
				cursor: pointer;
			}
			.main_img{
				width: 210px;
				height: 250px;
				border: 1px solid red;
			}
			.main_img img{
				width: 200px;
				height: 250px;
				position: absolute;
				left: 220px;
				top: 9px;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.main_ul li').mouseover(function(){
					var index = $(this).index();
					$('.main_img img').eq(index).show();
					$('.main_img img').eq(index).siblings('img').hide();
				})
			})
		</script>
	</head>
	<body>
		<div class="main">
			<ul class="main_ul">
				<li>1</li>
				<li>2</li>
				<li>3</li>
			</ul>
			<div class="main_img">
				<img src="img/1.gif" >
				<img src="img/2.gif" >
				<img src="img/3.gif" >
			</div>
		</div>
	</body>
</html>

```

![[00 assets/9e3bacf23049639cdf4d8ad413d84bfb_MD5.gif]]

#### 3.8.4 突出显示

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
				background-color: darkcyan;
			}
			.wrap{
				display: flex;
				justify-content: center;
				align-content: center;
				flex-wrap: wrap;
			}
			.wrap li{
				list-style: none;
			}
			.wrap li img{
				width: 300px;
				height: 300px;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function(){
				$('.wrap>li').hover(
					function(){
						$(this).siblings().stop().fadeTo(400,0.5);
					},function(){
						$(this).siblings().stop().fadeTo(400,1);
					}
				);
			})
		</script>
	</head>
	<body>
		<ul class="wrap">
			<li><img src="img/tom猫.jpeg"></li>
			<li><img src="img/v2-3628043abb578ef69eaa39249debc765_r.jpg"></li>
			<li><img src="img/喜马拉雅猫.jpeg"></li>
			<li><img src="img/异国短毛猫.jpeg"></li>
			<li><img src="img/苏格兰折耳猫.jpeg"></li>
			<li><img src="img/英国短毛猫.jpeg"></li>
		</ul>
	</body>
</html>

```

![[00 assets/bf163fc035dcb12e6d8cae017cea901a_MD5.gif]]

#### 3.8.5 王者手风琴

P384，P385

#### 3.8.6 购物车

P387，P388，P390，P391-P393，P396-P399

#### 3.8.7 带有动画的返回顶部

这里有一个要注意的点，就是要滚动的不是文档 document，而是元素滚动，所以这里使用的是 body 和 html

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style type="text/css">
			.father{
				width: 500px;
				height: 2000px;
				background-color: pink;
			}
			.hui{
				width: 50px;
				height: 50px;
				background-color: blueviolet;
				position: absolute;
				left: 600px;
				top: 1900px;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				$('.hui').click(function(){
					$('body,html').stop().animate({
						scrollTop:0
					})
				});
			})
		</script>
	</head>
	<body>
		<div class="father"></div>
		<div class="hui">回到顶部</div>
	</body>
</html>

```

![[00 assets/a85736d8d7fe2c6e81a27d6d1082aa17_MD5.gif]]

#### 3.8.8 电梯导航

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

			.one,
			.two,
			.three,
			.four {
				width: 500px;
				height: 700px;
			}

			.one {
				background-color: #8A2BE2;
			}

			.two {
				background-color: brown;
			}

			.three {
				background-color: chocolate;
			}

			.four {
				background-color: cornflowerblue;
			}

			.hui_ul {
				position: fixed;
				left: 580px;
				top: 200px;
			}

			.hui_ul li {
				width: 50px;
				height: 50px;
				list-style: none;
				margin-left: -40px;
				border: 1px solid #6495ED;
				cursor: pointer;
			}

			.current {
				background-color: pink;
			}
		</style>
		<script src="js/Jquery3.6-production.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			$(function() {
				var flag = true;

				var one_top = $('.one').offset().top;
				var two_top = $('.two').offset().top;
				var three_top = $('.three').offset().top;
				var four_top = $('.four').offset().top;

				//防止页面加载的时候，电梯消失
				sc_sc();
				function sc_sc() {
					if ($(document).scrollTop() >= 100) {
						$('.hui_ul').fadeIn();
					} else {
						$('.hui_ul').fadeOut();
					}
				}
				$(window).scroll(function() {
					sc_sc();
					if (flag) {
						$('.main div').each(function(index, ele) {
							if ($(document).scrollTop() >= $(ele).offset().top) {
								$('.hui_ul li').eq(index).addClass('current').siblings().removeClass();
							}
						})
					}
				});

				$('.hui_ul li').click(function() {
					flag = false;
					var index = $(this).attr('index');
					var sc_top = $('.main div').eq(index).offset().top;
					$('body,html').animate({
						scrollTop: sc_top
					},function(){
						flag = true;
					});
					$(this).addClass('current').siblings('.hui_ul li').removeClass();
				});


			})
		</script>
	</head>
	<body>
		<div class="main">
			<div class="one">页面A</div>
			<div class="two">页面A</div>
			<div class="three">页面A</div>
			<div class="four">页面A</div>
		</div>
		<ul class="hui_ul">
			<li index="0" class="current">页面A</li>
			<li index="1">页面B</li>
			<li index="2">页面C</li>
			<li index="3">页面D</li>
		</ul>
	</body>
</html>

```

![[00 assets/d9b4632d04a30fa1cb6384bdaa017742_MD5.gif]]

#### 3.8.9 微博发布案例

P412
