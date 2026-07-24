视频讲解：[130*Mongodb_Mongodb 介绍*哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1gM411W7ex?p=130&vd_source=2d46cc0fa105788201e3e43d9c83f528)

# 1. 基本介绍

## 1.1 基本介绍

![image-20230315104324919](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356933.png)

1、对于`Mongodb`来说本质就是下图中的格式

![image-20230315104331892](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356938.png)

其实就是按照`JSON`格式来编写

![image-20230315104508286](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356956.png)

## 1.2 下载安装

1、**下载链接**：[Download MongoDB Community Server | MongoDB](https://www.mongodb.com/try/download/community)，目前我按照下面的版本来下载

![image-20230331171452604](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356950.png)

2、配置环境变量。下载`mongosh`才能直接在控制台操作`mongodb`，我们需要将`mongosh`复制到`bin`文件夹中，`mongosh`下载地址：[MongoDB Shell Download | MongoDB](https://www.mongodb.com/try/download/shell)

![image-20230331193449909](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356953.png)

# 2. 数据库命令

```
show dbs			 // 显示所有数据库
use 数据库名		  // 切换到指定的数据库，如果数据库不存在会自动创建数据库
db				     // 显示当前所在的数据库

use 库名
db.dropDatabase()    // 删除当前数据库
```

# 3. 集合命令

```
db.createCollection('集合名称')		   // 创建集合
show collections					  // 显示当前数据库中的所有集合
db.集合名.drop()						// 删除某个集合
db.集合名.renameCollection('newName')  // 重命名集合
```

# 4. 文档命令

> 插入文档、查询文档

```
db.集合名.insert(文档对象);			// 插入文档

// _id 是 mongodb 自动生成的唯一编号，用来唯一标识文档
db.集合名.find(查询条件)				// 查询文档
```

1、我们插入的都是对象数据，并且可以发现可以存入不规律的数据格式

![image-20230331200140976](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356970.png)

2、我们可以给`find()`添加查询条件

![image-20230331200331405](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356802.png)

> 更新文档

```
db.集合名.update(查询条件,新的文档)	 // 更新文档
db.集合名.update({name:'张三'},{$set:{age:19}})
```

![image-20230331200945512](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356825.png)

> 删除文档

```
db.集合名.remove(查询条件)				// 删除文档
```

![image-20230331201426819](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032356856.png)
