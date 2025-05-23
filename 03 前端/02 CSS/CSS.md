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

## 6.1 常用属性

### 6.1.1 display

当然`display`包含`block、inline-block、inline、none`属性值

![[00 assets/fd9e550b12beeee10df0331bd947074d_MD5.jpeg]]

> 编写 HTML 原则

![[00 assets/0d5f46284226b9249bb9419d2465d0f1_MD5.png]]

假如我们将`div`写在`p`中就会导致整个`HTML`结构混乱，所以不是很建议这样书写

![[00 assets/5b0d2173f921d5336294d22a72c0af41_MD5.png]]

### 6.1.2 box-sizing

`box-sizing`设置如何计算一个盒子的宽度和高度。

1.默认值是`content-box`。**将`padding、border`布置到`width、height`外边**

比如下图中的`example1`的`div `的`width`为 300px，其计算规则是`内容 = 完整宽度`，但`完整宽度`为 `300px + 20px (左边框和右边框) + 60px (左边距和右边距) `= 380px

2.还有一个计算是`border-box`。**将`padding、border`布置到`width、height 里边**

比如下图中的`example2`的`div`不管如何设置其`完整宽度`都为`300px`，也就是`完整宽度` = `width + padding + border`

![[00 assets/098146fe3a3a62283d9fcd40d227fd0b_MD5.png]]

其中`id值为example1`的计算图

![[00 assets/18fe9b4b729a0586764eb7748b49065c_MD5.png]]

其中`id值为example2`的计算图，可以发现不同的差异

![[00 assets/3469632de47fd8f1ec7040e954db53c3_MD5.jpeg]]

### 6.1.3 border-radius

> 基本使用

`border-radius`用于设置圆角。一般我们都会使用简写形式，这个就是设置四个角

![[00 assets/b7ad8e4edbe79d53fe1eb564dc98ceac_MD5.png]]

当然我们也可以单独设置一个角度的值

![[00 assets/3e7dafc6563d12d0607813df8af63371_MD5.png]]

> 设置圆形

我们也可以使用下面的方式设置圆形

![[00 assets/fca6347e0547a9f24de42cf336dabf0e_MD5.png]]

> 简写

我们使用`border-radius`也可以进行简写处理

1、一个值：四个角都设置值

2、两个值：`左上/右下`、`右上/左下`。也即是一个盒子的对角之间

3、三个值：`左上`、`右上/左下`、`右下`。

4、四个值：`左上`、`右上`、`右下`、`左下`。也就是顺时针的方向

### 6.1.4 box-shadow

因为我们使用`box-shadow`比较少，所以这个属性我们可以使用[Smooth Shadow (brumm.af)](https://shadows.brumm.af/)来调整生成，或者使用`box-shadow生成器`来处理

`box-shadow`是设置元素的阴影效果，阴影不会影响布局。

![[00 assets/6a016d10961aee02d502786229565950_MD5.jpeg]]

1、假如想要设置多个阴影的可以设置`","`来处理：`box-shadow:10px 10px 20px ref,10px 20px 30px pink`

2、假如你没设置阴影的颜色，那么就会自动跟随`color`来设置

假如我们想要盒子的左右 2 边都有阴影的话，可以尝试不给`box-shadow`的`x值`。只设置阴影半径，这样也可以实现效果

![[00 assets/e8d07e1e2ea82d0b2d106600d8cc3a13_MD5.png]]

## 6.2 不常见属性

### 6.2.1 outline

`outline`用来设置元素的轮廓线，用法和`border`一模一样，但是设置了`outline`并不会影响盒子的内容。就比如下图中设置`outline`的话就会覆盖掉原本的文字

![[00 assets/4fc7dea6f8eaa3014b0dd0af64c4a0b2_MD5.png]]

## 6.3 盒子模型

### 6.3.1 content

![[00 assets/512e1a62e7da06e307e7532671c94342_MD5.png]]

> 基本使用

我们设置`width、height`就可以给盒子`content`宽高

![[00 assets/e56dce9530b0eac39667970120a9ea89_MD5.png]]

一开始创建一个盒子的初始值为`auto`，由浏览器决定，而非`100%`。

一开始浏览器给了`width`为`auto`的话，那么对于`块元素`，浏览器就会给它`100%`；`行内元素`就是内容决定；`行内可替换元素`也是元素的内容决定，只不过该元素为`img、input...`。所以对于不同的属性`auto`表示的值都不一样

![[00 assets/4530997b4ce3c7d0cbef6aaf8106efcb_MD5.png]]

> max-width/min-width

这 2 个属性在设置移动端适配的时候经常使用

下图就是设置一个`max-width`，假如超过`400px`的话就不会再增加了

![[00 assets/5e64e84ed5880a85dbed07b606b1dfae_MD5.jpeg]]

下图就是设置了一个`min-width`，假如缩小到`200px`的话就该盒子并不会变化，而且浏览器也会展示滚动条

![[00 assets/ab2b55c986a5b9a8928c3c1737ea7820_MD5.png]]

### 6.3.2 padding

> 基本使用

下面就是`padding`的使用

![[00 assets/b345cb808e4629d8ac6905a970b08517_MD5.png]]

> padding 缩写规律

其中书写的 4 个值就是顺时针旋转，依次表示`上右下左`

![[00 assets/ca7541d290119538871b41249d0ba896_MD5.png]]

### 6.3.3 border

#### 6.3.3.1 基本使用

> 基本使用

![[00 assets/8b865290b15612baf0a690709bf4d9bb_MD5.png]]

![[00 assets/f50177d5aede6e51fb60a321e0afd479_MD5.jpeg]]

`border-style`也包含下面的属性

![[00 assets/a612f2ff34ded52c03f4aa707c7d3817_MD5.jpeg]]

> 简写形式

`border-width`和`padding`中的简写是一样，如：`border-width:10px 20px 30px 40px`

`border-style`，如：`border-style:soild dashed groove ridge`

`boder-color`，如：`border-color:red blue green black`

`border:10px red solid`，表示边框四边`边框为10px，颜色为red，边框为soild`，假如`border-style`不写的话就默认为`none`，所以就不会显示边框

#### 6.3.3.2 绘制图形

##### 6.3.3.2.1 基本介绍

因为`border`的特性，我们为盒子添加的`border`本身是一个梯形来处理的，其中设置的值就是按照下面的方式来显示的

![[00 assets/7930a9f2c657456180a4bd7c95cc0309_MD5.jpeg]]

##### 6.3.3.2.2 三角形

使用下面的方式就可以绘制一个三角形

![[00 assets/7836a13cfe445014ab407b83460a9f22_MD5.jpeg]]

当然我们也可以使用`transform`来旋转，不用调整`border`的方向来处理。假如我们想要绘制更多的图片可以参考下面的网址来处理：[The Shapes of CSS | CSS-Tricks - CSS-Tricks](https://css-tricks.com/the-shapes-of-css/#top-of-site)

![[00 assets/bba4efe13a30c0785a9c3d295374c3ed_MD5.jpeg]]

> 应用场景

下面就是一个应用的场景来处理

![[00 assets/51ca08f719abefc6e8d5203c09ac2087_MD5.png]]

##### 6.3.3.2.3 梯形

![[00 assets/e37468d40d39a142998209f89036f3ae_MD5.png]]

### 6.3.4 margin

#### 6.3.4.1 基本使用

![[00 assets/5d3585bb53fbd944e0f410f1cc98e298_MD5.png]]

其整体的使用方式和`padding、border`也差不多，缩写模式也是一样的

![[00 assets/e580c8e3440d58d77980b8bd79326b48_MD5.png]]

#### 6.3.4.2 使用规范

我们要实现下面的效果，我们有很多的方式来处理

![[00 assets/38ffd27731b4abadaed7d104190a2edb_MD5.png]]

1、将父盒子使用`padding`来扩大，然后让这个盒子设置为`box-sizing:border-box`来将盒子的宽度定为`width`

，这样就可以实现盒子的向右移动

![[00 assets/a87584ed433529f2fb351ff659a5a090_MD5.png]]

2、设置子盒子的`margin`值也可以实现

![[00 assets/f437dbb556df9de2db61a2d6350a9614_MD5.png]]

假如这个时候我们再将子盒子向下移动`100px`的话又该如何处理？

![[00 assets/5079f12ce4445ca5030d5a24c7a51610_MD5.png]]

1、我们对子盒子的`margin`值进行处理

![[00 assets/b3291f540e49a4e4f446a20e8b0ae798_MD5.png]]

2、我们对父盒子设置`padding`进行处理

![[00 assets/4d1de2276c6a70e3ffe39ddc9cc5a2b9_MD5.png]]

我们通过上面的移动案例中`不同的方法`处理可以发现各有优劣，并没有最好的。所以我们这里可以通过语义化的角度来区分，因为`子盒子`作为`父盒子`的内容，所以设置`子盒子`相对于`父盒子`距离最好的方式就是使用`padding`来处理

#### 6.3.4.3 值传递

我们给子盒子的`margin-top`设置值的时候，会让父盒子向下移动

![[00 assets/3d2f98a462307695a97f653d18517a9a_MD5.jpeg]]

我们设置`margin-bottom`也会发生值传递的效果，只不过很难遇到这样的问题

![[00 assets/c2f620d9b483097a829b0ae3ee10f97f_MD5.jpeg]]

我们假如想要避免这个问题的话，可以使用下面的方法来解决

![[00 assets/c83f59cc22db8a26a0625616056bf67e_MD5.jpeg]]

1、但是在实际应用中可以利用`值传递`的特性来实现特定的功能，比如下面的案例中，子元素设置`margin-left:-90px`的话就会拖着父元素一起向左移动，这在面对一些组件库来说是比较实用的

![[00 assets/7f7a03bdd2d0e734371c6bc4926d83f7_MD5.jpeg]]

其大致实现原理和下面差不多

![[00 assets/c73a7ff67d8615b7eb5e11c25763b5ee_MD5.jpeg]]

#### 6.3.4.4 值折叠

![[00 assets/801ed0fe857d76ed1853874ac0ec7aa9_MD5.png]]

1、`margin`的`margin-top`和`margin-bottom`的值会重合，相邻的盒子之间设置相同的`margin`的一方会失效

![[00 assets/7a2106f13cf6acfae34890588c454b9c_MD5.png]]

当我们将一方的`margin值`调整的比另一方大，那么就会采用较大的一边

![[00 assets/05eeddd7967af5f570585e8259457223_MD5.png]]

假如我们将盒子设置为`inline-block`的话，上下之间的外边距就不会重叠

![[00 assets/a5521d69febd4539500c7c2cbce3e8c7_MD5.png]]

2、因为左右相邻的`inline-block`的盒子之间会有间距，这里消除间距的一个方式就是使用`font-size:0px`来处理也可以

![[00 assets/ceaf93ad7684f8f4d7e59002a36ce2f9_MD5.png]]

#### 6.3.4.5 盒子居中

> 1、text-align

`text-align`是**父盒子给子盒子**设置`行内级元素`居中的，只要下面的盒子为`inline-block/inline`就可以实现子盒子的居中显示

![[00 assets/4d84e92dc016b8cb6d4477b7f20229a6_MD5.png]]

> 2、margin

我们设置`margin:0 auto`的话有可以设置盒子居中显示。但是按照上面的`使用规范`来说，这个方案不是很好，因为这个是父盒子的内容，所以按照道理来说应该是`padding`来处理。这是因为一开始`W3C`制定规范的时候存在时代的局限性，所以会出现这种问题

![[00 assets/4e33c6ba7d4ca57ff79ac17337886f8f_MD5.jpeg]]

## 6.4 块/行元素

### 6.4.1 对比

块级元素和行内元素表现出来的区别不仅仅为是否独占一行，还有一个最重要的区别就是能不能设置宽高。

**其中块级元素就可以设置宽高，但是行内元素不能设置宽高，行内元素的宽高由内容决定**。但是这个并不是很准确，而是**行内非替换元素(span/a)**不可以设置宽高，而**行内可替换元素**可以设置宽高

![[00 assets/0f3e8b1656eaec5cbcab5c9edef0ba93_MD5.png]]

但是这里就存在一个疑点，为什么`img、input、button...`作为行内元素就可以设置宽高？

这个标签不能理解为行内元素，这个标签也不能理解为`行内块元素`，即便它的特性和`行内块元素`差不多。但是官方的解释为`行内可替换元素`，所以可以设置宽高

![[00 assets/59692c057895a07165da3a1a5ebdafdd_MD5.png]]

### 6.4.2 特殊性

对于`行内非替换元素`来说有很多的特殊性

![[00 assets/4cb45965df3290c4c6b4c9683f9311b6_MD5.png]]

## 6.5 水平距离

对于**水平方向的距离**有很多值`margin`、`padding`、`border`、`width`......。水平样式布局满足下面的公式：

```bash
margin-left + border-left + padding-left
+ width +
padding-right + border-right + margin-right = AllWidth
```

> 1.基本推算

按照公式来推算：`0+0+0+200+0+0+0=400`，是不是最后不满足。所以浏览器会自动调整最后一个`marign-right`的值，自动加上`200`

![[00 assets/7005736c653d202260e9a76fa94d19b1_MD5.png]]

> 2.width 设置 auto

当然还有`auto`值，可以设置 auto 值的有`width、marign-left、marign-right`

按照公式来推算：`0+0+0+auto+0+0+0 = 600`，所以`auto`的值是`600`

![[00 assets/23650b04e7a7ab85a1f995aee881023f_MD5.png]]

> 3.margin 设置 auto

按照公式来推算：`auto+0+0+200+0+0+0 = 600`，那么`margin-left`的值就是`400`。假如是设置的`margin-right`的值的话就是同理

![[00 assets/6fc74e21313a8747076e443a15fd7732_MD5.png]]

> 4.width 和 margin 设置 auto

按照公式来推算：`auto+0+0+auto+0+0+200 = 600`，默认将`width`赋值填满，也就是先`width`再`margin`的原则

![[00 assets/3045877875b0c20a72954c0ea7fb6c25_MD5.png]]

> 5.marin-left 和 margin-right 设置 auto

按照公式来推算：`auto+0+0+200+0+0+auto=600`，那么就会自动平分

![[00 assets/1c9b380b2b8b5b2be03f9212f6102a05_MD5.jpeg]]

> 6.width 超过 AllWidth 的值

按照公式来推算：`200+0+1000+0+auto=600`，那么`margin-right`就是`-400px`，也就是下面的形式

![[00 assets/60a19cfb72800eaf95315bc1a5b11e13_MD5.png]]

# 7. 背景

## 7.1 常见属性

### 7.1.1 background-image

![[00 assets/d3abd556e5ab8c1ccfca8d04fd349c18_MD5.png]]

`background-image`是设置背景图片的。

![[00 assets/5a4ca49225335f89aac46b198dbfe839_MD5.png]]

下面是截取自`MDN`中的，我们可以设置多张图片。其中层级就是文件的顺序

![[00 assets/38ba900cae0a138e9c120b8fc45e0538_MD5.png]]

> background-image 和 img 对比

![[00 assets/6079db1e72b35111cd58cd1baa91fbae_MD5.png]]

### 7.1.2 background-repeat

`background-repeat`是设置背景平铺

![[00 assets/bfa595f38e847ec8867e15e0e8d69988_MD5.png]]

### 7.1.3 background-size

![[00 assets/1830f992de5af69ca894e73f406751cc_MD5.png]]

`background-size`是设置背景图片的大小。

![[00 assets/2dcc4133f22518ac5ea7076b313006af_MD5.png]]

### 7.1.4 background-position

`background-position`是设置背景图片的方位。

1、可选值有`top、left、right、bottom、center`，其使用的方式就是

```bash
background-position:left top;	// 表示左上
```

假如我们只设置一个值的话会默认补一个 center

```bash
background-position:left;  --> background-postion:left center // 表示左中
```

2、假如说你设置的是数字的话，那么就是第一个参数是 x 轴，第二个参数是 y 轴

![[00 assets/085462827deb45c653e49ffb2f74c2e0_MD5.jpeg]]

其中`background-position`有一个应用就是设置图片一直居中显示

![[00 assets/37ab360104e70e86b0a338551d4e14cf_MD5.png]]

### 7.1.5 background 缩写属性

我们可以使用`background`属性来简写一系列的背景属性

![[00 assets/2e4b6af621a89782632d9ed03c7b7606_MD5.png]]

## 7.2 不常见属性

### 7.2.1 background-attachment

![[00 assets/4139be6ab48eeaad5c8054b599d36e63_MD5.png]]

具体的效果可以参考`MDN文档`中给的实例：[background-attachment - CSS（层叠样式表） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-attachment)

# 8. 定位

## 8.1 基本介绍

> 标准文档流

![[00 assets/a6f48fcca5eba8663ec81faf7fcfa9e2_MD5.png]]

> 定位介绍

你为这个元素添加上`position`的话就会脱离标准流，但是`relative`不会脱离标准流

![[00 assets/c1242657071c1c0007c26869f001bfb6_MD5.jpeg]]

![[00 assets/82c4bec202a76f46fb5d5ac56210154a_MD5.png]]

## 8.3 relative

### 8.3.1 基本使用

`relative`只是按照自己原本的位置来定位的，原本的位置依旧会被占据，如：下面的`left`设置为`200px`，也就是向右移动`200px`。也只是按照自己原本在`标准流`的位置来处理

![[00 assets/46a87f14f11c1a137bed9e8acc2c5cb6_MD5.png]]

### 8.3.2 图片居中处理

这个样式在`background-position`可以直接设置为`center`来处理，假如我们不使用`background`的话，也可以使用`img`标签中使用`relative`处理

![[00 assets/4a1a619a588c1e45a8d558b37bbf1076_MD5.png]]

![[00 assets/05dfb09d3e9d52c6d0c7e9141d45460d_MD5.png]]

## 8.4 absolute

### 8.4.1 基本使用

`absolute`是相对于最近的包含块中`开启定位`的元素的位置，原本的位置会被其他元素填充，如：下面的`.one`没开启`relative`的话就会相对`视口`来定位

对于布局来说一般子元素开启了`绝对定位`的话，父元素都要设置`相对定位`

![[00 assets/5f43297b307eefbf5c267cb2d039d448_MD5.jpeg]]

### 8.4.2 定位特点

下面的特点适用于`absolute`和`fixed`

1、元素可以随意设置宽高，即便是`行内元素`

![[00 assets/28476fa2d06c9827e3c9ee52212e0ff0_MD5.jpeg]]

2、宽度默认由内容决定，并且不再给父元素汇报宽高

![[00 assets/4b3bb67d7f2f6836c0aa0ba43454d0d8_MD5.png]]

3、不再严格按照从上到下、从左到右排布。不再严格区分块级（block）、行内级（inline）,行内块级（inline-block）的很多特性都会消失

4、定位元素内部依旧是遵循标准流

![[00 assets/185a7b88b6613e07e467f15fb0043198_MD5.png]]

5、对于定位元素相对于`父元素`的定位遵循下面的原则

**水平距离**：父元素 = 子盒子宽度 + left + right + margin-left + margin-right

**垂直距离**：父元素 = 子盒子高度 + top + bottom + margin-top + margin-bottom

假如想要水平/垂直居中可以使用下面的方式，将`left，right，top，bottom`设置为`0`，让浏览器自己计算`margin`的值，其具体的计算方式可以参考`6.5 水平距离`

当我们把`margin-left`、`margin-right`设置为`0`，而`left`、`right`设置为`auto`的话并不会居中，因为`auto`表示交给浏览器来处理，但是浏览器并没有处理，所以并不会居中

![[00 assets/9055ace2ab7b9348752248e5b6ced6b6_MD5.png]]

### 8.4.3 网易案例

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      /* 公共CSS */
      .sprite_01 {
        background: url("./img/music_sprite_01.png") no-repeat;
        display: inline-block;
      }
      .sprite_02 {
        background: url("./img/music_sprite_02.png") no-repeat;
        display: inline-block;
      }

      /* 样式CSS */
      .musicStyle {
        width: 140px;
      }

      .musicStyle .box {
        position: relative;
      }
      .musicStyle .box img {
        /* 消除图片下面的线 */
        vertical-align: top;
      }
      .musicStyle .box .mask {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;

        background-position: 0 0;
        width: 140px;
        height: 141px;
      }
      .musicStyle .box .info {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;

        background-position: 0 -537px;
        width: 130px;
        height: 27px;

        padding-left: 10px;
        line-height: 27px;

        font-size: 12px;
        color: #ccc;
      }
      .musicStyle .box .info .icon-left {
        background-position: 0 -24px;
        width: 14px;
        height: 11px;
      }
      .musicStyle .box .info .icon-right {
        background-position: 0 0px;
        width: 16px;
        height: 17px;

        position: absolute;
        right: 10px;
        top: 0;
        bottom: 0;
        margin: auto 0;
      }

      .musicStyle .text {
        display: block;
        margin-top: 8px;
        font-size: 14px;
      }
    </style>
  </head>
  <body>
    <div class="musicStyle">
      <!-- 顶部图片 -->
      <div class="box">
        <div class="mask sprite_01"></div>
        <img src="./img/music_album01.jpg" alt="" />
        <div class="info sprite_01">
          <i class="icon-left sprite_02"></i>
          <span>90万</span>
          <i class="icon-right sprite_02"></i>
        </div>
      </div>
      <!-- 底部图片 -->
      <div class="text">天气好的话，把耳机分给我一半吧</div>
    </div>
  </body>
</html>
```

![[00 assets/60328e81ea3600904d7df516ba30473e_MD5.png]]

1、编写`网页`的时候遵循先整体后局部的处理方式，编写`CSS`的时候尽量使用下面的显示格式

![[00 assets/f7b2c02f1c39e9deb7e1a3f9d7f190e2_MD5.png]]

2、我们可以将这些`公共CSS`抽取处理，尽量命名为`xxx_xxx`的格式

![[00 assets/3429cc6dda5060e57deefaec197d6aa5_MD5.png]]

3、对于这种拥有相同属性的`CSS`可以设置为`xxx-xxx`的格式

![[00 assets/e67ff7d1972938fe398c8c1ba694a5f3_MD5.png]]

## 8.5 fixed

`fixed`是相对于视口来定位。因为是相对于视口所以会一直定位在哪里，不会根据视口改变

![[00 assets/dbc936874371afb74d4a439224e4287d_MD5.jpeg]]

## 8.6 sticky

![[00 assets/fe877ed3bf4ed39f0983443a9b70c8b9_MD5.jpeg]]

1、当你设置了`sticky`定位，就是`relative`和`fixed`的结合。当你设置了`top...`等方向，就是距离该位置阈值，只要超过了这个阈值就会变为`fixed`定位，固定在滚动元素中

![[00 assets/5dac977609cf1cc4a8aac63debc00ba8_MD5.png]]

左图是超过阈值之后，右图为没超过阈值，那么就是`relative`

![[00 assets/fae93a322705d53a5a74175d6e4d7572_MD5.png]]

2、`sticky`的阈值是相当于最近的滚动元素的，不能按照`fixed`一样，完全相对于视口来处理 ^6d6071

![[00 assets/eb6b03369a248f3668dc08646aa9093c_MD5.png]]

## 8.7 z-index

![[00 assets/fcdfd430cb82a587f88f1269110f2c65_MD5.png]]

1、只有`定位元素`有`z-index`，如果不是`定位元素`你设置了`z-index`也不行。而且需要看`z-index`的层级关系

2、如果是兄弟关系的话，那么层级关系就是比较`z-index`的值。

![[00 assets/c508fe87cbe645d4bb0366e23e9d2101_MD5.png]]

3、当不是`兄弟元素`的话，那么就会寻找`最邻近的定位元素`进行比较，必须要设置`z-index`

![[00 assets/4104d3bdeb123e571ee272111fb18333_MD5.png]]

如果`父盒子`设置了`定位`和`z-index`，那么就会影响下面子盒子的定位

![[00 assets/f8b06f806b6382e437d2861ce22cc816_MD5.png]]

# 9. 浮动

## 9.1 基本介绍

![[00 assets/2ecec8a4d58ca3a84d344ff479547cf8_MD5.png]]

## 9.2 浮动特点

> 规则一

![[00 assets/cc0ded276fc3864f4bedd72de92eace7_MD5.png]]

![[00 assets/6dfa2bdbf32ae24a97c1e8e241c76c83_MD5.png]]

> 规则二

![[00 assets/7d15373a51c272f3283a2b1274f9212f_MD5.png]]

> 规则三

![[00 assets/1a1298f3934e6b42b8701b8eef47c2fb_MD5.png]]

![[00 assets/f1bbe7abae90ba2ad05c788edad0c269_MD5.png]]

> 规则四

![[00 assets/41c09d870c484cb8a89e73422c39745b_MD5.png]]

> 规则五

![[00 assets/29fd2890b157935217f0a2c08deacd03_MD5.png]]

## 9.3 导航条练习

要练习的样式

![[00 assets/2d5597583ae5800bb561a4d825b8492b_MD5.png]]

我们的做法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
        .main{
            float: left;
            color: slategray;
            background-color:rgb(223, 224, 215);
            height: 40px;
            width: 860px;
        }
        span{
            margin-left: 30px;
            line-height: 40px;
        }
    </style>
</head>
<body>
    <div class="main">
        <span>HTML/CSS</span>
        <span>Browser Side</span>
        <span>Server Side</span>
        <span>Programming</span>
        <span>XML</span>
        <span>Web Building</span>
        <span>Reference</span>
    </div>
</body>
</html>
```

![[00 assets/1830f992de5af69ca894e73f406751cc_MD5.png]]

下面是老师的做法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="2.css">
    <style>
        .main{
            width: 1205px;
            height: 48px;

            background-color: #E8E7E3;

            margin: 100px auto;

            list-style-type:none;
        }
        .main li{
            float: left;

            line-height: 48px;
        }
        .main a{
            display: block;
            text-decoration: none;
            color: #777777;
            font-size: 18px;
            padding: 0 39px;
        }
        .main a:hover{
            background-color: #3F3F3F;
            color: #E8E7E3;
        }
    </style>
</head>
<body>
    <ul class="main">
        <li>
            <a href="#">HTML/CSS</a>
        </li>
        <li>
            <a href="#">Browser Side</a>
        </li>
        <li>
            <a href="#">Server Side</a>
        </li>
        <li>
            <a href="#">Programming</a>
        </li>
        <li>
            <a href="#">XML</a>
        </li>
        <li>
            <a href="#">Web Building</a>
        </li>
        <li>
            <a href="#">Reference</a>
        </li>
    </ul>
</body>
</html>
```

```css
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
```

![[00 assets/6552b1ce6e5489d4ed710217a02859a7_MD5.png]]

# 10. 动画

[[动画]]

# 12. 补充

## 12.1 元素隐藏的 4 种方式

![[00 assets/b683c4911d6db2cd9883a7c876aab1c0_MD5.png]]

> display

使用`display`来达到隐藏元素的效果

![[00 assets/b77c2dc8ed9eb406bb1f6c83b37a97ff_MD5.png]]

> visibility

这个和`display`的区别，就是`display`隐藏元素就不会占据位置了，但是`visibility`隐藏元素依旧会占据位置

![[00 assets/2ae17271761a3fba04eb784f805172ff_MD5.png]]

> rgba

使用`rgba`的形式只会设置该元素的值，并不存在继承，所以设置比较麻烦

![[00 assets/055ae8ba2dc2c9c151d6c950c5d21266_MD5.png]]

> opacity

使用`opacity`也就是相当于`rgba(0,0,0,0)`，但是该属性存在继承，所以设置之后都会隐藏

![[00 assets/80ef0723d67147472ff966b98ab5dc84_MD5.png]]

## 12.2 精灵图

### 12.2.1 基本介绍

![[00 assets/dcfaec787969ff9670c14a1b12b98bd2_MD5.png]]

下面就是一种精灵图，将很多的小图片合成到一张图片中

![[00 assets/c42a24d4a617e17d7744a662c7ac8303_MD5.png]]

### 12.2.2 基本使用

**精灵图处理网站**：[Sprite Cow - Generate CSS for sprite sheets](http://www.spritecow.com/)，可以选择精灵图中的图标来获取位置

![[00 assets/56146d355eefc51fe6286f5db723d320_MD5.png]]

然后在`HTML`中复制上面的代码即可

![[00 assets/8672031b0a65549b39624633504ce997_MD5.png]]

## 12.3 cursor

`cursor`可以设置光标的显示样式，**MDN 官方文档**：[cursor - CSS（层叠样式表） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/cursor)

![[00 assets/03286829c8c3ebf342e221d1e36b43c7_MD5.png]]

## 12.4 问题汇总

### 12.4.1 解决盒子中字母数字不换行问题

当你输入`数字`或`字母`过长的时候，就会超出盒子。这是因为浏览器把这些字母当成一个单词，作为一行显示，假如我们打一个空格就会完整显示，如果我们想避免这个问题，就可以使用`word-break`来处理

`MDN文档`：[word-break - CSS（层叠样式表） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/word-break)

![[00 assets/d5a13d859beedfb382fc2406b3285888_MD5.png]]

使用`word-break`的话就可以解决这个问题了

![[00 assets/ad97f913c203a3d7291fde524d2a1527_MD5.png]]

### 12.4.2 行内元素间隙去除

相邻得行内元素之间会存在空隙

![[00 assets/cc6acb6187e01aba3b44c38229d3af9d_MD5.png]]

1、这是因为`换行`得问题，假如我们不换行的话就不存在这个问题

![[00 assets/bf7cd476e84baf5d822773a51f8b4f7e_MD5.png]]

2、我们对`行内元素`使用`float`也可以实现功能

![[00 assets/1b8208c9d2617a79d9b84587e8865fa8_MD5.png]]

3、使用`flex布局`处理也可以

![[00 assets/6b2e6f1811d8527cfa5481d4750e81d6_MD5.png]]

# CSS3

## 6. 伪类选择器

### 6.4 伪元素

::selection{} 表示选中的内容，就是用鼠标选中的时候会改变

```html
<head>
    <style>
        p::selection{
            color:red;
        }
    </style>
</head>

<p>我是一个大傻逼</p>
```

![[00 assets/f8dcd930a59a4c9737383c2c959ea28e_MD5.jpeg]]

### 6.7 :target

设置当你点击链接的时候，跳转的标签的属性根据你的设定而改变

而且前面加上标签名可以指定标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			p:target{
				width: 2.8rem;
				height: 24px;
				background-color: chocolate;
			}

			div:target{
				width: 50px;
				height: 23px;
				background-color: red;
			}
		</style>
	</head>
	<body>
		<p><a href=" #one">点击链接1</a></p>
		<div><a href="#two">点击链接2</a></div>


		<p id="one">内容1</p>
		<div id="two">内容2</div>
	</body>
</html>
```

![[00 assets/d095f02ef952f7261b1405906888638f_MD5.png]]

![[00 assets/012a006674ff0c7acc3e3ddb55902f60_MD5.jpeg]]

### 6.8 enabled 和 disabled

假如这个表单是允许输入的话，就是 enabled 的伪类选择器

假如不允许输入的话，就是 disabled

```html
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<style>
			input:enabled{
				background-color: red;
			}
			input:disabled{
				background-color: brown;
			}
		</style>
	</head>
	<body>
		<input type="text" disabled="disabled" />
		<input type="text" />
	</body>
</html>

```

## 10. 盒子模型

### 10.6 垂直方向的布局

垂直方向基本没什么特殊的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1{
            background-color: royalblue;
            height: 500px;
        }
        .box2{
            background-color: salmon;
            height: 100px;
            width: 100px;
            margin-bottom: 100px;
        }
    </style>
</head>
<body>
    <div class="box1">
        <div class="box2"></div>
        <div class="box2"></div>
    </div>
</body>
</html>
```

![[00 assets/a5dbd0e9205cc291a273d3fda22f74f9_MD5.jpeg]]

假如说子元素超过父元素的话，那么这个子元素是从父元素溢出

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1{
            background-color: royalblue;
            height: 100px;
        }
        .box2{
            background-color: salmon;
            height: 200px;
            width: 100px;
        }
    </style>
</head>
<body>
    <div class="box1">
        <div class="box2"></div>
    </div>
</body>
</html>
```

![[00 assets/77afe1c708f93f0fed9209baa647c95d_MD5.png]]

#### 10.6.1 overflow 属性

visible：默认值，子元素可以超过父元素

hidden：溢出的内容会被剪接

scroll：生成一个滚动条

auto：根据需求生成滚动条

但是还要两个属性，就是 overflow-x、overflow-y

### 10.7 外边距的折叠

相邻的垂直方向的外边距会发生重叠现象

兄弟元素

1）假如说两个都是正的，兄弟元素间的相邻垂直外边距会取最大值

2）假如说一个正一个负的话，就是，就是两者相加

3）假如是两个负值的话，就是取绝对值最大的那个

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1,.box2{
            height: 200px;
            width: 200px;
        }
        .box1{
            background-color: seagreen;
            margin-bottom: 100px;
        }
        .box2{
            background-color: silver;
            margin-top: 200px;
        }
    </style>
</head>
<body>
    <div class="box1"></div>
    <div class="box2"></div>
</body>
</html>
```

![[00 assets/7f3f13e6663ac7a8805cc635b3600012_MD5.png]]

父子元素

父子元素之间相邻的外边距，子元素会传递给父元素

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1{
            width: 200px;
            height: 200px;
            background-color: seagreen;
        }
        .box2{
            width: 100px;
            height: 100px;
            background-color: silver;
            margin-top: 100px;
        }
    </style>
</head>
<body>
    <div class="box1">
        <div class="box2"></div>
    </div>
</body>
</html>
```

![[00 assets/2c2116ca1e5e2b52cb7ba6963ebad4cc_MD5.png]]

### 10.11 边框阴影和圆角

#### 10.11.4 border-image

下面是关于图片边框的属性

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			div{
				width: 300px;
				height: 6.25rem;
				border-style: solid;
				border-image-source: url(img href="2.html");
				border-image-slice: 33%;
				border-width: 41px;
				border-image-outset: 0;
				border-image-repeat: repeat;
                <!--repeat是重复填充，streach是拉伸填充-->

			}
		</style>
	</head>
	<body>
		<div>
		</div>
	</body>
</html>
```

## 13. 网页布局

也就是关于网页布局的一个代码，也是一种思维，html 强调的是语义化标签的使用，下面就是语义化标签的使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="2.css">
    <style>
        header,main,footer{
            width: 900px;
            margin: 0 auto;
        }

        header{
            height: 150px;
            background-color: black;
        }

        main{
            height: 300px;
            background-color: blanchedalmond;
            margin: 10px auto;
        }

        nav,article,aside{
            height: 300px
        }
        nav{
            width: 200px;
            background-color: blueviolet;
            float: left;
        }
        article{
            width: 480px;
            margin: auto 10px;
            background-color: brown;
            float: left;
        }
        aside{
            width: 200px;
            background-color: cadetblue;
            float: left;
        }

        footer{
            height: 150px;
            background-color: blue;
        }
    </style>
</head>
<body>
    <header>

    </header>
    <main>
        <nav></nav>
        <article></article>
        <aside></aside>
    </main>
    <footer>

    </footer>
</body>
</html>
```

![[00 assets/030be36a47e15d83a186a28864232b60_MD5.png]]

## 14. 高度塌陷和 BFC

### 14.1 高度塌陷

我们先设置这个内容，是不是不设置父元素的高度的话，那么父元素的高度就由子元素来接替

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .aaa{
            border: 10px royalblue solid;
        }
        .bbb{
            width: 100px;
            height: 200px;
            background-color: seagreen;
        }
    </style>
</head>
<body>
    <div class="aaa">
        <div class="bbb"></div>
    </div>
</body>
</html>
```

![[00 assets/72340dfc43360bae2546feac1d3806d0_MD5.png]]

但是假如我们设置浮动的话，就会发现高度塌陷了

![[00 assets/5a5f3bfdafc8e96507b86081e509ba89_MD5.png]]

### 14.2 BFC

BFC 是一个 css 的隐含样式，叫做块级格式化环境，开启之后会变成一个独立的布局区域

开启后的特点

1）元素不会被浮动元素所覆盖

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .aaa{
            width: 200px;
            height: 200px;
            background-color: slateblue;
            float: left;
        }
        .ccc{
            width: 200px;
            height: 200px;
            background-color: skyblue;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <div class="aaa"></div>
    <div class="ccc"></div>
</body>
</html>
```

![[00 assets/1e31c4cd69fa7c50a0adf24575ce4c6e_MD5.png]]

2）子元素和父元素外边距不会重叠

你看下面的外边距的问题，是不是父元素移动了，但是子元素并没有移动

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .aaa{
            width: 200px;
            height: 200px;
            background-color: slateblue;
        }
        .bbb{
            width: 100px;
            height: 100px;
            background-color: skyblue;
            margin-top: 100px;
        }
    </style>
</head>
<body>
    <div class="aaa">
        <div class="bbb"></div>
    </div>
</body>
</html>
```

![[00 assets/a25474f37891b5a62e2d292c1b9be76f_MD5.png]]

但是我们可以设置 BFC 来改变

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .aaa{
            width: 200px;
            height: 200px;
            background-color: slateblue;
            overflow:hidden;
        }
        .bbb{
            width: 100px;
            height: 100px;
            background-color: skyblue;
            margin-top: 100px;
        }
    </style>
</head>
<body>
    <div class="aaa">
        <div class="bbb"></div>
    </div>
</body>
</html>
```

![[00 assets/ec3107df607bf9d409be6758420cd86c_MD5.png]]

3）可以包含浮动的子元素

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .aaa{
            border: 10px royalblue solid;
            /* float: left; */
            /* display: inline-block; */
            overflow: hidden;
        }
        .bbb{
            width: 100px;
            height: 100px;
            background-color: seagreen;
            float: left;
        }
        .ccc{
            width: 200px;
            height: 200px;
            background-color: skyblue;
        }
    </style>
</head>
<body>
    <div class="aaa">
        <div class="bbb"></div>
    </div>
    <div class="ccc"></div>
</body>
</html>
```

![[00 assets/d5cebd70f37c24a65b309cdb72792437_MD5.png]]

我们可以通过一些特殊手段来开启

1）设置元素的浮动

2）将元素设置为行内块元素

3）使用 overflow 元素，一般使用 hidden 来开启 BFC

### 14.3 使用 after 伪类解决高度塌陷

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .aaa{
            border: 10px red solid;
        }
        .bbb{
            width: 100px;
            height: 200px;
            background-color: skyblue;
            float: left;
        }
        .aaa::after{
            content: '';
            display: block;
            clear: both;
        }

    </style>
</head>
<body>
    <div class="aaa">
        <div class="bbb"></div>
    </div>
</body>
</html>
```

![[00 assets/009a094716136ebf9650ccdf01f67307_MD5.png]]

## 15. clear

### 15.1 clear 属性

清除浮动元素对当前元素所产生的影响，其原理是添加了外边距，使其不受影响

可选值：

left 是设置左侧浮动元素的影响

right 是设置右侧浮动元素的影响

both 请除最大影响

下面就是清除左侧浮动的影响

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .aaa{
            width: 200px;
            height: 200px;
            background-color: slateblue;
            float: left;
        }
        .bbb{
            width: 200px;
            height: 400px;
            background-color: skyblue;
            float: right;
        }
        .ccc{
            width: 200px;
            height: 200px;
            background-color: slategrey;
            clear: left;
        }
    </style>
</head>
<body>
    <div class="aaa"></div>
    <div class="bbb"></div>
    <div class="ccc"></div>
</body>
</html>
```

![[00 assets/b2ce58023c495f06c087e8dd01bad382_MD5.png]]

清除最大的影响

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .aaa{
            width: 200px;
            height: 200px;
            background-color: slateblue;
            float: left;
        }
        .bbb{
            width: 200px;
            height: 400px;
            background-color: skyblue;
            float: right;
        }
        .ccc{
            width: 200px;
            height: 200px;
            background-color: slategrey;
            clear: both;
        }
    </style>
</head>
<body>
    <div class="aaa"></div>
    <div class="bbb"></div>
    <div class="ccc"></div>
</body>
</html>
```

![[00 assets/eb7f711339dfb51f6bbebbe00f7223e3_MD5.png]]

但是这里发现了一个问题，还是说一下，有时间的话可以去研究一下，假如说你去更换盒子的位置的，就会导致这个没正常运行

### 15.2 clear 解决高度塌陷

这个是在 html 里面解决的，不是很完美，可以使用伪类 after

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .aaa{
            border: 10px red solid;
        }
        .bbb{
            width: 100px;
            height: 200px;
            background-color: skyblue;
            float: left;
        }
        .ccc{
            clear: both;
        }
    </style>
</head>
<body>
    <div class="aaa">
        <div class="bbb"></div>
        <div class="ccc"></div>
    </div>
</body>
</html>
```

![[00 assets/11694e285040e3b5206724f38b0798cb_MD5.png]]

### 15.3 clearfix

clearfix 不仅可以解决外边距重叠的问题，还可以解决高度塌陷的问题

下面这个是解决了外边距重叠的问题

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .aaa{
            width: 200px;
            height: 200px;
            background-color: red;
        }
        .bbb{
            width: 100px;
            height: 100px;
            background-color: skyblue;
            margin-top: 100px;
        }
        .clearfix::before,.clearfix::after{
            content: '';
            display: table;
            clear: both;
        }
    </style>
</head>
<body>
    <div class="aaa clearfix">
        <div class="bbb"></div>
    </div>
</body>
</html>
```

![[00 assets/347e8cd28291873f9d2342ab012708ce_MD5.png]]

下面的是解决了高度塌陷的问题

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .aaa{
            border: red 10px solid;
        }
        .bbb{
            width: 100px;
            height: 100px;
            background-color: skyblue;
        }
        .clearfix::before,.clearfix::after{
            content: '';
            display: table;
            clear: both;
        }
    </style>
</head>
<body>
    <div class="aaa clearfix">
        <div class="bbb"></div>
    </div>
</body>
</html>
```

![[00 assets/2c3551307acc45d6d56679b1d2bbc41b_MD5.png]]

## 17. 字体

### 17.2 图标字体简介

这里介绍的是 font swesome 的图标库，注意这里最好下载英文版的，中文版的版本很低

在文件夹里面有一个 zeal 的文档查看器，可以查看各个语言的文档指南

下面是使用的格式，还要注意的是 all.css 是没压缩过的，all.min.css 是压缩过的格式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/555/css/css/all.css">
</head>
<body>
    <div class="fa-3x">
        <i class="fas fa-spinner fa-spin"></i>
        <i class="fas fa-circle-notch fa-spin"></i>
        <i class="fas fa-sync fa-spin"></i>
        <i class="fas fa-cog fa-spin"></i>
        <i class="fas fa-spinner fa-pulse"></i>
        <i class="fas fa-stroopwafel fa-spin"></i>
      </div>
</body>
</html>
```

![[00 assets/45e61dd5dea263c7ba74b286b153059e_MD5.jpeg]]

下面还有一些使用

首先还是引用 link，然后使用伪类来处理，在 zeal 文档的后面有一个编号，然后再引入图标字体，在 all.css 的文件里面 ctrl+f 查找，设置 font-weight，下面是基本格式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/555/css/css/all.css">
    <style>
        li{
            list-style: none;
        }
        li::before{
            content: '\f2a1';
            font-family: 'Font Awesome 5 Free';
            font-weight: 900;
        }
    </style>
</head>
<body>
    <ul>
        <li>我是一个li语句</li>
        <li>我是一个li语句</li>
        <li>我是一个li语句</li>
        <li>我是一个li语句</li>
        <li>我是一个li语句</li>
    </ul>
</body>
</html>
```

![[00 assets/b593bb8e86462840eb373f9fd9641161_MD5.png]]

### 17.3 iconfont

iconfont 是阿里的一个图标字体库，注意不能商用

下面是基本格式，和 font awwsome 是一样的使用格式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/666/2/font_2782100_5wfh48o7nto/iconfont.css">
    <style>
        i.iconfont{
            font-size: 100px;
        }
    </style>
</head>
<body>
    <i class="iconfont">&#xe60d;</i>
</body>
</html>
```

![[00 assets/4a6a2c8dcf0027bdc0d1b3925393fe76_MD5.png]]

下面是伪类元素的使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/666/2/font_2782100_5wfh48o7nto/iconfont.css">
    <style>
        li{
            list-style: none;
        }
        li::before{
            content: '\e60e';
            font-family: 'iconfont';
            font-size: 50px;
        }
    </style>
</head>
<body>
    <ul>
        <li>这是</li>
        <li>它是</li>
        <li>你是</li>
        <li>就是</li>
    </ul>
</body>
</html>
```

### 17.5 字体的简写属性

一般的 font 的简写是 font:字体风格 字体大小/行高 字体

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>111</title>
    <style>
        div{

            font:bold italic 50px/2 微软雅黑;
        }
    </style>
</head>
<body>
    <div>这是一个什么语句</div>
</body>
</html>
```

![[00 assets/adfb57333d9efade02de499e2f403a3d_MD5.png]]

注意一个情况，在简写上面设置的样式是没用的，font 简写默认是 normal，你在前面设置的样式会在后面进行覆盖，最后还是 normal，行高也是一样的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>111</title>
    <style>
        div{

            font-style: italic;
            font: 50px/2 微软雅黑;
        }
    </style>
</head>
<body>
    <div>这是一个什么语句</div>
</body>
</html>
```

![[00 assets/e29de90e1d140af48484b7632f438673_MD5.jpeg]]

### 17.8 文本的水平和垂直对齐

#### 17.8.2 vertical-align

vertical-align 是垂直对齐，可选值:baseline 基线对齐、top 顶端对齐、bottom 底端对齐、middle 居中对齐

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>111</title>
    <style>
        div{
            font-size: 100px;
            border: 1px red solid;
        }
        span{
            font-size: 20px;
            border: 1px blue solid;
            vertical-align: middle;
        }
    </style>
</head>
<body>
    <div>这是一个什么<span>语句</span></div>
</body>
</html>
```

![[00 assets/fb36d06596d4839d182ba3f47ad31358_MD5.png]]

垂直对齐也是可以设置数值的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>111</title>
    <style>
        div{
            font-size: 100px;
            border: 1px red solid;
        }
        span{
            font-size: 20px;
            border: 1px blue solid;
            vertical-align: 50px;
        }
    </style>
</head>
<body>
    <div>这是一个什么<span>语句</span></div>
</body>
</html>
```

![[00 assets/f406029c188ea03d78ac0ab4910313a0_MD5.png]]

我们再来看图片，是不是受基线的影响，下面一直会有一个空隙，我们可以设置垂直对齐来消除

![[00 assets/18000722187b3f770486753661d15121_MD5.png]]

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>111</title>
    <style>
        div{
            border: 1px red solid;
        }
        img{
            vertical-align: top;
        }
    </style>
</head>
<body>
    <div>
        <img src="iii/屏幕截图 2027-20 121032.png">
    </div>
</body>
</html>
```

![[00 assets/668c26747e4f6fbe850b767a7563646f_MD5.jpeg]]

## 18. 背景

### 18.6 background-origin

自行定义背景图像的位置，可以实现背景图片夹在文字下面，里面的方向通过 background-position 来实现调整

content-box 背景图像的相对位置的内容框

border-box 背景图像边界框的相对位置

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<style>
div
{
	border:1px solid black;
	padding:35px;
	background-image:url(./img/up.png);
	background-repeat:no-repeat;
	background-position:left;/*来调背景图像的方向*/
}
#div1
{
	background-origin:border-box;
}
#div2
{
	background-origin:content-box;
}
</style>
</head>
<body>

<p>背景图像边界框的相对位置：</p>
<div id="div1">
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
</div>

<p>背景图像的相对位置的内容框：</p>
<div id="div2">
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
</div>

</body>
</html>
```

![[00 assets/591c707033fceff76e1f6701ff7d866d_MD5.png]]

### 18.5 background_clip

background_clip 设置背景的裁剪

border-box 默认值。背景绘制在边框方框内（剪切成边框方框）

padding-box 背景绘制在衬距方框内（剪切成衬距方框）

content-box 背景绘制在内容方框内（剪切成内容方框）

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<style>
#example1 {
    border: 10px dotted black;
    padding:35px;
    background: yellow;
}

#example2 {
    border: 10px dotted black;
    padding:35px;
    background: yellow;
    background-clip: padding-box;
}

#example3 {
    border: 10px dotted black;
    padding:35px;
    background: yellow;
    background-clip: content-box;
}
</style>
</head>
<body>

<div id="example1">
<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</p>
</div>

<div id="example2">
<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</p>
</div>

<div id="example3">
<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</p>
</div>

</body>
</html>
```

![[00 assets/717e3268712ac188d8f48457d9d7acb9_MD5.png]]

### 18.6 线性渐变

基本语法格式:background-image: linear-gradient(),可以实现渐变的效果，里面的 deg 的值是设置渐变的方向

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			div{
				width: 200px;
				height: 200px;
				background-image: linear-gradient(30deg,#0f0,#00f);
			}
		</style>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/d740e3fcef552e44d2bf1765b625952d_MD5.png]]

关于里面值的改变

```html
/* 从上到下，蓝色渐变到红色 */
linear-gradient(blue, red);

/* 渐变轴为45度，从蓝色渐变到红色 */
linear-gradient(45deg, blue, red);

/* 从右下到左上、从蓝色渐变到红色 */
linear-gradient(to left top, blue, red);

/* 从下到上，从蓝色开始渐变、到高度40%位置是绿色渐变开始、最后以红色结束 */
linear-gradient(0deg, blue, green 40%, red);
```

下面是设置重复的渐变

```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			div{
				width: 200px;
				height: 200px;
				background-image: repeating-linear-gradient(90deg,#0f0,#00f 10%,#666 15%);
			}
		</style>
	</head>
	<body>
		<div></div>
	</body>
</html>
```

![[00 assets/7035eca14b42bc7aaa65e4f8db088647_MD5.jpeg]]

### 18.7 径向渐变

background-image: radial-gradient()

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			div{
				width: 200px;
				height: 200px;
				border-radius: 50%;
				background-image: radial-gradient(ellipse at center,#0f0,#f30);
			}
		</style>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/b2fdbd60759bb6c56c723c9a6dd22ce8_MD5.jpeg]]

基本格式：background-image: repeating-radial-gradient(shape size at position, start-color, ..., last-color);

**shape** 确定圆的类型

ellipse (默认): 指定椭圆形的径向渐变。

circle ：指定圆形的径向渐变

**size** 定义渐变的大小，可能值：

farthest-corner (默认) : 指定径向渐变的半径长度为从圆心到离圆心最远的角

closest-side ：指定径向渐变的半径长度为从圆心到离圆心最近的边

closest-corner ： 指定径向渐变的半径长度为从圆心到离圆心最近的角

farthest-side ：指定径向渐变的半径长度为从圆心到离圆心最远的边

**position** 定义渐变的位置。可能值：

center（默认）：设置中间为径向渐变圆心的纵坐标值。

top：设置顶部为径向渐变圆心的纵坐标值。

bottom：设置底部为径向渐变圆心的纵坐标值。

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style>
			div{
				width: 200px;
				height: 200px;
				border-radius: 50%;
				background-image: repeating-radial-gradient(circle at 50% 50%,#111,#666 10%,#eee 15%);
			}
		</style>
	</head>
	<body>
		<div></div>
	</body>
</html>

```

![[00 assets/eb3e6e31ae2ace18bb66e39884ee3b22_MD5.png]]

## 19. 页面交互元素

这个基本 ie 都不支持，就少用

### 19.1 meter

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>展示给定的数据范围：</p>
<meter value="2" min="0" max="10">2 out of 10</meter><br>
<meter value="0.6">60%</meter>

<p><strong>注意：</strong> IE 浏览器不支持 meter 标签。</p>

</body>
</html>
```

![[00 assets/eb4b1e51e1840e1d51924b516daa8688_MD5.png]]

### 19.2 mark

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<p>Do not forget to buy <mark>milk</mark> today.</p>

</body>
</html>
```

![[00 assets/ffe5ee21675e7351cb16dcd0d47783f0_MD5.png]]

### 19.3 progress

```html
<!DOCTYPE html>
<html>
<body>

下载进度：
<progress value="22" max="100">
</progress>

<p><b>注释：</b>Internet Explorer 9 以及更早的版本不支持 <progress> 标签。</p>

</body>
</html>
```

![[00 assets/f5c0f6f762545bf2701e50cbfae36b5a_MD5.jpeg]]

## 21. 变换

## 1.1 基本介绍

![[00 assets/87750e02fdf4d8db4cf0d210a6ac2639_MD5.png]]

## 2.2 坐标系

原本得坐标系是在元素得左上角位置‘，假如我们使用`transform属性`得话就会移动到中心

![[00 assets/d3a3dccc01a787b844eed8cae68c23b4_MD5.png]]

1、假如我们使用了`transform`得话，坐标系就会发生改变

![[00 assets/cc1dae20151af410fb750ed3d05a37f0_MD5.png]]

2、我们在`transform`中参数顺序得不同要会导致不同得结果，根本原因是因为坐标系的改变

![[00 assets/1a24d33dd70e207bfb47c6dfde9487f6_MD5.png]]

## 2.3 transform-origin

1、使用该属性可以修改元素得坐标系位置

![[00 assets/6249968590c89ff18f285be04afc1e73_MD5.png]]

### 21.1 2D 转换

#### 21.1 平移

使用 transform: translate(100px,50px)，前面是 x 轴，后面是 y 轴

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
		<style>
			div{
				width: 100px;
				height: 100px;

				background-color: chocolate;
				border: 1px solid red;
			}
			#one{
				transform: translate(100px,50px);
			}
		</style>
	</head>
	<body>
		<div>原位置</div>
		<div id="one">变化之后的位置</div>+
	</body>
</html>

```

![[00 assets/8db4e467f9d312b1ac75ba5179c9878e_MD5.png]]

#### 21.2 缩放

transform: scale(2,2)；是可以缩放，但是需要注意的一个点，它的宽和高是不会改变的，主要是 x 和 y 轴改变，所以视觉上是改变了

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
		<style>
			div{
				width: 100px;
				height: 100px;

				background-color: chocolate;
				border: 1px solid red;

				margin: 100px auto;
			}
			#one{
				transform: scale(2,2);
                transform: scaleX(2),scaleY(2);//这个和上面的效果是一样的

			}
		</style>
	</head>
	<body>
		<div>原位置</div>
		<div id="one">变化之后的位置</div>
	</body>
</html>

```

![[00 assets/2830a5a501db8d25966b0fa11ee56368_MD5.png]]

#### 21.3 倾斜

前面是沿着 x 轴来倾斜，后面是沿着 y 轴来倾斜

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
		<style>
			div{
				width: 100px;
				height: 100px;

				background-color: chocolate;
				border: 1px solid red;

				margin: 100px auto;
			}
			#one{
				transform: skew(0,30deg);

			}
		</style>
	</head>
	<body>
		<div>原位置</div>
		<div id="one">变化之后的位置</div>
	</body>
</html>

```

![[00 assets/08c6442a133ab66d4c5da6f1a67b396d_MD5.gif]]

#### 21.4 旋转

transform: rotate(30deg)，是设置旋转的角度的，deg 表示的是角度，但是我们通常搭配 transfrom-origin 来使用，这个是设置以那个点为基准来旋转的，一般默认的值是 50% 50% 0,分别是 x 轴，y 轴和 z 轴

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
		<style>
			div{
				width: 100px;
				height: 100px;

				background-color: chocolate;
				border: 1px solid red;

				margin: 100px auto;
			}
			#one{
				transform: rotate(30deg);
				transform-origin:0px 0px ;
			}
		</style>
	</head>
	<body>
		<div>原位置</div>
		<div id="one">变化之后的位置</div>
	</body>
</html>

```

![[00 assets/53ac337ecf55aeee81d64f4f01b5cb4b_MD5.png]]

#### 21.5 transfrom-origin

设置中心点的位置，默认值的位置是 50% 50% 0，分别是 x 轴，y 轴和 z 轴

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>菜鸟教程(runoob.com)</title>
		<style>
			#one{
				width: 100px;
				height: 100px;
				background-color: chocolate;
				transform: rotate(45deg);

				position: absolute;
			}
			#four{
				width: 100px;
				height: 100px;
				background-color: cornflowerblue;
				transform: rotate(45deg);

				transform-origin:50% 0 ;
				position: absolute;
			}
			#three{
				width: 200px;
				height: 200px;

				border: 1px solid red;

				margin: 100px auto;

				position: relative;
			}
		</style>
	</head>
	<body>
		<div id="three">
			<div id="one"></div>
			<div id="four"></div>
		</div>
	</body>
</html>

```

![[00 assets/566db6f7cdd4c615f232ffcc99f887a9_MD5.png]]

## 22. 盒子模型和定位的补充

### 22.1 盒子模型

#### 22.1.1 块元素

每个块级元素都独自占一行；并且可以使用 margin 和 padding，line-height 来设置位置；假如没设置宽度的话，元素本身是没有宽度的，里面的内容撑起父元素的宽度；

#### 22.1.2 内联元素（行内元素）

和其他元素共占一行；不能设置宽度和高度；并且是里面的内容撑开元素的宽度；

#### 22.1.3 内联块级元素

就是可以设置宽度和高度的内联元素

#### 22.1.4 补充

对于行级元素，margin-top 和 margin-bottom 是无效的

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title>
		<style>
			#content{
				width: 200px;
				height: 200px;
				background-color: chocolate;
			}

			#nav{

			}

			#size{
				margin-top: 50px;
				background-color: blueviolet;
			}
		</style> 
	</head>
	<body>
		<div id="content"></div>

		<div id="nav">
			<span id="size">这是一个行内元素</span>
		</div>
	</body>
</html>

```

![[00 assets/ad4169ec1ea427c13d6fafdb694d0c55_MD5.png]]

对于上面，假如你对 nav 的块设置一个 margin-top 的话，还是会改变位置，但是这里改变的是块的位置，然后这个块载着这个行内元素改变了位置，但是行内元素是不会改变其中的位置的

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title>
		<style>
			#content{
				width: 200px;
				height: 200px;
				background-color: chocolate;
			}

			#nav{
				margin-top: 100px;
			}

			#size{
				margin-top: 50px;
				background-color: blueviolet;
			}
		</style> 
	</head>
	<body>
		<div id="content"></div>

		<div id="nav">
			<span id="size">这是一个行内元素</span>
		</div>
	</body>
</html>

```

![[00 assets/6dae9c0c995153909c6aff4c88d9a894_MD5.png]]

对于块级元素，设置 padding-top 和 padding-bottom 在显示上面是有影响的，但是你可以理解为无效

这里面的 nav 的块元素的高度是行内元素设置的，但是行内元素是不能改变高度的，假如设置设置 padding，会在视觉上改变，但是实际上是已经没有了

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title>
		<style>
			#content{
				width: 200px;
				height: 200px;
				background-color: chocolate;
			}

			#nav{

			}

			span{
				background-color: blueviolet;
				padding: 50px;
			}
		</style> 
	</head>
	<body>
		<div id="content"></div>

		<div id="nav">
			<span>这是一个虚胖的块</span>
		</div>
		<p>看看我是不是浮在其他颜色里面</p>
	</body>
</html>

```

![[00 assets/7b6ca412dd29bab6aedf77c114c7fdd9_MD5.png]]

这里还有一个外边距重合的问题，发现没是不是下面设置的 margin 的高度是重合的

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title>
		<style>
			*{
				margin: 0px;
				padding: 0px;
			}
			.one{
				width: 200px;
				height: 200px;
				background-color: blueviolet;

				margin-bottom: 50px;
			}
			.two{
				width: 200px;
				height: 200px;
				background-color: cornflowerblue;

				margin-top: 50px;
			}
		</style> 
	</head>
	<body>
		<div class="one"></div>
		<div class="two"></div>
	</body>
</html>

```

![[00 assets/ed926afa9bb00a38f88d49c1e89f28f0_MD5.png]]

下面还有一个问题，就是盒子嵌套盒子的情况

是不是子盒子的 margin 是没啥用的，因为上面的情况，所以就是设置的最大的 margin-top 的值，导致了合并，这里就是 bfc，可以设置 display 为行内块元素来解决

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>菜鸟教程(runoob.com)</title>
		<style>
			.one{
				width: 200px;
				height: 200px;
				background-color: blueviolet;

				margin-top: 25px;
			}
			.two{
				width: 100px;
				height: 100px;
				background-color: cornflowerblue;

				margin-top: 50px;
			}
		</style> 
	</head>
	<body>
		<div class="one">
			<div class="two"></div>
		</div>
	</body>
</html>

```

![[00 assets/bf42ca85bf8a6da4717609de12dedea9_MD5.png]]

#### 22.1.5 经验总结

基本现在的优先级，就是 width>padding>margin

假如是设计一个网页的话，可以按照下面的方式来思考

确定结构 -> 布局方式 -> 行内元素 -> 盒子类型 -> width?height? -> padding? -> margin?

# 扩展

## 1. 页面布局

### 1.1 布局

一般网页的布局

![[00 assets/26c2e5a06be84a8d776fe6e197dce200_MD5.png]]

### 1.2 流式布局

![[00 assets/aec959c77b5b917f312240cc4c5cb130_MD5.png]]

假如你拉伸窗体之后，即便下面的格子是不会主动上来的

![[00 assets/558ca4e8aeb8e3ca94923b1bae229efa_MD5.png]]

### 1.3 浮动布局

![[00 assets/cb5d71174448d184895d8a034822c885_MD5.png]]

假如你拉伸窗口的时候，下面的块会上来

![[00 assets/e83e0212c92ba8dc88090dd1b7d21e55_MD5.png]]

## 2. flex 布局

### 2.1 flex 布局体验

#### 2.1.1 传统布局

兼容性好；布局繁琐；局限性，不能再移动端很好的布局

#### 2.1.2 flex 弹性布局

操作方便；布局极为简单；移动端应用广泛，PC 端浏览器支持情况较差；IE11 或更低版本，不支持或仅支持部分

#### 2.1.3 基础对比

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

### 2.2 flex 布局原理

用来为盒状模型提供最大的灵活性，任何一个容器都可以指定为 flex 布局

当我们给父元素设置为 flex 布局的以后，子元素的 float、clear 和 vertical-align 属性都将失效

也就是说，采用 flex 布局的元素，称为 flex 容器(flex container)，它是所有子元素自动成为容器成员，称为 flex 项目(flex item)

在上面的 flex 布局体验里面 div 就是 flex 父容器，span 就是子容器 flex 项目，并且子容器可以横向和纵向的排列

flex 总结：通过给父盒子添加 flex 属性，来控制子盒子的位置和排列方式

### 2.3. flex 布局父项常见的属性

#### 2.3.1 flex-direction

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

#### 2.3.2 justify-content

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

#### 2.3.3 flex-wrap

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

#### 2.3.4 align-items

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

#### 2.3.5 align-content

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

#### 2.3.6 flex-flow

是 flex-direction 和 flex-wrap 属性的复合属性

```html
flex-direction: row;
flex-wrap: wrap;
//下面的和上面的是一样的，就是一个简写的方式
flex-flow: row wrap;
```

#### 2.3.7 总结

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

### 2.4. 常见的子项属性

#### 2.4.1 flex-basis

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

#### 2.4.2 flex-grow

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

#### 2.4.3 flex-shrink

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

#### 2.4.4 flex

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

#### 2.4.5 flex 特殊写法

| 属性      | 作用           |
| --------- | -------------- |
| flex:auto | flex:1 1 auto  |
| flex:none | flex: 0 0 auto |
| flex:0%   | flex:1 1 0%    |
| flex:100% | flex:1 1 100%  |
| flex:1    | flex:1 1 0%    |

#### 2.4.6 align-self

align-self 属性允许单个项目与其他项目采取不一样的对齐方式

#### 2.4.7 order

order 设置排列的顺序，-1 是在前面，1 是后面

### 2.5. 案例设置

#### 2.5.1 输入框布局

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
			.box{
				width: 215px;
				display: flex;
				border: 1px solid #dcdcdc;
			}
			.box label{
				background-color: #f5f5f5;
				font-family: "楷体";
				text-align: center;
				justify-content: space-between;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<label>姓名</label>
			<input type="text" />
			<label>go</label>
		</div>
	</body>
</html>

```

![[00 assets/688c4119eb7182d64a78e3cb46fb61c7_MD5.png]]

## 3. 媒体查询

@media

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			#box{
				width: 200px;
				height: 200px;
			}
			@media screen and (min-device-width:0px) and (max-device-width:300px) {
				#box{
					background-color: burlywood;
				}
			}
			@media  screen and (min-device-width:301px) and (max-device-width:500px) {
				#box{
					background-color: blueviolet;
				}
			}
		</style>
	</head>
	<body>
		<div id="box"></div>
	</body>
</html>

```

假如你的屏幕大小在 0-300px 的话就是屏幕的大小 / 假如你的屏幕大小在 300px-500px 话就会变成紫色

注意这个只能在手机端才可以这样使用，假如式 pc 端的话式不能成功运行的，这是因为你使用的式 min-device-width 这个属性，这个是设备的宽度，假如是 pc 的话一般在 1000px 以上，这个的意义在于根据屏幕的大小，可以执行相关的 css 样式

### 3.1 width、height

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			#box{
				width: 200px;
				height: 200px;
			}
			@media screen and (min-width:0px) and (max-width:500px) {
				#box{
					background-color: burlywood;
				}
			}
			@media  screen and (min-width:501px) and (max-width:900px) {
				#box{
					background-color: blueviolet;
				}
			}
		</style>
	</head>
	<body>
		<div id="box"></div>
	</body>
</html>

```

这个是获取浏览器的大小，注意是浏览器的，而不是屏幕的，下面的带 device 的是根据设备的宽度大小来设置

### 3.2 device-width

根据设备的宽度来计算

### 3.3 device-height

根据设备的高度来计算

### 3.4 媒体查询的其他引用方式

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		#box{
			width: 400px;
			height: 400px;
		}
		#box div{
			height: 100px;
			float: left;
		}
		#box div:nth-child(1){
			background-color: red;
		}
		#box div:nth-child(2){
			background-color: blue;
		}
		#box div:nth-child(3){
			background-color: brown;
		}
	</style>
	<style media="(min-width:1000px)">
		#box div{
			width: 33.3%;
		}
	</style>
	<style media="(min-width:700px) and (max-width:999px)">
		#box div{
			width: 50%;
		}
	</style>
	<style media="(max-width:699px)">
		#box div{
			width: 100%;
		}
	</style>
</head>
<body>
	<div id="box">
		<div></div>
		<div></div>
		<div></div>
	</div>
</body>
</html>
```

下面是不同浏览器宽度的不同现实效果

![[00 assets/2b32474c14e34915d2921eb64e774ca1_MD5.png]]

![[00 assets/2866114e452ce7a7dc98d4dc8a595939_MD5.png]]

![[00 assets/b97eaa14bbdab57f13c34ab20b8353ff_MD5.png]]

我们也可以使用 link 来使用 media

```html
<link rel="stylesheet" type="text/css" href="#" media="(min-width:200px) and (max-width:800px)"/>
```

## 4. rem 的使用

指相对于根元素的字体大小，假如根元素的 font-size 是 10px，子元素的 font-size 是 1rem 的话，那么字体元素的大小就是 10px,假如设置的是 2rem 的话，就是 20px，这个会根据网页的大小来改变

## 5.grid 布局

https://zhuanlan.zhihu.com/p/256353171

# 积累

## 1. 高度塌陷问题

当我们同时设置了子元素和父元素的 margin 的值，就会取最大的 margin，并且子元素是不会动的，而是带着父元素一起动

解决方法：可以参考这个文档的高度塌陷解决方法

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
			}
			.son{
				width: 50px;
				height: 50px;
				margin-top: 500px;
				background-color: burlywood;
			}
		</style>
	</head>
	<body>
		<div class="father">
			<div class="son"></div>
		</div>
	</body>
</html>

```

## 2. href 和 src 的区别

[HTML 元素属性 href 和 src 的区别 - Web 前端工程师面试题讲解\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1jJ411P7iD)

herf 的英文别名为 Hypertext Reference(超文本 引用或者参照)

src 的英文别名为 Source(资源)

其实 href 本质就是给他了一个 onclick 的事件，然后发送 http 请求传输数据

```
<a href="../js/1.html">点击我</a>
```

下面就是请求到的页面，在浏览器的网络部分是看的到发送的 GET 请求

![[00 assets/ae2421e2fa9b03bef15da1bf755e0aa2_MD5.png]]

并且 href 是开辟了一个通道，点击之后就通过这个通道传输数据，这个通道其实就是 http 协议

sre 其实是将数据下载下来，然后将数据替换掉

![[00 assets/2611be5bf0e99514a0eaf027644ea636_MD5.png]]
