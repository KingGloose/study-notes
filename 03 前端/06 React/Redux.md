

## 3.1 基本介绍

> 纯函数

具体参考`JS高级`中的笔记

![[00 assets/f02d7dade869f13b738afaacadce84e7_MD5.png]]

![[00 assets/be9a2d87cc18ecd717c9a87f15a1c59d_MD5.png]]

> Redux 介绍

![[00 assets/6b94817001535aff9ab098d56b52817d_MD5.jpeg]]

> Redux 核心理念 - store

![[00 assets/df5bafe1b5664a3dfb3714237e8736f3_MD5.png]]

> Redux 核心理念 - action

![[00 assets/6f42d35ff654ba9034a9a4101f94cedb_MD5.png]]

> Redux 核心理念 - reducer

![[00 assets/47687e147713687c4e02036714ee667e_MD5.png]]

## 3.2 非项目使用

### 3.2.1 基本使用

```bash
npm i redux	 // 安装redux
```

1、目前演示都是直接使用`Redux`原生函数，而非使用封装好的，所以比较繁琐

2、`reducer`函数执行之后返回的结果需要是一个对象

3、通过`dispatch()`传入的数据，会再执行一次`reducer函数`，并且传入的数据都会传入到`action`中

![[00 assets/990db6d460c0445ab6ae6c3658c417f0_MD5.png]]

### 3.2.2 优化处理

> reducer 选择和订阅模式优化

1、我们将`reducer`中的`if`改为`switch`，这样更易读

2、我们使用`store.subscribe()`来订阅，只要每次`dispatch`的话就会执行订阅函数

![[00 assets/ea966ebdacd3c4137eb1e6afb253d6df_MD5.png]]

> action 优化

1、将原本`{ type:xxx , name:xxx }`的形式的代码抽取为一个函数，放在`actionCreaters.js`中

![[00 assets/3a36b41439ece54e5b58b3bfdf8c8356_MD5.jpeg]]

> reducer 常量抽取

1、一般情况每个`type`都会抽取到`constants.js`中作为一个常量

![[00 assets/ed79375264b71dfb3e89210eb10c1d8f_MD5.png]]

> reducer 函数抽取

1、后期`reducer`函数会越来越大，所以建议将`reducer`函数抽到单独一个`.js`文件中处理

![[00 assets/9b4c63c1e43532c2bcc08c48c92a4f92_MD5.png]]

### 3.2.3 使用流程

> Redux 三大原则

![[00 assets/682e32b8da280b794587dcbd32e2efb1_MD5.png]]

> 使用过程

![[00 assets/abde9e6d3f7298da55953ac06d320e65_MD5.png]]

![[00 assets/f4f64dbdecedc1e1caf1ecfae7e87eed_MD5.png]]

> Redux 结构划分

![[00 assets/811212f99a9d564b7b96d6a150e1d2ba_MD5.png]]

## 3.3 React 使用

### 3.3.1 基本使用

其实一切的本质就是在`3.2`的笔记中，下面只是将其融合到`React项目`中

```bash
npm i redux		// 安装redux
```

1、其基本的逻辑和上面是类似的，文件结构都是一样

![[00 assets/a69d373a35b98d04b4273113739ab9c4_MD5.png]]

2、随后就是相应的`.jsx`文件中的逻辑

![[00 assets/8d3ad55d25eee663236d201467c4acf5_MD5.jpeg]]

![[00 assets/68b10eb8acf2a73bafd7cfbcb0db52dd_MD5.png]]

### 3.3.2 React-redux

参考上面的代码会发现有很多重复的代码，比如`components`中组件的`订阅...`

![[00 assets/9c484cabd6526873c85f4066952cd98a_MD5.png]]

所以就需要一个高阶函数来处理这个情况，这样会让代码更加简单

```bash
npm i react-redux 	// 安装react-redux
```

1、首先我们需要为全局`App`提供`store`

![[00 assets/cf6dfca227b6f927d3a945152bbf43d0_MD5.png]]

2、我们需要使用`state`的话，就需要使用函数`mapStateToProps`来映射。最后取值就是通过`props`来取值，因为底层就是通过高阶函数，将参数作为`props`传递给传入的组件

![[00 assets/6475054888ea728f68d5e18503a083d5_MD5.jpeg]]

3、我们需要使用`action`的话，也是一样传入一个函数`mapActionToProps`。将其中的`dispatch`封装到该函数返回的对象中，组件调用的话就是`this.props.xxx`来处理

![[00 assets/cf290b45f780e261a41ac85252c24d1f_MD5.png]]

其中`action`就是我们一开始编写的`action`，这个和调用`store.dispatch()`是一样的，只不过迁移组件外的函数了

![[00 assets/58de8f6b9fd7d50faa87a2702e281f87_MD5.png]]

4、我们使用`react-redux`的`connect`的时候，一定要注意`mapState`、`mapAction`的顺序，如果顺序反的话就会报错

![[00 assets/ee5854e2c851a161cbfedbf4e622c3c7_MD5.png]]

### 3.3.3 网络请求

#### 3.3.3.1 基本使用

在`mount`生命周期中发送网络请求，然后使用`action`来更新其中的数据

![[00 assets/c08079a2f96104ae2a2b220f0959705b_MD5.png]]

#### 3.3.3.2 redux-thunk

![[00 assets/840b435e78cf751190514e5790b925e6_MD5.png]]

而且我们直接将网络请求写在`action`的话，这样就是直接返回`Promise`，那么还需要在`mapAction`中编写接收异步函数的代码，这样并不是将网络请求移到`redux`

![[00 assets/d0954088877b24b7f846f52e45c6a3ff_MD5.png]]

即便你将函数改为`async`的形式，因为`async`的函数默认会返回`Promise`，所以也不行

![[00 assets/4c27468c4c2094cf37c9ca00593fbc98_MD5.png]]

所以这个时候我们就需要安装`redux-thunk`中间件来对`react-redux`增强

```bash
npm i redux-thunk	// 安装
```

![[00 assets/0304d67ee7ae010b11bb6e0ec2d7cd4c_MD5.png]]

1、在`createStore`中使用`redux-thunk`中间件，这样`dispatch`就可以接收函数

![[00 assets/ff4b2d6fb21f90a798b843be5c19aea8_MD5.png]]

2、我们在`mapActionToProps`中`dispatch`其实只能接收对象，但是我们使用`redux-thunk`增强之后就会自动调用这个函数

3、我们在`action`中`fetchHomeMultidataAction`中返回的函数第一个参数就是`dispatch`，我们可以在该函数中`dispatch`来改变参数，第二个参数就是`getState`，可以获取`State`中的参数`getState().count`

4、下面这一套处理方式就是页面中`componentDidMount`生命周期中调用`mapActionToProps`，`getHomeMultidata`函数，然后执行`fetchHomeMultidataAction函数`，返回的函数就会被`redux-thunk`来执行，然后内部执行的就会调用`changeBannerAction`和`changeRecommendAction`方法，实现数据的改变

![[00 assets/5537d4528135da5284ac1c6128969820_MD5.png]]

### 3.3.4 开发工具

我们可以下载`redux devtools`和`react devtools`工具，和`vue.js devtools`工具是一样的

1、`github`中库的文件落后很多，所以建议在插件市场中下载

2、如果`react devtools`插件没显示的话，我们需要重新启动项目

![[00 assets/39a4d0b7151bedc2e31ac99f9d9126d1_MD5.png]]

3、其中`redux devtools`工具默认是关闭，我们需要按照下面的步骤来开启

**官方网址**：[zalmoxisus/redux-devtools-extension: Redux DevTools extension. (github.com)](https://github.com/zalmoxisus/redux-devtools-extension)

![[00 assets/1289cd32b8e67b110e592607ceb6dc51_MD5.png]]

如果开启的话，我们就可以看到下面的`redux`的数据

![[00 assets/00b8e84318c2f1aeb7c4ceebba1b53ec_MD5.png]]

### 3.3.5 模块划分

> 基本使用

1、首先是对`store`模块进行划分处理，这里重点就是`index.js`导出各级模块的处理

![[00 assets/12e9d759accdc2cf1f724f4443bfda71_MD5.png]]

2、随后便是使用`combineReducers`对各级模块进行组合处理，下图中`counter`导入的就是`reducer`

![[00 assets/64efbbbc1ac9b25fd833d47eba934349_MD5.png]]

_这里需要补充关于模块导出的知识，在各级模块中使用`export default xxx`导出的时候，就需要使用`import xxx from "xxx"`来导入。使用`export _ from "xxx"`导出的模块，就需要使用`import { xxx } from "xxx"`来导入。或者直接使用`import \* as xxx from "xxx"`来全部导入

![[00 assets/fa93275e57e744cd267300965ddf84b9_MD5.png]]

3、我们使用`state`的时候需要加上你要使用库的名字，也就是`combinReducers`中设置的属性名

![[00 assets/29a7f2e8c9dd35bbb9f82004e5b08379_MD5.png]]

其中对于直接用`redux`而非`react-redux`库的数据，也需要加上`库名`来区分数据

![[00 assets/7df95913e1705980513dc085242546f6_MD5.jpeg]]

> combinReucers 理解

![[00 assets/0b0da6a806dfbe5db35f7980ed0ab86b_MD5.png]]

其实底层本质是执行下面的代码

![[00 assets/1cabdbca2926d31a9f3d7756a68feb36_MD5.png]]

### 3.3.6 connect 实现

> 基本实现

左边就是`connect`的实现处理，其实原理很简单，就是将传入的数据遍历然后丢给传入组件的`props`中

![[00 assets/8c7b2d705702cb4cd6b1ed87d6ac8efa_MD5.png]]

> store 解耦

此时`connect`需要传入`store`，所以这个封装的不是很好，所以我们需要将这个部分来解耦处理

1、我们创建一个`context`，并且传入`store`

![[00 assets/2fb5b5466f228e58cec4c1bc0b68e088_MD5.png]]

2、我们传入的`context`进行使用，此时就将封装的`高阶组件`进行解耦操作了

![[00 assets/21a2f84ce240e34cc6bd0c6aee67b2cc_MD5.png]]

3、其实`React-redux`本质就是进行上面的操作

![[00 assets/35290eef517dac4e1147e6cad1bc4bb8_MD5.png]]

### 3.3.7 中间件

#### 3.3.7.1 基本介绍

![[00 assets/09a1cf562bf04a2742f609af11637255_MD5.png]]

#### 3.3.7.2 中间件原理

![[00 assets/9b0a4dea8adc8dd7018ef6734944ae22_MD5.jpeg]]

![[00 assets/ea386944260f20e5b68acc0a49f682fd_MD5.png]]

1、下面其实就是`中间件`的原理，我们阻断原生的`dispatch`，中间加一个`Hook`。只要使用`store.dispatch`就等于去执行里面的`logDispatch`函数，这样就可以实现中间件的调用

![[00 assets/83944ad96142a607ea209711eb84aec9_MD5.png]]

这样你就可以实现`log`的打印

![[00 assets/6b81dabae214e22d47ee93c38eb1feb3_MD5.png]]

其实在函数内部也是可以去修改外部的对象值，上面修改`store`中的`dispatch`其实就是按照下面的原理来处理的

![[00 assets/733f391da5278d04f47562165ea66bc0_MD5.jpeg]]

2、我们也可以去编写`Redux-thunk`中间件，其原理基本和`log函数`是一样的，其实底层就是帮助我们来执行传入的函数

![[00 assets/6c01dd68e5b283faf20e60c1eb80ea80_MD5.png]]

对于`thunkDispatch`中`action()`回调传入的第一个参数最好是`store.dispatch`，因为可能存在`dispatch`中再去执行`dispatch`函数。我们希望传入的`dispatch`还能再调用`thunkDispatch`，所以最好传入`store.dispatch`，而非`next`

![[00 assets/0a437efb3fa7ef26b28052aad62ac458_MD5.png]]

#### 3.3.7.3 applyMiddleware

1、我们可以将`log`和`thunk`抽取到文件中来处理

![[00 assets/571752d2500bc3ade088284e983ba01a_MD5.png]]

2、我们引入`applyMiddleware`，这个函数的作用就是将传入的中间件依次执行，并且赋值`store`

![[00 assets/7ccf111af720e47cc7de89959a97776e_MD5.png]]

3、我们在`index.js`中导入导出所有的函数即可

![[00 assets/cdc9fd60b2e77408d6e6d871d5c6b231_MD5.png]]

## 3.4 ReduxToolKit

### 3.8.1 基本介绍

![[00 assets/8671f80ddb8274440b635d55bb5f33a7_MD5.png]]

### 3.8.2 基本使用

```bash
npm install @reduxjs/toolkit react-redux  // 安装TRK和react-redux
```

1、我们使用`@reduxjs/toolkit`中的`createSlice`来创建一个片段

2、其中`reducers`表示是`reduce`中的`action`，因为底层做了处理，所以我们直接使用`state.xxx`的方式来对数据进行修改。而非以前的传递`{ ... }`的形式

3、传给`action`的数据使用`payload`来接收

4、对于`actions`的导出是为了给`dispatch`使用的

5、最后要导出`slice`中的`reducer`来处理

![[00 assets/7b2883c996bf9b1ba11142b8bd9664dd_MD5.png]]

6、最后的使用也是和之前的做法是一样的

![[00 assets/30c34af5c910765705773f22b7b15804_MD5.png]]

### 3.8.3 网络请求

#### 3.8.3.1 基本使用

> 问题

其中的一个方法就是按照`3.3.3.1 基本使用`中的模式来处理，将网络请求写在组件里面来处理。但是这种方式不是很好，因为网络请求都是写在组件里面的，后续不方便管理。

![[00 assets/1171d55cd9c49955d962037d71f5a657_MD5.png]]

> 解决方法

1、使用`createAsyncThunk`来创建一个异步的函数，并且传入参数

2、再这个回调函数中返回的`res.data`数据会被传入到`extraReducers`中下面的计算属性来接收，然后再这里面完成相应的逻辑处理

3、并且写在外面的`fetchHomeAction`依旧需要导出并且在组件中被调用

![[00 assets/12a4a09a817f73df9c0d9fead81f85f6_MD5.png]]

4、调用传入给组件中`props`的函数

![[00 assets/b4eac591c3e6eeb970840950a9c2d736_MD5.jpeg]]

和之前使用`redux-thunk`工具是一样的，传入函数来处理，而非传入对象

![[00 assets/70ada4748bbeb4d9e3598a052d00ebee_MD5.png]]

#### 3.8.3.2 额外写法

> 1、extraReducers 额外写法

下面就是`extraReducers`的 2 种额外的写法

![[00 assets/a0066293305db3e37514c23156887b4d_MD5.png]]

> 2、state 变化额外方式

原本是通过`extraReducers`来处理这些数据，但是现在可以直接在自己的异步函数中处理

![[00 assets/39165cea0a06246529de5fd8e00554fa_MD5.jpeg]]

### 3.8.4 数据不可变

这里就是介绍为什么我们以前都是直接将`{...}`传入给`reducers`的

![[00 assets/f2c4b220563c33f1d4d0bfb010959462_MD5.png]]

但是为什么我们使用`ReduxToolKit`就不需要返回对象，而是直接修改里面的值即可，其实就是使用到了`ImmutableJS`，介绍：[React 系列十八 - Redux(四)state 如何管理 (qq.com)](https://mp.weixin.qq.com/s/hfeCDCcodBCGS5GpedxCGg)

![[00 assets/71841a96335831bf9077a0b8cd6a04eb_MD5.png]]

## 3.5 状态管理

![[00 assets/f23398997d439feb51ff0d3d265fdefa_MD5.png]]

![[00 assets/3e67c200325379fe9d7289ffe574540c_MD5.png]]
