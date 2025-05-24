
# 1 基本介绍

> 什么是状态管理？

![[00 assets/cd4f22a16797bbd822a5e310dd46c085_MD5.png]]

> 复杂得状态管理

![[00 assets/e784aeb4e9cac75597c89fb81891abef_MD5.png]]

> 状态管理流程

![[00 assets/88d4318f430709115fd7b42f54f6aada_MD5.png]]

# 2 State

## 2.1 基本使用

![[00 assets/bcac879d71cc3ba69357cc016b6ae91a_MD5.png]]

```bash
npm i vuex // 下载vuex
```

下面为基本的使用，通过`store.commit()`来发送一个`commit`给`store仓库`，仓库对数据进行处理

![[00 assets/e0e7d017e710f48e22585df6abc40478_MD5.png]]

其中在`模板语法`中展示数据，可以使用下面的 3 种方式

![[00 assets/c0751447ef86aed63b4db4ebdc8f0e79_MD5.png]]

## 2.2 状态映射

因为在模板语法中一直使用`$store.state.xxx`来显示数据，这个写的很麻烦，所以需要状态映射。

当然这个状态映射不仅仅是`store`，还有`actions和mutations`

> optionsAPI

![[00 assets/887052412be0c7e289f1ca13a3f9a95a_MD5.jpeg]]

> compositionAPI

方式一：自己封装函数，返回`computed`数据。

使用下面封装函数的原理其实是因为使用`mapState`的话，返回的是函数，其中执行的其实是`this.$store.state.xxx`，因为`setup()`里面没有`this`，所以就需要动态绑定`this`来处理，所以就有了下面的封装函数

其中为了能在模板中直接书写，所以就需要使用`computed`来编写

![[00 assets/e93e52509284f591098efe5c2d3481ae_MD5.jpeg]]

方式二：使用`toRefs`来处理（**推荐**）

![[00 assets/c2af3a45df9819eb14532fb544c7b461_MD5.png]]

# 3 Getters

## 3.1 基本使用

我们在`store`中添加`getters`，专门将处理之后的`state`返回出去，可以理解为`computed`

![[00 assets/b24b36658c6374bf8be38252ed58884c_MD5.png]]

![[00 assets/d5bc45aa7ba088e9e8b260234468412a_MD5.png]]

其实在`getters`中可以返回一个函数，

![[00 assets/5b202768a021c1dd0ab8f40ec746b6f9_MD5.png]]

## 3.2 Getters 映射

> optionsAPI

![[00 assets/bb55cff44b1c25b00e50fb6a9190291c_MD5.png]]

> compositionAPI

**方式一**：使用`toRefs`处理，和`State`得处理方式差不多，虽然方便，但是控制台会报警报，所以这个还是比较推荐使用封装函数的方式处理

![[00 assets/f0cd027a9bf0b615794861a25e21bc15_MD5.png]]

下面就是报错的提示

![[00 assets/df1713d614a075048ceffa293028a240_MD5.png]]

**方式二**：下面为封装的处理，和`State`是差不多的

![[00 assets/55bce9e5785ca701f21b7e82907c358b_MD5.jpeg]]

# 4 Mutation

## 4.1 基本使用

首先要知道为什么修改参数需要使用`store.commit`的方式，是为了`Vue插件`可以实时的追踪数据的改变

下面就是基本的使用，我们使用`commit`的方式提交一个命令，给`mutations`中的函数进行执行。当然我也可以携带参数来处理

![[00 assets/d502fbc592377fb8b809cfddc1f36670_MD5.png]]

当然我们使用`mutations`有一个设计规范，就是将方法都抽取到一个单独的文件里面

![[00 assets/5b798aa23e4ab749dbf84371c8b6416c_MD5.png]]

## 4.2 Mutation 映射

> optionsAPI

![[00 assets/5f38ac51dc1b8ce2512fd62d35b0a824_MD5.png]]

> compositionAPI

封装的本质和上面的`State`是差不多的

![[00 assets/1cc754cc2e7815be1c1d9ca083477ac6_MD5.jpeg]]

## 4.3 注意事项

![[00 assets/f40302509f983bbe8ef9afc41f730e1e_MD5.png]]

# 5 Actions

## 5.1 基本使用

![[00 assets/bef3d2d4bd2991836f67b8b6055ceb84_MD5.png]]

下面就是基本的使用，我们首先需要使用`store.dispatch`来对`Action`进行控制，然后`action`中发送命令给`mutations`处理，然后再来操作`state`

![[00 assets/e3d818eecd356706fed28690f1fdc76d_MD5.png]]

## 5.2 Actions 映射

> optionsAPI

![[00 assets/3c72ce8e3d09f2a122044bcc19fe1ee9_MD5.png]]

> compositionAPI

![[00 assets/a94f4c2059f38c2b75d3687f0308f369_MD5.png]]

## 5.3 网络请求

当然有 2 种网络请求方式，一个是使用`vuex`来处理网络请求，这个是将网络请求的方式抽取出来。还有一个而方式就是在组件中发送请求和管理数据。这个是 2 套不同的处理方式。

下面就是使用`vuex`来发送网络请求的一整套流程，需要在组件中发送一个`dispatch`。然后在`actions`中发送网络处理，然后发送命令给`mutations`，然后`state`来存储

![[00 assets/776818191142477e56ab8a35a1e434ca_MD5.jpeg]]

![[00 assets/aff98360cdcbb7bdafad46eb028a98df_MD5.png]]

当然我们想要监听该函数是否完毕的话，需要使用下面的`new Promise()`来处理

![[00 assets/ce6d5d93182f8e857cf875b56040e4cf_MD5.png]]

# 6 Modules

## 6.1 基本使用

![[00 assets/fe9295058e9e9598ad572ec48e05a176_MD5.png]]

下面就是整个`modules`的使用，我们将`home`的数据抽取到外面，在`index.js`中使用`modules`进行导入

最后使用的时候记得要加上`modules`的名字，比如下面使用`modules`来导入的时候加上了`home`，那么最后取出的时候就需要使用`store.state.home`来处理。当然默认情况下，使用`state`需要拼接，但是使用`actions、mutations、getters`是不需要使用的

![[00 assets/91c9144972013c6846f4992997a73cee_MD5.png]]

在`getters、actions`中存在第三个参数`rootState`，这个就是`根状态库`中的所有`state`。其中第二个参数`getters`十所有的`getters`，因为没有设置命名空间，所以都是混在一起处理的，直接使用`state.getters.xxx`就可以使用

![[00 assets/0d8da4dd7fda29f40500373e040f8ed4_MD5.png]]

![[00 assets/d3e906d2f73991dce4d618756bd27555_MD5.png]]

## 6.2 命名空间

![[00 assets/f5853952cd5725f8de80470d226c8848_MD5.png]]

我们可以将`namesepaced`设置为`true`的方式处理，设置命名空间，这样需要取出`doublenum`的话就需要使用`[name/doublenum]`处理

![[00 assets/bcd992439ddd94c8553686c88db58906_MD5.png]]

## 6.3 module 中派发

![[00 assets/a95ac7a2395aaa8de47d920ce12fb911_MD5.png]]
