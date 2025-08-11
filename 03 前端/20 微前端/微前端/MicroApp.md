# 1 基本介绍

官网介绍：[MicroApp](https://micro-zoe.github.io/doc/zh/)

1、微前端的概念是由ThoughtWorks在2016年提出的，它借鉴了微服务的架构理念，核心在于将一个庞大的前端应用拆分成多个独立灵活的小型应用，每个应用都可以独立开发、独立运行、独立部署，再将这些小型应用融合为一个完整的应用，或者将原本运行已久、没有关联的几个应用融合为一个应用。微前端既可以将多个项目融合为一，又可以减少项目之间的耦合，提升项目扩展性，相比一整块的前端仓库，微前端架构下的前端仓库倾向于更小更灵活。

2、它主要解决了两个问题：
- 1、随着项目迭代应用越来越庞大，难以维护。
- 2、跨团队或跨部门协作开发项目导致效率低下的问题。
![[00 assets/c144bc97a4ec1afe8be90db8ca599ce6_MD5.jpeg]]

3、在`micro-app`之前，业内已经有一些开源的微前端框架，比较流行的有2个：`single-spa`和`qiankun`。

4、`single-spa`是通过监听 url change 事件，在路由变化时匹配到渲染的子应用并进行渲染，这个思路也是目前实现微前端的主流方式。同时`single-spa`要求子应用修改渲染逻辑并暴露出三个方法：`bootstrap`、`mount`、`unmount`，分别对应初始化、渲染和卸载，这也导致子应用需要对入口文件进行修改。因为`qiankun`是基于`single-spa`进行封装，所以这些特点也被`qiankun`继承下来，并且需要对webpack配置进行一些修改。

5、`micro-app`并没有沿袭`single-spa`的思路，而是借鉴了WebComponent的思想，通过CustomElement结合自定义的ShadowDom，将微前端封装成一个类WebComponent组件，从而实现微前端的组件化渲染。并且由于自定义ShadowDom的隔离特性，`micro-app`不需要像`single-spa`和`qiankun`一样要求子应用修改渲染逻辑并暴露出方法，也不需要修改webpack配置，是目前市面上接入微前端成本最低的方案。
![[00 assets/39c4ef05dd69d8001a29a007c0433e82_MD5.jpeg]]

6、micro-app优势
- 使用简单：我们将所有功能都封装到一个类WebComponent组件中，从而实现在基座应用中嵌入一行代码即可渲染一个微前端应用。
- 功能强大：`micro-app`提供了`js沙箱`、`样式隔离`、`元素隔离`、`路由隔离`、`预加载`、`数据通信`等一系列完善的功能。
- 兼容所有框架：为了保证各个业务之间独立开发、独立部署的能力，`micro-app`做了诸多兼容，在任何前端框架中都可以正常运行。

# 2 基本接入

快速接入：[快速开始 | MicroApp](https://micro-zoe.github.io/doc/zh/start.html#%E4%B8%BB%E5%BA%94%E7%94%A8)

## 2.1 主应用接入

1、我们使用 Vue2 作为主应用，分别接入 React、Vue2、Vue3
2、`npm i @micro-zoe/micro-app` 安装
![[00 assets/01f90517f70c56240b057ea72240a897_MD5.jpeg]]

3、针对 micro-app 主要存在几种路由模式，称为虚拟路由系统：[虚拟路由系统 | MicroApp](https://micro-zoe.github.io/doc/zh/router.html)，我这里主要使用的是 `native-scope模式`
![[00 assets/b28a43d5f0056adf7937808e5f2cbb65_MD5.jpeg]]

4、我们在主应用中启动即可，并且在主应用中编写路由，其中子应用的路由 path 编写为 `/xxx*` 表示非严格模式，都会匹配到这里
![[00 assets/5913a494b7c8852a52ba5a40f5abd000_MD5.jpeg]]

5、我们使用 `micro-app` 标签作为入口
- name 表示唯一标识
- url 是你应用启动的地址，也就是加载 index.html 的位置
- baseroute 表示路由前缀
- router-mode 表示路由模式，现在最新版本使用的 search 模式，将子应用路由带到 query 参数中，我手动切换到了 native-scope 模式来处理
![[00 assets/bd9eeaa3822c715ff0e905540c60a0eb_MD5.jpeg]]

6、其实子应用路由使用 `window.__MICRO_APP_BASE_ROUTE__` 来作为前缀，这个主要是 `Native` 模式来做配置，这是为什么呢？具体可以参考：[MicroApp](https://micro-zoe.github.io/doc/zh/browser-router.html)

总结：因为子应用和主应用路由系统不是公用的一套，而是各自一套，那么路由检测也是一套。所以在 vue-router 中添加 base 来当作 scope 作用域来使用，避免路由冲突

![[00 assets/e2d15cce3d4876cb0bf399a9cc577b48_MD5.jpeg]]

7、如果是 Webpack 项目的话，需要添加跨域申请，Vite 是默认开启的
![[00 assets/b8c47474ddb11df4767acc666d160f49_MD5.jpeg]]

## 2.2 React 接入

1、我们访问会加载到 React 的子应用
![[00 assets/a7b7dca157beed865c80e0f8cfe85834_MD5.jpeg]]

2、然后再 React 中引入 Router，但是最好做一个路由前缀，避免有问题
![[00 assets/3de25384229e72fa7e5271cbb942502c_MD5.jpeg]]

3、如果在 React 中发现静态资源无法加载，可以参考下面的内容：[React](https://cangdu.org/micro-app/docs.html#/zh-cn/framework/react)
![[00 assets/f793320f7aaae1110ec00422e49bef01_MD5.jpeg]]

## 2.3 Vite 接入

1、Vite 作为子应用存在一系列的问题，并且接入 Vite 应用可以直接参考这里的教程：[Vite](https://cangdu.org/micro-app/docs.html#/zh-cn/framework/vite)
![[00 assets/27ef9f24f0b1d8768f024fb52de4f7fd_MD5.jpeg]]

2、首先来说 Vite 作为子应用需要修改的地方，路由需要修改成 Hash 路由，并且还要加载 Vite 插件
![[00 assets/e01d0eef107ddc2ceab95d210c2b4fa2_MD5.jpeg]]

3、针对基座应用需要关闭沙盒等，还要给 Vite 子应用编写 plugins
![[00 assets/9f1102175392e0f0cbeb3ae9d5e46ee6_MD5.jpeg]]

# 3 基础API

## 3.1 生命周期

1、可以直接参考文档：[生命周期](https://cangdu.org/micro-app/docs.html#/zh-cn/life-cycles)
![[00 assets/35f2a99e1d4ccadf42577eff96c0a8a5_MD5.jpeg]]

## 3.2 性能/内存优化

1、文档：[高级功能](https://cangdu.org/micro-app/docs.html#/zh-cn/advanced?id=_2%e3%80%81%e6%80%a7%e8%83%bdamp%e5%86%85%e5%ad%98%e4%bc%98%e5%8c%96)
![[00 assets/676039b31c7c22ec132d89fd579f6fc1_MD5.jpeg]]

## 3.3 JS 隔离

1、文档：[JS沙箱](https://cangdu.org/micro-app/docs.html#/zh-cn/sandbox)，针对子应用的 window 使用 Proxy 来做代理实现
![[00 assets/59f77c54e70c5642b1158a5e7f526f05_MD5.jpeg]]


## 3.4 CSS 隔离

1、文档：[样式隔离](https://cangdu.org/micro-app/docs.html#/zh-cn/scopecss)，它的本质和 Vue 的 Scoped 是差不多的


## 3.5 资源共享

1、文档：[静态资源](https://cangdu.org/micro-app/docs.html#/zh-cn/static-source?id=%e8%b5%84%e6%ba%90%e5%85%b1%e4%ba%ab)


## 3.6 预加载

1、文档：[预加载](https://cangdu.org/micro-app/docs.html#/zh-cn/prefetch)

2、预加载的本质就是使用的 [[requestIdleCallback]] API 在空闲的时间来预加载数据



# 4 数据通信





# 99 渲染原理

1、其实原理的本质就是 Web Component（Custom Element） + HTML Entry
![[00 assets/b73c612373c3b9991c128bf33ab11a1a_MD5.jpg]]

2、当我们通过路由匹配到之后，如果是 css 的话就会远程加载然后通过 style 来加载，如果是 JS 的话就是通过 eval 来加载渲染页面
![[00 assets/dcfa5ce0a1ed3ba3c0da5f9fa15194d9_MD5.jpeg]]
