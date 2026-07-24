# 1 基本介绍

![[00 assets/cf35f1dcd6598963f7271e84ff06ff90_MD5.png]]

Set 是一种新的数据结构 Set 集合，他类似于数组，但是值是唯一的，并且这个集合实现了 Iterator 接口，所以可以使用 for..of 来遍历

```javascript
let s = new Set(["1", "2", "3", "4", "1"]); // Set的一个功能就是对数组进行去重操作

console.log(s, ...s); // Set也支持扩展运算符(...)
```

![[00 assets/2640d19f6fda960bfe62d9a3c8e8003d_MD5.png]]

假如你传入的是对象的话，就不会去重。因为对象的本质就是一个内存地址，每创建一个对象内存地址都不一样

![[00 assets/51a6a65a3de1a42b42f0b7b8322303f9_MD5.png]]

# 2 常用方法

当然他还有一些 API

```javascript
let s = new Set(["1", "2", "3", "4", "1"]);
s.size; //元素的个数
s.add("5"); //增加
s.delete("1"); //删除
s.has("2"); //存在
s.clear(); //清空
//遍历
for (let i of s) {
  console.log(i);
}
s.forEach((ele) => {
  console.log(ele);
});
```

# 3 强引用/弱引用

我们创建了这样一个对象。其中`obj`和`obj.friend`就是强引用，假如把它们设置为`null`的话，这样就没有其他引用指向它，那么就会被销毁。

这个时候我们使用`WeakSet`引用的话，就是弱引用。弱引用和强引用的区别就是，弱引用依旧可以使用`info.name`来获取数据，但是`GC`在回收的时候不会管这条引用，依旧会直接销毁该对象

其中`WeakSet`对对象的引用就是一个弱引用

![[00 assets/205d6b6cf90714aca0b316c7e5a54d6e_MD5.jpeg]]

# 4 WeakSet

![[00 assets/30626b44550c670536a2127654a6d8bb_MD5.png]]

![[00 assets/fdcb13b99256695ef4aa6e3fc8be51f0_MD5.png]]

```javascript
let ws = new WeakSet();
ws.add({ name: "张三" });
```

当然`WeakSet`的应用场景比较少，下面就是为数不多的几个。下面的应用场景是只**允许对象隐式调用，而不允许对象显示调用**

下面为解释，其中有一个点就是为什么不能使用`Set`。因为`Set`是一个强引用，后期假如要消除对象`p = null`的时候，因为`Set`也强引用了一份，所以并不会删除该对象，还需要`Set`来删除一份，才能消除该对象。

![[00 assets/920b8dea9fa66248ee5c5351c8c2f679_MD5.png]]
