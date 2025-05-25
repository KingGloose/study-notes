参考视频：[尚硅谷 Web 前端 Promise 教程从入门到精通\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1GA411x7z1?p=2&spm_id_from=pageDriver)

# 1 初始 Promise

## 1.1 Promise 简介

Promise 是一门新的技术(ES6 规范)，并且是 JS 中`进行异步编程`的新解决方案(旧方案是单纯使用回调函数) ^15cb91

从**语法**上来说: Promise 是一个`构造函数`，从功能上来说: promise 对象用来封装一个异步操作并可以获取其成功/ 失败的结果值

## 1.2 使用 Promise 理由

### 1.2.1 指定回调函数的方式更加灵活

**旧的**: 必须在启动异步任务前指定

**现在**: 启动异步任务 => 返回 promie 对象 => 给 promise 对象绑定回调函数(甚至可以在异步任务结束后指定/多个)

### 1.2.2 支持链式调用, 可以解决回调地狱问题

**1.什么是回调地狱**

回调函数嵌套调用, 外部回调函数异步执行的结果是嵌套的回调执行的条件

![[00 assets/0c50da5c3ff8e4951a6f5987731ac5c1_MD5.png]]

**2.回调地狱的缺点**

不便于阅读 不便于异常处理

**3.解决方案**

promise `链式调用`，用来解决回调地狱问题，但是`只是简单的改变格式`，并没有彻底解决上面的问题真正要解决上述问题，一定要利用 promise 再加上 await 和 async 关键字实现异步传同步(**promise +async/await**)

### 1.2.3 减少沟通的成本

比如下面的`sendRequest()方法`，对于一些库可能存在不同的调用方式，可能会有很大的学习成本。所以就会存在`Promise`，其中`Promise`就翻译为`承诺`，就是指定一个统一的规范，以后按照`Promise`调用即可。

![[00 assets/12ef4215a5621fb12f14ec1ee2d56dfe_MD5.png]]

## 1.3 初识 Promise

```html
//普通写法
<body>
 <button class="BtnReward">点击我抽奖</button>
 <script>
   function GetRandom(n, m) {
     return Math.ceil(Math.random() * (n - m + 1)) + m - 1;
   }
   const btn = document.querySelector(".BtnReward");
   btn.addEventListener("click", function () {
     setTimeout(() => {
       let r = GetRandom(1, 100);
       if (r <= 30) {
         alert("恭喜你中奖了");
       } else {
         alert("再接再厉");
       }
     }, 1000);
   });
 </script>
</body>


//Promise写法
<button class="BtnReward">点击我抽奖</button>
<script>
  function GetRandom(n, m) {
    return Math.ceil(Math.random() * (n - m + 1)) + m - 1;
  }
  const btn = document.querySelector(".BtnReward");
  btn.addEventListener("click", function () {
    const p = new Promise((res, rej) => {
      setTimeout(() => {
        let r = GetRandom(1, 100);
        if (r <= 30) {
          res(r);
        } else {
          rej(r);
        }
      }, 1000);
    });
    p.then(
      (value) => {
        alert("恭喜你中奖了，你的号码为" + value);
      },
      (reason) => {
        alert("可惜了你没中奖，你的号码为" + reason);
      }
    );
  });
</script>
```

## 1.4 Promise 实践练习

### 1.4.1 fs 文件读取

```javascript
//普通写法
const fs = require("fs");
fs.readFile("./1.txt", (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});


//Primise写法
const fs = require("fs");
const p = new Promise((res, rej) => {
  fs.readFile("./1.txt", (err, data) => {
    if (err) rej(err);
    res(data);
  });
});
p.then(
  (value) => {
    console.log(value.toString());
  },
  (reason) => {
    console.log(reason);
  }
);


//Primise封装为函数写法
const fs = require("fs");
function mineReadFile(path) {
  return new Promise((res, rej) => {
    fs.readFile(path, (err, data) => {
      if (err) rej(err);
      res(data);
    });
  }).then(
    (value) => {
      console.log(value.toString());
    },
    (reason) => {
      console.log(reason);
    }
  );
}
mineReadFile("./1.txt");


//util.promisify进行Promise化
//使用node.js里面的util.promisify将方法转换为Promise，这样就不用每次都自己手动封装
const util = require("util");
const fs = require("fs");

let mineReadFile = util.promisify(fs.readFile);
mineReadFile("./1.txt").then(
  (value) => {
    console.log(value.toString());
  },
  (reason) => {
    console.log(reason);
  }
);
```

### 1.4.2 AJAX 请求

```html
<button class="BtnGetAJAX">点击AJAX</button>
<script>
  var btn = document.querySelector(".BtnGetAJAX");
  btn.addEventListener("click", () => {
    // 普通写法
    const xhr = new XMLHttpRequest();
    xhr.open(
      "GET",
      "http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList"
    );
    xhr.send();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status >= 200 && xhr.status < 300) {
          console.log(xhr.response);
        } else {
          console.log(xhr.status);
        }
      }
    };

    //Promise写法
    const p = new Promise((res, rej) => {
      const xhr = new XMLHttpRequest();
      xhr.open(
        "GET",
        "http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList"
      );
      xhr.send();
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status >= 200 && xhr.status < 300) {
            res(xhr.response);
          } else {
            rej(xhr.status);
          }
        }
      };
    });
    p.then(
      (value) => {
        console.log(value);
      },
      (reason) => {
        console.log(reason);
      }
    );
  });
</script>


//将Promise封装为函数写法
<body>
  <script>
    function GetAjax(url) {
      return new Promise((res, rej) => {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.send();
        xhr.onreadystatechange = function () {
          if (xhr.readyState === 4) {
            if (xhr.status >= 200 && xhr.status < 300) {
              res(xhr.response);
            } else {
              rej(xhr.status);
            }
          }
        };
      }).then(
        (value) => {
          console.log(value);
        },
        (reason) => {
          console.log(reason);
        }
      );
    }
    GetAjax("http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList");
  </script>
</body>
```

## 1.5 Promise 的值

下面就是 Promise 对象上面的三个值

![[00 assets/aff2b6d3899794392ce691856e8e66ea_MD5.png]]

### 1.5.1 PromiseState

**pending** 未决定的，**resolved / fullfilled** 成功，**rejected** 失败

**pending** 可以变为 **resolved**和**rejected**，并且状态只能改变一次

### 1.5.2 PromiseResult

```javascript
new Promise((res,rej)=>{
	res(data) //也就是这里传递的data
	rej(data)
})
```

### 1.5.3 Promise 参数

1、传入普通的参数，就是按照正常的处理方式

2、传入另外一个`Promise`，那么该`Promise`的控制就不会被移交给传入的`Promise`

![[00 assets/954b356b0afa844deb3baa755e81c0ec_MD5.png]]

3、传入的对象中包含`then方法`，那么就会执行`对象`中的方法

![[00 assets/f96def5aef716bae0f322aeef726af06_MD5.png]]

## 1.6 Promise 工作流程

![[00 assets/30c5dc05a1e9d621de3f55792dc4262d_MD5.png]]

# 2 Promise 的 API

## 2.1. Promise 构造函数

(1) executor 函数：执行器(resolve,reject) => {}

(2) resolve 函数：内部定义成功时我们调用的函数 value => {}

(3) reject 函数：内部定义失败时我们调用的函数 reason => {}

```javascript
new Promise((res,rej)=>{
	if(result) rej(data) //成功调用rej
	elsr res(data) 	//失败调用res
})
```

且 Promise 里面的执行器是同步调用的

```javascript
new Promise((res,rej)=>{
	console.log("aaaa")
})
console.log("bbbb")
```

![[00 assets/18dd21b82fba91437d7cf060c4857dad_MD5.png]]

## 2.2 Promise.prototype.then()

(1) onResolved 函数：成功的回调函数(value)=>{}

(2) onRejected 函数：失败的回调函数(reason)=>{}

说明：指定用于得到成功 value 的成功回调和用于得到失败 reason 的失败回调返回一个新的 promise 对象

```javascript
const p = new Promise((res, rej) => {
  res();
  rej();
});
function onResolved(value) {
  console.log("这是成功的回调");
}
function onRejected(reason) {
  console.log("这是失败的回调");
}
p.then(onResolved, onRejected);


//但是我们平常简写
const p = new Promise((res, rej) => {
  res();
  rej();
}).then(
  (value) => {
    console.log("这是成功的回调");
  },
  (reason) => {
    console.log("这是失败的回调");
  }
);
```

说明：这里就观察到一个特点，就是 Promise 只能修改一次状态，这个在上面就说过，我们同时调用了`res`和`rej`但是最后的状态就是`res`

## 2.3.Promise.prototype.catch()

(1) onRejected 函数：失败的回调函数(reason)=>{}

说明：只有失败的回调

```javascript
const p = new Promise((res, rej) => {
  rej();
}).catch(
  (reason) => {
    console.log("这是失败的回调");
  }
);
```

## 2.4 Promise.resolve()

(1) 你传入非 Promise 对象，结果为 fulfilled 表示成功。并且 PromiseResult 的结果就是你传入的数据

(2) 你传入的是 Promise 对象，结果就根据 Promise 参数的处理结果来，假如参数是 rejected，那么外部 Promise 的结果就是 rejected。并且参数是根据回调函数传入的值决定的

```javascript
const p = Promise.resolve(123);
console.log(p);

const p1 = Promise.resolve(
  new Promise((res, rej) => {
    rej("哈哈哈");
  })
);
// 用来解决失败回调，浏览器报错的问题
p1.catch((reason)=>{
   console.log("ERROR")
})
console.log(p1);
```

![[00 assets/912dae95798eb21cbffe39bef5598293_MD5.png]]

## 2.5 Promise.reject()

(1) 不管你传入什么，都是`reject`，你传入什么，失败的结果就是什么

```javascript
const p = Promise.reject(123);
console.log(p);

const p1 = Promise.reject(
  new Promise((res, rej) => {
    res("哈哈哈");
  })
);
console.log(p1);
```

![[00 assets/fbd2f7324b33a08fc562caccc681cf57_MD5.png]]

## 2.6 Promise.all()

(1) promises 包含 n 个 promise 的数组

说明：返回一个新的 promise，只有所有的 promise 都成功才成功，只要有一个失败了就直接失败

```javascript
//假如都成功的话，最后的结果就是zhuan'ru
const p1 = Promise.resolve(123);
const p2 = Promise.resolve(
  new Promise((res, rej) => {
    res("哈哈哈");
  })
);
const p3 = new Promise((res, rej) => {
  res("哈哈哈哈哈");
});

const result = Promise.all([p1, p2, p3]);
console.log(result);
```

![[00 assets/4ac3d9c40fc02b69783e5e2d0d7b76f9_MD5.png]]

假如里面有一个失败的话，其结果就是失败

```javascript
const p1 = Promise.resolve(123);
const p2 = Promise.resolve(
  new Promise((res, rej) => {
    rej("哈哈哈");
  })
);
const p3 = new Promise((res, rej) => {
  res("哈哈哈哈哈");
});

const result = Promise.all([p1, p2, p3]);
console.log(result);
```

![[00 assets/e142e3bd0cfa49fe5eeb05e3ee759f67_MD5.png]]

## 2.7 Promise.race()

只接受第一个 Promise 的状态的改变，一开始的结果是 reject

但是你给 p1 定时器的话，就让 p2 先执行了，所以结果就是 resolve

```javascript
const p1 = Promise.resolve(
  new Promise((res, rej) => {
    rej("哈哈哈");
  })
);
const p2 = new Promise((res, rej) => {
  res("哈哈哈哈哈");
});

const result = Promise.race([p1, p2]);
console.log(result);

```

![[00 assets/6a121a1cb282f242472eaa0f0cf230b0_MD5.png]]

## 2.8 Promise.allSettled()

[Promise.allSettled() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)

# 3 Promise 关键问题

## 3.1 改变 Promise 状态的方式

一共三种方式

```javascript
const p = new Promise((res,rej)=>{
   // 1.调用res函数
   res()
   // 2.调用rej函数
   rej()
   // 3.抛出错误
   throw "ERROR"
})
```

## 3.2 指定多个 then 都会执行吗？

```javascript
const p = new Promise((res,rej)=>{
   res("ok")
})
p.then((value)=>{
   console.log("1:" + value)
})
p.then((value)=>{
   console.log("2：" + value)
})
```

![[00 assets/e3bb16991076d35e22513304b3639423_MD5.png]]

## 3.3 改变状态和 then 指定回调那个先？

(1) 都有可能，正常情况下是先指定回调再改变状态，但也可以先改状态再指定回调

(2) 如何先改状态再指定回调？

    1.在执行器中直接调用resolve() / reject()

    2.延迟更长时间才调用then()

(3) 什么时候才能得到数据？

    1.如果先指定的回调，那当状态发生改变时，回调函数就会调用，得到数据

    2.如果先改变的状态，那当指定回调时，回调函数就会调用，得到数据

​
首先要理解指定回调和执行回调的区别，指定可以理解为创建 then 回调，但是执行回调就必须在 Promise 构造函数里面执行 resolve() / reject()才可以执行回调

我们在进行同步任务的时候，可能先改变状态，再去指定回调，然后执行回调

平时我们执行异步任务居多，这样的话就是先指定回调，再改变状态，然后执行回调

```javascript
const p = new Promise((res, rej) => {
  //1. 进行同步任务
  res("ok");
  //2. 进行异步任务
  setTimeout(() => {
    res("ok");
  }, 2000);
});
p.then((value) => {
  console.log(value);
});
console.log(p);
```

## 3.4 then 返回的结果由什么决定?

首先我们来看 then()方法的返回值是什么？结果是一个 Promise 对象

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
let result = p.then((value) => {
  console.log(value);
});
console.log(result);
```

![[00 assets/65b1aa2981a75a7fc8ded166ae709648_MD5.png]]

这个 Promise 的返回值是由里面的 resolve() / reject()回调函数决定的，其结果和 Promise.resolve()是一样的规律

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
let result = p.then((value) => {
  return "ok"
});
console.log(result);
```

![[00 assets/b2bc818f28cf757fc0389cb52ea50d39_MD5.png]]

假如我们返回 Promise 对象，返回 resolve() 状态的 Promise 的话，结果就是 resolve

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
let result = p.then((value) => {
  return new Promise((res, rej) => {
    rej("Error");
  });
});
console.log(result);
```

![[00 assets/46548ee9061cbd8ff273b6e85adcc0f2_MD5.png]]

## 3.5 串联任务

下面就是串联任务的一种

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
p.then((value) => {
  //根据上面一点，then()方法返回的值为resolve，那么就是Promise对象执行后面的then回调
  return new Promise((res, rej) => {
    res("Error");
  });
})
  .then((value) => {	//这里参数为上面的Error
    console.log(value); //Error
  })
  .then((value) => {	//不返回reject的话，就是resolve，并且没返回值，所以这里就是undefined
    console.log(value); //undefined
  });
```

## 3.6 异常穿透

(1) 当使用 promise 的 then 链式调用时，可以在最后指定失败的回调

(2) 前面任何操作出了异常，都会传到最后失败的回调中处理

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
p.then((value) => {
  throw "ERROR"
})
  .then((value) => {
    console.log("111");
  })
  .then((value) => {
    console.log("111");
  })
  .catch((reason) => {
    console.log(reason);
  });

```
![[00 assets/4c6b490831f20cc092bc3e8c744b15e9_MD5.jpeg]]

## 3.7 如何中断 Promide 链？

(1) 当使用 promise 的 then 链式调用时，在中间中断，不再调用后面的回调函数

(2) 办法：在回调函数中返回一个 pendding 状态的 promise 对象

```javascript
const p = new Promise((res, rej) => {
  res("ok");
});
p.then((value) => {
  return new Promise(() => {});
})
  .then((value) => {
    console.log("111");
  })
  .then((value) => {
    console.log("111");
  })
  .catch((reason) => {
    console.log(reason);
  });

```

为什么返回一个 Padding 状态的 Promise 对象就可以了，因为你不管是 resolve 和 reject，都会触发 then()方法的回调函数，所以我们直接传递 padding 状态的 Promise 对象就不会再执行后面的操作

# 4 自定义封装

## 4.1 初始结构

```javascript
function Promise(executor) {}

Promise.prototype.then = function (onResolved, onRejected) {};
```

## 4.2 resolve 和 reject

```javascript
function Promise(executor) {

  this.PromiseState = "Pending";
  this.PromiseResult = null;
  const _this = this;

  function resolve(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  function reject(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  executor(resolve, reject);
}

Promise.prototype.then = function (onResolved, onRejected) {};
```

## 4.3 throw 抛出异常改变状态

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  function reject(data) {
    _this.PromiseState = "resolve";
    _this.PromiseResult = data;
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this)
}

Promise.prototype.then = function (onResolved, onRejected) {};
```

## 4.4 Promise 状态只能修改一次

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this);
}

Promise.prototype.then = function (onResolved, onRejected) {};
```

## 4.5 异步任务回调的执行

下面为运行的代码，这里就是上面的 Promise 关键问题第 3 个的实际场景，`指定回调`和`执行回调`的区别。

我们运行到 Promise 里面的`executor函数`之后，因为是一个定时器，这个时候 JS 就会开启异步任务，将这个定时器纳入队列中。然后执行后面的代码，这个时候就指定了 then 回调，执行 then 回调。但是这个时候 Promise 对象的状态是没有改变的，所以里面的方法一个都不会执行。当定时器结束之后，状态改变，但是 then 回调并不是再去执行一遍。

```javascript
<script>
  let p = new Promise((res, rej) => {
    setTimeout(() => {
      res(123);
    }, 3000);
  });
  p.then(
    (value) => {
      console.log(value);
    },
    (reason) => {
      console.log(reason);
    }
  );
</script>
```

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callback = {};
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      if (_this.callback.onResolved) {
        _this.callback.onResolved(data);
      }
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      if (_this.callback.onRejected) {
        _this.callback.onRejected(data);
      }
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this);
}

Promise.prototype.then = function (onResolved, onRejected) {
  if (this.PromiseState === "resolve") {
    onResolved(this.PromiseResult);
  }
  if (this.PromiseState === "reject") {
    onRejected(this.PromiseResult);
  }
  if (this.PromiseState === "Pending") {
    this.callback = {
      onResolved,
      onRejected,
    };
  }
};
```

## 4.6 指定多个回调

每次调用 then，就将 onResolved、onRejected 存起来就可以了

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
         item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }

  console.log(this);
}

Promise.prototype.then = function (onResolved, onRejected) {
  if (this.PromiseState === "resolve") {
    onResolved(this.PromiseResult);
  }
  if (this.PromiseState === "reject") {
    onRejected(this.PromiseResult);
  }
  if (this.PromiseState === "Pending") {
    this.callbacks.push({
      onResolved,
      onRejected,
    });
  }
};

```

## 4.7 then 方法结果返回

## 4.8 异步修改 then 方法结果返回

## 4.9 完善 then 方法

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

```

## 4.10 catch 方法，异常穿透与值传递

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

```

## 4.11 resolve 方法封装

## 4.12 all 方法封装

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};
```

## 4.13 race 方法封装

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      ChangePending(onResolved);
    }
    if (this.PromiseState === "reject") {
      ChangePending(onRejected);
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          ChangePending(onResolved);
        },
        onRejected: function () {
          ChangePending(onRejected);
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};

Promise.race = function (value) {
  return new Promise((res, rej) => {
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") return;
        if (item.PromiseState === "resolve") {
          res(item.PromiseResult);
        }
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        }
      });
    } catch (e) {}
  });
};

```

## 4.14 then 方法异步执行

给 then 里面的回调添加一个定时器，让回调异步执行就可以了

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      setTimeout(() => {
        ChangePending(onResolved);
      });
    }
    if (this.PromiseState === "reject") {
      setTimeout(() => {
        ChangePending(onRejected);
      });
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          setTimeout(() => {
            ChangePending(onResolved);
          });
        },
        onRejected: function () {
          setTimeout(() => {
            ChangePending(onRejected);
          });
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};

Promise.race = function (value) {
  return new Promise((res, rej) => {
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") return;
        if (item.PromiseState === "resolve") {
          res(item.PromiseResult);
        }
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        }
      });
    } catch (e) {}
  });
};

```

## 4.15 class 版本的封装

下面这个是 class 版本的封装

```javascript
class Promise {
  // 构造函数
  constructor(executor) {
    //添加属性
    this.PromiseState = "Pending";
    this.PromiseResult = null;
    this.callbacks = [];
    //将对象自己保存到_this
    const _this = this;

    function resolve(data) {
      if (_this.PromiseState === "Pending") {
        _this.PromiseState = "resolve";
        _this.PromiseResult = data;
        _this.callbacks.forEach((item) => {
          if (item.onResolved) {
            item.onResolved(data);
          }
        });
      }
    }

    function reject(data) {
      if (_this.PromiseState === "Pending") {
        _this.PromiseState = "reject";
        _this.PromiseResult = data;
        _this.callbacks.forEach((item) => {
          if (item.onRejected) {
            item.onRejected(data);
          }
        });
      }
    }

    try {
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  // then方法
  then(onResolved, onRejected) {
    const _this = this;
    if (typeof onRejected !== "function") {
      onRejected = (reason) => {
        throw reason;
      };
    }
    if (typeof onResolved !== "function") {
      onResolved = (value) => value;
    }
    return new Promise((res, rej) => {
      function ChangePending(onChange) {
        try {
          const onResult = onChange(_this.PromiseResult);
          if (onResult instanceof Promise) {
            onResult.then(
              (value) => {
                res(value);
              },
              (reason) => {
                rej(reason);
              }
            );
          } else {
            res(onResult);
          }
        } catch (e) {
          rej(e);
        }
      }
      if (this.PromiseState === "resolve") {
        setTimeout(() => {
          ChangePending(onResolved);
        });
      }
      if (this.PromiseState === "reject") {
        setTimeout(() => {
          ChangePending(onRejected);
        });
      }
      if (this.PromiseState === "Pending") {
        this.callbacks.push({
          onResolved: function () {
            setTimeout(() => {
              ChangePending(onResolved);
            });
          },
          onRejected: function () {
            setTimeout(() => {
              ChangePending(onRejected);
            });
          },
        });
      }
    });
  }

  //catch方法
  catch(onRejected) {
    this.then(undefined, onRejected);
  }

  // resolve方法
  static resolve(value) {
    return new Promise((res, rej) => {
      try {
        if (value instanceof Promise) {
          value.then(
            (data) => {
              res(data);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(value);
        }
      } catch (e) {
        rej(e);
      }
    });
  }

  //reject方法
  static reject(value) {
    return new Promise((res, rej) => {
      rej(value);
    });
  }

  // all方法
  static all(value) {
    return new Promise((res, rej) => {
      const array = [];
      try {
        value.forEach((item) => {
          if (item.PromiseState === "Pending") throw new Error("");
          if (item.PromiseState === "reject") {
            rej(item.PromiseResult);
          } else {
            array.push(item.PromiseResult);
          }
        });
      } catch (e) {
      } finally {
        if (value.length === array.length) {
          res(array);
        }
      }
    });
  }

  // race方法
  static race(value) {
    return new Promise((res, rej) => {
      try {
        value.forEach((item) => {
          if (item.PromiseState === "Pending") return;
          if (item.PromiseState === "resolve") {
            res(item.PromiseResult);
          }
          if (item.PromiseState === "reject") {
            rej(item.PromiseResult);
          }
        });
      } catch (e) {}
    });
  }
}
```

下面这个是使用原型来控制的封装

```javascript
function Promise(executor) {
  //添加属性
  this.PromiseState = "Pending";
  this.PromiseResult = null;
  this.callbacks = [];
  //将对象自己保存到_this
  const _this = this;

  function resolve(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "resolve";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onResolved) {
          item.onResolved(data);
        }
      });
    }
  }

  function reject(data) {
    if (_this.PromiseState === "Pending") {
      _this.PromiseState = "reject";
      _this.PromiseResult = data;
      _this.callbacks.forEach((item) => {
        if (item.onRejected) {
          item.onRejected(data);
        }
      });
    }
  }

  try {
    executor(resolve, reject);
  } catch (e) {
    reject(e);
  }
}

Promise.prototype.then = function (onResolved, onRejected) {
  const _this = this;
  if (typeof onRejected !== "function") {
    onRejected = (reason) => {
      throw reason;
    };
  }
  if (typeof onResolved !== "function") {
    onResolved = (value) => value;
  }
  return new Promise((res, rej) => {
    function ChangePending(onChange) {
      try {
        const onResult = onChange(_this.PromiseResult);
        if (onResult instanceof Promise) {
          onResult.then(
            (value) => {
              res(value);
            },
            (reason) => {
              rej(reason);
            }
          );
        } else {
          res(onResult);
        }
      } catch (e) {
        rej(e);
      }
    }
    if (this.PromiseState === "resolve") {
      setTimeout(() => {
        ChangePending(onResolved);
      });
    }
    if (this.PromiseState === "reject") {
      setTimeout(() => {
        ChangePending(onRejected);
      });
    }
    if (this.PromiseState === "Pending") {
      this.callbacks.push({
        onResolved: function () {
          setTimeout(() => {
            ChangePending(onResolved);
          });
        },
        onRejected: function () {
          setTimeout(() => {
            ChangePending(onRejected);
          });
        },
      });
    }
  });
};

Promise.prototype.catch = function (onRejected) {
  this.then(undefined, onRejected);
};

Promise.resolve = function (value) {
  return new Promise((res, rej) => {
    try {
      if (value instanceof Promise) {
        value.then(
          (data) => {
            res(data);
          },
          (reason) => {
            rej(reason);
          }
        );
      } else {
        res(value);
      }
    } catch (e) {
      rej(e);
    }
  });
};

Promise.reject = function (value) {
  return new Promise((res, rej) => {
    rej(value);
  });
};

Promise.all = function (value) {
  return new Promise((res, rej) => {
    const array = [];
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") throw new Error("");
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        } else {
          array.push(item.PromiseResult);
        }
      });
    } catch (e) {
    } finally {
      if (value.length === array.length) {
        res(array);
      }
    }
  });
};

Promise.race = function (value) {
  return new Promise((res, rej) => {
    try {
      value.forEach((item) => {
        if (item.PromiseState === "Pending") return;
        if (item.PromiseState === "resolve") {
          res(item.PromiseResult);
        }
        if (item.PromiseState === "reject") {
          rej(item.PromiseResult);
        }
      });
    } catch (e) {}
  });
};

```

# 5 async 和 await 函数

## 5.1 async

返回值未 Promise 类型的对象，其基本和 then 的返回的逻辑是一样的

```javascript
async function fn() {
  // return "ok"
  // throw "Error"
  return new Promise((res, rej) => {
    rej(111);
  });
}
let result = fn();
console.log(result);
```

## 5.2 await

1.await 右侧的表达式一般为 promise 对象，但也可以是其它的值

2.如果表达式是 promise 对象，await 返回的是 promise 成功的值

3.如果表达式是其它值，直接将此值作为 await 的返回值

注意

1.await 必须写在 async 函数中，但 async 函数中可以没有 await

2.如果 await 的 promise 失败了，就会抛出异常，需要通过 try.catch 捕获处理

```javascript
async function fn() {
  const p = new Promise((res, rej) => {
    res(111);
  });
  const result = await p;
  console.log(result);
}
fn();
```

![[00 assets/37f993d7deff4af3f5462f3bcd2072a4_MD5.png]]

## 5.3. async 和 await 实践

### 5.3.1 读取文件

```javascript
const fs = require("fs");
const util = require("util");

const miniReanFile = util.promisify(fs.readFile);

async function main() {
  try {
    let a = await miniReanFile("./1.txt");
    let b = await miniReanFile("./2.txt");
    console.log(a + b);
  } catch (e) {
    console.log(e);
  }
}
main();
```

### 5.3.2 发送 AJAX 请求

```javascript
async function GetAjax(url) {
  const result = await new Promise((res, rej) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.send();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status >= 200 && xhr.status < 300) {
          res(xhr.response);
        } else {
          rej(xhr.status);
        }
      }
    };
  });
  console.log(result);
}
GetAjax("http://gmall-h5-api.atguigu.cn/api/product/getBaseCategoryList")
```
