# 1. 基本介绍

1、bun 基于 Zig 语言来搭建，并且使用 JSC 来作为底层引擎
- JavaScriptCore 引擎有更快的启动速度和更少的内存占用，但是执行效率会底一点
- V8 作为引擎，运行会快很多，但是内存占用相对就高了

2、bun还是一个包管理工具，而且几乎支持目前市面上所有的包
![[00 assets/4ed92bc5ac397e3742dd027eca4e6d77_MD5.jpeg]]
bun 支持测试运行器、EMS和CommonJS的兼容、支持浏览器API
![[00 assets/4cce9dc3e7a201b2df091747c72b53cb_MD5.jpeg]]
bun 还是构建工具、天生支持TS
![[00 assets/e5749c64a5530751426944ff7a69c2d9_MD5.jpeg]]
还可以配置 `--watch` 天生支持热更新
![[00 assets/c705a436ed41b94af93703dc08eb0ec1_MD5.jpeg]]
能够使用顶层await、支持webAPI，天生支持TS和JSX

3、性能对比，bun确实快很多


# 2. 基本使用

![[00 assets/46556c4e33d7989cdadb65ae8739c744_MD5.jpeg]]


# 3. Elysia框架



