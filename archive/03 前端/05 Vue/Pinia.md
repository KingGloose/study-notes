# 1 基本介绍

> 基本介绍

![[00 assets/e78c6191ed2776ddf74e12caa801dc5e_MD5.png]]

> 对比

![[00 assets/c6d3f88456894c26a513a891941ab064_MD5.png]]

> Store 基本介绍

![[00 assets/86ce0eb21b041147c0c17a1525579c26_MD5.png]]

> 定义 Store

![[00 assets/b8f6797948e6c3c9988abf3c62ed63e1_MD5.png]]

# 2 State

## 2.1 基本使用

首先是在`Vue`中注册`pinia`，这里就是第一步和`vuex`不一样，这里不需要直接在`createPinia()`中书写对象来处理数据

![[00 assets/f38da48d66c9e5031d918d9de4d44af0_MD5.png]]

下面就是使用`State`，需要使用`defineStore`来创建仓库，第一个参数可以理解为`vuex`的`namespaced`，作为唯一的`id`。假如需要使用这个仓库的话直接导出使用即可

![[00 assets/89a283640ad3031513e5979e53952d96_MD5.png]]

下面为整体的结构流程图

![[00 assets/84f1638aa7b25c99de929d15fa1ac98b_MD5.png]]

当然假如我们感觉直接写`counterStore.count`还是很麻烦的话，也可以使用解构来操作，但是直接使用解构的话可能会丢失原本的响应式，所以`Vue提供的toRefs`，或者直接使用`pinia提供的storeToRefs`

![[00 assets/d2ae3a5f95d9045344e1c05a63664988_MD5.png]]

## 2.2 操作 state

我们可以直接使用`countStore.xxx`来操作数据，因为它返回来的数据是响应式的。我们使用解构之后会在外面套一层`storeToRefs`，将它变成`refs`的响应式，所以改变需要使用`xxx.value`来处理

![[00 assets/3688cfe8b0c7a3eb550b030d49c26c18_MD5.jpeg]]

> $reset

可以重置数据，将数据变为原来的样子

![[00 assets/18b2298308aceefed8479c24781fbaec_MD5.png]]

> $patch

一次修改多个值

![[00 assets/669f36c0bc79c5ffeaed0d97a0e58ee3_MD5.png]]

> $state

累加数据进入`state`。但是官网记录的是替换数据，不是很准确

![[00 assets/ca97b2607c9a25c4f3ee0eab43a46580_MD5.png]]

# 3 Getters

我们可以使用下面的 2 种方式来调用。第一种是直接使用`countStore.xxx`调取，第二种是使用`解构`的方式来调取

![[00 assets/0f93117a6f5e09efde4d1a597efeb359_MD5.png]]

当然还有一些其他的用法，比如下面的`返回一个函数`和`使用其他store在的数据`

![[00 assets/ec08fd9b251340bf8fd9944a1f400de8_MD5.png]]

![[00 assets/05f983c327602778c9599a08f22e0e29_MD5.png]]

# 4 Actions

## 4.1 基本使用

我们可以直接调用里面的`Actions`，其中`Actions`不带有类似于`State`的默认参数，需要的数据直接使用`this.xxx`就可以了

![[00 assets/dab3912d243a2af26c071d17b7b0e918_MD5.png]]

## 4.2 网络请求

在`actions`中也是支持异步请求的，可以在里面发送网络请求，使用异步函数处理，基本的使用方式和`vuex`中的`actions`的网路请求是一样的

![[00 assets/55c1d70db25a3edd3ccb254b397cfbc6_MD5.png]]

当然我们还可以在添加`then`来监听请求的结束，但是它返回的值是`undefined`

![[00 assets/7b6b0e514e19b2060f05c21e05c1ed83_MD5.png]]

假如你觉得返回`undefined`不是很好得话，可以自己返回`Promise()`来处理

![[00 assets/153e5ea5212c3148f9597798d464d912_MD5.png]]
