# 1 基本介绍

![[00 assets/bc901b9e5a7d96417f5e8a51921b96c2_MD5.png]]


# 2 基本使用

![[00 assets/debfb9de3e5db6d438eb111fba346523_MD5.png]]

下面为基本使用的过程，假如我们需要使用到监听需要使用`proxy`对象来操作

```javascript
let obj = {
  name: "张三",
  age: 18,
};

const objProxy = new Proxy(obj, {
  // 获取值时的捕获器
  get(target, key) {
    console.log(`监听到${key}被获取~`);
    return target[key];
  },

  // 设置值时的捕获器
  set(target, key, newValue) {
    console.log(`监听到${key}被改变~`);
    target[key] = newValue;
  },

  // 监听in的捕获器
  has(target, key) {
    console.log(`监听到${key}的in操作~`);
    return key in target;
  },

  // 监听delete的捕获器
  deleteProperty(target, key) {
    console.log(`监听到${key}的delete操作~`);
    delete target[key];
  },
});

console.log(objProxy.name);
objProxy.name = "李四";
console.log("name" in objProxy);
delete objProxy.name;
```

![[00 assets/e4572afad8bdbbd94698c2374f097a23_MD5.png]]

# 3 捕获器

![[00 assets/86b83b8f8ff733fafb0a91a678765842_MD5.png]]

下面时`apply`、`construct`的捕获器的使用案例

![[00 assets/31ca669c8e2b388e9b98493f2820161a_MD5.png]]

