前端系统课 - coderwhy - react

# 1. 非脚手架 - 非 Hook

## 1.1 基本介绍

### 1.1.1 基本了解

> 基本介绍

![image-20221114091937171](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322008.png)

> 技术特点

![image-20221114093027064](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322041.png)

> Vue/React 选择

![image-20221114093446032](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322036.png)

> React 技术介绍

![image-20221114103514514](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322048.png)

### 1.1.2 依赖认识

其中`react`需要依赖 3 个包，每个包都各司其职

![image-20221114105329125](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322068.png)

其中`babel和react`的的关系，主要用于将`jsx语法`转化为`react`的语法 ![image-20221114105551889](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322060.png)

## 1.2 基本使用

### 1.2.1 Hello React！

因为我们这里使用的是`非脚手架`的环境，所以需要额外的引入 3 个包

```bash
// cdn引入的地址
https://unpkg.com/react@18/umd/react.development.js // 引入react
https://unpkg.com/react-dom@18/umd/react-dom.development.js // 引入react-dom
https://unpkg.com/babel-standalone@6/babel.min.js // 引入babel
```

下面就是基本的使用，其中包含了很多与`Vue`不一样的地方

![image-20221114111049207](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322987.png)

下面就是实现简单的`数据绑定`和`事件绑定`，里面暴露出来的语法和`Vue`是完全不一样的

1.模板语法不一样：在`Vue`中使用`{{ }}`来展示数据，但是`React`使用`{ }`来展示数据

2.事件绑定不一样：在`Vue`中使用`@click="btnClick"`表示事件绑定，但是在`React`表示使用`onClick={btnClick}`

3.数据渲染不一样：在`Vue`中定义的响应式数据变化，模板就会变化。但是在`React`中就需要重新调用`root.render()`来重新渲染才可以

![image-20221114112459599](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322005.png)

### 1.2.2 Hello React！组件化重构

> 1.定义组件

这里暂时是使用`类`来定义一个组件

![image-20221114181307738](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322022.png)

> 2.数据依赖

![image-20221114182017518](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322040.png)

> 3.事件绑定

![image-20221114213012984](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322063.png)

这里面存在一个`this`引用的问题，我们通过下面的方式就是一个`默认绑定`，所以按照常规的处理方式，这个`this`就绑定的`window`，但是最后的结果是`undefined`。

1.这个就是因为在`严格模式`下，`默认绑定`的`this`就是`undefined`，而且在`ES6`下定义的`class`内部就默认是严格模式，所以是`undefined`

![image-20221114204026529](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322086.png)

2.我们直接在`script`中写的，并且直接调用`foo`的话，里面的`this`也会是`undefined`。这是因为`react`的`babel`在转换代码之后默认开启了严格模式

![image-20221114205158849](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322839.png)

了解了上面`React`的`this`的运行机制，所以我们再来看下`React`如何进行事件绑定。因为我们继承了`React.Component`，所以我们重写里面的方法`render`，这里面的`this`默认绑定的是里面的是`App`组件，所以这里我们使用`bind`来显式绑定数据，然后在`ChangeMessage`中调用`App组件`中的`setState`

![image-20221114211808360](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322859.png)

或者我们先在`constructor`中提前对`方法`进行绑定，再来进行调用也可以

![image-20221114212621416](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322886.png)

### 1.2.3 列表遍历

因为`React`比较灵活，所以存在很多的`列表遍历`的方式

> 1.

我们将数组遍历出来，然后通过`li`的`虚拟DOM`遍历处理。这样再传递给`render`，这样就可以自动遍历里面的数组

![image-20221114215613990](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322954.png)

> 2.

其实遍历的本质就是将`数据`传输给`标签`，然后将该数组遍历渲染，所以我们不如直接`map`遍历展示。这里就展示了`React`的灵活处理的方式

![image-20221114215821351](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322005.png)

### 1.2.4 计数器

下面就是`React`实现`计数器`的方式，只要理解了`Hello React!组件化重构`中的逻辑，就知道这里的逻辑

![image-20221114223702620](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322037.png)

## 1.3 JSX

### 1.3.1 基本介绍

![image-20221114225117228](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322612.png)

> React 为什么选择 JSX?

![image-20221114225734764](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322648.png)

> 书写规范

![image-20221114225925911](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322689.png)

### 1.3.2 编写注释

在`React`中编写注释的话需要使用下面的`{/* 这是一个注释 */}`

![image-20221114230442992](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322724.png)

### 1.3.3 模板语法

![image-20221114231353540](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322767.png)

我们使用模板语法必须要遵守下面的 3 条规则

![image-20221114231302059](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322822.png)

当然我们不只是传入基本的数据类型，我们还可以传入`表达式`。和`Vue`的处理语法是一样的

![image-20221115090709796](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322423.png)

### 1.3.4 属性绑定

#### 1.3.4.1 基本属性

我们使用下面的`{ }`就可以对元素中的属性进行绑定处理

![image-20221115091520343](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322446.png)

#### 1.3.4.2 绑定 Class

我们一般使用下面的 3 个方式来对`class`进行动态的绑定。并且这里推荐使用`className`来绑定

这里来说下数组形式，因为我们默认将数组丢进`{ }`中的话，默认拆解的是`abc,cba,active`，所以这里我们先使用`join`来拆分即可

![image-20221115092552732](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322470.png)

#### 1.3.4.3 绑定 Style

我们使用下面的方式来绑定样式

![image-20221115093656689](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322499.png)

### 1.3.5 事件绑定

#### 1.3.5.1 基本使用

其他的基础部分可以参考`1.2 基本使用`中的 4 个案例，下面是介绍`this绑定`的 3 个方式

#### 1.3.5.2 this 绑定

1.使用`bind`来绑定，这个可以参考上面的`this绑定`

2.这里使用的是`Class Field`来处理，也就是成员字段。首先需要知道一个知识，在`Class`中定义的成员字段在任何其他地方都可以通过`this.xxx`来获取，所以可以在`render`中获取。因为绑定的是箭头函数，所以会根据作用域向上查询，就会找到`App`

3.这个是直接使用箭头函数来处理。本质是`() => { this.addCountArrow() }`，只要点击之后就会执行箭头函数，所以就会执行里面的`addCountArrow()`函数，因为`render`中的`this`是指向该组件实例的，所以相当于隐式绑定的方式来调用

![image-20221116095003837](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322524.png)

#### 1.3.5.3 event 处理

1.我们使用`bind`和`class field`调用的函数，默认就会传递一个`event`参数，所以直接获取即可

![image-20221116111143786](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322565.png)

2.但是对于第三种方式`箭头函数`的处理方式就不存在`event`，因为内部本质在调用`箭头函数`，所以这个箭头函数是有`event`，但是对于最后调用的函数并不存在`event`

![image-20221116111510524](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322228.png)

所以我们直接将`箭头函数`中的`event`传递给调用的函数就可以处理了

![image-20221116111805745](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322254.png)

#### 1.3.5.4 参数传递

1.我们使用`bind`来传输参数，可以进行传递。但是会出现左图中的问题，`event`出现了在了最后

![image-20221116112102165](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322281.png)

在了解上面的知识之前可以先看下面的原理，我们在使用`bind`调用的时候首先先传入`张三,16`的数据，这个时候就会占用`foo函数`中的前 2 个参数，这个时候我们再来调用`fn`再来传入数据就会占用`height`

![image-20221116112359266](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322309.png)

所以上图中的`bind绑定`来传输参数也是这个原因

![image-20221116112823448](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322339.png)

2.当然假如我们使用的是第三种方式的话，直接給该函数传递参数就可以了，不需要按照上面的方式处理

![image-20221116113023925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322366.png)

3.对于参数传递中我们可以参考下面的这个案例，点击左边的电影就会更改颜色。这个本质就是一个排他的思想

![image-20221116115825501](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322973.png)

### 1.3.6 条件渲染

1.其中`条件渲染`存在下面的 3 种方式的处理；其中第一个就是通过`if`判断，适合逻辑较多的情况处理；但是对于第二种情况，使用三元运算符的，这个就是比较推荐逻辑较少的情况来使用；第三种情况比较当某一个值可能为空的情况的话，所以比较适合网络请求的数据中

![image-20221116122606580](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322998.png)

其中第 3 个条件渲染的方式，比较适合在网络请求中进行处理。比如下面的`firends`是一个网络请求中数据，所以一开始的值为`null`，那么我们使用`firend.name`或`firend.age`的时候会报错，所以我们可以使用下面的`&& and ||`来处理

当然`React`本身就是比较灵活的，所以这里的知识一个参考，可能它本身有其他的用处

![image-20221116123202228](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322021.png)

2.当然在`vue`中还存在`v-show`的效果，在`react`中也可以实现相应的`v-show`的处理方式。我们使用`style`的方式对元素的`display`属性进行处理即可

![image-20221116151723697](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322052.png)

### 1.3.7 列表渲染

![image-20221116152351783](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322083.png)

1.下面就是一个基本的使用，在前面的`1.2 基本使用 列表遍历`中就已经演示过了

![image-20221116153114589](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322106.png)

2.当然我们也可以对数组进行处理再来展示，来实现一些展示的需求

![image-20221116153729050](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322823.png)

但是对于`Reacr`中的列表循环，我们也可以对要展示的数据进行链式调用处理，再来展示

![image-20221116153924993](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322845.png)

## 1.4 JSX 本质

### 1.4.1 基本介绍

![image-20221116154748732](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322866.png)

### 1.4.2 babel 转换

我们可以在`babel`的官网（[Babel · The compiler for next generation JavaScript (babeljs.io)](https://babeljs.io/repl/#?browsers=defaults%2C not ie 11%2C not ie_mob 11&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=BQKABBlRA8AmBLAbgPnNDtFLAYwDYCGAzsQHKEC2ApgLwBEAFtYXNQE70qBpmYK4ZMAemxpMmeMjxFSFGg1wB7AHYAXaiq7pRGGAFd8IraJj4EKQKGKgTu0AjIJMHD2u5YBMt05odRjpywGY39p5ggnqBhoLCHuHYkiTkVHT0AGby8qqcKIB8OvxCyGFiuahR0ACUQA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=react%2Cstage-2&prettier=false&targets=&version=7.20.4&externalPlugins=&assumptions={})）对`jsx`的语法进行转换，我们可以发现其实本质就是`React.createElement`的函数

![image-20221116155715540](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322894.png)

假如我们不使用`babel`，直接将`React.createElement()`在我们的代码中使用，也是可以渲染出页面。

![image-20221116160155997](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322926.png)

我们使用`React.createElement`也可以对页面进行渲染

![image-20221116160351370](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322968.png)

### 1.4.3 虚拟 DOM

我们这里打印使用`React.createElement`创建的节点，可以来查看虚拟`DOM`

![image-20221116164351121](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322692.png)

下面就是转换的过程，对于这些虚拟`DOM`在`Vue`中有相应的解释，也可以套在`React`

![image-20221116164441414](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322718.png)

### 1.4.4 声明式编程

![image-20221116165845026](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322741.png)

## 1.5 购物车案例

下面是我自己实现的写法

```react
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
    <script src="../依赖包/react.development.js"></script>
    <script src="../依赖包/react-dom.development.js"></script>
    <script src="../依赖包/babel.min.js"></script>

    <div id="root"></div>

    <script type="text/babel">
      class App extends React.Component {
        constructor() {
          super();
          this.state = {
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
        }
        countBookNum(index, count) {
          let newBookList = [...this.state.booklist];
          newBookList[index].num += count;

          this.setState({
            booklist: newBookList,
          });
        }
        removeBook(index) {
          let newBookList = [...this.state.booklist];
          newBookList.splice(index, 1);

          this.setState({
            booklist: newBookList,
          });
        }
        countBookPrice(item) {
          return item.num * item.price;
        }
        formatBookPrice(price) {
          return `￥${price}`;
        }
        countBookTotalPrice(booklist) {
          const total = booklist.reduce((preValue, oldValue) => {
            return preValue + oldValue.num * oldValue.price;
          }, 0);

          return total;
        }
        selectBook(index) {
          if (index == this.state.currentIndex) {
            this.setState({
              currentIndex: -1,
            });
          } else {
            this.setState({
              currentIndex: index,
            });
          }
        }
        renderBookTable() {
          const { booklist, currentIndex } = this.state;
          const { countBookPrice, formatBookPrice, countBookTotalPrice } = this;

          return (
            <div>
              <table className="BookTable">
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
                  {booklist.map((item, index) => (
                    <tr
                      key={index}
                      className={currentIndex == index ? "SelectTr" : ""}
                    >
                      <td onClick={() => this.selectBook(index)}>{item.id}</td>
                      <td>{item.name}</td>
                      <td>{item.time}</td>
                      <td>{formatBookPrice(countBookPrice(item))}</td>
                      <td>
                        <button
                          onClick={() => this.countBookNum(index, -1)}
                          disabled={item.num <= 0}
                        >
                          -1
                        </button>
                        {item.num}
                        <button onClick={() => this.countBookNum(index, 1)}>
                          +1
                        </button>
                      </td>
                      <td>
                        <button onClick={() => this.removeBook(index)}>
                          删除
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
              <h3>总价：{formatBookPrice(countBookTotalPrice(booklist))}</h3>
            </div>
          );
        }
        renderNullBookTable() {
          return (
            <div>
              <h3>没有更多的数据~</h3>
            </div>
          );
        }
        render() {
          const { booklist } = this.state;

          return (
            <div>
              {booklist.length == 0
                ? this.renderNullBookTable()
                : this.renderBookTable()}
            </div>
          );
        }
      }

      const root = ReactDOM.createRoot(document.querySelector("#root"));
      root.render(<App />);
    </script>
  </body>
</html>

```

下面是老师实现的方式

![image-20221116211731463](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322769.png)

1.对于`totalReduce`和`formatePrice`的方法进行抽取，这样可以有更多的组件进行使用，对于组件中可以抽取到一个单独的文件中

2.首先是对于`addNum`和`subNum`的实现原理，在`react`中对这些数据进行处理的方式就是将原本的数据进行浅拷贝一份，对该数据进行处理，然后再将数据赋值到原本的变量中。

并且老师写的案例中再次使用到了封装的思想，因为整体的逻辑基本一样，只是加减的不同，这里直接直接抽取为`changeNum`来处理

3.还有一个就是关于`数据删除显示“没有更多的数据了~”`的处理方式，本质就是`v-if`的处理。我之前使用的方式阅读性不是很强，所以不是很推荐我之前的写法，我这里将渲染的`虚拟DOM`作为函数封装起来处理，通过返回值的方式来处理

```react
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
    <script src="./依赖包/react.development.js"></script>
    <script src="./依赖包/react-dom.development.js"></script>
    <script src="./依赖包/babel.min.js"></script>

    <div id="root"></div>

    <script type="text/babel">
      class App extends React.Component {
        constructor() {
          super();
          this.state = {
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
        }
        changeNum(index, count) {
          const newBookList = [...this.state.booklist];
          newBookList[index].num += count;

          this.setState({
            booklist: newBookList,
          });
        }
        removeItem(index) {
          const newBookList = [...this.state.booklist];
          newBookList.splice(index, 1);

          this.setState({
            booklist: newBookList,
          });
        }
        selectBook(id) {
          this.setState({
            currentIndex: id,
          });
        }
        totalReduce(item) {
          return item.reduce((preValue, oldValue) => {
            return preValue + oldValue.num * oldValue.price;
          }, 0);
        }
        formatePrice(price) {
          return `￥${Number(price).toFixed(2)}`;
        }
        renderBooksList() {
          const { booklist, currentIndex } = this.state;
          const { totalReduce, formatePrice } = this;

          return (
            <div>
              <table className="BookTable">
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
                  {booklist.map((item, index) => {
                    return (
                      <tr
                        key={index}
                        className={currentIndex === item.id ? "SelectTr" : ""}
                      >
                        <td onClick={() => this.selectBook(item.id)}>
                          {item.id}
                        </td>
                        <td>{item.name}</td>
                        <td>{item.time}</td>
                        <td>{formatePrice(item.price * item.num)}</td>
                        <td>
                          <button
                            onClick={() => this.changeNum(index, -1)}
                            disabled={item.num <= 0}
                          >
                            -
                          </button>
                          {item.num}
                          <button onClick={() => this.changeNum(index, 1)}>
                            +
                          </button>
                        </td>
                        <td>
                          <button onClick={() => this.removeItem(index)}>
                            移除
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
              <h3>总计：{formatePrice(totalReduce(booklist))}</h3>
            </div>
          );
        }
        renderBooksEmpty() {
          return <h2>没有更多的数据了~</h2>;
        }
        render() {
          const { booklist } = this.state;

          return (
            <div>
              <div className="BookTable">
                {booklist.length <= 0
                  ? this.renderBooksEmpty()
                  : this.renderBooksList()}
              </div>
            </div>
          );
        }
      }

      const root = ReactDOM.createRoot(document.querySelector("#root"));
      root.render(<App />);
    </script>
  </body>
</html>
```

# 2. 脚手架 - 非 Hook

## 2.1 基本介绍

![image-20221116212352113](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322794.png)

![image-20221116212800001](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322818.png)

## 2.2 基本使用

### 2.2.1 开始项目

> 基本使用

```bash
npm i create-app-react  // 安装react
```

我们使用`create-react-app`来创建`react`项目

```
npx create-react-app xxx // 使用脚手架创建项目 项目名不能大写
```

> 目录结构分析

![image-20221116214237425](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322448.png)

> Hello World!

我们就是使用下面的方式进行组件化的开发，其实本质和`Vue`是差不多的。每个`jsx`文件就是作为一个组件存在

![image-20221116224249333](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322470.png)

### 2.2.2 基本概念

> 了解 PWA

`MDN`官方文档：[渐进式 Web 应用（PWA） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/Progressive_web_apps)

其实`PWA`的本质就是将`web页面`添加到`手机主页面`中，作为一个`手机App`来启动。但是技术在国内的公司用的比较少，所以只是了解一下

![image-20221116222035059](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322496.png)

> 了解 robots

这个是为`爬虫`指定爬取的数据

![image-20221116222516738](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322522.png)

> webpack 配置

`React`对于`webpack`是进行隐藏的处理，假如你想查看的话可以参考下面的`react-scripts`文件夹下面的文件

![image-20221116224807198](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322542.png)

当然我们不想这么麻烦的话，可以使用`npm run eject`来显示，这个操作是不可逆的，所以不是很推荐来使用。假如运行失败的话可以尝试提交代码之后再来尝试

![image-20221116225129650](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322567.png)

> 组件化

![image-20221117181259723](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322282.png)

## 2.3 组件化

### 2.3.1 类组件

> 基本使用

![image-20221117211129057](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322303.png)

我们使用`类组件`来渲染下面的页面，这个在前面演示了很多次了

![image-20221117221405823](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322327.png)

> render 返回值

![image-20221118223537683](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322348.png)

`render`返回值可以返回下面的基础结构

![image-20221118224128050](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322433.png)

### 2.3.2 函数组件

> 基本使用

![image-20221118224636708](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322458.png)

我们使用下面的方式来创建一个函数式组件

![image-20221118224707874](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322996.png)

## 2.4 生命周期

### 2.4.1 基本使用

![image-20221118230146042](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322021.png)

> 基础生命周期 - constructor/render

1、我们认为的组件其实本质是一个个的`class`，所以每使用一个组件的话就会`new xxx()`创建一个实例，所以会优先执行`constructor`。其中`constructor`作为一个生命周期其主要做的事情就是`绑定事件`、`初始化state`

2、随后就是执行`对象`的实例方法`render`来重新渲染页面

![image-20221118231317540](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322041.png)

> 挂载 - 更新

1、其中`挂载`和`更新`的生命周期分别是`componentDidMount`、`componentDidUpdate`

2、`componentDidMount`作为一个挂载的地方，最好的应用场景是`网络请求`、`事件绑定`、`DOM操作`

3、`componentDidUpdate`当`state`中的数据更新之后回调的函数，里面包含了`3`个参数，参数分别是`preProp`、`preState`、`snapshot`。其中前 2 个表示更新前的数据，所以在网络请求中需要比对数据的话可以使用。第 3 个表示`getSnapShotBeforeUpdate`回调函数传递来的数据

![image-20221118231647471](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322071.png)

> 卸载

![image-20221118231902582](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322114.png)

### 2.4.3 不常用周期

![image-20221119092759667](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322173.png)

> shouldComponentUpdate

`shouldComponentUpdate`返回值为`false`的话就不会重新渲染页面，返回为`true`的话就会重新渲染

![image-20221119093518974](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322797.png)

> getSnapshotBeforeUpdate

这个是为了给`ComponentDidUpdate`传递第三个参数，为了作数据比对

![image-20221119093829845](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322815.png)

## 2.5 组件通信

### 2.5.1 props - 父传子

> 基本使用

`props`主要是用于**父传子**，其中也存在 2 种形式来处理。

1、第一种就是自身存在`state`的话需要将`props`传给`super()`处理

2、假如没有`state`的话可以不写`super()`，系统会自动添加`props`

![image-20221119103429846](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322837.png)

当然为了应对这种传输得`props`比较多的情况，可以使用`...`语法来拆分属性处理

![image-20221119224354685](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322863.png)

> 网络请求处理

假如我们是网络请求的话也是类似的处理方式，在`componentDidMount()`生命周期函数中发送网络请求，将值以`props`的形式传输过来

![image-20221119114259991](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322888.png)

> 参数校验

更多的可以参考官网案例：[使用 PropTypes 进行类型检查 – React (reactjs.org)](https://zh-hans.reactjs.org/docs/typechecking-with-proptypes.html)

首先需要导入`PropTypes`的包，进行类型判定

![image-20221119171458577](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322939.png)

下面就是基本的`类型判定`和`默认值`

![image-20221119171446983](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322577.png)

### 2.5.2 props - 子传父

因为`React`本身并不存在事件总线这个说法，所以本质还是通过`props`传递函数。下面是记录的思考的过程

1、子组件需要传递数据给父组件，首先是自己存在数据，也就是下面的`addClick()`。

2、父组件需要接收到子组件传输来的数据，所以就会存在`addCount()`

3、父组件需要将这个函数传递给子组件处理，所以需要通过`props`的形式传输过去。然后再以参数的形式接收到父组件进行处理

4、因为我这里使用到的形式是`箭头函数`，所以传递参数的接收主体为这个`箭头函数`，所以最后的参数需要再传递给执行的函数才会执行

![image-20221119174223057](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322598.png)

![image-20221119182108723](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322623.png)

### 2.5.3 context - 非父子

#### 2.5.3.1 基本使用

`context`主要是实现上层组件向下层组件传递数据。假如要实现下层组件传递上去可以使用`events`

1、首先需要创建一个`Context`，将要传输的组件包裹，其中`value`表示要传输的值

![image-20221119225904159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322645.png)

2、然后将创建的`Context`传输给要使用的组件的`contextType`中，然后使用`this.context`即可获取

![image-20221119230053109](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322673.png)

#### 2.5.3.2 Consumer

> 1、函数式组件使用 Context

对于`函数式组件`使用`Context`，肯定不能按照`类组件`的使用方式来处理，因为不存在`xxx.contextType`的属性。所以需要使用`<xxxContext.Consumer>`的方式来接收参数

![image-20221119231436088](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322703.png)

> 2、嵌套使用/接收 Context

因为一个组件的`contextType`不能加入多个`Context`，所以应对这种多个`Context`嵌套的情况也可以使用`Consumer`的方式来接收数据

![image-20221119231948316](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322482.png)

如果需要使用到嵌套的`Provide`的话，就需要使用下面的嵌套`Consumer`，很明显这样的方式非常的复杂

![image-20230304234102593](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322506.png)

#### 2.5.3.3 默认参数

当我们不将组件放在`Context`，那么就会使用到`默认参数`。这个默认参数要写在`createContext()`中

![image-20221119232528693](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322532.png)

#### 2.5.3.3 相关 API

![image-20221119232706346](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322563.png)

![image-20221119232742802](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322584.png)

### 2.5.4 events - 非父子

`events`的方式可以实现`上级`对`下级`组件，也可以实现`下级`对`上级`组件的传递数据。这里使用的是老师自己封装的库，其实其他的库也大差不差，只需改名字即可

```bash
npm i hy-event-store
```

1、创建`eventBus`。使用`emit`发送数据，其中`sendInfo`表示事件名

![image-20221120174833201](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322605.png)

2、使用`on`表示接收数据

![image-20221120174946462](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322334.png)

## 2.6 插槽

### 2.6.1 基本使用

`React`的本身并不存在插槽的概念，因为本身`React`太灵活了，所以下面对`React`来说只是一个传值

> 方式一：children 方式

我们将插槽作为一个`children`值传输到`props`中显示处理，其实这个的本质就是`createElement()`的第三个参数，这段笔记可以参考我`JSX本质`中记录的笔记

![image-20221119184408928](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322356.png)

但是这个方式有一个缺点，当我们只传输一个`children`值得时候不是一个数组，而是一个元素。假如因为传输值得不同导致类型得不同就会出现很多得问题。而且索引得方式也会有很多得问题

![image-20221119184746222](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322375.png)

假如我们想要解决得话，可以使用`propTypes`来做类型判定。这样就有效的阻止了传输值得不同导致类型不同得问题

![image-20221119185001367](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322400.png)

> props

下面就是以`props`得方式来传输插槽，实现页面得渲染

![image-20221119214734843](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322430.png)

### 2.6.2 作用域插槽

作用域插槽可以参考我`Vue`得笔记。其主要是将`子组件`中的数据传输给父组件，然后再将组件传输给`子组件`渲染，这里重点的思想就是传输函数进去，调用函数渲染

![image-20221119222156983](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322465.png)

## 2.7 性能优化

### 2.7.1 setState 解析

#### 2.7.1.1 基本解析

![image-20221121094721898](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322222.png)

#### 2.7.1.2 3 种使用方式

对于`setState`有下面的 3 种使用方式来修改`state`中的数据

![image-20221121101118305](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322249.png)

#### 2.7.1.3 异步处理

> 为什么 setState 是异步更新？

![image-20221121112558115](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322271.png)

1、先解释一下`显著提升性能`，假如我们一次执行多个`setState`的话，就会执行多次`render()`。但是结果并不是这样，点击之后是获取到所有的`setState`，放入队列中一次都执行完。所以就会出现下面的`state.count`的值并不会`+3`的情况

![image-20221121112922312](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322299.png)

假如要实现累加的功能，就可以是要下面的方式来处理。

![](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322323.png)

2、还有一个就是`state`和`props`更新不同步的问题。假如我们这里的`setState`执行完需要一段时间，但是`state`的已经修改，假如不执行`render`函数，那么`props`就不会更新，所以就会出现更新不同步的问题

![image-20221121113724655](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322343.png)

> React 的 setState 一定是异步的吗？

在`React18之前`下面的操作都是同步的处理。但是在`React18`之后所有的处理都是实现的批处理，所以`setState`就是异步的调用

![image-20221121120050223](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322119.png)

> setState 实现同步处理

需要导入`flushSync`来进行`同步`的操作，当然`flushSync`内部依旧是异步的处理，只有`flushSync函数`外面的执行是同步的

![image-20221121120838811](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322144.png)

### 2.7.2 diff 算法

> 更新流程

![image-20221121152620045](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322169.png)

> key 优点

![image-20221121152645421](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322194.png)

### 2.7.3 render 优化

#### 2.7.3.1 基本优化

当我们一开始进入网页的时候会自动执行一遍`App render`，或者数据修改的时候都会自动执行一遍`App render`。即便下面的子组件里面的数据没有发生修改，也会执行一遍`render`，这个是非常消耗性能。所以我们可以使用`shouldComponentUpdate`来更新数据

![image-20221121155221899](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322225.png)

1、首先是对`App`的性能优化。当数据是一样的话，就让`shouldComponentUpdate`返回为`false`，不去重新调用`render`函数

![image-20221121160256521](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322274.png)

2、然后就是对于`父组件`传递给`子组件`的`props`的优化处理，当传入的值和原本的不一样的话就修改

![image-20221121160629548](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322053.png)

但是使用这种方式来处理的话会非常的麻烦，所以一般都不使用这种方式。这个只是下面的`PureComponent`的实现原理

#### 2.7.3.2 PureComponent

一直写`shouldComponentUpdate`的话会很麻烦，假如我们要实现上面一样的功能就可以使用`pureComponent`来处理，但是这个处理只是`浅层次`的拷贝

![image-20221121161112914](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322074.png)

![image-20221121161055909](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322091.png)

#### 2.7.3.3 memo

因为`PureComponent`是一个类，对于`类组件`可以使用继承来处理。但是对于函数组件来说就需要使用并不能实现相应处理，所以就需要使用`memo`高阶函数来处理优化

![image-20221121162511749](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322128.png)

![image-20221121162450975](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322156.png)

### 2.7.4 数据不可变

假如我们继承的是`Component`的话，我们使用下面的数据添加的方式，依旧会渲染 。

但是这种方式很大的弊端，不建议使用，因为`PureComponent`中有一个`shallowEquals`比较，也就是浅比较，直接将`bookList`是否等于`newBookList`，也就是比较的内存值，并不关心内部值得变化![image-20221121164613841](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322189.png)

假如我们使用的是`PureComponent`的话，上面这种方式就会失效。因为为了后续的性能优化，大部分的组件都会使用`PureComponent`来处理，我们依旧使用上面的方式来赋值渲染的话显然会出现问题。所以处理的方式依旧是先`浅拷贝`处理，然后对这个数据进行处理，然后再赋值为`state`来渲染。

这个就是数据不可变的魅力，原本的`this.state`中的数据就是不可变的，如果需要修改的话直接整个替换处理

![image-20221121165125569](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322818.png)

但是对于使用`...`来浅拷贝得数据，都是一个指向得一个对象。所以我们修改里面得值得话都是一样得，但是为什么最后不允许使用`this.state.xxxx`来修改数据呢？这是因为底层使用到得就是一个浅层次得比较，我们使用原本得`this.state.xxx`得方式来修改得话，对于`React`来说依旧是没有修改得，在继承`PureComponent`得情况下这种方式就不会生效

![image-20221121171343904](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322845.png)

## 2.8 refs

### 2.8.1 原生 DOM

我们可以使用下面得三种方式来获取`原生DOM`

![image-20221121173111174](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322866.png)

### 2.8.2 组件

> 类组件

我们可以使用`createRef()`来获取到组件得实例，因为获取了实例，所以也可以重新调用函数

![image-20221121174448109](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322898.png)

> 函数组件

我们需要使用`forwardRef`高阶函数包裹处理，这样回调函数中就会出现二个参数`ref`来获取元素

![image-20221121174853615](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322921.png)

## 2.9 表单

### 2.9.1 受控组件区分

> 非受控组件

我们是要监听表单的话，可以使用`onChange`来监听数据的变化，数据通过`e`来传递给`username`处理，再渲染到页面即可，我们通过整个方式还可以控制表单，所以是`非受控组件`

![image-20221122163437314](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322967.png)

> 受控组件

当表单元素被`React`接替的话就是受控组件，因为我们操作不了表单元素，这个时候就需要使用`onChange`事件来处理`value`值得改变

![image-20221122165445121](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322797.png)

### 2.9.2 基本使用

假如我们要使用`表单`的话就可以使用下面的方式来实现数据的`双向绑定`

![image-20221122165535928](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322823.png)

### 2.9.3 提交数据

> 表单提交 - form

对与现在项目表单提交得方式使用的场景比较有限，为了实现不刷新页面提交，一般都不会通过`form`来提交数据

![image-20221123164320231](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322844.png)

> 表单提交 - ajax

1、假如我们不想使用浏览器的发送请求，可以添加`onSubmit`事件，在这个事件中阻止默认行为，获取数据发送

2、因为存在多个表单，所以我们可以写一个通用的函数`changeUserAndPass`来处理。其中对象名使用计算属性`[ ]`获取；`e.target.name`就是对应的`input`中的`name`；`e.target.value`就是对应的`input`中的`value`

![image-20221123172603981](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322866.png)

### 2.9.4 checkbox

> 单个

对于单个`checkbox`来说，本质就是对于`isAgree`的控制

![image-20221123183303716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322896.png)

> 多个

这个的本质就是使用一个自定义的数组`hobbies`来处理，只要改变的话就改变这个数组，然后页面进行渲染

![image-20221123184422912](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322921.png)

### 2.9.5 select

> 多个

1、下面就是对于`select`的处理方式，其中对于`selct`的`value`本质是通过`React`控制的，对于原生的`HTML5`中是不存在这种处理方式

2、对于`Array.from(...)`这种本质是将一个`Collection`类数组转换为一个数组，因为`Collection`本质是一个可迭代对象，所以可以转换，这个在`ES6`中的`arguments`有记录笔记。

3、其中`Array.from(...)`的第二个参数是一个`map`的回调，本来我们需要将`hobbies.map(item => item.value)`来额外处理，但是`Array.from()`提供了处理方式，所以我们直接使用即可

![image-20221123192614820](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322702.png)

> 单个

![image-20221123193317925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322724.png)

### 2.9.6 非受控组件取值

1、我们也可以使用非受控组件来取值，那就是使用`ref`处理获取`原生DOM`中的`value`来处理

2、`defaultValue`这个也可以默认设置`value`值，但是这个是为`非受控组件`设计的。`value`是为`受控组件`设计的

![image-20221123194138911](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322751.png)

## 2.10 高阶组件

### 2.10.1 基本介绍

![image-20221211161637355](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322778.png)

下面为基本的使用，所以可以理解`高阶组件`其实就是`高阶函数`。并且`React`并不是`ReactAPI`的一部分，而是一种设计模式

![image-20221211162644564](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322805.png)

### 2.10.2 应用场景

#### 2.10.1.1 props 增强

> 基本使用

下面就是对`props`的处理，这样只要传入的组件，里面都会带上`personInfo`的`props`

![image-20221211165733176](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322828.png)

当然我们传递`类组件`和`函数组件`也是可以的，只要经过`enhancedProps`的高阶函数，那么就会自动带上`props`

![image-20221211165914027](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322688.png)

![image-20221211170002432](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322711.png)

#### 2.10.1.2 Context 封装

其中一个就是对于`Context`的高阶处理，这里可以参考我`Context`的笔记，里面的传值和取值很麻烦，所以我们直接使用高阶函数来抽象，这样更易维护

下面的`enhancedContext`就是对`Context`取值的抽象处理

![image-20221211183631607](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322738.png)

对于封装好的`enhancedContext`直接使用即可，最后作为`props`的值来处理

![image-20221211184110481](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322763.png)

#### 2.10.1.3 登录鉴权

我们还可以使用`高阶组件`来做登录鉴权的处理，只需要将需要登录鉴权的组件放入`loginAuth`即可

![image-20221211190013123](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322794.png)

放入`loginAuth`的`高阶组件`即可对登录进行鉴权处理

![image-20221211190122504](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322820.png)

#### 2.10.1.4 生命周期劫持

我们也可以对`生命周期`进行劫持处理，这样我们就可以计算该组件的`渲染时间`

![image-20221211195516792](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322671.png)

![image-20221211195541051](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322694.png)

### 2.10.3 HOC 意义

其中对于`memo`、`forwardRef`都是一个`高阶函数`

![image-20221211200116390](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322713.png)

### 2.10.4 createPortal

![image-20221211204918399](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322739.png)

我们使用`createPortal`就可以将该组件转移到`div的home`中，这样就可以实现一些特殊的操作。不能直接在`App`中返回`createPortal函数`，这样就会报错

![image-20221211203246176](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322764.png)

\*我们还可以将插槽中的值进行传进`createPortal`中

## 2.11 Fragment

可以理解为`Vue`中的`template`，作为一个`片段`来处理，最后是不会渲染到页面中

![image-20221211211600887](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322785.png)

当然`Fragment`存在一个`语法糖`的写法。但是这种语法糖对于使用`map`遍历的时候不能使用，因为需要在里面添加上`key`，如果使用下面的`语法糖`的话就不能添加`key`了

![image-20221211211735028](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322518.png)

## 2.12 StrictMode

### 2.12.1 基本使用

![image-20221211212657256](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322539.png)

我们使用`StrictMode`包裹的组件就会在内部开启严格模式，即便里面有组件的嵌套

![image-20221211213010257](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322558.png)

### 2.12.2 检测范围

![image-20221211213849775](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322580.png)

比如下面就是会自动检测是否使用`React`过时的`API`，就会报错处理

![image-20221211213057211](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322607.png)

## 2.13 过渡动画

### 2.13.1 基本介绍

`React`现在本身是没有集成`动画库`，所以需要我们自己来下载使用，下面使用的就是官方推荐得`react-transition-group`动画库

![image-20221211214518529](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322629.png)

该库中包含下面得 4 种组件，我们一般都是使用的`CSSTransition`组件来实现过渡动画

![image-20221212092257583](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322312.png)

其中`appear`表示第一次展示的时候的状态，`enter`表示进入的时候的状态，而`exit`表示离开状态

![image-20221212093238576](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322335.png)

### 2.13.2 CSSTransition

下面就是基本的使用过程

1、使用`CSSTransition`包裹，并且下面只能由一个子元素，如果存在多个的话就会报错

2、其中`in`表示`开启`和`结束`得控制，`true`表示开启，`false`表示结束。并且`unmountOnExit`表示动画结束之后将`组件移除`

3、`timeout`是表示动画的时间，也就是`transition`中的`2s`，这里表示的是`ms`

4、动画首先是执行`why-enter`和`why-enter-active`，然后再来执行`why-enter-done`

![image-20221212095523905](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322353.png)

5、我们添加了`appear`属性表示组件刚刚加载得时候出现得动画

![image-20221214161049129](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322375.png)

### 2.13.3 钩子函数

我们只要经过了执行得动画之后就会执行`钩子函数`

![image-20221214162039547](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322402.png)

### 2.13.4 SwitchTransition

![image-20221214164412938](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322432.png)

1、`SwitchTransition`表示该组件用于动画得切换效果，其中`mode`表示动画显示得模式，`out-in`表示动画主体先移走再移入

2、其实本质就是`SwitchTransition`控制`CSSTransition`得动画，下面得`key`就表示得`in`

![image-20221214163909310](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322214.png)

![86](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322241.gif)

### 2.13.5 TransitionGroup

使用`TransitionGroup`来包裹多个动画组件，其中`component`属性表示要包裹下面得标签

![image-20221214173250918](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322263.png)

![动画86](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322297.gif)

## 2.14 CSS 编写

### 2.14.1 基本介绍

> 组件化开发下的 CSS

![image-20221219201538477](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322325.png)

> React 中的 CSS

![image-20221219202002782](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322348.png)

### 2.14.2 编写方式

#### 2.14.2.1 内联样式

![image-20221219203726047](D:\lib\图片素材\image-20221219203726047.png)

1、我们可以使用对象的形式来编写样式

2、因为在对象中不存在`background-back`的写法，所以就需要使用驼峰写法

3、我们也可以编写`state`来动态控制样式属性值

![image-20221219205021548](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322023.png)

#### 2.14.2.2 普通方式

![image-20221219221421704](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322047.png)

就是将`.css`文件引入来使用，这种方式就是样式都会互相影响

![image-20221219221403670](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322071.png)

#### 2.14.2.3 CSS Module

![image-20221219222251142](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322090.png)

1、需要将`.css`改为`.module.css`的后缀方式，然后使用`模块化`的方式来导入

2、最后使用的话，就是`导入名.类名`的方式来使用。这样使用的话就不存在样式冲突的情况

![image-20221219222428237](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322135.png)

对于其他组件的使用也是一样的

![image-20221219222637169](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322299.png)

其实这个本质就是动态添加一个`独特`的类名，其中就是`组件名_类名__样式值`得方式来区分

![image-20221219222712547](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322809.png)

#### 2.14.2.4 CSS in JS

##### 2.14.2.4.1 基本介绍

![image-20221220201616759](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322830.png)

![image-20221220202136297](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322859.png)

##### 2.14.2.4.2 基本使用

```bash
npm i styled-components		// 安装styled
```

如果需要的话，可以下载一个`styled-components`的插件

![image-20221220222453611](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322892.png)

1、我们需要使用`styled.div`来创建一个`div`标签，最后导出包裹在要设置样式的地方

2、我们使用`模板字符串`来调用`styled.div`中的函数，里面就编写相应的样式即可

![image-20221220222715384](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322044.png)

里面的样式就是按照下面的规则来编写的

![image-20221220222954512](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322189.png)

##### 2.14.2.4.3 高级特性

> 1、样式抽取

和我们抽取组件是一样的，将相应的组件抽取出来使用

![image-20221220223448070](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322615.png)

> 2、props

我们可以使用`props`对其组件传递参数，最后使用的话就是使用箭头函数返回值处理

![image-20221220224516653](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322710.png)

> 3、默认值

1、其中`styled.div`存在一个`attrs`属性来设置默认值

2、其中`attrs`中的参数要是函数，下图中存在`({ ... })`的写法，其实是返回对象。如果只是写`{ }`的话就是函数的代码块了

3、作为默认值是使用`... || "xxx"`的形式来处理的

![image-20221221210448225](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322737.png)

> 4、实现继承

![image-20221221201505774](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322761.png)

##### 2.14.2.4.4 全局变量

我们有的时候需要将一些`CSS属性`抽取为全局的样式，所以设置一个属性值。其中`styled-components`为我们提供了下面的 2 种方式

> 主题样式

在要覆盖的组件中编写`ThemeProvider`组件，为组件提供`theme`属性，其中属性值为一个对象

![image-20221221205029536](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322788.png)

> 引入变量

我们可以单独编写一个文件`variables.js`文件，专门存储样式值。需要的时候使用`import`来引入使用

![image-20221220225425781](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322878.png)

### 2.14.3 动态 Class

> 传统方法

![image-20221221212800743](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322650.png)

> classnames 库

![image-20221221212909420](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322672.png)

```bash
npm i classnames // 安装classnames
```

其基本得使用和`Vue`中是差不多得

![image-20221221213440890](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322698.png)

# 3. 状态管理 - Redux

## 3.1 基本介绍

> 纯函数

具体参考`JS高级`中的笔记

![[00 assets/f02d7dade869f13b738afaacadce84e7_MD5.png|86]]

![image-20221222211325759](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322750.png)

> Redux 介绍

![image-20221222211956893](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322781.png)

> Redux 核心理念 - store

![[00 assets/df5bafe1b5664a3dfb3714237e8736f3_MD5.png|86]]

> Redux 核心理念 - action

![image-20221222212558400](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322466.png)

> Redux 核心理念 - reducer

![image-20221222212849625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322491.png)

## 3.2 非项目使用

### 3.2.1 基本使用

```bash
npm i redux	 // 安装redux
```

1、目前演示都是直接使用`Redux`原生函数，而非使用封装好的，所以比较繁琐

2、`reducer`函数执行之后返回的结果需要是一个对象

3、通过`dispatch()`传入的数据，会再执行一次`reducer函数`，并且传入的数据都会传入到`action`中

![image-20221222220051296](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322515.png)

### 3.2.2 优化处理

> reducer 选择和订阅模式优化

1、我们将`reducer`中的`if`改为`switch`，这样更易读

2、我们使用`store.subscribe()`来订阅，只要每次`dispatch`的话就会执行订阅函数

![image-20221222221111680](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322542.png)

> action 优化

1、将原本`{ type:xxx , name:xxx }`的形式的代码抽取为一个函数，放在`actionCreaters.js`中

![image-20221223102259833](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322605.png)

> reducer 常量抽取

1、一般情况每个`type`都会抽取到`constants.js`中作为一个常量

![image-20221223102703170](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322316.png)

> reducer 函数抽取

1、后期`reducer`函数会越来越大，所以建议将`reducer`函数抽到单独一个`.js`文件中处理

![image-20221223103449376](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322337.png)

### 3.2.3 使用流程

> Redux 三大原则

![image-20221223112317947](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322360.png)

> 使用过程

![image-20221223112819597](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322390.png)

![image-20221223113012867](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322419.png)

> Redux 结构划分

![image-20221223112952664](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322447.png)

## 3.3 React 使用

### 3.3.1 基本使用

其实一切的本质就是在`3.2`的笔记中，下面只是将其融合到`React项目`中

```bash
npm i redux		// 安装redux
```

1、其基本的逻辑和上面是类似的，文件结构都是一样

![image-20221223120907921](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322185.png)

2、随后就是相应的`.jsx`文件中的逻辑

![image-20221223121037637](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322207.png)

![image-20221223121048305](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322232.png)

### 3.3.2 React-redux

参考上面的代码会发现有很多重复的代码，比如`components`中组件的`订阅...`

![[00 assets/9c484cabd6526873c85f4066952cd98a_MD5.png|86]]

所以就需要一个高阶函数来处理这个情况，这样会让代码更加简单

```bash
npm i react-redux 	// 安装react-redux
```

1、首先我们需要为全局`App`提供`store`

![image-20221223154255208](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322286.png)

2、我们需要使用`state`的话，就需要使用函数`mapStateToProps`来映射。最后取值就是通过`props`来取值，因为底层就是通过高阶函数，将参数作为`props`传递给传入的组件

![image-20221223154437836](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322309.png)

3、我们需要使用`action`的话，也是一样传入一个函数`mapActionToProps`。将其中的`dispatch`封装到该函数返回的对象中，组件调用的话就是`this.props.xxx`来处理

![image-20221223154610412](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322143.png)

其中`action`就是我们一开始编写的`action`，这个和调用`store.dispatch()`是一样的，只不过迁移组件外的函数了

![image-20221223154957766](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322165.png)

4、我们使用`react-redux`的`connect`的时候，一定要注意`mapState`、`mapAction`的顺序，如果顺序反的话就会报错

![image-20230222163149179](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322188.png)

### 3.3.3 网络请求

#### 3.3.3.1 基本使用

在`mount`生命周期中发送网络请求，然后使用`action`来更新其中的数据

![image-20221223201100524](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322207.png)

#### 3.3.3.2 redux-thunk

![image-20221223201845474](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322236.png)

而且我们直接将网络请求写在`action`的话，这样就是直接返回`Promise`，那么还需要在`mapAction`中编写接收异步函数的代码，这样并不是将网络请求移到`redux`

![image-20221223215412859](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322265.png)

即便你将函数改为`async`的形式，因为`async`的函数默认会返回`Promise`，所以也不行

![image-20221223220046701](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322032.png)

所以这个时候我们就需要安装`redux-thunk`中间件来对`react-redux`增强

```bash
npm i redux-thunk	// 安装
```

![image-20221223221433289](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322053.png)

1、在`createStore`中使用`redux-thunk`中间件，这样`dispatch`就可以接收函数

![image-20221223220206685](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322075.png)

2、我们在`mapActionToProps`中`dispatch`其实只能接收对象，但是我们使用`redux-thunk`增强之后就会自动调用这个函数

3、我们在`action`中`fetchHomeMultidataAction`中返回的函数第一个参数就是`dispatch`，我们可以在该函数中`dispatch`来改变参数，第二个参数就是`getState`，可以获取`State`中的参数`getState().count`

4、下面这一套处理方式就是页面中`componentDidMount`生命周期中调用`mapActionToProps`，`getHomeMultidata`函数，然后执行`fetchHomeMultidataAction函数`，返回的函数就会被`redux-thunk`来执行，然后内部执行的就会调用`changeBannerAction`和`changeRecommendAction`方法，实现数据的改变

![image-20221223220834238](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322104.png)

### 3.3.4 开发工具

我们可以下载`redux devtools`和`react devtools`工具，和`vue.js devtools`工具是一样的

1、`github`中库的文件落后很多，所以建议在插件市场中下载

2、如果`react devtools`插件没显示的话，我们需要重新启动项目

![image-20221223223210437](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322129.png)

3、其中`redux devtools`工具默认是关闭，我们需要按照下面的步骤来开启

**官方网址**：[zalmoxisus/redux-devtools-extension: Redux DevTools extension. (github.com)](https://github.com/zalmoxisus/redux-devtools-extension)

![image-20221223223550207](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322153.png)

如果开启的话，我们就可以看到下面的`redux`的数据

![image-20221223223629617](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322882.png)

### 3.3.5 模块划分

> 基本使用

1、首先是对`store`模块进行划分处理，这里重点就是`index.js`导出各级模块的处理

![image-20221224105032089](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322902.png)

2、随后便是使用`combineReducers`对各级模块进行组合处理，下图中`counter`导入的就是`reducer`

![image-20221224104854417](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322925.png)

_这里需要补充关于模块导出的知识，在各级模块中使用`export default xxx`导出的时候，就需要使用`import xxx from "xxx"`来导入。使用`export _ from "xxx"`导出的模块，就需要使用`import { xxx } from "xxx"`来导入。或者直接使用`import \* as xxx from "xxx"`来全部导入

![image-20221224105617244](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322960.png)

3、我们使用`state`的时候需要加上你要使用库的名字，也就是`combinReducers`中设置的属性名

![image-20221224105758016](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322985.png)

其中对于直接用`redux`而非`react-redux`库的数据，也需要加上`库名`来区分数据

![image-20221224105855792](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322019.png)

> combinReucers 理解

![image-20221224110044441](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322596.png)

其实底层本质是执行下面的代码

![image-20221224110704912](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322619.png)

### 3.3.6 connect 实现

> 基本实现

左边就是`connect`的实现处理，其实原理很简单，就是将传入的数据遍历然后丢给传入组件的`props`中

![image-20221229221943754](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322639.png)

> store 解耦

此时`connect`需要传入`store`，所以这个封装的不是很好，所以我们需要将这个部分来解耦处理

1、我们创建一个`context`，并且传入`store`

![image-20230103223647591](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322659.png)

2、我们传入的`context`进行使用，此时就将封装的`高阶组件`进行解耦操作了

![image-20230103223824926](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322684.png)

3、其实`React-redux`本质就是进行上面的操作

![image-20230103224005769](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322712.png)

### 3.3.7 中间件

#### 3.3.7.1 基本介绍

![image-20230223195859106](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322564.png)

#### 3.3.7.2 中间件原理

![image-20230223195907467](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322585.png)

![image-20230224094701606](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322605.png)

1、下面其实就是`中间件`的原理，我们阻断原生的`dispatch`，中间加一个`Hook`。只要使用`store.dispatch`就等于去执行里面的`logDispatch`函数，这样就可以实现中间件的调用

![image-20230223195842086](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322632.png)

这样你就可以实现`log`的打印

![image-20230223200748293](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322669.png)

其实在函数内部也是可以去修改外部的对象值，上面修改`store`中的`dispatch`其实就是按照下面的原理来处理的

![image-20230223200225411](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322698.png)

2、我们也可以去编写`Redux-thunk`中间件，其原理基本和`log函数`是一样的，其实底层就是帮助我们来执行传入的函数

![image-20230223202637285](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322461.png)

对于`thunkDispatch`中`action()`回调传入的第一个参数最好是`store.dispatch`，因为可能存在`dispatch`中再去执行`dispatch`函数。我们希望传入的`dispatch`还能再调用`thunkDispatch`，所以最好传入`store.dispatch`，而非`next`

![image-20230223202929329](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322487.png)

#### 3.3.7.3 applyMiddleware

1、我们可以将`log`和`thunk`抽取到文件中来处理

![image-20230223204130712](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322509.png)

2、我们引入`applyMiddleware`，这个函数的作用就是将传入的中间件依次执行，并且赋值`store`

![image-20230223204425715](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322533.png)

3、我们在`index.js`中导入导出所有的函数即可

![image-20230223204626366](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322559.png)

## 3.4 ReduxToolKit

### 3.8.1 基本介绍

![image-20221224111513678](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322583.png)

### 3.8.2 基本使用

```bash
npm install @reduxjs/toolkit react-redux  // 安装TRK和react-redux
```

1、我们使用`@reduxjs/toolkit`中的`createSlice`来创建一个片段

2、其中`reducers`表示是`reduce`中的`action`，因为底层做了处理，所以我们直接使用`state.xxx`的方式来对数据进行修改。而非以前的传递`{ ... }`的形式

3、传给`action`的数据使用`payload`来接收

4、对于`actions`的导出是为了给`dispatch`使用的

5、最后要导出`slice`中的`reducer`来处理

![image-20221226211304108](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322308.png)

6、最后的使用也是和之前的做法是一样的

![image-20221226211831039](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322331.png)

### 3.8.3 网络请求

#### 3.8.3.1 基本使用

> 问题

其中的一个方法就是按照`3.3.3.1 基本使用`中的模式来处理，将网络请求写在组件里面来处理。但是这种方式不是很好，因为网络请求都是写在组件里面的，后续不方便管理。

![image-20221229201453133](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322353.png)

> 解决方法

1、使用`createAsyncThunk`来创建一个异步的函数，并且传入参数

2、再这个回调函数中返回的`res.data`数据会被传入到`extraReducers`中下面的计算属性来接收，然后再这里面完成相应的逻辑处理

3、并且写在外面的`fetchHomeAction`依旧需要导出并且在组件中被调用

![image-20221229204652857](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322388.png)

4、调用传入给组件中`props`的函数

![image-20221229204938892](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322414.png)

和之前使用`redux-thunk`工具是一样的，传入函数来处理，而非传入对象

![image-20221229205047526](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322448.png)

#### 3.8.3.2 额外写法

> 1、extraReducers 额外写法

下面就是`extraReducers`的 2 种额外的写法

![image-20221229205600262](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322453.png)

> 2、state 变化额外方式

原本是通过`extraReducers`来处理这些数据，但是现在可以直接在自己的异步函数中处理

![image-20221229210446677](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322498.png)

### 3.8.4 数据不可变

这里就是介绍为什么我们以前都是直接将`{...}`传入给`reducers`的

![image-20221229211545057](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322539.png)

但是为什么我们使用`ReduxToolKit`就不需要返回对象，而是直接修改里面的值即可，其实就是使用到了`ImmutableJS`，介绍：[React 系列十八 - Redux(四)state 如何管理 (qq.com)](https://mp.weixin.qq.com/s/hfeCDCcodBCGS5GpedxCGg)

![image-20221229211456650](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322555.png)

## 3.5 状态管理

![image-20230224094900161](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322585.png)

![image-20230224094910331](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322606.png)

# 4. 路由管理 - Router

## 4.1 基本使用

![image-20230224104658361](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322322.png)

```bash
npm i react-router-dom	// 安装
```

![image-20230224113036811](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322344.png)

![image-20230224113048374](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322365.png)

![image-20230224113057162](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322393.png)

1、下载`raect-router-dom`，并且导出`HashRouter`和`BrowserRouter`包裹，这样整个`App`就可以使用路由

2、`Routes`包裹`Route`，表示单个路由。使用`Link`表示导航，其实底层本质就是`a标签`

![image-20230224112726296](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322421.png)

## 4.2 Navigate

![image-20230225194227265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322474.png)

1、`Navigate`本质就是做重定向。下面就是登录场景的重定向，我们点击登录之后重新执行`render`函数，就会将`Navigate`挂载上去，就会自动执行`/home`的路由

![image-20230225194406379](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322157.png)

2、我们之前是按照这样的方式来加载重定向的，这个本质会加载 2 个`Home`组件，所以不是最优解

![image-20230225194611096](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322177.png)

我们直接使用`Navigate`组件就可以解决这个问题即可，只要加载`/`就会跳转到`/home`

![image-20230225195202533](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322195.png)

## 4.3 路由嵌套

![image-20230225203623322](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322221.png)

1、下面就是路由嵌套的原理，这样我们输入`/home/banner`就会跳转到`HomeBanner`。并且需要注意，如果你写在`/home`映射下面，就必须要带有`/home/xxx`才能正常使用

![image-20230225202446528](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322250.png)

2、在`Home.jsx`中直接使用`Link`标签确定路由，并且使用`Outlet`来占位，类似于`Vue`的`RouterView`，只要切换了路由就会将`组件`填入到`Outlet`

![image-20230225203002581](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322270.png)

3、这里有一个小细节，`Outlet`组件只作为父路由中的子路由的元素。假如我在`About`和`Home`中分别写上`Outlet`的话

![image-20230225203731617](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322006.png)

就会根据路由映射来写入子元素的内容

![image-20230225203835599](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322028.png)

## 4.4 手动跳转

![image-20230226213318555](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322048.png)

1、我们需要手动的跳转路由就需要使用`useNavigate`函数，但是我们在`class`组件中使用就会报错

![image-20230225204652040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322080.png)

现在唯一的方式就是使用函数组件来处理，或者采用`React Hook`来处理。在类组件中没有方法

![image-20230225212420397](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322103.png)

2、假如我们要在`类组件`中实现这类效果，就需要封装高阶组件来处理

3、我们在函数组件中使用`useNavigate`，因为后续可能通过`router`来传递其他的数据，所以将`navigate`方法通过`props`传递给类组件

4、在类组件中通过`this.props`来接收传递的函数，进行路由的跳转

![image-20230226212904158](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322127.png)

5、这样嵌套内层的路由也可以跳转到其他上层路由中

![image-20230226213125667](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322956.png)

## 4.5 参数传递

![image-20230226214456566](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322977.png)

> params

1、配置路由映射得时候添加`:id`，这样我们输入`/home/songInfo/100`得时候就可以获取到`id`为 100

![image-20230301202311987](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322000.png)

2、我们编写高阶组件`withRouter.jsx`，为里面添加`useParams`函数，并且传递出去即可

![image-20230301203019681](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322027.png)

3、使用高阶组件`withRouter`来包裹，右边得组件使用用于跳转路由得，左边得组件时用于接收参数得。

![image-20230301203212143](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322051.png)

> query

1、发送`query`参数得`URL`

![image-20230301214822235](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322074.png)

这里有一个注意得点，就是`Query`参数不需要在后面编写类似`:id`得标识

![image-20230301214850848](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322899.png)

2、这里存在 2 个方法来解析`query参数`，第一个`useLocation方法`相对来说比较难，但是基本都是使用第二个方法。将数据解析出来之后通过`props`传递即可

![image-20230301215019707](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322924.png)

获取`query`然后使用就行

![image-20230301215356765](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322943.png)

3、这里解析一下`useSearchParams()`返回得参数`URLsearchParams`，下面是`MDN`得解释

![image-20230301215516704](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322969.png)

1、我们看下面打印得结果可以看到，首先`URLSearchParams`是实现了`entries`函数，并且`URLSearchParams`内部就实现了迭代器，并且迭代器得名字就叫做`entries`，所以本质`entries`就是迭代器

2、并且我们使用`entries()`返回得对象使用`next()`就会输出数据，这一部分得源码可以参考我`ES6 迭代器`得笔记

3、我们使用`foreach`来遍历得时候可以看到最后得结果其实就是`[["name","zs"],["age",18]]`得格式，这里其实就是`ES8`得`entries`得格式，所以这里我们使用`Object.fromEntries`转化为对象

4、并且遍历`searchParams`得时候，就是遍历`searchParams.entries()`

![image-20230301220058782](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322994.png)

5、下面就是模拟的上面的`searchParams`，可能因为历史遗留问题，所以底层可能不是这么实现的。但是本质就是下面的代码，迭代器遍历，只不过数据模式不是常见的`对象模式`

![image-20230302111943278](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322019.png)

## 4.6 路由配置

### 4.6.1 路由抽离

![image-20230302143950707](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322935.png)

1、我们一开始默认在`App.jsx`中编写得路由映射存在问题，当项目变大之后，入口文件`App.jsx`就会变得很大，所以就可以使用类似`Vue`得路由配置，将路由信息抽离出去。

其中得属性都是和原本得路由映射是一一对应得

![image-20230302144314726](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322955.png)

2、最后在函数组件中使用`useRoutes`，并且导入刚刚得编写的`routes`，它就会将数组变为路由映射，这样就实现了路由配置信息的抽离

![image-20230302144415264](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322976.png)

### 4.6.2 路由懒加载

1、其实`import(...)`是`webpack`的特性，这样我们打包的时候就会分包处理，提升首屏开启速度

![image-20230302151119795](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322999.png)

2、但是存在包还没下载下来，但是路由已经跳转进去的情况，这个时候需要做应急处理。这个时候就需要使用`Suspense`高阶组件来处理。这样即便没下载到包也可以内容可以显示

![image-20230302151259159](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322018.png)

## 4.7 额外使用

### 4.7.1 NavLink

![image-20230224153505206](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322039.png)

1、`NavLink`使用的场景不是很多，和`Link`唯一的区别就是可以添加`style`和`class`。下面就是一种，只要你点击之后就会将颜色变为`red`

![image-20230224154316688](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322935.png)

我们点击之后`style`会自动变化

![image-20230224155040867](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322958.png)

2、对于`className`的本质也是和`style`差不多，点击之后修改`style`或者`className`

![image-20230224160301291](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322980.png)

### 4.7.2 NotFound

`path`为`*`的话表示统配，这样不知名的路由就会跳转到`NotFound页面`

![image-20230225195253798](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322009.png)

# 5. 脚手架 - Hook

## 5.1 基本介绍

### 5.1.1 基本介绍

> 为什么需要 Hook

![image-20230303193256587](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322030.png)

> Class 组件存在的问题

![image-20230303193328974](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322052.png)

> Hook 的出现

![image-20230303193346117](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322809.png)

### 5.1.2 使用差别

> Class 组件和 Functional 组件对比

![image-20230303194118329](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322829.png)

> 计数器案例对比

下面分别编写了`Class组件`和`Hook`语法的实现，可以很明显的看出代码量少很多，而且更加易读。所以现在也大部分都会使用`React Hook`来编写

![image-20230303200728304](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322857.png)

![image-20230303200825357](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322887.png)

## 5.2 useState

![image-20230303201030164](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322905.png)

1、下面就是`setState`的基本使用

![image-20230303202112058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322929.png)

2、并且使用`useState`的情况下，我们可以将`Hook`移出组件，但是是有条件的。只能在`useXXX`的函数中移出，假如是`XXX`函数就会报错

![image-20230303202511420](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322678.png)

3、原生的函数在结束之后内部的变量就会被销毁，但是我们使用`useState`的话，内部就会将状态交给`React`来保存，所以就不会导致每次加载组件的时候数据消失

![image-20230303202631402](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322698.png)

4、对于`useState`还可以传入函数，这就会将这个函数的返回值作为`count`的值，如果这样写的话就可以提取对数据进行一系列的操作再返回

而且`useState`内部函数只执行一次，也就是组件渲染的时候执行，后续即便页面渲染也不会再去执行

![image-20230306163618250](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322719.png)

## 5.3 useEffect

### 5.3.1 基本使用

![image-20230304104812024](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322749.png)

1、下面就是实现的`count`数字增加，网页标题就随之改变，可以很明显的看出使用`Hook`的写法会简洁很多。

2、这里使用了`useEffect`的`Hook`函数，这个`Hook`只要页面重新渲染就会执行一次。而且`Effect`也表示副作用，很明显`doucument.title`就是很明显的副作用，我们可以将这类操作放在这里

![image-20230304104910554](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322778.png)

3、对于`useEffect`可以返回一个函数，并且每次执行组件的时候先优先执行返回的回调函数。这样我们就可以在这个回调函数这种进行一些取消订阅的操作，但是基本很少这样使用

![image-20230304225339425](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322799.png)

![image-20230304225237885](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322547.png)

4、`useEffect`一般都是函数`return`组件渲染完成之后才会执行`useEffect`，但是`useLayoutEffect`则是在`组件渲染`之前进行操作

### 5.3.2 Effect 抽取

![image-20230304230827137](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322570.png)

我们可以将多个`Effect`进行抽取出来，这样逻辑会更加清晰，并且这些`effect`会由上到下依次执行

![image-20230304230519435](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322593.png)

### 5.3.3 性能优化

![image-20230304230838130](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322620.png)

1、`useEffect`存在第二个参数`[ ... ]`，里面的参数只要改变就会执行`useEffect`

2、如果只是传入`[ ]`的话，就只会在组件挂载的时候执行，如果组件再次渲染也不会执行

3、如果没有传入`[ ]`的话，只要组件渲染就会执行一次

![image-20230304232115420](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322644.png)

## 5.4 useContext

![image-20230304234618187](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322666.png)

1、下面是我们之前使用`Context`的步骤，非常的复杂，并且一层层嵌套处理。所以在`Hook`中可以直接使用`useContext`来处理

![image-20230304234220834](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322414.png)

下面为创建`Context`的方式

![image-20230304234709374](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322444.png)

我们换为`useContext`就可以发现，使用的过程简单很多

![image-20230304234609483](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322466.png)

2、只要`Context.Provider`中的数据发生了改变，在使用了该`Context`的`useContext`就会返回一个新的`Consumer`，然后再去重新渲染页面

![image-20230304234901222](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322498.png)

## 5.5 useReducer

![image-20230304235135491](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322523.png)

1、下面就是`useReducer`的用法，其实就是`redux`的一套使用流程，使用这种方式来编写的概率很小，所以只是了解这个`Hook`

![image-20230305100449630](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322546.png)

2、其实使用`useReducer`是为了管理更加复杂且多的数据，如果数据很多，就需要编写很多的`useState`，这样就难以管理，但是实际情况也很少使用，如果数据真的很多就会使用`redux`

![image-20230305100626969](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322306.png)

## 5.6 useCallback

### 5.6.1 闭包陷阱

![image-20230305102246588](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322323.png)

1、我们每次调用`App`的时候就会定义一次`increment函数`，如果组件渲染又会定义一次，这样每次数据修改就会定义同一个功能的函数，所以这里可以使用`useCallback`来做性能优化

![image-20230305102237335](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322341.png)

2、这里存在`闭包陷阱`的问题，可以看下面的例子。

我们定义了`f1`并且为`name`传入`zs`，所以这个时候`bar`内部的`name`为`zs`。我们再定义`f2`并且为`name`传入`ls`，这个时候`name`值被修改了，再去调用`f1`的时候就会发现`name`依旧是一开始传入的值，并未做修改。所以可以得出一个结论，就是闭包获取出来的值就是定义的那一刻的值

![image-20230305104841402](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322369.png)

我们换成`num + 1`就会发现问题了，只会取一开始定义的值来处理，后续即便`num`修改，也会一直执行一开始闭包保存的值，也就是存在`记忆性`

![image-20230305152817803](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322395.png)

3、所以我们换成这里的`useCallback`并且添加第二个参数`[ ]`的话也会存在上面的闭包陷阱，这样就不是每次都创建一个新的函数，而是使用之前的函数来处理

因为每次执行`组件`的时候就会执行一次函数，那么`useCallback`就会重新创建一个`function`，所以就会存在`foo1`、`foo2`、`foo3`......函数，其中每一个函数都会默认记录上面的`count`。因为我们添加了第二个参数`[ ]`的话，那么`useCallback`就会记录一开始的`foo1`，并且每次组件渲染的时候就调用`foo1`，即便创建了`foo2`。但是这个函数的`count`是一直没有改变的，所以就会导致数字一直卡在`1`，并不会增加，也就是我上面例子中的样子

![image-20230305153357326](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322480.png)

这个时候就存在一个疑问就是，以前写的函数为啥就不存在闭包陷阱呢？这个就是函数直接调用和`回调函数`的区别了，外面实在`useCallback`中回调的函数，这里面直接获取函数外部的值就是闭包处理，所以就会存在闭包陷阱的问题

![image-20230305151633555](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322019.png)

4、假如我们要解决这个问题的话，需要往`useCallback`中添加参数。这样只要`count`发生了改变，就会创建一个新函数`foo2`，这个时候就会重新读取闭包外部的`count`的值来执行

![image-20230305153930303](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322043.png)

但是我们折腾这么长事件来解决这个问题，最后还是需要重新创建回调函数的形式获取值，这还不如直接使用`const increment = () => setCount(count + 1)`来处理，其实这个优化的就是将这个函数传递给子组件的时候使用的

### 5.6.2 性能优化

> 子组件优化

1、其实`useCallback`就是做下面的性能优化的，我们将`increment`换为普通函数

2、当我们点击`onClick={increment}`的时候，就会重新渲染子组件`MessageComponent`，这是因为每次进入都是创建的新函数，所以就需要重新渲染

3、当我们点击了`onClick={()=>setMessage("你好啊!")}`的时候就会发现依旧会重新渲染`MessageComponent`，这也是因为每次都是重新创建的新函数`increment`，即便你没有做数据变化，也会重新创建

![image-20230305171528956](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322060.png)

4、所以这里我们使用`useCallback`的话，就可以避免这个问题。只要`count`不去改变就会不会去使用新的函数，也就不会导致`MessageComponent`的`props`变化，然后更新子组件

5、这虽然只是一个看起来不是很大的优化，但是落地在实际项目中会有很多的子组件，如果都这样直接用普通函数来处理的话，就会导致重新加载了很多的子组件，造成性能的损耗

![image-20230305172041597](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322086.png)

> 内部函数优化 + 子组件优化

1、我们之前一直都是创建一个新函数来获取`count`的值，所以`props`就会更新，所以就会重新渲染`MessageComponent`组件

2、但是这种重新渲染和重新创建函数的方式还是比较浪费性能，如果能一直都是同一个函数，这样即不用重新创建函数，而且传入`props`的值也不需要重新渲染组件

3、如果使用`useRef()`的话就可以解决这个问题，因为`useRef()`会返回同一个对象，即便组件重新渲染了很多遍，也还是同一个对象

4、下面的方式就是返回同一个`ref`，每次都是获取最新的`count`赋值给`countRef.current`，`useCallback`也不会需要为第二个参数传值，因为依赖已经被`ref`取代了，只需要使用 useCallback`的记忆性即可

![image-20230305175006284](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322123.png)

## 5.7 useMemo

![image-20230305175434030](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322157.png)

1、我们会写一些工具函数来处理数据，比如：`1-50`之和的计算......，我们每次渲染页面的时候就会执行这个函数，所以就会导致性能的浪费。如果我们只要执行一次这个函数，并且保存该值就不需要重复执行了

![image-20230305203648870](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322875.png)

2、这里我们可以使用`useMemo`来记忆这个值，这样就不会重复执行，而是只执行一次。而第二个参数和`useCallback`一样，传入的参数就是作为依赖来处理，只要依赖值改变就会重新执行这个回调函数

3、`useCallback`是记录的回调函数，而`useMemo`则是记录的返回值，所以还是有区别的

![image-20230305204922947](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322897.png)

4、如果我们写入依赖的话，只要`count`改变就会重新执行这个回调函数，并且返回值

![image-20230305211229407](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322918.png)

5、但是对于子组件来说，我们传入对象的话，只要每次执行重新执行组件函数，都会重新赋值对象，所以就会重复执行子函数

![image-20230305212443769](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322940.png)

所以这个也可以使用`useMemo`来进行优化，这样每次都不会重新赋值对象，所以就不会重新渲染子组件了

![image-20230305212635744](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322967.png)

## 5.8 useRef

![image-20230305213348978](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322993.png)

1、下面就是引入`DOM`的操作

![image-20230305214300810](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322760.png)

2、这里验证每次返回出来得`ref`都是同一个`ref`

![image-20230305215239689](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322781.png)

3、其中保存上一次保存值得功能在`useCallBack`中性能优化中使用过，可以回去参考

4、下面就是如何在父组件创建`ref`，绑定子组件得`DOM`元素

![image-20230306094444885](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322806.png)

## 5.9 useImperativeHandle

![image-20230305215518010](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322835.png)

1、传入子组件`ref`获取其中得`DOM`。在子组件需要嵌套`forwardRef`函数，并且`memo`和`forwardRef`不能颠倒顺序，`forwardRef`第二个参数就是传来得`ref`，传入到想要获取得`DOM`即可。这样我们在父组件中就可以直接操作子组件

![image-20230306094444885](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322806.png)

2、但是对于一些情况，我们并不想直接被操作元素得`DOM`，而想去做一些拦截处理。所以就会去使用`useImperativeHandle`拦截`DOM`得操作，最后直接将返回得对象传递给`ref`，而且这个`ref`就是`inputComponentRef`，所以`inputComponentRef`只能按照返回得属性和函数来操作

3、一般情况下很少使用这个`Hook`来操作，可能在一些库里面见到

![image-20230306100302297](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322858.png)

## 5.10 useLayoutEffect

![image-20230306100606688](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322894.png)

1、下面就是`useLayoutEffect`和`useEffect`得执行顺序得区别，`useLayoutEffect`就是渲染之前处理，而`useEffect`就是渲染之后处理

![[00 assets/e0cd74fcda7a55de5e9775089f2a5911_MD5.png|86]]

2、假如我们使用`useEffect`就会导致下面得问题，所以就可以使用`useLayoutEffct`来解决这个问题

![image-20230306111252649](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322674.png)

## 5.11 自定义 Hook

### 5.11.1 生命周期

我们使用`useEffect`就可以实现生命周期的打印处理

![image-20230306145622042](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322701.png)

### 5.11.2 获取 Context

我们在外面的`.js`中封装一个`UserTokenContext`的函数，这样在其他组件使用的时候直接导入`UserTokenContext`即可

![image-20230306152240326](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322729.png)

### 5.11.3 监听窗口位置

![image-20230306153934154](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322756.png)

### 5.11.4 localStorage

1、`useState`可以传入函数，并且可以将函数返回值作为参数

2、下面就是`localStorage`的操作，其目的就是想要渲染`loacalStorage`的数据，只要数据改变，就同时改变内部的`localStorage`的值和`State`的值，并且重新渲染页面

![image-20230306164206530](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322799.png)

## 5.12 redux Hook

1、我们之前使用`redux`的时候需要编写`connect()()`高阶函数，并且需要写`mapStateToProps`、`mapActionToProps`.....一系列的函数，这导致代码变得很多

![image-20230307153411130](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322593.png)

所以我们可以使用`Hook`得方式来编写，这样就轻松很多

![image-20230307153641075](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322609.png)

2、这里也存在一些性能优化的问题，和前面的`useCallback`...是一样的问题

![image-20230307155800446](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322627.png)

我们不管是修改`App组件`或者`Home`组件里面的数据，都会重新渲染。这是因为都会重新从`stroe`中拿去数据，所以都会统一发生组件渲染处理

![image-20230307155812603](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322662.png)

3、`useSelector`存在第二个参数，可以用作参数的比较。但是一般情况我们都是直接传入`shallowEqual`做处理

![[00 assets/03801f8616ce61091b78779b64e8a084_MD5.png|86]]

这样做了参数比较就不会出现重复渲染的问题

![image-20230307161302842](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322715.png)

## 5.13 useId

### 5.13.1 SPA/SSR

![image-20230307172250134](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322473.png)

> SSR 同构应用

![image-20230307191900198](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322497.png)

> Hydration

![image-20230307204443318](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322523.png)

### 5.13.2 基本使用

这一段内容在`SSR`的笔记中进行处理

![image-20230307205918922](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322548.png)

## 5.14 useTransition

![image-20230307210627650](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322571.png)

1、我们可以使用`faker.js`来生成一些伪数据

```bash
npm i --save-dev @faker-js/faker
```

![image-20230307214724613](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322591.png)

2、我们一次处理`10000`条数据，可能存在页面卡顿的情况，并且每次为`input`输入数据的时候，`input`也会卡一会，这个体验就很差，所以可能使用`useTransition`将数据过滤和页面渲染先降低优先级，先渲染`input`的输入字符的显示

![image-20230307214822516](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322306.png)

3、`setTransition`中是一个回调函数，将执行的逻辑放入就可以降低优先级

4、`pedding`是作为参数存在，只要在加载的话就为`true`，如果加载完毕就是`false`，所以一般都是加载`Loading`画面使用

![image-20230307215039754](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322327.png)

## 5.15 useDeferredValue

![image-20230307220012360](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322346.png)

我们使用`useDeferredValue`备份一个副本，只要修改了数据就会延时放入`deferredValue`进行数据渲染。本质和上面的`useTranstion`的效果是一样的

![image-20230307221207603](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322374.png)

# 6. 项目 - 爱彼迎

## 6.1 基本介绍

### 6.1.1 项目介绍

![image-20230308215504225](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322395.png)

### 6.1.2 项目规范

![image-20230506143515019](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322425.png)

![image-20230506143634256](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322179.png)

## 6.2 项目搭建

### 6.2.1 基本搭建

![image-20230506152908085](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322199.png)

1、通过`webpack`来初始化项目，使用`create-react-app xxx`来创建新项目

2、进入项目之后，删除不相关的文件，编写测试代码让项目跑起来

![image-20230506152222323](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322219.png)

3、配置网站图标和标题

![image-20230506152744286](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322240.png)

### 6.2.2 目录划分

![image-20230506153207948](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322271.png)

### 6.2.3 配置 craco

1、因为`react`默认使用隐藏`webpack`的配置，但是我们最好不要使用`npm run eject`来显示`webpack`，并且对其进行修改

2、所以我们可以使用插件来默认配置文件别名和样式，`npm i @craco/craco -D`

> 配置别名

1、我们创建一个`craco.config.js`来配置`craco`，后面就基本和之前配置`webpack`是一样的

2、封装函数，这样就不需要每次都写`path.resolve()`

![image-20230506161048728](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322309.png)

3、但是配置了别名，也只是在打包的时候会修改。但是我们编写的时候是不会有提示的，我们就需要添加`js.config.json`文件来为我们写代码的时候服务

![image-20230507140746568](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322026.png)

> 配置样式

1、这里使用`craco-less`，但是目前直接安装会出现问题，所以使用`npm i craco-less@2.1.0-alpha.0`

2、随后安装`less`，`npm install less-loader less --save`

![image-20230506161423438](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322045.png)

### 6.2.4 样式重置

![image-20230506161541476](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322061.png)

1、安装`npm i normalize.css`

![image-20230506162019905](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322086.png)

2、自己编写`reset.css`

![image-20230506162055965](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322112.png)

### 6.2.5 全家桶配置

#### 6.2.5.1 Router

1、安装`router`，`npm i react-router-dom`

2、对于路由的配置存在 2 种方式来编写。第一种就是在`jsx`中处理，但是这样编写会导致管理复杂。第二种就是单独搞一个文件来存放，这里选择第二种方式

3、编写路由懒加载`React.lazy()`

4、因为一开始进入到页面中，并不是`/home`页面，所以要设置重定向`Navigate`

5、还存在`NotFound`页面，只要路由不匹配就需要跳转到`NotFound页面`

![image-20230506170746792](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322137.png)

6、因为我们使用了路由懒加载，可能存在还在等待加载的情况，这个时候就需要一个等待页`Suspense`

7、并且编写路由要嵌套高阶组件`BrowserRouter`

![image-20230506171230106](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322865.png)

8、最后在页面中使用`useRoutes`函数就可以遍历其中编写的路由映射，并且应用其中

![image-20230506171419581](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322885.png)

#### 6.2.5.2 Redux

1、安装`Redux`这里使用`RTK`的解决方案，`npm install @reduxjs/toolkit react-redux`

2、安装之后使用`configureStore`来创建`store`

![image-20230506211345031](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322909.png)

3、我们创建一个`createSlice`，并且传入对应的参数

4、因为我们需要`dispatch`，所以还需要手动导入函数，并且导出函数

5、最后导出的就是`countSlice`的`reducer`

![image-20230506211442253](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322935.png)

6、使用`Provider`来为组件引入`store`

![image-20230506211947898](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322957.png)

8、因为这里使用的是`Hook`的写法，所以这里也修改为`Redux Hook`

![image-20230506212021166](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322977.png)

> 原始配置

1、因为很多老项目都是使用的`react-redux`而非`rtk`，所以这里也创建一个原始`redux`的配置方式

![image-20230506212233758](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322758.png)

2、依旧使用`rtk`来管理数据

![image-20230506212300544](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322782.png)

3、在`redux`的插件中也可以看到响应的数据

![image-20230506212454847](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322805.png)

#### 6.2.5.3 Axios

1、封装`axios`请求，这个在我之前就已经封装完毕了

```javascript
import axios from "axios";
import { BASE_URL, TIMEOUT } from "./config";

class RequestService {
  constructor(baseURL, timeout) {
    this.instance = axios.create({ baseURL, timeout });

    // 请求拦截器
    this.instance.interceptors.request.use(
      (config) => {
        return config;
      },
      (err) => {
        return err;
      }
    );

    // 响应拦截器
    this.instance.interceptors.response.use(
      (res) => {
        return res;
      },
      (err) => {
        return err;
      }
    );
  }
  request(config) {
    return new Promise((resolve, reject) => {
      this.instance.request(config).then(
        (res) => {
          resolve(res.data);
        },
        (rej) => {
          reject(rej);
        }
      );
    });
  }
  get(config) {
    return this.request({ ...config, method: "get" });
  }
  post(config) {
    return this.request({ ...config, method: "post" });
  }
}

const requestService = new RequestService(BASE_URL, TIMEOUT);

export default requestService;
```

2、然后正常测试封装的`axios`是否可以使用即可

![image-20230507140210789](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322822.png)

## 6.3 Header 头部

### 6.3.1 \*基础搭建 - 结构搭建

![image-20230507154424843](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322846.png)

1、因为要做到中间的搜索栏的居中，这就需要将 2 边的宽度设置为`flex:1`

![image-20230507153935716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322865.png)

2、并且头部`header`存在很多的状态控制，这里有 2 个方式来搭建`header`。这里使用第二种方式来制作

​ 方式一：每个页面中设置一个单独的`header`

​ 方式二：集中设置一个`header`，并且做好状态管理

3、并且对于`header`还存在 3 个部分，这 3 个部分也可以抽取为组件，也就是下面的框架

![image-20230507154650433](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322648.png)

4、对于样式，这里采用的是`styled-components`，`npm i styled-components`

5、我在这里编写的时候出现`vscode-styled-components`的语法提示问题，这里可以尝试将插件降级来解决

![image-20230507154208060](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322667.png)

引入`HeaderWrapper`，对编写的样式进行包裹

![image-20230507154307353](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322686.png)

### 6.3.2 \*Logo 搭建 - SVG 使用

1、对于`svg`的使用也存在 3 种方式

​ 方式一：将`svg`作为图片来处理，但是这种方式会导致网络请求没加载的时候出现空白

​ 方式二：将`svg`直接写在页面中，这种方式会导致页面中代码很多，所以也排除

​ 方式三：将`svg`作为组件来使用，这样可以解决上面的问题

2、按照这种方式来创建一个组件，并且只返回`svg`元素

3、因为对于`jsx`来说`style={ }`中的内容要是一个对象，所以编写一个`styleStrToObject`的函数来转化

![[00 assets/ad99213290eb23f002c36aef2dcd1bf6_MD5.png|86]]

该函数就是将`str`传入，之后转化为`object`的形式输出

![image-20230507155740909](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322737.png)

4、最后导出，在组件中使用即可

![image-20230507155841691](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322759.png)

### 6.3.3 \*主题配置 - 主题文件

1、对于主题配置也存在 2 种方式，这里使用方式二来配置

​ 方式一：使用`CSS`变量来配置

​ 方式二：使用`styled-components`的`theme`功能来配置

2、我们在全局编写`theme`文件

![image-20230507160443167](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322549.png)

3、我们需要全局使用这个`theme`的话，就需要引入`styled-components`中的`ThemeProvider`组件

![image-20230507160517991](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322566.png)

4、使用的话就使用`${ }`中函数返回值的形式来显示

![image-20230507160622371](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322589.png)

### 6.3.4 \*菜单搭建 - flex 值/样式抽取

![image-20230507162747823](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322620.png)

1、先对整体的结构进行搭建，使用`svg`依旧参考之前的笔记

![image-20230507162809742](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322727.png)

2、在编写的时候发现，`justify-content`存在`space-evenly`属性，该值和`space-around`存在什么区别？

![image-20230507162928619](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322747.png)

这张图是`space-evenly`，可以发现它们之间的距离是一样的，也就是关注元素和元素的距离

![image-20230507162220714](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322148.png)

使用`space-around`就只关注该元素周边的距离

![image-20230507162243649](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322172.png)

4、因为我们手指放在上面存在一个阴影的动画，但是可以发现存在很多这样的动画，都是一样的，所以我们可以将该动画进行抽取

![image-20230507162734382](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322197.png)

我们将该动画抽取到`theme`的`index.js`中

![image-20230507163346574](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322386.png)

5、依旧使用这种方式就可以引入该动画

![image-20230507163423763](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322473.png)

### 6.3.5 搜索栏搭建

![image-20230507210024089](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032322919.png)

1、参考结构搭建`HTML`和`CSS`即可

![image-20230507165141246](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323010.png)

![image-20230507165151890](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323039.png)

## 6.4 Home 页面

### 6.4.1 \*轮播图 - 资源引入

1、下面是轮播图的搭建结构

![image-20230508093652577](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323062.png)

2、首先要理解一个点，`React`和`Vue`只要跑在`webpack`环境下面，就是不能直接引入图片资源，而是需要将该图片按照模块的形式来引入

3、为什么在`Vue`中可以直接引入呢？这是因为`Vue`在解析`template`模板的时候就已经在底层做好了处理，所以不需要我们手动操作

4、但是在`React`中是没有做这些处理的，而是需要自己来做

5、我们可以按照下面的 2 种方式来引入资源，我一般选择使用`require()`来引入资源

![image-20230508094007922](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323086.png)

6、这个就是`sass`的语法，也就是`div > .content`的语法

![image-20230508100806062](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323203.png)

### 6.2.2 \*高性价比数据获取 - 网络请求/Redux 数据管理

![image-20230508094758385](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323705.png)

![image-20230508094708313](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323724.png)

1、我们需要请求到数据，并且丢给`redux`来管理数据

2、首先来对网络请求进行归纳管理

![image-20230508094931360](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323742.png)

3、使用`createAsyncThunk`来创建异步函数，用于网络请求

4、在`extraReducers`监听网络请求，并且将数据交给`state`中管理，这里笔记参考`Redux`的内容

![[00 assets/8b0f24093cb36190912e0aa88113da94_MD5.png|86]]

5、导出该网络请求的`action`，使用`Redux Hook`来对`Redux`进行操作

6、`dispatch`用于事件发送，`useSelector`用于数据的监听

![image-20230508095227291](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323792.png)

7、获取数据进行展示

![image-20230508095418076](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323440.png)

### 6.2.3 \*AreaHeader 组件搭建 - props 参数传递

1、下面是组件结构得搭建

![image-20230508202027231](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323463.png)

![image-20230508202033182](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323482.png)

2、我们给组件传入参数，使用`propTypes`作为参数校验

3、函数中使用`props`来获取传入得参数

![image-20230508202107579](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323515.png)

### 6.2.4 \*RoomItem 组件搭建 - 样式搭建

1、我们参考下面得结构

![image-20230508202206183](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323543.png)

2、因为图片存在长短不一得情况，所以我们按照下面得方式来搭建组件。但是具体为什么这样可以实现，我就不是很了解了

![image-20230508202345808](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323584.png)

![image-20230508202259738](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323480.png)

### 6.2.5 \*组件引入 - antDesign/MUI

> 引入 antDesign

1、安装`npm i antd`，随后就是正常的组件引入流程

![image-20230508205616190](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323495.png)

2、但是我们想要配置`antdesign`的主题颜色的话，目前官网提供的方式是使用`Provider`

![image-20230508210153632](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323515.png)

3、但是老师讲的是通过`webpack`中引入`less`来修改主题颜色

![image-20230508210235291](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323538.png)

然后再去引入`less`文件

![image-20230508210303586](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323569.png)

> 引入 MUI

1、安装`npm install @mui/material @mui/styled-engine-sc styled-components`。但是目前使用`styled-engine`存在很多问题，这里还是`emtion`

2、`npm install @mui/material @emotion/react @emotion/styled`

3、然后引入使用即可

![image-20230508220039536](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323589.png)

4、引入完组件之后，直接搭建评分样式即可

![image-20230508220149623](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323418.png)

![image-20230508220135878](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323437.png)

### 6.2.6 \*AreaRoom 组件搭建 - 结构组件抽取

![image-20230508220242116](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323462.png)

1、这是一种组件的思想，不仅仅只是抽取单一功能，还可以抽取结构作为一个组件

![image-20230508220234280](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323505.png)

![image-20230508220356265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323536.png)

### 6.2.7 高评分数据 - 网络请求优化

1、我们将网络请求都封装到`redux`中的`createAsyncThunk`，但是按照我们之前的写法就会存在一些问题。如果按照`async/await`的语法糖来写的话，会导致网络请求速度很慢

2、所以对于这种多个请求一起发送的情况，我们使用下面的方式来处理

3、对于`createAsyncThunk`中的回调函数存在第二个参数`store`，`store`存在`dispatch()`和`getState()`函数，我们派发`action`来达成数据的更新，也就是放弃`extraReducers`

![image-20230509162716906](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323559.png)

4、将`store`中的`action`导出给`createAsyncThunk`

![image-20230509163021066](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323505.png)

### 6.2.8 RoomItem 组件宽度控制

1、通过`props`传输数据给`组件`

![image-20230509163400673](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323525.png)

### 6.2.9 \*SectionV2 组件封装

1、因为基本的逻辑已经和上面的差不多，直接参考代码即可。但是还是存在一些比较难理解的点

2、这里就是比之前多封装一个`area-tabs`组件

![image-20230509163734815](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323547.png)

> area-tabs 封装

1、这里包含了`classNames`库的函数

![image-20230509163929985](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323585.png)

2、还包含了子组件给父组件使用事件传递参数

![image-20230509164128412](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323607.png)

> 网络请求到才渲染界面

1、因为这里存在初始化值得处理方式，在一开始渲染界面得时候`useState`传递得参数是`""`

![image-20230509164253264](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323631.png)

2、如果我们想要做到网络请求到数据之后才会渲染界面得话，可以使用下面得方式

![image-20230509164749333](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323645.png)

3、将监测对象是否有数据封装为一个函数来判断

![image-20230509164759752](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323664.png)

> areafooter 组件封装

![image-20230509164904581](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323680.png)

### 6.2.10 \*ScrollView 组件封装

这里没怎么看懂，可以直接看代码

## 6.5 Entire 页面

### 6.5.1 过滤器功能

1、这里界面就不记录了，主要是选中和取消选中

2、这里主要还是用到了数组的内置的高阶函数，其逻辑主要是判断依据存入的`selectFilter`中是否包含了已经选中的部分，如果选中的话就删除，没选中就添加

3、`findIndex`传入高阶函数，如果函数返回值为`true`的话就返回该索引，为`false`的话就跳过

4、`splice`表示要删除的数据，第一个参数为开始索引，第二个参数表示要删除的数据

5、`slice`表示截取的数组的数据

![image-20230513162213360](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323705.png)

### 6.5.2 房间列表数据 - 非 RTK 中 Redux 的使用

> 基本结构

1、在实际的开发中大部分还是非`RTK`的选择

2、其中目录结构依旧和之前一样，这里参考我之前`Redux`的笔记

![image-20230513162828196](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323740.png)

3、因为之前使用的`rtk`来管理这些`reducer`，但是因为`rtk`本质就是基于之前的`redux`的高阶封装，所以我们原生编写也可以直接使用，并且内部还集成了`react-thunk`，不需要我们手动安装

![image-20230513163027115](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323772.png)

4、后续的时候和之前是一样的，使用`redux Hook`

![image-20230513163240739](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323602.png)

> 网络请求

1、因为我之前记得的笔记是`class`组件，但是这里使用的函数式组件，所以存在一定的区别

2、这里的本质就是执行`fetchRoomListAction`函数，然后返回函数`(dispatch,getState) => { }`并且内部调用，这里没处理`redux-thunk`是因为`rtk`内部就集成进去了，所以不需要处理

![image-20230513163413288](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323623.png)

### 6.5.3 分页器 - 修改 UI 组件库的样式

1、使用开发者工具调试，修改内部样式即可

![image-20230513163736311](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323645.png)

### 6.5.4 RoomItem 补充 - 图片轮播/指示器封装/依情况展示组件数据

实现点击左右箭头轮播显示，并且下面指示器提示

![image-20230513163924880](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323674.png)

> 轮播效果

1、最终的结构分为这 3 部，其中轮播图部分使用`ant-design`封装好的组件

![image-20230513164052089](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323704.png)

2、最终实现的逻辑部分

![image-20230513164227923](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323724.png)

> 指示器

1、这一段涉及到了`DOM`距离的计算，这和`scrollView`组件的封装是差不多的思想，我这里不是很懂，就不去记录了

2、中间部分为核心变化的代码，且该组件使用插槽的形式扩展

![image-20230513164401516](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323641.png)

3、这里包含一个数组临界的算法

4、设置`selectIndex`的值，并且作为`props`传递出去

![image-20230513164520410](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323662.png)

> 依情况展示组件

1、因为`RoomItem`还存在`/home`页中无组件的显示模式，如果再去封装一个组件就很浪费

2、所以这里将`jsx`的组件拆为一个变量，这和之前的类组件是一样的

![image-20230513164810086](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323687.png)

### 6.5.5 跳转到详情 - 事件传递

1、封装为一个组件，所以最好不要将单一特殊事件给组件来调，而是抛出来给父组件来处理

![image-20230513165007324](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323711.png)

### 6.5.6 详情页图片开发 - 页面跳转数据传递/Redux 数据持久化处理/样式排他思想

> 页面跳转数据传递

1、对于页面跳转需要数据传递，但是使用路由中的`param`和`query`来传递这么多参数，很显然不现实

2、所以最好的方式就是使用`redux`来保存该数据，之后就可以在另外一个页面中使用

![image-20230513165156860](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323736.png)

> redux 持久化存储

1、因为存在`redux`中的数据在刷新之后就会小时，所以这里我使用`session`存储的方式来持久化`redux`中的数据

2、所以我们需要封装一个可以存储的工具，这里的思路参考了`Vue`后台管理中封装的`utils`

![image-20230513165643016](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323757.png)

3、每次进入页面请求`actions`的时候就保存该数据，并且初始化的时候就使用保存在`session`的数据

![image-20230513165737787](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323688.png)

> 样式排他思想

我们鼠标放置在上面的时候只有该元素显示，其他元素都显示遮盖层

![image-20230513165909001](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323711.png)

1、下面为`HTML结构`

![image-20230513170040563](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323758.png)

2、这一段就是排他思想的核心代码

3、只要`pictures`处于`hover`状态的时候，就将`cover`设置为显示，并且这时候只要`item`为`hover`状态的话就让`cover`消失。

4、这里使用到的原理是`CSS`层叠样式，后面的`item`为`hover`状态的时候覆盖上面的`opacity`的状态，就达成了这种效果

![image-20230513170127594](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323782.png)

## 6.6 图片浏览

### 6.6.1 图片展示

![image-20230516183657436](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323807.png)

1、因为该图片浏览器在各个地方都可以使用，所以将该组件封装到`base-ui`中

![image-20230516183740821](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323844.png)

### 6.6.2 关闭功能 - 使用 JS 设置样式

1、这里组件展示的原理就是在背后设置一个遮盖层

![image-20230516183841543](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323287.png)

2、我们点击了上部组件之后就关闭也组件，并且打开的时候不能滑动

3、这里采用设置`overflow`的值来解决

![image-20230516183953985](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323306.png)

### 6.6.3 图片切换 - React 动画

1、这个是图片切换的 HTML 结构

![image-20230516184139728](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323324.png)

2、这里比较难的点就是存在多个元素的动画，并且是一个元素进入，一个元素出去。最好的方式就是使用`Switch`和`CSS`组合使用

![image-20230516194809814](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323353.png)

### 6.6.4 图片列表浏览 - Indicator 组件使用

![image-20230516194850151](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323374.png)

1、下面是 HTML 结构

![image-20230516194925371](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323406.png)

2、这里主要的`Indicator`组件的使用

![image-20230516195211444](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323217.png)

### 6.6.5 页面滚动到顶部 - Hook 使用

1、我们每次进入到新的页面都需要页面滚动到顶部，这里就可以尝试封装一个`Hook`来简化代码

![image-20230516195450610](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323236.png)

## 6.7 Header 开发

### 6.7.1 页面搭建

这里的头部需要变化，且存在`fixed`定位的可能

![image-20230516195548859](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323256.png)

![image-20230516195555701](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323296.png)

1、下面是`HTML`结构

![image-20230516195651087](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323325.png)

### 6.7.2 fixed 控制 - 配置信息使用 Redux 控制/Susponse 和 Redux 冲突问题

1、因为有写页面需要控制头部是否一直吸附在顶部，所以需要一个变量来控制，最好的方式就是我们传入配置就可以实现功能

2、我这里使用`Redux`来动态控制

![image-20230516195949053](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323349.png)

3、落实到每个页面中，就是进入时就发送`action`来控制初始值

![image-20230516200029446](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323349.png)

> Susponse 和 Redux 冲突问题

1、我们目前采用这种方式是可以监听到的，并且`action`也是可以发出，且逻辑没有任何问题

![image-20230516200545100](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323367.png)

2、但是我们使用了路由懒加载的技术，可能存在`Redux`已经准备好了，但是页面还没请求到的情况，所以这个时候可能`Redux`中的值依旧是原来的值

3、为了解决这个问题，最好的方式就是将`Suspense`组件放置在`Provider`里面

![image-20230516200832969](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323389.png)

### 6.7.3 头部动画效果 - React 动画效果

1、因为是 2 个部分，并且动画都不一样，所以这里采用的是 2 个动画同时加载

![image-20230516200209145](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323420.png)

2、动画效果的`CSS`

![image-20230516200257616](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323441.png)

### 6.7.4 页面滚动搜索关闭 - 滚动监听/Hook 使用

1、这是封装的滚动监听的`Hook`

![image-20230516200952943](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323464.png)

使用`Hook`并且滚动监听

![image-20230516201024750](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323201.png)

2、因为只要滚动就开始监听，所以这里需要记录一下之前的值，因为记录并不需要刷新页面，这里就采用`useRef`的方式来保存数据

3、下面是滚动搜索结果消失的核心代码

![image-20230516201152635](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323225.png)

### 6.7.5 顶部搜索栏透明 - 使用注意传递参数

1、我们滚动到顶部之后页面中的元素样式都需要修改

![image-20230516201306906](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323247.png)

但是监听`isAlpha`的值只在`app-header`中存在

![image-20230516201348904](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323287.png)

2、我们需要将该值传输给下面的多级组件的`styled-components`中，很显然单纯使用`props`和`event`已经不能处理了，但是使用`Redux`又没有必要

3、这里使用`styled-componets`的`ThemeProvider`来传递参数，这样就可以在每个组件的`Wrapper`中都可以使用到了

![image-20230516201639233](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323316.png)

![image-20230516201650720](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323335.png)

## 6.8 开发部署

参考`Vue`笔记

# 7. 项目 - 网易云

## 7.1 项目搭建

### 7.1.1 基本搭建

1、可能我们使用`create-react-app`会出现错误，所以需要使用`npm i create-react-app -g`来安装命令

2、我们使用`create-raect-app xxx --template typescript`来创建项目

![image-20230522200209950](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323235.png)

3、我们按照之前的配置创建了`craco`，还需要手动来配置`teconfig.json`文件才不会导致报错

![image-20230522202515323](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323254.png)

### 7.1.2 代码规范

1、按照我之前的`Vue`笔记配置即可，但是老师对于`eslint`的配置存在一些其他的操作

2、我们安装下面的插件`npm i eslint -D`，然后输入`npx eslint --init`来初始化`eslint`的配置

![image-20230522205002822](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323272.png)

这是我选择好的`eslint`的配置，这里根据情况来选择

![image-20230522205426467](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323295.png)

3、下面就是配置的结果

![image-20230522210658539](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323319.png)

![image-20230522210705901](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323344.png)

![image-20230522210720822](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323094.png)

![image-20230522210727647](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323115.png)

下面是我这里配置安装的包

![image-20230522210758168](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323133.png)

### 7.1.3 目录搭建

![image-20230522211413528](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323154.png)

### 7.1.4 全家桶配置

> 路由配置

1、参考之前的笔记来配置即可，但是因为目前使用的是`typescript`来搭建的项目，所以可能部分存在差异

2、首先就是创建文件，之前创建`.js`文件的时候也可以使用`jsx`的语法，但是对于`ts`来说就不行了，所以需要编写`.tsx`的文件

3、然后就是类型导入，对于`react-router-dom`来说，我们编写`routes`最好不要写成`any[]`类型。最好的方式就是导入类型`RouteObject`，它内部提供了对于的类型

![image-20230523104702936](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323173.png)

4、依旧使用之前的方式来做路由映射

![image-20230523105213767](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323192.png)

对应的`index.tsx`的配置也是使用下面的方式来处理

![image-20230523105558707](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323918.png)

5、且需要注意一个点，对于`React`即便你没有使用导入的`React`，也需要导入，不然就会报错

![image-20230523110156327](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032323939.png)
