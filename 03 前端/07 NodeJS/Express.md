## 12.1 基本介绍

![[00 assets/457761969ad529f8870fe0d9a90006ee_MD5.png]]

**express 官网**：[Express - 基于 Node.js 平台的 web 应用开发框架 - Express 中文文档 | Express 中文网 (expressjs.com.cn)](https://www.expressjs.com.cn/)

其实`express`的本质就是一个中间件

![[00 assets/7949ee3231eef9ba76751614c7afa3ee_MD5.jpeg]]

## 12.2 基本使用

### 12.2.1 使用脚手架

![[00 assets/bf7b47a5716c3a8093cb363a29579327_MD5.png]]

经过上面的处理就会发现已经将项目创建完成了

![[00 assets/2107ad0373a5b82ec31a25d7a24a0557_MD5.jpeg]]

### 12.2.2 常规方式

首先我们需要在一个常规的项目中下载`express`

```bash
npm i express
```

下面就是使用`express`来创建`web服务器`

```js
// 导入express,express本质就是一个函数
const express = require("express");
// 创建app服务器,app本身也是一个函数
const app = express();

// 第一个参数 请求url
// 第二个参数 回调函数，req和res分别为请求和响应对象
app.get("/", (req, res, next) => {
  res.end("Hello,Express!");
});

app.get("/user", function (req, res) {
  res.send({ name: "张三", age: 12 }); // 向客户端响应内容
});
// 和上面一样
app.post("/user", function (req, res) {
  res.send({ name: "张三", age: 12 });
});

// 监听端口为 80
app.listen(80, () => {
  console.log("开启服务");
});
```

这里有一个小知识，就是`app.get()`...中的回调函数本质也是一个中间件。`app.method`就是一种特殊的中间件

![[00 assets/b1850b997fdbf0e5f1187e5eb7b50d3b_MD5.jpeg]]

## 12.3 参数解析

![[00 assets/33ea3b0507d5e0ad5d0b0da43d456fb7_MD5.png]]

### 12.3.1 json,urlencoded

下面就是使用中间件来处理`JSON`格式的数据，这样所有的请求都会自动来处理`JSON`格式

```javascript
const expres = require("express");
const qs = require("querystring");
const app = expres();
const HTTP_PORT = 8080;

app.use((req, res, next) => {
  const ContentType = req.headers["content-type"].split(";")[0];
  if (ContentType === "application/json") {
    req.on("data", (data) => {
      req.body = JSON.parse(data.toString());
    });
    req.on("end", () => {
      res.end("服务器读取完毕");
      next();
    });
  } else {
    next();
  }
});

app.post("/login", (req, res, next) => {
  console.log(req.body);
});
// 2个post请求的JSON数据都可以直接使用中间件来获取
app.post("/Select", (req, res, next) => {
  console.log(req.body);
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听`);
});
```

![[00 assets/0d1d4142a28de564dba8a70a760f69d9_MD5.png]]

> json urlencoded

我们也可以直接使用`body-parser`来处理上面各式数据，在`express版本 4.16.x`中内置了。下面直接书写`express.json()`就可以直接处理`JSON`格式的数据了，我们不需要去手动编写

```javascript
const express = require("express");
const qs = require("querystring");
const app = express();
const HTTP_PORT = 8080;

app.use(express.json()); // 处理JSON

// 处理x-www-form-urlencoded格式的数据
// extend true:对urlencoded解析，使用第三方库qs
//        false:对urlencoded解析，使用Node.js的querystring
app.use(express.urlencoded({ extended: true }));

app.post("/login", (req, res, next) => {
  console.log(req.body);
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听`);
});
```

### 12.3.2 form-data

> form-data

**multer 官方文档**：[multer/README-zh-cn.md at master · expressjs/multer (github.com)](https://github.com/expressjs/multer/blob/master/doc/README-zh-cn.md)

下面就是解析`form-data`形式的数据

```bash
npm i multer // 先下载multer,这是express官方发布的库
```

我们使用`multer`可以解析`form-data`

```javascript
const qs = require("querystring");

const express = require("express");
const multer = require("multer");

const app = express();
const upload = multer();

const HTTP_PORT = 8080;

app.use(upload.any())

app.post("/login", (req, res, next) => {
  console.log(req.body);
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听`);
});
```

![[00 assets/20b381f72d421940e48c94f34837d75a_MD5.png]]

### 12.3.3 文件上传

> form-data 文件上传

这里有一个小问题，假如你将`app.use(upload.any())`写在`upload.single()`前面就会出现这样的问题。

![[00 assets/eccec669ee52cb9e0daa8dfb4c205813_MD5.jpeg]]

可以查看官方文档，可以发现官方的处理方式，不允许`app.any()`作为全局使用

![[00 assets/2b62f3f1b7eea09f535929859d34e87e_MD5.png]]

下面就是上传文件的整体代码。并且解决了上面的`Unexpected end of form`的问题，我们将上传的中间件写在`app.use(upload.any())`前面就可以了

```javascript
const qs = require("querystring");
const path = require("path");

const express = require("express");
const multer = require("multer");

const app = express();
const storage = multer.diskStorage({
  // 存储的位置
  destination: (req, file, callback) => {
    callback(null, "./uploads");
  },
  // 文件名字和后缀名
  filename: (req, file, callback) => {
    callback(null, Date.now() + path.extname(file.originalname));
  },
});
const upload = multer({
  storage,
});

/*
  假如你要上传文件的话，需要插入一个中间件
  upload.single就是上传单个文件，输入的参数表示获取的文件名
  upload.array表示上传多个文件
*/
app.post("/upload", upload.single("image"), (req, res, next) => {
  res.end("文件上传成功");
});

// 下面就是解析参数的代码-和上面的上传文件分开
const HTTP_PORT = 8080;
app.use(upload.any());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post("/login", (req, res, next) => {
  console.log(req.body);
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听`);
});
```

我们还可以查看文件的相关信息

```javascript
app.post("/upload", upload.single("image"), (req, res, next) => {
  console.log(req.file); // 获取文件的信息
  res.end("文件上传成功");
});
```

![[00 assets/41f4899a8203db1d7857b527d5704fe1_MD5.jpeg]]

这个时候我们也可以上传多个文件和输出多个文件的信息

```javascript
// 这里使用`upload.array`
app.post("/upload", upload.array("image"), (req, res, next) => {
  console.log(req.files); // 获取文件的信息，注意这里是files
  res.end("文件上传成功");
});
```

![[00 assets/89e337f1938595beff54d7ea7a68a008_MD5.jpeg]]

我们上传文件的时候使用的就是下面的格式来上传多个文件

![[00 assets/e05cbc7d028f7237f98d23d231942f4c_MD5.png]]

假如我们需要限制上传的个数也可以使用下面的方式

![[00 assets/569daf9765e9c88a3244f0e0dd54cd12_MD5.png]]

下面是实例的代码

```javascript
app.post(
  "/upload",
  upload.fields([{ name: "image", maxCount: 2 }]),
  (req, res, next) => {
    console.log(req.files); // 获取文件的信息
    res.end("文件上传成功");
  }
);
```

### 12.3.4 query,param

```javascript
const express = require("express");
const app = express();
const HTTP_PORT = 8080;

app.get("/user", (req, res, next) => {
  console.log(req.query); // 获取query参数
});
app.post("/login/:name/:age", (req, res, next) => {
  console.log(req.params); // 获取params参数
});

app.listen(HTTP_PORT, () => {
  console.log(`${HTTP_PORT}端口监听ing~`);
});
```

![[00 assets/d857b64af5945749c2d65b8cc2f13dfa_MD5.png]]

## 12.4 显示日志

### 12.4.1 mogan

morgan`官方文档：[expressjs/morgan: HTTP request logger middleware for node.js (github.com)](https://github.com/expressjs/morgan)

如果我们希望将请求日志记录下来，那么可以使用 express 官网开发的第三方库：`morgan`

```bash
npm i morgan // 先下载morgan
```

我们需要写`WriteStream`添加到`morgan`中，用于数据的写入

![[00 assets/86ad10cc87d48b6f7313032716401a81_MD5.png]]

下面就是日志文件的显示

![[00 assets/4eb5ee954d1b4fe514785a26783a4d44_MD5.jpeg]]

下面就是带有日志记录、文件上传、请求响应的代码

```javascript
const qs = require("querystring");
const path = require("path");
const fs = require("fs");

const express = require("express");
const multer = require("multer");
const morgan = require("morgan");

const app = express();
const storage = multer.diskStorage({
  // 存储的位置
  destination: (req, file, callback) => {
    callback(null, "./uploads");
  },
  // 文件名字和后缀名
  filename: (req, file, callback) => {
    callback(null, Date.now() + path.extname(file.originalname));
  },
});
const upload = multer({
  storage,
});
const WriteStream = fs.createWriteStream("./logs/access.log", {
  flags: "a+",
});

app.use(morgan("combined", { stream: WriteStream }));

/*
  假如你要上传文件的话，需要插入一个中间件
  upload.single就是上传单个文件，输入的参数表示获取的文件名
  upload.array表示上传多个文件
*/
app.post(
  "/upload",
  upload.fields([{ name: "image", maxCount: 2 }]),
  (req, res, next) => {
    console.log(req.files); // 获取文件的信息
    res.end("文件上传成功");
  }
);

const HTTP_PORT = 8080;
app.use(upload.any());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post("/login", (req, res, next) => {
  console.log(req.body);
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听`);
});

```

### 12.4.2 winston

1、用 `createLogger` 创建了 `logger 实例`，指定 level、format、tranports。level：打印的日志级别、format：日志格式、transports：日志的传输方式，我们指定了 `Console 和 File` 两种传输方式。

![[00 assets/5de9aff5c37cc0f037a493c148e048f8_MD5.png]]

2、如果出现未捕获的异常，可以使用`exceptionHandlers`来记录

![[00 assets/d3b60a1aad0eb8900ccb8c8caa96616b_MD5.png]]

3、我们也可以使用下面的方式创建多个`logger`实例，各司其职

![[00 assets/ed679110cceeb33079028dfcd7c7d452_MD5.png]]

4、还可以使用`rejectionHandlers`来捕获`Promise`出现的异常

![[00 assets/92455026580dc8e83c7b0a21652b379f_MD5.jpeg]]

> transports

transports 文档：[winston/docs/transports.md at a7c2eec1ef2209022f5420a314b741d88ee2ebe9 · winstonjs/winston (github.com)](https://github.com/winstonjs/winston/blob/HEAD/docs/transports.md#winston-core)

1、可能日志存在很多的需求，这里需要配置`transports`，下面介绍的`transports`需要下载一个第三方库`npm install --save winston-daily-rotate-file`

2、下面是一个`http库`，他会请求对应的地址，并且将打印的参数传递过去

![[00 assets/d55afa037a58f93077daa6252150fae5_MD5.png]]

3、当然我们也可以使用时间的库，这样即可按照时间来打印日志

![[00 assets/379396e013088dff0905f30559d8eee2_MD5.png]]

4、同时他也支持动态添加`transports`

![[00 assets/55eca2857357a57871be31f4911973d1_MD5.png]]

5、如果需要直接在社区中查找对应的`transports`即可

> 日志等级

1、从上往下，重要程度依次降低。比如当你指定 level 是 info 时，那 info、warn、error 的日志会输出，而 http、debug 这些不会。

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325048.png" alt="image-20231220232522229" style="zoom:50%;" />

> format

1、下面是`format`的几个模式

![[00 assets/bdea9b479924dd6bac3cd0de0cf7118f_MD5.jpeg]]

2、我们也可以使用`winston.format.combine()`来添加组合`format`

![[00 assets/c370da49a2d99010694cf8c1fca88e53_MD5.png]]

3、可能不同的`transports`存在许多的`format`，分别设置即可

![[00 assets/3534b2975327eda47319e7bbaa2b405e_MD5.jpeg]]

## 12.5 响应数据

假如你是原生的形式，可以使用下面的方法来响应`JSON`数据

```javascript
const express = require("express");
const app = express();
const HTTP_PORT = 8000;

app.get("/login", (req, res, next) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ name: "zjh", age: 18 }));
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});
```

![[00 assets/072fde14044b3a6f0db424fd52eeadf1_MD5.png]]

假如我们使用`express`的形式来发送`JSON`数据的话，直接使用`res.json()`就可以了

```javascript
app.get("/login", (req, res, next) => {
  res.status(200); // 发送状态码
  res.json({ name: "zjh", age: 18 }); // 发送数据
});
```

假如你想发送更多的信息的话，可以查看官方网站：[Express 4.x - API Reference - Express 中文文档 | Express 中文网 (expressjs.com.cn)](https://www.expressjs.com.cn/4x/api.html#res)

## 12.6 路由

下面就是路由的使用

![[00 assets/9df2aebd09bef724ffd9d402eed4a98b_MD5.png]]

假如我们去访问的话没啥问题

![[00 assets/e7303cba6a02b68325c32368c01fe543_MD5.png]]

## 12.7 静态资源托管

![[00 assets/10721197290e87e7e7524f6dae510f73_MD5.png]]

1、我们这里使用`app.use(express.static("public"))`来托管该目录下的资源，这样我们直接在 url 里面输入`http://127.0.0.1:80/index.html`就可以进行访问，而不需要去输入文件地址

![[00 assets/e07e34d16a5b9978007c193605a12252_MD5.png]]

并且我们也可以一次性去挂载多个静态文件，假如在 public 文件夹下面没有相应的文件，就会去 files 文件下去寻找

![[00 assets/d204a61804c8acb5154e6a1e307cceb3_MD5.png]]

假如我们要访问里面的文件，直接输入文件名就可以访问到。因为你设置了静态部署的话，就默认摊在一个文件夹中被读取，客户端这里输入的和服务器端是不一样的

![[00 assets/f2f11e12addace4fefa7f0ca94e0e2ea_MD5.png]]

使用上面的方式就是**从上往下寻找**，但是我们使用这种方式指定访问前缀

![[00 assets/0997a7b55e764c4293da0b0a2d54eb3e_MD5.png]]

2、如果外面使用静态资源托管来处理`Vue`打包之后的项目，可能存在路由问题，比如前端路由显示`/device/index`，但是这只是`spa`中`Vue`的前端路由显示的。这个时候我们刷新浏览器的话，就会导致使用该地址请求服务器，这个时候肯定是没有对应的前端路由，而且也不会有对应的`html`文件，因为这里使用的是`spa`页面

3、我们可以使用`connect-history-api-fallback`库来处理这个问题

参考文章：[connect-history-api-fallback 库的理解\_astonishqft 的博客-CSDN 博客](https://blog.csdn.net/astonishqft/article/details/82762354)

![[00 assets/324b6a1c9780b0963151573f60c54303_MD5.png]]

## 12.8 错误处理

下面的方式来处理不是很好，因为判断的逻辑。到时候查询的逻辑都是写在一起的，这样会导致逻辑糅合在一起

![[00 assets/f07af98793e199a758077235d2cc098f_MD5.png]]

错误码总结：[Koa(koa.js)中文网 -- 基于 Node.js 平台的下一代 web 开发框架 (koajs.com.cn)](https://www.koajs.com.cn/#response)

下面就是模拟的错误代码的处理，这里还是分离的思想，将错误的信息都定义好，到时候直接直接输出即可，假如要更改错误的信息，直接修改这里错误信息就可以了。

`next()`里面可以直接传入错误信息，并带入到下一个中间件中。而且`app.use()`是四个参数的时候，你在`next()`中添加`new Error()`，就会自动执行这里的代码带四个参数的`app.use()`。假如你输入的三个参数就不会执行

```javascript
const express = require("express");

const app = express();

const HTTP_PORT = 8000;
const USERNAME_DOES_NOT_EXITS = "USERNAME_DOES_NOT_EXITS";
const USERNAME_ALREADY_EXITS = "USERNAME_ALREADY_EXITS";

app.post("/login", (req, res, next) => {
  // 模拟登录失败
  if (false) {
    res.json("登录成功");
  } else {
    // 假如这里使用 new Error() 传入next()
    next(new Error(USERNAME_DOES_NOT_EXITS));
  }
});

app.post("/register", (req, res, next) => {
  // 模拟注册失败
  if (false) {
    res.json("注册成功");
  } else {
    next(new Error(USERNAME_ALREADY_EXITS));
  }
});

app.use((err, req, res, next) => {
  let status = 400;
  let message = "";

  switch (err.message) {
    case "USERNAME_DOES_NOT_EXITS":
      message = "username does not exits";
      break;
    case "USERNAME_ALREADY_EXITS":
      message = "username alreday exits";
      break;
    default:
      message = "NOT FOUND~";
      break;
  }

  res.status(400);
  res.json({
    errCode: status,
    errMessage: message,
  });
});

app.listen(HTTP_PORT, () => {
  console.log(`端口${HTTP_PORT}正在监听~`);
});
```
