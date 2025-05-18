# 1. 基本介绍

![[00 assets/26f8c77bd54490a2dce520ea937d7d79_MD5.jpeg]]

# 2. 创建任务

## 2.1 基本使用
![[00 assets/0b4a448ad2c058052f32783f415f3eb9_MD5.jpeg]]

![[00 assets/d4e55e6e0457d83b42d12b3f83b01144_MD5.jpeg]]


1、`gulp` 的本质就是返回函数执行，如果任务执行完毕需要执行 `cb()` 表示任务完成了
2、使用 `npx glup xxx` 可以执行某个任务
![[00 assets/7261064e6867f4627b654e722be208de_MD5.jpeg]]

3、当我们使用 `Promise` 返回的时候，会直接结束，而不是根据 `cb`的回调
![[00 assets/dffb3c3322aa75cfed4998925b71d4cf_MD5.jpeg]]
![[00 assets/f853ab22972ed5b08b16893d28d83172_MD5.jpeg]]

## 2.2 默认任务

1、使用 `module.exports.default` 表示默认任务，直接使用 `npx gulp`就可以执行，而不需要在后面带上`name`
![[00 assets/224a809748e2a00052818a3f293a00e9_MD5.jpeg]]

## 2.3 串/并行任务组合

1、他会像任务队列一样，依次串行执行
![[00 assets/3051e08d4cf508b5e098c1ee3db4407e_MD5.jpeg]]

2、也可以并行任务执行
![[00 assets/b7876aba0c67d552e8ef4be691396ecc_MD5.jpeg]]

# 3. 操作文件

## 3.1 读写文件

![[00 assets/3ff1fbbee439516c600e9da41fdfc894_MD5.jpeg]]
![[00 assets/d7553ee0b68361a0175f6ea441dc9492_MD5.jpeg]]

1、按照如下的方式进行文件读写，再通过`pipe + dest`写入文件
![[00 assets/e232f9a1b4dfe08b1031d5809c4abbe7_MD5.jpeg]]

## 3.2 文件夹监听

1、使用 `watch` 可以监听内容的变化，执行创建的任务
![[00 assets/8b6358dd7c7bb755be4f3a60b5f707e6_MD5.jpeg]]

# 4. 资源处理

1、按照如下的 `gulp`可以针对`html、css、js`来做处理，并且可以将处理的代码插入到`html`中
2、和 `webpack` 几乎一致，按照如下的方式就可以对`JS、css、less`代码进行压缩转换等操作
![[00 assets/efee7f593753553f7c4341f38e5f5d5f_MD5.jpeg]]

3、如果你想下载不同的`plugins`可以参考网站搜索[Plugins | gulp.js](https://gulpjs.com/plugins)
![[00 assets/05fcc73a57f958539b73883bfa9bccc8_MD5.jpeg]]

4、这样我们就可以使用 `parallel、series`来组建打包的构建任务队列
5、因为我们插入的`js、css`需要是相对路径，所以需要针对`injectTask`做额外的配置
![[00 assets/9920afac25577b7cc912a95fc629021a_MD5.jpeg]]

# 5. 本地服务器

1、使用 `browser-sync`来开启本地服务器，初始化做配置，`files`表示监听文件变化就通知浏览器，`server`就是静态代理文件的配置
2、使用`watch()`来监听开发文件，如果变化就重新打包
![[00 assets/c1a48846e95914b7166f3d7e57a19de8_MD5.jpeg]]
