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

![image-20220806231837433](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324871.png)

`V8引擎`中`浏览器`和`Node.js`的的关系

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324901.png" alt="image-20220831092825273" style="zoom:80%;" />

所以它**不具有浏览器提供的 DOM API**，比如 Window 对象、Location 对象、Document 对象、HTMLElement 对象、Cookie 对象等等。但是，Node.js 提供了自己特有的 API，比如全局的 global 对象，也提供了当前进程信息的 Process 对象，操作文件的 fs 模块，以及创建 Web 服务的 http 模块等等。这些 API 能够让我们使用 JavaScript 操作计算机，所以我们可以用 Node.js 平台开发 web 服务器。

![[00 assets/ab671e7d69782709646925e0035a124f_MD5.png]]

下面就是`node.js`的另外一种原理图片，我们可以知道在**中间层**支持**事件循环队列**

![image-20220820181731620](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324904.png)

下面是 Node.js 的基本架构，我们可以看到，Node.js 是运行在操作系统之上的，它底层由 V8 JavaScript 引擎，以及一些 C/C++ 写的库构成，包括 libUV 库、c-ares、llhttp/http-parser、open-ssl、zlib 等等。

其中，libUV 负责处理事件循环，c-ares、llhttp/http-parser、open-ssl、zlib 等库提供 DNS 解析、HTTP 协议、HTTPS 和文件压缩等功能。

在这些模块的上一层是中间层，中间层包括`Node.js Bindings`、`Node.js Standard Library`以及`C/C++ AddOns`。`Node.js Bindings`层的作用是将底层那些用 C/C++ 写的库接口暴露给 JS 环境，而`Node.js Standard Library`是 Node.js 本身的核心模块。至于`C/C++ AddOns`，它可以让用户自己的 C/C++ 模块通过桥接的方式提供给`Node.js`。

中间层之上就是 Node.js 的 API 层了，我们使用 Node.js 开发应用，主要是使用 Node.js 的 API 层，所以 Node.js 的应用最终就运行在 Node.js 的 API 层之上。

![image-20220831095734746](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324911.png)

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

![image-20220820182358095](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324922.png)

## 1.2 安装

> Node.js 安装

Node.js 官方文档：[Node.js (nodejs.org)](https://nodejs.org/en/)

Node.js 中文文档：[Node.js 中文网 (nodejs.cn)](http://nodejs.cn/)

> Node 版本

如果需要安装多个`Node.js`的话，需要`nvm(Node version manager)`或者`n`来管理`Node`版本，但是不支持**windows**

这里只是指一条路，假如需要一个计算机同时要安装多个版本的可以参考这个工具

## 1.3 使用

![image-20220807213714597](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324661.png)

## 1.4 REPL

**REPL**是**Read-Eval-Print Loop**的简称，翻译为**"读取-求值-输出”循环**。REPL 是一个简单的、交互式的编程环境。其实浏览器的`console`就是一个基本的`REPL`

![image-20220820195430924](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324679.png)

下面就是`Node`的`REPL`的环境

![image-20220820195721706](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324696.png)

在`Node`的`REPL`也支持多行函数语句

![image-20220820212212954](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324713.png)

`Node`其实也有`浏览器`差不多的`window`对象，它就是`global`。但是`process`也是属于一种全局变量

![image-20220820211707694](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324731.png)

## 1.5 全局对象

### 1.5.1 特殊的全局对象

![image-20220820215720174](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324764.png)

其中`__dirname`、`__filename`可以查看我下面的笔记

#### 1.5.1.1 __dirname

1、用于获取当前执行`js`文件的绝对路径
![image-20220807222531697](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324252.png)

2、为什么可以拿到 `__dirname` 本质是因为 NodeJS 是一个函数的环境 `function(xxx)` 那么可以直接拿到 `__dirname` ，如果你在 NodeJS 中使用 ESM 模块，就没有 `__dirname`，那么我们想使用 `__dirname` 该怎么做呢？
![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202503072209040.png)

#### 1.5.1.2 \_\_filename

这个和上面的`__dirname`的区别就是，就是这个全局对象是带有文件，但是上面的只能到文件夹

![image-20220820220237645](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324277.png)

`__dirname`和`__filename`就是一种**特殊的全局变量**，算是全局变量。但是只能在模块中使用，并且控制台打印也是没有的

![image-20220820220655498](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324305.png)

### 1.5.2 常见的全局对象

![image-20220820222137555](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324353.png)

#### 1.5.2.1 process

我们在`node`的时候可以给运行环境传递参数

![image-20220820213543865](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324377.png)

下面是关于`argv`的解释，`vetor`这种数据结构在`Java`集合里面提到过

![image-20220820213901902](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324430.png)

\*`process.platform`可以获取电脑的平台

#### 1.5.2.2 console

其实最基本的就是`console.log()`可以在控制台打印数据。假如我们需要清除控制台的话就需要使用到`console.clear()`，我们直接在控制台打`cls`也是可以的

这里有一个特别的数据，可以追溯调用栈，他就是`console.trace()`

![image-20220820214754487](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324975.png)

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

![image-20220820222304585](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324015.png)

当然还有`clearSetTimeout`...等可以去清除定时器

#### 1.5.2.4 global

![image-20220820222454134](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324053.png)

但是上面并不是`global`所有的内容，我们需要进入到`REPL`中，输入`global. + tab + tab`就可以去查看`global`所有的内容。

![image-20220820222711404](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324081.png)

`global全局变量`和浏览器中的`window`有点像，但是并不完全像，我们可以看下面的例子

![image-20220820223615140](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324109.png)

你放在`Node`中是不行的

![image-20220820224501438](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324721.png)

这是因为**window**本身是不分模块的，所以数据可以访问到。但是**node**是分模块的，假如你设置了一个变量，这样就干扰了各个模块的变量名

下面就是`node`源码，它是通过`ObjectDefineProperty()`来对`global.process`中进行双向绑定

![image-20220820225106791](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324744.png)

不是很清楚为什么进入到`node`的`REPL`的时候就可以去运行，并且可以查找到数据

![image-20220820224630505](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324768.png)

## 1.6 版本切换

1、`nvm-window`用于`window`系统中`Node.js`的版本切换：[coreybutler/nvm-windows: A node.js version management utility for Windows. Ironically written in Go. (github.com)](https://github.com/coreybutler/nvm-windows)

![image-20230219220324229](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324811.png)

2、注意我们安装`nvm`的时候不能出现中文路径。下面就是基本使用

![image-20230219220511600](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324834.png)

3、我们也可以使用`n`工具来切换`nodejs`的版本

![image-20230219220715970](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324891.png)

## 1.7 输入输出

![image-20230219221100390](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324358.png)

1、一般情况下我们是不会主动转入参数

![image-20230219221046137](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324385.png)

2、`argv`的名字由来

![image-20230219221224204](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324410.png)

# 2. fs

## 2.1 基本介绍

假如你使用的`vscode`没有语法提示的话，可以安装下面的插件

```cmd
npm install --save-dev @types/node
```

在`Node.js`中`fs`模块很重要

![image-20220823091940062](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324438.png)

在 API 中大多数都提供了这三种操作方式

![image-20220823092246990](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324461.png)

我们也可以使用下面的代码来查看`Node.js`有那些模块

![image-20220902130116634](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324523.png)

## 2.2 读取文件信息

> 1.同步操作

```javascript
const fs = require("fs");

const filepath = "./abc.txt";

const info = fs.statSync(filepath); // 执行的异步操作
console.log("他是同步执行代码");
console.log(info);
```

![image-20220823093137776](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324201.png)

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

![image-20220823093416159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324222.png)

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

![image-20220823093833663](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324247.png)

## 2.3 文件描述符

![image-20220823094545335](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324267.png)

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

![image-20220823103352742](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324290.png)

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

![image-20220823104757410](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324316.png)

## 2.4 写入和读取

### 2.4.1 基础使用

![image-20220823111735143](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324835.png)

下面就是**读取和写入**文件的 2 个方法`readFile`和`writeFile`

![image-20220807220329322](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324858.png)

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

![image-20220823112012497](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324880.png)

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

![image-20220823113703568](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324902.png)

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

![image-20220823115021411](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324940.png)

✨ 这里有一个小坑，下面写的是一个读取文件夹下所有的文件，使用这种方式不行。假如采用硬编码的会导致可维护性很差，所以这就是一个小坑。

![image-20220823151407137](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324984.png)

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

![image-20220823153410813](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324443.png)

就是`readdir`有一个书写就是`{ withFileTypes:true }`。这样获取来的文件是一个对象数组，里面包含了文件的名称和状态

![image-20220823154519148](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324462.png)

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

![image-20220823154632227](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324483.png)

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

![image-20220910180352177](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324618.png)

## 2.6 动态路径问题

在`node.js`中，我们直接`node`的话就会进行路径的拼接来执行

![image-20220807221346050](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324638.png)

假如我们换一个路径来执行这个程序的话就会出现问题，这个时候根路径就出现问题了

![image-20220807221559258](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324858.png)

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

![image-20220823191240014](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324947.png)

# 3. path

## 3.1 基本介绍

**path 模块**用于对路径和文件进行处理，提供了很多好用的方法。

但是为什么一定要使用`path`来进行拼接路径呢？不仅仅是因为语法规范，更是因为操作系统不一样，所以路径的名字也不一样，所以直接使用`path`的话就可以解决这个问题

![image-20230218152508995](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324984.png)

为什么会有`windows`和`Mac Linux`的路径区别呢？就是因为这个**可移植操作系统接口**

![image-20230218152527480](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324016.png)

## 3.2 基本 API

![image-20230218152545579](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324135.png)

#### 3.2.1 path.dirname()

`path.dirname`可以获取文件的根路径，但是不包含文件名

![image-20220822113116380](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324278.png)

#### 3.2.2 path.basename()

`path.basename()`方法，可以获取路径中的最后一部分，经常通过这个方法获取路径中的文件名

![image-20220808104148906](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324593.png)

#### 3.2.3 path.extname()

使用`path.extname()`方法，可以获取路径中的扩展名部分

![image-20220808104714069](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324615.png)

#### 3.2.4 path.join()

`path.join()`方法可以将多个代码片段连接在一起，拼接成完整得路径字符串。并且你会发现使用这种方式，可以将原本`Linux和Mac`的`/`标识符改变为`\`，用于`windows`

![image-20220808102656437](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324633.png)

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

![image-20220822234235687](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324722.png)

4、对于`path.resolve()`必定是返回一个绝对路径

![image-20230218154644896](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324760.png)

5、 在`webpack`中可以一般都是使用`path.resolve()`来解决这些问题

![image-20230218152824962](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324164.png)

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

![image-20220902231751467](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324185.png)

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

![image-20220902235505691](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324234.png)

### 4.2.4 listen()

![image-20220903093235808](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324288.png)

当然`listen()`也包含 3 个参数

> 参数一

![image-20220903093348695](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324339.png)

```javascript
// 假如你不写端口号的话，就默认分配端口号
server.listen(() => {
  // 使用该方式可以查看当前服务器的端口号
  console.log(server.address().port);
});
```

![image-20220903093538896](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324866.png)

> 参数二

![image-20220903093559609](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324896.png)

假如你的`主机host`设置为其他`ip`的话，就会导致其他 ip 访问不到。

![image-20220903093745338](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324931.png)

假如你设置为`0.0.0.0`的话就不会有这些问题，默认`IPV4`都是可以访问的

![image-20220903093924071](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324953.png)

> 参数三

![image-20220903094011783](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324990.png)

## 4.2 req 和 res

### 4.2.1 req

#### 4.2.1.1 基本使用

![image-20220903094755500](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324014.png)

在`req`中也包含了很多的数据，可以使用`req`来查看

![image-20220903095018857](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324546.png)

#### 4.2.1.2 解析 url

但是这里就有一个问题，假如传来的 url 是带`query`参数的，`req`获取到的`url`就是带参的，不方便判断

![image-20220903100157576](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324570.png)

所以这个时候就需要使用`url模块`

![image-20220903100506580](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324593.png)

#### 4.2.1.3 解析 query

假如我们需要解析`query参数`，我们可以导入`queryString`参数，并且解析出来为对象

![image-20220903100856028](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324617.png)

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

![image-20220903103434125](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324649.png)

#### 4.2.1.5 请求 header

![image-20220903104746696](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324800.png)

> 1

![image-20220903104512722](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324226.png)

这个在`http`请求的测试软件中一般都会自动切换

> 2.

![image-20220903104610272](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324249.png)

1.在最后项目打包的时候`webpack`会对项目进行打包，但是这种打包还是不够。我们可以将`js`文件打包为`.gz`文件，只要`header`中包含`accept-encoding`的`gzip`，这样我们就可以发送`.gz`文件给浏览器进行解压，这样减少了传输的数据量

2.accept 可以设置客户端接收的数据，比如:`image/jpg;image/jpeg;image/*`

### 4.2.2 res

#### 4.2.2.1 基本使用

假如我们追踪`createServer`回调函数中的`res`就会发现，其实`res`的本质就是`Stream.Writeable`

![image-20220902233609492](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324279.png)

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

![image-20220808222818724](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324305.png)

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

![image-20220903144811397](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324415.png)

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

![image-20220903151601338](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324593.png)

不是以前的以前`http.createServer()`中的`res`

![image-20220903151759797](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324975.png)

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

![image-20220903153543452](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324992.png)

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

![image-20220903153837388](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324014.png)

当你设置了`req.end()`的话就会正常接收数据

![image-20220903153903586](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324036.png)

一般的开发中都会使用`axios`来发送网络请求，使用原生的方式比较少

## 4.5 文件上传

下面是错误的示例，不能使用这种方式来处理文件上传。这里的整个思路是没问题的，客户端分批发送字节流数据，服务端使用流来接收。但是发送的数据包含`请求头数据，以及其他的数据`一起夹杂在流中，所以就会导致文件打不开

![image-20220903160122062](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324212.png)

下面使用原生的方式来处理文件上传，在项目中大部分都会使用框架

![image-20220903161240704](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324357.png)

1.下面就是传输来的数据，可以发现头部的信息基本就是`header`信息，在`PNG`的后面就是真正需要存入的数据。

2.`image/png`后面的`\r\n\r\n`表示的是 2 个空格。

3.`--------------2157167123124131370\r\n`表示的是`boundary`，表示的是上一段数据和下一段数据的分隔符

![image-20220903162056643](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324424.png)

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

![image-20220809083329624](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324507.png)

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

![image-20220809083831914](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324527.png)

# 5. event

## 5.1 基本介绍

![image-20220823192001478](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324733.png)

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

![image-20220823195243479](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324056.png)

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

![image-20220829221414260](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324077.png)

![image-20240120234321364](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324098.png)

## 8.2 is......

1、内部存在很多的`is`实现的方法，直接使用判断类型即可，但是要注意很多的`is...`在不同的版本被废弃了，使用的时候注意甄别

![image-20240120234907008](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324158.png)

2、取而代之的是很多不常用的类型的判断

![image-20240120234950857](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324191.png)

## 8.3 callbackify

1、使用`callbackify`可以将采用 `async` 函数（或返回 `Promise` 的函数）转化为回调的形式

2、这个和`promisify`基本相反，这个是转为回调函数，但是他不仅仅可以转化`promise函数`，还可以转化普通函数

![image-20240121000122885](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324481.png)

# 6. 模块化

具体可以参考这里的介绍：[[模块化]]

# 7. 包管理工具

## 7.1 基本介绍

![image-20220823221410872](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324437.png)

**npm 官网**：[npm (npmjs.com)](https://www.npmjs.com/)。具体的`npm`使用可以参考我**以前的笔记**

1、如果可以的话可以查看下面的指令

```bash
node -v		// 查看nodejs版本
npm - v		// 查看npm版本

npm install npm -g // 安装最新的npm

npm update jquery 		//更新jquery
npm uninstall jquery	//卸载jquery
```

2、并且这里存在一个`Windows`的问题，我们使用`-v`查看包版本的时候，都是查看当前文件夹下处理命令，并不会去`子文件夹`下去查看，所以我们查看的所有包版本都是查看的`全局版本`。

假如要查看当前项目中的版本可以使用下面的方法，方法一：进入`node_modules/.bin`文件夹中查看版本。方法二：使用`npx`工具查看，因为`npx`就是在导入到`node_modules/.bin`中进行执行

## 7.2 项目配置文件

![image-20220823222528783](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324488.png)

下面就是`Vue cli4`、`Vue cli2`和`自己创建的文件`的配置文件的信息

![image-20220823222639896](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324545.png)

当然现在很多包都有自己的非标字段，可以参考下面的视频：[开源库中的 package【渡一教育】-村头一只鹅鹅-稍后再看-哔哩哔哩视频 (bilibili.com)](https://www.bilibili.com/list/watchlater?bvid=BV17s421N7qF&oid=1854283439)

## 7.3 常见的属性

### 7.3.1 基础属性

![image-20220823222931870](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324086.png)

![屏幕截图 2022-03-02 224507](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324109.png)

### 7.3.2 private

![image-20220823222945969](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324131.png)

当我们在`package.json`中配置了`private`为`true`的话就可以设置该项目为私有的

![image-20220823223004664](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324153.png)

### 7.3.3 main

![image-20220823223114138](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324181.png)

这个`main`属性可以设置程序的入口，我们在自己写的项目中用处不是很大，因为大部分的操作都是使用`webpack`来操作的，所以我们设置这个属性没啥用。

但是在你要发布的`npm`项目中就需要这个配置来作为入口，假如你不写的话可能别人下载你的包就不会被执行，来执行后续的操作

![image-20220823223324439](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324256.png)

### 7.3.4 scripts

![image-20220823223943630](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324777.png)

1、下面就是配置`scripts`中的信息

![image-20220823224132971](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324798.png)

2、假如我们在`script`中配置`start,test,stop,restart`就可以省略`run`，直接输入`npm start`...

![image-20220823224403690](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324826.png)

3、我们配置`scripts`属性的时候，可以不写`npx`或者`npm`的，因为我们配置之后会默认在该项目的`./node_modules/.bin`文件夹下面寻找。这一点非常重要，因为我们在查看`包版本`的时候就需要使用到这个知识

![image-20230218175250296](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324855.png)

### 7.3.5 dependencies

![image-20220823224722956](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324890.png)

其实在真实的开发中和`main`是一样的，基本不用区分这个 2 个属性，只要我们的项目中依赖了这个包`webpack`就会自动打包进去。

这个属性的真正意义是在自己发布`npm`包的时候使用，使用者可以使用`npm i --production`来安装生成环境的包，这样开发者可以节省了安装的时间

### 7.3.6 engines

![image-20220823230304695](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324952.png)

### 7.3.7 browserslist

![image-20220823230327896](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324489.png)

## 7.4 版本管理

我这里例举几个版本号：`^2.1.3`、`~2.1.2`

`2`表示大版本更新，`1`表示功能更新，`3`表示问题修正。`^`表示功能会更新，`~`表示功能不更新

![image-20220823225500158](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324510.png)

**npm**遵循下面 2 种方式来区分版本号

**semver**：https://semver.org/lang/zh-CN/

**npm semver**：https://docs.npmjs.com/misc/semver

## 7.5 npm i

### 7.5.1 基本使用

![image-20220823232100217](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324530.png)

下面的 3 种模式都是可以的，无非就是写法的不同

![image-20220824104103936](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324551.png)

![image-20220825163812054](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324618.png)

还有很多的命令需要的时候可以查看官网：[CLI Commands | npm Docs (npmjs.com)](https://docs.npmjs.com/cli/v8/commands)

```bash
npm i axios@1.1.2 // 安装特定的版本
```

### 7.5.2 全局安装误解

![image-20220823232208947](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324648.png)

其实我也有这样误解：**首先全局安装不等于全局引用**，你全局下载的包不一定会被全局引用。这里打个比方：你全局安装了`jquery`，这个包会放置在`C:\Users\张嘉辉\AppData\Roaming\npm\node_modules`路径下

如果你使用了 nvm 来做 node 版本管理得话，可以在 nvm/node_modules 下面来寻找

![image-20220824101226697](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324201.png)

但是你引入的时候，不可能引入到这个文件，除非你修改`npm`的全局路径。并且你会发现下面的路径根本和上面对不上，所以也不存在找到这一说

![image-20220824101409986](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324227.png)

但是，为什么全局安装工具就可以找到呢？这是因为你全局安装的是工具库的话就会自动在 node 在根目录下生成`cmd`可执行文件，假如你是安装的`jQuery`、`axios`...这种的，就不会生成可执行文件

![image-20220824101629339](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324250.png)

并且还配置了环境变量，所以我们在任何一个终端输入名字就可以定位到这里来执行。

![image-20220824101044081](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324274.png)

### 7.5.3 npm i 原理

![image-20220825093555090](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324304.png)

这里的构建依赖关系是因为一些包可能会重复依赖一个包。比如`webpack`和`aixos`同时依赖一个包的情况下，就会对让他们直接引入这个包，这是以前的依赖方式，就是一个树形结构。但是现在就是扁平化的模式，你引入的包都摊平在一起

![image-20220825093628133](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324384.png)

下面就是有无`package.lock.json`的描述

![image-20220825110741902](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324815.png)

我们安装`axois`可以发现，其实他也会安装其他的依赖

![image-20220825112614523](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324843.png)

我们再来看`axios`中的依赖`form-data`，里面也会引入其他的依赖

![image-20220825112902245](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324958.png)

### 7.5.4 package-lock.json

![image-20220825115214206](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032324980.png)

但是最新的版本中会有一个`packages`的属性，官网对这个属性的解释：[package-lock.json |npm Docs (npmjs.com)](https://docs.npmjs.com/cli/v8/configuring-npm/package-lock-json#packages)。个人理解：可能是为包的名字打上属性

![image-20220825115458292](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325006.png)

我们在这里就会发现`package-lock.json`文件的作用了，原本的`package.json`文件只能记录你安装的包的版本，但是不会记录依赖的依赖的版本，下面的`follow-redirects`有 2 个不同的版本，虽然只是功能的升级。所以在传递代码的时候记得带上`package.lock.json`文件，不然会导致安装的版本不同

![image-20220825163316242](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325107.png)

### 7.5.5 缓存机制

具体也可以参考这个文章：[深入浅出 package-lock.json - 简书 (jianshu.com)](https://www.jianshu.com/p/5c877c5c5bc3)

我们输入下面的命令可以查看`npm`的缓存文件的位置

![image-20220825120417942](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325635.png)

我们打开文件夹之后，进入`npm-cache`就可以进入该文件的缓存目录了。其中`index-v5`就是`content-v2`的索引

![image-20220825120642210](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325656.png)

我们随便打开`index-v5`其中的一个索引就会发现里面对应的是一个文件，通过算法来查找这些文件。

![image-20220825162723577](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325673.png)

我们将这些文件加上`.tgz`的后缀进行解压其实我们缓存中的依赖了

![image-20220825163123535](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325692.png)

## 7.6 其他工具

### 7.6.1 yarn

![image-20220825170716816](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325727.png)

假如我们需要使用`yarn`来安装依赖的话

```bash
npm i yarn -g
```

下面就是`yarn`和`npm`的命令的关系图，其实`yarn`和`npm`是差不多的

![image-20220825170730117](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325241.png)

### 7.6.2 cnpm

![image-20220825171645191](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325263.png)

### 7.6.3 npx

![image-20220825173432715](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325287.png)

1、假如我们需要全局安装`webpack`的话需要输入`npm i webpack -g`和`npm i webpack-cli -g`

这个时候我们在局部来安装`webpack`，再使用`webpack -v`来查看该工具的版本，很显然调用的是全局的`webpcck`，那要怎么才能使用局部的`webpack`呢？

![image-20220825173639151](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325309.png)

假如我们要执行局部的`webpack`，其实本质就是执行`node_modules/.bin/`下面的`webpack`文件

![image-20220825173918836](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325350.png)

所以就会出现下面的 3 种方式来执行局部的`webpack`。这里要说下第二种方式，在`package.json`中配置`webpack`的话，会默认在最近的`node_modules`中去执行

![image-20220825173445043](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325386.png)

2、但是这里存在一个特殊的情况，我们在查看`webpcak`的版本的时候就会一直查看全局的`webpack`版本。即便你在`node_modules\.bin`中或者使用`npx`查看版本也会查看全局版本

并且因为`VSCode`权限问题，所以我们要查看`webpack`版本需要使用`管理员权限`，并且上述问题都是只有`webpack`才存在的问题

![image-20230218205221163](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325893.png)

### 7.6.4 pnpm

#### 7.6.4.1 基本介绍

原本使用`npm/yarn`的时候，每下载一个项目就会将原本所有的包下载一遍，这样就会导致项目越来越大。所以就可以使用 pnpm`对包进行`软链接`和`硬链接`处理来节约内存

![image-20230218211708167](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325925.png)

#### 7.6.4.2 硬链接和软链接

> 基本介绍

![image-20230218214910863](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325025.png)

> 基本使用

![image-20230218215845150](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325047.png)

1、我们使用`硬链接`之后只要修改了其中的一个文件，建立链接的文件也可以进行同步

![image-20230218225429883](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325068.png)

2、其实就可以理解为操作系统中的`快捷方式`，如果你删除了原本的文件，这个软连接就会消失

![image-20230218230120357](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325206.png)

#### 7.6.4.3 高效/节省磁盘

`pnpm`会对你下载的包进行`硬链接`，所以我们构建项目直接将库中的数据读取即可，而且节省磁盘

![image-20230218231002628](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325630.png)

#### 7.6.4.4 非扁平化 node_modules

1、原本的`npm`就是非扁平化的`node_modules`的包，我们下载`webpack`可能出现`webpack包`中还存在一个`node_modules`，里面又包含很多的包，这样就会导致下载很多的重复的包

现在的`npm`就是下载的非扁平化的包`node_modules`，也就是会将不同的包都放置到`node_modules`中，不会再出现一个包中又出现`node_modules`。但是这种方式还是有问题，因为包都是扁平化的，所以我们可能存在引入没有下载包，也就是不能随意引入代码

![image-20230218232915542](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325655.png)

2、我们使用`pnpm add xxx`来下载包，因为是第一次下载所以并没有复用的包

3、查看左边的标识箭头，可以看到其实底层的文件夹是使用的`软链接`来处理的，它会跳转到`硬链接`中

![image-20230218233316240](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325679.png)

4、其中`pnpm`中包管理就是按照下面的方式来存储，都是`软链接和硬链接`组合来操作的

![image-20230218234902121](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325704.png)

5、我们再下载一遍`axios`的时候，就会发现速度很快，而且并没有下载包，而是直接复用

![image-20230218235243588](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325850.png)

#### 7.6.4.5 基本操作

![image-20230218235537764](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325396.png)

#### 7.6.4.6 store 存储

![image-20230219140859969](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325420.png)

## 7.8 发布项目

![image-20220830223954011](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325446.png)

假如你要发布的话，可能还需要注意下面的 4 个属性

![image-20220902191620811](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325474.png)

另外还需要一个`readme文档`，假如在项目里包含`readme文档`的话，到时候查看我们的项目就会在主页显示文档

![[00 assets/677140fcef310f3af92322110bf9eea5_MD5.png]]

## 7.9 配置镜像

> 查看镜像

```bash
npm config get registry		//registry表示登记
npm config get disturl
```

> 配置镜像

```bash
npm config set registry http://registry.npm.taobao.org --global
npm config set disturl http://npm.taobao.org/dist --global

npm config set registry http://registry.npmjs.org --global	//切换到原生的地址
```

当然我们不仅仅使用网址来配置，还可以使用`npx`

```bash
npx nrm use taobao	//nrm切换为淘宝源
npx nrm use npm //切换为官方源
```

使用`cnpm`来配置，这样的话就可以使用淘宝的镜像来下载了

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

我们再来查看 cnpm 的版本

```
cnpm -v
```

有的时候 cnpm 会有一系列的问题，所以我们使用下面的方式来使用淘宝镜像来下载

```
npm install --registry=https://registry.npm.taobao.org
```

# 9. buffer

## 9.1 基本介绍

### 9.1.1 基本介绍

我们通常情况下，是浏览器来处理图片和文件。并且一个图片其中的一个像素点的`rgb`值就是`0~255`，其中当`rgb`值为 0 时，二进制值就是`0000 0000`；当`rgb`值为 255 时，二进制就是`1111 1111`。就是这样一组的二进制值可以来展示一个图片

![image-20220830224727051](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325880.png)

但是`Node.js`是服务器语言，不能依赖浏览器。所以`Node.js`就需要执行二进制流

![image-20220830225701453](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325905.png)

### 9.1.2 字符串

![image-20220831150303063](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325936.png)

下面就是使用`Buffer`来存储的基本过程，因为`1111 -> f`，所以使用八位最大的 16 进制就是`ff`

但是下面的这种方式已经过时了，不推荐使用这种方式

![image-20220831151437720](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325071.png)

现在可以使用`Buffer.from()`来转换

![image-20220831151741262](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325617.png)

大致的存储过程，将字符串`why`转换为`0000 0000`的八位二进制，然后转换为十六进制进行存储

![image-20220831152037152](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325637.png)

### 9.1.3 中文编码

下面就是使用`utf8`和`utf16le`的编码差别，`utf8`对中文默认是 3 组 6 字节，而`utf16le`对中文默认是 2 组 4 字节

![image-20220831152501040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325654.png)

假如我们来解码的话，默认也是使用`utf8`来解码的。假如你是使用`utf16le`来编码，却是`utf8`来解码的，就会出现乱码

![image-20220831153227277](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325681.png)

## 9.2 创建方式

![image-20220831153353139](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325717.png)

Buffer 的官方文档：[Buffer | Node.js v18.8.0 Documentation (nodejs.org)](https://nodejs.org/dist/latest-v18.x/docs/api/buffer.html)

### 9.2.1 Buffer.alloc

`Buffer.alloc()`里面可以传入一个值，就是要开辟的字节长度。假如是**1kb**的话就是**1024byte**，在`Buffer.alloc`里面写入的参数就是**1024**

![image-20220831153841507](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325787.png)

## 9.3 文件读取

### 9.3.1 基本使用

下面的`readFile`的本质就是使用`Buffer`来读取进制流。

![image-20220831154631527](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325187.png)

我们使用`readFile`也可以读取其他文件

![image-20220831155044948](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325291.png)

下面就是使用`readFile`来读取其他文件，并且将读取到的进制流写入到另外一个文件中

![image-20220831155201830](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325311.png)

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

![image-20220831194900405](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325335.png)

### 10.1.2 进程和线程

![image-20220831195008159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325377.png)

### 10.1.3 多进程多线程开发

![image-20220831195642150](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325464.png)

### 10.1.4 JavaScript 和进程

![image-20220831195803716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325912.png)

## 10.2 JS 执行过程

### 10.2.1 非异步执行

![image-20220831200959561](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325941.png)

### 10.2.2 异步执行

![image-20220901101550109](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325979.png)

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
![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202406031118418.png)

## 10.4 宏任务和微任务

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202410171348777.png)

但是既然有 2 个队列，那么事件循环是如何处理这 2 个队列。通过下面的代码就可以知道

首先是优先执行`微任务`，当`微任务队列`都被事件循环压入函数调用栈之后，就会去执行`宏任务队列`。当处理了一个宏任务队列，就会去检查`微任务队列`是否其他任务。假如有的话就去处理`微任务队列`，假如没有的话就继续执行下一个`宏任务队列`中的函数。每次执行一个`宏任务队列`中的函数，就会去检查`微任务队列`

![image-20220901153142851](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325638.png)

这个就很好的简述了上图代码的执行情况

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202410171348850.png)

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

![image-20220901192717142](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325683.png)

这里其实有一个我以前理解不是很深的一个点，就是`new Promise()`中的回调函数，他其实不属于上面的事件循环的流程，而是直接在`script`中执行。而`then()`才是丢到微任务队列中执行。这就意味着`new Promise()`中先去执行，然后才会去执行`微任务`中的函数

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202410171348222.png)

这里有一个小知识，`async`和`await`可以看作是`Promise`的语法糖

1.我们可以将`await`关键字后面执行的代码，看做是包裹在`(res,rej) => { 函数执行 }`中的代码

2.`await`的下一条语句，可以看做是`then ( res => { 函数执行 } )`中的代码；

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202410171348979.png)

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

![image-20220901194211419](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325765.png)

## 10.5 Node 架构

![image-20220901194702608](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325275.png)

我们在`Application`中写了一个`fs.readFile`，`js`本身不会去读取文件，首先是`V8`引擎来翻译，丢到`NodeAPI`中去读取文件，`NodeAPI`又会去调用`Libuv`来读取文件。最后其实就是`Libuv`来读取的文件。

## 10.6 阻塞 IO 和非阻塞 IO

> 基本介绍

![image-20220901232425761](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325300.png)

其实对于文件的操作就是使用`Libuv`来实现的，然后来调用`操作系统`设置好的文件操作

![image-20220901232720420](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325331.png)

当然操作系统也分为 2 种调用方式

![image-20220901233052468](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325355.png)

> 非阻塞 IO 的缺点

![image-20220901233454738](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325391.png)

当然也是有解决的方法，这个在`Java`中有提到

![image-20220901233517301](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325436.png)

在线程池只有很多正在等待的线程，比如`fs.readfile()`在`Application`端被书写，经过`V8`转义，`NodeAPI`的调用`Libuv`，这个时候就会调用线程池来读取文件。当读取完成之后，`libuv`就会将`fs.readFile()`中的回调函数压入`事件队列`中，通过`事件循环`将队列中的函数给`函数调用栈`，然后返回给`application`端被读取

> 阻塞和非阻塞，同步和异步的区别

![image-20220902091614026](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325994.png)

线程不安全是因为多个线程同时读取一个文件，可能一个线程在修改该文件，这就导致了文件读取的错误。但是其实这样`Node.js`就不会存在线程不安全的问题，多个线程读取完成之后，就会将注册的函数和取来的值一起放入事件队列中，通过事件循环来读取压入单线程的函数调用栈，一个个执行。

## 10.7 Node 事件循环

![image-20220902110804039](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325021.png)

官方文档：[Node.js 事件循环，定时器和 process.nextTick() | Node.js (nodejs.org)](https://nodejs.org/zh-cn/docs/guides/event-loop-timers-and-nexttick/)

![image-20220902110951652](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325049.png)

## 10.8 Node 宏任务和微任务

![image-20220902111304214](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325083.png)

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

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202406101705342.png)

可以看下下面是为什么？

![image-20220902130946248](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325173.png)

结果并不是想的那样

![image-20220902185825779](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325750.png)

因为`setImmediate`属于`check`阶段，而`setTimeout`属于`timer`阶段。注意`poll`阶段会进行阻塞。

![image-20220902184625342](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325773.png)

而且在执行循序中`check`阶段是在`Timer`阶段后面，所以可以得出`setTimeOut`比`setImmediate`先执行吗？不对

![image-20220902184700815](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325797.png)

`main`函数首先执行`setTimeout`函数，然后会将`setTimeout`中的回调函数给一个树形结构，当时间过去之后`时间循环`就会读取该树形结构的的回调函数，然后函数调用栈来执行。

这里就会出现一个问题，将`setTimeOut`存入树形结构，然后再将该回调函数取出会有时间的损耗，假如存入就花费了`20ms`，但是事件循环初始化花费了`10ms`，这个时候就会优先来执行`setImmediate`。假如存入只花费了`5ms`的话，那就就会优先来执行`setTimeOut`，这就导致了执行顺序的问题

![image-20220902190728831](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325822.png)

# 11. stream

## 11.1 基本介绍

> 基本介绍

![image-20220902193305230](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325847.png)

> 读写文件的流

![image-20220902193447737](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325904.png)

下面就是为所有流都是`EventEmitter`的实例，因为在源码部分基本就是通过`Stream`来实现的

![image-20220902193912146](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325226.png)

## 11.2 Readable

### 11.2.1 基本介绍

![image-20220902194237174](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325481.png)

这个时候我们就可以使用`Readable`来实现

![image-20220902194305756](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325500.png)

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

![image-20220902200928927](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325520.png)

## 11.3 Writeable

### 11.3.1 基本介绍

![image-20220902201130229](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325570.png)

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

![image-20220902230615805](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325652.png)

## 11.4 pipe 方法

![image-20220902210109764](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325991.png)

# 12. os

## 12.1 基本使用

> 输出系统版本信息

![image-20230911215148948](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325019.png)

> 输出用户目录

1、返回用户目录，原理就是在`windows`执行 `echo %USERPROFILE%`，在`posix`中执行`$HOME`

![image-20230911215317793](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325112.png)

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

![image-20230911215542967](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325135.png)

> 输出网络信息

![image-20230911220607623](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325189.png)

## 12.2 案例

> 打开浏览器

1、在`webpack`和`vite`中编译之后自动打开浏览器，下面就是实现的原理

2、`exec`可以执行`命令`，本质就是在控制台中输入执行

![[00 assets/be4ccb736a8de8219737e9e238d90872_MD5.png]]

# 13. process

## 13.1 基本使用

> 输出信息

1、`process.cwd()`表示获取当前执行进程路径，他主要用于`esm`环境中

2、`process.argv`可以获取执行当前线程中的参数，主要用于一些开发包工具中

![image-20230911223644463](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325713.png)

3、`process.memoryUsage()`获取系统内存使用量，这个主要是做性能优化的

![image-20230911223744648](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325732.png)

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

![image-20230911223157112](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325751.png)

5、`process.env`表示获取当前系统的所有环境变量

![image-20230911224158802](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325779.png)

并且该环境变量是可以被修改的，但是只是当前进程中被修改，不会影响全局的变量使用

![image-20230911224252111](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325890.png)

> 退出进程

![image-20230911223944253](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325442.png)

1、如果按照下面的方式来执行，就会在`2s`的时候退出当前进程，所以`5s`的定时器就会被挂载，不能被执行

![image-20230911223957513](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325463.png)

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

![image-20230912223447301](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325485.png)

3、如果只是单个指令的话，也可以使用`execSync`来处理，这个表示同步的方式来调用

![image-20230912223729314](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325504.png)

4、使用`execFile`也可以运行可执行文件

![image-20230912223909912](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325544.png)

### 13.2.2 spawn

1、`spawn` 用于执行一些实时获取的信息，因为`spawn`返回的是流边执行边返回，`exec`是返回一个完整的`buffer`，`buffer`的大小是`200k`，如果超出会报错，而`spawn`是无上限的。

2、`spawn`在执行完成后会抛出`close`事件监听，并返回状态码，通过状态码可以知道子进程是否顺利执行。`exec`只能通过返回的`buffer`去识别完成状态，识别起来较为麻烦

3、并且对于`exec`、`spwan`之间的底层原理的实现是`exec` -> `execFile` -> `spawn`，`exec`是基于`execFile`实现的

![image-20230912224242679](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325589.png)

### 13.2.3 fork

1、场景适合大量的计算，或者容易`阻塞主进程`操作的一些代码，就适合开发`fork`

2、他只能调用`JS模块`，他的原理就是`IPC通讯`，`IPC`又是基于`libvu`

3、我们使用`fork`会创建一个子线程来执行该`js模块`，我们可以与该子线程之间进行通讯

![image-20230912224858175](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325123.png)

## 13.3 案例

> 区分开发/生产环境

1、我们可以根据`process.env`来做很多的操作，比如：区分`开发环境`和`生产环境`

2、`cross-env`本质就是`windows`调用`SET`来设置环境变量，`posix`就是调用`export`来设置环境变量

```bash
set NODE_ENV=production  	#windows
export NODE_ENV=production 	#posix
```

![image-20230911224915013](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325145.png)

> 调用 Java 程序

1、可以使用`exec`来调用`.java`编译之后的`.class`文件

![image-20230912223129834](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325165.png)

# 14. ffmpeg

## 14.1 基本使用

1、进入网站下载：[Builds - CODEX FFMPEG @ gyan.dev](https://www.gyan.dev/ffmpeg/builds/)，并且将该`ffmpeg`配置环境变量即可，控制台输入`ffmpeg`可以打印字符就代表安装完成

![image-20240120231440273](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325189.png)

> 转化视频格式

1、这里使用了`execSync`子线程来做处理，`-i`表示输入，`1.mp4`表示输入文件，`2.avi`表示输出文件，`{ stdio: "inherit" }`表示打印对应的参数

2、不仅仅是`.avi`，还可以转化为`.gif`等格式

![image-20240120232045800](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325219.png)

> 提取音频

1、这里直接改为`mp3`即可，就可以提取出音频

![image-20240120232501657](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325267.png)

> 裁剪视频

1、`-ss`表示从多少开始，`-to`表示多少结束

![image-20240120232702074](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325146.png)

> 添加/删除水印

1、下面的参数就是为视频添加一个`zjh`的水印，并且设置了他的颜色为白色

![image-20240120233909892](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325168.png)

2、使用`delogo`来删除水印

![image-20240120234000689](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325191.png)

# 12. express

## 12.1 基本介绍

![image-20220903223542284](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325219.png)

**express 官网**：[Express - 基于 Node.js 平台的 web 应用开发框架 - Express 中文文档 | Express 中文网 (expressjs.com.cn)](https://www.expressjs.com.cn/)

其实`express`的本质就是一个中间件

![image-20220903230435333](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325245.png)

## 12.2 基本使用

### 12.2.1 使用脚手架

![image-20220903224307142](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325272.png)

经过上面的处理就会发现已经将项目创建完成了

![image-20220903224239306](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325044.png)

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

![image-20220903231007943](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325066.png)

## 12.3 参数解析

![image-20220904232215684](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325090.png)

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

![image-20220904000130379](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325116.png)

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

![image-20220904154923058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325149.png)

### 12.3.3 文件上传

> form-data 文件上传

这里有一个小问题，假如你将`app.use(upload.any())`写在`upload.single()`前面就会出现这样的问题。

![image-20220904223602833](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325193.png)

可以查看官方文档，可以发现官方的处理方式，不允许`app.any()`作为全局使用

![image-20220904230111935](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325671.png)

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

![image-20220904225941243](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325691.png)

这个时候我们也可以上传多个文件和输出多个文件的信息

```javascript
// 这里使用`upload.array`
app.post("/upload", upload.array("image"), (req, res, next) => {
  console.log(req.files); // 获取文件的信息，注意这里是files
  res.end("文件上传成功");
});
```

![image-20220904225923166](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325711.png)

我们上传文件的时候使用的就是下面的格式来上传多个文件

![image-20220904225827456](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325734.png)

假如我们需要限制上传的个数也可以使用下面的方式

![image-20220904230633761](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325775.png)

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

![image-20220904232842950](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325148.png)

## 12.4 显示日志

### 12.4.1 mogan

morgan`官方文档：[expressjs/morgan: HTTP request logger middleware for node.js (github.com)](https://github.com/expressjs/morgan)

如果我们希望将请求日志记录下来，那么可以使用 express 官网开发的第三方库：`morgan`

```bash
npm i morgan // 先下载morgan
```

我们需要写`WriteStream`添加到`morgan`中，用于数据的写入

![image-20220904231803708](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325165.png)

下面就是日志文件的显示

![image-20220904231847135](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325189.png)

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

![image-20231220225116387](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325220.png)

2、如果出现未捕获的异常，可以使用`exceptionHandlers`来记录

![image-20231221090935871](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325281.png)

3、我们也可以使用下面的方式创建多个`logger`实例，各司其职

![image-20231221090519978](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325313.png)

4、还可以使用`rejectionHandlers`来捕获`Promise`出现的异常

![image-20231221091316770](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325947.png)

> transports

transports 文档：[winston/docs/transports.md at a7c2eec1ef2209022f5420a314b741d88ee2ebe9 · winstonjs/winston (github.com)](https://github.com/winstonjs/winston/blob/HEAD/docs/transports.md#winston-core)

1、可能日志存在很多的需求，这里需要配置`transports`，下面介绍的`transports`需要下载一个第三方库`npm install --save winston-daily-rotate-file`

2、下面是一个`http库`，他会请求对应的地址，并且将打印的参数传递过去

![image-20231220231630917](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325969.png)

3、当然我们也可以使用时间的库，这样即可按照时间来打印日志

![image-20231220231742548](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325992.png)

4、同时他也支持动态添加`transports`

![image-20231220232441278](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325023.png)

5、如果需要直接在社区中查找对应的`transports`即可

> 日志等级

1、从上往下，重要程度依次降低。比如当你指定 level 是 info 时，那 info、warn、error 的日志会输出，而 http、debug 这些不会。

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325048.png" alt="image-20231220232522229" style="zoom:50%;" />

> format

1、下面是`format`的几个模式

![image-20231221083959936](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325085.png)

2、我们也可以使用`winston.format.combine()`来添加组合`format`

![image-20231221085842154](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325971.png)

3、可能不同的`transports`存在许多的`format`，分别设置即可

![[00 assets/c26c0ca4c25a3d85eee5f77bf74efb94_MD5.png]]

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

![image-20220905201455689](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325015.png)

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

![image-20220905205100253](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325040.png)

假如我们去访问的话没啥问题

![image-20220905205123638](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325061.png)

## 12.7 静态资源托管

![image-20220811225740716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325077.png)

1、我们这里使用`app.use(express.static("public"))`来托管该目录下的资源，这样我们直接在 url 里面输入`http://127.0.0.1:80/index.html`就可以进行访问，而不需要去输入文件地址

![image-20220905210329379](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325666.png)

并且我们也可以一次性去挂载多个静态文件，假如在 public 文件夹下面没有相应的文件，就会去 files 文件下去寻找

![image-20220811230951661](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325689.png)

假如我们要访问里面的文件，直接输入文件名就可以访问到。因为你设置了静态部署的话，就默认摊在一个文件夹中被读取，客户端这里输入的和服务器端是不一样的

![image-20220905210550225](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325712.png)

使用上面的方式就是**从上往下寻找**，但是我们使用这种方式指定访问前缀

![image-20220811231314246](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325738.png)

2、如果外面使用静态资源托管来处理`Vue`打包之后的项目，可能存在路由问题，比如前端路由显示`/device/index`，但是这只是`spa`中`Vue`的前端路由显示的。这个时候我们刷新浏览器的话，就会导致使用该地址请求服务器，这个时候肯定是没有对应的前端路由，而且也不会有对应的`html`文件，因为这里使用的是`spa`页面

3、我们可以使用`connect-history-api-fallback`库来处理这个问题

参考文章：[connect-history-api-fallback 库的理解\_astonishqft 的博客-CSDN 博客](https://blog.csdn.net/astonishqft/article/details/82762354)

![image-20230810114900421](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325763.png)

## 12.8 错误处理

下面的方式来处理不是很好，因为判断的逻辑。到时候查询的逻辑都是写在一起的，这样会导致逻辑糅合在一起

![image-20220905211833493](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325832.png)

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

# 13. koa

## 13.1 基本介绍

![image-20220905231820922](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325434.png)

**Koa 官方文档**：[Koa(koa.js)中文网 -- 基于 Node.js 平台的下一代 web 开发框架 (koajs.com.cn)](https://www.koajs.com.cn/#)

## 13.2 基本使用

我们先下载 koa

```bash
npm i koa  // 下载koa
```

这里就是体现出和`express`的区别，假如你在读取服务器的时候，没有任何中间件执行，就会自动爆`404`的错误，并且会返回`NOT FOUND`

假如是`express`的话，就是超出时间默认关闭连接

![image-20220906130332510](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325462.png)

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

![image-20220906131231335](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325485.png)

## 13.3 路由使用

![image-20220906131631433](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325512.png)

很显然这种方式非常非常的麻烦，所以我们可以`kao-router`第三方库来解决

```
npm i koa-router
```

![image-20220906134036424](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325538.png)

假如我们添加`app.use(userRouter.allowedMethods())`这个中间件，就可以修改默认报错的信息

![image-20220906160453571](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325590.png)

这样默认回复的报错内容就不一样了

![image-20220906160357709](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325225.png)

下面为报错默认回复的信息

![image-20220906160608434](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325244.png)

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

![image-20220906162215461](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325263.png)

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

![image-20220906164318621](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325293.png)

2、可能存在上传时请求体过大的情况，我们需要配置`koa-bodyparser`

参考文章：[解决 koa request entity too large - 慕尘 - 博客园 (cnblogs.com)](https://www.cnblogs.com/baby123/p/13359472.html#:~:text=解决的方法 const koaBody %3D require ('koa-body')%3B const bodyParser,jsonLimit%3A"10mb" }))%3B app.use (bodyParser ({ formLimit%3A"10mb"%2C jsonLimit%3A"10mb" }))%3B)

![image-20230917212505310](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325316.png)

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

![image-20220906165759778](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325339.png)

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

![image-20220923152108489](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325845.png)

## 13.5 数据响应

下面为常见的数据响应的方式

![image-20220906171811703](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325863.png)

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

![image-20220906182943159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325887.png)

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

![image-20220906184638119](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325915.png)

使用`./dist`路径就是表示的项目根目录下面的`dist`文件夹

![image-20230409101254101](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325963.png)

因为现在很多的网页都是 SPA 网页，静态部署网页可能需要安装下面的库

![image-20231029193349380](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325043.png)

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

![image-20220906190525244](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325613.png)

## 13.8 Koa 源码分析

> 1.创建 Koa 的过程

其实本质就是导出了一个`Application`，在里面进行了初始化的操作

![image-20220906191157971](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325633.png)

> 监听操作

其实`app.listen()`的本质就是创建一个`server`来监听

![image-20220906191405118](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325661.png)

> 注册中间件

其实注册中间件的本质就是将这个中间件塞到`middleware`数组里面

![image-20220906191457171](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325687.png)

> 监听回调

当响应客户端数据的时候，本质就是`server`的响应，也就是执行这里面的`this.callback()`

![image-20220906191650118](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325711.png)

这里的`compose`是将所有的中间件都传输给`fn`

![image-20220906192015275](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325759.png)

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

![image-20220906223411698](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325420.png)

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

![image-20220906232908589](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325444.png)

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

![image-20220907130534547](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325467.png)

## 13.10 洋葱模型

这个是对应上面的`13.9 对比express`

![image-20220907132143900](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325492.png)

## 13.11 Cookie,Session

这段内容可以查看**P16.2.4** 登录凭证的笔记

# 14. 中间件

## 9.1 基本介绍

![image-20220812133427872](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325549.png)

我感觉其实本质就是路由守卫，在跳转路由之前执行操作

![image-20220903230828209](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325095.png)

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

![image-20220812135516913](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325118.png)

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

![image-20220903233323681](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325134.png)

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

![image-20220812141728012](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325160.png)

### 9.4.2 路由级别中间件

![image-20220812141828178](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325205.png)

### 9.4.3 错误级别中间件

![image-20220812142011667](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325278.png)

下面就是错误级别中间件的使用方式

![image-20220812143244347](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325809.png)

### 9.4.4 Express 内置中间件

![image-20220812143522293](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325831.png)

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

![image-20220819102717211](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325856.png)

> 防盗链

1、可能存在一些资源只在自己的域名下访问，但是其他域名不允许访问，这里是通过`referer`来判断

![image-20230315103541640](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325884.png)

2、下面就是实现的原理，只要监测到请求的地址中和自己本身的`referer`不匹配的话就不去继续请求，这样就实现了防盗链的效果

![image-20230315103259939](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325909.png)

# 15. 数据库

## 15.1 基本介绍

![image-20220907133502566](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325966.png)

我们也可以对数据库进行分类

![image-20220907133519942](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325498.png)

数组库的组织方式

![image-20220907160204998](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325519.png)

## 15.2 mysql 基础

这段可以查看我的`mysql`笔记，以及**最重要的将查询到的数据转换为对象和数组**，这对后面传输数据很重要

## 15.3 mysql

✨ 该版本较低，可以查看`mysql2`

首先先安装`mysql`的模块

```bash
npm i mysql
```

但是这里会有一个小问题，就是 mysql 的`版本问题`，假如你是`mysql8`以上的版本就会出现下面的错误

![image-20220819220201831](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325541.png)

这其实是因为 Node 不支持最新版本的 mysql 的密码加密方式，所以这个时候就需要设置 mysql 的加密方式了，将加密方式改为这种就可以正常连接了

![image-20220819220307625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325575.png)

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

![image-20220819223748901](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325691.png)

## 15.4 mysql2

### 15.4.1 基本介绍

![image-20220908100233643](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325079.png)

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

![image-20220908101112834](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325189.png)

我们可以看到回调中第三个参数`fields`，里面包含了数组中每个列得相关信息

![image-20220908102008380](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325207.png)

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

![image-20220908105039328](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325227.png)

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

![image-20220908102230224](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325280.png)

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

![image-20220908103208032](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325346.png)

### 15.4.5 连接池

![image-20220908103329999](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325869.png)

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

![image-20231223163247709](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325902.png)

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

![image-20220908105755058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325924.png)

其实`ORM`得本质就是下面图

![image-20220908111006937](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325948.png)

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

![image-20220908133708137](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325993.png)

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

![image-20220908134105725](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325080.png)

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

![image-20220908134834840](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325558.png)

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

![image-20220908134815743](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325577.png)

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

![image-20220908202301896](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325592.png)

## 15.6 typeorm

### 15.6.1 基本介绍

参考`sequelize`即可

### 15.6.2 基本使用

1、使用`npx typeorm@latest init --name typeorm-mysql-test --database mysql`来初始化一个`typeorm`的项目，`--name` 指定项目名，`--database` 指定连接的数据库

2、还需要下载`npm install --save mysql2`来连接数据库

3、我们需要额外的填写用户名和密码，并且还要指定连接数据库的包名，这里我们使用的`mysql2`，`sha256_password`，这个是切换密码的加密方式的，新版本 mysql 改成这种密码加密方式了

4、`synchronize` 是根据同步建表，也就是当 database 里没有和 Entity 对应的表的时候，会自动生成建表 sql 语句并执行

5、`poolSize`是指定数据库连接池中连接的最大数量

![image-20231224220731786](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325614.png)

5、我们看下代码， 有一个`entity`，通过装饰器声明了主键列和其他的列，这个就是数据库中的结构，我们以对象的形式映射出来

6、我们使用`save`和`find`来保存和查找对应的数据

![image-20231223232928056](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325676.png)

7、我们开启`typeorm`的`logging`可以看到本质就是自动生成`sql`语句

![image-20231223233156795](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325731.png)

8、并且会开启事务，我们可以提交和回滚

![image-20231223233302588](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325066.png)

### 15.6.3 增删改查

#### 15.6.3.1 建表

1、创建表的依据就是 `Entity`，如果我们开启了`synchronize`就会自动根据`Entity`来建表

2、当然我们也可以手动来设置`Entity`来控制表的字段

![image-20231224222402541](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325279.png)

3、当然我们也可以修改里面的数据类型，还可以设置一些其他的配置

4、下面是对这些属性的解释，如果想知道更多可以查看文档

​ `@Entity` 指定它是一个 Entity，name 指定表名为 person。

​ `@PrimaryGeneratedColumn` 指定它是一个自增的主键，通过 comment 指定注释。

​ `@Column` 映射属性和字段的对应关系。通过 `name` 指定字段名，`type` 指定映射的类型，`length` 指定长度，`default` 指定默认值。`nullable` 设置 NOT NULL 约束，`unique` 设置 UNIQUE 唯一索引。`type` 这里指定的都是数据库里的数据类型

![image-20231224223102077](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325310.png)

#### 15.6.3.2 添加

##### 15.6.3.2.1 save

> 单条数据

1、使用`save`来插入数据，如果`id`相同的话就会变为`update`，前提是`id`为主键才能实现

![image-20231224225157080](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325333.png)

> 多条数据

2、如果我们想要插入多条数据，使用下面的方式

![image-20231224225801102](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325375.png)

#### 15.6.3.3 删除

##### 15.6.3.3.1 delete/remove

1、使用`delete`来删除数据，下面默认选择的主键来删除

![image-20231224225939025](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325494.png)

2、`delete` 和 `remove` 的区别是，`delete` 直接传 id、而 `remove` 则是传入 entity 对象

3、目前看只能使用主键 id 来删除数据，以后有时间查看一下文档

![image-20231224230526530](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325109.png)

#### 15.6.3.4 查询

##### 15.6.3.4.1 find

1、使用`find`来查询表中所有数据

![image-20231224232801683](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325129.png)

2、当然我们也可以添加一些条件，`In()`表示的就是`mysql`中的`in`

![image-20231224234059403](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325150.png)

##### 15.6.3.4.2 findBy

1、可以通过 `findBy` 方法根据条件查询

![image-20231224232921938](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325170.png)

##### 15.6.3.4.3 findAndCount

1、此外，你还可以用 `findAndCount` 来拿到有多少条记录

![image-20231224233034504](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325194.png)

##### 15.6.3.4.4 findAndCountBy

1、还可以添加查询条件

![image-20231224233126900](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325221.png)

##### 15.6.3.4.5 findOne

1、使用`findOne`表示查询一条数据，可以添加查询条件

![image-20231224233813230](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325909.png)

##### 15.6.3.4.6 findOneBy

1、通过`xxx`值查询一条数据

![image-20231224234228987](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325927.png)

##### 15.6.3.4.7 findOneOrFail / findOneByOrFail

1、`findOneOrFail` 或者 `findOneByOrFail`，如果没找到，会抛一个 `EntityNotFoundError` 的异常

![image-20231224234522917](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325945.png)

##### 15.6.3.4.8 query

1、还可以用 `query` 方法直接执行 `sql` 语句

![image-20231224234759970](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325964.png)

2、不仅仅是普通的`select`，还可以执行一些其他的语句

![[00 assets/42e09a091f6b67c5d4dcdc29b35d2d6b_MD5.png]]

#### 15.6.3.5 querybuilder

1、一般情况下，复杂 `sql` 语句不会直接写，而是会用 `query builder`，下面就是一个简单的使用

![image-20231224235839507](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325008.png)

2、用 `query builder` 和我用 `find` 指定 `where` 有什么区别么？比如这种复杂的关联查询

3、涉及到多个表，也就是多个 `Entity `的关联查询，就得用 `query builder` 了。简单点查询直接 `find` 指定 `where` 条件就行。

![image-20231224235942727](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325740.png)

### 15.6.4 getRepository

1、调用每个方法的时候都要先传入`实体类`，这也太麻烦了

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325764.png" alt="image-20231225000449054" style="zoom:67%;" />

2、可以先调用 `getRepository` 传入 `Entity`，拿到专门处理这个 `Entity` 的增删改查的类，再调用这些方法

![image-20231225000430449](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325798.png)

3、我们查看查看下面的代码，可以发现不用写那么多的`AppDataSource.manager(User)`，而是使用统一的`user_repo`即可

![image-20240115214923809](D:\%23\1.5 Node.js\NodeJS.assets\image-20240115214923809.png)

### 15.6.5 事务

1、使用`transaction`可以开启事务

![image-20231225000303546](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325831.png)

### 15.6.6 关系

#### 15.6.6.1 一对一

1、默认情况下我们需要额外设置一个表和另外一个表得一对一得关系，在`typeorm`中使用下面得方式设置

2、在 IdCard 的 `Entity` 添加一个 user 列，指定它和 User 是 `@OneToTone` 一对一的关系。

3、还要指定 `@JoinColum` 也就是外键列在 IdCard 对应的表里维护，该注解是一定要指定得

4、同时设置外键得时候，还可以设置`mysql`得联级关系

![image-20231227110927645](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325851.png)

可以看到数据库中填写了对应得数据

![image-20231227111326978](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325876.png)

5、同时我们还可以设置`cascade`为`true`，该联级关系是`typeorm`中维护得，告诉 `typeorm` 当你增删改一个 `Entity` 的时候，是否级联增删改它关联的 `Entity` 因为我们手动设置了`OnetoOne`得关系，并且直接传入了`user`，可以只保存`idcard`即可自动更新插入`user`得数据

![image-20231227111519947](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325651.png)

6、我们还可以设置联级查询，设置`relations`即可，他会联级一起查询

![image-20231227111955357](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325672.png)

#### 15.6.6.2 一对多

1、下面就是一个例子，比如说：员工对部门就是一对多的关系，我们分别创建一个`员工（employee）`和`部门（department）`2 个表，其中`employee`需要连接`department`，也就是设置外键

> ManyToOne

1、不管是`一对一`、`一对多`可以这样理解，我需要和外部连接，所以我的关系注解就写在哪里，下面的`@ManyToOne`就是一个例子

2、`many`指的是`employee`，也就是`employee`作为外键来指向`department`，这就是`ManyToOne`

![image-20240116140158073](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325692.png)

3、创建之后保存即可，和上面类似

![image-20240116142042135](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325720.png)

4、当然还可以设置`cascade`，他使用`typeorm`来自动保存联级，这样我们就不需要额外写`Department`的保存了

![image-20240116142509061](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325744.png)

> OneToMany

1、一般情况一对多关系更多还是在一的那一方来保持关系，一般情况写的时候也是需要`oneToMany`和`manyToOne`都会去编写，也就是下面的依赖关系

2、一对一的时候我们还通过 `@JoinColumn` 来指定外键列，为什么一对多就不需要了呢？因为一对多的关系只可能是在多的那一方保存外键呀！所以并不需要 `@JoinColumn`。不过你也可以通过 `@JoinColumn` 来修改外键列的名字

3、并且这里我们将`manyToOne`的`cascade`移到`department`中，如果 2 边都编写的话就变成依赖循环了

![image-20240118231351334](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325785.png)

4、这里我们可以看到，因为为`department`添加了`employee`，所以这里需要将数据传递给`department`来处理，和上面的不同

![image-20240118231857731](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325906.png)

5、并且`relations`本质就是一个`left join ... on ...`，我们也可以使用`query builder`来处理

![image-20240119202106310](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325930.png)

![image-20240119202125096](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325950.png)

6、删除的时候也是一样，要先删除`employee`，才能删除`department`，这个和`mysql`是一致的

7、或者在创建的时候设置配置外键`onDelete`的属性即可，这里一定要设置给`Employee`，不能设置给`Department`。这里我就不是很理解了，因为大部分的关系都是给`one`的部分，理所应当也要把`onDelete`给`one`的部分，但是却给了`more`的部分

![image-20240119221447438](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325976.png)

我们删除`department`的时候，`employee`也会同步删除

![image-20240119221513466](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325003.png)

#### 15.6.6.3 多对多

1、其中`多对多`上面的关系都类似，下面就文章和标签的多对多的关系

2、这里解释一下下面的第二个参数的作用，也就是`() => tag.articles`的作用，这个是手动指定外键。因为在多对多的关系中他们不存储外键，所以需要手动指定

![image-20240120002430574](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325029.png)

3、因为如果当前 `Entity` 对应的表是包含外键的，那它自然就知道怎么找到关联的 `Entity`。但如果当前 `Entity` 是不包含外键的那一方，怎么找到对方呢？这时候就需要手动指定通过哪个外键列来找当前 Entity 了。之前 `OneToOne`、`OneToMany` 都是这样

4、一对多的 `department` 那方，不维护外键，所以需要第二个参数来指定通过哪个外键找到 department

![image-20240120003011716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325043.png)

5、下面就是存储并且查找对应的数据

![image-20240120003058015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325067.png)

可以看到这里多对多的的模型已经构建出来了

![image-20240120002336463](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325106.png)

6、当然我们也可以去更新`article`，他也会自动维护中间表

![image-20240120003630310](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325132.png)

7、至于删除就简单了，因为中间表的外键设置了 `CASCADE` 的级联删除，这样只要你删除了 `article` 或者 `tag`，它都会跟着删除关联记录。

![image-20240120003712257](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325153.png)

## 15.6 Mongodb

### 15.6.1 基本介绍

可以参考我的`Mongodb`的笔记

### 15.6.2 Mongoose

#### 15.6.2.1 基本使用

1、我们使用`Mongoose`库来连接`mongodb`数据库

2、这里使用`once`函数表示，只连接一次并且执行内部函数，如果掉线之后并不会再次连接。而`on`就会一直询问`mongodb`连接

![image-20230331202526573](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325178.png)

## 15.7 redis

1、对于`redis`存在很多的官方推荐的库，可以参考下面的网址：[Clients | Redis](https://redis.io/resources/clients/#nodejs)

2、我这里就使用`node-redis`库来连接`redis`

3、下面为基本的使用，主要是用于查询所有的`keys`

![image-20231224140459518](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325100.png)

4、还有一些其他命令，这里直接可以参考`redis`的命令即可，基本是一致的

![image-20231224140558526](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325118.png)

# 16. 解决跨域

## 8.1 基本介绍

1、主要是因为现在前后端分离之后导致的问题，对于现在前端和后端的服务器不是一样的

![image-20230701191049683](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325139.png)

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

![image-20230701220415436](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325166.png)

## 8.2 解决方案

下面是比较常见的跨域的解决方式，上面使用`node.js`作为一个静态服务器就是`方案一`

![image-20230701221237959](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325191.png)

### 8.2.1 CORS

> 基本介绍

![image-20230701222959099](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325213.png)

> 基本使用

1、下面就是老师给出解决跨域问题的方式，参考文章：[Koa CORS 跨域问题 - 掘金 (juejin.cn)](https://juejin.cn/post/7136151612724084773)

2、但是这种解决方式用的并不多

![image-20230701223239393](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325931.png)

3、这里有一个坑，我们在使用`kao2-cors`的跨域库的时候，我们需要在`router`注册之前使用，不然无法使用

![image-20240306104147336](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325954.png)

### 8.2.2 node 代理服务器

1、这个解决方式就是`webpack`中常见的`proxy`代理服务器的方式

![image-20230701225239551](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325974.png)

下面就是整体的结构图

![image-20230701231008454](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325998.png)

2、下面就是使用`http-proxy-middleware`中间件配合`express`来搭建的代理服务器

`http-proxy-middleware地址`：[chimurai/http-proxy-middleware： ：zap：单行节点.js http-proxy 中间件，用于连接，express，next.js 等 (github.com)](https://github.com/chimurai/http-proxy-middleware#pathrewrite-objectfunction)

3、对于`webpack`的代理服务器的本质就是下面的方式，但是要主要这个代理服务器只是`开发时依赖`，如果我们使用`webpack`打包之后就不存在这个代理服务器了

![image-20230701231827605](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325019.png)

### 8.2.3 nginx 反向代理

1、`nginx`反向代理是**上线**的时候使用的，而`node代理服务器`是**开发**时使用的。其实`nginx反向代理`的本质和`node代理服务器`是一样的，也是将请求的数据进行转发

2、下面是`nginx`的代理处理，只是简单的将`http://localhost:80`转发到了`http://localhost:8000`中

![image-20230702121028676](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325044.png)

3、如果是真实的线上环境的话，其实就是`nginx`代理`静态资源`，随后同一端口的中再去代理转发`API服务器`

![image-20230702122130411](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325854.png)

# 17. 项目实战

## 16.1 day01

### 16.1.1 项目介绍

![image-20220908202348032](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325871.png)

### 16.1.2 项目搭建

> 1.该项目使用 koa 来搭建

```bash
npm init -y // 初始化npm包
npm i koa // 安装koa
```

> 2.规定目录的划分

![image-20220908221008695](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325891.png)

当然我们也可以来参考`egg.js`的目录规范：[目录规范 | Egg (eggjs.github.io)](https://eggjs.github.io/zh/guide/directory.html)

我们再来配置我们项目的目录。然后配置`npm`的启动

![image-20220908221735035](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325917.png)

我们再对业务进行分包，这样分离方便维护。这是暂时是对`app`的分离

![image-20220908222544522](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325941.png)

> 3.应用配置信息写到环境变量

![image-20220908222922329](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325973.png)

因为在项目中人数较多，很多配置的敏感信息不能被暴露，所以需要写一个配置文件。在根目录下创建一个`.env`文件。我们可以使用文件导入的形式来获取这些信息

![image-20220908223314946](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325544.png)

但是并不是很方便，所以这里需要使用`dotenv`，`dotenv`官网：[dotenv - npm (npmjs.com)](https://www.npmjs.com/package/dotenv)

```bash
npm i dotenv // 安装dotenv
```

我们使用`dotenv`就会自动读取更目录下面的`.env`文件。

下面的导出的写法，其实是因为赋值运算符优先执行右边的语句，右边为`解构赋值`然后作为对象导出

![image-20220908224821656](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325567.png)

### 16.1.3 postman

我们接口测试使用的是`postman`，我们可以设置集合，对这次项目的接口进行管理

![image-20220909130115718](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325586.png)

我们还需要配置环境，可能开发、测试、上线服务器都是不一样的，我们设置环境可以方便切换

![image-20220909130727813](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325609.png)

这样我们直接切换环境，可以改变`{{baseURL}}`的值，这样可以方便端口调试

![image-20220909130835060](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325630.png)

### 16.1.4 用户注册接口

我们首先将路由抽取出来放在一个单独的文件夹`router`中，因为后期有很多的路由接口。在文件命名上，也可以参考，这里使用的是`user.router.js`，假如以后有其他模块也叫做`user.js`的话就可以很好的区分

![image-20220909162542666](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325705.png)

我们再来将路由中的方法进行拆分，因为该路由下面的接口也会很多，所以我们简化其中的代码。但是不仅仅只是简化其中的代码，这里涉及到了拆分的思想。作为路由的文件就做好路由跳转的事情。

![image-20220909165404873](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325273.png)

这里再来拆分查询数据的代码

![image-20220909165715475](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325293.png)

最后安装上`koa-bodyparser`就可以解析`json`数据，注意中间件是从上往下执行

![image-20220909165816274](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325315.png)

### 16.1.5 数据库连接

因为数据库是`全局`的，所以我们按照目录划分需要写在`app`中。首先要`npm i mysql2`，并且数据库的配置信息都要写在`.env`中，通过`dotenv`来读取操作

![image-20220909175722220](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325343.png)

我们在封装好的`UserService`中进行数据的查询

![image-20220909190220573](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325362.png)

### 16.1.6 错误判断

在路由跳转的时候执行中间件`verifyUser`对传输来的数据进行判断。然后在`error-handle.js`中对这个中间件的逻辑进行编写

![image-20220909200822721](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325421.png)

我们再来编写专门收集错误类型的`error-type.js`文件

![image-20220909201221488](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325150.png)

我们再来编写专门处理错误类型的函数

![image-20220909213030893](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325169.png)

我们再来编写该用户是否存在的代码，原理其实是一样的

![image-20220909220032943](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325193.png)

## 16.2 day02

### 16.2.1 密码加密

在对路由中输入的用户名和密码进行验证之后。再去对密码进行加密处理，密码最好不要明文存储

![image-20220910141736070](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325223.png)

这个就是处理密码加密的代码，我们可以使用`Node.js`中内置的加密模块来处理

![image-20220910142039217](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325249.png)

### 16.2.2 登录验证

这里有一个细节问题，不一定所有的功能都抽到`utils`中，有的时候抽出为中间件就可以

下面的整个流程就是这样的，按照上面的流程来书写就没问题

![image-20220910175442484](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325265.png)

### 16.2.3 动态加载路由

我们在`index.js`文件中一直引入路由很麻烦，所以我们需要做出改进

![image-20220910175854007](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325947.png)

再在`router`文件夹下面编写加载路由的`.js`文件，用于动态加载路由。只要在该目录下的路由都会自动加载

![image-20220910230610299](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325968.png)

因为传入的`app`是一个对象，所以我们使用他的中间件导入的路由会以内存地址的形式来存储，所以不会存在函数结束，数据都丢失的情况，也就达到了路由动态加载的效果。但是这只是一种猜测

### 16.2.4 登录凭证

#### 16.2.4.1 基本介绍

![image-20220911154717795](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325994.png)

#### 16.2.4.2 cookie

##### 16.2.4.2.1 基本介绍

对于`Cookie`有不同的划分，这个在以前的学习中确实不是很清楚。其中就划分了内存`Cookie`和硬盘`Cookie`

![image-20220911160102104](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325017.png)

##### 16.2.4.2.2 常见属性

下面就是`Cookie`的常见属性

![image-20220911175144416](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325046.png)

##### 16.2.4.2.3 客户端添加 Cookie

下面就是在客户端添加`Cookie`值

![image-20220911174845714](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325126.png)

下面就是添加的`Cookie`值。注意这个`Cookie`是没有设置任何属性值的，所以他是内存`Cookie`，关闭浏览器就会自动清除这个`Cookie`，假如我们设置了过期时间的话就会转变为硬盘`Cookie`

![image-20220911174818471](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325702.png)

我们关闭浏览器，再次打开的时候你会发现`Cookie`消失了，这就是没有设置属性值的效果

![image-20220911203409912](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325725.png)

当然我们也可以设置属性值`max-age`来将内存`Cookie`转变为存储`Cookie`，并且可以设置最大存储时间，到了时间之后，就会自动消失

![image-20220911180041769](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325743.png)

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

![image-20220911220531539](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325771.png)

为什么后台可以获取到`Cookie`值，这是因为在网络请求中会自动携带上

![image-20220911220636599](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325798.png)

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

![image-20220911224955610](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325866.png)

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

![image-20220911230309996](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325341.png)

假如这个时候我们来修改其中的任何一个值，就会导致数据问题

![image-20220911230558894](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325361.png)

#### 16.2.4.4 token

##### 16.2.4.4.1 基本介绍

在上面介绍的`Cookie`和`Session`其实不是很好

![image-20220912192918550](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325382.png)

这里缺点主要就是下面的 2 点，上面的问题都是可以解决的。第一个就是不能解决不同客户端的问题。

第二个就是不能解决服务器集群的问题，假如密文是通过`Session`是通过服务器 1 来加密的，但是`Nginx`是将该数据转发给服务器 2 了，这个时候服务器 2 并没有服务器 1 的密钥，所以数据根本解析不了。但是这些问题都是可以解决的，但是不是很好，所以就会出现 token

![image-20220912193227217](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325403.png)

这个时候就可以使用`token`来处理

![image-20220912194824301](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325563.png)

##### 16.2.4.4.2 JWT

![image-20220912195825628](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325064.png)

这里需要注意一点，就是`jwt`是自带公钥的。所以所有人都可以解密`jwt`来获取信息，但是不能自己捏造`jwt`来传输，这个没用。`jwt.io`可以在没有公钥的情况下读取信息，但是不能修改

![image-20220915171913625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325085.png)

也可以看下`JWT`的场景：[深入理解 JWT 的使用场景和优劣 (qq.com)](https://mp.weixin.qq.com/s?__biz=MzI0NzEyODIyOA==&mid=2247483918&idx=1&sn=12683bae55f2ab1a8281ab398472362f&chksm=e9b58bc5dec202d385d1c1d861f7e0ff495296ed9387b32a8d01ae195eae03688e5aeebe6396&token=1557545914&lang=zh_CN#rd)

##### 16.2.4.4.3 postman 鉴权

1、在`postman`中我们添加授权，这样每次的请求都会自动在`header`中加上`token`值。一般我们都会去使用`Bearer Token`的模式

![image-20220913092120362](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325106.png)

2、如果我们想要自动保存`token`，还需要手动编写测试接口

![image-20230827100113625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325132.png)

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

![image-20220913102300665](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325234.png)

##### 16.2.4.4.4 非对称加密

大致就是这样，持有`privateKey`的用户系统，可以颁发`token`。持有`publicKey`的可以验证`token`。这个就是非对称加密。

![image-20220913160555333](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325993.png)

下面就是基本介绍

![image-20220913161046252](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325013.png)

我们也可以使用`SSL`来生成一个非对称加密，这里演示的是`windows`系统的`git`来生成的

![image-20220913161120804](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325034.png)

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

![image-20220913231852253](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325058.png)

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

![image-20220913232051939](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325082.png)

这个时候就会好奇，假如我们加密的时候使用公钥的话，能成功加密吗？答案是否定的，公钥是不能颁发`Token`的，所以我们使用公钥去加密的话会报错

![image-20220913232421549](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325137.png)

假如别人不知道我们的私钥，他就不能颁发`Token`。虽然他能获取到公钥，他也只能解析出信息，但是不能伪造`token`来调用接口

#### 16.2.4.5 项目登录凭证

基本操作和上面是一样的，假如是简化步骤的话，可以查看上面的介绍

首先是来加密信息，发给前端来保存

![image-20220914111326604](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325776.png)

然后我们对发送来的`token`进行解密

![image-20220914111415528](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325797.png)

MDN 响应状态码：[HTTP 响应状态码 - HTTP | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)

这里还有一个对于`postman`的操作，可以自动化设置`token`值，不必我们每次都添加。在服务器发送给客户端的接口里面写上这一段，就可以自动获取`token`到全局

![image-20220914111831940](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325835.png)

这里就会自动填充

![image-20220914111747826](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325890.png)

这里还需要注意一个`fs`读取的问题，因为我们使用的`npm`来执行的。本质就是将我们写的代码都存在`main.js`来执行，所以这个读取文件也需要修改，应该是按照`main.js`为基础来编写路径的，但是又可能搞混，这里直接就是`path`来拼接了

![image-20220914112143422](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325918.png)

### 16.2.5 查看动态

这个项目本身就是一个发表动态的论坛，所以我们需要搭建一个可以查看动态的接口。其基本的思想和上面的类似，首先编写接口，然后再来编写中间件。下面只是阐述写这些东西获取到的经验

> 1.

首先来看路由的特点，`post`的请求方式就是添加，下面的 2 条`get`请求就是查询，不做修改。这个就是`restful`风格的接口模式

![image-20220914171324083](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325944.png)

> 2.

这个就是编写一般接口的逻辑，首先增加中间件来对数据进行判断。然后在`Controller`中添加创建的方法

![image-20220914171739490](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325546.png)

再将对执行`sql`执行放在`service`中

![image-20220914171652939](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325565.png)

最后返回数值

> 3.

这个就是通过数据库表中的`user_id`到用户表中查询到的数据

![image-20220914214817680](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325585.png)

在返回的时候就需要按照这种格式来返回

![image-20220914172050961](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325615.png)

这里的查询格式为左连接来查询到改动态下面的用户，并且使用了`JSON_OBJECT`将其转化为对象格式

![image-20220914172017405](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325645.png)

并且这里还有一个思想，就是这个`sql`很长，所以我们可以抽取出来复用

## 16.3 day03

### 16.3.1 修改文章

这里就不去阐述了，大致步骤也和上面差不多的

但是这里有一个抛出异常的问题。我们在这里执行语句，假如出现错误的话，因为我们没有使用`try-catch`包裹，所以这里抛出的异常会抛出给上一个函数，假如上一个函数也没有处理的话，又会抛出。

![image-20220914225707894](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325699.png)

所以为了代码的健壮性，我们应该为这些函数包裹`try-catch`。一般的处理时包裹`sql`处理语句

![image-20220914225850624](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325269.png)

### 16.3.2 删除文章

操作基本和修改文章一样。

这里有一个点就是**业务接口和后台管理接口**的区别，后台管理接口的开发更加复杂，而且他们是不同系统的开发不能混杂在一起

### 16.3.3 发表评论

这里重点就是创建数据库。

1.首先评论是依附于文章的，所以需要添加`文章id`。

2.并且设置外键的时候带上`cascade`会很方便，这样每次这个数据表就会跟着外键表数据改变。

3.并且这里还有一个`comment_id`设置外键为自己的这个表。这样就可以体现出不同的层级

![image-20220917103944105](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325288.png)

### 16.3.4 回复评论

按照上面的数据库解释，这里回复也是存在一个表中。这个表示回复`id`为 2 的评论值

![image-20220917162830614](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325310.png)

这个就是评论回复的数据库思路。其实里面的业务代码很简单，按照流程来处理即可

### 16.3.5 修改评论

注意这里的使用。因为他们验证权限很类似（只需要修改查询的`sql`和获取到`params`值），而且代码可以复用，但是验证权限需要知道他们的区别。

![image-20220917163121129](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325335.png)

所以这里就有 2 个思路

> 1.对`verifyPermission`作高阶函数处理，对其进行闭包

将要处理的函数作为返回值处理，并且将高阶函数的参数作为区分。这也就可以动态调节里面值得变化了。也让这个`verifyPermission`得职能就扩大了

![image-20220917163513171](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325361.png)

然后将验证是否存在得`sql`进行修改，这样就可以动态修改

![image-20220917163805755](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325449.png)

这段得使用在我得笔记`JS高级`里面也有，可以参考

> 2.如果后续的接口都是按照`restful`风格来编写得话。可以直接获取`params`得参数的键来区分。

![image-20220917164045143](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325888.png)

### 16.3.6 删除评论

和上面类似

> 1.编写路由

![image-20220917164221038](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325908.png)

> 2.编写 Controller

![image-20220917164236644](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325926.png)

> 3.编写 sql 执行

![image-20220917164310054](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325963.png)

完成，基本这就是编写业务代码的全部。后面的非特殊处理，基本都是这个套路

## 16.4 day04

### 16.4.1 获取评论的个数

我们在这里加上一个子查询即可，这样就可以查询到个数

![image-20220918125821648](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325052.png)

只要`moment_id`是一样的，就可以链接到`moment`表查询到该动态的评论个数

![image-20220918125946233](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325495.png)

### 16.4.2 获取评论

> 方案一

将获取评论的接口和获取动态的接口分离来处理。这样直接获取`moment_id`即可

![image-20220920223420511](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325513.png)

> 方案二

在获取动态的时候，顺便获取该动态下面的评论，这里的难点主要是`sql语句`的编写。假如对于`sql`语句实在不知道怎么编写的话，可以参考下面的思路

![image-20220918215414938](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325533.png)

### 16.4.3 标签开发

1.因为`标签`和`帖子`是多对多的关系，在`mysql`课中学过，多对多最好的处理方式就是建立中间表，即这里创建`moment_label`表来作为中间表

![image-20220922104517260](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325557.png)

2.这里还有一个联合主键的概念。这个和普通主键是一样的，这里可以将他们 2 个字段连在一体作为主键来处理

**参考文章**：[联合主键有什么用？ - UniqueColor - 博客园 (cnblogs.com)](https://www.cnblogs.com/UniqueColor/p/7234340.html#:~:text=联合 主键 就是用 2 个或 2 个以上的字段组成 主键 。 用这个 主键 包含的字段作为主键，这个组合在,数据表 中是唯一，且加了主键索引。 那么这时单独使用订单号就不可以了，因为会有重复。 那么你可以再使用个订单 序列号 bill_seq 来 作为区别。 把 bill_no 和 bill_seq 设成联合主键。)

比如：`moment_id和label_id`分别是：(1,1)，(1,2)...这个就表示的是一个帖子包含 2 个标签，这个时候就会问，为什么`moment_id`是一样的，这里只需要(`moment_id`，`label_id`)的排列不一样就可以了

3.这里再来解释一下`on update cascade...`的使用，其实就是下面的图，只要`buildings`表更新或者删除，就更新和删除下面的`rooms`表。类比到这里就是，只要`label`表或者`moment`表更新或者删除就会影响`label_moment`表中的数据，这样做的好处就是方便更新数据，不需要你手动来维护了

![image-20220922115650250](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325602.png)

4.所以这里的标签开发。首先是分析数据模式，这个功能的模式就是`多对多`，一个文章可以使用多个标签，多个文章可以复用多个标签。然后就是构建数据库，是多对多所以需要设置`中间表`。并且构建外键的时候也是一样的，当更新和删除需要更新和删除，所以需要将中间表的外键的`on update 和 on delete`设置为`cascade`

### 16.4.4 动态添加标签

动态添加标签逻辑就是，用户的权限是：**登录**，**文章是自己的**。

剩下的就是后台关心的事情，假如用户添加的标签，数据库中不存在的话，就会自动添加到数据库中。并且该文章没有有该标签的话，就会自动与标签建立联系，假如有的话就会跳过

![image-20220922210332484](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325669.png)

剩下的逻辑就很简单了，大致逻辑就是如此

![image-20220922210745765](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325031.png)

### 16.4.5 动态显示标签

> 方式一

可以参考`16.4.2`的编写方式

![image-20220923101840196](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325113.png)

> 方式二

单独再来写一个接口，或者数据库查询的方式。来单独处理，这个也是我比较推荐的方式。下面的方式和`16.4.2`又不一样，下面的是将各个步骤写为单独的方式。但是`16.4.2`是写一个`sql`直接处理完返回

![image-20220922215848398](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325139.png)

## 16.5 day05

### 16.5.1 头像上传

首先来编写上传图像的中间件

![image-20220923152315227](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325158.png)

这中间的逻辑在`13.4.4`里面有讲，这里有一个`storage`的小坑需要注意一下

![image-20220923152355080](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325233.png)

然后再保存到数据库中即可

![image-20220923152447727](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325296.png)

### 16.5.2 头像查看

1.注意这里的一个小细节，为什么不直接获取头像的路径然后直接保存到数据库呢？这个其实理解起来很简单，因为我们直接将该路径存储，假如后期需要更换路径的话就会很麻烦，因为这些都是写死的，所以直接获取文件名，到时候拼接路径即可

2.当我们从数据库中查询到头像数据之后，可以创建流来传输给服务器

![image-20220923160352242](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325795.png)

但是这种形式浏览器并不知道是什么文件，所以默认是直接下载处理的

![image-20220923160520210](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325813.png)

3.假如我们需要让浏览器知道这是一个图片，就需要设置`Content-Type`来传输了，这个时候就是直接显示的图片

![image-20220923160719200](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325833.png)

4.当然这里还有一个细节就是变量都抽出来作为常量，后续只需要修改这一处就可以了

![image-20220923160815474](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325856.png)

### 16.5.3 用户头像

当添加头像数据之后，去更新用户的头像数据，这里可以直接拼接获取，也最好做成拼接获取即可

![image-20220923163113628](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325896.png)

下面就是数据库中的存放的数据模式

![image-20220923163319924](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325945.png)

### 16.5.4 动态配图

其实头像配图的逻辑已经完成了，动态配图就很简单了。就是一个单独的，一个多个的处理方式。但是还是有逻辑的区别的。这里建议使用文件名来查询

### 16.5.5 图片压缩

```bash
npm i jump // 使用工具库
```

下面就是基本的使用，这里将图片压缩为`1280`、`640`、`320`的格式

![image-20220924210155385](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325521.png)

# 18. 云服务器部署

## 17.1 基本介绍

下面的介绍为`CentOS 8.2`，因为该版本有`dnf`对于安装包更加方便

我们不仅仅可以使用`XShell`来连接`linux`服务器。我们也可以使用`git bash`来连接`linux`服务器

![image-20220924233447819](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325545.png)

当然我们这里使用`XSehll`来连接

![image-20230306090621311](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325572.png)

## 17.2 Node.js

因为服务器选择是`8.2`，所以是自带`dnf`的，下面可以使用`dnf --help`来查看该版本是否安装过`dnf`

![image-20220924233711922](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325596.png)

1.首先来搜索是否包含`Node.js`的包，可以使用命令`den search dnf`。很明显假如要安装的话，就安装下面的`Nodejs.x84_64`的版本

![image-20220924234019323](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325619.png)

2.当然我们也可以通过`dnf info nodejs`来查看你要下载的`node.js`的信息

![[00 assets/6b47ff68ce707eebcb31b131c400e433_MD5.png]]

3.通过下面的命令可以下载到`Node.js`

```bash
# 安装node.js
dnf install nodejs
```

但是下载的并不是`nodejs`的最新版本，而是比较老的

![image-20220925185743221](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325202.png)

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

![image-20220925190115422](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325226.png)

✨ 如果使用`n`来切换`nodejs`的版本之后`服务器`没有反应的话

1.解决方法一：通过`SSH`来建立连接

2.解决方法二：重启`ssh service sshd restart`

1、如果使用 CentOS7 的版本，可能会有很多的依赖库不存在，下面就是解决依赖库的问题

[node: /lib64/libm.so.6: version `GLIBC_2.27' not found - 丁少华 - 博客园 (cnblogs.com)](https://www.cnblogs.com/dingshaohua/p/17103654.html)

![image-20231115232715588](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325245.png)

2、因为 CentOS7 版本比较低，所以很多的功能都没有，需要一个个安装依赖库太麻烦了，可以直接使用二进制包来处理

[如何部署 Node.js 环境\_云服务器 ECS-阿里云帮助中心 (aliyun.com)](https://help.aliyun.com/zh/ecs/use-cases/deploy-a-node-js-environment-on-a-centos-7-instance#2c8bcdf02116b)

因为使用阿里云给的方式可以安装，因为是软链接设置了，没有环境变量，所以使用下面的方式可以设置环境变量，这样就可以全局使用`pm2`和`n`类似的工具库了

![image-20231117201318982](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325268.png)

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

![image-20220925193743158](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325292.png)

2.但是我们这样填写之后肯定是连接不上的，因为我们服务器的`3306`端口并没有开启。这个时候就需要添加规则来开放`3306`端口

![image-20220925193653245](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325366.png)

3.这之后还是不能连接，我们可以查看`msql`中的`user`表。可以发现`root`用户名的`host`是`localhost`，所以连接不上

![image-20220925194447959](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325752.png)

我们需要去修改`root`的`host`为`%`，这里就需要使用到`mysql`的`update`，`update user set host = "%" where user = "root";`

![image-20220925194700063](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325769.png)

4.假如还是连接不上的，就需要清除缓存了。输入下面的指令来重新授权，`flush privileges;`

![image-20220925195539297](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325788.png)

你安装`mysql`可能存在密码一直错误的情况，不要信网上的修改`authentication_string`，这个是凭证信息，修改也没用，最多置空就行，可以参考下面的文章来配置

[MySQL8.0 正确修改密码的姿势[通俗易懂\]-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/2115190)

### 17.3.3 mysql 迁移

我们将在本地建立好的`mysql`转储为`sql`文件

![image-20220925200049849](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325893.png)

可以看到这里有运行`sql文件`，直接将刚刚保存的`sql`文件运行即可

![image-20220925200216319](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325929.png)

## 17.4 手动部署

### 17.4.1 简单部署

使用`xftp`将`nodejs`的文件丢到服务器执行即可

![image-20220925202739365](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325218.png)

### 17.4.2 git 部署

#### 17.4.2.1 git 上传

1.首先将代码都上传到`github`中，现在已经上传完成

![image-20220925204020596](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325270.png)

2.这个时候服务器是没有安装`git`的，所以我们需要安装`git`

```bash
# 安装git
dnf search git
dnf info git
dnf intall git
```

这个时候输入下面的指令就可以`clone`项目到本地了

![image-20220925204319267](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325469.png)

这个时候我们就可以看到下面已经被`clone`的文件了

![image-20220925204846733](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325486.png)

#### 17.4.2.2 vscode 连接 ssh

但是没有**依赖包(node_modules)**，这个时候我们可以直接在服务器里面`npm install`就可以了，但是这样并不是很高效，也不是很直观，所以这里可以直接使用`vscode`来编辑`linux`里面的文件

我们来下载`remote-ssh`来进行`ssh`的连接

![image-20220925205052393](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325570.png)

这个时候我们输入上面的命令就可以连接了

![image-20220925205150703](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325909.png)

这里可以看到已经连接上远程了，选择你要展示的文件夹即可

![image-20220925205333450](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325930.png)

这个时候就可以看到已经完成了

![image-20220925210134140](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325954.png)

#### 17.4.2.3 执行

这个时候我们再来`npm install`就可以在`vscode`中进行安装

![image-20220925210551255](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325007.png)

我们再来执行即可（假如报错的话要注意有没有安装`nodemon`），这样就可以开启服务器版本的`nodejs`

![image-20220925210855946](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325098.png)

✨ 注意：这里我开启的端口是`8000`，但是该服务器的并没有开启端口`8000`，所以我们需要到控制台来开启

![image-20220925211538282](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325552.png)

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

![image-20220925213414925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325575.png)

## 17.5 自动部署

### 17.5.1 安装 Java

我们需要使用`Jenkins`来进行自动化部署，其实`Jenkins`的运行机制就是本地写完代码`push`到`git`上，然后到了一个时间就自动获取`git`的最新版本，然后再`npm i`添加最新的包，然后重新`pm2`

![image-20220925214227422](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325593.png)

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

![image-20220925220137286](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325627.png)

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

![image-20231222143811901](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325678.png)

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

![image-20231222155552908](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325724.png)

### 1.6 配置文件启动

1、输入`pm2 ecosystem`会创建一个配置文件，`apps` 部分就是配置应用的，`scripts` 就是应用的启动路径

2、剩下直接查看配置信息即可

3、使用`pm2 start ecosystem.config.js`，可以批量执行脚本

![image-20231222160702963](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032325320.png)

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
