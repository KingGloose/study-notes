# 1 虚拟DOM


# 2 任务切片

![[00 assets/3e7a00b15214b91b660956bb38bc8f52_MD5.jpeg]]

![[00 assets/92de3a4b33464574e0c1d3b45acd911e_MD5.jpeg]]

![[00 assets/59218495f3a5df01b15ad0546c0a374e_MD5.jpeg]]

requestAnimationFrame、requestIdleCallback、webworker、微任务、宏任务

为什么不使用 setTimeout 的话，存在 4ms 左右的延迟，即便设置时间为 0
![[00 assets/9f9f7d80569f6d380b1f89476a556cea_MD5.jpg]]

React 在这么多的选项中选择了 [MessageChannel - Web API | MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/MessageChannel)

本质其实就是使用 requestAnimationFrame 来计算还剩多长时间，如果有空闲的就将计算通过MessageChannel将逻辑推到宏任务中，避免阻塞了主线程中的代码执行，这就是一个比较经典的fiber

下面就是实现的一个很简单的 fiber
![[00 assets/94a7fe5e699f02ad8a5a975978b2f85a_MD5.jpeg]]

# 3 performUnitOfWork

1、其实本质就是将原本的 虚拟DOM 结构进行串联，变成 `Root -> A -> B -> C -> D`并且 `A、B、C、D` 都可以访问 `Root`
![[00 assets/3b38ca8fbd4a089011b482a165d6f087_MD5.jpeg]]

# 4 createElement

![[00 assets/4c7e1c88ec7a35125545773cbe6581fd_MD5.jpg]]

![[00 assets/507a05a690076c20c536092eb370f8e3_MD5.jpg]]


![[00 assets/032af8e710f5ed5be5dd3cd53cb1cfe3_MD5.jpg]]

![[00 assets/e1fcda05037f10b0f5c1a13b6e93dfce_MD5.jpg]]

![[00 assets/3562c8c799eb1f3e6d825a1f09e2fb98_MD5.jpg]]

![[00 assets/5f5351e88b56d3694423a4cd0aed2239_MD5.jpg]]


针对 React15 就是使用的 Stack Fiber 来实现的，也就是递归
![[00 assets/59b45e15e0bedd956b43916dff4cf0e9_MD5.jpeg]]