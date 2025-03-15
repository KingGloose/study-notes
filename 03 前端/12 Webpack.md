视频讲解：[尚硅谷 2022 版 Webpack5 入门到原理（面试开发一条龙）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV14T4y1z7sw?p=4&spm_id_from=pageDriver)

视频讲解：前端系统课 - coderwhy - webpack

# 1. 基本介绍

> 基本作用

![[00 assets/1afb546f4ff9d3b6722cc6087e175a3a_MD5.png]]

> 使用 webpack 原因

开发时，我们会使用框架（React、Vue）、ES6 模块化语法、Less/Sass 等 css 预处理器等语法进行开发。这样的代码要想在浏览器运行必须经过编译成浏览器能识别的 JS、CSS 等语法，才能运行。所以我们需要打包工具帮我们做完这些事。除此之外，打包工具还能压缩代码、做兼容性处理、提升代码性能等。

![[00 assets/5fe5367239728e2f973f364e52162ced_MD5.png]]

> 其他打包工具

目前市面上最流量的是 Webpack，所以我们主要以 Webpack 来介绍使用打包工具

目前的打包工具：Grunt、Gulp、Parcel、Webpack、Rollup、Vite、...

> 基本介绍

![[00 assets/db2ea5bb2148bb2ebf2a32799259374d_MD5.png]]

> webpack 依赖图

![[00 assets/a28c7a28641f1c15e9e12674f5ec8327_MD5.png]]

# 2. 基本使用

## 2.1 安装

1、我们安装`webpack`会下载下面的 2 个版本，其中一个就是`webpack`，我们可以使用`require("webpack")`导出，然后使用`webpack.complie()`来编译搭建，将要编译的文件传入进去即可

2、但是现在的构建方式不是这样的，主要是通过命令行来处理，所以就需要下载`webpack-cli`

3、而且下载的话也是进行`局部下载 -D`，因为各个项目的配置都不一样，所以各个项目使用不同配置的`webpack`

![[00 assets/577ab8fb19b59c3d2fcfb46e154f29c1_MD5.png]]

## 2.2 使用

![[00 assets/ce1cf6ff0ee70baa662ceb8fb7e4d1f7_MD5.png]]

1、我们使用`npx webpack`的时候，默认会寻找文件夹`src`下面的`index.js`，然后进行打包处理，最后生成的文件会传入到`dist`中

![[00 assets/f5ebc60c221c36545318f43582781366_MD5.png]]

2、当然我们也可以在命令行中输入一些参数，很显然这样操作非常的麻烦，所以就需要`webpack配置`

![[00 assets/5f6f4273bbc2aa969181f669e460b489_MD5.png]]

## 2.3 基本配置

1、对于`基本使用`中命令行需要输入多个参数麻烦的问题，我们可以创建一个`webpack.config.js`文件来编写你的配置属性

2、其中一一对应的就是`--entry、--output-filename、--output-path`的属性

![[00 assets/599919089bcf31f04a7329a5cb8c128e_MD5.png]]

2、`webpack`默认读取的文件名是`webpack.config.js`，假如我们修改了`webpack.config.json`文件名，就需要额外添加配置文件名

![[00 assets/9d38ca1405320203046493a845b744ec_MD5.png]]

3、但是使用这样的方式还是比较麻烦，我们就可以将`webpack`的参数传输给`包管理工具npm`来处理。假如没使用`npm init`初始化的包是不包含需要的属性的，所以在这之前可以使用`npm init`来初始化

![[00 assets/dd91f8c7d30d7e824cbe96b92451dbeb_MD5.png]]

按照下面的配置输入`npm run build`即可执行输入好的命令，

![[00 assets/f910e1f42418f65e1c04245dcacbbcde_MD5.png]]

4、下面就是基本的配置属性

```javascript
// 1.entry（入口）：指示Webpack从哪个文件开始打包
// 2.output（输出）：指示Webpack打包完的文件输出到哪里去，如何命名等
// 3.loader（加载器）webpack本身只能处理 js、json 等资源，其他资源需要借助 oader，Webpack才能解析
// 4.plugins（插件）：扩展Webpack的功能
// 5.mode（模式）：主要由两种模式：开发模式：development、生产模式：production


const path = require("path"); // node.js核心模块，专门用于处理路径问题

module.exports = {
  // 入口
  entry: "./src/main.js", // 相对路径
  // 输出
  output: {
    // 文件输出路径
    // __dirname node.js变量，代表当前文件的文件夹目录
    // __dirname表示的是hello文件夹，后面的dist是hello文件夹里面的dist
    path: path.resolve(__dirname, "dist"), // 绝对路径
    //文件名
    filename: "main.js",
  },
  // 加载器
  module: {
    rules: [
      // loader的配置
    ],
  },
  // 插件
  plugins: [
     // plugin的配置
  ],
  // 模式
  mode: "production",
};
```

# 3. 资源处理

## 3.1 样式处理

### 3.1.1 基本介绍

1、`Webpack`本身是不能识别样式资源的，如果我们在`.js`里面引入样式文件，就会报下面的错误

![[00 assets/74ecc8adc305fff988ba57bf268d3f01_MD5.png]]

### 3.1.2 css-loader

1、所以我们就需要使用`loader`来处理`webpack`不能打包的文件

![[00 assets/291210827a2040858690423f3602838e_MD5.png]]

2、对于`css-loader`存在下面的方式来处理，现在基本都是使用`配置方式`来处理样式文件

![[00 assets/21f49c10ea37849f724df7cf2bf3d56a_MD5.png]]

3、下面就是配置`CSS-loader`，配置完毕就可以打包`样式文件`了

![[00 assets/f6ce2ade6e116dabdf3633c7ce345b6d_MD5.png]]

![[00 assets/572c27066586650c086474dd5961c001_MD5.png]]

### 3.1.3 style-loader

1、对于`css-loader`只能加载解析`CSS`，但是我们需要将`CSS`加载到`index.html`中

![[00 assets/697563fd8c832c176cf752640fcce753_MD5.png]]

2、我们下载`style-loader`，然后再该`rules`中配置`style-loader`即可，并且执行的顺序是从右向左处理

![[00 assets/67af68a959cda2b24c70f70d8a37ab80_MD5.png]]

### 3.1.4 处理 CSS 文件

```bash
pnpm i css-loader style-loader	// 下载css-loader、style-loader
```

1、下面就是相应的`CSS`配置处理

```javascript
const path = require("path"); // node.js核心模块，专门用于处理路径问题

module.exports = {
  entry: "./src/main.js", // 相对路径 // 入口
  output: {	 // 输出
    // 文件输出路径
    // __dirname node.js变量，代表当前文件的文件夹目录
    // __dirname 表示的是hello文件夹，后面的dist是hello文件夹里面的dist
    path: path.resolve(__dirname, "dist"), // 绝对路径
    filename: "main.js", //文件名
  },
  module: {  //加载器
    rules: [ //loader的配置
      {
        test: /\.css$/, //检测以css结尾的文件
        //执行的顺序从下到上(从右向左)
        use: [
           // 会动态创建一个 Style 标签，里面放置 Webpack 中 Css 模块内容
           "style-loader",
           // 将css编译为common.js的模块放在js中
           "css-loader"
         ],
      },
    ],
  },
  plugins: [ // 插件 //plugin的配置 ],
  mode: "production", //模式
};
```

![[00 assets/c09a3c3e937c6291434e6926a3a1e898_MD5.png]]

2、我们需要引入`样式文件`才能被`webpack`打包处理，这里可以参考`webpack依赖图`

![[00 assets/539a07c249cb7e4fbd1c7052089220a0_MD5.png]]

3、我们再手动引入打包好的`css`文件即可，后面会有`webpack`插件会自动引入`script`

![[00 assets/0bbc20485cf857cf5d8619aba05db0c3_MD5.png]]

### 3.1.5 处理其他样式

```
// less
pnpm i less				//下载less
pnpm i less-loader -D	//下载less-loader，负责将less文件编译为css

// sass
pnpm i sass
pnpm add sass-loader

// stylus
pnpm i stylus			//下载stylus
pnpm i stylus-loader -D	//下载stylus-loader
```

根据样式处理的模式可以总结为：`创建样式 -> 引入样式 -> 下载loader -> 写入规则 -> 打包`

```javascript
const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./build"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      // 处理css
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      // 处理less
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      // 处理sass
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      // 处理stylus
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
    ],
  },
};

```

### 3.1.6 postcss 处理

![[00 assets/bba3b187788597ff6dcf0d2ce0e56444_MD5.png]]

1、下面就是`postcss`在`webpack`中的配置，并且`postcss`只是一个现代化工具，我们需要安装相应的插件才可以实现相应的功能，比如下面的`autoprefixer`会为属性添加浏览器前缀

并且下载的时候需要注意开发依赖和生产依赖，各个版本不是相互对应的

```bash
pnpm add postcss-loader autoprefixer -D	// 安装postcss autoprefixer
```

![[00 assets/937c15562f8d889ba425c4b9ccb6d48a_MD5.png]]

这样就可以为属性添加浏览器前缀，减小兼容性的问题

![[00 assets/6dbe1a2eba2558a501f610389aa9740a_MD5.png]]

2、我们创建一个`postcss.config.js`作为`postcss`的配置文件，这样我们可以直接写`post-loader`即可

![[00 assets/3398d88342c6eb4004188d205b810354_MD5.png]]

这样我们就有很好的扩展性，不用每次都写这么多的配置

![[00 assets/9042835f79682eb9076f80d868905d45_MD5.png]]

3、其实`postcss-preset-env`就是一个`postcss`的集大成者，里面包含了很多的处理插件，这样我们就不需要一个个下载了

![[00 assets/56fa338be3f83e1690fbcaced5618a3f_MD5.png]]

和`autoprefixer`的使用方式一样即可

![[00 assets/fbf7aed6133007270793d4ddb0154fda_MD5.png]]

## 3.2 图片处理

### 3.2.1 基本使用

![[00 assets/17160edc1859226b0338054d8443f719_MD5.png]]

我们按照下面的配置即可对静态资源进行打包

![[00 assets/1ea0eaaa2dded8dce2dba64c4b374166_MD5.png]]

我们导入的话，就会进入到`webpack`的依赖图中，这样`webpack`就会对静态文件进行打包

![[00 assets/22350d0c4dacfe73aa9f5c14b330382a_MD5.png]]

> asset

### 3.2.2 资源模块类型

> asset/resource

1、`webpack`会对`img`进行打包，复制图片并且对其进行哈希命名

![[00 assets/59515524e15f26421a1e94ad7b041cc2_MD5.png]]

2、在`bundle.js`文件中创建该图片的地址，并写入引入的元素中

![[00 assets/82b99b727d037f9e46877b96a9382315_MD5.png]]

> asset/inline

这个会对资源进行`Base64`的编码，并且将编码后的源码放入到打包的`.js`文件中

![[00 assets/9a5bf8b2d5bfdfd5410c6b3f41c21199_MD5.png]]

![[00 assets/2c30a2bb0e07c9a938d48c929b735676_MD5.png]]

> asset

1、但是对于上面 2 种极端都是不行的，使用`asset/resource`的话，会打包很多的`img`文件，这样`http请求`就会变多。如果打包为`asset/inline`的话，就会造成`.js`文件变得很大，导致加载变慢

![[00 assets/6766791ae848db7dbf1a488a7de9cda2_MD5.png]]

所以就存在下面得打包方式，当资源没达到一定得大小，就打包到`.js`中。

![[00 assets/82b99b727d037f9e46877b96a9382315_MD5.png]]

2、并且这个打包资源也可以修改输出名称

![[00 assets/5db578e933e81dc3f2d471cb08e0f5ac_MD5.png]]

![[00 assets/f2138dcdb0ed094a82d96ba96261ee10_MD5.png]]

## 3.3 JS 处理

### 3.3.1 babel

#### 3.3.1.1 基本介绍

![[00 assets/7d23d6f4e9d3dc43070b18091340d65c_MD5.png]]

#### 3.3.1.2 命令行使用

真实开发很少使用这个来处理，大部分情况还是配合`webpack`来使用

> Babel 命令行使用

![[00 assets/efcba8c303d62acc22cc654bb3288148_MD5.png]]

![[00 assets/ff3a94019033751cbe1c060bbc638617_MD5.png]]

> 插件的使用

![[00 assets/82b99b727d037f9e46877b96a9382315_MD5.png]]

> Babel 的预设 preset

![[00 assets/87cedb614064c0c5ec8b9c289631ba0a_MD5.png]]

如果是做预设 `preset` 的话，还有 `StageX` 得 `preset`

![[00 assets/58612c6213dd1ec44ca4254183a23e80_MD5.png]]

#### 3.3.1.3 底层原理

![[00 assets/f14c85f3a8304d0a91d4a6fca11a4558_MD5.png]]

![[00 assets/51a43d1e2ef44e3c9236b1134993bf84_MD5.png]]

#### 3.3.1.4 配合 webpack

1、只要是和`webpack`使用，并且要触发某一个转化的情况下，都需要安装`loader`

![[00 assets/dae63c8d98dabd44c3f1e51cee77773b_MD5.png]]

2、因为这个是配合`webpack`使用，所以没有使用`命令行`就不需要安装`@babel/cli`

```bash
pnpm add babel-loader @babel/core @babel/plugin-transform-arrow-functions @babel/plugin-transform-block-scoping -D  // 安装
```

![[00 assets/684f5d8ac176e2bcd8774508c321fbaa_MD5.png]]

> babel.config.js

1、如果按照上面得方式有很多得选项，所以我们可以抽取到`babel.config.js`中，这个和`postcss.config.js`类似

![[00 assets/5720440fddd8ad4b56b0e19d561a01d8_MD5.png]]

> babel-preset

![[00 assets/2c30a2bb0e07c9a938d48c929b735676_MD5.png]]

1、我们不可能一个个来配置`babel`的插件，所以也可以和上面一样将`presets`预设配置到`babel.config.js`中

```bash
pnpm add @babel/preset-env -D
```

![[00 assets/25d99096b3834c7d403a6e49e2ad2e75_MD5.png]]

2、上面的写法只是一种可维护的写法，如果配置比较简单可以使用下面的方式

![[00 assets/6cd79b940930a58d1ca8b3053bc41dfb_MD5.png]]

## 3.4 Vue 处理

```bash
pnpm add vue-loader -D
pnpm add vue
```

对于`Vue`来说使用`vue-loader`来处理，但是对于这个`loader`需要额外引入`VueLoaderPlugin`

![[00 assets/06b6fa31a2db2d59a96da38dbae43ffd_MD5.png]]

其中`Vue`文件就是按照下面的方式来编写

![[00 assets/a1743aeaff4da44d09ceee9964424def_MD5.png]]

## 3.5 React 处理

1、我们需要安装 React 得依赖

```
pnpm add react react-dom
```

# 4. 配置选项

## 4.1 resolve 模块

> resolve 模块解析

![[00 assets/981632cc39d715db5c600c31fbc1eab3_MD5.png]]

> 确定文件

对于文件来说，我们每次引入`.js`的时候都是没有加`.js`后缀，这是因为`webpack`帮忙添加了

![[00 assets/f72488ca93ebe2c863746f2f5760dc7e_MD5.png]]

我们可以对引入文件添加后缀名称

![[00 assets/b92d15e1e3edabe6d947eb1a35ab7b86_MD5.png]]

我们手动编写了`extensions`的话，就不需要自己手动添加后缀名了

![[00 assets/6616ee8357e3072e99cd0bfc8e2bec24_MD5.png]]

> 确定文件夹

![[00 assets/e61e0f4a93e8a83db3d3b6f0c62a2180_MD5.png]]

我们按照下面的`alias`即可对文件夹进行别名设置，这样我们就不需要写很多的目录结构，使用`alias`别名即可

![[00 assets/b6bf52e1a00744861941f1623df53e73_MD5.png]]

## 4.2 mode 配置

![[00 assets/83accd791af2035e7b8229e2543fa6b1_MD5.png]]

![[00 assets/3713834dfba0ce6ee9516d15126b4c0e_MD5.png]]

如果我们开启相应的`mode模式`就会默认开启下面的优化模式

![[00 assets/30560b32b4a620217a951b07c4628fcb_MD5.png]]

# 5. 插件模式

## 5.1 基本介绍

![[00 assets/1d1ed55a6880cd0014ba8584de1104e2_MD5.png]]

## 5.2 CleanWebpackPlugin

![[00 assets/314e250a61ccc62a56d09caa24fcdcd5_MD5.png]]

## 5.3 HtmlWebpackPlugin

> 基本使用

![[00 assets/59951f79b1da6fb56bb05bdd9f471953_MD5.png]]

其实上面的`title`属性会填充到`html-webpack-plugin`中的`.ejs`中进行处理

![[00 assets/fcb1f2b391951eee0c3cf6c8ddd626cf_MD5.png]]

![[00 assets/d542590f3b0e26656361dd58f6b9d2e7_MD5.png]]

> 自定义 html 模板

![[00 assets/1019ac43f78b76985c264c97a2eb5a54_MD5.png]]

![[00 assets/a9f5f3a85001573d8ee77626c727f077_MD5.png]]

当然我们也可以自定义`html`模板，这样就可以针对性的生成 html

![[00 assets/24dcfe7ee0f8f32210a70d9bb4cf3bc4_MD5.png]]

## 5.4 DefinePlugin

1、我们在自定义`HTML模板`的时候存在`<%= BASE_URL %>`这样的模板，所以我们不能使用`HtmlWebpackPlugin`插件，这里`webpack`内置了该插件

![[00 assets/237471b3334bfbb51494434f5a1c0a86_MD5.png]]

2、按照下面的配置，不仅仅是可以编译`.html`中的数据，还可以为全局设置变量

![[00 assets/5b73b0f62a278cb1c4e24e066a850a92_MD5.png]]

![[00 assets/a7b8848f7e3086ee4a24387cec31b28e_MD5.png]]

# 6. 开发服务器

## 6.1 基本介绍

![[00 assets/f81bcd48d457e6eda0616d8658a04f55_MD5.png]]

## 6.2 webpack-dev-server

> 基本使用

![[00 assets/e9ed937e53878f68a40887ed1eaa6ebe_MD5.png]]

下载包之后直接使用`webpack serve`即可开启`webpack-dev-serve`插件的功能。如果需要额外配置的话，可以设置`devServer`来处理

![[00 assets/a493236e48d97cf5516295a63a9971b9_MD5.png]]

> devServer 配置

![[00 assets/9e1dd9beb8eaf31a5a6e09e30a2e9a2b_MD5.png]]

![[00 assets/4f8cacbf62ce4e8bdc96afaa2ff423b5_MD5.png]]

下面就是`devServer`的配置

![[00 assets/f81bcd48d457e6eda0616d8658a04f55_MD5.png]]

下面就是`Vue`中的配置

![[00 assets/a5cc1edbc360440a6a1b272a8a4a788d_MD5.png]]

![[00 assets/3ddeccdac02b8e301dbea97ba43f8f8c_MD5.png]]

![[00 assets/24dcfe7ee0f8f32210a70d9bb4cf3bc4_MD5.png]]

## 6.3 HotModuleReplacement

> 基本介绍

![[00 assets/237471b3334bfbb51494434f5a1c0a86_MD5.png]]

> 基本使用

![[00 assets/3092aee91fb3561364cc34511cd0994c_MD5.png]]

写入`hot`配置，这个时候我们`修改样式`的话，就不会重新整个页面打包

![[00 assets/90c45dbab077081dd33a94f1298d76bb_MD5.png]]

但是还是不支持`.js`。我们需要将热插拔的`.js`传入到`module.hot.accept()`中，首先就需要检查是否支持`module.hot`，假如支持得话我们就是使用热模块加载

![[00 assets/9ba6dc06fcc63ac13ea0f4e28791059e_MD5.png]]

> 框架 HMR

![[00 assets/7a559bed1eb44ae0d9bd7205409e14c7_MD5.png]]

# 7. 区分开发环境

## 7.1 基本介绍

![[00 assets/9f8a9d99b1af3449495d00e6d06afcd5_MD5.png]]

## 7.2 不同环境文件

`生产环境(production)`：标识项目已经上线了

`开发环境(development)`：自己编写代码时配置的环境

我们要区分开发模式和生产模式，就要将不同模式的配置文件进行分类

![[00 assets/2de4182e4a9a436f43cd88e6039f2612_MD5.png]]

然后先配置 webpack.dev.js 文件，也就是平时开发时候的模式

![[00 assets/cd9ac4a7e3234d54e67213af92d1af8b_MD5.png]]

![[00 assets/3ff6ca15961ed10ffa3195640e1562af_MD5.png]]

> 开发环境

```javascript
const path = require("path"); //node.js核心模块，专门用于处理路径问题
const ESLintPlugin = require("eslint-webpack-plugin"); //引入eslint
const HtmlWebpackPlugin = require("html-webpack-plugin"); //引入Html文件打包

module.exports = {
  //入口
  entry: "./src/main.js", //相对路径
  //输出
  output: {
    path: undefined, // 开发模式没有输出，不需要指定输出目录
    //文件名
    filename: "./js/main.js",
    //自动清空上次打包的内容
    // clean: true, //当你配置了开发服务器的话，因为东西加载在内存，所以可以不要
  },
  //加载器
  module: {
    rules: [
      //loader的配置
      //css配置
      {
        test: /\.css$/, //检测以css结尾的文件
        //执行的顺序从下到上
        use: [
          //会动态创建一个 Style 标签，里面放置 Webpack 中 Css 模块内容
          "style-loader",
          //将css编译为common.js的模块放在js中
          "css-loader",
        ],
      },
      //less配置
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      //scss和sass配置
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      //stylus配置
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      //对图片进行Base64处理
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024, // 小于10kb的图片会被base64处理
          },
        },
        generator: {
          // 将图片文件输出到 static/imgs 目录中
          // 将图片文件命名 [hash:8][ext][query]
          // [hash:8]: hash值取8位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      //对于图标字体进行处理
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      //babel的配置
      {
        test: /\.js$/,
        exclude: /(node_modules)/, //表示排除
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  //插件
  plugins: [
    //plugin的配置
    new ESLintPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "../public/index.html"),
    }),
  ],
  // 开发服务器
  devServer: {
    host: "localhost", // 启动服务器域名
    port: "3000", // 启动服务器端口号
    open: true, // 是否自动打开浏览器
  },
  //模式
  mode: "development",
};
```

> 生产环境

```javascript
const path = require("path"); //node.js核心模块，专门用于处理路径问题
const ESLintPlugin = require("eslint-webpack-plugin"); //引入eslint
const HtmlWebpackPlugin = require("html-webpack-plugin"); //引入Html文件打包

module.exports = {
  //入口
  entry: "./src/main.js", //相对路径
  //输出
  output: {
    //文件输出路径
    //__dirname node.js变量，代表当前文件的文件夹目录
    //__dirname表示的是hello文件夹，后面的dist是hello文件夹里面的dist
    path: path.resolve(__dirname, "../dist"), // 生产模式需要输出
    //文件名
    filename: "./js/main.js",
    //自动清空上次打包的内容
    // clean: true, //当你配置了开发服务器的话，因为东西加载在内存，所以可以不要
  },
  //加载器
  module: {
    rules: [
      //loader的配置
      //css配置
      {
        test: /\.css$/, //检测以css结尾的文件
        //执行的顺序从下到上
        use: [
          //会动态创建一个 Style 标签，里面放置 Webpack 中 Css 模块内容
          "style-loader",
          //将css编译为common.js的模块放在js中
          "css-loader",
        ],
      },
      //less配置
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      //scss和sass配置
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      //stylus配置
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      //对图片进行Base64处理
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024, // 小于10kb的图片会被base64处理
          },
        },
        generator: {
          // 将图片文件输出到 static/imgs 目录中
          // 将图片文件命名 [hash:8][ext][query]
          // [hash:8]: hash值取8位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      //对于图标字体进行处理
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      //babel的配置
      {
        test: /\.js$/,
        exclude: /(node_modules)/, //表示排除
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  //插件
  plugins: [
    //plugin的配置
    new ESLintPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "src"),
    }),
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "public/index.html"),
    }),
  ],
  // 开发服务器
  // devServer: {
  //   host: "localhost", // 启动服务器域名
  //   port: "3000", // 启动服务器端口号
  //   open: true, // 是否自动打开浏览器
  // },
  //模式
  mode: "development",
};
```

## 7.3 配置运行指令

我们再来运行生产模式的代码，前面表示允许里面的开发服务器，`--config`后面的表示指定开发文件的目录

```bash
npx webpack serve --config ./config/webpack.dev.config.js		// 开发环境
npx webpack --config ./config/webpack.prod.config.js			// 生产环境
```

为了方便运行不同模式的指令，我们将指令定义在 package.json 中 scripts 里面

![[00 assets/71a6b8cfd472b7af6d68d9902a8c1ca6_MD5.png]]

以后启动指令：

- 开发模式：`npm start` 或 `npm run serve`
- 生产模式：`npm run build`

## 7.4 路径问题

![[00 assets/8e482c4e6b327b8b247aff81b505abbb_MD5.png]]

其中就存在`context`属性来指定路径，并且该属性只为`入口文件`、`加载器`和`插件`使用，这些地方默认就是项目根路径，而`output`、`alias`就是真实路径了

![[00 assets/7b0cf1f9af7de11bdf2c6d1326c068a7_MD5.png]]

## 7.5 抽取公共配置

```bash
pnpm add webpack-merge -D
```

将公共的配置都抽取到`common.config.js`中，然后通过`webpack-merge`来合并处理

![[00 assets/ca886ee4a3479a96dde926bbf98b83c8_MD5.png]]

对于`production`也是一样的处理方式，这样会让配置更加清晰

![[00 assets/724a1832447c898002f6714074cceb8e_MD5.png]]

# 8. source-map

## 8.1 基本介绍

![[00 assets/e79f3e75621f4661b398e33f92d79f1b_MD5.png]]

![[00 assets/b39cfae46b0b3c2de459fe984bd8c298_MD5.png]]

1、我们编写了下面的这一段代码，然后使用`webpack`的不同模式进行打包处理，也就是`development`和`production`，最后打包出来的结果也不一样，而且最后的报错信息也不一样

```javascript
let num = 1;
console.log(num++);

console.log(count); // 报错

function sayHello() {
  console.log("Hello~");
}
sayHello();
```

![[00 assets/ce94a879bab2a99a7d77198dbbb229a5_MD5.png]]

而且查看浏览器报错信息的时候，可以发现使用`development`打包的代码最后竟然有源码信息

![[00 assets/f083da941a6c5140e24d439e5cd0f633_MD5.png]]

我们点击之后竟然可以还原为之前的代码，这个就是`source-map`

![[00 assets/d8bc770e1b0842839db56ab697ed75ca_MD5.png]]

2、如果我们提高代码的复杂程度，其实最终的还原代码其实不是很完全

![[00 assets/5b73b0f62a278cb1c4e24e066a850a92_MD5.png]]

最终报错他提示在`14行`中，而实际情况是在第`9行`中，这是因为`devtool`设置为`eval`，该模式下精度没有那么高，但是他的好处就是比较快，适用于开发时使用

![[00 assets/e81cf67d6992b192a2a3664f59d0750f_MD5.png]]

3、而且一定要注意一个地方就是最后依赖的代码只有`build.js`，而最后的错误信息的提示则是浏览器通过`source-map`技术还原出来的

![[00 assets/03402b05be41dddab4b22895f18e9296_MD5.png]]

## 8.2 基本使用

![[00 assets/572c27066586650c086474dd5961c001_MD5.png]]

我们将`devtool`换为`source-map`之后编译出来的为`.map`结尾的文件

![[00 assets/697563fd8c832c176cf752640fcce753_MD5.png]]

1、生成的`.map`文件就是高精度的`source-map`文件

![[00 assets/a5cc1edbc360440a6a1b272a8a4a788d_MD5.png]]

我们查看对应的错误就可以发现，精度高了很多

![[00 assets/454f1766694a0812e68d8e6100cd02ef_MD5.png]]

![[00 assets/cea27dd79ac776fcfa8f2004ba3422c0_MD5.png]]

2、但是这个模式有一个缺点就是生成的速度比较慢，所以大部分都是在`production`中开启这个模式

3、而且在不同的`mode`下开启`source-map`模式生成的文件都不一样

![[00 assets/9d4bdc279ddcf9dbfb830ef46f3b5072_MD5.png]]

因为对于`development`模式下有很多其他的处理，而最后编译出来的`source-map`也不一样

![[00 assets/291210827a2040858690423f3602838e_MD5.png]]

而`production`则去除了很多的东西

![[00 assets/786010680cd1f0cbbdd5037ce17c205c_MD5.png]]

4、对于`//# sourceMappingURL=build.js.map`的注释，这个其实是给`浏览器`处理的，如果浏览器看到这个注释就会自动的请求`map`文件

![[00 assets/555331cc720a0687db29676e32bbfaf8_MD5.png]]

## 8.2 source-map 属性说明

![[00 assets/be41594dbbdc245320f13261e67ca9fc_MD5.png]]

![[00 assets/57b2db10a75c35f5d070ffb8a8d8540f_MD5.png]]

## 8.3 devtool 属性值

![[00 assets/5d852d7e470aa2a40004f372dba37801_MD5.png]]

1、也就是这个值的输入，如果想查看对应的值的区别可以查看官网：[Devtool | webpack 中文文档 (docschina.org)](https://webpack.docschina.org/configuration/devtool/#root)

![[00 assets/521e469e6583a039ac50076511516a3c_MD5.png]]

> eval

1、`开发(development)`时使用比较多，其特点就是生成速度比较快，而且有错误信息提示，但是精度不是很高

![[00 assets/965bab44895130c07e6decb01b8d2b83_MD5.png]]

> eval-source-map

1、也就是将`source-map`作为`Base64`的形式写入`.js`中

![[00 assets/539a07c249cb7e4fbd1c7052089220a0_MD5.png]]

> inline-source-map

![[00 assets/a370ddace24849e3d8216c78c6a441ca_MD5.png]]

> cheap-source-map

![[00 assets/91bfad546c90192ed58226c042fc7bba_MD5.png]]

> cheap-module-source-map

![[00 assets/2be30983c2fd29c21d8de47170391725_MD5.png]]

![[00 assets/4ad50ec640d4d71fda8f901c0d6df773_MD5.png]]

> hidden-source-map

![[00 assets/c4fee816bba5c0e4e8f8543fe9ece992_MD5.png]]

> nosources-source-map

![[00 assets/833c652d4cacdf0b9cc2bed50fd1f821_MD5.png]]

> 多个值的组合

![[00 assets/2495430ef528e6e1e2efbf5326cf4260_MD5.png]]

# 9. babel

## 9.1 基础配置

这段内容参考`3.3.1 babel`的笔记

## 9.2 browserslist

### 9.2.1 基本介绍

> 基本介绍

![[00 assets/31dd20867cff2e5538c7d060a7e2ebb7_MD5.png]]

![[00 assets/db045ef2e7738c6eacf5243c3f9e622c_MD5.png]]

> 认识 browserslist

![[00 assets/5db578e933e81dc3f2d471cb08e0f5ac_MD5.png]]

> 浏览器查询

![[00 assets/188c42c4ee0668c47e69c69f044b77b8_MD5.png]]

### 9.2.2 常见配置

![[00 assets/cb3df907f1c4b8d51ed8fbb9ed748e60_MD5.png]]

![[00 assets/965bab44895130c07e6decb01b8d2b83_MD5.png]]

### 9.2.3 基本使用

> 命令行使用

![[00 assets/47678e11e6994a4eb547f295a6ddb053_MD5.png]]

> 配置 browserslist

![[00 assets/8b28501be2ff8e3a55029af8d37ba524_MD5.png]]

上面是比较常见得方式，我们还可以在 `webpack.config.js` 中得 `presets` 中去做对应得配置，但是不是很常见，不是很推荐这样来做

![[00 assets/efefc0068f8b48af28e7dd3d93672480_MD5.png]]

> 默认配置和条件关系

![[00 assets/90d9dbff73d73a19e5f8415169676d51_MD5.png]]

## 9.3 配置文件

![[00 assets/2ca6c6a2d0a9fc2714a7625bff7857e0_MD5.png]]

# 10. polyfill

## 10.1 基本介绍

![[00 assets/8780025a025ec26313a6cd4d488d3df0_MD5.png]]

## 10.2 基本使用

![[00 assets/f8ad153627029b527f27989e7b67a8bf_MD5.png]]

1、目前大部分都是 **babel7**，所以我这里就安装 **corejs** 和 **regenerator-runtime** 这 2 个包

2、我们这里来做一些配置， corejs 设置为 3，同时 useBuiltIns 设置为 **false**，表示 **polyfill** 失效

![[00 assets/a53c1b434a95414b2e5407d1b2f01ce9_MD5.png]]

3、 除了 **false** 还有其他得属性 **usage** 和 **entry**

![[00 assets/d60448188c5bf49f3b298342166cf97f_MD5.png]]
![[00 assets/101bf75707f75234b57655aa8fe66406_MD5.png]]

4、一般情况是使用 **usage**，因为会引入最少得 polyfill 来完成打包

5、如果你要是有 enrty 的话，这种情况是你使用了第三方得包，那么就需要手动在入口文件引入文件

![[00 assets/a74b1214e2cabd46d074fa7768f7d703_MD5.png]]

# 2. webpack 使用

## 2.5 修改输出文件目录

我们写入规则的话，就可以规定资源文件输入的的目录

```javascript
const path = require("path");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js", // 将 js 文件输出到 static/js 目录中
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024, // 小于10kb的图片会被base64处理
          },
        },
        generator: {
          // 将图片文件输出到 static/imgs 目录中
          // 将图片文件命名 [hash:8][ext][query]
          // [hash:8]: hash值取8位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
    ],
  },
  plugins: [],
  mode: "development",
};
```

## 2.6 自动清空上次打包的内容

写入规则

```javascript
const path = require("path");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js",
    clean: true, // 自动将上次打包目录资源清空
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 40 * 1024,
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
    ],
  },
  plugins: [],
  mode: "development",
};
```

## 2.7 处理字体图标资源

写入配置

```javascript
const path = require("path");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024,
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
      //字体文件的配置
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
    ],
  },
  plugins: [],
  mode: "development",
};
```

先去下载字体文件，然后再去使用，然后`npx webpack`就可以了

## 2.8 处理其他资源

就是在处理字体图标资源基础上增加其他文件类型，统一处理即可

```javascript
const path = require("path");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024, // 小于10kb的图片会被base64处理
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
        //在这个位置加就可以了
      {
        test: /\.(ttf|woff2?|map4|map3|avi)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
    ],
  },
  plugins: [],
  mode: "development",
};
```

## 2.9 处理 JS 资源

有人可能会问，js 资源 Webpack 不能已经处理了吗，为什么我们还要处理呢？

原因是 Webpack 对 js 处理是有限的，只能编译 js 中 ES 模块化语法，不能编译其他语法，导致 js 不能在 IE 等浏览器运行，所以我们希望做一些兼容性处理。

其次开发中，团队对代码格式是有严格要求的，我们不能由肉眼去检测代码格式，需要使用专业的工具来检测。

- 针对 js 兼容性处理，我们使用 Babel 来完成
- 针对代码格式，我们使用 Eslint 来完成

我们先完成 Eslint，检测代码格式无误后，在由 Babel 做代码兼容性处理

### 2.9.1 Eslint

可组装的 JavaScript 和 JSX 检查工具。

这句话意思就是：它是用来检测 js 和 jsx 语法的工具，可以配置各项功能

我们使用 Eslint，关键是写 Eslint 配置文件，里面写上各种 rules 规则，将来运行 Eslint 时就会以写的规则对代码进行检查

#### 2.9.1.1 配置文件

配置文件由很多种写法：

- `.eslintrc.*`：新建文件，位于项目根目录
  - `.eslintrc`
  - `.eslintrc.js`
  - `.eslintrc.json`
  - 区别在于配置格式不一样
- `package.json` 中 `eslintConfig`：不需要创建文件，在原有文件基础上写

ESLint 会查找和自动读取它们，所以以上配置文件只需要存在一个即可

#### 2.9.1.2 具体配置

我们以 `.eslintrc.js` 配置文件为例：

```javascript
module.exports = {
  // 解析选项
  parserOptions: {},
  // 具体检查规则
  rules: {},
  // 继承其他规则
  extends: [],
  // ...
  // 其他规则详见：https://eslint.bootcss.com/docs/user-guide/configuring
};
```

1.parserOptions 解析选项

```javascript
parserOptions: {
  ecmaVersion: 6, // ES 语法版本
  sourceType: "module", // ES 模块化
  ecmaFeatures: { // ES 其他特性
    jsx: true // 如果是 React 项目，就需要开启 jsx 语法
  }
}
```

2.rules 具体规则

- `"off"` 或 `0` - 关闭规则

- `"warn"` 或 `1` - 开启规则，使用警告级别的错误：`warn` (不会导致程序退出)

- `"error"` 或 `2` - 开启规则，使用错误级别的错误：`error` (当被触发的时候，程序会退出)

```javascript
 rules: {
   semi: "error", // 禁止使用分号
   'array-callback-return': 'warn', // 强制数组方法的回调函数中有 return 语句，否则警告
   'default-case': [
     'warn', // 要求 switch 语句中有 default 分支，否则警告
     { commentPattern: '^no default$' } // 允许在最后注释 no default, 就不会有警告了
   ],
   eqeqeq: [
     'warn', // 强制使用 === 和 !==，否则警告
     'smart' // https://eslint.bootcss.com/docs/rules/eqeqeq#smart 除了少数情况下不会有警告
   ],
 }
```

更多规则详见：[规则文档](https://eslint.bootcss.com/docs/rules/)

3.extends 继承

开发中一点点写 rules 规则太费劲了，所以有更好的办法，继承现有的规则。

现有以下较为有名的规则：

- [Eslint 官方的规则 open in new window](https://eslint.bootcss.com/docs/rules/)：`eslint:recommended`
- [Vue Cli 官方的规则 open in new window](https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-eslint)：`plugin:vue/essential`
- [React Cli 官方的规则 open in new window](https://github.com/facebook/create-react-app/tree/main/packages/eslint-config-react-app)：`react-app`

```javascript
// 例如在React项目中，我们可以这样写配置
module.exports = {
  extends: ["react-app"],
  rules: {
    // 我们的规则会覆盖掉react-app的规则
    // 所以想要修改规则直接改就是了
    eqeqeq: ["warn", "smart"],
  },
};
```

#### 2.9.1.3 在 webpack 中使用 eslint

1.下载 eslint

```
npm i eslint-webpack-plugin eslint -D
```

2.我们在根目录创建一个.eslintrc.js 文件，里面就是写我们的 eslint 文件的配置

![[00 assets/cae9e7990727570978a28b8251a3a365_MD5.png]]

```javascript
module.exports = {
  // 继承 Eslint 规则
  extends: ["eslint:recommended"],
  env: {
    node: true, // 启用node中全局变量
    browser: true, // 启用浏览器中全局变量
  },
  parserOptions: {
    ecmaVersion: 6,
    sourceType: "module",
  },
  rules: {
    "no-var": 2, // 不能使用 var 定义变量
  },
};
```

3.写入插件，并且引入 Eslint 插件

```javascript
const path = require("path");
//引入eslint插件
const ESLintWebpackPlugin = require("eslint-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024,
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
    ],
  },
  plugins: [
    //创建eslint插件
    new ESLintWebpackPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "src"),
    }),
  ],
  mode: "development",
};
```

这样我们的 eslint 的插件就是安装完毕了，假如我们不按照规则来执行的话就会报错

![[00 assets/be7f3cd5daaf01158e1ab4e01814adf6_MD5.png]]

打开 VSCode，下载 Eslint 插件，可以在不用编译就能看到错误，可以提前解决

但是此时就会对项目所有文件默认进行 Eslint 检查了，我们 dist 目录下的打包后文件就会报错。但是我们只需要检查 src 下面的文件，不需要检查 dist 下面的文件。

所以可以使用 Eslint 忽略文件解决。在项目根目录新建下面文件:`.eslintignore`

![[00 assets/cb6d7f37ef1f887b0dba034b5cce7626_MD5.png]]

### 2.9.2 babel

JavaScript 编译器。

主要用于将 ES6 语法编写的代码转换为向后兼容的 JavaScript 语法，以便能够运行在当前和旧版本的浏览器或其他环境中

#### 2.9.2.1 配置文件

配置文件由很多种写法：

- babel.config.\*：新建文件，位于项目根目录
  - `babel.config.js`
  - `babel.config.json`
- .babelrc.\*：新建文件，位于项目根目录
  - `.babelrc`
  - `.babelrc.js`
  - `.babelrc.json`
- `package.json` 中 `babel`：不需要创建文件，在原有文件基础上写

Babel 会查找和自动读取它们，所以以上配置文件只需要存在一个即可

#### 2.9.2.2 具体配置

我们以 `babel.config.js` 配置文件为例：

```javascript
module.exports = {
  // 预设
  presets: [],
};
```

1. presets 预设

简单理解：就是一组 Babel 插件, 扩展 Babel 功能

- `@babel/preset-env`: 一个智能预设，允许您使用最新的 JavaScript。
- `@babel/preset-react`：一个用来编译 React jsx 语法的预设
- `@babel/preset-typescript`：一个用来编译 TypeScript 语法的预设

#### 2.9.2.3 babel 使用

下载包

```bash
cnpm i babel-loader @babel/core @babel/preset-env -D
```

写入规则

```javascript
const path = require("path");
const ESLintPlugin = require("eslint-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "./js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          "style-loader",
          "css-loader",
        ],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024,
          },
        },
        generator: {
          filename: "./dist/imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      //babel的配置
      {
        test: /\.js$/,
        exclude: /(node_modules)/, //表示排除
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  plugins: [
    new ESLintPlugin({
      context: path.resolve(__dirname, "src"),
    }),
  ],
  mode: "development",
};

```

再创建 babel.config.js，定义 Babel 配置文件

![[00 assets/078c95c2862b7f60339221f7fc1a6b73_MD5.png]]

再使用`npx webpack`来创建就会发现向下兼容了

## 2.10 处理 HTML 文件

下载包

```javascript
cnpm i html-webpack-plugin -D
```

写入插件

```javascript
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024,
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      context: path.resolve(__dirname, "src"),
    }),
      //引入插件
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "public/index.html"),
    }),
  ],
  mode: "development",
};
```

我们将原本的 html 文件里面的引入 js 去掉

再使用`npx webpack`就会发现文件多了一个 dist 里面多了一个 html 文件，而且自动引入了 main.js

## 2.11 开发服务器&自动化

每次写完代码都需要手动输入指令才能编译代码，太麻烦了，我们希望一切自动化

下载包

```bash
cnpm i webpack-dev-server -D
```

写入服务器

```javascript
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024,
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      context: path.resolve(__dirname, "src"),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "public/index.html"),
    }),
  ],
  // 开发服务器
  devServer: {
    host: "localhost", // 启动服务器域名
    port: "3000", // 启动服务器端口号
    open: true, // 是否自动打开浏览器
  },
  mode: "development",
};
```

我们使用`npx webpack serve`就会自动打开服务器，这样的话每次只要文件变化的话，然后保存就会自动编译，并且显示再浏览器上面

我们将 dist 文件删除，但是服务器一样可以运行，因为当你使用开发服务器时，所有代码都会在内存中编译打包，并不会输出到 dist 目录下。

开发时我们只关心代码能运行，有效果即可，至于代码被编译成什么样子，我们并不需要知道。

## 2.13 处理 CSS 资源

### 2.13.1 提取 CSS 成单独文件

Css 文件目前被打包到 js 文件中，当 js 文件加载时，会创建一个 style 标签来生成样式

这样对于网站来说，会出现闪屏现象，用户体验不好

我们应该是单独的 Css 文件，通过 link 标签加载性能才好

下载包

```bash
cnpm i mini-css-extract-plugin -D
```

配置 webpack.prod.js

```javascript
const path = require("path");
const ESLintPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin"); //引入CSS插件

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "../dist"),
    filename: "./js/main.js",
    clean: true,
  },
  //加载器
  module: {
      {
        test: /\.css$/,
        //执行的顺序从下到上
        use: [MiniCssExtractPlugin.loader,
          // "style-loader",  //因为使用了css插件，这里的style-loader就可以去掉了
          "css-loader",
        ],
      },
      {
        test: /\.less$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024,
          },
        },
        generator: {
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  plugins: [
    new ESLintPlugin({
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../public/index.html"),
    }),
    // 提取css成单独文件
    new MiniCssExtractPlugin({
      // 定义输出文件名和目录
      filename: "./css/main.css",
    }),
  ],
  mode: "development",
};

```

我们再使用`npm run build`就可以运行，因为上面的生产模式里面配置了执行的命令

而且你会发现打包的 webpack 文件的 html 文件自动引入了 css 文件，因为我们在 2.10 里面，使用了 HTML 插件，所以这个时候就不需要再手动引入了

### 2.13.2 CSS 兼容性处理

下载包

```
npm i postcss-loader postcss postcss-preset-env -D
```

配置包

```javascript
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "../dist"),
    filename: "static/js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        // 用来匹配 .css 结尾的文件
        test: /\.css$/,
        // use 数组里面 Loader 执行顺序是从右到左
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [
                  "postcss-preset-env", // 能解决大多数样式兼容性问题
                ],
              },
            },
          },
        ],
      },
      {
        test: /\.less$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {	//注意这个配置要写在css-loader下面，less-loader前面
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [
                  "postcss-preset-env", // 能解决大多数样式兼容性问题
                ],
              },
            },
          },
          "less-loader",
        ],
      },
      {
        test: /\.s[ac]ss$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [
                  "postcss-preset-env", // 能解决大多数样式兼容性问题
                ],
              },
            },
          },
          "sass-loader",
        ],
      },
      {
        test: /\.styl$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: [
                  "postcss-preset-env", // 能解决大多数样式兼容性问题
                ],
              },
            },
          },
          "stylus-loader",
        ],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024,
          },
        },
        generator: {
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../public/index.html"),
    }),
    new MiniCssExtractPlugin({
      filename: "static/css/main.css",
    }),
  ],
  mode: "production",
};
```

假如我们想考虑兼容性的问题，我们可以可以在`package.json`里面写入下面的配置

![[00 assets/fe8a2c0282f0e8b6ad8dd034834e368e_MD5.png]]

```javascript
{
	......
	"browserslist": [
    	"ie >= 8"
  	]
}
```

想要知道更多的 `browserslist` 配置，查看[browserslist 文档](https://github.com/browserslist/browserslist)

以上为了测试兼容性所以设置兼容浏览器 ie8 以上。

实际开发中我们一般不考虑旧版本浏览器了，所以我们可以这样设置：

```json
{
  // 其他省略
  "browserslist": [
    "last 2 version",
    "> 1%",
    "not dead"
  ]
}
```

我们这个时候再来看上面的配置文件，是不是有很多重复的部分，所以下面就是将上面的配置信息进行简化

```javascript
const path = require("path"); //node.js核心模块，专门用于处理路径问题
const ESLintPlugin = require("eslint-webpack-plugin"); //引入eslint
const HtmlWebpackPlugin = require("html-webpack-plugin"); //引入Html文件打包
const MiniCssExtractPlugin = require("mini-css-extract-plugin"); //引入CSS插件

//封装的函数
const getStyleLoaders = (preProcesser) => {
  return [
    MiniCssExtractPlugin.loader,
    "css-loader",
    {
      loader: "postcss-loader",
      options: {
        postcssOptions: {
          plugins: [
            "postcss-preset-env", // 能解决大多数样式兼容性问题
          ],
        },
      },
    },
    preProcesser
  ].filter(Boolean);//这里是为了排除undefined的错误
}


module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "../dist"),
    filename: "./js/main.js",
    clean: true,
  },
  //加载器
  module: {
    rules: [
      //loader的配置
      //css配置
      {
        test: /\.css$/,
        use: getStyleLoaders()
      },
      //less配置
      {
        test: /\.less$/,
        use: getStyleLoaders("less-loader")
      },
      //scss和sass配置
      {
        test: /\.s[ac]ss$/,
        use: getStyleLoaders("sass-loader")
      },
      //stylus配置
      {
        test: /\.styl$/,
        use: getStyleLoaders("stylus-loader")
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024,
          },
        },
        generator: {
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  plugins: [
    new ESLintPlugin({
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../public/index.html"),
    }),
    new MiniCssExtractPlugin({
      filename: "./css/main.css",
    }),
  ],
  mode: "development",
};

```

### 2.13.3 CSS 压缩

下载包

```bash
cnpm i css-minimizer-webpack-plugin -D
```

写入配置

```javascript
const path = require("path"); //node.js核心模块，专门用于处理路径问题
const ESLintPlugin = require("eslint-webpack-plugin"); //引入eslint
const HtmlWebpackPlugin = require("html-webpack-plugin"); //引入Html文件打包
const MiniCssExtractPlugin = require("mini-css-extract-plugin"); //引入CSS插件
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin"); //用于CSS压缩

const getStyleLoaders = (preProcesser) => {
  return [
    MiniCssExtractPlugin.loader,
    "css-loader",
    {
      loader: "postcss-loader",
      options: {
        postcssOptions: {
          plugins: [
            "postcss-preset-env", // 能解决大多数样式兼容性问题
          ],
        },
      },
    },
    preProcesser
  ].filter(Boolean);
}


module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "../dist"),
    filename: "./js/main.js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: getStyleLoaders()
      },
      {
        test: /\.less$/,
        use: getStyleLoaders("less-loader")
      },
      {
        test: /\.s[ac]ss$/,
        use: getStyleLoaders("sass-loader")
      },
      {
        test: /\.styl$/,
        use: getStyleLoaders("stylus-loader")
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024,
          },
        },
        generator: {
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  plugins: [
    new ESLintPlugin({
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../public/index.html"),
    }),
    new MiniCssExtractPlugin({
      filename: "./css/main.css",
    }),
    // css压缩
    new CssMinimizerPlugin(),
  ],
  mode: "production",
};
```

注意这里 css 的压缩不能将 mode 调为 development，而要调为 production

## 2.14 HTML 压缩

默认生产模式已经开启了：html 压缩和 js 压缩

不需要额外进行配置

![[00 assets/dd0e53a4871a19fdcd889d7373efbed9_MD5.png]]

## 2.15 总结

本章节我们学会了 Webpack 基本使用，掌握了以下功能：

1. 两种开发模式

- 开发模式：代码能编译自动化运行
- 生产模式：代码编译优化输出

1. Webpack 基本功能

- 开发模式：可以编译 ES Module 语法
- 生产模式：可以编译 ES Module 语法，压缩 js 代码

1. Webpack 配置文件

- 5 个核心概念
  - entry
  - output
  - loader
  - plugins
  - mode
- devServer 配置

1. Webpack 脚本指令用法

- `webpack` 直接打包输出
- `webpack serve` 启动开发服务器，内存编译打包没有输出

### 2.15.1 个人总结

下面是我的文件目录

`config`文件夹是将 webpack 的文件进行分类，`webpack.dev.js`是平时开发的时候使用的，`webpack.prod.js`是最后项目上线的时候使用的

`dist`文件是最后输出的文件资源

`public`是静态的 HTML 文件

`src`是里面的样式，JS......等内容

`.eslintignore`是 eslint 插件，进行语法检查的时候设置省略的文件

`.eslintrc.js`是设置 eslint 插件的各项配置

`babel.config.js`是设置 babel 的各项配置

![[00 assets/b1c13976948c42eeaa2a504f0014fa36_MD5.png]]

下面是`webpack.dev.js`文件的配置

```javascript
const path = require("path"); //node.js核心模块，专门用于处理路径问题
const ESLintPlugin = require("eslint-webpack-plugin"); //引入eslint
const HtmlWebpackPlugin = require("html-webpack-plugin"); //引入HTML文件打包，自动引入JS和CSS

module.exports = {
  //入口：设置打包的开始的文件
  entry: "./src/main.js", //相对路径
  //输出：我们输出在那个文件夹
  output: {
    path: undefined, // 开发模式没有输出，直接使用代理服务器，在内存中执行，不需要指定输出目录
    //文件名
    filename: "./js/main.js",
    //自动清空上次打包的内容
    // clean: true, //当你配置了开发服务器的话，因为东西加载在内存，所以可以不要
  },
  //加载器
  module: {
    rules: [
      //css配置
      {
        test: /\.css$/, //检测以css结尾的文件
        //执行的顺序从下到上
        use: [
          //会动态创建一个 Style 标签，里面放置 Webpack 中 Css 模块内容
          "style-loader",
          //将css编译为common.js的模块放在js中
          "css-loader",
        ],
      },
      //less配置
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      //scss和sass配置
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      //stylus配置
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      //对图片进行Base64处理
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024, // 小于50kb的图片会被base64处理
          },
        },
        generator: {
          // 将图片文件输出到 static/imgs 目录中
          // 将图片文件命名 [hash:8][ext][query]
          // [hash:8]: hash值取8位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      //对于图标字体进行处理
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      //babel的配置
      {
        test: /\.js$/,
        exclude: /(node_modules)/, //表示排除
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  //插件
  plugins: [
    //plugin的配置
    new ESLintPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "../public/index.html"),
    }),
  ],
  // 开发服务器
  devServer: {
    host: "localhost", // 启动服务器域名
    port: "3000", // 启动服务器端口号
    open: true, // 是否自动打开浏览器
  },
  //模式
  mode: "development",
};

```

下面是平时开发时候设置的文件

```javascript
const path = require("path"); //node.js核心模块，专门用于处理路径问题
const ESLintPlugin = require("eslint-webpack-plugin"); //引入eslint
const HtmlWebpackPlugin = require("html-webpack-plugin"); //引入Html文件打包
const MiniCssExtractPlugin = require("mini-css-extract-plugin"); //引入CSS插件
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin"); //用于CSS压缩

//用于文件的数组的输出，这样的话就不需要写相同的配置
const getStyleLoaders = (preProcesser) => {
  return [
    MiniCssExtractPlugin.loader,
    "css-loader",
    {
      loader: "postcss-loader",
      options: {
        postcssOptions: {
          plugins: [
            "postcss-preset-env", // 能解决大多数样式兼容性问题
          ],
        },
      },
    },
    preProcesser,
  ].filter(Boolean);
};

module.exports = {
  //入口
  entry: "./src/main.js", //相对路径
  //输出
  output: {
    //文件输出路径
    //__dirname node.js变量，代表当前文件的文件夹目录
    //__dirname表示的是hello文件夹，后面的dist是hello文件夹里面的dist
    path: path.resolve(__dirname, "../dist"), // 生产模式需要输出
    //文件名
    filename: "./js/main.js",
    //自动清空上次打包的内容
    clean: true, //当你配置了开发服务器的话，因为东西加载在内存，所以可以不要
  },
  //加载器
  module: {
    rules: [
      //css配置
      {
        test: /\.css$/, //检测以css结尾的文件
        //执行的顺序从下到上
        use: getStyleLoaders(),
      },
      //less配置
      {
        test: /\.less$/,
        use: getStyleLoaders("less-loader"),
      },
      //scss和sass配置
      {
        test: /\.s[ac]ss$/,
        use: getStyleLoaders("sass-loader"),
      },
      //stylus配置
      {
        test: /\.styl$/,
        use: getStyleLoaders("stylus-loader"),
      },
      //对图片进行Base64处理
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024, // 小于50kb的图片会被base64处理
          },
        },
        generator: {
          // 将图片文件输出到 static/imgs 目录中
          // 将图片文件命名 [hash:8][ext][query]
          // [hash:8]: hash值取8位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: "./imgs/[hash:8][ext][query]",
        },
      },
      //对于图标字体进行处理
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "./media/[hash:8][ext][query]",
        },
      },
      //babel的配置
      {
        test: /\.js$/,
        exclude: /(node_modules)/, //表示排除
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
    ],
  },
  //插件
  plugins: [
    //plugin的配置
    new ESLintPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "../public/index.html"),
    }),
    // css压缩
    new CssMinimizerPlugin(),
    // 提取css成单独文件
    new MiniCssExtractPlugin({
      // 定义输出文件名和目录
      filename: "./css/main.css",
    }),
  ],
  //模式
  mode: "production",
};
```

# 3. webpack 高级

本章节主要介绍 Webpack 高级配置。

所谓高级配置其实就是进行 Webpack 优化，让我们代码在编译/运行时性能更好~

我们会从以下角度来进行优化：

1. 提升开发体验
2. 提升打包构建速度
3. 减少代码体积
4. 优化代码运行性能

## 3.1 SourceMap

开发时我们运行的代码是经过 webpack 编译后的，例如下面这个样子：

![[00 assets/7e644a125bdd9a09cb0fd8428b1f8fdc_MD5.png]]

所有 css 和 js 合并成了一个文件，并且多了其他代码。此时如果代码运行出错那么提示代码错误位置我们是看不懂的。一旦将来开发代码文件很多，那么很难去发现错误出现在哪里。

所以我们需要更加准确的错误提示，来帮助我们更好的开发代码

SourceMap（源代码映射）是一个用来生成源代码与构建后代码一一映射的文件的方案。

它会生成一个 xxx.map 文件，里面包含源代码和构建后代码每一行、每一列的映射关系。当构建后代码出错了，会通过 xxx.map 文件，从构建后代码出错位置找到映射后源代码出错位置，从而让浏览器提示源代码文件出错位置，帮助我们更快的找到错误根源。

通过查看[Webpack DevTool 文档 open in new window](https://webpack.docschina.org/configuration/devtool/)可知，SourceMap 的值有很多种情况.

但实际开发时我们只需要关注两种情况即可：

- 开发模式：`cheap-module-source-map`
  - 优点：打包编译速度快，只包含行映射
  - 缺点：没有列映射

![[00 assets/004eb526f01eb8459eb9d1fd42119cdd_MD5.png]]

- 生产模式：`source-map`
  - 优点：包含行/列映射
  - 缺点：打包编译速度更慢

![[00 assets/e59d472d07d0e9ffc695acd670c72a65_MD5.png]]

## 3.3 oneof

我们在日常使用的情况下，都是一个一个文件和 loader 来进行匹配，这样的话效率就会非常低，这是因为 test 的正则配置没有用到

所以这个时候我们就需要使用 oneof 来进行处理，顾名思义就是只能匹配上一个 loader, 剩下的就不匹配了

![[00 assets/ab1c8d979609b958cf5f7f9cb1c7016c_MD5.png]]

## 3.4 include/exclude

`exclude`表示排除这个文件，`include`表示包含这个文件，这样的话我们匹配到了，就会按照匹配到的文件规则来进行处理

![[00 assets/8224af68baa66f37b815a73642434429_MD5.png]]

## 3.5 cache

每次打包时 js 文件都要经过 Eslint 检查 和 Babel 编译，速度比较慢。我们可以缓存之前的 Eslint 检查 和 Babel 编译结果，这样第二次打包时速度就会更快了。

所以这个时候我们可以对 Eslint 检查 和 Babel 编译结果进行缓存。

![[00 assets/25e2648a92c4e2eeefb3abe2c3591b9e_MD5.png]]

下面是 eslint 的缓存

![[00 assets/5aab9703fac3390ac96031f9c9a866cc_MD5.png]]

## 3.6 Thead

当项目越来越庞大时，打包速度越来越慢，甚至于需要一个下午才能打包出来代码。这个速度是比较慢的。

我们想要继续提升打包速度，其实就是要提升 js 的打包速度，因为其他文件都比较少。

而对 js 文件处理主要就是 eslint 、babel、Terser 三个工具，所以我们要提升它们的运行速度。

我们可以开启多进程同时处理 js 文件，这样速度就比之前的单进程打包更快了。

多进程打包：开启电脑的多个进程同时干一件事，速度更快。

**需要注意：请仅在特别耗时的操作中使用，因为每个进程启动就有大约为 600ms 左右开销。**

![[00 assets/59951f79b1da6fb56bb05bdd9f471953_MD5.png]]

![[00 assets/249014b0c88188c746dbef05d67a4f6a_MD5.png]]

![[00 assets/e723715d24bad419b0db0d7f1305147b_MD5.png]]
