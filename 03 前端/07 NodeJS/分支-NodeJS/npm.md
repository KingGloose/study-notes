# 1 基本介绍

![[../../../00 assets/1c782cc6cdeac87756ad36a4f0f789a4_MD5.jpeg]]

**npm 官网**：[npm (npmjs.com)](https://www.npmjs.com/)。具体的`npm`使用可以参考我**以前的笔记**

1、如果可以的话可以查看下面的指令

```bash
node -v		// 查看nodejs版本
npm - v		// 查看npm版本

npm install npm -g // 安装最新的npm

npm update jquery 		//更新jquery
npm uninstall jquery	//卸载jquery
```

2、并且这里存在一个`Windows`的问题，我们使用`-v`查看包版本的时候，都是查看当前文件夹下处理命令，并不会去`子文件夹`下去查看，所以我们查看的所有包版本都是查看的`全局版本`。

假如要查看当前项目中的版本可以使用下面的方法，方法一：进入`node_modules/.bin`文件夹中查看版本。方法二：使用`npx`工具查看，因为`npx`就是在导入到`node_modules/.bin`中进行执行





# 2 项目配置文件

![[../../../00 assets/a15f7e93b0121dbb5c1054b225f1051b_MD5.png]]

下面就是`Vue cli4`、`Vue cli2`和`自己创建的文件`的配置文件的信息

![[../../../00 assets/52e167ee193e5d06a3880a2ef2f8a26b_MD5.png]]

当然现在很多包都有自己的非标字段，可以参考下面的视频：[开源库中的 package【渡一教育】-村头一只鹅鹅-稍后再看-哔哩哔哩视频 (bilibili.com)](https://www.bilibili.com/list/watchlater?bvid=BV17s421N7qF&oid=1854283439)

# 3 常见的属性

## 3.1 基础属性

![[../../../00 assets/cef56077f0f9b873dc02fff9adce6aef_MD5.png]]

![[../../../00 assets/2d062ec304c8917d0fc112b4fe99508e_MD5.png]]

## 3.2 private

![[../../../00 assets/7f35568169381d11425dbe3a7c3ed6af_MD5.png]]

当我们在`package.json`中配置了`private`为`true`的话就可以设置该项目为私有的

![[../../../00 assets/8a189a3c76172f9b4e34d8be233c0301_MD5.png]]

## 3.3 main

![[../../../00 assets/c2a99ba88847da19eba86cd1c9444faa_MD5.png]]

这个`main`属性可以设置程序的入口，我们在自己写的项目中用处不是很大，因为大部分的操作都是使用`webpack`来操作的，所以我们设置这个属性没啥用。

但是在你要发布的`npm`项目中就需要这个配置来作为入口，假如你不写的话可能别人下载你的包就不会被执行，来执行后续的操作

![[../../../00 assets/b590347e2f991e755d35e846caffd570_MD5.png]]

## 3.4 scripts

![[../../../00 assets/08fd534ec25bededb05cf7c799640429_MD5.png]]

1、下面就是配置`scripts`中的信息

![[../../../00 assets/ba790261964e651521a751ffb53dc8c5_MD5.png]]

2、假如我们在`script`中配置`start,test,stop,restart`就可以省略`run`，直接输入`npm start`...

![[../../../00 assets/9ae9dca517290a4e2f068a02fa034b52_MD5.png]]

3、我们配置`scripts`属性的时候，可以不写`npx`或者`npm`的，因为我们配置之后会默认在该项目的`./node_modules/.bin`文件夹下面寻找。这一点非常重要，因为我们在查看`包版本`的时候就需要使用到这个知识

![[../../../00 assets/ae9c92ab9121ff6049a4feade2df8ac5_MD5.png]]

## 3.5 dependencies

![[../../../00 assets/44ac285d90024d588853fc7185a4ee4b_MD5.png]]

其实在真实的开发中和`main`是一样的，基本不用区分这个 2 个属性，只要我们的项目中依赖了这个包`webpack`就会自动打包进去。

这个属性的真正意义是在自己发布`npm`包的时候使用，使用者可以使用`npm i --production`来安装生成环境的包，这样开发者可以节省了安装的时间

## 3.6 engines

![[../../../00 assets/0bd66424afc2e68bffbd606dc339ce1c_MD5.png]]

## 3.7 browserslist

![[../../../00 assets/256da5561bbb3b3b31ac5391999a04af_MD5.png]]

# 4 版本管理

我这里例举几个版本号：`^2.1.3`、`~2.1.2`

`2`表示大版本更新，`1`表示功能更新，`3`表示问题修正。`^`表示功能会更新，`~`表示功能不更新

![[../../../00 assets/6214567ca4b9c8bd99052eb98105a55d_MD5.png]]

**npm**遵循下面 2 种方式来区分版本号

**semver**：https://semver.org/lang/zh-CN/

**npm semver**：https://docs.npmjs.com/misc/semver

# 5 npm i

## 5.1 基本使用

![[../../../00 assets/066f570e59dd242d6cfc6b6d11f3e204_MD5.png]]

下面的 3 种模式都是可以的，无非就是写法的不同

![[../../../00 assets/74360cdca1c65acd5aa12e2c4bf97459_MD5.png]]

![[../../../00 assets/15dd50a9eabd5de0383ce65d0b83ff1a_MD5.png]]

还有很多的命令需要的时候可以查看官网：[CLI Commands | npm Docs (npmjs.com)](https://docs.npmjs.com/cli/v8/commands)

```bash
npm i axios@1.1.2 // 安装特定的版本
```

## 5.2 全局安装误解

![[../../../00 assets/9aa02dd3252d8f3e7d81121f6b673cf0_MD5.png]]

其实我也有这样误解：**首先全局安装不等于全局引用**，你全局下载的包不一定会被全局引用。这里打个比方：你全局安装了`jquery`，这个包会放置在`C:\Users\张嘉辉\AppData\Roaming\npm\node_modules`路径下

如果你使用了 nvm 来做 node 版本管理得话，可以在 nvm/node_modules 下面来寻找

![[../../../00 assets/f52fb7ecd5baa1bd6dccd50d52a8e14e_MD5.png]]

但是你引入的时候，不可能引入到这个文件，除非你修改`npm`的全局路径。并且你会发现下面的路径根本和上面对不上，所以也不存在找到这一说

![[../../../00 assets/97167d7ccaf67839cedbe3d6a8c405a2_MD5.png]]

但是，为什么全局安装工具就可以找到呢？这是因为你全局安装的是工具库的话就会自动在 node 在根目录下生成`cmd`可执行文件，假如你是安装的`jQuery`、`axios`...这种的，就不会生成可执行文件

![[../../../00 assets/90a1b37fbfcc2b58b74a3a9d3788f02d_MD5.png]]

并且还配置了环境变量，所以我们在任何一个终端输入名字就可以定位到这里来执行。

![[../../../00 assets/5545f56c9f965c5d3dc861f28f844e87_MD5.png]]

## 5.3 npm i 原理

![[../../../00 assets/5bf47de7b2857a78b0687b03841dd9f1_MD5.png]]

这里的构建依赖关系是因为一些包可能会重复依赖一个包。比如`webpack`和`aixos`同时依赖一个包的情况下，就会对让他们直接引入这个包，这是以前的依赖方式，就是一个树形结构。但是现在就是扁平化的模式，你引入的包都摊平在一起

![[../../../00 assets/0673bf560b48539d76c80859d017f7c5_MD5.png]]

下面就是有无`package.lock.json`的描述

![[../../../00 assets/25a6dda1391ec8f0317c95f53934e78a_MD5.png]]

我们安装`axois`可以发现，其实他也会安装其他的依赖

![[../../../00 assets/482f5080576d58919f69395bb55b005c_MD5.png]]

我们再来看`axios`中的依赖`form-data`，里面也会引入其他的依赖

![[../../../00 assets/9ff89e686f43d40bd460014ff0733971_MD5.png]]

## 5.4 package-lock.json

![[../../../00 assets/4fd471a92a22612697dfff81759b11ec_MD5.png]]

但是最新的版本中会有一个`packages`的属性，官网对这个属性的解释：[package-lock.json |npm Docs (npmjs.com)](https://docs.npmjs.com/cli/v8/configuring-npm/package-lock-json#packages)。个人理解：可能是为包的名字打上属性

![[../../../00 assets/d466c9470a1d3b61619aba9bd90c6a4a_MD5.png]]

我们在这里就会发现`package-lock.json`文件的作用了，原本的`package.json`文件只能记录你安装的包的版本，但是不会记录依赖的依赖的版本，下面的`follow-redirects`有 2 个不同的版本，虽然只是功能的升级。所以在传递代码的时候记得带上`package.lock.json`文件，不然会导致安装的版本不同

![[../../../00 assets/33a47a531543682d56168af622bc321a_MD5.png]]

## 5.5 缓存机制

具体也可以参考这个文章：[深入浅出 package-lock.json - 简书 (jianshu.com)](https://www.jianshu.com/p/5c877c5c5bc3)

我们输入下面的命令可以查看`npm`的缓存文件的位置

![[../../../00 assets/db1f3df91fbcfbea774ca3d73f46da13_MD5.png]]

我们打开文件夹之后，进入`npm-cache`就可以进入该文件的缓存目录了。其中`index-v5`就是`content-v2`的索引

![[../../../00 assets/e4d03101289ee71d3835678a7dad4f03_MD5.png]]

我们随便打开`index-v5`其中的一个索引就会发现里面对应的是一个文件，通过算法来查找这些文件。

![[../../../00 assets/4e7884a85afc186e87866cd100612054_MD5.png]]

我们将这些文件加上`.tgz`的后缀进行解压其实我们缓存中的依赖了

![[../../../00 assets/626dfe78cb7936bcfbc078ba618334a4_MD5.jpeg]]

## 5.6 完整性校验

[npm 完整性校验](npm%20完整性校验.md)


# 6 yarn

![[../../../00 assets/fa43163925dc00205b9b0e62dc097f90_MD5.png]]

假如我们需要使用`yarn`来安装依赖的话

```bash
npm i yarn -g
```

下面就是`yarn`和`npm`的命令的关系图，其实`yarn`和`npm`是差不多的

![[../../../00 assets/442702fdd48873d4e102878814434878_MD5.png]]

# 7 cnpm

![[../../../00 assets/42b9ba69acaa3fc15386a315c90bc1ab_MD5.jpeg]]

# 8 npx

![[../../../00 assets/7dd4bc9a79c5572585bb338e7d79cc54_MD5.png]]

1、假如我们需要全局安装`webpack`的话需要输入`npm i webpack -g`和`npm i webpack-cli -g`

这个时候我们在局部来安装`webpack`，再使用`webpack -v`来查看该工具的版本，很显然调用的是全局的`webpcck`，那要怎么才能使用局部的`webpack`呢？

![[../../../00 assets/cacc3024bc1a9ac3eefbc11ee0fa4e2b_MD5.png]]

假如我们要执行局部的`webpack`，其实本质就是执行`node_modules/.bin/`下面的`webpack`文件

![[../../../00 assets/cdfb4c398f6073e8195a8989177d10db_MD5.png]]

所以就会出现下面的 3 种方式来执行局部的`webpack`。这里要说下第二种方式，在`package.json`中配置`webpack`的话，会默认在最近的`node_modules`中去执行

![[../../../00 assets/92de8e055d23a96a8e2bfb702540b295_MD5.png]]

2、但是这里存在一个特殊的情况，我们在查看`webpcak`的版本的时候就会一直查看全局的`webpack`版本。即便你在`node_modules\.bin`中或者使用`npx`查看版本也会查看全局版本

并且因为`VSCode`权限问题，所以我们要查看`webpack`版本需要使用`管理员权限`，并且上述问题都是只有`webpack`才存在的问题

![[../../../00 assets/3ce8c398f38b81b28712cea504f31f43_MD5.jpeg]]


# 9 发布项目

![[../../../00 assets/0b1f1e53ab6bb0c8d03da556a3b7671a_MD5.png]]

假如你要发布的话，可能还需要注意下面的 4 个属性

![[../../../00 assets/a63e80178cc6585836541297a51133d1_MD5.png]]

另外还需要一个`readme文档`，假如在项目里包含`readme文档`的话，到时候查看我们的项目就会在主页显示文档

![[../../../00 assets/677140fcef310f3af92322110bf9eea5_MD5.png]]

按照如下的方式可以发布镜像Ï

> 查看镜像

```bash
npm config get registry		//registry表示登记
npm config get disturl
```

> 配置镜像

```bash
npm config set registry http://registry.npm.taobao.org --global
npm config set disturl http://npm.taobao.org/dist --global

npm config set registry http://registry.npmjs.org --global	//切换到原生的地址
```

当然我们不仅仅使用网址来配置，还可以使用`npx`

```bash
npx nrm use taobao	//nrm切换为淘宝源
npx nrm use npm //切换为官方源
```

使用`cnpm`来配置，这样的话就可以使用淘宝的镜像来下载了

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

我们再来查看 cnpm 的版本

```
cnpm -v
```

有的时候 cnpm 会有一系列的问题，所以我们使用下面的方式来使用淘宝镜像来下载

```
npm install --registry=https://registry.npm.taobao.org
```
