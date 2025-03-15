参考视频：[如何获取组件的类型 #JavaScript #前端开发工程师 #编程 #程序员 #web 前端 - 抖音 (douyin.com)](https://www.douyin.com/video/7368768642969816331)

1、我们参考下图可以看到 ElForm 不能直接作为泛型的参数传递进去

![[00 assets/9e630ac9e4a5780d59c9b8f3f8599d4c_MD5.png]]

首先 ElForm 本质就是一个值，它使用 DefineComponent 导出，这里涉及 Vue 原理的问题，模板最终就会编译成下面的 DefineComponent 函数 导入

![[00 assets/26a6b87ab5e1a365049ea64737bffb77_MD5.png]]

其实上面的赋值本质就是下面的样子，所以会报错

![[00 assets/03335bde8f033d4fbf65b271784b4d5f_MD5.png]]

2、InstanceType 就可以看到下面 ElForm 的实例暴露出来的类型，因为我们模板使用的 ElForm，但是本质编译之后还是使用的它的实例

![[00 assets/b29cf8f5a121c8ba9c3cd38be0a21975_MD5.png]]

3、这段内容好久没用了，留个记录，后续使用 TS + Vue3 项目的时候再来看
