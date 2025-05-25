
## 1. rest 参数

这个是扩展运算符关于对象的使用

```javascript
function con({name,...other}){
	console.log(name);
	console.log(other);
}
con({
	name:'张三',
	age:12,
	sex:'男'
});
```

![[00 assets/8ac14920232e9c95488de4a43e502b66_MD5.png]]

## 2. 扩展运算符

其基本的原理也是 ES 差不多

```javascript
const p1 = {
	name1:'张三',
	age:12
}
const p2 = {
	name2:'李四'
}
const p3 = {
	name3:'王五'
}
const l = {...p1,...p2,...p3};
console.log(l);
```

![[00 assets/142ff4b969c078ff1ef1d8cc408e4c38_MD5.png]]
