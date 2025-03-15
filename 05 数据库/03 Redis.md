文章介绍：[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7229127664756326455)

**官方文档**：[Redis Strings | Redis](https://redis.io/docs/data-types/strings/)

**可视化 UI**：[qishibo/AnotherRedisDesktopManager: 🚀🚀🚀A faster, better and more stable Redis desktop manager [GUI client\], compatible with Linux, Windows, Mac. (github.com)](https://github.com/qishibo/AnotherRedisDesktopManager)

# 1. 基本介绍

1、前面我们学了 `mysql`，它是通过表和字段来存储信息的，表和表之间通过 id 关联，叫做`关系型数据库`。它提供了 sql 语言，可以通过这种语言来描述对数据的增删改查。mysql 是通过硬盘来存储信息的，并且还要解析并执行 sql 语句，这些决定了它会成为性能瓶颈。也就是说服务端执行计算会很快，但是等待数据库查询结果就很慢了。

2、计算机领域最经常考虑到的性能优化手段就是`缓存`了。能不能把结果缓存在内存中，下次只查内存就好了呢？内存和硬盘的速度差距还是很大的

![image-20231223102918716](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356490.png)

3、所以做后端服务的时候，我们不会只用 mysql，一般会结合内存数据库来做缓存，最常用的是 `redis`。因为需求就是缓存不同类型的数据，所以 redis 的设计是 `key、value` 的键值对的形式。

# 2. 基本使用

1、输入`redis-cli`进入`redis`的控制台界面，我这里使用`docker`来部署的，这段内容可以参考`docker`笔记

![image-20231223105425948](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356518.png)

## 2.1 String

> set / get / setnx / mget

1、使用`set`来创建一个键值对，`get`来获取

![image-20231223105735043](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356520.png)

2、`setnx`如果键存在就不保存

![image-20231223110944283](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356528.png)

3、`megt`可以联合多个键一起查询

![image-20231223111112275](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356531.png)

> incr

`incr`用于递增，一般阅读量、点赞量等都是通过这个来计数

![image-20231223110629673](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356541.png)

## 2.2 List

> lpush / rpush / lpop / rpop / lrange

1、可以理解为数组中的`push`和`pop`，其中`l`和`r`分别表示向左`push`还是`pop`

2、`lrange`表示查看该`list`数据，`0 -1`表示从 1 到-1 查询，也就是查完，而`0 5`表示查询前 5 个

![image-20231223143540786](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356230.png)

> ltrim

1、表示截取 list 中的数据，`1 3`表示开始索引和结束索引，而`1 -2`表示开始索引为 1，倒数索引为-2 的段落

![image-20231223144627671](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356253.png)

> lmove

查看文档即可

## 2.3 Set

### 2.3.1 set

![image-20231223145003210](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356277.png)

> sadd / sismember

1、set 的特点是无序并且元素不重复

2、`sadd`表示添加数据

![image-20231223145102787](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356306.png)

3、`sismember`表示查看该`set`中是否含有该元素

![image-20231223145200307](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356337.png)

### 2.3.2 zset

![image-20231223145340770](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356374.png)

> zadd / zrange

1、`set` 只能去重、判断包含，不能对元素排序。如果排序、去重的需求，比如排行榜，可以用 `sorted set`，也就是 `zset`

2、其中`1`表示`score`，第二个表示`member`，`zset`就是根据`socre`来排序的

![image-20231223145542561](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356087.png)

3、使用`zrange`来查看数据

![image-20231223145735351](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356122.png)

## 2.4 Hash

![image-20231223145819469](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356160.png)

> hset / hget

1、`hset`表示为`hash1`添加一个键为`name1`，值为`1`的键值对数据

![image-20231223150250613](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356193.png)

2、使用`hget`来取

![image-20231223150345213](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356217.png)

## 2.5 Geo

> geoadd / geodist / georadius

1、`geo` 的数据结构，就是经纬度信息，根据距离计算周围的人用的，平时我们查找周围的人、周围的 xxx 都可以通过 `redis` 的 geo 数据结构实现

2、用 `loc` 作为 key，分别添加 `guangguang` 和 `dongdong` 的经纬度，`13.36...`表示经度，`38.11...`表示纬度

![image-20231223150612201](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356280.png)

3、`redis` 实际使用 `zset` 存储的，把经纬度转化为了二维平面的坐标

![image-20231223150936164](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356862.png)

4、使用`geodist`可以计算 2 个之间的距离

![image-20231223151033887](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356884.png)

5、用 `georadius` 搜索某个半径内的其他点，传入经纬度、半径和单位

![image-20231223151340575](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356908.png)

# 3. 过期时间

> expire / ttl

1、表示设置`info1`，30s 之后过期删除

![image-20231223151544917](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356932.png)

2、使用`ttl`查看剩余过期时间使用 `ttl`

![image-20231223151803381](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356957.png)
