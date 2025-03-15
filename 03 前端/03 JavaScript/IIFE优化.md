【使用 IIFE 提升性能【渡一教育】】https://www.bilibili.com/video/BV1Xw6GYhEdM?vd_source=8992a13080c32977bce93a5140823f3b

我们可以在开始的时候就获取相应的数据，而不是每次都去重新获取
![[00 assets/7793ad003a6a79e6f5e2328c7ffd6659_MD5.png]]

比如这里的正则每次都是重新会创建，我们可以使用闭包来创建重新获取即可
![[00 assets/8f6c0d687bff5ab97a6e9d1f86925765_MD5.png]]
