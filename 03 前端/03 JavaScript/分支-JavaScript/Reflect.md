**参考视频：** coderwhy 前端系统课

**参考视频**：[Reflect 的本质【渡一教育】\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1ZJ4m1J7WM/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b)

# 1. 基本介绍

其实本质就是一句话：**调用对象的基础方法**

![[00 assets/f88cf1f70318b565558133c3a3ec524f_MD5.png]]

对于上述的**调用对象的基础方法**如何理解呢？因为我们在正常的使用 Object.? 的时候本质是调用封装之后的方法，而非对象最底层的方法

![[00 assets/d46ec22d85cc4579f6723a6198ec208f_MD5.png]]

我们来查看 **ECMAScript** 规范中的处理：使用 `Object.keys()` 本质调用的 `EnumerableOwnProperties` 方法，该方法会去调用底层的 `OwnPropertyKeys` 方法，但是该封装方法做了其他判断，比如：判断该元素是否可以被遍历等

![[00 assets/e918d2c6acf026eba393337b84353456_MD5.png]]

所以这个时候我们就可以直接使用 `Reflect API` 来直接调用对象的底层方法

![[00 assets/1036cb7b77d6d836a501887d9349502c_MD5.png]]

所以总结对象方法的调用链条为：**对象方法 -> 封装方法 -> 底层方法**

# 2. 常见方法

`MDN文档`：[比较 Reflect 和 Object 方法 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect/Comparing_Reflect_and_Object_methods)

![[00 assets/17e328351ae5efe482f120aa1ae11df8_MD5.png]]

# 3. 基本使用

因为`Proxy`本身只是对原本的对象进行代理，假如还是要对原本的对象进行操作的话就违背了初衷。所以就需要下面的`reflect`来对原本的对象进行操作。

`Reflect.*`会返回一个布尔值，当设置或者获取失败的时候会返回`false`，如果可以的话可以用这个返回值判断

![[00 assets/b6849d0afaf6d36ce7e3ed64b59bb00d_MD5.png]]

# 4. Receiver 参数

我们为对象的属性添加`存取描述符`的时候，再来获取或者设置该值的时候，你会发现`get和set`并不会走代理的对象，所以这个对于`Vue响应式`来说是一个隐患，这个时候就需要使用`receiver`来避免这个问题。

其中对于`Proxy`来说，只有`set和get`方法才有`receiver`

![[00 assets/519f6e9c28f1e091381200a69764e85d_MD5.png]]

`receiver`表示是自己的代理对象，也就是下图中的`objProxy`，我们传入该参数，对于`obj`中的`get和set`的指向就是`objProxy`，这样每一步的获取操作都可以被监听到

![[00 assets/27cf73d19ce8452253e53bfd2befaa9b_MD5.png]]

# 5. construct 方法

我们可以使用`Reflect`的`construct`来使用`Student`的函数来创建`Person`的的对象，这个在`babel`转换`super()`的源码中有使用

![[00 assets/9e2a9894a640f77e671988608bfbf314_MD5.png]]
