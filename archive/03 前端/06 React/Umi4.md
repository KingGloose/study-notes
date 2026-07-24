# 1 基本介绍

[Umi 介绍](https://umijs.org/docs/introduce/introduce)

1、我们可以知道 Umi 是做什么用的
![[00 assets/0e0bde55c78b54c97de87cb9ab5c6d7a_MD5.jpeg]]

2、Umi 如果是一个前端的应用框架，那么 Umi Max 就是积累了大量的插件而开发使用的
![[00 assets/53bca58a99e276e6a47405182cbcbe29_MD5.jpeg]]


# 2 基本使用

## 2.1 项目创建

1、这里我们使用 Umi Max 来做项目的创建，本质其实是一个脚手架
![[00 assets/ce365f281f55ae68bfea8565b3d02439_MD5.jpeg]]

2、按照如上的操作方式，最终生成的结果如下。可以看到不仅仅做了 Git 约束、格式化等内容，并且组件使用 antd 组件库
![[00 assets/6cbc1c8c9d9f3158c271917c42a80599_MD5.jpeg]]

3、如果发现不满足要求要怎么做？依旧可以使用脚手架的微生成器来自动生成代码
![[00 assets/32c4cafe76716cd2b40e28485810dea3_MD5.jpeg]]


## 2.2 项目配置

1、针对配置有2种方式， `.umirc.ts` 和 `config/config.ts` 其中 `.umirc.ts` 优先级比较高
2、其中的配置可以参考：[Umi配置](https://umijs.org/docs/api/config)
![[00 assets/b2c33e5744df0f2acc2047fd1e09c144_MD5.jpeg]]
我们就可以配置一个 `alias` 来做路径映射
![[00 assets/5b78b84b030764170d85dbb8cf1813ea_MD5.jpeg]]

3、另外一种就是 `config/config.ts` 的模式
![[00 assets/110c0791053d2fc30dab749423950858_MD5.jpeg]]


# 3 微生成器

1、如果你想使用微生成器，可以使用 `npm i umi -g`，再使用 `umi` 来作为脚手架生成文件
![[00 assets/2e242b3524a35f2517313475ea4a4990_MD5.jpeg]]

2、但是目前的 `umi` 有一个问题，在 `.umirc.ts` 中编写 `require.resolve` 的时候会出现解析错误
![[00 assets/eb1e0e2f310adb893d407e4cee604c46_MD5.jpeg]]

3、我们可以使用脚手架自动生成文件，基本和 nestjs 差不多
![[Pasted image 20250519003452.png]]


# 4 路由配置

[Umi路由参考链接](https://umijs.org/docs/guides/routes#%E8%B7%AF%E7%94%B1%E7%B1%BB%E5%9E%8B%E9%85%8D%E7%BD%AE)

1、针对 Umi 来讲路由是约定式和配置式都有，可以自己选择
2、针对路由中的 Component 设置，可以使用相对路径也可以使用`@`来定义
![[00 assets/8070371d8546880d92aeb409f5ac5def_MD5.jpeg]]
3、如下就是路由的配置
![[00 assets/678a304077f3de3899a81ae2e4134545_MD5.jpeg]]

4、要实现路由的跳转可以使用下面的3种方式
![[00 assets/187af8d2d6a9d5c5d0b0e855685ef345_MD5.jpeg]]


# 5 Tailwind CSS

[Tailwind CSS 插件](https://umijs.org/docs/max/tailwindcss)

# 6 Pro Component

[布局与菜单](https://umijs.org/docs/max/layout-menu)

1、我们可以直接使用 Pro Component 的 ProLayout，并且还内置了 antd
![[00 assets/e940fbdda3b4bf084dc59210c21fb618_MD5.jpeg]]


# 7 数据流

[数据流](https://umijs.org/docs/max/data-flow)


