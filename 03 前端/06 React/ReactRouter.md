## 4.1 基本使用

![[00 assets/08fda75a8395436cc8f65b0534da0b26_MD5.png]]

```bash
npm i react-router-dom	// 安装
```

![[00 assets/08bccc6647417c6670798bff93cb54d0_MD5.png]]

![[00 assets/f6b8296c79a0675c29a08d0e2b83f375_MD5.png]]

![[00 assets/ba178202388e964f0ff74dff52245c2a_MD5.png]]

1、下载`raect-router-dom`，并且导出`HashRouter`和`BrowserRouter`包裹，这样整个`App`就可以使用路由

2、`Routes`包裹`Route`，表示单个路由。使用`Link`表示导航，其实底层本质就是`a标签`

![[00 assets/cd4dd165c75fd40193dfafe43c3ee5d0_MD5.png]]

## 4.2 Navigate

![[00 assets/5f1db87996518de1118b8f056f84e3b3_MD5.png]]

1、`Navigate`本质就是做重定向。下面就是登录场景的重定向，我们点击登录之后重新执行`render`函数，就会将`Navigate`挂载上去，就会自动执行`/home`的路由

![[00 assets/97105ee45d7494e04f847e75d4d90c08_MD5.jpeg]]

2、我们之前是按照这样的方式来加载重定向的，这个本质会加载 2 个`Home`组件，所以不是最优解

![[00 assets/e00b6d01a4d4e15140c217867ef41463_MD5.png]]

我们直接使用`Navigate`组件就可以解决这个问题即可，只要加载`/`就会跳转到`/home`

![[00 assets/05a5f300d8c3fc82edcfb8191fe939a9_MD5.png]]

## 4.3 路由嵌套

![[00 assets/b27ff5b8a861567c4d3dc3780ca34402_MD5.png]]

1、下面就是路由嵌套的原理，这样我们输入`/home/banner`就会跳转到`HomeBanner`。并且需要注意，如果你写在`/home`映射下面，就必须要带有`/home/xxx`才能正常使用

![[00 assets/5e5fdaec2574e9c3042adfc67c238616_MD5.png]]

2、在`Home.jsx`中直接使用`Link`标签确定路由，并且使用`Outlet`来占位，类似于`Vue`的`RouterView`，只要切换了路由就会将`组件`填入到`Outlet`

![[00 assets/c3a452ba8f52080ad2451bddeb0c9936_MD5.png]]

3、这里有一个小细节，`Outlet`组件只作为父路由中的子路由的元素。假如我在`About`和`Home`中分别写上`Outlet`的话

![[00 assets/5249b2adadae6d5a9b5e7b7ce116ac7a_MD5.png]]

就会根据路由映射来写入子元素的内容

![[00 assets/9e655f2a3d09402633ca653e5273fb60_MD5.png]]

## 4.4 手动跳转

![[00 assets/3cc5dac65f28c893e52e9f0bfbb5c1cc_MD5.png]]

1、我们需要手动的跳转路由就需要使用`useNavigate`函数，但是我们在`class`组件中使用就会报错

![[00 assets/2fc9a7ba23cf6067d3e3f401ed05c7df_MD5.png]]

现在唯一的方式就是使用函数组件来处理，或者采用`React Hook`来处理。在类组件中没有方法

![[00 assets/3b69afec29cf65eb872e57976e39607c_MD5.png]]

2、假如我们要在`类组件`中实现这类效果，就需要封装高阶组件来处理

3、我们在函数组件中使用`useNavigate`，因为后续可能通过`router`来传递其他的数据，所以将`navigate`方法通过`props`传递给类组件

4、在类组件中通过`this.props`来接收传递的函数，进行路由的跳转

![[00 assets/551857b3aa650e8ea7fc82e7ffc9c489_MD5.png]]

5、这样嵌套内层的路由也可以跳转到其他上层路由中

![[00 assets/7ae619771428db53d01e00a4cc714e07_MD5.png]]

## 4.5 参数传递

![[00 assets/7ab49d482d50e430ceeffe4950be9e76_MD5.jpeg]]

> params

1、配置路由映射得时候添加`:id`，这样我们输入`/home/songInfo/100`得时候就可以获取到`id`为 100

![[00 assets/4bada381c9cbba04e7d2dbf256f265e0_MD5.png]]

2、我们编写高阶组件`withRouter.jsx`，为里面添加`useParams`函数，并且传递出去即可

![[00 assets/06965b04bac0d3744fed660ab137d820_MD5.png]]

3、使用高阶组件`withRouter`来包裹，右边得组件使用用于跳转路由得，左边得组件时用于接收参数得。

![[00 assets/46b9c11d32b1557a31b54082a1af2b74_MD5.png]]

> query

1、发送`query`参数得`URL`

![[00 assets/c7198256e83e79720f409cf90cb6b3ce_MD5.png]]

这里有一个注意得点，就是`Query`参数不需要在后面编写类似`:id`得标识

![[00 assets/4f8440c990b25731428145231d6195af_MD5.png]]

2、这里存在 2 个方法来解析`query参数`，第一个`useLocation方法`相对来说比较难，但是基本都是使用第二个方法。将数据解析出来之后通过`props`传递即可

![[00 assets/3dc214355b6b0b8742544f14822381da_MD5.png]]

获取`query`然后使用就行

![[00 assets/0e0c22c75f230c709f1e7b1d66243c99_MD5.png]]

3、这里解析一下`useSearchParams()`返回得参数`URLsearchParams`，下面是`MDN`得解释

![[00 assets/65c7fe27b89df77eff4f732a4befae8c_MD5.png]]

1、我们看下面打印得结果可以看到，首先`URLSearchParams`是实现了`entries`函数，并且`URLSearchParams`内部就实现了迭代器，并且迭代器得名字就叫做`entries`，所以本质`entries`就是迭代器

2、并且我们使用`entries()`返回得对象使用`next()`就会输出数据，这一部分得源码可以参考我`ES6 迭代器`得笔记

3、我们使用`foreach`来遍历得时候可以看到最后得结果其实就是`[["name","zs"],["age",18]]`得格式，这里其实就是`ES8`得`entries`得格式，所以这里我们使用`Object.fromEntries`转化为对象

4、并且遍历`searchParams`得时候，就是遍历`searchParams.entries()`

![[00 assets/ed84bed7d2cc01d59cca53e3f2261ff2_MD5.png]]

5、下面就是模拟的上面的`searchParams`，可能因为历史遗留问题，所以底层可能不是这么实现的。但是本质就是下面的代码，迭代器遍历，只不过数据模式不是常见的`对象模式`

![[00 assets/a8c013475bcffd5be72f5e4e00681a52_MD5.jpeg]]

## 4.6 路由配置

### 4.6.1 路由抽离

![[00 assets/fb5f8d805049229a83ad37d20417acb2_MD5.jpeg]]

1、我们一开始默认在`App.jsx`中编写得路由映射存在问题，当项目变大之后，入口文件`App.jsx`就会变得很大，所以就可以使用类似`Vue`得路由配置，将路由信息抽离出去。

其中得属性都是和原本得路由映射是一一对应得

![[00 assets/47f7bfbece0ca3996aebc8888ad2875a_MD5.png]]

2、最后在函数组件中使用`useRoutes`，并且导入刚刚得编写的`routes`，它就会将数组变为路由映射，这样就实现了路由配置信息的抽离

![[00 assets/3f1e7309820899dd60462b11bb1a2653_MD5.png]]

### 4.6.2 路由懒加载

1、其实`import(...)`是`webpack`的特性，这样我们打包的时候就会分包处理，提升首屏开启速度

![[00 assets/e9cfe1579e970050fa60f55fb406f19f_MD5.png]]

2、但是存在包还没下载下来，但是路由已经跳转进去的情况，这个时候需要做应急处理。这个时候就需要使用`Suspense`高阶组件来处理。这样即便没下载到包也可以内容可以显示

![[00 assets/77b30af2ff249e9e8dbcc6eeb864254f_MD5.png]]

## 4.7 额外使用

### 4.7.1 NavLink

![[00 assets/bbb79241be71ea7a2802bdcf5368c317_MD5.png]]

1、`NavLink`使用的场景不是很多，和`Link`唯一的区别就是可以添加`style`和`class`。下面就是一种，只要你点击之后就会将颜色变为`red`

![[00 assets/348d3b0d0e0c5a34139a981977188d7c_MD5.jpeg]]

我们点击之后`style`会自动变化

![[00 assets/92f2f4eb7c8843dc9f06429a5b52c48b_MD5.png]]

2、对于`className`的本质也是和`style`差不多，点击之后修改`style`或者`className`

![[00 assets/8d84ef458e723d902d2df0753980b44b_MD5.png]]

### 4.7.2 NotFound

`path`为`*`的话表示统配，这样不知名的路由就会跳转到`NotFound页面`

![[00 assets/fe738d1da181bfcdb9d3f10811a2063b_MD5.png]]
