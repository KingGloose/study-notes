文章链接：[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605?scrollMenuIndex=1)

# 1. 基本介绍

## 1.1 基础介绍

1、开发 `node` 应用有 3 个层次：

​ 1.1 直接用 `http`、`https` 包的 `createServer api`

​ 1.2 使用 `express`、`koa` 这种处理请求响应的库

​ 1.3 使用 `nest`、`egg`、`midway` 这类企业级框架

2、下面是一整套前后端的架构，可以参考里面的技术，这也是一个后端的常规架构图

![[00 assets/4bc232197f46fd2c6ab8fe96599ab450_MD5.png]]

3、Nestjs 包含下面的核心概念

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032344337.png" alt="image-20231219082955321" style="zoom:67%;" />

4、`Nest` 并不和 `Express` 耦合，你可以轻松切换到 `Fastify`，这就是因为它用了`适配器`的设计模式

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032344356.png" alt="image-20231026101454018" style="zoom:67%;" />

## 1.2 IOC 介绍

文章介绍：[Nest.js 入门 —— 控制反转与依赖注入（一） - 掘金 (juejin.cn)](https://juejin.cn/post/7085614364396355598)

![[00 assets/848ec7bf39730907ffa5e730299169ab_MD5.png]]

1、使用下面的写法就是一个耦合度比较低的写法，因为`Person`的`playGame`，并且和`Phone`强耦合

![[00 assets/1ce075eadd6b96d1cb6faee7caa2f94c_MD5.png]]

2、为了解决这个问题，我们就可以使用`DI`的思维模式来解决这个问题，也就是下面的代码的实现

![[00 assets/fd839404e3998a0b8379c3d27b06b890_MD5.png]]

3、如果想要模拟注解的模式，可以参考下面的代码运行

![[00 assets/ceb39ac902fb00c23a3d2ef367beea54_MD5.png]]

## 1.3 Express 关系

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7235068983614341177?enter_from=course_center&utm_source=course_center)

# 2. 基本使用

## 2.1 nestjs/cli

1、项目开发离不开工程化的部分，比如`创建项目`、`编译构建`、`开发时 watch 文件变动自动构建`等。`Nest` 项目自然也是这样，所以它在 `@nestjs/cli` 这个包里提供了 `nest` 命令。可以直接 `npx` 执行，`npm` 会把它下载下来然后执行：

```bash
npx @nestjs/cli new 项目名		  // 不推荐
```

2、也可以安装到全局，然后执行，更推荐这种，不过后者要时不时升级下版本，不然可能用它创建的项目版本不是最新的

```bash
npm install -g @nestjs/cli		// 下载nestjs/cli
nest new 项目名				  // 创建新的nest项目

npm update -g @nestjs/cli		// 更新nestjs/cli
```

### 2.1.1 nest -h

如果使用`nest -h`就可以看到`nest/cli`提供的各项功能

![[00 assets/4873574fa21b9436e03e1cba3bfe7375_MD5.png]]

### 2.1.2 nest new xxx

1、使用`nest new 项目名`用于创建一个新的`nest`项目，使用`nest new -h`就可以查看`nest new xxx`的命令

![[00 assets/6c8ee0e503de08174904bdb9bb64a653_MD5.png]]

2、`--skip-git` 和`--skip-install` 很容易理解，就是跳过 `git 的初始化`，跳过 `npm install`，我们也可以简写为`-g`和`-s`

3、`--package-manager` 是`指定包管理器工具`，创建项目的时候会让我们自己选择，我们也可以手动选择，这样就跳过了包选择

![[00 assets/d9f4db497776930deba76196cd262d00_MD5.png]]

4、`--language` 可以指定 `typescript` 和` javascript`，一般我们都选择 `ts`，用默认的就好。

5、`--strict` 是指定 `ts` 的编译选项是否`开启严格模式`的，也就是这么 5 个选项会变为`true`

![[00 assets/08d20671835a7e9c32d2a085f96451c1_MD5.png]]

6、其中`nest new xxx`的本质就是使用的`nest g application`，只不过`nest new xxx`做了额外的`git`和`install`等的操作

![[00 assets/37a623f76b380c99fa35e2b286bc86d3_MD5.png]]

### 2.1.3 nest generate xxx

1、我们使用`nest generate -h`可以看到大部分的指令

![[00 assets/bb09dae050fc6dc18a06070d6108e33a_MD5.png]]

其中有一个`@nestjs/schematics`的包，如果你打开它的源码就可以看到本质就是基于`模版引擎填充变量`，这个在`nodejs`的笔记中有介绍使用

![[00 assets/6eccbfab5cf778b63d00ce9bdd77e527_MD5.png]]

2、使用`nest generate module xxx`，会自动创建`module`模块

![[00 assets/2c78dfca214551620ccf07633433585b_MD5.png]]

并且会自动导入更新进入`app.module.ts`中

![[00 assets/4afe978fe19c865c0285f26850f8505d_MD5.png]]

3、对应的`nest generate controlle xxx`和`nest generate service xxx`也是一样的效果

![[00 assets/774f15046a3f761a46704728d257b8ae_MD5.png]]

4、当然，如果是要完整生成一个模块的代码，不需要一个个生成，可以用`nest generate resource xxx`。它会让你选择是哪种代码，因为 `nest` 支持 `http、websocket、graphql、tcp` 等，其中 `http` 表示 `REST 风格 api`

![[00 assets/cd96a58df76f712c12ee4933bb13bf29_MD5.png]]

然后会让你选择是否生成 `CRUD` 代码

![[00 assets/1e4a8d96f1d94e75afa64c38c20202ff_MD5.png]]

下面就是生成的`REST + CRUD`的代码

![[00 assets/6af766579e148fc0614f22fccda91447_MD5.png]]

5、`--flat` 和 `--no-flat` 是指定是否生成对应目录

6、`--spec` 和 `--no-spec` 是指定是否生成测试文件

7、`--skip-import` 是指定不在 `AppModule` 里引入

### 2.1.4 nest build

1、使用`nest build`会实现编译打包的功能

![[00 assets/01b134e8865c7baaae3afa7a9be4ddc3_MD5.png]]

如果我们输入`nest build -h`就可以看到大部分的指令

![[00 assets/37c900c686290025a895390a6bb5ef41_MD5.png]]

2、`--wepback` 和 `--tsc` 是指定用什么编译，默认是 `tsc 编译`，也可以切换成 `webpack`，下面为`tsc`打包目录

![[00 assets/fffad95c7eb5a8c840735e2c5e167447_MD5.png]]

下面是使用`webpack`打包后的目录，`tsc 不做打包、webpack 会做打包`，两种方式都可以。node 模块本来就不需要打包，但是**打包成单模块能提升加载的性能**。

![[00 assets/f049ed14aa95ddc018ed933359112067_MD5.png]]

3、`--watch` 是监听文件变动，自动 build 的。但是 `--watch` 默认只是监听 `ts、js` 文件，加上 `--watchAssets` 会连别的文件一同监听变化，并输出到 `dist` 目录，比如 `md、yml` 等文件。

![[00 assets/878a46bb85b0d67d0a0dbed872942869_MD5.png]]

4、`--path` 是指定 `tsc` 配置文件的路径的，`--config` 是指定 `nest cli` 的配置文件

### 2.1.5 nest-cli.json

**配置信息**：[json.schemastore.org/nest-cli](https://json.schemastore.org/nest-cli)

1、`nest-cli.json`是`nest`的配置文件，上述的所有的配置信息都可以在`nest-cli.json`中找到并且配置

2、`compilerOptions` 里设置 `webpack` 为 `true` 就相当于 `nest build --webpack`，`webpack` 设置为` false` 就是用 `tsc` 了

3、`deleteOutDir` 设置为 `true`，每次 `build` 都会都清空 `dist` 目录

4、剩下的配置可以查看官网的解释

![[00 assets/6c365818d7f08ee04a040e3d24494175_MD5.png]]

### 2.1.6 nest start

1、我们使用`nest start -h`可以看到该命令

![[00 assets/cea49ce4ee0cb676993033481c96c80a_MD5.png]]

2、`--watch`改动文件之后自动重新 build，并且运行

3、`--debug` 是启动调试的 `websocket 服务`，用来 `debug`

![[00 assets/8b112c1808de23c4799b93a53e0ad497_MD5.png]]

4、`--exec` 可以指定用什么来跑，默认是用 `node` 跑，你也可以切换别的 `runtime`

5、其余选项和 `nest build` 一样，就不复述了

### 2.1.7 nest info

`nest info` 命令，这个就是查看项目信息的，包括`系统信息、 node、npm 和依赖版本`

![[00 assets/c5863b1e7ac3d54b7006ed4e89b3683e_MD5.png]]

### \* 扩展

> nest 使用 webpack 打包后加载性能更好，为什么 nest 要默认使用 tsc 编译

![[00 assets/d5f8ea7caa6dc1de41261c4d8a5ba950_MD5.png]]

1、`tsc`和`babel`之间区别不是很大，`tsc`支持更多的语法，`babel`则有更多的语言特性

文章参考：[编译 ts 代码用 tsc 还是 babel？ - 掘金 (juejin.cn)](https://juejin.cn/post/7084882650233569317)

![[00 assets/e67d03c97d41fa264a4f9254d82d2088_MD5.png]]

2、之前使用的`glup`编译的，后面`ts`支持了`project reference`之后，提升了`rebuild`的性能。而且提供了更好的调试效果

文章参考：[Nest.js 这么大的项目是怎么优化 ts 编译性能的？ - 掘金 (juejin.cn)](https://juejin.cn/post/7181462211964076093)

![[00 assets/697f9c7ea36a975bccf6a92deca7b808_MD5.png]]

## 2.2 项目运行

### 2.2.1 基本运行

1、使用下面的命令来简单的运行

```
nest new xxx			// 创建nest项目
nest g resource xxx		// 创建xxx CRUD接口
nest start -w 			// 启动项目并且监听
```

2、使用`http`测试也是可以接受到的

![[00 assets/e4c3130b0cbf9746664da69f665fadf1_MD5.png]]

### 2.2.2 静态资源部署 - ESModule 导出 Node 模块

1、导出`NestExpressApplication`类型，并且在创建的时候作为`create`的泛型传入，不然会出现编译时报错

2、使用`app.useStaticAssets()`来部署静态资源，下面的 2 种方式都可以

​ 2.1 第一种方式默认取得根目录下面得`public`，而不是`src`中得

​ 2.2 第二种方式就是`nodejs`中得`path`模块来处理位置，我个人更倾向于第二种方式，更加灵活

![[00 assets/b7a74ca207cad862a65b31fc75513ed4_MD5.png]]

3、对于`nestjs`中导入`nodejs`原生得模块存在很多得问题，例如上面得案例`import path from "path"`来默认导出`path`模块，在标准得`node.js`中是可以实现得，但是在`nestjs`就存在这个问题

4、我使用`tsc`将编译后得代码看了一眼，发现编译后得代码变成了`path.default.resolve`，所以会出现`path`为输出为`undefined`得情况，这就导致默认没找到模块

![[00 assets/93006ea067fe24fbc4665dd27cd69318_MD5.png]]

5、后续我查找发现，是因为`tsc`编译`ESModules`和`CommonJS`得区别，下面为文章的解释，参考文章：[esModuleInterop 是如何影响 tsc 的 - 掘金 (juejin.cn)](https://juejin.cn/post/7138308695900815373)

最后得出结果，如果在`tsconfig.ts`中配置`esModuleInterop`就需要对应的修改`import`的模式，ts 中导入一个 `CommonJS 模块`最佳实践仍然是：

- `esModuleInterop = false`，使用 `import * as XX`语法

* `esModuleInterop = true`，使用 `import XX from 'XX'`语法

![[00 assets/c4c3ca4ec535834d15e9ee058840b06e_MD5.png]]

6、深入的了解可以查看`前端技术记录`的文档

## 2.3 调试项目

node 调试文章参考：[nodejs 各种姿势断点调试 - 掘金 (juejin.cn)](https://juejin.cn/post/6844904193489125390)

> node 调试 - 浏览器调试

1、正常都是使用`console.log`来调试项目代码，如果只是小型项目其实还好，如果是比较大型的项目就会导致无法看到执行过程

2、`--inspect` 是调试模式运行，而 `--inspect-brk` 会在首行断住调试，可以看到下面输出了一个`websocket`的地址

![[00 assets/a8ab7ace8e6b23ae9a878dca13830306_MD5.png]]

3、我们再浏览器输入`edge://inspect`，如果是谷歌的话就是`chrome://inspect`，可以看到这里有一个`Remote Target`

![[00 assets/7d7ef8f98539b436440156f4d8b947c0_MD5.png]]

4、这样我们就可以在浏览器中调试该`node.js`代码了

![[00 assets/dfc27ead0c4e2c436509d6573cf60f59_MD5.png]]

> node 调试 - vscode 调试

1、在`nodejs`项目中打上断点，在`vscode`中执行`运行和调试`，即可调试`node代码`

![[00 assets/0eac715adf3af40cd03eb17a1dd483da_MD5.png]]

2、还有一种方式就是创建`launch.json`，但是比较麻烦，需要的时候再去处理

> nest 调试 - 浏览器调试

1、在需要的地方打上`debugger;`，使用`nest start --debug`，在浏览器中输入`edge://inspect`，即可进入调试模式

![[00 assets/5d5f7ee3bee1c9e15c22739c4552bb7a_MD5.png]]

![[00 assets/f140fb07aaf0b473d5f3a22f44ac35e9_MD5.png]]

> nest 调试 - vscode 调试

1、其中一个方式就是配置`lanuch.json`，然后再来运行，我感觉比较麻烦，如果需要使用这种方式的时候再去查询

2、这里介绍比较简单的方式，进入`package.json`，将鼠标放在`start:dev`上，进行`调试脚本`即可

![[00 assets/2380a1d9b0956516b08a5e65e59210b5_MD5.png]]

3、打上断点即可开始调试

![[00 assets/eb2601de6c5c587af2c1fc89f8539ec3_MD5.png]]

# 3. Provider

## 3.1 useClass

1、使用`@Injectable()`装饰器表示可以注入到任意的地方，比方说下方的处理方式，不仅仅只是注入`appService`，还可以注入`personService`

2、在`providers`中编写`PersonService`是简写，如果写完整的话就是`{ provide: PersonService, useClass: PersonService }`，其中`provide`参数表示注入时的`唯一标识token`，而`useClass`表示注入时使用的`class`，`IOC`会自动实例化该类

3、如果默认使用简写形式`PersonService`，那么在`AppController`构造器中，直接写参数即可。如果你修改了`AppService`的名字为`app_service`，那么就需要编写`@inject("app_service")`来注入

![[00 assets/45cb8150de80c5f4fdec71237034c6ba_MD5.png]]

4、如果觉得`构造器`注入比较麻烦，还可以尝试一下`属性`注入的模式

![[00 assets/ce960e7cdfcc15c6db63702a27285e55_MD5.png]]

## 3.2 useValue

1、我们可以使用`useValue`来注入固定参数

![[00 assets/3e0bf828fbbdd9b91290b5b9495375ba_MD5.png]]

## 3.3 useFactory

1、使用`useFactory`可以支持动态传入数据

![[00 assets/e8fa85a2b10ced37a76ee20e8965749c_MD5.png]]

2、因为`useFactory`是一个函数，所以我们使用它的形参动态传入参数也可以

3、使用`inject`数组来动态传入`providers`中提供的`token标识`即可传入到`useFactory`中，而且`inject`中数组的是一一对应到`useFactory`中的参数，和名称无关

4、而且需要注意的一点是，动态传入`service`，类型必须一一对应。例如下面：你要传入`AppService`，形参就必须是`AppService`类型，不然无法导入

5、还需要注意一点，`inject`中的`token`必须是`providers`中存在的，如果不存在不能导入

![[00 assets/dc4a296c5ea409da08e2c5a124c1fd1a_MD5.png]]

6、`useFactory`也支持异步注入参数，使用这样的方式会存在导入延迟，也就是`10s`之后`useFactory`正常注入之后，该系列接口才能正常使用

![[00 assets/ca3b8cf32ef69aca8e04719333d7c267_MD5.png]]

## 3.4 useExisting

1、使用`useExisting`可以给`provide`取别名，这样就可以换一个`token标识`来使用了

![[00 assets/ac7a8bef53740393ac11f021744ca18e_MD5.png]]

# 4. 模块导入

## 4.1 局部导入

一般情况下可以使用下面的 2 种模式来导入对应的模块，一致就是使用`exports`和`import`来导入使用，另外一种就是`Provider`

来导入。注意区别，并且需要注意`imports`导入的是`Module`，`provider`导入的是`Service`

> 使用 export 和 imports 引入

1、我们可以将需要的模块使用`exports`导出，在需要的模块中使用`imports`引入即可

![[00 assets/3bc392d2f299e251ce0c072d025a8cee_MD5.png]]

2、在构造器中引入即可使用

![[00 assets/649e7fbeb6fac894b6956eb5f3d1513b_MD5.png]]

> 使用 providers 引入

![[00 assets/cf43249cbb12d271627d3ae91a7a643b_MD5.png]]

## 4.2 全局导入

1、因为上面需要一个个局部导入太麻烦了，我们可以使用`@Global()`来全局导入，注意依旧要使用`exports`

2、但是我们可以不使用`imports`来导入

![[00 assets/2049265a47f75e024bf6e6272cdb489d_MD5.png]]

3、不导入，依旧可以使用。不过全局模块还是尽量少用，不然注入的很多 `provider` 都不知道来源，会降低代码的可维护性。

![[00 assets/50bbae340ee979093cc7d24728a498e0_MD5.png]]

# 5. 生命周期

![[00 assets/3c4d07aef3b7c76c9c3d877380caaf62_MD5.png]]

> `onModuleInit`和`OnApplicationBootstrap`

1、首先，递归初始化模块，会依次调用模块内的 `ontroller、provider` 的 `onModuleInit` 方法，然后再调用 `module` 的 `onModuleInit` 方法。全部初始化完之后，再依次调用模块内的`controller、provider` 的 `onApplicationBootstrap` 方法，然后调用 `module` 的 `onApplicationBootstrap` 方法，然后监听网络端口。之后 `Nest` 应用就正常运行了。

2、使用的时候记得继承一下`onModuleInit`和`OnApplicationBootstrap`

3、他会依次解析`controllers`和`providers`下面的生命周期

![[00 assets/257cbdda73e49649c2f664f3a5d088f1_MD5.png]]

![[00 assets/a7e29e8114bd400a8f964cdfdcd0ffff_MD5.png]]

4、生命周期依次是`onModuleInit`和`onApplicationBootstrap`来执行

5、`onModuleInit`是在解析主机模块的依赖项后调用，而`onApplicationBootstrap`是在所有模块初始化后调用，但在监听连接之前，注意生命周期的区别

![[00 assets/e69ff98e287da7cb36e7f29a43b54956_MD5.png]]

> onModuleDestroy 和 beforeApplicationShutdown

1、先调用每个模块的 `controller、provider 的 onModuleDestroy` 方法，然后调用`Module` 的 `onModuleDestroy` 方法。之后再调用每个模块的 `controller、provider 的 beforeApplicationShutdown` 方法，然后调用 `Module` 的 `beforeApplicationShutdown` 方法。然后停止监听网络端口。之后调用每个模块的 `controller、provider 的 onApplicationShutdown` 方法，然后调用 `Module` 的 `onApplicationShutdown` 方法。之后停止进程。

2、剩下的本质就和上面的一致，这里就不去赘述了

![[00 assets/91aa0450815a194b1d4bd6dbcd1d20ba_MD5.png]]

3、为了测试，所以可以在`main.ts`中设置`app.close()`来关闭当前服务，app.close() 只是触发销毁逻辑，但不会真正退出进程

![[00 assets/7c73e31090d2142951e44926b6268e2f_MD5.png]]

4、`beforeApplicationShutdown` 是可以拿到 `signal` 系统信号的，比如 `SIGTERM`。这些终止信号是别的进程传过来的，让它做一些销毁的事情，比如用 `k8s 管理容器`的时候，可以通过这个信号来通知它

![[00 assets/59c6370e346c282bd349fb3362171b93_MD5.png]]

5、下面是使用`@nestjs/typeorm、@nestjs/mongoose`库的写法，可以看到，一般都是通过 `moduleRef` 取出一些 provider 来销毁，比如关闭连接。这里的 `moduleRef` 就是当前模块的对象。

![[00 assets/26e7e2e0d100e25ad3430e0664a8283b_MD5.png]]

# 6. Module

## 6.1 moduleRef

1、使用`moduleRef`可以获取当前的`module`对象，这样就可以获取通过当前模块做其他操作

![[00 assets/07aae27f6b5fe4a50cc40472bd8d2c00_MD5.png]]

2、可以看到获取到的`Test01Service`已经被调用了

![[00 assets/cc993a9003e37d89fa6547f9b2786054_MD5.png]]

## 6.2 forwardRef

1、下面意思是在解析 `Test01Module` 的时候，它的第一个 imports 是 undefined。这有两个原因，一个是这个值本来就是 undefined，第二个就是形成了循环依赖

2、其中依赖循环就是下图，`appModule`引入`Test01Module`会自动递归创建它的依赖，而它的依赖又依赖了这个 `Test02Module`，所以没法创建成功，拿到的就是 undefined

![[00 assets/4be13051b42f6eb164eac7e5bb25b515_MD5.png]]

3、这个时候就需要`forwardRef`来处理，这样就可以正常运行了

![[00 assets/22179e9828af5d6d0141e65bd5955223_MD5.png]]

4、`nest` 会单独创建两个 `Module`，之后再把 `Module` 的引用转发过去，也就是 `forwardRef` 的含义

![[00 assets/a14ccf77698e7b938e1937897048bd1a_MD5.png]]

5、也可能存在`Service`相互引用的情况，依旧使用`forwardRef`来解决即可

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345858.png" alt="image-20231120112142375" style="zoom:80%;" />

## 6.3 动态模块

### 6.3.1 register

1、我们创建了一个`bbb.module`，可以发现他是静态的，但是我们可以将他配置成动态的

![[00 assets/30de5cfcf0c1c94dadc53fe8372ffaf6_MD5.png]]

2、将原本的`module`改为成下面的模式进行注册，这样我们就可以实现了一个动态模块的创建，并且为该动态模块写入了参数

![[00 assets/277f3872a04021b524c7476f9c654ed6_MD5.png]]

传入动态模块的参数可以直接注入

![[00 assets/af1f9ecda3d042ca633d7198a02efba4_MD5.png]]

3、这里的 register 方法其实叫啥都行，但 nest **约定**了 3 种方法名：register、forRoot、forFeature。我们约定它们分别用来做不同的事情，注意是约定，不是强制：

- **register**：用一次模块传一次配置，比如这次调用是 BbbModule.register({aaa:1})，下一次就是 BbbModule.register({aaa:2}) 了

- **forRoot**：配置一次模块用多次，比如 XxxModule.forRoot({}) 一次，之后就一直用这个 Module，一般在 AppModule 里 import

- **forFeature**：用了 forRoot 固定了整体模块，用于局部的时候，可能需要再传一些配置，比如用 forRoot 指定了数据库链接信息，再用 forFeature 指定某个模块访问哪个数据库和表。

4、下面就是一个`forRoot`和`forFeature`的例子，`forRoot`用于配置全局的`typeorm`，而`forFeature`用于配置局部的`entity`

![[00 assets/f51dbfe141f8b6a0b318d4ce22a14732_MD5.png]]

### 6.3.2 builder

1、不仅仅是上面的动态模块创建的方式，我们还可以使用`builder`的方式，在目录下创建`ccc.module-definition.ts`的文件，使用`builder`构造函数创建`ConfigurableModuleClass`，我们再将需要使用动态模块进行继承即可

2、对于`builder`默认的注册方法是`register`，如果我们想要设置为别的可以使用`setClassMethodName()`

3、如果还想使用额外参数该如何处理，可以使用`setExtras`，这里使用的是全局模块的判断

![[00 assets/079c61d60891f05b9627ce9333a25ab0_MD5.png]]

4、`forRoot`默认是从下往上执行的，所以最后的结果是`{ name: "cccModule", ... }`，并且最后注入使用

5、这里的注入参数使用的`builder`导出的参数，这样有更好的类型推断，也就是`typeof OPTIONS_TYPE`

![[00 assets/c468c0186d1cb543643a38114595f224_MD5.png]]

# 7. AOP

## 7.1 基本介绍

1、`MVC` 是 `Model View Controller` 的简写。`MVC 架构`下，请求会先发送给 `Controller`，由它调度 `Model 层`的 `Service` 来完成业务逻辑，然后返回对应的 `View`

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345939.png" alt="image-20231119101939226" style="zoom: 50%;" />

2、在这个流程中，`Nest` 还提供了 `AOP （Aspect Oriented Programming）`的能力，也就是面向切面编程的能力。AOP 是什么意思呢？什么是面向切面编程呢？一个请求过来，可能会经过 `Controller（控制器）、Service（服务）、Repository（数据库访问）` 的逻辑

如果想在这个调用链路里加入一些通用逻辑该怎么加呢？比如`日志记录、权限控制、异常处理`等。容易想到的是直接改造 Controller 层代码，加入这段逻辑。这样可以，但是不优雅，因为这些通用的逻辑侵入到了业务逻辑里面。能不能透明的给这些业务逻辑加上日志、权限等处理呢？那是不是可以在调用 Controller 之前和之后加入一个执行通用逻辑的阶段呢？比如这样：

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345712.png" alt="image-20231119102131930" style="zoom: 80%;" />

3、AOP 的好处是可以把一些通用逻辑分离到切面中，保持业务逻辑的纯粹性，这样切面逻辑可以复用，还可以动态的增删。其实 Express 的中间件的洋葱模型也是一种 AOP 的实现，因为你可以透明的在外面包一层，加入一些逻辑，内层感知不到。而 Nest 实现 AOP 的方式更多，一共有五种，包括 Middleware、Guard、Pipe、Interceptor、ExceptionFilter。

## 7.2 Middleware

### 7.2.1 全局中间件

1、因为我们使用的是基于`Express`，所以也提供了全局中间件的处理方式

![[00 assets/1779f71e888f7414b21433a580cee7d5_MD5.png]]

2、这部分可以参考`nodejs`中`express`的笔记，基本是一致的

![[00 assets/cc993a9003e37d89fa6547f9b2786054_MD5.png]]

### 7.2.2 路由中间件

1、使用`nest g middleware log --no-spec --flat`可以自动生成`middreware`文件，`--no-spec 是不生成测试文件，--flat 是平铺，不生成目录`

2、我们来打印对应的`log`日志，如果使用可以在`modules`中使用`configure`来注册，`forRoutes`就是用于区分对应的路由，如果你不在`forRoutes`中编写路由的话就是全局生效

![[00 assets/96fc53c157075fff7494032a99127993_MD5.png]]

3、如果你添加了路由的话就只会匹配对应路由去执行中间件，`test01*`表示`test01`开头的路由，`test01/queryLog`也可以匹配

![[00 assets/9b61a8c91d4da126cbcff2d1a80d7c80_MD5.png]]

4、**注意**，一般情况下是在`app.module`中去注册，即便如上图在`test01.module`中注册也是可以正常运行

![[00 assets/19b60dbd95391516d64654727e27b00b_MD5.png]]

## 7.3 guard

Guard 是路由守卫的意思，可以用于在调用某个 Controller 之前判断权限，返回 true 或者 false 来决定是否放行

![[00 assets/e6218909fa7ba4514dabc0559dbde8a0_MD5.png]]

### 7.3.1 @UseGuard

1、我们可以使用`nest g guard login --no-spec --flat`来创建一个`guard`，创建出来的`guard`如下图

2、在对应的路由使用`@UseGuards`注解即可使用

![[00 assets/ed888d030e0d21d403db57d8752e4df7_MD5.png]]

3、可以看到整个路由就访问不到了，因为`Guard`输出为`false`。这个就特别适合做接口`token`鉴权使用

![[00 assets/ca6989190ce4c0a1e23c80b223b2b330_MD5.png]]

### 7.3.2 全局使用

1、如果是全局可以使用`useGlobalGuards`来为每个路由都注入`guard`

![[00 assets/05bdbb8c2c75975ece19a66e8630cfc0_MD5.png]]

2、还有一种全局注入的方式，就是在`app_modules`中使用`providers`来注入，`provider`必须是`APP_GUARD`才能全局生效

![[00 assets/f0185a5c024b51e54af7473488125b5f_MD5.png]]

3、存在上面 2 种方式来全局注入，他们之间有什么区别吗？第一种方式是手动 `new 的 Guard 实例`，不在 `IoC 容器`里，而用 `provider`的方式声明的 `Guard` 是在 `IoC 容器`里的，可以注入别的 `provider`

4、这个时候就有疑问了，如果有些路由不需要做`guard`的话，那不是没办法了，这个在后续的代码中有方法来介绍

![[00 assets/6f290f9feb3f02751873eb142daea126_MD5.png]]

### 7.3.3 ExecutionContext

1、`ExecutionContext` 是 `ArgumentHost` 的子类，扩展了 `getClass、getHandler` 方法

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345812.png" alt="image-20231119201051896" style="zoom:67%;" />

2、其中`getClass`和`getHandler`是分别获取`Controller`和`执行函数`

![[00 assets/0b7b0dd9be6aab24098ef20cc3e2c792_MD5.png]]

3、这个参数最常见的使用方式就是作为获取`metadata`来做权限判断，我们自定义一个注解来注入`metadata`参数

![[00 assets/df6725f7b03ab6a5f5683a323c8e87eb_MD5.png]]

![[00 assets/0be25888b04363723a7a1d5d5252428f_MD5.png]]

4、使用自定义的注解`@Roles()`为接口定义`matedata`参数，这个就可以判断该接口的权限范围了

5、使用`reflector`来获取当前`Handler`的`metadata`，并且取出参数

6、如果该接口存在权限注解就进行判断，没有就放行。因为`ExceptionContext`继承自`ArgumentsHost`，所以自然存在`switchToHttp()...`函数

![[00 assets/03a97bad8d6d22c2ac0b0f6cfc82edb0_MD5.png]]

7、因为**Interceptor**也存在`ExceptionContext`，所以和上述一致

## 7.4 Interceptor

### 7.4.1 基本使用

> 单路由级别

1、使用`nest g interceptor time --no-spec --flat`来创建一个`Interceptore`

2、`Interceptor` 要实现 `NestInterceptor` 接口，实现 `intercept` 方法，调用 `next.handle()` 就会调用目标 `Controller`，可以在之前和之后加入一些处理逻辑。`Controller` 之前之后的处理逻辑可能是异步的。`Nest` 里通过 `rxjs` 来组织它们，所以可以使用 `rxjs` 的各种 `operator`

3、[RxJS 中文版](https://rxjs.tech/)，如果对`rxjs`感兴趣的话可以查看下该库的`API`

4、`Interceptor`主要和`Middleware`类似，但是存在一定的区别

![[00 assets/f1f4dcef05445ff9fdf56a9208b6e0ca_MD5.png]]

> Controller 级别

1、可以在`Controller`级别添加也可以生效

![[00 assets/4be13051b42f6eb164eac7e5bb25b515_MD5.png]]

2、因为注入到了`ioc容器`了，所以也可以注入对应的`Service`

![[00 assets/048e99bf91b1f8f5c69d45056b14cfd6_MD5.png]]

> 全局使用 - main.ts 使用 use - 不进入 IOC 容器

1、并不推荐使用这样的方式来注入，因为并不进入 IOC 容器

![[00 assets/ab1c6539675c892ec2e1ebf3ebc16332_MD5.png]]

> 全局使用 - app.module - 进入 IOC 容器

1、在`app.module`中全局注册，可以引入其他的`provider`来使用，其他和`guard`类似

![[00 assets/308eec46bd5c24de255a2b8dcef71487_MD5.png]]

2、也是比较推荐使用这个方式来全局引入`Interceptor`，因为使用这种方式可以进入`ioc容器`中，这样我们就可以注入服务了

![[00 assets/dcfc46cf20eed7b0ab9dcc8b427f22b7_MD5.png]]

### 7.4.2 middleware 区别

1、`Interceptor 和 Middleware` 差不多，其实是有区别的，主要在于`参数`的不同。`Interceptor` 可以拿到调用的 `controller 和 handler`，后面我们会在 `controller 和 handler` 上加一些 `metadata`，这种就只有 `Interceptor或者 guard` 里可以取出来，`middleware` 不行。

2、其中`middleware`更加适合通用的逻辑

![[00 assets/0b7b0dd9be6aab24098ef20cc3e2c792_MD5.png]]

### 7.4.3 rxjs 使用

> map

1、`map`对响应数据做修改，一般都是改成 `{code, data, message} `的格式

![[00 assets/69ee31122b4bcd6d13fa2bf2e2c09575_MD5.png]]

> tap

1、`tap`不修改响应数据，执行一些额外逻辑，比如记录日志、更新缓存等

2、`new Logger(xxx.name)`表示创建一个`nestjs`日志

![[00 assets/8b112c1808de23c4799b93a53e0ad497_MD5.png]]

> catcherror

1、`catchError`在 `exception filter` 之前处理抛出的异常，可以记录或者抛出别的异常

![[00 assets/f0185a5c024b51e54af7473488125b5f_MD5.png]]

> timeout

1、`timeout`处理响应超时的情况，抛出一个 `TimeoutError`，配合 `catchError` 可以返回超时的响应

![[00 assets/35b9ddc84fe59e2ac9e4d61960df500d_MD5.png]]

## 7.5 Pipe

### 7.5.1 基本使用

> 单路由级别

1、`Pipe` 是管道的意思，用来对参数做一些检验和转换，可以使用`nest g pipe validate --no-spec --flat`来创建

![[00 assets/77711964840d8c9edc482bbb6c08220d_MD5.png]]

![[00 assets/45836d974146d105523312801aa6b148_MD5.png]]

2、`Pipe` 要实现 `PipeTransform` 接口，实现 `transform` 方法，里面可以对传入的参数值 `value` 做参数验证，比如格式、类型是否正确，不正确就抛出异常。也可以做转换，返回转换后的值

![[00 assets/77b4d23882078afcbbe36c28ff69a4b3_MD5.png]]

3、下面的实现方式就是通过`pipe`来解析对应的参数，如果参数是数字就 \* 10，如果不是就报错

![[00 assets/f06a3fc4373f62303495c64b1f7abfd9_MD5.png]]

![[00 assets/1dbf3ca4a081685086474948fd2cc434_MD5.png]]

![[00 assets/7f7ac0775d33a86cbc7d181a1a031b4a_MD5.png]]

> controller 级别

1、可以使用`controller`级别的`pipe`

![[00 assets/545bd3c695830d5c7f6004bc5d3b0197_MD5.png]]

2、当然我们也可以为`pipe`注入参数

![[00 assets/eaf1b37f8d6c2a88c0301ddcb7f15e61_MD5.png]]

对应的`@Body`注解不能使用`new`的方式来创建，这个时候交给`ioc容器`即可

![[00 assets/27a53a472859cf7a1ba29776e2bafb49_MD5.png]]

> 全局级别

1、和上述的`guard`类似，也是存在 2 种方式来创建

![[00 assets/9b61a8c91d4da126cbcff2d1a80d7c80_MD5.png]]

2、并且注意全局级别真的是全局生效，即便不写也可以使用，默认为每个参数注解添加`pipe`

![[00 assets/382e66d59dc663edef0fb7069dafaee2_MD5.png]]

### 7.5.2 内置 Pipe

#### 7.5.2.1 ParseIntPipe

1、使用`ParseIntPipe`可以将参数转为`int`类型

![[00 assets/3cf93882af8b48f62ac30d4fe8f327be_MD5.png]]

2、如果传入的参数不能转为数字类型，就会报错

![[00 assets/958b42b21a9a7cb218e32d34e6d65fb3_MD5.png]]

3、我们也可以`new ParseIntPipe()`来创建`pipe`，并且可以在创建的适合传入参数

![[00 assets/c7158f44d282cbf26c5e056a19cf31f6_MD5.png]]

4、使用`exceptionFactory`可以手动执行`Exception`，并且抛出错误，查看下方信息可以看到错误信息被改了

![[00 assets/b47db04cf758864947fdd24f6e9c4298_MD5.png]]

![[00 assets/35cec286225649f426bbf9399be90df8_MD5.png]]

5、当然我们传入`optional`的时候表示可以将该参数设置为`undefined`，也就是可以为空

![[00 assets/af1f9ecda3d042ca633d7198a02efba4_MD5.png]]

#### 7.5.2.2 ParseFloatPipe

1、和`ParseIntPipe`使用方式类似，可以转为`flaot`类型

![[00 assets/4064a271c3220a5e2d3491b0547c3647_MD5.png]]

#### 7.5.2.3 ParseBoolPipe

![[00 assets/9b61a8c91d4da126cbcff2d1a80d7c80_MD5.png]]

#### 7.5.2.4 ParseArrayPipe

1、他会提示需要下载`class-transformer`：它是把普通对象转换为对应的 class 实例的包，`class-validator`：可以用装饰器和非装饰器两种方式对 class 属性做验证的库，`pnpm i class-transformer class-validator -d`

2、他会自动将下面的的字符转化，因为我使用`reduce`，所以会他会进行字符串的拼接

![[00 assets/b02a3219732be82efe39e20ecb422c3b_MD5.png]]

3、需要进行下面的`items`配置将数组里面的各个数值转为`number`类型

![[00 assets/dda246ac997b1ae538da78df31ec5472_MD5.png]]

4、我们可以手动配置`:::`分隔符`separator`来切割数组转为对应的类型

![[00 assets/76237463c282f82e3792181cbe38b3cb_MD5.png]]

#### 7.5.2.5 ParseEnumPipe

1、使用`parseEnumPipe`可以传入枚举类型

2、我们查看下面传入的参数和返回的参数，不是一样的吗？但是使用下面的方式也是有好处，(1) 只能在枚举类型内才能使用，不然会报错 （2）自动转类型

![[00 assets/c9532e9df81a10df8d11fc2c15a65d42_MD5.png]]

#### 7.5.2.6 ParseUUIDPipe

1、可以校验`uuid`

![[00 assets/2021dce8a82a162526a7addb471d7d47_MD5.png]]

#### 7.5.2.7 DefaultValuePipe

1、可以设置默认值，如果没有参数的话会使用默认值

![[00 assets/94912649be6c669d40b8f99d5aa89d57_MD5.png]]

#### 7.5.2.8 ValidationPipe

> 自定义

1、下面就是自定义一个`ValidationPipe`，并且使用到了`class-validator`和`class-transformer`这 2 个库，其中`class-validator`是使用注解的方式做验证，`class-transformer`是做对象转化

参考文章：[在学习 nestjs 的过程中，我学到了 class-transform - 掘金 (juejin.cn)](https://juejin.cn/post/6844904117115027463)

![[00 assets/2422a42a998307fa5a6761a78dcd5fbf_MD5.png]]

![[00 assets/8fe6876abf8c2c30ae6ca46924d06200_MD5.png]]

> ValidationPipe

2、一般情况下会使用他自带的`ValidationPipe`，自己写的不一定完整，上面只是实现的大致原理

3、如果想要实现对应的类的参数验证就可以使用`class-validator`，可以为类添加注解验证

![[00 assets/e6538ac57fd4a5d046f216e3c10e7caa_MD5.png]]

> class-validator

4、当然对应`class-validator`也存在很多的参数验证的注解

![[00 assets/711413f761177031111c59c467f4a1f8_MD5.png]]

5、当然我们也可以自定义错误的消息

![[00 assets/6bca4f0bf84922582ae1202471da041d_MD5.png]]

#### 7.5.2.9 ParseFilePipe

1、当然`nestjs`提供了对应的`pipe`来做参数验证，里面也封装好了很多的`validator`，直接使用即可

![[00 assets/09b8b5c7d39753e6fc365d1e417dc398_MD5.png]]

2、我们也可以自定义错误提示类型，使用`exceptionFactory()`

![[00 assets/4ac029f4281c024021f15a5f9bbb9546_MD5.png]]

3、不仅仅使用内置的`filevalidator`，我们也可以自定义`validator`

4、这样就存在 2 个方式来检测文件 （1）直接写一个`filepipe`，参考`2.基本使用 / 2.4 参数解析 / 2.4.5 form-data`的笔记即可 （2）直接使用`parseFilePipe`来检测，不仅仅可以使用内置的`validator`还可以使用自定义的`validator`

![[00 assets/83e83afba28219d1231a3233ccd7f221_MD5.png]]

## 7.6 ExceptionFilter

### 7.6.1 基本使用

1、不管是 `Pipe、Guard、Interceptor` 还是最终调用的 `Controller`，过程中都可以抛出一些异常，如何对某种异常做出某种响应呢？这种异常到响应的映射也是一种通用逻辑，Nest 提供了 `ExceptionFilter` 来支持，`ExceptionFilter` 可以对抛出的异常做处理，返回对应的响应

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345359.png" alt="image-20231119153736350" style="zoom:67%;" />

![[00 assets/28e7521baf951e286b28744030267ab7_MD5.png]]

2、我们在`pipe`中`throw`的错误就是`ExceptionFilter`

![[00 assets/88642ece30e7cf244cca76073fce0aed_MD5.png]]

3、我们使用`@UseFilters`就可以抛出对应的错误

![[00 assets/9835e5b251f1e31459f337c584745afb_MD5.png]]

4、如果使用自定义`Exception Filter`的话，可能会和`pipe`冲突，所以为了解决这个问题，我们需要做下面的修改，单独添加一个`message`属性来做处理

![[00 assets/a24cf0225ca1f71fad24313f38f6dc31_MD5.png]]

5、不仅如此，你也可以自定义一个`Exception`

![[00 assets/94ea1709dfa92a184ec68a23afd59eb2_MD5.png]]

> Controller 级别

![[00 assets/75a342a3ca5181d0becc4939f4785212_MD5.png]]

> 全局使用

1、依旧可以用这 2 种方式来全局使用，当然在`app.module`中可以使用`app_filter`来全局注入，这样就进入到了`ioc容器`中来做处理

![[00 assets/53ddab14434f49bf319af87def8b469c_MD5.png]]

### 7.6.2 ArgumentsHost

**ArgumentHost 是用于切换 http、ws、rpc 等上下文类型的，可以根据上下文类型取到对应的 argument**。

1、`Nest` 支持创建 `HTTP 服务`、`WebSocket 服务`，还有`基于 TCP 通信的微服务`。这些不同类型的服务都需要 `Guard、Interceptor、Exception Filter` 功能。那么问题来了：不同类型的服务它能拿到的参数是不同的，比如 `http 服务`可以拿到 `request、response` 对象，而 ws 服务就没有，如何让 `Guard、Interceptor、Exception Filter` 跨多种上下文复用呢？`Nest` 的解决方法是 `ArgumentHost` 和 `ExecutionContext` 类

2、我们可以自定义`Expection`

![[00 assets/db601397f46bfa6a566e6b64c42ecf54_MD5.png]]

3、这样我们注入了`Filter`之后，直接`throw new mainException`即可自定义抛出错误的信息

![[00 assets/efbacf825ec5981acc09a352fa4d6a8e_MD5.png]]

4、`catch`有 2 个参数，第一个是自定义的错误数据，第二个就是通信类型上下文实例了

![[00 assets/29a3c25f0f892c4afc18d81415760ccb_MD5.png]]

修改配置即可调试对应的`nestjs`文件

![[00 assets/c7251a37c3ba7d9cc7082d75de82b676_MD5.png]]

```json
{
    "type": "pwa-node",
    "request": "launch",
    "name": "debug nest",
    "runtimeExecutable": "npm",
    "args": [
        "run",
        "start:dev",
    ],
    "skipFiles": [
        "<node_internals>/**"
    ],
    "console": "integratedTerminal",
}
```

5、在 `debug console` 输入 `host`，可以看到它有这些属性方法，`host.getArgs 方法`就是取出当前上下文的 `reqeust、response、next` 参数。因为当前上下文是 `http。host.getArgByIndex` 方法是根据下标取参数

![[00 assets/774f15046a3f761a46704728d257b8ae_MD5.png]]

![[00 assets/8f5ac82b937be69ccaec4f00c331cbea_MD5.png]]

这种按照下标取参数的写法不太建议用，因为不同上下文参数不同，这样写就没法复用到 `ws、tcp` 等上下文了，一般是这样来使用的

![[00 assets/94ea1709dfa92a184ec68a23afd59eb2_MD5.png]]

如果是 `ws`、`基于 tcp 的微服务`等上下文，就分别调用 `host.swtichToWs`、`host.switchToRpc` 方法。这样，就可以在 filter 里处理多个上下文的逻辑，跨上下文复用 filter 了

6、一般情况是使用下面的方式来传递数据

![[00 assets/8d7fd29b845d3bbcd9b4d3c1be668955_MD5.png]]

![[00 assets/c4989020c15d0da0a41c4512eddce608_MD5.png]]

## 7.7 AOP 执行顺序

![[00 assets/311ee479588e0e9d7f6550466bdb641d_MD5.png]]

# 8. 装饰器

## 8.1 常见装饰器

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7234726536342372412?scrollMenuIndex=1)

下面是`nestjs`所有的装饰器

- @Module： 声明 Nest 模块
- @Controller：声明模块里的 controller
- @Injectable：声明模块里可以注入的 provider
- @Inject：通过 token 手动指定注入的 provider，token 可以是 class 或者 string
- @Optional：声明注入的 provider 是可选的，可以为空
- @Global：声明全局模块
- @Catch：声明 exception filter 处理的 exception 类型
- @UseFilters：路由级别使用 exception filter
- @UsePipes：路由级别使用 pipe
- @UseInterceptors：路由级别使用 interceptor
- @SetMetadata：在 class 或者 handler 上添加 metadata
- @Get、@Post、@Put、@Delete、@Patch、@Options、@Head：声明 get、post、put、delete、patch、options、head 的请求方式
- @Param：取出 url 中的参数，比如 /aaa/:id 中的 id
- @Query: 取出 query 部分的参数，比如 /aaa?name=xx 中的 name
- @Body：取出请求 body，通过 dto class 来接收
- @Headers：取出某个或全部请求头
- @Session：取出 session 对象，需要启用 express-session 中间件
- @HostParm： 取出 host 里的参数
- @Req、@Request：注入 request 对象
- @Res、@Response：注入 response 对象，一旦注入了这个 Nest 就不会把返回值作为响应了，除非指定 passthrough 为 true
- @Next：注入调用下一个 handler 的 next 方法
- @HttpCode： 修改响应的状态码
- @Header：修改响应头
- @Redirect：指定重定向的 url
- @Render：指定渲染用的模版引擎

## 8.2 自定义装饰器

### 8.2.1 @SetMetadata

#### 8.2.1.1 基本使用

> @SetMetadata

1、我们可以使用`@SetMetadata`来设置`metadata`，但是这样的方式太传统了

![[00 assets/f2f39075456eac9e7c0f5483d57e82ca_MD5.png]]

> 自定义装饰器 - @SetMetadata

1、使用`nest g decorator Test01 --no-spce --flat`来创建一个自定义装饰器，这样就简化成这样了

![[00 assets/8db00e6b722616bd06cea9d2b1aa8240_MD5.png]]

2、如果该`metadata`是`Controller`级别的，就需要使用`getClass`来获取

![[00 assets/daf72840af21f6e0d27efada76ee4fb1_MD5.png]]

#### 8.2.1.2 reflector

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7235075295521275965)

### 8.2.2 合并装饰器

1、我们可以使用`applyDecorators`来合并多个装饰器，效果是一样的

![[00 assets/7e706c2cd33d442debe434fecc0909db_MD5.png]]

### 8.2.3 参数装饰器

1、使用`createParamDecorator`来创建一个参数装饰器，第一个参数为`key`，第二个为`ExecutionContext`

![[00 assets/5eb7e0043091cc813cbb459b78ed20f4_MD5.png]]

2、这样那些内置的 `@Param、@Query、@Ip、@Headers 等装饰器`，我们是不是能自己实现了，下面就是实现的`@Headers`的功能

![[00 assets/7e877bd80685c5e3ba861b29cb971fa3_MD5.png]]

3、我们也可以实现`@Query`装饰器

![[00 assets/796ce9fdb6b31b9962cd2ec95fccaf01_MD5.png]]

4、我们也可以在该参数装饰器中配置对应的`pipe`，来对参数做校验。对于设置参数校验我们有上述的 2 种方式，第二种就是使用`@UsePipes`做参数校验，但是他就会校验该`handler`下面的所有参数，写在里面的只会校验内部的

![[00 assets/36a6fed37c1f27a7a32eec63e519058b_MD5.png]]

我们换成内置的也是可以进行校验处理

![[00 assets/61821d497e79d35ba7c864bf69e21afc_MD5.png]]

# 9. 参数解析

## 9.1 HTTP 参数

对于前端来说，后端主要是提供 http 接口来传输数据，而这种数据传输的方式主要有 5 种：`url param`、`query`、`form-urlencoded`、`form-data`、`json`

### 9.1.1 url param

1、我们可以把参数写在 `url` 中，`http://guang.zxg/person/1111`，这里的 `1111` 就是路径中的参数（url param），服务端框架或者单页应用的路由都支持从 url 中取出参数

### 9.1.2 query

1、通过 url 中 ？后面的用 & 分隔的字符串传递数据，`http://guang.zxg/person?name=guang&age=20`，这里的 name 和 age 就是 query 传递的数据。

2、其中非英文的字符和一些特殊字符要经过编码，可以使用 `encodeURIComponent` 的 `api` 来编码，

```js
const query = "?name=" + encodeURIComponent('光') + "&age=20"

// ?name=%E5%85%89&age=20
```

3、或者使用`query-string`库来处理

```js
const queryString = require('query-string');
queryString.stringify({
  name: '光',
  age: 20
});

// ?name=%E5%85%89&age=20
```

### 9.1.3 form-urlencoded

1、直接用 form 表单提交数据就是这种，它和 query 字符串的方式的区别只是放在了 `body` 里，然后指定下 `content-type` 是 `application/x-www-form-urlencoded`。

2、因为内容也是 `query` 字符串，所以也要用 `encodeURIComponent` 的 api 或者 `query-string` 库处理下。这种格式也很容易理解，`get` 是把数据拼成 `query` 字符串放在 `url` 后面，于是表单的 `post` 提交方式的时候就直接用相同的方式把数据放在了 `body` 里。通过 `&` 分隔的 `form-urlencoded` 的方式需要对内容做 `url encode`，如果传递大量的数据，比如上传文件的时候就不是很合适了，因为文件 `encode` 一遍的话太慢了，这时候就可以用`form-data`

![[00 assets/54cb87937b1373d7c2f9c82f43ebc14c_MD5.png]]

### 9.1.4 form-data

1、`form data` 不再是通过 `&` 分隔数据，而是用 `--------- + 一串数字`做为 `boundary 分隔符`。因为不是 url 的方式了，自然也不用再做 `url encode`。

2、`form-data` 需要指定 `content type` 为 `multipart/form-data`，然后指定 `boundary` 也就是分割线。`body` 里面就是用 `boundary 分隔符`分割的内容。很明显，这种方式适合`传输文件`，而且可以传输多个文件。但是毕竟多了一些只是用来分隔的 boundary，所以请求体会增大。

![[00 assets/8f5ac82b937be69ccaec4f00c331cbea_MD5.png]]

### 9.1.5 json

1、`form-urlencoded` 需要对内容做 `url encode`，而 `form data` 则需要加很长的 `boundary`，两种方式都有一些缺点。如果只是传输 json 数据的话，不需要用这两种。可以直接指定`content type` 为 `application/json` 就行：

![[00 assets/18edb89a7a06b66cd5bbd3cb04026d7b_MD5.png]]

## 9.2 参数解析

### 9.2.1 url param

1、`Controller("/api/person")`表示请求的地址，`@Get(":id")`表示`url Param`的参数，最后拼接为`/api/person/:id`

2、`@Param("id")`表示接收的`url param`参数

![[00 assets/370f90653058f12ac3e94dd25f59f2a5_MD5.png]]

### 9.2.2 query

1、其基础的使用方式和上述差不多，使用`@Query`来接收`query参数`

![[00 assets/172aad591b3395c0e2a17e50afe25a65_MD5.png]]

### 9.2.3 form-urlencoded

> dto 类

1、一般情况下是在该接口下面创建一个`dto文件夹`，下面专门创建`xxxdto`类来实现参数的映射，再使用`@body`装饰器来实现`body`参数的传递

![[00 assets/b4e6e017fa9696250fda03953f7b8ede_MD5.png]]

2、当然不只是使用`xxxdto`类来映射，我们使用`type`或`interface`也是可以的

![[00 assets/850ee7364686bbed2dd7e82df448da19_MD5.png]]

3、如果更加极端一点，可以不去使用类型去做参数映射也是可以，只是类型推导默认为`any`

![[00 assets/57ebe1b97f20fd13ec11deecf48c7af2_MD5.png]]

### 9.2.4 json

1、传递`JSON`也是和`form-urlencoded`是一样的

2、后端代码同样使用 `@Body` 来接收，不需要做啥变动。`form urlencoded` 和 `json` 都是从 `body` 取值，Nest 内部会根据 `content type` 做区分，使用不同的解析方式

![[00 assets/77711964840d8c9edc482bbb6c08220d_MD5.png]]

### 9.2.5 form-data

#### 9.2.5.1 传递参数

1、因为也是在`body`中，所以直接使用`@Body`装饰器即可获取参数

![[00 assets/45836d974146d105523312801aa6b148_MD5.png]]

2、当然我们也可以为`@Body`添加参数校验，这里需要注意一定都是`IsString`，因为`form-data`默认传输的就是`string`

![[00 assets/731e267885b26df79a5126800b2e614b_MD5.png]]

#### 9.2.5.2 传递文件

##### 9.2.5.2.1 基本使用

1、目前用的都是`Express`的接口。传递文件的话，需要下载`npm i @types/multer -save-dev`类型文件，才会有`Express.Multer.File`的类型提示

2、`Nest` 解析 `form data` 使用 `FilesInterceptor` 的拦截器，用 `@UseInterceptors 装饰器`启用，然后通过 `@UploadedFiles` 来取。非文件的内容，同样是通过 `@Body` 来取

![[00 assets/62e2c290d23d7cbd64256d6e6dea2445_MD5.png]]

3、当然还有其他的`FileInterceptor`，`info`表示`form-data`的名，`dest`表示保存的地址

![[00 assets/61d060c67028a1a0043b786033c11800_MD5.png]]

![[00 assets/bfb53e37e5690cdfcb1b12828f5279fe_MD5.png]]

4、当然我们也可以接收多个参数，就是将`FileInterceptor`修改为`FilesInterceptor`，如果需要接收也需要修改

![[00 assets/6043873190f216aecd1dfd3653c9b675_MD5.png]]

5、如果我们需要上传多个参数不同的文件，使用`FileFieldsInterceptor`来设置参数

![[00 assets/e088e4a2e898d50e30dfea7fbf618b11_MD5.png]]

> 限制上传文件大小

1、第一种最简单的方式就是结合`multer`来处理

![[00 assets/34d66025f61cded65b6168014ecf6d97_MD5.png]]

2、第二种方式就是使用`pipe`来做处理，但是这种方式有一个弊端，他会先保存文件到磁盘之后再去提示报错，这不可避免的造成了文件磁盘的浪费，以及服务器流量的浪费

![[00 assets/51ae5788868af1db3cd529b8ed7f7611_MD5.png]]

3、一般情况下`nestjs`帮我们封装好了对应的 API，这里可以选择直接使用，相应的使用请参考`pipe/ParseFilePipe`的笔记

> 手动集成 multer 的 storage

![[00 assets/00aa800d41bfce9362906f04dadfdfce_MD5.png]]

##### 9.2.5.2.2 分片上传

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7284435949386694708)

##### 9.2.5.2.3 oss 上传

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7324620995183968293)

# 10. 日志

## 10.1 基本使用

1、使用`new Logger()`即可使用`nestjs`配置好的`logger`

2、这里的 `verbose、debug、log、warn、error` 就是日志级别，而 `[]` 中的是 `context`，也就是当前所在的上下文，最后是日志的内容

![[00 assets/2a2324fe4d3c7ef68590fd53501f26df_MD5.png]]

3、我们也可以设置关闭日志

![[00 assets/90fc6828742c1e71c5a5ad3f89d45a24_MD5.png]]

也可以设置显示的日志等级

![[00 assets/382e66d59dc663edef0fb7069dafaee2_MD5.png]]

## 10.2 自定义日志 - 未完

1、我们也可以自定义日志信息，但是使用这种方式不好看

![[00 assets/434f0364de644dd35ce8492e08f6931d_MD5.png]]

2、不仅仅可以在`create`里面配置，还可以使用`useLogger`函数来配置自定义`logger`

![[00 assets/958b42b21a9a7cb218e32d34e6d65fb3_MD5.png]]

3、这个适合我们可以集成`ConsoleLogger`，这样就可以使用 nestjs 的打印方式来自定义了，因为涉及到了动态模块，这里我就放会之后再看

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7235205849751224380)

## 10.3 集成 winston - 未完

1、下面就是在`nestjs`中集成`winston` 我们需要下载第三方包`pnpm i --save winston`，更多的使用方式可以参考`nodejs/express`中的笔记

![[00 assets/4f45c5efa2f77d77f799c4b84471e833_MD5.png]]

2、我们也可以自定义成`nestjs`的打印风格，可以直接使用`printf`既可以打印

![[00 assets/f2de041cbf5015ef9a04aba4106dbc71_MD5.png]]

3、当然我们也可以使用`transports.File`来保存对应的日志文件

![[00 assets/89bef90b84b035f9baffe231d19b1087_MD5.png]]

4、我们可以将`winston`抽取为一个动态模块，这里没学动态模块，所以暂时不记了，到时候来处理

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7283507588007165952)

# 11. docker

## 11.1 基本使用

参考我的`docker笔记`即可

## 11.2 pm2 启动

1、参考`nodejs`中的`pm2`笔记即可

2、对于`pm2`有一些新的理解，首先`pm2`支持`进程管理、日志管理、负载均衡等`功能，对于日志管理`docker`做的很好，而`进程管理`主流的做法是配置健康检查的接口，一旦健康检查的接口报错了 就会重启`docker`，所以`pm2`可用可不用，基本上应用挂了，`docker`已经重启了，`docker`重启了就等于所有的应用开始初始化了

3、但是对于`负载均衡`这一段我是这样理解的，服务进入`docker`的时候，首先会经过`nginx`的负载均衡，分配到不同的服务器，然后各个不同的服务器中使用`pm2`实现的`多进程服务`，就会进入到不同的进程，实现了单个服务器中的`进程`的`负载均衡`，这样理论上也可以实现性能的提升

4、这里暂时只是我的浅显的理解，其中`pm2`的负载均衡使用`cluster`来实现的，有时间的话会研究一下

![[00 assets/4064a271c3220a5e2d3491b0547c3647_MD5.png]]

5、对于这个问题，有对应的解释，如果使用`k8s`可以动态跑多个`docker`容器来动态扩缩容，而对于单个`docker`可以使用`pm2`来做负载均衡，正好解决上面提出的问题

![[00 assets/daa00e97e6d10ccfc5adf94b6ba99a32_MD5.png]]

## 11.3 mysql 安装

1、首先需要在镜像市场下载`mysql`镜像

2、我们需要按照下面的配置，这里我们就使用`mount`挂载卷的方式做持久化存储

3、必须设置参数`MYSQL_ROOT_PASSWORD`，这是数据库的密码

![[00 assets/be3c2ebc5c10efd779d9c3210737c588_MD5.png]]

4、可以看到服务已经跑起来了

5、因为我将`mysql`的文件`mount`到外面了，下次我们再次创建镜像的时候直接再选择挂载的地址，即可继承上一个镜像的数据

![[00 assets/72109d5975c86f1f231e7dc5efed4699_MD5.png]]

## 11.4 redis 安装

1、按照下面配置即可，主要还是`mount`，剩余的参考`mysql`即可

![[00 assets/e619174a8332c9fd4dbe6075835ecefb_MD5.png]]

# 12. 数据库

## 12.1 mysql

### 12.1.1 集成 typeorm

1、先安装对应的环境`npm i --save @nestjs/typeorm typeorm mysql2`来做处理，首先要面对的就是全局使用`typeorm`，这一块在`动态模块`中介绍了

2、在对应的`service`注入`entityManage`即可，就可以实现下述基本的增删改查

![[00 assets/0930a9426530e715d664b7c49ea504d1_MD5.png]]

3、但是上述的使用存在问题，在`entityManager`需要写很多的重复的`entity`，也就是下图中对应的`1 方式`的使用

4、大部分情况下是`entity`使用`forFeature`来做注入，也就是对应的下面的`2 方式`的使用

5、当然我们也可以使用`dataSource`来做注入，但是这样做的比较少，也就是下面的`3 方式`的使用

![[00 assets/d05359837b66de3fac37b19186e882af_MD5.png]]

## 12.2 redis

### 12.2.1 集成 redis

1、我们参考[Clients | Redis](https://redis.io/resources/clients/#nodejs)文档，里面推荐了很多的语言的`redis`库，我们这里选择`node-redis`

2、我们在`app_module`中注入`redis`，这里暂时还没选择全局注入的方式

![[00 assets/09b9ea40ba2a58f93d42b597aeca7318_MD5.png]]

3、注入`redis`连接对象，查询所有的`keys`并且返回

![[00 assets/03a97bad8d6d22c2ac0b0f6cfc82edb0_MD5.png]]

### 12.2.2 集成 cache-manager

1、使用`npm install @nestjs/cache-manager cache-manager`来安装，这里需要注意`cache-manager`是自己在内存中处理，如果要采用`redis`需要额外的库

2、因为目前使用的版本存在问题，`get`一直都是`undefined`，这里我就不写了，使用老师的笔记

3、全局注册之后导入即可，就可以实现内存中的数据写入和导出

![[00 assets/47cbc3de09e647f421556debc6355b0a_MD5.png]]

4、我们使用`cache-manager`提供的`CacheInterceptor`即可实现对参数的缓存，比如我们请求的参数为`http://localhost:3000/get?a=1`，那么他就会缓存`/get?a=1`来对参数进行缓存

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345997.png" alt="image-20240122225536245" style="zoom:50%;" />

5、我们还可以接入`redis`，使用`npm install cache-manager-redis-store`安装

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345698.png" alt="image-20240122225802449" style="zoom:50%;" />

6、但是非常不推荐使用`cache-manager`，因为他只支持`get`和`set`，其余都需要自己手动进行封装，非常的不方便，而且有一个好用的就是`CacheInterceptor`，我们也可以自己手动封装，所以不如只使用`redis`库来做连接

```typescript
import { CACHE_MANAGER } from '@nestjs/cache-manager';
import { CallHandler, ExecutionContext, Inject, Injectable, NestInterceptor } from '@nestjs/common';
import { HttpAdapterHost } from '@nestjs/core';
import { RedisClientType } from 'redis';
import { of, tap } from 'rxjs';

@Injectable()
export class MyCacheInterceptor implements NestInterceptor {
  @Inject('REDIS_CLIENT')
  private redisClient: RedisClientType;

  @Inject(HttpAdapterHost)
  private httpAdapterHost: HttpAdapterHost;

  async intercept(context: ExecutionContext, next: CallHandler) {
    const request = context.switchToHttp().getRequest();
    const key = this.httpAdapterHost.httpAdapter.getRequestUrl(request);
    const value = await this.redisClient.get(key);

    if(!value) {
      return next.handle().pipe(tap((res) => {
        this.redisClient.set(key, res);
      }));
    } else {
      return of(value);
    }
  }
}
```

# 13. 配置读取

## 13.1 基本使用

> dotenv

此处参考`nodejs`笔记，该方式只适合简单的配置

> config

1、如果想要查看更多的配置可以参考：[node-config/node-config: Node.js Application Configuration (github.com)](https://github.com/node-config/node-config)

2、我们可以参考下面的 3 个配置文件，包括`default.json`、`production.json`、`development.json`，其中`pro... dev...`是生成环境和开发环境的配置文件，他会默认覆盖`default.json`中的配置

![[00 assets/1779f71e888f7414b21433a580cee7d5_MD5.png]]

3、因为`windows`中执行设置`node_env`的时候会导致出现问题，所以我们这里引入`cross-env`来执行操作

4、这样我们就可以根据不同的环境来进行配置不同的信息了

![[00 assets/30d0121820598c2efcce96d96ed83f8c_MD5.png]]

> js-yaml

参考上述操作，基本一致，只是配置文件换成了`.yaml`

## 13.2 nestjs 配置

1、`nestjs`不带对应的配置库，需要手动进行下载`npm i @nestjs/config --save`

2、在`app.module.ts`中要进行`ConfigModule`的配置，使用`isGlobal`表示全局注入

![[00 assets/09503994f30b05a45d0e4ab279c02978_MD5.png]]

3、他默认依赖`dotenv`的库，他默认读取`.env`

![[00 assets/048e99bf91b1f8f5c69d45056b14cfd6_MD5.png]]

4、如果要导入配置，可以使用`ConfigService`来进行导入

![[00 assets/0d7f14a2255d371a207f2adf5fd99f05_MD5.png]]

5、最好使用`enum`来做配置名的读取

![[00 assets/bbe1030d7066dc2d5ac803a6b5bdf66b_MD5.png]]

6、详细的参考下面的文章：[Nest 系列（十一）NestJS 环境变量使用大全(长文警告) - 掘金 (juejin.cn)](https://juejin.cn/post/7177407436381388858#heading-1)

7、当然可以也可以使用`config，js.yml...`等库来读取配置

# 14. 登录鉴权

## 14.1 Session

如果想看`koa`的版本，可以查看我`nodejs`中的笔记，这里面也记录了一部分

### 14.1.1 基本介绍

1、给 `http` 添加状态，那就给每个请求打上个标记，然后在服务端存储这个标记对应的数据。这样每个被标记的请求都可以找到对应的数据，自然可以做到**登录、权限**等状态的存储。

2、这个标记应该是自动带上的，所以 http 设计了 cookie 的机制，在里面存储的数据是每次请求都会带上的。然后根据 cookie 里的标记去查找的服务端对应的数据叫做 session，这个标记就是 session 的 id。

3、如图，因为请求自动带上 cookie，那两次请求就都可以找到 id 为 1 对应的 session，自然就知道当前登录的用户是`guang`，也可以存储其他的状态数据。

![[00 assets/b318d6d68e0571bd28606549f1da75a5_MD5.png]]

### 14.1.2 存在问题

> CSRF

1、`cookie` 会在请求时自动带上，那你在一个网站登录了，再访问别的网站，万一里面有个按钮会请求你登录的网站，那么 `cookie` 依然能带上，这个时候你的登录凭证都泄露了，而且一般这种利用 `CSRF 漏洞`的网站都会伪装的很好，让你很难看出破绽来，这种网站叫做钓鱼网站

2、为了解决这个问题，我们一般会`验证 referer`，就是请求是哪个网站发起的，如果发起请求的网站不对，那就阻止掉。但这样依然不能完全解决问题，万一你用的浏览器也是有问题的，能`伪造 referer` 呢？

3、所以一般会用`随机值`来解决，每次随机生成一个值返回，后面再发起的请求需要包含这个值才行，否则就认为是非法的。这个随机值叫做 token，可以放在参数中，也可以放在 header 中，但是不放置在`cookie`中，所以钓鱼网站拿不到这个随机值，也就不存在`CSRF`问题

> 分布式 Session

1、`session` 是把状态数据保存在服务端，那么问题来了，如果有多台服务器呢？当并发量上去了，单台服务器根本承受不了，自然需要做集群，也就需要多台服务器来提供服务。而且现在后端还会把不同的功能拆分到不同的服务中，也就是微服务架构，自然也需要多台服务器。那不同服务器之间的 `session` 怎么同步？

![[00 assets/e915c24ec3abcea34bf0415707ea43a5_MD5.png]]

2、登录之后 session 是保存在某一台服务器的，之后可能会访问到别的服务器，这时候那台服务器是没有对应的 session 的，就没法完成对应的功能。这个问题的解决有两种方案：

​ 2.1 一种是 **session 复制**，也就是通过一种机制在各台机器自动复制 session，并且每次修改都同步下。这个有对应的框架来做，比如 java 的 **spring-session**。各台服务器都做了 session 复制了，那你访问任何一台都能找到对应的 session。

​ 2.2 还有一种方案是把 session 保存在 **redis**，这样每台服务器都去那里查，只要一台服务器登录了，其他的服务器也就能查到 session，这样就不需要复制了。分布式会话的场景，**redis + session** 的方案更常用一点。

> 跨域

1、cookie 为了安全，是做了 `domain 的限制`的，设置 cookie 的时候会指定一个 domain，只有这个 domain 的请求才会带上这个 cookie。而且还可以设置过期时间、路径等。

![[00 assets/4b73bec292536df493b36495af2059f3_MD5.png]]

2、那万一是不同 `domain` 的请求呢？也就是跨域的时候，怎么带 cookie 呢？a.xxx.com 和 b.xxx.com 这种还好，只要把 domain 设置为**顶级域名 xxx.com** 就可以了，那二三级域名不同也能自动带上。但如果顶级域名也不同就没办法了，这种只能在服务端做下中转，把这俩个域名统一成同一个。

​ 2.1 **前端 ajax 请求**：ajax 请求有额外的机制：ajax 请求跨域的时候是不会挟带 cookie 的，除非手动设置 withCredentials 为 true 才可以。

​ 2.2 **后端 header 设置**：而且也要求后端代码设置了对应的 header，这里的 allow origin 设置 \* 都不行，必须指定具体的域名才能接收跨域 cookie。

![[00 assets/bd206c90a0adf3e953346e248b85d30f_MD5.png]]

### 14.1.3 Nest 集成

1、我们需要安装库`npm install express-session @types/express-session`来做集成，因为本质`nest`底层的本质就是`express`

2、`secret` 指定加密的密钥 ；`resave` 为 true 是每次访问都会更新 session，不管有没有修改 session 的内容，而 false 是只有 session 内容变了才会去更新 session；`saveUninitalized` 设置为 true 是不管是否设置 session，都会初始化一个空的 session 对象。比如你没有登录的时候，也会初始化一个 session 对象，这个设置为 false 就好

![[00 assets/7136a35a00adc73c43a2256dbd51dc20_MD5.png]]

3、创建一个`controller`来设置对应的`session`和`cookie`

![[00 assets/d4790f43666430b8e11999f9005aea23_MD5.png]]

我们请求就可以看到加密的`session`，并且每次请求返回的数据都不同，而且返回了一个 `cookie` 是 `connect.sid`，这个就是对应 `session` 的 id。因为 `cookie` 在请求的时候会自动带上，就可以实现请求的标识，给 http 请求加上状态

![[00 assets/194905eb5f9737a880e0df9f4cb6f745_MD5.png]]

## 14.2 JWT

### 14.2.1 基本介绍

1、**token** 的方案常用 json 格式来保存，叫做 json web token，简称 JWT。JWT 是保存在 request header 里的一段字符串（比如用 header 名可以叫 authorization），它分为三部分：**header** 部分保存当前的加密算法，**payload** 部分是具体存储的数据，**verify signature** 部分是把 header 和 payload 还有 salt 做一次加密之后生成的。（salt，盐，就是一段任意的字符串，增加随机性）

2、这三部分会分别做 Base64，然后连在一起就是 JWT 的 header，放到某个 header 比如 **authorization** 中：`authorization: Bearer xxxxx.xxxxx.xxxx`

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345941.png" alt="image-20240122234001805" style="zoom:50%;" />

3、请求的时候把这个 header 带上，服务端就可以解析出对应的 header、payload、verify signature 这三部分，然后根据 header 里的算法也对 header、payload 加上 salt 做一次加密，如果得出的结果和 verify signature 一样，就接受这个 token。也就是分为两步，第一步是解密，第二步是根据参数再去加密一遍防止**伪造 token**

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032345977.png" alt="image-20240122234624986" style="zoom:50%;" />

### 14.2.2 存在问题

1、虽然使用`JWT`解决了`Session`中的`CSRF`、`跨域`、`分布式Session`问题，但是也带来了新的问题。

​ 1.1 **安全性**：因为 `JWT` 把数据直接 `Base64` 之后就放在了 header 里，那别人就可以轻易从中拿到状态数据，比如用户名等敏感信息，也能根据这个 `JWT` 去伪造请求。所以 `JWT` 要搭配 **https** 来用，让别人拿不到 header，因为 https 不是明文的

​ 1.2 **性能**：JWT 把状态数据都保存在了 header 里，每次请求都会带上，比起只保存个 id 的 cookie 来说，请求的内容变多了，性能也会差一些。所以 JWT 里也不要保存太多数据。

​ 1.3 **没法让 JWT 失效**：`session` 因为是存在服务端的，那我们就可以随时让它失效，而 JWT 不是，因为是保存在客户端，那我们是没法手动让他失效的。比如踢人、退出登录、改完密码下线这种功能就没法实现。但也可以配合 redis 来解决，记录下每个 token 对应的生效状态，每次先去 redis 查下 jwt 是否是可用的，这样就可以让 jwt 失效。

### 14.2.3 Nest 集成

#### 14.2.3.1 基本使用

1、首先我们需要导包`npm i @nestjs/jwt`

2、并且该模块是动态模块，导入使用即可。我们不仅仅可以使用`register`注册，还可以使用`registerAsync`来动态请求网络参数，这样，后续就可以动态配置`jwt`的信息

3、`secret` 是加密 jwt 的密钥，`expiresIn` token 过期时间 设置 7 天

![[00 assets/45836d974146d105523312801aa6b148_MD5.png]]

4、我们要使用`Inject`注入`jwtService`，也就是上图中导入的

5、使用`@Headers("authorization")`来获取`headers`中的`authorization`参数

6、使用`@Res()`来获取响应对象，这里要注意一个`{ passthrough: true }`。如果为 `false / 不添加这个参数`，后面`return`就不会生效了，就需要我们手动来处理`Res`的操作，比如手动使用`Res.send()`来发送响应。如果为`true`，表示执行完用户操作之后，再次将处理交给`Nestjs`

7、使用`verify`来解码`token`，使用`sign`来加密 token。下面的代码意思是代码默认在响应的`Headers`中添加`token`，如果有`token`就动态修改值，再发送

8、使用内置的`Execption Filter`来表示非鉴权`execption`

![[00 assets/3f632e9979edda13dacdd2438602c44b_MD5.png]]

#### 14.2.3.2 登录注册
