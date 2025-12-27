视频介绍：[尚硅谷 Vue2.0+Vue3.0 全套教程丨 vuejs 从入门到精通\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Zy4y1K7SH?from=search&seid=15643037923276153545&spm_id_from=333.337.0.0)

视频参考：coderwhy - 前端系统课 - 2022 - Vue

# 1. 非脚手架 - OptionsAPI

## 1.1 基本介绍

> 基本介绍

vue 是一套用于构建用户界面的**渐进式**JS 框架，vue 可以自底向上逐层的应用

![[00 assets/a4a33ec3ae0d76d52e31a906dfc98397_MD5.jpeg]]

> Vue 地位

![[00 assets/abd25b27a88bb40e3d8f7b251181039c_MD5.jpeg]]

> 优点

**1.**采用组件化的模式，提高代码复用率，且让代码更好维护，其中一个组件就是一个 vue 文件格式

![[00 assets/50baf26f2614d8ce65eb33099592eab8_MD5.jpeg]]

**2.**声明式编码，不需要直接操作 DOM，提高开发效率。具体的介绍可以参考`Vue3 1.3 声明式编程和命令式编程`的介绍

![[00 assets/f767cf7ac8fa1760820a551a1db341e9_MD5.jpeg]]

**3.**使用虚拟 DOM——优秀的 Diff 算法，尽量复用 DOM 节点。提高渲染的效率，并且更好的支持跨平台

![[00 assets/7b64c2a5a7f91647a2738773e7faadd0_MD5.jpeg]]

![[00 assets/67cf32f436ce047acaaedec867604696_MD5.jpeg]]

## 1.2 基本使用

我们需要导入`Vue文件`再来编写单文件的`Vue`，这个也是最简单的引用方式，后续会使用脚手架来创建

![[00 assets/b5a8d9fee79d982f3cedfc97351ba57d_MD5.png]]

这个时候我们再来看使用`脚手架`创建的`Vue`，其实本质也是一样的，我们将入口文件的`App`引入，然后放到`createApp`来创建，最后再挂载到`index.html`中`id属性`为`app`的`div`中。和我们写单文件是一样的

![[00 assets/d257dacfb6d25d745e109fe47575953d_MD5.jpeg]]

下面为基本的使用，其中包含了很`Vue2`到`Vue3`的创建的`API`的变化，但是本质其实是差不多的

```vue
// ------------- Vue2 -------------- //
<div id="main">
	<h1>{{name}}</h1>
	<h2>{{age}}</h2>
</div>
<script type="text/javascript">
	//创建vue模板
    new Vue({
		el:'#main',			//指示vue实例为那个容器服务
		data:{				//data用于存储数据
			name:'张三',
			age:18
		}
	})
</script>


// ------------- Vue3 -------------- //
<div id="main">
  <h1>{{name}}</h1>
  <h1>{{age}}</h1>
</div>
<script src="./Vue.js"></script>
<script>
  const app = Vue.createApp({
    data: function () { // Vue3必须使用函数返回值的写法
      return {
        name: "张三",
        age: 18,
      };
    },
  });
  app.mount("#main"); // 这里和Vue2版本里面的el是一样的
</script>
```

## 1.3 data

![[00 assets/63c89050002098ab21f9d76ba1a6f5f7_MD5.jpeg]]

下面就是`Vue3`和`Vue2`的 data 的区别，但是这个东西不经常使用，在`Vue3`中基本都是使用`setup语法糖`

```javascript
// ------------- Vue3 -------------- //
const app = createApp({
	data:function() {
		return {
			message:"Hello World!"
		}
	}
})

// ------------- Vue2 -------------- //
const app = createApp({
    data:{
		message:"Hello World!"
    }
})
```

假如我们需要修改`data`里面的值的话，一般都是使用下面的方式来修改，可能后续会有`pinia`、`router`、`setup语法`......的差异，但是其本质就是下面的方式

![[00 assets/f00cbf5b04dbcc36da2782e4bcf4bd8d_MD5.png]]

## 1.4 methods

```javascript
// ------------- Vue3 -------------- //
const app = Vue.createApp({
	data:function(){
		return {
			message:"Hello Vue!"
		}
	},
	methods:{
        // 方式一
		ChangeMessage:function() { }

        // 方式二 ES6简写
        ChangeMessage() { }
	}
})
```

但是对于`methods`中的`函数`来说，`this的指向`遵循下面的规律

![[00 assets/06a08448b435a2790b89c5ee52c134a8_MD5.jpeg]]

## 1.5 模板语法

![[00 assets/99e602d6cdc8c49e9e2a34f799b7a1bb_MD5.jpeg]]

对于`Vue`的模板语法来说只能使用`表达式`，所以需要区分`表达式`和`语句`的概念，其实就一个思想

**表达式**：一个表达式会产生一个值，所以需要放在一个需要值的地方，比如：a、a+b、fn(1)、x === y ? 'a' : 'b';

**js 代码：**比如：if( ){ }、for( ){ }

![[00 assets/26b3b939046af4f7ce674200605824a3_MD5.png]]

## 1.6 指令

```bash
总结
1. v-bind:单向绑定解析表达式，可简化为:
2. v-model:双向数据绑定
3. v-for:遍历数组/对象/字符串
4. v-on:绑定事件监听，可简化为@
5. v-if:条件演染（动态控制节点是否存在）
6. v-else:条件渲染（动态控制节点是否存在）
7. v-show:条件渲染（动态控制节点是否展示）
8. v-cloak:用于隐藏尚未完成编译的 DOM 模板
9. v-once:仅渲染元素和组件一次，并跳过之后的更新
10. v-pre:跳过该元素及其所有子元素的编译
```

### 1.6.1 v-text

`v-text`可以插入数据，并且将你传入的数据都当作文本来解析，所以不能解析标签，并且会将标签里面的文本都替换掉

```vue
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<div>你好,{{name}}</div>
	<div v-text="name">你好,</div>
	<div v-text="str">你好,</div>
</div>
<script type="text/javascript">
	let vm = new Vue({
		el:'#main',
		data:{
			name:'张三',
			str:'<h3>啥呀</h3>'
		}
	})
</script>
```

![[00 assets/feb12cec4b82fa6be3d3f3c466968dcd_MD5.png]]

### 1.6.2 v-html

这个和上面的`v-text`最主要的区别：它是`解析HTML标签`，其他的特点基本和`v-text`是一样的。但是 v-html 存在安全性问题，容易导致 XSS 攻击，导致 cookie 被盗取，所以建议少使用

### 1.6.3 v-cloak

我们在使用浏览器访问服务器的时候，并不一定是每次都是加载的很快。并且是将`Vue.js`放在`CDN`来加速的时候，也不一定在`html`之前下载下来，这样就会导致`{{ message }}`等语法提前显示出来，影响用户体验。为了应对着一种情况我们需要一个解决的方法

![[00 assets/7e7942c35078386ee33f9aa374ba8d73_MD5.png]]

> 解决方式一

将引入的`script`放在前面，浏览器只有请求到前面的`js`才会开始后面的渲染。这种方式最大的坏处就是渲染时间较长

```html
// ------------- Vue2、Vue3同理 -------------- //
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
        <!-- 假如这里服务器延迟大概5s的话，页面就没画面了-->
		<script src="../js/vue.min.js" type="text/javascript" charset="utf-8"></script>
	</head>
	<body>
		<div id="main">
			<div>你好,{{name}}</div>
		</div>
		<script type="text/javascript">
        	let vm = new Vue({
				el:'#main',
				data:{
					name:'张三',
				}
			})
		</script>
	</body>
</html>
```

> 解决方式二

假如要把`script`写在后面的话。也可以使用`vue`为我们提供的`v-cloak`，所以这里就可以配合我们的`css属性`来处理这个问题

**官网参考**：[内置指令 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/built-in-directives.html#v-cloak)

**CSS 规则参考**：[属性选择器 - CSS（层叠样式表） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Attribute_selectors)

上面设置的`CSS`规则为属性选择器，只要`HTML`中包含该属性就会执行里面的`CSS语句`。比如：`p[lang]`表示`p标签`里面包含`lang`的话就执行。上面表示只要任意元素里面有该标签就执行

```html
// ------------- Vue2、Vue3同理 -------------- //
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
	</head>
    <style type="text/css">
		/* 这个是属性选择器，只要存在该属性就隐藏，请求到Vue，Vue就将该属性设置为为显示 */
		[v-clock]{
			display: none;
		}
	</style>
	<body>
		<div id="main">
			<div v-cloak>你好,{{name}}</div>
		</div>
        <!-- 假如这里服务器延迟大概5s的话，页面就没画面了-->
		<script src="../js/vue.min.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript">
			let vm = new Vue({
				el:'#main',
				data:{
					name:'张三',
				}
			})
		</script>
	</body>
</html>
```

### 1.6.4 v-once

`v-once`就是只会挂载的时候加载一次，即便后续我们去修改它的值也不会改变

```html
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<div v-once>初始化的{{n}}</div>
	<div>可以变化的{{n}}</div>
	<button type="button" @click="n++">点击+1</button>
</div>
<script type="text/javascript">
	let vm = new Vue({
		el:'#main',
		data:{
			n:1
		}
	})
</script>
```

### 1.6.5 v-pre

`v-pre`提示`Vue`不去解析该标签，直接跳过编译的过程，这个是为了加快编译的速度

```html
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<div v-pre>我没有被渲染哦</div>
	<div>可以变化的{{n}}</div>
	<button type="button" @click="n++">点击+1</button>
</div>
<script type="text/javascript">
	let vm = new Vue({
		el:'#main',
		data:{
			n:1
		}
	})
</script>
```

### 1.6.6 v-bind

#### 1.6.6.1 基本使用

`v-bind`属性是对标签里面的属性值进行动态加载的，和模板语法是一样的，只能添加`表达式`不能添加`语句`

```vue
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<a v-bind:href="url">点击我</a>
    <!-- 简写 -->
    <a :href="url">点击我</a>
</div>

<script type="text/javascript">
	new Vue({
		el:'#main',
		data:{
			url:'https://www.bilibili.com/'
		}
	})
</script>
```

`v-bind`还有一个功能，假如我们在`Vue组件`里面使用`props`传值的话可能需要将某个值变为`number类型`，只需要将添加`v-bind`即可，因为使用`v-bind`的话就当作是`js`代码来解析

```vue
<app :num="12"></app>
```

#### 1.6.6.2 绑定 class

##### 1.6.6.2.1 字符串形式

```vue
// ------------- Vue2、Vue3同理 -------------- //
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<script src="../js/vue.js"></script>
		<style type="text/css">
            /* class的值 */
			.basic{
				width: 200px;
				height: 200px;
				border: 1px solid black;
			}
			.normal{ background-color: pink; }
		</style>
	</head>
	<body>
		<div class="main" @click="q">
            <!-- 使用:表示v-bind来动态加载属性值 -->
			<div class="basic" :class="mood"></div>
		</div>
		<script type="text/javascript">
			let vm = new Vue({
				el:'.main',
				data:{
					mood:'basic'
				},
				methods:{
					q(){
						this.mood = 'normal';
					}
				}
			});
		</script>
	</body>
</html>
```

![[00 assets/54703b5cfd9385e1b3ae222310119cc0_MD5.gif]]

##### 1.6.6.2.2 数组形式

可以参考上面的`字符串形式`，下面就是使用数组的形式来处理

![[00 assets/ac688237cbdaaa140e2cb9299cbd91b5_MD5.jpeg]]

##### 1.6.6.2.3 对象形式

对于对象形式的本质就是`:class="{active : true}"`，只要是`true`的话就可以使用名为`active`的类名。

并且对象语法也可以和数组语法合并在一起使用

![[00 assets/560aa8490f0c069eeafa23336dd0979b_MD5.png]]

##### 1.6.6.2.4 总结

1. 字符串写法：样式类名不确定，需要动态指定
2. 数组写法：要绑定的样式不确定，名字不确定
3. 对象写法：要绑定的样式个数不确定、名字不确定，但需要动态决定

#### 1.6.6.3 绑定 style

##### 1.6.6.3.1 对象形式

![[00 assets/88fc2a5f71168a6da142ca5958953944_MD5.png]]

下面为`Vue3`的官方的写法，官方文档：[Class 与 Style 绑定 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/essentials/class-and-style.html#binding-inline-styles)

![[00 assets/2e580c60003cb2f49d745f4182117010_MD5.png]]

##### 1.6.6.3.2 数组形式

![[00 assets/94d7485a44e5f8e97ddca65236ce6b54_MD5.png]]

#### 1.6.6.4 绑定属性

##### 1.6.6.4.1 字符串形式

一般使用这种形式来添加的方式很少，所以不是很推荐

![[00 assets/8e6968c2093035d4ab5f1305ca90ca74_MD5.png]]

##### 1.6.6.4.2 对象形式

这个方式在使用组件中经常使用

![[00 assets/e76df434781b25f9dac2ca2a5ac5060b_MD5.png]]

##### 1.6.6.4.3 外部样式

官网介绍：[单文件组件 CSS 功能 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/sfc-css-features.html#v-bind-in-css)

![[00 assets/a0179807cb3157b8479970f2845d9992_MD5.jpeg]]

### 1.6.7 v-model

#### 1.6.7.1 基本介绍

`v-bind`是一个单向的绑定。参考下面的 gif 图，`Vue`插件中修改值但是并不会同步显示，所以需要使用`v-model`

```html
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<input type="text" v-bind:value="name">
    //简写
    <input type="text" :value="name">
</div>
<script type="text/javascript">
	new Vue({
		el:'#main',
		data:{
			name:'张三',
			person:{
				name:'李四'
			}
		}
	})
</script>
```

![[00 assets/08b8c43dd6d209b37a5647232c02ac6c_MD5.gif]]

下面就是一个`双向的数据绑`定，我们使用`v-model`。但是`v-model`只能放在表单类元素里面，这很好理解，这是因为 v-model 是需要输入的，但是非表单类标签是不能输入的。

```html
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<input type="text" v-model:value="name">
    <!-- 简写 可以省略value -->
    <input type="text" v-model="name">
</div>
<script type="text/javascript">
	new Vue({
		el:'#main',
		data:{
			name:'张三',
			person:{
				name:'李四'
			}
		}
	})
</script>
```

![[00 assets/545eb9158bd9b69e05549df4a188cfd6_MD5.gif]]

#### 1.6.7.2 v-model 本质

![[00 assets/b61b710b3de489cf0533662de80dcc78_MD5.png]]

对于`v-model`其实我们也可以手写来实现双向绑定，所以本质不过是一个`语法糖`

![[00 assets/46c584f19194bdf2440ea0e05ed2f057_MD5.jpeg]]

#### 1.6.7.3 收集表单数据

它最主要的功能就是收集表单元素

```vue
// ------------- Vue2、Vue3同理 -------------- //
<!-- 当表单提交的时候就触发方法stat，并且取消默认行为prevent，这样的话就不用刷新页面了 -->
<form id="main" @submit.prevent="stat">

	<!-- v-model默认是收集input的value值，这样就是数据的双向绑定 -->
    <!-- trim是消除空格 -->
	账号:<input type="text" v-model.trim="user.username"/><br/><br/>
	密码:<input type="password" v-model="user.passward"/><br/><br/>

	<!-- 你输入年龄的时候记得进行数据转换 -->
	年龄<input type="number" v-model.number="user.age"/><br/><br/>

	<!-- radio里面就需要设置value，不然就是返回的null -->
    <!-- 假如我们使用了v-model得话，去掉name也可以对表单进行互斥得操作 -->
	性别:男<input type="radio" name="sex" v-model="user.sex" value="男"/>
	女<input type="radio" name="sex" v-model="user.sex" value="女"/><br/><br/>

	<!-- 这里你不写value的话，就默认收集的是checked的值，就会返回true，又因为你是双向的绑定，所以后面的节点的checked的值也是true，所以就定勾选 -->
	爱好:抽烟<input type="checkbox" name="hobby" value="抽烟" v-model="user.hobby"/>
	喝酒<input type="checkbox" name="hobby" value="喝酒" v-model="user.hobby"/>
	烫头<input type="checkbox" name="hobby" value="烫头" v-model="user.hobby"/><br/><br/>

    <!-- 绑定的值填在select里面 -->
	<select v-model="user.position">
		<option>请选择校区</option>user.
		<option value="北京">北京</option>
		<option value="南京">南京</option>
		<option value="湖北">湖北</option>
		<option value="湖南">湖南</option>
	</select><br/><br/>

    <!-- lazy就是懒加载，假如你不加的话，就是打一个子就默认输入一个字，假如你加上了lazy的话就没这样的问题，只有在失去焦点的时候进行数据的交换 -->
	其他信息:<textarea v-model.lazy="user.other"></textarea><br/><br/>

	<!-- 下面就是在不同的使用场景使用是不一样的，上面的那个是收集相应的值，这里只需要确定你是不是统一，使用默认的checked的值也是可以的 -->
	<input type="checkbox" v-model="user.agree"/>阅读并接受<a href="www.baidu.com">用户协议</a><br/><br/>

	<!-- 假如不去写type="button"的话就是submit,就是刷新页面,默认提交了 -->
	<button>提交</button>
</form>
<script type="text/javascript">
	let vm = new Vue({
		el:'#main',
		data:{
            user:{
            	username:'',
				passward:'',
				sex:'男',	//当然我们也可以输入来设置默认值
				hobby:[],
				position:'',
				other',
				agree:'',
				age:''
            }
		},
		methods:{
			stat(){
               	//这个是转换为JSON格式，在AJAX里面有写，并且注意在开发的时候需要用对象包裹起来user.这样就不用调用_data了
				console.log(JSON.stringify(this.user));
			}
		}
	})
</script>
```

#### 1.6.7.4 修饰符

官方参考文档：[表单输入绑定 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/essentials/forms.html)

当然`v-model`也有一些修饰符。当然我们也可以对`v-model`得修饰符进行连写操作`v-model.lazy.number`

![[00 assets/c7eb695c4c7f3b41c4cef0712e1a05d3_MD5.jpeg]]

#### 1.6.7.5 :model

1、对于`:model`并不是`v-model`的简写，而是`v-bind:model`的简写，在`elementui`中要注意这 2 类指令的写法

2、如果写成`v-model`的话就会导致`el-form`做校验的时候读取不到数据

![[00 assets/89a6add97050463e2934d32ceddfc823_MD5.png]]

#### 1.6.7.6 h 函数使用 v-modal

1、一些组件库，比如：naive-ui 会使用 **h 函数** 来做数据渲染，一些情况我们需要去做一些额外的处理，我们都知道 **v-modal 本质其实一个语法糖**，在 h 函数 中就不能再使用这个语法糖了，下面代码就是解决方法

![[00 assets/03f0566a6b62e14b0655a66ef46b23eb_MD5.png]]

### 1.6.8 v-memo

官方文档：[内置指令 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/built-in-directives.html#v-memo)

这个是为了做性能优化，只要`v-memo`数组中包含的属性，就会更新下面的子树中的模板

![[00 assets/d412e23d380a9e938b1ab567eb76ac98_MD5.png]]

### 1.6.9 条件渲染

#### 1.6.9.1 v-if

使用`v-if`渲染的话，条件为`false`那么连`HTML标签`都不会渲染

![[00 assets/2b33074c8b289e5ce1044de4a96355fa_MD5.png]]

我们不仅可以使用`v-if`，还有`v-if-else`和`v-else`。分别对应的就是语句中的`if { }`、`else if { }`、`eles { }`。

并且添加了`v-if`、`v-if-else`和`v-else`指令的标签之间不能添加其他标签，必须连在一起

```vue
// ------------- Vue2、Vue3同理 -------------- //
<div class="main">
	<p>n:{{n}}</p>
	<button type="button" @click="n++">点击我</button>
	<div v-if="n===1">很好</div>
	<div v-else-if="n===2">不好</div>
	<div v-else-if="n===3">一般</div>
	<div v-else>啥啥</div>
</div>
<script type="text/javascript">
	let vm = new Vue({
		el:'.main',
		data:{
			n:1
		},
	});
</script>
```

还有一个方式就是使用`template标签`和`v-if指令`，这个标签最大的好处就是你写在里面的标签并不会破坏页面原本的结构。我们可以看下图的开发者工具，会发现渲染的时候就不见了，而且`template标签`只能和`v-if`一起使用，但是不能和`v-show`一起使用

```html
// ------------- Vue2、Vue3同理 -------------- //
<div class="main">
	<p>n:{{n}}</p>
	<button type="button" @click="n++">点击我</button>
	<template v-if='n===1'>
		<div>很好</div>
		<div>不好</div>
		<div>一般</div>
		<div>啥啥</div>
	</template>
</div>
<script type="text/javascript">
	let vm = new Vue({
		el:'.main',
		data:{
			n:1
		}
	});
</script>
```

![[00 assets/ef944e0446eeb1b2765c3661666e9715_MD5.png]]

#### 1.6.9.2 v-show

官方文档参考：[条件渲染 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/essentials/conditional.html#v-show)

`v-show`的的本质就是为该元素添加`display:none;`

```vue
<div v-show="false">Hello World!</div>
```

### 1.6.10 列表渲染

#### 1.6.10.1 基本使用

`v-for`包含 2 个参数，`item`表示是下面的每个对象，`index`表示得索引，其中`index`是可以选的。并且对于列表循环最好还是添加`:key`，这是为了循环的性能和`diff`的比对

```html
// ------------- Vue2、Vue3同理 -------------- //
<ul id="main">
	<h2>人员名单</h2>
	<li v-for="(item,index) in Person" :key='id'>
		{{p.name}},{{p.age}},{{index}}
	</li>
</ul>
<script type="text/javascript">
	let vm = new Vue({
		el:'#main',
		data:{
			Person:[
				{id:1,name:'张三',age:18},
				{id:2,name:'李四',age:19},
				{id:3,name:'王五',age:20}
			]
		}
	})
</script>
```

![[00 assets/5bebcb9e3581d118920cc152256ec545_MD5.jpeg]]

我们使用`v-for`不仅仅可以遍历数组，还可以遍历`对象、字符串、数字`。并且`v-for`遍历对象的时候里面包含 3 个值，分别为`value、key、index`

![[00 assets/69740d851c36ef5a674af08bc2eba917_MD5.png]]

当然`v-for`也可以使用`of`来遍历，第一个参数是`value`，第二个参数为`key`，即：`键值`

```html
// ------------- Vue2、Vue3同理 -------------- //
<ul id="main">
	<h2>人员名单</h2>
	<li v-for="(value,key) of Person">
		{{value}},{{key}}
	</li>
</ul>
<script type="text/javascript">
	let vm = new Vue({
		el:'#main',
		data:{
			Person:{
				id:1,
				name:'张三',
				age:19,
				sex:'男',
			}
		}
	})
</script>
```

![[00 assets/fd63feafbfbf1869b081f94ea1933321_MD5.jpeg]]

假如我们想要数组处理的列表渲染也是响应式的话，可以使用下面的方法

![[00 assets/01f2ee54071655a20187a5d2ed47ad60_MD5.png]]

#### 1.6.10.2 VNode

![[00 assets/23621806bdab8f876e05011576316438_MD5.png]]

最后的结构会创建一个`VNode`树。但是为什么需要构建这样一个树？为了做`diff算法`，还为了跨平台，比如该`虚拟DOM`可以渲染成`真实DOM`到`浏览器`中，还可以渲染到安卓中的控件来部署到`安卓`中

![[00 assets/85fb4843dacd23ca67eb20920b977108_MD5.png]]

#### 1.6.10.3 key

首先我们在上面的基本渲染篇描述了 key，其实 key 就是身份证

我们可以看下面 GIF 图，是不是 input 有错位的问题，假如我们把:key 里面的值改为 p.id 或这 p.name 的时候就没任何问题

```html
// ------------- Vue2、Vue3同理 -------------- //
<ul id="main">
	<button type="button" @click="Add">点击我</button>
	<li v-for="p in Person" :key="index">
		{{p.name}},{{p.age}}
		<input type="text"/>
	</li>
</ul>
<script type="text/javascript">
	let vm = new Vue({
		el: '#main',
		data: {
			Person: [
				{id: 1,name: '张三',age: 18},
				{id: 2,name: '李四',age: 19},
				{id: 3,name: '王五',age: 20}
			]
		},
		methods:{
			Add(){
				let per = {id:4,name:'刘六',age:21}
				this.Person.unshift(per);
			}
		}
	})
</script>
```

![[00 assets/d0b7fe68071b67a9cdc078f72efc30e7_MD5.gif]]

下面是文字的描述，建议看视频的描述

我们一开始的初始数据就是 id 为 001、002、003，我们根据数据来生成虚拟的 DOM，但是要记住只是生成的虚拟的，只是在内存中并不在页面中，相当于你只是创建了，但是还没和页面连接

假如我们加入一个新的数据，我们根据新的数据生成的虚拟 DOM，但是后面的步骤不是直接根据这个虚拟的 DOM 来创建真实的 DOM，不然的话这样设置一个虚拟 DOM 就没必要了，所以这个时候就进行虚拟 DOM 的对比算法

这个时候就需要使用 key 了，首先是 key=0 的时候和初始数据的虚拟 DOM 中的 key=0 对比，里面有 2 个节点，第一个是文字节点，第二个是 input 节点，通过检测文字节点并不是一样的，所以就替换了初始 DOM 里面的文字节点，但是 input 节点是一样的，所以就直接使用

后面的节点依次类推，key=1 的虚拟 DOM，文字节点也会替换，input 节点直接使用，到了 key=3 的时候，发现初始 DOM 里面没有，所以就直接添加上去

![[00 assets/52d156c6205a9f74aefe200d7edcf8b2_MD5.png]]

这就是为什么会有这样的问题，要注意的是这个情况并不是经常发生，我们在正常使用的时候不会打乱 index 的值，所以故意让它错是为了引出这个解释

假如你使用 p.id 的话就不会有问题

![[00 assets/cd4f2c5d3eb186360c933e5ac931d8f9_MD5.png]]

这样的话，我们没有使用 key 的话，就会 vue 就会默认写一个 index

**总结**

![[00 assets/3f40fc3674b16657f7af2b08a2ec9701_MD5.jpeg]]

#### 1.6.10.4 实践

##### 1.6.10.4.1 列表过滤

实现下面的功能，本质其实是`watch`和`computed`的对比

![[00 assets/6b5b125044ade2dc46710ad31f65590a_MD5.gif]]

> watch 版本

```vue
// ------------- Vue2、Vue3同理 -------------- //
<ul id="main">
	<input type="text" v-model="keyWard"/>
	<li v-for="p in filPerson" :key="p.id">
		{{p.name}},{{p.age}},{{p.sex}}
	</li>
</ul>
<script type="text/javascript">
	let vm = new Vue({
		el: '#main',
		data: {
			keyWard:'',
			Person: [
				{id: 1,name: '张三',age: 28,sex:'男'},
				{id: 2,name: '李四',age: 19,sex:'男'},
				{id: 3,name: '王五',age: 21,sex:'女'},
				{id: 4,name: '刘六',age: 20,sex:'女'}
			],
			filPerson:[]
		},
		watch:{
			keyWard:{
				immediate:true,
				handler(val){
					this.filPerson = this.Person.filter((p)=>{
						return p.name.indexOf(val) !== -1;
					})
				}
			}
		}
	});
</script>
```

> computed 版本

```vue
// ------------- Vue2、Vue3同理 -------------- //
<ul id="main">
	<input type="text" v-model="keyWard"/>
	<li v-for="(p,index) of filPerson" :key="index">
		{{p.name}},{{p.age}},{{p.sex}}
	</li>
</ul>
<script type="text/javascript">
	let vm = new Vue({
		el: '#main',
		data: {
			keyWard:'',
			Person: [
				{id: 1,name: '张三',age: 28,sex:'男'},
				{id: 2,name: '李四',age: 19,sex:'男'},
				{id: 3,name: '王五',age: 21,sex:'女'},
				{id: 4,name: '刘六',age: 20,sex:'女'}
			]
		},
		computed:{
			filPerson(){
				return this.Person.filter((p)=>{
					return p.name.indexOf(this.keyWard) !== -1;
				})
			}
		}
	});
</script>
```

##### 1.6.10.4.2 列表排序

```vue
// ------------- Vue2、Vue3同理 -------------- //
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="../js/vue.js"></script>
		<style type="text/css">

		</style>
	</head>
	<body>
		<ul id="main">
			<input type="text" v-model="keyWard" />
			<li v-for="(p,index) of filPerson" :key="index">
				{{p.name}},{{p.age}},{{p.sex}}
			</li>
			<button type="button" @click="sortType = 1">升序</button>
			<button type="button" @click="sortType = 2">降序</button>
			<button type="button" @click="sortType = 0">原序</button>
		</ul>
		<script type="text/javascript">
			let vm = new Vue({
				el: '#main',
				data: {
					keyWard: '',
					sortType: 0,
					Person: [
						{id: 1,name: '张王三',age: 28,sex: '男'},
						{id: 2,name: '李刘四',age: 19,sex: '男'},
						{id: 3,name: '王李五',age: 21,sex: '女'},
						{id: 4,name: '刘张六',age: 20,sex: '女'}
					]
				},
				computed: {
					filPerson() {
						let arr = this.Person.filter((p) => {
							return p.name.indexOf(this.keyWard) !== -1;
						})
						if (this.sortType) {
							arr.sort((a, b) => {
								return this.sortType === 1 ? b.age - a.age : a.age - b.age;
							});
						}
						return arr;
					}
				}
			});
		</script>
	</body>
</html>
```

## 1.7 事件绑定

### 1.7.1 基本使用

编写事件指令`v-on(@)`及触发条件(`click`)，并且指明方法

```html
// ------------- Vue2，但是Vue3使用的setup语法就直接写在script中即可 -------------- //
<button type="button" v-on:click="say">点击我</button>
<script type="text/javascript">
	let v = new Vue({
		el:'button',
		data:{
			name:'张三'
		},
		methods:{
			say(){
				console.log("你好!");
			}
		}
	})
</script>
```

### 1.7.2 参数传递

> 不传递参数

在默认不传递参数的情况下第一个是事件对象，也就是下面的`a`。其中`event`就是`原生JS`里面的`event`，其他的都是`undefined`

```javascript
// ------------- Vue2，但是Vue3使用的setup语法就直接写在script中即可 -------------- //
let v = new Vue({
	el:'button',
	data:{
		name:'张三'
	},
	methods:{
		say(a,b,c,d){
			console.log(a,b,c,d);
		}
	}
})
```

![[00 assets/9284ebea68cb05dabb2a0d125fa63291_MD5.png]]

> 传递参数

假如我们传递一个参数，这个时候`event`就不会默认被赋值上去了

```html
// ------------- Vue2，但是Vue3使用的setup语法就直接写在script中即可 -------------- //
<button type="button" v-on:click="say(18)">点击我</button>
<script type="text/javascript">
	let data = {
		name:'张三'
	}
	let v = new Vue({
		el:'button',
		data:data,
		methods:{
			say(a,b,c,d){
				console.log(a,b,c,d);
			}
		}
	})
</script>
```

![[00 assets/44765d3f468075a2311e8607c86109e7_MD5.png]]

为了防止一些业务需求，我们也可以加上`$event`来传递`event`对象

```html
// ------------- Vue2，但是Vue3使用的setup语法就直接写在script中即可 -------------- //
<button type="button" v-on:click="say(18,$event)">点击我</button>
//button的点击事件也可以简写
<button type="button" @click="say(18,$event)">点击我</button>

<script type="text/javascript">
	let data = {
		name:'张三'
	}
	let v = new Vue({
		el:'button',
		data:data,
		methods:{
			say(a,b,c){
				console.log(a,b,c);
			}
		}
	})
</script>
```

![[00 assets/aa44e08b29ea70d4f5943dba8e48d58c_MD5.png]]

### 1.7.3 事件修饰符

#### 3.2.1 基本使用

假如需要使用到事件修饰符的话可以参考**官方文档**：[事件处理 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/essentials/event-handling.html#event-modifiers)，下图为基本的事件修饰符

![[00 assets/ece4f1bef1b4e9d05361f5158cdc001b_MD5.png]]

使用事件里面的修饰符`prevent`来移除元素的默认行为

```html
// ------------- Vue2、Vue3同理 -------------- //
// 使用原生的来移除默认行为
<a href="http://www.baidu.com" @click="say">点击我跳转</a>
<script type="text/javascript">
	let v = new Vue({
		el:'a',
		methods:{
			say(event){
				alert("你点击了");
				event.preventDefault();
			}
		}
	})
</script>

// 也可以直接使用事件修饰符处理
<a href="http://www.baidu.com" @click.prevent="say">点击我跳转</a>
<script type="text/javascript">
	let v = new Vue({
		el:'a',
		methods:{
			say(){
				alert("你点击了");
			}
		}
	})
</script>
```

![[00 assets/57241a4510430914f11436d63192af59_MD5.gif]]

#### 3.2.2 stop、once、capture、self

下面基本在原生 JS 里面都介绍过

```html
//stop	//阻止事件的冒泡
//假如你不使用stop的话就会出现2次alert
<div id="main" @click="say">
	<button type="button" @click.stop="say">点击我</button>
</div>
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(event){
				alert("你点击了");
			}
		}
	})
</script>

//once //事件只能触发一次
<div id="main">
	<button type="button" @click.once="say">点击我</button>
</div>
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(event){
				alert("你点击了");
			}
		}
	})
</script>

//capture	//更改为事件的捕获
//冒泡是事件往父元素浮动，捕获就是你点击父元素，捕获到子元素
<div id="main">
	<button type="button" @click.capture="say">点击我</button>
</div>
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(event){
				alert("你点击了");
			}
		}
	})
</script>

//self	//只有event.target的元素才能触发事件
//冒泡是事件往父元素浮动，捕获就是你点击父元素，捕获到子元素
<div id="main" @click.slef="say">
	<button type="button" @click="say">点击我</button>
</div>
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(event){
				console.dir(event.target);
			}
		}
	})
</script>
```

#### 3.2.3 passive

在了解该事件修饰符之前，我先来介绍一下`wheel`和`scroll`

`wheel`和`scroll`的关注主体是不一样的，`wheel`关注的是`鼠标的滚轮`，而`scroll`关注的是`滚动条`

```html
// ------------- Vue2、Vue3同理 -------------- //
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<script src="../js/vue.js"></script>
		<style type="text/css">
			#main{
				width: 200px;
				height: 200px;
				overflow: auto;
				background-color: burlywood;
			}
			#main li{
				height: 100px;
			}
		</style>
	</head>
	<body>
		<ul id="main" @scroll="say">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
			<li>5</li>
		</ul>
		<script type="text/javascript">
			let v = new Vue({
				el:'#main',
				methods:{
					say(event){
						console.dir(event.target);
					}
				}
			})
		</script>
	</body>
</html>

```

![[00 assets/2c3a64444ba64e0ad822d82b3c2c6549_MD5.gif]]

假如我们将`scroll`改为`wheel`话

![[00 assets/330d8baea0659fe2382383c143f4f915_MD5.gif]]

唯一的不同就是监听的主体不一样，`scroll`是滚动条滚动就触发事件，但是`wheel`就是鼠标滚轮滚动就触发事件，所以第二张图是滚到底了，但是鼠标滚轮继续滚动，就继续触发事件

`passive` 事件的默认行为立即执行，无需等待事件回调执行完毕

```html
// ------------- Vue2、Vue3同理 -------------- //
<!DOCTYPE html>
<html lang="zh">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title></title>
		<script src="../js/vue.js"></script>
		<style type="text/css">
			#main{
				width: 200px;
				height: 200px;
				overflow: auto;
				background-color: burlywood;
			}
			#main li{
				height: 100px;
			}
		</style>
	</head>
	<body>
		<ul id="main" @wheel="say">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
			<li>5</li>
		</ul>
		<script type="text/javascript">
			let v = new Vue({
				el:'#main',
				methods:{
					say(event){
						for (let i = 0; i < 10000000; i++) {
							console.log("#");
						}
					}
				}
			})
		</script>
	</body>
</html>

```

我们先使用`scroll`来验证一下，是不是在滚动的同时回调函数也在执行

![[00 assets/5900b1e07e1d0ce3da6a81099d6fe307_MD5.gif]]

但是我们来看下`wheel`，必须回调函数执行完毕之后再滚动滚动条

![[00 assets/6b3d5b5fcc8cdb5583fc2466cf2cea9d_MD5.gif]]

所以这里我们需要使用`passive`来取消`wheel`这种情况

### 1.7.4 键盘事件

键盘的事件有`keyup`和`keydown`

![[00 assets/4b1ee0835fc01907eb453008ae9bd672_MD5.jpeg]]

这个 vue 为你添加的按键其实是设置了一个限制，只有你键盘输入`enter`或者`esc`....的话，才能执行后面的回调函数，不然的话是执行不了的，不像原生 JS 你按下任意键都执行函数

```html
// ------------- Vue2、Vue3同理 -------------- //
<input type="text" id="main" @keydown.enter="say"  />
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(){
				console.log('1');
			}
		}
	})
</script>
```

但是要注意 tab 键，

我们使用下面的代码，是不是并不能执行，这是因为你按下 tab 的时候，也就是按下，不等按键弹起来就会失去对文字框焦点，所以我们要改的话，就要改为 keydown

```html
// ------------- Vue2、Vue3同理 -------------- //
<input type="text" id="main" @keyup.tab="say"  />
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(){
				console.log('1');
			}
		}
	})
</script>

//改进为

<input type="text" id="main" @keydown.tab="say"  />
<script type="text/javascript">
	let v = new Vue({
		el:'#main',
		methods:{
			say(){
				console.log('1');
			}
		}
	})
</script>
```

下面就是和 tab 的感觉是差不多的

![[00 assets/2ba69c3652b24d132de71285c467ef12_MD5.jpeg]]

这里有一个要注意的问题，现在 KeyCode 这个方法已经从 Web 标准中去除了，所以谨慎使用，下面的是 vue 自带的自定义的按键设置

```html
// ------------- Vue2、Vue3同理 -------------- //
<input type="text" id="main" @keydown.hui="say"  />
<script type="text/javascript">
	Vue.config.keyCodes.hui = 13;	//自定义的家键盘按键：回车
	let v = new Vue({
		el:'#main',
		methods:{
			say(){
				console.log('1');
			}
		}
	})
</script>
```

### 1.7.5 动态事件绑定

参考链接：[内置指令 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/built-in-directives.html#v-on)

1、在一些情况下我们需要**通过配置得形式将一个事件传递给下面得组件**，比如：我封装了一个高阶组件，我通过配置得形式来动态生成表单，而表单有很多得事件绑定，我们就需要进行动态绑定，将事件写在父组件中，这样我们就可以通过配置来决定哪些事件可以去监听

2、直接参考下面得写法即可，有对应得解决方法

![[00 assets/955f60d358fa5e773c41849d9b0590e6_MD5.png]]

### 1.7.6 事件总结

我们的事件修饰符可以连着写，

```html
// ------------- Vue2、Vue3同理 -------------- //
<div @click="say">
	<a href="www.bilibili.com" id="main" @click.stop.prevent="say">点击我</a>
</div>
<script type="text/javascript">
	Vue.config.keyCodes.hui = 13;//定义的回车
	let v = new Vue({
		el:'#main',
		methods:{
			say(){
				console.log('1');
			}
		}
	})
</script>
```

当然我们的键盘事件也可以连着写，下面的就是 ctrl+y 按着就可以执行回调函数

```html
// ------------- Vue2、Vue3同理 -------------- //
<div @click="say">
    <input type="text" @keydown.ctrl.y="say" id="main"/>
</div>
<script type="text/javascript">
	Vue.config.keyCodes.hui = 13;//定义的回车
	let v = new Vue({
		el:'#main',
		methods:{
			say(){
				console.log('1');
			}
		}
	})
</script>
```

## 1.8 计算属性

### 1.8.1 原始写法

我们来和计算属性进行对比，下面是使用`methods`和`插值语法`进行处理

![[00 assets/6a50d938b143473bfa4cc0f9e163d326_MD5.gif]]

**使用下面的方式有很多的缺点**

1.每次你改变了 data 里面的值的时候，vue 会重新渲染页面，所以 methods 里面的 add 函数也会重新执行一遍，这样的话，执行的效率会比较低

2.逻辑不清晰

```vue
// ------------- Vue2、Vue3同理 -------------- //
/ ------- methods写法 ------- /
<div id="main">
	<input type="text" id="main_inp" v-model="name"/>
	<input type="text" id="main_inp2" v-model="name1"/>
	<p>{{add()}}</p>
</div>
<script type="text/javascript">
	let f1 = new Vue({
		el:'#main',
		data:{
			name:'张',
			name1:'三'
		},
		methods:{
			add(){
				return this.name + this.name1;
			}
		}
	})
</script>

/ ------- 插值语法 ------- /
<div id="main">
	<input type="text" id="main_inp" v-model="name"/>
	<input type="text" id="main_inp2" v-model="name1"/>
	<p>{{name}} + {{name1}}</p>
</div>
<script type="text/javascript">
	let f1 = new Vue({
		el:'#main',
		data:{
			name:'张',
			name1:'三'
		},
		methods:{
			add(){
				return this.name + this.name1;
			}
		}
	})
</script>
```

### 1.8.2 计算属性使用

![[00 assets/f9e5ee9dc5937a5d6c634de5ce5a04d4_MD5.png]]

使用**计算属性是要用的属性本身就不存在**，要通过**己有的属性**计算而来的，要注意理解这句话，是已有的属性，假如你在 vue 外面写一个变量的话，vue 就检测不到了，所以你改变了这个变量，计算属性是不改变的，而且底层借助**defineproperty**方法来提供的**getter**和**setter**

**计算属性被调用**的情况：1、一开始的读取得时候 2、和计算属性关联的值改变

而且计算属性有一个**缓存的机制**，假如你是 methods 的话，比如上面的 Add()，每次调用函数的话，就会自动执行一次，但是计算属性有一个缓存机制，所以下面我写了很多的`fullname`，但是最后也只会执行一次，这个就是一个性能优化

```vue
// ------------- Vue2、Vue3同理 -------------- //
<script type="text/javascript">
	let f1 = new Vue({
		el:'#main',
		data:{
			name:'张',
			name1:'三'
		},
		computed:{
            // 简写 - plus
			fullname(){
				return this.name + ',' + this.name1;
			},
            // 简写
            fullname:function(){
				return this.name + ',' + this.name1;
			},
            // 完整写法
            fullname:{
                // 当需要输出的时候就调用get()
				get(){
					return this.name + ',' + this.name1;
				}
                // 当下面的值改变就会改变
                set(val){
					const arr = val.split(',');
					this.name = arr[0];
					this.name1 = arr[1];
				}
			}
		}
	})
</script>
```

## 1.9 侦听器

### 1.9.1 基本使用

对象名为监听的属性名，只要被监听的属性发生了改变，那么就会执行里面的`handler`属性

```vue
// ------------- Vue2、Vue3同理 -------------- //
<div id="main">
	<button type="button" @click="q">点击我切换</button>
	<p>现在的天气真的是{{qie}}</p>
</div>
<script type="text/javascript">
	const vm = new Vue({
		el:'#main',
		data:{
			flag:true
		},
		methods:{
			q(){
				this.flag = !this.flag;
			}
		},
		computed:{
			qie(){
				return this.flag ? '炎热' : '寒冷';
			}
		},
        watch:{
            // 1. 可以监视data中的属性
			flag:{
				immediate:true,	// 2. 初始化的时候就执行一次
				handler(newValue,oldValue){ // 3. 分别是改变后的数据和改变前的数据
					console.log(newValue,oldValue);
				}
			},
            flag(){ // 4. 简写
                console.log(newValue,oldValue);
            }
            // 5. 当然也可以监视computed中的属性
            qie:{
				immediate:true,
				handler(newValue,oldValue){
					console.log(newValue,oldValue);
				}
			},
            qie(){
				return this.flag ? '炎热' : '寒冷';
			}
		}
	})
</script>
```

假如监听的是对象的话，返回的就是一个`Proxy`对象，处理起来很难受。所有有下面的 2 种方式变为普通对象

```javascript
watch: {
   // 使用监听器-简写
   firstname(newValue, oldValue) {
       console.log(newValue, oldValue);

      // 1.方式一
      let obj = {...newValue}
      // 2.方式二
      let obj = Vue.toRaw(newValue)
   },
},
```

### 1.9.2 深度监听

`Vue`本身是可以检测到对象的内部值得改变，但是 vue 里面得 watch 是默认不检测，所以我们需要开启 watch 得深度检测模式，也就是 deep。假如使用这种形式就不能使用侦听器的简写形式了

```html
<div id="main">
	<button type="button" @click="num.a++;num.b++">点击我切换</button>
	<p>{{num.a}},{{num.b}}</p>
</div>
<script type="text/javascript">
	const vm = new Vue({
		el:'#main',
		data:{
			num:{
				a:1,
				b:2
			}
		},
		watch:{
            deep:true,
			num:{
				handler(){
					console.log('1')
				}
			}
		}
	})
</script>
```

首先我们需要理解一个点，就是我们平常直接写侦听属性的时候都是直接写的，这是因为`JS引擎`给我们自动处理的，但是其实真正的写法是`'num'`。

假如我们需要侦听`num`下面的`a`的时候，可以不书写`deep`属性，手动指定对象下面的属性值

```html
<div id="main">
	<button type="button" @click="num.a++">点击我切换</button>
	<p>{{num.a}}</p>
</div>
<script type="text/javascript">
	const vm = new Vue({
		el:'#main',
		data:{
			num:{
				a:1,
				b:2
			}
		},
		watch:{
            //深度监视
			'num.a':{
				handler(){
					console.log('1')
				}
			}
		}
	})
</script>
```

当然`watch`还有其他的`options`

![[00 assets/cf485867d2f6aa3feefcfcec6f339881_MD5.png]]

### 1.9.3 其他写法

我们也可以在生命周期函数中这样书写

![[00 assets/40b59484eef1375d555e91284408ea4c_MD5.png]]

## 1.10 购物车案例

下面为一开始我自己编写的购物车案例，有很多的不足

```vue
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .BookTable {
        border-collapse: collapse;
      }
      .BookTable th,td {
        border: 1px solid #aaa;
        padding: 8px 16px;
      }
    </style>
  </head>
  <body>
    <div class="BookTable">
      <table class="BookTable">
        <thead>
          <tr>
            <th></th>
            <th>书籍名称</th>
            <th>出版日期</th>
            <th>价格</th>
            <th>购买数量</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item,index) in booklist" :key="item.id">
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
            <td>{{item.time}}</td>
            <td>{{item.price * item.num}}</td>
            <td>
              <button @click="reduceNum(item.id)" :disabled="item.num==0">
                -
              </button>
              {{item.num}}
              <button @click="addNum(item.id)">+</button>
            </td>
            <td>
              <button @click="removeBook(index)">移除</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div>总计:{{total}}</div>
    </div>

    <script src="./Vue.js"></script>
    <script>
      const app = Vue.createApp({
        data: function () {
          return {
            booklist: [
              {
                id: 1,
                name: "Java基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
              {
                id: 2,
                name: "JavaScript基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
              {
                id: 3,
                name: "Go基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
              {
                id: 4,
                name: "CSS基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
            ],
            total: 0,
          };
        },
        methods: {
          reduceNum(index) {
            let { booklist } = this;
            if (booklist[--index].num != 0) {
              booklist[index].num -= 1;
            }
          },
          addNum(index) {
            let { booklist } = this;
            booklist[--index].num += 1;
          },
          removeBook(index) {
            let { booklist } = this;
            booklist.splice(index, 1);
          },
        },
        watch: {
          booklist: {
            handler(newValue, oldValue) {
              let { booklist } = this;
              this.total = 0;
              booklist.forEach((ele) => {
                this.total += ele.price * ele.num;
              });
            },
            deep: true,
            immediate: true,
          },
        },
      });

      app.mount(".BookTable");
    </script>
  </body>
</html>
```

下面为修改之后案例，修改很多的地方，可以参考一下

```vue
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .BookTable {
        border-collapse: collapse;
      }
      .BookTable th,
      td {
        border: 1px solid #aaa;
        padding: 8px 16px;
      }
      .SelectTr {
        background-color: cadetblue;
        opacity: 0.5;
      }
    </style>
  </head>
  <body>
    <div class="BookTable">
      <template v-if="booklist.length">
        <table class="BookTable">
          <thead>
            <tr>
              <th></th>
              <th>书籍名称</th>
              <th>出版日期</th>
              <th>价格</th>
              <th>购买数量</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(item,index) in booklist"
              :key="item.id"
              @click="SelectBook(item.id)"
              :class="{SelectTr:index === currentIndex}"
            >
              <td>{{item.id}}</td>
              <td>{{item.name}}</td>
              <td>{{item.time}}</td>
              <td>{{formatePrice(item.price * item.num)}}</td>
              <td>
                <button @click="reduceNum(item)" :disabled="item.num==0">
                  -
                </button>
                {{item.num}}
                <button @click="addNum(item)">+</button>
              </td>
              <td>
                <button @click="removeBook(index)">移除</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div>总计:{{formatePrice(totalPrice)}}</div>
      </template>
      <div v-else>没有更多的数据了~</div>
    </div>

    <script src="./Vue.js"></script>
    <script>
      const app = Vue.createApp({
        data: function () {
          return {
            booklist: [
              {
                id: 1,
                name: "Java基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
              {
                id: 2,
                name: "JavaScript基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
              {
                id: 3,
                name: "Go基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
              {
                id: 4,
                name: "CSS基础",
                time: "2022-12-12",
                price: 12,
                num: 1,
              },
            ],
            currentIndex: -1,
          };
        },
        methods: {
          reduceNum(item) {
            item.num--;
          },
          addNum(item) {
            item.num++;
          },
          removeBook(index) {
            this.booklist.splice(index, 1);
          },
          formatePrice(price) {
            return "￥" + price;
          },
          SelectBook(id) {
            this.currentIndex = --id;
          },
        },
        computed: {
          totalPrice() {
            return this.booklist.reduce((preValue, curValue) => {
              return preValue + curValue.price * curValue.num;
            }, 0);
          },
        },
      });

      app.mount(".BookTable");
    </script>
  </body>
</html>

```

1.`total`的问题，在一开始案例中我使用了`watch`来监听，只要数组中的数据改变就自动变化`total`的值，这个逻辑是没问题的，但是我们有更好的处理方式。那就是使用`computed`，只要里面使用的数据，变化之后就会自动重新计算值，这很显然书写的逻辑比上面的`watch`的版本好很多

2.函数传值的问题，来对列表中的数据进行加减。其核心的逻辑就是找到你点击的那一列，然后在数组中对里面的数据进行操作。所以该问题的本质就是对数据进行操作，这里我们可以直接将数据传入即可。不用传入索引，再通过索引来查找数据，再来对数据进行操作

3.`函数抽象`，这里面有一个对价格前面拼接"￥"的操作，可以的话这里直接抽象为一个数组，假如后续需要修改为其他字符的时候，直接修改这里前面的字符"￥"即可

4.`排他思想`，这里有一个需求。只要点击列表中的一项，就会自动为该项添加颜色

![[00 assets/8fb0290e161a38d736fa23c0b7100d17_MD5.jpeg]]

下面为核心的代码，在以前`JQuery`中学习的排他思想，就是消除所有元素的属性，为自己添加属性。下面是通过`:class`的对象形式的写法来实现的，只要该属性值为`true`的话就设置`class`为该属性。

其中主要的是对点击的索引进行存储，所以这里使用了点击事件来进行处理，

![[00 assets/e720b90321d49d6dd2ac51919866e0c4_MD5.png]]

## 1.11 组件化开发

### 1.11.1 全局组件

![[00 assets/ea74662a4bdc2f0c043c8a90c24983a1_MD5.jpeg]]

下面就是使用`app.component`来注册一个组件

![[00 assets/74bb69506a9727eb1839ea9e7650e0d0_MD5.png]]

当然我们也可以将组件中得`template`抽取到外面

![[00 assets/8328517cd6526865d91ad780dca28e8a_MD5.jpeg]]

在使用`app.component`注册组件的时候需要注意组件名

![[00 assets/58e6c1c8e55e417b32d11a5769d78d93_MD5.png]]

### 1.11.2 局部组件

![[00 assets/f637e88906737b8d1f89cc4a1b5febae_MD5.png]]

下图就是注册局部组件

![[00 assets/e3eb357ee0804d871d2fa2136cfbfe4b_MD5.jpeg]]

# 2. 脚手架 - OptionsAPI

下面记录得笔记都为`Vue3`中得语法，如果需要可以查看我`Vue2`得笔记

## 2.1 基本介绍

### 2.1.1 Vue CLI

![[00 assets/b0d7d79237ec8f98906826b91cfc9b0e_MD5.png]]

> webpack

首先先是安装 vue 的脚手架，这个在 npm 的笔记里面有

```bash
npm i -g @vue/cli	//只在第一次配置
```

然后我们在我们要创建项目的文件下面打开 cmd，这里就有 vue 的脚手架和 vue 的基础项目

```bash
vue create XXX	//XXX表示的项目名字
```

babel 就是 ES6 转换为 ES5 的，这个在 ES6-ES11 的笔记里面有，eslient 是语法提示工具

![[00 assets/1ea94ed5bb3c3d3f18e0fd6279973d54_MD5.png]]

假如我们下载完毕的话，就是下面的这个样子

![[00 assets/8d8201814d46a89e4a8756d015095fba_MD5.jpeg]]

我们再进入这个文件夹里面

```bash
cd vue_test
```

我们再使用这个代码就可以编译代码了

```bash
npm run serve
```

> vite

下面就是创建一个`vite`项目

```bash
npm init vue@latest  // 安装create-vue工具，使用create-vue工具创建vue项目
```

剩下的操作和`webpack`基本都是一样的

> pnpm

我们可以使用`pnpm`来接替`npm`作为包管理工具

```bash
pnpm create vite my-vue-app --template vue	// 创建my-vue-app的vite项目
pnpm add 	// 下载所有的包
```

### 2.1.2 项目文件分析

可能各个版本的文件都不一样，所以这里只是提示的比较关键的文件配置

![[00 assets/d8a900d369b5067fa4051c06ed77c43e_MD5.png]]

### 2.1.3 声明式和命令式编程

![[00 assets/1fa123aafe883a05be171f7c471d0ee5_MD5.jpeg]]

命令式编程：每一步都需要自己操作

声明式编程：只需要提供数据和方法就可以自动完成操作

![[00 assets/d174603a192ff9cdec6738fc6d1f0eeb_MD5.png]]

### 2.1.4 VSCode 代码片段

`VSCode代码片段`就是我们在生成`html5格式`的时候输入的`!`。当我们输入设定好的语法，那么就会生成已经配置好的代码片段来使用，这样的话就减少了写重复代码的时间

1.首先写好代码片段

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <div id="main">
      <h2>{{message}}</h2>
    </div>

    <script src="./Vue.js"></script>
    <script>
      const app = Vue.createApp({
        data: function () {
          return {
            message: "Hello World!",
          };
        },
      });

      app.mount("#main")
    </script>
  </body>
</html>
```

2.进入网站配置`VSCode`语法，[snippet generator (snippet-generator.app)](https://snippet-generator.app/)

![[00 assets/a0761ad8ab4bd89d623383b2140629cf_MD5.png]]

**\***当然还有很多其他的代码片段的语法

![[00 assets/efb04181803b49251f1aa33cace32526_MD5.png]]

3.`VSCode`配置，首先进入设置就有一个`配置用户代码片段`

![[00 assets/d556543fee864501fab5c3bcb25e68f5_MD5.png]]

然后将代码复制过来即可

![[00 assets/f7b6e069b8f8f2e0308d420a796bf990_MD5.png]]

配置完毕之后，以后只需要输入`VueCreate`就会出现下面的代码

### 2.1.5 组件化理解

在组件化开发之前，先来看下面的案例

其实工程化得本质就是将`App`中得`script`和`template`抽取出来，放到对象里面。所以我们使用下面得方式也是可以正常渲染页面，其中导包得时候要导入`vue.esm-bundler.js`才可以。

![[00 assets/a50ed1df67db563ed25d527c6925d325_MD5.png]]

下面是解释为什么使用`template选项`的时候需要使用`vue.esm-bundler.js`文件

下面为`Vue`渲染节点的过程，这个在`VNode`中提过一点。首先`Vue`会将元素转换为一个个的`VNode`，其实每个`VNode`都是一个函数，走的都是`createVNode函数`创建的，然后才会转换为虚拟`DOM`，再来转换为`真实DOM`。

![[00 assets/c94bc6ac57b74bc944b25d493c6d7214_MD5.png]]

但是为什么编写`template`的时候需要引入`vue.esm-bundler.js`呢？而编写的`App.vue`就不需要引入？这是因为在`webpack`编译的时候加载了一个`vue-loader`的`loader`，会自动将标签转换为一个个的`VNode`，所以在`Vue`的源码中不需要`compile`的过程，但是对于`template`选项来说`webpack`并不会进行识别，所以需要引入`vue.esm-bundler.js`

### 2.1.6 Scoped

其实`Vue`中的`Style`包含自己的作用域，这里的使用的原理就是使用`CSS选择器`中的`属性选择器`。每个标签中添加一个哈希值，设置样式的时候就是使用`属性选择器`选择即可，这样就实现了样式作用域

![[00 assets/612f61f3d69c41acf585e70d0015e058_MD5.png]]

我们为`style`添加`scoped`就可以实现样式作用域

```vue
//App.vue
<template>
	<h3></h3>
	<mian></mian>
</template>

<script>
import mian from "./component/main.vue"
export default {
  name: 'App',
  component:{
      main
  }
}

</script>

<!-- scoped设置样式作用域 -->
<style scoped>
    h3{
        background-color:red
    }
</style>
```

## 2.2 组件注册

**全局注册组件**需要在`main.js`中使用`createApp(App)`的返回值来注册

**局部注册组件**需要在`.vue`中`import`导入，然后使用`components`注册才可以在该组件中使用

![[00 assets/257bb0391bd2cdcb40efdc5f12371c4b_MD5.png]]

## 2.3 组件通信

### 2.3.1 基本介绍

`Vue`中经常出现组件数据的传递

![[00 assets/2809608b255d36ab956a55361525fac6_MD5.jpeg]]

### 2.3.2 props

#### 2.3.2.1 数组类型

下面就是使用`props`用父组件给子组件传值

![[00 assets/020bb7884ee49ce1dbb5d0c5db2304af_MD5.png]]

![[00 assets/a5798e0172f69e863c5910442f9a6e65_MD5.jpeg]]

#### 2.3.2.2 对象类型

> 基本使用

使用数组的形式只能接收数据，但是不能做类型的限制和初始化值

![[00 assets/78e28d1935e71d18a5a63c2e7184b42a_MD5.jpeg]]

> props 参数

`props`中的属性包含 3 个参数

![[00 assets/53876d4546fd159962e6dd14131ee2a5_MD5.png]]

关于`props`的命名问题，这里可以总结为只要是涉及在`HTML`命名的问题，都理解为下面的方式，因为`HTML`不区分大小写

![[00 assets/18fd684499cc4327dc1d83db9c398b41_MD5.png]]

> type 使用

`type`可以传递得参数有`String、Number、Boolean、Array、Object、Date、Function、Symbol`，下图中包含了`props`在日常开发中大多数得开发场景

![[00 assets/fa38c8b65c2a689e92c70a3edafccfe0_MD5.png]]

#### 2.3.2.3 非 props 的属性

![[00 assets/782bb997ae759e556396074a2bd64c6e_MD5.png]]

当然我们不想看到的话也可以直接关闭，添加`inheritAttrs`为`false`就可以了

![[00 assets/c7645bf485629c2fbca332728625a892_MD5.png]]

但是我们取消之后又想在该子组件的其他标签中添加呢？可以使用`$attrs 属性就可以手动添加上

![[00 assets/883506ffebcd6444b06c1168b526ec31_MD5.jpeg]]

![[00 assets/d1fc92eb7faa4a11b9f59ac701d632e3_MD5.png]]

### 2.3.3 emit

#### 2.3.3.1 基本使用

![[00 assets/c8e36cdf10b5f516b426a3b962055c56_MD5.png]]

因为`Vue`是组件化开发，所以有的时候会将`操作逻辑`分离到`子组件`中去。但是该操作需要可以影响到父组件中的数据，所以这个时候就需要用到`emit`

下图中将`+1`的操作都分离到了子组件，需要点击按钮影响到父组件中的`count`，实现响应式

![[00 assets/73d0d8630cd73fca8c3aaaa5bb76588c_MD5.png]]

下面就是整个`子给父`传递参数的整个流程

![[00 assets/28d05ffb4ef66479ece2b268d195a46d_MD5.jpeg]]

#### 2.3.3.2 事件验证

> 数组形式

![[00 assets/d9b669a1751ff91e2f238189d1039717_MD5.png]]

> 对象形式

当然假如我们需要做事件校验的话，就需要使用对象形式来编写

![[00 assets/de0d7f4978ebae77201a95206deca972_MD5.png]]

### 2.2.4 商品切换案例

下面为依赖关系图

![[00 assets/b069d0b7a09ba11da9872dc5d9a0d910_MD5.png]]

```vue
// ==== App.vue ==== //
<template>
  <div class="AppStyle">
    <ShopTarBarVue
      :ShopTarBarList="ShopTarBarList"
      @SwitchShopContent="SwitchShopContent"
    ></ShopTarBarVue>
    <ShopContentVue :CurrentShopContent="CurrentShopContent"></ShopContentVue>
  </div>
</template>

<script>
import ShopContentVue from "./components/ShopContent.vue";
import ShopTarBarVue from "./components/ShopTarBar.vue";

export default {
  name: "App",
  data() {
    return {
      ShopTarBarList: [
        {
          id: 1,
          name: "衣服",
        },
        {
          id: 2,
          name: "鞋子",
        },
        {
          id: 3,
          name: "裤子",
        },
      ],
      CurrentShopContent: {},
    };
  },
  methods: {
    SwitchShopContent(item) {
      this.CurrentShopContent = item;
    },
  },
  mounted() {
    this.CurrentShopContent = this.ShopTarBarList[0];
  },
  components: { ShopContentVue, ShopTarBarVue },
};
</script>

<style>
body {
  background-color: #eee;
}
.AppStyle {
  width: 300px;
  height: 200px;
  background-color: white;
}
</style>

// ==== ShopTarBar.vue ==== //
<template>
  <div class="ShopTarBarStyle">
    <div
      v-for="(item, index) of ShopTarBarList"
      :key="item.id"
      @click="ClickSwitchTarBar(item)"
      :class="{ ShopTarBarActice: index === currentIndex }"
    >
      {{ item.name }}
    </div>
  </div>
</template>

<script>
export default {
  name: "ShopTarBar",
  components: {},
  data() {
    return {
      currentIndex: 0,
    };
  },
  props: {
    ShopTarBarList: {
      type: Object,
      default: () => ({}),
    },
  },
  emits: ["SwitchShopContent"],
  methods: {
    ClickSwitchTarBar(item) {
      this.currentIndex = item.id - 1;
      this.$emit("SwitchShopContent", item);
    },
  },
};
</script>

<style scoped>
.ShopTarBarStyle {
  height: 40px;
  display: flex;
  justify-content: space-around;
  line-height: 40px;
  font-weight: 600;
}
.ShopTarBarActice {
  color: red;
  border-bottom: 3.5px solid red;
}
.ShopTarBarStyle > div {
  width: 20%;
  height: 100%;
  text-align: center;
}
</style>

// ==== ShopContent.vue ==== //
<template>
  <div class="ShopContent">{{ CurrentShopContent.name }}详细页面</div>
</template>

<script>
export default {
  name: "ShopContent",
  components: {},
  props: {
    CurrentShopContent: {
      type: Object,
      default: () => ({}),
    },
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
.ShopContent {
  padding: 10px;
}
</style>
```

下面实际的效果，点击上面的`tarbar`下面的内容发送变化

![[00 assets/1d3eeb051ca0a525ea3da3b890164f6d_MD5.png]]

### 2.2.5 Provide 和 Inject

#### 2.2.5.1 基本介绍

上面的`props`和`emit`是实现父子组件传递数据，但是使用`Provide和inject`是实现祖孙组件传递数据

![[00 assets/bb23c6a861241b972dc0d20aea062a86_MD5.png]]

#### 2.2.5.2 字符串写法

下面就是使用`字符串的写法`，但是这种方式不是很好，因为数据都是存储在`data`中，不能动态获取

![[00 assets/f3b01df624a70e004ad4d9c33e8d1db3_MD5.png]]

![[00 assets/9fd44209e4012656ba14ab3ff586587f_MD5.png]]

#### 2.2.5.3 函数写法

使用函数的写法就可以动态获取到`data`中的数据

![[00 assets/ae90c0181919960a16c928d800898c69_MD5.jpeg]]

![[00 assets/f7610fe3a933d9aaf48a38a675b59626_MD5.png]]

#### 2.2.5.4 实现响应式

我们在使用函数写法获取到该组件中`data`中的值，但是当我们修改了值，`inject`的值并不会改变，也就是不能实现响应式的处理

![[00 assets/c7abed605706edb8b1e10a9435fb066f_MD5.png]]

![[00 assets/edfa24efc2a58408936a50ddf35b6363_MD5.png]]

假如我们需要处理这种场景的话，可以使用`computed`来处理，但是一般都使用`pinia和vuex`来管理了，所以这个`API`使用的场景比较小

这里需要注意的一个点就是`provide()`中的`computed()`的`this`的处理，在`computed`中使用的箭头函数，但是可以寻找到`this`，这是因为箭头函数是根据作用域依次寻找的，它需要访问的是`provide`中的`this`，所以需要在这里写箭头函数来向上级作用域寻找

![[00 assets/81f6e5cceba54d7dcdbe77d2840a3d83_MD5.jpeg]]

![[00 assets/ee49c6ef78e118a0725e3068cee840ad_MD5.jpeg]]

因为`computed`返回值是`computedref`，可以理解为`ref`，这里的响应式原理就可以参考我的`JS高级`里面的内容。这样就可以实现响应式的原理

![[00 assets/7c8246a295de65cb5bfca06cac6ff9e1_MD5.png]]

### 2.2.6 全局事件总线

#### 2.2.6.1 基本介绍

我们使用全局事件总线的话，不仅仅可以父子组件通信，还可以祖孙组件通信，还可以非关系组件通信。也就是可以理解为可以**任意组件之间通信**

![[00 assets/6c665d743c148e8634b094411164fcd8_MD5.jpeg]]

#### 2.2.6.2 hy-event-store

下面是使用的`hy-event-store`来实现的事件总线，`npm官网介绍：`[hy-event-store - npm (npmjs.com)](https://www.npmjs.com/package/hy-event-store)

> 安装

```bash
npm i hy-event-store
```

> 配置事件总线

![[00 assets/b2e187f32fb962d517be8eba26840371_MD5.png]]

> 使用事件总线

1.导入`eventBus`

2.使用`eventBus`的`emit`来发送事件总线的数据

3.使用`on`来接收事件总线的数据

![[00 assets/54db226747f3fa2727561b209343d11f_MD5.jpeg]]

![[00 assets/1d1b8d83b775976207c671131faeb12a_MD5.jpeg]]

> 移除事件总线

当组件被销毁之后记得要移除事件总线的监听，因为移除需要获取到方法，所以这里的处理方式就时将方法写在`methods`选项中进行处理

![[00 assets/116a7586db4b04c8de9993200623f545_MD5.png]]

#### 2.2.6.3 mitt

参考文档：[(54 条消息) Vue3 笔记*mitt 库(事件总线)*英凛 zzZ 的博客-CSDN 博客\_mitt vue3](https://blog.csdn.net/qq_41196217/article/details/120695349?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~default-3-120695349-blog-124167423.pc_relevant_downloadblacklistv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~default-3-120695349-blog-124167423.pc_relevant_downloadblacklistv1&utm_relevant_index=4)

> 安装

```bash
npm install mitt
```

> 部署事件总线

![[00 assets/f5410fc91ffc3cf406da9a60d2905e26_MD5.jpeg]]

> 使用全局事件总线

本质和`hy-event-store`的库使用方式是一样的

![[00 assets/dac7c502f9a1e09b9eafca2bf75b984d_MD5.png]]

🎉：这里需要注意一个点，就是事件总线不能放到`setup`中使用

> 取消所有的事件总线

```
mittbus.all.clear()
```

## 2.3 插槽

### 2.3.1 基本介绍

![[00 assets/0e24cc98f6f0bebc27ac01c3a183a91e_MD5.png]]

### 2.3.2 基本使用

![[00 assets/30a984eb9b11aa386e3fb7ad51300b98_MD5.png]]

下面为基本的使用

![[00 assets/cd503cf3fae0ffb8bc5b7928d7943720_MD5.png]]

![[00 assets/a803b3115943dc88df6ce8edeaf12dbf_MD5.jpeg]]

### 2.3.3 插槽默认值

当你在不填写插槽的内容，但是想要它显示默认值。只要在`slot`中填写默认的`标签、组件`即可

![[00 assets/b11df699b4ddcacc492210c4d4dfd138_MD5.png]]

![[00 assets/b0eaa9d217746a8d9d32ea33abfea04e_MD5.jpeg]]

### 2.3.4 具名插槽

下面就是具名插槽得具体使用过程，其中`v-slot:`可以简写为`#`

下面得例子是作为一个搜索栏得处理方式，其中`center`得搜索内容就可以封装为一个组件填充到该模板中，然后`left`得图标就是放大镜图片，只需要传入固定得标签`img`即可，变化`img`得`url`

![[00 assets/f5407afe66bfdab28e7ff46b6fcca862_MD5.png]]

![[00 assets/2a3dbcae74c206fa55a3df2ac9e95279_MD5.jpeg]]

### 2.3.5 动态插槽名

当然我们也控制插槽的位置，下面就是使用`v-slot:[SlotName]`来动态设置里面的参数，从而动态渲染插槽的位置。其中`v-slot:`也可以简写为`#`，比如`#[SlotName]`

![[00 assets/aa1a369562781141bc10e293bc6cad5f_MD5.png]]

![[00 assets/cea24679e1f533b5a0b96ad39b2c5a14_MD5.png]]

### 2.3.6 渲染作用域

![[00 assets/b6aa3c143247759dc8c7f1f7c1ad0f1b_MD5.jpeg]]

也就是渲染的页面只能找本页面下面的数据，即便是通过**插槽**传给了子组件也不行

![[00 assets/f7ee6f9d771e32bcf8a863b57e2dd521_MD5.jpeg]]

### 2.3.7 作用域插槽

先说下为什么需要使用作用域插槽？比如说：`商品切换案例`，原本是使用`span`标签来显示的数据，假如在后续的组件中需要使用`button`来替换该标签在另外一个地方使用，这个时候数据是在子组件得，但是`button`是在父组件得，数据传输不是很方便，所以就需要子组件中的数据传输给该插槽中进行动态显示，这个时候就需要作用域插槽

![[00 assets/27f7f064009223062b5f57c6b5930559_MD5.png]]

> 默认插槽 + 作用域插槽

下面为基本的使用，将子组件渲染的数据传输给父组件渲染再来显示

![[00 assets/ed529f9d4b04d617d0b942f8a6c95a44_MD5.jpeg]]

![[00 assets/e9a3c331964cdf0a1dc8ca590ebf92d5_MD5.png]]

对于默认插槽不仅仅可以使用上图中的`#default="props"`还可以直接使用`#="props"`来编写

![[00 assets/9109f110c490615a320d53fd85400304_MD5.png]]

> 具名插槽 + 作用域插槽

因为默认插槽的值为`default`，所以上面的直接使用`default`就可以接收到。假如是具名插槽的话，使用方法就差不多

![[00 assets/cbe493e2c8668373a1b85b670d290548_MD5.jpeg]]

![[00 assets/b82db031ab6b77f96ef4ac1415a28ac7_MD5.png]]

## 2.4 生命周期

### 2.4.1 基本介绍

![[00 assets/0bde5564998a6f1689389c6c9c494620_MD5.png]]

### 2.4.2 生命周期流程

其中`created、mounted、unmounted`是比较重要的

![[00 assets/28a4d855851ba3ec764f4e3a7c375d39_MD5.jpeg]]

```vue
<template></template>

<script>
export default {
  name: "App",
  beforeCreate() {
    console.log("组件被实例化");
  },
  created() {
    // 1. 发送网络请求
    // 2. 监听eventbus事件
    // 3. 监听watch数据
    console.log("组件被创建成功");
  },

  beforeMount() {
    console.log("组件template准备被挂载");
  },
  mounted() {
    // 1. 获取DOM
    // 2. 使用DOM
    console.log("组件template已经被挂载");
  },
  beforeUpdate() {
    console.log("数据已经修改，准备更新DOM");
  },
  updated() {
    console.log("已经更新DOM");
  },
  beforeUnmount() {
    console.log("卸载之前");
  },
  unmounted() {
    console.log("已经被卸载完成");
  },
  data() {
    return {};
  },
  methods: {},
  mounted() {},
  components: {},
};
</script>

<style></style>
```

## 2.5 ref

### 2.5.1 获取普通元素

下面就是使用`ref`来获取`DOM元素`，但是一般的情况下基本不获取`DOM`

![[00 assets/84c0ffc9b31df68c270d0a0830c7d631_MD5.jpeg]]

### 2.5.2 获取组件

> 获取 ref 实例

我们使用`ref`也可以获取组件中实例

![[00 assets/97d12b063a5cce6f41f9f1fae207176f_MD5.png]]

> 调用组件中的方法

我们也可以使用获取到的`ref对象`来手动调用组件中的方法

![[00 assets/9cb580563a3a5ea42e8da6add5c31790_MD5.png]]

> 获取组件中的节点

使用下面的方式来获取组件中的节点

```vue
this.$refs.RefHome.$el
```

有可能该组件中存在一个节点和多个节点

![[00 assets/c5b5fb149c1ebc228514a4f4745abe01_MD5.png]]

> 获取父组件/根组件

```
this.$refs.RefHome.$parent  // 获取父组件
this.$refs.RefHome.$root 	// 获取根组件
```

## 2.6 动态组件

### 2.6.1 基本使用

比如说：点击按钮切换不同的组件。这个功能就可以使用动态组件来处理

![[00 assets/4e5f34f557604bb668e7714caa60d796_MD5.png]]

我们可以使用`component`标签来动态展示组件。其中`is`属性就是表示显示那个组件，里面填写的就是组件名，假如是全局注册的组件也是一样填写组件名即可

![[00 assets/325305b206c7250de50f58b5aa763e7f_MD5.jpeg]]

### 2.6.2 传递数据

对于动态组件，我们可以使用`emit和prop`进行父子传递数据

![[00 assets/b054e894cc706c69b7fc1d52a19190af_MD5.png]]

![[00 assets/bcd8d6df8398a66aaf12d34ee9b13760_MD5.png]]

## 2.7 keep-alive

### 2.7.1 基本使用

`keep-alive`可以让套在里面的组件被缓存起来，即便切换也会依旧存在。如下图中配合动态组件，那么动态组件都会被缓存，不会被清楚

![[00 assets/bc03968e7d227f509ef35c5459698f37_MD5.png]]

![[00 assets/8183b0cb99c8d76c2930976f70b6f336_MD5.png]]

### 2.7.2 相关属性

当然下面我们也可以规定只缓存那些组件，而不是所有组件都缓存，只需要在`include`中写组件名就表示该组件缓存，其他组件不缓存。这个组件名和组件中的`name`有关，而不是使用`component`注册的组件名

![[00 assets/39c22809fc2c8bd75d4dccf85aad33fc_MD5.jpeg]]

当然`keep-alive`还存在其他的属性，比如下面的`exclude`就是`include`的相反，还有`max`表示最多缓存个数

![[00 assets/c39fd11c75a305c14a2618f4a8573a46_MD5.png]]

### 2.7.3 生命周期

假如需要记录`keep-alive`的生命周期的话，不能使用上面常规的生命周期函数，而是使用专门提供的`activated`和`deactivated`函数表示显示和结束

![[00 assets/d88da1752276b7cf833b9b9eb32437cb_MD5.jpeg]]

![[00 assets/898cd5bf4157046d1d44f07c359686a3_MD5.jpeg]]

## 2.8 异步组件

### 2.8.1 分包文件

我们在打包之后，会发现最后会有 2 个包，第一个是`自己编写的包`，第二个是`第三方包`的，如:Vue.....。

假如是浏览器加载数据的时候，一次都请求过来再来渲染界面会很慢，所以就需要进行分包的处理

![[00 assets/943cf74d6c07d7ae68575745c100dddd_MD5.png]]

假如我们使用`import()`函数来导入的话，就会进行分包的处理，`import()`是一个异步函数

![[00 assets/92370094eb8339f8fa125d0137a3d68f_MD5.png]]

我们再来打包就会发现会多一个包，这个就是使用`import()`函数进行的分包处理

![[00 assets/64aa52e652cb9c7c74417c7a3453c9cf_MD5.png]]

### 2.8.2 分包组件

因为现在都会使用路由懒加载，所以这个用的不是很多

#### 2.8.2.1 函数写法

假如需要对组件进行分包的话和`分包文件`是一样处理，也是使用`import()`。还需要借助`Vue`提供的`definAsyncComponent`函数来创建异步组件

![[00 assets/01f64d9fb073adf2bf244e53d2d74e40_MD5.png]]

我们再来打包就会发现该组件已经被分出去了

![[00 assets/b2c1aa82c3b480d531daf1f1dcab4f76_MD5.jpeg]]

#### 2.8.2.2 对象写法

一般都是使用`函数写法`，对象写法不是经常使用。

![[00 assets/3c35d87b6dd3f7f15b244577ccbe5c50_MD5.png]]

## 2.9 组件的 v-model

**官方文档参考**：[组件事件 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/components/events.html#usage-with-v-model)

其实使用`v-model`的本质就是下面的`:modelValue`和`@update:model`的 2 个过程，分别是`props`和`emit`

![[00 assets/5e019c6e9b065c55801ba12d08e8108c_MD5.png]]

我们可以使用`v-model`的话就相当于上面的 2 步，在子组件中就可以直接控制父组件传入的数据

![[00 assets/ad20c610afc216ce28500c92f1b973f6_MD5.png]]

![[00 assets/eddd6fff347223f3d0ca3a2292a0972d_MD5.png]]

假如你没有编写`v-model`的名字的话，即：`v-model="num"`，那么就会需要使用`modelValue`在`props`中接收

## 2.10 mixin

### 2.10.1 基本介绍

![[00 assets/e9c8babd5c79295be0d63109cd3ff719_MD5.png]]

### 2.10.2 基本使用

我们可以使用`mixins`可以对组件中重复的选项进行抽离，比如下面就是对`About.vue和Home.vue`中相同的`data`和`created`进行抽离，这样就不需要多次书写

![[00 assets/589015493a82ecaadf4548d230227e39_MD5.png]]

### 2.10.3 合并规则

当然合并存在一定的规则，现在基本都不去使用了，因为一般都是`components API`

![[00 assets/788e9180a41f19a1d6fb815ccb9428c9_MD5.png]]

### 2.10.4 全局混入

我们可以在`main.js`中使用`createApp()`的返回值`app`的`mixin`对所有的组件都进行混入，这样下面的所有组件就不需要写`mixin选项`

![[00 assets/4532c4ce8074a37edbc93c2de87046ff_MD5.png]]

# 3. 脚手架 - CompositionAPI

## 3.1 基本介绍

![[00 assets/acc3b7aa3d899b785df2fce0ddce5b96_MD5.png]]

> 对比 Options API

![[00 assets/51c9976af207576d1a878540d97c3cc1_MD5.png]]

![[00 assets/d1c16c9f50eb1b5367d27bfe149dbf45_MD5.png]]

> setup 中不能使用 this

![[00 assets/54307d71b66d704de7059bc76104e1b2_MD5.jpeg]]

## 3.2 基本使用

这样我们就不用写`data、methods...`选项了

![[00 assets/18885c63157b18d8dfa8888917cb4887_MD5.jpeg]]

因为改成了函数式编程，所以我们可以将原本逻辑抽取出来直接使用即可，更加灵活

![[00 assets/972219bfafcd138f34d1fe8d421d9b36_MD5.jpeg]]

## 3.3 响应式函数

### 3.3.1 reactive 函数

整个`reactive函数`的响应式原理在我的`JS高级`中已经写过，假如想要理解底层的话可以去看下

![[00 assets/99cdc22dcb7bef27ef04b5594666b0b3_MD5.png]]

### 3.3.2 ref 函数

![[00 assets/0479b6d09619e63fe0ccfd04c8ca7882_MD5.png]]

### 3.3.3 基本使用

下面就可以总结为`ref`为`String、Number、Boolean`数据类型使用，`reactive`的话就是`Object、Array`使用，但是在实际的开发情况并不是这样，因为`ref`也可以使用`Object`

![[00 assets/c77fbeae5c6ad89ad762a1d7a94bf870_MD5.png]]

### 3.3.4 自动解包

我们使用`ref函数`在模板中使用就会自动解包，不需要你写`.value`。其中`reactive`的话也是一样的，可能`Vue`之前的版本的可能会存在`reactive`中的数据不解包的情况，但是截至`2022-11-4`之后的版本都没问题

![[00 assets/8e24b2c7654cc2c6482d717585c40709_MD5.jpeg]]

### 3.3.5 对比

在实际开发中一般都是使用`ref`比`reactive`多很多

> reactive 应用场景

1.本地定义的数据。因为本地定义得需要修改，所以使用`reactive`才可以。因为网络接口传输来得值就不需要进行修改，所以使用`ref`是最好得

![[00 assets/cc7389a1dd430aaf830fbbbd06f26af4_MD5.png]]

2.相互有关联的数据，比如：下面的`账号和密码`，因为它们一般是一体的，所以直接定义在`reactive`中获取是最好的，假如是`ref`的话就分离的太散了，不符合逻辑

![[00 assets/ed46acf2e7b342253cf76db0afdbec89_MD5.png]]

> ref 应用场景

1.定义简单数据

2.定义网络中获取到的数据，比如：下面的网络获取到了的`arr`数组，使用`reactive`的写法就需要一个个添加，但是使用`ref`的话，直接使用`.value`传入就可以了

![[00 assets/b73adc59b3b52d1717acafb729e8ba14_MD5.jpeg]]

## 3.4 单向数据流

### 3.4.1 基本使用

因为`vue`存在一个`单向数据流`得概念，比如说：使用`props`将数据传入给子组件，子组件修改`props`中的数据，这样会修改父组件中的数据，这样处理不是很好。当然`单向数据流`只是一个概念，你不遵守一样没问题，只是代码的维护性会很差

![[00 assets/9c3a5a19fefec2e57a7137b00a00abee_MD5.png]]

![[00 assets/0e4336018adeafd768a1e4a3bab79b51_MD5.png]]

假如真得要解决得话，就需要使用`props`传入，使用`emits`来修改

![[00 assets/f41e70277e4486f096b42ad102d5f40a_MD5.png]]

### 3.4.2 解决方法

`readonly`：让一个响应式数据变为只读的（深只读）。

`shallowReadonly`：让一个响应式数据变为只读的（浅只读）。

![[00 assets/c3b2a817a19168fb541f8f0c53d06659_MD5.jpeg]]

假如站在`3.4 单向数据流`的案例上，这个时候就可以使用`readonly/shallowReadonly`来限制处理。假如要修改得值得话使用`emit`修改原本得值即可

![[00 assets/5dea6a7f199046039306cb3bb98f06c2_MD5.jpeg]]

## 3.5 computed

![[00 assets/5f0f6a6ad1b638412121be827425e3d3_MD5.png]]

下面就是`computed`的基本使用方式，当然它还可以监视`ref`数据，本质和`OptionsAPI`是一样的，只不过单独抽出来为一个函数

![[00 assets/e7113c5c0bf4193acc1b736dc214d823_MD5.png]]

当然`computed`还有完整的写法，添加`set`的选择，只要修改了`fullnameAll`的话就会触发。其中`computed`的本质就是返回一个`ref()`，所以我们可以直接使用`fullnameAll.value`来修改里面的值，然后触发`set`

![[00 assets/2e29f7e2e4cf39362c902f0adbf2d5cf_MD5.png]]

这里是对于`computed`的总结：什么情况适合使用`computed`？只有在想要和数据和另外一个响应式数据有联系的话可以使用

## 3.6 ref

我们使用下面的方式来获取`ref`就可以了，其他的功能的`OptionsAPI`是一样的

![[00 assets/2e378a51489e1037ee55c01ad045aa2b_MD5.png]]

## 3.7 生命周期

![[00 assets/ddbe0e25c1c9d4acaacb96684c94ec30_MD5.png]]

一般是先注册`setup()`，然后`setup`中的生命周期比`setup`外面的`生命周期函数`优先级要低一级

![[00 assets/303719397cf8a0d71a0a98c0836ca537_MD5.png]]

## 3.8 侦听器

### 3.8.1 监视 ref

`watch`有 3 个参数，第一个是`监视的属性`；第二个是`回调函数`，`回调函数`里面的第一个参数是`变化后的值`，第二个是`变化前的值`；第三个参数就是`配置项`

![[00 assets/5b317b070ee0921abd004ff78276c387_MD5.png]]

![[00 assets/ca45b82d5d9ee1baabe0c6306724e144_MD5.png]]

### 3.8.2 监视 reactive

下面就是使用`watch`来监视`reactive`，对于监视`reactive`的话有很多的情况

```vue
<template>
  <div>
    姓名：{{ person.name }}<br />
    年龄：{{ person.age }}<br />
    job1：{{ person.work.job1.jobname }},{{ person.work.job1.salary }}<br />
    job2：{{ person.work.job2.jobname }},{{ person.work.job2.salary }}<br />
    <button type="button" @click="person.name += '!'">修改name</button><br />
    <button type="button" @click="person.age++">修改age</button><br />
    <button type="button" @click="person.work.job1.jobname += '!'">
      改jobname</button
    ><br />
    <button type="button" @click="person.work.job1.salary++">涨薪</button>
  </div>
</template>

<script>
import { reactive, watch } from "vue";
export default {
  name: "HelloWorld",
  setup() {
    let person = reactive({
      name: "张三",
      age: 18,
      work: {
        job1: { jobname: "工程师", salary: "10000" },
        job2: { jobname: "搬砖大哥", salary: "12000" },
      },
    });

    //情况一：使用reactive来监视对象里面得数据
    /*
		1.里面得回调函数只有newValue，没有oldValue
	*/
    watch(person, (newValue, oldValue) => {
      console.log("person得值改变了", newValue, oldValue);
    });

    //情况二：使用reactive来监视对象里面得对象
    /*
		1.里面得回调函数只有newValue，没有oldValue，其中oldValue不会求修改
		2.默认开启deep，你配置也无效
	*/
    // watch(person, (newValue, oldValue) => {
    //   console.log("person得值改变了", newValue, oldValue);
    // });

    //情况三：使用reactive来监视对象里面得某一个属性
    // watch(()=>person.name,(newValue,oldValue)=>{
    // 	console.log("person得值改变了",newValue,oldValue)
    // })

    //情况四：使用reactive来监视对象的对象中的某些属性
    // watch([()=>person.name,()=>person.age],(newValue,oldValue)=>{
    // 	console.log("person得值改变了",newValue,oldValue)
    // })

    //情况五：使用下面写法来监视对象里面得对象得值
    /*
		1.因为监视的是普通对象，所以deep不是默认开启的，如果需要侦听需要手动开启
	*/
    // watch(person.work,(newValue,oldValue)=>{
    // 	console.log("person得值改变了",newValue,oldValue)
    // }，{deep:true})

    return { person };
  },
};
</script>

<style></style>
```

### 3.8.3 watchEffect

我们使用`watchEffect函数`自动收集依赖，这个在`JS高级`中写过这个代码的实现，可以参考一下。里面`watchEffect`中出现了`Person.work.job1.jobname`的话，假如修改了该数据，就会自动调用该函数。并且该函数默认就会执行一次

![[00 assets/3da8b6eb854907dc9ca08cf1a579c9d9_MD5.png]]

![[00 assets/de634e7822ae5ee044f700703d00e0f4_MD5.jpeg]]

假如我们需要手动停止监听的话，就需要收集`watchEffect`的返回值，在回调函数内部调用即可

![[00 assets/2fff3d924af72d3b0f75c19ee1ada23a_MD5.png]]

### 3.8.4 监听 props

1、在一般的业务需求中，我们需要在 **父组件中进行网络请求，然后将数据传递给子组件** ，可以参考下图的代码

2、我们网络请求之后就会将数据给 `articleData` ，响应式数据更新，那么 `props` 更新，所以监听到对应的数据，我们就可以做对应的事情，可是结果并非如此

![[00 assets/4cf4aec606b7ceb1fe168fbac57d16e5_MD5.png]]

我们来看下为什么不是这样的，这里需要注意 2 个点

> watch 监听 props

1、我们可以查看官网的介绍，我们可以看到在 watch 一开始监听的时候是监听的 obj.count，它默认就是一个 number 类型，而非**响应式数据、getter...**，所以这里很好理解，因为外层是响应式对象，但是我们监听的知识对象中的值，所以监听无效

![[00 assets/e23ebfd107641d3c2bcf68af84f660d1_MD5.png]]

2、我们再来看上述代码出现的问题：我们一开始组件创建的时候网络请求还没到，所以这里就使用的默认值 `{ }`，使用 **props.content** 监听的默认值就是普通的 `{ }` 类型，而非响应式数据类型，所以我们监听不到，即便后续网络请求来了

![[00 assets/bf90dddfcf652348f64fa91b5fe86c1a_MD5.png]]

3、所以这里需要使用 getter 函数来封装一下才行，也就是下述的代码

![[00 assets/7d3098daec907f63fc2fd7f9ce87315d_MD5.png]]

> props 更新原则

1、第二点就是关于 props 的更新原则，其实就是**父组件更新，子组件就会将所有的 props 更新到最新的状态**，之前其实是没有理解到这一点的，我以为响应式数据传递进去就按照响应式数据状态来更新

![[00 assets/833941da5b2c7fc252bf1000ea25de33_MD5.png]]

2、如果是上述这样的话，我们就可以略微改造代码，来实现部分的性能优化

3、在下述的代码中，`articleTitle` 默认和 `articleData` 是同步一起更新的，因为响应式数据变化就会导致组件更新，所以我们只需要设置 `articleTitle` 的值，那么 `articleData` 就会作为 `props` 传递给子组件也会同步更新到最新的值，这样就节省了一个响应式数据

![[00 assets/9000bfad381c071b5f7c12425a88d8bd_MD5.png]]

## 3.9 函数式抽取

> useCounter

以前我们在`OptionsAPI`中使用`mixin`来对代码进行抽取，但是只是对选项中的混入。假如是`CompositionAPI`的话，我们可以直接将函数式代码抽取出来，放在一个单独的文件中进行处理

![[00 assets/e4ff6cec930b104d6c483d2ebf3354d5_MD5.jpeg]]

下面就是`useCounter`函数中的返回值，对代码的抽取处理

![[00 assets/534a27978f973bcacabb53cafae1587e_MD5.png]]

![[00 assets/27e925ff74ebee1b39f5db15e1688861_MD5.png]]

这个只是对`函数式编程`和`对象式编程`的思想的转变，现在`Vue`就是转变为`函数式编程`

> useTitle

点击下面的`一级按钮`和`二级按钮`对浏览器的标题进行切换

![[00 assets/949c63b2ca70ebb218f5e6d3fdd37f7e_MD5.png]]

下面的右边就是对函数逻辑的抽取

![[00 assets/88e5c53d6befd8d9f6dcfa8e9190c5aa_MD5.png]]

> useScrollPosition

监视浏览器的滚动条的位置

![[00 assets/d335bc8abdce2bd3eb7d94c96d847642_MD5.png]]

## 3.7 其他 API

### 3.7.1 shallowRef 与 shallowReactive

`shallowReactive`：只处理对象最外层属性的响应式（浅响应式）。

`shallowRef`：只处理基本数据类型的响应式，不进行对象的响应式处理。

![[00 assets/182c0d508e9b834797c1cab99c5c9f9d_MD5.jpeg]]

![[00 assets/bf42b76c45cf83c5b72173076220dd13_MD5.png]]

什么时候使用？

1.`shallowReactive`：如果有一个对象数据，结构比较深，但变化时只是外层属性变化

2.`shallowRef`：如果有一个对象数据，后续功能不会修改该对象中的属性，而是生新的对象来替换

### 3.7.2 toRaw 与 markRaw

`toRaw`：将一个由 reactive 生成的响应式对象转为普通对象。

`markRaw`：标记一个对象，使其永远不会再成为响应式对象。

![[00 assets/16dcb36192111c95d89bd5c17411107f_MD5.png]]

什么时候使用？

1.`toRaw`：用于读取响应式对象对应的普通对象，对这个普通对象的所有操作，不会引起页面更新。还有一个就是在`watch`中假如是监听得对象，那么返回得就是`Proxy对象`，使用`toRaw`处理会更好

2.`markRaw`：有些值不应被设置为响应式的，例如复杂的第三方类库等。当渲染具有不可变数据源的大列表时，跳过响应式转换可以提高性能。

`markRaw`的本质其实就是将给属性值加上`_v_skip`属性，这样的话就跳过响应式

![[00 assets/4b00bda281a50f8313c98f3b39dc7470_MD5.png]]

### 3.7.3 响应式数据的判断

`isRef`：检查一个值是否为一个 ref 对象

`isReactive`：检查一个对象是否是由 reactive 创建的响应式代理

`isReadonly`：检查一个对象是否是由 readonly 创建的只读代理

`isProxy`：检查一个对象是否是由 reactive 或者 readonly 方法创建的代理

### 3.7.4 toRef 和 toRefs

![[00 assets/8f81fd1c29464bd8585a85eba96efe5d_MD5.png]]

![[00 assets/046ca6152752d13312e39e9dba3737ca_MD5.png]]

因为在模板中书写`reactive`代理得对象一直书写`person.name、person.age`很不方便，所以就出现了`toRef`和`toRefs`。其中`toRefs`与`toRef`功能一致，但是`toRefs`可以批量创建多个`Ref对象`

![[00 assets/5b98f9f91aa51f3aa4e15317f2eb74fd_MD5.jpeg]]

深度解析：[toRef toRefs](分支-Vue/toRef%20toRefs.md)

### 3.7.5 ref 其他的 API

![[00 assets/ed4bd0c3d43d8262ffe4dc46d33c2e7f_MD5.jpeg]]

### 3.7.6 Provide 与 Inject

和`OptionsAPI`中的`provide和inject`功能基本是一样的，实现祖孙组件数据的传递。

这里这原本的`OptionsAPI`的区别就是，我们传入的是`ref`的数据，那么`inject注入`的话也会是`ref`的数据，也就是说会跟着一起响应式修改，不需要再额外写`computed`了

![[00 assets/a54f3fb7fa315286b8c9b31bbe265d02_MD5.png]]

![[00 assets/bd4abc59de28f8c8a963754590d47304_MD5.png]]

当然假如`provide`不提供数据的话，可以传入`inject()`第二个参数，这就作为默认值

![[00 assets/c70a9e3695545120c44b989515b06f45_MD5.png]]

# 4. 脚手架 - Setup

## 4.1 基本介绍

![[00 assets/d66aabe4c5288cdbeb666a70eb48efb0_MD5.png]]

## 4.2 基本使用

![[00 assets/6ee7e7b0f3c4926d3754eacdbf8a763e_MD5.png]]


## 4.3 props

1、现在使用`setup`语法糖需要使用`defineProps`来接收

![[00 assets/94a317c264d666b09db162a851f77a61_MD5.png]]

假如你不想限定类型得话，使用数组来接收也是可以得

![[00 assets/ce5cea38dfb6b2c64e16a1a5a7056af8_MD5.jpeg]]

2、我们来看下面的代码，可以看到如果我将 `ref` 包裹一个对象，那样也会默认使用 `reactive`

![[00 assets/bab0f2449cfb19648ffbf4de344ddcea_MD5.png]]

我们使用 `isReactive` 来检测一下就知道了，可以看到默认给转换为 `reactive`

![[00 assets/8b2e926e48970af56f839fa3b3b9f97a_MD5.png]]

3、针对 props，你可以知道一般都会传递 type 属性，之前其实没有理解为什么传递 Number，我以为是 ts 的类型，其实是 Number 构造器

![[00 assets/01e3691412b6969e0fd880e10d1dc65a_MD5.png]]

如果你已经编写了一个 props，需要给这个 props 自动推导类型就知道差别了，下述的 iconProps 就是要传递的对象，我们需要推导 iconProps 的类型

![[00 assets/c28e28121f1a92505e706cf7dac05edb_MD5.png]]

## 4.4 emits

需要使用`defineEmits`来提前注册`emits`事件

![[00 assets/b8f77bf8aa11601e36cdf4c2bdb2f601_MD5.png]]


## 4.5 ref

1、使用`defineExpose`来提前暴露想要暴露的数据，比如：直接使用`RefHome.value.showMessage()`来外部调用

![[00 assets/79805fb56996eee1d63d09618851266e_MD5.png]]

![[00 assets/2882eb443f9511396dd7b6cd61f9135f_MD5.png]]

2、如果我们使用 **ref** 来获取组件的 DOM 元素，如果想获取对应的 **offsetWidth、offsetTop...** 等数据，需要额外添加 **$el** 来获取

![[00 assets/a36ae75d6f883b279f9eca7bfc439fdf_MD5.png]]

# 5. 脚手架 - 高级语法

## 10.1 自定义指令

### 10.1.1 基本介绍

![[00 assets/d7127fd5ad498100cfe9bf050a2f8f00_MD5.png]]

目前存在一个需求就是，只要进入页面就自动对`input`获取焦点

![[00 assets/8879b5a686e157c27d0ad0aa6204e568_MD5.png]]

我们也可以抽取`Hook`来处理也可以，但是我们应对这种需求最好的方式就是使用`自定义指令`来处理

![[00 assets/54c995952cd708cc9908776270a7aac1_MD5.png]]

### 10.1.2 局部/全局指令

> 局部指令

1、在`OptionsAPI`中使用下面的方式来获取焦点，`focus`表示指令后续使用就是`v-focus`，只要该元素挂载就会执行里面的`mounted`函数，并且会传入`el`参数也就是该元素的`DOM`属性

![[00 assets/f1126ad2195e6519514993eb6618f625_MD5.png]]

2、如果在`setup语法糖`中使用的话就是按照下面的方式来处理，`vFocus函数`表示`v-focus`指令

![[00 assets/a960f4c92c6e464c6dc7edbdd23ffed9_MD5.png]]

> 全局指令

1、我们可以在`main.js`中单独执行`app.directive`，其语法和上面的`局部指令`是一样的

2、对于`全局指令`也可以抽取指令，可以参考下图中的编写方式来处理

![[00 assets/be92e49c2e936599fa342b448f4482dc_MD5.png]]

### 10.1.3 生命周期

![[00 assets/58efa75de2e0db7521c9fbc0ac08c67a_MD5.png]]

其本质的使用是按照下面的方式来处理，和上面组件的生命周期是一样的

![[00 assets/d934cc050a5773082826b4d764ba8b1f_MD5.png]]

### 10.1.4 指令参数/修饰符

![[00 assets/fefc2ca6bc46517aadcf40700c241d0d_MD5.jpeg]]

我们传入的`text`就是`arg`，`string、name`就表示的`modifiers`。并且因为是`JS`代码，所以里面还要写`''`来包裹起来，表示传入的是`Directive`字符串。如果你是传入的响应式数据的话，就不需要写`''`来包裹

![[00 assets/ad7b4bb4120d502306048c23ed2230a7_MD5.png]]

> 人民币转化

可能存在下面的案例，就是将数字转化为`人民币`符号，我们可以按照下面的方式来处理即可

![[00 assets/3d027cfcb1be533d0b0e9a03a9e488d2_MD5.png]]

![[00 assets/3a565edb884392ba3d83bfae0574a59e_MD5.png]]

> 时间格式化

![[00 assets/39c774916ced38775ee483d52a9bdcbb_MD5.png]]

## 10.2 teleport

> 基本介绍

![[00 assets/ee1c928dd36fe38ca1239eb6d5d1af88_MD5.png]]

> 基本使用

![[00 assets/3031dc8f113153b1e61f7d3bdd2dc583_MD5.png]]

> 组件使用

![[00 assets/5f38ac51dc1b8ce2512fd62d35b0a824_MD5.png]]

> 多个 teleport

![[00 assets/c0c817932db601b99c349a3ce878af1f_MD5.png]]

## 10.3 suspense

> 基本介绍

![[00 assets/6f72911f9bfa751c6d07b36d1d40f227_MD5.png]]

![[00 assets/54d9bddfa43f5ab85d948a5f86c6df53_MD5.png]]

## 10.4 vue 插件本质

![[00 assets/587dc05650adf62a448b3a93cc237d06_MD5.png]]

![[00 assets/a94f4c2059f38c2b75d3687f0308f369_MD5.png]]

1、我们使用插件其本质就是执行里面的`install`函数，并且传入`app`对象。或者传入函数，执行该函数

![[00 assets/ecfa7354e859d5b5adae035224d6c483_MD5.png]]

2、并且传入的`app`对象，会在内部执行全局组件、全局对象......，使得内部进行处理

![[00 assets/6297f867412db7670a6978bc774ce727_MD5.png]]

## 10.5 h 函数

### 10.5.1 基本介绍

![[00 assets/a7fae20440b3e5ead3e7c1837d394927_MD5.png]]

### 10.5.2 基本使用

![[00 assets/14d49fef05decbfffe74d9288080bfc4_MD5.png]]

1、我们不编写`template`标签，在`OptionsAPI`中编写`render`函数返回就可以生成`DOM`

2、`h函数`就是`createVNode函数`的另外一种写法

3、`h`函数第一个是标签，第二个是属性，第三个是内容，当然第三个也可以编写为数组，这样就可以凸显层级

![[00 assets/646aca275e704fc8868ed83d8c1d3a13_MD5.png]]

4、如果我们想使用`h函数`渲染组件的话，直接传入组件即可

![[00 assets/f476f0adf8f6c0172a44a7b4e6314b2f_MD5.png]]

### 10.5.3 计数器

1、我们可以使用模板语法来显示数字，因为`render`使用`bind`指向过`this`，所以我们可以直接使用`this.count`来获取到

2、对于绑定的事件可以在属性中编写，并且使用`onClick`作为属性名表示事件

![[00 assets/9308a5072a4e8946bd2222c6415d3916_MD5.png]]

### 10.5.4 组合式 API

> 基本使用

![[00 assets/ebc83159f84d8ac4b5c21ad472ff7328_MD5.png]]

> setup 语法糖

![[00 assets/8cdbedaa3bf4ccb7acc435559db9c256_MD5.png]]

## 10.6 JSX

1、我们这里使用`vite`环境来搭建

![[00 assets/baa32e6f0a8aaeddb1deb253b4baa5ff_MD5.png]]

2、首先我们需要安装`jsx`的`babel`的插件，`npm i @vitejs/plugin-vue-jsx -D`

3、在`vite`中的`plugin`中配置即可，对于`webpack`也是一样的

![[00 assets/b14bf5a7d6365c7a704f8e3c7191b936_MD5.png]]

4、下面实现了一个计数器的按钮，还实现了一个`map`遍历的案例，其基本你的代码和`React`是差不多的，对于`JSX`的语法直接查看`React`的笔记即可

5、其基本的规则在`h函数`中都介绍了，下面只写了 2 种编写方式，对于非`setup语法糖`的内容可以参考上面的

![[00 assets/838f34dd8ff3234c92fea26f20caa2e4_MD5.png]]

## 10.7 动画

### 10.7.1 基本介绍

![[00 assets/5512b091949ab6b251f666181174f49f_MD5.png]]

### 10.7.2 基本使用

1、其实`Vue`为动画所作的工作就是为下面的元素添加`v-enter-from`、`v-leave-to`......等类名，而不是`Vue`帮忙我们实现动画

![[00 assets/d63e429708d7043b20e17659ddb224cf_MD5.png]]

2、使用`Transition`对想要实现动画的标签进行包裹，在`css`中编写动画效果即可，达到一个阶段`Vue`就会自动添加上类名

![[00 assets/d72a82bf879078cbad1775e6d31c7f39_MD5.png]]

我们截图就可以看到`Vue`添加`class`的时机

![[00 assets/0e8d25d17a0dc2c0dd37bd49b1c04c57_MD5.png]]

3、`Vue动画`实现的效果

![[00 assets/8b8dbd780fca61e3897723245f516474_MD5.png]]

### 10.7.3 过渡动画 class

> 过渡动画 Class

![[00 assets/7db018d21cb995a1560d27af2b29da36_MD5.png]]

> Class 添加时机和命名规则

![[00 assets/267d4160dbc2b2ff5008742931d0162e_MD5.png]]

### 10.7.4 animation 动画

![[00 assets/f31a40bcbfebbe3501bafd9bf4b7ef60_MD5.png]]

1、下面是对`animation`动画的基本使用

2、如果我们使用这个形式的动画的话，`Vue`就会自动嗅探之后再来添加`text-enter-active`或者`text-leave-active`

3、如果我们写一个`50%`的话，就会导致动画运行到一半的时候卡一下，表示动画已经运行到`50%`。如果你不想卡这一下的话，直接写`0%`和`100%`就行了

![[00 assets/7e2e26cd1211f416e69994a8f8fd8579_MD5.png]]

### 10.7.5 动态组件切换

1、这个就是动态加载组件的操作，和前面的元素之间的切换始是一样的

![[00 assets/b9ed1670dda12a98d646f50ac00f1b93_MD5.jpeg]]

2、因为这里直接使用的`setup语法糖`，所以我们需要添加`:`将里面的代码变为`js代码`，将组件传入就可以动态加载组件了

![[00 assets/b9edeb9d0b9ef53c5ea55800bf0a61b2_MD5.png]]

### 10.7.6 动画属性

#### 10.7.9.1 appear 属性

![[00 assets/871a832f88ff204acb1c2d0c093886bf_MD5.png]]

#### 10.7.9.2 type 属性

1、首先我们需要知道`transition`和`animation`动画是可以叠加的，最后实现的效果是一样的

![[00 assets/f64fcbc6a1ec1ad336d7ea09aba5a68d_MD5.jpeg]]

2、首先`Vue`会自动监听元素动画的变化，自动选择时间最长的动画执行

3、但是对于自动选择我们可能不是很满意，需要自己手动来调整，这个时候就可以使用`type`属性来指定监听的类型。但是在实际项目中最好不要去这样处理

![[00 assets/c287a452b0dd98709216b3813d7e58ec_MD5.jpeg]]

#### 10.7.9.3 durations 属性

1、我们可以手动设置动画时长，也就是和上面的`type`一样，在实际项目中尽量减少使用的次数

![[00 assets/a1eba590644994a238fa2ac10b5bfaf4_MD5.png]]

#### 10.7.9.4 mode 属性

1、我们按照下面的方式来设置元素的显示和隐藏的话就存在问题，2 个元素同时存在，并且都在执行动画。

![[00 assets/f8800c084676db6b3a67e106cf4a9e29_MD5.png]]

![[00 assets/99a27712a7939b278be74b2e8033b3be_MD5.png]]

2、为了解决这个问题，就存在`mode属性`来处理这个问题

![[00 assets/1a46f2f979a3ee54cd3f2b6b2e26f905_MD5.png]]

我们使用`out-in`表示先执行`离开动画`，然后再来执行`进入动画`

![[00 assets/862f09393bc68c98b658062ff3ee4c49_MD5.png]]

### 10.7.7 列表动画

![[00 assets/d0428674e6c2c0aa349029a126fa47ef_MD5.gif]]

1、对于多个元素的动画添加可以使用`TransitionGroup`动画组，下面是官方中对`TransitionGroup`的介绍

![[00 assets/06ca0a1527e74048700310f4d6abc70f_MD5.png]]

2、下面中插入数据的话就会触发`.list-enter-from`.....动画，移出也是一样会触发动画，这里就过多的赘述

3、我们插入数据之后，需要将后排的数字向旁边移动。这个动画的实现我们使用`.list-move`来处理，里面添加动画的属性即可

4、但是移除数字会因为动画还没执行完，所以元素会一直占据在原位，移动动画即便执行了也不会移动，所以我们给移除的元素添加`position:absolute`属性，让它脱离文档流

5、对于打乱数组的方法，我们使用`underscore`库来处理。我们下载`npm i underscore`，使用`shuffle`函数来打乱数组

![[00 assets/02111f9ef029ea0717e90018d927e12d_MD5.png]]

6、下面是代码的示例

```vue
<template>
  <div class="List">
    <button @click="addNum">添加数字</button>
    <button @click="deleteNum">删除数字</button>
    <button @click="shuffleNum">打乱数字</button>

    <div class="content">
      <TransitionGroup name="list">
        <template v-for="item of nums" :key="item">
          <span>{{ item }}</span>
        </template>
      </TransitionGroup>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { shuffle } from "underscore";

const nums = ref([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

// 获取随机索引
const randomIndex = () => Math.floor(Math.random() * nums.value.length);

// 添加 / 删除 / 打乱数字
const addNum = () => nums.value.splice(randomIndex(), 0, nums.value.length);
const deleteNum = () => nums.value.splice(randomIndex(), 1);
const shuffleNum = () => (nums.value = shuffle(nums.value));
</script>

<style scoped>
.content span {
  font-size: 20px;
  margin-left: 20px;
  display: inline-block;
}
/* 添加动画 */
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease-in;
}
.list-leave-active {
  position: absolute;
}
.list-enter-to,
.list-leave-from {
  opacity: 1;
  transform: translateY(0px);
}
.list-move {
  transition: all 0.5s;
}
</style>

```

## 10.8 响应式原理

在`ES6-ES12`的笔记里面记录了手写响应式原理，可以参考

## 10.9 effectScope

[effectScope](分支-Vue/effectScope.md)


# 10. 前台项目 - 弘源旅途

## 9.1 前期准备

### 9.1.1 划分结构

我们先优先划分结构，一般是按照下面的结构来处理项目

![[00 assets/283952d210ace04302fb9980f982361d_MD5.png]]

### 9.1.2 代码提示

这个主要是为了给`vscode`的提示使用的，一般使用`vite`创建的项目可能没有这个文件，假如需要的话可以将这个文件添加进来

![[00 assets/6f95564e7eaea4fc514699ad51a3eddb_MD5.png]]

### 9.1.3 重置 CSS

一般我们会使用`normalize.css`来重置不同浏览器的样式问题，需要使用的话直接在`webpack`中打包即可

```bash
npm install --save normalize.css
```

当然我们不仅仅需要`normalize.css`，我们还需要添加`reset.css`来重置一些样式。还有`common.css`表示一些属性共有的样式。并且最后怕样式都在`main.js`中引入会导致浏览混乱，所以创建一个`index.css`来专门引入

![[00 assets/eceb3e921ea4c680765cc9c9e7dba4bc_MD5.png]]

### 9.1.4 路由配置

先来看项目，首先最重要的就是下面的`tarbar`页面。其中包含了 4 个主要页面，所以我们先来配置路由

![[00 assets/d274a98c4e538d4df45e06cd37f919fd_MD5.png]]

1.简单配置路由，因为这几个页面都是主要的页面，所以要优先创建

![[00 assets/772c125ff9a38f380b8303221df3075a_MD5.png]]

2.当然这里创建`Views`中的项目也是有讲究的，一般这种主要的视图都是创建一个文件夹表示。而且文件夹中的文件都是不一样的，存在下面的 2 种写法，有`home.vue`和`index.vue`的 2 种形式

![[00 assets/9467ce2ee48aa4bbe62796f232cbf135_MD5.png]]

### 9.1.5 状态管理

先进行基本的配置

![[00 assets/2a45c220a9bdeb3ce893171545f2ef20_MD5.png]]

对于其他组件中的状态管理可以放到`modules`中来处理

![[00 assets/c35d84ddbcae0058ce6c6755bbfefb9c_MD5.png]]

## 9.2 页面搭建

接口地址：[HYTrip (getpostman.com)](https://documenter.getpostman.com/view/12387168/UzXPxcSi)

### 9.2.1 \*tabbar - 手动封装/动态引入资源

> 手动封装

我们需要制作下面的`tabbar`页面，对其进行处理

![[00 assets/d274a98c4e538d4df45e06cd37f919fd_MD5.png]]

1.首先我们来搭建页面结构，这个页面结构的`CSS`非常的清晰，所以这里截图参考一下。

​ 1.1 首先是定位，这里使用了`fixed`定位，基于浏览器来定位的，只要`bottom`为`0px`的话就会默认在底部

​ 1.2 另一个就是图片和文字的垂直排列，这里使用的是`flex布局`，一个思路就是更改排列方向`flex-direction`

​ 1.3 对于图片来说，因为图片本身是长方形，所以这里直接设置宽度，不去设置高度，让浏览器来动态设置

![[00 assets/ce554bf9854a3ef0cd2b9a47e13de25a_MD5.png]]

当然对于颜色我们可以设置变量，其中`CSS`就存在变量的语法。这样`.Tabbar .TabbarItem.active`就会设置变量里面的颜色

![[00 assets/ac9f1d7d976297d913d2ba793d95f69a_MD5.png]]

2.因为对于`tabbar`来说数据都是固定的，所以这里将数据动态抽取到一个文件中处理，以后方便处理

![[00 assets/49cd18dc8255519bec227507c48dee7e_MD5.png]]

3.因为图片的地址是动态加载的，所以可能会加载不出来导致报错。在`webpack`中一般是使用`require()`处理，假如是`vite`的话可能需要编写一个函数来处理

![[00 assets/b6c0c25dddb726c30e7821f52ad81bbc_MD5.png]]

其中`new URL()`是动态拼接地址的，其中第一个参数是`相对路径`，第二个参数是`当前路径的URL`。最后对路径进行拼接处理来获取

![[00 assets/1c673fe17204c56691f595b1ec7b4ff0_MD5.png]]

4.因为后续会有很多获取本地图片的处理，所以这里将这个方法抽取到一个文件中，需要用的时候直接调取就可以

![[00 assets/6cb3c8f9a81436a68c388be6b084bb36_MD5.png]]

5.编写逻辑代码

![[00 assets/489678742697aa9de9f3b62031d50503_MD5.png]]

上面为整体的`tabbar`的设计思路，可以参考一下

```vue
<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

import { getImage } from "../../utils/load_assets";
import tabbarData from "../../assets/data/tabbar";

const router = useRouter();
const currentIndex = ref(1);
const tabbarSwitch = (id, path) => {
  currentIndex.value = id;
  router.push(path);
};
</script>

<template>
  <div class="TarBar">
    <template v-for="(item, index) of tabbarData" :key="item.id">
      <div
        class="TarBarItem"
        :class="{ active: currentIndex === item.id }"
        @click="tabbarSwitch(item.id, item.path)"
      >
        <img
          :src="
            getImage(currentIndex === item.id ? item.imageActive : item.image)
          "
        />
        <span class="text">{{ item.text }}</span>
      </div>
    </template>
  </div>
</template>

<style scoped>
.TarBar {
  position: fixed;
  bottom: 0px;
  left: 0px;
  right: 0px;
  display: flex;
  justify-content: space-around;
  height: 50px;
  border: 1px solid #f3f3f3;
}
.TarBar .TarBarItem {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.TarBar .TarBarItem.active {
  color: var(--primary-color);
}
.TarBar .TarBarItem img {
  width: 36px;
}
.TarBar .TarBarItem span {
  font-size: 12px;
  margin-top: 2px;
}
</style>
```

> vant 封装

但是最终使用的方案是是`vant`的处理，代码更少更简洁，而且很多功能都封装好了

![[00 assets/a6137dbd2e1548b04a5a27eeb1051739_MD5.png]]

但是这里存在一个小的问题，就是路由改变了，但是底部的`tabbar`并不会变，这是因为这是通过`currentIndex`来驱动的，只要`currentIndex`不改变的话就不响应

1、其中对于使用它原生的图标的话，可以添加上`route`来处理

![[00 assets/a265e3b450a8dd1bb953ab184fd8362a_MD5.png]]

2、但是我们这里使用的是自己定义的图标，并不会自动跳转。所以就需要按照下面的方式来监听处理

![[00 assets/975f5e3323c7832351ccd2c4c158204d_MD5.png]]

### 9.2.2 vant 引入

#### 9.2.2.1 按需引入

```bash
npm i vant   // 安装vant
```

对于这种项目直接全部引用的话，可能会导致包体积增大，所以这里采用的是按需引用的方式。

这里有一个坑就是关于官网的问题，对于`vant`来说网址比较多，所以建议直接查询和当前版本相同的官网。官网网址：[快速上手 - Vant 3 (gitee.io)](https://vant-contrib.gitee.io/vant/#/zh-CN/quickstart)，下面就是按需引入组件，但是需要下载相应的插件

![[00 assets/6a2e130476229e0e881e3b0d0894218d_MD5.png]]

我们按照上面的操作下载插件的话，就不需要自己来写按需引入的代码，直接写组件就可以了，`vite`会自动添加组件

![[00 assets/bc30afc14b08085c4624d7292f47dc90_MD5.png]]

#### 9.2.2.2 vant 替换

我们这里直接使用`vant组件`来替换以前的`tabbar`代码，是不是就简洁很多，直接使用即可。

![[00 assets/59e718790d4e4f552761eaef2df1916f_MD5.png]]

#### 9.2.2.3 样式修改

1.因为这里使用的插槽，并且写的是自己的元素，所以这里可以直接修改

![[00 assets/814f53e0d475b0fe6cd4ff3315145526_MD5.png]]

2.使用`CSS变量`属性，下面的是在全局中进行修改，在官方文档中就有介绍

![[00 assets/01a3496c0459a1f86ba5311399be3624_MD5.png]]

假如我们不想全局修改的话，就需要写在对应的类中

![[00 assets/f9c3f48b2b0be63f1a1efa0974946e22_MD5.png]]

当然可以根据浏览器的控制台中的属性来修改

![[00 assets/84c69518e2855c2ee5eab96864da737f_MD5.png]]

3.直接根据控制台找到它的类并修改，但是这种方式不一定生效，因为存在样式作用域

![[00 assets/e442e75efd1ea757553adbe61aece267_MD5.png]]

首先`tab-bar`是作为一个单独的文件来处理，其中`van-tabbar-item`也是作为一个单独的文件来处理，因为存在样式的作用域所以根本不生效

![[00 assets/9f00d88f4996677f38ac11606dd860ea_MD5.png]]

这里存在 2 个方法来处理，其中第一个就是删除`style`中的`scoped`，但是不是很推荐；另一个方式就是使用**样式穿透**，这样就可以修改子组件中的样式

![[00 assets/b48e032c703220ee610b291c8749ae5e_MD5.png]]

### 9.2.3 city 开发

大致开发成这个样子

![[00 assets/65d6938567897f8267d1387784660e99_MD5.jpeg]]

#### 9.2.3.1 获取地址

对于浏览器原生来说可以直接获取到地址，但是误差很大。假如真的要在网页中做位置获取的操作，建议使用百度`API`来调用

![[00 assets/7b7b9127796bb874132a19be6acc3c1e_MD5.png]]

这个获取地址在`谷歌`中是获取不到的，但是在`edge`是可以获取到的。其实是因为它们之间实现的原理不一样，对于`谷歌`来说，是将你网络的`IP地址`上传到它的服务器，然后来返回地址的，但是对于`edge`来说，是获取你电脑当前的定位来处理的

下面是是`W3C`的中对于`geolocation`接口的介绍（[Geolocation API (w3.org)](https://www.w3.org/TR/geolocation/)），其中`geolocation`是实现的一个高等级的接口，所以`W3C`在定义这个接口的时候只是定义了这个接口，但是不关心这个接口是怎么实现的，所以就出现了相同的代码中`edge`是获取的到定位的，但是在`谷歌`中就获取不到的情况，这个就是因为接口都是一个接口，但是实现的原理不同

![[00 assets/c93e40317cabb8d7b7019f8f5dbce698_MD5.png]]

#### 9.2.3.2 隐藏 Tabbar

因为一些界面不需要显示`tabbar`，所以这里需要对一些界面进行特殊的处理

![[00 assets/2fa5f5ad3ea9941f5f42a6265457f05d_MD5.jpeg]]

> 1.

我们可以在要隐藏的路由中设置`meta`信息，这样我们使用`useRoute()`可以直接获取到，假如不设置`meta`的`hideTabbar`的话就默认是`undefined`为`false`，所以这里我们设置的`hideTabbar`为`true`

![[00 assets/d88249d5e8c8886a5a47fe90eb72a84f_MD5.png]]

这里需要注意`useRouter`和`useRoute`的区别，我们使用`useRoute`获取到当前的路由地址

![[00 assets/4ebb9b46f051ea61768146d11b9e16c7_MD5.png]]

> 2.

或者使用`CSS`的方式来隐藏，其原理就是将让设置的盒子盖在原本的`tabbar`上面就可以了

![[00 assets/de14ee8cee547f7cccdf77405da910f9_MD5.png]]

#### 9.2.3.3 搜索栏和 tab 栏

![[00 assets/7355301a14f6d5beb6a1248133353145_MD5.jpeg]]

下面就是开发`搜索栏`和`tab`栏，这里就是使用的`vant`来开发的

![[00 assets/16994e6aa2a00bd56fa42ecc7205cb7f_MD5.png]]

#### 9.2.3.4 网络请求

下面就是对`网络请求`的基本封装，我们一般是单独设置一个文件夹专门封装`axios`，其中`config.js`是填写配置

![[00 assets/7801e8f14fd152fa3d3875749c4ab071_MD5.png]]

当然对于其他的网络请求的`接口`，也是单独放置在`modules文件夹`中，来统一接口。为了方便请求，所以我们也会单独设置一个`index.js`来导入所有的接口，这样我们在其他文件导入接口的时候只需要关心接口名就可以了

![[00 assets/ad2cc81fef511f0c9db42e5ef016f941_MD5.png]]

#### 9.2.3.5 数据封装

我们对于网络请求来的数据一般都是直接使用`pinia`的`actions`来处理的，这样让数据更加统一

![[00 assets/56cf3575e2d684a6c6aa9ff2c2b75cad_MD5.png]]

#### 9.2.3.6 搜索栏和 tab 栏定位

因为搜索栏和 tab 栏下面是信息流页面，所以上面需要固定。实现这个效果有 2 个方法

![[00 assets/6d5910b31e8d9c85d1281d49f5d7ad63_MD5.png]]

> 1

我们这里使用`fixed`定位的方式来处理，其中一个就是需要将内容手动的往下调整，比如：`margin-top:98px`

![[00 assets/1ef88662cdc3f34a93f0ba1d4e71245d_MD5.png]]

还有一个就是滚动条的处理了，你会发现这个滚动条会对整个页面进行滚动，处在搜索栏的位置

![[00 assets/62ab29ed625ff6ffb07b7c78e48d99e8_MD5.png]]

> 2

还有一个方式就是使用下面的方式来处理

![[00 assets/35170120d9397f4cedd86add21f641b1_MD5.png]]

就不会存在上面出现的问题

![[00 assets/eb14301931eb388ffce4eadb9953826a_MD5.jpeg]]

#### 9.2.3.7 citygroup 动态数据

1.首先第一个难点就是关于`van-tabs`中数据切换时，使用的是索引值，所以我们很难选中对象中的值，所以这里我们使用`vant`提供给`van-tab`的属性值`name`来处理

![[00 assets/107f84b11fc22250b1256dac4c282de6_MD5.png]]

其中`citylist`是对象值，其格式大概是这种格式

![[00 assets/27e2b7e9c57d6644fa0e98218a2cfc22_MD5.png]]

我们将对对象遍历的`key`传输给`van-tab`的`name`就可以了

![[00 assets/3442d9501503fdb5006d2e0637aa086f_MD5.png]]

2.我们实现了切换之后获取到对象的`key`值，还有一个问题就是我们取出的数据不是响应式的，因为`cityList.value[tabActive.value]`本质就是对象的取值，并不是`Proxy`，所以这里会丢失响应式。

这里的解决方法就是使用`computed`，或者在`模板语法`中使用也可以

![[00 assets/1b92a3ba38e4b7e08af41b45793724f0_MD5.png]]

#### 9.2.3.8 citygroup 数据展示

这里直接使用的`vant`中提供的`indexbar`来处理

![[00 assets/94d55378b3a93da16481c4fe3d28049b_MD5.jpeg]]

下面就是展示的过程，这里做了一个优化，因为一开始是将所有的列表数据都传输进去了，所以切换的时候渲染速度很慢，所以我们一开始就将所有数据都展示处理，通过`v-show`来控制显示和隐藏，这样切换的话会流畅很多

![[00 assets/66fd8d68371de72ab830385be6f53bbe_MD5.png]]

#### 9.2.3.9 热门城市展示

![[00 assets/6767f5dc867f7fd3c0f8100529b92203_MD5.jpeg]]

下面为热门城市的`CSS`，这个主要是考验的`CSS`的编写

![[00 assets/4a2717093813ea693ec6987c7bd41890_MD5.png]]

#### 9.2.3.10 索引栏问题处理

因为这里多加了一个`热门`，所以索引栏无法正确定位到数据

![[00 assets/21fa91356d536368d9f99fcbd386be1b_MD5.jpeg]]

所以我们这里需要使用到`index-list`属性来重新定义一个动态的`索引栏`

![[00 assets/3a97dd179214bf696c80e4b5e8c4fc44_MD5.jpeg]]

我们这里使用`computed`来处理这里动态展示数据的要求。这里的索引主要是依靠`van-index-anchor`来处理，不是按照里面的`index`来对应，而是个数来处理

![[00 assets/41c32139538e053a5b7e79388095a30d_MD5.png]]

#### 9.2.3.11 选择城市回退

当你选择了城市之后回退到首页

![[00 assets/5eb3dfaca96d73b51cd025e5ab9c69ef_MD5.png]]

因为`currentCityInfo`的数据在后面的每个页面都可能使用，所以我们这里将数据存储到`pinia`中

![[00 assets/007c972cc35d50a5a97e8d50095af31c_MD5.png]]

#### 9.2.3.12 热门建议处理

我们需要实现下面的功能

![[00 assets/59e28a26b4b06f0c244375fd114b63b6_MD5.png]]

这里面对于网络请求的部分，我就不展示了。这里主要是`CSS`样式的问题，我们使用下面的`overflow-x`可以自动展示一个`x轴`滚动条

![[00 assets/126e8b74d8ddedb77b114f71f590d263_MD5.jpeg]]

### 9.2.4 box 开发

#### 9.2.4.1 动态显示时间

我们这里直接使用`dayjs`来处理时间，对于当前时间加一天的操作可以参考`nowDate.setDate(nowDate.getDate) + 1`就可以了，或者使用`getTime()`来获取时间戳再加上`24 * 60 * 60 * 1000`处理

![[00 assets/4775eefab3f208fbc531107dc882b32b_MD5.jpeg]]

#### 9.2.4.2 使用 van-calendar

我们可以`vant组件`中的`calendar`来处理，下面就是配置的信息

![[00 assets/91611af678407a55faa32a510234e1d5_MD5.png]]

#### 9.2.4.3 计算时间之差

我们使用`dayjs`来处理时间之差

![[00 assets/97c50e4ed9a594ea2ab5a73da00350b7_MD5.jpeg]]

#### 9.2.4.4 热门建议

这里我们将网络请求和状态管理封装到`service`和`store`中

![[00 assets/58e07c9604c1a55968b1e13c89c0658e_MD5.png]]

#### 9.2.4.5 搜索按钮处理

点击之后跳转页面，并且将数据通过路由传输过去，这个其实很简单。但是对于`views`文件夹，这里有一个创建规则，只要你新建了一个页面，那么这里就要多创建一个文件夹

![[00 assets/05e1807aa8f0ab1b0cca258bcea71e2b_MD5.png]]

#### 9.2.4.6 房间首页请求

我们使用下面的方式来对房间中的数据进行请求

![[00 assets/3096174daefc473139ebb67c4768efe4_MD5.png]]

#### 9.2.4.7 房间首页展示

实现下面得 2 种房间首页得装饰，其中`9`表示左边得全局，`3`表示右边得一半

![[00 assets/3de903865dec1cae69ad64dc6f9ea027_MD5.png]]

下面是`3`表示得`HTML结构`布局

![[00 assets/599ca0675826a419639944abc18499e1_MD5.png]]

因为存在超过盒子得宽度就显示`...`得功能，可以使用下面得方式来处理

![[00 assets/b81fd37e92281240532545cdd151d436_MD5.jpeg]]

还有一个显示评分得功能，因为整个评级只需要传输进去值，因为我们这里使用得是组件，所以需要使用到`组件v-model`

![[00 assets/3ed8ff7a96ec74fcf1d5c4e93ba6033b_MD5.jpeg]]

假如为了节省性能得话可以是下面得方式来设置评级处理得分数，这里可以参考我得`组件v-model`得笔记，默认是`props`和`emit`得处理，其中``props`默认传入得值就是`modelValue`，这样就只实现了单向绑定，节省了开销

![[00 assets/0db7913d0134bc304c51374a8cc669af_MD5.png]]

#### 9.2.4.8 滚动条 hook 抽取

下面就是整个`hook`得抽取，这个是完整版得。可以通过传递`参数elRef`得形式来决定是否为`window`或者`elRef`。

最后是通过返回一个参数`isReachBottom`得方式来判断是否到达底部，这是一个很重要得思想，其中你想实现得逻辑通过`hook`外部得文件来处理，这个封装`hooks`只是一个监听得作用，不承担其他职责，所以返回一个值处理逻辑

![[00 assets/23679164a3fd22a3c0a8f889bbc54d53_MD5.png]]

当你获取到返回得`isReachBottom`的值，对其进行监听处理，只要发生改变就发送请求

![[00 assets/9725ce493df298633b0cd899b0c487d1_MD5.png]]

因为监听的情况很频繁，所以我们可以使用`throttle`来处理

![[00 assets/11a870786525b388c3e11b85ebd3cac7_MD5.png]]

下面是整个`hook`抽取的逻辑，以后需要的话可以复用

```javascript
import { onMounted, onUnmounted, ref } from "vue";
import { throttle } from "underscore";

const useScroll = (elRef) => {
  let el = window;

  let isReachBottom = ref(false);

  let scrollTop = ref(0);
  let scrollHeight = ref(0);
  let clientTop = ref(0);

  const elListenerScroll = throttle(() => {
    if (el === window) {
      scrollTop.value = document.documentElement.scrollTop;
      scrollHeight.value = document.documentElement.scrollHeight;
      clientTop.value = document.documentElement.clientHeight;
    } else {
      scrollTop.value = el.scrollTop;
      scrollHeight.value = el.scrollHeight;
      clientTop.value = el.clientHeight;
    }

    if (scrollTop.value + clientTop.value + 2 >= scrollHeight.value) {
      isReachBottom.value = true;
    }
  }, 200);

  onMounted(() => {
    if (elRef) el = elRef.value;
    el.addEventListener("scroll", elListenerScroll);
  });
  onUnmounted(() => {
    el.removeEventListener("scroll", elListenerScroll);
  });

  return {
    isReachBottom,
    scrollTop,
    scrollHeight,
    clientTop,
  };
};

export default useScroll;
```

#### 9.2.4.9 搜索栏时间处理

以前我们的时间处理的数据都存在`.vue`文件中，但是这种全局的事件最好存在一个共享库中`mainStore`来处理

![[00 assets/9c9b8ff70c649f5a49cb0b6053932047_MD5.png]]

这样搜索栏也可以自动的更新来显示数据

![[00 assets/242bc515bd9c186f09744c8369a989fa_MD5.png]]

### 9.2.5 Loading 开发

#### 9.2.5.1 组件封装

1、首先作为一个`Loading`组件肯定需要重新封装作为一个组件来使用的

![[00 assets/f0b52bb325bf028111e233335e6f2972_MD5.png]]

2、我们对于样式的处理，这里存在一个小技巧就是`position`为`fixed`，并且`left、right、top、bottom`要都为`0`，这样的话就会同时占用全部页面，而不需要设置`width:100%......`属性

![[00 assets/8c9a22676ad559a178798cdbd2763e6b_MD5.jpeg]]

#### 9.2.5.2 状态控制

1、作为一个`laoding`的页面，其状态的控制和其他的所有页面都有关系，所以其状态控制最好时定义一个全局的变量`store`中，前面我们定义了一个`mainStore`来存储全局控制的变量。我们现在依旧在这里定义

![[00 assets/5a4dcf5c3a7d64df01f695e485107709_MD5.png]]

2、因为这一类的状态控制都是网络请求的，所以这个状态控制编写的最优解就是编写在网络拦截器中，只要请求发出的话，就显示`Loading`，如果响应结果的话就关闭`Loading`

![[00 assets/e22c7eabb020d3d4a97e170176aa3965_MD5.jpeg]]

![[00 assets/a9fa81c4bcfb20a249416f2380ef1107_MD5.jpeg]]

### 9.2.6 房间详情页

#### 9.2.6.1 基本搭建

1、我们在首页点击了房间的信息，就需要跳转到房间的详情页

![[00 assets/6498c7010f525125463134df718e9a24_MD5.jpeg]]

2、首先我们先搭建页面，这里取名为`detail`

![[00 assets/9fa8623fe287159c9e8c4ddda250e3c5_MD5.jpeg]]

然后就需要配置路由，并且需要传入`id`的参数

![[00 assets/e45ecf579b4511ea2b967f0b5bb26834_MD5.png]]

3、其中房间的`Item`要进行事件绑定，并且我们直接在组件中编写`@click`其本质是传入给`homeItemV9`的根标签进行处理了，所以这个组件存在 2 个根标签就需要做其他处理了

![[00 assets/094f6773bf428ddbed1fc69e477b49f1_MD5.png]]

跳转之后，进行路由参数解析即可

![[00 assets/c762e8af786dee3a97337dba93e82f71_MD5.png]]

#### 9.2.6.2 导航栏搭建

![[00 assets/f835560243b21c4563e1c986d313f8e9_MD5.png]]

使用`vant`组件库中的导航栏，并且我们可以使用`--van....`来调节该组件的颜色，这里的修改可以参考我`9.2.2 vant引入`的处理

![[00 assets/a500b7a476053e3b57355ad9133f8ac4_MD5.png]]

#### 9.2.6.3 网络请求

房间详情页的整体都使用组件中管理数据，而非使用`pinia`来处理，如果需要查看使用方式可以参考之前的笔记

![[00 assets/f56a48213e77221f1425928924a05c2b_MD5.png]]

#### 9.2.6.4 轮播图

![[00 assets/eadbf9c5f882de9cb638f7a5cee32594_MD5.jpeg]]

1、房间详情页使用`props`传递参数给`Swiper`

2、其中`mainPart`是网络请求过来的，所以存在一开始加载组件的时候为空的情况。所以一种处理方式就是使用`mainPort?.topModule?.housePicture....`这样会出现很多的`?`，这样很麻烦。所以我们使用`v-if`先判断是否内部有值，如果有的话就加载，非则就不加载

![[00 assets/f451f49e190e1b747a1eb5581a74291a_MD5.jpeg]]

3、`vant`组件库可以插槽来自定义轮播图的提示器。`#indicator`表示具名插槽的名字，`props`表示其子组件传来的数据`props`，里面有当前的页数和总页数

![[00 assets/a64da641d0e0d74dc74176fcf03a7758_MD5.png]]

4、按照下面的方式对数据先进行转换，这里提供的是一个思路，根据`enumPictureCategory`来生成数据

![[00 assets/bbfeaeea6a595e1bf690bd139134a3d7_MD5.png]]

这一段就是核心算法。

`swiperGroup`是存储分组之后的结果，遍历原本的数组`swiperData`取出每个数组的`enumPictureCategory`的数据作为对象`key`，如果没有该`key`的话就会返回`undefined`，也就是不存在`"02"`这个对象`key`。

所以需要创建该对象`key`并且该对象`key`为一个数组，里面都是同类数据。创建了对象`key`之后就往对象`key`为`"02"`中填充数据

其核心思路就是是否存在`key`，如果不存在就创建，然后填充数据

![[00 assets/583df5bba0c1288fb46f8f1db4363343_MD5.png]]

5、对于一开始的数据存在一些非法字符，所以我们需要替换处理，我们这里使用的`replace`来处理

![[00 assets/0fe3f38375f0c7c07a211685c4360ee3_MD5.png]]

最后的效果是这样的

![[00 assets/3902e67e48923d3747eb9ef4a093bfae_MD5.jpeg]]

6、下面就是实现得效果，不仅显示这个房间得总页数，而且还有样式得变化

![[00 assets/ae674f59b490cbf404d9c194a89ac26b_MD5.png]]

我们使用`swiperData`的`enumPictureCategory`和遍历`swiperGroup`的`key`比较，只要为`true`的话就显示白块。但是我们并不知道当前显示的数据索引

![[00 assets/274afdd7cea65b7f955cf115d9ea5c28_MD5.png]]

所以我们将当前显示轮播图的数据全部传输给`getSwiperGroup`方法，来遍历`swiperGroup`处理出索引即可

![[00 assets/a5ea070af72242ae8c2b6a5add43a91c_MD5.png]]

#### 9.2.6.5 信息栏

![[00 assets/d727306875e9a1aef6c8d9271c5c3076_MD5.jpeg]]

1、我们为组件传入参数`topInfos`

![[00 assets/612702fbc9b0063be4a9803ea1f7b0fd_MD5.png]]

2、我们来搭建页面结构，并且编写样式

![[00 assets/f706057952dd58eefc3e9d96a226d1f7_MD5.jpeg]]

#### 9.2.6.6 详情封装

![[00 assets/89c6f4c4ba569eeb520561f56b718a83_MD5.png]]

1、因为这里有很多这样的样式，所以我们这里封装为一个组件。并且这里使用一个插槽来处理插入组件信息

![[00 assets/5e4e5b4d45fe5be644ba6eb23a1e7673_MD5.png]]

这样我们直接将数据填入`slot`中，就可以在设置同一个模板来处理

![[00 assets/9347d9612d1f17857ceea6ad46204556_MD5.png]]

2、假如我们这样封装的话，就节省了很多的成本直接插入信息即可

![[00 assets/cdd818030589c2b1d76a13f396ecea76_MD5.png]]

其结构是相同的

![[00 assets/a188ee6036370f53fca8ea2c18bea135_MD5.png]]

3、剩下的都是按照上面的方式来封装，这里不做介绍了

![[00 assets/6269cdde8bf0905ebe74ad1e56fa667d_MD5.png]]

#### 9.2.6.7 百度地图集成

![[00 assets/c709a0b4a4e511dfe66b2abe3c23ca40_MD5.png]]

1、首先需要在`百度开发者中心`申请账号，并且需要创建一个应用才能使用。其中`referer白名单`填写`*`

![[00 assets/6e62b87e055cde61aa4fde6230bcf6aa_MD5.png]]

2、其基本的使用还是查看文档来处理。你需要使用`ref`来获取元素`DOM`，然后使用`baidu`的`webgl`来渲染地图

![[00 assets/0c6000417ff209aaea947e33caf923ad_MD5.png]]

3、记住要在`index.html`中添加下面的`script`，这样全局才会有`baidu的webgl`，并且后面填写你创建应用的`密钥(AP)`

![[00 assets/c6a9d30d33605d66831fdb093a5119be_MD5.png]]

我们在`web`中引入，可以将`api`改为`getscript`，这样就不会报错了

![[00 assets/e000384a0c9a900b5782d0fb894482f6_MD5.png]]

#### 9.2.6.8 tabControl

![[00 assets/29a5825a69698eeeb1373fe23a01b4e4_MD5.png]]

1、我们这里依旧使用之前封装好的`useScroll`，并且最好使用`ref`来获取`DOM`元素

![[00 assets/9b295277c0527c3a61fffac555807646_MD5.jpeg]]

2、这里一定要注意一个细节，就是关于滚动。必须要传入给`useScroll`的元素溢出之后才能被监听到滚动，也就是滚动条是传入的元素的，否则就需要监听父元素的`id=app`的，很显然我们监视不到

![[00 assets/2a45413f6afd409ce546def6aca1e4cf_MD5.png]]

所以需要设置元素的`height`为`100vh`，并且`overflow-y`为`auto`，所以就会导致该元素溢出

![[00 assets/b16fb16d2874014604e0cb09203c1df4_MD5.png]]

3、`tabControl`需要使用`emit`来传递参数给父组件。其基本的使用可以参考前面的`emit`的笔记

![[00 assets/c8c77c2ff0570b6c467ab14747d97499_MD5.png]]

![[00 assets/335936a181705fdf342a62b2f768bece_MD5.png]]

4、因为`tabControl`的名字需要是动态的，我们只需要编写参数就可以自动控制`tabControl`的名字

![[00 assets/25227c9c0677579333b502e30640505f_MD5.png]]

​ 4.1 首先就需要获取组件的名称。一个常规的方式就是使用`ref()`参数来处理，但是需要编写很多`ref变量`。这个方式不是很好，所以这里使用函数的方式来处理，只要组件加载就会执行这个函数并且传入参数

![[00 assets/a2da8b325942852b67186f8246400175_MD5.png]]

这里需要一个性能优化，使用`v-memo`来处理，只要`mainPart`变化就会重新更新组件，不然只要页面变化就会自动更新并且重复执行`getSelectRef`函数

![[00 assets/d2fe58065a3f0c90ae170df79af84622_MD5.png]]

​

​ 4.2 我们使用`{ "详情" : DOM信息 }`的对象形式来处理存储，我们编写`getSelectRef`来获取`DOM`元素并且存储到对象`selectEl`中

​ 4.3 对于`getSelectRef`下面需要编写`if(!value) return;`来处理，因为我们返回的时候`mainPart`会变化，所以这个时候就会执行这个函数，我们需要编写这个判断来结束函数

​ 4.5 获取`value`参数，并且判断是否存在一样的`对象key`，如果不存在就添加，如果存在就不管。这个时候对应的`对象name`和`对象key`都存入到`selectEl`映射中

![[00 assets/564f189062e3a27de28e75c97b0ecd74_MD5.png]]

​ 4.6 我们使用`Object.keys`来获取`selectEl`的所有`key`，这样就动态绑定了`tabControl`的`name`

![[00 assets/39d2f00eb993b46e8a892f32707c5277_MD5.jpeg]]

5、我们前面将`selectEl`的`DOM`信息存储，获取其元素的`offsetTop`，使用父元素的`DOM`的`scrollTo`跳转即可

![[00 assets/fafe069ea10300bc8ef296497c631cde_MD5.png]]

#### 9.2.6.9 tabControl 索引

想要页面滚动到特定位置显示对应的标题

![[00 assets/77ba9af9b09630957c1593bd7d85fa2b_MD5.png]]

其本质的逻辑参考下面的

![[00 assets/0509eee7198732a86aef955ddc4036db_MD5.jpeg]]

1、下面时候整套`索引匹配算法`的全貌，其本质就是将`位置信息`和`索引`挂钩，只要每次位置信息变化就会遍历位置信息，只要比`newValue`大的即可，就是目前的索引位置

![[00 assets/e47423cb38e63d83325e35fa92d46a41_MD5.png]]

2、算法这里有一个问题，我一开始使用的`index = -1`，但是最后可能存在最后一个获取不到的问题，因为我们都是`index = i - 1`，所以极限就是`4`

![[00 assets/d86a90c8e8d5a00c72a2a555a34057ba_MD5.png]]

所以这里解决的最简单的方法就是一开始默认赋值位`values.length - 1`即可，这样就解决了最后一个获取不到的问题了

![[00 assets/92378e4b0cb8c2876041082d0de59b02_MD5.png]]

3、对于下面的获取子组件`tabControl`的`ref`，然后调用里面的方法。对于`Vue3.2`的`setup`的语法，需要使用`defineExpose`将子元素中的东西暴露出来，才能被调用

![[00 assets/c838410ce0047ad2b5dc42a97103b4e4_MD5.png]]

4、下面是解决`tabs`的跳动`bug`的处理。只要点击之后就会将代码调整为点击模式`isClick`改为`true`

![[00 assets/a6034da059917d6618ea3e95ac3491ac_MD5.png]]

如果跳转到点之后，这个时候`currentDistance`就和`newValue`是一样的，所以就接触点击模式，将`isClick`改为`false`。但是这里存在一个`bug`，如果跳转的时候滚动页面，就不会精准落到点里面，所以`isClick`就一直为`true`，所以我们在跳转的时候可以静止用户滑动

![[00 assets/4da825e9577455682e956944cd3d5367_MD5.jpeg]]

## 9.3 细节优化

### 9.3.1 keep-alive

1、我们在首页中进行网络请求，当我们点击了下面的`tabbar`之后就会清除缓存，就会重新加载首页，很显然这样的方式很消耗网络性能，最好的方式就是缓存起来

![[00 assets/41bc1d94eec638b9df444a41d4b54783_MD5.png]]

2、存在这 2 种处理方式，以前都是使用的下面的方式来处理，现在最好使用上面的方式来处理

![[00 assets/861a158fb1923fd20c256e199c7ae77f_MD5.png]]

​ 2.1 在使用这 2 个方式之前的处理是要为`.vue`组件添加`name`属性，之前因为是`OptionsAPI`，所以直接写`name`属性即可，但是现在使用的是`setup`语法糖，不存在使用`name属性`，所以按照下面文章的配置即可

[(121 条消息) Vue3 使用 vite-plugin-vue-setup-extend 不生效问题-CSDN 博客](https://blog.csdn.net/ruisenLi/article/details/124385175)

​ 2.2 这里使用的是`include`而非`includes`，在一些版本里面是可以使用`includes`不会报错，这里官方的写法就是`include`

### 9.3.2 首页网络请求问题

![[00 assets/af38a9d1eeb7634e06a2ebd987fe29a6_MD5.png]]

1、我们写网络请求的时候，就是只要页面滚动到底部就发送请求，但是我们没传入参数，所以就是监听的`window`，所以我们只要切换页面的话就会触底，导致发送网络请求

![[00 assets/9c2f4fa7e9104eda08a7b04a2cefaaeb_MD5.jpeg]]

2、所以我们传入`homeref`即可，只监听自己的`滚动`即可

![[00 assets/4cf9d56e32eb2311458184d726cc9944_MD5.png]]

### 9.3.3 保留首页记录

1、我们想要`tabbar`页面跳转之后，在`home页面`也能保持之前浏览的位置

2、这里使用`onActived`，只要页面显示就执行，因为本身就记录了`scrollTop`的记录，所以这里直接跳转过去即可

![[00 assets/b4e92e8b5107469487d533ff9903a016_MD5.png]]

### 9.3.4 禁止用户缩放

因为是移动端的项目，所以可以缩放会导致页面很奇怪，所以我们需要禁止用户缩放

![[00 assets/2fa99d8086268072d4e539fe5c924dcf_MD5.jpeg]]

### 9.3.5 单位转换

```bash
npm install postcss-px-to-viewport --save-dev	// 安装
```

可以参考`Vant`中的文档介绍配置，或者直接去官网来编写

![[00 assets/5a176f5f92b44759215a27e0fc33f501_MD5.png]]

这样所有的`px`都转化为`vw`，在`github`中存在配置信息，使用时查看

![[00 assets/efdbb771e1cbd3955a76588f581836ce_MD5.png]]

# 11. 后台项目 - 后台管理

## 11.1 前期介绍

### 11.1.1 基本介绍

> 技术介绍

![[00 assets/67fe132bcb727d98cc7794d33d9118b6_MD5.png]]

> 创建项目

![[00 assets/e3ed0d24c50d6c4f78e8b3785650dc9d_MD5.png]]

这次得项目按照下面得方式来编写

![[00 assets/54b6a4e5f6b5868a18371e08963780a7_MD5.png]]

### 11.1.2 文件介绍

其他基本文件介绍参考我之前得笔记

![[00 assets/7dc5e0207e52caf1e722a5c11a00ff99_MD5.jpeg]]

> extensions.json

1、生成得文件中存在`extensions.json`文件，只要开启该项目`vscode`就会自动推荐使用下面得插件

![[00 assets/51b5921e625b513f54cdffa164fe9881_MD5.png]]

> vite.config.ts

2、这里是`vite.config.ts`得文件，如果是`.ts`得话就又更好得语法提示，并且该文件是接替`vue.config.js`得作用，我们想要写`webpack`得配置都可以在这里面编写

![[00 assets/f4a1ebf0317754f3902637222b5dab58_MD5.png]]

3、这里需要注意一个小细节，下面得`vite.config.ts`都是打包得时候使用得，而`tsconfig.json`中是在代码提示得时候使用得，并不是一类东西。比如下面得`@`路径得表示

![[00 assets/c8d1cb1479439e01010e8d033586e353_MD5.jpeg]]

> tsconfig.json

4、下面就是`tsconfig.json`得配置信息，这个文件时为`ts`做配置信息得，为什么这里得配置信息这么少，这是因为前面得`extends`配置，他将其他得配置文件都隐藏到`node_modules`中了

![[00 assets/255eee9020a76ae1bb366b87df7bb1b2_MD5.png]]

我们根据地址位置就可以找到信息了。这个就是作为一个被暴露出来得主要得配置文件

![[00 assets/32335eb2f2ed7d67f7a3bd6f2892c472_MD5.jpeg]]

5、当然我们还要一些其他得配置文件，这个文件主要是配置`vite.config.*......`等文件。目前猜测得是这个文件是开发者可以修改得文件，而`tsconfig.json`是不能修改得文件，并且该文件作为`tsconfig.node.json`文件是作为`SSR`优化时得文件

6、`types:node`表示上面得这些文件可能需要跑在`node环境`中进行处理。

7、`composite:true`表示可以合成进去，因为`tsconfig.node.json`是通过`tsconfig.json`中得`references`导进去得，所以需要添加`composite:true`表示可以合成进去

![[00 assets/49e0bfb75f3e625e19c6e640260bcb98_MD5.png]]

> env.d.ts

6、该文件是引入`类型声明`得，我们点击`vite/client`就跳转至`类型声明`文件中

![[00 assets/86bb18896411bc1b05df5b4b674bf87f_MD5.png]]

就可以看到`Vue`帮忙声明了很多得类型，这样我们就不需要自己手动来编写了

![[00 assets/8cd8bbd770a2f3c37ed1c0637822315d_MD5.png]]

7、我们查看了上面得`env.d.ts`文件，可以发现没有`.vue`文件得声明，但是我们导入得`Vue`文件没有报错

![[00 assets/7d9718fc74931bbfc4bb349d798be8e4_MD5.png]]

下面就是`Vue`编写`ts`代码的另一个方式，也就是函数参数编写类型，这样传入参数的时候就会有代码提示，并且可以看到最后导出组件的时候是`DefineComponent`，所以下面我们自己声明的模块就需要导出`DefineComponent`

![[00 assets/a35ccd926f558795bea7a55e641c434f_MD5.jpeg]]

可能是内部做了配置，但是这个配置做得并不是很好，所以我们可以自己做一个`类型声明`最后到处得是`component`而非`any`

![[00 assets/f4e210893e7fcc2644db7fe85350aa8b_MD5.png]]

8、假如说不想配置上面的信息的话，可以按照`Volar`，它会自动帮忙导入`.vue`文件

![[00 assets/48ecfc8f74910a4eea534891d3871f82_MD5.png]]

### 11.1.3 项目配置

![[00 assets/f25aba58a0203fc3e443a4474c36221a_MD5.png]]

#### 11.1.3.1 图标/标题

![[00 assets/acad7121458801d8f122bc415c9af279_MD5.jpeg]]

#### 11.1.3.2 代码规范

> .editorconfig

1、这个文件的主要目的就是为了统一`IDE`的配置。比如：各个`IDE`中的字符编码不一样，所以为了统一就需要编写``来保持编码风格

![[00 assets/6638ae71f6d82d18eab342f3229d69b6_MD5.png]]

```bash
# http://editorconfig.org

root = true

[*] # 表示所有文件适用
charset = utf-8 # 设置文件字符集为 utf-8
indent_style = space # 缩进风格（tab | space）
indent_size = 2 # 缩进大小
end_of_line = lf # 控制换行类型(lf | cr | crlf)
trim_trailing_whitespace = true # 去除行尾的任意空白字符
insert_final_newline = true # 始终在文件末尾插入一个新行

[*.md] # 表示仅 md 文件适用以下规则
max_line_length = off
trim_trailing_whitespace = false
```

如果想要使用的话还需要安装`EditorConfig for VS Code`插件

![[00 assets/310b0115524bb21b4b34ebdd87feccad_MD5.png]]

> prettier

Prettier 是一款强大的代码格式化工具，支持 JavaScript、TypeScript、CSS、SCSS、Less、JSX、Angular、Vue、GraphQL、JSON、Markdown 等语言，基本上前端能用到的文件格式它都可以搞定，是当下最流行的代码格式化工具。

1、安装`prettier`

```shell
npm install prettier -D
```

2、配置`.prettierrc`文件：

```json
{
  "useTabs": false,				// 使用tab缩进还是空格缩进，选择false；
  "tabWidth": 2,				// tab是空格的情况下，是几个空格，选择2个；
  "printWidth": 80,				// 当行字符的长度，推荐80，也有人喜欢100或者120；
  "singleQuote": true,			// 使用单引号还是双引号，选择true，使用单引号；
  "trailingComma": "none",		// 在多行输入的尾逗号是否添加，设置为 none，比如对象类型的最后一个									属性后面是否加一个，；
  "semi": false					// 语句末尾是否要加分号，默认值true，选择false表示不加；
}
```

3、创建.prettierignore 忽略文件（可选），也就是配置不使用`pretter`的文件

```
/dist/*
.local
.output.js
/node_modules/**

**/*.svg
**/*.sh

/public/*
```

4、`VSCode`需要安装`prettier`的插件

![[00 assets/643dece29789ed982cd6f9ea600e0425_MD5.jpeg]]

5、并且对`VSCode`进行配置，按照下面的方式改为`Prettier`即可

![[00 assets/c225bf4e29e134c340a5b4b52f58ded1_MD5.png]]

并且开启`format on save`就可以实现保存文件就格式化稳定

![[00 assets/ff1209ff137ab9071467d84c5b31a4c6_MD5.png]]

\*上面的配置基本是使用`ctrl + s`就格式化代码，但是现在可以`alt + shift + F`格式化代码，所以上面的配置看自己是否愿意配置

> eslint

1.在前面创建项目的时候，我们就选择了 ESLint，所以 Vue 会默认帮助我们配置需要的 ESLint 环境。

2.VSCode 需要安装 ESLint 插件：

![[00 assets/3dadbde0b44e65cd381c286f963299d4_MD5.jpeg]]

3.解决 eslint 和 prettier 冲突的问题：

安装插件：（vue 在创建项目时，如果选择 prettier，那么这两个插件会自动安装）

```shell
npm install eslint eslint-plugin-prettier eslint-config-prettier -D
```

添加`.eslintrc.cjs`文件，然在再添加 prettier 插件：

```json
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/typescript/recommended",
    "@vue/prettier",
    "@vue/prettier/@typescript-eslint",
    'plugin:prettier/recommended'		// 添加这个选项
  ],
```

4.如果想要`eslint`不去监测那个错误

![[00 assets/9b8137d5c3ac02d7af33c0f3116a36ed_MD5.png]]

可以在`.eslintrc.cjs`中的`rules`配置该错误，并且属性值设置为`off`

![[00 assets/851b22797e34c44d2e7c1f6ce641403f_MD5.png]]

5.VSCode 中 eslint 的配置

```json
"eslint.lintTask.enable": true,
"eslint.alwaysShowStatus": true,
"eslint.validate": [
  "javascript",
  "javascriptreact",
  "typescript",
  "typescriptreact"
],
"editor.codeActionsOnSave": {
  "source.fixAll.eslint": true
},
```

## 11.2 前期准备

### 11.2.1 目录结构划分

![[00 assets/743124a41ce789f468e8794c21558a36_MD5.png]]

### 11.2.2 样式重置

参考`9.1.3`的内容

### 11.2.3 路由配置

我们按照下面的模式来配置路由

![[00 assets/7834d34547d9f0700c3851a0cea09dd4_MD5.png]]

### 11.2.4 状态管理

1、我们按照下面的方式来编写`pinia`的模式

![[00 assets/c5425ad84c56c1fd3160bdc9f57d3428_MD5.png]]

2、使用也和之前是一样的

![[00 assets/161d4ac0749c774851a841760a7a9375_MD5.png]]

### 11.2.5 网络请求

使用我之前封装好的`ts`网络请求即可

![[00 assets/5bcf1655438344208d1984322b6d077b_MD5.png]]

![[00 assets/130ea0842ab193ee60b6be1ccd7829b5_MD5.png]]

### 11.2.6 生产/开发环境

1、我们在日常的开发中需要区分`生产/开发环境`，可能存在一些配置文件需要修改，但是每次都是手动修改的话会导致出现配置错误的情况，所以我们可以使用`vite`中的`import.meta.env.xxx`的参数来处理

![[00 assets/4acef3eabef78fb61a86845568dcc145_MD5.jpeg]]

2、如果你使用`npm run build`打包之后，想要看到打包之后在服务器的效果，可以使用`npm run preview`指令来运行已经打包好的网页

3、可以看到下面的服务器地址也会跟着你的环境变化而变化

![[00 assets/1f044bf2d71d99f55e18c92f3f4b9068_MD5.png]]

4、对于环境变量存在还存在下面的配置信息，我们新建文件来区分，这个方式是配置信息较多时处理

![[00 assets/119df2cd98d29b253ff1ad9e3b5434fb_MD5.png]]

编辑文件为`.env.xxx`开头，后面添加`mode`，写上`.local`表示`git`时忽略该文件，在`gitignore`中有明确忽略的语法，这样也可以实现区分`开发/生产环境`

![[00 assets/6e057bba43aeee38e2fca1edc9cb1f27_MD5.jpeg]]

### 11.2.7 组件库引入

> 全局引入

直接参考文档来操作即可

![[00 assets/eb5ed2829aad3326ce1b5e62868c1329_MD5.jpeg]]

如果需要按照写的组件中的属性有提示的话，可以按照下面的方式引入

![[00 assets/fe4c0a3180ef23ec80025f5729f6e3bf_MD5.png]]

> 按需引入

1、剩下的安装过程参考文档即可，但是我们安装完之后会发现并没有代码提示，但是会给我们生产 2 个文件

![[00 assets/7a0eb1fb5b42bdfe1425898730d2cf07_MD5.png]]

![[00 assets/1e5eee00a5e7c665f0d68b98bb419af8_MD5.png]]

2、如果想要代码提示的话，将该文件配置在`tsconfig.json`中即可

![[00 assets/8a8e12d98d23b9b5871b72390be749f6_MD5.png]]

![[00 assets/cac1019e4593ec6234f67e4ae0b1dcd5_MD5.png]]

> 样式覆盖

查看按钮就可以知道，`elementui`是支持`CSS变量`的，但是文档中并未说明，实际上我们是可以使用的

![[00 assets/c8fd485a6d2362658df55d1bf5d5e4e8_MD5.png]]

### 11.2.8 宽高铺满

1、我们想要页面都铺满存在 2 种方式，第一个就是在`index.html`中修改属性，很显然这种方式不被推荐

2、第二种方式就是按照下面的方式来处理，使用`vw、vh`的方式来铺满整个视口即可

![[00 assets/c39140c13feb864fc1d41f36e0ac7f85_MD5.png]]

## 11.3 页面搭建

### 11.3.1 登录面板

#### 11.3.1.1 页面搭建

![[00 assets/7940bb49add5610e4b9518fa0881471a_MD5.png]]

1、使用`elementplus`中的组件即可，这里的样式直接参考老师的代码即可

![[00 assets/be80689c0faea10b7c6c58c83d12adf8_MD5.jpeg]]

2、因为我们在`app`中设置了`width、height`的宽度和高度为`100vw、100vh`，所以我们作为其子元素可以直接设置为`100%`就行

3、对于`flex`布局，因为`.login`占据了整个屏幕，所以我们设置`flex`居中就可以实现其子元素的居中效果

![[00 assets/edcd57cc1bdfcde34b155e78b4cbca0f_MD5.jpeg]]

4、需要搭建`tabs`页面，我们按照下面的思路来编写

![[00 assets/a4ef3546ac641c21e8e21537b6885ec2_MD5.png]]

​ 4.1 我们使用`label`具名插槽将标签插入到`tabs`中，并且切换之后的内容通过组件来显示

​ 4.2 我们使用`actionTabName`来作为变量来存储，使用`name`来区分不同的`tabs`

![[00 assets/0f6483d6f3121338be063e88cb30ced0_MD5.jpeg]]

​ 4.3 我们将表单的输入框都写入组件中

![[00 assets/0a1518a1ce5909ac46ad0ab9016344ae_MD5.png]]

#### 11.3.1.2 \*图标引入

![[00 assets/6de30bf6f30c42a14300fcbc10d7be90_MD5.png]]

1、文档中有一段是关于自动引入图标，但是这个只是引入`iconify`，并不能自动引入`elementui`的图标

![[00 assets/6d37be399c05307a0ebbb61e02356ef1_MD5.png]]

2、所以这里选择全局引入图标，并且采取插件的形式的来编写。

3、`app.use()`传入函数，第一个参数就是`app`，同时执行该函数，这样就全局注册了图标，这样就不需要在`main.ts`中编写过多的引入代码

![[00 assets/5b4b8bd1e874d7a5610c8d3453dbeb8d_MD5.png]]

#### 11.3.1.3 校验规则

1、我们按照下面的方式来编写校验规则，这里需要注意`:model`的写法，而非`v-model`，不然会导致检验错误

2、`required`表示必选，`trigger`表示触发条件，`pattern`表示校验规则。这个可以写多套，因为一开始没输入内容的时候是一套校验规则，但是输入之后又是一套校验规则，所以这里使用数组

![[00 assets/85886941e89f32a4a17b0fd7c4569e3d_MD5.jpeg]]

#### 11.3.1.4 登录操作

1、因为这里存在 2 个种登录方式，所以每种登录都会存在不同，我们就将登录的逻辑写在`panel`的子组件中，其中`panel`组件表示`tabs`

2、使用`ref()`获取组件元素，其中`validate`内部存在回调函数，只要内部校验不通过`valid`就是`false`，通过就为`true`

![[00 assets/3193b87e696aa46c737859b6506676f8_MD5.png]]

3、在父组件中使用`ref()`来获取去子组件，这样就可以调用里面的方法了。

![[00 assets/f99cc49b7dce2288c2f53a07d74561e5_MD5.png]]

#### 11.3.1.5 \*获取组件类型

可以使用`<InstanceType<typeof panelAccount>>`来获取组件的实例的类型

![[00 assets/f99cc49b7dce2288c2f53a07d74561e5_MD5.png]]

#### 11.3.1.5 Message 显示 - 自动导入

1、我们点击登录之后应该会弹出消息框，但是并没有弹出，这是因为没有添加样式

![[00 assets/f157e3e1af6ac1c54d8772ba0365fb5b_MD5.png]]

2、其中一个方法就是全局添加一个样式，这样就不需要手动导入了，但是这种方式显然不是很好。或者选择手动导包，这样我们还需要自己去找，也不是很好

![[00 assets/c07cce651a4003ce3004ed6e678d53ce_MD5.png]]

3、我们可以使用插件的形式来引入，也就是前面的自动引入

```bash
npm i vite-plugin-style-import -D	// 安装
```

在`vite.config.js`中编写插件的配置

![[00 assets/66acdb2349e2a7de24b11aec694422a8_MD5.png]]

#### 11.3.1.6 登录逻辑

1、获取用户信息 -> 发送网络请求 -> 存储数据。按照这套流程来编写即可

2、在组件中获取到的信息传输到`pinia`中的 actions 中，然后进行网络请求的处理将数据存储到`pinia`中

![[00 assets/3a546b210f061204d30aa133493a85cc_MD5.png]]

3、因为这里多次出现`{ name , password }`的对象，所以最好的方式是设置单独的类型

![[00 assets/1156c4ad3e6728e8a44303bf6c56c6b2_MD5.png]]

#### 11.3.1.7 \*缓存封装

1、我们按照下面的形式进行封装，结构比较简单这里就不做解释了

```typescript
enum cacheEnum {
  Local = "local",
  Session = "session"
}

class cache {
  storage: Storage;

  constructor(storageType: cacheEnum) {
    this.storage = storageType === cacheEnum.Local ? localStorage : sessionStorage;
  }

  setCache(key: string, value: any) {
    if (value) {
      this.storage.setItem(key, JSON.stringify(value));
    }
  }
  getCache(key: string) {
    const value = this.storage.getItem(key);
    if (value) {
      return JSON.parse(value);
    }
  }
  deleteCache(key: string) {
    this.storage.removeItem(key);
  }
  clearCache() {
    this.storage.clear();
  }
}

const localCache = new cache(cacheEnum.Local);
const sessionCache = new cache(cacheEnum.Session);

export { localCache, sessionCache };
```

2、这里使用也是和原本的`localStorage`是一样的，只是多做了一套封装，这样就可以定制更多的功能

3、可能存在一些单词拼写错误，所以一般会写一个常量来进行引入使用，比如下面的`LOGIN_TOKEN`

![[00 assets/e380a6c8579b17a16c7f855e7f3ef6c6_MD5.png]]

#### 11.3.1.8 路由守卫

1、默认进入网页的时候是`/`，会重定向进入到`/main`。我们这里需要判断是否登录，如果没有登录就进入`login`，登录的话就进入`/main`

2、如果我们登录之后又输入`/login`的话，肯定是不允许再登录，所以就需要定向到`/main`中

![[00 assets/eb9b432d8633991f5c0911cf37a9475f_MD5.png]]

3、退出登录的时候删掉`token`再跳转到`/login`中

![[00 assets/2a7b63ac28a410f06f47ce4e427315ed_MD5.png]]

#### 11.3.1.9 记住密码

1、也就是记住`记住密码`的状态，只要为`true`的话就将账户和密码存入`localStorage`。如果为`false`的话就删掉存储的账户和密码

![[00 assets/f6b17d645309ceb9d03ca7b136d1a80f_MD5.png]]

2、因为登录的逻辑都写在子组件中，所以我们在调用子组件函数的时候传入参数即可

![[00 assets/c019075650b88e3e4ffd77afac61af98_MD5.png]]

### 11.3.2 菜单设计

#### 11.3.2.1 基本介绍

`RBAC`也就是`role based access control`基于角色的访问控制。如果我们设计权限系统的话，也是按照下面的方式来设计，其中数据库对于权限的设计也是这样处理的

![[00 assets/c7861eb6a2718b7e7352691d02ed2c3a_MD5.png]]

#### 11.3.2.2 获取用户信息

1、我们再编写一个接口即可

![[00 assets/96d404838d6b8ff3948b59b0c6820f75_MD5.jpeg]]

2、但是存在鉴权的问题，我们将鉴权的`token`写在请求拦截器中

![[00 assets/d36915c4c7d558dfcb7c772d03dcfa56_MD5.png]]

#### 11.3.2.3 获取菜单信息

1、其基本的操作和之前是一样的

![[00 assets/4d830b976a26dcdca619e2b788e3fe5c_MD5.png]]

2、老师这里使用的权限管理的方案是将用户的权限地址都存入到了服务器，并且是一个树结构，所以就不存在本地修改代码导致权限泄漏的问题了

![[00 assets/a9f9400fd83da69bf675a414bfc41059_MD5.png]]

#### 11.3.2.4 菜单树布局

![[00 assets/f6709e8d8af0dc5f5f8d63ab1a05582c_MD5.png]]

#### 11.3.2.5 动态菜单

1、我们将菜单信息都存在到`localStorage`，因为直接存在`pinia`中就是存在`内存`中，如果网页刷新的话，这些数据就会消失

![[00 assets/e09e5801a30f3916a93497aa02d5cd68_MD5.png]]

2、下面就是动态菜单的结构

![[00 assets/bab9b14827ce5488b82719bc670a3844_MD5.png]]

3、因为返回的数据中带有图标信息，也就是图标的名字，但是并不带图标的网址。所以这里选择使用动态组件的方式来填充图标，我们已经将所有的图标注册为全局的组件，所以这里直接输入图标的名字的就可以显示图标

![[00 assets/4a2717093813ea693ec6987c7bd41890_MD5.png]]

![[00 assets/61336e1d7990a63356194fe7085ba5b6_MD5.png]]

可以看下之前图标的设置就是下面的形式

![[00 assets/00e4cc448afbb4b069285a02db6cc6a8_MD5.jpeg]]

#### 11.3.2.6 \*动态路由

> 传统方式

一次配置所有的路由信息，编写所有的页面信息。但是这种方式存在一个问题，如果一个权限比较低的用户知道你的路由信息就可以无权限进入，这是一个很危险的事情。所以可以采用动态路由的方式来处理

![[00 assets/004660256a19995433e428e1db920ac5_MD5.png]]

> 动态路由

1、一般存在下面的 2 种方式来实现动态路由。第一种就是将所有权限的路由都编写成一个`JSON`格式或者一个数组形式，根据用户的信息来决定使用那个路由，这种方式存在一个弊端，如果需要再添加一个权限的话就需要重新编写代码部署。第二种方式就是根据返回的动态菜单的数据，动态设置路由并且使用

![[00 assets/cd2f5ecec0aa2185cbd4b9669eefdf4d_MD5.png]]

2、我们先按照`动态菜单`的格式来编写`路由文件夹`的层级

![[00 assets/a844c51bfc787198fd0aa4c928af820a_MD5.png]]

相对应的`views`文件夹中的层级也是一一对应的，这样方便查找

![[00 assets/6001509c20b533430a2dad7b05ed8c03_MD5.png]]

3、我们使用`import.meta.glob()`方法，来查找路径下所有的路由，并且导出，这里是全部权限的路由。最后导出匹配用户权限的路由即可，导出的数组就是全部的路由

![[00 assets/d7797006bbc40ea925c40079c565ef50_MD5.png]]

4、只要用户登录之后就会自动的添加路由进去。但是这里就存在一个问题，只要我们重新刷新页面的话路由信息就会消失，所以就会找不到路由

![[00 assets/98b18966a7f6bbcb4fc177606e8883e1_MD5.jpeg]]

5、所以我们刷新页面之后需要重新执行路由映射，首先来看下各个部分执行的顺序。`router外部加载` -> App 显示 -> `beforeEach`加载 。

6、如果在`router外部加载`的话`pinia`还没加载完毕所以不能在这里写。如果在`beforeEach`里面编写的话就会存在路由匹配直接加载页面了，就会加载到`NotFound`中，也直接排除

![[00 assets/16045cc9a21fda14201a0893cc024ac1_MD5.png]]

7、所以目前的方式是在`pinia`创建的时候加载即可，只要重新刷新页面的话就会重新加载`pinia`，就会重新执行加载路由的操作，所以这个就在执行路由之前加载了，不会跳转到`notfound`页面了

![[00 assets/87acbb28ee12aede1999b281e9afc4cd_MD5.jpeg]]

![[00 assets/4a2a3ad446fc9494e7bef7420b63b194_MD5.jpeg]]

8、下面就是处理，登录首次进入`Main`页面的话默认加载第一个路由的组件。只要我们登录跳转的时候就默认加载第一个路由

![[00 assets/c63389ce6a9908516eaace19c3b3aa17_MD5.png]]

但是这就存在一个问题，如果浏览器输入`/main`的话也需要跳转到第一个路由，按照上面的方式是不能跳转的。所以我们只要执行了`mapMenuToRouter`的话就获取第一个路由并且导出

![[00 assets/a50c7f6be7743bf30f6febc1738c7659_MD5.png]]

导出之后，只要`登录`或者`手动输入路由"/main"`的话就会自动跳转到第一个路由

![[00 assets/edf944cee72e507e054dc3a322f94d0d_MD5.png]]

\*`startWith`表示只要开头包含`/main`，并且不包含`token`的话就会自动跳转到`/login`页面

![[00 assets/1c719428c86e47afb0727684f0d1871f_MD5.png]]

#### 11.3.2.7 path 匹配菜单

1、也就是传入当前`path`，匹配路由信息导出`id`值。如果这样设计的话，只要重新加载`menu`的话就会匹配菜单，但是重新加载的场景只有`登录进入`、`刷新页面`、`地址栏输入地址`......会执行，剩下的都是点击`菜单`切换路由

![[00 assets/953a37ea4ea8959a5d04c77c8a8f7dfa_MD5.png]]

2、最后的`id`值传入给`elementui`的`default-active`即可

![[00 assets/22d3d8cb0f21e65da672f89e5f7800ee_MD5.jpeg]]

### 11.3.3 头部设计

#### 11.3.3.1 头部信息展示

![[00 assets/df1a55a6ed80ee6d7f7e419da9baab84_MD5.jpeg]]

1、按照下面的结构来做下拉菜单，剩下布局问题参考代码即可

![[00 assets/8f39cdae44f2de0c13ef7b276cb3d8da_MD5.png]]

2、这里依旧采用组件化的思路对头部拆分，方便管理

![[00 assets/0886c848fc4940830801cb2b08275fb5_MD5.jpeg]]

3、因为下拉菜单处于`app`的外面，所以外面很难对这个元素设置样式

![[00 assets/40fb952a4bc6510f8595e14022a74cb2_MD5.png]]

所以使用`:global`将元素设置全局的`HTML`的样式，就可以设置`#app`外面的样式

![[00 assets/54b7939da3abba0dc8caee7822c48f70_MD5.png]]

#### 11.3.3.2 :deep 使用场景

1、我们想要在父组件中对子组件中标签添加样式，按照下面的层级很明显不能生效

2、设置样式只会对根组件样式生效

![[00 assets/4051bdbd7b3da1b8438dc5fa65b5779e_MD5.png]]

3、使用`:deep()`属性就可以对子标签设置样式

![[00 assets/c672d71020ff9c092f1112d6192c548a_MD5.png]]

4、所以这个`:deep`的使用场景在`ElementUI`组件中设置修改其组件的样式

#### 11.3.3.3 面包屑

1、只要加载面包屑组件的话，就会自动执行`mapPathToCrumb`函数，其中 2 个`push`表示的就是`一级菜单`和`二级菜单`

2、为函数套上`computed`的话，只要里面的`path`发生了改变就会重新执行回调函数，这样不管啥情况，只要`path`改变的话就会自动修正面包屑

![[00 assets/09c803074a3600228db1a94b706898ac_MD5.jpeg]]

3、只要我们点击了系统管理，就会自动跳转到这个类别的第一个路由

![[00 assets/ef7215961f2a3c8343c22d2043e9abaa_MD5.png]]

第一个方法：我们在传入父路由的时候就默认传第一个即可，但是这个方式存在权限问题，如果第一个路由没权限的话就会跳转到`notfound`

![[00 assets/15ea4f4ca2fce4a332daabd17c8e0001_MD5.png]]

第二个方法：为父路由添加路由映射，重定向到第一个子路由。下面的逻辑就是，只要添加了父路由之后，后续就会检查是否已经添加，如果添加了就不去重定向的`push`，如果没添加就去添加

![[00 assets/7c15d0cc61331a24bf6580f70af3db62_MD5.png]]

这样就会有父路由重定向了

![[00 assets/7ff94a166c437a30dc549848903a62f3_MD5.png]]

4、我们点击上面的父路由菜单`系统管理`之后不会自动切换动态菜单，所以我们这里也让执行和`path`挂钩即可

![[00 assets/53c86b6ea356f30fb65c06e0f7c67cb0_MD5.png]]

### 11.3.4 User 页面 - 基础搭建

#### 11.3.4.1 界面搭建

![[00 assets/9d70891d08d14bf12ec80339a5b26ef4_MD5.png]]

1、我们按照下面的方式搭建页面

![[00 assets/59ab6469c21d2fb9608216b10deee4a3_MD5.jpeg]]

2、但是时间选择的位置默认是英文的，很明显不是很友好

![[00 assets/6d342300899b062d8b2f4e0b2692f5b4_MD5.png]]

这里就涉及到了国际化的处理，我们导入`zhCn`即可

![[00 assets/4d7169c9be302617547ec2f3adae6237_MD5.png]]

#### 11.3.4.2 重置按钮

1、我们获取`form`的`ref`，使用`resetFields`方法即可清除所有数据

![[00 assets/11bec58e46fd8575f39ecc951ddbdac7_MD5.png]]

2、注意这里一定要添加`prop`属性，并且要和`reactive`中的属性名一致

![[00 assets/0c312d5974fe23c63b99dde2118a00e6_MD5.png]]

![[00 assets/5d5cd235a702f09272582126fbf3a4b7_MD5.jpeg]]

#### 11.3.4.3 表格展示

1、在`pinia`中的`action`来网络请求数据即可

![[00 assets/f047de377f9524ae52cd1d6942ac968c_MD5.png]]

2、使用`el-table`显示数据即可

![[00 assets/d568ea358db208f8be485634f5c0eaf0_MD5.png]]

并且这里为了定义表格中状态的样式，可以使用作用域插槽来解决，插槽会默认向外部传输数据`scoped`表示的是整行的数据

![[00 assets/618b69c697d35e6b2e41d401b1544038_MD5.png]]

在文档中还有可以定义表头

![[00 assets/3fcd180ddcf5dc43930a022bc2e85c7c_MD5.png]]

3、相应的使用`store`中的数据即可

![[00 assets/cedeb8822b5d6c8183c4f2b896475ee9_MD5.png]]

4、我们这里显示的时间数据存在问题，我们需要修改一下。这里使用`dayjs`库来对时间进行处理

![[00 assets/2c80a576e6fab23e91809d7dbf722140_MD5.png]]

我们和上面的`enable`一样，使用作用域插槽来对时间进行处理

![[00 assets/dc8121c953db718aabc26950a3a40122_MD5.png]]

#### 11.3.4.4 \*分页器

![[00 assets/0c95a514bc23c30a9a8d351f17608b50_MD5.png]]

1、页面搭建，按照官网的例子搭建即可

![[00 assets/ce5b8377936188251e32fde6ac8f7aab_MD5.png]]

2、对于这里的`size`和`offset`就涉及了`Mysql`的分页查询。第一页就是`size:10 offset:0`，所以第一页就是`limit 0 10`，第三页就是`size:10 offset:20`，就是第二页。所以后端开发者直接就可以使用`limit 20 10`就行了

![[00 assets/091917675b8fca30f276c84112dc9479_MD5.png]]

3、这里还存在一个小坑，我们在第二页的时候修改`size`的话，就会先修改`size`，发送请求。这个时候如果数据不够，所以就会跳转到第一页再发送一次请求，这就发送了 2 次请求，也就是`size为20`页面为`2`的时候，`size:20 offset:20`，但是数据总数为`14`，所以可能导致没有数据的情况。所以我们设置一个`if`判断数据长度来发送请求，如果长度不够，就只请求页码修改的网络请求

4、并且需要考虑用户在第一页切换`size`，并且总数小于`size`的情况，所以我们还需要加一层判断

![[00 assets/a0b41bf8fb44e78b83f3eca6503bedb8_MD5.png]]

#### 11.3.4.5 重置/查询按钮

1、我们点击了查询/重置按钮的话，就会发出事件，并且传出数据

![[00 assets/6cb19bdead660253cee24c8816a5f261_MD5.png]]

2、我们获取`userContent`的`ref`，并且直接调用内部的网络请求的方法

![[00 assets/fa97e208f45c6369985e0fb65085ae94_MD5.png]]

3、这里就有一个小坑，我们查询之后点击分页是不带查询数据的，所以我们需要手动保存查询数据，只要传入的对象中有属性就覆盖

![[00 assets/c92256731419b94d5720dae0a7387fff_MD5.png]]

#### 11.3.4.6 删除数据

编写网络请求，写入`pinia`的删除`action`，监听删除按钮，调用删除接口并且重新请求数据

![[00 assets/022c5393a63afe1932cd36b34f778f4b_MD5.png]]

#### 11.3.4.7 新建用户

![[00 assets/92f982efd632c52120d05eff55ea9bae_MD5.png]]

1、搭建页面，按照框架来搭建即可

![[00 assets/d505859e02cc4988f80f7ac2cdbe0e95_MD5.png]]

2、我们新建用户的`userContent`发送事件，并且携带数据

![[00 assets/b5266469537fa3b39f685adaaadd97b8_MD5.png]]

将事件传输给`user`接受，并且使用`ref`来调用内部的函数

![[00 assets/29c8603ca880490d8403a6ab77435c00_MD5.png]]

传输数据修改变量，控制模态框的显示和隐藏

![[00 assets/492f78951216f53f185f1f9b648d283b_MD5.png]]

3、随后就是发送请求，存储数据

![[00 assets/9cbc6442588f6069d5a664e00550cd7f_MD5.jpeg]]

就是做出展示，回显数据

![[00 assets/80b55383ede2e4947109d27f57c5a6d7_MD5.png]]

4、这里不多赘述，大致业务逻辑基本都一样

#### 11.3.4.8 \*编辑用户

1、其基本的逻辑和新建用户差不多，这里不过多赘述了

2、但是这里有一个`ElementuiPlus`的`resetFields`的方法的坑，他并不是重置所有数据，而是回溯到`DOM`插入之前的数据。比如我在`setup`中调用函数，并且传入数据，如果后续调用`resetFields`就会回溯到一开始的数据，而不是清除

![[00 assets/29be0397056702e779fa5342dd300623_MD5.png]]

我们可以将显示`Message`封装为一个函数，这样直接调用即可

![[00 assets/27d19e6831c2e1d0119447cf5cb82636_MD5.jpeg]]

#### 11.3.7.2 \*分页细节 - $onAction

1、我们以前创建新用户的时候都不会进行页面跳转到第一页，这是一个小细节的优化。目前存在 2 种方式的运用，第一种就是使用`事件`，第二种就是使用`事件总线`。我偏向于第一种，因为这样的传递有迹可循

![[00 assets/e8f1652cc5008e88af8cb5af612859c8_MD5.png]]

2、但是我们还存在第三种方式来处理，就是使用`pinia`的`$onAction`来监听`store`的`action`即可

![[00 assets/7b732d98c315c6f46303251167bb8f2c_MD5.png]]

3、我们使用`pinia`的`$onAction`来处理，它可以监听`systemStore`中`action`函数的调用，只要调用的话就会执行里面的回调函数，我们通过`name`来作为参考进行处理

![[00 assets/bef6ee9857e7623966daee5be9338514_MD5.png]]

### 11.3.5 Dep 页面 - 组件抽取

#### 11.3.5.1 Search 抽取

1、我们可以发现后台管理系统的很多页面都是差不多的，所以我们可以抽取高阶组件，使用配置文件的方式来编辑页面

![[00 assets/8b1fa2a2ca568b2e64bf9711f700b313_MD5.png]]

![[00 assets/3358d264acf03ba951152348c36ba20d_MD5.png]]

2、在抽取页面之前，我们可以先归纳网络请求部分。我们网络请求的架构是`axios -> pinia -> 页面`，所以我们需要修改`axios和pinia`部分

3、网络请求大致可以分为下面的 5 条接口，即`增删改查`，对于不同部分的接口就使用`pageName`传入作为区分即可

![[00 assets/07b520133a191cc4709452640dc4bfd6_MD5.png]]

4、网络请求分出来之后，就需要区分`pinia`中的`action`的使用

![[00 assets/39f50e602c6971afedc7d393b3b07b5b_MD5.png]]

我们只需要传入`pageName`中即可表示不同的接口处理

![[00 assets/0e55471dbc7fc06d44937b23410cb683_MD5.png]]

5、我们再来搭建页面，因为我们需要使用配置文件的方式来搭建页面，所以先编写配置文件的格式

![[00 assets/9efd16574d1e70427e01d49bbe2e0cb2_MD5.jpeg]]

我们使用`v-for`来遍历配置文件，使用`template + v-if`的方式来动态生成不同的组件

![[00 assets/d7db0100c5dc4fa0be601ed2bb23552b_MD5.png]]

其内部的逻辑基本没变，这里使用`pageXXX`的方式命名，让该高阶组件更加通用

![[00 assets/57c949c23d4e2a8d52b6a22c3b86c5d8_MD5.png]]

6、我们使用`ts`来编写`Vue`项目的话可以使用`props`的语法糖，传入接口就可以获取该`props`数据，并且组件也有相应的提示

![[00 assets/fb7ab42ec1b84b52224081ac1edcd3cb_MD5.png]]

#### 11.3.5.2 Model 抽取

1、对于`模态框`的设计，其遵循的原则和上面的`搜索框`是一样的，这里直接看源码就行了

![[00 assets/e0de9bcfdb54acd6d1b25df13c66f839_MD5.png]]

2、但是对于`模态框`存在一个`options`，这个东西内部的数据是动态的

![[00 assets/5e9fa61b854bf4a431d5d8459a824588_MD5.png]]

3、但是我们编写的配置文件的`options`是没有数据的，所以我们需要手动将数据填充进去

4、只要加载该组件就会自动请求数据，并且这里使用`计算属性`来处理，这里可能最优解就是使用`计算属性`，因为网络请求可能会延迟，所以将`DepartmentData`放在`computed`中，只要数据变化就会自动更新数据，这样就避免了网络延迟的问题

5、内部将网络请求到的数据存入`options`，这样内部数据就是动态的

![[00 assets/495c19c838fdbc461415285f5bd49688_MD5.png]]

#### 11.3.5.3 Content 抽取

1、其抽取也和之前是差不多的，这里直接看源码

2、这里主要的就是对于`table`中插槽的处理，相对来说比较复杂

![[00 assets/adc50164f55d9985b436fc2efe551d42_MD5.png]]

3、比如下面的表格中`状态、创建时间、更新时间`都是需要进行处理之后才能使用的

![[00 assets/12c3a8764feb25f7c4bb43c9c24c61fe_MD5.png]]

如果我们按照之前的方式就是编写很多的`template + v-if`来处理，但是会发现这样就需要写很多的`v-if`，很显然这很麻烦，而且需要很多的`type`

![[00 assets/cb9f4f93b14b7b54adcaaed51c1a1ded_MD5.png]]

4、所以这里就可以使用插槽来处理，使用`:name="item.slotName"`来设置插槽名，并且对于`el-table-column`下的`#default`就是插入到`table`中的插槽，并且传出数据`scoped`，最后传入到`slot`中，所以这里存在一层嵌套。梳理一下就是`el-table-column -> #default -> slot`的嵌套关系

![[00 assets/54731f028b81d8225b6f38470bc338e8_MD5.png]]

5、这样就实现了表格内的定制化处理

#### 11.3.5.4 Hook 抽取

因为存在很多的相同的方法，我们可以使用`hook`抽取的方式来抽象方法

![[00 assets/3814bd84abbf1aa9448a104c8d0c0f31_MD5.png]]

#### 11.3.5.5 showMessage 抽取

![[00 assets/584e26e93f17e3b7c7c5a6c28b2d4ab6_MD5.jpeg]]

1、我们将`showmessage`进行抽取，这样我们只需要传入`message`即可

2、并且我们对常量进行抽取，这样我们以后想修改的话，只需要修改这个部分就行

![[00 assets/5b319567ddbd467a8690c5f357f2676e_MD5.png]]

### 11.3.6 Menu 页面

#### 11.3.6.1 页面设计

![[00 assets/047c47378911c6cb8aa621488065b46b_MD5.jpeg]]

1、这个在`elementui`中有对应的组件，可以直接使用

![[00 assets/5ee4d5d28faa252d8affbef1e6231b64_MD5.png]]

2、我们在使用的时候就参考文档即可

3、对于参数来说，可以直接使用`v-bind`指令，这样就会展开对象，也就会变成`rowKey:"id" treeProps:{ children:"children" }`放入到`el-table`中

![[00 assets/7e3f8193edb6b5e2684980672d99f998_MD5.png]]

4、后续的编辑，删除，新建等功能这里就不去做了，直接参考老师源码即可

#### 11.3.6.2 User 菜单子树

![[00 assets/b18356cd707ac4204390727dbcfcf2a8_MD5.png]]

1、这个对于`elementui`也是存在组件直接使用

![[00 assets/2dccccd12906aabd4b9d782a552f5a34_MD5.png]]

2、但是这里就存在一个问题，我们在`Model`中并未封装`插槽`，所以我们还需要使用`template + v-if`的操作模式再编写一个树结构的组件，并且在内部编写事件，很显然这样会导致高阶组件的代码变得不可维护，所以我们这里添加插槽的选项，在使用时传入就行

3、这里其实就是一种高阶组件使用的思想，我们封装的高阶组件，经可能将复用的方法写入，但是对于独特的方法，组件最好就是外部传入，这样就避免了耦合，提高了高阶组件的纯度，在后续的样式和数据传入也有涉及

![[00 assets/2502e41920b79260b988b587c87ceb98_MD5.png]]

4、我们通过`请求三层架构`获取数据并且传入更新`DOM`，这样就出现了`菜单子树`

![[00 assets/e38df93dd0abc02e156d1ff9ae70fec0_MD5.png]]

5、我们点击了菜单子树的选项之后，就会获取绑定的`node-key`的值，我们整理之后传入就行

6、这里就体现了`高阶组件`的封装思想，这个数据只有自己拥有，所以我们需要将该数据放置在外面，而非高阶组件中。并且对于参数的设置也需要思考，外面使用对象的形式，这样可以传入很多的其他参数，而非一种

![[00 assets/2fdc66ef50d90cd5dbd69a92abf45478_MD5.png]]

7、新建和编辑都是封装好的`Hook`，并且参数也是直接传入到`Hook`中，所以我们可以使用回调函数的方式获取参数，只要新建或者编辑的话就会执行该回调函数

8、使用这种方式就扩展了`Hook`的功能，只需要传入回调函数就能执行特定的功能。比如：新建中就是清除之前的数据，而编辑需要数据回显，就需要遍历`菜单id`并且返回设置

![[00 assets/2cda17cfe295b79f15806d7e34cc0248_MD5.png]]

9、对于菜单的返回`id`可以写在`utils`中，这里使用的是函数递归来获取

![[00 assets/4be6a6d9c160c0d0318967466abae564_MD5.png]]

#### 11.3.6.2 \*nextTick 原理

1、我们首先可以看`Vue`文档中如何说明的，可以看到其实`Vue`会将一些执行的东西放入到`缓存队列`中，所以有的时候获取`DOM`不是更新之后的`DOM`，而是队列执行之前的

![[00 assets/955b85efcc6bb460e77395e7f7892476_MD5.png]]

2、我们这里写的时候时先显示的`模态框`，然后执行的`CallBack`。这个时候可能`ref`没有获取到了`DOM元素`，所以数据根本插不进去，就会导致报错。所以这里就使用了`nextTick()`回调函数来处理，只要`DOM`都更新完毕之后才会去执行

![[00 assets/9b8c381dc43ce749ce585a3fa7be07e5_MD5.png]]

如果简化的话，就是下面的步骤。数据已经更新了，但是在获取`DOM`的时候，`Vue`并没有重新执行`DOM`，所以导致获取`DOM`并且插入值就是之前的

![[00 assets/2e4915787b20d829367c0e3f609d01da_MD5.png]]

3、其实在源码中，`nextTick`就是`new Promise(() => { ...任务队列 }).then(nextTickCallBack)`的执行过程，就是放在`.then()`中执行的，这样就保证了`DOM更新`完毕了。

4、并且对于`nextTick`来说，他是属于`微任务队列`的，这个面试比较常见

![[00 assets/24b52263ed68d5a1a89217422b08c757_MD5.png]]

### 11.3.7 按钮权限

对于按钮权限存在增删改查 4 种方式，我们在返回菜单信息都是一并返回，所以需要对其进行处理

![[00 assets/bd7741242c262ac92a6fd6f94c5cac04_MD5.png]]

1、首先是对`menus`进行处理，并且返回`permissions`，下面的遍历使用到了递归

![[00 assets/f298797223b10520cfa0892750a71828_MD5.png]]

2、获取到数据之后对数据进行查询，如果有的话就修改`isCreate`......等作为判断条件的值，没有的话就不显示

3、但是这种方式存在一个问题，就是我们在这个页面中需要写一遍，但是跳转到另外一个页面的话就需要再来写一遍了

![[00 assets/38fab7b0bbd92ffec470390593a7e9e7_MD5.png]]

4、所以我们这里可以抽取`hook`来处理，我们传入查询的参数即可

![[00 assets/af3ca184084e19dcea79b66fa6bf4f42_MD5.png]]

然后使用`isCreate`......来控制页面组件是否显示，就可以完成组件的显示了

![[00 assets/9731a8fe4040ed2eef18452d6c54bac1_MD5.png]]

## 11.4 图表搭建

### 11.4.1 countCard 搭建

我们要实现下面界面的搭建

![[00 assets/799d641c0d034b947fbfc64f6d6d8caa_MD5.png]]

我们按照下面的格式进行编写即可，剩余的就是请求数据放入到`store`中，最后来渲染即可

![[00 assets/b7c36bd42eb9ca091333790e51cd0934_MD5.png]]

### 11.4.2 数字滚动实现

1、这里使用到了`CountUp`的库进行处理`npm i countup.js`

2、我们需要在数字前面加上`￥`来处理，这里存在 2 种实现方式，其中一种就是直接在`html`中添加`￥`来处理

3、第二种方式就是添加对`CountUp`中添加`prefix`配置

![[00 assets/500024ce2035fd5a44ee3411787363cc_MD5.png]]

### 11.4.3 echarts 基本实现

1、我们需要引入`echarts.js`的包`npm i echarts`

2、我们需要书写配置，并且`echarts`的实例化需要放入到`onMounted()`的回调函数中进行处理，因为这里需要操作`DOM`，所以需要放入里面

3、引入的时候一定要使用`import * as echarts from "echarts"`来引入，不然会引入失败

4、下面的`renderer`表示使用`canvas`引擎来渲染图表信息，还可以切换为`svg`的形式

![[00 assets/b367dc6ab945c8058681d0eb11406f14_MD5.png]]

### 11.4.4 echarts 封装

1、我们按照三层来封装`echarts`，首先是`用户显示层`，我们直接调用`pieEcharts`即可，传入数据

![[00 assets/4d2079e22e0f3555e5df180ab2168594_MD5.png]]

显示层将数据传输给`pieEcharts`之后，`pieEcharts`会进行配置，该组件就是专门存放配置的。然后就就将配置传输给`baseEcharts`，这是所有图表的根基，它专门用于实例化图表的

![[00 assets/2a5778dc70a06b45bd48bcdc1f2bb564_MD5.png]]

2、最后汇总其实就是`显示(传输数据) => 上层图表(写入配置信息) => 下层图表(实例化图表)`的过程

3、这样我们只需要编写配置信息之后，再传入数据即可

![[00 assets/6cb9d254bece1fb2a08f910e1947d1ba_MD5.png]]

### 11.4.5 \*数据动态展示

1、首先就是书写网络请求的部分，下面提供了一种新的思路，我们可以将请求都写成枚举类型，这样只需要修改枚举类型里面的值即可

![[00 assets/ce7ba73eccd7a16b1ab3f0fe29fd2680_MD5.jpeg]]

然后将网络请求写进`action`中，因为都是不相干的数据，所以可以同时异步请求处理

![[00 assets/5bbbbbd25e7980c1705b62aceee1588f_MD5.png]]

2、请求到数据之后进行映射。注意，一定要使用`computed`，因为一开始是获取不到数据的，所以要计算它的依赖，它需要实时变化

![[00 assets/f012c225205b114c9b1876cf64ff1106_MD5.png]]

3、同理，因为是三层架构，所以`pieEcharts`也需要使用`computed`来实时监听变化，然后传输给`baseEcharts`

4、这里就有一个需要注意的点，因为我们使用`computed`传输给`baseEcharts`之后，我们使用`setOptions`设置的表格就是第一次的传输的数据，也就是数据为空的配置。

5、但是后续网络请求到达之后`props`中的数据已经发送变化了，但是图表已经渲染成功，所以即便数据改变也不会重新渲染图表。这里我们就需要使用`watchEffect`来处理，它会搜集依赖，只要内部响应式数据改变就会重新执行，这样后续网络请求达到之后也能做出改变

![[00 assets/6b5cd29cefbb44e81f9f1365719fe705_MD5.png]]

### 11.4.7 图表展示

我们需要展示下面的一系列图表数据

![[00 assets/fad3506aaa22816c995a67f5a96e184b_MD5.png]]

1、我们按照上面的方式封装了`echarts`，并且实现了动态数据加载的处理，这里再添加图表就方便很多了

2、我们只需要编写配置信息，最后传入到`baseEcharts`中即可

![[00 assets/d0c46685b030efb5df496ab117e36f27_MD5.jpeg]]

3、相应的这里有很多的数据映射，因为服务器返回的数据不一样，我们需要手动的进行映射处理

![[00 assets/ea1ae7ba6e2e0053bf79fe94cebc3fc3_MD5.png]]

4、其基本步骤就是`请求数据 -> 放入pinia -> 页面获取(computed) -> 通过props传入 -> 图表展示`

### 11.4.8 地图展示

1、我们需要展示地图数据，第一步就是注册地图。其中第一个参数是地图名，第二个是传入`ChinaJSON`值

2、然后就是在`baseEcharts`的基础上再传入`地图`的配置。

![[00 assets/4c28dc8cc0bfadf587adf8251044eb45_MD5.png]]

3、这里展示的数据我们需要经过转化之后才能使用，所以这里我们写了一个`utils`的函数转化

![[00 assets/1ce21f3a4659dde80b8d12f82eff6635_MD5.png]]

4、剩下的代码查看我写的代码即可

### 11.4.9 Card 封装

1、可以发现下面有很多的代码其实是不必要的，我们可以将图表的`Card`封装为一个组件来进行处理

![[00 assets/081de6861d102caa72bb1ce8ad0dbf82_MD5.png]]

2、下面为封装的过程，这里使用到了插槽

![[00 assets/aef248fe67d04192228fc88407f70b22_MD5.png]]

### 11.4.10 \*页面自适应

1、首先就是使用`Echarts`的重新渲染的处理，我们可以在`onMounted`编写`onUnMounted`钩子函数，这个也是可以正常生效的，这样我们就可以共享数据的同时删除数据

![[00 assets/9ec5015ad9ebf4f8c0f48c4d26f95161_MD5.png]]

2、第二个就是布局的处理，我们在`ELementUI`中有响应式布局

![[00 assets/f840fefb8ddc9dd174f215984e3477a5_MD5.png]]

下面就是响应式的处理，我们传入相应的参数即可，下面就和`:span`是一样的，一行是`24格`

![[00 assets/86038c9119ca65eabbb8889fad04a9f9_MD5.png]]

下面是我们之前写的`:span`的处理方式，如果实现响应式就可以参考上面的代码

![[00 assets/3f8ebad4d5085196450e9adc49bbb435_MD5.png]]

## 11.5 Git 约束

### 11.5.1 husky

1、我们在项目中使用`npm run lint`就可以自动格式化所有的代码

![[00 assets/639db15b2706d541e7fbb7aeb7ce6878_MD5.png]]

2、如果团队编写可能风格不一样，我之前使用`eslint`来约束代码规范，但是可能再`git`的时候没去格式化代码，所以我们代码可能和没约束是一样的

3、所以我们使用`husky`来避免这个情况，它可以在提交代码的时候格式化代码。我们执行下面的命令来安装

```bash
npx husky-init && npm install
```

4、这里需要注意一个问题，使用之前一定要有`git仓库`，而且`powershell`需要使用下面的命令

```bash
npx husky-init '&&' npm install
```

5、我们需要再`.husky`中编写`npm run lint`才可以自动执行

![[00 assets/d7e231776789175ace5554045e532594_MD5.png]]

6、然后正常提交代码就行了，它会自动执行格式化代码

![[00 assets/a7c2c293ef6d953093b44cae9b99c8e0_MD5.png]]

格式化之后的代码

![[00 assets/5f4080f1803ce95d0c165abd2519be65_MD5.png]]

### 11.5.2 commit 规范

通常我们的 git commit 会按照统一的风格来提交，这样可以快速定位每次提交的内容，方便之后对版本进行控制。

![[00 assets/3ce74ef51dcaf6ec3660ecb37bceb3ae_MD5.png]]

但是如果每次手动来编写这些是比较麻烦的事情，我们可以使用一个工具：`Commitizen`，`Commitizen` 是一个帮助我们编写规范 `commit message` 的工具；

1.安装 Commitizen

```shell
npm install commitizen -D
```

2.安装 cz-conventional-changelog，并且初始化 cz-conventional-changelog：

```shell
npx commitizen init cz-conventional-changelog --save-dev --save-exact
```

这个命令会帮助我们安装 cz-conventional-changelog：

![[00 assets/68feb37d240ca309e61effc7c25301db_MD5.png]]

并且在 package.json 中进行配置：

![[00 assets/aa3501cfc357ca40f4783dbac6dd57f6_MD5.png]]

这个时候我们提交代码需要使用 `npx cz`：

1、第一步是选择 type，本次更新的类型

| Type     | 作用                                                                                   |
| -------- | -------------------------------------------------------------------------------------- |
| feat     | 新增特性 (feature)                                                                     |
| fix      | 修复 Bug(bug fix)                                                                      |
| docs     | 修改文档 (documentation)                                                               |
| style    | 代码格式修改(white-space, formatting, missing semi colons, etc)                        |
| refactor | 代码重构(refactor)                                                                     |
| perf     | 改善性能(A code change that improves performance)                                      |
| test     | 测试(when adding missing tests)                                                        |
| build    | 变更项目构建或外部依赖（例如 scopes: webpack、gulp、npm 等）                           |
| ci       | 更改持续集成软件的配置文件和 package 中的 scripts 命令，例如 scopes: Travis, Circle 等 |
| chore    | 变更构建流程或辅助工具(比如更改测试环境)                                               |
| revert   | 代码回退                                                                               |

![[00 assets/1a976bd4ae4ee5f886118311acbbd952_MD5.png]]

2、第二步选择本次修改的范围（作用域），也就是修改了那些文件

![[00 assets/4688d790c8cb81941d4d0c7c4d6ab4ee_MD5.png]]

3、第三步选择提交的信息

![[00 assets/8f5e6aef2c3e7580e5ceb46cbd2c9323_MD5.png]]

4、第四步提交详细的描述信息

![[00 assets/23383975e37fae6f6f3d16dd8d4370ab_MD5.png]]

5、第五步是否是一次重大的更改

![[00 assets/f160c87cf8d6edff3d3082b0477b0091_MD5.png]]

6、第六步是否影响某个 open issue

![[00 assets/81befbc96a3784704aefcd0da8b769af_MD5.png]]

下面就是我们使用`cz`来生成的`log`记录

![[00 assets/9d8eacf9c519e7ac39a744ce51a990e3_MD5.png]]

我们也可以在 scrips 中构建一个命令来执行 cz

![[00 assets/3e906fc4e89fef703cde0589cfcaeaf3_MD5.png]]

### 11.5.3 提交验证

如果我们按照`cz`来规范了提交风格，但是依然有同事通过 `git commit` 按照不规范的格式提交应该怎么办呢？我们可以通过 commitlint 来限制提交；

1.安装 @commitlint/config-conventional 和 @commitlint/cli

```shell
npm i @commitlint/config-conventional @commitlint/cli -D
```

2.在根目录创建 commitlint.config.js 文件，配置 commitlint

```js
module.exports = {
  extends: ['@commitlint/config-conventional']
}
```

![[00 assets/8519ece26f0e2dee79e9f8462929c9ec_MD5.png]]

3.使用 husky 生成 commit-msg 文件，验证提交信息：

```shell
npx husky add .husky/commit-msg "npx --no-install commitlint --edit $1"
```

![[00 assets/d9a50eb24635608e89edb4507dd55c6d_MD5.png]]

4、可以看到我们使用`git commit -m "123"`提交的时候就会被拦截，然后报错

![[00 assets/1a5c955144804c340594d6ad11a7bf91_MD5.png]]

5、因为我们安装了提交验证，所以需要使用`cz`来提交

6、我们看命令就可以发现，其实是依次执行命令的，首先就是执行`cz`，然后就是值`husky`的`npm run lint`，然后`commitlint`全程都是验证作用

![[00 assets/a579ed5664732fe6498f793cd4649a11_MD5.jpeg]]

7、按照这样的方式我们就搭建了一个很严密的`git`提交验证流程

