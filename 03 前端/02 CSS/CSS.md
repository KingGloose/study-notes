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

# 11 Flex

[[Flex]]

# 12 Grid

[[Grid]]

# 13 媒体查询

[[媒体查询]]

# 14 CSS工程化

有的人可能会问，书写 *CSS* 也会涉及到工程化的内容么？如果你只是单纯的书写原生的 *CSS*，那么确实不能够称之为工程化，但是现在书写 *CSS* 也没有那么简单了，多了很多事情要做。*CSS* 工程化主要体现在以下几个方面：

>模块化

模块化是将 *CSS* 代码分解成独立的、可重用的模块，从而提高代码的可维护性和可读性。通常，每个模块都关注一个特定的功能或组件的样式。这有助于减少样式之间的依赖和冲突，也使得找到和修改相关样式变得更容易。模块化的实现可以通过原生的 *CSS* 文件拆分，或使用预处理器（如 *Sass*）的功能（例如 @*import* 和 @*use*）来实现。

>命名规范：

为 *CSS* 类名和选择器定义一致的命名规范有助于提高代码的可读性和可维护性。以下是一些常见的命名规范：

*BEM*（*Block*, *Element*, *Modifier*）：*BEM* 是一种命名规范，将类名分为三个部分：块（*Block*）、元素（*Element*）和修饰符（*Modifier*）。这种方法有助于表示组件之间的层级关系和状态变化。例如，*navigation__link--active*。

*OOCSS*（面向对象的 *CSS*）：*OOCSS* 旨在将可重用的样式划分为独立的“对象”，从而提高代码的可维护性和可扩展性。这种方法强调将结构（如布局）与皮肤（如颜色和字体样式）分离。这样可以让你更容易地复用和组合样式，创建更灵活的 UI 组件。

```html
<button class="btn btn--primary">Primary Button</button>
<button class="btn btn--secondary">Secondary Button</button>
```

```css
/* 结构样式 */
.btn {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

/* 皮肤样式 */
.btn--primary {
  background-color: blue;
  color: white;
}

.btn--secondary {
  background-color: gray;
  color: white;
}
```

*SMACSS*（可扩展和模块化的 *CSS* 架构）：是一种 *CSS* 编写方法，旨在提高 *CSS* 代码的可维护性、可扩展性和灵活性。*SMACSS* 将样式分为五个基本类别：*Base、Layout、Module、State* 和 *Theme*。这有助于组织 *CSS* 代码并使其易于理解和修改。

- *Base*：包含全局样式和元素默认样式，例如：浏览器重置、全局字体设置等。
- *Layout*：描述页面布局的大致结构，例如：页面分区、网格系统等。
- *Module*：表示可重用的 *UI* 组件，例如：按钮、卡片、表单等。
- *State*：表示 *UI* 组件的状态，例如：激活、禁用、隐藏等。通常，状态类会与其他类一起使用以修改其显示。
- *Theme*：表示 *UI* 组件的视觉样式，例如：颜色、字体等。通常，主题类用于支持多个主题或在不同上下文中使用相同的组件。

>预处理器

*CSS* 预处理器（如 *Sass、Less* 和 *Stylus*）是一种编程式的 *CSS* 语言，可以在开发过程中提供更高级的功能，如变量、嵌套、函数和混合等。预处理器将这些扩展语法编译为普通的 *CSS* 代码，以便浏览器能够解析。

>后处理器

*CSS* 后处理器（如 *PostCSS*）可以在生成的 *CSS* 代码上执行各种操作，如添加浏览器前缀、优化规则和转换现代 *CSS* 功能以兼容旧浏览器等。它通常与构建工具（例如 *Webpack*）一起使用，以自动化这些任务。

>代码优化

代码优化旨在减少 *CSS* 文件的大小、删除无用代码和提高性能。一些常见的优化工具包括：
- *CSSO*：*CSSO* 是一个 *CSS* 优化工具，可以压缩代码、删除冗余规则和合并相似的声明。
- *PurgeCSS*：*PurgeCSS* 是一个用于删除无用 *CSS* 规则的工具。它通过分析项目的 *HTML、JS* 和模板文件来检测实际使用的样式，并删除未使用的样式。
- *clean-css*：*clean-css* 是一个高效的 *CSS* 压缩工具，可以删除空格、注释和重复的规则等，以减小文件大小。

>版本控制

使用版本控制系统（如 *Git*）可以更好地管理 *CSS* 代码的变更历史、合并冲突和多人协作。此外，它还可以帮助您快速回溯到以前的版本，以便排查和修复问题。

>构建工具和自动化

构建工具（如 *Webpack*、*Gulp* 或 *Grunt*）可以帮助您自动化开发过程中的任务，如编译预处理器代码、合并和压缩 *CSS* 文件、优化图片等。这可以提高开发效率，确保项目的一致性，并简化部署流程。这些工具通常可以通过插件和配置来定制，以满足项目的特定需求。

>响应式设计和移动优先

响应式设计是一种使网站在不同设备和屏幕尺寸上都能保持良好显示效果的方法。这通常通过使用媒体查询、弹性布局（如 *Flexbox* 和 *CSS Grid*）和其他技术实现。移动优先策略是从最小屏幕尺寸（如手机）开始设计样式，然后逐步增强以适应更大的屏幕尺寸（如平板和桌面）。这种方法有助于保持代码的简洁性，并确保网站在移动设备上的性能优先。

>设计系统和组件库

设计系统是一套规范，为开发人员和设计师提供统一的样式指南（如颜色、排版、间距等）、组件库和最佳实践。这有助于提高项目的一致性、可维护性和协作效率。组件库通常包含一系列预定义的可复用组件（如按钮、输入框、卡片等），可以快速集成到项目中。一些流行的组件库和 *UI* 框架包括 *Bootstrap、Foundation* 和 *Material-UI* 等。

因此整个 CSS 都是逐渐在向工程化靠近的，上面所罗列的那么几点都是 CSS 在工程化方面的一些体现。




