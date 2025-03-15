视频介绍：[尚硅谷 Vue2.0+Vue3.0 全套教程丨 vuejs 从入门到精通\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Zy4y1K7SH?from=search&seid=15643037923276153545&spm_id_from=333.337.0.0)

视频参考：coderwhy - 前端系统课 - 2022 - Vue

# 1. 非脚手架 - OptionsAPI

## 1.1 基本介绍

> 基本介绍

vue 是一套用于构建用户界面的**渐进式**JS 框架，vue 可以自底向上逐层的应用

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319101.png" alt="image-20220930091611114" style="zoom: 67%;" />

> Vue 地位

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319132.png" alt="image-20220930092036824" style="zoom:67%;" />

> 优点

**1.**采用组件化的模式，提高代码复用率，且让代码更好维护，其中一个组件就是一个 vue 文件格式

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319135.png" alt="屏幕截图 2022-03-03 170917" style="zoom:67%;" />

**2.**声明式编码，不需要直接操作 DOM，提高开发效率。具体的介绍可以参考`Vue3 1.3 声明式编程和命令式编程`的介绍

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319127.png" alt="屏幕截图 2022-03-03 171345" style="zoom:67%;" />

**3.**使用虚拟 DOM——优秀的 Diff 算法，尽量复用 DOM 节点。提高渲染的效率，并且更好的支持跨平台

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319151.png" alt="屏幕截图 2022-03-03 171949" style="zoom:67%;" />

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319159.png" alt="屏幕截图 2022-03-03 172007" style="zoom:67%;" />

## 1.2 基本使用

我们需要导入`Vue文件`再来编写单文件的`Vue`，这个也是最简单的引用方式，后续会使用脚手架来创建

![image-20221003093416270](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319909.png)

这个时候我们再来看使用`脚手架`创建的`Vue`，其实本质也是一样的，我们将入口文件的`App`引入，然后放到`createApp`来创建，最后再挂载到`index.html`中`id属性`为`app`的`div`中。和我们写单文件是一样的

![image-20221003093500389](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319928.png)

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

![image-20221003103654144](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319945.png)

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

![image-20221003104131968](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319965.png)

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

![image-20221003105324040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319984.png)

## 1.5 模板语法

![image-20221003111703409](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319002.png)

对于`Vue`的模板语法来说只能使用`表达式`，所以需要区分`表达式`和`语句`的概念，其实就一个思想

**表达式**：一个表达式会产生一个值，所以需要放在一个需要值的地方，比如：a、a+b、fn(1)、x === y ? 'a' : 'b';

**js 代码：**比如：if( ){ }、for( ){ }

![image-20221003123131681](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319656.png)

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

![屏幕截图 2022-03-15 122322](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319686.png)

### 1.6.2 v-html

这个和上面的`v-text`最主要的区别：它是`解析HTML标签`，其他的特点基本和`v-text`是一样的。但是 v-html 存在安全性问题，容易导致 XSS 攻击，导致 cookie 被盗取，所以建议少使用

### 1.6.3 v-cloak

我们在使用浏览器访问服务器的时候，并不一定是每次都是加载的很快。并且是将`Vue.js`放在`CDN`来加速的时候，也不一定在`html`之前下载下来，这样就会导致`{{ message }}`等语法提前显示出来，影响用户体验。为了应对着一种情况我们需要一个解决的方法

![image-20221003130057396](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319714.png)

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

![动画11](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319745.gif)

##### 1.6.6.2.2 数组形式

可以参考上面的`字符串形式`，下面就是使用数组的形式来处理

![image-20221003152753374](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319777.png)

##### 1.6.6.2.3 对象形式

对于对象形式的本质就是`:class="{active : true}"`，只要是`true`的话就可以使用名为`active`的类名。

并且对象语法也可以和数组语法合并在一起使用

![image-20221003152626867](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319813.png)

##### 1.6.6.2.4 总结

1. 字符串写法：样式类名不确定，需要动态指定
2. 数组写法：要绑定的样式不确定，名字不确定
3. 对象写法：要绑定的样式个数不确定、名字不确定，但需要动态决定

#### 1.6.6.3 绑定 style

##### 1.6.6.3.1 对象形式

![image-20221003155026751](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319118.png)

下面为`Vue3`的官方的写法，官方文档：[Class 与 Style 绑定 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/essentials/class-and-style.html#binding-inline-styles)

![image-20221031111246224](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319159.png)

##### 1.6.6.3.2 数组形式

![image-20221031111418658](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319198.png)

#### 1.6.6.4 绑定属性

##### 1.6.6.4.1 字符串形式

一般使用这种形式来添加的方式很少，所以不是很推荐

![image-20221003162839048](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319347.png)

##### 1.6.6.4.2 对象形式

这个方式在使用组件中经常使用

![image-20221003163247686](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319628.png)

##### 1.6.6.4.3 外部样式

官网介绍：[单文件组件 CSS 功能 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/sfc-css-features.html#v-bind-in-css)

![image-20221122162436893](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319649.png)

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

![动画1](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319669.gif)

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

![动画2](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319709.gif)

#### 1.6.7.2 v-model 本质

![image-20221024190153840](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319747.png)

对于`v-model`其实我们也可以手写来实现双向绑定，所以本质不过是一个`语法糖`

![image-20221024190555232](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319133.png)

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

![image-20221024213334924](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319314.png)

#### 1.6.7.5 :model

1、对于`:model`并不是`v-model`的简写，而是`v-bind:model`的简写，在`elementui`中要注意这 2 类指令的写法

2、如果写成`v-model`的话就会导致`el-form`做校验的时候读取不到数据

![image-20230321171044321](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319335.png)

#### 1.6.7.6 h 函数使用 v-modal

1、一些组件库，比如：naive-ui 会使用 **h 函数** 来做数据渲染，一些情况我们需要去做一些额外的处理，我们都知道 **v-modal 本质其实一个语法糖**，在 h 函数 中就不能再使用这个语法糖了，下面代码就是解决方法

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405112112174.png)

### 1.6.8 v-memo

官方文档：[内置指令 | Vue.js (vuejs.org)](https://cn.vuejs.org/api/built-in-directives.html#v-memo)

这个是为了做性能优化，只要`v-memo`数组中包含的属性，就会更新下面的子树中的模板

![image-20221003145243337](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319351.png)

### 1.6.9 条件渲染

#### 1.6.9.1 v-if

使用`v-if`渲染的话，条件为`false`那么连`HTML标签`都不会渲染

![image-20221031125942015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319369.png)

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

![屏幕截图 2022-03-09 192744](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319445.png)

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

![image-20221031145550736](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319913.png)

我们使用`v-for`不仅仅可以遍历数组，还可以遍历`对象、字符串、数字`。并且`v-for`遍历对象的时候里面包含 3 个值，分别为`value、key、index`

![image-20221003193835147](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319939.png)

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

![屏幕截图 2022-03-09 195040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319964.png)

假如我们想要数组处理的列表渲染也是响应式的话，可以使用下面的方法

![image-20221003200605033](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319989.png)

#### 1.6.10.2 VNode

![image-20221003202558121](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319016.png)

最后的结构会创建一个`VNode`树。但是为什么需要构建这样一个树？为了做`diff算法`，还为了跨平台，比如该`虚拟DOM`可以渲染成`真实DOM`到`浏览器`中，还可以渲染到安卓中的控件来部署到`安卓`中

![image-20221003202750361](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319069.png)

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

![动画12](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319564.gif)

下面是文字的描述，建议看视频的描述

我们一开始的初始数据就是 id 为 001、002、003，我们根据数据来生成虚拟的 DOM，但是要记住只是生成的虚拟的，只是在内存中并不在页面中，相当于你只是创建了，但是还没和页面连接

假如我们加入一个新的数据，我们根据新的数据生成的虚拟 DOM，但是后面的步骤不是直接根据这个虚拟的 DOM 来创建真实的 DOM，不然的话这样设置一个虚拟 DOM 就没必要了，所以这个时候就进行虚拟 DOM 的对比算法

这个时候就需要使用 key 了，首先是 key=0 的时候和初始数据的虚拟 DOM 中的 key=0 对比，里面有 2 个节点，第一个是文字节点，第二个是 input 节点，通过检测文字节点并不是一样的，所以就替换了初始 DOM 里面的文字节点，但是 input 节点是一样的，所以就直接使用

后面的节点依次类推，key=1 的虚拟 DOM，文字节点也会替换，input 节点直接使用，到了 key=3 的时候，发现初始 DOM 里面没有，所以就直接添加上去

![屏幕截图 2022-03-11 122114](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319586.png)

这就是为什么会有这样的问题，要注意的是这个情况并不是经常发生，我们在正常使用的时候不会打乱 index 的值，所以故意让它错是为了引出这个解释

假如你使用 p.id 的话就不会有问题

![屏幕截图 2022-03-11 123300](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319622.png)

这样的话，我们没有使用 key 的话，就会 vue 就会默认写一个 index

**总结**

![屏幕截图 2022-03-11 124003](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319660.png)

#### 1.6.10.4 实践

##### 1.6.10.4.1 列表过滤

实现下面的功能，本质其实是`watch`和`computed`的对比

![动画13](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319686.gif)

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

![屏幕截图 2022-03-05 120613](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319702.png)

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

![屏幕截图 2022-03-05 120853](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319426.png)

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

![屏幕截图 2022-03-05 121044](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319443.png)

### 1.7.3 事件修饰符

#### 3.2.1 基本使用

假如需要使用到事件修饰符的话可以参考**官方文档**：[事件处理 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/essentials/event-handling.html#event-modifiers)，下图为基本的事件修饰符

![image-20221003165508811](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319463.png)

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

![动画3](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319485.gif)

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

![动画4](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319507.gif)

假如我们将`scroll`改为`wheel`话

![动画5](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319530.gif)

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

![动画6](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319077.gif)

但是我们来看下`wheel`，必须回调函数执行完毕之后再滚动滚动条

![动画7](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319107.gif)

所以这里我们需要使用`passive`来取消`wheel`这种情况

### 1.7.4 键盘事件

键盘的事件有`keyup`和`keydown`

![屏幕截图 2022-03-05 212456](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319128.png)

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

![屏幕截图 2022-03-05 214132](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319148.png)

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

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405091627406.png)

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

![动画8](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319170.gif)

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

![image-20221004195110151](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319246.png)

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

![image-20221006231432096](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319638.png)

### 1.9.3 其他写法

我们也可以在生命周期函数中这样书写

![image-20221020212930838](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319681.png)

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

![image-20221024163705506](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319792.png)

下面为核心的代码，在以前`JQuery`中学习的排他思想，就是消除所有元素的属性，为自己添加属性。下面是通过`:class`的对象形式的写法来实现的，只要该属性值为`true`的话就设置`class`为该属性。

其中主要的是对点击的索引进行存储，所以这里使用了点击事件来进行处理，

![image-20221024163611843](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319819.png)

## 1.11 组件化开发

### 1.11.1 全局组件

![image-20221024215027363](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319862.png)

下面就是使用`app.component`来注册一个组件

![image-20221024220614750](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319170.png)

当然我们也可以将组件中得`template`抽取到外面

![image-20221024220805879](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319222.png)

在使用`app.component`注册组件的时候需要注意组件名

![image-20221024221908730](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319267.png)

### 1.11.2 局部组件

![image-20221031155252925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319370.png)

下图就是注册局部组件

![image-20221031155302858](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319394.png)

# 2. 脚手架 - OptionsAPI

下面记录得笔记都为`Vue3`中得语法，如果需要可以查看我`Vue2`得笔记

## 2.1 基本介绍

### 2.1.1 Vue CLI

![image-20221025201343603](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319618.png)

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

![屏幕截图 2022-03-19 205208](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319665.png)

假如我们下载完毕的话，就是下面的这个样子

![屏幕截图 2022-03-19 210717](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319798.png)

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

![image-20221031160040836](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319144.png)

### 2.1.3 声明式和命令式编程

![image-20221003101735759](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319172.png)

命令式编程：每一步都需要自己操作

声明式编程：只需要提供数据和方法就可以自动完成操作

![image-20221003101446062](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319200.png)

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

![image-20221003111154594](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319234.png)

**\***当然还有很多其他的代码片段的语法

![image-20221110223042202](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319357.png)

3.`VSCode`配置，首先进入设置就有一个`配置用户代码片段`

![image-20221003111318312](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319496.png)

然后将代码复制过来即可

![image-20221003111351038](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319985.png)

配置完毕之后，以后只需要输入`VueCreate`就会出现下面的代码

### 2.1.5 组件化理解

在组件化开发之前，先来看下面的案例

其实工程化得本质就是将`App`中得`script`和`template`抽取出来，放到对象里面。所以我们使用下面得方式也是可以正常渲染页面，其中导包得时候要导入`vue.esm-bundler.js`才可以。

![image-20221025225804754](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319005.png)

下面是解释为什么使用`template选项`的时候需要使用`vue.esm-bundler.js`文件

下面为`Vue`渲染节点的过程，这个在`VNode`中提过一点。首先`Vue`会将元素转换为一个个的`VNode`，其实每个`VNode`都是一个函数，走的都是`createVNode函数`创建的，然后才会转换为虚拟`DOM`，再来转换为`真实DOM`。

![image-20221031163125797](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319092.png)

但是为什么编写`template`的时候需要引入`vue.esm-bundler.js`呢？而编写的`App.vue`就不需要引入？这是因为在`webpack`编译的时候加载了一个`vue-loader`的`loader`，会自动将标签转换为一个个的`VNode`，所以在`Vue`的源码中不需要`compile`的过程，但是对于`template`选项来说`webpack`并不会进行识别，所以需要引入`vue.esm-bundler.js`

### 2.1.6 Scoped

其实`Vue`中的`Style`包含自己的作用域，这里的使用的原理就是使用`CSS选择器`中的`属性选择器`。每个标签中添加一个哈希值，设置样式的时候就是使用`属性选择器`选择即可，这样就实现了样式作用域

![image-20221101185308525](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319117.png)

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

![image-20221101170713718](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319137.png)

## 2.3 组件通信

### 2.3.1 基本介绍

`Vue`中经常出现组件数据的传递

![image-20221101195806318](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319240.png)

### 2.3.2 props

#### 2.3.2.1 数组类型

下面就是使用`props`用父组件给子组件传值

![image-20221101200937701](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319698.png)

![image-20221101201017929](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319721.png)

#### 2.3.2.2 对象类型

> 基本使用

使用数组的形式只能接收数据，但是不能做类型的限制和初始化值

![image-20221101202651705](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319738.png)

> props 参数

`props`中的属性包含 3 个参数

![image-20221101202756656](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319848.png)

关于`props`的命名问题，这里可以总结为只要是涉及在`HTML`命名的问题，都理解为下面的方式，因为`HTML`不区分大小写

![image-20221101205221295](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319876.png)

> type 使用

`type`可以传递得参数有`String、Number、Boolean、Array、Object、Date、Function、Symbol`，下图中包含了`props`在日常开发中大多数得开发场景

![image-20221101204436528](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319975.png)

#### 2.3.2.3 非 props 的属性

![image-20221101215512241](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319606.png)

当然我们不想看到的话也可以直接关闭，添加`inheritAttrs`为`false`就可以了

![image-20221101215621939](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319633.png)

但是我们取消之后又想在该子组件的其他标签中添加呢？可以使用`$attrs 属性就可以手动添加上

![image-20221101215931639](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319668.png)

![image-20221101220132955](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319695.png)

### 2.3.3 emit

#### 2.3.3.1 基本使用

![image-20221101221711859](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319720.png)

因为`Vue`是组件化开发，所以有的时候会将`操作逻辑`分离到`子组件`中去。但是该操作需要可以影响到父组件中的数据，所以这个时候就需要用到`emit`

下图中将`+1`的操作都分离到了子组件，需要点击按钮影响到父组件中的`count`，实现响应式

![image-20221101222012740](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319742.png)

下面就是整个`子给父`传递参数的整个流程

![image-20221101222313232](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319398.png)

#### 2.3.3.2 事件验证

> 数组形式

![image-20221101223126625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319420.png)

> 对象形式

当然假如我们需要做事件校验的话，就需要使用对象形式来编写

![image-20221101223413672](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319436.png)

### 2.2.4 商品切换案例

下面为依赖关系图

![image-20221102085706573](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319461.png)

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

![image-20221102090043460](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319493.png)

### 2.2.5 Provide 和 Inject

#### 2.2.5.1 基本介绍

上面的`props`和`emit`是实现父子组件传递数据，但是使用`Provide和inject`是实现祖孙组件传递数据

![image-20221103103113649](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319522.png)

#### 2.2.5.2 字符串写法

下面就是使用`字符串的写法`，但是这种方式不是很好，因为数据都是存储在`data`中，不能动态获取

![image-20221103104730525](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319268.png)

![image-20221103105121868](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319285.png)

#### 2.2.5.3 函数写法

使用函数的写法就可以动态获取到`data`中的数据

![image-20221103105305898](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319305.png)

![image-20221103105623071](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319336.png)

#### 2.2.5.4 实现响应式

我们在使用函数写法获取到该组件中`data`中的值，但是当我们修改了值，`inject`的值并不会改变，也就是不能实现响应式的处理

![image-20221103105810866](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319358.png)

![image-20221103105905732](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319415.png)

假如我们需要处理这种场景的话，可以使用`computed`来处理，但是一般都使用`pinia和vuex`来管理了，所以这个`API`使用的场景比较小

这里需要注意的一个点就是`provide()`中的`computed()`的`this`的处理，在`computed`中使用的箭头函数，但是可以寻找到`this`，这是因为箭头函数是根据作用域依次寻找的，它需要访问的是`provide`中的`this`，所以需要在这里写箭头函数来向上级作用域寻找

![image-20221103110729013](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319162.png)

![image-20221103110739391](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319190.png)

因为`computed`返回值是`computedref`，可以理解为`ref`，这里的响应式原理就可以参考我的`JS高级`里面的内容。这样就可以实现响应式的原理

![image-20221103110806373](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319207.png)

### 2.2.6 全局事件总线

#### 2.2.6.1 基本介绍

我们使用全局事件总线的话，不仅仅可以父子组件通信，还可以祖孙组件通信，还可以非关系组件通信。也就是可以理解为可以**任意组件之间通信**

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319231.png" alt="屏幕截图 2022-03-24 164803" style="zoom: 67%;" />

#### 2.2.6.2 hy-event-store

下面是使用的`hy-event-store`来实现的事件总线，`npm官网介绍：`[hy-event-store - npm (npmjs.com)](https://www.npmjs.com/package/hy-event-store)

> 安装

```bash
npm i hy-event-store
```

> 配置事件总线

![image-20221103130222508](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319253.png)

> 使用事件总线

1.导入`eventBus`

2.使用`eventBus`的`emit`来发送事件总线的数据

3.使用`on`来接收事件总线的数据

![image-20221103130457012](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319281.png)

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319982.png" alt="image-20221103130557797" style="zoom:67%;" />

> 移除事件总线

当组件被销毁之后记得要移除事件总线的监听，因为移除需要获取到方法，所以这里的处理方式就时将方法写在`methods`选项中进行处理

![image-20221103131930631](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319002.png)

#### 2.2.6.3 mitt

参考文档：[(54 条消息) Vue3 笔记*mitt 库(事件总线)*英凛 zzZ 的博客-CSDN 博客\_mitt vue3](https://blog.csdn.net/qq_41196217/article/details/120695349?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~default-3-120695349-blog-124167423.pc_relevant_downloadblacklistv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~default-3-120695349-blog-124167423.pc_relevant_downloadblacklistv1&utm_relevant_index=4)

> 安装

```bash
npm install mitt
```

> 部署事件总线

![image-20221103132546086](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319024.png)

> 使用全局事件总线

本质和`hy-event-store`的库使用方式是一样的

![image-20221103133014391](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319056.png)

🎉：这里需要注意一个点，就是事件总线不能放到`setup`中使用

> 取消所有的事件总线

```
mittbus.all.clear()
```

## 2.3 插槽

### 2.3.1 基本介绍

![image-20221102091803074](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319084.png)

### 2.3.2 基本使用

![image-20221102091934396](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319111.png)

下面为基本的使用

![image-20221102093512220](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319374.png)

![image-20221102093535026](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319805.png)

### 2.3.3 插槽默认值

当你在不填写插槽的内容，但是想要它显示默认值。只要在`slot`中填写默认的`标签、组件`即可

![image-20221102095632366](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319825.png)

![image-20221102095746793](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319847.png)

### 2.3.4 具名插槽

下面就是具名插槽得具体使用过程，其中`v-slot:`可以简写为`#`

下面得例子是作为一个搜索栏得处理方式，其中`center`得搜索内容就可以封装为一个组件填充到该模板中，然后`left`得图标就是放大镜图片，只需要传入固定得标签`img`即可，变化`img`得`url`

![image-20221102101315403](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319871.png)

![image-20221102101331660](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319936.png)

### 2.3.5 动态插槽名

当然我们也控制插槽的位置，下面就是使用`v-slot:[SlotName]`来动态设置里面的参数，从而动态渲染插槽的位置。其中`v-slot:`也可以简写为`#`，比如`#[SlotName]`

![image-20221102111818264](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319683.png)

![image-20221102111826226](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319703.png)

### 2.3.6 渲染作用域

![image-20221102142209241](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319721.png)

也就是渲染的页面只能找本页面下面的数据，即便是通过**插槽**传给了子组件也不行

![image-20221102142156535](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319744.png)

### 2.3.7 作用域插槽

先说下为什么需要使用作用域插槽？比如说：`商品切换案例`，原本是使用`span`标签来显示的数据，假如在后续的组件中需要使用`button`来替换该标签在另外一个地方使用，这个时候数据是在子组件得，但是`button`是在父组件得，数据传输不是很方便，所以就需要子组件中的数据传输给该插槽中进行动态显示，这个时候就需要作用域插槽

![image-20221102152522153](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319767.png)

> 默认插槽 + 作用域插槽

下面为基本的使用，将子组件渲染的数据传输给父组件渲染再来显示

![image-20221102153056015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319792.png)

![image-20221102154131103](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319517.png)

对于默认插槽不仅仅可以使用上图中的`#default="props"`还可以直接使用`#="props"`来编写

![image-20221102154721448](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319532.png)

> 具名插槽 + 作用域插槽

因为默认插槽的值为`default`，所以上面的直接使用`default`就可以接收到。假如是具名插槽的话，使用方法就差不多

![image-20221102153959387](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319556.png)

![image-20221102154027595](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319588.png)

## 2.4 生命周期

### 2.4.1 基本介绍

![image-20221103152750588](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319610.png)

### 2.4.2 生命周期流程

其中`created、mounted、unmounted`是比较重要的

![image-20221103154418874](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319632.png)

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

![image-20221103163340345](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319290.png)

### 2.5.2 获取组件

> 获取 ref 实例

我们使用`ref`也可以获取组件中实例

![image-20221103164145587](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319314.png)

> 调用组件中的方法

我们也可以使用获取到的`ref对象`来手动调用组件中的方法

![image-20221103164109976](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319334.png)

> 获取组件中的节点

使用下面的方式来获取组件中的节点

```vue
this.$refs.RefHome.$el
```

有可能该组件中存在一个节点和多个节点

![image-20221103164741457](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319361.png)

> 获取父组件/根组件

```
this.$refs.RefHome.$parent  // 获取父组件
this.$refs.RefHome.$root 	// 获取根组件
```

## 2.6 动态组件

### 2.6.1 基本使用

比如说：点击按钮切换不同的组件。这个功能就可以使用动态组件来处理

![image-20221103171652779](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319387.png)

我们可以使用`component`标签来动态展示组件。其中`is`属性就是表示显示那个组件，里面填写的就是组件名，假如是全局注册的组件也是一样填写组件名即可

![image-20221103171922990](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319410.png)

### 2.6.2 传递数据

对于动态组件，我们可以使用`emit和prop`进行父子传递数据

![image-20221103172812038](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319029.png)

![image-20221103172924589](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319052.png)

## 2.7 keep-alive

### 2.7.1 基本使用

`keep-alive`可以让套在里面的组件被缓存起来，即便切换也会依旧存在。如下图中配合动态组件，那么动态组件都会被缓存，不会被清楚

![image-20221103211603242](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319073.png)

![image-20221103211753100](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319101.png)

### 2.7.2 相关属性

当然下面我们也可以规定只缓存那些组件，而不是所有组件都缓存，只需要在`include`中写组件名就表示该组件缓存，其他组件不缓存。这个组件名和组件中的`name`有关，而不是使用`component`注册的组件名

![image-20221103212323859](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319124.png)

当然`keep-alive`还存在其他的属性，比如下面的`exclude`就是`include`的相反，还有`max`表示最多缓存个数

![image-20221103212509445](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319162.png)

### 2.7.3 生命周期

假如需要记录`keep-alive`的生命周期的话，不能使用上面常规的生命周期函数，而是使用专门提供的`activated`和`deactivated`函数表示显示和结束

![image-20221103223143216](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319782.png)

![image-20221103223300390](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319818.png)

## 2.8 异步组件

### 2.8.1 分包文件

我们在打包之后，会发现最后会有 2 个包，第一个是`自己编写的包`，第二个是`第三方包`的，如:Vue.....。

假如是浏览器加载数据的时候，一次都请求过来再来渲染界面会很慢，所以就需要进行分包的处理

![image-20221103224219167](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319862.png)

假如我们使用`import()`函数来导入的话，就会进行分包的处理，`import()`是一个异步函数

![image-20221103224910881](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319902.png)

我们再来打包就会发现会多一个包，这个就是使用`import()`函数进行的分包处理

![image-20221103225001020](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319926.png)

### 2.8.2 分包组件

因为现在都会使用路由懒加载，所以这个用的不是很多

#### 2.8.2.1 函数写法

假如需要对组件进行分包的话和`分包文件`是一样处理，也是使用`import()`。还需要借助`Vue`提供的`definAsyncComponent`函数来创建异步组件

![image-20221103225654690](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319946.png)

我们再来打包就会发现该组件已经被分出去了

![image-20221103225845246](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319599.png)

#### 2.8.2.2 对象写法

一般都是使用`函数写法`，对象写法不是经常使用。

![image-20221103225946599](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319634.png)

## 2.9 组件的 v-model

**官方文档参考**：[组件事件 | Vue.js (vuejs.org)](https://cn.vuejs.org/guide/components/events.html#usage-with-v-model)

其实使用`v-model`的本质就是下面的`:modelValue`和`@update:model`的 2 个过程，分别是`props`和`emit`

![image-20221104090756957](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319666.png)

我们可以使用`v-model`的话就相当于上面的 2 步，在子组件中就可以直接控制父组件传入的数据

![image-20221104091112377](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319688.png)

![image-20221104091205021](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319710.png)

假如你没有编写`v-model`的名字的话，即：`v-model="num"`，那么就会需要使用`modelValue`在`props`中接收

## 2.10 mixin

### 2.10.1 基本介绍

![image-20221104091932485](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319728.png)

### 2.10.2 基本使用

我们可以使用`mixins`可以对组件中重复的选项进行抽离，比如下面就是对`About.vue和Home.vue`中相同的`data`和`created`进行抽离，这样就不需要多次书写

![image-20221104093052419](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319378.png)

### 2.10.3 合并规则

当然合并存在一定的规则，现在基本都不去使用了，因为一般都是`components API`

![image-20221104092739617](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319408.png)

### 2.10.4 全局混入

我们可以在`main.js`中使用`createApp()`的返回值`app`的`mixin`对所有的组件都进行混入，这样下面的所有组件就不需要写`mixin选项`

![image-20221104093449654](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319460.png)

# 3. 脚手架 - CompositionAPI

## 3.1 基本介绍

![image-20221104100604959](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319512.png)

> 对比 Options API

![image-20221104095227183](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319562.png)

![image-20221104095327310](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319596.png)

> setup 中不能使用 this

![image-20221104211030744](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319110.png)

## 3.2 基本使用

这样我们就不用写`data、methods...`选项了

![image-20221104101841988](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319240.png)

因为改成了函数式编程，所以我们可以将原本逻辑抽取出来直接使用即可，更加灵活

![image-20221104102152133](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319265.png)

## 3.3 响应式函数

### 3.3.1 reactive 函数

整个`reactive函数`的响应式原理在我的`JS高级`中已经写过，假如想要理解底层的话可以去看下

![image-20221104105257667](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319299.png)

### 3.3.2 ref 函数

![image-20221104110649873](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319345.png)

### 3.3.3 基本使用

下面就可以总结为`ref`为`String、Number、Boolean`数据类型使用，`reactive`的话就是`Object、Array`使用，但是在实际的开发情况并不是这样，因为`ref`也可以使用`Object`

![image-20221104105604026](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319381.png)

### 3.3.4 自动解包

我们使用`ref函数`在模板中使用就会自动解包，不需要你写`.value`。其中`reactive`的话也是一样的，可能`Vue`之前的版本的可能会存在`reactive`中的数据不解包的情况，但是截至`2022-11-4`之后的版本都没问题

![image-20221104111304625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319097.png)

### 3.3.5 对比

在实际开发中一般都是使用`ref`比`reactive`多很多

> reactive 应用场景

1.本地定义的数据。因为本地定义得需要修改，所以使用`reactive`才可以。因为网络接口传输来得值就不需要进行修改，所以使用`ref`是最好得

![image-20221104174628368](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319138.png)

2.相互有关联的数据，比如：下面的`账号和密码`，因为它们一般是一体的，所以直接定义在`reactive`中获取是最好的，假如是`ref`的话就分离的太散了，不符合逻辑

![image-20221104165130194](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319172.png)

> ref 应用场景

1.定义简单数据

2.定义网络中获取到的数据，比如：下面的网络获取到了的`arr`数组，使用`reactive`的写法就需要一个个添加，但是使用`ref`的话，直接使用`.value`传入就可以了

![image-20221104165728386](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319216.png)

## 3.4 单向数据流

### 3.4.1 基本使用

因为`vue`存在一个`单向数据流`得概念，比如说：使用`props`将数据传入给子组件，子组件修改`props`中的数据，这样会修改父组件中的数据，这样处理不是很好。当然`单向数据流`只是一个概念，你不遵守一样没问题，只是代码的维护性会很差

![image-20221104172222737](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319250.png)

![image-20221104172300099](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319286.png)

假如真得要解决得话，就需要使用`props`传入，使用`emits`来修改

![image-20221104174904113](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319831.png)

### 3.4.2 解决方法

`readonly`：让一个响应式数据变为只读的（深只读）。

`shallowReadonly`：让一个响应式数据变为只读的（浅只读）。

![image-20221104173334060](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319864.png)

假如站在`3.4 单向数据流`的案例上，这个时候就可以使用`readonly/shallowReadonly`来限制处理。假如要修改得值得话使用`emit`修改原本得值即可

![image-20221104175159384](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319903.png)

## 3.5 computed

![image-20221104221030130](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319943.png)

下面就是`computed`的基本使用方式，当然它还可以监视`ref`数据，本质和`OptionsAPI`是一样的，只不过单独抽出来为一个函数

![image-20221104221021803](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319974.png)

当然`computed`还有完整的写法，添加`set`的选择，只要修改了`fullnameAll`的话就会触发。其中`computed`的本质就是返回一个`ref()`，所以我们可以直接使用`fullnameAll.value`来修改里面的值，然后触发`set`

![image-20221104221510574](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319995.png)

这里是对于`computed`的总结：什么情况适合使用`computed`？只有在想要和数据和另外一个响应式数据有联系的话可以使用

## 3.6 ref

我们使用下面的方式来获取`ref`就可以了，其他的功能的`OptionsAPI`是一样的

![image-20221104222747246](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319758.png)

## 3.7 生命周期

![image-20221104223426884](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319782.png)

一般是先注册`setup()`，然后`setup`中的生命周期比`setup`外面的`生命周期函数`优先级要低一级

![image-20221104223057829](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319807.png)

## 3.8 侦听器

### 3.8.1 监视 ref

`watch`有 3 个参数，第一个是`监视的属性`；第二个是`回调函数`，`回调函数`里面的第一个参数是`变化后的值`，第二个是`变化前的值`；第三个参数就是`配置项`

![image-20221104230734233](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319835.png)

![image-20221104230745088](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319859.png)

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

![image-20221104232320651](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319879.png)

![image-20221104232328755](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319723.png)

假如我们需要手动停止监听的话，就需要收集`watchEffect`的返回值，在回调函数内部调用即可

![image-20221104232848304](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319743.png)

### 3.8.4 监听 props

1、在一般的业务需求中，我们需要在 **父组件中进行网络请求，然后将数据传递给子组件** ，可以参考下图的代码

2、我们网络请求之后就会将数据给 `articleData` ，响应式数据更新，那么 `props` 更新，所以监听到对应的数据，我们就可以做对应的事情，可是结果并非如此

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405072325334.png)

我们来看下为什么不是这样的，这里需要注意 2 个点

> watch 监听 props

1、我们可以查看官网的介绍，我们可以看到在 watch 一开始监听的时候是监听的 obj.count，它默认就是一个 number 类型，而非**响应式数据、getter...**，所以这里很好理解，因为外层是响应式对象，但是我们监听的知识对象中的值，所以监听无效

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405072328446.png)

2、我们再来看上述代码出现的问题：我们一开始组件创建的时候网络请求还没到，所以这里就使用的默认值 `{ }`，使用 **props.content** 监听的默认值就是普通的 `{ }` 类型，而非响应式数据类型，所以我们监听不到，即便后续网络请求来了

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405072330995.png)

3、所以这里需要使用 getter 函数来封装一下才行，也就是下述的代码

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405072335034.png)

> props 更新原则

1、第二点就是关于 props 的更新原则，其实就是**父组件更新，子组件就会将所有的 props 更新到最新的状态**，之前其实是没有理解到这一点的，我以为响应式数据传递进去就按照响应式数据状态来更新

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405072336454.png)

2、如果是上述这样的话，我们就可以略微改造代码，来实现部分的性能优化

3、在下述的代码中，`articleTitle` 默认和 `articleData` 是同步一起更新的，因为响应式数据变化就会导致组件更新，所以我们只需要设置 `articleTitle` 的值，那么 `articleData` 就会作为 `props` 传递给子组件也会同步更新到最新的值，这样就节省了一个响应式数据

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405072338698.png)

## 3.9 函数式抽取

> useCounter

以前我们在`OptionsAPI`中使用`mixin`来对代码进行抽取，但是只是对选项中的混入。假如是`CompositionAPI`的话，我们可以直接将函数式代码抽取出来，放在一个单独的文件中进行处理

![image-20221105102630021](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319763.png)

下面就是`useCounter`函数中的返回值，对代码的抽取处理

![image-20221105103000392](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319792.png)

![image-20221105103124533](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319816.png)

这个只是对`函数式编程`和`对象式编程`的思想的转变，现在`Vue`就是转变为`函数式编程`

> useTitle

点击下面的`一级按钮`和`二级按钮`对浏览器的标题进行切换

![image-20221105110110952](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319833.png)

下面的右边就是对函数逻辑的抽取

![image-20221105110048864](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319504.png)

> useScrollPosition

监视浏览器的滚动条的位置

![image-20221105110920362](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319525.png)

## 3.7 其他 API

### 3.7.1 shallowRef 与 shallowReactive

`shallowReactive`：只处理对象最外层属性的响应式（浅响应式）。

`shallowRef`：只处理基本数据类型的响应式，不进行对象的响应式处理。

![image-20221104203828738](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319545.png)

![image-20221104203850113](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319572.png)

什么时候使用？

1.`shallowReactive`：如果有一个对象数据，结构比较深，但变化时只是外层属性变化

2.`shallowRef`：如果有一个对象数据，后续功能不会修改该对象中的属性，而是生新的对象来替换

### 3.7.2 toRaw 与 markRaw

`toRaw`：将一个由 reactive 生成的响应式对象转为普通对象。

`markRaw`：标记一个对象，使其永远不会再成为响应式对象。

![image-20221104204341832](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319599.png)

什么时候使用？

1.`toRaw`：用于读取响应式对象对应的普通对象，对这个普通对象的所有操作，不会引起页面更新。还有一个就是在`watch`中假如是监听得对象，那么返回得就是`Proxy对象`，使用`toRaw`处理会更好

2.`markRaw`：有些值不应被设置为响应式的，例如复杂的第三方类库等。当渲染具有不可变数据源的大列表时，跳过响应式转换可以提高性能。

`markRaw`的本质其实就是将给属性值加上`_v_skip`属性，这样的话就跳过响应式

![image-20220619135735027](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319624.png)

### 3.7.3 响应式数据的判断

`isRef`：检查一个值是否为一个 ref 对象

`isReactive`：检查一个对象是否是由 reactive 创建的响应式代理

`isReadonly`：检查一个对象是否是由 readonly 创建的只读代理

`isProxy`：检查一个对象是否是由 reactive 或者 readonly 方法创建的代理

### 3.7.4 toRef 和 toRefs

![image-20221104205152674](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319315.png)

![image-20221104205215514](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319341.png)

因为在模板中书写`reactive`代理得对象一直书写`person.name、person.age`很不方便，所以就出现了`toRef`和`toRefs`。其中`toRefs`与`toRef`功能一致，但是`toRefs`可以批量创建多个`Ref对象`

![image-20221104205702343](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319360.png)

### 3.7.5 ref 其他的 API

![image-20221104210440358](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319385.png)

### 3.7.6 Provide 与 Inject

和`OptionsAPI`中的`provide和inject`功能基本是一样的，实现祖孙组件数据的传递。

这里这原本的`OptionsAPI`的区别就是，我们传入的是`ref`的数据，那么`inject注入`的话也会是`ref`的数据，也就是说会跟着一起响应式修改，不需要再额外写`computed`了

![image-20221104224706697](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319407.png)

![image-20221104224742368](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319425.png)

当然假如`provide`不提供数据的话，可以传入`inject()`第二个参数，这就作为默认值

![image-20221104225621428](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319134.png)

# 4. 脚手架 - Setup

![image-20221105211338871](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319160.png)

> 基本使用

![image-20221105213612872](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319187.png)

> props

1、现在使用`setup`语法糖需要使用`defineProps`来接收

![image-20221105213724254](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319216.png)

假如你不想限定类型得话，使用数组来接收也是可以得

![image-20221121184019905](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319241.png)

2、我们来看下面的代码，可以看到如果我将 `ref` 包裹一个对象，那样也会默认使用 `reactive`

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405081240238.png)

我们使用 `isReactive` 来检测一下就知道了，可以看到默认给转换为 `reactive`

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405081242049.png)

3、针对 props，你可以知道一般都会传递 type 属性，之前其实没有理解为什么传递 Number，我以为是 ts 的类型，其实是 Number 构造器

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202411101703529.png)

如果你已经编写了一个 props，需要给这个 props 自动推导类型就知道差别了，下述的 iconProps 就是要传递的对象，我们需要推导 iconProps 的类型

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202411101707066.png)

> emits

需要使用`defineEmits`来提前注册`emits`事件

![image-20221105213838938](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319290.png)

> ref

1、使用`defineExpose`来提前暴露想要暴露的数据，比如：直接使用`RefHome.value.showMessage()`来外部调用

![image-20221105213940530](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319914.png)

![image-20221105214019375](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319935.png)

2、如果我们使用 **ref** 来获取组件的 DOM 元素，如果想获取对应的 **offsetWidth、offsetTop...** 等数据，需要额外添加 **$el** 来获取

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405081633978.png)

# 5. 脚手架 - 高级语法

## 10.1 自定义指令

### 10.1.1 基本介绍

![image-20230314162731128](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319956.png)

目前存在一个需求就是，只要进入页面就自动对`input`获取焦点

![image-20230314194220643](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319984.png)

我们也可以抽取`Hook`来处理也可以，但是我们应对这种需求最好的方式就是使用`自定义指令`来处理

![image-20230314194425062](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319007.png)

### 10.1.2 局部/全局指令

> 局部指令

1、在`OptionsAPI`中使用下面的方式来获取焦点，`focus`表示指令后续使用就是`v-focus`，只要该元素挂载就会执行里面的`mounted`函数，并且会传入`el`参数也就是该元素的`DOM`属性

![image-20230314195433256](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319042.png)

2、如果在`setup语法糖`中使用的话就是按照下面的方式来处理，`vFocus函数`表示`v-focus`指令

![image-20230314195819062](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319700.png)

> 全局指令

1、我们可以在`main.js`中单独执行`app.directive`，其语法和上面的`局部指令`是一样的

2、对于`全局指令`也可以抽取指令，可以参考下图中的编写方式来处理

![image-20230314200931806](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319721.png)

### 10.1.3 生命周期

![image-20230314201840633](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319744.png)

其本质的使用是按照下面的方式来处理，和上面组件的生命周期是一样的

![image-20230314201903962](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319776.png)

### 10.1.4 指令参数/修饰符

![image-20230314213625236](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319799.png)

我们传入的`text`就是`arg`，`string、name`就表示的`modifiers`。并且因为是`JS`代码，所以里面还要写`''`来包裹起来，表示传入的是`Directive`字符串。如果你是传入的响应式数据的话，就不需要写`''`来包裹

![image-20230314204408213](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319823.png)

> 人民币转化

可能存在下面的案例，就是将数字转化为`人民币`符号，我们可以按照下面的方式来处理即可

![image-20230314210111894](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319462.png)

![image-20230314210619535](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319483.png)

> 时间格式化

![image-20230314213434912](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319505.png)

## 10.2 teleport

> 基本介绍

![image-20230314214223894](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319530.png)

> 基本使用

![image-20230314214250794](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319556.png)

> 组件使用

![image-20230314215240383](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319587.png)

> 多个 teleport

![image-20230314215306647](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319311.png)

## 10.3 suspense

> 基本介绍

![image-20230314215602570](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319339.png)

![image-20230315094514264](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319360.png)

## 10.4 vue 插件本质

![image-20230315100757822](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319388.png)

![image-20230315100807730](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319413.png)

1、我们使用插件其本质就是执行里面的`install`函数，并且传入`app`对象。或者传入函数，执行该函数

![image-20230315101201557](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319466.png)

2、并且传入的`app`对象，会在内部执行全局组件、全局对象......，使得内部进行处理

![image-20230315101406040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319146.png)

## 10.5 h 函数

### 10.5.1 基本介绍

![image-20230417213719499](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319190.png)

### 10.5.2 基本使用

![image-20230419094936018](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319228.png)

1、我们不编写`template`标签，在`OptionsAPI`中编写`render`函数返回就可以生成`DOM`

2、`h函数`就是`createVNode函数`的另外一种写法

3、`h`函数第一个是标签，第二个是属性，第三个是内容，当然第三个也可以编写为数组，这样就可以凸显层级

![image-20230418215059117](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319261.png)

4、如果我们想使用`h函数`渲染组件的话，直接传入组件即可

![image-20230418215437906](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319292.png)

### 10.5.3 计数器

1、我们可以使用模板语法来显示数字，因为`render`使用`bind`指向过`this`，所以我们可以直接使用`this.count`来获取到

2、对于绑定的事件可以在属性中编写，并且使用`onClick`作为属性名表示事件

![image-20230418215744359](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319320.png)

### 10.5.4 组合式 API

> 基本使用

![image-20230419094707345](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319217.png)

> setup 语法糖

![image-20230419094809096](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319241.png)

## 10.6 JSX

1、我们这里使用`vite`环境来搭建

![image-20230419095653181](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319296.png)

2、首先我们需要安装`jsx`的`babel`的插件，`npm i @vitejs/plugin-vue-jsx -D`

3、在`vite`中的`plugin`中配置即可，对于`webpack`也是一样的

![image-20230419095937555](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319337.png)

4、下面实现了一个计数器的按钮，还实现了一个`map`遍历的案例，其基本你的代码和`React`是差不多的，对于`JSX`的语法直接查看`React`的笔记即可

5、其基本的规则在`h函数`中都介绍了，下面只写了 2 种编写方式，对于非`setup语法糖`的内容可以参考上面的

![image-20230419101210629](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319365.png)

## 10.7 动画

### 10.7.1 基本介绍

![image-20230422150245440](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319394.png)

### 10.7.2 基本使用

1、其实`Vue`为动画所作的工作就是为下面的元素添加`v-enter-from`、`v-leave-to`......等类名，而不是`Vue`帮忙我们实现动画

![image-20230422150821609](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319154.png)

2、使用`Transition`对想要实现动画的标签进行包裹，在`css`中编写动画效果即可，达到一个阶段`Vue`就会自动添加上类名

![image-20230422150333857](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319179.png)

我们截图就可以看到`Vue`添加`class`的时机

![image-20230422150711427](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319219.png)

3、`Vue动画`实现的效果

![[00 assets/8b8dbd780fca61e3897723245f516474_MD5.png]]

### 10.7.3 过渡动画 class

> 过渡动画 Class

![image-20230422151448349](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319277.png)

> Class 添加时机和命名规则

![image-20230422151708185](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319301.png)

### 10.7.4 animation 动画

![image-20230422151950154](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319045.png)

1、下面是对`animation`动画的基本使用

2、如果我们使用这个形式的动画的话，`Vue`就会自动嗅探之后再来添加`text-enter-active`或者`text-leave-active`

3、如果我们写一个`50%`的话，就会导致动画运行到一半的时候卡一下，表示动画已经运行到`50%`。如果你不想卡这一下的话，直接写`0%`和`100%`就行了

![image-20230422152602211](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319078.png)

### 10.7.5 动态组件切换

1、这个就是动态加载组件的操作，和前面的元素之间的切换始是一样的

![image-20230422152602211](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319078.png)2、因为这里直接使用的`setup语法糖`，所以我们需要添加`:`将里面的代码变为`js代码`，将组件传入就可以动态加载组件了

![image-20230422161612624](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319110.png)

### 10.7.6 动画属性

#### 10.7.9.1 appear 属性

![image-20230422161849392](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319133.png)

#### 10.7.9.2 type 属性

1、首先我们需要知道`transition`和`animation`动画是可以叠加的，最后实现的效果是一样的

![image-20230422154610172](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319161.png)

2、首先`Vue`会自动监听元素动画的变化，自动选择时间最长的动画执行

3、但是对于自动选择我们可能不是很满意，需要自己手动来调整，这个时候就可以使用`type`属性来指定监听的类型。但是在实际项目中最好不要去这样处理

![image-20230422154736968](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319185.png)

#### 10.7.9.3 durations 属性

1、我们可以手动设置动画时长，也就是和上面的`type`一样，在实际项目中尽量减少使用的次数

![image-20230422155105214](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319024.png)

#### 10.7.9.4 mode 属性

1、我们按照下面的方式来设置元素的显示和隐藏的话就存在问题，2 个元素同时存在，并且都在执行动画。

![image-20230422155610146](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319044.png)

![image-20230422155515301](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319066.png)

2、为了解决这个问题，就存在`mode属性`来处理这个问题

![image-20230422155441054](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319094.png)

我们使用`out-in`表示先执行`离开动画`，然后再来执行`进入动画`

![image-20230422155755005](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319119.png)

### 10.7.7 列表动画

![动画88](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319146.gif)

1、对于多个元素的动画添加可以使用`TransitionGroup`动画组，下面是官方中对`TransitionGroup`的介绍

![image-20230422172214745](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319836.png)

2、下面中插入数据的话就会触发`.list-enter-from`.....动画，移出也是一样会触发动画，这里就过多的赘述

3、我们插入数据之后，需要将后排的数字向旁边移动。这个动画的实现我们使用`.list-move`来处理，里面添加动画的属性即可

4、但是移除数字会因为动画还没执行完，所以元素会一直占据在原位，移动动画即便执行了也不会移动，所以我们给移除的元素添加`position:absolute`属性，让它脱离文档流

5、对于打乱数组的方法，我们使用`underscore`库来处理。我们下载`npm i underscore`，使用`shuffle`函数来打乱数组

![image-20230422171810187](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319855.png)

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

# 6. 前端路由 - VueRouter

## 5.1 基本介绍

> 基本介绍

![image-20221106203430629](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319877.png)

> 后端路由阶段

![image-20221106205204498](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319900.png)

> 前后端分离阶段

![image-20221106205418166](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319936.png)

> 单页面富应用

![image-20221106205511015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319971.png)

## 5.2 路由原理

使用下面得 2 种方式是实现路由得原理，在 URL 改变得情况下不刷新页面

> URL 的 hash

![image-20230224103229716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319660.png)

> HTML 的 History

![image-20221106205712385](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319684.png)

## 5.3 基本使用

### 5.3.1 基本流程

下面只是展示基本配置基本流程

> 下载

```bash
npm i vue-router // 下载vue路由
```

> 使用

![image-20221106214207380](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319715.png)

下面就是使用`路由`得一整套流程，可以参考上面得流程图来配置`Vue-Router`

![image-20221106215154413](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319738.png)

### 5.3.2 history 模式

假如你使用`Hash模式`得话，前面会多一个`#/`得符号来区分后面得地址。但是使用`History模式`就不会存在

![image-20221106215450685](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319763.png)

我们这里使用`router`中得`history`来配置

![image-20221106215632431](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319805.png)

### 5.3.3 router-link

![image-20221106220311231](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319546.png)

> to 属性

可以使用 2 种方式来配置`to属性`

![image-20221106220508432](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319571.png)

> replace 属性

也就是**覆盖**上一条记录，点击浏览器得返回按钮就回不到上一条记录

> active-class

原本我们点击`routerlink`得时候会有类名`router-link-active`在按钮之间跳转，表示点击了那个`router-link`，但是这个`class`可能不是很好，所以我们可以使用`active-class`来修改这个类名

![image-20221106220700135](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319593.png)

### 5.3.4 路由懒加载

![image-20221107103151055](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319625.png)

我们使用`import函数`来对`路由`中得组件进行懒加载得操作，这样在打包得时候就会分包处理

![image-20221107103412808](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319649.png)

下面就是打包的效果，其中前面是`About.86...`就是名为`About`的包

![image-20221107111159674](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319670.png)

## 5.4 获取参数

> 2023.9.23

最近在做项目的时候发现了下面的`params`和`query`使用上的一个区别，因为`params`在路由上需要添加`/:id`来表示当前占位，如果没有这个路由就会跳转不到，但是`query`不需要也可以

在后端返回动态路由的时候，可能有的时候是不带有`:id`这类的`params`的参数，所以我们可以采取使用`query`来替代

![image-20230923224234016](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319281.png)

### 5.4.1 params

![image-20221107111424532](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319305.png)

下面就是获取参数的方式

![image-20221107111700836](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319326.png)

假如我们要获取的话和下面的`query`是一样的，只需要在`route.params`中获取即可。并且这里需要注意一个`router`和`route`的区别，其中`router`是获取实例的，但是`route`是获取当前地址

### 5.3.2 query

我们可以使用`编程式导航`传递`query参数`，假如需要获取的话，就使用`$route.query`来获取

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405061510971.png)

其实我们在这里传输`query`，并且取出该数据和上面的`params`是一样的处理方式

![image-20221115115134642](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319382.png)

## 5.5 NotPage 处理

当匹配不到任何路径的情况下，可以使用`/:pathMatch(.*)`来将路由指定到`NotFound页面`

![image-20221107122019456](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319451.png)

下面就是在后面添加`*`来区别解析的方式

![[00 assets/9f00d88f4996677f38ac11606dd860ea_MD5.png]]

## 5.6 编程式导航

下面是基本的使用，我们使用`push`的方式来进行跳转，进行手动跳转

![image-20221107150832631](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319148.png)

其中`向前向后`的跳转就是下面的`go、back、forward`

![image-20221107150338695](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319167.png)

## 5.7 动态管理路由

这个技术一般是在`管理后台`来做，因为需要区分`管理员、服务员....`得身份，因为以前都是直接通过隐藏路由得方式来处理，这个方法很不好，所以我们可以通过下面动态添加路由得方式来处理，这样管理员就不能通过`url`控制栏相互跳转

下面得方式就是动态管理路由得一个思路，其中`isAdmin`是后台传输过来得，来动态管理权限

![image-20221107170731390](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319184.png)

我们使用下面得`3种方式`来对路由进行管理，但是不是经常使用

![image-20221107170442025](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319211.png)

## 5.8 路由守卫

路由守卫主要是使用`beforeEach()`。该函数还有 2 个参数，第一个参数是`去哪里`，第二个参数是`从哪里来`

![image-20221107194246622](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319237.png)

下面就是路由守卫在`beforeEach`中得返回值不同，可以达到不同得效果

![image-20221107194427752](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319955.png)

下面是完整得导航解析流程

![image-20221107204358265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319977.png)

# 7. 状态管理 - vuex

## 6.1 基本介绍

> 什么是状态管理？

![image-20221107205750840](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319001.png)

> 复杂得状态管理

![image-20221107210100570](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319059.png)

> 状态管理流程

![image-20221107211735173](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319086.png)

## 6.2 State

### 6.2.1 基本使用

![image-20221107215808744](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319109.png)

```bash
npm i vuex // 下载vuex
```

下面为基本的使用，通过`store.commit()`来发送一个`commit`给`store仓库`，仓库对数据进行处理

![image-20221107221627054](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319773.png)

其中在`模板语法`中展示数据，可以使用下面的 3 种方式

![image-20221107221933230](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319799.png)

### 6.2.2 状态映射

因为在模板语法中一直使用`$store.state.xxx`来显示数据，这个写的很麻烦，所以需要状态映射。

当然这个状态映射不仅仅是`store`，还有`actions和mutations`

> optionsAPI

![image-20221107222518953](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319818.png)

> compositionAPI

方式一：自己封装函数，返回`computed`数据。

使用下面封装函数的原理其实是因为使用`mapState`的话，返回的是函数，其中执行的其实是`this.$store.state.xxx`，因为`setup()`里面没有`this`，所以就需要动态绑定`this`来处理，所以就有了下面的封装函数

其中为了能在模板中直接书写，所以就需要使用`computed`来编写

![image-20221107225059164](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319841.png)

方式二：使用`toRefs`来处理（**推荐**）

![[00 assets/c2af3a45df9819eb14532fb544c7b461_MD5.png]]

## 6.3 Getters

### 6.3.1 基本使用

我们在`store`中添加`getters`，专门将处理之后的`state`返回出去，可以理解为`computed`

![[00 assets/b24b36658c6374bf8be38252ed58884c_MD5.png]]

![image-20221108095930063](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319779.png)

其实在`getters`中可以返回一个函数，

![image-20221108095958913](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319795.png)

### 6.3.2 Getters 映射

> optionsAPI

![image-20221108101011145](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319815.png)

> compositionAPI

**方式一**：使用`toRefs`处理，和`State`得处理方式差不多，虽然方便，但是控制台会报警报，所以这个还是比较推荐使用封装函数的方式处理

![image-20221108101954954](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319841.png)

下面就是报错的提示

![image-20221108105523166](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319870.png)

**方式二**：下面为封装的处理，和`State`是差不多的

![image-20221108102244114](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319889.png)

## 6.3 Mutation

### 6.3.1 基本使用

首先要知道为什么修改参数需要使用`store.commit`的方式，是为了`Vue插件`可以实时的追踪数据的改变

下面就是基本的使用，我们使用`commit`的方式提交一个命令，给`mutations`中的函数进行执行。当然我也可以携带参数来处理

![image-20221108110757199](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319547.png)

当然我们使用`mutations`有一个设计规范，就是将方法都抽取到一个单独的文件里面

![image-20221108131116325](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319569.png)

### 6.3.2 Mutation 映射

> optionsAPI

![image-20221108131456532](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319587.png)

> compositionAPI

封装的本质和上面的`State`是差不多的

![image-20221108131950268](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319613.png)

### 6.3.3 注意事项

![image-20221108132604396](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319639.png)

## 6.4 Actions

### 6.4.1 基本使用

![[00 assets/bef3d2d4bd2991836f67b8b6055ceb84_MD5.png]]

下面就是基本的使用，我们首先需要使用`store.dispatch`来对`Action`进行控制，然后`action`中发送命令给`mutations`处理，然后再来操作`state`

![[00 assets/e3d818eecd356706fed28690f1fdc76d_MD5.png]]

### 6.4.2 Actions 映射

> optionsAPI

![image-20221108171001672](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319391.png)

> compositionAPI

![[00 assets/a94f4c2059f38c2b75d3687f0308f369_MD5.png]]

### 6.4.3 网络请求

当然有 2 种网络请求方式，一个是使用`vuex`来处理网络请求，这个是将网络请求的方式抽取出来。还有一个而方式就是在组件中发送请求和管理数据。这个是 2 套不同的处理方式。

下面就是使用`vuex`来发送网络请求的一整套流程，需要在组件中发送一个`dispatch`。然后在`actions`中发送网络处理，然后发送命令给`mutations`，然后`state`来存储

![image-20221108195903967](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319438.png)

![image-20221108200851469](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319468.png)

当然我们想要监听该函数是否完毕的话，需要使用下面的`new Promise()`来处理

![image-20221108201435107](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319506.png)

## 6.5 Modules

### 6.5.1 基本使用

![image-20221108204140113](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319164.png)

下面就是整个`modules`的使用，我们将`home`的数据抽取到外面，在`index.js`中使用`modules`进行导入

最后使用的时候记得要加上`modules`的名字，比如下面使用`modules`来导入的时候加上了`home`，那么最后取出的时候就需要使用`store.state.home`来处理。当然默认情况下，使用`state`需要拼接，但是使用`actions、mutations、getters`是不需要使用的

![image-20221108203931870](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319185.png)

在`getters、actions`中存在第三个参数`rootState`，这个就是`根状态库`中的所有`state`。其中第二个参数`getters`十所有的`getters`，因为没有设置命名空间，所以都是混在一起处理的，直接使用`state.getters.xxx`就可以使用

![image-20221108214652093](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319211.png)

![image-20221108214608050](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319240.png)

### 6.5.3 命名空间

![image-20221108220934633](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319265.png)

我们可以将`namesepaced`设置为`true`的方式处理，设置命名空间，这样需要取出`doublenum`的话就需要使用`[name/doublenum]`处理

![image-20221108220809703](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319294.png)

### 6.5.3 module 中派发

![image-20221108221111284](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319097.png)

# 8. 状态管理 - pinia

## 7.1 基本介绍

> 基本介绍

![image-20221108223259188](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319116.png)

> 对比

![image-20221108224130586](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319139.png)

> Store 基本介绍

![image-20221108231738365](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319171.png)

> 定义 Store

![image-20221108232123036](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319197.png)

## 7.2 State

### 7.2.1 基本使用

首先是在`Vue`中注册`pinia`，这里就是第一步和`vuex`不一样，这里不需要直接在`createPinia()`中书写对象来处理数据

![image-20221108230453856](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319221.png)

下面就是使用`State`，需要使用`defineStore`来创建仓库，第一个参数可以理解为`vuex`的`namespaced`，作为唯一的`id`。假如需要使用这个仓库的话直接导出使用即可

![image-20221108230943179](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319928.png)

下面为整体的结构流程图

![image-20221108230234366](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319948.png)

当然假如我们感觉直接写`counterStore.count`还是很麻烦的话，也可以使用解构来操作，但是直接使用解构的话可能会丢失原本的响应式，所以`Vue提供的toRefs`，或者直接使用`pinia提供的storeToRefs`

![image-20221108233027950](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319967.png)

### 7.2.2 操作 state

我们可以直接使用`countStore.xxx`来操作数据，因为它返回来的数据是响应式的。我们使用解构之后会在外面套一层`storeToRefs`，将它变成`refs`的响应式，所以改变需要使用`xxx.value`来处理

![image-20221109085332860](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319987.png)

> $reset

可以重置数据，将数据变为原来的样子

![image-20221109085553754](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319018.png)

> $patch

一次修改多个值

![image-20221109090444703](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319040.png)

> $state

累加数据进入`state`。但是官网记录的是替换数据，不是很准确

![image-20221109091056901](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319854.png)

## 7.3 Getters

我们可以使用下面的 2 种方式来调用。第一种是直接使用`countStore.xxx`调取，第二种是使用`解构`的方式来调取

![image-20221109093804331](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319874.png)

当然还有一些其他的用法，比如下面的`返回一个函数`和`使用其他store在的数据`

![image-20221109094216332](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319903.png)

![image-20221109094506662](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319931.png)

## 7.4 Actions

### 7.4.1 基本使用

我们可以直接调用里面的`Actions`，其中`Actions`不带有类似于`State`的默认参数，需要的数据直接使用`this.xxx`就可以了

![image-20221109095710647](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319950.png)

### 7.4.2 网络请求

在`actions`中也是支持异步请求的，可以在里面发送网络请求，使用异步函数处理，基本的使用方式和`vuex`中的`actions`的网路请求是一样的

![image-20221109101145972](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319977.png)

当然我们还可以在添加`then`来监听请求的结束，但是它返回的值是`undefined`

![image-20221109101340139](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319875.png)

假如你觉得返回`undefined`不是很好得话，可以自己返回`Promise()`来处理

![image-20221109101719463](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319899.png)

# 9. 网络请求 - Axios

## 8.1 基本介绍

![image-20221109104708527](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319918.png)

> 请求方式

![image-20221109104745467](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319947.png)

> 配置选项

![image-20221109104822238](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319969.png)

## 8.2 基本使用

```bash
npm i axios 	// 下载axios
```

> request

![image-20221109111253585](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319994.png)

![image-20221109111306186](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319777.png)

> get

第二个参数就是填写配置信息

![image-20221109111343315](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319798.png)

![image-20221109111351001](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319847.png)

> post

![image-20221109111526750](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319893.png)

当然我们也可以直接将第二个参数作为配置选项，假如需要写入`data`的话，直接编写`data`的对象就可以了

![image-20221109111545437](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319922.png)

![image-20221109125437876](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319944.png)

> 公共配置

当然我们也可以使用`axios.default.xxx`来配置一些公共配置

![image-20221109130340186](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319503.png)

## 8.3 发送多个请求

当然我们可以一次发送多个请求，当这些请求都成功之后会返回一个`成功的Promise`

![image-20221109130446178](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319523.png)

![image-20221109130430292](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319545.png)

## 8.4 创建实例

![image-20221109131026795](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319564.png)

我们可以编写多个`axios`实例来处理不同的网络请求

![image-20221109130925004](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319591.png)

## 8.5 拦截器

下面就是设置`拦截器`，其中`axios.interceptors.request`就是`请求拦截器`，`axios,interceptores.response`就是`响应拦截器`，当你请求或者响应的时候都会先走这个拦截器处理。在这个拦截器里面可以进行`loading`动画的加载、数据处理......

![image-20221109204953590](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319671.png)

![image-20221109205257342](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319307.png)

## 8.6 axios 封装

下面是对`axios`简单的封装，假如需要进一步封装的话可以根据项目的实际情况来

![image-20221109231426424](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319330.png)

# 10. 前台项目 - 弘源旅途

## 9.1 前期准备

### 9.1.1 划分结构

我们先优先划分结构，一般是按照下面的结构来处理项目

![image-20221110212154662](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319354.png)

### 9.1.2 代码提示

这个主要是为了给`vscode`的提示使用的，一般使用`vite`创建的项目可能没有这个文件，假如需要的话可以将这个文件添加进来

![image-20221110212250077](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319385.png)

### 9.1.3 重置 CSS

一般我们会使用`normalize.css`来重置不同浏览器的样式问题，需要使用的话直接在`webpack`中打包即可

```bash
npm install --save normalize.css
```

当然我们不仅仅需要`normalize.css`，我们还需要添加`reset.css`来重置一些样式。还有`common.css`表示一些属性共有的样式。并且最后怕样式都在`main.js`中引入会导致浏览混乱，所以创建一个`index.css`来专门引入

![image-20221110213605864](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319410.png)

### 9.1.4 路由配置

先来看项目，首先最重要的就是下面的`tarbar`页面。其中包含了 4 个主要页面，所以我们先来配置路由

![image-20221110215922505](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319451.png)

1.简单配置路由，因为这几个页面都是主要的页面，所以要优先创建

![image-20221110220040259](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319124.png)

2.当然这里创建`Views`中的项目也是有讲究的，一般这种主要的视图都是创建一个文件夹表示。而且文件夹中的文件都是不一样的，存在下面的 2 种写法，有`home.vue`和`index.vue`的 2 种形式

![image-20221110220411699](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319147.png)

### 9.1.5 状态管理

先进行基本的配置

![image-20221110225212946](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319167.png)

对于其他组件中的状态管理可以放到`modules`中来处理

![image-20221110225257899](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319194.png)

## 9.2 页面搭建

接口地址：[HYTrip (getpostman.com)](https://documenter.getpostman.com/view/12387168/UzXPxcSi)

### 9.2.1 \*tabbar - 手动封装/动态引入资源

> 手动封装

我们需要制作下面的`tabbar`页面，对其进行处理

![image-20221110215922505](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319451.png)

1.首先我们来搭建页面结构，这个页面结构的`CSS`非常的清晰，所以这里截图参考一下。

​ 1.1 首先是定位，这里使用了`fixed`定位，基于浏览器来定位的，只要`bottom`为`0px`的话就会默认在底部

​ 1.2 另一个就是图片和文字的垂直排列，这里使用的是`flex布局`，一个思路就是更改排列方向`flex-direction`

​ 1.3 对于图片来说，因为图片本身是长方形，所以这里直接设置宽度，不去设置高度，让浏览器来动态设置

![image-20221111092150072](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319222.png)

当然对于颜色我们可以设置变量，其中`CSS`就存在变量的语法。这样`.Tabbar .TabbarItem.active`就会设置变量里面的颜色

![image-20221111105328665](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319278.png)

2.因为对于`tabbar`来说数据都是固定的，所以这里将数据动态抽取到一个文件中处理，以后方便处理

![image-20221111094749112](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319920.png)

3.因为图片的地址是动态加载的，所以可能会加载不出来导致报错。在`webpack`中一般是使用`require()`处理，假如是`vite`的话可能需要编写一个函数来处理

![image-20221111100341383](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319949.png)

其中`new URL()`是动态拼接地址的，其中第一个参数是`相对路径`，第二个参数是`当前路径的URL`。最后对路径进行拼接处理来获取

![image-20221111091535097](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319971.png)

4.因为后续会有很多获取本地图片的处理，所以这里将这个方法抽取到一个文件中，需要用的时候直接调取就可以

![image-20221111102612743](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319998.png)

5.编写逻辑代码

![image-20221111105506823](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319025.png)

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

![image-20221122102749293](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319055.png)

但是这里存在一个小的问题，就是路由改变了，但是底部的`tabbar`并不会变，这是因为这是通过`currentIndex`来驱动的，只要`currentIndex`不改变的话就不响应

1、其中对于使用它原生的图标的话，可以添加上`route`来处理

![image-20221122115648241](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319818.png)

2、但是我们这里使用的是自己定义的图标，并不会自动跳转。所以就需要按照下面的方式来监听处理

![image-20221122115815537](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319842.png)

### 9.2.2 vant 引入

#### 9.2.2.1 按需引入

```bash
npm i vant   // 安装vant
```

对于这种项目直接全部引用的话，可能会导致包体积增大，所以这里采用的是按需引用的方式。

这里有一个坑就是关于官网的问题，对于`vant`来说网址比较多，所以建议直接查询和当前版本相同的官网。官网网址：[快速上手 - Vant 3 (gitee.io)](https://vant-contrib.gitee.io/vant/#/zh-CN/quickstart)，下面就是按需引入组件，但是需要下载相应的插件

![image-20221111164159345](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319864.png)

我们按照上面的操作下载插件的话，就不需要自己来写按需引入的代码，直接写组件就可以了，`vite`会自动添加组件

![image-20221111233024607](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319889.png)

#### 9.2.2.2 vant 替换

我们这里直接使用`vant组件`来替换以前的`tabbar`代码，是不是就简洁很多，直接使用即可。

![image-20221112122918878](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319913.png)

#### 9.2.2.3 样式修改

1.因为这里使用的插槽，并且写的是自己的元素，所以这里可以直接修改

![image-20221112123530716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319940.png)

2.使用`CSS变量`属性，下面的是在全局中进行修改，在官方文档中就有介绍

![image-20221112123922564](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319611.png)

假如我们不想全局修改的话，就需要写在对应的类中

![image-20221112124031757](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319632.png)

当然可以根据浏览器的控制台中的属性来修改

![image-20221112124249193](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319652.png)

3.直接根据控制台找到它的类并修改，但是这种方式不一定生效，因为存在样式作用域

![image-20221112124953663](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319678.png)

首先`tab-bar`是作为一个单独的文件来处理，其中`van-tabbar-item`也是作为一个单独的文件来处理，因为存在样式的作用域所以根本不生效

![image-20221112125032330](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319704.png)

这里存在 2 个方法来处理，其中第一个就是删除`style`中的`scoped`，但是不是很推荐；另一个方式就是使用**样式穿透**，这样就可以修改子组件中的样式

![image-20221112125448530](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319723.png)

### 9.2.3 city 开发

大致开发成这个样子

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319384.png" alt="image-20221113172712572" style="zoom:67%;" />

#### 9.2.3.1 获取地址

对于浏览器原生来说可以直接获取到地址，但是误差很大。假如真的要在网页中做位置获取的操作，建议使用百度`API`来调用

![image-20221112191534465](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319398.png)

这个获取地址在`谷歌`中是获取不到的，但是在`edge`是可以获取到的。其实是因为它们之间实现的原理不一样，对于`谷歌`来说，是将你网络的`IP地址`上传到它的服务器，然后来返回地址的，但是对于`edge`来说，是获取你电脑当前的定位来处理的

下面是是`W3C`的中对于`geolocation`接口的介绍（[Geolocation API (w3.org)](https://www.w3.org/TR/geolocation/)），其中`geolocation`是实现的一个高等级的接口，所以`W3C`在定义这个接口的时候只是定义了这个接口，但是不关心这个接口是怎么实现的，所以就出现了相同的代码中`edge`是获取的到定位的，但是在`谷歌`中就获取不到的情况，这个就是因为接口都是一个接口，但是实现的原理不同

![image-20221115110507272](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319419.png)

#### 9.2.3.2 隐藏 Tabbar

因为一些界面不需要显示`tabbar`，所以这里需要对一些界面进行特殊的处理

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319438.png" alt="image-20221112194404028" style="zoom: 50%;" />

> 1.

我们可以在要隐藏的路由中设置`meta`信息，这样我们使用`useRoute()`可以直接获取到，假如不设置`meta`的`hideTabbar`的话就默认是`undefined`为`false`，所以这里我们设置的`hideTabbar`为`true`

![image-20221112193151940](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319457.png)

这里需要注意`useRouter`和`useRoute`的区别，我们使用`useRoute`获取到当前的路由地址

![image-20221112193403743](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319481.png)

> 2.

或者使用`CSS`的方式来隐藏，其原理就是将让设置的盒子盖在原本的`tabbar`上面就可以了

![image-20221112194318472](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319079.png)

#### 9.2.3.3 搜索栏和 tab 栏

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319105.png" alt="image-20221112225127696" style="zoom: 80%;" />

下面就是开发`搜索栏`和`tab`栏，这里就是使用的`vant`来开发的

![image-20221112224846017](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319128.png)

#### 9.2.3.4 网络请求

下面就是对`网络请求`的基本封装，我们一般是单独设置一个文件夹专门封装`axios`，其中`config.js`是填写配置

![image-20221112235956884](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319161.png)

当然对于其他的网络请求的`接口`，也是单独放置在`modules文件夹`中，来统一接口。为了方便请求，所以我们也会单独设置一个`index.js`来导入所有的接口，这样我们在其他文件导入接口的时候只需要关心接口名就可以了

![image-20221113000259988](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319192.png)

#### 9.2.3.5 数据封装

我们对于网络请求来的数据一般都是直接使用`pinia`的`actions`来处理的，这样让数据更加统一

![image-20221113002037647](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319226.png)

#### 9.2.3.6 搜索栏和 tab 栏定位

因为搜索栏和 tab 栏下面是信息流页面，所以上面需要固定。实现这个效果有 2 个方法

![image-20221113102913779](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319945.png)

> 1

我们这里使用`fixed`定位的方式来处理，其中一个就是需要将内容手动的往下调整，比如：`margin-top:98px`

![image-20221113103032190](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319964.png)

还有一个就是滚动条的处理了，你会发现这个滚动条会对整个页面进行滚动，处在搜索栏的位置

![image-20221113102842280](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032319987.png)

> 2

还有一个方式就是使用下面的方式来处理

![image-20221113104002080](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320018.png)

就不会存在上面出现的问题

![image-20221113104056372](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320043.png)

#### 9.2.3.7 citygroup 动态数据

1.首先第一个难点就是关于`van-tabs`中数据切换时，使用的是索引值，所以我们很难选中对象中的值，所以这里我们使用`vant`提供给`van-tab`的属性值`name`来处理

![image-20221113110029265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320072.png)

其中`citylist`是对象值，其格式大概是这种格式

![image-20221113110148928](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320687.png)

我们将对对象遍历的`key`传输给`van-tab`的`name`就可以了

![image-20221113110105468](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320718.png)

2.我们实现了切换之后获取到对象的`key`值，还有一个问题就是我们取出的数据不是响应式的，因为`cityList.value[tabActive.value]`本质就是对象的取值，并不是`Proxy`，所以这里会丢失响应式。

这里的解决方法就是使用`computed`，或者在`模板语法`中使用也可以

![image-20221113110300688](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320738.png)

#### 9.2.3.8 citygroup 数据展示

这里直接使用的`vant`中提供的`indexbar`来处理

![image-20221113140615610](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320762.png)

下面就是展示的过程，这里做了一个优化，因为一开始是将所有的列表数据都传输进去了，所以切换的时候渲染速度很慢，所以我们一开始就将所有数据都展示处理，通过`v-show`来控制显示和隐藏，这样切换的话会流畅很多

![image-20221113140702903](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320786.png)

#### 9.2.3.9 热门城市展示

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320811.png" alt="image-20221113171313817" style="zoom: 67%;" />

下面为热门城市的`CSS`，这个主要是考验的`CSS`的编写

![image-20221113171237212](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320393.png)

#### 9.2.3.10 索引栏问题处理

因为这里多加了一个`热门`，所以索引栏无法正确定位到数据

![image-20221113172338854](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320418.png)

所以我们这里需要使用到`index-list`属性来重新定义一个动态的`索引栏`

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320438.png" alt="image-20221113172319072" style="zoom: 67%;" />

我们这里使用`computed`来处理这里动态展示数据的要求。这里的索引主要是依靠`van-index-anchor`来处理，不是按照里面的`index`来对应，而是个数来处理

![image-20221113172526395](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320468.png)

#### 9.2.3.11 选择城市回退

当你选择了城市之后回退到首页

![image-20221113174313159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320504.png)

因为`currentCityInfo`的数据在后面的每个页面都可能使用，所以我们这里将数据存储到`pinia`中

![image-20221113174236244](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320540.png)

#### 9.2.3.12 热门建议处理

我们需要实现下面的功能

![image-20221115123300249](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320170.png)

这里面对于网络请求的部分，我就不展示了。这里主要是`CSS`样式的问题，我们使用下面的`overflow-x`可以自动展示一个`x轴`滚动条

![image-20221115123550740](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320188.png)

### 9.2.4 box 开发

#### 9.2.4.1 动态显示时间

我们这里直接使用`dayjs`来处理时间，对于当前时间加一天的操作可以参考`nowDate.setDate(nowDate.getDate) + 1`就可以了，或者使用`getTime()`来获取时间戳再加上`24 * 60 * 60 * 1000`处理

![image-20221113204407678](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320209.png)

#### 9.2.4.2 使用 van-calendar

我们可以`vant组件`中的`calendar`来处理，下面就是配置的信息

![image-20221113213207173](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320232.png)

#### 9.2.4.3 计算时间之差

我们使用`dayjs`来处理时间之差

![image-20221113213421177](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320300.png)

#### 9.2.4.4 热门建议

这里我们将网络请求和状态管理封装到`service`和`store`中

![image-20221114085204956](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320324.png)

#### 9.2.4.5 搜索按钮处理

点击之后跳转页面，并且将数据通过路由传输过去，这个其实很简单。但是对于`views`文件夹，这里有一个创建规则，只要你新建了一个页面，那么这里就要多创建一个文件夹

![image-20221115120641096](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320024.png)

#### 9.2.4.6 房间首页请求

我们使用下面的方式来对房间中的数据进行请求

![image-20221115170414432](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320048.png)

#### 9.2.4.7 房间首页展示

实现下面得 2 种房间首页得装饰，其中`9`表示左边得全局，`3`表示右边得一半

![image-20221121215922486](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320071.png)

下面是`3`表示得`HTML结构`布局

![image-20221121220108973](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320101.png)

因为存在超过盒子得宽度就显示`...`得功能，可以使用下面得方式来处理

![image-20221121220353804](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320121.png)

还有一个显示评分得功能，因为整个评级只需要传输进去值，因为我们这里使用得是组件，所以需要使用到`组件v-model`

![image-20221121220608393](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320154.png)

假如为了节省性能得话可以是下面得方式来设置评级处理得分数，这里可以参考我得`组件v-model`得笔记，默认是`props`和`emit`得处理，其中``props`默认传入得值就是`modelValue`，这样就只实现了单向绑定，节省了开销

![image-20221121220556337](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320955.png)

#### 9.2.4.8 滚动条 hook 抽取

下面就是整个`hook`得抽取，这个是完整版得。可以通过传递`参数elRef`得形式来决定是否为`window`或者`elRef`。

最后是通过返回一个参数`isReachBottom`得方式来判断是否到达底部，这是一个很重要得思想，其中你想实现得逻辑通过`hook`外部得文件来处理，这个封装`hooks`只是一个监听得作用，不承担其他职责，所以返回一个值处理逻辑

![image-20221122094413417](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320970.png)

当你获取到返回得`isReachBottom`的值，对其进行监听处理，只要发生改变就发送请求

![image-20221122100844626](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320994.png)

因为监听的情况很频繁，所以我们可以使用`throttle`来处理

![image-20221122101656228](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320023.png)

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

![image-20221122161300911](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320052.png)

这样搜索栏也可以自动的更新来显示数据

![image-20221122161514084](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320074.png)

### 9.2.5 Loading 开发

#### 9.2.5.1 组件封装

1、首先作为一个`Loading`组件肯定需要重新封装作为一个组件来使用的

![image-20230309193136720](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320750.png)

2、我们对于样式的处理，这里存在一个小技巧就是`position`为`fixed`，并且`left、right、top、bottom`要都为`0`，这样的话就会同时占用全部页面，而不需要设置`width:100%......`属性

![image-20230309193226129](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320772.png)

#### 9.2.5.2 状态控制

1、作为一个`laoding`的页面，其状态的控制和其他的所有页面都有关系，所以其状态控制最好时定义一个全局的变量`store`中，前面我们定义了一个`mainStore`来存储全局控制的变量。我们现在依旧在这里定义

![image-20230309195545256](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320796.png)

2、因为这一类的状态控制都是网络请求的，所以这个状态控制编写的最优解就是编写在网络拦截器中，只要请求发出的话，就显示`Loading`，如果响应结果的话就关闭`Loading`

![image-20230309195819374](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320819.png)

![image-20230309200011165](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320857.png)

### 9.2.6 房间详情页

#### 9.2.6.1 基本搭建

1、我们在首页点击了房间的信息，就需要跳转到房间的详情页

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320898.png" alt="image-20230309203302211" style="zoom:67%;" />

2、首先我们先搭建页面，这里取名为`detail`

![image-20230309203323764](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320885.png)

然后就需要配置路由，并且需要传入`id`的参数

![image-20230309203411839](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320909.png)

3、其中房间的`Item`要进行事件绑定，并且我们直接在组件中编写`@click`其本质是传入给`homeItemV9`的根标签进行处理了，所以这个组件存在 2 个根标签就需要做其他处理了

![image-20230309203454555](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320937.png)

跳转之后，进行路由参数解析即可

![image-20230309203726842](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320962.png)

#### 9.2.6.2 导航栏搭建

![image-20230309205733159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320981.png)

使用`vant`组件库中的导航栏，并且我们可以使用`--van....`来调节该组件的颜色，这里的修改可以参考我`9.2.2 vant引入`的处理

![image-20230309205722585](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320003.png)

#### 9.2.6.3 网络请求

房间详情页的整体都使用组件中管理数据，而非使用`pinia`来处理，如果需要查看使用方式可以参考之前的笔记

![image-20230309213446430](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320705.png)

#### 9.2.6.4 轮播图

![image-20230310091554009](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320725.png)

1、房间详情页使用`props`传递参数给`Swiper`

2、其中`mainPart`是网络请求过来的，所以存在一开始加载组件的时候为空的情况。所以一种处理方式就是使用`mainPort?.topModule?.housePicture....`这样会出现很多的`?`，这样很麻烦。所以我们使用`v-if`先判断是否内部有值，如果有的话就加载，非则就不加载

![image-20230309220253329](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320746.png)

3、`vant`组件库可以插槽来自定义轮播图的提示器。`#indicator`表示具名插槽的名字，`props`表示其子组件传来的数据`props`，里面有当前的页数和总页数

![image-20230310091917916](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320773.png)

4、按照下面的方式对数据先进行转换，这里提供的是一个思路，根据`enumPictureCategory`来生成数据

![image-20230310093003249](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320795.png)

这一段就是核心算法。

`swiperGroup`是存储分组之后的结果，遍历原本的数组`swiperData`取出每个数组的`enumPictureCategory`的数据作为对象`key`，如果没有该`key`的话就会返回`undefined`，也就是不存在`"02"`这个对象`key`。

所以需要创建该对象`key`并且该对象`key`为一个数组，里面都是同类数据。创建了对象`key`之后就往对象`key`为`"02"`中填充数据

其核心思路就是是否存在`key`，如果不存在就创建，然后填充数据

![image-20230310110018935](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320819.png)

5、对于一开始的数据存在一些非法字符，所以我们需要替换处理，我们这里使用的`replace`来处理

![image-20230310121147524](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320713.png)

最后的效果是这样的

![image-20230310121856507](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320739.png)

6、下面就是实现得效果，不仅显示这个房间得总页数，而且还有样式得变化

![image-20230310195302058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320784.png)

我们使用`swiperData`的`enumPictureCategory`和遍历`swiperGroup`的`key`比较，只要为`true`的话就显示白块。但是我们并不知道当前显示的数据索引

![image-20230310195156212](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320811.png)

所以我们将当前显示轮播图的数据全部传输给`getSwiperGroup`方法，来遍历`swiperGroup`处理出索引即可

![image-20230310195536046](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320832.png)

#### 9.2.6.5 信息栏

![image-20230310201145622](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320910.png)

1、我们为组件传入参数`topInfos`

![image-20230310201306976](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320670.png)

2、我们来搭建页面结构，并且编写样式

![image-20230310201134949](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320691.png)

#### 9.2.6.6 详情封装

![image-20230311212433678](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320714.png)

1、因为这里有很多这样的样式，所以我们这里封装为一个组件。并且这里使用一个插槽来处理插入组件信息

![image-20230311212520109](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320741.png)

这样我们直接将数据填入`slot`中，就可以在设置同一个模板来处理

![image-20230311212545428](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320769.png)

2、假如我们这样封装的话，就节省了很多的成本直接插入信息即可

![image-20230311213119786](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320797.png)

其结构是相同的

![image-20230311213257107](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320609.png)

3、剩下的都是按照上面的方式来封装，这里不做介绍了

![image-20230311214012324](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320627.png)

#### 9.2.6.7 百度地图集成

![image-20230312162958570](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320649.png)

1、首先需要在`百度开发者中心`申请账号，并且需要创建一个应用才能使用。其中`referer白名单`填写`*`

![image-20230312163511191](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320682.png)

2、其基本的使用还是查看文档来处理。你需要使用`ref`来获取元素`DOM`，然后使用`baidu`的`webgl`来渲染地图

![image-20230312205829988](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320706.png)

3、记住要在`index.html`中添加下面的`script`，这样全局才会有`baidu的webgl`，并且后面填写你创建应用的`密钥(AP)`

![image-20230312210124444](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320727.png)

我们在`web`中引入，可以将`api`改为`getscript`，这样就不会报错了

![image-20230314093356845](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320464.png)

#### 9.2.6.8 tabControl

![image-20230313085745596](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320487.png)

1、我们这里依旧使用之前封装好的`useScroll`，并且最好使用`ref`来获取`DOM`元素

![image-20230313085120665](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320510.png)

2、这里一定要注意一个细节，就是关于滚动。必须要传入给`useScroll`的元素溢出之后才能被监听到滚动，也就是滚动条是传入的元素的，否则就需要监听父元素的`id=app`的，很显然我们监视不到

![image-20230313085448297](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320545.png)

所以需要设置元素的`height`为`100vh`，并且`overflow-y`为`auto`，所以就会导致该元素溢出

![image-20230313085541758](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320575.png)

3、`tabControl`需要使用`emit`来传递参数给父组件。其基本的使用可以参考前面的`emit`的笔记

![image-20230313110506335](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320600.png)

![image-20230313110536011](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320327.png)

4、因为`tabControl`的名字需要是动态的，我们只需要编写参数就可以自动控制`tabControl`的名字

![image-20230313110849689](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320351.png)

​ 4.1 首先就需要获取组件的名称。一个常规的方式就是使用`ref()`参数来处理，但是需要编写很多`ref变量`。这个方式不是很好，所以这里使用函数的方式来处理，只要组件加载就会执行这个函数并且传入参数

![image-20230313115315713](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320372.png)

这里需要一个性能优化，使用`v-memo`来处理，只要`mainPart`变化就会重新更新组件，不然只要页面变化就会自动更新并且重复执行`getSelectRef`函数

![image-20230313115411421](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320410.png)

​

​ 4.2 我们使用`{ "详情" : DOM信息 }`的对象形式来处理存储，我们编写`getSelectRef`来获取`DOM`元素并且存储到对象`selectEl`中

​ 4.3 对于`getSelectRef`下面需要编写`if(!value) return;`来处理，因为我们返回的时候`mainPart`会变化，所以这个时候就会执行这个函数，我们需要编写这个判断来结束函数

​ 4.5 获取`value`参数，并且判断是否存在一样的`对象key`，如果不存在就添加，如果存在就不管。这个时候对应的`对象name`和`对象key`都存入到`selectEl`映射中

![image-20230313115721063](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320430.png)

​ 4.6 我们使用`Object.keys`来获取`selectEl`的所有`key`，这样就动态绑定了`tabControl`的`name`

![image-20230313140306879](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320450.png)

5、我们前面将`selectEl`的`DOM`信息存储，获取其元素的`offsetTop`，使用父元素的`DOM`的`scrollTo`跳转即可

![image-20230313140732206](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320218.png)

#### 9.2.6.9 tabControl 索引

想要页面滚动到特定位置显示对应的标题

![image-20230313205945899](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320241.png)

其本质的逻辑参考下面的

![image-20230313212218502](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320262.png)

1、下面时候整套`索引匹配算法`的全貌，其本质就是将`位置信息`和`索引`挂钩，只要每次位置信息变化就会遍历位置信息，只要比`newValue`大的即可，就是目前的索引位置

![image-20230314091426276](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320292.png)

2、算法这里有一个问题，我一开始使用的`index = -1`，但是最后可能存在最后一个获取不到的问题，因为我们都是`index = i - 1`，所以极限就是`4`

![image-20230314090925354](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320314.png)

所以这里解决的最简单的方法就是一开始默认赋值位`values.length - 1`即可，这样就解决了最后一个获取不到的问题了

![image-20230314091037644](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320333.png)

3、对于下面的获取子组件`tabControl`的`ref`，然后调用里面的方法。对于`Vue3.2`的`setup`的语法，需要使用`defineExpose`将子元素中的东西暴露出来，才能被调用

![image-20230314092102805](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320121.png)

4、下面是解决`tabs`的跳动`bug`的处理。只要点击之后就会将代码调整为点击模式`isClick`改为`true`

![image-20230314102135057](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320143.png)

如果跳转到点之后，这个时候`currentDistance`就和`newValue`是一样的，所以就接触点击模式，将`isClick`改为`false`。但是这里存在一个`bug`，如果跳转的时候滚动页面，就不会精准落到点里面，所以`isClick`就一直为`true`，所以我们在跳转的时候可以静止用户滑动

![image-20230314102432132](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320166.png)

## 9.3 细节优化

### 9.3.1 keep-alive

1、我们在首页中进行网络请求，当我们点击了下面的`tabbar`之后就会清除缓存，就会重新加载首页，很显然这样的方式很消耗网络性能，最好的方式就是缓存起来

![image-20230314160010217](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320196.png)

2、存在这 2 种处理方式，以前都是使用的下面的方式来处理，现在最好使用上面的方式来处理

![image-20230314105322527](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320222.png)

​ 2.1 在使用这 2 个方式之前的处理是要为`.vue`组件添加`name`属性，之前因为是`OptionsAPI`，所以直接写`name`属性即可，但是现在使用的是`setup`语法糖，不存在使用`name属性`，所以按照下面文章的配置即可

[(121 条消息) Vue3 使用 vite-plugin-vue-setup-extend 不生效问题-CSDN 博客](https://blog.csdn.net/ruisenLi/article/details/124385175)

​ 2.2 这里使用的是`include`而非`includes`，在一些版本里面是可以使用`includes`不会报错，这里官方的写法就是`include`

### 9.3.2 首页网络请求问题

![image-20230314105759590](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320254.png)

1、我们写网络请求的时候，就是只要页面滚动到底部就发送请求，但是我们没传入参数，所以就是监听的`window`，所以我们只要切换页面的话就会触底，导致发送网络请求

![image-20230314105636731](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320893.png)

2、所以我们传入`homeref`即可，只监听自己的`滚动`即可

![image-20230314105810462](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320914.png)

### 9.3.3 保留首页记录

1、我们想要`tabbar`页面跳转之后，在`home页面`也能保持之前浏览的位置

2、这里使用`onActived`，只要页面显示就执行，因为本身就记录了`scrollTop`的记录，所以这里直接跳转过去即可

![image-20230314111305863](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320938.png)

### 9.3.4 禁止用户缩放

因为是移动端的项目，所以可以缩放会导致页面很奇怪，所以我们需要禁止用户缩放

![image-20230314143833257](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320966.png)

### 9.3.5 单位转换

```bash
npm install postcss-px-to-viewport --save-dev	// 安装
```

可以参考`Vant`中的文档介绍配置，或者直接去官网来编写

![image-20230314153722053](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320000.png)

这样所有的`px`都转化为`vw`，在`github`中存在配置信息，使用时查看

![image-20230314153810412](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320056.png)

# 11. 后台项目 - 后台管理

## 11.1 前期介绍

### 11.1.1 基本介绍

> 技术介绍

![image-20230315211332794](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320722.png)

> 创建项目

![image-20230315213039494](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320745.png)

这次得项目按照下面得方式来编写

![image-20230315213033226](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320766.png)

### 11.1.2 文件介绍

其他基本文件介绍参考我之前得笔记

![image-20230315213605731](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320798.png)

> extensions.json

1、生成得文件中存在`extensions.json`文件，只要开启该项目`vscode`就会自动推荐使用下面得插件

![image-20230315213424319](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320822.png)

> vite.config.ts

2、这里是`vite.config.ts`得文件，如果是`.ts`得话就又更好得语法提示，并且该文件是接替`vue.config.js`得作用，我们想要写`webpack`得配置都可以在这里面编写

![image-20230315214155910](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320857.png)

3、这里需要注意一个小细节，下面得`vite.config.ts`都是打包得时候使用得，而`tsconfig.json`中是在代码提示得时候使用得，并不是一类东西。比如下面得`@`路径得表示

![[00 assets/d505859e02cc4988f80f7ac2cdbe0e95_MD5.png]]

> tsconfig.json

4、下面就是`tsconfig.json`得配置信息，这个文件时为`ts`做配置信息得，为什么这里得配置信息这么少，这是因为前面得`extends`配置，他将其他得配置文件都隐藏到`node_modules`中了

![image-20230316091150718](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320398.png)

我们根据地址位置就可以找到信息了。这个就是作为一个被暴露出来得主要得配置文件

![image-20230316091440433](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320418.png)

5、当然我们还要一些其他得配置文件，这个文件主要是配置`vite.config.*......`等文件。目前猜测得是这个文件是开发者可以修改得文件，而`tsconfig.json`是不能修改得文件，并且该文件作为`tsconfig.node.json`文件是作为`SSR`优化时得文件

6、`types:node`表示上面得这些文件可能需要跑在`node环境`中进行处理。

7、`composite:true`表示可以合成进去，因为`tsconfig.node.json`是通过`tsconfig.json`中得`references`导进去得，所以需要添加`composite:true`表示可以合成进去

![[00 assets/49e0bfb75f3e625e19c6e640260bcb98_MD5.png]]

> env.d.ts

6、该文件是引入`类型声明`得，我们点击`vite/client`就跳转至`类型声明`文件中

![image-20230316104858135](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320470.png)

就可以看到`Vue`帮忙声明了很多得类型，这样我们就不需要自己手动来编写了

![image-20230316105551354](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320510.png)

7、我们查看了上面得`env.d.ts`文件，可以发现没有`.vue`文件得声明，但是我们导入得`Vue`文件没有报错

![image-20230316110739040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320224.png)

下面就是`Vue`编写`ts`代码的另一个方式，也就是函数参数编写类型，这样传入参数的时候就会有代码提示，并且可以看到最后导出组件的时候是`DefineComponent`，所以下面我们自己声明的模块就需要导出`DefineComponent`

![image-20230316150433598](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320244.png)

可能是内部做了配置，但是这个配置做得并不是很好，所以我们可以自己做一个`类型声明`最后到处得是`component`而非`any`

![image-20230316145531676](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320265.png)

8、假如说不想配置上面的信息的话，可以按照`Volar`，它会自动帮忙导入`.vue`文件

![image-20230316152926992](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320293.png)

### 11.1.3 项目配置

![image-20230316153222483](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320317.png)

#### 11.1.3.1 图标/标题

![image-20230316153652885](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320359.png)

#### 11.1.3.2 代码规范

> .editorconfig

1、这个文件的主要目的就是为了统一`IDE`的配置。比如：各个`IDE`中的字符编码不一样，所以为了统一就需要编写``来保持编码风格

![image-20230316155353315](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320924.png)

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

![image-20230316155604466](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320949.png)

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

![image-20230316162318725](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320973.png)

5、并且对`VSCode`进行配置，按照下面的方式改为`Prettier`即可

![[00 assets/c225bf4e29e134c340a5b4b52f58ded1_MD5.png]]

并且开启`format on save`就可以实现保存文件就格式化稳定

![[00 assets/ff1209ff137ab9071467d84c5b31a4c6_MD5.png]]

\*上面的配置基本是使用`ctrl + s`就格式化代码，但是现在可以`alt + shift + F`格式化代码，所以上面的配置看自己是否愿意配置

> eslint

1.在前面创建项目的时候，我们就选择了 ESLint，所以 Vue 会默认帮助我们配置需要的 ESLint 环境。

2.VSCode 需要安装 ESLint 插件：

![[00 assets/081de6861d102caa72bb1ce8ad0dbf82_MD5.png]]

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

![[00 assets/004660256a19995433e428e1db920ac5_MD5.png]]

2、如果你使用`npm run build`打包之后，想要看到打包之后在服务器的效果，可以使用`npm run preview`指令来运行已经打包好的网页

3、可以看到下面的服务器地址也会跟着你的环境变化而变化

![[00 assets/1f044bf2d71d99f55e18c92f3f4b9068_MD5.png]]

4、对于环境变量存在还存在下面的配置信息，我们新建文件来区分，这个方式是配置信息较多时处理

![[00 assets/119df2cd98d29b253ff1ad9e3b5434fb_MD5.png]]

编辑文件为`.env.xxx`开头，后面添加`mode`，写上`.local`表示`git`时忽略该文件，在`gitignore`中有明确忽略的语法，这样也可以实现区分`开发/生产环境`

![[00 assets/091917675b8fca30f276c84112dc9479_MD5.png]]

### 11.2.7 组件库引入

> 全局引入

直接参考文档来操作即可

![[00 assets/edf944cee72e507e054dc3a322f94d0d_MD5.png]]

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

![image-20230319201952923](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320110.png)

2、因为我们在`app`中设置了`width、height`的宽度和高度为`100vw、100vh`，所以我们作为其子元素可以直接设置为`100%`就行

3、对于`flex`布局，因为`.login`占据了整个屏幕，所以我们设置`flex`居中就可以实现其子元素的居中效果

![image-20230319202029360](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320134.png)

4、需要搭建`tabs`页面，我们按照下面的思路来编写

![image-20230320213303418](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320158.png)

​ 4.1 我们使用`label`具名插槽将标签插入到`tabs`中，并且切换之后的内容通过组件来显示

​ 4.2 我们使用`actionTabName`来作为变量来存储，使用`name`来区分不同的`tabs`

![image-20230320213415348](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320817.png)

​ 4.3 我们将表单的输入框都写入组件中

![image-20230320213728642](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320839.png)

#### 11.3.1.2 \*图标引入

![image-20230320202434746](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320860.png)

1、文档中有一段是关于自动引入图标，但是这个只是引入`iconify`，并不能自动引入`elementui`的图标

![image-20230320202601210](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320885.png)

2、所以这里选择全局引入图标，并且采取插件的形式的来编写。

3、`app.use()`传入函数，第一个参数就是`app`，同时执行该函数，这样就全局注册了图标，这样就不需要在`main.ts`中编写过多的引入代码

![image-20230320203307065](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320910.png)

#### 11.3.1.3 校验规则

1、我们按照下面的方式来编写校验规则，这里需要注意`:model`的写法，而非`v-model`，不然会导致检验错误

2、`required`表示必选，`trigger`表示触发条件，`pattern`表示校验规则。这个可以写多套，因为一开始没输入内容的时候是一套校验规则，但是输入之后又是一套校验规则，所以这里使用数组

![image-20230321171306665](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320932.png)

#### 11.3.1.4 登录操作

1、因为这里存在 2 个种登录方式，所以每种登录都会存在不同，我们就将登录的逻辑写在`panel`的子组件中，其中`panel`组件表示`tabs`

2、使用`ref()`获取组件元素，其中`validate`内部存在回调函数，只要内部校验不通过`valid`就是`false`，通过就为`true`

![image-20230321180327228](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320617.png)

3、在父组件中使用`ref()`来获取去子组件，这样就可以调用里面的方法了。

![image-20230321185157015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320653.png)

#### 11.3.1.5 \*获取组件类型

可以使用`<InstanceType<typeof panelAccount>>`来获取组件的实例的类型

![image-20230321185157015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320653.png)

#### 11.3.1.5 Message 显示 - 自动导入

1、我们点击登录之后应该会弹出消息框，但是并没有弹出，这是因为没有添加样式

![image-20230321181400326](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320681.png)

2、其中一个方法就是全局添加一个样式，这样就不需要手动导入了，但是这种方式显然不是很好。或者选择手动导包，这样我们还需要自己去找，也不是很好

![image-20230321181545133](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320711.png)

3、我们可以使用插件的形式来引入，也就是前面的自动引入

```bash
npm i vite-plugin-style-import -D	// 安装
```

在`vite.config.js`中编写插件的配置

![image-20230321184949045](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320739.png)

#### 11.3.1.6 登录逻辑

1、获取用户信息 -> 发送网络请求 -> 存储数据。按照这套流程来编写即可

2、在组件中获取到的信息传输到`pinia`中的 actions 中，然后进行网络请求的处理将数据存储到`pinia`中

![image-20230321211107317](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320762.png)

3、因为这里多次出现`{ name , password }`的对象，所以最好的方式是设置单独的类型

![image-20230321211349447](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320602.png)

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

![image-20230321214222152](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320618.png)

#### 11.3.1.8 路由守卫

1、默认进入网页的时候是`/`，会重定向进入到`/main`。我们这里需要判断是否登录，如果没有登录就进入`login`，登录的话就进入`/main`

2、如果我们登录之后又输入`/login`的话，肯定是不允许再登录，所以就需要定向到`/main`中

![image-20230322103855986](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320641.png)

3、退出登录的时候删掉`token`再跳转到`/login`中

![image-20230322104315797](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320665.png)

#### 11.3.1.9 记住密码

1、也就是记住`记住密码`的状态，只要为`true`的话就将账户和密码存入`localStorage`。如果为`false`的话就删掉存储的账户和密码

![image-20230322112301018](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320685.png)

2、因为登录的逻辑都写在子组件中，所以我们在调用子组件函数的时候传入参数即可

![image-20230322112719842](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320709.png)

### 11.3.2 菜单设计

#### 11.3.2.1 基本介绍

`RBAC`也就是`role based access control`基于角色的访问控制。如果我们设计权限系统的话，也是按照下面的方式来设计，其中数据库对于权限的设计也是这样处理的

![image-20230322173316485](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320450.png)

#### 11.3.2.2 获取用户信息

1、我们再编写一个接口即可

![image-20230322175347462](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320469.png)

2、但是存在鉴权的问题，我们将鉴权的`token`写在请求拦截器中

![image-20230322175512811](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320490.png)

#### 11.3.2.3 获取菜单信息

1、其基本的操作和之前是一样的

![image-20230322192515610](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320518.png)

2、老师这里使用的权限管理的方案是将用户的权限地址都存入到了服务器，并且是一个树结构，所以就不存在本地修改代码导致权限泄漏的问题了

![image-20230322192640447](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320547.png)

#### 11.3.2.4 菜单树布局

![image-20230322204426149](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320566.png)

#### 11.3.2.5 动态菜单

1、我们将菜单信息都存在到`localStorage`，因为直接存在`pinia`中就是存在`内存`中，如果网页刷新的话，这些数据就会消失

![image-20230322212414969](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320354.png)

2、下面就是动态菜单的结构

![image-20230322212452431](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320371.png)

3、因为返回的数据中带有图标信息，也就是图标的名字，但是并不带图标的网址。所以这里选择使用动态组件的方式来填充图标，我们已经将所有的图标注册为全局的组件，所以这里直接输入图标的名字的就可以显示图标

![image-20230322212653357](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320393.png)

![image-20230322212705949](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320418.png)

可以看下之前图标的设置就是下面的形式

![image-20230322212737504](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320439.png)

#### 11.3.2.6 \*动态路由

> 传统方式

一次配置所有的路由信息，编写所有的页面信息。但是这种方式存在一个问题，如果一个权限比较低的用户知道你的路由信息就可以无权限进入，这是一个很危险的事情。所以可以采用动态路由的方式来处理

![image-20230327212934992](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320466.png)

> 动态路由

1、一般存在下面的 2 种方式来实现动态路由。第一种就是将所有权限的路由都编写成一个`JSON`格式或者一个数组形式，根据用户的信息来决定使用那个路由，这种方式存在一个弊端，如果需要再添加一个权限的话就需要重新编写代码部署。第二种方式就是根据返回的动态菜单的数据，动态设置路由并且使用

![image-20230327215316037](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320188.png)

2、我们先按照`动态菜单`的格式来编写`路由文件夹`的层级

![image-20230328161452256](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320208.png)

相对应的`views`文件夹中的层级也是一一对应的，这样方便查找

![image-20230328161656085](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320233.png)

3、我们使用`import.meta.glob()`方法，来查找路径下所有的路由，并且导出，这里是全部权限的路由。最后导出匹配用户权限的路由即可，导出的数组就是全部的路由

![image-20230328162024264](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320257.png)

4、只要用户登录之后就会自动的添加路由进去。但是这里就存在一个问题，只要我们重新刷新页面的话路由信息就会消失，所以就会找不到路由

![image-20230328162315144](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320284.png)

5、所以我们刷新页面之后需要重新执行路由映射，首先来看下各个部分执行的顺序。`router外部加载` -> App 显示 -> `beforeEach`加载 。

6、如果在`router外部加载`的话`pinia`还没加载完毕所以不能在这里写。如果在`beforeEach`里面编写的话就会存在路由匹配直接加载页面了，就会加载到`NotFound`中，也直接排除

![image-20230328162636046](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320311.png)

7、所以目前的方式是在`pinia`创建的时候加载即可，只要重新刷新页面的话就会重新加载`pinia`，就会重新执行加载路由的操作，所以这个就在执行路由之前加载了，不会跳转到`notfound`页面了

![image-20230328170956772](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320244.png)

![image-20230328171020376](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320262.png)

8、下面就是处理，登录首次进入`Main`页面的话默认加载第一个路由的组件。只要我们登录跳转的时候就默认加载第一个路由

![image-20230328171722971](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320285.png)

但是这就存在一个问题，如果浏览器输入`/main`的话也需要跳转到第一个路由，按照上面的方式是不能跳转的。所以我们只要执行了`mapMenuToRouter`的话就获取第一个路由并且导出

![image-20230328203059265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320316.png)

导出之后，只要`登录`或者`手动输入路由"/main"`的话就会自动跳转到第一个路由

![image-20230328203231255](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320342.png)

\*`startWith`表示只要开头包含`/main`，并且不包含`token`的话就会自动跳转到`/login`页面

![image-20230328203358291](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320364.png)

#### 11.3.2.7 path 匹配菜单

1、也就是传入当前`path`，匹配路由信息导出`id`值。如果这样设计的话，只要重新加载`menu`的话就会匹配菜单，但是重新加载的场景只有`登录进入`、`刷新页面`、`地址栏输入地址`......会执行，剩下的都是点击`菜单`切换路由

![image-20230328205502154](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320202.png)

2、最后的`id`值传入给`elementui`的`default-active`即可

![image-20230328205650920](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320228.png)

### 11.3.3 头部设计

#### 11.3.3.1 头部信息展示

![image-20230326205738513](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320256.png)

1、按照下面的结构来做下拉菜单，剩下布局问题参考代码即可

![image-20230326205846047](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320277.png)

2、这里依旧采用组件化的思路对头部拆分，方便管理

![image-20230326210320032](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320306.png)

3、因为下拉菜单处于`app`的外面，所以外面很难对这个元素设置样式

![image-20230326210557805](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320331.png)

所以使用`:global`将元素设置全局的`HTML`的样式，就可以设置`#app`外面的样式

![image-20230326210514593](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320028.png)

#### 11.3.3.2 :deep 使用场景

1、我们想要在父组件中对子组件中标签添加样式，按照下面的层级很明显不能生效

2、设置样式只会对根组件样式生效

![image-20230327211038144](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320051.png)

3、使用`:deep()`属性就可以对子标签设置样式

![image-20230327211641646](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320080.png)

4、所以这个`:deep`的使用场景在`ElementUI`组件中设置修改其组件的样式

#### 11.3.3.3 面包屑

1、只要加载面包屑组件的话，就会自动执行`mapPathToCrumb`函数，其中 2 个`push`表示的就是`一级菜单`和`二级菜单`

2、为函数套上`computed`的话，只要里面的`path`发生了改变就会重新执行回调函数，这样不管啥情况，只要`path`改变的话就会自动修正面包屑

![image-20230328220159922](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320118.png)

3、只要我们点击了系统管理，就会自动跳转到这个类别的第一个路由

![image-20230328220520920](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320145.png)

第一个方法：我们在传入父路由的时候就默认传第一个即可，但是这个方式存在权限问题，如果第一个路由没权限的话就会跳转到`notfound`

![image-20230328220607547](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320164.png)

第二个方法：为父路由添加路由映射，重定向到第一个子路由。下面的逻辑就是，只要添加了父路由之后，后续就会检查是否已经添加，如果添加了就不去重定向的`push`，如果没添加就去添加

![image-20230328220824311](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320932.png)

这样就会有父路由重定向了

![image-20230328221006668](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320964.png)

4、我们点击上面的父路由菜单`系统管理`之后不会自动切换动态菜单，所以我们这里也让执行和`path`挂钩即可

![image-20230328221050601](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320009.png)

### 11.3.4 User 页面 - 基础搭建

#### 11.3.4.1 界面搭建

![image-20230330090149526](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320042.png)

1、我们按照下面的方式搭建页面

![image-20230330090756059](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320075.png)

2、但是时间选择的位置默认是英文的，很明显不是很友好

![image-20230330104142303](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320102.png)

这里就涉及到了国际化的处理，我们导入`zhCn`即可

![image-20230330104208037](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320848.png)

#### 11.3.4.2 重置按钮

1、我们获取`form`的`ref`，使用`resetFields`方法即可清除所有数据

![image-20230330104249977](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320868.png)

2、注意这里一定要添加`prop`属性，并且要和`reactive`中的属性名一致

![image-20230330104515146](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320893.png)

![image-20230330104610550](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320923.png)

#### 11.3.4.3 表格展示

1、在`pinia`中的`action`来网络请求数据即可

![image-20230330214506893](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320944.png)

2、使用`el-table`显示数据即可

![image-20230330220229487](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320966.png)

并且这里为了定义表格中状态的样式，可以使用作用域插槽来解决，插槽会默认向外部传输数据`scoped`表示的是整行的数据

![image-20230330220346863](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320733.png)

在文档中还有可以定义表头

![image-20230330220416226](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320754.png)

3、相应的使用`store`中的数据即可

![image-20230330220429156](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320772.png)

4、我们这里显示的时间数据存在问题，我们需要修改一下。这里使用`dayjs`库来对时间进行处理

![image-20230331095726110](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320798.png)

我们和上面的`enable`一样，使用作用域插槽来对时间进行处理

![image-20230331095759107](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320821.png)

#### 11.3.4.4 \*分页器

![image-20230331113629401](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320843.png)

1、页面搭建，按照官网的例子搭建即可

![image-20230331113607137](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320524.png)

2、对于这里的`size`和`offset`就涉及了`Mysql`的分页查询。第一页就是`size:10 offset:0`，所以第一页就是`limit 0 10`，第三页就是`size:10 offset:20`，就是第二页。所以后端开发者直接就可以使用`limit 20 10`就行了

![image-20230331114440662](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320546.png)

3、这里还存在一个小坑，我们在第二页的时候修改`size`的话，就会先修改`size`，发送请求。这个时候如果数据不够，所以就会跳转到第一页再发送一次请求，这就发送了 2 次请求，也就是`size为20`页面为`2`的时候，`size:20 offset:20`，但是数据总数为`14`，所以可能导致没有数据的情况。所以我们设置一个`if`判断数据长度来发送请求，如果长度不够，就只请求页码修改的网络请求

4、并且需要考虑用户在第一页切换`size`，并且总数小于`size`的情况，所以我们还需要加一层判断

![image-20230331152056414](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320565.png)

#### 11.3.4.5 重置/查询按钮

1、我们点击了查询/重置按钮的话，就会发出事件，并且传出数据

![image-20230331162028682](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320592.png)

2、我们获取`userContent`的`ref`，并且直接调用内部的网络请求的方法

![image-20230331162053034](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320616.png)

3、这里就有一个小坑，我们查询之后点击分页是不带查询数据的，所以我们需要手动保存查询数据，只要传入的对象中有属性就覆盖

![image-20230331162111843](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320648.png)

#### 11.3.4.6 删除数据

编写网络请求，写入`pinia`的删除`action`，监听删除按钮，调用删除接口并且重新请求数据

![image-20230331204423579](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320335.png)

#### 11.3.4.7 新建用户

![image-20230331212933421](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320358.png)

1、搭建页面，按照框架来搭建即可

![image-20230331212917843](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320378.png)

2、我们新建用户的`userContent`发送事件，并且携带数据

![image-20230331212847678](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320407.png)

将事件传输给`user`接受，并且使用`ref`来调用内部的函数

![image-20230331212959156](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320431.png)

传输数据修改变量，控制模态框的显示和隐藏

![image-20230331213116060](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320467.png)

3、随后就是发送请求，存储数据

![image-20230402125410831](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320253.png)

就是做出展示，回显数据

![image-20230402125511788](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320278.png)

4、这里不多赘述，大致业务逻辑基本都一样

#### 11.3.4.8 \*编辑用户

1、其基本的逻辑和新建用户差不多，这里不过多赘述了

2、但是这里有一个`ElementuiPlus`的`resetFields`的方法的坑，他并不是重置所有数据，而是回溯到`DOM`插入之前的数据。比如我在`setup`中调用函数，并且传入数据，如果后续调用`resetFields`就会回溯到一开始的数据，而不是清除

![image-20230401213342582](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320300.png)

我们可以将显示`Message`封装为一个函数，这样直接调用即可

![image-20230402125649424](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320332.png)

#### 11.3.7.2 \*分页细节 - $onAction

1、我们以前创建新用户的时候都不会进行页面跳转到第一页，这是一个小细节的优化。目前存在 2 种方式的运用，第一种就是使用`事件`，第二种就是使用`事件总线`。我偏向于第一种，因为这样的传递有迹可循

![image-20230416165326494](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320356.png)

2、但是我们还存在第三种方式来处理，就是使用`pinia`的`$onAction`来监听`store`的`action`即可

![image-20230416165231972](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320385.png)

3、我们使用`pinia`的`$onAction`来处理，它可以监听`systemStore`中`action`函数的调用，只要调用的话就会执行里面的回调函数，我们通过`name`来作为参考进行处理

![image-20230416165250708](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320169.png)

### 11.3.5 Dep 页面 - 组件抽取

#### 11.3.5.1 Search 抽取

1、我们可以发现后台管理系统的很多页面都是差不多的，所以我们可以抽取高阶组件，使用配置文件的方式来编辑页面

![image-20230403191134846](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320189.png)

![image-20230403191150368](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320209.png)

2、在抽取页面之前，我们可以先归纳网络请求部分。我们网络请求的架构是`axios -> pinia -> 页面`，所以我们需要修改`axios和pinia`部分

3、网络请求大致可以分为下面的 5 条接口，即`增删改查`，对于不同部分的接口就使用`pageName`传入作为区分即可

![image-20230403191447351](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320238.png)

4、网络请求分出来之后，就需要区分`pinia`中的`action`的使用

![image-20230403191630493](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320262.png)

我们只需要传入`pageName`中即可表示不同的接口处理

![image-20230403194248587](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320295.png)

5、我们再来搭建页面，因为我们需要使用配置文件的方式来搭建页面，所以先编写配置文件的格式

![image-20230403191804770](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320156.png)

我们使用`v-for`来遍历配置文件，使用`template + v-if`的方式来动态生成不同的组件

![image-20230403191841409](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320175.png)

其内部的逻辑基本没变，这里使用`pageXXX`的方式命名，让该高阶组件更加通用

![image-20230403192034438](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320198.png)

6、我们使用`ts`来编写`Vue`项目的话可以使用`props`的语法糖，传入接口就可以获取该`props`数据，并且组件也有相应的提示

![image-20230403192052004](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320226.png)

#### 11.3.5.2 Model 抽取

1、对于`模态框`的设计，其遵循的原则和上面的`搜索框`是一样的，这里直接看源码就行了

![image-20230403192304793](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320246.png)

2、但是对于`模态框`存在一个`options`，这个东西内部的数据是动态的

![image-20230403192440042](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320266.png)

3、但是我们编写的配置文件的`options`是没有数据的，所以我们需要手动将数据填充进去

4、只要加载该组件就会自动请求数据，并且这里使用`计算属性`来处理，这里可能最优解就是使用`计算属性`，因为网络请求可能会延迟，所以将`DepartmentData`放在`computed`中，只要数据变化就会自动更新数据，这样就避免了网络延迟的问题

5、内部将网络请求到的数据存入`options`，这样内部数据就是动态的

![image-20230403192602001](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320165.png)

#### 11.3.5.3 Content 抽取

1、其抽取也和之前是差不多的，这里直接看源码

2、这里主要的就是对于`table`中插槽的处理，相对来说比较复杂

![image-20230403193046672](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320191.png)

3、比如下面的表格中`状态、创建时间、更新时间`都是需要进行处理之后才能使用的

![image-20230403193152937](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320219.png)

如果我们按照之前的方式就是编写很多的`template + v-if`来处理，但是会发现这样就需要写很多的`v-if`，很显然这很麻烦，而且需要很多的`type`

![image-20230403193404947](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320256.png)

4、所以这里就可以使用插槽来处理，使用`:name="item.slotName"`来设置插槽名，并且对于`el-table-column`下的`#default`就是插入到`table`中的插槽，并且传出数据`scoped`，最后传入到`slot`中，所以这里存在一层嵌套。梳理一下就是`el-table-column -> #default -> slot`的嵌套关系

![image-20230403193508625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320284.png)

5、这样就实现了表格内的定制化处理

#### 11.3.5.4 Hook 抽取

因为存在很多的相同的方法，我们可以使用`hook`抽取的方式来抽象方法

![image-20230403194001671](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320306.png)

#### 11.3.5.5 showMessage 抽取

![image-20230403194154784](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320252.png)

1、我们将`showmessage`进行抽取，这样我们只需要传入`message`即可

2、并且我们对常量进行抽取，这样我们以后想修改的话，只需要修改这个部分就行

![image-20230403194343475](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320273.png)

### 11.3.6 Menu 页面

#### 11.3.6.1 页面设计

![image-20230404141335392](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320298.png)

1、这个在`elementui`中有对应的组件，可以直接使用

![image-20230404141425430](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320320.png)

2、我们在使用的时候就参考文档即可

3、对于参数来说，可以直接使用`v-bind`指令，这样就会展开对象，也就会变成`rowKey:"id" treeProps:{ children:"children" }`放入到`el-table`中

![[00 assets/7e3f8193edb6b5e2684980672d99f998_MD5.png]]

4、后续的编辑，删除，新建等功能这里就不去做了，直接参考老师源码即可

#### 11.3.6.2 User 菜单子树

![image-20230404141841839](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320376.png)

1、这个对于`elementui`也是存在组件直接使用

![image-20230404141916935](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320244.png)

2、但是这里就存在一个问题，我们在`Model`中并未封装`插槽`，所以我们还需要使用`template + v-if`的操作模式再编写一个树结构的组件，并且在内部编写事件，很显然这样会导致高阶组件的代码变得不可维护，所以我们这里添加插槽的选项，在使用时传入就行

3、这里其实就是一种高阶组件使用的思想，我们封装的高阶组件，经可能将复用的方法写入，但是对于独特的方法，组件最好就是外部传入，这样就避免了耦合，提高了高阶组件的纯度，在后续的样式和数据传入也有涉及

![image-20230404142359234](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320268.png)

4、我们通过`请求三层架构`获取数据并且传入更新`DOM`，这样就出现了`菜单子树`

![image-20230404142800168](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320298.png)

5、我们点击了菜单子树的选项之后，就会获取绑定的`node-key`的值，我们整理之后传入就行

6、这里就体现了`高阶组件`的封装思想，这个数据只有自己拥有，所以我们需要将该数据放置在外面，而非高阶组件中。并且对于参数的设置也需要思考，外面使用对象的形式，这样可以传入很多的其他参数，而非一种

![image-20230404143207293](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320332.png)

7、新建和编辑都是封装好的`Hook`，并且参数也是直接传入到`Hook`中，所以我们可以使用回调函数的方式获取参数，只要新建或者编辑的话就会执行该回调函数

8、使用这种方式就扩展了`Hook`的功能，只需要传入回调函数就能执行特定的功能。比如：新建中就是清除之前的数据，而编辑需要数据回显，就需要遍历`菜单id`并且返回设置

![image-20230404143610684](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320361.png)

9、对于菜单的返回`id`可以写在`utils`中，这里使用的是函数递归来获取

![image-20230404144611570](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320386.png)

#### 11.3.6.2 \*nextTick 原理

1、我们首先可以看`Vue`文档中如何说明的，可以看到其实`Vue`会将一些执行的东西放入到`缓存队列`中，所以有的时候获取`DOM`不是更新之后的`DOM`，而是队列执行之前的

![image-20230404135102826](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320210.png)

2、我们这里写的时候时先显示的`模态框`，然后执行的`CallBack`。这个时候可能`ref`没有获取到了`DOM元素`，所以数据根本插不进去，就会导致报错。所以这里就使用了`nextTick()`回调函数来处理，只要`DOM`都更新完毕之后才会去执行

![image-20230404135306134](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320228.png)

如果简化的话，就是下面的步骤。数据已经更新了，但是在获取`DOM`的时候，`Vue`并没有重新执行`DOM`，所以导致获取`DOM`并且插入值就是之前的

![image-20230404135632622](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320252.png)

3、其实在源码中，`nextTick`就是`new Promise(() => { ...任务队列 }).then(nextTickCallBack)`的执行过程，就是放在`.then()`中执行的，这样就保证了`DOM更新`完毕了。

4、并且对于`nextTick`来说，他是属于`微任务队列`的，这个面试比较常见

![image-20230404140016397](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320279.png)

### 11.3.7 按钮权限

对于按钮权限存在增删改查 4 种方式，我们在返回菜单信息都是一并返回，所以需要对其进行处理

![image-20230416112336238](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320301.png)

1、首先是对`menus`进行处理，并且返回`permissions`，下面的遍历使用到了递归

![image-20230416112535100](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320319.png)

2、获取到数据之后对数据进行查询，如果有的话就修改`isCreate`......等作为判断条件的值，没有的话就不显示

3、但是这种方式存在一个问题，就是我们在这个页面中需要写一遍，但是跳转到另外一个页面的话就需要再来写一遍了

![image-20230416112826151](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320147.png)

4、所以我们这里可以抽取`hook`来处理，我们传入查询的参数即可

![[00 assets/af3ca184084e19dcea79b66fa6bf4f42_MD5.png]]

然后使用`isCreate`......来控制页面组件是否显示，就可以完成组件的显示了

![image-20230416164644238](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320199.png)

## 11.4 图表搭建

### 11.4.1 countCard 搭建

我们要实现下面界面的搭建

![image-20230416190826899](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320229.png)

我们按照下面的格式进行编写即可，剩余的就是请求数据放入到`store`中，最后来渲染即可

![image-20230416201640692](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320253.png)

### 11.4.2 数字滚动实现

1、这里使用到了`CountUp`的库进行处理`npm i countup.js`

2、我们需要在数字前面加上`￥`来处理，这里存在 2 种实现方式，其中一种就是直接在`html`中添加`￥`来处理

3、第二种方式就是添加对`CountUp`中添加`prefix`配置

![image-20230416204509976](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320275.png)

### 11.4.3 echarts 基本实现

1、我们需要引入`echarts.js`的包`npm i echarts`

2、我们需要书写配置，并且`echarts`的实例化需要放入到`onMounted()`的回调函数中进行处理，因为这里需要操作`DOM`，所以需要放入里面

3、引入的时候一定要使用`import * as echarts from "echarts"`来引入，不然会引入失败

4、下面的`renderer`表示使用`canvas`引擎来渲染图表信息，还可以切换为`svg`的形式

![image-20230416211610655](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320075.png)

### 11.4.4 echarts 封装

1、我们按照三层来封装`echarts`，首先是`用户显示层`，我们直接调用`pieEcharts`即可，传入数据

![image-20230417100221422](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320095.png)

显示层将数据传输给`pieEcharts`之后，`pieEcharts`会进行配置，该组件就是专门存放配置的。然后就就将配置传输给`baseEcharts`，这是所有图表的根基，它专门用于实例化图表的

![image-20230417100115593](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320118.png)

2、最后汇总其实就是`显示(传输数据) => 上层图表(写入配置信息) => 下层图表(实例化图表)`的过程

3、这样我们只需要编写配置信息之后，再传入数据即可

![image-20230417100651522](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320154.png)

### 11.4.5 \*数据动态展示

1、首先就是书写网络请求的部分，下面提供了一种新的思路，我们可以将请求都写成枚举类型，这样只需要修改枚举类型里面的值即可

![image-20230417093422591](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320178.png)

然后将网络请求写进`action`中，因为都是不相干的数据，所以可以同时异步请求处理

![image-20230417100750824](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320204.png)

2、请求到数据之后进行映射。注意，一定要使用`computed`，因为一开始是获取不到数据的，所以要计算它的依赖，它需要实时变化

![image-20230417100909149](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320038.png)

3、同理，因为是三层架构，所以`pieEcharts`也需要使用`computed`来实时监听变化，然后传输给`baseEcharts`

4、这里就有一个需要注意的点，因为我们使用`computed`传输给`baseEcharts`之后，我们使用`setOptions`设置的表格就是第一次的传输的数据，也就是数据为空的配置。

5、但是后续网络请求到达之后`props`中的数据已经发送变化了，但是图表已经渲染成功，所以即便数据改变也不会重新渲染图表。这里我们就需要使用`watchEffect`来处理，它会搜集依赖，只要内部响应式数据改变就会重新执行，这样后续网络请求达到之后也能做出改变

![image-20230417101203632](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320059.png)

### 11.4.7 图表展示

我们需要展示下面的一系列图表数据

![image-20230417154522003](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320082.png)

1、我们按照上面的方式封装了`echarts`，并且实现了动态数据加载的处理，这里再添加图表就方便很多了

2、我们只需要编写配置信息，最后传入到`baseEcharts`中即可

![image-20230417154654570](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320110.png)

3、相应的这里有很多的数据映射，因为服务器返回的数据不一样，我们需要手动的进行映射处理

![image-20230417154751291](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320136.png)

4、其基本步骤就是`请求数据 -> 放入pinia -> 页面获取(computed) -> 通过props传入 -> 图表展示`

### 11.4.8 地图展示

1、我们需要展示地图数据，第一步就是注册地图。其中第一个参数是地图名，第二个是传入`ChinaJSON`值

2、然后就是在`baseEcharts`的基础上再传入`地图`的配置。

![image-20230417160601501](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320160.png)

3、这里展示的数据我们需要经过转化之后才能使用，所以这里我们写了一个`utils`的函数转化

![image-20230417161231603](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320068.png)

4、剩下的代码查看我写的代码即可

### 11.4.9 Card 封装

1、可以发现下面有很多的代码其实是不必要的，我们可以将图表的`Card`封装为一个组件来进行处理

![image-20230417104319934](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320090.png)

2、下面为封装的过程，这里使用到了插槽

![image-20230417104511510](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320110.png)

### 11.4.10 \*页面自适应

1、首先就是使用`Echarts`的重新渲染的处理，我们可以在`onMounted`编写`onUnMounted`钩子函数，这个也是可以正常生效的，这样我们就可以共享数据的同时删除数据

![image-20230417165408079](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320134.png)

2、第二个就是布局的处理，我们在`ELementUI`中有响应式布局

![image-20230417165849934](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320156.png)

下面就是响应式的处理，我们传入相应的参数即可，下面就和`:span`是一样的，一行是`24格`

![image-20230417165829754](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320178.png)

下面是我们之前写的`:span`的处理方式，如果实现响应式就可以参考上面的代码

![image-20230417171156665](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320954.png)

## 11.5 Git 约束

### 11.5.1 husky

1、我们在项目中使用`npm run lint`就可以自动格式化所有的代码

![image-20230417191145164](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320973.png)

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

![image-20230417192550176](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320992.png)

6、然后正常提交代码就行了，它会自动执行格式化代码

![image-20230417192447529](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320021.png)

格式化之后的代码

![image-20230417193550915](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320043.png)

### 11.5.2 commit 规范

通常我们的 git commit 会按照统一的风格来提交，这样可以快速定位每次提交的内容，方便之后对版本进行控制。

![image-20230417193701893](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320094.png)

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

![image-20230417193806359](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320779.png)

并且在 package.json 中进行配置：

![image-20230417193823836](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320799.png)

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

![image-20230417195121896](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320817.png)

2、第二步选择本次修改的范围（作用域），也就是修改了那些文件

![image-20230417195156451](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320838.png)

3、第三步选择提交的信息

![image-20230417200738918](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320859.png)

4、第四步提交详细的描述信息

![image-20230417200902867](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320880.png)

5、第五步是否是一次重大的更改

![image-20230417200926273](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320355.png)

6、第六步是否影响某个 open issue

![image-20230417201005593](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320375.png)

下面就是我们使用`cz`来生成的`log`记录

![image-20230417201043683](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320395.png)

我们也可以在 scrips 中构建一个命令来执行 cz

![image-20230417201236307](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320414.png)

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

![image-20230417202710860](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320481.png)

3.使用 husky 生成 commit-msg 文件，验证提交信息：

```shell
npx husky add .husky/commit-msg "npx --no-install commitlint --edit $1"
```

![image-20230417202647498](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320526.png)

4、可以看到我们使用`git commit -m "123"`提交的时候就会被拦截，然后报错

![image-20230417210514635](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320978.png)

5、因为我们安装了提交验证，所以需要使用`cz`来提交

6、我们看命令就可以发现，其实是依次执行命令的，首先就是执行`cz`，然后就是值`husky`的`npm run lint`，然后`commitlint`全程都是验证作用

![image-20230417210645402](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320014.png)

7、按照这样的方式我们就搭建了一个很严密的`git`提交验证流程

# 12. 项目部署

## 12.1 DevOps

### 12.1.1 传统的开发模式

在传统的开发模式中，开发的整个过程是按部就班就行：

![image-20230422134558891](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320039.png)

但是这种模式存在很大的弊端：

- 工作的不协调：开发人员在开发阶段，测试和运维人员其实是处于等待的状态。等到测试阶段，开发人员等待测试反馈 bug，也会处于等待状态。
- 线上 bug 的隐患：项目准备交付时，突然出现了 bug，所有人员需要加班、等待问题的处理；

### 12.1.2 DevOps 开发模式

DevOps 是 Development 和 Operations 两个词的结合，将开发和运维结合起来的模式：

![image-20230422134628345](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320065.png)

![image-20230422134638296](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320104.png)

### 12.1.3 持续集成和持续交付

伴随着 DevOps 一起出现的两个词就是持续集成和持续交付(部署)：

- CI 是 Continuous Integration（持续集成）；
- CD 是两种翻译：Continuous Delivery（持续交付）或 Continuous Deployment（持续部署）；

1、持续集成 CI：

![image-20230422134709110](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320166.png)

2、持续交付和持续部署：第一张图就是持续交付，我们将最后的代码编写出来手动做部署就是持续交付；第二张图就是持续部署，它最后的部署都是自动的，所以就是持续部署

![image-20230422134919980](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320543.png)

![image-20230422134931358](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320564.png)

### 12.1.4 自动化部署流程

![image-20230422135119714](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320638.png)

## 12.2 云服务器

这里参考我之前的笔记即可

## 12.3 nginx 部署

### 12.3.1 部署

其实`nginx`本质就是一个软件，我们使用`nginx`来监听`80端口`的话，只要我们来访问`80端口`的话就会自动返回需要的资源，下面是`nginx`的部署：

> 1、搜索 nginx

`dnf search nginx`，我们使用这个命令来搜索`nginx`

![image-20230422141408769](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320662.png)

> 2、安装 nginx

`dnf install nginx`，如果我们搜索之后发现存在这些包的话，就可以选择安装了

![image-20230422141447983](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320707.png)

> 3、启动 nginx

```shell
systemctl start nginx	// 启动nginx
systemctl status nginx	// 查看nginx状态
systemctl enable nginx	// 系统启动，nginx就会自动启动
```

![image-20230422141905380](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320805.png)

### 12.3.2 配置

我们这里将我们`弘源旅途`的项目配置到`root/hytrip`中

![image-20230422142745660](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320906.png)

1、我们需要找到`nginx`中的配置文件的地方`etc/nginx`中，我们找到`nginx.conf`文件

![image-20230422142835844](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320923.png)

2、我们修改`nginx`的权限，这里改为`user root`，这样`nginx`就具备了`root`权限的身份

![image-20230422142918501](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320941.png)

3、然后就是修改`nginx`访问的地址，我们这里在`location`中进行编写，`root`表示默认访问的地址，`index`表示默认访问的文件

![image-20230422143403181](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320967.png)

4、最后使用`systemctl restart nginx`来重启`nginx`之后，就可以看到我们部署的网页了

5、如果想让`nginx`作为路由来返回数据，按照上面的配置会有问题。因为现在前端都是单页面，不存在多个`HTML`，我们在有路由的情况下刷新就会导致`404`

![image-20230516205623537](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320988.png)

6、我们配置下面的`try_files`就可以解决这个问题，`try_files $uri $uri/ /index.html;`

解决文档：[(129 条消息) nginx 代理后刷新显示 404*nginx 代理后 404*一只拖后腿的程序猿的博客-CSDN 博客](https://blog.csdn.net/xu622/article/details/87348848)

![image-20230516205348139](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320014.png)

## 12.4 自动化部署 - jenkins

### 12.4.1 安装 Java 环境

\*注意：如果服务器一开始安装了`Java`的版本，一定要重新卸载之后再安装，不要把`Java`版本搞混了

1、Jenkins 本身是依赖 Java 的，所以我们需要先安装 Java 环境

2、因为`jenkins`的最新版需要使用`Java`的最新版本，所以这里我使用最新版的`Java`

```
dnf search java  // 安装最新版Java
```

![image-20230515144309557](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320652.png)

```
dnf install java-17-openjdk  // 安装最新版Java
```

![image-20230515144423875](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320691.png)

3、但是追求稳定的话最好安装 Java1.8 的环境

```shell
dnf search java
dnf install java-1.8.0-openjdk.x86_64
```

### 12.4.2 安装/启动 Jenkins

1、因为`Jenkins`本身是没有在`dnf`的软件仓库包中的，所以我们需要连接`Jenkins`仓库

![image-20230515144700625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320725.png)

2、`wget`是 Linux 中下载文件的一个工具，`-O`表示输出到某个文件夹并且命名为什么文件；

3、`rpm`：全称为**The RPM Package Manage**，是`Linux`下一个软件包管理器；

```shell
wget –O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
```

![image-20230515144933034](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320746.png)

```shell
# 导入GPG密钥以确保您的软件合法
rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
# 或者
rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
```

![image-20230515145009437](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320785.png)

4、编辑一下文件`vi /etc/yum.repos.d/jenkins.repo`通过 vim 编辑

5、编辑时先输入`i`表示插入文字，将下面的文字复制上去。按住`esc`表示退出编辑模式，再按住`shift+;`输入`wq`表示保存并退出

```
[jenkins]

name=Jenkins-stable

baseurl=http://pkg.jenkins.io/redhat

gpgcheck=1
```

6、安装 Jenkins，但是可能存在下面的`公钥没有安装`的问题，这里的解决方法就是将`gpgcheck`改为`0`

```shell
dnf install jenkins # --nogpgcheck(可以不加)
```

![image-20230515150553030](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320809.png)

6、启动`Jenkins`的服务：如果`jenkins`启动失败，大概率是`Java`版本和`jenkins`版本不对应，注意检查

```shell
systemctl start jenkins
systemctl status jenkins
systemctl enable jenkins
```

7、`Jenkins`默认使用`8080`端口提供服务，所以需要加入到安全组中：

![image-20230516104934606](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320498.png)

8、进入网页，按照指示执行下一步操作，这里推荐使用`安装默认推荐插件`

![image-20230516105236747](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320516.png)

### 12.4.3 创建仓库

1、因为自动化部署是将`仓库`中的数据拉取下来，所以我们需要创建一个仓库

![image-20230516110556805](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320534.png)

2、执行下面的步骤将本地仓库的数据上传到云端

![image-20230516110636195](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320559.png)

### 12.4.4 使用流程

#### 12.4.4.1 安装 git

1、检查`云服务器`是否安装了`git`，因为我着这里是将`git`中的数据`clone`下来

![image-20230516115010375](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320580.png)

2、如果没有的话就需要安装了`dnf install git`

![image-20230516115056583](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320608.png)

#### 12.4.4.2 基础配置

1、因为这里使用的是`gitbuh`的仓库，所以这里添加了`github`项目的地址

![image-20230516135440992](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320373.png)

2、这里是源码管理，依旧是需要输入仓库的地址。因为这里是公开的仓库所以不需要输入凭证，但是一般的公司项目不是开源的，所以就需要输入下面的凭证信息

3、凭证信息的设置在设置面板使用，这里就不介绍了

![image-20230516135537770](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320408.png)

如果是`github`项目的话最好就是指定分支`/main`，它默认是`/master`

![image-20230516135708933](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320439.png)

#### 12.4.4.3 触发器

5、因为需要一定时间就触发一次，问下`github`的仓库是否更新了，所以需要设置触发器

![image-20230516135758975](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320469.png)

**构建触发器：**

这里的触发器规则是这样的：

- 定时字符串从左往右分别是：分 时 日 月 周

```js
#每半小时构建一次OR每半小时检查一次远程代码分支，有更新则构建
H/30 * * * *

#每两小时构建一次OR每两小时检查一次远程代码分支，有更新则构建
H H/2 * * *

#每天凌晨两点定时构建
H 2 * * *

#每月15号执行构建
H H 15 * *

#工作日，上午9点整执行
H 9 * * 1-5

#每周1,3,5，从8:30开始，截止19:30，每4小时30分构建一次
H/30 8-20/4 * * 1,3,5
```

#### 12.4.4.4 构建环境

1、我这里使用的是`js`的环境，所以需要安装`node.js`和`npm`，但是`jenkins`默认是没有安装对应的环境

2、进入该目录，搜索`node.js`并且执行`install without restart`表示安装`node.js`

![image-20230516140132443](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320497.png)

3、这个时候就可以看到`node.js`的配置了

![image-20230516140445223](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320517.png)

按照下面的方式来配置`node.js`的环境，我们点击保存之后会自动下载并安装

![image-20230516140617760](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320243.png)

4、这个时候在`构建环境`中就可以看到`node & npm`的配置选项了

![image-20230516140804579](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320264.png)

5、我们选择`build steps`中的`执行shell`，我们按照下面写好的进行配置即可

![image-20230516140918651](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320288.png)

构建执行的任务：

- 查看 Node 的版本等是否有问题；
- 执行 `npm install` 安装项目的依赖；
- 移除原来 mall_cms 文件的所有内容；
- 将打包的 dist 文件夹内容移动到 mall_cms 文件夹；

```shell
pwd
node -v
npm -v

npm install
npm run build

pwd

echo '构建成功'

ls

# 删除/root/aribnb文件夹里所有的内容
rm -rf /root/aribnb/*

cp -rf ./build/* /root/aribnb/
```

#### 12.4.4.5 Jenkins 用户

1、我们选择立即构建可以返现，我们无法删除内容，这是因为`jenkins`权限不够

![image-20230516142756991](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320339.png)

2、我们后面会访问 centos 中的某些文件夹，默认 Jenkins 使用的用户是 `jenkins`，可能会没有访问权限，所以我们需要修改一下它的用户：修改文件的路径：`/etc/sysconfig/jenkins`

![image-20230516141611938](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032320384.png)

3、我按照上面的方式修改不行，所以我们按照下面的方式来处理

```shell
# 也可以将Jenkins添加到root组中
sudo usermod -a -G root jenkins # 我使用的该方式

# 也可以给Jenkins目录权限
chown -R jenkins  /xxx/xxx (chown -R jenkins /root/aribnb)

systemctl restart jenkins
```
