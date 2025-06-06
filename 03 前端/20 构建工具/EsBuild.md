# 1. 基本介绍

## 1.1 esbuild为什么快？

>esbuild 为什么很快？

![[00 assets/d25ec077e767afd4ee756a36195ab3c2_MD5.jpeg]]
1、采用Go语言开发，传统的JS开发的构建工具并不适合资源打包这种CPU密集场景下，Go更具性能优势。而go具有多线程运行能力，而JS本质上就是一门单线程语言。由于go的多个线程是可以共享内存的，所以可以将解析、编译和生成的工作井行化。

2、从一开始就考虑性能，不使用第三方依赖，从始至终是使用的是一致的数据结构，从而避免数据转换无意义的消耗。

3、在JS开发的传统打包工具当中一般会频繁地解析和传递抽象语法树（AST）数据，比如：字符串 -> TS -> JS -> 字符串，然后字符串 -> JS -> 旧的JS -> 字符串，然后字符串 -> JS -> minifiedJS -> 字符串，这其中会涉及复杂的编译工具链，比如webpack -> babel -> terser，每次接触到新的工具链，都得重新解析AST，导致大量的内存占用。

4、针对 esbuild 仅触及整个 JavaScript AST 3次，当AST数据在CPU缓存中仍然处于活跃状态时，会最大化AST数据的重用：
- 进行词法分析，解析，作用域设置和声明符号的过程。
- 绑定符号，最小化语法。比如：将 JSX / TS 转换为 JS。
- AST 生成 JS，source map 生成等

![[00 assets/5084d51fb0032cccb4b39b6cdbeacea9_MD5.jpeg]]


>esbuild 很快，为什么没有大规模普及呢？

![[00 assets/17ae57b90a77b416ce0361525c4416bf_MD5.jpeg]]

>为什么 vite 要使用 esbuild

本质就是快，现在来说，Vite在下面几个地方都依托于 esbuild，而未来随着 esbuild 的完善，应该会做进一步处理
- 依赖预构建：作为 Bundle 工具
- 单文件编译：作为 TS 和 JSX 编译工具
- 代码压缩：作为压缩工具

![[00 assets/afff5505b6a8a5357c78204c1ccb0fe2_MD5.jpeg]]

## 1.2 什么是 no-bundle？

1、本质就是 ESM，不去打包成 bundle，而是直接复用浏览器得动态加载模块得能力，而 Vite 就是提倡 no-bundle，相对于 Webpack，能做到开发得时候不先打包完整再加载

2、这个是传统得 webpack 打包得流程，最终会输出 bundle
![[00 assets/94ef4548c3098eeaaf13a256b126e7e9_MD5.png]]

3、但是针对 ESM 他会依据你的路由来动态加载，而不是一次加载全部
![[00 assets/795ee755724a084f4367d7e741e140b8_MD5.png]]

## 1.3 什么是依赖预构建？

1、模块代码其实分为两部分：业务代码，另一部分是第三方依赖的代码，即node_modules中的
代码。所谓的no-bundle只是对于业务代码而言，对于第三方依赖而言，我们基本不会去改变他，Vite还是选择

2、bundle（打包），这个部分，就依赖于esbuild。但是关键点是，为什么在开发阶段我们要对第三方依赖进行预构建？如果不进行预构建会怎么样？首先Vite是基于浏览器原生ES模块规范实现的DevServer，不论是应用代码，还是第三方依赖的代码，理应符合ESM规范才能够正常运行。但是，我们没有办法控制第三方的打包规范。还有相当多的第三方库仍然没有ES版本的产物。

3、此外，ESM还有一个比较重要的问题一一请求瀑布流问题。ESM的每个import都会触发一次新的文件请求，因此在依赖层级深、涉及模块数量多的情况下，会触发很多个网络请求，巨大的请求量加上Chrome对同一个域名下只能同时支持6个HTTP并发请求的限制，导致页面加载十分缓慢，与Vite主导性能优势的初衷背道而驰。在进行依赖的预构建之后，这种第三方库的代码被打包成了一个文件，这样请求的数量会骤然减少，页面加载也快了许多

4、其实本质就是针对一些第三方库得代码还是会进行 bundle，不然很多库请求会很慢，而且每次热更新都会重新加载，这样就会导致很慢
![[00 assets/a9f53c537b9ac5defe703ce536722506_MD5.jpeg]]


# 2. 基本使用

1、`pnpm i esbuild`，我们可以在 `package.json` 中做配置，这样就可以执行打包
![[00 assets/25070e0b9ccd857612c48e0b8410e825_MD5.jpeg]]

2、当然也可以使用 JSX 来做转换，他提供了自带得 laoder。其实不仅仅是 JSX，一些图片文字都可以处理，esbuild也内置了对应得 loader
![[00 assets/9dfc9f3cd03c148236c27182c5553893_MD5.jpeg]]


