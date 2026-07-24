
## 13.1 基本介绍

![[00 assets/223bfc528b717727f01198bad6ac9c64_MD5.png]]

**Koa 官方文档**：[Koa(koa.js)中文网 -- 基于 Node.js 平台的下一代 web 开发框架 (koajs.com.cn)](https://www.koajs.com.cn/#)

## 13.2 基本使用

我们先下载 koa

```bash
npm i koa  // 下载koa
```

这里就是体现出和`express`的区别，假如你在读取服务器的时候，没有任何中间件执行，就会自动爆`404`的错误，并且会返回`NOT FOUND`

假如是`express`的话，就是超出时间默认关闭连接

![[00 assets/9bf498646dbedfea2c7fab8d8a66b033_MD5.png]]

当然下面的网络请求和响应的方式和`express`还是有不一样的地方

```javascript
const koa = require("koa");
const app = new koa();

const HTTP_PORT = 8000;

app.use((context, next) => {
  // context.request;  请求
  // context.response; 响应
  // 获取请求的信息
  console.log(context.request);
  // 给客户端发送数据
  context.response.body = "Hello,Koa!";
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});

```

![[00 assets/611d5f21e9a375c487be4dcd83c41f2d_MD5.png]]

## 13.3 路由使用

![[00 assets/b494b20a910280e31f8a2c4197dabb08_MD5.png]]

很显然这种方式非常非常的麻烦，所以我们可以`kao-router`第三方库来解决

```
npm i koa-router
```

![[00 assets/38187d3bfa54b4a835cd1218fac95cef_MD5.png]]

假如我们添加`app.use(userRouter.allowedMethods())`这个中间件，就可以修改默认报错的信息

![[00 assets/0d21a41b35bf223392375f2cd7f0a64d_MD5.png]]

这样默认回复的报错内容就不一样了

![[00 assets/03d00941160e0dc3a117f9a51f906251_MD5.png]]

下面为报错默认回复的信息

![[00 assets/ec2409a48b3db15d9bac572be3091fb5_MD5.png]]

## 13.4 参数解析

### 13.4.1 params,query

下面就是使用路由来获取`params`和`query`参数

```javascript
const koa = require("koa");
const Router = require("koa-router");

const app = new koa();
const router = new Router({ prefix: "/user" });

const HTTP_PORT = 8000;

router.get("/GetInfo", (context, next) => {
  console.log(context.request.query); // 获取query参数
  context.response.body = "Query参数";
});

router.post("/GetId/:id", (context, next) => {
  console.log(context.request.params); // 获取params参数
  context.response.body = "Param参数";
});

app.use(router.routes());

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});

```

![[00 assets/75c5887593478e167be9e6d277ad1328_MD5.png]]

### 13.4.2 json,urlencoded

1、`koa`没有内置处理`json`，所以我们需要安装第三方库

```bash
npm install koa-bodyparser
```

下面就是代码的实现，其实本质和`express`是差不多的。但是这里需要注意很坑的地方，中间件是从上往下执行的，所以参数的解析必须放在路由之前，不然会出现还没解析到数据就路由跳转的情况。

而且使用这种方式会出现在前面书写一个中间件，后面的`context.request.body`不需要知道是解析`json`还是`urlencoded`的数据

```javascript
const koa = require("koa");
const Router = require("koa-router");
const bodyParser = require("koa-bodyparser");

const app = new koa();
const router = new Router({ prefix: "/user" });

const HTTP_PORT = 8000;

// 注意这里的顺序不能变
app.use(bodyParser());
app.use(router.routes());

router.post("/GetJSONorGetUrlencoded", (context, next) => {
  console.log(context.request.body); // 同时解析JSON和urlencoded数据
  context.response.body = "获取JSON数据";
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});
```

![[00 assets/04a13c7ccdf097cfd5ae2bdfc29a8062_MD5.jpeg]]

2、可能存在上传时请求体过大的情况，我们需要配置`koa-bodyparser`

参考文章：[解决 koa request entity too large - 慕尘 - 博客园 (cnblogs.com)](https://www.cnblogs.com/baby123/p/13359472.html#:~:text=解决的方法 const koaBody %3D require ('koa-body')%3B const bodyParser,jsonLimit%3A"10mb" }))%3B app.use (bodyParser ({ formLimit%3A"10mb"%2C jsonLimit%3A"10mb" }))%3B)

![[00 assets/ab79d810e9035fa32464ba495f1b8ea2_MD5.png]]

### 13.4.4 form-data

```bash
npm i koa-multer // 安装第三方库来解析koa
```

这里有一个坑，就是如何获取`context.req.body`，前面获取数据都是`context.request.body`，而且官方文档并没有提及

```javascript
const koa = require("koa");
const Router = require("koa-router");
const bodyParser = require("koa-bodyparser");
const multer = require("koa-multer");

const app = new koa();
const router = new Router({ prefix: "/user" });
const upload = multer();

const HTTP_PORT = 8000;

app.use(bodyParser());

router.post("/Upload", upload.any(), (context, next) => {
  // 这里有一个坑就是获取到的参数丢到context.req.body中了
  console.log(context.req.body);
  context.response.body = "获取form-data数据";
});

app.use(router.routes());

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});
```

上面接收的都是文本数据

![[00 assets/d6c8456ab06c986e421c58c66c9a08bb_MD5.png]]

下面就是使用该插件来提供上传文件的操作，其实和`express`是一样的。这些操作可以参考我前面的笔记

```javascript
const path = require("path"); // 处理路径

const koa = require("koa");
const Router = require("koa-router");
const bodyParser = require("koa-bodyparser");
const multer = require("koa-multer");

const app = new koa();
const router = new Router({ prefix: "/user" });
// 假如你需要指定保存地址和文件后缀名需要添加
const storage = multer.diskStorage({
  destination: (req, file, callback) => {
    callback(null, "./uploads");
  },
  filename: (req, file, callback) => {
    callback(null, Date.now() + path.extname(file.originalname));
  },
});
const upload = multer({ storage });

const HTTP_PORT = 8000;

app.use(bodyParser());

// 这里使用的是upload.single()
router.post("/Upload", upload.single("image"), (context, next) => {
  console.log(context.req.body);
  console.log(context,req.file)
  context.response.body = "获取form-data数据";
});

app.use(router.routes());

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});
```

✨ 这里有一个小坑，这里保存文件写的属性的`key`必须是`storage`，假如是`{avaterStorage : avaterSorage}`就会读取不到

![[00 assets/85fe2501cbca7e471277a16de95a8d61_MD5.png]]

## 13.5 数据响应

下面为常见的数据响应的方式

![[00 assets/606baf2f84054a72797b5189b0db7b0e_MD5.png]]

`koa`发送的数据类型会自动修改，假如你发送的是纯文本类型，`Content-type`就会设置为`text/plain`。假如你发送的是对象，数组类型的话，`Content-type`就会设置为`application/json`数据

```javascript
const koa = require("koa");
const Router = require("koa-router");

const app = new koa();
const router = new Router();

const HTTP_PORT = 8000;

app.use(router.routes());

router.get("/GetUserInfo", (context, next) => {
  // 设置状态码
  context.response.status = 400
  // 设置状态码也可以简写
  context.status = 400;


  // 响应字符串
  context.response.body = "张三";
  // 响应对象
  context.response.body = {
     name: "zjh",
     age: 18,
  };
  /*
  	context.respnse.body = "张三"，我们也可以简写为
  	context.body = "张三"，其实内部是做了一个代理
  */
  // 响应数组
  context.response.body = ["a", "b", "c"];
});

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

为什么可以简写，因为本质是在内部做了一个代理模式，这个在源码里面有

![[00 assets/b0690de1161777db83356aec944c69d2_MD5.png]]

## 13.6 静态服务器

```bash
npm install koa-static // 安装第三库
```

和`express`的处理方式差不多

```javascript
const koa = require("koa");
const KoaStatic = require("koa-static");

const app = new koa();

const HTTP_PORT = 8000;

app.use(KoaStatic("./dist"));

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

这里就可以部署静态资源，来加载使用`Vue`搭建的网页

![[00 assets/5e678483681a0980dea633288cb93dcf_MD5.png]]

使用`./dist`路径就是表示的项目根目录下面的`dist`文件夹

![[00 assets/46f36276585a7d6648345497c2ad2c2a_MD5.jpeg]]

因为现在很多的网页都是 SPA 网页，静态部署网页可能需要安装下面的库

![[00 assets/f00e8b70cd63560b8d71124c69786f87_MD5.jpeg]]

## 13.7 错误处理

下面就是错误的处理方式

```javascript
const koa = require("koa");
const app = new koa();
const HTTP_PORT = 8000;

app.use((context, next) => {
  // 模拟登录失败
  if (false) {
    context.body = "登录成功";
  } else {
    // 这里为什么是使用context.app呢？
    // 因为后期项目开发的时候，分包很多，不是那么容易就可以拿到app
    // 但是每个context中就包含了一个app
    context.app.emit("error", new Error("登录错误~"), context);
  }
});

app.on("error", (err, context) => {
  context.status = 401;
  context.body = err.message;
});

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

![[00 assets/271783b8d1cd4ed81a6ee604ad84b631_MD5.png]]

## 13.8 Koa 源码分析

> 1.创建 Koa 的过程

其实本质就是导出了一个`Application`，在里面进行了初始化的操作

![[00 assets/b5e6cdbc21edd85939e18e16e68baf78_MD5.png]]

> 监听操作

其实`app.listen()`的本质就是创建一个`server`来监听

![[00 assets/7b62ce17ad87f305817c07e7ea75c5ec_MD5.png]]

> 注册中间件

其实注册中间件的本质就是将这个中间件塞到`middleware`数组里面

![[00 assets/580dea69aac342a4c4b96ba2086a7595_MD5.png]]

> 监听回调

当响应客户端数据的时候，本质就是`server`的响应，也就是执行这里面的`this.callback()`

![[00 assets/d2ce71a4509a5e3d3cb9471e5090da09_MD5.png]]

这里的`compose`是将所有的中间件都传输给`fn`

![[00 assets/4a0d43d4826df97702b4c4a8fd0ae1fa_MD5.png]]

略...后面执行了很多操作，建议自己看源码

## 13.9 对比 express

![[00 assets/76913764a26e72f74e5652af7d69ff33_MD5.png]]

下面就是对`koa`和`express`的对比案例，这里主要是演示异步的处理方式

> express - 同步方式

```javascript
const express = require("express");
const app = express();
const HTTP_PORT = 8000;

const middleware1 = (req, res, next) => {
  req.message = "aaa";
  next();
  res.end(req.message);
};
const middleware2 = (req, res, next) => {
  req.message += "bbb";
  next();
};
const middleware3 = (req, res, next) => {
  req.message += "ccc";
};

app.use(middleware1, middleware2, middleware3);

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

当执行中间件的时候，会先执行`next()`，这个时候就会去执行`middleware1`函数，遇到`next()`的时候就会去执行`middleware2`，然后再去执行`middleware3`。

当`middleware3`执行完毕，就是去执行`middleware2`中`next()`下面的语句，执行完毕就会去执行`middleware1`中`next()`下面的语句。其实本质就是在方法中去调用其他方法

![[00 assets/daaf966639a262b11d499a6427ce3615_MD5.png]]

> express - 异步方式

这个就是`express`的短板了，假如遇到这样的需求就会很麻烦。就不能会使用中间件来处理，只能将网络调用改为`async await`同步函数

```javascript
const { default: axios } = require("axios");
const express = require("express");
const app = express();
const HTTP_PORT = 8000;

const middleware1 = (req, res, next) => {
  req.message = "aaa";
  next();
  res.end(req.message);
};
const middleware2 = (req, res, next) => {
  req.message += "bbb";
  next();
};
const middleware3 = (req, res, next) => {
  // 这里进行异步请求
  const result = axios
    .get("http://123.207.32.32:9001/lyric?id=167876")
    .then((result) => {
      req.message += result.data;
    });
};

app.use(middleware1, middleware2, middleware3);

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

结果就可以看出来，最后接口里面的数据没有连接到`req.message`上面。因为这个请求是异步请求，请求数据之后，依旧会执行后面的代码，所以不会将数据添加上去。

![[00 assets/a07dba168bd05cba7d0375df94e531df_MD5.png]]

假如要使用的话，可以使用函数来处理

> koa - 同步方式

```javascript
const koa = require("koa");

const app = new koa();

const HTTP_PORT = 8000;

const middleware1 = (context, next) => {
  context.request.message = "aaa";
  next();
  context.response.body = context.request.message;
};
const middleware2 = (context, next) => {
  context.request.message += "bbb";
  next();
};
const middleware3 = (context, next) => {
  context.request.message += "ccc";
};

app.use(middleware1);
app.use(middleware2);
app.use(middleware3);

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

> koa - 异步方式

```javascript
const koa = require("koa");
const axios = require("axios");

const app = new koa();

const HTTP_PORT = 8000;

const middleware1 = async (context, next) => {
  context.request.message = "aaa";
  await next();
  context.response.body = context.request.message;
};
const middleware2 = async (context, next) => {
  context.request.message += "bbb";
  await next();
};
const middleware3 = async (context, next) => {
  let result = await axios.get("http://123.207.32.32:9001/lyric?id=167876");
  context.request.message += result.data;
};

app.use(middleware1);
app.use(middleware2);
app.use(middleware3);

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口正在监听`);
});
```

我们使用这个方式就可以添加上去，因为`koa`本身调用`next()`的时候返回的是`Promise`，但是在`express`中调用`next()`并不是`Promise`，我们添加`async`和`await`是没用的。

![[00 assets/6220a5ab185e7f62e350ba8ab7b630ee_MD5.png]]

## 13.10 洋葱模型

这个是对应上面的`13.9 对比express`

![[00 assets/2a724102d3d379a3817ea9b77ff89982_MD5.png]]

## 13.11 Cookie,Session

这段内容可以查看**P16.2.4** 登录凭证的笔记
