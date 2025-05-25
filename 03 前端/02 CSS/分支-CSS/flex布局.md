# 1 基本介绍

## 1.1 传统布局

兼容性好；布局繁琐；局限性，不能再移动端很好的布局

## 1.2 flex 弹性布局

操作方便；布局极为简单；移动端应用广泛，PC 端浏览器支持情况较差；IE11 或更低版本，不支持或仅支持部分

## 1.3 基础对比

假如你不设置 flex 的话，普通的行内元素是不能设置宽高的

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/facfe9410141dbf7748599c5b904be72_MD5.png]]

但是，假如你在父元素设置一个 flex 的话，就可以改变行内元素的宽高，这样的话，就不用设置浮动了

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/a4de18cac87cdcf1b9f640d24f654262_MD5.png]]

# 2 布局原理

用来为盒状模型提供最大的灵活性，任何一个容器都可以指定为 flex 布局

当我们给父元素设置为 flex 布局的以后，子元素的 float、clear 和 vertical-align 属性都将失效

也就是说，采用 flex 布局的元素，称为 flex 容器(flex container)，它是所有子元素自动成为容器成员，称为 flex 项目(flex item)

在上面的 flex 布局体验里面 div 就是 flex 父容器，span 就是子容器 flex 项目，并且子容器可以横向和纵向的排列

flex 总结：通过给父盒子添加 flex 属性，来控制子盒子的位置和排列方式

# 3 父项属性

## 3.1 flex-direction

flex-direction 是设置主轴的方向

一般在 flex 布局里面是分为主轴和侧轴两个方向，也就是 x 轴和 y 轴

![[00 assets/12a7d3d140dcf5a22806592545c3221b_MD5.png]]

**属性值**

注意：主轴和侧轴是会变化的，就看 flex-direction 设置谁为主轴，剩下的就是侧轴，而我们的子元素是跟着主轴来排列的

**1.**row 默认值从左到右

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/754d20173fff2eec8dad959c37747d6b_MD5.png]]

2.row-reverse 是从右向左排列

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row-reverse;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/8191a821d8771d0846d312ca970cfb1b_MD5.png]]

3.column 设置主轴是 y 轴

发现下面的一个特性没，是不是即便子元素超过了父元素，也不会超过父元素

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: column;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/ad77bee4ec4d67170b2e2d7b1677c6de_MD5.png]]

4.column-reverse 就是从下到上排列

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: column-reverse;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/d80216b9cab43b3912019406b0fbc938_MD5.png]]

## 3.2 justify-content

设置主轴上子元素的排列方式，重点是主轴

**属性值**

1.flex-start 默认值 从头部开始，如国主轴是 x 轴，则从左到右

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			justify-content: flex-start;

		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>
</html>
```

![[00 assets/cfe95902888f677d9f60cfaaf37d6408_MD5.png]]

2.flex-end 从尾部开始排列

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			justify-content: flex-end;

		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>
</html>
```

![[00 assets/064f4da1afaf9a07e9bd8c817ff2f9ff_MD5.png]]

3.center 在主轴居中对齐（如果主轴是 x 轴则水平居中）

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			justify-content: center;

		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>
</html>
```

![[00 assets/0bd98de53b42e93cb8f0d3fae3a197c3_MD5.png]]

4.space-around 平分剩余空间

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			justify-content: space-around;

		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>
</html>
```

![[00 assets/5cfdeafc09882b9ee72b2a665a2e9ccf_MD5.png]]

5.space-between 先两边贴边 再平分剩余空间

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 80%;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			justify-content: space-between;

		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>
</html>
```

![[00 assets/92d9978251ac3c71f32d4bcb58c7f776_MD5.png]]

## 3.3 flex-wrap

设置子元素是否换行

默认情况，项目都是排在一条线（又称“轴线”）上，flex-wrap 属性定义，flex 布局默认是不换行的

我们可以考虑一个场景，就是子元素是宽度超过了父元素的宽度，在 flex 里面就是改变子元素的宽度来塞在父元素里面

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			justify-content: space-between;

		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>
</html>
```

![[00 assets/d9909afc90c66d9e085117ba0524d2f7_MD5.png]]

但是我们想不改变子元素的大小，让子元素自己下去

**属性值**

1.nowrap 默认值，不换行

2.wrap 换行

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			flex-wrap: wrap;


		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
	</div>
</body>

</html>
```

![[00 assets/1bba1aaf45a829d945dd1ac739be63f0_MD5.png]]

## 3.4 align-items

设置侧轴上的子元素排列方式，但是要注意的是只能单排使用，假如是多排的话，就不能正常使用了

1.flex-start 默认值 从上到下

2.flex-end 从下到上

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 400px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			align-items: flex-end;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/e4867386ace865d65d62c2f1eb3805ab_MD5.png]]

3.center 垂直居中

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 400px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			align-items: center;
		}
		.main span{
			width: 150px;
			height: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/b2e9138b3dea8fe6a1135549bbb60c65_MD5.png]]

4.stretch 拉伸

只要不给子元素高度就可以了

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 400px;

			background-color: pink;

			display: flex;
			flex-direction: row;
			align-items: stretch;
		}
		.main span{
			width: 150px;

			background-color: cadetblue;
			margin-right: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/0edc5453bb07cc8b61aa5fd3baf3cb90_MD5.png]]

注意：align-items 这里的理解，是把每一行当作单行来处理

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-items: center;
		}
		.main span{
			width: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 0px 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
	</div>
</body>
</html>
```

![[00 assets/c23970f7465b6e22ffe082e9b15d1b3a_MD5.png]]

## 3.5 align-content

设置侧轴上的子元素排列方式，但是它和上面的 align-items 是不一样的，它是使用于多行的情况，在单行的情况下是没有效果的，所以需要设置可以换行

**属性值**

1.flex-start 默认值在侧轴的头部开始排列

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-content: flex-start;
		}
		.main span{
			width: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
		<span>9</span>
		<span>10</span>
		<span>11</span>
	</div>
</body>
</html>
```

![[00 assets/0588bfc460ef517eddbb294052ae105b_MD5.png]]

2.flex-end 默认值的尾部开始排列

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-content: flex-end;
		}
		.main span{
			width: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
		<span>9</span>
		<span>10</span>
		<span>11</span>
	</div>
</body>
</html>
```

![[00 assets/6d4f9c2e678ec4d18ce944c804431c51_MD5.png]]

3.center 在侧轴中间显示

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-content: center;
		}
		.main span{
			width: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
		<span>9</span>
		<span>10</span>
		<span>11</span>
	</div>
</body>
</html>
```

![[00 assets/8fb17d7e41444d745a996d0b41757b86_MD5.png]]

4.space-around 子项在侧轴平分剩余空间

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-content: space-around;
		}
		.main span{
			width: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
		<span>9</span>
		<span>10</span>
		<span>11</span>
	</div>
</body>
</html>
```

![[00 assets/aa80dfa32cbcc4b7f8b521ec82fc759d_MD5.png]]

5.space-between 子项侧轴先分布在两头，再平分剩余空间

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-content: space-between;
		}
		.main span{
			width: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
		<span>9</span>
		<span>10</span>
		<span>11</span>
	</div>
</body>
</html>
```

![[00 assets/7659316de50af7ad1a53b6364f8a078a_MD5.png]]

6.stretch 设置子项元素高度平分父元素高度

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-content: stretch;
		}
		.main span{
			width: 100px;


			background-color: cadetblue;
			margin: 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
		<span>9</span>
		<span>10</span>
		<span>11</span>
	</div>
</body>
</html>
```

![[00 assets/e7d5bc046fbcab8ffc139390d7f7478e_MD5.png]]

## 3.6 flex-flow

是 flex-direction 和 flex-wrap 属性的复合属性

```html
flex-direction: row;
flex-wrap: wrap;
//下面的和上面的是一样的，就是一个简写的方式
flex-flow: row wrap;
```

## 3.7 总结

![[00 assets/3c532b8c1b2824748f84b49464e9546d_MD5.png]]

假如父元素的宽度正好是 2 个还有多的，3 个太少了，设置了 wrap 的话，就会换行进行

```HTML
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.search{
			display: flex;
			flex-flow: row nowrap;

			width: 500px;
			height: 200px;
			background-color: chocolate;

		}
		.search div:nth-child(1){
			width: 200px;
			height: 200px;
			background-color: blueviolet;
		}
		.search div:nth-child(2){
			width: 200px;
			height: 200px;
			background-color: darksalmon;
		}
		.search div:nth-child(3){
			width: 200px;
			height: 200px;
			background-color: cadetblue;
		}
	</style>
</head>
<body>
	<div class="search">
		<div></div>
		<div></div>
		<div></div>
	</div>
</body>
</html>
```

# 4 子项属性

## 4.1 flex-basis

设置弹性盒伸缩基准值，注意你设置了 flex-basis 的话，width 就失效了

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 500px;
			height: 500px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-items: center;
		}
		.main span{
			flex-basis: 100px;
			height: 100px;

			background-color: cadetblue;
			margin: 0px 10px;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
		<span>4</span>
		<span>5</span>
		<span>6</span>
		<span>7</span>
		<span>8</span>
	</div>
</body>
</html>
```

## 4.2 flex-grow

设置伸缩值

400-50-100-50=200

200/3 = 66.6

第一个块:66.6+50=116.6

第二个块:66.6+50=166.6

第三个块:66.6+50=116.6

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-items: center;
		}
		.main span:nth-child(1){
			flex-basis: 50px;
			flex-grow: 1;
			height: 100px;

			background-color: red;
		}
		.main span:nth-child(2){
			flex-basis: 100px;
			flex-grow: 1;
			height: 100px;

			background-color: blue;
		}
		.main span:nth-child(3){
			flex-basis: 50px;
			flex-grow: 1;
			height: 100px;

			background-color: yellow;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
		<span>3</span>
	</div>
</body>
</html>
```

![[00 assets/de09c4eca3a04d9efea318490f3c5494_MD5.png]]

## 4.3 flex-shrink

400-300-200=100

100/2= 50

第一个块:300-50=250

第二个块:200-50=150

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.main{
			width: 400px;
			height: 300px;

			background-color: pink;

			display: flex;
			flex-wrap: wrap;
			align-items: center;
		}
		.main span:nth-child(1){
			flex-basis: 300px;
			flex-grow: 1;
			flex-shrink: 1;
			height: 100px;

			background-color: red;
		}
		.main span:nth-child(2){
			flex-basis: 200px;
			flex-grow: 1;
			flex-shrink: 1;
			height: 100px;

			background-color: blue;
		}
	</style>
</head>
<body>
	<div class="main">
		<span>1</span>
		<span>2</span>
	</div>
</body>
</html>
```

## 4.4 flex

flex 属性定义子项项目分配剩余空间，用 flex 来表示占多少份

我们来看下面的案例，是不是左右两边是固定的，但是中间是剩下的，你写一个 flex：1 的话就是把这个剩余的都给第二个 div

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.search{
			display: flex;
			width: 80%;
			height: 200px;
			background-color: chocolate;

			margin: 0 auto;
		}
		.search div:nth-child(1){
			width: 200px;
			height: 200px;
			background-color: blueviolet;
		}
		.search div:nth-child(2){
			flex: 1;
			background-color: darksalmon;
		}
		.search div:nth-child(3){
			width: 200px;
			height: 200px;
			background-color: cadetblue;
		}
	</style>
</head>
<body>
	<div class="search">
		<div></div>
		<div></div>
		<div></div>
	</div>
</body>
</html>
```

![[00 assets/65fdfc030d2f3fdbe8c7be28dc0da630_MD5.png]]

简写的话就是 flex : flex-grow flex-shrink flex-basis

## 4.5 flex 特殊写法

| 属性      | 作用           |
| --------- | -------------- |
| flex:auto | flex:1 1 auto  |
| flex:none | flex: 0 0 auto |
| flex:0%   | flex:1 1 0%    |
| flex:100% | flex:1 1 100%  |
| flex:1    | flex:1 1 0%    |

## 4.6 align-self

align-self 属性允许单个项目与其他项目采取不一样的对齐方式

## 4.7 order

order 设置排列的顺序，-1 是在前面，1 是后面
