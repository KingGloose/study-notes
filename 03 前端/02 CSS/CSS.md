视频讲解：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1XJ411X7Ud?spm_id_from=333.788.b_636f6d6d656e74.4)

视频讲解：Codewhy - 前端系统课 - CSS

# 1. 基本入门

## 1.1 基本介绍

![[00 assets/d0085915a8f5dd5d0bae2c6fc7d39305_MD5.png]]

## 1.2 历史了解

![[00 assets/e7a4cef9d41d45bd366f6f22a7a74223_MD5.png]]

## 1.3 引入方式

### 1.3.1 内联样式

`内联样式`存在与`HTML`中。使用内联样式只能对一个标签生效，不能多个使用

```html
<p style="color:red; font-size:30px;">我是一个可爱的语句</p>
```

### 1.3.2 内部样式表

一般都是写在`head`的标签里面，使用`style`标签包裹。我们使用选择器来进行选择下面的`HTML`元素，里面编写`CSS`样式

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      /* 编写的CSS样式 */
      .main {
        width: 200px;
        height: 200px;
        background-color: pink;
      }
    </style>
  </head>
  <body>
    <div class="main"></div>
  </body>
</html>
```

### 1.3.3 外部样式表

使用改方式可以将`CSS`抽取到独立的文件，这样不仅方便阅读，而且可以进行样式的复用。使用该方式还可以最大的使用浏览器的缓存机制，加快网站的加载速度

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- 下面为外部引入样式 -->
    <!-- 下面的rel="stylesheet"表示引入外部样式 -->
    <link rel="stylesheet" href="./1.css" />
  </head>
  <body></body>
</html>
```

不仅仅只是上面的样式的引入，但是引入的样式太多的话就会导致文件的逻辑很零落。所以就会创建一个`indec.css`作为入口文件，来专门引入外部的`css`。可以使用下面的`@import url()`来引入即可

![[00 assets/d6d46872f022c7e6ebc0e95949177517_MD5.png]]

> link 标签

对于`link`标签，不仅仅可以引入`样式表`，还可以引入`图标`，以及其他很多的作用。具体可以参考**MDN 官方文档**：[：外部资源链接元素 - HTML（超文本标记语言） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/link)

![[00 assets/21266eef397b2a344abc22dd1252035c_MD5.jpeg]]

我们可能看一些网站可能已经优先使用了`dns-prefetch`。这个的作用主要是提前解析域名，因为一个网站可能后续存在多个域名的解析，使用这个属性可以在请求域名的时候，顺便把该网站的其他域名都解析出来，用户的阅览的时候就不需要等待`DNS`解析了

![[00 assets/b1a57c9f819b5ac9fe756b738e85b192_MD5.png]]

## 1.4 基本概念

### 1.4.1 注释

```css
/* 我是css的注释 */
```

### 1.4.2 长度

`px`：表示一个像素，但是因为存在视口的概念，所以每个电脑的像素都表示的不一样

`em`：相对于父元素字体的大小改变的，比如：字体大小是 20px 的话，那么 1em 的值就是 20px

`rem`：相对于根元素(html)的字体大小改变的，换算的比例和 em 是类似的

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
    <style>
      html {
        font-size: 20px;
      }
      p {
        font-size: 10rem;
      }
    </style>
  </head>
  <body>
    <p>我是一个可爱的语句</p>
  </body>
</html>
```

### 1.4.3 颜色

`RGB`：每一种颜色范围在(0-255 或者 0-100%之间)，其基本的语法是`rgb(n,n,n);`

我们还可以让`rgb`使用十六进制来表示，基本语法是`rgb:#ff00ff`。假如是两两相同的话，可以简写，比如`#aabbcc`的话，可以简写为`#abc`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
    <style>
      p {
        color: rgb(255, 255, 255); // 或者直接使用white、red....
      }
    </style>
  </head>
  <body>
    <p>我是一个可爱的语句</p>
  </body>
</html>
```

`rgba`：就是在`rgb`的基础上加上了透明，基本语法是`rgba(255,255,255,.5)`，最后一个参数表示透明的值，0 是完全透明，1 是完全不透明

`HSL` H:色相(0-360) S:饱和度(0%-100%) L:亮度(0%-100%)，一般格式是:hsl(0,100%,100%)

## 1.5 常见的 CSS 属性

![[00 assets/9f05bebe1ac212d1c2823a08c4048bad_MD5.png]]

![[00 assets/36e5aa1d836cd7221653a4a75ecb2ed8_MD5.png]]

其中`Color`是设置前景色，而非文本颜色，假如我们给文本添加`text-decoration`的时候也会给它添加颜色

![[00 assets/549d89cbcae99fc6545fb2a1c1b28ad4_MD5.png]]

# 2. 文本

[[文字]]

# 3. 字体

[[字体]]

# 4. 选择器

[[选择器]]

# 5. 继承

[[继承]]

# 6. 盒子

[[盒子]]

# 7. 背景

[[背景]]

# 8. 定位

[[定位]]

# 9. 浮动

[[浮动]]

# 10. 动画

[[动画]]

# 11 flex

[[flex布局]]

# 12 grid

[[grid布局]]

# 13 媒体查询

[[媒体查询]]


