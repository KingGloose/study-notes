# 1. transition

## 1.1 基本使用

一般情况按照下面的方式来使用，但是为了性能优化不会去使用 **all** 来为所有属性添加动画

![[00 assets/9d3f319f434dd3c9e05657a82ba45509_MD5.png]]

![[00 assets/cd8751c5b2ce52ecc82213e7be506e33_MD5.gif]]

一般情况按照下面的方式来添加，可以避免一些性能损失

![[00 assets/71e56e5ef92531df22da9b1b951e85e0_MD5.png]]

## 1.2 transition-property

我们可以使用 **transition-property** 来指定执行动画的 CSS 属性

如果指定**简写属性**，比如下图的 **transform**，那么其完整版中所有可以动画的属性都会被应用过渡，尽量不填入简写属性

![[00 assets/620379c44d2dc50f49cbf9ad2ce916ce_MD5.png]]

## 1.2 transition-duration

参考链接：[transition-duration - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition-duration)

用于设置动画的时间，可以参考上图

## 1.3 transition-timing-function

参考链接：[transition-timing-function - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition-timing-function)

设置动画的演示的速度

![[00 assets/42f26b7ddb4bb997103aa9f67c8d0829_MD5.png]]

## 1.4 transition-delay

参考链接：[transition-delay - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition-delay)

设置动画的延迟，也就是设置多久之后才执行动画

## 1.5 transition 简写

参考链接：[transition - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/transition)

![[00 assets/fecac8e3de8bfd07b9774ba0dd7e01da_MD5.png]]

# 2. animation

## 2.1 基本使用

1、使用 **animation-name** 来为该元素添加 keyframes 动画

2、使用 **animation-duration** 来为动画添加动画时长

3、一般情况使用 **animation** 来简写属性

![[00 assets/8da3d64bcbf63ab6374263d470e1f1d3_MD5.png]]

![[00 assets/35dbd894d2f335c6dde9f5cc97be8cd6_MD5.gif]]

## 2.1 @keyframes

参考链接：[@keyframes - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@keyframes)

使用 **@keyframes** 来编辑动画，其中一个就是使用 **form / to** 来表示 **0% 和 100%**，或者直接使用 **%** 为单位表示该关键帧的样式

## 2.2 animation-duration

参考链接：[animation-duration - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-duration)

表示动画持续的时间

## 2.3 animation-timing-function

参考链接：[animation-timing-function - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-timing-function)

设置动画的演示的速度，参考属性：ease...

## 2.4 animation-delay

参考链接：[animation-delay - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-delay)

设置动画的延迟，也就是设置多久之后才执行动画

## 2.5 animation-iteration-count

参考链接：[animation-iteration-count - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-iteration-count)

设置动画播放的次数；如果是**数字**的话，就是重复了多少次，并且输入的数字会四舍五入；如果是 **infinite** 的就是循环无数次

![[00 assets/4ec21cea60363c1018349d6ad1dd9400_MD5.png]]

## 2.6 animation-direction

参考链接：[animation-direction - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-direction)

**animation-direction** 可以设置动画的正向播放、反向播放还是在正向和反向之间交替播放，具体的属性可以参考链接的网站

![[00 assets/82b38e123a46ba5cfa1df83ed2b20316_MD5.png]]

![[00 assets/edeee6b2d09cb06b533766869f0e95d8_MD5.gif]]

# 3. 3D 动画 / 3D 元素

## 3.1 基本介绍

![[00 assets/f09d0981eb7880f241f908b90455bba3_MD5.png]]

## 3.2 rotate3d - 旋转

![[00 assets/2011e23532180bb9df825cc68b1fa73c_MD5.png]]

![[00 assets/cd5fb321f21d2887cea6d397064efe13_MD5.png]]

![[00 assets/6168bb99b182d307909a6865b6239ab3_MD5.png]]

1、下面 2 个本质是一样的，`rotate`本质就是`rotateZ`的简写，因为本质就是 z 轴的旋转

2、`rotate3d`是`rotateZ、rotateX、rotateY`的简写，前三位是`x、y、z轴`，`1`表示开启，`0`表示关闭

![[00 assets/1556b19060eaca2d4a78e45657da038c_MD5.png]]

3、如果我们设置 2 个坐标轴的话，也会进行对应的变换

![[00 assets/85ad431956a9a0e9f9f00f50e2b4646a_MD5.png]]

4、如果想单独旋转的话，也可以单独写`rotateZ、rotateX、rotateY`

![[00 assets/ad8a56afea4e9b51af56f9915ab75466_MD5.png]]

## 3.3 perspective - 透视

![[00 assets/bf4263331bcd48a5a69aeda77e40fb6d_MD5.png]]

1、这里重点理解，透视`perspective`函数主要是定义观察者和`z轴`之间的距离，如果距离比较远就小，距离比较近就大

![[00 assets/b1375e4ae0e81abc6080d3b5ffc4c73b_MD5.png]]

2、对于`perspective`属性，你可以理解为只要给谁加了就以谁为观察者，适用于给父元素添加，如果你给子元素添加的话是没效果的

![[00 assets/326e0db48a956bced4a4b978b8fae2eb_MD5.png]]

3、但是对于`perspective()`函数来说，适用于给自己添加透视效果

![[00 assets/9b24408a446be79a32f3e8d60aee8cb0_MD5.png]]

## 3.4 translate3d - 平移

![[00 assets/4c31fc6e32335f9bd5f4e47935377446_MD5.png]]

![[00 assets/79e331f01c33e6996580ca010b020992_MD5.png]]

1、如果我们想要在`z轴`移动的话，需要添加上`perspective透视`才能看到效果

![[00 assets/ed8c67fd8fdca3724acbf82799039f2e_MD5.png]]

2、如果我们使用简写的形式`translateX`、`translateY`也可以实现元素的移动

![[00 assets/bb21cf87ceeb677a9e1f412572e0d0d9_MD5.png]]

## 3.5 scale3d - 缩放

![[00 assets/a95b3baeded1aa86595fae21bef020cb_MD5.png]]

![[00 assets/e1052fed6dae5c2d41f186b1cf991121_MD5.png]]

1、其基本的写法和上面是类似的，但是这个属性表示缩放

![[00 assets/e24e059e2b59bf35c609c5d0e20c5d54_MD5.png]]

## 3.6 transform-style

![[00 assets/4888736df5f33aabcb907f1d6abb8595_MD5.png]]

1、下面开启了`3d空间`之后的效果，明显能看出来子元素已经穿过父元素了

2、对于`transform-style`来说默认值就是`flat`，也就是平面

3、大部分的编写都是给父元素设置`perspective透视`和`transform-style`来表示`3d空间`

![[00 assets/3ab183821e580bdb9f75b8e603e045eb_MD5.png]]

## 3.7 backface-visibility

![[00 assets/f5f0daad4214335075971474f984351c_MD5.png]]

1、这里使用的下面的`正方形案例`来编写的，因为我这里没有注意背向的问题，所以观看不是很完整

2、我们添加了该属性之后，只要是背对着的元素就不可见

![[00 assets/4d8c06dba263d8d1f1602892235f77f9_MD5.png]]

## 3.8 案例

### 3.8.1 正方形

![[00 assets/47fa0b69449503e511db3eb2c976f49a_MD5.png]]

1、我们使用`3d`特效的时候，最好还是开启**定位**

​ 1.1 这是因为脱离了标准流，这样就是一个新的渲染层来执行效果，不仅性能会好很多，这是因为新的渲染层和原有的渲染层不同，所以只更新该渲染层，减少了很多的重绘步骤。

​ 1.2 而且不会影响原有标准流文档中的元素排版

2、最好的方式就是边写边绘制对应的`x,y,z轴`

![[00 assets/ac5ff50118d5607160ba0d85ab753b7f_MD5.png]]

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        background: url("./image/grid.png");
      }
      .main {
        position: relative;

        width: 100px;
        height: 100px;
        background-color: pink;
        /* opacity: 0.4; */

        margin-left: 200px;
        margin-top: 200px;

        /* perspective: 100px; */
        transform: rotateX(33.5deg) rotateY(45deg);
        transform-style: preserve-3d;
      }
      .item {
        position: absolute;
        left: 0px;
        top: 0px;

        width: 100%;
        height: 100%;
      }
      /* 顶部 */
      .top {
        background-color: rgba(105, 2, 249, 0.4);
        transform: rotateX(90deg) translateZ(50px);
      }
      .bottom {
        background-color: rgba(80, 94, 249, 0.4);
        transform: rotateX(90deg) translateZ(-50px);
      }
      .front {
        background-color: rgba(109, 249, 87, 0.4);
        transform: translateZ(50px);
      }
      .back {
        background-color: rgba(217, 249, 60, 0.4);
        transform: translateZ(-50px);
      }
      .right {
        background-color: rgba(75, 249, 246, 0.4);
        transform: rotateY(90deg) translateZ(50px);
      }
      .left {
        background-color: rgba(249, 52, 239, 0.4);
        transform: rotateY(-90deg) translateZ(50px);

        display: flex;
        justify-content: center;
        align-items: center;
      }
    </style>
  </head>
  <body>
    <div class="main">
      父元素
      <div class="item top">上</div>
      <div class="item bottom">下</div>
      <div class="item front">前</div>
      <div class="item back">后</div>
      <div class="item right">右</div>
      <div class="item left">左</div>
    </div>
  </body>
</html>
```

3、如果是开启对应的调试功能，在`edge`中是没有这个功能的，但是对于`chrome`来说是有的，相对来说调试旋转会方便很多

![[00 assets/2e02e39552540b03d918c37147cbad09_MD5.png]]

### 3.8.2 长方形

1、如果已经绘制成功正方形的话，要绘制长方形就很简单了，在父元素中使用`scale`属性就可

![[00 assets/9a68d31f3c20069b1772bdd0c0db01df_MD5.png]]

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        background: url("./image/grid.png");
      }
      .main {
        position: relative;

        width: 100px;
        height: 100px;
        background-color: pink;
        /* opacity: 0.4; */

        margin-left: 200px;
        margin-top: 200px;

        /* perspective: 100px; */
        transform: rotateX(33.5deg) rotateY(45deg) scaleX(2);
        transform-style: preserve-3d;
      }
      .item {
        position: absolute;
        left: 0px;
        top: 0px;

        width: 100%;
        height: 100%;
      }
      /* 顶部 */
      .top {
        background-color: rgba(105, 2, 249, 0.4);
        transform: rotateX(90deg) translateZ(50px);
      }
      .bottom {
        background-color: rgba(80, 94, 249, 0.4);
        transform: rotateX(90deg) translateZ(-50px);
      }
      .front {
        background-color: rgba(109, 249, 87, 0.4);
        transform: translateZ(50px);
      }
      .back {
        background-color: rgba(217, 249, 60, 0.4);
        transform: translateZ(-50px);
      }
      .right {
        background-color: rgba(75, 249, 246, 0.4);
        transform: rotateY(90deg) translateZ(50px);
      }
      .left {
        background-color: rgba(249, 52, 239, 0.4);
        transform: rotateY(-90deg) translateZ(50px);

        display: flex;
        justify-content: center;
        align-items: center;
      }
    </style>
  </head>
  <body>
    <div class="main">
      父元素
      <div class="item top">上</div>
      <div class="item bottom">下</div>
      <div class="item front">前</div>
      <div class="item back">后</div>
      <div class="item right">右</div>
      <div class="item left">左</div>
    </div>
  </body>
</html>
```

### 3.8.3 添加动画

![[00 assets/e914c21e0c3bb7642fb81a964480a712_MD5.gif]]

1、这样结合`css动画`的效果，也可以实现对应的动画旋转的效果

![[00 assets/21265984fce5ccbd42157b8c5e591d14_MD5.png]]

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        background: url("./image/grid.png");
      }
      .main {
        position: relative;

        width: 100px;
        height: 100px;
        background-color: pink;
        /* opacity: 0.4; */

        margin-left: 200px;
        margin-top: 200px;

        /* perspective: 100px; */
        transform: rotateX(33.5deg) rotateY(45deg) scaleX(2);
        transform-style: preserve-3d;

        animation: loop 2000ms linear infinite;
      }
      @keyframes loop {
        0% {
          transform: rotateX(33.5deg)  rotateY(45deg);
        }
        100% {
          transform: rotateX(33.5deg)  rotateY(405deg);
        }
      }

      .item {
        position: absolute;
        left: 0px;
        top: 0px;

        width: 100%;
        height: 100%;

        /* backface-visibility: hidden; */
      }
      /* 顶部 */
      .top {
        background-color: rgba(105, 2, 249, 0.4);
        transform: rotateX(90deg) translateZ(50px);
      }
      .bottom {
        background-color: rgba(80, 94, 249, 0.4);
        transform: rotateX(90deg) translateZ(-50px);
      }
      .front {
        background-color: rgba(109, 249, 87, 0.4);
        transform: translateZ(50px);
      }
      .back {
        background-color: rgba(217, 249, 60, 0.4);
        transform: translateZ(-50px);
      }
      .right {
        background-color: rgba(75, 249, 246, 0.4);
        transform: rotateY(90deg) translateZ(50px);
      }
      .left {
        background-color: rgba(249, 52, 239, 0.4);
        transform: rotateY(-90deg) translateZ(50px);

        display: flex;
        justify-content: center;
        align-items: center;
      }
    </style>
  </head>
  <body>
    <div class="main">
      父元素
      <div class="item top">上</div>
      <div class="item bottom">下</div>
      <div class="item front">前</div>
      <div class="item back">后</div>
      <div class="item right">右</div>
      <div class="item left">左</div>
    </div>
  </body>
</html>
```

### 3.8.4 webpack 动画 - keyframes 动画重复执行/停顿

![[00 assets/e55967de584ac588e3b1a5835de68b83_MD5.gif]]

![[00 assets/61c2246a84e64c3a69888d87475ae29d_MD5.png]]

1、这个正方形不会很难绘制，直参考上面的代码即可

2、但是这里有一个`keyframes帧动画`的一个小技巧：我们在绘制动画的时候有的时候想要一直重复的执行该动画，但是我们又想执行完改该动画之后停顿一段时间之后再去重复执行

我们可以采取下面的方式，只要该动画执行到`50%`的时候动画已经执行完毕，后续的`50%`就是已经执行好的的形式，表面上就没有任何的执行，所以就实现了停顿的效果

![[00 assets/73702f8960289d124b6438f07f199ed2_MD5.png]]

```html
/* HTML代码 */
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="./css/webpack动画.css" />
  </head>
  <body>
    <div class="main">
      <div class="inner">
        <div class="item top"></div>
        <div class="item bottom"></div>
        <div class="item front"></div>
        <div class="item back"></div>
        <div class="item right"></div>
        <div class="item left"></div>
      </div>

      <div class="outer">
        <div class="item top"></div>
        <div class="item bottom"></div>
        <div class="item front"></div>
        <div class="item back"></div>
        <div class="item right"></div>
        <div class="item left"></div>
      </div>
    </div>
  </body>
</html>
```

```css
/* CSS代码 */
body {
  margin: 0;
  padding: 0;
  background: url("../image/grid.png");
}
.main {
  width: 200px;
  height: 200px;

  position: relative;
  left: 0;
  top: 0;

  margin-left: 200px;
  margin-top: 200px;
}

.inner {
  position: absolute;

  margin-left: 24px;
  margin-top: 24px;

  width: 50px;
  height: 50px;

  transform: rotateX(-33.5deg) rotateY(45deg);
  transform-style: preserve-3d;

  animation: inner-loop 6000ms ease-in-out infinite;
}
.outer {
  position: absolute;

  width: 100px;
  height: 100px;

  transform: rotateX(-33.5deg) rotateY(45deg);
  transform-style: preserve-3d;

  animation: outer-loop 6000ms ease-in-out infinite;
}
@keyframes inner-loop {
  0% {
    transform: rotateX(-33.5deg) rotateY(45deg);
  }
  50%,
  100% {
    transform: rotateX(-33.5deg) rotateY(-315deg);
  }
}
@keyframes outer-loop {
  0% {
    transform: rotateX(-33.5deg) rotateY(45deg);
  }
  50%,
  100% {
    transform: rotateX(-33.5deg) rotateY(405deg);
  }
}

.item {
  position: absolute;
  left: 0px;
  top: 0px;

  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}
/* 内部 */
.inner .item {
  background-color: #175d96;
  border: 1px solid white;
}
.inner .top {
  transform: rotateX(90deg) translateZ(25px);
}
.inner .bottom {
  transform: rotateX(-90deg) translateZ(25px);
}
.inner .front {
  transform: translateZ(25px);
}
.inner .back {
  transform: rotateY(180deg) translateZ(25px);
}
.inner .right {
  transform: rotateY(90deg) translateZ(25px);
}
.inner .left {
  transform: rotateY(-90deg) translateZ(25px);
}

/* 外部 */
.outer .item {
  background-color: rgba(141, 214, 249, 0.5);
  border: 1px solid white;
}
.outer .top {
  transform: rotateX(90deg) translateZ(50px);
}
.outer .bottom {
  transform: rotateX(-90deg) translateZ(50px);
}
.outer .front {
  transform: translateZ(50px);
}
.outer .back {
  transform: rotateY(180deg) translateZ(50px);
}
.outer .right {
  transform: rotateY(90deg) translateZ(50px);
}
.outer .left {
  transform: rotateY(-90deg) translateZ(50px);
}
```

### 3.8.5 2.5D 数据平台可视化 - keyframes 使用

![[00 assets/5d2dfdf6b71909c29233c786d6acdcdd_MD5.png]]

![[00 assets/0f9bc77cb0f6d9c06e6ae43f744f68c8_MD5.gif]]

> 停顿效果

1、这段动画的是想营造一种停顿的感觉

![[00 assets/d31e7fb3eb8a3eaed0da3b20460e9f40_MD5.png]]

![[00 assets/5fc1bb107f03d1d10f80e33e606a0f9f_MD5.png]]

> 循环效果

当动画执行到`50%`的时候，就会对比下一步的变化，而下一步就是`100%`，所以这个时候变化就是循环的

![[00 assets/46df30f8529d7d9236089debbc3cc772_MD5.png]]

![[00 assets/558fd8af70bde6c2d5416ff04b262882_MD5.png]]

> 关键帧

如果使用`keyframes`动画的话，就是帧动画。我们写一个`100%`的话就会保留`100%`这一帧，让这一帧多显示一会

![[00 assets/4254eacd83d485764f30c657e8b15eb9_MD5.png]]

# 4. 浏览器渲染原理

1、如果只是普通元素的话就是`标准流`

2、如果你开启了`定位......`之类的属性就会开启`渲染层`，我们编写动画最好就添加定位，这样可以就可以开启单独的渲染层，我们执行动画不会导致`回流`和`重绘`，提高了性能

3、如果我们使用`3d效果`的话就会开启`合成层`，会开启`gpt加速`，但是会导致内存使用过多

![[00 assets/dad5a49423531542e74cca5f54d8bf8d_MD5.png]]

4、下面设计开启`渲染层`和`合成层`的 CSS 属性

![[00 assets/731d67f33ebf49926b7a1dc2adda6358_MD5.png]]

5、我们使用了`css3d`之后会开启一个`合成层`

![[00 assets/fb3c9b567a81cb6ef7c70936af00d589_MD5.png]]

# 5. CSS3 动画对比 JS 动画

参考链接：[CSS 动画与 JavaScript 动画的性能 - Web 性能 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/Performance/CSS_JavaScript_animation_performance)

1、**CSS transition** 和 **CSS animation** 在性能上没有区别，都归类为基于 CSS 的动画

2、如果你将 **requestAnimationFrame()** 作为 JS 动画来使用的话，相比于 **setTimeout() 或 setInterval()** 会更加流畅

3、一般情况下 **CSS transition** 和 **requestAnimationFrame** 动画性能是一致的，除非我们将 JS 动画放进 **web worker** 中，这样就不会占用主线程了

![[00 assets/d20bb7c24cd122961d43400e9f4b9ad4_MD5.png]]

4、一般情况下还是优先选择 **CSS** 来做动画，因为他会单独设置一个 **layer**，那么就会在 GPU 中进行，并且不会导致重排 [[CSS3 动画#4. 浏览器渲染原理]]

5、我也单独封装了一个 **requestAnimationFrame** 的 hook 函数来流程的执行动画 [[requestAnimationFrame]]

6、但是我们使用 JS 来实现会导致主线程重新回流重绘，也不一定比CSS动画更好
