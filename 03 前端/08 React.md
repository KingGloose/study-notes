前端系统课 - coderwhy - react

# 1. 非脚手架 - 非 Hook

## 1.1 基本介绍

### 1.1.1 基本了解

> 基本介绍

![[00 assets/5824a0aaa4bfa794b66a4191ad0eb382_MD5.png]]

> 技术特点

![[00 assets/d147871c822652670441cf8761f59535_MD5.jpeg]]

> Vue/React 选择

![[00 assets/326dba8b802ba4958df0b2887b8242a2_MD5.png]]

> React 技术介绍

![[00 assets/67b2e36e3e29ee1b158571d1354b06ac_MD5.jpeg]]

### 1.1.2 依赖认识

其中`react`需要依赖 3 个包，每个包都各司其职

![[00 assets/859d8b26d79bbfcdda91a294db0e1acb_MD5.png]]

其中`babel和react`的的关系，主要用于将`jsx语法`转化为`react`的语法
![[00 assets/3fd3681a7423eeca89b0fda2f05060bc_MD5.jpeg]]

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

![[00 assets/9638463bcbf99f4fe0e95a23c6fe1752_MD5.png]]

下面就是实现简单的`数据绑定`和`事件绑定`，里面暴露出来的语法和`Vue`是完全不一样的

1.模板语法不一样：在`Vue`中使用`{{ }}`来展示数据，但是`React`使用`{ }`来展示数据

2.事件绑定不一样：在`Vue`中使用`@click="btnClick"`表示事件绑定，但是在`React`表示使用`onClick={btnClick}`

3.数据渲染不一样：在`Vue`中定义的响应式数据变化，模板就会变化。但是在`React`中就需要重新调用`root.render()`来重新渲染才可以

![[00 assets/4aaa362f0cf395a4356778570ddddb56_MD5.jpeg]]

### 1.2.2 Hello React！组件化重构

> 1.定义组件

这里暂时是使用`类`来定义一个组件

![[00 assets/8fc4fb66517289ce24f29ae867344376_MD5.png]]

> 2.数据依赖

![[00 assets/9be7e3d5dacee8e53a7cc1a8f953ea96_MD5.png]]

> 3.事件绑定

![[00 assets/62a911dfe8bef3acc6e5d434b4126e69_MD5.png]]

这里面存在一个`this`引用的问题，我们通过下面的方式就是一个`默认绑定`，所以按照常规的处理方式，这个`this`就绑定的`window`，但是最后的结果是`undefined`。

1.这个就是因为在`严格模式`下，`默认绑定`的`this`就是`undefined`，而且在`ES6`下定义的`class`内部就默认是严格模式，所以是`undefined`

![[00 assets/cc39a6a158f3a910140f14d24743947e_MD5.jpeg]]

2.我们直接在`script`中写的，并且直接调用`foo`的话，里面的`this`也会是`undefined`。这是因为`react`的`babel`在转换代码之后默认开启了严格模式

![[00 assets/75f304f07c75dafdde107918191d58a3_MD5.png]]

了解了上面`React`的`this`的运行机制，所以我们再来看下`React`如何进行事件绑定。因为我们继承了`React.Component`，所以我们重写里面的方法`render`，这里面的`this`默认绑定的是里面的是`App`组件，所以这里我们使用`bind`来显式绑定数据，然后在`ChangeMessage`中调用`App组件`中的`setState`

![[00 assets/aa26ea51abeaa32d473ed8480ba8b546_MD5.jpeg]]

或者我们先在`constructor`中提前对`方法`进行绑定，再来进行调用也可以

![[00 assets/a3b8d264af30a40e614c405a9c9df5fc_MD5.png]]

### 1.2.3 列表遍历

因为`React`比较灵活，所以存在很多的`列表遍历`的方式

> 1.

我们将数组遍历出来，然后通过`li`的`虚拟DOM`遍历处理。这样再传递给`render`，这样就可以自动遍历里面的数组

![[00 assets/1d4586cc65a67615638f6e52c87205be_MD5.png]]

> 2.

其实遍历的本质就是将`数据`传输给`标签`，然后将该数组遍历渲染，所以我们不如直接`map`遍历展示。这里就展示了`React`的灵活处理的方式

![[00 assets/2d0f3455c37da66cc0d3532bbd6387f1_MD5.png]]

### 1.2.4 计数器

下面就是`React`实现`计数器`的方式，只要理解了`Hello React!组件化重构`中的逻辑，就知道这里的逻辑

![[00 assets/e46b5cbf2669568c700077c275bc4aaf_MD5.png]]

## 1.3 JSX

### 1.3.1 基本介绍

![[00 assets/df89282de87296d1f945b6be430a0a49_MD5.png]]

> React 为什么选择 JSX?

![[00 assets/ef1e86cad2a8c6feb40b02c276fe0de9_MD5.jpeg]]

> 书写规范

![[00 assets/0480367444d4a35cd66f8496f2e142de_MD5.png]]

### 1.3.2 编写注释

在`React`中编写注释的话需要使用下面的`{/* 这是一个注释 */}`

![[00 assets/f5745ed1333c458f90480684bbd5b12b_MD5.jpeg]]

### 1.3.3 模板语法

![[00 assets/75e4ab680f58226ed77fcded61e04f20_MD5.png]]

我们使用模板语法必须要遵守下面的 3 条规则

![[00 assets/71471fdf1a94ec589ac941272626c270_MD5.jpeg]]

当然我们不只是传入基本的数据类型，我们还可以传入`表达式`。和`Vue`的处理语法是一样的

![[00 assets/ac1d615d165f256ce821d2be85bf145c_MD5.png]]

### 1.3.4 属性绑定

#### 1.3.4.1 基本属性

我们使用下面的`{ }`就可以对元素中的属性进行绑定处理

![[00 assets/3c9a1b7bf4f2c60730bf2fec8134b2f7_MD5.png]]

#### 1.3.4.2 绑定 Class

我们一般使用下面的 3 个方式来对`class`进行动态的绑定。并且这里推荐使用`className`来绑定

这里来说下数组形式，因为我们默认将数组丢进`{ }`中的话，默认拆解的是`abc,cba,active`，所以这里我们先使用`join`来拆分即可

![[00 assets/3a451eb8a1fbe27fa5e93fa40e4d79d9_MD5.jpeg]]

#### 1.3.4.3 绑定 Style

我们使用下面的方式来绑定样式

![[00 assets/f0159b4687e5ea77facc872964868668_MD5.png]]

### 1.3.5 事件绑定

#### 1.3.5.1 基本使用

其他的基础部分可以参考`1.2 基本使用`中的 4 个案例，下面是介绍`this绑定`的 3 个方式

#### 1.3.5.2 this 绑定

1.使用`bind`来绑定，这个可以参考上面的`this绑定`

2.这里使用的是`Class Field`来处理，也就是成员字段。首先需要知道一个知识，在`Class`中定义的成员字段在任何其他地方都可以通过`this.xxx`来获取，所以可以在`render`中获取。因为绑定的是箭头函数，所以会根据作用域向上查询，就会找到`App`

3.这个是直接使用箭头函数来处理。本质是`() => { this.addCountArrow() }`，只要点击之后就会执行箭头函数，所以就会执行里面的`addCountArrow()`函数，因为`render`中的`this`是指向该组件实例的，所以相当于隐式绑定的方式来调用

![[00 assets/355305aae3ed30fa993b900e42dc00dc_MD5.png]]

#### 1.3.5.3 event 处理

1.我们使用`bind`和`class field`调用的函数，默认就会传递一个`event`参数，所以直接获取即可

![[00 assets/4ba8e616a81e1127cdadae6b8a2070e5_MD5.png]]

2.但是对于第三种方式`箭头函数`的处理方式就不存在`event`，因为内部本质在调用`箭头函数`，所以这个箭头函数是有`event`，但是对于最后调用的函数并不存在`event`

![[00 assets/ab1f121d191ebcbe746d370bc2cab9c4_MD5.jpeg]]

所以我们直接将`箭头函数`中的`event`传递给调用的函数就可以处理了

![[00 assets/fabdff303e083c279ec3752a786acb96_MD5.png]]

#### 1.3.5.4 参数传递

1.我们使用`bind`来传输参数，可以进行传递。但是会出现左图中的问题，`event`出现了在了最后

![[00 assets/05c6b0c06811ec14a5e1e3d5626aa5fc_MD5.png]]

在了解上面的知识之前可以先看下面的原理，我们在使用`bind`调用的时候首先先传入`张三,16`的数据，这个时候就会占用`foo函数`中的前 2 个参数，这个时候我们再来调用`fn`再来传入数据就会占用`height`

![[00 assets/5cb369d6cc3d45addab3c0013ff6b590_MD5.jpeg]]

所以上图中的`bind绑定`来传输参数也是这个原因

![[00 assets/116044f33c336a58aef943901117e18c_MD5.png]]

2.当然假如我们使用的是第三种方式的话，直接給该函数传递参数就可以了，不需要按照上面的方式处理

![[00 assets/0f9434f0d735ed6b8ae1d15033e64085_MD5.png]]

3.对于参数传递中我们可以参考下面的这个案例，点击左边的电影就会更改颜色。这个本质就是一个排他的思想

![[00 assets/a9a7198369349bdb224b9f089ff9fa45_MD5.png]]

### 1.3.6 条件渲染

1.其中`条件渲染`存在下面的 3 种方式的处理；其中第一个就是通过`if`判断，适合逻辑较多的情况处理；但是对于第二种情况，使用三元运算符的，这个就是比较推荐逻辑较少的情况来使用；第三种情况比较当某一个值可能为空的情况的话，所以比较适合网络请求的数据中

![[00 assets/a19232c41ed8de0616f3e4c244f92c80_MD5.png]]

其中第 3 个条件渲染的方式，比较适合在网络请求中进行处理。比如下面的`firends`是一个网络请求中数据，所以一开始的值为`null`，那么我们使用`firend.name`或`firend.age`的时候会报错，所以我们可以使用下面的`&& and ||`来处理

当然`React`本身就是比较灵活的，所以这里的知识一个参考，可能它本身有其他的用处

![[00 assets/485d2940ea02c53c8a4de1c51da014f1_MD5.jpeg]]

2.当然在`vue`中还存在`v-show`的效果，在`react`中也可以实现相应的`v-show`的处理方式。我们使用`style`的方式对元素的`display`属性进行处理即可

![[00 assets/08b10158c26ecb3f643183f155e3f594_MD5.jpeg]]

### 1.3.7 列表渲染

![[00 assets/41130ebf15faec3a6042d058c16bb857_MD5.png]]

1.下面就是一个基本的使用，在前面的`1.2 基本使用 列表遍历`中就已经演示过了

![[00 assets/c3b7b3db5ecff9f8e13af3ae143c15c2_MD5.png]]

2.当然我们也可以对数组进行处理再来展示，来实现一些展示的需求

![[00 assets/39cd184f8c09eb384017657e0f47a366_MD5.jpeg]]

但是对于`Reacr`中的列表循环，我们也可以对要展示的数据进行链式调用处理，再来展示

![[00 assets/93679baea08f17f70a07333ef5b5dbb7_MD5.jpeg]]

## 1.4 JSX 本质

### 1.4.1 基本介绍

![[00 assets/01534a0374d53ba50cff08a31dd27324_MD5.jpeg]]

### 1.4.2 babel 转换

我们可以在`babel`的官网（[Babel · The compiler for next generation JavaScript (babeljs.io)](https://babeljs.io/repl/#?browsers=defaults%2C not ie 11%2C not ie_mob 11&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=BQKABBlRA8AmBLAbgPnNDtFLAYwDYCGAzsQHKEC2ApgLwBEAFtYXNQE70qBpmYK4ZMAemxpMmeMjxFSFGg1wB7AHYAXaiq7pRGGAFd8IraJj4EKQKGKgTu0AjIJMHD2u5YBMt05odRjpywGY39p5ggnqBhoLCHuHYkiTkVHT0AGby8qqcKIB8OvxCyGFiuahR0ACUQA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=react%2Cstage-2&prettier=false&targets=&version=7.20.4&externalPlugins=&assumptions={})）对`jsx`的语法进行转换，我们可以发现其实本质就是`React.createElement`的函数

![[00 assets/5e1eee993e3ec265d4fd58e8d0c9737f_MD5.jpeg]]

假如我们不使用`babel`，直接将`React.createElement()`在我们的代码中使用，也是可以渲染出页面。

![[00 assets/08ecae6a2962afd8116c78b9c5f4788c_MD5.png]]

我们使用`React.createElement`也可以对页面进行渲染

![[00 assets/82b114d80055810d21c9e285728bb2ca_MD5.png]]

### 1.4.3 虚拟 DOM

我们这里打印使用`React.createElement`创建的节点，可以来查看虚拟`DOM`

![[00 assets/890ad3448c104774d1b6c6b9a4e3a2b1_MD5.png]]

下面就是转换的过程，对于这些虚拟`DOM`在`Vue`中有相应的解释，也可以套在`React`

![[00 assets/76df4fdf72da3ac6e1baf8a097ccef4c_MD5.png]]

### 1.4.4 声明式编程

![[00 assets/488ec0e7ca981786ddb6ac5f83dc9378_MD5.png]]

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

![[00 assets/9588c36ed1cacf3e3ef999c7c588e33f_MD5.png]]

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

![[00 assets/e08e0934163f794562c1d6bebe66fde7_MD5.jpeg]]



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

![[00 assets/891831364bd1cf0db330b27cb146766f_MD5.jpeg]]

> Hello World!

我们就是使用下面的方式进行组件化的开发，其实本质和`Vue`是差不多的。每个`jsx`文件就是作为一个组件存在

![[00 assets/f4b650084bc6ccdd00b4c21c1d9b5901_MD5.png]]

### 2.2.2 基本概念

> 了解 PWA

`MDN`官方文档：[渐进式 Web 应用（PWA） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/Progressive_web_apps)

其实`PWA`的本质就是将`web页面`添加到`手机主页面`中，作为一个`手机App`来启动。但是技术在国内的公司用的比较少，所以只是了解一下

![[00 assets/a9b0288b0e420e29233e4992d22b8305_MD5.png]]

> 了解 robots

这个是为`爬虫`指定爬取的数据

![[00 assets/69998b32f59e572f43c7c2447defc849_MD5.png]]

> webpack 配置

`React`对于`webpack`是进行隐藏的处理，假如你想查看的话可以参考下面的`react-scripts`文件夹下面的文件

![[00 assets/fbc932586f21706e8ff95719c5128960_MD5.jpeg]]

当然我们不想这么麻烦的话，可以使用`npm run eject`来显示，这个操作是不可逆的，所以不是很推荐来使用。假如运行失败的话可以尝试提交代码之后再来尝试

![[00 assets/e3ba5eae822d9d5b13e96fd1cb941d14_MD5.png]]

> 组件化

![[00 assets/88c8fed37258defc56054e4194bb2318_MD5.png]]

## 2.3 组件化

### 2.3.1 类组件

> 基本使用

![[00 assets/c607ccac7f3f1bf5806709e9138449ca_MD5.png]]

我们使用`类组件`来渲染下面的页面，这个在前面演示了很多次了

![[00 assets/24f47563b05c26c95022617c8f03a957_MD5.jpeg]]

> render 返回值

![[00 assets/05f2ac5350b84d7190df1846881ecc86_MD5.png]]

`render`返回值可以返回下面的基础结构

![[00 assets/26ea793019275a16843c75e735914f73_MD5.png]]

### 2.3.2 函数组件

> 基本使用

![[00 assets/f972fcd8c2d0b0889a5893be73663dcb_MD5.png]]

我们使用下面的方式来创建一个函数式组件

![[00 assets/f19035cbf8277d053321ab61700702a9_MD5.png]]

## 2.4 生命周期

### 2.4.1 基本使用

![[00 assets/d9393ab8bdb062cbbb82fc7ae9793e8d_MD5.png]]

> 基础生命周期 - constructor/render

1、我们认为的组件其实本质是一个个的`class`，所以每使用一个组件的话就会`new xxx()`创建一个实例，所以会优先执行`constructor`。其中`constructor`作为一个生命周期其主要做的事情就是`绑定事件`、`初始化state`

2、随后就是执行`对象`的实例方法`render`来重新渲染页面

![[00 assets/92751342fddb28bbced94d0fd6220cd7_MD5.png]]

> 挂载 - 更新

1、其中`挂载`和`更新`的生命周期分别是`componentDidMount`、`componentDidUpdate`

2、`componentDidMount`作为一个挂载的地方，最好的应用场景是`网络请求`、`事件绑定`、`DOM操作`

3、`componentDidUpdate`当`state`中的数据更新之后回调的函数，里面包含了`3`个参数，参数分别是`preProp`、`preState`、`snapshot`。其中前 2 个表示更新前的数据，所以在网络请求中需要比对数据的话可以使用。第 3 个表示`getSnapShotBeforeUpdate`回调函数传递来的数据

![[00 assets/0a8328e961d3e85f9670063bf9dde581_MD5.jpeg]]

> 卸载

![[00 assets/29015682d1b22cfd9d44d943d0bf9013_MD5.png]]

### 2.4.3 不常用周期

![[00 assets/884ab1d4775c8f7c2d071f501afbcf5b_MD5.png]]

> shouldComponentUpdate

`shouldComponentUpdate`返回值为`false`的话就不会重新渲染页面，返回为`true`的话就会重新渲染

![[00 assets/cbe447cf87f43c5a64855afb77bcf765_MD5.jpeg]]

> getSnapshotBeforeUpdate

这个是为了给`ComponentDidUpdate`传递第三个参数，为了作数据比对

![[00 assets/ee7c05dcc8bacd135a65485bbdb02dcd_MD5.png]]

## 2.5 组件通信

### 2.5.1 props - 父传子

> 基本使用

`props`主要是用于**父传子**，其中也存在 2 种形式来处理。

1、第一种就是自身存在`state`的话需要将`props`传给`super()`处理

2、假如没有`state`的话可以不写`super()`，系统会自动添加`props`

![[00 assets/01b8697932ac8f1edc619ce3e9f2ec2c_MD5.png]]

当然为了应对这种传输得`props`比较多的情况，可以使用`...`语法来拆分属性处理

![[00 assets/f841879a1edf68578dd8f208dff2ec9c_MD5.png]]

> 网络请求处理

假如我们是网络请求的话也是类似的处理方式，在`componentDidMount()`生命周期函数中发送网络请求，将值以`props`的形式传输过来

![[00 assets/b9a077958b7251e2897839c84a470301_MD5.png]]

> 参数校验

更多的可以参考官网案例：[使用 PropTypes 进行类型检查 – React (reactjs.org)](https://zh-hans.reactjs.org/docs/typechecking-with-proptypes.html)

首先需要导入`PropTypes`的包，进行类型判定

![[00 assets/124afb535065920ac9ec34159f255759_MD5.png]]

下面就是基本的`类型判定`和`默认值`

![[00 assets/51e97d907b399f1d6d6d4ea4f5ed1755_MD5.png]]

### 2.5.2 props - 子传父

因为`React`本身并不存在事件总线这个说法，所以本质还是通过`props`传递函数。下面是记录的思考的过程

1、子组件需要传递数据给父组件，首先是自己存在数据，也就是下面的`addClick()`。

2、父组件需要接收到子组件传输来的数据，所以就会存在`addCount()`

3、父组件需要将这个函数传递给子组件处理，所以需要通过`props`的形式传输过去。然后再以参数的形式接收到父组件进行处理

4、因为我这里使用到的形式是`箭头函数`，所以传递参数的接收主体为这个`箭头函数`，所以最后的参数需要再传递给执行的函数才会执行

![[00 assets/20a0e789a950168f9741e821245936fc_MD5.png]]

![[00 assets/e732e794bf48511e8cb248036b1d216e_MD5.png]]

### 2.5.3 context - 非父子

#### 2.5.3.1 基本使用

`context`主要是实现上层组件向下层组件传递数据。假如要实现下层组件传递上去可以使用`events`

1、首先需要创建一个`Context`，将要传输的组件包裹，其中`value`表示要传输的值

![[00 assets/59f29e21c288c6e6de555aae0b39a3e4_MD5.jpeg]]

2、然后将创建的`Context`传输给要使用的组件的`contextType`中，然后使用`this.context`即可获取

![[00 assets/e26e3074d269a5087dc95d0fdb4b6708_MD5.png]]

#### 2.5.3.2 Consumer

> 1、函数式组件使用 Context

对于`函数式组件`使用`Context`，肯定不能按照`类组件`的使用方式来处理，因为不存在`xxx.contextType`的属性。所以需要使用`<xxxContext.Consumer>`的方式来接收参数

![[00 assets/a758047666558da7c3a5cb879fa3105b_MD5.png]]

> 2、嵌套使用/接收 Context

因为一个组件的`contextType`不能加入多个`Context`，所以应对这种多个`Context`嵌套的情况也可以使用`Consumer`的方式来接收数据

![[00 assets/a6d9cb921eb7ebaf4219c0a16f9f184b_MD5.png]]

如果需要使用到嵌套的`Provide`的话，就需要使用下面的嵌套`Consumer`，很明显这样的方式非常的复杂

![[00 assets/aad46b33c7221b4d00b6508982f00134_MD5.png]]

#### 2.5.3.3 默认参数

当我们不将组件放在`Context`，那么就会使用到`默认参数`。这个默认参数要写在`createContext()`中

![[00 assets/cf96792a3a19691249944bf81d172d02_MD5.png]]

#### 2.5.3.3 相关 API

![[00 assets/5f742837d423aa749db25d20f0372fb6_MD5.png]]

![[00 assets/e0f0e4161925849f0a9bfe276916ecf9_MD5.png]]

### 2.5.4 events - 非父子

`events`的方式可以实现`上级`对`下级`组件，也可以实现`下级`对`上级`组件的传递数据。这里使用的是老师自己封装的库，其实其他的库也大差不差，只需改名字即可

```bash
npm i hy-event-store
```

1、创建`eventBus`。使用`emit`发送数据，其中`sendInfo`表示事件名

![[00 assets/99ef657c714093b8161a36f080876c11_MD5.jpeg]]

2、使用`on`表示接收数据

![[00 assets/15c987f2d7a01602236477487f5c5a78_MD5.png]]

## 2.6 插槽

### 2.6.1 基本使用

`React`的本身并不存在插槽的概念，因为本身`React`太灵活了，所以下面对`React`来说只是一个传值

> 方式一：children 方式

我们将插槽作为一个`children`值传输到`props`中显示处理，其实这个的本质就是`createElement()`的第三个参数，这段笔记可以参考我`JSX本质`中记录的笔记

![[00 assets/6aca0ce37aae0cae3ac9de8c32a06db0_MD5.png]]

但是这个方式有一个缺点，当我们只传输一个`children`值得时候不是一个数组，而是一个元素。假如因为传输值得不同导致类型得不同就会出现很多得问题。而且索引得方式也会有很多得问题

![[00 assets/39a09df824c10b702641291b098d67c9_MD5.jpeg]]

假如我们想要解决得话，可以使用`propTypes`来做类型判定。这样就有效的阻止了传输值得不同导致类型不同得问题

![[00 assets/dedd4b11f995a7ed43711146e73fc9a4_MD5.png]]

> props

下面就是以`props`得方式来传输插槽，实现页面得渲染

![[00 assets/140802d8a02a653da801f3244dbb290b_MD5.png]]

### 2.6.2 作用域插槽

作用域插槽可以参考我`Vue`得笔记。其主要是将`子组件`中的数据传输给父组件，然后再将组件传输给`子组件`渲染，这里重点的思想就是传输函数进去，调用函数渲染

![[00 assets/dc1ce13c1ca28b4e04718161d53dc0bd_MD5.png]]

## 2.7 性能优化

### 2.7.1 setState 解析

#### 2.7.1.1 基本解析

![[00 assets/bd2e71c268670fb1e8befe9521648f96_MD5.png]]

#### 2.7.1.2 3 种使用方式

对于`setState`有下面的 3 种使用方式来修改`state`中的数据

![[00 assets/c05463975bd66f16d1fed9dc1f63837a_MD5.png]]

#### 2.7.1.3 异步处理

> 为什么 setState 是异步更新？

![[00 assets/c0a4e572511c3b6c7be9d64927fcbc28_MD5.jpeg]]

1、先解释一下`显著提升性能`，假如我们一次执行多个`setState`的话，就会执行多次`render()`。但是结果并不是这样，点击之后是获取到所有的`setState`，放入队列中一次都执行完。所以就会出现下面的`state.count`的值并不会`+3`的情况

![[Pasted image 20250502180404.png]]

假如要实现累加的功能，就可以是要下面的方式来处理。

![[00 assets/9fd3a9bbeeb2dbf34abc193e21c5cb9c_MD5.jpeg]]

2、还有一个就是`state`和`props`更新不同步的问题。假如我们这里的`setState`执行完需要一段时间，但是`state`的已经修改，假如不执行`render`函数，那么`props`就不会更新，所以就会出现更新不同步的问题

![[00 assets/51d4066defc649df385b7e3255ecb182_MD5.png]]

> React 的 setState 一定是异步的吗？

在`React18之前`下面的操作都是同步的处理。但是在`React18`之后所有的处理都是实现的批处理，所以`setState`就是异步的调用

![[00 assets/4d76e4a2b0daa52af5cf167588af885b_MD5.png]]

> setState 实现同步处理

需要导入`flushSync`来进行`同步`的操作，当然`flushSync`内部依旧是异步的处理，只有`flushSync函数`外面的执行是同步的

![[00 assets/56cf1baed55ef9b3de932ce1d08f725e_MD5.png]]

### 2.7.2 diff 算法

> 更新流程

![[00 assets/972106f94ac3bd8667b859e76a8d89b9_MD5.png]]

> key 优点

![[00 assets/3f5a6431746178cbccb767062d0c4645_MD5.png]]

### 2.7.3 render 优化

#### 2.7.3.1 基本优化

当我们一开始进入网页的时候会自动执行一遍`App render`，或者数据修改的时候都会自动执行一遍`App render`。即便下面的子组件里面的数据没有发生修改，也会执行一遍`render`，这个是非常消耗性能。所以我们可以使用`shouldComponentUpdate`来更新数据

![[00 assets/b428bd0f2efa3fafa5aa90cdd946c88e_MD5.png]]

1、首先是对`App`的性能优化。当数据是一样的话，就让`shouldComponentUpdate`返回为`false`，不去重新调用`render`函数

![[00 assets/fbb5ca2f1c4fb6feb196a90f6f79d9af_MD5.png]]

2、然后就是对于`父组件`传递给`子组件`的`props`的优化处理，当传入的值和原本的不一样的话就修改

![[00 assets/b78d95cb9ebfb7b8cc0772f445fbba42_MD5.jpeg]]

但是使用这种方式来处理的话会非常的麻烦，所以一般都不使用这种方式。这个只是下面的`PureComponent`的实现原理

#### 2.7.3.2 PureComponent

一直写`shouldComponentUpdate`的话会很麻烦，假如我们要实现上面一样的功能就可以使用`pureComponent`来处理，但是这个处理只是`浅层次`的拷贝

![[00 assets/194e053f0957dd99c8af93d7d3d54cf9_MD5.jpeg]]

![[00 assets/1e8758c7857f341c4318efefbe4ad8f8_MD5.png]]

#### 2.7.3.3 memo

因为`PureComponent`是一个类，对于`类组件`可以使用继承来处理。但是对于函数组件来说就需要使用并不能实现相应处理，所以就需要使用`memo`高阶函数来处理优化

![[00 assets/460da25097c8fcd0e211407edb9cdfa1_MD5.png]]

![[00 assets/7a574e68905c37dc901e3fdacf02b02a_MD5.png]]

### 2.7.4 数据不可变

假如我们继承的是`Component`的话，我们使用下面的数据添加的方式，依旧会渲染 。

但是这种方式很大的弊端，不建议使用，因为`PureComponent`中有一个`shallowEquals`比较，也就是浅比较，直接将`bookList`是否等于`newBookList`，也就是比较的内存值，并不关心内部值得变化

![[00 assets/a2136c44a56a8fc4126ef00798ec9946_MD5.jpeg]]

假如我们使用的是`PureComponent`的话，上面这种方式就会失效。因为为了后续的性能优化，大部分的组件都会使用`PureComponent`来处理，我们依旧使用上面的方式来赋值渲染的话显然会出现问题。所以处理的方式依旧是先`浅拷贝`处理，然后对这个数据进行处理，然后再赋值为`state`来渲染。

这个就是数据不可变的魅力，原本的`this.state`中的数据就是不可变的，如果需要修改的话直接整个替换处理

![[00 assets/023198bf06ecd1fa7ffe609ea46ea115_MD5.png]]

但是对于使用`...`来浅拷贝得数据，都是一个指向得一个对象。所以我们修改里面得值得话都是一样得，但是为什么最后不允许使用`this.state.xxxx`来修改数据呢？这是因为底层使用到得就是一个浅层次得比较，我们使用原本得`this.state.xxx`得方式来修改得话，对于`React`来说依旧是没有修改得，在继承`PureComponent`得情况下这种方式就不会生效

![[00 assets/8aa9cb6afe5f2a71ee2f9aafdef7c622_MD5.png]]

## 2.8 refs

### 2.8.1 原生 DOM

我们可以使用下面得三种方式来获取`原生DOM`

![[00 assets/47f57e89688940bb9e5a47c27cdc56a3_MD5.jpeg]]

### 2.8.2 组件

> 类组件

我们可以使用`createRef()`来获取到组件得实例，因为获取了实例，所以也可以重新调用函数

![[00 assets/f4ac8ca4b9a3c99efaa3f1eaeb2dd4ed_MD5.png]]

> 函数组件

我们需要使用`forwardRef`高阶函数包裹处理，这样回调函数中就会出现二个参数`ref`来获取元素

![[00 assets/c8f806cfbcca339f077fb8c2a209da86_MD5.jpeg]]

## 2.9 表单

### 2.9.1 受控组件区分

> 非受控组件

我们是要监听表单的话，可以使用`onChange`来监听数据的变化，数据通过`e`来传递给`username`处理，再渲染到页面即可，我们通过整个方式还可以控制表单，所以是`非受控组件`

![[00 assets/e7d3a053acb854ff6d2f9895d1c6af01_MD5.jpeg]]

> 受控组件

当表单元素被`React`接替的话就是受控组件，因为我们操作不了表单元素，这个时候就需要使用`onChange`事件来处理`value`值得改变

![[00 assets/cdef32d876b2e366dc4144a4252280f3_MD5.png]]

### 2.9.2 基本使用

假如我们要使用`表单`的话就可以使用下面的方式来实现数据的`双向绑定`

![[00 assets/af942178d1bbb0a171594142923e98de_MD5.png]]

### 2.9.3 提交数据

> 表单提交 - form

对与现在项目表单提交得方式使用的场景比较有限，为了实现不刷新页面提交，一般都不会通过`form`来提交数据

![[00 assets/eaa495cd974b73af368ca61106232d91_MD5.png]]

> 表单提交 - ajax

1、假如我们不想使用浏览器的发送请求，可以添加`onSubmit`事件，在这个事件中阻止默认行为，获取数据发送

2、因为存在多个表单，所以我们可以写一个通用的函数`changeUserAndPass`来处理。其中对象名使用计算属性`[ ]`获取；`e.target.name`就是对应的`input`中的`name`；`e.target.value`就是对应的`input`中的`value`

![[00 assets/4595b56be266294b9570fdbff9b06b53_MD5.png]]

### 2.9.4 checkbox

> 单个

对于单个`checkbox`来说，本质就是对于`isAgree`的控制

![[00 assets/52cfaf1e5d3686ee7328c8179b164396_MD5.png]]

> 多个

这个的本质就是使用一个自定义的数组`hobbies`来处理，只要改变的话就改变这个数组，然后页面进行渲染

![[00 assets/45784d257359c4d8c519051ec1d54678_MD5.png]]

### 2.9.5 select

> 多个

1、下面就是对于`select`的处理方式，其中对于`selct`的`value`本质是通过`React`控制的，对于原生的`HTML5`中是不存在这种处理方式

2、对于`Array.from(...)`这种本质是将一个`Collection`类数组转换为一个数组，因为`Collection`本质是一个可迭代对象，所以可以转换，这个在`ES6`中的`arguments`有记录笔记。

3、其中`Array.from(...)`的第二个参数是一个`map`的回调，本来我们需要将`hobbies.map(item => item.value)`来额外处理，但是`Array.from()`提供了处理方式，所以我们直接使用即可

![[00 assets/69389140282028981663643458954bc7_MD5.png]]

> 单个

![[00 assets/e93317a66e9a9059bd908ac464776527_MD5.png]]

### 2.9.6 非受控组件取值

1、我们也可以使用非受控组件来取值，那就是使用`ref`处理获取`原生DOM`中的`value`来处理

2、`defaultValue`这个也可以默认设置`value`值，但是这个是为`非受控组件`设计的。`value`是为`受控组件`设计的

![[00 assets/6c4f69ab34471d901424646f4b46958e_MD5.png]]

## 2.10 高阶组件

### 2.10.1 基本介绍

![[00 assets/8292a514299eafbad4f3b4dcde997c42_MD5.jpeg]]

下面为基本的使用，所以可以理解`高阶组件`其实就是`高阶函数`。并且`React`并不是`ReactAPI`的一部分，而是一种设计模式

![[00 assets/ebe8f53945dcd7bb51bb1d14553b74af_MD5.jpeg]]

### 2.10.2 应用场景

#### 2.10.1.1 props 增强

> 基本使用

下面就是对`props`的处理，这样只要传入的组件，里面都会带上`personInfo`的`props`

![[00 assets/3220f3063c1ff6cad658cf9a9756478f_MD5.png]]

当然我们传递`类组件`和`函数组件`也是可以的，只要经过`enhancedProps`的高阶函数，那么就会自动带上`props`

![[00 assets/c8c51a98299099afeb94517c3bb7d79e_MD5.png]]

![[00 assets/0b8ac93e74509de8e69e14de4142dc88_MD5.jpeg]]

#### 2.10.1.2 Context 封装

其中一个就是对于`Context`的高阶处理，这里可以参考我`Context`的笔记，里面的传值和取值很麻烦，所以我们直接使用高阶函数来抽象，这样更易维护

下面的`enhancedContext`就是对`Context`取值的抽象处理

![[00 assets/098ee50de3ebec44af030b55cbc827ff_MD5.png]]

对于封装好的`enhancedContext`直接使用即可，最后作为`props`的值来处理

![[00 assets/4fc699e37455360fbf4299d93112b4e5_MD5.png]]

#### 2.10.1.3 登录鉴权

我们还可以使用`高阶组件`来做登录鉴权的处理，只需要将需要登录鉴权的组件放入`loginAuth`即可

![[00 assets/f3598d7253d485bde2abc3e009d39b05_MD5.png]]

放入`loginAuth`的`高阶组件`即可对登录进行鉴权处理

![[00 assets/cae4241a02b2345c73b7c46fbffa9d98_MD5.png]]

#### 2.10.1.4 生命周期劫持

我们也可以对`生命周期`进行劫持处理，这样我们就可以计算该组件的`渲染时间`

![[00 assets/5c726e64643649b05920c62d30037d07_MD5.png]]

![[00 assets/b6abd6f63b3774f4bde1110b2de917d7_MD5.png]]

### 2.10.3 HOC 意义

其中对于`memo`、`forwardRef`都是一个`高阶函数`

![[00 assets/ba8cff663e10eb0b9094943ec4f592b8_MD5.png]]

### 2.10.4 createPortal

![[00 assets/03509fa3fed81ae7e452f417acef3738_MD5.png]]

我们使用`createPortal`就可以将该组件转移到`div的home`中，这样就可以实现一些特殊的操作。不能直接在`App`中返回`createPortal函数`，这样就会报错

![[00 assets/b73c5902d4691e7cfbd21ada01c9c354_MD5.png]]

\*我们还可以将插槽中的值进行传进`createPortal`中

## 2.11 Fragment

可以理解为`Vue`中的`template`，作为一个`片段`来处理，最后是不会渲染到页面中

![[00 assets/ef84a7519d63c285fcba3fe6e73b983b_MD5.png]]

当然`Fragment`存在一个`语法糖`的写法。但是这种语法糖对于使用`map`遍历的时候不能使用，因为需要在里面添加上`key`，如果使用下面的`语法糖`的话就不能添加`key`了

![[00 assets/5fd417f4daa4793f84191c29dc60c662_MD5.png]]

## 2.12 StrictMode

### 2.12.1 基本使用

![[00 assets/69d59702bbf8a11d959bb7f1110fbfc9_MD5.jpeg]]

我们使用`StrictMode`包裹的组件就会在内部开启严格模式，即便里面有组件的嵌套

![[00 assets/fbafd0c925b905c65a5c43a184679059_MD5.png]]

### 2.12.2 检测范围

![[00 assets/be4716b3e5f7f6fba2520549904bd215_MD5.png]]

比如下面就是会自动检测是否使用`React`过时的`API`，就会报错处理

![[00 assets/df9e9fd9e16ec046aebce883f9c7c802_MD5.png]]

## 2.13 过渡动画

### 2.13.1 基本介绍

`React`现在本身是没有集成`动画库`，所以需要我们自己来下载使用，下面使用的就是官方推荐得`react-transition-group`动画库

![[00 assets/97f6c4dba1f06a0f4ad0083be432ba2b_MD5.png]]

该库中包含下面得 4 种组件，我们一般都是使用的`CSSTransition`组件来实现过渡动画

![[00 assets/eec65b193141976c9f3dac31480ca777_MD5.png]]

其中`appear`表示第一次展示的时候的状态，`enter`表示进入的时候的状态，而`exit`表示离开状态

![[00 assets/a4cd1d5104bc8c69cb4acec23f72b25e_MD5.png]]

### 2.13.2 CSSTransition

下面就是基本的使用过程

1、使用`CSSTransition`包裹，并且下面只能由一个子元素，如果存在多个的话就会报错

2、其中`in`表示`开启`和`结束`得控制，`true`表示开启，`false`表示结束。并且`unmountOnExit`表示动画结束之后将`组件移除`

3、`timeout`是表示动画的时间，也就是`transition`中的`2s`，这里表示的是`ms`

4、动画首先是执行`why-enter`和`why-enter-active`，然后再来执行`why-enter-done`

![[00 assets/2caae00185be799414eec1cbc11ff9bf_MD5.jpeg]]

5、我们添加了`appear`属性表示组件刚刚加载得时候出现得动画

![[00 assets/0e8949ea7e564123a1174f9926a48546_MD5.png]]

### 2.13.3 钩子函数

我们只要经过了执行得动画之后就会执行`钩子函数`

![[00 assets/0a4ea055014d81555e3e33a11912a985_MD5.png]]

### 2.13.4 SwitchTransition

![[00 assets/0cf00fa4d52adad6d65c81c580afef35_MD5.png]]

1、`SwitchTransition`表示该组件用于动画得切换效果，其中`mode`表示动画显示得模式，`out-in`表示动画主体先移走再移入

2、其实本质就是`SwitchTransition`控制`CSSTransition`得动画，下面得`key`就表示得`in`

![[00 assets/86029320569a8c4576215c4405998a04_MD5.png]]

![[00 assets/8a4dadb27b2be6f75495ddf294a05e37_MD5.gif]]

### 2.13.5 TransitionGroup

使用`TransitionGroup`来包裹多个动画组件，其中`component`属性表示要包裹下面得标签

![[00 assets/1f1488f98ed949499b7c5946b74fceb4_MD5.png]]

![[00 assets/223da985b385a7e147a4bed3ca954dbb_MD5.gif]]

## 2.14 CSS 编写

### 2.14.1 基本介绍

> 组件化开发下的 CSS

![[00 assets/ce1c57582a0cc92bf37be3240811549a_MD5.png]]

> React 中的 CSS

![[00 assets/05f2ac5350b84d7190df1846881ecc86_MD5.png]]

### 2.14.2 编写方式

#### 2.14.2.1 内联样式

![[00 assets/808eb8c34214391b1100ed0c2d91d10f_MD5.jpeg]]

1、我们可以使用对象的形式来编写样式

2、因为在对象中不存在`background-back`的写法，所以就需要使用驼峰写法

3、我们也可以编写`state`来动态控制样式属性值

![[00 assets/e9d9cc3709bb3e800560085fbadc73c2_MD5.png]]

#### 2.14.2.2 普通方式

![[00 assets/4bd4e9f1724495b50bd4eac3b1c832a3_MD5.png]]

就是将`.css`文件引入来使用，这种方式就是样式都会互相影响

![[00 assets/2903b5811e5188f45a4ca50ec3d38501_MD5.png]]

#### 2.14.2.3 CSS Module

![[00 assets/133472782062b752363ffc32701870e1_MD5.png]]

1、需要将`.css`改为`.module.css`的后缀方式，然后使用`模块化`的方式来导入

2、最后使用的话，就是`导入名.类名`的方式来使用。这样使用的话就不存在样式冲突的情况

![[00 assets/cb9ed25f4d2bafd492d71a284b964b87_MD5.png]]

对于其他组件的使用也是一样的

![[00 assets/6bb17f399de65063fb524fb89df6cda8_MD5.png]]

其实这个本质就是动态添加一个`独特`的类名，其中就是`组件名_类名__样式值`得方式来区分

![[00 assets/09ed7b0a683ab6a2c6736841c04a1634_MD5.jpeg]]

#### 2.14.2.4 CSS in JS

##### 2.14.2.4.1 基本介绍

![[00 assets/24bbbd72adb1ba48b0b1e14268447fa9_MD5.png]]

![[00 assets/eea0682835327c434508c035ac41fafb_MD5.png]]

##### 2.14.2.4.2 基本使用

```bash
npm i styled-components		// 安装styled
```

如果需要的话，可以下载一个`styled-components`的插件

![[00 assets/7fe0531f0826b47652085c90c824c490_MD5.png]]

1、我们需要使用`styled.div`来创建一个`div`标签，最后导出包裹在要设置样式的地方

2、我们使用`模板字符串`来调用`styled.div`中的函数，里面就编写相应的样式即可

![[00 assets/8ea1bb0ce8094edbc6a641facab74ccb_MD5.png]]

里面的样式就是按照下面的规则来编写的

![[00 assets/969c23f8a8a48304bd3f2d1c2754a32a_MD5.png]]

##### 2.14.2.4.3 高级特性

> 1、样式抽取

和我们抽取组件是一样的，将相应的组件抽取出来使用

![[00 assets/d88f026b1b60cda45a1c74e9c675f0ac_MD5.png]]

> 2、props

我们可以使用`props`对其组件传递参数，最后使用的话就是使用箭头函数返回值处理

![[00 assets/5bab100656c20196c9f1e7fdd83b3d94_MD5.png]]

> 3、默认值

1、其中`styled.div`存在一个`attrs`属性来设置默认值

2、其中`attrs`中的参数要是函数，下图中存在`({ ... })`的写法，其实是返回对象。如果只是写`{ }`的话就是函数的代码块了

3、作为默认值是使用`... || "xxx"`的形式来处理的

![[00 assets/158114709f360f3e662bdb67ca48c84c_MD5.jpeg]]

> 4、实现继承

![[00 assets/a2e52067d3dd88c9cc766fe624c36d63_MD5.png]]

##### 2.14.2.4.4 全局变量

我们有的时候需要将一些`CSS属性`抽取为全局的样式，所以设置一个属性值。其中`styled-components`为我们提供了下面的 2 种方式

> 主题样式

在要覆盖的组件中编写`ThemeProvider`组件，为组件提供`theme`属性，其中属性值为一个对象

![[00 assets/952b272c849e04788578e81ad63f6008_MD5.png]]

> 引入变量

我们可以单独编写一个文件`variables.js`文件，专门存储样式值。需要的时候使用`import`来引入使用

![[00 assets/4d0a977413cafc8e115ea1f7514e03da_MD5.png]]

### 2.14.3 动态 Class

> 传统方法

![[00 assets/0ca6173b9de7d5e95d86a664446dffba_MD5.png]]

> classnames 库

![[00 assets/125e3bbe778c68985fecc5fcf7a55583_MD5.png]]

```bash
npm i classnames // 安装classnames
```

其基本得使用和`Vue`中是差不多得

![[00 assets/b4043436d912ae44096d6c429b5e3e61_MD5.jpeg]]

# 3. 状态管理 - Redux

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

# 4. 路由管理 - Router

## 4.1 基本使用

![[00 assets/08fda75a8395436cc8f65b0534da0b26_MD5.png]]

```bash
npm i react-router-dom	// 安装
```

![[00 assets/08bccc6647417c6670798bff93cb54d0_MD5.png]]

![[00 assets/f6b8296c79a0675c29a08d0e2b83f375_MD5.png]]

![[00 assets/ba178202388e964f0ff74dff52245c2a_MD5.png]]

1、下载`raect-router-dom`，并且导出`HashRouter`和`BrowserRouter`包裹，这样整个`App`就可以使用路由

2、`Routes`包裹`Route`，表示单个路由。使用`Link`表示导航，其实底层本质就是`a标签`

![[00 assets/cd4dd165c75fd40193dfafe43c3ee5d0_MD5.png]]

## 4.2 Navigate

![[00 assets/5f1db87996518de1118b8f056f84e3b3_MD5.png]]

1、`Navigate`本质就是做重定向。下面就是登录场景的重定向，我们点击登录之后重新执行`render`函数，就会将`Navigate`挂载上去，就会自动执行`/home`的路由

![[00 assets/97105ee45d7494e04f847e75d4d90c08_MD5.jpeg]]

2、我们之前是按照这样的方式来加载重定向的，这个本质会加载 2 个`Home`组件，所以不是最优解

![[00 assets/e00b6d01a4d4e15140c217867ef41463_MD5.png]]

我们直接使用`Navigate`组件就可以解决这个问题即可，只要加载`/`就会跳转到`/home`

![[00 assets/05a5f300d8c3fc82edcfb8191fe939a9_MD5.png]]

## 4.3 路由嵌套

![[00 assets/b27ff5b8a861567c4d3dc3780ca34402_MD5.png]]

1、下面就是路由嵌套的原理，这样我们输入`/home/banner`就会跳转到`HomeBanner`。并且需要注意，如果你写在`/home`映射下面，就必须要带有`/home/xxx`才能正常使用

![[00 assets/5e5fdaec2574e9c3042adfc67c238616_MD5.png]]

2、在`Home.jsx`中直接使用`Link`标签确定路由，并且使用`Outlet`来占位，类似于`Vue`的`RouterView`，只要切换了路由就会将`组件`填入到`Outlet`

![[00 assets/c3a452ba8f52080ad2451bddeb0c9936_MD5.png]]

3、这里有一个小细节，`Outlet`组件只作为父路由中的子路由的元素。假如我在`About`和`Home`中分别写上`Outlet`的话

![[00 assets/5249b2adadae6d5a9b5e7b7ce116ac7a_MD5.png]]

就会根据路由映射来写入子元素的内容

![[00 assets/9e655f2a3d09402633ca653e5273fb60_MD5.png]]

## 4.4 手动跳转

![[00 assets/3cc5dac65f28c893e52e9f0bfbb5c1cc_MD5.png]]

1、我们需要手动的跳转路由就需要使用`useNavigate`函数，但是我们在`class`组件中使用就会报错

![[00 assets/2fc9a7ba23cf6067d3e3f401ed05c7df_MD5.png]]

现在唯一的方式就是使用函数组件来处理，或者采用`React Hook`来处理。在类组件中没有方法

![[00 assets/3b69afec29cf65eb872e57976e39607c_MD5.png]]

2、假如我们要在`类组件`中实现这类效果，就需要封装高阶组件来处理

3、我们在函数组件中使用`useNavigate`，因为后续可能通过`router`来传递其他的数据，所以将`navigate`方法通过`props`传递给类组件

4、在类组件中通过`this.props`来接收传递的函数，进行路由的跳转

![[00 assets/551857b3aa650e8ea7fc82e7ffc9c489_MD5.png]]

5、这样嵌套内层的路由也可以跳转到其他上层路由中

![[00 assets/7ae619771428db53d01e00a4cc714e07_MD5.png]]

## 4.5 参数传递

![[00 assets/7ab49d482d50e430ceeffe4950be9e76_MD5.jpeg]]

> params

1、配置路由映射得时候添加`:id`，这样我们输入`/home/songInfo/100`得时候就可以获取到`id`为 100

![[00 assets/4bada381c9cbba04e7d2dbf256f265e0_MD5.png]]

2、我们编写高阶组件`withRouter.jsx`，为里面添加`useParams`函数，并且传递出去即可

![[00 assets/06965b04bac0d3744fed660ab137d820_MD5.png]]

3、使用高阶组件`withRouter`来包裹，右边得组件使用用于跳转路由得，左边得组件时用于接收参数得。

![[00 assets/46b9c11d32b1557a31b54082a1af2b74_MD5.png]]

> query

1、发送`query`参数得`URL`

![[00 assets/c7198256e83e79720f409cf90cb6b3ce_MD5.png]]

这里有一个注意得点，就是`Query`参数不需要在后面编写类似`:id`得标识

![[00 assets/4f8440c990b25731428145231d6195af_MD5.png]]

2、这里存在 2 个方法来解析`query参数`，第一个`useLocation方法`相对来说比较难，但是基本都是使用第二个方法。将数据解析出来之后通过`props`传递即可

![[00 assets/3dc214355b6b0b8742544f14822381da_MD5.png]]

获取`query`然后使用就行

![[00 assets/0e0c22c75f230c709f1e7b1d66243c99_MD5.png]]

3、这里解析一下`useSearchParams()`返回得参数`URLsearchParams`，下面是`MDN`得解释

![[00 assets/65c7fe27b89df77eff4f732a4befae8c_MD5.png]]

1、我们看下面打印得结果可以看到，首先`URLSearchParams`是实现了`entries`函数，并且`URLSearchParams`内部就实现了迭代器，并且迭代器得名字就叫做`entries`，所以本质`entries`就是迭代器

2、并且我们使用`entries()`返回得对象使用`next()`就会输出数据，这一部分得源码可以参考我`ES6 迭代器`得笔记

3、我们使用`foreach`来遍历得时候可以看到最后得结果其实就是`[["name","zs"],["age",18]]`得格式，这里其实就是`ES8`得`entries`得格式，所以这里我们使用`Object.fromEntries`转化为对象

4、并且遍历`searchParams`得时候，就是遍历`searchParams.entries()`

![[00 assets/ed84bed7d2cc01d59cca53e3f2261ff2_MD5.png]]

5、下面就是模拟的上面的`searchParams`，可能因为历史遗留问题，所以底层可能不是这么实现的。但是本质就是下面的代码，迭代器遍历，只不过数据模式不是常见的`对象模式`

![[00 assets/a8c013475bcffd5be72f5e4e00681a52_MD5.jpeg]]

## 4.6 路由配置

### 4.6.1 路由抽离

![[00 assets/fb5f8d805049229a83ad37d20417acb2_MD5.jpeg]]

1、我们一开始默认在`App.jsx`中编写得路由映射存在问题，当项目变大之后，入口文件`App.jsx`就会变得很大，所以就可以使用类似`Vue`得路由配置，将路由信息抽离出去。

其中得属性都是和原本得路由映射是一一对应得

![[00 assets/47f7bfbece0ca3996aebc8888ad2875a_MD5.png]]

2、最后在函数组件中使用`useRoutes`，并且导入刚刚得编写的`routes`，它就会将数组变为路由映射，这样就实现了路由配置信息的抽离

![[00 assets/3f1e7309820899dd60462b11bb1a2653_MD5.png]]

### 4.6.2 路由懒加载

1、其实`import(...)`是`webpack`的特性，这样我们打包的时候就会分包处理，提升首屏开启速度

![[00 assets/e9cfe1579e970050fa60f55fb406f19f_MD5.png]]

2、但是存在包还没下载下来，但是路由已经跳转进去的情况，这个时候需要做应急处理。这个时候就需要使用`Suspense`高阶组件来处理。这样即便没下载到包也可以内容可以显示

![[00 assets/77b30af2ff249e9e8dbcc6eeb864254f_MD5.png]]

## 4.7 额外使用

### 4.7.1 NavLink

![[00 assets/bbb79241be71ea7a2802bdcf5368c317_MD5.png]]

1、`NavLink`使用的场景不是很多，和`Link`唯一的区别就是可以添加`style`和`class`。下面就是一种，只要你点击之后就会将颜色变为`red`

![[00 assets/348d3b0d0e0c5a34139a981977188d7c_MD5.jpeg]]

我们点击之后`style`会自动变化

![[00 assets/92f2f4eb7c8843dc9f06429a5b52c48b_MD5.png]]

2、对于`className`的本质也是和`style`差不多，点击之后修改`style`或者`className`

![[00 assets/8d84ef458e723d902d2df0753980b44b_MD5.png]]

### 4.7.2 NotFound

`path`为`*`的话表示统配，这样不知名的路由就会跳转到`NotFound页面`

![[00 assets/fe738d1da181bfcdb9d3f10811a2063b_MD5.png]]

# 5. 脚手架 - Hook

## 5.1 基本介绍

### 5.1.1 基本介绍

> 为什么需要 Hook

![[00 assets/165527960cdaa8f69bf51333bd080756_MD5.png]]

> Class 组件存在的问题

![[00 assets/a5c6468f00cd5658f824692f89318002_MD5.png]]

> Hook 的出现

![[00 assets/34129884ab0fee91651b51356a1dc05b_MD5.png]]

### 5.1.2 使用差别

> Class 组件和 Functional 组件对比

![[00 assets/b00d19959203a27ffd1eb5503643ac96_MD5.png]]

> 计数器案例对比

下面分别编写了`Class组件`和`Hook`语法的实现，可以很明显的看出代码量少很多，而且更加易读。所以现在也大部分都会使用`React Hook`来编写

![[00 assets/f69b1da3c626ff127ab2320facf91d85_MD5.png]]

![[00 assets/c987bf3bd5a104ee48bb5d108cf184fa_MD5.png]]

## 5.2 useState

![[00 assets/72f823a026d78dcff5ff5166fd7046be_MD5.png]]

1、下面就是`setState`的基本使用

![[00 assets/f51937c610641e49afec5c4685c74935_MD5.png]]

2、并且使用`useState`的情况下，我们可以将`Hook`移出组件，但是是有条件的。只能在`useXXX`的函数中移出，假如是`XXX`函数就会报错

![[00 assets/71e11962448c02d93bd3ea39b023af94_MD5.png]]

3、原生的函数在结束之后内部的变量就会被销毁，但是我们使用`useState`的话，内部就会将状态交给`React`来保存，所以就不会导致每次加载组件的时候数据消失

![[00 assets/10f91e8d1abb33b4e1a5c5ba77e2741e_MD5.png]]

4、对于`useState`还可以传入函数，这就会将这个函数的返回值作为`count`的值，如果这样写的话就可以提取对数据进行一系列的操作再返回

而且`useState`内部函数只执行一次，也就是组件渲染的时候执行，后续即便页面渲染也不会再去执行

![[00 assets/fe27d0b2db16e122e063253df009ce09_MD5.png]]

## 5.3 useEffect

### 5.3.1 基本使用

![[00 assets/c1535a75ff240194fd6e080c384dbdc6_MD5.png]]

1、下面就是实现的`count`数字增加，网页标题就随之改变，可以很明显的看出使用`Hook`的写法会简洁很多。

2、这里使用了`useEffect`的`Hook`函数，这个`Hook`只要页面重新渲染就会执行一次。而且`Effect`也表示副作用，很明显`doucument.title`就是很明显的副作用，我们可以将这类操作放在这里

![[00 assets/850bfb6bb2081788f7210e9e65ac66d4_MD5.png]]

3、对于`useEffect`可以返回一个函数，并且每次执行组件的时候先优先执行返回的回调函数。这样我们就可以在这个回调函数这种进行一些取消订阅的操作，但是基本很少这样使用

![[00 assets/daecf7de86d29553b20f4f706f328775_MD5.jpeg]]

![[00 assets/113e080be2cedacf472594cd89ae4299_MD5.png]]

4、`useEffect`一般都是函数`return`组件渲染完成之后才会执行`useEffect`，但是`useLayoutEffect`则是在`组件渲染`之前进行操作

### 5.3.2 Effect 抽取

![[00 assets/7347b0a7c29d52e3e0d86ea62036eff5_MD5.png]]

我们可以将多个`Effect`进行抽取出来，这样逻辑会更加清晰，并且这些`effect`会由上到下依次执行

![[00 assets/5c2cf7a986a6de15ea56c1b8dbc77fa2_MD5.jpeg]]

### 5.3.3 性能优化

![[00 assets/053ec8078c39b0d648d1367886dd96df_MD5.jpeg]]

1、`useEffect`存在第二个参数`[ ... ]`，里面的参数只要改变就会执行`useEffect`

2、如果只是传入`[ ]`的话，就只会在组件挂载的时候执行，如果组件再次渲染也不会执行

3、如果没有传入`[ ]`的话，只要组件渲染就会执行一次

![[00 assets/b4e530f0f9e8dc3b1166bb5ec701c998_MD5.png]]

## 5.4 useContext

![[00 assets/18b9017d03e3fc262b802ffd0784eee9_MD5.png]]

1、下面是我们之前使用`Context`的步骤，非常的复杂，并且一层层嵌套处理。所以在`Hook`中可以直接使用`useContext`来处理

![[00 assets/aad46b33c7221b4d00b6508982f00134_MD5.png]]

下面为创建`Context`的方式

![[00 assets/4fdf0c7a908ed1180921eb430505f19a_MD5.png]]

我们换为`useContext`就可以发现，使用的过程简单很多

![[00 assets/6f42d35ff654ba9034a9a4101f94cedb_MD5.png]]

2、只要`Context.Provider`中的数据发生了改变，在使用了该`Context`的`useContext`就会返回一个新的`Consumer`，然后再去重新渲染页面

![[00 assets/ef699ddc258e560c38cf206295e69190_MD5.png]]

## 5.5 useReducer

![[00 assets/b7daf7c7b02ca4d6074dcdd75b4a54eb_MD5.jpeg]]

1、下面就是`useReducer`的用法，其实就是`redux`的一套使用流程，使用这种方式来编写的概率很小，所以只是了解这个`Hook`

![[00 assets/25ec289c4a60407efe0ca01d7f93d465_MD5.png]]

2、其实使用`useReducer`是为了管理更加复杂且多的数据，如果数据很多，就需要编写很多的`useState`，这样就难以管理，但是实际情况也很少使用，如果数据真的很多就会使用`redux`

![[00 assets/9f708a0e2428c34bd82714fcc6bd27c1_MD5.jpeg]]

## 5.6 useCallback

### 5.6.1 闭包陷阱

![[00 assets/8f40882bb93411b020e6062d1bc51d09_MD5.png]]

1、我们每次调用`App`的时候就会定义一次`increment函数`，如果组件渲染又会定义一次，这样每次数据修改就会定义同一个功能的函数，所以这里可以使用`useCallback`来做性能优化

![[00 assets/2f8745b3c226d58d13134d51f88a13a3_MD5.png]]

2、这里存在`闭包陷阱`的问题，可以看下面的例子。

我们定义了`f1`并且为`name`传入`zs`，所以这个时候`bar`内部的`name`为`zs`。我们再定义`f2`并且为`name`传入`ls`，这个时候`name`值被修改了，再去调用`f1`的时候就会发现`name`依旧是一开始传入的值，并未做修改。所以可以得出一个结论，就是闭包获取出来的值就是定义的那一刻的值

![[00 assets/bb0eb56067547f44039178c3303a089a_MD5.png]]

我们换成`num + 1`就会发现问题了，只会取一开始定义的值来处理，后续即便`num`修改，也会一直执行一开始闭包保存的值，也就是存在`记忆性`

![[00 assets/52d863246536914ac7dc7c36b5057439_MD5.jpeg]]

3、所以我们换成这里的`useCallback`并且添加第二个参数`[ ]`的话也会存在上面的闭包陷阱，这样就不是每次都创建一个新的函数，而是使用之前的函数来处理

因为每次执行`组件`的时候就会执行一次函数，那么`useCallback`就会重新创建一个`function`，所以就会存在`foo1`、`foo2`、`foo3`......函数，其中每一个函数都会默认记录上面的`count`。因为我们添加了第二个参数`[ ]`的话，那么`useCallback`就会记录一开始的`foo1`，并且每次组件渲染的时候就调用`foo1`，即便创建了`foo2`。但是这个函数的`count`是一直没有改变的，所以就会导致数字一直卡在`1`，并不会增加，也就是我上面例子中的样子

![[00 assets/602348c0b0ae821ff43f4b5d69c4f544_MD5.png]]

这个时候就存在一个疑问就是，以前写的函数为啥就不存在闭包陷阱呢？这个就是函数直接调用和`回调函数`的区别了，外面实在`useCallback`中回调的函数，这里面直接获取函数外部的值就是闭包处理，所以就会存在闭包陷阱的问题

![[00 assets/760da396d9aa43c8b8f07d91a63d406a_MD5.png]]

4、假如我们要解决这个问题的话，需要往`useCallback`中添加参数。这样只要`count`发生了改变，就会创建一个新函数`foo2`，这个时候就会重新读取闭包外部的`count`的值来执行

![[00 assets/cf9bba8a74add58287dd000e0711d209_MD5.png]]

但是我们折腾这么长事件来解决这个问题，最后还是需要重新创建回调函数的形式获取值，这还不如直接使用`const increment = () => setCount(count + 1)`来处理，其实这个优化的就是将这个函数传递给子组件的时候使用的

### 5.6.2 性能优化

> 子组件优化

1、其实`useCallback`就是做下面的性能优化的，我们将`increment`换为普通函数

2、当我们点击`onClick={increment}`的时候，就会重新渲染子组件`MessageComponent`，这是因为每次进入都是创建的新函数，所以就需要重新渲染

3、当我们点击了`onClick={()=>setMessage("你好啊!")}`的时候就会发现依旧会重新渲染`MessageComponent`，这也是因为每次都是重新创建的新函数`increment`，即便你没有做数据变化，也会重新创建

![[00 assets/b03a66fdbc80f7708f30735a31b0279d_MD5.png]]

4、所以这里我们使用`useCallback`的话，就可以避免这个问题。只要`count`不去改变就会不会去使用新的函数，也就不会导致`MessageComponent`的`props`变化，然后更新子组件

5、这虽然只是一个看起来不是很大的优化，但是落地在实际项目中会有很多的子组件，如果都这样直接用普通函数来处理的话，就会导致重新加载了很多的子组件，造成性能的损耗

![[00 assets/eb946bbf80a1661fcbd58f8b0add58c5_MD5.jpeg]]

> 内部函数优化 + 子组件优化

1、我们之前一直都是创建一个新函数来获取`count`的值，所以`props`就会更新，所以就会重新渲染`MessageComponent`组件

2、但是这种重新渲染和重新创建函数的方式还是比较浪费性能，如果能一直都是同一个函数，这样即不用重新创建函数，而且传入`props`的值也不需要重新渲染组件

3、如果使用`useRef()`的话就可以解决这个问题，因为`useRef()`会返回同一个对象，即便组件重新渲染了很多遍，也还是同一个对象

4、下面的方式就是返回同一个`ref`，每次都是获取最新的`count`赋值给`countRef.current`，`useCallback`也不会需要为第二个参数传值，因为依赖已经被`ref`取代了，只需要使用 useCallback`的记忆性即可

![[00 assets/9910b60f99a71e8e23fed7d21afa22d6_MD5.png]]

## 5.7 useMemo

![[00 assets/b7e9a03e009b4c529634a1d0f4496886_MD5.png]]

1、我们会写一些工具函数来处理数据，比如：`1-50`之和的计算......，我们每次渲染页面的时候就会执行这个函数，所以就会导致性能的浪费。如果我们只要执行一次这个函数，并且保存该值就不需要重复执行了

![[00 assets/0d243c02a49f613032b2201b744a3b94_MD5.png]]

2、这里我们可以使用`useMemo`来记忆这个值，这样就不会重复执行，而是只执行一次。而第二个参数和`useCallback`一样，传入的参数就是作为依赖来处理，只要依赖值改变就会重新执行这个回调函数

3、`useCallback`是记录的回调函数，而`useMemo`则是记录的返回值，所以还是有区别的

![[00 assets/12dc37a6dde3c327cbb5d9d2c520c2ba_MD5.png]]

4、如果我们写入依赖的话，只要`count`改变就会重新执行这个回调函数，并且返回值

![[00 assets/e950bf79e7121035e565e477bfa45dd8_MD5.png]]

5、但是对于子组件来说，我们传入对象的话，只要每次执行重新执行组件函数，都会重新赋值对象，所以就会重复执行子函数

![[00 assets/01dc86271991824ba37b850aed682f7e_MD5.png]]

所以这个也可以使用`useMemo`来进行优化，这样每次都不会重新赋值对象，所以就不会重新渲染子组件了

![[00 assets/ca47879d255fc8510702ccde1be2c0b3_MD5.png]]

## 5.8 useRef

![[00 assets/442a1b4c34569a62e6974ef1693e67bb_MD5.png]]

1、下面就是引入`DOM`的操作

![[00 assets/5bc643224002098f198ba7d654eefeba_MD5.png]]

2、这里验证每次返回出来得`ref`都是同一个`ref`

![[00 assets/d3894f8bb6700c6742999120aabed595_MD5.png]]

3、其中保存上一次保存值得功能在`useCallBack`中性能优化中使用过，可以回去参考

4、下面就是如何在父组件创建`ref`，绑定子组件得`DOM`元素

![[00 assets/b4797a80f726262cd621a984a257ea48_MD5.png]]

## 5.9 useImperativeHandle

![[00 assets/5471a871dd6555e644fa183d1e085ae2_MD5.png]]

1、传入子组件`ref`获取其中得`DOM`。在子组件需要嵌套`forwardRef`函数，并且`memo`和`forwardRef`不能颠倒顺序，`forwardRef`第二个参数就是传来得`ref`，传入到想要获取得`DOM`即可。这样我们在父组件中就可以直接操作子组件

![[00 assets/b4797a80f726262cd621a984a257ea48_MD5.png]]

2、但是对于一些情况，我们并不想直接被操作元素得`DOM`，而想去做一些拦截处理。所以就会去使用`useImperativeHandle`拦截`DOM`得操作，最后直接将返回得对象传递给`ref`，而且这个`ref`就是`inputComponentRef`，所以`inputComponentRef`只能按照返回得属性和函数来操作

3、一般情况下很少使用这个`Hook`来操作，可能在一些库里面见到

![[00 assets/c0c9e4acee914185e80a32dc138738b1_MD5.png]]

## 5.10 useLayoutEffect

![[00 assets/f2b560c200204158636ccde8f1b1ad35_MD5.png]]

1、下面就是`useLayoutEffect`和`useEffect`得执行顺序得区别，`useLayoutEffect`就是渲染之前处理，而`useEffect`就是渲染之后处理

![[00 assets/e0cd74fcda7a55de5e9775089f2a5911_MD5.png]]

2、假如我们使用`useEffect`就会导致下面得问题，所以就可以使用`useLayoutEffct`来解决这个问题

![[00 assets/81d9c59616c54c6987ab211d55919b77_MD5.png]]

## 5.11 自定义 Hook

### 5.11.1 生命周期

我们使用`useEffect`就可以实现生命周期的打印处理

![[00 assets/8797bfe1321ddde2ff5f2c22e0fe03f8_MD5.png]]

### 5.11.2 获取 Context

我们在外面的`.js`中封装一个`UserTokenContext`的函数，这样在其他组件使用的时候直接导入`UserTokenContext`即可

![[00 assets/8b92cc7cac2efd71a08f08b3e95135dd_MD5.png]]

### 5.11.3 监听窗口位置

![[00 assets/88f4fd9f93061de1385dece76b744158_MD5.png]]

### 5.11.4 localStorage

1、`useState`可以传入函数，并且可以将函数返回值作为参数

2、下面就是`localStorage`的操作，其目的就是想要渲染`loacalStorage`的数据，只要数据改变，就同时改变内部的`localStorage`的值和`State`的值，并且重新渲染页面

![[00 assets/0681c851b7edb2bcb3705a373a8a5e6c_MD5.png]]

## 5.12 redux Hook

1、我们之前使用`redux`的时候需要编写`connect()()`高阶函数，并且需要写`mapStateToProps`、`mapActionToProps`.....一系列的函数，这导致代码变得很多

![[00 assets/611f062c4dacd7b3b4c41feff1ff051a_MD5.png]]

所以我们可以使用`Hook`得方式来编写，这样就轻松很多

![[00 assets/eca1b887a59f9c1db7e9910aa2738260_MD5.png]]

2、这里也存在一些性能优化的问题，和前面的`useCallback`...是一样的问题

![[00 assets/e3c12732e7cd05bf47052dd5b1b88b7a_MD5.png]]

我们不管是修改`App组件`或者`Home`组件里面的数据，都会重新渲染。这是因为都会重新从`stroe`中拿去数据，所以都会统一发生组件渲染处理

![[00 assets/d6c8d50865d92e2ee86dbddd5398b543_MD5.png]]

3、`useSelector`存在第二个参数，可以用作参数的比较。但是一般情况我们都是直接传入`shallowEqual`做处理

![[00 assets/b4bf7d0728268e2cf9af026405060a0a_MD5.jpeg]]

这样做了参数比较就不会出现重复渲染的问题

![[00 assets/ab4af3d981c8d2b7c7c7621a44093bac_MD5.png]]

## 5.13 useId

### 5.13.1 SPA/SSR

![[00 assets/c03725cd98485a847caa3c90583e71ee_MD5.jpeg]]

> SSR 同构应用

![[00 assets/a3ae36ee6c4c76e84865510404fc2c78_MD5.png]]

> Hydration

![[00 assets/d0019e2957efb82f5d0c6f8473778509_MD5.png]]

### 5.13.2 基本使用

这一段内容在`SSR`的笔记中进行处理

![[00 assets/24177a2ca0ffed1cfc14c55b7f3b806a_MD5.png]]

## 5.14 useTransition

![[00 assets/90c7021d9a3433eab57b716de5272ea9_MD5.png]]

1、我们可以使用`faker.js`来生成一些伪数据

```bash
npm i --save-dev @faker-js/faker
```

![[00 assets/b196610f6325e5a0119dbafc20207fb4_MD5.png]]

2、我们一次处理`10000`条数据，可能存在页面卡顿的情况，并且每次为`input`输入数据的时候，`input`也会卡一会，这个体验就很差，所以可能使用`useTransition`将数据过滤和页面渲染先降低优先级，先渲染`input`的输入字符的显示

![[00 assets/6084902c8ee4cbc92e83b11b9a1c5460_MD5.png]]

3、`setTransition`中是一个回调函数，将执行的逻辑放入就可以降低优先级

4、`pedding`是作为参数存在，只要在加载的话就为`true`，如果加载完毕就是`false`，所以一般都是加载`Loading`画面使用

![[00 assets/4bcda4272c02f2d62f7b40dccbde0a46_MD5.png]]

## 5.15 useDeferredValue

![[00 assets/444da656543afd951f163890175dbc7c_MD5.png]]

我们使用`useDeferredValue`备份一个副本，只要修改了数据就会延时放入`deferredValue`进行数据渲染。本质和上面的`useTranstion`的效果是一样的

![[00 assets/33b822176049385e5397ae8b5eb9f7c2_MD5.png]]

# 6. 项目 - 爱彼迎

## 6.1 基本介绍

### 6.1.1 项目介绍

![[00 assets/fac5721569eb3795a60c7048184e3b25_MD5.png]]

### 6.1.2 项目规范

![[00 assets/f3c884d8aba19d1de50dd45237efb423_MD5.png]]

![[00 assets/e2be9b657163e2e0f6da0fa49dcc3edb_MD5.png]]

## 6.2 项目搭建

### 6.2.1 基本搭建

![[00 assets/ef9632b2bb345b4129093efb30df958d_MD5.png]]

1、通过`webpack`来初始化项目，使用`create-react-app xxx`来创建新项目

2、进入项目之后，删除不相关的文件，编写测试代码让项目跑起来

![[00 assets/6420b1a79c84bf28f86cc6ace0547e1e_MD5.png]]

3、配置网站图标和标题

![[00 assets/e8f86b10f498eb47ecc876b19f842d13_MD5.png]]

### 6.2.2 目录划分

![[00 assets/0131d5e0f1bc29a34f9389c167cdce4c_MD5.png]]

### 6.2.3 配置 craco

1、因为`react`默认使用隐藏`webpack`的配置，但是我们最好不要使用`npm run eject`来显示`webpack`，并且对其进行修改

2、所以我们可以使用插件来默认配置文件别名和样式，`npm i @craco/craco -D`

> 配置别名

1、我们创建一个`craco.config.js`来配置`craco`，后面就基本和之前配置`webpack`是一样的

2、封装函数，这样就不需要每次都写`path.resolve()`

![[00 assets/f69f9eee740643ea523ed45f5490c6c1_MD5.png]]

3、但是配置了别名，也只是在打包的时候会修改。但是我们编写的时候是不会有提示的，我们就需要添加`js.config.json`文件来为我们写代码的时候服务

![[00 assets/9e637d914338150285d54996ffa6e6e0_MD5.png]]

> 配置样式

1、这里使用`craco-less`，但是目前直接安装会出现问题，所以使用`npm i craco-less@2.1.0-alpha.0`

2、随后安装`less`，`npm install less-loader less --save`

![[00 assets/4776c8fa584dbc2f91b11b5798c3c463_MD5.png]]

### 6.2.4 样式重置

![[00 assets/17da32926c1665f6467eb7e0d80cd500_MD5.png]]

1、安装`npm i normalize.css`

![[00 assets/3a4270d02d2400e085569ec930c8d8ee_MD5.png]]

2、自己编写`reset.css`

![[00 assets/f59cdbcfb74ae06aece8f5efbd363782_MD5.png]]

### 6.2.5 全家桶配置

#### 6.2.5.1 Router

1、安装`router`，`npm i react-router-dom`

2、对于路由的配置存在 2 种方式来编写。第一种就是在`jsx`中处理，但是这样编写会导致管理复杂。第二种就是单独搞一个文件来存放，这里选择第二种方式

3、编写路由懒加载`React.lazy()`

4、因为一开始进入到页面中，并不是`/home`页面，所以要设置重定向`Navigate`

5、还存在`NotFound`页面，只要路由不匹配就需要跳转到`NotFound页面`

![[00 assets/5800a9f86bf514acd421e11915f77dc3_MD5.png]]

6、因为我们使用了路由懒加载，可能存在还在等待加载的情况，这个时候就需要一个等待页`Suspense`

7、并且编写路由要嵌套高阶组件`BrowserRouter`

![[00 assets/fc66ef147f1215e52e6de84cea522d35_MD5.jpeg]]

8、最后在页面中使用`useRoutes`函数就可以遍历其中编写的路由映射，并且应用其中

![[00 assets/2d8b8265098574289c016ca5e5c89f19_MD5.png]]

#### 6.2.5.2 Redux

1、安装`Redux`这里使用`RTK`的解决方案，`npm install @reduxjs/toolkit react-redux`
2、安装之后使用`configureStore`来创建`store`
![[00 assets/ad0c4ab6751629730302789a0e205b09_MD5.png]]

3、我们创建一个`createSlice`，并且传入对应的参数
4、因为我们需要`dispatch`，所以还需要手动导入函数，并且导出函数
5、最后导出的就是`countSlice`的`reducer`
![[00 assets/3c4827fe775beff4327eb60d56e1ced4_MD5.png]]

6、使用`Provider`来为组件引入`store`
![[00 assets/a1f8ed6db12c745a068f024c7c9d7b9f_MD5.png]]

7、因为这里使用的是`Hook`的写法，所以这里也修改为`Redux Hook`
![[00 assets/b0ab7b66e4a05b1509250d81b7577e8c_MD5.png]]

> 原始配置

1、因为很多老项目都是使用的`react-redux`而非`rtk`，所以这里也创建一个原始`redux`的配置方式
![[00 assets/ca628c9d752d085b4e9b36a12c45839a_MD5.png]]

2、依旧使用`rtk`来管理数据
![[00 assets/8ee53e73591b7eaa21cf68b3eef6623f_MD5.png]]

3、在`redux`的插件中也可以看到响应的数据
![[00 assets/eb8203ada9f725891b88dcc3670129bd_MD5.png]]

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
![[00 assets/786996987c3c94d0f7509b525f2f86db_MD5.png]]

## 6.3 Header 头部

### 6.3.1 基础搭建 - 结构搭建

![[00 assets/5f155a19825cd4f5cff2f4b674bd1ac2_MD5.png]]

1、因为要做到中间的搜索栏的居中，这就需要将 2 边的宽度设置为`flex:1`

![[00 assets/6b0e5d47919fd8abbcbf5036e4bbec5b_MD5.png]]

2、并且头部`header`存在很多的状态控制，这里有 2 个方式来搭建`header`。这里使用第二种方式来制作

 方式一：每个页面中设置一个单独的`header`

 方式二：集中设置一个`header`，并且做好状态管理

3、并且对于`header`还存在 3 个部分，这 3 个部分也可以抽取为组件，也就是下面的框架

![[00 assets/a1fad5973e2643d3897ab2d411f5fc85_MD5.png]]

4、对于样式，这里采用的是`styled-components`，`npm i styled-components`

5、我在这里编写的时候出现`vscode-styled-components`的语法提示问题，这里可以尝试将插件降级来解决

![[00 assets/b545aa9c540d04b05fc1123e4103654c_MD5.png]]

引入`HeaderWrapper`，对编写的样式进行包裹

![[00 assets/03801f8616ce61091b78779b64e8a084_MD5.png]]

### 6.3.2 Logo 搭建 - SVG 使用

1、对于`svg`的使用也存在 3 种方式

 方式一：将`svg`作为图片来处理，但是这种方式会导致网络请求没加载的时候出现空白

 方式二：将`svg`直接写在页面中，这种方式会导致页面中代码很多，所以也排除

 方式三：将`svg`作为组件来使用，这样可以解决上面的问题

2、按照这种方式来创建一个组件，并且只返回`svg`元素

3、因为对于`jsx`来说`style={ }`中的内容要是一个对象，所以编写一个`styleStrToObject`的函数来转化

![[00 assets/ad99213290eb23f002c36aef2dcd1bf6_MD5.png]]

该函数就是将`str`传入，之后转化为`object`的形式输出

![[00 assets/39d6ada745c1168011b7d29659cf74bb_MD5.png]]

4、最后导出，在组件中使用即可

![[00 assets/5fee36e72a8ce2cab620a38b1364f87c_MD5.png]]

### 6.3.3 主题配置 - 主题文件

1、对于主题配置也存在 2 种方式，这里使用方式二来配置

 方式一：使用`CSS`变量来配置

 方式二：使用`styled-components`的`theme`功能来配置

2、我们在全局编写`theme`文件

![[00 assets/472ea94c7f0b4d8be50435364c01695c_MD5.png]]

3、我们需要全局使用这个`theme`的话，就需要引入`styled-components`中的`ThemeProvider`组件

![[00 assets/5a6c910ecdf3abaa843264ea045f0e3d_MD5.png]]

4、使用的话就使用`${ }`中函数返回值的形式来显示

![[00 assets/22cb3f1c395eb134108b15e3934ab61e_MD5.png]]

### 6.3.4 菜单搭建 - flex 值/样式抽取

![[00 assets/e494b9405ab660d001a86645b87fc6f5_MD5.png]]

1、先对整体的结构进行搭建，使用`svg`依旧参考之前的笔记

![[00 assets/c5aa2f5f1d8692939aa22b45a57fde46_MD5.png]]

2、在编写的时候发现，`justify-content`存在`space-evenly`属性，该值和`space-around`存在什么区别？

![[00 assets/c62887a72c0cd054865224cefa8f17c9_MD5.png]]

这张图是`space-evenly`，可以发现它们之间的距离是一样的，也就是关注元素和元素的距离

![[00 assets/88720dacb0a4d6868ec8a61519ef204f_MD5.png]]

使用`space-around`就只关注该元素周边的距离

![[00 assets/5bfc850777e015d368012ab11ef43dc9_MD5.png]]

4、因为我们手指放在上面存在一个阴影的动画，但是可以发现存在很多这样的动画，都是一样的，所以我们可以将该动画进行抽取

![[00 assets/ffc9a5f8c69d55de86b856566cef4c6b_MD5.png]]

我们将该动画抽取到`theme`的`index.js`中

![[00 assets/82c0c1cc1abd60edce19018e1bda017a_MD5.png]]

5、依旧使用这种方式就可以引入该动画

![[00 assets/f69ea160b154a56e09257bb4d0008d77_MD5.png]]

### 6.3.5 搜索栏搭建

![[00 assets/26cd37ef8f805f35acf7ad5fbba93f2e_MD5.png]]

1、参考结构搭建`HTML`和`CSS`即可

![[00 assets/5c1ef0653c4d25c24113e5dcdc9e8c21_MD5.png]]

![[00 assets/aa40f621f180c7a61d569ab7d600afe5_MD5.png]]

## 6.4 Home 页面

### 6.4.1 \*轮播图 - 资源引入

1、下面是轮播图的搭建结构

![[00 assets/30f0e44d1f50e94a6ce5d5bdbeaeb515_MD5.png]]

2、首先要理解一个点，`React`和`Vue`只要跑在`webpack`环境下面，就是不能直接引入图片资源，而是需要将该图片按照模块的形式来引入

3、为什么在`Vue`中可以直接引入呢？这是因为`Vue`在解析`template`模板的时候就已经在底层做好了处理，所以不需要我们手动操作

4、但是在`React`中是没有做这些处理的，而是需要自己来做

5、我们可以按照下面的 2 种方式来引入资源，我一般选择使用`require()`来引入资源

![[00 assets/894a0dd0a40324e894c5c8bf2de33d25_MD5.png]]

6、这个就是`sass`的语法，也就是`div > .content`的语法

![[00 assets/67f9c47632a27b544a670d6f1dec4b33_MD5.png]]

### 6.2.2 \*高性价比数据获取 - 网络请求/Redux 数据管理

![[00 assets/df8d977101428cf37d9a7254f368e207_MD5.jpeg]]

1、我们需要请求到数据，并且丢给`redux`来管理数据

2、首先来对网络请求进行归纳管理

![[00 assets/20263ffc326b25ebbda24f2f42fb828a_MD5.png]]

3、使用`createAsyncThunk`来创建异步函数，用于网络请求

4、在`extraReducers`监听网络请求，并且将数据交给`state`中管理，这里笔记参考`Redux`的内容

![[00 assets/8b0f24093cb36190912e0aa88113da94_MD5.png]]

5、导出该网络请求的`action`，使用`Redux Hook`来对`Redux`进行操作

6、`dispatch`用于事件发送，`useSelector`用于数据的监听

![[00 assets/0f4c9cbf2d5573216772aec6a3d80f3a_MD5.png]]

7、获取数据进行展示

![[00 assets/246a8af1133e9489dddb5dcf5f0e6224_MD5.png]]

### 6.2.3 \*AreaHeader 组件搭建 - props 参数传递

1、下面是组件结构得搭建

![[00 assets/56becb42ef0aa0d2c932516a87abdb33_MD5.png]]

![[00 assets/95a62a9df479c9bc431b919e201a1091_MD5.png]]

2、我们给组件传入参数，使用`propTypes`作为参数校验

3、函数中使用`props`来获取传入得参数

![[00 assets/4b480f75fd406fb6ed8bad96284a3a55_MD5.jpeg]]

### 6.2.4 \*RoomItem 组件搭建 - 样式搭建

1、我们参考下面得结构

![[00 assets/68976f784b93618c05c1b9451e3c682a_MD5.png]]

2、因为图片存在长短不一得情况，所以我们按照下面得方式来搭建组件。但是具体为什么这样可以实现，我就不是很了解了

![[00 assets/e8052ae140d645392912700a4bf987f5_MD5.png]]

![[00 assets/0ab3274a56310c1e96edd03727dafd51_MD5.png]]

### 6.2.5 \*组件引入 - antDesign/MUI

> 引入 antDesign

1、安装`npm i antd`，随后就是正常的组件引入流程

![[00 assets/bbbba18ab41cb74ea0931d120e0ddf75_MD5.png]]

2、但是我们想要配置`antdesign`的主题颜色的话，目前官网提供的方式是使用`Provider`

![[00 assets/290ccf23627492aad70bae6ac8a5721c_MD5.png]]

3、但是老师讲的是通过`webpack`中引入`less`来修改主题颜色

![[00 assets/4a50b23bf36772ea54d28122136bc3cd_MD5.png]]

然后再去引入`less`文件

![[00 assets/a966c01be2984ad6e8e6328c435a991f_MD5.png]]

> 引入 MUI

1、安装`npm install @mui/material @mui/styled-engine-sc styled-components`。但是目前使用`styled-engine`存在很多问题，这里还是`emtion`

2、`npm install @mui/material @emotion/react @emotion/styled`

3、然后引入使用即可

![[00 assets/bab0e2441722d3a0954b81b1bad8e5ca_MD5.png]]

4、引入完组件之后，直接搭建评分样式即可

![[00 assets/df637f5a516f3d2670f7a2cbc1072032_MD5.png]]

![[00 assets/5738d9ee8b1e21deed9f4dafc90fafff_MD5.jpeg]]

### 6.2.6 \*AreaRoom 组件搭建 - 结构组件抽取

![[00 assets/2a3aac9fd8ef8f421f9dad2752d19543_MD5.png]]

1、这是一种组件的思想，不仅仅只是抽取单一功能，还可以抽取结构作为一个组件

![[00 assets/a263a140e99b223b01fb6b271f348d19_MD5.jpeg]]

![[00 assets/47115c2b22fb42cdef7e1ee318695479_MD5.png]]

### 6.2.7 高评分数据 - 网络请求优化

1、我们将网络请求都封装到`redux`中的`createAsyncThunk`，但是按照我们之前的写法就会存在一些问题。如果按照`async/await`的语法糖来写的话，会导致网络请求速度很慢

2、所以对于这种多个请求一起发送的情况，我们使用下面的方式来处理

3、对于`createAsyncThunk`中的回调函数存在第二个参数`store`，`store`存在`dispatch()`和`getState()`函数，我们派发`action`来达成数据的更新，也就是放弃`extraReducers`

![[00 assets/6003c34e12c424ad3d02ecf84238063c_MD5.png]]

4、将`store`中的`action`导出给`createAsyncThunk`

![[00 assets/7a0a95630e67e9d441073acf203b46ab_MD5.png]]

### 6.2.8 RoomItem 组件宽度控制

1、通过`props`传输数据给`组件`

![[00 assets/41d42eb55352b17a66b4a0a71f3c824f_MD5.png]]

### 6.2.9 \*SectionV2 组件封装

1、因为基本的逻辑已经和上面的差不多，直接参考代码即可。但是还是存在一些比较难理解的点

2、这里就是比之前多封装一个`area-tabs`组件

![[00 assets/ed85ed0dc9e75d1f5ad47ab7e90d93a2_MD5.png]]

> area-tabs 封装

1、这里包含了`classNames`库的函数

![[00 assets/d10a3daf01aa1497728ea98cbcb6dcab_MD5.png]]

2、还包含了子组件给父组件使用事件传递参数

![[00 assets/3d47d1a4240060948278e4159de48a49_MD5.png]]

> 网络请求到才渲染界面

1、因为这里存在初始化值得处理方式，在一开始渲染界面得时候`useState`传递得参数是`""`

![[00 assets/d9e760c866e4eb039e7ae566378cfd2b_MD5.png]]

2、如果我们想要做到网络请求到数据之后才会渲染界面得话，可以使用下面得方式

![[00 assets/9ce903807de9118b46ae026a074da2db_MD5.jpeg]]

3、将监测对象是否有数据封装为一个函数来判断

![[00 assets/f63546032d7702c7e9a177999f94af90_MD5.png]]

> areafooter 组件封装

![[00 assets/8707dfd7bc38e651e7ee03d5639c3458_MD5.png]]

### 6.2.10 \*ScrollView 组件封装

这里没怎么看懂，可以直接看代码

## 6.5 Entire 页面

### 6.5.1 过滤器功能

1、这里界面就不记录了，主要是选中和取消选中

2、这里主要还是用到了数组的内置的高阶函数，其逻辑主要是判断依据存入的`selectFilter`中是否包含了已经选中的部分，如果选中的话就删除，没选中就添加

3、`findIndex`传入高阶函数，如果函数返回值为`true`的话就返回该索引，为`false`的话就跳过

4、`splice`表示要删除的数据，第一个参数为开始索引，第二个参数表示要删除的数据

5、`slice`表示截取的数组的数据

![[00 assets/8590dc3101d5b0934e07c9e336b55e04_MD5.png]]

### 6.5.2 房间列表数据 - 非 RTK 中 Redux 的使用

> 基本结构

1、在实际的开发中大部分还是非`RTK`的选择

2、其中目录结构依旧和之前一样，这里参考我之前`Redux`的笔记

![[00 assets/4d228e76a8f82b0cd1154b4518c79b87_MD5.png]]

3、因为之前使用的`rtk`来管理这些`reducer`，但是因为`rtk`本质就是基于之前的`redux`的高阶封装，所以我们原生编写也可以直接使用，并且内部还集成了`react-thunk`，不需要我们手动安装

![[00 assets/32c9fe11b6b3ac6e9feda961fee0eaaa_MD5.png]]

4、后续的时候和之前是一样的，使用`redux Hook`

![[00 assets/93c95548d394ce110163c3feb0239e45_MD5.png]]

> 网络请求

1、因为我之前记得的笔记是`class`组件，但是这里使用的函数式组件，所以存在一定的区别

2、这里的本质就是执行`fetchRoomListAction`函数，然后返回函数`(dispatch,getState) => { }`并且内部调用，这里没处理`redux-thunk`是因为`rtk`内部就集成进去了，所以不需要处理

![[00 assets/fda6d9e397d77eb76689a97bf86ec7f6_MD5.png]]

### 6.5.3 分页器 - 修改 UI 组件库的样式

1、使用开发者工具调试，修改内部样式即可

![[00 assets/e1b87fcb264a2f2c86d9c8260aea3e5f_MD5.png]]

### 6.5.4 RoomItem 补充 - 图片轮播/指示器封装/依情况展示组件数据

实现点击左右箭头轮播显示，并且下面指示器提示

![[00 assets/8f910e1e672fabc9a86da656038a7b21_MD5.png]]

> 轮播效果

1、最终的结构分为这 3 部，其中轮播图部分使用`ant-design`封装好的组件

![[00 assets/c36b4d631d6a1b265d18d4b7e301967c_MD5.png]]

2、最终实现的逻辑部分

![[00 assets/a5a20a786d20b14f760eaa592aab139b_MD5.png]]

> 指示器

1、这一段涉及到了`DOM`距离的计算，这和`scrollView`组件的封装是差不多的思想，我这里不是很懂，就不去记录了

2、中间部分为核心变化的代码，且该组件使用插槽的形式扩展

![[00 assets/6c4b609834d4315b4007a6105c002cc7_MD5.png]]

3、这里包含一个数组临界的算法

4、设置`selectIndex`的值，并且作为`props`传递出去

![[00 assets/26b0995357e03105253f880f0cb7cfd5_MD5.png]]

> 依情况展示组件

1、因为`RoomItem`还存在`/home`页中无组件的显示模式，如果再去封装一个组件就很浪费

2、所以这里将`jsx`的组件拆为一个变量，这和之前的类组件是一样的

![[00 assets/761f44b8cb9d14f0612cd5a78e9ee598_MD5.png]]

### 6.5.5 跳转到详情 - 事件传递

1、封装为一个组件，所以最好不要将单一特殊事件给组件来调，而是抛出来给父组件来处理

![[00 assets/b91b9f4312c4bb5cdd1efbcda90da95b_MD5.jpeg]]

### 6.5.6 详情页图片开发 - 页面跳转数据传递/Redux 数据持久化处理/样式排他思想

> 页面跳转数据传递

1、对于页面跳转需要数据传递，但是使用路由中的`param`和`query`来传递这么多参数，很显然不现实

2、所以最好的方式就是使用`redux`来保存该数据，之后就可以在另外一个页面中使用

![[00 assets/cc39cdf60741f6ba0e8ba45af04b8e83_MD5.png]]

> redux 持久化存储

1、因为存在`redux`中的数据在刷新之后就会小时，所以这里我使用`session`存储的方式来持久化`redux`中的数据

2、所以我们需要封装一个可以存储的工具，这里的思路参考了`Vue`后台管理中封装的`utils`

![[00 assets/c153660378fef988b816a120a27ba5d5_MD5.png]]

3、每次进入页面请求`actions`的时候就保存该数据，并且初始化的时候就使用保存在`session`的数据

![[00 assets/6ded7cb316c466d81dc4e86cde059f7b_MD5.png]]

> 样式排他思想

我们鼠标放置在上面的时候只有该元素显示，其他元素都显示遮盖层

![[00 assets/252e5afd2e21d46121528ce5686dc246_MD5.png]]

1、下面为`HTML结构`

![[00 assets/76f7a8d29623a2ae22801a40f1d504e9_MD5.png]]

2、这一段就是排他思想的核心代码

3、只要`pictures`处于`hover`状态的时候，就将`cover`设置为显示，并且这时候只要`item`为`hover`状态的话就让`cover`消失。

4、这里使用到的原理是`CSS`层叠样式，后面的`item`为`hover`状态的时候覆盖上面的`opacity`的状态，就达成了这种效果

![[00 assets/100664dfef3e70ac6c257c8c777d8dbc_MD5.png]]

## 6.6 图片浏览

### 6.6.1 图片展示

![[00 assets/6f9acb2fa8986a1e8998fca5a2c49c93_MD5.png]]

1、因为该图片浏览器在各个地方都可以使用，所以将该组件封装到`base-ui`中

![[00 assets/1c3ff4ad840b45debf5a7bdb76f3adf1_MD5.png]]

### 6.6.2 关闭功能 - 使用 JS 设置样式

1、这里组件展示的原理就是在背后设置一个遮盖层

![[00 assets/89ec0d6223da7fa7a8048290bd1b2cb3_MD5.jpeg]]

2、我们点击了上部组件之后就关闭也组件，并且打开的时候不能滑动

3、这里采用设置`overflow`的值来解决

![[00 assets/3be017f12cb49ef29eb0ddebb1bd0ada_MD5.png]]

### 6.6.3 图片切换 - React 动画

1、这个是图片切换的 HTML 结构

![[00 assets/1495b9a080a89dccc8e446e8e3d746ab_MD5.png]]

2、这里比较难的点就是存在多个元素的动画，并且是一个元素进入，一个元素出去。最好的方式就是使用`Switch`和`CSS`组合使用

![[00 assets/b92e336f14a61a131a7e60179c317cea_MD5.png]]

### 6.6.4 图片列表浏览 - Indicator 组件使用

![[00 assets/5ad8017f74a6b33309cf6429b9c9ca8b_MD5.png]]

1、下面是 HTML 结构

![[00 assets/fbc51388afa9a03ee4cb245a7d55e9d5_MD5.png]]

2、这里主要的`Indicator`组件的使用

![[00 assets/9b60ed94057c067ea88c41adff80abd6_MD5.png]]

### 6.6.5 页面滚动到顶部 - Hook 使用

1、我们每次进入到新的页面都需要页面滚动到顶部，这里就可以尝试封装一个`Hook`来简化代码

![[00 assets/01a9f3ee017a80c9ca9ad7cc10a0f91f_MD5.png]]

## 6.7 Header 开发

### 6.7.1 页面搭建

这里的头部需要变化，且存在`fixed`定位的可能

![[00 assets/032c155c03051be934034d818d4ceefc_MD5.png]]

![[00 assets/1ab46d39f85994eb023cedf5e52ce50f_MD5.png]]

1、下面是`HTML`结构

![[00 assets/518d43a145e92778e36275cc0550566b_MD5.png]]

### 6.7.2 fixed 控制 - 配置信息使用 Redux 控制/Susponse 和 Redux 冲突问题

1、因为有写页面需要控制头部是否一直吸附在顶部，所以需要一个变量来控制，最好的方式就是我们传入配置就可以实现功能

2、我这里使用`Redux`来动态控制

![[00 assets/6e427977b8da64c314a91f77d4633481_MD5.jpeg]]

3、落实到每个页面中，就是进入时就发送`action`来控制初始值

![[00 assets/ea8cb444929d47c742f056a1c4307a59_MD5.png]]

> Susponse 和 Redux 冲突问题

1、我们目前采用这种方式是可以监听到的，并且`action`也是可以发出，且逻辑没有任何问题

![[00 assets/58d5af4c2190385eba85656b21f8c125_MD5.png]]

2、但是我们使用了路由懒加载的技术，可能存在`Redux`已经准备好了，但是页面还没请求到的情况，所以这个时候可能`Redux`中的值依旧是原来的值

3、为了解决这个问题，最好的方式就是将`Suspense`组件放置在`Provider`里面

![[00 assets/454e78a3c0f0b3ca0cd352910aeada77_MD5.png]]

### 6.7.3 头部动画效果 - React 动画效果

1、因为是 2 个部分，并且动画都不一样，所以这里采用的是 2 个动画同时加载

![[00 assets/98303549110d0a3d2099308e04c3179d_MD5.png]]

2、动画效果的`CSS`

![[00 assets/62d47b12ac611356c337b689c4aace93_MD5.png]]

### 6.7.4 页面滚动搜索关闭 - 滚动监听/Hook 使用

1、这是封装的滚动监听的`Hook`

![[00 assets/84db8b346108b770ae29c9e9f752f299_MD5.png]]

使用`Hook`并且滚动监听

![[00 assets/61f8d7fe12785982b20f5ed15ddd1e57_MD5.png]]

2、因为只要滚动就开始监听，所以这里需要记录一下之前的值，因为记录并不需要刷新页面，这里就采用`useRef`的方式来保存数据

3、下面是滚动搜索结果消失的核心代码

![[00 assets/f266f4593ec59ff5568565af90c380ef_MD5.png]]

### 6.7.5 顶部搜索栏透明 - 使用注意传递参数

1、我们滚动到顶部之后页面中的元素样式都需要修改

![[00 assets/4af8eb2786eef37b99f6cc24f1728eb4_MD5.png]]

但是监听`isAlpha`的值只在`app-header`中存在

![[00 assets/33a7f85931665a7750d63c117ca1ce7f_MD5.png]]

2、我们需要将该值传输给下面的多级组件的`styled-components`中，很显然单纯使用`props`和`event`已经不能处理了，但是使用`Redux`又没有必要

3、这里使用`styled-componets`的`ThemeProvider`来传递参数，这样就可以在每个组件的`Wrapper`中都可以使用到了

![[00 assets/b8e59bec888c681a03bd0173e4bd10cb_MD5.png]]

![[00 assets/444aa611e4da3ac7310c5d4533d11f5f_MD5.png]]

## 6.8 开发部署

参考`Vue`笔记

# 7. 项目 - 网易云

## 7.1 项目搭建

### 7.1.1 基本搭建

1、可能我们使用`create-react-app`会出现错误，所以需要使用`npm i create-react-app -g`来安装命令

2、我们使用`create-raect-app xxx --template typescript`来创建项目

![[00 assets/06e06a6b9fd586b2506c1e388d560422_MD5.png]]

3、我们按照之前的配置创建了`craco`，还需要手动来配置`teconfig.json`文件才不会导致报错

![[00 assets/60b1f2b6646437044c247be6f930b6dc_MD5.png]]

### 7.1.2 代码规范

1、按照我之前的`Vue`笔记配置即可，但是老师对于`eslint`的配置存在一些其他的操作

2、我们安装下面的插件`npm i eslint -D`，然后输入`npx eslint --init`来初始化`eslint`的配置

![[00 assets/4d462d9c1892f048df62056dac329bf5_MD5.png]]

这是我选择好的`eslint`的配置，这里根据情况来选择

![[00 assets/e4df8daa048dcfc94c622c7117b33423_MD5.png]]

3、下面就是配置的结果

![[00 assets/d43b14ea5e4ddc5dab60e33fb571a345_MD5.png]]

![[00 assets/7480e71cb434f94e5e78dd12bfa6fe1a_MD5.png]]

![[00 assets/b0d2e753264ca1d6954640db302e4e22_MD5.png]]

![[00 assets/94cebfbf954d34283b9276d0e453976d_MD5.png]]

下面是我这里配置安装的包

![[00 assets/5223397f4b31a2d2709a3be0d11f3599_MD5.png]]

### 7.1.3 目录搭建

![[00 assets/423090fd8d975eb2040dd783bf55b6a7_MD5.png]]

### 7.1.4 路由配置

1、参考之前的笔记来配置即可，但是因为目前使用的是`typescript`来搭建的项目，所以可能部分存在差异
2、首先就是创建文件，之前创建`.js`文件的时候也可以使用`jsx`的语法，但是对于`ts`来说就不行了，所以需要编写`.tsx`的文件
3、然后就是类型导入，对于`react-router-dom`来说，我们编写`routes`最好不要写成`any[]`类型。最好的方式就是导入类型`RouteObject`，它内部提供了对于的类型
![[00 assets/50085bd5d8c25f4729e1fe1a2fdeb9cf_MD5.png]]

4、依旧使用之前的方式来做路由映射
![[00 assets/be6e3a963e8cb22441fb039a948036d4_MD5.png]]
对应的`index.tsx`的配置也是使用下面的方式来处理
![[00 assets/75f30f1d1553ba3aa66ce8810557271a_MD5.png]]

5、且需要注意一个点，对于`React`即便你没有使用导入的`React`，也需要导入，不然就会报错
![[00 assets/ccffd3d49d13b0d4fc2b12db8a002875_MD5.png]]

6、最终我们配置了二级路由，这里和Vue基本一致，不再赘述了，而且针对每个页面都可以配置路由懒加载
7、针对二级路由的话，需要配置 `Suspense` 组件来作为临时的显示，不然整个二级路由都会跳转
8、二级路由中的显示可以使用 `Outline` 来作为占位使用
![[00 assets/645f067d17437408d7b45e0cd59e6d6f_MD5.jpeg]]

### 7.1.5 props 约束

1、针对 React 比较推荐使用下面的方式来编写 `React.FC<Props>`，这样不仅针对函数式组件`Discover`进行语法提示，还可以直接泛型表示参数参数类型，并且伴有语法提示
2、针对现在的语法，我们可以直接传入 `<span>` 作为插槽，但是他没有语法报错？这是因为React底层针对这里的泛型Props做了交叉类型Children，这样就不存在语法错误了
![[00 assets/3c04654041c2ad0eb4d457526c6e8b4a_MD5.jpeg]]

### 7.1.6 Redux配置

1、`npm i @reduxjs/toolkit react-redux`，按照如下图中的方式就可以创建
![[00 assets/9b601ee714903e63027f8d37004ee3b2_MD5.jpeg]]

2、但是在完成如上的编写之后，在使用的时候是没有类型推导的，需要额外编写类型推导的函数
![[00 assets/639ec2d0cf42f86676eece6348b2b8f0_MD5.jpeg]]
这里针对`useSelector`本质是下面这段工具类型来做推导的
![[00 assets/a0567fc11a81cc502ad2a33192ad54d3_MD5.jpeg]]

3、如下图就是完整的使用方式
![[00 assets/d98854712e7cdaa669cae0ea1ad71815_MD5.jpeg]]