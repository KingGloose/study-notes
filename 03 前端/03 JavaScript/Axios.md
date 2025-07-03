# 1 基本介绍

![[00 assets/a3bbb65b9d2b2e966a49ef295841c602_MD5.png]]

> 请求方式

![[00 assets/6a5801f8a15e2e2d29b1b348bf1510be_MD5.png]]

> 配置选项

![[00 assets/951372e113e6f25ee1cf6b5b263defaf_MD5.png]]

# 2 基本使用

```bash
npm i axios 	// 下载axios
```

> request

![[00 assets/c389d8e1b23fc4b5db571e9158712a45_MD5.png]]

![[00 assets/36ab5c68b109a7f7088639d1152f73aa_MD5.png]]

> get

第二个参数就是填写配置信息

![[00 assets/0561cb981cd974247a5e9196217f91db_MD5.png]]

![[00 assets/9bc6023a83c0448fc37969a30d274fb3_MD5.png]]

> post

![[00 assets/9ace8e89f797a629216d766ce241fc3e_MD5.png]]

当然我们也可以直接将第二个参数作为配置选项，假如需要写入`data`的话，直接编写`data`的对象就可以了

![[00 assets/01e6e373ccb4928cb62cd0d951b25f33_MD5.png]]

![[00 assets/0ecb64d3bf40b47452246ba2cd417e18_MD5.png]]

> 公共配置

当然我们也可以使用`axios.default.xxx`来配置一些公共配置

![[00 assets/daffa2437a7359f0ca46b3b8eed6b375_MD5.png]]

# 3 发送多个请求

当然我们可以一次发送多个请求，当这些请求都成功之后会返回一个`成功的Promise`

![[00 assets/78fd66b8c95b381c03bc7b5e115c754c_MD5.png]]

![[00 assets/c5a68b7bd76bbe6956e8b6469ebbff66_MD5.png]]

# 4 创建实例

![[00 assets/4d35cb15cf407873a001a3f07443ba96_MD5.png]]

我们可以编写多个`axios`实例来处理不同的网络请求

![[00 assets/53e67896345bb924a63e126f29805d54_MD5.png]]

# 5 拦截器

下面就是设置`拦截器`，其中`axios.interceptors.request`就是`请求拦截器`，`axios,interceptores.response`就是`响应拦截器`，当你请求或者响应的时候都会先走这个拦截器处理。在这个拦截器里面可以进行`loading`动画的加载、数据处理......

![[00 assets/84e38775b455d158ef4f4ade4c9558cf_MD5.png]]

![[00 assets/6e3ad7a1280461fa403aec6533f95769_MD5.png]]

# 6 axios 封装

下面是对`axios`简单的封装，假如需要进一步封装的话可以根据项目的实际情况来

![[00 assets/391d813c4298bfffe364b52beca16f57_MD5.png]]
