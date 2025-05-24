# 1、渲染器原理

这部分内容可以直接参考 [[2024.4.20 【Vue.js 设计与实现】渲染器实现]]

# 2. Vue 响应式原理

代码如下，需要回顾先前的知识`proxy`、[[Reflect]]、`defineproperty`、`WeakMap`

```javascript
let activeReacriveFn = null;

class Depend {
  constructor() {
    this.receiverFn = new Set();
  }
  addDepend(fn) {
    this.receiverFn.push(fn);
  }
  depend() {
    if (activeReacriveFn) {
      this.receiverFn.add(activeReacriveFn);
    }
  }
  notify() {
    this.receiverFn.forEach((ele) => {
      ele();
    });
  }
}

function watchFn(fn) {
  activeReacriveFn = fn;
  fn();
  activeReacriveFn = null;
}

let targetMap = new WeakMap();
function getDepend(target, key) {
  let map = targetMap.get(target);
  if (!map) {
    map = new Map();
    targetMap.set(target, map);
  }

  let depend = map.get(key);
  if (!depend) {
    depend = new Depend();
    map.set(key, depend);
  }

  return depend;
}

// Vue3 使用Proxy实现响应式
function reactive(obj) {
  return new Proxy(obj, {
    get(target, key, receiver) {
      const depend = getDepend(target, key);
      depend.depend();
      return Reflect.get(target, key, receiver);
    },
    set(target, key, newValue, receiver) {
      Reflect.set(target, key, newValue, receiver);
      const depend = getDepend(target, key);
      depend.notify();
    },
  });
}

// Vue2 使用defineproperty实现响应式
function reactiveVue2(obj) {
  Object.keys(obj).forEach((key) => {
    let value = obj[key];
    Object.defineProperty(obj, key, {
      get() {
        const depend = getDepend(obj, key);
        depend.depend();
        return value;
      },
      set(newValue) {
        value = newValue;
        const depend = getDepend(obj, key);
        depend.notify();
      },
    });
  });

  return obj;
}

let obj = reactive({
  name: "张三",
  age: 18,
});

watchFn(function () {
  obj.name;
  console.log("执行一段代码~ - 1");
});
watchFn(function () {
  obj.name;
  console.log("执行一段代码~ - 2");
});
watchFn(function () {
  obj.age;
  console.log("执行一段代码~ - 3");
});
watchFn(function () {
  obj.name;
  obj.age;
  console.log("执行一段代码~ - 4");
});

console.log("============== 第一次代码执行完毕 ==============");

// objProxy.name = "李四";
obj.age = 20;
```

![[00 assets/35503c4f75faa274e73418e2eb233624_MD5.png]]
