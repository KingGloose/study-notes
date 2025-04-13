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

2、针对于 React 来讲，使用 babel 即可实现代码的转换，因为麻烦可以使用 `preset-react` 来做打包的预设，`html-webpack-plugin`让指定的 `html` 文件作为模块来输出

![[00 assets/823f0c62138fc25c28bcc9ef86e2b20b_MD5.jpeg]]

![[00 assets/db72baccefa0fd6c1f66c58f6058dccd_MD5.jpeg]]

## 3.6 TS 处理

### 3.6.1 tsc

1、直接使用 `tsc` 就可以编译
![[00 assets/309a50cc1f80a67dab31a74b0be2091b_MD5.jpeg]]

### 3.6.2 ts-loader

![[00 assets/6535ff132f74567db1818600e2675d69_MD5.jpeg]]

1、使用 `ts-loader` 就可以实现转换，如果我们想实现转换还要初始化一个 `tsconfig.json`，他会自动读取
2、但是使用 `ts-loader` 会有一个问题，他使用得 `ts` 中得 `complier` 来做得编译。如果使用这种方式得话，就不能使用 `polyfill`了，所以一般使用 `babel-loader` 来使用
![[00 assets/d26b7a5406ce9bee5e1b832f309b1c30_MD5.jpeg]]

### 3.6.3 babel-loader

![[00 assets/0f6c7ef59357ca687febb7e41d825d14_MD5.jpeg]]

1、可以使用 `babel-loader` 来实现转换，直接使用 `@babel/preset-typescript` 来做预设即可
2、如果只是使用 `babel-loader` 来编译得话也存在问题，那就是编译得时候不会出现编译错误得报错 
![[00 assets/c27ea0ea45cb418e85525e9d73a3780c_MD5.jpeg]]

### 3.6.4 联合编译

![[00 assets/b29d3218640a7e9b3a00600bc1ffb6f6_MD5.jpeg]]


1、使用 `npm run ts-check-watch` 来监听 `ts` 中是否有错误，也就是开发得时候执行 `ts-check-watch`，要打包得时候使用 `npm run build` 来做 `ts` 得编译
![[00 assets/6c646900bcf8ed3628ebdd165851798c_MD5.jpeg]]


# 4. 基础配置

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

![[00 assets/052aa4e7b447661754d9cd91da238b01_MD5.jpeg]]

![[00 assets/f81bcd48d457e6eda0616d8658a04f55_MD5.png]]

## 6.2 webpack-dev-server

### 6.2.1 基本使用

> 基本使用

![[00 assets/e9ed937e53878f68a40887ed1eaa6ebe_MD5.png]]

下载包之后直接使用`webpack serve`即可开启`webpack-dev-serve`插件的功能。如果需要额外配置的话，可以设置`devServer`来处理

![[00 assets/a493236e48d97cf5516295a63a9971b9_MD5.png]]

> devServer 配置

下面就是`devServer`的一些基础配置
![[00 assets/f81bcd48d457e6eda0616d8658a04f55_MD5.png]]

### 6.2.2 static

![[00 assets/ceb7b9c88dc9009dc6d93d87ce741fd8_MD5.jpeg]]

1、因为我们使用本地服务器得话，会将打包得内容加入到内存中，然后浏览器运行结果。但是开发中我们在 `index.html` 中引入了图片、JS等内容，它是没有加入到内存中得。所以是访问不到得，我们就需要进行静态资源得部署

2、配置 `static` 即可完成静态资源，这样我们在 `index.html` 模板html 中就要按照如下路径来编写
![[00 assets/b543d050f0c2ca0416c3ca9a14339bbd_MD5.jpeg]]

### 6.2.3 liveReload

![[00 assets/fab4d9038bac09d5060cfc3cf8957c9b_MD5.jpeg]]

### 6.2.4 host

![[00 assets/9e1dd9beb8eaf31a5a6e09e30a2e9a2b_MD5.png]]

### 6.2.5 port

设置监听得端口，默认是 8000

### 6.2.6 open

![[00 assets/6cc652ec394b3c22ea1b19193fb375f9_MD5.jpeg]]

### 6.2.7 compress

![[00 assets/eec76f6534f635a7ce67f1c99f2af916_MD5.jpeg]]

### 6.2.8 proxy

![[00 assets/f12c01d97cd119ce20678cceac612e5f_MD5.jpeg]]

1、解决开发阶段得跨域问题，这块可以详细看看我之前得关于跨域解释
2、它这里会将原本为`http://localhost:8080/api/user`转为`http://localhost:9000/user`，因为遇到了`/api`那么就会将头部转为`http://localhost:9000`，然后重写`/api`为`''`空字符串
![[00 assets/91299ac7e6be938587ee22f74047d14a_MD5.jpeg]]

3、这里还有一个 `changeOrigin` 得属性，因为我们发送请求得时候会在请求得 `haeder` 发送 `origin`，如果为 `false` 得话，那么服务器拿到得 `origin`是本地得地址`http://localhost:8888`，如果你改为 `true` 得话，那么服务器拿到得地址就是`api`得地址，改变了源
![[00 assets/ef5c531fdf37092992339399241ccf35_MD5.jpeg]]

### 6.2.9 historyApiFallback

![[00 assets/24dcfe7ee0f8f32210a70d9bb4cf3bc4_MD5.png]]

1、按照如下方式来即可开启
![[00 assets/0b98ab0c30267332c7cb82b3c5f4b220_MD5.jpeg]]


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


# 7. 区分环境

## 7.1 基本介绍

![[00 assets/9f8a9d99b1af3449495d00e6d06afcd5_MD5.png]]

## 7.2 不同环境文件

1、`生产环境(production)`：标识项目已经上线了、`开发环境(development)`：自己编写代码时配置的环境，我们要区分开发模式和生产模式，就要将不同模式的配置文件进行分类
![[00 assets/2de4182e4a9a436f43cd88e6039f2612_MD5.png]]

2、然后先配置 webpack.dev.js 文件，也就是平时开发时候的模式
![[00 assets/cd9ac4a7e3234d54e67213af92d1af8b_MD5.png]]
![[00 assets/3ff6ca15961ed10ffa3195640e1562af_MD5.png]]

## 7.3 配置运行指令

1、为了方便运行不同模式的指令，我们将指令定义在 package.json 中 scripts 里面
2、开发模式：`npm start` 或 `npm run serve`；生产模式：`npm run build`
![[00 assets/71a6b8cfd472b7af6d68d9902a8c1ca6_MD5.png]]


## 7.4 路径问题

![[00 assets/8e482c4e6b327b8b247aff81b505abbb_MD5.png]]

1、其中就存在`context`属性来指定路径，并且该属性只为`入口文件`、`加载器`和`插件`使用，这些地方默认就是项目根路径，而`output`、`alias`就是真实路径了
![[00 assets/7b0cf1f9af7de11bdf2c6d1326c068a7_MD5.png]]

## 7.5 抽取公共配置

1、`pnpm add webpack-merge -D`
2、将公共的配置都抽取到`common.config.js`中，然后通过`webpack-merge`来合并处理
![[00 assets/ca886ee4a3479a96dde926bbf98b83c8_MD5.png]]

3、对于`production`也是一样的处理方式，这样会让配置更加清晰
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

## 9.1 基础介绍

### 9.1.1 基本介绍

![[00 assets/7d23d6f4e9d3dc43070b18091340d65c_MD5.png]]

### 9.1.2 命令行使用

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

### 9.1.3 底层原理

![[00 assets/f14c85f3a8304d0a91d4a6fca11a4558_MD5.png]]

![[00 assets/51a43d1e2ef44e3c9236b1134993bf84_MD5.png]]


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

# 11. 性能优化

## 11.1 基本介绍

![[00 assets/50a02469122eff50e643d4bf423289fa_MD5.jpeg]]

## 11.2 代码分包

![[00 assets/e8f02bdf4f426dc90af60d91116c0db0_MD5.jpeg]]

### 11.2.1 多入口分包

![[00 assets/5e86483db4294433b4354ba5b5f99992_MD5.jpeg]]
1、如果我们想实现多个入口来进行分包，按照如上配置即可，`enrty`可以是一个对象得形式，针对输出直接使用 `[name]-bundle.js` 他就会将 `entry` 中得 `key` 直接填入到 `[name]` 中
![[00 assets/dc58c957c1d65b04dc3d22bf659524be_MD5.jpeg]]

### 11.2.2 多入口共享代码

![[00 assets/3ec0674ea26385c50327eb29bf90253a_MD5.jpeg]]

1、我们已经使用多入口来做打包了，但是针对一些比较通用包，多个入口文件中都会使用得情况，可以按照如下得方式来做编写
2、`import`表示导入得包，`dependOn`表示依赖得入口，下图中的`index`和`main`就使用的同一个
![[00 assets/8dd099cbed235bfdfbd488750abd447d_MD5.jpeg]]

###  11.2.3 动态导入
#### 11.2.3.1 基本使用

![[00 assets/ae196d8f990e7f8b099aab9f9e90786c_MD5.jpeg]]
![[00 assets/69ad4b906b1d9fcad60dc87d53aad369_MD5.jpeg]]

1、我们在 `webpack` 的打包下面进行打包的操作，如果我们使用 `import()` 函数，那么在实际的情况中会额外打包出 `js`
2、这样在首包加载会少很多的代码，如下图示例，只有在点击的时候才会自动的请求加载`js`进行执行
![[00 assets/7dcad3dfced6a65975de37e22f229e70_MD5.jpeg]]

#### 11.2.3.2 分包命名

![[00 assets/cfd7a499e50908a34f28f4fb52c9c8f3_MD5.jpeg]]

1、因为我们使用了 `import()` 来分包，但是名字我们可以额外配置
![[00 assets/06c9a98333d9f45e6d28cfb42f7edfde_MD5.jpeg]]

2、针对于 `[name]` 的显示可以在 `import()` 中编写 `webpack` 的魔法注释
![[00 assets/d98c1141fbea7500a1f87bc3ffcbdfe8_MD5.jpeg]]

### 11.2.4 splitChunks

#### 11.2.3.1 基本使用

![[00 assets/1a62a01bf90e4c0bf519b381096e466f_MD5.jpeg]]
1、针对于使用的第三方库中的内容都会被打进 `vendors` 中使用
![[00 assets/cb55ca15b8bb67b9d070a1f5c35e68cd_MD5.jpeg]]

#### 11.2.3.2 maxSize/minSize

1、配置拆包的大小maxSize/minSize
![[00 assets/74d048aae46d8bda1fbbab32221f9adc_MD5.jpeg]]

#### 11.2.3.3 cacheGroups

1、我们可以根据匹配倒的 `test` 来实现自定义的拆包操作，并且按照 `filename` 的方式来进行命名
![[00 assets/8dd735c80c1099d7a62644fdb73b1259_MD5.jpeg]]

### 11.2.5 chunkIds

![[00 assets/76c6565a4863b1cbd2c4955bd336831e_MD5.jpeg]]

1、为什么不适应 `natural` 的方式来打包呢？因为他本身打包的js经常变化，那么每次打包都不利于浏览器的缓存
![[00 assets/d8516e2b60c4d1a4a516cc77a091ce1c_MD5.jpeg]]

### 11.2.6 hash名称

1、针对 hash 值名称，其实是有利于浏览器得缓存，所以在合适得时候使用不同得 hash 值来命名
![[00 assets/0e1a23c3658d4fad32260b35e841f9af_MD5.jpeg]]

## 11.3 prefetch/preload

![[00 assets/3ad06113ce7d531a1faaa5f2ce889303_MD5.jpeg]]

1、打包的时候使用 `webpack 魔法注释` 来实现标记即可
![[00 assets/4d253b4de4483c0314ea189cd075a3a9_MD5.jpeg]]
2、如果你编写了 `preload/prefetch` 的话，就会额外在空闲的时候请求
![[00 assets/8592652791ea0c2522e0e96dea5601ea_MD5.jpeg]]


## 11.4 cdn

### 11.4.1 基本介绍

![[00 assets/e5595b1c2c098bbbc888cab057451e07_MD5.jpeg]]



### 11.4.2 基本使用

![[00 assets/b9e85a9893a75d6f0899fbbe870cd381_MD5.jpeg]]

1、这里编写 `publicPath` 就可以在编译的时候将这个地址编写进去
![[00 assets/6a3ac903b3da511b76da4577a7ca7d61_MD5.jpeg]]
2、打包的时候就会带上 `publicPath` 的地址
![[00 assets/08b6f36bfbcd4cfba957b06f8a6c806d_MD5.jpeg]]

### 11.4.3 第三方库

![[00 assets/bfb557d4cb1a83b288cebb0d52c66db2_MD5.jpeg]]

1、我们使用 `externals` 表示哪些代码不需要打包
2、`key` 表示框架的名字（`package.json` 中的名字）；`value` 表示实际使用的名称，比如你使用的 `Jquery`，那么就是 `jQuery: "$"`，因为你在项目中使用的就是 `$`
![[00 assets/35094fd65b0df86ae44de0ea02c22365_MD5.jpeg]]

## 11.5 shimming

### 11.5.1 基本介绍

![[00 assets/c2c1cc64883fade43d3e9c398bf0a634_MD5.jpeg]]

### 11.5.2 基本使用

![[00 assets/cca5c1210b1949feb68580921fde3805_MD5.jpeg]]

1、其实本质和 `npm` 得 `隐式依赖` 有关，比如你 `隐式依赖` 了 `axios`，但是你没有导入，并且在全局没有引入 `cdn` 来全局使用，就可以使用下面得方式让 `axios` 变成一个全局变量来使用
![[00 assets/57a8d68eda41f2a0fa9090d6cb587dd5_MD5.jpeg]]


## 11.6 提取CSS

![[00 assets/0746d8b7ea944e1ac0be04e15739315a_MD5.jpeg]]

1、我们可以使用  `mini-css-extract-plugin` 来做 `css代码`得抽取，这个时候 `loader` 也需要换成 `mini-css-extract-plugin` 得 `loader`
2、开发得时候可以使用 `style-loader`，在生产环境可以使用`css-loader`就行
![[00 assets/6b40aa58a70c8e72ff9e532d00493e78_MD5.jpeg]]

## 11.7 DLL库

![[00 assets/6a32b36ce34d0d3e384afd31c556108b_MD5.jpeg]]

## 11.8 Terser

### 11.8.1 基本介绍

![[00 assets/445477f15a6b2bbaecb244a881748449_MD5.jpeg]]

### 11.8.2 命令行使用

![[00 assets/2adf87083c9d3efca8c83ff921278d6a_MD5.jpeg]]
![[00 assets/d69c508a37f6f8359a1181ebef504795_MD5.jpeg]]
 

### 11.8.3 webpack使用

![[00 assets/cf7c6d26dc7e9ed958d2b5f6dff264e6_MD5.jpeg]]
![[00 assets/9e35bec93ff477e9e297bb19e7e0d7b1_MD5.jpeg]]

1、安装之后直接使用即可，可以自动优化你的 `JS代码`，但是需要你做一些额外得配置
![[00 assets/f4b4e88f6ef49b9b7df47f95d6b983b9_MD5.jpeg]]

## 11.9 CSS压缩

![[00 assets/604a3068ff9e09c436f67f6840cffd6b_MD5.jpeg]]
1、可以使用 `CssMinimizerWebpackPlugin` 就可以实现针对 `CSS压缩`
![[00 assets/29b4c53071cce50ee37e86045c28c1a0_MD5.jpeg]]

## 11.10 JS Tree Shaking

### 11.10.1 usedExports

![[00 assets/7da5ebffccf436f85558418ffcf4207f_MD5.jpeg]]

1、我们使用 `usedExports` 来做模块得分析时会将没使用到得函数做额外得标注
![[00 assets/f52ff0e887ffd77c72db4f55369982c1_MD5.jpeg]]

2、这样在 `Terser` 做代码压缩得时候会将这部分代码给优化掉
![[00 assets/b92602d362853b51019137d108de91a0_MD5.jpeg]]

### 11.10.2 sideEffects

![[00 assets/ba2096e700757dff62e5fa409e2482c2_MD5.jpeg]]

1、一般情况我们直接使用 `import "./src/main.js"`得时候，即便里面函数什么都没干，也依旧会打包进来，所以我们可以在 `package.json` 中进行配置`sideEffects: false`，表示当前得所有模块都是 `纯模块`，没有任何副作用针对没有使用得可以直接 `Tree Sharking`
![[00 assets/f6859458e14b30d171da25c9536553ad_MD5.jpeg]]

2、但是在项目中不可能所有得模块都是纯模块，这个时候就需要额外得配置了，表示这些模块有副作用，需要打包进去
3、我们直接引入 `import "main.css"`也需要额外去做相应得配置
![[00 assets/7abbd412427ee47276913bd9c8e8c424_MD5.jpeg]]

### 11.10.3 最佳实践

![[00 assets/c1feb486102f9c3fe2545d9b703bd7fc_MD5.jpeg]]

## 11.11 CSS Tree Shaking

![[00 assets/d5e7073ae37b03039a158c749c98386e_MD5.jpeg]]
![[00 assets/c0f0bc0349e2a1de6147549f80ff2d4a_MD5.jpeg]]

1、我们可以使用 `purgecss-webpack-plugin`来针对`css tree shaking`，`paths`表示扫描得路径，`safelist`表示是白名单
2、该插件要配合 `mini-css-extract-plugin`一起使用
![[00 assets/221c6ac4d2bda6cf3232d1a8ae762eaf_MD5.jpeg]]


## 11.12 作用域提升

![[00 assets/635e6de1448ac1308d8f7025599e080e_MD5.jpeg]]

1、这个是 `webpack` 下面内置得模块
![[00 assets/0dbb7c9a9aded8ec76b3e12e90ce0b67_MD5.jpeg]]

2、看下图中得代码，上面是没开启之前得，如果想在 `demo.js` 中访问到 `math.js` 中得 `sum函数`，需要越过函数作用域，这样导致执行得效率不是很高
3、我们可以开启作用域得提升，查看优化之后得代码可以发现已经将函数提升了作用域，提高了执行得效率
![[00 assets/2b992152da866b35d8779f351ba8523b_MD5.jpeg]]

## 11.13 HTTP压缩

### 11.13.1 基本介绍

![[00 assets/d33b06fb1877de5db9ca8484fcfcded6_MD5.jpeg]]
![[00 assets/2e1aaa51f724a942a614ffab55eab02c_MD5.jpeg]]

### 11.13.2 基本使用

![[00 assets/604c62b173df449876619eb15b5311ea_MD5.jpeg]]
## 11.14 HTML压缩

![[00 assets/55b3fafffc723429b123fc9d7af09fcf_MD5.jpeg]]
1、我们使用 `html-webpack-plugin` 就可以进行对应得压缩配置
![[00 assets/5f0621acc6781a4da26988675c4ed72b_MD5.jpeg]]

## 11.15 打包时间分析

1、我们可以使用 `speed-measure-webpack-plugin`来分析各个模块的执行速度
![[00 assets/94f3019928f43f40c719f56e044992c3_MD5.jpeg]]

## 11.16 打包结果分析

![[00 assets/cddf49724044c13771bab5268f96825a_MD5.jpeg]]

# 12. 源码分析

## 12.1 准备开发

1、下载 `webpack源码`，为了方便调试编写如下代码来执行编译操作，其实和使用 `webpack-cli` 是一样的效果
![[00 assets/d70eb642425a550924788f7e78e27d0c_MD5.jpeg]]


## 12.2 compiler

1、我们使用`webpack.compiler`的本质就是底层的`create`方法
2、我们也可以在第二个参数传入`cb`来实现`run`的效果
![[Pasted image 20250413160909.png]]

