**视频讲解**[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1XJ411X7Ud?spm_id_from=333.788.b_636f6d6d656e74.4)

**视频讲解**Codewhy - 前端系统课 - HTML

# 1. 基础入门

## 1.1 基本介绍

服务器开发语言：**java，php，c#，python，node.js**

客户端形式：**文字客户端，图形化界面（C/S 架构 客户端/服务器），网页（B/S 架构 浏览器/服务器）**

其中对于网页来说，下面的 3 个语言很重要，它们分别代表的不同的作用：**结构（HTML）、表现（CSS）、行为（JavaScript）**

> 浏览器内核

![image-20220915211450253](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119318.png)

> HTML 介绍

`HTML`是一个`标记语言`，不属于`编程语言`，因为它能在计算机上面跑，所以也可以叫做`计算机语言`

当然 HTML 文件的扩展名有`.htm\html`，这是因为历史遗留问题，`Win95\Win98`系统扩展名不允许超过 3 个字符

![image-20220915211730868](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119328.png)

> div/span 历史

![image-20221027170827628](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119332.png)

![image-20221027171452651](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119339.png)

## 1.2 骨架介绍

下面为一个很简单完整的`html`骨架

```html
<!DOCTYPE html> <!-- 文档声明(doctype)用来告诉浏览器当前网页的版本,html就是html5 -->
<html lang="en">
  <head>
    <meta charset="UTF-8" /> <!-- 字符编码，告诉浏览器你是使用的UTF-8 -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <p></p> <!-- 双标签 -->
    <img src="./p1.png"/>  <!-- 单标签，标签页可以包含属性 -->
  </body>
</html>
```

1.`<!DOCTYPE html>` 是文档声明

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119344.png" alt="image-20221027124953228"  />

2.`<html>`是整个`HTML`文档的根元素。其中`<!DOCTYPE html>`就不是元素，它只是一个文档声明

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119350.png" alt="image-20221027125501780"  />

3.`<head>`是网页的头部，`head`中的内容不会再网页直接出现，里面配置一些信息来帮助浏览器或搜索引擎来解析网页

​ 3.1.`<title>` 内容会显示在浏览器的标题栏，搜索引擎会根据`title`中的内容来判断网页的主要内容

​ 3.2.`<meta >` 是用来设置网页的元数据，这里`meta`用来设置网页的字符集。当然也又很多其他配置，如：`浏览器兼容性优化`、`SEO优化`

4.`<body>` 是 html 的子元素，表示网页的主体，网页的所有内容都应该写在 body 里面

`HTML`文档：[HTML 元素参考 - HTML（超文本标记语言） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element)

其中`head`是`html`的子标签，`title`是`head`的子标签，是`html`的后代。这个在`CSS`的选择器里面经常使用。

其中有一个很重要的细节，就是`HTML`不区分大小写。所以在`Vue`中编写`HelloWorld`和`helloworld`是一样的，假如你开启了`eslint`的话就会报错

```html
<html>
    <head>
        <title></title>
    </head>
    <body>
        <p></p> <!-- 双标签 -->
    	<img/>  <!-- 单标签 -->
    </body>
</html>
```

## 1.3 meta 标签

meta 主要设置网页中的一些元数据，元数据用户看不到

charset 是告诉浏览器用什么字符集打开

name 指定数据的名称

content 指定数据的内容

keywards 是表示网页的关键字，比如你设置前端，你去搜索前端的话，就会弹处理来

description 是设置网页的描述的，比如你搜索了一个网站，网站名字下面的显示的文字就是描述

```html
<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="UTF-8">
    <meta name="keywards" content="html,前端,css"> <!--设置关键字-->
    <meta name="description" content="这是一个可爱的语句"><!--设置描述-->
    <meta http-equiv="refresh" content="3;url=http://www.baidu.com">
  	<!--设置跳转的网页,及其设置多少秒之后跳转-->
    <title>Document</title>
</head>
<body>

</body>
</html>
```

## 1.4 HTML 编写思路

1. 先编写`HTML结构`
2. `重置`里面各个元素的样式
3. 对于结构`从内到外`的`编写样式`
4. 去除重复的代码；相同的样式抽到一个`class`中，不同的就设置一个单独的`class`

# 2. 常见元素

## 2.1 块元素

在页面中占一行的元素称为块元素，并且可以改变宽高

### 2.1.1 h1~h6 标签

`h1-h6`标记，`h1`最大，`h6`最小

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>h1标记</h1>
    <h2>h2标记</h2>
    <h3>h3标记</h3>
    <h4>h4标记</h4>
    <h5>h5标记</h5>
    <h6>h6标记</h6>
  </body>
</html>
```

浏览器在解析`h1~h6`标签的时候本质就是加上相应的`CSS`样式

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119099.png" alt="image-20221027131557896" style="zoom:67%;" />

### 2.1.2 p 标签

p 标记表示段落，是一个块元素，就是文字中的一段

```html
<p>
    我是一个可爱的语句
</p>
<p>
    我是一个可爱的语句
</p>
```

![屏幕截图 2021-07-14 162742](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119135.png)

### 2.1.3 div 标签

`div`标记，没有语义，用来表示一个区块，宽是 100%，高是被内容撑开的

### 2.1.4 a 标签

#### 2.1.4.1 常见属性

##### 2.1.4.1.1 href 属性

超链接的作用，通过超链接可以从浏览器向服务器发送请求，一般是请求(request)和响应(response)

a 标记就是定义超链接的，且也是行内式，但是这里面可以嵌套除它外的任何元素，意思就是说虽然它是行内式，但是可以嵌套块元素，它什么都可以嵌套，就是不能嵌套自己

下面是超链接的使用，下面注意的一个问题，就是点击了话就会变成紫色，不点地话，会默认是蓝色

```html
<a href="http://www.baidu.com">超链接</a>
<a href="http://www.baidu.com">超链接</a>
```

![屏幕截图 2021-07-14 215431](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119152.png)

这个是跳到一个文件里面的另一个文件

```html
<a href="code.html">超链接</a>
```

假如你点击下面的

![屏幕截图 2021-07-14 215931](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119172.png)

就是下面的问题

![屏幕截图 2021-07-14 215943](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119189.png)

alt+shift+上键是向上复制，alt+shift+下键是向下复制

当然`a标签`里面也可以和`img标签`进行结合

![image-20221027163523028](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119220.png)

也就是下面的效果，点击整张图片就会实现`a标签`的功能

![image-20221027163553634](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119601.png)

当然`a标签`也可以使用除`.html`文件之外的文件，我们也可以下载文件。或者指向其他协议地址

![image-20221027164045858](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119679.png)

##### 2.1.4.1.2 target 属性

target 属性用来指定超链接打开的位置

可选值

\_self 默认值 在当前页面打开超链接

\_blank 表示用新页面打开

```html
<a href="code.html" target="_blank">超链接</a>
```

#### 2.1.4.2 锚点链接

可以将超链接的值设置为#的话，点击超链接页面不会跳转，而是回到页面的顶部的位置

```html
<a href="#">超链接</a>
```

**id 属性值**，每个标签添加一个 id 属性，id 属性是唯一标识，同一页面不能不能出现重复的 id 属性

```html
<p id="bottom">
    我是一个要跳转的一个属性
</p>
<a href="#bottom">超链接</a>
```

锚点链接可以做类似右边的目录栏，点击之后就会实现左边内容的跳转

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119692.png" alt="image-20221027163338045" style="zoom:67%;" />

**javascript:;属性值**，可以在开发的时候当占位符来使用

```html
<a href="javascript:;">超链接</a>
```

### 2.1.5 iframe

#### 2.1.5.1 基本介绍

可以使用该标签来嵌套其他的网页

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119715.png" alt="image-20221027164458177" style="zoom:67%;" />

但是很多的网页不允许使用该标签的使用

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119736.png" alt="image-20221027164708628" style="zoom:67%;" />

假如你也不允许`ifeame`来访问你的网站，需要在`X-Feame-Options`中设置`同源策略`，这样就访问不到了

![image-20221027164940754](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119857.png)

#### 2.1.5.2 常见属性

##### 2.1.5.2.1 src 属性

src 里面放引入的属性

```html
<iframe src="http://www.baidu.com"></iframe>
```

##### 2.1.5.2.2 frameborder 属性

表示引入网页的边框，一般写上 0，不然上面显示边框不是很好看。其中 1 表示显示边框

```html
<iframe src="http://www.baidu.com" frameborder="0"></iframe>
```

![屏幕截图 2021-07-15 142925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119216.png)

##### 2.1.5.2.3 width/height 属性

设置宽度和高度

#### 2.1.5.3 iframe 与 a

\_self 默认值 在当前页面打开超链接，也就是在`iframe`中打开

\_blank 表示用新页面打开，在当前父窗口开打新页面，也就是浏览器本身打开新网页，开启一个新标签

\_parent：在父窗口中打开 URL，在当前浏览器的当前标签中打开

\_top：在顶层窗口打开 URL，这个是在`iframe`相互嵌套的时候使用，默认就是要对顶层的窗口打开，也就是浏览器

![image-20221027165807013](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119248.png)

### 2.1.6 语义化标签

#### 2.1.6.1 blockquoye 标记

表示长引用的话，就是前面会缩进

```html
<blockquote>这是一个可爱的语句</blockquote>
```

![屏幕截图 2021-07-14 162925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119290.png)

#### 2.1.6.2 header 标记

header 标记表示网页的头部，也可以表示内容区块或一整个页面的标题

#### 4.1.5 main 标记

main 标记表示网页的主体内容，网页只能有一个

#### 4.1.6 footer 标记

footer 标记表示网页的底部

#### 4.1.7 nav 标记

nav 标记表示网页中的导航

#### 4.1.8 aside 标记

aside 标记表示和主体相关的其他内容，一般表示侧边栏

#### 4.1.9 article 标记

article 标记表示一个独立的文章

#### 4.1.10 section 标记

section 标记表示一个独立的区块

#### 4.1.11 hgroup 标记

表示对整个页面的页面中的一个内容区块的标题进行组合

1、如果只有一个标题元素不建议使用 hgroup 元素

2、当出现一个或者一个以上的标题与元素时，推荐使用 hgroup 元素作为标题元素

3、当以恶搞标题包含副标题、section 或者 article 元素时，建议将 hgroup 元素和标题相关元素存放到 header 元素容器中

```html
<hgroup>
    <h1>
        我是一级标题
    </h1>
    <h2>
        我是二级标题
    </h2>
</hgroup>
```

![屏幕截图 2021-07-14 162619](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119363.png)

#### 4.1.13 figure 标记

表示一段的流内容，一般表示文档主体流内容中的独立单元

#### 4.1.14 figcaption 标记

定义 figure 标记的标题，一般只使用一次

#### 4.1.13 语义化标签实例

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<article>
			<header>
				<h2>这是一个标题</h2>
			</header>
			<section>
				<h3>评论A</h3>
				<article>
					可爱
				</article>
				<h3>评论B</h3>
				<article>
					真大
				</article>
			</section>
		</article>
	</body>
</html>
```

![屏幕截图 2021-09-05 083911](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119388.png)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<p>潦草阿松东方红七五阿佛啊哈</p>

		<figure>
			<figcaption>潦草</figcaption>
			<p>记者:人人人</p>
		</figure>
	</body>
</html>

```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<header>
			<hgroup>
				<h1>这是一个1级标题</h1>
				<h2>这是一个2级标题</h2>
			</hgroup>
			<p>内容</p>
		</header>
	</body>
</html>
```

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<hgroup>
			<figcaption>橡树</figcaption>
			<p>橡树相关内容</p>
			<figcaption>华数</figcaption>
			<p>华数相关内容</p>
			<figcaption>杨树</figcaption>
			<p>杨树相关内容</p>
		</hgroup>
	</body>
</html>
```

## 2.2 行内元素

在页面中不独占一行，不能改变宽高

### 2.2.1 span 标签

span 标记，没有语义，用来表示一个区块，和 div 的区别就是这个是行内元素

### 2.1.4 img 标签

`HTML`中`img标签`将一份图像嵌入进去

#### 2.1.4.1 属性值

##### 6.1.1 src 属性

`src`指定的是图片的路径

```html
<img src="./img/1.gif"><!--引入内部文件-->

<img src="https://image.baidu.com/search/1.png"><!--引入外部图片-->
```

对于网页来说，不管是`Windows/Mac/Linux`中都默认是`/`

##### 6.1.2 alt 属性

`alt`表示图片描述

1.当图片没加载出来的时候，会显示你设置的字，现在搜索引擎中，可以作为分析

2.屏幕阅读器会将这些描述读给需要使用阅读器的使用者听，让他们知道图像的含义

##### 6.1.3 不常用属性

更多的`<img>标签`的属性：https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img

###### 6.1.3.1 title 属性

当鼠标悬浮到图片的时候的显示的值

###### 6.1.3.2 width 属性

图片的宽度，注意一般只修改了一个，另一个会等比例而缩放。但是整个属性一般是在`CSS`中进行控制，所以不经常使用，但是在写 demo 的时候为了方便会经常使用

```html
<img src="./img/1.gif" width="200">
```

###### 6.1.3.4 hight 属性

图片的高度，但是在移动端，检查需要对图片进行缩放。但是整个属性一般是在`CSS`中进行控制

```html
<img src="./img/1.gif" hight="200">
```

#### 2.1.4.2 图片格式

1.`jpg格式`：支持颜色丰富，不支持透明效果，不支持动图

2.`gif格式`：支持颜色少，支持简单透明，支持动图

3.`png格式`：支持颜色丰富，支持复杂透明，不支持动图

4.`webp格式`：它是谷歌专门的表示网页的格式，它具备其他图片格式的所有优点，并且文件还特别小，但是兼容性不是很好

5.`base64格式`：将图片使用 base64 进行编码，这样可以直接将图片转换为字符，通过字符的形式来引入图片，一般都是和网页一起加载的图片才会使用 base64，这样可以加快使用的速度

### 2.2.2 不常用标签

#### 4.2.1 em 标记

em 表示语音语义加重，就是斜体

```html
<em>我是一个可爱的语句</em>
```

![屏幕截图 2021-07-14 163041](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119694.png)

#### 4.2.2 strong

strong 表示重要内容，就是加粗

```html
<strong>我是一个可爱的语句</strong>
```

![屏幕截图 2021-07-14 163121](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119716.png)

#### 4.2.3 q 标记

表示短引用，会缩进，并且会加上双引号

```html
<q>我是一个可爱的语句</q>
```

![屏幕截图 2021-07-14 163151](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119746.png)

#### 4.2.5 删除字

删除字

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>
		<del>删除字</del>
	</body>
</html>

```

![屏幕截图 2021-11-07 214408](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119853.png)

#### 4.2.6 插入字

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>
		<ins>插入字</ins>
	</body>
</html>

```

#### 4.2.7 粗体字

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>
		<b>粗体字</b>
	</body>
</html>

```

#### 4.2.8 斜体字

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>
		<i>斜体字</i>
	</body>
</html>

```

#### 4.2.9 sub 和 sup

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>
		<p>这是一个在上面的显示10<sup>2</sup></p>
		<p>这是一个在下面的显示10<sub>2</sub></p>
	</body>
</html>

```

4.3 br 标记

br 标记表示换行

```html
<em>我是一个可爱的语句</em>
<br>
<em>我是一个可爱的语句</em>
```

![屏幕截图 2021-07-14 163624](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119873.png)

假如我们使用`p`标签和`br`标签换行的距离是不一样的

![image-20220710102011501](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119100.png)

#### 4.4 pre 标记

预留标记，就是再标记里面是什么形式，在外面显示的就是什么形式

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>
		<pre>
			这是一个什么东西
				这不是个什么东西
		</pre>
	</body>
</html>

```

![屏幕截图 2021-11-07 175130](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119247.png)

#### 4.4.10 code 标签

用于显示代码

## 2.3 全局属性

文档：[全局属性 - HTML（超文本标记语言） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes)

但是下面的 4 个是常见的全局属性

![image-20221027172452876](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119272.png)

## 2.4 元素类型

![image-20221102193002003](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119301.png)

当然块级元素或者行内级元素在浏览器的本质，就是`display:block;`

![image-20221102193100326](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119362.png)

我们可以修改元素的类型，只需要通过`display`来修改。所以`HTML`中的元素没有本质的区别，只不过浏览器中给各个元素设置了`CSS`的属性

![image-20221102193424463](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119429.png)

# 3. 基础概念

## 3.1 字符实体

![image-20221027172936131](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119583.png)

下面为常见的字符实体作为参考

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119905.png" alt="image-20221027173020357" style="zoom:80%;" />

## 3.2 SEO

![image-20221118161912688](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119926.png)

## 3.3 字符编码

更加详细的笔记可以参考我：`前端相关知识`的笔记里面的内容

![image-20221028221414449](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119974.png)

# 4. 列表

## 4.1 有序列表

![image-20221118162556533](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119011.png)

> 列表嵌套

![image-20221118162815604](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119042.png)

> 样式重置

```css
list-style:none  /* 重置列表的样式 */
```

## 4.2 无序列表

![image-20221118162623786](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119615.png)

## 4.3 定义列表

![image-20221118162931802](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119648.png)

# 6. 表格

## 6.1 基本使用

现在对于`HTML`属性来说，已经不建议使用`table`的属性来设置样式了，而是比较推荐`CSS`处理

![image-20221118171822304](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119679.png)

其中表格的内容是`tr`包裹`td`来处理

![image-20221118172003685](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119706.png)

## 6.2 语义化处理

对于`表格`新增加了下 main 的几个元素，假如我们使用这个方式也会提高`SEO`

![image-20221118172353627](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119736.png)

下面为基本的使用方式

![image-20221118173025980](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119759.png)

## 6.3 单元格合并

![image-20221118173203762](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119337.png)

> colspan

![image-20221118174013761](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119360.png)

> rowspan

![image-20221118174105551](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119381.png)

> 案例

![image-20221118175521217](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119406.png)

## 6.4 间隔变颜色

这个我们一般使用`结构伪类`来处理

![image-20221118175752526](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119449.png)

# 7 表单

## 7.1 input

### 7.1.1 常见属性

`input`存在很多的属性，下面为经常使用的属性。其中对于`input`是否为行内可替换元素，官方没有明确的规定，而是根据不同的场景来展示不同的属性

![image-20221118182401827](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119494.png)

`input`也存在一些常见的布尔属性

![image-20221118182634588](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119117.png)

### 7.1.2 type

假如需要使用的话可以参考`MDN文档`：[：输入（表单输入）元素 - HTML（超文本标记语言） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/Input)

> type 属性

1、`text`：表示输入的是文本类型

2、`password`：表示输入的是密码

3、`checkbox`：设置多选框

4、`radio`：设置单选框

5、`button`：设置按钮，这个可以使用`<button>`标签代替

6、`radio`：设置单选框

7、`button`：设置为按钮

8、`submit`：设置提交按钮，表面和`button`一样，但是它的默认行为不一样，它可以将数据提交给服务器

> 不常见类型

1、`date`：表示输入的是日期，但是各个浏览器的值不一样，所以不是很推荐使用

2、`url`：专门用来输入网址

3、`tel`：专门用来输入电话号码

4、` search`：专门用来输入搜索关键字的文本框

5、`range`：设置一个滑动的条

6、`number`：设置只能输入数字

7、`reset`：设置重置按钮

其中对于`form`来说，`name`不仅仅是唯一标识符，用途可以用于区分`radio`和`checkbox`，而且是作为`key`存在。`value`就是作为提交的时候`value`的存在

![image-20221122173157386](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119147.png)

### 7.1.3 label

**MDN 文档参考**：[ - HTML（超文本标记语言） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/label)

我们可以使用`label`属性来关联`input`的操作，假如想要知道详细的使用方式可以参考`MDN文档`中的解释

![动画85](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119179.gif)

假如你将`input`包在`label`中就不用编写`for`也可以实现相应的效果

![image-20221122171326941](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119208.png)

## 7.2 select

下面就是`select`的基本使用

![image-20221122174216556](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119230.png)

假如我们想要给`select`分组的话，就可以使用`optgroup`来处理

![image-20221122174236411](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119252.png)

## 7.3 textarea

下面为`textarea`基本的使用

![image-20221122173844535](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119872.png)

## 11.1 表单设置

设置一个表单时是使用 from 属性，可选值有 action，表示表单要提交的服务器的地址

### 11.1.1 input

#### 11.1.1.1 autocomplete

启用自动完成功能的表单，on 就是打开，off 是关闭

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title> 
	</head>
	<body>

		<form action="demo-form.php" autocomplete="on">
			First name:<input type="text" name="fname"><br>
			Last name: <input type="text" name="lname"><br>
			E-mail: <input type="email" name="email" autocomplete="off"><br>
			<input type="submit">
		</form>
	</body>
</html>
```

![屏幕截图 2021-10-08 082731](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119900.png)

#### 11.1.1.2 maxlength

属性规定 < input > 元素中允许的最大字符数

#### 11.1.1.3 size

size 属性规定以字符数计的 < input > 元素的可见宽度

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>

<body>

<form action="demo_form.php">
  Email: <input type="text" name="email" size="35"><br>
  PIN: <input type="text" name="pin" maxlength="4" size="4"><br>
  <input type="submit" value="提交">
</form>
</body>
</html>
```

![屏幕截图 2021-10-08 091947](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119929.png)

#### 11.1.1.5 pattern

设置正则表达式的，基本不怎么用

#### 11.1.1.6 placeholder

设置提示框里面的提示内容

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
	<body>
		<input type="text" placeholder="这里输入文字"/>
	</body>
</html>
```

![屏幕截图 2021-10-08 112033](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119950.png)

#### 11.1.1.7 required

设置用户必填写表单

# 8. Emmet

> ！

直接生成`HTML5`的代码片段

> ">"父子元素 "+"兄弟元素

![image-20221122174755755](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119973.png)

> "\*"多个 "^"上一级

![image-20221122174933505](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119004.png)

> () 分组

![image-20221122175052103](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119494.png)

> 属性(id 属性、class 属性、普通属性){}(内容)

![image-20221122175236578](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119511.png)

> $ 数字

![image-20221122175430917](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119529.png)

```bash
ul>li{电脑列表$}*100 	// 生成100个ul>li标签，里面的显示电脑列表1、电脑列表2....
```

> 隐式标签

![image-20221122175402137](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119553.png)

> CSS

![image-20221122175546930](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032119577.png)

# 5. 音视频播放

## 9.1 audio 标签

引入音频文件

### 9.1.1 src 属性

```html
<audio src="./soc/mm.mp3"></audio>
```

这样是不行的，用户不能去控制

### 9.1.2 controls 属性

假如你想用户去控制的话

```html
<audio src="./soc/mm.mp3" controls></audio>
```

### 9.1.3 autoplay 属性

表示进入浏览器就自动播放音乐

```html
<audio src="./soc/mm.mp3" controls autoplay></audio>
```

假如你要循环播放的话，就加上 loop

```html
<audio src="./soc/mm.mp3" controls autoplay loop></audio>
```

### 9.1.4 source 属性

这个为了兼容性的问题

```html
<audio>
	对不起你的浏览器不支持，请升级浏览器
    <source src="./soc/mm.mp3">
    <source src="./soc/mm.ogg">//这个是为了不同版本的浏览器，支持不一样的文件类型
</audio>
```

或者下面的办法，下面这个是直接兼容所有的版本的浏览器

```html
<audio>
    <source src="./soc/mm.mp3">
    <source src="./soc/mm.ogg">//这个是为了不同版本的浏览器，支持不一样的文件类型
    <embed src="./soc/mm.ogg" type="audio/mp3" width="300" hight="300">
</audio>
```

## 9.2 video 标签

引入视频文件，基本和 audio 一样

```html
<video>
    <source src="./soc/mm.mp4">
    <source src="./soc/mm.webm">//这个是为了不同版本的浏览器，支持不一样的文件类型
    <embed src="./soc/mm.webm" type="video/mp3">//为了兼容IE8以后的浏览器
</video>
```

preload，这个是当视频没有及时播放的时候，可以显示一个东西

## 9.3 视频编解码器

视频编解码器定义了多媒体数据流编码和解码的算法。其中编码器主要是对数据流进行编码操作，用于存储和传输。

### 9.3.1 H.264

H.264 是国际标准化组织（ISO）和国际电信联盟（ITU）共同提出的继 MPEG4 之后的新一代数字视频压缩格式

### 9.3.2 Theora

Theora 是免费开放的视频压缩编码技术，可以支持从 VP3 HD 高清到 MPEG-4/DiVX 视频格式

### 9.3.3 VP8

VP8 是第八代的 On2 视频，能以更少的数据提供更高质量的视频，而且只需较小的处理能力即可播放视频

## 9.4 音频编解码器

音频编解码器定义了音频数据流编码和解码的算法。与视频编解码器的工作原理一样，音频编码器主要用于对数据流进行编码操作，解码器主要用于对音频文件进行解码

### 9.4.1 ACC

ACC 是高级音频编码（英文：Advanced Audio Coding）的简称，该音频编码是基于 MPEG-2 的音频编码技术，目的是取代 MP3 格式。

### 9.4.2 MP3

MP3 是“MPEG-1 音频层 3”的简称。它被设计用来大幅度地降低音频数据量。

### 9.4.3 Ogg

Ogg 全称为 Ogg Vorbis，是一种新的音频压缩格式，类似于 MP3 等现有的音乐格式。OGG Vorbis 有一个很出众的特点，就是支持多声道。
