# 1. 基本介绍

![[00 assets/0c77e33534df91802f7d45110231baa3_MD5.jpeg]]


# 2. 基本使用

![[00 assets/c3542a3bac4ecbd7f3e8d898c6c0747d_MD5.jpeg]]

1、可以打包成浏览器环境可以使用的代码，参考上图的指令，可以将我们的库文件打包成不同版本的库
![[00 assets/01d3d1ac6c2f1bc2e60dd6c033b7baf4_MD5.jpeg]]

2、这里有意思的是针对 `umd`版本的打包，他会在执行的时候判断当前的环境
![[00 assets/a00fe3d05130b2471742490ff39657d1_MD5.jpeg]]

3、我们也可以编写一个 `rollup.config.js`来做为配置文件
4、`input`表示入口文件，`output`表示出口，并且可以编写为一个数组，来打包出不同版本的库
![[00 assets/88dc5b10d6bda19b4721ae2e7e56491b_MD5.jpeg]]

# 3. 第三方库导入

1、我们导入 `lodash` 来导入，但是不做配置是导入不进来的，所以需要做额外的配置
2、又因为`lodash`是`commonjs`来导入的，但是`rollup`默认处理`es module`，那么就不会将代码打包进来，我们需要额外安装一个`rollup`插件来处理
![[00 assets/7fa7ebe01c5c83ca2e8cc569c14891be_MD5.jpeg]]
3、按照如下配置就可以实现针对一系列库的实现
![[00 assets/200afb4c1d62dab44d831d3e634ce156_MD5.jpeg]]


# 4. 资源处理

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


# 5. 开发服务器

![[00 assets/d86d835ac865349f6742845adfa8cccf_MD5.jpeg]]

1、按照如下的配置即可完成服务器的搭建
![[00 assets/4daf7b8fcf2c1bd89eae605172026589_MD5.jpeg]]


# 6. 区分环境

1、我们可以传入`NODE_ENV`的环境变量，在打包和开发的时候可以读取到这个变量再来区分配置
![[00 assets/75bf8e79ebeea9d50511e7d2ff37b384_MD5.jpeg]]