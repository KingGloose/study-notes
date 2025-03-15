前端系统课 - coderwhy - uniapp

# 1. 基本介绍

## 1.1 跨平台认识

> 基本介绍

![[00 assets/58992f0e055bfc77fca4da6bf486a73f_MD5.png]]

> 原生 vs 跨平台

![[00 assets/85ea5128e70fb9ea72ecffd723a02929_MD5.png]]

> 跨平台发展史

![[00 assets/68debc2cc68a3e99d731f3f7c71bb644_MD5.png]]

> 跨平台对比

![[00 assets/638429ffbc702c8a93a66488104718cf_MD5.png]]

## 1.2 uniapp 理解

> 认识 uniapp

![[00 assets/c5f1fb96913e637dabe933cd57dd0903_MD5.png]]

> uniapp vs 微信小程序

![[00 assets/21cdf313784f3100a67cd2193065e7bc_MD5.png]]

> uniapp 架构图

![[00 assets/d19fc6fe506ee92c156b9cb041efd756_MD5.png]]

## 1.3 环境配置

![[00 assets/0591a53a4516a897d8ab4b2d9999d1e9_MD5.png]]

![[00 assets/82e2265f27367f2768a75a1adee5b8a0_MD5.png]]

### 1.3.1 网页运行

![[00 assets/dec63039a56c1fddc7f985ff3d3f7648_MD5.png]]

### 1.3.2 微信小程序运行

1、我们需打开微信小程序的`服务端口`

![[00 assets/a6408449006be208fe98c6272460f12c_MD5.png]]

2、在`uniapp`中配置`微信小程序`的运行，配置相关路径即可

![[00 assets/a1fb179a45a7ebd0f5144eff622c6e9f_MD5.png]]

3、如果不想使用`uniapp`来打开微信小程序，也可以手动在`微信小程序开发工具`打开下面的文件夹，也是可以运行

![[00 assets/dbcfe5e32cfa75d5987c783f9d6f5296_MD5.png]]

### 1.3.3 Android 运行

![[00 assets/68debc2cc68a3e99d731f3f7c71bb644_MD5.png]]

1、下载/安装`mumu模拟器`

2、我们设计程序的时候基本都会参考`iphone6`的比例，所以我们将模拟器设置为下面的宽高

![[00 assets/b52e658b347cb825f6b8bf16f01ce26e_MD5.png]]

3、为了将`uniapp`输出的程序安装到模拟器中，所以需要设置`adb`调试桥

4、对应的移动端开发安装，参考`uniapp`文件夹中的`移动端搭建`文档来安装

```shell
# mumu模拟器
# 每次运行到模拟器中都需要执行下面的命令
adb connect 127.0.0.1:7555 # 配置链接的端口
adb devices # 查看配置是否成功
```

5、如果`mumu`多开想要使用`adb`来连接，需要进入到`.../shell`页面输入下面的指令`MuMuManager.exe adb -v 1`，其中`1`表示的躲开模拟器的序号，第 0 个默认是`7555`

![[00 assets/38c7e88169284455ec5a8c52d9c049bc_MD5.png]]

## 1.4 目录结构

![[00 assets/b552e3ff49695d2f0bcaf43f8d959143_MD5.png]]

这是我目前创建的项目的目录结构

- `main.js` -> 入口文件

- `index.html` -> html 模板

- `App.vue` -> 入口组件

- `manifes.json` -> 配置文件

- `pages.json` -> 类似微信小程序中的`app.json`

- `uni.scss` -> uniapp 内置组件样式变量
- `unpackage` -> 是各个平台运行打包之后的文件

剩下的基本和其他的框架目录同理

![[00 assets/ea170c1041d47c4cda93bd5991f8d79c_MD5.png]]

## 1.5 开发规范

![[00 assets/d74037142ff914f1718309e8a2ace724_MD5.png]]

# 2. 基本文件

## 2.1 main.js

![[00 assets/5d8aa372cf6379781a6adf8fc969c997_MD5.png]]

1、这是我目前项目中创建的`main.js`中的文件

2、其中`#ifndef`标识区分不同的编译环境，在上面有介绍

3、剩下的状态管理和路由可以参考我后面的笔记

![[00 assets/b75c707b8855e65ff804094bc1c1e35a_MD5.png]]

## 2.2 App.vue

![[00 assets/b4435737125d96acb52ef1f62eb57a50_MD5.png]]

### 2.2.1 页面生命周期

官方文档：[页面简介 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/page.html#lifecycle)

1、对于`uniapp`来说，存在很多的生命周期，因为它支持多端同步代码

2、而且和小程序一样，分为`组件生命周期`和`页面生命周期`，下面为比较常见的生命周期钩子

![[00 assets/11fe083104c1a3b2fee3f541d1f27972_MD5.png]]

3、并且生命周期中都会传递参数`options`，这和小程序是一样的

![[00 assets/3f31b97cc938c419819c66485a73e691_MD5.png]]

4、因为支持多端同步，所以一些生命周期钩子都会存在差异，这个就需要参考官方文档了

![[00 assets/83b7eb48a5689d7d7ba557351d1f828b_MD5.png]]

### 2.2.2 全局/局部样式

![[00 assets/3610aa1fcc3e91b85907e17f50ed7e10_MD5.png]]

![[00 assets/ee5122fa708c2cc63a48f850427cfba7_MD5.png]]

#### 2.2.2.1 全局样式

> App.vue

1、如果在`App.vue`中的`style`中不编写`scoped`的前提下，里面编写的样式默认是在全局使用的

![[00 assets/3e4486dd122b6958997e231e5549f767_MD5.png]]

2、我们也可以将这些样式都抽取到外部使用，并且使用`@import`来引入

![[00 assets/89f0819c1fd63508549ef7c064ea90e7_MD5.png]]

![[00 assets/8b834b43389b0b4307b6d4a5526d5144_MD5.png]]

因为可以抽取外部的话，对应的`CSS`变量也是可以使用的，并且`uniapp`默认就是支持`scss`

![[00 assets/477050a98a7934b9bebf34f37b99f85d_MD5.png]]

> uni.scss

1、该`.scss`文件也可以设置全局的样式，但是大部分都是使用下面的 3 个功能

![[00 assets/98ad54a4a3b17dab9b79ba429ce864ab_MD5.png]]

2、我们如果需要使用`uniapp`的跨平台功能，最好就是使用它提供的语法。我们查看`web`端就可以知道，下面是内部定义的组件

![[00 assets/6d05521b7fa844b5c6440a1f1ef3e08b_MD5.png]]

#### 2.2.2.2 局部样式

1、对于局部样式不需要写`scoped`，可以直接使用

![[00 assets/3d087b7cb3f111ff7958b60713ff0a52_MD5.png]]

### 2.2.3 全局数据

![[00 assets/3b8d9780bd18bbc30491a347a2969ed8_MD5.png]]

> 全局数据 - globalData

1、在`app.vue`中定义的全局变量，可以使用`getApp()`来调用，这个其实和小程序中的使用方式是一样的

![[00 assets/c3ee5c9f8bd634ab904c80ae388bdb51_MD5.png]]

> 获取当前路由

1、可以使用`getCurrentPages()`来获取当前页面的路由信息

![[00 assets/786ef392f635a9f2fa607920cf811f79_MD5.png]]

2、所以对于这种`API`其实可以引申一下，因为`uniapp`已经帮我们写好了，所以直接调用它写好的`API`就可以实现跨端的编写。但是我不使用它的`API`呢？很显然，可以使用，但是不能实现跨端的使用

## 2.3 page.json

### 2.3.1 基本使用

![[00 assets/b1ea969c86248ca4b87f607336518855_MD5.png]]

官方文档：[pages.json 页面路由 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/collocation/pages.html#pages)

1、该配置可以参考微信小程序中的`app.json`文件，基本都是一样的

![[00 assets/315d74c2d7b2837e83791a7b28f02c83_MD5.png]]

### 2.3.2 tabbar

官方文档：[pages.json 页面路由 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/collocation/pages.html#tabbar)

1、如果想要配置`tabbar`的话可以参考文档的`API`，下面只是一个示例代码

![[00 assets/e50276f2689ad99e4213e1db6cf30dcf_MD5.png]]

## 2.4 manifest.json

![[00 assets/a18b1e00d8a8f336657ffcd16c32ec5d_MD5.png]]

# 3. 内置组件

![[00 assets/adddd1a60dfe683ef7f579b877e62dd8_MD5.png]]

1、上面介绍都是比较常见的内置组件，但是使用的方式基本和微信小程序类似

![[00 assets/dbb8846b7af4ebfc10877108d7b6472f_MD5.png]]

![[00 assets/b9382a86d127af4547343e4bc69e3325_MD5.png]]

![[00 assets/5fc58bfc87a48d73cc673e2b7dad3750_MD5.png]]

2、如果你想要隐藏滚动条的话使用下面的方式来编写全局样式

![[00 assets/b0ca19ed47807fe9c5fbde5c576ab0b0_MD5.png]]

# 4. 扩展组件

## 4.1 基本介绍

![[00 assets/a8e708adeb7978fde9303ba9c7cd4a82_MD5.png]]

## 4.2 导入使用

### 4.2.1 导入组件

![[00 assets/98d3b5a5e9aaa04ed34687207a3f4c4c_MD5.png]]

> 方式一 - 通过 uni_modules 单独导入

1、我这里使用方式一来按照组件，我们点击官网找到自己想要的组件

![[00 assets/d8d3728e881bd0114ef5866b1326e42e_MD5.png]]

进入之后点击下载插件并且导入项目即可

![[00 assets/a7ad4b843dd334f25dc3ec4b42e06e9d_MD5.png]]

> 方式二 - 通过 uni_modules 全部导入

1、我们进入官网：[uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/component/uniui/quickstart.html)，点击导入会进入到插件页面，和上面一样点击下载插件即可

![[00 assets/f7b0be2acff8acf2eb126c5cc607835c_MD5.png]]

2、或者在一开始创建项目的时候就引入，这样就不需要后续手动安装

![[00 assets/66b0b5f1994ab5e1c8c6db6e49cf11b7_MD5.png]]

### 4.2.2 使用组件

1、对于这些扩展组件不需要导入直接使用，并且支持跨平台使用

![[00 assets/0f97a9b6b0c9f404bb0491d68b4a33b2_MD5.png]]

下面分别是 H5、微信小程序、安卓，基本都能完美运行

![[00 assets/3d087b7cb3f111ff7958b60713ff0a52_MD5.png]]

## 4.3 定制主题色

官方文档：[uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/component/uniui/uni-sass.html)

1、我们需要重写样式就需要引入`uni-scss`的文件，才能进行重写

![[00 assets/efef93845dd2e0bb54ce3aa391a57a4b_MD5.png]]

2、更加详细的重写参考官网即可

## 4.3 uni-forms

### 4.3.1 基本使用

![[00 assets/d127998280b159205204c1860090d707_MD5.png]]

1、对于`uni-forms`的使用基本和`elementui`中的表单元素使用是一样的，下面介绍的就是最基本的使用方式

![[00 assets/bd24c17b09038e7803fbdcda7eccf00b_MD5.png]]

2、这是作为一个表单最基本的`HTML结构`

![[00 assets/fc686feb6a6842cd3e7918b5a4322c3a_MD5.png]]

这里是对应的逻辑部分，因为需要使用到`form`内部的方法，我们需要获取它的`ref`

![[00 assets/631d0685f0e623635ea8cfa4f768ab16_MD5.png]]

### 4.3.2 重写样式

![[00 assets/f33dd20b380b32f4dee6a096ccc15e26_MD5.png]]

1、我们使用控制台查看元素的类名

![[00 assets/b07fefac42fb206969c3892ad955a500_MD5.png]]

2、我们通过下面的 3 种方式都可以生效，并且需要注意一定要加上`!important`

![[00 assets/3300a45bdbd0084c4da015339ddc8b1e_MD5.png]]

# 5. Page 页面

## 5.1 创建页面

![[00 assets/e43ce755fa8472399867b1d1e59eaaa2_MD5.png]]

1、这个和`微信小程序`不一样，直接在`app.json`写是不会创建的，而是需要通过`Hbuildx`来创建

![[00 assets/9478b55eecc9f9decfc75f2f2f43ff4b_MD5.png]]

2、和微信小程序的路由类似

![[00 assets/7e8ce661a8fee3753ad4241484df0b58_MD5.png]]

## 5.2 页面路由

![[00 assets/7ef128479e8c5aa41c4a0f93acb54b8c_MD5.png]]

1、这里基本和微信小程序类似，剩下其他的跳转的`API`类似使用即可

![[00 assets/bbd134d9edce752228a80c77993895c7_MD5.png]]

2、或者直接使用路由组件也可以实现跳转的功能，但是大概率使用场景不是很多

![[00 assets/0b04d74e4f62fc8052bbcec783136370_MD5.png]]

## 5.3 页面通讯

![[00 assets/e794cbe413789f3a13a68498b5e88de1_MD5.png]]

### 5.3.1 路由传递参数 - setup 语法糖

1、语法上来讲基本和微信小程序是一样的，这里就不去赘述了

![[00 assets/e1b808a5b01aa2f530dc4c4167793838_MD5.png]]

> 解析路由参数

官方文档：[组合式 API（Composition API） | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/vue3-composition-api.html#使用组合式api)

2、但是这里有一个比较奇怪的点，对于`Vue`来说是存在`mounted,ready......`等生命周期的，但是对于`uniapp`来说是不存在的，所以我们需要使用官方提供的`API`来实现跨平台的生命周期

3、但是对于`Vue`的`OptionsAPI`来说是可以直接使用的，但是对于`ComponsitionAPI`来说需要进行额外的操作才可以

4、我们需要导入对应的`API`才可以使用

![[00 assets/ae4c7b0ae25ed8ef6f29b2eae0d665f6_MD5.png]]

在对于的`onLoad`生命周期钩子中的`options`可以获取

![[00 assets/8a57a8266bd6bccfcfebbf9ddcc23482_MD5.png]]

5、我们也可以使用`props`来获取路由传递来的参数

![[00 assets/c1bb811303992980646e393953183235_MD5.png]]

> eventChannel - 正向传递

官方文档：[uni.navigateTo(OBJECT) | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/api/router.html#event-channel)

1、官方不仅仅支持上面常规的路由参数传递解析的方式，而且还支持`eventChannel`的方式来传递参数

2、对于`OptionsAPI`来说直接参考文档来操作即可，但是对于`ComponsitionAPI`来说需要一些特殊的方式来处理参数的问题，目前官方没有提到可以导入`@dcloudio/uni-app`包来解决

3、下面是目前的解决方式，使用`Vue`原生的方法`getCurrentInstance()`来获取当前实例

参考文档：[vue3 使用 setup 语法糖时$scope 和 getOpenerEventChannel 怎么获取 - DCloud 问答](https://ask.dcloud.net.cn/question/152154)

```javascript
const instance = getCurrentInstance().proxy;
const eventChannel = instance.getOpenerEventChannel();
```

![[00 assets/fa9c9b1ddef6a09ee2c72b99059f6b38_MD5.png]]

并且该方式多端都是可以使用的

![[00 assets/798554790d21055e42eb61fe61ec8db4_MD5.png]]

4、但是也可以使用下面的方式来编写，这是网课老师提供的思路，使用`ref`来包裹

5、因为在外部获取可能`DOM`还没更新，所以不会有值，如果使用`ref`包裹的话就是响应式数据

![[00 assets/f209e268c93236da860d203d216439a3_MD5.png]]

> eventChannel - 逆向传递

1、我们从`页面A`跳转到`页面B`的时候可以传递参数，也就是`正向传递参数`。但是我们也可以将`页面B`的参数传递给`页面A`，这叫做`逆向传递参数`

2、其原理也基本一样，就是使用`EventChannel`来发送事件来实现传递参数

3、对于参数的传递思路基本都是一样的，但是接受的地方不一样

​ `页面A` -> `页面B` ：`success`中发出事件，`页面B`来接受

​ 页面 B -> 页面 A：`页面B`中发出事件，`页面A`中的`events`来接受

![[00 assets/8c3c940b34310344f8aac2004b7a49b3_MD5.png]]

### 5.3.2 事件总线

官方文档：[页面简介 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/page.html#emit)

![[00 assets/b9f1095d682236187924145c39a89617_MD5.png]]

1、使用`uni.$on`来监听该事件，`uni.$emit`来发送事件，`uni.$off`来删除事件

2、基本的时候和之前的事件总线的使用是差不多的

![[00 assets/130fff848d9d1e997422087626c20cae_MD5.png]]

## 5.4 页面生命周期

![[00 assets/e26d68f9ad75bf58ee93048eb9e9d4f9_MD5.png]]

官方文档：[页面简介 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/page.html#lifecycle)

1、下面是比较常见的页面的生命周期

![[00 assets/a96fb8345ea39abbbd46db68195c51ea_MD5.png]]

2、下面是组件的生命周期

![[00 assets/2853149cea774cb7fd3a84af6f0e257e_MD5.png]]

3、但是我们需要使用`setup`语法糖中使用页面生命周期，可以参考`5.3.1 路由传递参数`中的笔记

# 6. API

## 6.1 网络请求

![[00 assets/d5fe152e75ba15d778a2d791e123caa5_MD5.png]]

官网文档：[uni.request(OBJECT) | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/api/request/request.html)

1、对于网络请求基本和微信小程序是类似的，直接套用即可

![[00 assets/585045760e5e0d1870bdaf5e6298bdd1_MD5.png]]

2、但是对于网络请求也和之前一样，直接封装使用

```javascript
class RequestService {
	constructor(baseUrl, timeout) {
		this.baseUrl = baseUrl
		this.timeout = timeout
	}
	request(options) {
		return new Promise((resolve, reject) => {
			uni.request({
				...options,
				url: this.baseUrl + options.url,
				success(res) {
					resolve(res)
				},
				fail(err) {
					reject(err)
				}
			})
		})
	}
	get(options) {
		return this.request({
			...options,
			method: "get"
		})
	}
	post(options) {
		return this.request({
			...options,
			method: "post"
		})
	}
}

export const mallService = new RequestService('http://1.117.220.127:3000', 60000);
```

3、如果是编写`APP`端，使用真机调试的话，可能存在`IP不一致的问题`。因为真机调试时，真机需要进行网络请求，如果还是使用`127.0.0.1`肯定是请求不到的，需要在同一个网下面，使用`ipconfig`查询局域网`IP`来配置即可

参考文章：[uni-app 填坑{“errMsg“:“request:fail abort statusCode:-1“}\_浮沉逆旅的博客-CSDN 博客](https://blog.csdn.net/qq_44046765/article/details/114321312)

## 6.2 本地数据存储

![[00 assets/204577980a92763ba31044af37032caf_MD5.png]]

官方文档：[uni.setStorage(OBJECT) @setstorage | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/api/storage/storage.html#setstorage)

![[00 assets/d638498dd8033d94bc2f835a2cf4d7a5_MD5.png]]

# 7. 自定义组件

## 7.1 基本介绍

![[00 assets/a7b232b39124a7ec3849b42fe0cec4de_MD5.png]]

## 7.2 基本使用

1、其使用的方式基本和之前是一样的

![[00 assets/8bdabec00fefdf40f6ec015535e345e7_MD5.png]]

## 7.3 生命周期

![[00 assets/efef93845dd2e0bb54ce3aa391a57a4b_MD5.png]]

1、下面是`Composition API`中的效果，组件中`页面生命周期`是可以执行的

![[00 assets/29672a525f1af4064257b4b08b52cb7a_MD5.png]]

2、但是在`Options API`中`页面生命周期`是不会执行，所以对于不同`Vue`的语法存在不同的差异

![[00 assets/e135448d0b19b2a177eb2f064f9735d3_MD5.png]]

# 8. 状态管理 - pinia

## 8.1 基本介绍

![[00 assets/d90eeecb6416979c2d4f286187b5fa2f_MD5.png]]

## 8.2 基本使用

1、按照下面的操作来注册

![[00 assets/86c030d7e9786c1cd56f00df8c2fb557_MD5.png]]

2、最后的效果基本也是一样的，直接参考我`Vue`笔记即可

![[00 assets/f43a98032614adac14fa6a5ae05b31a3_MD5.png]]

3、使用基本都是一样的，直接参考之前的笔记即可

# 9. 项目 - 蘑菇街

因为该项目相对来说比较简单，所以我这里只说和之前编写不同的地方

## 9.1 项目搭建

1、下面是项目的目录结构

![[00 assets/3a272d5a46b5bfe44c7f4cf382da538d_MD5.png]]

2、下面是`tabbar`的搭建

![[00 assets/102c9a8022d39d3e3de0f6aea38f761d_MD5.png]]

下面是`头部bar`的搭建

![[00 assets/249751b16102ec31f0540c100eefefeb_MD5.png]]

最后效果是这样的

![[00 assets/867cc68a4d8e3113028b0b0d78e9dba0_MD5.png]]

## 9.2 多端适配 - 条件编译/图片懒加载

1、因为对于图片懒加载官方只提供了小程序端的使用。所以对于`H5`平台的使用需要条件编译

2、这里使用的是`vue3-lazy`库来实现的懒加载

3、`#ifndef`表示非该端的所有平台，`#ifdef`表示该端

![[00 assets/e1bc0bed9a24ca4c6d6e814c6b2b7665_MD5.png]]

## 9.3 项目发布

### 9.3.1 微信小程序

1、我们在`manifest.json`中配置微信小程序的信息

![[00 assets/e6bd4e49ea70831abf54215677445bfb_MD5.png]]

2、填写之后在这里发行

![[00 assets/3f107ab4d1fc308c5829faf71b354714_MD5.png]]

3、最后的发布还是在微信小程序开发者工具中发布的，剩下的发行内容就可以参考之前的笔记了

### 9.3.2 H5 发布

1、参考我之前的代码

### 9.3.3 安卓部署

> 云端证书打包

1、首先来配置一下`App`中的打包配置

![[00 assets/fc686feb6a6842cd3e7918b5a4322c3a_MD5.png]]

2、配置一下`App图标`

![[00 assets/7e760e62ae3b163b618b521555b77fa8_MD5.png]]

配置一下基础信息基本就可以了，后续的其他的配置直接根据情况来选择即可

![[00 assets/942841f0c252d4760d9f35233c7f682e_MD5.png]]

3、点击发行打包即可，这里证书选择云端证书，这个是`ucloud`帮助我们自动生成的

4、使用云端证书之前，一定要登录`uniapp`的账号，并且需要进行认证才能使用

![[00 assets/5df0379b8cf05d06ec852e48c8ac94b8_MD5.png]]

> 手动生成证书

1、可视化手动生成证书需要下载`Android Studio`

2、选择`构建`，然后生成证书，选择`APK`

![[00 assets/33fe4a9ed59052a5271e0edefd957ee0_MD5.png]]

3、选择`Create New`创建一个新证书，然后填写相关信息即可

![[00 assets/1cc80a00c5921a15dc606b9c2abca296_MD5.png]]

4、依旧在`uniapp`中进行云端打包处理，并且需要注意`证书密钥`和`别名密钥`一定要一样，不然会报错

![[00 assets/45d7bb42735d84d3b810fd073a7dfa46_MD5.png]]

> 离线打包

![[00 assets/d9054372ad94200a20273e673a0c666d_MD5.png]]

![[00 assets/e93fe469c3a7d23972c90c77cb9749cc_MD5.png]]

![[00 assets/dd0c2b86d508d58c9372dd5f6e962551_MD5.png]]

![[00 assets/03d56eba550dcd9b416628875c5aef39_MD5.png]]

官方文档：[开发环境 | uni 小程序 SDK (dcloud.net.cn)](https://nativesupport.dcloud.net.cn/AppDocs/usesdk/android.html#)

1、这种打包方式是公司比较常见的打包方式，本质就是使用`Android Studio`本地的原生软件来进行打包

2、因为这里打包的方式比较复杂，建议直接看官网来处理

3、注意看官网的信息，并且需要注意`HbuildX`的版本和下载的`SDK`的版本要是对应的

![[00 assets/b17c187bb3dd5e19b5c7cb709a0487a7_MD5.png]]

4、而且还需要申请`Appkey`，这个在开发者工具中申请即可

![[00 assets/02ec9a540c69206a69f36a7df31367f7_MD5.png]]

5、包名一定要记住，因为这在后面配置会需要的。在做这一步操作之前一定要先手动生成一个证书

6、`SHA1值`可以使用`jdk`的包进行生成`keytool -list -v -keystore 生成的证书文件`

![[00 assets/0fafe698c4b42c3a6d058ea34e321e39_MD5.png]]

7、后续直接参考文档即可

8、因为文档更新可能没有`SDK`快，所以项目中的一些配置如果存在就不要使用文档中的信息、如果说这种就可能不写，可能`sdk`中是最新的

![[00 assets/585045760e5e0d1870bdaf5e6298bdd1_MD5.png]]

# 其他

## 1. # ifndef

![[00 assets/cd21ffd1ce234d140f9d5820b921a821_MD5.png]]

![[00 assets/e4d456a93be60ff82533cfaedec9ff72_MD5.png]]

![[00 assets/0e94fdc1015782a3b70787417e80afcd_MD5.png]]

1、我们在入口文件`main.js`中可以看到该标识符

2、该标识符用作跨端兼容的处理，一开始创建的项目只有`Vue3`的项目

文档地址：[跨端兼容 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/platform.html#跨端兼容)

![[00 assets/19abd74b13ba775b7f0e793fc77f7a35_MD5.png]]

3、我按照条件编译编写了下面的 3 个标签，可以看到对于各个平台适配都不一样

4、对于该条件编译在，直接在`HbuildX`中输入`if`就可以实现

![[00 assets/54533c08818a87159a161e8ab88ea713_MD5.png]]

![[00 assets/b2bdf5dce5ef76744245d9b1b66fe18e_MD5.png]]

5、相对应的`js`的部分也可以使用条件编译来区分，对于`H5`和`微信小程序`来说可以直接调用原生的`API`来使用，但是对于`APP`则需要使用`uni`的`API`来处理

![[00 assets/7d1b6e363a55d68f2c243b092f0de213_MD5.png]]

## 2. 尺寸单位

1、该单位在小程序中是一样的，如果是移动端开发最好使用该方式

![[00 assets/1e19aa15da0138fc9657e41962894368_MD5.png]]

## 3. 背景图片

文档地址：[CSS 支持 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/syntax-css.html#背景图片)

![[00 assets/fefd44756d07c100ceb31bdf83fd76b9_MD5.png]]

1、我们知道对于小程序来说是不支持`backgroud-image`，但是我们使用`uniapp`是可以的

![[00 assets/f11a4b17ae77c1a511ae198b2f0ada17_MD5.png]]

因为对于`uniapp`来说，为了兼容多端所以会将图片按照不同的形式来编译

- 网页 -> 原生图片引入

- 小程序 -> 低于`40kb`转为`Base64`，高于`40kb`就不转为`Base64`，所以高于`40kb`的图片不会显示

![[00 assets/95d04715aa4bbf2312e958e94cf63ddc_MD5.png]]

## 4. 字体图标

![[00 assets/7f0e4827c088f06a8db73dde107531ab_MD5.png]]

官方文档：[CSS 支持 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/syntax-css.html#字体图标)

1、对于字体图标基本就和原生的`H5`是一样的

![[00 assets/e86c07ff125b2b131b5475414b1f9f18_MD5.png]]

## 5. easycom 规范

官方文档：[组件使用的入门教程 | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/component/#easycom组件规范)

![[00 assets/e50276f2689ad99e4213e1db6cf30dcf_MD5.png]]

# 问题汇总

**Q：页面一直卡在`页面同步完成`页面？**

可能存在`Hbuilder`和`Android`模拟器版本的问题，我这里直接选择最新的模拟器版本

**Q：adb 能够调试`mumu模拟器`但是不能调试`android studio`**

我在配置`uniapp`的时候填写了`adb调试服务端口`，将这个删除就行了

![[00 assets/d8d3728e881bd0114ef5866b1326e42e_MD5.png]]

**Q：真机调试问题。**

一般情况下，直接将真机使用`USB`连接设备即可进行调试工作，[真机运行常见问题@run | uni-app 官网 (dcloud.net.cn)](https://uniapp.dcloud.net.cn/tutorial/run/run-app-faq.html#)

如果不存在设备的话，可能使用`adb devices`来重新刷新设备即可

**Q：uni-app 针对小程序的 setData 做了什么优化**

参考文章：[跨端框架深度评测：微信原生、wepy、mpvue、uni-app、taro、chameleon - DCloud 问答](https://ask.dcloud.net.cn/article/35867)

根据下面的说明可以知道，`uniapp`其实本质就是将大量的`setData`合并为一个，并且一次更新，并且使用了`diff算法`来传递变动数据

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032333753.png" alt="image-20240116141520439" style="zoom: 40%;" />
