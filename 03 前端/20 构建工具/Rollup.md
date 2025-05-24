# 1 基本介绍

![[00 assets/0c77e33534df91802f7d45110231baa3_MD5.jpeg]]


# 2 基本使用

![[00 assets/c3542a3bac4ecbd7f3e8d898c6c0747d_MD5.jpeg]]

1、可以打包成浏览器环境可以使用的代码，参考上图的指令，可以将我们的库文件打包成不同版本的库
![[00 assets/01d3d1ac6c2f1bc2e60dd6c033b7baf4_MD5.jpeg]]

2、这里有意思的是针对 `umd`版本的打包，他会在执行的时候判断当前的环境
![[00 assets/a00fe3d05130b2471742490ff39657d1_MD5.jpeg]]

3、我们也可以编写一个 `rollup.config.js`来做为配置文件
4、`input`表示入口文件，`output`表示出口，并且可以编写为一个数组，来打包出不同版本的库
![[00 assets/88dc5b10d6bda19b4721ae2e7e56491b_MD5.jpeg]]

# 3 第三方库导入

1、我们导入 `lodash` 来导入，但是不做配置是导入不进来的，所以需要做额外的配置

2、又因为`lodash`是`commonjs`来导入的，但是`rollup`默认处理`es module`，那么就不会将代码打包进来，我们需要额外安装一个`rollup`插件来处理
![[00 assets/7fa7ebe01c5c83ca2e8cc569c14891be_MD5.jpeg]]
3、按照如下配置就可以实现针对一系列库的实现
![[00 assets/200afb4c1d62dab44d831d3e634ce156_MD5.jpeg]]

4、那么我们就需要思考为什么导入不进来？

其实是因为 Rollup 默认只能解析导入的相对路径，也就是 `/`，`./` 或者` / 开头` 的路径，对于`bare impsrt`，也就是 `import chunk from lodash-es` 这种直接导入的第三方包的格式，并不支持

`rollup` 相比 `webpack` 最大的优势并不是构建一个足够大的应用打包，大多是情况下，我们使用`rollup` 用来构建工具库，因此，这里导入的 `lodash-es` 并没有报错，而仅仅报出警告，因为`rollup` 认为 `lodash-es` 这个库并没有加入构建，那么你的意思是将来用作第三方库来使用，因此将 `lodash-es` 使用配置 `external` 排除掉就好

`lodash-es` 这个包本身就是支持ESM的

最后打包好的 `index.js` 文件只所以在 `nodejs` 环境下运行，是因为 `nodejs` 可以帮我们解析`bare import`，我们可以试着将 `index.js` 放入到 `html` 文件中运行，你就可以看到其中的问题所在，在html环境中就会报错了


# 4 资源处理

## 4.1 JS

1、执行 `pnpm i @babel/core @babel/preset-env @rollup/plugin-babel rollup-plugin-terser -D`下载所需的库
2、下述主要是针对`js`进行转换和压缩，使用的`babel`和`terser`，可以详细参考使用库的文档来进行配置即可
![[00 assets/e5ab4610ba3a4d1fbe8498b994bc77ec_MD5.jpeg]]

## 4.2 CSS

1、安装 `pnpm i postcss rollup-plugin-postcss -D`来安装所需要的库
2、导入所需要的即可，需要的类似前缀、压缩等内容，可以查看`postcss`的文档
![[00 assets/f0e8ee0b44e4f1d80134d97133a129bf_MD5.jpeg]]

## 4.3 Vue

1、安装`pnpm i rollup-plugin-vue rollup-plugin-replace @vue/compiler-sfc -D`
2、按照如下配置就可以将`vue`的代码进行编译
![[00 assets/619ab00747e379b9578deca9756e03d4_MD5.jpeg]]

3、但是目前的打包会存在如下的问题，这里使用`rollup-plugin-replace`将配置的环境变量替换
![[00 assets/04476645bc2a94a716bb2cada26542d3_MD5.jpeg]]


# 5 开发服务器

![[00 assets/d86d835ac865349f6742845adfa8cccf_MD5.jpeg]]

1、按照如下的配置即可完成服务器的搭建
![[00 assets/4daf7b8fcf2c1bd89eae605172026589_MD5.jpeg]]


# 6 区分环境

1、我们可以传入`NODE_ENV`的环境变量，在打包和开发的时候可以读取到这个变量再来区分配置
![[00 assets/75bf8e79ebeea9d50511e7d2ff37b384_MD5.jpeg]]

# 7 常见配置

中文官网：[配置选项 | rollup.js 中文文档 | rollup.js中文网](https://www.rollupjs.com/configuration-options/#output-manualchunks)



# 8 JavaScript API

中文官网：[JavaScript API | rollup.js 中文文档 | rollup.js中文网](https://www.rollupjs.com/javascript-api/)

1、在整个构建阶段，他就分析了文件之间的关系
![[00 assets/1dfba31e2bc92c3da8ad2959b59136a3_MD5.jpeg]]
我们也可以输出整个的 `ast` 树
![[00 assets/e18497289b18e403737ed2ae53399e3b_MD5.jpeg]]

2、针对 rollup 分析出来的 bundle，我们可以使用 `generate` 来向内存中生成对应的代码
![[00 assets/1f19ca09c53e077d71b962a09c572aec_MD5.jpeg]]

3、当然我们也可以使用 `write api` 他和 `generate` 的本质区别就是他会主动的将文件写到本地磁盘中，但是 `generate` 就是生成到内存中
![[00 assets/9bee97b1e15e827bf54aff07ac6fdc5b_MD5.jpeg]]

4、还有 `watch` 可以监听打包的流程，如果文件发生了变化就重新打包
![[00 assets/696b33afde8ca975c3a2e5f122c87f21_MD5.jpeg]]


# 9 插件开发

## 9.1 基本介绍

中文官网：[插件开发 | rollup.js 中文文档 | rollup.js中文网](https://www.rollupjs.com/plugin-development/)

1、其实针对插件来讲，那么多的钩子函数基本分为2个 `构建`、`输出`，也就是 `JS API` 中的 `rollup.rollup(init)` 和 `rollup.generate(output) / rollup.write(output)`

2、并且钩子函数的执行是按照顺序的
![[00 assets/bfc462631699dc6ed05a631c9d53e742_MD5.jpeg]]

3、在构建的初始化时有2个钩子函数，也就是 `options` 和 `buildStart`
![[00 assets/ef4ce054b1edffc9d9a8cbd4891f046b_MD5.jpeg]]
钩子函数也可以使用对象的形式来编写，这样编写可以添加额外的配置
![[00 assets/fdd06220a8a86362aba175cd70c07d4f_MD5.jpeg]]


## 9.2 构建流程图

1、各个 钩子函数 之间都存在一定的执行顺序，也就是 `resolvedId -> load -> transform -> ...`，具体可以参考流程图的顺序
![[00 assets/3628d4a176c9a7cb02b3c34f38b1dd4d_MD5.jpeg]]
还会在 `moduleParsed` 来做模块的分析
![[00 assets/54adc237f3c2f2b459356004dc57535a_MD5.jpeg]]

2、整个就是针对 `rollup` 整个打包构建的流程，会走 `options -> buildStart -> resolvedId -> transform -> moduleParsed` 如果分析模块还有导入就会重新走 `resolveId -> load -> ...` 直到发现没有导入了，如果发现存在 `import()` 导入，就会使用 `resolveDynamicImport`，然后再走到 `resolveId -> load -> ...` 
![[00 assets/2640e65dac5a387e945988e65522c185_MD5.jpeg]]

## 9.3 输出流程图

1、其实和构建差不多的流程 `outputOptions -> renderStart` 一个是刚刚初始化，另外一个则是分析之后的处理
![[00 assets/d2415e169403a7620cf0c3b92669e839_MD5.jpeg]]

2、顺序大致是 `outputOptions -> renderStart -> 如果有 import() 就是 renderDynamicImport -> banner / footer / intro / outro 本质就是在文件的头部和尾部添加内容，可以参考文档 -> renderChunk 是生成 chunk 文件的时候做处理 -> augmentChunkHash 如果文件有处理 hash 的话执行 -> generateBundle 打包完了，还没准备写 -> writeBundle 准备开始写`
![[00 assets/a8f221712cb85fdb0bc154f70ed9e017_MD5.jpeg]]


## 9.4 插件开发

### 9.4.1 虚拟模块

1、这个插件的本质就是将写有 `vitual-module` 的模块输出为 `export default 'Hello World!'`
2、虚拟模块本质是在本地磁盘是不存在的，只在内存中存在，在模块处理的时候手动将该模块输出为自己编辑的代码
![[00 assets/13219d79a29fd8f90e89482a8e0626cb_MD5.jpeg]]

3、最终输出的代码如下
![[00 assets/06eae2bb46a041b04315c3a73701b5e4_MD5.jpeg]]

### 9.4.2 json解析

1、如果是插件开发的话，官方也提供工具包可以使用：[plugins/packages/pluginutils](https://github.com/rollup/plugins/tree/master/packages/pluginutils)
2、最终编写的插件如下图，在 transform 中做的代码转换的工作。在 钩子函数 中提供了上下文可以使用，比如说常见的 `this.error` 表示错误提示等
3、我们将 `json` 转为 对象 的形式输出
![[00 assets/cd403804d1832703a5bf6dabf5454d9a_MD5.jpeg]]

4、最终结果如下
![[00 assets/588d5883b88f4f072407d496dfa94f79_MD5.jpeg]]

### 9.4.3 图片解析

1、rollup 无法处理图片，这里就不再写了其实和 `json解析` 是差不多的，下面只说一下大致的思路

2、在 `transform` 钩子函数中如果找到图片就查看配置中的限制文件大小，如果超出文件大小就复制图片到指定路径，然后将返回 `code` 为路径即可，如果没超出就转为 base 返回


