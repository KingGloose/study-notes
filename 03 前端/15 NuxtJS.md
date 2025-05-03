coderwhy - 前端系统课 - SSR 服务器端渲染

# 1. 基本介绍

## 1.1 SPA

> SPA

![[00 assets/e7a742f2487852519b5825e1ba88ba0c_MD5.jpeg]]

> SPA 优缺点

![[00 assets/d0ed15d9a650ab40cb9a070e9cf7c05d_MD5.jpeg]]

## 1.2 SEO

> 爬虫 - 工作流程

![[00 assets/d60ae147e3eb13395d33fefd0ec9bee6_MD5.png]]

> SEO 优化

![[00 assets/d435928b8aa9e05eae0a9282535133e6_MD5.png]]

## 1.3 SSR

> SSG

1、对于一些程序的文档，比如`Vite`、`Vue`......文档，就比较适合`SSG`

![[00 assets/2b122df463e945ffef98211eb1a37c23_MD5.png]]

> SSR

![[00 assets/3026184abc0d0dcaeef48207654f14cc_MD5.png]]

> SSR 优缺点

![[00 assets/4faa3564da32cac6d00aa656b15818b8_MD5.png]]

> SSR 解决方案

![[00 assets/ebdaf85a28ba6d3611b45ae066d10e26_MD5.jpeg]]

# 2. 非框架编写

## 2.1 Node Server

![[00 assets/c62fc4a36ce32f2f6dca62d11fc332eb_MD5.jpeg]]

1、我们使用`SSR`的之前，最好搭建一个`node server`服务

![[00 assets/629cab318cc6ebe05b6ba809c857372d_MD5.png]]

2、下面为核心代码，我们使用`express`创建了一个服务器，并且编写了一条接口

![[00 assets/685083dcc163ca7a0c6a4fff4a58c69f_MD5.png]]

3、因为是服务器端渲染，到时候肯定有`Vue`、`ES Module`......的导入，所以我们引入`webpack`进行处理

​ 3.1 `target`设置为`node`的话，`webpack`会进行额外的处理

​ 3.2 我们直接用`webpack`打包的话，会让`内置库(fs,path...)`和`node_modules`都被打包进来，所以会导致打包变慢以及包体积变大，所以我们使用`webpack-node-externals`来处理

![[00 assets/36455203f20643fcde21a93b03f6d333_MD5.png]]

## 2.2 \*Vue SSR - 跨请求状态污染

![[00 assets/10b845f46cc6cb50cc9b9beb8ac143cb_MD5.png]]

1、针对`node-server`又新增了下面的包，来处理`.vue`文件

![[00 assets/74e6e6b04227a24656f8ded3f8b5d084_MD5.png]]

2、这里我们正常编写`.vue`的项目

![[00 assets/1ae3b610ea442b504edc26d61440902e_MD5.jpeg]]

3、针对`SSR`的应用需要导出`createSSRApp`来创建`vue实例`

4、并且对于创建的`SSR实例`，最好的方式就是通过创建一个函数的方式来调用。这是为了通过函数返回`app实例`，可以保证每个请求都会返回一个新的`app实例`，来避免跨请求状态污染

5、因为之前都是`单页面`，只需要将对应的`实例`传递过去，用户自己电脑`配置状态`即可。如果使用`SSR`的话，所有状态都保存在`服务器端`，所以需要保存大量的实例，这样就会消耗更多的服务器资源

![[00 assets/d742f324ccd8f9f7063832b08be253df_MD5.png]]

![[00 assets/35125c2cdfa0f688f68ca9460cba901b_MD5.png]]

6、在前面写的`node-server`中，我们创建的`app`实例，需要使用`renderToString`来将`HTML`转化为字符串，通过`模板字符串`来写入，最后通过请求的方式发送过去渲染页面

![[00 assets/2069c4eb35bf8093ab17008bfc856058_MD5.png]]

7、针对`Vue`使用`webpack`来处理，这就是常规配置了

![[00 assets/2a4795d0d55daa47506192f89563ee23_MD5.png]]

8、编写对应的脚本，运行打包好的`server_bundler.js`

![[00 assets/fed7dbf471764d24bb9ddf1402b5d805_MD5.png]]

9、最后的结果就是这样的，页面可以正常显示，但是对应的交互暂时没有

![[00 assets/8aba3741e943eccafcd68f88ee40e942_MD5.png]]

## 2.3 Hydration

1、我们已经能成功使用`服务器端`渲染将`静态网页`渲染出来了，但是可以发现没有对应的交互。这个时候我们就需要使用`Hydration`的功能来为网页添加交互处理

![[00 assets/21e559e9fe40524ae8bc37952fdeea55_MD5.png]]

2、我们使用正常的`spa`的写法来挂载`vue`组件，这一步主要是为了将`vue`的核心功能都导出为`.js`文件

![[00 assets/1aaddf5cc88c828e4beb7ff3dae8eada_MD5.png]]

3、重新编写一个`client.config.js`文件，来配置`client端`的打包服务

![[00 assets/1429e61894ab5deb1b31ada4cd05348e_MD5.png]]

4、因为需要加载`.js`文件，所以我们使用`express`的`静态资源`部署的功能，让返回过去的页面能正常请求到`client_bundler.js`的文件，实现对应的交互效果

![[00 assets/0124806146af591339e3446bdb69c71b_MD5.png]]

5、添加对应的打包脚本

![[00 assets/5134b45be959ec3b29eca3ca6f55e639_MD5.png]]

6、运行即可正常显示

![[00 assets/3057896c501926a0b2c576bea3696f9f_MD5.png]]

## 2.4 \*Vue Router - Vue Tree Shark 警告处理 / webpack 配置抽取

> Vue Tree Shark 警告处理

1、我们在`开发环境`中，会出现下面的警告信息，这个需要我们额外配置，告诉`Vue Tree Shark`的处理

![[00 assets/a4ceaf330f16276e4f86cfa35764dc4e_MD5.jpeg]]

2、添加这些属性，告诉`Vue`不需要将这些代码打包即可

![[00 assets/b9dc32ebb9ea7f36340b4893b6a2ea86_MD5.png]]

> webpack 配置抽取

1、我们使用`webpack-merge`来将基础配置和`额外配置`区分，这样就可以尽可能减少`webpack`的配置

2、这里也可以查看我`wepack`的笔记

![[00 assets/32062eef1b28b096b6857c5750106fee_MD5.png]]

![[00 assets/6f559362f6622e6723453295d0bdd2c0_MD5.png]]

> Vue Router

1、第一步就是下载`npm i vue-router`。第二步就是创建路由，唯一不同的就是也是使用`函数`的方式来创建，这样可以避免状态污染

![[00 assets/932baf342005b9d0170c3d4b598e3202_MD5.png]]

2、依旧按照之前编写`Vue Router`的配置

![[00 assets/f5791c95f99e6a1ec95e520afbd396da_MD5.png]]

3、在服务器端使用下面的方式来加载路由，因为在`node`中不存在`web`中的路由，所以只能使用`内存路由`

4、因为用户在浏览器中输入`/`的时候，对应的`Vue Router`的路由也需要跳转到该位置，所以我们需要手动跳转路由，方便`app`渲染对应的页面

5、跳转之后，因为需要等待`路由加载`，所以需要使用`isReady()`来等待

![[00 assets/a4d7a514282cb94101895a774a1a56f7_MD5.png]]

6、我们在`客户端`中也需要使用`router`的`isReady`函数来让`服务器端和客户端`输出一致

![[00 assets/ec0be4e0a3c7dd667acf0995ef7c2f81_MD5.png]]

![[00 assets/a21573b607946e29d51ba434daefc5b4_MD5.png]]

7、记住`SSR`可以提高首屏渲染速度，且优化`SEO`。再来看下面的内容，我们进入路由输入`/about`，就会首屏渲染对应的`html`，然后请求对应的`client_bundler.js`也就是`Vue核心包`，然后根据核心包再来请求`about.vue`组件内容(路由懒加载)

![[00 assets/45414aaca84adf9f6ae7511d2678441d_MD5.png]]

这个时候路由切换到`/`的时候，可以看到没有加载对应的`home页面`，而是请求的`组件`，这个时候就回归到了`spa`页面的处理方式

![[00 assets/83482f39b2887fd642e30345575d017e_MD5.png]]

我们刷新页面，又会重新请求`home页面的html`，然后依次`请求处理/挂载`

![[00 assets/8ad1ea7f9c1d7da1ef11c82a1b7877b8_MD5.png]]

## 2.5 Pinia

1、下面是`SSR`中`pinia`的实现方式，服务器端会将对应的数据转化为`JSON字符串`，然后丢给`window`对象中，后续就会将这些数据同步到客户端的`pinia`中

2、不仅仅是`pinia`是这样处理的，`redux`也是这样处理的

![[00 assets/5de994d11b5525bdc7a45c97aefda433_MD5.png]]

3、正常编写`pinia`的配置

![[00 assets/5f78bb878425aad334eaa71deeb1895b_MD5.jpeg]]

4、在`服务器端`开启`pinia`

![[00 assets/8f996e57a2c89d2ee8face46ba6319ac_MD5.png]]

5、在`客户端`注册`pinia`

![[00 assets/c2f6d85d3e24a6d9828090974e4c4967_MD5.jpeg]]

6、然后对应的页面中使用即可

![[00 assets/aa726f1df2ab64788794fa71a3ff1add_MD5.png]]

# 3. 框架介绍

> 简要介绍

![[00 assets/d5c774648dbc33e850a5d0a518eb0dfc_MD5.png]]

> 发展史

![[00 assets/13e5ff743adce0a5f8b0d1c72553cfea_MD5.jpeg]]

> Nuxt3 特点

![[00 assets/0d6d73cd848dbde2c98914988ba03a97_MD5.png]]

> Nuxt.js vs Nuxt 3

![[00 assets/0ad933d5b2d7d684353c84d4df1fa874_MD5.png]]

# 4. 基本使用

## 4.1 环境搭建

![[00 assets/3a4a4616d9ee31773a2520af5ebf1203_MD5.png]]

## 4.2 项目介绍

> 脚本介绍

![[00 assets/82fbed0f97c26a8520104f89fb9f4eba_MD5.png]]

> 目录结构

![[00 assets/36d3e0968aba11d49e2a6898cc8423e4_MD5.png]]

> 应用入口

![[00 assets/8c19081dce47c4dc3693b98d9d5f9e04_MD5.png]]

## 4.3 配置文件

![[00 assets/f69370e9596d981a75390ce79cdcfc8a_MD5.png]]

### 4.3.1 RuntimeConfig

如果想要知道更多的配置信息可以查看下面的网站：[配置 · 开始使用 Nuxt3 Nuxt 中文站](https://nuxt.com.cn/docs/getting-started/configuration#环境变量和私有令牌)、[Nuxt Configuration Reference · Nuxt](https://nuxt.com/docs/api/configuration/nuxt-config#runtimeconfig)

1、我们可以通过`process.server`和`process.client`来区分`服务端`和`客户端`

![[00 assets/996e1e84c93c11092a3c0e242699d734_MD5.png]]

2、我们使用`useRuntimeConfig()`导出的对象获得配置信息

3、看结果就可以知道，一些配置是只有`服务端`可以获取的，一些只有`客户端`才可以获取

![[00 assets/51561cd381293196bd6e098268db8857_MD5.png]]

4、如果在`nuxt.config.ts`中编写太麻烦的话，也可以使用`.env`来动态配置`参数信息`

5、并且可以发现，`.env`的配置`优先级`高于`nuxt.config.ts`，如果相同就覆盖

6、使用的时候，使用`NUXT_.....`的方式来编写，如果是单个字母就拆分

![[00 assets/badca003ea7d7ff4c3f8fc9b9ef95bdf_MD5.png]]

7、写入`.env`的配置也会写入`process.env`中，而在`nuxt.config.ts`中是不会写入进去的

![[00 assets/ad58de0a0bf2f4a1faad9a2569ad8956_MD5.png]]

8、这个配置不单单只能写这些配置，如下图就可以直接在这里编写修改`启动`端口号

![[00 assets/008729c8da187423517a1607d632c5b2_MD5.jpeg]]

### 4.3.2 AppConfig

1、我们可以在`nuxt.config.ts`中编写一些`appConfig`的配置

![[00 assets/b702bab8d4c9b29934df70bf1c48e5ff_MD5.png]]

2、使用`useAppConfig`来获取数据

![[00 assets/b4df1a9132806894aae1f4d2e1c1ded5_MD5.png]]

3、我们也可以将这些配置抽取出去为`app.config.ts`，该配置文件的优先级高于`nuxt.config.ts`

![[00 assets/7d106adf7def91e6943e2f05a6aedd44_MD5.jpeg]]

> RuntimeConfig vs AppConfig

1、这是官方的对比图，我现在使用的`Nuxt 3.6`

![[00 assets/1e5727d145fe4058eca751ea4371d4c5_MD5.png]]

### 4.3.3 \*App - SEO

官方文档：[SEO and Meta · Get Started with Nuxt](https://nuxt.com/docs/getting-started/seo-meta)

1、我们使用`SSR`的其中一个原因就是为了`SEO`的优化

![[00 assets/c5117166ff07f52ebe005d922ac32b00_MD5.png]]

2、我们可以发现在`Nuxt`的项目中是没有`index.html`，所以不能直接编写`SEO`的标签，但是对于`Nuxt`提供了对应的配置来处理`SEO`的优化，我们也可以在`nuxt.config.ts`中进行配置处理

3、剩下的配置直接去官网查看即可

![[00 assets/671229ebd6d5e78c081d19f73b9c153f_MD5.png]]

4、我们不仅仅可以在`nuxt.config.ts`中配置，还可以在`script`中动态来配置

5、这里的配置只针对该页面来配置，如果切换页面就会使用`nuxt.config.ts`的配置

![[00 assets/1ec84bca883034684bdadb79af625943_MD5.jpeg]]

6、当然我们还可以直接在`template`中编写，这些配置优先级是`内置组件 > useHead > Nuxt.config.ts`

![[00 assets/04f5fa7b32fffeeecffb5d421a66f8de_MD5.png]]

### 4.3.4 渲染模式

1、我们可以配置`ssr`来开启和关闭渲染模式的配置

![[00 assets/246f6f3b672fcc1280b6bc4a2dccb27f_MD5.jpeg]]

# 5. 内置组件

![[00 assets/8a8c09d6d612c714536997baf9bf858d_MD5.png]]

> NuxtPage

1、该组件的本质就是对于`routerview`的封装，我们在`pages`下面编写的`页面`就会放置在`NuxtPage`，这个`pages`是固定的目录结构

![[00 assets/2f151818b88fe3ab82a230f18b479aea_MD5.png]]

> ClientOnly

1、使用`clientonly`表示只在`客户端渲染`

2、但是只在客户端渲染的话，就会导致`js`文件没加载的情况，所以需要一个`loading`的页面来支撑

​ 2.1 下面是 2 种渲染的方式，一种是标签，一种是插槽，我推荐使用插槽

![[00 assets/e68e772acb64bfeaf4c6a3e8c20a23a2_MD5.png]]

3、下面分别是`SSR`渲染和`客户端渲染`的截图

![[00 assets/1e54c11bcc0d26d3c213c1d4d7aafca9_MD5.png]]

![[00 assets/cc3be9a286c728fabba71f17769cbc47_MD5.png]]

# 6. 样式/资源

## 6.1 样式

![[00 assets/e97a2bd8d7a27b306d894d261eebc641_MD5.png]]

### 6.1.1 局部样式

![[00 assets/2c21ea159c3e0084f29689aff4c54729_MD5.png]]

### 6.1.2 全局样式 - CSS

1、在`app.vue`中的`style`中编写样式，但是一般开发中不使用这种形式

![[00 assets/04e461bdae195d18908fc1d3f9a2a325_MD5.png]]

2、第二种方式就是在`nuxt.config.ts`中配置全局的`css`

![[00 assets/bae1fb835e58a58b7cc3b538827ca65f_MD5.png]]

### 6.1.3 全局样式 - SCSS

```bash
pnpm add sass -D	// 安装库
```

1、我们也可以将`sass`的变量进行导入，并且这个导入是全局生效的

2、这个使用的样式库是`sass`

​ 2.1 使用`$xxx`表示创建变量

​ 2.2 `@mixin fn() { ... }`表示混入，使用`@include fn()`表示使用![[00 assets/753cb3209cc0aa97b3dd94733f5fe008_MD5.png]]

3、现在`SASS`对于`@import`差不多要废弃，现在最好使用`@use ... as ...`的形式来导入，这样可以设置命名空间，避免变量覆盖的问题，而且使用该方式导入还能提高导入性能

![[00 assets/4f3d46a2977180860fa861f3467216cd_MD5.png]]

我们也可以直接写`*`，这样下面就不需要写`命名空间`的名字了

![[00 assets/addeb16aca2e27b27e76d75de2dd8551_MD5.png]]

4、如果按照上面的方式来编写的话，就会导致每一个`style`中都会导入`variable.scss`， 这样操作很麻烦，所以`nuxt.config.ts`中提供了对应的配置，可以自动的在每一个`页面`中导入

更多的可以参考官网：[Assets · Get Started with Nuxt](https://nuxt.com/docs/getting-started/assets)

![[00 assets/1f7117bce866a809d74d728d3ce6fab8_MD5.jpeg]]

![[00 assets/eb31c597ae2a99c1e05ee2d340b9fb94_MD5.png]]

5、我们也可以直接在`SASS`中配置，也可以实现全局样式的效果

![[00 assets/533a94fccd89e6af59d412914fcdec81_MD5.png]]

## 6.2 资源

![[00 assets/a6bc9f14253857d2021f756667365b3c_MD5.png]]

1、如果是`public`中的资源，可以直接使用`/xxx.png`的方式来访问

2、如果是`assets`中的资源，就需要定位到该资源才行

3、不仅仅是图片是这样导入，背景图片、视频都是这种形式来导入

![[00 assets/65fe1906d1ec392941a5deeb5d24d1b8_MD5.png]]

## 6.3 字体图标

1、我们在`iconfont`中下载的字体图标，大概率只是使用下面的`css`和`ttf`

![[00 assets/616f00600f7e57165168495e9ad275d2_MD5.png]]

2、因为字体图标是全局需要使用的，所以我们可以在`nuxt.config.ts`中进行配置

![[00 assets/1fe466169c08a346f670286d54dd154f_MD5.png]]

3、使用类名的形式即可

![[00 assets/8e14d82404a7638c841ff8a0f37724e5_MD5.jpeg]]

# 7. 页面/导航

## 7.1 创建页面

![[00 assets/6ac31c82c5890915646c911ddae12eb1_MD5.png]]

> 手动

1、`Nuxt.js`框架会自动的收集`pages`中的页面来配置路由信息

​ 1.1 `index`表示根路由，比如`pages/index.vue`就是`/`，如果是`pages/home/index.vue`就是`/home`

​ 1.2 该路由还支持嵌套，比如下面的`/pages/detail/shop`对应的路由就是`/detail/shop`

2、对应的`NuxtPage`本质就是对`RouterView`的封装，而`NuxtLink`就是对`RouterLink`的封装

![[00 assets/4eb4d845dcd3d8ebe20c07f51ea653ec_MD5.png]]

> 命令行

1、不仅仅可以手动来创建页面，还可以使用命令行的方式来创建，但是该方式我不是很喜欢。

![[00 assets/13b313e37845dd2ba6c778bf4243e4da_MD5.png]]

## 7.2 组件导航

官方文档：[ · Nuxt Components](https://nuxt.com/docs/api/components/nuxt-link)

![[00 assets/8a8c09d6d612c714536997baf9bf858d_MD5.png]]

1、该路由的导航和我之前介绍的差不多，只有在第一次进入页面的时候会进行路由刷新`SSR`，当`hydration`成功之后就会走`客户端`的路由

2、`NuxtLink`本质就是`RouterLink`的高阶封装，而`RouterLink`本质也是`a`标签的高阶封装

![[00 assets/0cd819c09689163648de336949a8b162_MD5.png]]

## 7.3 编程式导航

> navigateTo

![[00 assets/6ab6620257ba99798132730055c8d21a_MD5.jpeg]]

1、我们使用`navigateTo()`可以进行路由跳转

2、可以使用下面的 2 种方式，因为`navigateTo`本身就是返回`Promise`的

![[00 assets/bc266c78223a1a76942d23af6d482b8d_MD5.png]]

> useRouter

官网：[useRouter · Nuxt Composables](https://nuxt.com/docs/api/composables/use-router)

![[00 assets/0051015c2862c043966cadd149493c5f_MD5.png]]

1、单纯使用`navigateTo`不满足开发的需求，也可以使用`useRouter`来作为扩展

2、路由守卫最好只在`app.vue`中编写，这样创建页面就会监听路由，如果多处监听会导致性能较差

![[00 assets/c4328f668818a994ce2884743dc2f8c9_MD5.png]]

## 7.4 动态路由

> 动态路由

![[00 assets/2c61b763f93494e0bf0d081e3a281cf0_MD5.png]]

1、其大致的语法是`[xxx]`的形式，比如我是`detail-[role]/[id].vue`的文件，地址就可以是`detail-admin/01.vue`，最后的结果是`detail = admin;id = 01`

2、当然我们单独嵌套也是可以的`detail/[id].vue`也是可以的

3、动态路由页面和`index.vue`是可以相互共存的

![[00 assets/d89de624a92b46b4a2e8a42c2fc673ff_MD5.png]]

## 7.5 路由参数

![[00 assets/253880dc258094ece200af6cd22f8f61_MD5.png]]

## 7.6 404 页面

![[00 assets/83ab72e7adc70231fa4a07fb484c2332_MD5.png]]

1、在页面中编写`[..slug].vue`就表示没有匹配的路由，就会跳转到`[..slug].vue`页面

![[00 assets/91da925cd12f721b79572063b3aaab52_MD5.png]]

如果是有层级的话，优先是层级内的`[..slug].vue`中的页面

![[00 assets/ccbec265f1cb9fc82f94eb0c3b86606d_MD5.png]]

2、也可以使用`params参数`来获取对应的额外的参数

![[00 assets/1ed78bfcf2659f0080ecebcca2c4dc8d_MD5.png]]

## 7.7 嵌套路由

![[00 assets/c10519affc469a70046f9188379bf273_MD5.png]]

1、也就是在一级路由中添加二级路由，下面就是演示的`about`的路由加载到`app`中

![[00 assets/36ae1953ebd02708008cbd630af449be_MD5.png]]

2、而`about`作为二级路由，也可以进行切换，这就是路由的嵌套`about路由`嵌套到了`app`中了

![[00 assets/9a441279838ae7415f41e73365d81e7f_MD5.jpeg]]

## 7.8 路由中间件

![[00 assets/9c0117a6ade2e40940e28fadbb6eaf7f_MD5.png]]

> 匿名中间件

1、我们使用`definePageMete { middleware: [ ... ] }`来设置路由的中间件，这个属于`匿名中间件`

![[00 assets/afa00f7aa20d28a39752995c87c96370_MD5.png]]

> 具名中间件

2、当然我们也可以设置`命名路由中间件`，只要符合命名规范就可以自动加载

3、对应的命名规范是`middleware/xxx.ts`表示具名中间件，该中间件的文件名传递给`definePageMete`就可以实现装载

![[00 assets/6798e8ec2de1d293e8667c327e1b1f5e_MD5.png]]

4、使用`defineNuxtRouterMiddleware`来定义该具名中间件

![[00 assets/e0b3220a701337a1d142afc4f1c224a1_MD5.png]]

> 全局中间件

5、如果按照上面的方式来定义中间件的话，可能会存在一些全局都需要使用的中间件，就需要一个个来写，很麻烦，所以可以使用全局中间件

6、全局中间件的定义方式就是`xxx.global.ts`来定义，这样就需要额外来写名字就可以使用

![[00 assets/1fd5243614fdd28f91c938adba4999fa_MD5.png]]

> \*其他

7、中间件作为一个函数，存在返回值，如果使用`navigateTo`返回的话就是停止中间件，如果是`" "、null、undedined`的话就可以继续执行中间件

## 7.9 路由验证/自定义错误页面

> 路由验证

1、在`definePageMete`中的`vaildate`来验证路由，如果放回是`true`就放行，如果为`false`就不放行并且报错

2、我们还可以通过返回`{ statusCode: 404 , .... }`来是实现错误页面传递的效果

![[00 assets/444d66ccdab23116076a0d47de6581d6_MD5.png]]

> 错误页面

1、我们还可以在根目录中写`error.vue`来实现自定义错误页面，这个名字是定死的，只要验证错误就会跳转到该页面

2、我们还可以使用`defineProps`来错误传递进来的参数

3、`clearError`表示清除`错误信息`，然后路由重定向到`/`

![[00 assets/e1e824f9746e6e99ab403dcbae733fc3_MD5.png]]

# 8. Layout 布局

![[00 assets/f520d3d54adb1be1dbd0223deffa3cb8_MD5.png]]

1、一些页面可能存在一些通用的布局，这个时候就可以将这些布局抽取出来全局使用

2、其编写原则也基本类似，Nuxt.js 支持自动导入的模式，在`layouts/default.vue`表示默认导入的布局

![[00 assets/c4c593c33c62fcc269abeae47be712d3_MD5.jpeg]]

3、最后会将页面插入到`slot`中显示

![[00 assets/3807c1bcbdae40a91751b93e654d454e_MD5.png]]

4、我们还可以自定义`layout布局`，如果想使用的话。`NuxtLayout`有一个`name`属性，传递文件名即可使用

![[00 assets/8a9e6f483fc01661954be7b28e0552fb_MD5.png]]

5、可能存在一些页面使用`layout1`的情况，而一些页面使用`layout2`，所以这里可以通过`definePageMete`来定义使用的`layout`布局

![[00 assets/92366419600dec87d047376ff391a370_MD5.jpeg]]

对应的`login页面`就是使用`custom-layout`布局

![[00 assets/7cae6d302445c7bff352f977850a1262_MD5.png]]

# 9. 渲染模式

![[00 assets/679b058f735a4809647c14e6a07f68b6_MD5.png]]

1、我们在`nuxt.config.ts`中可以配置下面的属性，即可按照路由来配置渲染的方式

![[00 assets/538d3e3bea9624113e049c52c2438916_MD5.png]]

2、在`nitro`中也可以有详细的渲染模式的说明

![[00 assets/648a58510ed272dbbdfbf6edc0afa4d7_MD5.png]]

# 10. 编写插件

![[00 assets/a3b1d579e598fec46bb2e9f30a50271c_MD5.png]]

1、如果是编写插件的话最好的方式就是写在全局，这样都可以直接使用。使用`provide`将`函数`和`常量`进行全局注册

![[00 assets/174743df63972b4f813730c25f5db919_MD5.png]]

2、我们也可以将这些编写的插件单独抽取出来使用，使用`plugins`文件夹下面编写就会自动导入

3、使用`defineNuxtPlugin`来导入插件，之后便可以全局使用

![[00 assets/cd0b3bc1046372382dc7cc4fe1a03a84_MD5.png]]

4、使用该方式来注册的插件就会在`Vue实例`创建的时候执行

5、我们添加`.client`就表示`client端`运行，并且在执行的时候要加上`process.client`，不然服务器端执行就会报错

![[00 assets/8e1fc6fcc4abb1c8786ac7e04996ff23_MD5.png]]

# 11. 生命周期

## 11.1 App 生命周期

官方文档：[Lifecycle Hooks · Nuxt](https://nuxt.com.cn/docs/api/advanced/hooks)

1、相对来说官方文档写的内容已经很详细了，可以直接查看官方文档

![[00 assets/a770351ad7ca7c0dfa07326a639b9fe8_MD5.png]]

2、但是这里要注意一个问题，记得我`插件`部分的笔记，使用`plugins/xxxx`文件夹下的自动导入的模式吗？使用该模式会在`Vue实例`创建之前，所以可以看到全部的生命周期

![[00 assets/00a6a32489c6d0382298a4122350e628_MD5.png]]

3、如果在页面里面直接编写的话，`setup`语法糖是在`created`、`beforeMount`之后的，所以看不到大部分的生命周期

4、这边直接使用`nuxtApp.hook()`函数来调取对应的`生命周期 hook`的钩子

![[00 assets/1c1eabcb93a8180591e4e30527414fe3_MD5.png]]

## 11.2 组件生命周期

![[00 assets/93520170f1f6b604c74a89642e366c61_MD5.png]]

1、如果在`客户端`中编写对应的生命周期，只会执行下面的`setup`、`beforeCreate`、`created`。而`客户端`依旧会依次执行

![[00 assets/e3e0b2ca57fd78b86cecf5b8c23a6ee6_MD5.png]]

# 12. 数据获取

![[00 assets/3c74a256676f7ea27c207a98036196e8_MD5.png]]

## 12.1 $fetch

1、按照`Nuxt2`有对应的库来实现`Nuxt`的网络请求

2、现在官方提供了`$fetch`API，可以直接使用，底层封装的`axios`

![[00 assets/8b5e1eecfc0f7405ad1045fbcf790b99_MD5.png]]

## 12.2 useAsyncData

1、但是官方比较推荐这个`API`来实现网络请求，这是因为使用`$fetch`进行网络请求，在页面刷新的时候会在`客户端`和`服务端`都跑一遍

2、如果使用`useAsyncData`的话就不会，只会在`客户端运行`一遍，而且返回的参数是`响应式`

![[00 assets/e9b016fe1978c10cfcf001d7fa1e0cee_MD5.png]]

3、使用`useAsyncData`第一个参数就是`key`，该参数用于第一次进入页面，或者刷新页面的时候，服务器进行`hydrution`时候数据的判断，如果 2 个参数一致就会导致数据重复的问题

4、如果我们后续在前端路由中刷新就不会存在这些问题

![[00 assets/6057f2f0249cb171b4752f0dfb9a621a_MD5.png]]

## 12.3 useFetch

### 12.3.1 基本使用

![[00 assets/2915821ec7ac35d6b48d755d7f5733ab_MD5.png]]

1、`useFetch`是`useAsyncData`的一个简写，之前我们需要对应的回调函数，但是对于`useFetch`不需要

2、而且`useAsyncData`需要传递一个`key`作为一个独立的值存在，而`useFetch`会自动使用该`文件名 + 行数`作为`key`

3、并且里面还存在很多的`options`，这个可以直接上`nuxt3`的官网来查看

![[00 assets/988cef60f6316606f36e42e9bfacee0b_MD5.jpeg]]

### 12.3.2 lazy

1、如果我们按照这个上图中的方式来编写会出现一个现象，也就是`await`同步，只有网络请求到之后才会走后面的逻辑，如果我们不想让这个网络请求阻塞页面渲染，就可以使用`lazy`属性

![[00 assets/251d2462f0e6e9286e2b626ae215a326_MD5.png]]

或者使用`useLazyFetch`API 来作为上面方式的简写

![[00 assets/eddfed1e25b8aded8de99398b50b051c_MD5.png]]

2、但是我实际测试其实并没有那么复杂，只要删掉`await`即可，依旧不影响获取数据

![[00 assets/96ebb62835167808d6f17de4e5c3aced_MD5.png]]

### 12.3.3 refresh

1、我们仔细观察客户端的网络请求就可以发现一个问题，我们在首次进入或者刷新页面的时候，控制台是没有网络请求的

![[00 assets/5762327b76d9a51f796c0d9022e43602_MD5.png]]

对应的网络请求就交给了`服务器`来处理，也就是页面刷新，服务器请求数据并且和前端页面进行`hydrution`

![[00 assets/22559666576d16028aff92a90e6a4c52_MD5.png]]

2、如果只是前端自身的路由进行跳转就会进行网络请求

![[00 assets/3f0beffaf5b2e4fa7006da93612d0476_MD5.png]]

3、对于`useFetch`来说，存在一个`refresh`函数，调用该函数就可以刷新数据，并且该刷新只在`客户端`发送网络请求

![[00 assets/5f0f92a89e32b34fc49919316be9e1fc_MD5.png]]

4、不仅仅是`refresh`函数，`useFetch`内部对应的参数发生变化也会重新发送网络请求

![[00 assets/46d9162e26950054fecd188a11dabfa0_MD5.png]]

### 12.3.4 pending

1、还存在`pending`参数，表示该请求是否已经完成

![[00 assets/5f1adfc8ccfc736e980c3b52f3c59d02_MD5.png]]

## 12.4 拦截器

1、我们使用`onRequest`......就作为该`API`请求的拦截器，具体的各个`API`中数据可以在官网中查询到

![[00 assets/bc735145ff99c26eaba020a3d9192cda_MD5.png]]

## 12.5 请求封装

文章参考：[nuxt3 学习之数据获取，useFetch 的类封装 - 掘金 (juejin.cn)](https://juejin.cn/post/7249585135788671013)

1、我这里使用的这 3 个文件夹来分块处理的

![[00 assets/e350da11387f03f7356a2294b8c65365_MD5.png]]

2、下面就是对应的代码

> 请求封装

```typescript
import type { AsyncData, UseFetchOptions } from "nuxt/app";

export interface IInterpoter
  extends Pick<
    UseFetchOptions<any>,
    "onRequest" | "onRequestError" | "onResponse" | "onResponseError"
  > {}

export type IMethod = "GET" | "POST" | "DELETE" | "PATCH";

export type IReqPromise<T> = Promise<AsyncData<T, Error>>;

export class NuxtRequest {
  public BASE_URL: string;
  public INTERCEPTOR: IInterpoter;

  constructor(BASE_URL: string, INTERCEPTOR: IInterpoter) {
    this.BASE_URL = BASE_URL;
    this.INTERCEPTOR = INTERCEPTOR;
  }

  request<T = any>(
    url: string,
    method?: IMethod,
    data?: any,
    options?: UseFetchOptions<any>
  ): IReqPromise<T> {
    return new Promise((resolve, reject) => {
      const newOptions: UseFetchOptions<any> = {
        baseURL: this.BASE_URL,
        method,
        ...options,
        onRequest: this.INTERCEPTOR.onRequest,
        onRequestError: this.INTERCEPTOR.onRequestError,
        onResponse: this.INTERCEPTOR.onResponse,
        onResponseError: this.INTERCEPTOR.onResponseError,
      };

      if (method === "GET" || method === "DELETE") {
        newOptions.query = data;
      }
      if (method === "POST" || method === "PATCH") {
        newOptions.params = data;
      }

      useFetch<T>(url, newOptions as any)
        .then((res) => {
          // res => { data: T, pending, refresh, error ... } => AsyncData
          resolve(res as AsyncData<T, Error>);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }

  get<T = any>(
    url: string,
    data?: any,
    options?: UseFetchOptions<any>
  ): IReqPromise<T> {
    return this.request<T>(url, "GET", data, options);
  }

  post<T = any>(
    url: string,
    data?: any,
    options?: UseFetchOptions<any>
  ): IReqPromise<T> {
    return this.request<T>(url, "POST", data, options);
  }

  delete<T = any>(
    url: string,
    data?: any,
    options?: UseFetchOptions<any>
  ): IReqPromise<T> {
    return this.request<T>(url, "DELETE", data, options);
  }

  patch<T = any>(
    url: string,
    data?: any,
    options?: UseFetchOptions<any>
  ): IReqPromise<T> {
    return this.request<T>(url, "PATCH", data, options);
  }
}
```

> 创建实例

```typescript
import { NuxtRequest } from "@/service/index";

const MainRequest = new NuxtRequest("https://api.wrdan.com", {
  onRequest() {
    console.log("请求拦截器");
  },
  onRequestError() {
    console.log("请求错误拦截器");
  },
  onResponse() {
    console.log("响应拦截器");
  },
  onResponseError() {
    console.log("响应错误拦截器");
  },
});

export { MainRequest };
```

> 请求模块

```typescript
import { MainRequest } from "./request";

export const getHitokoto = () => {
  return MainRequest.get("/hitokoto");
};
```

> 页面使用

![[00 assets/4724cdf83a72ca473f865ed2baf24397_MD5.png]]

# 13. 服务器端接口

1、`server`中的文件夹也是规定好的，这里可以直接在官网中查看，其中`return`表示返回对应的数据回去

![[00 assets/37eac70a16ab96ddac517b7f24ad0cb5_MD5.png]]

2、按照目录文件夹可以直接调用该网络请求

![[00 assets/46eea28331a68c9ebf59e5bf8f6fd14e_MD5.png]]

3、我们也可以使用在文件名后面添加`.get`或者`.post`的后缀，来表示请求方法

4、还有对应的`getQuery`，`readBody`，`getMethod`方法来获取参数

![[00 assets/6144940aeceb8211bc43e44d82004373_MD5.png]]

# 14. 状态管理

## 14.1 useState

![[00 assets/5ee41787d5e53c6c2e4243201f03d9d4_MD5.png]]

1、我们在`composables`中编写对应的全局状态共享，使用`useState`函数

2、页面中使用就是使用对应的文件名来获取全局的数据

![[00 assets/88943134f98f20e8f259c58143c20a6d_MD5.png]]

## 14.2 Pinia

> 基本使用

![[00 assets/1800eb31b0ea7ffb07120bdee7e544ee_MD5.png]]

1、安装库`pnpm add pinia @pinia/nuxt`，随后在`nuxt.config.ts`中配置模块

![[00 assets/d80a5666b02db9125f68a199641d1766_MD5.png]]

2、剩下的使用基本类似，下面有`普通方法`和`异步方法`

3、这里需要注意，如果直接将`data`赋值给`state`中的数据会导致`empty`，必须使用`.value`获取内部值之后，页面才会正常显示

![[00 assets/287e48332c1f069fa6e90f0cd8dc6b9a_MD5.png]]

4、页面中正常使用即可

![[00 assets/f862cdd360f9382dfa01ff6f6e612484_MD5.png]]

> useState VS Pinia

![[00 assets/0ec096850cf27b2256edbd469f094fb1_MD5.png]]

# 15. Element Plus

![[00 assets/9fc07053787b43cd7f48a2f3e2a0a180_MD5.png]]

1、先安装对应的库`pnpm add element-plus --save / pnpm add unplugin-element-plus --save-dev`

2、随后在`nuxt.config.ts`中添加下面 2 个配置

![[00 assets/1eb2b3726d8294a970f99b5cdac34d4f_MD5.png]]

3、如果要使用的话，需要手动引入对应的组件，目前不存在自动引入的方式

![[00 assets/71c65691162589662abbba089c753c04_MD5.png]]

# 16. 项目

## 16.1 oppo 商城

### 16.1.1 前期准备

#### 16.1.1.1 样式

1、`pnpm add normalize.css`使用`normalize.css`来清除额外样式，不需要额外的引入，直接在`nuxt.config.ts`中配置就可以实现全局引入

![[00 assets/9d9f832091d40bd73ce5b01d08f8d67f_MD5.png]]

2、`pnpm add scss`，然后设置全局样式和全局变量

![[00 assets/08aa251b9f55d953bca1d26bdb444ae3_MD5.png]]

![[00 assets/37c28e550e357b91603754a57e483e64_MD5.png]]

3、为了实现全局引入，添加后续配置即可

![[00 assets/a049d38a13de132d9bdd11ca504e35dd_MD5.png]]

4、页面中可以实现效果，并且不需要额外的引入样式文件

![[00 assets/3622e8a318a9079f1c2492542add3ccb_MD5.png]]

#### 16.1.1.2 布局

根据业务需求，我们需要编写一个全局的布局

![[00 assets/bb6c40bbe8386ed7a0d0ed2e51be8981_MD5.png]]

### 16.1.2 页面搭建

#### 16.1.2.1 app-header

![[00 assets/b0c69d3565dc3fc9ef2450c2d4633b77_MD5.png]]

#### 16.1.2.2 SEO

1、我们这里也可以在`nuxt.config.ts`中进行`SEO`的优化

![[00 assets/5533a52e2500edbc2e6adca287d8f39b_MD5.png]]

#### 16.1.2.3 404 页面

![[00 assets/15a172075457f3ef255061f72716fcc9_MD5.png]]

#### 16.1.2.4 \*登录/注册页面 - 布局切换/definePageMeta

1、我们使用`defineMetaPage`编译器宏可以在页面中定制布局

2、该编译宏不仅仅可以切换布局，还有很多其他的用处，**官网地址**：[definePageMeta · Nuxt Utils](https://nuxt.com.cn/docs/api/utils/define-page-meta/)

![[00 assets/86badacba5b27223f6a5e1e616c2fe1b_MD5.png]]

#### 16.1.2.5 navBar

![[00 assets/601374c2fb515517d6c7030a351697a9_MD5.png]]

#### 16.1.2.6 网络请求/pinia - types

1、因为这里使用的是`ts`，所以对于一些网络请求接口都可以编写一些接口，来提高编写提示的效率

![[00 assets/d7cd00ea0dad411196ce39727ee3f9ab_MD5.png]]

2、剩余的`网络请求`和`pinia`的状态集成可以直接看我之前的笔记

![[00 assets/c6d411f74d56f194e2c1c4e414c489f2_MD5.png]]

![[00 assets/04c004b19731ff0fcaae5e03a95a6a65_MD5.png]]

#### 16.1.2.7 轮播图 - ElementUI 集成

1、`pnpm add element-plus unplugin-element-plus -s`，安装库

2、我们在`nuxt.config.ts`中添加下面的配置

![[00 assets/54cf20a1d6f810f4582516af06518a71_MD5.png]]
