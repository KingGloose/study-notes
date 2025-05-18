视频地址：[P2. 02.Electron 技术架构\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1xd4y1J7dB?p=2&spm_id_from=pageDriver&vd_source=2d46cc0fa105788201e3e43d9c83f528)

文章地址：[Electron 应用开发实践指南 - muwoo - 掘金小册 (juejin.cn)](https://juejin.cn/book/7302990019642261567/section/7302990019164110887)

文章地址：[Vue3 Vite electron 开发桌面程序*vue 桌面应用开发*小满 zs 的博客-CSDN 博客](https://blog.csdn.net/qq1195566313/article/details/131713875?ops_request_misc=%7B%22request%5Fid%22%3A%22169971691616800197096226%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fblog.%22%7D&request_id=169971691616800197096226&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-131713875-null-null.nonecase&utm_term=electron&spm=1018.2226.3001.4450)

# 1、基本介绍

1、下面是目前大多数跨端桌面程序的对比

![[00 assets/ef70d15df25ef7a4b4d9ed55c28068dc_MD5.png]]

2、当然使用`electron`存在下面的这些优点

​ 2.1 **无兼容性问题**：由于 `Electron` 内置了 `Chromium` 浏览器，所以几乎不需要考虑不同浏览器兼容性问题。与此同时，这也意味着，我们可以使用一些 ES 6/7/8/9/10 的高级语法，比如：async、await、Promise……而不需要 PolyFill。

​ 2.2 **最新浏览器 Feature**：通常情况下，`Electron` 会在新的稳定版本发布后相对快速地更新其 `Chromium` 版本，这也意味着你可以快速体验和使用一些浏览器最新的 `Feature`。比如，通过对图片、iframe 设置 `loading="lazy"` 属性，可以天然支持懒加载：

```html
<img src="image.jpg" alt="..." loading="lazy" />
<iframe src="video-player.html" title="..." loading="lazy"></iframe>
```

​ 2.3 **轻松绕过跨域问题**：在浏览器环境中，作为一个前端开发，经常会碰到各种各样的跨域问题，比如 `iframe` 跨域、`request` 请求跨域……而对于请求类跨域问题通常需要后端配合着设置跨域限制。在 Electron 应用中，由于可以自由地访问本地文件系统和系统资源，也可以通过 Node.js 模块实现对底层操作系统的访问。这种能力使得 Electron 应用可以绕过浏览器的跨域限制，可以在本地环境中自由通信和交互，而无需担心同源策略带来的限制。

​ 2.4 **使用 Node.js 提供的能力**：[Node.js 的所有内置模块](https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2F)在 Electron 中都可用，同时第三方 node 模块也完全支持（包括[本地 native 模块](https://link.juejin.cn/?target=https%3A%2F%2Fwww.electronjs.org%2Fzh%2Fdocs%2Flatest%2Ftutorial%2Fusing-native-node-modules)）。试想一下，有了这个能力，就可以实现前端开发多年的梦想：直接在浏览器中无限制地使用 Node API！

​ 2.5 **客户端能力的支持**：为了弥补 `Node.js` 和前端技术访问系统 `API` 方面的不足，`Electron` 内部对系统 `API` 做了封装，比如：客户端 GUI：右键菜单、窗⼝定制、系统托盘、Dock……；桌⾯环境集成：系统通知、剪切板、系统快捷键、⽂件拖放……；设备 API：电源监视、内存、CPU、屏幕……开发者基于 `Electron` 开发应用时，可以直接使用 `JavaScript` 访问这些 API。

​ 2.6 **调用 OS 能力**：`Electron` 可以通过 Node.js 的 `Child Process` 模块执行系统命令，因此可以间接地调用 `AppleScript`（在 macOS 上）和 `Windows RT`（在 Windows 上）以及一些 `Shell` 脚本。

3、`Electron` 由 `Node.js + Chromium + Native API` 构成。你可以理解成，它是一个得到了 `Node.js` 和基于不同平台的 `Native API` 加强的 `Chromium` 浏览器

![[00 assets/a1d365852093005f2fca0973b179d7fd_MD5.png]]

# 2、基本使用

## 2.1 vue

目前支持 `Vue` 的 `Electron` 工程化工具主要有 [electron-vue](https://link.juejin.cn/?target=https%3A%2F%2Fsimulatedgreg.gitbooks.io%2Felectron-vue%2Fcontent%2Fcn%2F)、[Vue CLI Plugin Electron Builder](https://link.juejin.cn/?target=https%3A%2F%2Fnklayman.github.io%2Fvue-cli-plugin-electron-builder%2F)、[electron-vite](https://link.juejin.cn/?target=https%3A%2F%2Fcn.electron-vite.org%2F)。其中`electron-vue`好久没更新了，这里就不介绍了

### 2.1.1 vue-cli-plugin-electron-builder

1、他是基于`vue-cli`创建的项目，使用`npm install -g @vue/cli`下载脚手架；使用`vue create electron-vue`来创建新的项目；`vue-cli-plugin-electron-builder` 是个 `Vue-cli` 插件，那么就可以使用 `CLI` 命令 `vue add` 的方式进行插件安装

```bash
npm install -g @vue/cli		--下载脚手架
vue create electron-vue		--创建新项目
vue add electron-builder	--添加vuecli插件
```

2、下面是添加了上面的配置后的目录结构

![[00 assets/92905fda2340bd2da0b5c585b8da852a_MD5.png]]

很显然，我们需要为了整体工程化来为目录做调整，`main`放置`主进程代码`，`renderer`放置`渲染进程`代码

![[00 assets/f1fddec67259213dc1794e15e1a2a5da_MD5.png]]

3、修改`vue.config.js`的配置，因为我们修改了默认的目录结构，需要重新指定

![[00 assets/922d7f71c944b44d744cdfd23df45870_MD5.png]]

4、记得修改`package.json`中的`main`入口的文件

![[00 assets/876c975594c42b6a40459d084c49842e_MD5.png]]

5、最后我们再来升级一下`electron`的版本，目前版本最新的是`28`

```bash
npm i electron@28	--升级electron版本
```

6、使用`npm run electron:serve`来开启服务

![[00 assets/f993d037b3b9da61e6ca44dbc3131e50_MD5.png]]

7、如果在使用的过程中发现无法下载`electron`的话，可以设置局部/全局的`.npmrc`，镜像地址为`electron_mirror=https://npmmirror.com/mirrors/electron/`，局部的在文件目录下创建`.npmrc`添加配置即可，全局的在`c盘用户目录`下

![[00 assets/67b6df82dd0a3137b8a23c28f823412c_MD5.png]]

### 2.1.2 electron-vite

1、`electron-vite `全新的 Electron 开发构建工具，为 Electron 提供更快、更精简的开发体验，基于 `vite` 构建 `Electron` 应用。使用`npm create @quick-start/electron`来创建一个`electron`应用，使用`npm run dev`来执行程序

![[00 assets/0f63e381d24ff5f9bd399caac217c349_MD5.png]]

2、使用`createWindow`来创建窗口

3、在窗口初始化时，指定了 `show: false` 的参数，表示窗口创建完成后不会立即显示。然后通过监听 `mainWindow.on('ready-to-show')` 的事件触发后再通过 `mainWindow.show()` 方法来显示窗口。这样是因为 Electron 中的 `ready-to-show` 事件表示窗口内容已经加载完成且应用程序准备好显示给用户。在等待 `ready-to-show` 事件触发后再调用 `window.show()`，可以确保用户看到的是完全加载并准备好的界面，避免了展示未完成的内容。

![[00 assets/fa1f29a0dda910747887f1de87e8ce1c_MD5.png]]

4、通过监听 `app.on('window-all-close')` 事件，来处理非 `macOS` 下的所有窗口关闭后的逻辑：退出整个 electron 应用。这是因为在 `windows` 平台上，通常我们把应用的窗口都关了之后也就默认把这个应用给退出了。而如果在 macOS 系统上却不是这样。我们把应用的窗口关闭了，但是并非完全退出这个应用。

![[00 assets/931a1a39f5bb9e889c0778b1c16b1bc5_MD5.png]]

### 2.1.3 vite 自建

[Vue3 Vite electron 开发桌面程序*vue 桌面应用开发*小满 zs 的博客-CSDN 博客](https://blog.csdn.net/qq1195566313/article/details/131713875?ops_request_misc=%7B%22request%5Fid%22%3A%22169971691616800197096226%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fblog.%22%7D&request_id=169971691616800197096226&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-131713875-null-null.nonecase&utm_term=electron&spm=1018.2226.3001.4450)

1、直接参考 up 主的文章即可，唯一的好处就是可以自己做定义，可以了解其中的原理

2、下面的是`config`的代码

![[00 assets/379eb42e9d5c0d099538dd6c02912f27_MD5.png]]

```typescript
// utils.ts

import fs from "fs";
import path from "path";

// 遍历文件夹下面所有的文件
export type fileInfo = {
  name: string;
  path: string;
};

export const findFiles = (currentDirPath: string, ext: string) => {
  const allFileInfo: fileInfo[] = [];

  const walkSync = (currentDirPath: string, ext: string) => {
    fs.readdirSync(currentDirPath, { withFileTypes: true }).forEach(function (file) {
      const fileName = file.name;
      const filePath = path.join(currentDirPath, fileName);
      if (file.isFile()) {
        // 如果是文件
        if (path.extname(fileName) === `.${ext}`) {
          allFileInfo.push({ name: fileName, path: filePath });
        }
      } else if (file.isDirectory()) {
        // 如果是文件夹，回调
        walkSync(filePath, ext);
      }
    });
  };
  walkSync(currentDirPath, ext);

  return allFileInfo;
};
```

```typescript
// vite.electron.build.ts

import fs from "fs";
import path from "path";

import type { Plugin } from "vite";

import * as electronBuilder from "electron-builder";

import { findFiles } from "./utils";

// 初始化electron函数 - 将ts编译为js使用
const initElectron = () => {
  const allFilePath = findFiles(path.resolve(__dirname, "../src/desktop"), "ts").map((item) => item.path);

  require("esbuild").buildSync({
    entryPoints: allFilePath,
    bundle: true,
    outdir: "dist",
    platform: "node",
    external: ["electron"],
    minify: true // 压缩代码
  });
};

export const viteElectronBuild = (): Plugin => ({
  name: "vite-electron-build",
  closeBundle() {
    // 服务器启动 初始化electron
    initElectron();

    // 修改package.json文件的main字段 不然会打包失败
    const json = JSON.parse(fs.readFileSync("package.json", "utf-8"));
    json.main = "background.js";
    fs.writeFileSync("dist/package.json", JSON.stringify(json, null, 4));

    // 创建一个空的node_modules目录 不然会打包失败
    fs.mkdirSync("dist/node_modules");

    // 使用electron-builder打包Electron应用程序
    electronBuilder.build({
      config: {
        appId: "hh_admin_desktop",
        productName: "七夕诗墙_管理后台",
        directories: {
          output: path.resolve(process.cwd(), "release"), // 输出目录
          app: path.resolve(process.cwd(), "dist") // app目录
        },
        mac: {
          icon: "../public/logo.ico"
        },
        win: {
          icon: "../public/logo.ico"
        },
        linux: {
          icon: "../public/logo.ico"
        },
        asar: true,
        nsis: {
          oneClick: false, // 取消一键安装
          allowToChangeInstallationDirectory: true // 允许用户安装
        }
      }
    });
  }
});
```

```typescript
// vite.electron.dev.ts

// 生产环境的插件
import fs from "fs";
import path from "path";
import { spawn } from "child_process";

import type { AddressInfo } from "net";
import type { Plugin } from "vite";

import { findFiles } from "./utils";

// 初始化electron函数 - 将ts编译为js使用
const initElectron = () => {
  const allFilePath = findFiles(path.resolve(__dirname, "../src/desktop"), "ts").map((item) => item.path);

  require("esbuild").buildSync({
    entryPoints: allFilePath,
    bundle: true,
    outdir: "dist",
    platform: "node",
    external: ["electron"]
    // minify: true // 压缩代码
  });
};

export const viteElectronDev = (): Plugin => ({
  name: "vite-electron-dev",
  configureServer(server) {
    initElectron(); // 服务器启动 初始化electron

    server.httpServer?.once("listening", () => {
      // 获取HTTP服务的监听地址和端口号
      const addressInfo = server.httpServer?.address() as AddressInfo;
      const url = `http://localhost:${addressInfo.port}`;

      // 启动electron进程
      let electronProcess = spawn(require("electron"), ["dist/background.js", url]);

      // desktop/*.ts 文件修改就重新编译使用
      const allFilePath = findFiles(path.resolve(__dirname, "../src/desktop"), "ts").map((item) => item.path);
      allFilePath.forEach((item) => {
        fs.watchFile(item, () => {
          electronProcess.kill(); // 杀死当前electron进程
          initElectron(); // 重新编译

          // 重新启动electron进程
          electronProcess = spawn(require("electron"), ["dist/background.js", url]);
        });
      });

      // 监听打印日志
      electronProcess.stdout.on("data", (data) => {
        if (data) console.log(`日志: ${data.toString()}`);
      });
    });
  }
});
```

我们再来设置一下`config`的配置

![[00 assets/dbb39f809b3975264f5199453bade436_MD5.png]]

## 2.2 react

# 3、主进程/渲染进程

## 2.1 基本介绍

1、Electron 继承了来自 Chromium 的多进程架构，Chromium 始于其主进程。从主进程可以派生出渲染进程。渲染进程与浏览器窗口是一个意思。主进程保存着对渲染进程的引用，并且可以根据需要创建/删除渲染器进程。每个 Electron 的应用程序都有一个主入口文件，它所在的进程被称为 `主进程（Main Process）`。而主进程中创建的窗体都有自己运行的进程，称为 `渲染进程（ Renderer Process）`。**每个 Electron 的应用程序有且仅有一个主进程，但可以有多个渲染进程**。

2、简单来说浏览器默认就存在一个主进程，该主进程就是管理下面的渲染进程，并且主进程是是作为入口存在的

![[00 assets/76f69f95bd211fef86c9b330832fd36d_MD5.png]]

## 2.2 主进程

### 2.2.1 基本使用

1、通常情况下`package.json`中的`main`就是主进程

![[00 assets/34c9d6cad42af2ee0f893b12db4612da_MD5.png]]

2、它是应用程序的入口点，负责管理整个应用的`生命周期、创建窗口、原生 API 调用`等。主进程可以访问底层的系统资源，如文件系统、操作系统 API 等，这些功能通常是通过 Node.js 提供的模块实现的。它是 Electron 应用的主要控制中心

![[00 assets/3679d1add1cae1dbe190b5b93485d737_MD5.png]]

### 2.2.2 窗口创建

1、主进程的主要目的之一是使用 [BrowserWindow](https://link.juejin.cn/?target=https%3A%2F%2Fwww.electronjs.org%2Fzh%2Fdocs%2Flatest%2Fapi%2Fbrowser-window) 模块创建和管理应用程序窗口，窗口管理是指创建、控制和管理应用程序中的窗口

2、跟`app`模块一样，`BrowserWindow`也有很多常用的事件钩子，比如：

- `closed` 当窗口被关闭的时候。
- `focus` 当窗口被激活的时候。
- `show` 当窗口展示的时候。
- `hide` 当窗口被隐藏的时候。
- `maxmize` 当窗口最大化时。
- `minimize` 当窗口最小化时。

![[00 assets/ed6e94038bcb27f9bd663a3765e554f1_MD5.png]]

### 2.2.3 原生 API

1、为了使 Electron 的功能不仅仅限于对网页内容的封装，主进程也添加了自定义的 API 来与用户的操作系统进行交互。比如，和 `客户端 GUI` 相关的 `右键菜单、窗⼝定制、系统托盘、Dock……`，和 `桌⾯环境集成` 相关的`系统通知、剪切板、系统快捷键、⽂件拖放……`，和 `设备` 相关的`电源监视、内存、CPU、屏幕` 等等

![[00 assets/2aaa759c26e7c795804a307c4b24f2e9_MD5.png]]

### 2.2.4 生命周期

1、`app` 的常用生命周期钩子如下，其余的可以参考官方文档：[app | Electron (electronjs.org)](https://www.electronjs.org/zh/docs/latest/api/app)

- `will-finish-launching` 在应用完成基本启动进程之后触发。
- `ready` 当 electron 完成初始化后触发。
- `window-all-closed` 所有窗口都关闭的时候触发，在 windows 和 linux 里，所有窗口都退出的时候**通常**是应用退出的时候。
- `before-quit` 退出应用之前的时候触发。
- `will-quit` 即将退出应用的时候触发。
- `quit` 应用退出的时候触发

2、而我们通常会在 `ready` 的时候执行创建应用窗口、创建应用菜单、创建应用快捷键等初始化操作。而在 `will-quit` 或者 `quit` 的时候执行一些清空操作，比如解绑应用快捷键。特别的，在非 `macOS` 的系统下，通常一个应用的所有窗口都退出的时候，也是这个应用退出之时。所以，可以配合 `window-all-closed` 这个钩子来实现

![[00 assets/ce003e08d3220de4b2046f0ab3297fdf_MD5.png]]

## 2.3 渲染进程

### 2.3.1 remote

1、`渲染进程`是 Electron 应用程序中负责展示用户界面的部分。每个渲染进程对应一个窗口（BrowserWindow）或者一个网页

2、**渲染进程**与**主进程**是分开的，它们之间通过 **IPC（进程间通信）**来进行通信。在 `Electron` 中，因为安全性等问题的考量，提供给 `Renderer` 可用的 `API` 是比较少的，下面是主进程和渲染进程的 API 区别图

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032342404.png" alt="image-20240121232443581" style="zoom: 50%;" />

3、如上图能够在渲染进程中使用的 API 一共有 7 个。那么如果需要在渲染进程中使用主进程的 API 要怎么操作呢？`Electron` 提供了一个库 `@electron/remote`，使用这个库可以用来调用主进程的一些 API 能力

4、使用`npm install --save @electron/remote`来下载库，我们需要在主进程中来做初始化

![[00 assets/51319932bc54d401f39032bbf520ae83_MD5.png]]

后续可以在渲染进程中使用该`API`，可以参考对应的库：[@electron/remote - npm (npmjs.com)](https://www.npmjs.com/package/@electron/remote)

![[00 assets/1f0933ca947aacc9718bc292d3bf2858_MD5.png]]

5、**electron v14** 版本后开始去掉了内置的 `remote` 模块，`@electron/remote` 是 Electron 中内置 remote 模块的替代品。之所以移除 `remote` 模块，其主要是因为：

1. **性能问题：** 通过 `remote` 模块可以访问主进程的对象、类型、方法，但这些操作都是跨进程的，跨进程操作性能上的损耗可能是进程内操作的几百倍甚至上千倍。假设你在渲染进程通过 `remote` 模块创建了一个 `BrowserWindow` 对象，不但你创建这个对象的过程很慢，后面你使用这个对象的过程也很慢。小到更新这个对象的属性，大到使用这个对象的方法，都是跨进程的。
2. **安全性问题：** 使用 `remote` 模块可以让渲染进程直接访问主进程的模块和对象，这可能导致一些潜在的安全风险。因为这种方式打破了主进程和渲染进程之间的隔离，可能存在恶意代码利用这一特性进行攻击或者不当操作。
3. **影子对象问题：** 我们在渲染进程中通过 `remote` 模块使用了主进程的某个对象，得到的是这个对象的影子（代理），是一个影子对象，它看起来像是真正的对象，但实际上不是。首先，这个对象原型链上的属性不会被映射到渲染进程的代理对象上。其次，类似 `NaN`、`Infinity` 这样的值不会被正确地映射给渲染进程，如果一个主进程方法返回一个 `NaN` 值，那么渲染进程通过 `remote` 模块访问这个方法将会得到 `undefined`。

### 2.3.2 preload

1、**预加载**（preload.js）在渲染进程中执行，并且先于网页加载。 在 `preload.js` 中，我们可以使用 `Node API`、 `Electron 渲染进程的 API` 和 `DOM API`。可以通过 `IPC` 和主进程进行通信达成调用主进程模块的目的

![[00 assets/53332c508d09aab7cee24b8435073a6c_MD5.png]]

预加载脚本可以在 `BrowserWindow` 构造方法中的 `webPreferences` 选项里被附加到主进程

![[00 assets/07299679d319591d4041317b5a88e0de_MD5.png]]

2、所以我们可以在`preload.js`中修改`window`来添加一些`渲染进程API`和`nodejs API`。但是自从 `Electron v12` 版本以后，添加了 `webPreferences.contextIsolation = true` 的默认设置，这就意味着你通过 `preload` 修改 `window` 上的内容后，在渲染进程（此处指的网页 window）中并不能访问到

![[00 assets/7f952a334e49f76a3ab4193db9bd77da_MD5.png]]

3、`contextIsolation` 是 Electron 中一个重要的安全特性，用于提高渲染进程的安全性。它的作用在于将渲染进程的 JavaScript 上下文（代码执行环境）与主进程隔离开来，以减少安全风险并加强安全性。

假设有一个 `Electron` 应用程序，其中有一个渲染进程需要执行一些文件系统操作，比如读取本地文件并在界面中显示。在未启用 `contextIsolation` 的情况下，渲染进程可以直接访问 Node.js 的 `fs` 模块来进行文件操作。但这样会存在安全风险，因为渲染进程可以执行任意的文件系统操作，**比如文件删除**，可能导致安全漏洞或恶意代码执行。

如果启用了 `contextIsolation`，渲染进程无法直接访问 Node.js 的 `fs` 模块。这个时候你就可以使用 `preload` 选项来为渲染进程加载一个预加载的脚本，在这个脚本中可以安全地访问 Node.js 的 `fs` 模块，并将需要的操作通过 [contextBridge](https://link.juejin.cn/?target=https%3A%2F%2Fwww.electronjs.org%2Fzh%2Fdocs%2Flatest%2Fapi%2Fcontext-bridge) 模块封装成 API 提供给渲染进程。这样，渲染进程只能通过预加载的 API 来请求文件操作，而无法直接执行文件系统操作。

# 4、进程通信
