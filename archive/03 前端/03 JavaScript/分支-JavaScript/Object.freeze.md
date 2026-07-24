1、我们可以使用 Object.freeze 来冻结对象，这样他就不可变了

2、但是对于深层次的数据不会去进行冻结

3、其实针对 Vue2 就可以使用 Object.freeze 就可以实现性能优化，因为数据不可变，Vue2 的渲染会加快

![[00 assets/889a919c8989c21a8ac1f11253d24cb6_MD5.png]]
