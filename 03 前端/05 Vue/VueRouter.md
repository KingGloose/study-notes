
# 1 基本介绍

> 基本介绍

![[00 assets/e46c436ee01842f5dbbea49756ce4888_MD5.png]]

> 后端路由阶段

![[00 assets/ed40444b6420cd74e09473fb8af1baf6_MD5.png]]

> 前后端分离阶段

![[00 assets/6e774495b80c38aa1de48baeac7da1e1_MD5.png]]

> 单页面富应用

![[00 assets/f13d8542112255504d5b8aae8f69a3e6_MD5.jpeg]]

# 2 路由原理

使用下面得 2 种方式是实现路由得原理，在 URL 改变得情况下不刷新页面

> URL 的 hash

![[00 assets/19b2c469317285136fc026716949d15c_MD5.png]]

> HTML 的 History

![[00 assets/cff186d4edfd715eda59308df6560d03_MD5.png]]

# 3 基本使用

## 3.1 基本流程

下面只是展示基本配置基本流程

> 下载

```bash
npm i vue-router // 下载vue路由
```

> 使用

![[00 assets/c87ebc623f3c27dd453773e5e62f6ed6_MD5.png]]

下面就是使用`路由`得一整套流程，可以参考上面得流程图来配置`Vue-Router`

![[00 assets/a2796b6d7e95213ab64d552d353b413a_MD5.png]]

## 3.2 history 模式

假如你使用`Hash模式`得话，前面会多一个`#/`得符号来区分后面得地址。但是使用`History模式`就不会存在

![[00 assets/32fd48fec481fee50357af2ba8e9589a_MD5.png]]

我们这里使用`router`中得`history`来配置

![[00 assets/896df1400b21a3d1c1924628dee63d69_MD5.png]]

## 3.3 router-link

![[00 assets/02377215da89f27a7562c5ccc6f245bd_MD5.png]]

> to 属性

可以使用 2 种方式来配置`to属性`

![[00 assets/931aa5178dbc46603849d81f7fad5012_MD5.png]]

> replace 属性

也就是**覆盖**上一条记录，点击浏览器得返回按钮就回不到上一条记录

> active-class

原本我们点击`routerlink`得时候会有类名`router-link-active`在按钮之间跳转，表示点击了那个`router-link`，但是这个`class`可能不是很好，所以我们可以使用`active-class`来修改这个类名

![[00 assets/87a5d0e26c9c2e9c8221a8c4f24c79e8_MD5.png]]

## 3.4 路由懒加载

![[00 assets/1eb49ab0ab313b3b4df3c833b415ae2a_MD5.png]]

我们使用`import函数`来对`路由`中得组件进行懒加载得操作，这样在打包得时候就会分包处理

![[00 assets/05ed64b5cc9e2548d245757f8f052cd9_MD5.png]]

下面就是打包的效果，其中前面是`About.86...`就是名为`About`的包

![[00 assets/7c531abe1ffb9b4f0a88b9904bdbb25c_MD5.png]]

# 4 获取参数

> 2023.9.23

最近在做项目的时候发现了下面的`params`和`query`使用上的一个区别，因为`params`在路由上需要添加`/:id`来表示当前占位，如果没有这个路由就会跳转不到，但是`query`不需要也可以

在后端返回动态路由的时候，可能有的时候是不带有`:id`这类的`params`的参数，所以我们可以采取使用`query`来替代

![[00 assets/b40ff0fcbff79ca7faee8edbe06be2f5_MD5.png]]

## 4.1 params

![[00 assets/227295d54b2c1cb736371da10962f0e5_MD5.png]]

下面就是获取参数的方式

![[00 assets/e5340efd1167127725df56018feda4d8_MD5.png]]

假如我们要获取的话和下面的`query`是一样的，只需要在`route.params`中获取即可。并且这里需要注意一个`router`和`route`的区别，其中`router`是获取实例的，但是`route`是获取当前地址

## 4.2 query

我们可以使用`编程式导航`传递`query参数`，假如需要获取的话，就使用`$route.query`来获取

![[00 assets/86014df6d5cfd6fba11a4f75aa2e92b0_MD5.png]]

其实我们在这里传输`query`，并且取出该数据和上面的`params`是一样的处理方式

![[00 assets/d260f870f10ee764824e0c7abf23d75c_MD5.png]]

# 5 NotPage 处理

当匹配不到任何路径的情况下，可以使用`/:pathMatch(.*)`来将路由指定到`NotFound页面`
![[00 assets/aa748104ff4128004e28e646785d75ba_MD5.jpeg]]

下面就是在后面添加`*`来区别解析的方式

![[00 assets/ea1ecf76e45a2df86a59b572f5ac96f4_MD5.jpeg]]

# 6 编程式导航

下面是基本的使用，我们使用`push`的方式来进行跳转，进行手动跳转

![[00 assets/2ba5e3071f1a4dc492e2819ec74c5254_MD5.png]]

其中`向前向后`的跳转就是下面的`go、back、forward`

![[00 assets/c814417188ef4ac4c6750cd602f89077_MD5.jpeg]]

# 7 动态管理路由

这个技术一般是在`管理后台`来做，因为需要区分`管理员、服务员....`得身份，因为以前都是直接通过隐藏路由得方式来处理，这个方法很不好，所以我们可以通过下面动态添加路由得方式来处理，这样管理员就不能通过`url`控制栏相互跳转

下面得方式就是动态管理路由得一个思路，其中`isAdmin`是后台传输过来得，来动态管理权限

![[00 assets/660f356dbded3d172e46d11fc7e72ebe_MD5.png]]

我们使用下面得`3种方式`来对路由进行管理，但是不是经常使用

![[00 assets/044e099241a4427afa3f7a9b9451f38c_MD5.jpeg]]

# 8 路由守卫

路由守卫主要是使用`beforeEach()`。该函数还有 2 个参数，第一个参数是`去哪里`，第二个参数是`从哪里来`

![[00 assets/b2e0aa4af86bbf89e67104d4e8cda560_MD5.png]]

下面就是路由守卫在`beforeEach`中得返回值不同，可以达到不同得效果

![[00 assets/8bd59de80cf66cae5567ed2c3f07ec0d_MD5.png]]

下面是完整得导航解析流程

![[00 assets/eb717b3679f5ba3172a047512efeadce_MD5.jpeg]]

