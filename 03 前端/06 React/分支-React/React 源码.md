# 1 虚拟DOM


# 2 任务切片

![[00 assets/3e7a00b15214b91b660956bb38bc8f52_MD5.jpeg]]

![[00 assets/92de3a4b33464574e0c1d3b45acd911e_MD5.jpeg]]

![[00 assets/59218495f3a5df01b15ad0546c0a374e_MD5.jpeg]]


# 3 performUnitOfWork

1、其实本质就是将原本的 虚拟DOM 结构进行串联，变成 `Root -> A -> B -> C -> D`并且 `A、B、C、D` 都可以访问 `Root`
![[00 assets/3b38ca8fbd4a089011b482a165d6f087_MD5.jpeg]]