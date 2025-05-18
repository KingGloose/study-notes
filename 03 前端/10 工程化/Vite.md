# 1. 基本介绍

![[00 assets/207bb556030115314905ca8325d949f9_MD5.jpeg]]

1、开发阶段依赖 `esbuild` 的极速能力，生产阶段借助 `Rollup` 的成熟生态，而`swc`作为性能更强的转译工具，可通过插件集成到 Vite 中，替代 Babel 或补充 `esbuild`
2、`swc` 和 `esbuild` 都用于代码转译，但 Vite 默认使用 `esbuild`、`swc` 是可选替代方案。
![[00 assets/c6924371a5af45e9b18f0d13a774fea7_MD5.jpeg]]

2、这里就引申了`esbuild、rollup、swc`这些工具和`vite`的区别
``` base
开发阶段 (Dev Server)
│
├─ 依赖预构建：esbuild（转换 CommonJS → ESM）
├─ 代码转译：esbuild（TS/JSX → JS） 或 SWC（通过插件）
├─ 按需加载：浏览器直接请求 ESM 模块
└─ 热更新：基于 ESM 的 HMR

生产构建 (Build)
│
├─ 代码转译：esbuild 或 SWC（可选）
├─ 打包优化：Rollup（代码分割、Tree Shaking、压缩）
└─ 输出静态资源：HTML/CSS/JS
```
![[00 assets/e37fc2a186f53d9e77e7ca2219405158_MD5.jpeg]]

3、针对浏览器来说本身就是原生支持`es module`
![[00 assets/bdf7900d1deb77e3c6a2f18e24410c8e_MD5.jpeg]]
4、如果你直接使用原生来写的话存在很多的问题：必须写后缀名、加载一个模块里面有很多的`import`会加载很多`js`、`ts、vue`等文件都是不识别的。所以`vite`出来了，解决上述的问题
![[00 assets/b0406e08a282c27a55746f5f97735aa1_MD5.jpeg]]
我们使用`vite`就可以解决了上述的流程，并且`vite`底层使用转发服务器，再使用`esbuild`来对文件进行简单的转换。比如你请求了`http://localhost:8080/index.vue`那么底层的`转发服务器connect`就会编译`vue`然后返回`js`
![[00 assets/968e755ed00b6e9e9a3e3daa44a2c207_MD5.jpeg]]

5、这也是`vite`和`webpack`的比较
![[00 assets/024fddf9ed7c223e85904f0bf376f268_MD5.jpeg]]

# 2. 资源处理

## 2.1 JS

参考上图直接导入即可

## 2.2 CSS

![[00 assets/7d907ff9b57597c93923f987067811b9_MD5.jpeg]]

1、针对`vite`来讲，他底层帮你已经把配置都处理好了，你只需要下载对应开发库即可
![[00 assets/b81ebbda9b613014885e1ce7aab19483_MD5.jpeg]]
![[00 assets/b436e1d949d1bd0648c4e718ab217d99_MD5.jpeg]]

## 2.3 TS

![[00 assets/f2b8ca351c721dd887dcedec11bc5a6e_MD5.jpeg]]

## 2.4 Vue

![[00 assets/2362d3abe95aaaa51a375a5a88acc21d_MD5.jpeg]]

1、按照如下配置就可以实现对`vue`进行编译，然后运用
![[00 assets/8796b8f171df89269989aef60648d1be_MD5.jpeg]]
针对底层虽然请求的是`vue`文件，但是本质还是会转换，然后转发给浏览器
![[00 assets/b36492ea219104bea168d1c8e3b55ddc_MD5.jpeg]]

## 2.5 React

1、针对于`React`项目甚至不需要做什么配置，就可以实现针对`React`的编译和实现
![[00 assets/928b8741e8a8efef203dc89f97741356_MD5.jpeg]]
![[00 assets/d6e6e90551aa13b13a283f9d665827f1_MD5.jpeg]]


# 3. 打包项目

![[00 assets/ac1858261fd83c75f17af1184f53f880_MD5.jpeg]]

# 4. vite脚手架

![[00 assets/9147fd28a89ba879c01c0cfe4aa7e381_MD5.jpeg]]

# 5. esbuild解析

![[00 assets/8c1856cf82effaf95434d975a8bb1bfd_MD5.jpeg]]
![[00 assets/dd7dca05565748b687143747bbbd2cfa_MD5.jpeg]]


