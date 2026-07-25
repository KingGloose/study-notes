# 新 OA 接入泛域名处理(原文留档)

> 来源:`文档内容/新OA接入泛域名处理.doc`(Confluence MHTML 导出)。
> 本文为提取清理后的纯文字版,去掉了 base64 图片和 Word 样式噪声,正文照原意保留。

## 泛域名使用规范 · 泛域名 - 无代理访问线下环境

### 1、webpack 是如何处理的

首先是了解一下针对 webpack 是如何处理的,使用 `__webpack_public_path__`。

分析打包结果,写进去的参数最终变成 `__webpack_require__.p`。

其中 `__webpack_require__.e` 可以理解为是 `import`,这是 webpack 自己重写,本质原理就是使用动态创建 script 来做的加载。

在这个函数中针对路径的拼接是动态的,也就是使用的 `__webpack_require__.p` 作为路径。

### 2、Vite 的处理

但是针对 vite 是没有这类的处理的,如果要实现的话就需要自己想办法处理,有如下几种方案:

**方案一**:自己重写 `import()` 函数,其实可行,而且还简单,那就需要考虑 css 中的静态资源如何处理。

**方案二**:改造 beetle,在打包的时候会自动读取项目中类似 `.beetle.config.js` 这类的配置文件,可以手动在项目中编写。但是有一个问题就是无法在打包的时候获取部署的 ip,如果这样做的话就需要额外修改 beetle 的流程,但是改造成本大。

但是我认为这是比较好的方式,因为自动化和项目可以实现通信了,这样项目有权利可以去修改 jenkins 的配置,然后将编译和部署流程合并,编译的时候直接将文件丢到指定机器中,然后再整做个历史编译。这样可以将指定的文件部署到其他机器上,但是这样就修改了大家都习惯的工作流,没必要改造,成本会很高,所以方案抛弃掉。

了解到,目前针对 beetle 部署和编译每个环节都有自己的操作,还不好合并,那么这个方案在目前的流程中可以 pass 了。

**方案三**:为 vite 编写 plugins,目前是有一个开源的来使用:

- https://juejin.cn/post/7063016723502333989#heading-3
- https://github.com/chenxch/vite-plugin-dynamic-base

下面是大致原理:

1. 会在加载的时候构建一个基于 dynamicPath 的地址,然后在初始化的时候 vendor 包的地址就修改了。
2. 在请求里面的 `import()` 的时候会自动跟随 vendor 包来做请求,就实现了动态加载。
3. 可以看到不仅仅 js 可以打包,css 也可以。
4. 一些打包进去的静态资源也是可以打包,动态注入。
5. 但是我发现针对资产这边的项目,会在接受信息的时候做这个拦截,如果是泛域名就不行,还需要编写特定的工具包来做轻量化的接入。目前分析 HTML 大。

或许可以使用 `define` 来替换定义,在打包的时候添加?

### 服务器架构

针对域名中的服务器,线上本质只有一台服务器,线下他会走定时任务将静态资源在每个申请的机器 docker 中 copy 一份,或者申请机器的时候 copy 一份。

也就是你访问域名的时候会经过 nginx 转发处理,而针对一些公共的资源,也都是在自己的 docker 中的,而不是一个公共的服务器来做请求。

### 相关 OA 审批单链接(留档)

- 采购申请审批单:`scp.zhuanspirit.com`
- 行政集采供应商准入申请单:`finaao.zhuanspirit.com`
- 资金调拨单:`finaao.zhuanspirit.com`
- 发票申请审批单:`zzfpsys.zhuanspirit.com`
- 公司银行账号申请单:`finaao.zhuanspirit.com`
- 员工交票入口:`zzfpsys.zhuanspirit.com`
- 自营机器借机申请审批单:`bmadmin.zhuanspirit.com`
- 短信模版修改申请单:`ipms.zhuanspirit.com`
- 自营商品报损丢件单-天路:`bmadmin.zhuanspirit.com`
- 权限申请审批单:`id.zhuanspirit.com`
- 资产管理:`asset.zhuanspirit.com`

### 小结

目前你要接入泛域名的话,需要项目额外做插件支持,在最后使用的时候使用 `http://oa-zhangjiahui04.test.zhuanspirit.com` 的方式来访问,现在机器可以区分了,后面是否为测试环境也可以区分了。

这样其实可以解决绝大部分的问题,可以在 beetle 中添加一个复制链接的按钮,这样也可以一定程度的减少开发者理解的成本。
