视频讲解：[01.初识 Node-浏览器中的 JavaScript 运行环境\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1a34y167AZ?p=2&spm_id_from=pageDriver&vd_source=2d46cc0fa105788201e3e43d9c83f528)

视频讲解：[【NPM】包管理工具 #node package manager\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Dv411W7XP?spm_id_from=333.999.0.0)

视频讲解：CodeWhy 王红元 - 深入 Node.js 技术栈 - 2020

视频讲解：coderwhy - 前端系统课 - Node.js

视频讲解：[130*Mongodb_Mongodb 介绍*哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1gM411W7ex?p=130&vd_source=2d46cc0fa105788201e3e43d9c83f528)

视频讲解：[OS\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1cV4y1B7P4?p=13&vd_source=2d46cc0fa105788201e3e43d9c83f528)

文档介绍：掘金 - 从前端到全栈 - 十年踪迹

# 1. 入门

## 1.1 介绍

> V8

**这里可以查看我`JS高级`的笔记**

> 基本介绍

首先`Node.js`也是`JS`，所以要运行在`JS运行引擎`中，这里主流的就是使用**V8**。但是`Node.js`并不运行在浏览器，而是在`服务器`中，所以也剔除了很多和浏览器不相关的东西，比如`HTML\CSS`、`Blink`......

![[00 assets/ecce7f1a38c43d2081216e09f3f80a3d_MD5.png]]

`V8引擎`中`浏览器`和`Node.js`的的关系

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324901.png" alt="image-20220831092825273" style="zoom:80%;" />

所以它**不具有浏览器提供的 DOM API**，比如 Window 对象、Location 对象、Document 对象、HTMLElement 对象、Cookie 对象等等。但是，Node.js 提供了自己特有的 API，比如全局的 global 对象，也提供了当前进程信息的 Process 对象，操作文件的 fs 模块，以及创建 Web 服务的 http 模块等等。这些 API 能够让我们使用 JavaScript 操作计算机，所以我们可以用 Node.js 平台开发 web 服务器。

![[00 assets/ab671e7d69782709646925e0035a124f_MD5.png]]

下面就是`node.js`的另外一种原理图片，我们可以知道在**中间层**支持**事件循环队列**

![[00 assets/0c8c4e81d92e854cf18689a8ff71cbd7_MD5.png]]

下面是 Node.js 的基本架构，我们可以看到，Node.js 是运行在操作系统之上的，它底层由 V8 JavaScript 引擎，以及一些 C/C++ 写的库构成，包括 libUV 库、c-ares、llhttp/http-parser、open-ssl、zlib 等等。

其中，libUV 负责处理事件循环，c-ares、llhttp/http-parser、open-ssl、zlib 等库提供 DNS 解析、HTTP 协议、HTTPS 和文件压缩等功能。

在这些模块的上一层是中间层，中间层包括`Node.js Bindings`、`Node.js Standard Library`以及`C/C++ AddOns`。`Node.js Bindings`层的作用是将底层那些用 C/C++ 写的库接口暴露给 JS 环境，而`Node.js Standard Library`是 Node.js 本身的核心模块。至于`C/C++ AddOns`，它可以让用户自己的 C/C++ 模块通过桥接的方式提供给`Node.js`。

中间层之上就是 Node.js 的 API 层了，我们使用 Node.js 开发应用，主要是使用 Node.js 的 API 层，所以 Node.js 的应用最终就运行在 Node.js 的 API 层之上。

![[00 assets/45a94aa6b718b8596c16e8ba3f3fef4c_MD5.jpeg]]

> 内置模块

Node.js 内置的模块比较丰富，常用的主要是以下几个。

- File System 模块：这是操作系统的目录和文件的模块，提供文件和目录的读、写、创建、删除、权限设置等等。
- Net 模块：提供网络套接字 socket，用来创建 TCP 连接，TCP 连接可以用来访问后台数据库和其他持久化服务。
- HTTP 模块：提供创建 HTTP 连接的能力，可以用来创建 Web 服务，也是 Node.js 在前端最常用的核心模块。
- URL 模块：用来处理客户端请求的 URL 信息的辅助模块，可以解析 URL 字符串。
- Path 模块：用来处理文件路径信息的辅助模块，可以解析文件路径的字符串。
- Process 模块：用来获取进程信息。
- Buffer 模块：用来处理二进制数据。
- Console 模块：控制台模块，同浏览器的 Console 模块，用来输出信息到控制台。
- Crypto 加密解密模块：用来处理需要用户授权的服务。
- Events 模块：用来监听和派发用户事件。

> 应用场景

![[00 assets/b25973939ce8f939d35a28e97653e0e4_MD5.png]]

## 1.2 安装

> Node.js 安装

Node.js 官方文档：[Node.js (nodejs.org)](https://nodejs.org/en/)

Node.js 中文文档：[Node.js 中文网 (nodejs.cn)](http://nodejs.cn/)

> Node 版本

如果需要安装多个`Node.js`的话，需要`nvm(Node version manager)`或者`n`来管理`Node`版本，但是不支持**windows**

这里只是指一条路，假如需要一个计算机同时要安装多个版本的可以参考这个工具

## 1.3 使用

![[00 assets/b2b14ebf856b6d29e2269772e5070184_MD5.jpeg]]

## 1.4 REPL

**REPL**是**Read-Eval-Print Loop**的简称，翻译为**"读取-求值-输出”循环**。REPL 是一个简单的、交互式的编程环境。其实浏览器的`console`就是一个基本的`REPL`

![[00 assets/aa70f08ac1cdbe4c5e44ba30fad5479c_MD5.jpeg]]

下面就是`Node`的`REPL`的环境

![[00 assets/cb06014f1c67845bde6214f4f5a80f2a_MD5.png]]

在`Node`的`REPL`也支持多行函数语句

![[00 assets/3d8a41ab83401fe8faf7fcd349aa0ee9_MD5.png]]

`Node`其实也有`浏览器`差不多的`window`对象，它就是`global`。但是`process`也是属于一种全局变量

![[00 assets/563dcd6f69b74df5bca8de0d851da6e7_MD5.png]]

## 1.5 全局对象

### 1.5.1 特殊的全局对象

![[00 assets/0e70e38e326dc022802e1e703a475866_MD5.png]]

其中`__dirname`、`__filename`可以查看我下面的笔记

#### 1.5.1.1 __dirname

1、用于获取当前执行`js`文件的绝对路径
![[00 assets/50f1100162cba87457df51da58308824_MD5.png]]

2、为什么可以拿到 `__dirname` 本质是因为 NodeJS 是一个函数的环境 `function(xxx)` 那么可以直接拿到 `__dirname` ，如果你在 NodeJS 中使用 ESM 模块，就没有 `__dirname`，那么我们想使用 `__dirname` 该怎么做呢？
![[00 assets/8555da7059229dbfe32029ba89df7279_MD5.png]]

#### 1.5.1.2 \_\_filename

这个和上面的`__dirname`的区别就是，就是这个全局对象是带有文件，但是上面的只能到文件夹

![[00 assets/9da90f412408b9ecf046c3287d8fc6cf_MD5.png]]

`__dirname`和`__filename`就是一种**特殊的全局变量**，算是全局变量。但是只能在模块中使用，并且控制台打印也是没有的

![[00 assets/e75ee867d5e030d82f89a683e607ce09_MD5.jpeg]]

### 1.5.2 常见的全局对象

![[00 assets/e747eb97f8e133f915afe7f0c80261b5_MD5.png]]

#### 1.5.2.1 process

我们在`node`的时候可以给运行环境传递参数

![[00 assets/b775136f379bf0a436c1a8effa946683_MD5.png]]

下面是关于`argv`的解释，`vetor`这种数据结构在`Java`集合里面提到过

![[00 assets/236bd230caf0ef19c61144cd416ef96f_MD5.png]]

\*`process.platform`可以获取电脑的平台

#### 1.5.2.2 console

其实最基本的就是`console.log()`可以在控制台打印数据。假如我们需要清除控制台的话就需要使用到`console.clear()`，我们直接在控制台打`cls`也是可以的

这里有一个特别的数据，可以追溯调用栈，他就是`console.trace()`

![[00 assets/b7265e9db28e367f0adc416a81ad045f_MD5.jpeg]]

官方文档：[Console | Node.js v16.17.0 Documentation (nodejs.org)](https://nodejs.org/dist/latest-v16.x/docs/api/console.html)

#### 1.5.2.3 定时器函数

```javascript
setTimeout(() => {
  console.log("setTimeOut");
}, 100);

setInterval(() => {
  console.log("setInterval");
}, 1000);

// 和setTimeout()设置为0是有区别的
setImmediate(() => {
  console.log("setImmediate");
});

// 它是优先去执行
process.nextTick(() => {
  console.log("process.nextTick");
});
```

![[00 assets/e7fc9844ab96f45cdc2e8492f17384fb_MD5.png]]

当然还有`clearSetTimeout`...等可以去清除定时器

#### 1.5.2.4 global

![[00 assets/de1d4f6c7cf8677a258a95c44238a3e3_MD5.png]]

但是上面并不是`global`所有的内容，我们需要进入到`REPL`中，输入`global. + tab + tab`就可以去查看`global`所有的内容。

![[00 assets/f95d3f3d2944a41821aa64256b99841b_MD5.png]]

`global全局变量`和浏览器中的`window`有点像，但是并不完全像，我们可以看下面的例子

![[00 assets/7a83129c252eb97384ea81ad56dcf86c_MD5.jpeg]]

你放在`Node`中是不行的

![[00 assets/6848f3051cbcf8b637c60f274202df32_MD5.png]]

这是因为**window**本身是不分模块的，所以数据可以访问到。但是**node**是分模块的，假如你设置了一个变量，这样就干扰了各个模块的变量名

下面就是`node`源码，它是通过`ObjectDefineProperty()`来对`global.process`中进行双向绑定

![[00 assets/fb18ab74b0758992ef34d96cb366ce1c_MD5.png]]

不是很清楚为什么进入到`node`的`REPL`的时候就可以去运行，并且可以查找到数据

![[00 assets/384b91e4ca8aadc30fdc3c81702e4fc0_MD5.png]]

## 1.6 版本切换

1、`nvm-window`用于`window`系统中`Node.js`的版本切换：[coreybutler/nvm-windows: A node.js version management utility for Windows. Ironically written in Go. (github.com)](https://github.com/coreybutler/nvm-windows)

![[00 assets/595c979893c5e5b7788a137f6890083b_MD5.png]]

2、注意我们安装`nvm`的时候不能出现中文路径。下面就是基本使用

![[00 assets/b3f3b77fc47ca5037eb99a8952503c33_MD5.png]]

3、我们也可以使用`n`工具来切换`nodejs`的版本

![[00 assets/20cbd3374d57cdc6f71c8bbbe3af6b22_MD5.png]]

## 1.7 输入输出

![[00 assets/fd4f9c1a6c4b581582219918a6752b52_MD5.png]]

1、一般情况下我们是不会主动转入参数

![[00 assets/b5b092f41e0f88c3d658a8d90ab11e97_MD5.png]]

2、`argv`的名字由来

![[00 assets/487b9eb26aa0d23c8e7a80b64d0dbac7_MD5.jpeg]]

# 2. fs

## 2.1 基本介绍

假如你使用的`vscode`没有语法提示的话，可以安装下面的插件

```cmd
npm install --save-dev @types/node
```

在`Node.js`中`fs`模块很重要

![[00 assets/249913fbb61e8ee790d37cb8f4ef72fc_MD5.png]]

在 API 中大多数都提供了这三种操作方式

![[00 assets/0783b1c85c632da9e40fdd7bd3d1b92c_MD5.png]]

我们也可以使用下面的代码来查看`Node.js`有那些模块

![[00 assets/67a5e6df0890c30005dbd947b1416fe3_MD5.jpeg]]

## 2.2 读取文件信息

> 1.同步操作

```javascript
const fs = require("fs");

const filepath = "./abc.txt";

const info = fs.statSync(filepath); // 执行的异步操作
console.log("他是同步执行代码");
console.log(info);
```

![[00 assets/616635ee65e9fabf88ff69781da28bd2_MD5.jpeg]]

当然还有`fstatSync`，这个和`statSync`唯一的区别就是它是传入**文件描述符**，这个在下一节可以看到

> 2.异步操作

```javascript
const fs = require("fs");

const filepath = "./abc.txt";

fs.stat(filepath, (err, info) => {
  if (err) return console.log(err);
  console.log(info);
});
console.log("这是异步操作")
```

![[00 assets/547f2fcf55de36c4d265d66f6ee655b6_MD5.png]]

我们获取到文件信息，不仅仅是`字符数`、`时间`......还可以判断是否为`文件夹`或者`文件`

```javascript
const fs = require("fs")
const filePath = "./abc"

fs.stat(filePath,(err,info)=>{
	console.log(info.isDirectory()); // 判断是否为文件夹
   	console.log(info.isFile()); // 判断是否为文件
})
```

> 3.异步操作 - Promise

```javascript
const fs = require("fs");

const filepath = "./abc.txt";

fs.promises.stat(filepath).then(info => {
   console.log(info)
}).catch(err => {
   console.log(err)
})
console.log("这是Promise的异步回调")
```

![[00 assets/35aa31e12d8c06dab8e22faacac7a541_MD5.png]]

## 2.3 文件描述符

![[00 assets/2c26afaebec433c524ba775dad7544d1_MD5.png]]

我们可以使用`fs.open()`中的回调函数来获取该文件的文件描述符。使用这个文件描述符可以操作该文件，而不需要写该文件的路径

```javascript
const fs = require("fs");

const filepath = "./abc.txt";

fs.open(filepath, (err, fd) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(fd);
})
```

![[00 assets/e601fd2a0175737ad0198563327d2e81_MD5.png]]

这里就是使用`fstat`来读取文件信息，这个和`stat`唯一的区别就是传入的第一个参数不同。`stat`传入的是文件路径，但是`fstat`传入的是文件描述符。同理`statSync`和`fstatSync`

```javascript
const fs = require("fs");
const filepath = "./abc.txt";

fs.open(filepath, (err, fd) => {
  if (err) {
    console.log(err);
    return
  }
  // 这里fstat和stat唯一的区别就是
  // stat 传入的是文件路径
  // fstat 传入的是文件描述符
  fs.fstat(fd, (err, info) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(info);
  });
});
```

![[00 assets/542a97864a7050735cf1e83e9648d0a0_MD5.png]]

## 2.4 写入和读取

### 2.4.1 基础使用

![[00 assets/d70289c768dd6678c4cb4754ab0d2702_MD5.png]]

下面就是**读取和写入**文件的 2 个方法`readFile`和`writeFile`

![[00 assets/bd08f2e34d4721cd206acc105d29a784_MD5.jpeg]]

```javascript
const fs = require("fs"); // 使用require来引入fs文件模块

/*
   第1个参数:文件路径，比如:./1.txt...
   第2个参数:编码方式
   第3个参数:回调函数，err表示失败的回调返回的值，dataStr表示读取到的值
*/
fs.readFile("1.txt", "utf-8", (err, dataStr) => {
  /*
      1.如果读取文件成功就是null
      2.如果读取文件失败就是返回失败的原因
   */
  if (err) {
    console.log("文件写入失败:" + err.message);
    return; // 用于结束该回调
  }
  console.log(dataStr);
});

/*
   第1个参数:文件路径，比如:./1.txt...
   第2个参数:写入的值
   第3个参数:编码方式
   第4个参数:回调函数，err表示失败的回调返回的值
*/
fs.writeFile("1.txt", "太阳真好!", "utf-8", function (err) {
  // 和上面是一样的
  if (err) {
    console.log("文件写入失败:" + err.message);
    return;
  }
});
```

并且`writeFile`创建文件，但是不能创建路径；而且是直接将数据覆盖到原本的文件中

### 2.4.2 options

当然`readFile`和`writeFile`的中还有一个参数`options`，可以改变是读写文件的方式

> flag

**flag 查询**：[File system | Node.js v16.17.0 Documentation (nodejs.org)](https://nodejs.org/dist/latest-v16.x/docs/api/fs.html#file-system-flags)

![[00 assets/0506f3c72a2e1c6ee7fd27f168891338_MD5.png]]

> encoding

就是传入的字符串编码形式

> 基本使用

下面就是`options`的基本使用

```javascript
const fs = require("fs");

fs.writeFile("./abc.txt","Hello World!",
  { flag: "a", encoding: "utf-8" }, // 可以指定读写的形式和编码的方式
  (err) => {
    if (err) {
      console.log(err);
      return;
    }
  }
);

fs.readFile("./abc.txt", { encoding: "utf-8" }, (err, dataStr) => {
  if (err) return console.log(err);
  console.log(dataStr);
});
```

![[00 assets/981f3b7d5d851d0cd98e8f5dff81b121_MD5.png]]

## 2.5 文件夹操作

### 2.5.1 创建文件夹

```javascript
const fs = require("fs");

const dirname = "./src";
/*
   exist() 是异步操作，已经被废弃了
   existsSync() 是同步操作，现在使用这个
   这个用于判断是否存在该文件，存在就返回true
*/
// 判断该文件夹是否存在，如果不存在就创建
if (!fs.existsSync(dirname)) {
  // mkdir用于创建该路径下的文件夹
  fs.mkdir(dirname, (err) => {
    console.log(err);
  });
}
```

### 2.5.2 读取文件夹

使用`readdir`可以读取文件夹下面有那些文件。但是只能读取到这一层，`文件夹中文件夹`的内容就读取不到了

```javascript
/*
   readdir() 为异步的方式
   readdirSync 为同步的方式
*/
fs.readdir(dirname, (err, files) => {
  if (err) return console.log(err);
  console.log(files);
});
```

![[00 assets/a01d8f8fd75aec4ade98012cfb5b2a65_MD5.png]]

✨ 这里有一个小坑，下面写的是一个读取文件夹下所有的文件，使用这种方式不行。假如采用硬编码的会导致可维护性很差，所以这就是一个小坑。

![[00 assets/df77024045d8c25ae57769e761e621cd_MD5.jpeg]]

下面就是读取文件夹中所有的文件，这里使用的`fs.stat()`来获取文件状态，判断是否为文件，然后再进行的嵌套递归

```javascript
function getFiles(dirname) {
  // 查询下面的所有文件
  fs.readdir(dirname, (err, files) => {
    // 遍历数组中所有文件
    files.forEach((ele) => {
      let filePath = path.resolve(dirname, ele);
      // 将该文件的信息获取到
      fs.stat(filePath, (err, info) => {
        // 如果是文件夹就遍历循环里面的文件
        if (info.isDirectory()) {
          getFiles(filePath);
        } else {
          console.log(ele);
        }
      });
    });
  });
}
getFiles(dirname);
```

![[00 assets/f4125499ad789fef76460f210a7d9c58_MD5.png]]

就是`readdir`有一个书写就是`{ withFileTypes:true }`。这样获取来的文件是一个对象数组，里面包含了文件的名称和状态

![[00 assets/76330bad08d5cb3a6e8ca6a82c237cb2_MD5.png]]

所以就不需要像上面的那种方式还需要自己来手写获取文件的状态，然后再来判断。其实也简单不了多少

```javascript
const fs = require("fs");
const path = require("path");

// 1. 创建文件夹
const dirname = "./src";

function getFiles(dirname) {
  fs.readdir(dirname, { withFileTypes: true }, (err, files) => {
    files.forEach((ele) => {
      if (ele.isDirectory()) {
        const filePath = path.resolve(dirname, ele.name);
        getFiles(filePath);
      } else {
        console.log(ele.name);
      }
    });
  });
}
getFiles(dirname);
```

![[00 assets/0841437f399656d0925f1de944daaaf9_MD5.png]]

### 2.5.3 文件夹重命名

这里就是使用`fs`的`rename`来进行文件夹的重命名

```javascript
const fs = require("fs");

// ./src(原始) -> ./csr(改后)
fs.rename("./src", "./csr", (err) => {
  console.log(err);
});
```

### 2.5.4 遍历文件

使用这个方式可以遍历指定文件夹下面的所有文件

```javascript
const fs = require("fs")

let files = fs.readdirSync(__dirname);

console.log(files)
```

![[00 assets/52bd296fdb7f7b0e5d5052aebc59b7a5_MD5.jpeg]]

## 2.6 动态路径问题

在`node.js`中，我们直接`node`的话就会进行路径的拼接来执行

![[00 assets/5159d7863d8b9a3f581d7af5c180b4f3_MD5.png]]

假如我们换一个路径来执行这个程序的话就会出现问题，这个时候根路径就出现问题了

![[00 assets/dc04769d87a39feaec63e1d70ef300b8_MD5.png]]

> 解决方法

1.书写`绝对路径`，我不是很推荐这种方式，不仅字符串多，而且不易维护

2.使用`__dirname`来进行处理，`__dirname`表示当前执行的`js`的文件的路径，然后拼接就可以了，这比直接写`绝对路径`好多了

## 2.7 文件拷贝案例

下面就是文件拷贝的案例。这里有一个新的 API 就是复制文件`copyFileSync`，这个是同步代码。假如你把`Sync`去掉的话就是异步代码

```javascript
const fs = require("fs");
const path = require("path");

const srcDir = "D:\\Test\\src";
const destDir = "D:\\Test\\dest";

var i = 0;
while (i < 3) {
  i++;
  const num = "day" + (i + "").padStart(2, 0);
  const srcPath = path.resolve(srcDir, num);
  const destPath = path.resolve(destDir, num);
  // 检测是否有该文件，如果有的话，就不去拷贝
  if (fs.existsSync(destPath)) continue;
  // 该文件夹不存在，先创建文件夹
  fs.mkdir(destPath, (err) => {
    // 读取该文件下的文件，同步方法
    const srcFiles = fs.readdirSync(srcPath);
    srcFiles.forEach((ele) => {
      // 设置要复制的文件
      const srcFile = path.resolve(srcPath, ele);
      // 设置要转移到那个路径
      const destFile = path.resolve(destPath, ele);
      // 复制的函数，同步执行
      // 第一个参数为要被复制的文件
      // 第二个参数为要复制到哪里
      fs.copyFileSync(srcFile, destFile);
      console.log(ele, "复制成功");
    });
  });
}
```

将`src`文件下的内容拷贝到`dest`文件下

![[00 assets/559cf080fa69f5f15220ce67feccfe8f_MD5.png]]

# 3. path

## 3.1 基本介绍

**path 模块**用于对路径和文件进行处理，提供了很多好用的方法。

但是为什么一定要使用`path`来进行拼接路径呢？不仅仅是因为语法规范，更是因为操作系统不一样，所以路径的名字也不一样，所以直接使用`path`的话就可以解决这个问题

![[00 assets/1b7f722ed955073cfa71b51f0c09476c_MD5.png]]

为什么会有`windows`和`Mac Linux`的路径区别呢？就是因为这个**可移植操作系统接口**

![[00 assets/8fd3aa1709e1816b7b79414aa44613ba_MD5.png]]

## 3.2 基本 API

![[00 assets/50f20b512f78b7e7bb0b6f45d6ab859a_MD5.png]]

#### 3.2.1 path.dirname()

`path.dirname`可以获取文件的根路径，但是不包含文件名

![[00 assets/93ea493f124328de383c4be1a0984f57_MD5.png]]

#### 3.2.2 path.basename()

`path.basename()`方法，可以获取路径中的最后一部分，经常通过这个方法获取路径中的文件名

![[00 assets/e7a58caf24e14d539d3e081dd574b807_MD5.jpeg]]

#### 3.2.3 path.extname()

使用`path.extname()`方法，可以获取路径中的扩展名部分

![[00 assets/db5599a11b8764f14b5fe0eb214489f7_MD5.jpeg]]

#### 3.2.4 path.join()

`path.join()`方法可以将多个代码片段连接在一起，拼接成完整得路径字符串。并且你会发现使用这种方式，可以将原本`Linux和Mac`的`/`标识符改变为`\`，用于`windows`

![[00 assets/9a0c3f2cfabd8a141172bc2eb8aa89b5_MD5.png]]

#### 3.2.5 path.resolve()

1、`path.resolve()`和`path.join()`的唯一区别就是：`path.resolve()`可以自动识别路径来判断，是否加上根路径

2、假如你遇到了类似于`/`，这属于是根路径，遇到这种不往上寻找，默认到这里就截至了

3、假如你遇到的是`./`或者`../`的情况，就会去寻找执行这条命令的`.js`文件的根路径，比如说：执行这条命令的`.js`文件路径为`D:\code\Node\index.js`，所以就会将这个文件的路径和你写入的文件进行拼接，直到找到根路径

```javascript
const path = require("path");

path.resolve("/src/Code", "abc.txt") // D:\src\Code\abc.txt
path.resolve("src/Code", "abc.txt") // D:\code\Node\src\Code\abc.txt
path.resolve("./src/Code", "abc.txt") // D:\code\Node\src\Code\abc.txt
path.resolve("../src/Code", "abc.txt") // D:\code\src\Code\abc.txt
path.resolve("../src/Code", "/", "abc.txt") // D:\abc.txt
```

![[00 assets/52d30050a648fc2e80b28857dc9df5bd_MD5.png]]

4、对于`path.resolve()`必定是返回一个绝对路径

![[00 assets/7456db68a1e0bb245b6cb900e883969f_MD5.png]]

5、 在`webpack`中可以一般都是使用`path.resolve()`来解决这些问题

![[00 assets/3b3e5286e280adbcdf049c8804c7287e_MD5.png]]

#### 3.2.6 其他 API

可以查阅 Node.js 文档：[Path | Node.js v16.17.0 Documentation (nodejs.org)](https://nodejs.org/dist/latest-v16.x/docs/api/path.html)

## 3.3 时钟案例

就是讲`html`中的`css`和`js`提取出到相对应的`.css`和`.js`文件，然后使用`link`和`script`引入相应的文件就可以了

```js
const fs = require("fs");
const path = require("path");

const regStyle = /<style>[\s\S]*<\/style>/;
const regScript = /<script>[\s\S]*<\/script>/;

fs.readFile(
  path.join(__dirname, "./src/index.html"),
  "utf-8",
  (err, dataStr) => {
    if (err) return console.log("你读取的有问题!" + err.message);

    resolveCSS(dataStr);
    resolveJS(dataStr);
    resolveHTML(dataStr);
  }
);

// 处理CSS样式
function resolveCSS(dataStr) {
  const r1 = regStyle.exec(dataStr);
  const newCSS = r1[0].replace("<style>", "").replace("</style>", "");

  fs.writeFile(
    path.join(__dirname, "./files/CSS.css"),
    newCSS,
    "utf-8",
    (err) => {
      if (err) return console.log("出现错误:" + err.message);
      console.log("成功写入CSS样式");
    }
  );
}

// 处理JS文件
function resolveJS(dataStr) {
  const r1 = regScript.exec(dataStr);
  const newCSS = r1[0].replace("<script>", "").replace("</script>", "");

  fs.writeFile(
    path.join(__dirname, "./files/JS.js"),
    newCSS,
    "utf-8",
    (err) => {
      if (err) return console.log("出现错误:" + err.message);
      console.log("成功写入JS样式");
    }
  );
}

// 处理HTML文件
function resolveHTML(dataStr) {
  const newHTML = dataStr
    .replace(regStyle, '<link rel="stylesheet" href="../files/CSS.css">')
    .replace(regScript, '<script src="../files/JS.js"></script>');
  fs.writeFile(
    path.join(__dirname, "./src/index.html"),
    newHTML,
    "utf-8",
    (err) => {
      if (err) return console.log("出现错误:" + err.message);
      console.log("成功写入替换HTML");
    }
  );
}
```

# 4. http

## 4.1 基本介绍

该模块主要是为了开发`Web服务器`，对外提供资源

![[00 assets/c2d919b0c62acce1fb5fd0fbe97ba25e_MD5.png]]

## 4.2 基本使用

### 4.2.1 基本使用

下面就是创建一个最简单的服务器的过程

```javascript
// 1. 导入Http模块
const http = require("http");
const Http_Port = 8080;

// 2. 创建web服务器实例
const server = http.createServer((req, res) => {
  res.end("服务器启动了");
});

// 3. 启动服务器
server.listen(Http_Port, () => {
  console.log(`${Http_Port}端口正在监听`);
});
```

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324206.png" alt="image-20220902233220067" style="zoom:67%;" />

### 4.2.2 创建多个服务器

当然我们不止可以开启一个服务器，我们也可以开启多个服务器。我们创建多个`http`的实例就可以实现创建多个服务器

```javascript
const http = require("http");

// 创建服务器1
const server1 = http.createServer((req, res) => {
  res.end("服务器1启动了");
});
server1.listen(8000, () => {
  console.log("端口正在监听");
});

// 创建服务器2
const server2 = http.createServer((req, res) => {
  res.end("服务器2启动了");
});
server2.listen(8001, () => {
  console.log("端口正在监听");
});
```

### 4.2.3 多种创建方式

当然创建服务器不止这一个方式，使用`http.createServer`和`http.Server`的 2 种方式本质其实是一样的

```javascript
const http = require("http");
const Http_Port = 8080;

// 方式一
const server = http.createServer((req, res) => {
  res.end("服务器启动了");
});
// 方式二
const server = new http.Server((req, res) => {
  res.end("服务器启动了");
});

server.listen(Http_Port, () => {
  console.log(`${Http_Port}端口正在监听`);
});

```

查看`Node.js`的源码可以发现，其实本质是一样的`createServer`就是`new Server()`

![[00 assets/6ec93ebf1c1af02c5cdd4e7429cea6ea_MD5.png]]

### 4.2.4 listen()

![[00 assets/083b0f7658e1b50fb86d95f9fcd0b2d9_MD5.png]]

当然`listen()`也包含 3 个参数

> 参数一

![[00 assets/2d77acfb01b4171632879a6b93d2d1db_MD5.png]]

```javascript
// 假如你不写端口号的话，就默认分配端口号
server.listen(() => {
  // 使用该方式可以查看当前服务器的端口号
  console.log(server.address().port);
});
```

![[00 assets/714fdc0d5a80ec869be205ce15dc36b4_MD5.png]]

> 参数二

![[00 assets/f2e10b9186ff042db941aefc235fcaf7_MD5.png]]

假如你的`主机host`设置为其他`ip`的话，就会导致其他 ip 访问不到。

![[00 assets/f1cd86897befcc0721182fbd7e76028c_MD5.png]]

假如你设置为`0.0.0.0`的话就不会有这些问题，默认`IPV4`都是可以访问的

![[00 assets/5dffe630cfac28e530794e384a45fd44_MD5.png]]

> 参数三

![[00 assets/2085e35fb12fd15266999bbc5f09f990_MD5.png]]

## 4.2 req 和 res

### 4.2.1 req

#### 4.2.1.1 基本使用

![[00 assets/61b3f8e9dc33831817169118f20bb188_MD5.png]]

在`req`中也包含了很多的数据，可以使用`req`来查看

![[00 assets/35b9c3459a586f334bb53a7eacc1b92f_MD5.png]]

#### 4.2.1.2 解析 url

但是这里就有一个问题，假如传来的 url 是带`query`参数的，`req`获取到的`url`就是带参的，不方便判断

![[00 assets/fbfca2ab7c61864bccdd3468a559d60c_MD5.png]]

所以这个时候就需要使用`url模块`

![[00 assets/657e203b8e459c8cfe274be4f6c328dd_MD5.jpeg]]

#### 4.2.1.3 解析 query

假如我们需要解析`query参数`，我们可以导入`queryString`参数，并且解析出来为对象

![[00 assets/cfb1540f813297d6666a01ab2a21de90_MD5.png]]

当然我们使用`queryString`模块的`parse()`来解析的时候可以传入第二个参数来做分隔，比如`qs.parse(url,"&")`这样就已`&`为基础来分隔整条`url`，而且`qs.parse()`的第二个参数默认就是`&`，第三个参数默认就是`=`，这样我们就可以分割`query`参数，比如`/login?name=zjh&age=18&weight=1.88`，最后分割出来就是`{name:zjh,age:18,weight:1.88}`

#### 4.2.1.4 解析 JSON

其实 POST 传输来的数据本质就是使用的`Stream`来传输的，所以我们这里使用`on`事件来监听处理`data`

```javascript
const http = require("http");
const url = require("url");
const Http_Port = 8080;

const server = http.createServer((req, res) => {
  const { pathname } = url.parse(req.url);
  if (pathname === "/login") {
    if (req.method === "POST") {
      // 这里统一将请求统一转换为utf-8
      req.setEncoding("utf-8");
      // 监听req,只要有数据就通过Stream获取丢进Buffer中
      req.on("data", (data) => {
        // 传输来的是JSON格式的对象，下面转化为JS对象
        const { name, age } = JSON.parse(data);
        console.log(name, age);
      });
      res.end("Hello,Node,js!");
    }
  }
});

server.listen(Http_Port, "0.0.0.0", () => {
  console.log(`${Http_Port}端口正在监听`);
});
```

![[00 assets/60e9cd4306f878af94234caff4729fca_MD5.png]]

#### 4.2.1.5 请求 header

![[00 assets/ca0ce2de3bd0e42adf7535159d087b15_MD5.png]]

> 1

![[00 assets/a8d6ea4d2bcf8093cbca4afe21d4c311_MD5.png]]

这个在`http`请求的测试软件中一般都会自动切换

> 2.

![[00 assets/de0f864a1fe6c461a62b449217124ffb_MD5.png]]

1.在最后项目打包的时候`webpack`会对项目进行打包，但是这种打包还是不够。我们可以将`js`文件打包为`.gz`文件，只要`header`中包含`accept-encoding`的`gzip`，这样我们就可以发送`.gz`文件给浏览器进行解压，这样减少了传输的数据量

2.accept 可以设置客户端接收的数据，比如:`image/jpg;image/jpeg;image/*`

### 4.2.2 res

#### 4.2.2.1 基本使用

假如我们追踪`createServer`回调函数中的`res`就会发现，其实`res`的本质就是`Stream.Writeable`

![[00 assets/83b76402f9adec25112c89179b10314e_MD5.png]]

我们使用`res`就可以给客户端来响应数据。其中`write`表示响应数据，但是不会关闭流，还可以继续响应。`end`表示响应最后一次，执行完毕就会关闭流

```javascript
const http = require("http");
const Http_Port = 8080;

const server = http.createServer((req, res) => {
  res.write("响应数据writer");
  res.end("响应数据结束");
});

server.listen(Http_Port, "0.0.0.0", () => {
  console.log(`${Http_Port}端口正在监听`);
});
```

#### 4.2.2.2 解决乱码问题

当然我们也可以设置`Content-Type`的值来解决中文乱码的问题

```javascript
// 1. 导入http模块
const http = require("http");

// 2. 创建web服务器实例
const server = http.createServer();

// 3. 为服务器实例绑定request时间，监听客户端的请求
server.on("request", function (req, res) {
  // req 是请求对象，可以获取到请求方的信息
  // 3.1 req.url 获取地址
  // 3.2 req.method 获取请求方法
  console.log(req.url + " , " + req.method);

  // 设置Content-Type的值为"text/html;charset=utf-8"来解决中文乱码
  res.setHeader("Content-Type", "text/html;charset=utf-8");
  // res 是响应对象，可以向客户端发送指定内容，并结束这次请求
  res.end("哈哈哈哈，这就是Node.js");
});

// 4. 启动服务器
server.listen(8080, function () {
  console.log("正在运行");
});
```

![[00 assets/da953f6f8c86db3182b21b2a0f95f598_MD5.png]]

#### 4.2.2.3 设置状态码

我们可以使用下面的 2 种方式来设置状态码

```javascript
const http = require("http");
const Http_Port = 8080;

const server = http.createServer((req, res) => {
  // 方式一：直接给属性赋值
  res.statusCode = 400;
  // 方式二：和Head一起设置
  res.writeHead(401);
  res.end("Hello,Node.js")
});

server.listen(Http_Port, "0.0.0.0", () => {
  console.log(`${Http_Port}端口正在监听`);
});
```

![[00 assets/ce7aaa242d12e5be1677433d17af2746_MD5.png]]

#### 4.2.2.4 响应 header

下面就是 2 种设置`header`的方式

```javascript
const http = require("http");
const Http_Port = 8080;

const server = http.createServer((req, res) => {
  // 方式一

  // 方式二
  res.writeHead(200, {
    "Content-Type": "text/plain;charset=utf8",
  });
  res.end("Hello,Node.js");
});

server.listen(Http_Port, "0.0.0.0", () => {
  console.log(`${Http_Port}端口正在监听`);
});
```

这里的`Content-type`有很多的属性，假如你设置的值为`application/html`的话，浏览器就会默认让我们下载这个 html。假如设置的是`text/html`的话，浏览器就会解析为`html`标签

## 4.3 http 请求

我们进入到`http.get()`就可以知道，回调函数中传入的参数的类型是`IncomingMessage`

![[00 assets/0dace8fcac5f8e53cb91cfaf6df425bc_MD5.png]]

不是以前的以前`http.createServer()`中的`res`

![[00 assets/ed3471a2a0f42c548f4e0e4fc46abc1b_MD5.png]]

下面是使用`Node.js`给我的另外一个服务器发送请求

这里使用的是`http.get()`方法发送`get`请求，并且使用事件监听`data`的方式来获取数据，最后的`end`用来关闭这次请求。并且传输的数据放入了`Buffer`中

```javascript
const http = require("http");

http.get("http://127.0.0.1:8080", (res) => {
  res.on("data", (data) => {
    console.log(data, data.toString());
  });
  res.on("end", () => {
    console.log("所有数据请求完毕！");
  });
});
```

![[00 assets/de90e59e59bf0063199939d26d6f442f_MD5.png]]

下面是使用`http.request`的方式来发送`POST`，当然使用这种方式也可以发送多种请求，只 i 需要将`method`改为其他的请求的名字即可。

```javascript
const http = require("http");

const req = http.request(
  {
    method: "POST",
    hostname: "127.0.0.1",
    port: 8080,
  },
  (res) => {
    res.on("data", (data) => {
      console.log(data, data.toString());
    });
    res.on("end", () => {
      console.log("所有数据请求完毕！");
    });
  }
);
req.end();
```

下面的发送`POST`请求的方式有一个小细节，假如你不去手动关闭`req.end()`的话，就会导致传输数据的阻塞，只有你手动关闭才能正常接收

![[00 assets/61b3f8e9dc33831817169118f20bb188_MD5.png]]

当你设置了`req.end()`的话就会正常接收数据

![[00 assets/7cff8372dbe1ce49761b7fd09e94498b_MD5.png]]

一般的开发中都会使用`axios`来发送网络请求，使用原生的方式比较少

## 4.5 文件上传

下面是错误的示例，不能使用这种方式来处理文件上传。这里的整个思路是没问题的，客户端分批发送字节流数据，服务端使用流来接收。但是发送的数据包含`请求头数据，以及其他的数据`一起夹杂在流中，所以就会导致文件打不开

![[00 assets/c7543a9395baf3be8a1510bd7f48d520_MD5.png]]

下面使用原生的方式来处理文件上传，在项目中大部分都会使用框架

![[00 assets/7fed0450b3b89fffc49a5a5c08a40add_MD5.png]]

1.下面就是传输来的数据，可以发现头部的信息基本就是`header`信息，在`PNG`的后面就是真正需要存入的数据。

2.`image/png`后面的`\r\n\r\n`表示的是 2 个空格。

3.`--------------2157167123124131370\r\n`表示的是`boundary`，表示的是上一段数据和下一段数据的分隔符

![[00 assets/a9a9f3a75ac85eec6b46c86462c36f66_MD5.png]]

下面就是原生写`文件上传`的代码，主要还是字符串的删减

```javascript
const http = require("http");
const fs = require("fs");
const qs = require("querystring");
const Http_Port = 8080;

const server = http.createServer((req, res) => {
  // 图片文件设置为二进制
  req.setEncoding("binary");

  let body = "";
  const fileSize = req.headers["content-length"];
  let curSize = 0;
  // 获取boundary，用于后续去除boundary
  const boundary = req.headers["content-type"]
    .split(";")[1]
    .replace(" boundary=", "");

  req.on("data", (data) => {
    body += data;

    // 获取当前文件上传的进度
    curSize += data.length;
    console.log(`文件上传的进度:${(curSize / fileSize) * 100}%\n`);
  });
  req.on("end", () => {
    // 处理body前面的header
    const payload = qs.parse(body, "\r\n", ": ");
    const type = payload["Content-Type"];

    // 获取type的位置
    const typeIndex = body.indexOf(type);
    const typeLength = type.length;
    let imageData = body.substring(typeIndex + typeLength);

    // 去掉中间的2个空格
    imageData = imageData.replace(/^\s\s*/, "");

    // 去除掉最后的boundary
    imageData = imageData.substring(0, imageData.indexOf(`--${boundary}--`));

    // 传入的文件必须是二进制
    fs.writeFile("./1.png", imageData, { encoding: "binary" }, (err) => {
      return console.log(err);
    });
  });
});

server.listen(Http_Port, "0.0.0.0", () => {
  console.log(`${Http_Port}端口正在监听`);
});
```

## 4.6 时钟案例

这个其实时钟案例，我们不是将`HTML`中的`CSS`和`JS`拆分出来了吗？现在我们就需要请求`HTML`来实现效果

![[00 assets/58130eae77ed98e6a615a031e6ee208c_MD5.png]]

下面就是代码

```javascript
const fs = require("fs");
const http = require("http");
const path = require("path");
const server = http.createServer();

server.on("request", function (req, res) {
  const url = req.url;
  let fpath = "";

  if (url === "/") {
    fpath = path.join(__dirname, "./src/index.html");
  } else if (url === "/index.html") {
    fpath = path.join(__dirname, "./src", url);
  } else {
    fpath = path.join(__dirname, url);
  }

  fs.readFile(fpath, "utf-8", function (err, dataStr) {
    if (err) return res.end("<h1>404 Not Found!</h1>");
    res.end(dataStr);
  });
});

server.listen(8080, function () {
  console.log("正在运行");
});
```

这里其实是需要注意的一个点，因为你请求了`HTML`的话，那么这个`HTML`也会去请求里面的`CSS`和`JS`，假如你加上第三句的话是请求不到，因为请求`CSS`和`JS`都需要走这个回调方法，如果没有匹配到`url`的话就不会请求到，所以需要加上第三句来保底

![[00 assets/4c47addff0b6faff70693eb6f4100b03_MD5.png]]

# 5. event

## 5.1 基本介绍

![[00 assets/32610f65e0a067830ba253af96d12371_MD5.png]]

## 5.2 基本使用

首先`EventEmitter`属于应该类，可以创建事件发射器`emitter`。并且使用`on`或者`emiy`来监听和发出一个事件

```javascript
// 1.引入
const EventEmitter = require("events");

// 2.创建发射器，类似Vue的全局事件总线
const emitter = new EventEmitter();

// 3.监听一个事件
emitter.on("click", (args) => {
  console.log("监听1到事件", args);
});

// 4.发出一个事件
emitter.emit("click", ["1", "2", "3", "4"]);


// 5.解绑事件
const listener = (args) => {
  console.log("监听2到事件", args);
};
emitter.on("click", listener);
emitter.off("click", listener);
```

## 5.3 获取信息

```javascript
// 1.引入
const EventEmitter = require("events");

// 2.创建发射器，类似Vue的全局事件总线
const emitter = new EventEmitter();

// 3.监听一个事件
emitter.on("click", (args) => {
  console.log("监听1到事件", args);
});

emitter.on("tap", (args) => {
  console.log("监听2到事件", args);
});

// 获取信息
console.log(emitter.eventNames()); // 1. 获取注册的事件
console.log(emitter.listenerCount("click")); // 2. 获取该事件的个数
console.log(emitter.listeners("click")); // 3. 获取该事件的监听
```

![[00 assets/ab279de914f85f396ce037210905b9a8_MD5.png]]

## 5.4 其他 API

```javascript
const EventEmitter = require("events");
const emitter = new EventEmitter();

// 1.once 表示只监听一次
emitter.once("click", (args) => {
  console.log("监听1到事件", args);
});

// 2.将本次监听放置在前面
emitter.prependListener("click", (args) => {
  console.log("监听2到事件", args);
});

// 3.将本次监听放置在前面，并且执行一次
emitter.prependOnceListener("click", (args) => {
  console.log("监听2到事件", args);
});

emitter.emit("click", "Hello!");

// 4.移除所有的监听
emitter.removeAllListeners();

// 5.移除click监听
emitter.removeListener("click");
```

# 8 util

## 8.1 promisify

1、该方法可以将基于回调的函数转换为基于`Promise`的函数

![[00 assets/f889002040b1a44fb64f5187f60c8135_MD5.png]]

![[00 assets/bd2f8ce8c5e355b9c3f3c9df9492d6a6_MD5.png]]

## 8.2 is......

1、内部存在很多的`is`实现的方法，直接使用判断类型即可，但是要注意很多的`is...`在不同的版本被废弃了，使用的时候注意甄别

![[00 assets/73da52f331dd1a48461e957c733cc5b6_MD5.png]]

2、取而代之的是很多不常用的类型的判断

![[00 assets/c5ccbc637ebb81ad2ed12233b5a10cae_MD5.png]]

## 8.3 callbackify

1、使用`callbackify`可以将采用 `async` 函数（或返回 `Promise` 的函数）转化为回调的形式

2、这个和`promisify`基本相反，这个是转为回调函数，但是他不仅仅可以转化`promise函数`，还可以转化普通函数

![[00 assets/348e34be23395ed39cd6fddef0fe1edc_MD5.png]]

# 6. 模块化

具体可以参考这里的介绍：[[模块化]]

# 7. 包管理工具



# 9. buffer

## 9.1 基本介绍

### 9.1.1 基本介绍

我们通常情况下，是浏览器来处理图片和文件。并且一个图片其中的一个像素点的`rgb`值就是`0~255`，其中当`rgb`值为 0 时，二进制值就是`0000 0000`；当`rgb`值为 255 时，二进制就是`1111 1111`。就是这样一组的二进制值可以来展示一个图片

![[00 assets/0447ff8fbb5e11cb1a7baae1daf1564d_MD5.png]]

但是`Node.js`是服务器语言，不能依赖浏览器。所以`Node.js`就需要执行二进制流

![[00 assets/e90003935a1ef51560ccd2eeec1d2221_MD5.png]]

### 9.1.2 字符串

![[00 assets/12acf413dc3ad64d15d7e1b7ebfb72b0_MD5.png]]

下面就是使用`Buffer`来存储的基本过程，因为`1111 -> f`，所以使用八位最大的 16 进制就是`ff`

但是下面的这种方式已经过时了，不推荐使用这种方式

![[00 assets/d14207270462f59f4ceeeb003fd39f95_MD5.png]]

现在可以使用`Buffer.from()`来转换

![[00 assets/faa634a180ac55c42fd576e4b036cf08_MD5.png]]

大致的存储过程，将字符串`why`转换为`0000 0000`的八位二进制，然后转换为十六进制进行存储

![[00 assets/fbff289ec0bccc7d70738706c2d02a9b_MD5.png]]

### 9.1.3 中文编码

下面就是使用`utf8`和`utf16le`的编码差别，`utf8`对中文默认是 3 组 6 字节，而`utf16le`对中文默认是 2 组 4 字节

![[00 assets/09493fc795ef3f892a1d7463972664fb_MD5.png]]

假如我们来解码的话，默认也是使用`utf8`来解码的。假如你是使用`utf16le`来编码，却是`utf8`来解码的，就会出现乱码

![[00 assets/7741840304d0e4ccb2005ca80dd39742_MD5.png]]

## 9.2 创建方式

![[00 assets/05130d1b83256ccd9a476a6584f2ab1a_MD5.png]]

Buffer 的官方文档：[Buffer | Node.js v18.8.0 Documentation (nodejs.org)](https://nodejs.org/dist/latest-v18.x/docs/api/buffer.html)

### 9.2.1 Buffer.alloc

`Buffer.alloc()`里面可以传入一个值，就是要开辟的字节长度。假如是**1kb**的话就是**1024byte**，在`Buffer.alloc`里面写入的参数就是**1024**

![[00 assets/64c24e1812a68c634cf34f2ddcf574a0_MD5.png]]

## 9.3 文件读取

### 9.3.1 基本使用

下面的`readFile`的本质就是使用`Buffer`来读取进制流。

![[00 assets/c28e0e0315163ea21634189e2530315e_MD5.png]]

我们使用`readFile`也可以读取其他文件

![[00 assets/e9c9534d38490cc6bbb67ccc98800d09_MD5.png]]

下面就是使用`readFile`来读取其他文件，并且将读取到的进制流写入到另外一个文件中

![[00 assets/537fe96d18b59de39b445e47c4f4deb1_MD5.png]]

### 9.3.2 Sharp 使用

`Sharp`官方文档：[lovell/sharp: High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library. (github.com)](https://github.com/lovell/sharp)

我们要使用首先要安装

```bash
npm i Sharp
```

下面就是`Sharp`的基本使用，具体的其他使用可以参考`Sharp`文档

```javascript
const fs = require("fs");
const sharp = require("sharp");


sharp("./Login.png")
  .resize(1000, 1000) // 长宽转换为1000,1000
  .toFile("./Login1.png");


sharp("./Login.png")
  .resize(300, 300) // 长宽转换为1000,1000
  .toBuffer() // 转换为Buffer流
  .then((data) => {
    // 赋值到Login2.png
    fs.writeFile("./Login2.png", data, (err) => {
      console.log(err);
    });
  });
```

# 10. 事件循环

^80c5ef

## 10.1 基本介绍

### 10.1.1 基本介绍

![[00 assets/8a98a3878f1d54c73099bf81d6dac1f4_MD5.jpeg]]

### 10.1.2 进程和线程

![[00 assets/6f540cc7fc6b1e84ddfd431d59b9e2bc_MD5.png]]

### 10.1.3 多进程多线程开发

![[00 assets/7a70de12824c8e4f6045c40df3b56e17_MD5.png]]

### 10.1.4 JavaScript 和进程

![[00 assets/54a5d53dec522bde4738607ba1b6443e_MD5.png]]

## 10.2 JS 执行过程

### 10.2.1 非异步执行

![[00 assets/b96e4ee349487a90e8755bdd21f8a662_MD5.jpeg]]

### 10.2.2 异步执行

![[00 assets/03f6def22d24b72b849725722ee68db9_MD5.png]]

## 10.3 浏览器事件循环

下面执行的就是下面的这段函数

```javascript
const name = "coderwhy";

console.log(name);

function sum(numi, num2) {
  return numl + num2;
}

function bar() {
  return sum(20, 30);
}
const result = bar();

setTimeout(() => {
  console.log("timerFunction");
}, 1000);

console.log(result);
```

前面的`sum`和`bar`执行完毕之后。就轮到了最后的`setTimeOut`定时器，这个时候会将该`timer`函数保存在某一个位置，不阻塞后面的代码。当定时器时间到了之后，就会将`timer`函数放置再事件队列中，通过事件循环将`timer`函数丢到函数调用栈中被执行。注意，这个是浏览器中的事件循环
![[00 assets/7c69d66d409b271a34da843de0fe8a04_MD5.png]]

## 10.4 宏任务和微任务

![[00 assets/5bc101dc23948f55a308184b4bc62626_MD5.png]]

但是既然有 2 个队列，那么事件循环是如何处理这 2 个队列。通过下面的代码就可以知道

首先是优先执行`微任务`，当`微任务队列`都被事件循环压入函数调用栈之后，就会去执行`宏任务队列`。当处理了一个宏任务队列，就会去检查`微任务队列`是否其他任务。假如有的话就去处理`微任务队列`，假如没有的话就继续执行下一个`宏任务队列`中的函数。每次执行一个`宏任务队列`中的函数，就会去检查`微任务队列`

![[00 assets/a0d215b0dbdf59164d46d6704e6bab92_MD5.png]]

这个就很好的简述了上图代码的执行情况

![[00 assets/6693cf7283aa529b46c5204810907541_MD5.png]]

> 面试题

注意下面的运行结果是在浏览器的环境下，看下最后的执行结果是什么样的

```javascript
setTimeout(function () {
  console.log("set1");

  new Promise(function (resolve) {
    resolve();
  }).then(function () {
    new Promise(function (resolve) {
      resolve();
    }).then(function () {
      console.log("then4");
    });

    console.log("then2");
  });
});

new Promise(function (resolve) {
  console.log("pr1");
  resolve();
}).then(function () {
  console.log("then1");
});

setTimeout(function () {
  console.log("set2");
});

console.log(2);

queueMicrotask(() => {
  console.log("queueMicrotaskl");
});

new Promise(function (resolve) {
  resolve();
}).then(function () {
  console.log("then3");
});
```

![[00 assets/d7e09e81e369e9e6d21488530502cd9e_MD5.png]]

这里其实有一个我以前理解不是很深的一个点，就是`new Promise()`中的回调函数，他其实不属于上面的事件循环的流程，而是直接在`script`中执行。而`then()`才是丢到微任务队列中执行。这就意味着`new Promise()`中先去执行，然后才会去执行`微任务`中的函数

![[00 assets/44832039e41292c8b001cf9ab676a904_MD5.png]]

这里有一个小知识，`async`和`await`可以看作是`Promise`的语法糖

1.我们可以将`await`关键字后面执行的代码，看做是包裹在`(res,rej) => { 函数执行 }`中的代码

2.`await`的下一条语句，可以看做是`then ( res => { 函数执行 } )`中的代码；

![[00 assets/94e014decc4c5580eb3f0dea596efd3c_MD5.png]]

看下下面执行的情况

```javascript
async function async1() {
  console.log("asyncl start");
  await async2();
  console.log("async1 end");
}

async function async2() {
  console.log("async2");
}

console.log("script start");

setTimeout(function () {
  console.log("setTimeout");
}, 0);

async1();

new Promise(function (resolve) {
  console.log("promisel");
  resolve();
}).then(function () {
  console.log("promise2");
  console.log("script end");
});
```

![[00 assets/856d0f27d4358ccc1130ba3df69101d8_MD5.png]]

## 10.5 Node 架构

![[00 assets/dd213e62b3ea276a4c857667b417ac88_MD5.png]]

我们在`Application`中写了一个`fs.readFile`，`js`本身不会去读取文件，首先是`V8`引擎来翻译，丢到`NodeAPI`中去读取文件，`NodeAPI`又会去调用`Libuv`来读取文件。最后其实就是`Libuv`来读取的文件。

## 10.6 阻塞 IO 和非阻塞 IO

> 基本介绍

![[00 assets/4004979c185de71d09ff85a28008f3a0_MD5.png]]

其实对于文件的操作就是使用`Libuv`来实现的，然后来调用`操作系统`设置好的文件操作

![[00 assets/2fea8cfcb1f3572026f83e37a0f3765c_MD5.png]]

当然操作系统也分为 2 种调用方式

![[00 assets/694bc29c2711635b8d226bcba4340107_MD5.png]]

> 非阻塞 IO 的缺点

![[00 assets/686945bb15701cee4eed510b9e083f7e_MD5.png]]

当然也是有解决的方法，这个在`Java`中有提到

![[00 assets/6b0ceec87d40ec4a3ef56e489ce9a523_MD5.png]]

在线程池只有很多正在等待的线程，比如`fs.readfile()`在`Application`端被书写，经过`V8`转义，`NodeAPI`的调用`Libuv`，这个时候就会调用线程池来读取文件。当读取完成之后，`libuv`就会将`fs.readFile()`中的回调函数压入`事件队列`中，通过`事件循环`将队列中的函数给`函数调用栈`，然后返回给`application`端被读取

> 阻塞和非阻塞，同步和异步的区别

![[00 assets/1d4d3953aed93ce55c67b83819728817_MD5.jpeg]]

线程不安全是因为多个线程同时读取一个文件，可能一个线程在修改该文件，这就导致了文件读取的错误。但是其实这样`Node.js`就不会存在线程不安全的问题，多个线程读取完成之后，就会将注册的函数和取来的值一起放入事件队列中，通过事件循环来读取压入单线程的函数调用栈，一个个执行。

## 10.7 Node 事件循环

![[00 assets/a34aeae0de7bf7312fbcbabe9a6aee96_MD5.png]]

官方文档：[Node.js 事件循环，定时器和 process.nextTick() | Node.js (nodejs.org)](https://nodejs.org/zh-cn/docs/guides/event-loop-timers-and-nexttick/)

![[00 assets/53eeb2ab32cb53b4975fcd0eae41717a_MD5.png]]

## 10.8 Node 宏任务和微任务

![[00 assets/9212d21a8db8491f5eb9927e4eb7f184_MD5.png]]

这个`Node.js`执行顺序又和`浏览器`不一样，首先是`tick`队列，然后是`Promise().then()`回调，然后就是`setTimeout`...按照上面的图依次向下执行

可以看下下面的执行结果，其实做这种面试题不是很难，有一个特定的规律，我们可以先按照`main`函数，`微任务`，`宏任务`的顺序来执行

```javascript
async function asyncl() {
  console.log("async1 start");
  await async2();
  console.log("asyncl end");
}

async function async2() {
  console.log("async2");
}

console.log("script start");

setTimeout(function () {
  console.log("setTimeouto");
}, 0);

setTimeout(function () {
  console.log("setTimeout2");
}, 300);

setImmediate(() => console.log("setImmediate"));

process.nextTick(() => console.log("nextTickl"));

async1();

process.nextTick(() => console.log("nextTick2"));

new Promise(function (resolve) {
  console.log("promisel");
  resolve();
  console.log("promise2");
}).then(function () {
  console.log("promise3");
});
console.log("script end");
```

![[00 assets/b63eb9840c8a59baa24df35f7ec2e8b3_MD5.png]]

可以看下下面是为什么？

![[00 assets/e45ca98c0f48905078b822572960ff75_MD5.png]]

结果并不是想的那样

![[00 assets/b4becc776abde048a9688b6d7dc162e1_MD5.png]]

因为`setImmediate`属于`check`阶段，而`setTimeout`属于`timer`阶段。注意`poll`阶段会进行阻塞。

![[00 assets/f86854b835f33851f7beed9829c3c9ce_MD5.png]]

而且在执行循序中`check`阶段是在`Timer`阶段后面，所以可以得出`setTimeOut`比`setImmediate`先执行吗？不对

![[00 assets/9931a41cc0290866541b1b89d564e4b0_MD5.jpeg]]

`main`函数首先执行`setTimeout`函数，然后会将`setTimeout`中的回调函数给一个树形结构，当时间过去之后`时间循环`就会读取该树形结构的的回调函数，然后函数调用栈来执行。

这里就会出现一个问题，将`setTimeOut`存入树形结构，然后再将该回调函数取出会有时间的损耗，假如存入就花费了`20ms`，但是事件循环初始化花费了`10ms`，这个时候就会优先来执行`setImmediate`。假如存入只花费了`5ms`的话，那就就会优先来执行`setTimeOut`，这就导致了执行顺序的问题

![[00 assets/cea74c4672240161408b2afc02aca676_MD5.png]]

# 11. stream

## 11.1 基本介绍

> 基本介绍

![[00 assets/792b1fb87b19845c80699451d6981c86_MD5.png]]

> 读写文件的流

![[00 assets/3503906604e0581809f62161e2649eea_MD5.png]]

下面就是为所有流都是`EventEmitter`的实例，因为在源码部分基本就是通过`Stream`来实现的

![[00 assets/c34c634590f5fc1c7539f437ece75d87_MD5.jpeg]]

## 11.2 Readable

### 11.2.1 基本介绍

![[00 assets/d03cec5fa3550ff972f5e06411cbb19e_MD5.png]]

这个时候我们就可以使用`Readable`来实现

![[00 assets/097d5f2bbaddba62706348cddb23f29e_MD5.png]]

假如想了解`Buffer`和`Stream`的话可以查看这个帖子：[理解 Node 中的 Buffer 与 stream - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/368045575)

### 11.2.2 基本使用

```javascript
const fs = require("fs");

const read = fs.createReadStream("./1.txt", {
  start: 1, // 读取开始位置，默认为0，单位是字节
  end: 8, // 读取结束位置，默认为Infinity，单位是字节
  highWaterMark: 4, // 读取的大小 默认是64 * 1024 单位是字节
});
// 其实这里就可以看出Stream继承了Event
// 当打开文件
read.on("open", (fd) => {
  console.log("文件被打开了");
});
// 当读取到文件
read.on("data", (data) => {
  console.log(data, data.toString());
  // 读取停止
  read.pause();
  // 文件读取恢复
  setTimeout(() => {
    read.resume();
  }, 100);
});
// 当文件读取结束
read.on("end", () => {
  console.log("文件读取结束");
});
// 当文件被关闭
read.on("close", () => {
  console.log("文件被关闭");
});
```

![[00 assets/38283311e4ac5d73d4a903ee34de9946_MD5.png]]

## 11.3 Writeable

### 11.3.1 基本介绍

![[00 assets/641c6e7d9ba3f1e95c05c00c72850430_MD5.jpeg]]

### 11.3.2 基本使用

```javascript
const fs = require("fs");

const writer = fs.createWriteStream("./1.txt", {
  flags: "a",
  start: 100,
});

writer.write("不好啊！", (err) => {
  if (err) return console.log(err);
  console.log("写入成功");
});

// 你关闭之后
writer.close(); // 方式一
writer.on("close", () => { // 方式二
  console.log("文件被关闭");
});
```

但是这里使用`Windows`电脑就会出现一个问题，将`flags`改成`a`不能正常的执行`start`，我们改成`r+`就可以使用

![[00 assets/6be0433ec3fd9d48b9cfeb1d17eae989_MD5.png]]

## 11.4 pipe 方法

![[00 assets/35449f792de7d64837dc79256ed8f1a4_MD5.png]]

# 12. os

## 12.1 基本使用

> 输出系统版本信息

![[00 assets/72c654ec0c37e196dd5db462ffb2911b_MD5.jpeg]]

> 输出用户目录

1、返回用户目录，原理就是在`windows`执行 `echo %USERPROFILE%`，在`posix`中执行`$HOME`

![[00 assets/80d0473e67706b583b8d2e1bd7837dd6_MD5.png]]

> 输出 CPU 信息

1、使用`os.cpus()`表示输入线程信息

```bash
[
  {
    model: 'Intel(R) Core(TM) i7 CPU         860  @ 2.80GHz',	// CPU的型号信息
    speed: 2926,			// CPU的时钟速度，其中2926MHz表示2.926GHz
    times: {
      user: 252020,			// CPU被用户程序使用的时间
      nice: 0,				// CPU被优先级较低的用户程序使用的时间
      sys: 30340,			// CPU被系统内核使用的时间
      idle: 1070356870,		// CPU处于空闲状态的时间
      irq: 0,				// CPU被硬件中断处理程序使用的时间
    },
  },
  {
    model: 'Intel(R) Core(TM) i7 CPU         860  @ 2.80GHz',
    speed: 2926,
    times: {
      user: 306960,
      nice: 0,
      sys: 26980,
      idle: 1071569080,
      irq: 0,
    },
  },
  ......
]
```

![[00 assets/28511c21aed600de82172e268cbcf4f0_MD5.png]]

> 输出网络信息

![[00 assets/cde8f737467af4946616c4954096552b_MD5.jpeg]]

## 12.2 案例

> 打开浏览器

1、在`webpack`和`vite`中编译之后自动打开浏览器，下面就是实现的原理

2、`exec`可以执行`命令`，本质就是在控制台中输入执行

![[00 assets/1adcf930623a745e3726c6210f7910b4_MD5.jpeg]]

# 13. process

## 13.1 基本使用

> 输出信息

1、`process.cwd()`表示获取当前执行进程路径，他主要用于`esm`环境中

2、`process.argv`可以获取执行当前线程中的参数，主要用于一些开发包工具中

![[00 assets/d1cc493d918e424370c70807e7c2e47c_MD5.png]]

3、`process.memoryUsage()`获取系统内存使用量，这个主要是做性能优化的

![[00 assets/e3b61531363705f6bc29278ba329c698_MD5.png]]

```bash
{
    rss: 30932992, // 常驻集大小 这是进程当前占用的物理内存量，不包括共享内存和页面缓存。它反映了进程实际占用的物理内存大小
    heapTotal: 6438912, //堆区总大小 这是 V8 引擎为 JavaScript 对象分配的内存量。它包括了已用和未用的堆内存
    heapUsed: 5678624,  //已用堆大小
    external: 423221, //外部内存使用量 这部分内存不是由 Node.js 进程直接分配的，而是由其他 C/C++ 对象或系统分配的
    arrayBuffers: 17606 //是用于处理二进制数据的对象类型，它使用了 JavaScript 中的 ArrayBuffer 接口。这个属性显示了当前进程中 ArrayBuffers 的数量
}
```

4、下面为主要使用方式

![[00 assets/49d3e5322839605a5d2acf995656b57d_MD5.png]]

5、`process.env`表示获取当前系统的所有环境变量

![[00 assets/8a2f9a244493c606f50b27cdf88aa543_MD5.png]]

并且该环境变量是可以被修改的，但是只是当前进程中被修改，不会影响全局的变量使用

![[00 assets/74ccb67b3b49f0b16e254b42b0e8f621_MD5.jpeg]]

> 退出进程

![[00 assets/18cbb83cbebf0fbe49776edcf46ef09b_MD5.png]]

1、如果按照下面的方式来执行，就会在`2s`的时候退出当前进程，所以`5s`的定时器就会被挂载，不能被执行

![[00 assets/bd96a9b1c760f0526fab0dfa76b5b68f_MD5.png]]

## 13.2 子线程

### 13.2.1 exec

1、可以使用`exec`来执行命令

2、下面为`options`选项

```bash
cwd <string> 子进程的当前工作目录。
env <Object> 环境变量键值对。
encoding <string> 默认为 'utf8'。
shell <string> 用于执行命令的 shell。 在 UNIX 上默认为 '/bin/sh'，在 Windows 上默认为 process.env.ComSpec。 详见 Shell Requirements 与 Default Windows Shell。
timeout <number> 默认为 0。
maxBuffer <number> stdout 或 stderr 允许的最大字节数。 默认为 200*1024。 如果超过限制，则子进程会被终止。 查看警告： maxBuffer and Unicode。
killSignal <string> | <integer> 默认为 'SIGTERM'。
uid <number> 设置该进程的用户标识。（详见 setuid(2)）
gid <number> 设置该进程的组标识。（详见 setgid(2)）
```

![[00 assets/40a1efa4619dfc7f5c0d984f0ca1e6c1_MD5.jpeg]]

3、如果只是单个指令的话，也可以使用`execSync`来处理，这个表示同步的方式来调用

![[00 assets/b36bd75d2e6c85ddbc30aceb9f42db09_MD5.png]]

4、使用`execFile`也可以运行可执行文件

![[00 assets/08a72ef9bfff4909d3267fa19565871e_MD5.jpeg]]

### 13.2.2 spawn

1、`spawn` 用于执行一些实时获取的信息，因为`spawn`返回的是流边执行边返回，`exec`是返回一个完整的`buffer`，`buffer`的大小是`200k`，如果超出会报错，而`spawn`是无上限的。

2、`spawn`在执行完成后会抛出`close`事件监听，并返回状态码，通过状态码可以知道子进程是否顺利执行。`exec`只能通过返回的`buffer`去识别完成状态，识别起来较为麻烦

3、并且对于`exec`、`spwan`之间的底层原理的实现是`exec` -> `execFile` -> `spawn`，`exec`是基于`execFile`实现的

![[00 assets/ddbb660a2b7ccb9002ac2c3815651432_MD5.png]]

### 13.2.3 fork

1、场景适合大量的计算，或者容易`阻塞主进程`操作的一些代码，就适合开发`fork`

2、他只能调用`JS模块`，他的原理就是`IPC通讯`，`IPC`又是基于`libvu`

3、我们使用`fork`会创建一个子线程来执行该`js模块`，我们可以与该子线程之间进行通讯

![[00 assets/485bf1b284fab74f7e49e06939186e10_MD5.png]]

## 13.3 案例

> 区分开发/生产环境

1、我们可以根据`process.env`来做很多的操作，比如：区分`开发环境`和`生产环境`

2、`cross-env`本质就是`windows`调用`SET`来设置环境变量，`posix`就是调用`export`来设置环境变量

```bash
set NODE_ENV=production  	#windows
export NODE_ENV=production 	#posix
```

![[00 assets/985494700f39b3e53962eaf8cc83432b_MD5.png]]

> 调用 Java 程序

1、可以使用`exec`来调用`.java`编译之后的`.class`文件

![[00 assets/c1e2b998a4b211bf050aab9ba901e868_MD5.jpeg]]

# 14. ffmpeg

## 14.1 基本使用

1、进入网站下载：[Builds - CODEX FFMPEG @ gyan.dev](https://www.gyan.dev/ffmpeg/builds/)，并且将该`ffmpeg`配置环境变量即可，控制台输入`ffmpeg`可以打印字符就代表安装完成

![[00 assets/eb652773020cdbf8bc3dbe9b11170245_MD5.jpeg]]

> 转化视频格式

1、这里使用了`execSync`子线程来做处理，`-i`表示输入，`1.mp4`表示输入文件，`2.avi`表示输出文件，`{ stdio: "inherit" }`表示打印对应的参数

2、不仅仅是`.avi`，还可以转化为`.gif`等格式

![[00 assets/d9bcc49ed6308e58ca7df5931e6a7082_MD5.jpeg]]

> 提取音频

1、这里直接改为`mp3`即可，就可以提取出音频

![[00 assets/c77717879a8d7c91fb4ea9f76a210f49_MD5.png]]

> 裁剪视频

1、`-ss`表示从多少开始，`-to`表示多少结束

![[00 assets/aca56b258c6225c36e9f49af6d258c8e_MD5.png]]

> 添加/删除水印

1、下面的参数就是为视频添加一个`zjh`的水印，并且设置了他的颜色为白色

![[00 assets/f72d651d971f2a7849ebd0882f378e08_MD5.png]]

2、使用`delogo`来删除水印

![[00 assets/cbddd4b6cb36358389585a84443468d2_MD5.jpeg]]


# 14. 中间件

## 9.1 基本介绍

![[00 assets/543e854b449a084bc8133ede30b144c1_MD5.png]]

我感觉其实本质就是路由守卫，在跳转路由之前执行操作

![[00 assets/fcf555de03ecbb1b310316d2c7f7ed3f_MD5.png]]

## 9.2 中间件分类

### 9.2.1 普通中间件

下面就是中间件的基本使用，下面的`app.use()`就是让这个函数全局生效，并且优先执行，然后再进行路由的跳转，而且中间件里面的`req`和`res`都是全局共享的，再上游的中间件使用，下游的中间件和路由都可以生效

```javascript
const express = require("express");
const app = express();

app.use(function (req, res, next) {
  const time = Date.now();
  req.time = time;
  console.log("这是一个中间件");
  // next()调用栈内的下一个中间件，假如你不调用的话就会阻塞
  next();
});

app.get("/", function (req, res) {
  console.log("Get请求" + req.time);
});
app.post("/", function (req, res) {
  console.log("Post请求" + req.time);
});

app.listen(80, function () {
  console.log("80端口打开");
});
```

下面就是上下游中间件，顺序是执行匹配到的中间件，然后从上到下依次执行

```javascript
const express = require("express");
const app = express();

app.use(function (req, res, next) {
  console.log("这是中间件1号");
  next();
});

app.use(function (req, res, next) {
   console.log("这是中间件2号");
   next();
 });

app.get("/", function (req, res) {
  console.log("Get请求");
});
app.post("/", function (req, res) {
  console.log("Post请求");
});

app.listen(80, function () {
  console.log("80端口打开");
});
```

![[00 assets/a0a860efb884988685fb9f5fc9ce1372_MD5.jpeg]]

### 9.2.2 路径匹配中间件

```javascript
const express = require("express");
const app = express();

const Http_Port = 8080;

app.use("/home", (req, res, next) => {
   console.log("路径中间件已经执行了")
   next()
});

app.listen(Http_Port, () => {
  console.log(`端口${Http_Port}监听中`);
});

```

![[00 assets/70d86187451b297e9ad4b0569cd29176_MD5.png]]

### 9.2.3 路径方法中间件

```javascript
const express = require("express");
const app = express();

app.use(function (req, res, next) {
  console.log("这是中间件1号");
  next();
});

// 其实express的method的本质就是一个中间件
app.get("/user", function (req, res) {
  res.send({ name: "张三", age: 12 }); // 向客户端响应内容
});
app.post("/user", function (req, res) {
  res.send({ name: "张三", age: 12 });
});

app.listen(80, () => {
  console.log("开启服务");
});
```

### 9.2.4 局部中间件

下面就是使用局部中间件，我们不仅可以使用单个，还可以使用多个

```javascript
const express = require("express");
const app = express();

const fn = function (req, res, next) {
  console.log("这是局部中间件1号");
  next();
};
const fn1 = function (req, res, next) {
  console.log("这是局部中间件2号");
  next();
};

// 使用单个中间件
app.get("/", fn, function (req, res) {
  console.log("Get请求");
});
// 使用多个中间件
app.get("/", fn, fn1, function (req, res) {
  console.log("Get请求");
});
// 或者使用数组包裹的中间件
app.get("/", [fn, fn1], function (req, res) {
  console.log("Get请求");
});
// 其实局部中间件的本质就是多写几个回调函数，从上往下执行
app.get(
  "/",
  (req, res, next) => {
    console.log("中间件1");
    next();
  },
  (req, res, next) => {
    console.log("中间件2");
    next();
  },
  (req, res, next) => {
    console.log("Get请求");
  }
);

app.post("/", function (req, res) {
  console.log("Post请求");
});

app.listen(80, function () {
  console.log("80端口打开");
});

```

## 9.4 中间件分类

### 9.4.1 应用级别中间件

![[00 assets/1d92d14def640b20922adbc4665f2b50_MD5.png]]

### 9.4.2 路由级别中间件

![[00 assets/d8e3b8e2e93ee76d7e0589350c3810da_MD5.png]]

### 9.4.3 错误级别中间件

![[00 assets/fc36888e04ace87b0470e48c812bd36a_MD5.png]]

下面就是错误级别中间件的使用方式

![[00 assets/ab95a89e271356d5ddbabeaf6fed42ce_MD5.png]]

### 9.4.4 Express 内置中间件

![[00 assets/c056ec7541639b41919863ad0b77afa9_MD5.jpeg]]

> express.json()

下面就是使用`express.json()`来解析`json`文件

```javascript
const express = require("express");
const app = express();

// 使用express.json()中间件 这样就可以解析JSON格式文件
app.use(express.json());

app.post("/", function (req, res) {
  res.send("这就是返回的值:" + req.body);
});

app.listen(80, function () {
  console.log("80端口打开");
});
```

> express.urlencoded()

其实本质和上面的`express.json()`是一样的

```javascript
const express = require("express");
const app = express();

// 使用express.json()中间件 这样就可以解析JSON格式文件
app.use(express.urlencoded({ extended: false }));

app.post("/", function (req, res) {
  res.send(req.body);
  console.log(req.body)
});

app.listen(80, function () {
  console.log("80端口打开");
});
```

x-www-form-urlencoded：[(77 条消息) form-data 和 x-www-form-urlencoded 的区别\_Bee.F 的博客-CSDN 博客](https://blog.csdn.net/qq_33732195/article/details/112854232)

### 9.4.5 第三方中间件

这里使用的是`npm i body-parser`来下载第三方中间件，下面就是基本的使用

```javascript
const express = require("express");
const app = express();
// 引入body-parser
const BodyParser = require("body-parser");
// 配置中间件
app.use(BodyParser.urlencoded({ extended: false }));

app.post("/", function (req, res) {
  console.log(req.body);
});

app.listen(80, function () {
  console.log("80端口打开");
});
```

## 9.5 自定义中间件

下面就是自定义中间件，我们可以自己写自定义的中间件

> 参数解析

`qs`是用于将字符串对象解析为 js 对象的

![[00 assets/5e5355bf2d5c20a696df3146598bd00c_MD5.jpeg]]

> 防盗链

1、可能存在一些资源只在自己的域名下访问，但是其他域名不允许访问，这里是通过`referer`来判断

![[00 assets/0698e324c0a8fc3a35149480613a8f0a_MD5.png]]

2、下面就是实现的原理，只要监测到请求的地址中和自己本身的`referer`不匹配的话就不去继续请求，这样就实现了防盗链的效果

![[00 assets/9c055be90649375a0ad938fdf2341415_MD5.jpeg]]

# 15. 数据库

## 15.1 基本介绍

![[00 assets/18d41f059972ac9ee4654ee3b0bf9d87_MD5.png]]

我们也可以对数据库进行分类

![[00 assets/9c96f955b9f8d9405aa61c8575ed5124_MD5.png]]

数组库的组织方式

![[00 assets/808de6aa8ed6e09409b0af53f3129f86_MD5.png]]

## 15.2 mysql 基础

这段可以查看我的`mysql`笔记，以及**最重要的将查询到的数据转换为对象和数组**，这对后面传输数据很重要

## 15.3 mysql

✨ 该版本较低，可以查看`mysql2`

首先先安装`mysql`的模块

```bash
npm i mysql
```

但是这里会有一个小问题，就是 mysql 的`版本问题`，假如你是`mysql8`以上的版本就会出现下面的错误

![[00 assets/ff104273ad40e0d25ca1222e8621bbc9_MD5.png]]

这其实是因为 Node 不支持最新版本的 mysql 的密码加密方式，所以这个时候就需要设置 mysql 的加密方式了，将加密方式改为这种就可以正常连接了

![[00 assets/89b1f755aafffe09f6786add1c00858d_MD5.jpeg]]

下面就是`连接mysql`和`执行sql`

```javascript
// 导入mysql模块
const mysql = require("mysql");

// 建立与mysql的连接
const db = mysql.createPool({
  host: "127.0.0.1", // 主机
  user: "root", // 用户名
  password: "201314", // 密码
  port: "3306", //端口号
  database: "db01", // 指定连接的数据库
});

// 查询
db.query("select * from user", (err, results) => {
  if (err) return console.log(err.message);
  console.log(results);
});

// 插入
const user = { username: "张三", address: "武汉" };
const sqlStr = "insert into user(name,address) values (?,?)";
db.query(sqlStr, [user.username, user.address], (err, results) => {
  if (err) return console.log(err.message);
  if (results.affectedRows == 1) console.log("执行成功:" + results);
});

// 插入 - 简化
const user1 = { name: "张三", address: "武汉" };
const sqlStr1 = "insert into user set ?"; // 这个其实是mysql支持的数据
db.query(sqlStr1, user1, (err, results) => {
  if (err) return console.log(err.message);
  if (results.affectedRows == 1) console.log("执行成功:" + results);
});

// 更新
const user2 = { id: 1, name: "李四", address: "北京" };
const sqlStr2 = "update user set name=?,address=? where id=?";
db.query(sqlStr2, [user2.name, user2.address, user2.id], (err, results) => {
  if (err) return console.log(err.message);
  if (results.affectedRows >= 1) console.log("执行成功:" + results);
});

// 更新 - 简化
const user3 = { name: "李四", address: "北京" };
const userid = { id: 1 }; // 因为id设置为主键
const sqlStr3 = "update user set ? where ?";
db.query(sqlStr3, [user3, userid.id], (err, results) => {
  if (err) return console.log(err.message);
  if (results.affectedRows >= 1) console.log("执行成功:" + results);
});

// 删除
const user4 = { id: 1 };
const sqlStr4 = "delete from user where id=?";
db.query(sqlStr4, user4.id, (err, results) => {
  if (err) return console.log(err.message);
  if (results.affectedRows >= 1) console.log("执行成功:" + results);
});
```

但是这里涉及了一个概念就是标记删除，我们可以将设置一个状态属性来标记这个字段将要删除

![[00 assets/b8d0ff7236ad3a8788697807f4cff632_MD5.png]]

## 15.4 mysql2

### 15.4.1 基本介绍

![[00 assets/4c84728565e5457f130d8c59fdc3c2ee_MD5.png]]

**mysql2 官方文档**：[node-mysql2/documentation_zh-cn at master · sidorares/node-mysql2 (github.com)](https://github.com/sidorares/node-mysql2/tree/master/documentation_zh-cn)

### 15.4.2 基本使用

```bash
npm i mysql2 // 安装mysql2
```

下面就是`连接数据库`和执行`sql`

```javascript
const mysql = require("mysql2");

// 创建数据库连接
const connect = mysql.createConnection({
  host: "localhost",
  port: "3306",
  database: "zjh_db04",
  user: "root",
  password: "201314",
});

// 这个可以测试数据库连接
connect.getConnection((err,conn)=>{
    conn.connect((err)=>{
		if(err) return console.log("数据库连接失败",err)
        console.log("数据库连接成功")
    })
})

// 执行sql语句
const statment = "select * from courses";
connect.query(statment, (err, result, fields) => {
  if (err) return console.log(err);
  console.log(result);
});
```

![[00 assets/e56bacdce777c7e61fd78241996fc90a_MD5.png]]

我们可以看到回调中第三个参数`fields`，里面包含了数组中每个列得相关信息

![[00 assets/388644b9401e947a08153f2f0f89676c_MD5.png]]

当然官方也提供非回调得方式，`connect`都可以进行`Promise()`化。**官方文档中提到了很多得写法**，可以去看看

```javascript
// 1.Promise()
const statment = "select * from courses where id = ? and name = ?";
connect.promise().execute(statment, [1, "英语"]).then((res) => {
   console.log(res[0]);
}).catch((err) => {
   console.log(err);
});


// 2.async await
const mysql = require("mysql2/promise"); // 这里需要引入mysql2/Primise

// 创建数据池
const connect = mysql.createPool({
  host: "localhost",
  port: "3306",
  database: "zjh_db04",
  user: "root",
  password: "201314",
  connectionLimit: 5,
});

// 执行sql语句
const statment = "select * from courses where id = ? and name = ?";
async function main() {
  const result = await connect.execute(statment, [1, "英语"]);
  console.log(result);
}
main()

// 官方文档还有很多得写法
```

![[00 assets/c9df93104e1debcc9804e221e55ea9e9_MD5.png]]

### 15.4.3 关闭数据库

我们可以使用下面的 2 种方式来关闭数据

```javascript
// 方式一
connect.end(); // 关闭于数据库的连接
connect.on("error", (err) => { // 进行监听，关闭的途中又错误就会报告错误信息
   console.log(err)
});

// 方式二
// 直接关闭，不会报错误信息
connect.destroy()
```

### 15.4.4 预编译语句

![[00 assets/6ddc1f6d8a459aeca161dc09bda3ed96_MD5.png]]

这里建议使用`预编译语句`，当你多次执行这条语句内部并不会多次执行，而是将以前查询到得语句给你。而且使用预编译语句可以防止`sql注入`

```javascript
const mysql = require("mysql2");

// 创建数据库连接
const connect = mysql.createConnection({
  host: "localhost",
  port: "3306",
  database: "zjh_db04",
  user: "root",
  password: "201314",
});

// 执行sql语句
const statment = "select * from courses where id = ? and name = ?";

// 这里使用[1,"英语"]来填充sql语句中得?
connect.execute(statment, [1, "英语"], (err, result, fields) => {
  if (err) return console.log(err);
  console.log(result);
  console.log(fields);
});
```

![[00 assets/224d6bb755b90b94794db90bdc32d6d9_MD5.png]]

### 15.4.5 连接池

![[00 assets/3cf5887def658fcaaa94749929a087e9_MD5.png]]

1、我们创建连接池得时候使用`mysql.createPool()`

```javascript
const mysql = require("mysql2");

// 创建数据池
const connect = mysql.createPool({
  host: "localhost",
  port: "3306",
  database: "zjh_db04",
  user: "root",
  password: "201314",
  connectionLimit: 5,
});

// 执行sql语句
const statment = "select * from courses where id = ? and name = ?";
connect.execute(statment, [1, "英语"], (err, result, fields) => {
  if (err) return console.log(err);
  console.log(result);
});
```

2、需要操作数据库的时候，建立连接，用完之后释放连接。但这样性能并不高。因为数据库的连接建立还是很耗时的，而且一个连接也不够用。我们一般都是用连接池来管理。连接池中放着好几个 mysql 的连接对象，用的时候取出来执行 sql，用完之后放回去，不需要断开连接。

![[00 assets/a521d206c0ad73b3c233bba59c2add20_MD5.png]]

3、当然对于连接池存在很多其他配置，也就是下面的内容，而且可以使用`mysql2/promise`来导出异步

```javascript
const mysql = require('mysql2/promise');

(async function() {
    const pool = mysql.createPool({
        host: 'localhost',
        user: 'root',
        password: 'guang',
        database: 'practice',
        waitForConnections: true, // 如果连接池已满，是否等待可用连接。设为true表示等待，false表示不等待
        connectionLimit: 10, // 连接池的最大连接数
        maxIdle: 10, // 最大空闲连接数，超过这个数量的空闲连接会被释放。
        idleTimeout: 60000, // 空闲连接超时时间（毫秒）
        queueLimit: 0, // 当连接池达到最大连接数时，新的连接请求会排队，此参数指定排队的最大数量。设为0表示无限制
        enableKeepAlive: true, // 是否启用连接保持活跃，保持心跳用的，用默认的就好
        keepAliveInitialDelay: 0 // 连接保持活跃的初始延迟，保持心跳用的
      });

    const [results] = await pool.query('select * from customers');
    console.log(results);
})();
```

### 15.4.6 query 和 execute 区别

## 15.5 sequelize

### 15.5.1 基本介绍

![[00 assets/682c4d9a418cef81d4a0acb3d26b27da_MD5.png]]

其实`ORM`得本质就是下面图

![[00 assets/e5f05b79dd2835b0e409b8dcddd20250_MD5.png]]

Node.js 中 ORM 介绍：[ORM 实例教程 - 阮一峰的网络日志 (ruanyifeng.com)](https://www.ruanyifeng.com/blog/2019/02/orm-tutorial.html)

介绍 MVC：[深入理解 MVC - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/35680070)

我们使用`ORM`主要是为了实现`MVC`架构，将`ORM`的实现直接写入`Model`中，方便代码的维护

### 15.5.2 基本使用

建议查看**Sequelize 官网**：[Sequelize | Feature-rich ORM for modern TypeScript & JavaScript](https://sequelize.org/)

```bash
npm i sequelize // 基本使用
```

下面为连接的方式

```javascript
const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("zjh_db04", "root", "201314", {
  host: "localhost",
  dialect: "mysql",
});

sequelize.authenticate().then(() => {
  console.log("数据库连接成功");
}).catch((err) => {
  console.log(err);
});
```

### 15.5.3 映射表

```javascript
const { Sequelize, Model, DataTypes, Op } = require("sequelize");

// 1.连接数据库
const sequelize = new Sequelize("zjh_db04", "root", "201314", {
  host: "localhost",
  dialect: "mysql",
});

sequelize
  .authenticate()
  .then(() => {
    console.log("数据库连接成功");
  })
  .catch((err) => {
    console.log(err);
  });


// 2.连接数据库中的表
class students extends Model {}
students.init(
  {
    id: {
      type: DataTypes.INTEGER, // 表示数据类型
      primaryKey: true, // 是否为主键
      autoIncrement: true, // 是否自动增长
    },
    name: {
      type: DataTypes.STRING(20), // 或者DataTypes.STRING()
      allowNull: false, // 是否为空
    },
    age: DataTypes.INTEGER,
  },
  {
    tableName: "students", // 明确与数据库的关系映射
    createdAt: false, // 在sql中默认会添加createdAt，这个是在sql中取消添加
    updatedAt: false, // 和上面类似
    sequelize,
  }
);
```

![[00 assets/da1ba91e2041163acdbc8b8abd581c6c_MD5.jpeg]]

### 15.5.4 执行 sql

> 查询

```javascript
------------- // 和映射表类似 // --------------

async function query() {
  // 1. 查询数据库中students表所有内容
  const result = await students.findAll();
  console.log(result);

  // 2.查询数据 - 添加条件
  const result1 = await students.findAll({
    where: {
      age: {
        /*
           gte表示大于等于,gt表示大于
           let表示小于等于,le表示小于
        */
        [Op.gte]: 20,
      },
    },
  });
  console.log(result1)
}
query();
```

![[00 assets/dd8d850eff2f33941cb8200049c490d5_MD5.png]]

> 插入

```javascript
async function query() {
  const result = await students.create({
    name: "张三",
    age: 100,
  });
  console.log(result)
}
query();
```

![[00 assets/0fb34f8f954337104753a9c67e591f7e_MD5.png]]

> 更新

```javascript
async function query() {
  const result = await students.update(
    {
      name: "赵六",
    },
    {
      where: {
        id: 6,
      },
    }
  );
  console.log(result);
}
query();
```

![[00 assets/da436310843ea5b6c9c2d87816d23c14_MD5.png]]

### 15.5.5 多对多关系

处理多对多的关系，一般使用中间表来处理，对应下面的代码中实例就是`students_select_courses`

```javascript
const { Sequelize, Model, DataTypes, Op } = require("sequelize");

// 1.连接数据库
const sequelize = new Sequelize("zjh_db04", "root", "201314", {
  host: "localhost",
  dialect: "mysql",
});

sequelize
  .authenticate()
  .then(() => {
    console.log("数据库连接成功");
  })
  .catch((err) => {
    console.log(err);
  });

// 2.连接表
class Students extends Model {}
Students.init(
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    name: {
      type: DataTypes.STRING(20), // 或者DataTypes.STRING()
      allowNull: false,
    },
    age: DataTypes.INTEGER,
  },
  {
    tableName: "students", // 明确与数据库的关系映射
    createdAt: false,
    updatedAt: false,
    sequelize,
  }
);

class Courses extends Model {}
Courses.init(
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    name: {
      type: DataTypes.STRING(20), // 或者DataTypes.STRING()
      allowNull: false,
    },
    price: {
      type: DataTypes.DOUBLE,
      allowNull: false,
    },
  },
  {
    tableName: "courses", // 明确与数据库的关系映射
    createdAt: false,
    updatedAt: false,
    sequelize,
  }
);

class students_select_courses extends Model {}
students_select_courses.init(
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    studentId: {
      type: DataTypes.INTEGER,
      /*
      	 因为不识别下划线的写法，所以field就是映射数据表的字段
      	 studentId -> student_id
      */
      field: "student_id",
      allowNull: false,
      references: { // 设置外键
        model: Students,
        key: "id",
      },
    },
    courseId: {
      type: DataTypes.INTEGER,
      allowNull: false,
      field: "course_id",
      references: {
        model: Courses,
        key: "id",
      },
    },
  },
  {
    tableName: "students_select_courses", // 明确与数据库的关系映射
    createdAt: false,
    updatedAt: false,
    sequelize,
  }
);

// 设置多对多的映射关系
Students.belongsToMany(Courses, {
  through: students_select_courses,
  foreignKey: "student_id",
  otherKey: "course_id",
});

Courses.belongsToMany(Students, {
  through: students_select_courses,
  foreignKey: "course_id",
  otherKey: "student_id",
});

async function query() {
  const result = await Students.findAll({
    include: {
      model: Courses,
    },
  });
  console.log(result)
}
query();
```

![[00 assets/5802008c0bea9522aeaeb3a391a5bf1b_MD5.png]]

## 15.6 typeorm

### 15.6.1 基本介绍

参考`sequelize`即可

### 15.6.2 基本使用

1、使用`npx typeorm@latest init --name typeorm-mysql-test --database mysql`来初始化一个`typeorm`的项目，`--name` 指定项目名，`--database` 指定连接的数据库

2、还需要下载`npm install --save mysql2`来连接数据库

3、我们需要额外的填写用户名和密码，并且还要指定连接数据库的包名，这里我们使用的`mysql2`，`sha256_password`，这个是切换密码的加密方式的，新版本 mysql 改成这种密码加密方式了

4、`synchronize` 是根据同步建表，也就是当 database 里没有和 Entity 对应的表的时候，会自动生成建表 sql 语句并执行

5、`poolSize`是指定数据库连接池中连接的最大数量

![[00 assets/9025dab619253cd84308f405846e6fcc_MD5.png]]

5、我们看下代码， 有一个`entity`，通过装饰器声明了主键列和其他的列，这个就是数据库中的结构，我们以对象的形式映射出来

6、我们使用`save`和`find`来保存和查找对应的数据

![[00 assets/d436a8fe82b78bd790f191f44654f297_MD5.png]]

7、我们开启`typeorm`的`logging`可以看到本质就是自动生成`sql`语句

![[00 assets/a0ddc019316fd6eb5917d920cdbf5dbc_MD5.png]]

8、并且会开启事务，我们可以提交和回滚

![[00 assets/36e6ad7451247f86b6df2d14bf68c2ec_MD5.png]]

### 15.6.3 增删改查

#### 15.6.3.1 建表

1、创建表的依据就是 `Entity`，如果我们开启了`synchronize`就会自动根据`Entity`来建表

2、当然我们也可以手动来设置`Entity`来控制表的字段

![[00 assets/fa7e556d4d9c961da90c75c3cb2b2cbe_MD5.png]]

3、当然我们也可以修改里面的数据类型，还可以设置一些其他的配置

4、下面是对这些属性的解释，如果想知道更多可以查看文档

​ `@Entity` 指定它是一个 Entity，name 指定表名为 person。

​ `@PrimaryGeneratedColumn` 指定它是一个自增的主键，通过 comment 指定注释。

​ `@Column` 映射属性和字段的对应关系。通过 `name` 指定字段名，`type` 指定映射的类型，`length` 指定长度，`default` 指定默认值。`nullable` 设置 NOT NULL 约束，`unique` 设置 UNIQUE 唯一索引。`type` 这里指定的都是数据库里的数据类型

![[00 assets/8a140094ed1449e9556dc261b1738620_MD5.jpeg]]

#### 15.6.3.2 添加

##### 15.6.3.2.1 save

> 单条数据

1、使用`save`来插入数据，如果`id`相同的话就会变为`update`，前提是`id`为主键才能实现

![[00 assets/535823f689281935f024c129d1ea6360_MD5.png]]

> 多条数据

2、如果我们想要插入多条数据，使用下面的方式

![[00 assets/5da6991cc12e39f87cab8368496aad85_MD5.png]]

#### 15.6.3.3 删除

##### 15.6.3.3.1 delete/remove

1、使用`delete`来删除数据，下面默认选择的主键来删除

![[00 assets/60d265f9c6e2487375cf57943d90e8a0_MD5.png]]

2、`delete` 和 `remove` 的区别是，`delete` 直接传 id、而 `remove` 则是传入 entity 对象

3、目前看只能使用主键 id 来删除数据，以后有时间查看一下文档

![[00 assets/416bb955a19ffbba79013ce8e70ace97_MD5.png]]

#### 15.6.3.4 查询

##### 15.6.3.4.1 find

1、使用`find`来查询表中所有数据

![[00 assets/92285f93ee0a253bf74d9a811bb9b784_MD5.png]]

2、当然我们也可以添加一些条件，`In()`表示的就是`mysql`中的`in`

![[00 assets/ec727cc4945b8df4ae989f6b72ebfb18_MD5.jpeg]]

##### 15.6.3.4.2 findBy

1、可以通过 `findBy` 方法根据条件查询

![[00 assets/0f670f502319cea8ced09f52dccbce9c_MD5.png]]

##### 15.6.3.4.3 findAndCount

1、此外，你还可以用 `findAndCount` 来拿到有多少条记录

![[00 assets/061f5d4864970cf0980264f360933d70_MD5.jpeg]]

##### 15.6.3.4.4 findAndCountBy

1、还可以添加查询条件

![[00 assets/be949839019293f6bfa2e4cdc32da5e0_MD5.png]]

##### 15.6.3.4.5 findOne

1、使用`findOne`表示查询一条数据，可以添加查询条件

![[00 assets/c55423f079c84578fd4bd4dcec7aa5f1_MD5.jpeg]]

##### 15.6.3.4.6 findOneBy

1、通过`xxx`值查询一条数据

![[00 assets/8057f4b7c89249b1a0379ebeb65ef303_MD5.png]]

##### 15.6.3.4.7 findOneOrFail / findOneByOrFail

1、`findOneOrFail` 或者 `findOneByOrFail`，如果没找到，会抛一个 `EntityNotFoundError` 的异常

![[00 assets/39bf116de27f28118312134baeb068fa_MD5.jpeg]]

##### 15.6.3.4.8 query

1、还可以用 `query` 方法直接执行 `sql` 语句

![[00 assets/905704c4b7273e5383831d1771dae9da_MD5.png]]

2、不仅仅是普通的`select`，还可以执行一些其他的语句

![[00 assets/09f6dbe6d28e7fa83dbb7d4e1a964599_MD5.jpeg]]

#### 15.6.3.5 querybuilder

1、一般情况下，复杂 `sql` 语句不会直接写，而是会用 `query builder`，下面就是一个简单的使用

![[00 assets/220603d1a2f6b7879597a7f73c881e45_MD5.png]]

2、用 `query builder` 和我用 `find` 指定 `where` 有什么区别么？比如这种复杂的关联查询

3、涉及到多个表，也就是多个 `Entity `的关联查询，就得用 `query builder` 了。简单点查询直接 `find` 指定 `where` 条件就行。

![[00 assets/7c6ce38761d149a6aba2d1363d7049a8_MD5.png]]

### 15.6.4 getRepository

1、调用每个方法的时候都要先传入`实体类`，这也太麻烦了

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325764.png" alt="image-20231225000449054" style="zoom:67%;" />

2、可以先调用 `getRepository` 传入 `Entity`，拿到专门处理这个 `Entity` 的增删改查的类，再调用这些方法

![[00 assets/3ea0c0061c7d397e9b9422146a5471fc_MD5.jpeg]]

3、我们查看查看下面的代码，可以发现不用写那么多的`AppDataSource.manager(User)`，而是使用统一的`user_repo`即可

![[00 assets/45da58f77dcbaf770563e9b7303f158b_MD5.jpeg]]
### 15.6.5 事务

1、使用`transaction`可以开启事务

![[00 assets/c7665e0df0f2520718214fb2dc1bd63e_MD5.jpeg]]

### 15.6.6 关系

#### 15.6.6.1 一对一

1、默认情况下我们需要额外设置一个表和另外一个表得一对一得关系，在`typeorm`中使用下面得方式设置

2、在 IdCard 的 `Entity` 添加一个 user 列，指定它和 User 是 `@OneToTone` 一对一的关系。

3、还要指定 `@JoinColum` 也就是外键列在 IdCard 对应的表里维护，该注解是一定要指定得

4、同时设置外键得时候，还可以设置`mysql`得联级关系

![[00 assets/2b1cc4eb472fa3d53270238117c48ace_MD5.png]]

可以看到数据库中填写了对应得数据

![[00 assets/6eed7f78ec9289edad5dfff725df87c5_MD5.png]]

5、同时我们还可以设置`cascade`为`true`，该联级关系是`typeorm`中维护得，告诉 `typeorm` 当你增删改一个 `Entity` 的时候，是否级联增删改它关联的 `Entity` 因为我们手动设置了`OnetoOne`得关系，并且直接传入了`user`，可以只保存`idcard`即可自动更新插入`user`得数据

![[00 assets/9af5fd81f12897d2442dfbf86f2c8cd9_MD5.png]]

6、我们还可以设置联级查询，设置`relations`即可，他会联级一起查询

![[00 assets/5f86a63341f187686d87c1ca1918ab0c_MD5.png]]

#### 15.6.6.2 一对多

1、下面就是一个例子，比如说：员工对部门就是一对多的关系，我们分别创建一个`员工（employee）`和`部门（department）`2 个表，其中`employee`需要连接`department`，也就是设置外键

> ManyToOne

1、不管是`一对一`、`一对多`可以这样理解，我需要和外部连接，所以我的关系注解就写在哪里，下面的`@ManyToOne`就是一个例子

2、`many`指的是`employee`，也就是`employee`作为外键来指向`department`，这就是`ManyToOne`

![[00 assets/debec2a39eb29255380c9762bdc51de7_MD5.png]]

3、创建之后保存即可，和上面类似

![[00 assets/622c33465e843a0d5f0b5a010ba28312_MD5.png]]

4、当然还可以设置`cascade`，他使用`typeorm`来自动保存联级，这样我们就不需要额外写`Department`的保存了

![[00 assets/2775a60916113e3583e4be67c42c67f7_MD5.png]]

> OneToMany

1、一般情况一对多关系更多还是在一的那一方来保持关系，一般情况写的时候也是需要`oneToMany`和`manyToOne`都会去编写，也就是下面的依赖关系

2、一对一的时候我们还通过 `@JoinColumn` 来指定外键列，为什么一对多就不需要了呢？因为一对多的关系只可能是在多的那一方保存外键呀！所以并不需要 `@JoinColumn`。不过你也可以通过 `@JoinColumn` 来修改外键列的名字

3、并且这里我们将`manyToOne`的`cascade`移到`department`中，如果 2 边都编写的话就变成依赖循环了

![[00 assets/e97809b57aa69ee3902e551e6dcde071_MD5.png]]

4、这里我们可以看到，因为为`department`添加了`employee`，所以这里需要将数据传递给`department`来处理，和上面的不同

![[00 assets/629548ffa985622f55087afb86de79aa_MD5.png]]

5、并且`relations`本质就是一个`left join ... on ...`，我们也可以使用`query builder`来处理

![[00 assets/b6b048beda501283ca71a868bb0a9d6d_MD5.jpeg]]


6、删除的时候也是一样，要先删除`employee`，才能删除`department`，这个和`mysql`是一致的

7、或者在创建的时候设置配置外键`onDelete`的属性即可，这里一定要设置给`Employee`，不能设置给`Department`。这里我就不是很理解了，因为大部分的关系都是给`one`的部分，理所应当也要把`onDelete`给`one`的部分，但是却给了`more`的部分

![[00 assets/053a1972b4ebac38acc00edeb2d753ad_MD5.png]]

我们删除`department`的时候，`employee`也会同步删除

![[00 assets/8c26a8ce86d79beb4bc883c997392834_MD5.png]]

#### 15.6.6.3 多对多

1、其中`多对多`上面的关系都类似，下面就文章和标签的多对多的关系

2、这里解释一下下面的第二个参数的作用，也就是`() => tag.articles`的作用，这个是手动指定外键。因为在多对多的关系中他们不存储外键，所以需要手动指定

![[00 assets/776cfe3ef3210262b2c89d0f9ce1cc11_MD5.png]]

3、因为如果当前 `Entity` 对应的表是包含外键的，那它自然就知道怎么找到关联的 `Entity`。但如果当前 `Entity` 是不包含外键的那一方，怎么找到对方呢？这时候就需要手动指定通过哪个外键列来找当前 Entity 了。之前 `OneToOne`、`OneToMany` 都是这样

4、一对多的 `department` 那方，不维护外键，所以需要第二个参数来指定通过哪个外键找到 department

![[00 assets/415a7a7ff42a2736034c67599b62598d_MD5.png]]

5、下面就是存储并且查找对应的数据

![[00 assets/4dc1012d9a8def96e73de961205f5b2c_MD5.png]]

可以看到这里多对多的的模型已经构建出来了

![[00 assets/e0932adf9e9d3a0ce54053a5e9aaed20_MD5.jpeg]]

6、当然我们也可以去更新`article`，他也会自动维护中间表

![[00 assets/6af71c329f69b3d2bde9ccd237d1e077_MD5.jpeg]]

7、至于删除就简单了，因为中间表的外键设置了 `CASCADE` 的级联删除，这样只要你删除了 `article` 或者 `tag`，它都会跟着删除关联记录。

![[00 assets/754af3221e777c3389f17b0c92b02d6a_MD5.png]]

## 15.6 Mongodb

### 15.6.1 基本介绍

可以参考我的`Mongodb`的笔记

### 15.6.2 Mongoose

#### 15.6.2.1 基本使用

1、我们使用`Mongoose`库来连接`mongodb`数据库

2、这里使用`once`函数表示，只连接一次并且执行内部函数，如果掉线之后并不会再次连接。而`on`就会一直询问`mongodb`连接

![[00 assets/625fbeeb07fce9b9bf635951b6001eae_MD5.png]]

## 15.7 redis

1、对于`redis`存在很多的官方推荐的库，可以参考下面的网址：[Clients | Redis](https://redis.io/resources/clients/#nodejs)

2、我这里就使用`node-redis`库来连接`redis`

3、下面为基本的使用，主要是用于查询所有的`keys`

![[00 assets/40cd2ad97441b2c14713691098a35530_MD5.png]]

4、还有一些其他命令，这里直接可以参考`redis`的命令即可，基本是一致的

![[00 assets/07111b629c8aa9b59ffbadd46a347641_MD5.png]]

# 16. 解决跨域

## 8.1 基本介绍

1、主要是因为现在前后端分离之后导致的问题，对于现在前端和后端的服务器不是一样的

![[00 assets/bf2b4bf4e57e3a36717469bad333f29c_MD5.jpeg]]

2、下面是模拟的代码，其中一份是前端代码，其中一份是后端代码，我们使用不同的方式来代理前端网页的时候就会出现不同的结果

```javascript
const koa = require("koa");
const koaRouter = require("@koa/router");
const koaStatic = require("koa-static");

const app = new koa();

const useRouter = new koaRouter({ prefix: "/api" });

useRouter.get("/list", (context, next) => {
    context.body = [
        { id: 1, name: "zjh" },
        { id: 2, name: "ls" },
    ];
});

app.use(koaStatic("./client"));
app.use(useRouter.routes());
app.use(useRouter.allowedMethods());

app.listen(8000, () => {
    console.log("服务器开启了~");
});
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World!</h1>

    <script>
      const xhr = new XMLHttpRequest();
      xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          console.log(JSON.parse(xhr.responseText));
        }
      };

      xhr.open("get", "http://127.0.0.1:8000/api/list");
      xhr.send();

      fetch("http://127.0.0.1:8000/api/list").then(async (res) => {
        console.log(await res.json());
      });
    </script>
  </body>
</html>
```

![[00 assets/668c198f3299cd3c3dff81dd10d83f6d_MD5.jpeg]]

## 8.2 解决方案

下面是比较常见的跨域的解决方式，上面使用`node.js`作为一个静态服务器就是`方案一`

![[00 assets/4c06d0d31ecd8cf1a47b45fcd3b2adde_MD5.png]]

### 8.2.1 CORS

> 基本介绍

![[00 assets/16d0d9e869a67271470f140a564f357d_MD5.png]]

> 基本使用

1、下面就是老师给出解决跨域问题的方式，参考文章：[Koa CORS 跨域问题 - 掘金 (juejin.cn)](https://juejin.cn/post/7136151612724084773)

2、但是这种解决方式用的并不多

![[00 assets/9cc822d7578708bf7b4a24e221f55e11_MD5.png]]

3、这里有一个坑，我们在使用`kao2-cors`的跨域库的时候，我们需要在`router`注册之前使用，不然无法使用

![[00 assets/6986cbd1145c255bed2d5b9a7f62c1da_MD5.jpeg]]

### 8.2.2 node 代理服务器

1、这个解决方式就是`webpack`中常见的`proxy`代理服务器的方式

![[00 assets/f6dc3c14196e091468fadf04e61cdabd_MD5.png]]

下面就是整体的结构图

![[00 assets/9b0d70a960829e180ca854df5cfe7e18_MD5.png]]

2、下面就是使用`http-proxy-middleware`中间件配合`express`来搭建的代理服务器

`http-proxy-middleware地址`：[chimurai/http-proxy-middleware： ：zap：单行节点.js http-proxy 中间件，用于连接，express，next.js 等 (github.com)](https://github.com/chimurai/http-proxy-middleware#pathrewrite-objectfunction)

3、对于`webpack`的代理服务器的本质就是下面的方式，但是要主要这个代理服务器只是`开发时依赖`，如果我们使用`webpack`打包之后就不存在这个代理服务器了

![[00 assets/29aa2f570e6ff5ee37237873af472cf5_MD5.png]]

### 8.2.3 nginx 反向代理

1、`nginx`反向代理是**上线**的时候使用的，而`node代理服务器`是**开发**时使用的。其实`nginx反向代理`的本质和`node代理服务器`是一样的，也是将请求的数据进行转发

2、下面是`nginx`的代理处理，只是简单的将`http://localhost:80`转发到了`http://localhost:8000`中

![[00 assets/18e2706dfdae039cc0ad32fbe94e8865_MD5.png]]

3、如果是真实的线上环境的话，其实就是`nginx`代理`静态资源`，随后同一端口的中再去代理转发`API服务器`

![[00 assets/94a47c778079ddcb87cd82c8cd81a60a_MD5.png]]

# 17. 项目实战

## 16.1 day01

### 16.1.1 项目介绍

![[00 assets/0e953ea6829aa4853db44e5b52a0ef8a_MD5.png]]

### 16.1.2 项目搭建

> 1.该项目使用 koa 来搭建

```bash
npm init -y // 初始化npm包
npm i koa // 安装koa
```

> 2.规定目录的划分

![[00 assets/f97de7bc0daa25bbf948dc9e82153ebf_MD5.png]]

当然我们也可以来参考`egg.js`的目录规范：[目录规范 | Egg (eggjs.github.io)](https://eggjs.github.io/zh/guide/directory.html)

我们再来配置我们项目的目录。然后配置`npm`的启动

![[00 assets/e66f9c6113660d9fb0063d4e3f9c0bf5_MD5.png]]

我们再对业务进行分包，这样分离方便维护。这是暂时是对`app`的分离

![[00 assets/3721c1c4ce70caee5497d5d24547d316_MD5.png]]

> 3.应用配置信息写到环境变量

![[00 assets/85cbf9aba662cf90cdb39c11c7488808_MD5.png]]

因为在项目中人数较多，很多配置的敏感信息不能被暴露，所以需要写一个配置文件。在根目录下创建一个`.env`文件。我们可以使用文件导入的形式来获取这些信息

![[00 assets/5b83b8d735b7048dc99590e7be37ce6b_MD5.png]]

但是并不是很方便，所以这里需要使用`dotenv`，`dotenv`官网：[dotenv - npm (npmjs.com)](https://www.npmjs.com/package/dotenv)

```bash
npm i dotenv // 安装dotenv
```

我们使用`dotenv`就会自动读取更目录下面的`.env`文件。

下面的导出的写法，其实是因为赋值运算符优先执行右边的语句，右边为`解构赋值`然后作为对象导出

![[00 assets/d4286e7a65e31f0abf38eab8cd01b05b_MD5.png]]

### 16.1.3 postman

我们接口测试使用的是`postman`，我们可以设置集合，对这次项目的接口进行管理

![[00 assets/38be29163601378250a769d454af1193_MD5.png]]

我们还需要配置环境，可能开发、测试、上线服务器都是不一样的，我们设置环境可以方便切换

![[00 assets/c11f3ea649406c260a949e79bea4e7e4_MD5.png]]

这样我们直接切换环境，可以改变`{{baseURL}}`的值，这样可以方便端口调试

![[00 assets/034c306e87ade8eea338fa684cf2e6ee_MD5.png]]

### 16.1.4 用户注册接口

我们首先将路由抽取出来放在一个单独的文件夹`router`中，因为后期有很多的路由接口。在文件命名上，也可以参考，这里使用的是`user.router.js`，假如以后有其他模块也叫做`user.js`的话就可以很好的区分

![[00 assets/b05e05d36359111f3429a5584a7baf0b_MD5.png]]

我们再来将路由中的方法进行拆分，因为该路由下面的接口也会很多，所以我们简化其中的代码。但是不仅仅只是简化其中的代码，这里涉及到了拆分的思想。作为路由的文件就做好路由跳转的事情。

![[00 assets/be4ccb736a8de8219737e9e238d90872_MD5.png]]

这里再来拆分查询数据的代码

![[00 assets/ae91cf76c1314e2cf81c44cc2b8832fe_MD5.png]]

最后安装上`koa-bodyparser`就可以解析`json`数据，注意中间件是从上往下执行

![[00 assets/a1e48959f28f2e1b0d77429bd0dd5d34_MD5.png]]

### 16.1.5 数据库连接

因为数据库是`全局`的，所以我们按照目录划分需要写在`app`中。首先要`npm i mysql2`，并且数据库的配置信息都要写在`.env`中，通过`dotenv`来读取操作

![[00 assets/df761840518ce20ecdfc7742bf8eb2ec_MD5.png]]

我们在封装好的`UserService`中进行数据的查询

![[00 assets/b02f007daf31b1193d45cca34b0bf9a1_MD5.png]]

### 16.1.6 错误判断

在路由跳转的时候执行中间件`verifyUser`对传输来的数据进行判断。然后在`error-handle.js`中对这个中间件的逻辑进行编写

![[00 assets/91cba583cb62a21d24a06c61db1e64cf_MD5.png]]

我们再来编写专门收集错误类型的`error-type.js`文件

![[00 assets/df060f8aa6df990676f6e026e6862157_MD5.png]]

我们再来编写专门处理错误类型的函数

![[00 assets/e245479310c01144e9b22bc5471f7930_MD5.png]]

我们再来编写该用户是否存在的代码，原理其实是一样的

![[00 assets/c8cb4e6cf2b22647100071dd8477dd6b_MD5.png]]

## 16.2 day02

### 16.2.1 密码加密

在对路由中输入的用户名和密码进行验证之后。再去对密码进行加密处理，密码最好不要明文存储

![[00 assets/337b073aff060a37a5af066f2aea8992_MD5.png]]

这个就是处理密码加密的代码，我们可以使用`Node.js`中内置的加密模块来处理

![[00 assets/110248b65f1687c78102b5212c0a044b_MD5.png]]

### 16.2.2 登录验证

这里有一个细节问题，不一定所有的功能都抽到`utils`中，有的时候抽出为中间件就可以

下面的整个流程就是这样的，按照上面的流程来书写就没问题

![[00 assets/2f2cde47ee118c9a7aa6762bfed620db_MD5.png]]

### 16.2.3 动态加载路由

我们在`index.js`文件中一直引入路由很麻烦，所以我们需要做出改进

![[00 assets/f8098468cddf6d131b35945dfbb0a65a_MD5.png]]

再在`router`文件夹下面编写加载路由的`.js`文件，用于动态加载路由。只要在该目录下的路由都会自动加载

![[00 assets/5e5083be33d49bb1a6f592631efc0435_MD5.png]]

因为传入的`app`是一个对象，所以我们使用他的中间件导入的路由会以内存地址的形式来存储，所以不会存在函数结束，数据都丢失的情况，也就达到了路由动态加载的效果。但是这只是一种猜测

### 16.2.4 登录凭证

#### 16.2.4.1 基本介绍

![[00 assets/6c4d8522f1b0bb7b909e47344099c957_MD5.png]]

#### 16.2.4.2 cookie

##### 16.2.4.2.1 基本介绍

对于`Cookie`有不同的划分，这个在以前的学习中确实不是很清楚。其中就划分了内存`Cookie`和硬盘`Cookie`

![[00 assets/f0ad0b2f9c27127609e9214f0da97b57_MD5.png]]

##### 16.2.4.2.2 常见属性

下面就是`Cookie`的常见属性

![[00 assets/9e2ca6d57dabd132de3c921fed543ad7_MD5.png]]

##### 16.2.4.2.3 客户端添加 Cookie

下面就是在客户端添加`Cookie`值

![[00 assets/80d45294c447222f44673a888ccca163_MD5.png]]

下面就是添加的`Cookie`值。注意这个`Cookie`是没有设置任何属性值的，所以他是内存`Cookie`，关闭浏览器就会自动清除这个`Cookie`，假如我们设置了过期时间的话就会转变为硬盘`Cookie`

![[00 assets/6ec7b4e8eb5397f446d5ed5878d4dedc_MD5.png]]

我们关闭浏览器，再次打开的时候你会发现`Cookie`消失了，这就是没有设置属性值的效果

![[00 assets/60c7656aceb3274b84fcaf1a29314064_MD5.png]]

当然我们也可以设置属性值`max-age`来将内存`Cookie`转变为存储`Cookie`，并且可以设置最大存储时间，到了时间之后，就会自动消失

![[00 assets/7ff26ac4b6f0b898dcdc9c6adaed5fa5_MD5.png]]

##### 16.2.4.2.4 服务端添加 Cookie

我们可以通过下面的方式来使用服务器来操作

```javascript
const koa = require("koa");
const app = new koa();

const KoaRouter = require("koa-router");
const router = new KoaRouter();

// 发送Cookie
router.get("/SetCookie", (context, next) => {
  // 通过 set 的方式来发送Cookie
  context.cookies.set("name", "zjh", {
    maxAge: 500 * 1000, // 设置Cookie的值，单位为毫秒
  });

  context.response.body = "Hello,Node.js!";
});

// 接收Cookie
router.get("/GetCookie", (context, next) => {
  // 通过 get 的方式来接收Cookie
  context.body = context.cookies.get("name");
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(8001, () => {
  console.log("正在监听");
});
```

![[00 assets/c22dcd51e39e68fd7ebe8ee5cf0f11e5_MD5.png]]

为什么后台可以获取到`Cookie`值，这是因为在网络请求中会自动携带上

![[00 assets/ddc13ee9456bc482ede2d87a700c0850_MD5.png]]

\*`cookie`存在一个`httponly属性`这个是指，只能使用`http`来设置。这样我们需要删除得话，就需要使用`name="";max-age:0;`就可以手动删除`cookie`了

#### 16.2.4.3 Session

假如你需要在`Koa`中使用`Session`的话，需要安装工具库

```bash
npm i koa-session // 安装koa-session
```

我们使用下面的方式来配置`Session`，向服务器发送`Session`数据并且保存，并且可以知道`Session`的本质就是`Cookie`

```javascript
const koa = require("koa");
const app = new koa();

const KoaSession = require("koa-session");

const KoaRouter = require("koa-router");
const router = new KoaRouter();

// 创建Session配置
const session = KoaSession(
  {
    key: "sessionid",
    maxAge: 500 * 1000,
    signed: false,
  },
  app
);
app.use(session);

router.get("/SetSession", (context, next) => {
  const name = "张三";
  const password = "zjh20011128";
  // 这里使用刚刚配置的session，并且对象的名称为user
  context.session.user = { name, password };

  context.body = "Hello";
});

router.get("/GetSession", (context, next) => {
  // 获取session的值
  context.body = context.session.user;
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(8001, () => {
  console.log("正在监听");
});
```

![[00 assets/93c1fb9ea36a1ccd7c4617f8cc2cfc8c_MD5.png]]

但是我们这样配置之后，假如有人修改`sessionid`里面的值不还是不行，所以我们需要设置`signed`的值为 true，现在默认就是 true。而且我们也可以通过`app.keys`的方式来加密内容

```javascript
// 创建Session配置
const session = KoaSession(
  {
    key: "sessionid",
    maxAge: 500 * 1000,
    // 是否使用加密的签名,现在默认为true
    signed: true,
  },
  app
);
app.keys = ["aaaaaa"]; // 加密的方式
app.use(session);
```

添加签名之后就会多一个`session.slg`的字段，这个就是加密的签名

![[00 assets/3ae947c53a0e811fdf65cd7540b6dac1_MD5.png]]

假如这个时候我们来修改其中的任何一个值，就会导致数据问题

![[00 assets/b847825dfcf5e281b647a0dfd4c3d48c_MD5.jpeg]]

#### 16.2.4.4 token

##### 16.2.4.4.1 基本介绍

在上面介绍的`Cookie`和`Session`其实不是很好

![[00 assets/cbf8642d293936d915fabbc4676078d3_MD5.png]]

这里缺点主要就是下面的 2 点，上面的问题都是可以解决的。第一个就是不能解决不同客户端的问题。

第二个就是不能解决服务器集群的问题，假如密文是通过`Session`是通过服务器 1 来加密的，但是`Nginx`是将该数据转发给服务器 2 了，这个时候服务器 2 并没有服务器 1 的密钥，所以数据根本解析不了。但是这些问题都是可以解决的，但是不是很好，所以就会出现 token

![[00 assets/6b87d8bddd19967d593838c33bab7268_MD5.png]]

这个时候就可以使用`token`来处理

![[00 assets/f56823971e93437ae941ce616b1abc6a_MD5.png]]

##### 16.2.4.4.2 JWT

![[00 assets/667c673efe0c4515ef986ad400709aac_MD5.png]]

这里需要注意一点，就是`jwt`是自带公钥的。所以所有人都可以解密`jwt`来获取信息，但是不能自己捏造`jwt`来传输，这个没用。`jwt.io`可以在没有公钥的情况下读取信息，但是不能修改

![[00 assets/58dbf62f2c25ec7a9c380deb11466066_MD5.png]]

也可以看下`JWT`的场景：[深入理解 JWT 的使用场景和优劣 (qq.com)](https://mp.weixin.qq.com/s?__biz=MzI0NzEyODIyOA==&mid=2247483918&idx=1&sn=12683bae55f2ab1a8281ab398472362f&chksm=e9b58bc5dec202d385d1c1d861f7e0ff495296ed9387b32a8d01ae195eae03688e5aeebe6396&token=1557545914&lang=zh_CN#rd)

##### 16.2.4.4.3 postman 鉴权

1、在`postman`中我们添加授权，这样每次的请求都会自动在`header`中加上`token`值。一般我们都会去使用`Bearer Token`的模式

![[00 assets/f363364082c28b0b42d4943b72507f90_MD5.png]]

2、如果我们想要自动保存`token`，还需要手动编写测试接口

![[00 assets/e903aa70d5cfdf90028d0ac0bad241fd_MD5.png]]

##### 16.2.4.4.3 基本使用

```bash
npm i jsonwebtoken // 安装工具库
```

下面就是创建一个`token`

```javascript
const koa = require("koa");
const app = new koa();

const KoaRouter = require("koa-router");
const router = new KoaRouter();

const jwt = require("jsonwebtoken"); // 使用jsonwebtoken来处理

const SERCET_KEY = "abc"; // 密钥

// 这里是模拟的登录情况
router.get("/Login", (context, next) => {
  // 用户登录发送token给用户
  const user = { id: 1, name: "zjh" };
  // 这里的expiresIn表示过期时间，单位为秒
  const token = jwt.sign(user, SERCET_KEY, { expiresIn: "100" });

  context.response.body = token;
});

router.get("/GetInfo", (context, next) => {
  // 解析出token值
  const token = context.header.authorization.replace("Bearer ", "");
  // 假如解析不到十直接报错的，所以需要try-catch来接住
  try {
    const result = jwt.verify(token, SERCET_KEY); // 通过密钥将token解密出来
    context.response.body = result;
  } catch (e) {
    context.response.body = "Token是无效的";
  }
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(8001, () => {
  console.log("正在监听");
});
```

下面就是获取到的`token`值

![[00 assets/6402172ad4714393f39834a325ab654c_MD5.png]]

当然在开发中不可能将`token`以数据的形式发送，一般都是直接加在`header`中，一起发送过来。所以我们可以借助`postman`来添加，这个参考`16.2.4.4.4 postman鉴权`，下面就是`token`解析出来的值了

![[00 assets/2b197f70a7f0c522be80fd09bcdb0d2c_MD5.png]]

##### 16.2.4.4.4 非对称加密

大致就是这样，持有`privateKey`的用户系统，可以颁发`token`。持有`publicKey`的可以验证`token`。这个就是非对称加密。

![[00 assets/c26c0ca4c25a3d85eee5f77bf74efb94_MD5.png]]

下面就是基本介绍

![[00 assets/4896b6dc20652a4eccbc2481fa84985a_MD5.png]]

我们也可以使用`SSL`来生成一个非对称加密，这里演示的是`windows`系统的`git`来生成的

![[00 assets/f80aea16285fe6893c58767158429e93_MD5.png]]

```bash
/* 先输入openssl */
openssl
/*
	1.genrsa 表示生成
	2.-out表示输出为文件
	3.private.key表示生成私钥的名字
	4.2024表示生成私钥的长度
*/
genrsa -out private.key 2024

/*
	1.-in private.key表示按照私钥private.key来
	2.-pubout表示生成公钥
	3.-out public.key表示向外输出公钥
*/
rsa -in private.key -pubout -out public.key
```

这个时候我们就可以生成私钥和公钥

![[00 assets/2866a98ee5a305b0ae51cde1a8d05ccb_MD5.png]]

##### 16.2.4.4.5 非对称加密基本使用

我们在`Node.js`中去使用

```javascript
const koa = require("koa");
const app = new koa();

const KoaRouter = require("koa-router");
const router = new KoaRouter();

const fs = require("fs");

const jwt = require("jsonwebtoken");

const PRIVATE_KEY = fs.readFileSync("./keys/private.key"); // 密钥
const PUBLIC_KEY = fs.readFileSync("./keys/public.key"); // 公钥

// 这里是模拟的登录情况
router.get("/Login", (context, next) => {
  // 用户登录发送token给用户
  const user = { id: 1, name: "zjh" };
  // 注意这里和上面的区别，这里就是使用非对称加密的私钥
  const token = jwt.sign(user, PRIVATE_KEY, {
    expiresIn: 100, // 这里的expiresIn表示过期时间，单位为秒
    algorithm: "RS256", // 采用的加密方法
  });

  context.response.body = token;
});

router.get("/GetInfo", (context, next) => {
  const token = context.header.authorization.replace("Bearer ", "");

  try {
    const result = jwt.verify(token, PUBLIC_KEY, {
      algorithms: ["RS256"], // 可传入多个数据
    });
    context.response.body = result;
  } catch (e) {
    context.response.body = "Token是无效的";
  }
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(8001, () => {
  console.log("正在监听");
});
```

我们将通过私钥加密之后信息读取出来，注意上面。在加密传递给客户端的时候，使用的私钥加密，但是需要读取信息的时候，就是使用的公钥来解密的

![[00 assets/62d287932dc57bf03b1130fef0e7ba99_MD5.png]]

这个时候就会好奇，假如我们加密的时候使用公钥的话，能成功加密吗？答案是否定的，公钥是不能颁发`Token`的，所以我们使用公钥去加密的话会报错

![[00 assets/3bc7e44630f0f5e8137e68e1f3d099d0_MD5.png]]

假如别人不知道我们的私钥，他就不能颁发`Token`。虽然他能获取到公钥，他也只能解析出信息，但是不能伪造`token`来调用接口

#### 16.2.4.5 项目登录凭证

基本操作和上面是一样的，假如是简化步骤的话，可以查看上面的介绍

首先是来加密信息，发给前端来保存

![[00 assets/e3790d102717cf7b57f823962f820965_MD5.png]]

然后我们对发送来的`token`进行解密

![[00 assets/466c88c4b2ce84e10b7968b88805887e_MD5.png]]

MDN 响应状态码：[HTTP 响应状态码 - HTTP | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)

这里还有一个对于`postman`的操作，可以自动化设置`token`值，不必我们每次都添加。在服务器发送给客户端的接口里面写上这一段，就可以自动获取`token`到全局

![[00 assets/2ac009865815a9582c0137c11b2313fc_MD5.png]]

这里就会自动填充

![[00 assets/a2c716df279fcd3c4b131092eb36e440_MD5.png]]

这里还需要注意一个`fs`读取的问题，因为我们使用的`npm`来执行的。本质就是将我们写的代码都存在`main.js`来执行，所以这个读取文件也需要修改，应该是按照`main.js`为基础来编写路径的，但是又可能搞混，这里直接就是`path`来拼接了

![[00 assets/95b48af00116373c4feefdd7e1cdcaf9_MD5.png]]

### 16.2.5 查看动态

这个项目本身就是一个发表动态的论坛，所以我们需要搭建一个可以查看动态的接口。其基本的思想和上面的类似，首先编写接口，然后再来编写中间件。下面只是阐述写这些东西获取到的经验

> 1.

首先来看路由的特点，`post`的请求方式就是添加，下面的 2 条`get`请求就是查询，不做修改。这个就是`restful`风格的接口模式

![[00 assets/cb2c712f15a56469f3527edecc075e7d_MD5.png]]

> 2.

这个就是编写一般接口的逻辑，首先增加中间件来对数据进行判断。然后在`Controller`中添加创建的方法

![[00 assets/061f9b34cb18286c0a4e6d973f62d3d2_MD5.png]]

再将对执行`sql`执行放在`service`中

![[00 assets/070cd2af3f0e56ae64f5876637b6e3fa_MD5.png]]

最后返回数值

> 3.

这个就是通过数据库表中的`user_id`到用户表中查询到的数据

![[00 assets/a3b25403413c81ac21f1f5e217516dbe_MD5.png]]

在返回的时候就需要按照这种格式来返回

![[00 assets/d063d79c671d74f081177aa75821a1d0_MD5.png]]

这里的查询格式为左连接来查询到改动态下面的用户，并且使用了`JSON_OBJECT`将其转化为对象格式

![[00 assets/507c8286095d1b482efb205fe2d28dfc_MD5.png]]

并且这里还有一个思想，就是这个`sql`很长，所以我们可以抽取出来复用

## 16.3 day03

### 16.3.1 修改文章

这里就不去阐述了，大致步骤也和上面差不多的

但是这里有一个抛出异常的问题。我们在这里执行语句，假如出现错误的话，因为我们没有使用`try-catch`包裹，所以这里抛出的异常会抛出给上一个函数，假如上一个函数也没有处理的话，又会抛出。

![[00 assets/0b5dc1ed18027b218ca0dfad7dad083d_MD5.png]]

所以为了代码的健壮性，我们应该为这些函数包裹`try-catch`。一般的处理时包裹`sql`处理语句

![[00 assets/cfda65ce44aa1bc6e0de7b7a565fb895_MD5.png]]

### 16.3.2 删除文章

操作基本和修改文章一样。

这里有一个点就是**业务接口和后台管理接口**的区别，后台管理接口的开发更加复杂，而且他们是不同系统的开发不能混杂在一起

### 16.3.3 发表评论

这里重点就是创建数据库。

1.首先评论是依附于文章的，所以需要添加`文章id`。

2.并且设置外键的时候带上`cascade`会很方便，这样每次这个数据表就会跟着外键表数据改变。

3.并且这里还有一个`comment_id`设置外键为自己的这个表。这样就可以体现出不同的层级

![[00 assets/b2c5d6ed7761189ba926ff326175cc39_MD5.png]]

### 16.3.4 回复评论

按照上面的数据库解释，这里回复也是存在一个表中。这个表示回复`id`为 2 的评论值

![[00 assets/192f4301e2b80df3c4352978faadaec4_MD5.png]]

这个就是评论回复的数据库思路。其实里面的业务代码很简单，按照流程来处理即可

### 16.3.5 修改评论

注意这里的使用。因为他们验证权限很类似（只需要修改查询的`sql`和获取到`params`值），而且代码可以复用，但是验证权限需要知道他们的区别。

![[00 assets/427cda34ed8e81c45c4b6f90a644de0f_MD5.png]]

所以这里就有 2 个思路

> 1.对`verifyPermission`作高阶函数处理，对其进行闭包

将要处理的函数作为返回值处理，并且将高阶函数的参数作为区分。这也就可以动态调节里面值得变化了。也让这个`verifyPermission`得职能就扩大了

![[00 assets/b0cf89f61832270e4eb6821384fd113f_MD5.png]]

然后将验证是否存在得`sql`进行修改，这样就可以动态修改

![[00 assets/f42e68b7e9a0469719c23913397e70e5_MD5.png]]

这段得使用在我得笔记`JS高级`里面也有，可以参考

> 2.如果后续的接口都是按照`restful`风格来编写得话。可以直接获取`params`得参数的键来区分。

![[00 assets/a714b53ed56dc3527b7991ddb412b4ee_MD5.png]]

### 16.3.6 删除评论

和上面类似

> 1.编写路由

![[00 assets/b8089c1e940616dfa970bc2d1b5081ae_MD5.png]]

> 2.编写 Controller

![[00 assets/c69b7e1e6f64f2aefadcfdc0b29215c2_MD5.png]]

> 3.编写 sql 执行

![[00 assets/3f92b238a980dfbb65ff85f717ee9d8e_MD5.png]]

完成，基本这就是编写业务代码的全部。后面的非特殊处理，基本都是这个套路

## 16.4 day04

### 16.4.1 获取评论的个数

我们在这里加上一个子查询即可，这样就可以查询到个数

![[00 assets/61bfdc6cfa8f6f6a95fc24cd1c58f502_MD5.png]]

只要`moment_id`是一样的，就可以链接到`moment`表查询到该动态的评论个数

![[00 assets/59b5d7193796951561f1a873a8908986_MD5.png]]

### 16.4.2 获取评论

> 方案一

将获取评论的接口和获取动态的接口分离来处理。这样直接获取`moment_id`即可

![[00 assets/83d303df102808824c811856eb520b63_MD5.png]]

> 方案二

在获取动态的时候，顺便获取该动态下面的评论，这里的难点主要是`sql语句`的编写。假如对于`sql`语句实在不知道怎么编写的话，可以参考下面的思路

![[00 assets/4b63c74466776cc6328b70577b2f191d_MD5.png]]

### 16.4.3 标签开发

1.因为`标签`和`帖子`是多对多的关系，在`mysql`课中学过，多对多最好的处理方式就是建立中间表，即这里创建`moment_label`表来作为中间表

![[00 assets/bf5f7f825a7a6af6497be831d9d52f76_MD5.png]]

2.这里还有一个联合主键的概念。这个和普通主键是一样的，这里可以将他们 2 个字段连在一体作为主键来处理

**参考文章**：[联合主键有什么用？ - UniqueColor - 博客园 (cnblogs.com)](https://www.cnblogs.com/UniqueColor/p/7234340.html#:~:text=联合 主键 就是用 2 个或 2 个以上的字段组成 主键 。 用这个 主键 包含的字段作为主键，这个组合在,数据表 中是唯一，且加了主键索引。 那么这时单独使用订单号就不可以了，因为会有重复。 那么你可以再使用个订单 序列号 bill_seq 来 作为区别。 把 bill_no 和 bill_seq 设成联合主键。)

比如：`moment_id和label_id`分别是：(1,1)，(1,2)...这个就表示的是一个帖子包含 2 个标签，这个时候就会问，为什么`moment_id`是一样的，这里只需要(`moment_id`，`label_id`)的排列不一样就可以了

3.这里再来解释一下`on update cascade...`的使用，其实就是下面的图，只要`buildings`表更新或者删除，就更新和删除下面的`rooms`表。类比到这里就是，只要`label`表或者`moment`表更新或者删除就会影响`label_moment`表中的数据，这样做的好处就是方便更新数据，不需要你手动来维护了

![[00 assets/74358590b5a76ac44f15e79e8f7ed553_MD5.png]]

4.所以这里的标签开发。首先是分析数据模式，这个功能的模式就是`多对多`，一个文章可以使用多个标签，多个文章可以复用多个标签。然后就是构建数据库，是多对多所以需要设置`中间表`。并且构建外键的时候也是一样的，当更新和删除需要更新和删除，所以需要将中间表的外键的`on update 和 on delete`设置为`cascade`

### 16.4.4 动态添加标签

动态添加标签逻辑就是，用户的权限是：**登录**，**文章是自己的**。

剩下的就是后台关心的事情，假如用户添加的标签，数据库中不存在的话，就会自动添加到数据库中。并且该文章没有有该标签的话，就会自动与标签建立联系，假如有的话就会跳过

![[00 assets/579b0c0813e7c87bde0287af45375952_MD5.png]]

剩下的逻辑就很简单了，大致逻辑就是如此

![[00 assets/305f02ee9620bd9c6cc19695b3e92a94_MD5.png]]

### 16.4.5 动态显示标签

> 方式一

可以参考`16.4.2`的编写方式

![[00 assets/c136c1894a20cae75d7b97b078c675f7_MD5.png]]

> 方式二

单独再来写一个接口，或者数据库查询的方式。来单独处理，这个也是我比较推荐的方式。下面的方式和`16.4.2`又不一样，下面的是将各个步骤写为单独的方式。但是`16.4.2`是写一个`sql`直接处理完返回

![[00 assets/e70993c31402a71254ae80f4ad1e7e4b_MD5.png]]

## 16.5 day05

### 16.5.1 头像上传

首先来编写上传图像的中间件

![[00 assets/773731407dfdd8409967fd30e6eec4e3_MD5.png]]

这中间的逻辑在`13.4.4`里面有讲，这里有一个`storage`的小坑需要注意一下

![[00 assets/3dd51c52b8490ff6db7c1bdb842b110c_MD5.png]]

然后再保存到数据库中即可

![[00 assets/3bdac696efc0aec8db40bb3f57e94017_MD5.png]]

### 16.5.2 头像查看

1.注意这里的一个小细节，为什么不直接获取头像的路径然后直接保存到数据库呢？这个其实理解起来很简单，因为我们直接将该路径存储，假如后期需要更换路径的话就会很麻烦，因为这些都是写死的，所以直接获取文件名，到时候拼接路径即可

2.当我们从数据库中查询到头像数据之后，可以创建流来传输给服务器

![[00 assets/3b06af5ca16cf11585d168ebe9cc15ac_MD5.png]]

但是这种形式浏览器并不知道是什么文件，所以默认是直接下载处理的

![[00 assets/0ac4f487c823b14e3ea56867b6b92373_MD5.png]]

3.假如我们需要让浏览器知道这是一个图片，就需要设置`Content-Type`来传输了，这个时候就是直接显示的图片

![[00 assets/71ba73eb160d01889df2f713cf8b6c83_MD5.png]]

4.当然这里还有一个细节就是变量都抽出来作为常量，后续只需要修改这一处就可以了

![[00 assets/6b26d6106ce72f5ee8bf5fea382f606c_MD5.png]]

### 16.5.3 用户头像

当添加头像数据之后，去更新用户的头像数据，这里可以直接拼接获取，也最好做成拼接获取即可

![[00 assets/cd761dd7ead0c252b22e067697bf63b9_MD5.png]]

下面就是数据库中的存放的数据模式

![[00 assets/0e13568c7e3f0000ae15427461714886_MD5.png]]

### 16.5.4 动态配图

其实头像配图的逻辑已经完成了，动态配图就很简单了。就是一个单独的，一个多个的处理方式。但是还是有逻辑的区别的。这里建议使用文件名来查询

### 16.5.5 图片压缩

```bash
npm i jump // 使用工具库
```

下面就是基本的使用，这里将图片压缩为`1280`、`640`、`320`的格式

![[00 assets/49d7e2c95a1060f3f13ae2ee555bc521_MD5.png]]

# 18. 云服务器部署

## 17.1 基本介绍

下面的介绍为`CentOS 8.2`，因为该版本有`dnf`对于安装包更加方便

我们不仅仅可以使用`XShell`来连接`linux`服务器。我们也可以使用`git bash`来连接`linux`服务器

![[00 assets/8526f84196c033cd73734147e6bde87e_MD5.png]]

当然我们这里使用`XSehll`来连接

![[00 assets/d479ef0f4417eea77a0e3e081460ab99_MD5.png]]

## 17.2 Node.js

因为服务器选择是`8.2`，所以是自带`dnf`的，下面可以使用`dnf --help`来查看该版本是否安装过`dnf`

![[00 assets/bac8d933cbe917d1763f50bf0bec8812_MD5.png]]

1.首先来搜索是否包含`Node.js`的包，可以使用命令`den search dnf`。很明显假如要安装的话，就安装下面的`Nodejs.x84_64`的版本

![[00 assets/bc1e19951bc7741fed5bafe978f76afc_MD5.png]]

2.当然我们也可以通过`dnf info nodejs`来查看你要下载的`node.js`的信息

![[00 assets/6b47ff68ce707eebcb31b131c400e433_MD5.png]]

3.通过下面的命令可以下载到`Node.js`

```bash
# 安装node.js
dnf install nodejs
```

但是下载的并不是`nodejs`的最新版本，而是比较老的

![[00 assets/e2f85a69f1c7a1b69571ad36b1400687_MD5.png]]

4.所以我们可以去更新`nodejs`的版本

```bash
# 安装n，用于切换nodejs的版本
npm install n -g

# 通过n来安装nodejs的最新的lts和current版本
n install lts # 安装lts版本
n install latest # 安装current版本

# 通过n来切换nodejs的版本
n
```

这里我们选择`lts`的最新版本

![[00 assets/a07abd8122d5e896125c064f9108a6cd_MD5.png]]

✨ 如果使用`n`来切换`nodejs`的版本之后`服务器`没有反应的话

1.解决方法一：通过`SSH`来建立连接

2.解决方法二：重启`ssh service sshd restart`

1、如果使用 CentOS7 的版本，可能会有很多的依赖库不存在，下面就是解决依赖库的问题

[node: /lib64/libm.so.6: version `GLIBC_2.27' not found - 丁少华 - 博客园 (cnblogs.com)](https://www.cnblogs.com/dingshaohua/p/17103654.html)

![[00 assets/985c116a1409974dea892fc2dacd7292_MD5.png]]

2、因为 CentOS7 版本比较低，所以很多的功能都没有，需要一个个安装依赖库太麻烦了，可以直接使用二进制包来处理

[如何部署 Node.js 环境\_云服务器 ECS-阿里云帮助中心 (aliyun.com)](https://help.aliyun.com/zh/ecs/use-cases/deploy-a-node-js-environment-on-a-centos-7-instance#2c8bcdf02116b)

因为使用阿里云给的方式可以安装，因为是软链接设置了，没有环境变量，所以使用下面的方式可以设置环境变量，这样就可以全局使用`pm2`和`n`类似的工具库了

![[00 assets/1e939c7feb3f7cf08394d6577f14d6fc_MD5.png]]

[解决 linux 中使用 npm 全局安装的命令无法运行-CSDN 博客](https://blog.csdn.net/weixin_44509607/article/details/103083280)

## 17.3 MySql

### 17.3.1 安装 mysql

下载`mysql-server`

```bash
# 查看mysql的包
dnf search mysql-server

# 查看mysql的信息
dnf info mysql-server

# 安装mysql
dnf install mysql-server -y
```

启动`mysql-server`

```bash
# 开启mysql的后台服务
systemctl start mysqld

# 查看mysql服务：active(running)表示启动成功
systemctl status mysqld

# 随着系统一起启动
systemctl enable mysqld
```

配置`mysql`

```bash
mysql_secure_installation

# 这个时配置mysql的密码，基本上都选择y即可，
# 但是mysql8的密码需要比较强的，这里我设置的就是zjh20011128.
```

使用`mysql`

```bash
mysql -u root -p	# 后面输入密码即可
```

### 17.3.2 连接 mysql

1.这里我们使用`navicat`来连接数据库，点击连接。其中主机就是你的服务器的`ip地址`。

![[00 assets/9de1b3d4eda6735327a731a27713ace0_MD5.png]]

2.但是我们这样填写之后肯定是连接不上的，因为我们服务器的`3306`端口并没有开启。这个时候就需要添加规则来开放`3306`端口

![[00 assets/c85e6e1edf008a0b07468626abfda720_MD5.png]]

3.这之后还是不能连接，我们可以查看`msql`中的`user`表。可以发现`root`用户名的`host`是`localhost`，所以连接不上

![[00 assets/e9a1161aa1949a8bf5fd984b998a1b5a_MD5.png]]

我们需要去修改`root`的`host`为`%`，这里就需要使用到`mysql`的`update`，`update user set host = "%" where user = "root";`

![[00 assets/665878eaba252f7e2a6d74b092d77096_MD5.png]]

4.假如还是连接不上的，就需要清除缓存了。输入下面的指令来重新授权，`flush privileges;`

![[00 assets/a273ee2410fcdf87b6127dc6f1b5081a_MD5.png]]

你安装`mysql`可能存在密码一直错误的情况，不要信网上的修改`authentication_string`，这个是凭证信息，修改也没用，最多置空就行，可以参考下面的文章来配置

[MySQL8.0 正确修改密码的姿势[通俗易懂\]-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/2115190)

### 17.3.3 mysql 迁移

我们将在本地建立好的`mysql`转储为`sql`文件

![[00 assets/6ecf8581879533d22f4e904d9c0b1620_MD5.png]]

可以看到这里有运行`sql文件`，直接将刚刚保存的`sql`文件运行即可

![[00 assets/6e4f36f2d6f1bba74b5550c3329d3b41_MD5.png]]

## 17.4 手动部署

### 17.4.1 简单部署

使用`xftp`将`nodejs`的文件丢到服务器执行即可

![[00 assets/256d7b24979be4f88db1b3f9373b87bd_MD5.png]]

### 17.4.2 git 部署

#### 17.4.2.1 git 上传

1.首先将代码都上传到`github`中，现在已经上传完成

![[00 assets/35909a0d2b957c55428420111e97c645_MD5.png]]

2.这个时候服务器是没有安装`git`的，所以我们需要安装`git`

```bash
# 安装git
dnf search git
dnf info git
dnf intall git
```

这个时候输入下面的指令就可以`clone`项目到本地了

![[00 assets/3c0f335926231b95b29837f1d8507f0a_MD5.png]]

这个时候我们就可以看到下面已经被`clone`的文件了

![[00 assets/a407d0add32869efc329390a4a197ade_MD5.png]]

#### 17.4.2.2 vscode 连接 ssh

但是没有**依赖包(node_modules)**，这个时候我们可以直接在服务器里面`npm install`就可以了，但是这样并不是很高效，也不是很直观，所以这里可以直接使用`vscode`来编辑`linux`里面的文件

我们来下载`remote-ssh`来进行`ssh`的连接

![[00 assets/b04fd92d94ef97e5176c41f045a84d48_MD5.png]]

这个时候我们输入上面的命令就可以连接了

![[00 assets/545b6c4a24f31215b438b3d17ac0a791_MD5.png]]

这里可以看到已经连接上远程了，选择你要展示的文件夹即可

![[00 assets/ee799543d5f6a58857cd20b529512ce4_MD5.png]]

这个时候就可以看到已经完成了

![[00 assets/a835fd2dcf374cdaeed5254aa6671e0f_MD5.png]]

#### 17.4.2.3 执行

这个时候我们再来`npm install`就可以在`vscode`中进行安装

![[00 assets/20f851583b86dcfc7749516a2f207634_MD5.png]]

我们再来执行即可（假如报错的话要注意有没有安装`nodemon`），这样就可以开启服务器版本的`nodejs`

![[00 assets/fdc5ee1ccc64b6f6338224f295a987f0_MD5.png]]

✨ 注意：这里我开启的端口是`8000`，但是该服务器的并没有开启端口`8000`，所以我们需要到控制台来开启

![[00 assets/f340fd9ee8d00891755443b37f2ef3fa_MD5.png]]

还有一个问题就是我们使用`vscode`使用插件通过`ssh`来启动的`nodejs`，这就意味着只要本机的`vscode`关闭，服务器的`nodejs`的服务也会关闭

### 17.4.3 pm2 启动

这是一个`node`进程的管理器，我们可以使用它来管理`node`的进程。这样我们关闭本机的`vscode`的进程就不会影响服务器端了

```bash
# 安装pm2
npm install pm2 -g
```

下面就是`pm2`的常见进程

```bash
#命名进程
pm2 start app.js --name my-api
#显示所有进程状态
pm2 list
#停止指定的进程
pm2 stop 0
#停止所有进程
pm2 stop all
#重启所有进程
pm2 restart all
#重启指定的进程
pm2 restart 0
#杀死指定的进程
pm2 delete 0
#杀死全部进程
pm2 delete all
#后台运行pm2,启动4个app.js,实现负截均衡
pm2 start app.js -i 4
```

我们使用下面的命令来持久开启`nodejs`的进程

![[00 assets/cf02796870f1fee0e7d3e0fd5129e7f6_MD5.png]]

## 17.5 自动部署

### 17.5.1 安装 Java

我们需要使用`Jenkins`来进行自动化部署，其实`Jenkins`的运行机制就是本地写完代码`push`到`git`上，然后到了一个时间就自动获取`git`的最新版本，然后再`npm i`添加最新的包，然后重新`pm2`

![[00 assets/06f26b064b4634bf9f83f0ee5ca5147c_MD5.png]]

我们使用下面的方式来安装`java`

```bash
dnf search java1.8
dnf install java-1.8.0-openjdk.x86_64
```

### 17.5.2 安装 Jenkins

因为`Jenkins`本身没有在`dnf`的软件仓库包中，所以我们需要连接`Jenkins`仓库

> 方式一

参考文档：[(89 条消息) linux 安装配置 jenkins\_舌尖上的蛋炒饭的博客-CSDN 博客](https://blog.csdn.net/qq13933506749/article/details/120493388)

> 方式二

或者使用下面的方式

```bash
wget -o /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo

# 导入GPC密钥确保软件的合法
rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
```

![[00 assets/c2ac0a5ea46cdc1f51b2cc02e4b036d4_MD5.png]]

### 17.5.3 使用

参考网上的文章，这里就不去赘述了

# 其他

## 1. pm2

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7236156810393043005)

### 1.1 基本介绍

1、前面我们都是 node 直接跑的 Nest 应用，但生产环境我们不会直接跑 node，而会用 pm2 来跑。

2、如果你的 node 应用跑的时候突然抛了个错，崩溃了，是不是需要重新跑起来？这时候是不是就需要另一个进程来自动做重启这件事情？

3、node 应用的日志默认输出在控制台，如果想输出到不同的日志文件，是不是可以让另一个进程获取 node 应用的输出，然后写文件来实现？

4、node 是单线程的，而机器是多个 cpu 的，为了充分利用 cpu 的能力，我们会用多个进程来跑 node 应用，这种通用逻辑是不是也可以放到一个单独进程里来实现？

5、node 运行时的 cpu、内存等资源的占用，是不是需要监控？这时候是不是可以让另一个进程来做？线上的 node 应用不只是跑起来就行了，还要做自动重启、日志、多进程、监控这些事情。

6、而这些事情，都可以用 pm2 来做。pm2 是 process manager，进程管理，它是第二个大版本，和前一个版本差异很大，所以叫 pm2.pm2 的主要功能就是**进程管理、日志管理、负载均衡、性能监控**这些。

### 1.2 基本使用

```bash
pm2 start xxx --max-memory-restart 200M			# 超过 200M 内存自动重启
pm2 start xxx --max-memory-restart 1K			# 指定 1k 内存就重启
pm2 start xxx --cron-restart "2/3 * * * * *"	# 从 2s 开始每 3s 重启一次
pm2 start xxx --watch							# 当文件内容改变自动重启
pm2 start xxx --no-autorestart					# 不自动重启
pm2 delete 0									# pm2 删除
```

### 1.3 日志管理

1、输入`pm2 logs`可以查看日志，并且`pm2`会将日志文件保存到下面对的路径中方便查找，也可以`pm2 logs 进程名 / 进程id`来针对进程进行查找

![[00 assets/4f5888850262dca27272f2029cdee168_MD5.png]]

2、使用 `pm2 flush` 或者 `pm2 flush 进程名|id`来清空日志

3、查看 `main` 进程的前 100 行日志：`pm2 logs main --lines 100 `

### 1.4 负载均衡

1、再就是负载均衡，`node` 应用是单进程的，而为了充分利用多核 cpu，我们会使用多进程来提高性能。`node` 提供的 `cluster 模块`就是做这个的，`pm2` 就是基于这个实现了负载均衡。我们只要启动进程的时候加上 `-i num` 就是启动 `num` 个进程做负载均衡的意思。

2、当然主要是下面的几个功能

```bash
pm2 start app.js -i max 			# 开启本机最多的进程执行
pm2 start app.js -i 2				# 开启2个进程来执行
pm2 scale main 3					# 动态扩展到3个
pm2 scale main +3					# 动态添加3个
```

### 1.5 查看监控

1、使用`pm2 monit`，可以查看监控，可以看到不同进程的 cpu 和内存占用情况

![[00 assets/5b4641ebea34ee68e82c3323db8e56c2_MD5.png]]

### 1.6 配置文件启动

1、输入`pm2 ecosystem`会创建一个配置文件，`apps` 部分就是配置应用的，`scripts` 就是应用的启动路径

2、剩下直接查看配置信息即可

3、使用`pm2 start ecosystem.config.js`，可以批量执行脚本

![[00 assets/0a67d8a91835d230847eaff034e8bffb_MD5.png]]

### 1.7 docker 启动 pm2

1、有同学说，不都是 docker 部署了么？还需要 `pm2` 么？当然需要了，万一 docker 容器内 node 服务崩溃了，是不是需要重启？docker 容器内的进程同样有日志管理、进程管理和监控的需求。一般都是 docker 镜像内安装 pm2 来跑 node

2、这一段内容可以看`docker`的笔记，一般只是添加一个`pm2`的依赖，并且使用`pm2`来跑项目即可

```dockerfile
# 构建环境（开发环境）
FROM node:18 as build-stage

WORKDIR /app

COPY ./package.json .

RUN npm config set registry https://registry.npmmirror.com/

RUN npm i

COPY . .

RUN npm run build

# 生产环境
FROM node:18 as production-stage

WORKDIR /app

COPY --from=build-stage /app/dist .
COPY --from=build-stage /app/package.json ./package.json

RUN npm config set registry https://registry.npmmirror.com/

RUN npm install --production

RUN npm install pm2 -g

EXPOSE 3000

CMD [ "pm2-runtime", "./main.js" ]
```
