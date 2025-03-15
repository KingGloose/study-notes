[【零基础 快速学 Java】韩顺平 零基础 30 天学会 Java\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1fh411y7R8?p=731&vd_source=2d46cc0fa105788201e3e43d9c83f528) (数据库部分)

# 1. 基本介绍

`客户端`通过端口号`3306`来操作`DBMS`，并且`数据库`和`数据库下面的`表其实本质就是**文件**

![image-20220723133543804](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355881.png)

其中每条数据在`Java`中一般都是一个对象来表示

![image-20220723133826787](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355937.png)

2、下面为`mysql`的整体架构图

![image-20231222210603076](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355919.png)

# 2. 数据库操作

## 2.1 创建数据库

```sql
CREATE DATABASE [IF NOT EXISTS] db_name [create_specification [,create_specification]...]
```

```sql
1.CHARACTER SET:指定数据库采用的字符集，如果不指定字符集，默认utf8
2.COLLATE:指定数据库字符集的校对规则(注意默认是utf8_general_ci)
（常用的utf8_bin[区分大小写]、utf8_general_cil[不区分大小写])
```

> 应用案例

![image-20220723140227307](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355924.png)

```sql
CREATE DATABASE ZJH_DB01; //1
CREATE DATABASE ZJH_DB02 CHARACTER SET utf8; //2
CREATE DATABASE ZJH_DB03 CHARACTER SET utf8 COLLATE utf8_bin; //3
```

当`数据库ZJH_DB03`指定了校对规则为`utf8_bin`，假如我们不去设置`数据库ZJH_DB03`下面的表的`校对规则`，就默认跟随库的校对规则`utf8_bin`

下面就是解释在`数据库`中什么叫做**区分大小写**，注意数据库`zjh_db03`是区分大小写的

![image-20220723141620733](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355923.png)

数据库`zjh_db01`是不区分大小写的，发现和上面的区别了没，是不是不区分大小写的是都可以查询到，但是你设置了区分大小写就只能查询到一个

![image-20220723141718287](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355918.png)

## 2.2 查询数据库

```sql
SHOW DATABASES; // 显示数据库语句
```

![image-20220723142215598](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355774.png)

在创建数据库或者表的时候为了规避关键字，所以就需要使用**``反引号**

```sql
SHOW CREATE DATABASE zjh_db01 // 显示数据库创建语句
```

![image-20220723142249664](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355807.png)

## 2.3 删除数据库

下面用于删除`数据库zjh_db01`，其中`IF EXISTS`表示如果存在就会删除

```sql
DROP DATABASE [IF EXISTS] zjh_db01; // 数据库删除语句
```

## 2.4 备份恢复数据库

![image-20220723142832261](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355832.png)

> 备份数据库

假如我们使用`DOS`来操作的话，就要进入到`MySql的bin目录`，因为里面有`mysqldump.exe`文件，可以执行备份的操作，我们其实可以备份多个`数据库zjh_db01和zjh_db02`，`>`后面书写备份的文件路径

```bash
mysqldump -u root -p -B zjh_db01 zjh_db02 > d:\\bak.sql
```

![image-20220723143315468](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355864.png)

> 备份数据库下面的表

我们也可以备份数据库下面的表，这里就是删除掉了上面语句的`-B`，假如说你加上了`-B`的话，就会把`表1、表2、表3`都当作数据库了

![image-20220723144322561](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355893.png)

```sql
mysqldump -u root -p zjh_db01 t2 > d:\\bak1.sql
```

![image-20220723144700960](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355943.png)

> 恢复

这个必须要在`Mysql的cmd`里面才能执行，`source`后面接文件名

```sql
source d:\\bak.sql
```

![image-20220723143846079](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355481.png)

还有一个办法就是将备份的`.sql`文件打开，将里面的数据复制粘贴进编辑器中，执行所有的`sql语句`也可以

![image-20220723144054767](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355501.png)

# 3. 表操作

## 3.1 创建表

![image-20220723145824548](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355524.png)

```sql
create table `t1`
(
	id int,
	name VARCHAR(255),
	password VARCHAR(255),
	birthday DATE
) CHARACTER SET utf8 COLLATE utf8_bin ENGINE INNODB;
```

我们在创建表的时候也可以设置默认值`default`，并且可以设置`on update`值，更新数据就会自动更新

```mysql
CREATE TABLE IF NOT EXISTS `user`
(
	id INT PRIMARY KEY auto_increment,
	NAME VARCHAR ( 20 ) NOT NULL UNIQUE,
	PASSWORD VARCHAR ( 20 ) NOT NULL,
	createAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updateAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
```

## 3.2 列类型

![image-20220723150817150](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355555.png)

### 3.2.1 整型

![image-20220723161952879](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355602.png)

```sql
create table `t3`
(
	num TINYINT // 默认创建有符号的，范围就是-128~127
);
create table `t4`
(
	num TINYINT unsigned // 创建无符号的，范围是0-255
);
insert into t3 values(-128) // 默认为有符号的
insert into t4 values(255) // 这里指定的是无符号的
// 其他的数据类型也是同理
```

### 3.2.2 bit

![image-20220723162748700](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355682.png)

```sql
create table `t6`
(
	num bit(10) // 表示 0000 0000 00 十位，没有符号
);
insert into t6 values(255); // 假如你设置的位数是8，那么就是1111 1111
insert into t6 values(1);
select * from t6
```

![image-20220723163609144](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355481.png)

### 3.2.3 浮点

![image-20220723163844856](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355505.png)

`decmial(4,2)`假如出现`1.123`，那么就按`1.12`来算；假如你使用`1.12345`，已经超过`精度4`了，但是会将小数位限制在 2 位，那么最后也是`1.12`

```sql
create table `t7`
(
	num1 float,
	num2 double,
	num3 decimal(4,2) //D标度:小数位为2位  M精度:整数+小数位<=4
);
insert into t7 values(1.22,1.22,1.22);
```

### 3.3.4 字符串

注意这里的一个细节，`char(size)`是存储的固定的`size个字符`

`varchar(size)`表示`65535个字节`，其中有`3`个字节用于存储`size`的大小，所以最后可以使用的是`65532个字节`，但是根据不同的编码形式会造成存储的字符也不同，假如你使用的是`utf8`编码形式，就是`65532/3`表示可以存储`21844个字符`，假如是`gbk`编码形式，就是`65532/2`表示可以存储`32766个字符`

![image-20220723165528419](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355534.png)

```sql
create table `t8`
(
	 str1 char(255),
	 str2 varchar(21000) -- 这里的表默认使用的utf8
	 -- 所以默认的是(65532 - 3)/3
) CHARSET utf8;
```

> 使用细节

**细节 1**

`char(4)` 这个 4 表示字符数(最大 255)，不是**字节数**，不管是中文还是字母都是放四个字符来计算

`varchar(4)` 这个 4 表示`字符数`，不管是字母还是中文都以定义好的表的编码来存放数据 utf8

**细节 2**

`char(4)` 是**定长**(固定的大小)，就是说，即使你插入'a',也会占用分配的 4 个字符.

`varchar(4)` 是**变长**，就是说，如果你插入了'aa',实际占用空间大小并不是 4 个字符，而是按照实际占用空间来分配(varchar 本身还需要占用 1-3 个字节来记录存放内容长度)

**细节 3**

什么时候使用 char，什么时候使 varchar

1.如果数据是**定长**，推荐使用 char，比如:md5 的密码，邮编，手机号，身份证号码等

2.如果一个字段的长度是**不确定**，我们使用 varchar，比如:留言文章

**细节 4**

在存放文本时，也可以使用**Text**数据类型.可以将**TEXT 列**视为**VARCHAR 列**

注意**Text**不能有默认值，大小 0-2^16 字节如果希望存放更多字符，可以选择`MEDIUMTEXT (0~2^24)`或者`LONGTEXT (0~2^32)`

### 3.3.5 日期

![image-20220723173031876](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355558.png)

```sql
create table `t9`
(
	birthday date, -- 生日，年月日
	jobtime datetime, -- 入职时间，年月日 时分秒
	login_time timestamp -- 登录时间，时间戳
		not null default CURRENT_TIMESTAMP -- 表示非空，默认是当前时间时间戳
		on update CURRENT_TIMESTAMP -- 自动更新
);
-- 因为你在后面写了自动更新，所以不用写也会自动更新
insert into t9(birthday,jobtime) values('2022-11-28','2022-12-12 12:12:12');
select * from t9;
```

![image-20220723174308273](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355586.png)

1、如果你想查询时间段的话，使用时间戳是查询不到的，最好使用时间字符，可以参考下图

![image.png](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405110019100.png)

## 3.3 修改表

![image-20220724162712829](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355607.png)

> 应用案例

![image-20220724162822207](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355653.png)

```sql
// 列
alter table emp add image varchar(255) after resume; -- 添加image类型为varchar(255)
alter table emp add (image varchar(244),job varchar(32)) -- 一次添加多个字段
alter table emp modify job varchar(60) -- 修改job列，使其长度为60
alter table employee change `name` `user_name` varchar(32) -- 修改列名name为user_name
alter table emp drop (sex); -- 删除sex列
// 表
rename table emp to employee; -- 修改表名emp为employee
alter table employee character set utf8; -- 修改emplyee的字符集为utf8
```

## 3.4 练习

![image-20220723174339685](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355685.png)

```sql
use zjh_db01;
create table emp
(
	id int,
	name varchar(32),
	sex char(1),
	birthday date,
	entry_date datetime,
	job varchar(32),
	Salary double,
	resume text
) charset utf8 collate utf8_bin;

insert into emp values(1,'张三','男','2001-11-12','2011-12-12 5:00:00','打程序',1200.9,'Hello World!');
```

# 4. insert

![image-20220724164003753](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355710.png)

> 应用案例

![image-20220724164047943](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355734.png)

```sql
use zjh_db01;
create table goods -- 创建表
(
	id int,
	goods_name varchar(10),
	price double
);

insert into goods values(1,'鸡翅',12.98); -- 插入数据
insert into goods values(2,'汉堡',90.89);
```

> 注意事项

1.插入的数据应与字段的数据类型**相同**。比如：把`"abc"`添加到`int类型`会错误

2.数据的长度应在列的**规定范围**内，例如：不能将一个长度为`80`的字符串加入到长度为`40`的列中。

3.在 valuest 中列出的数据位置必须与被加入的列的排列位置**相对应**。

```sql
insert into goods(id,goods_name) values(2,'汉堡');  -- 要一一对应
```

4.**字符**和**日期型数据**应包含在**单引号**中。

```sql
insert into goods values(2,'汉堡',90.89);  -- 字符串需要加上单引号
```

5.列可以插入**空值**（前提是该字段允许为空）

```sql
insert into table value(null) -- 可以添加空值
insert into table values(1,'鸡翅',null) -- 其中price允许为空值
```

6.可以使用 insert 一次添加多条记录

```sql
insert into goods values(3,'香蕉',21.9),(4,'苹果',90.9),(5,'栗子',null); -- 可以一次添加多条
```

7.如果是给表中的所有字段添加数据，可以不写前面的字段名称

```sql
insert into goods values(2,'汉堡',90.89);  -- 这个就包含了所有字段
```

8.在该字段设置为`not null`时，当不给某个字段值时，如果有默认值就会将默认值添加进去，否则就会报错

# 5. update

![image-20220724165528842](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355766.png)

> 应用案例

![image-20220724165553449](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355788.png)

```sql
update emp set salary = 5000 -- 将所有员工的薪水修改为5000
update emp set salary = 3000 where name = '张三'; -- 将姓名为张三的员工薪水改为3000
update emp set salary = salary + 1000 where name = '大妖怪' -- 在原来的基础上加1000
```

> 使用细节

1.`update`语法可以用新值更新原有表行中的各列。

2.`set`子句指示要修改哪些列和要给予哪些值。

3.`where`子句指定应更新哪些行。如：没有 WHERE 子句，则**更新所有的行**。

4.如果需要修改多个字段，可以通过`set `**字段 1 = 值 1，字段 2 = 值 2…**

```sql
update emp set salary = salary + 1000 , sex = '女' where name = '大妖怪' -- 可以修改salary和sex
```

# 6. delete

![image-20220724170757077](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355556.png)

> 应用案例

![image-20220724170810509](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355577.png)

```sql
delete from emp where `name`="大妖怪"; -- 删除老妖怪
delete from emp; -- 删除表中所有数据
```

> 使用细节

1.如果不使用 where 子句，将删除表中**所有数据**

2.**delete**语句不能删除某一列的值（可使用**update**设为 nul l 或者 ' '）

3.使用**delete**语句仅删除记录，不删除表本身。如要删除表，使用`drop table 表名`

# 7. select

## 7.1 基础查询

> 基础查询

![image-20220724171407625](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355603.png)

> 应用案例

![image-20220724171805027](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355641.png)

```sql
select * from student; -- 查询所有学生的成绩
select `name`,english from student; -- 查询字段为name,english的学生

select distinct * from student; -- 过滤表中的重复数据，要所有数据完全相同
select distinct math, english from student; -- 表示math和english一样才会去重
-- 假如出现90,90/91,90就不会去重，因为91和90不一样
```

> 计算符查询

![image-20220724172737924](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355666.png)

> 应用案例

![image-20220724175848545](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355695.png)

```sql
select `name`,(chinese+english+math) from student -- 统计所有学生的总分
select `name`,(chinese+english+math+10) from student -- 在总分下加10
select math as '数学',chinese as '语文',english as '英语' from student; -- 使用别名来查询
```

## 7.2 条件查询

> 条件查询

![image-20220724180232807](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355642.png)

> 应用案例 1

![image-20220724180402792](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355671.png)

```sql
select * from student where `name`='赵云'; -- 查询姓名为赵云的成绩
select * from student where english>90; -- 查询英语成绩大于90
select * from student where (chinese+english+math)>200; -- 查询总分大于200
select * from student where math>60 and id>4; -- 查询math大于60并且id大于4
select * from student where chinese < english; -- 查询英语大于语文
select * from student where (chinese+english+math)>200 and math>chinese and `name` like '韩%'; -- 查询总分大于200，数学成绩大于语文，姓韩的学生
```

> 应用案例 2

![image-20220724183018203](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355702.png)

```sql
select * from student where english between 80 and 90; -- 英语成绩在80-90之间的
select * from student where math in(89,90,91); -- 数学成绩有80,90,91
select * from student where `name` like '宋%'; -- 姓李的学生成绩
select * from student where math>80 and chinese>80; -- 数学>80,语文>80的学生成绩
select * from student where chinese between 70 and 80; -- 语文成绩在70~80
select * from student where (math+chinese+english) in (189,190,191); -- 总分在189,190,191
select * from student where `name` like '李%' or `name` like '宋%'; -- 姓李或者姓宋的学生成绩
select * from student where (english - math) > 30; -- 查询英语比数学多30分的学生成绩
```

## 7.3 group by

> group by 查询

![image-20220724222932124](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355747.png)

> 应用案例

![image-20220724223026265](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355784.png)

```sql
select * from student order by math asc; -- 按照数学成绩顺序查询
select * from student order by (math+chinese+english) desc; -- 按照总分逆序查询
select * from student where name='李%' order by math; -- 姓名为李，按照数学顺序来查询
```

![image-20220725221857124](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355814.png)

```sql
-- 显示每种岗位的雇员总数和平均工资
select job,count(*),avg(sal) from emp group by job;
-- 显示雇员总数，以及获得补助的雇员数
select count(*),count(comm) from emp; -- count(列)如果为null就不会统计
-- 显示雇员总数，以及没有获得补助的雇员数
-- 这里有一个要注意的就是count(null)就表示的不计数
select count(*),count(if(comm is null,1,null)) from emp;
-- 显示管理者的总人数
select count(distinct mgr) from emp; -- 表示对mgr去重
-- 显示雇员工资的最大差额
select max(sal)-min(sal) from emp; -- 最大差额
```

> 查询加强

![image-20220725215251652](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355876.png)

```sql
-- 1992.1.1后入职的员工
select ename,hiredate from emp where datediff(hiredate,'1992.1.1')>0;

select ename,sal from emp where ename like 'S%' -- 首字符为S
select ename,sal from emp where ename like '__O%' -- 第三个字符为O

select * from emp where mgr is null; -- 返回mgr为null的数据
desc emp; -- 查看emp表的结构
```

![image-20220725220140565](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355918.png)

```sql
select * from emp order by sal; -- 按照工资从低到高的顺序显示
-- 先按照部门号升序，再按照排好的部门号对工资进行降序排序
select * from emp order by deptno,sal desc;
```

![image-20220725220839628](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355954.png)

> 补充

```sql
SELECT class,AVG(score) AS avg_score FROM student GROUP BY class HAVING avg_score > 90;
-- having 用于分组 Group By 之后再过滤
```

## 7.4 分页查询

> 分页查询

![image-20220725221010306](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355978.png)

> 应用案例

![image-20220725221025458](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355005.png)

```sql
-- 第一页
select * from emp order by empno
	limit 0,3; -- 表示从第1个数据开始，显示3行
-- 第二页
select * from emp order by empno
	limit 3,3; -- 表示从第4个数据开始，显示3行
-- 第三页
select * from emp order by empno
	limit 6,3;
-- 这个可以用于做前台的分页查询
```

## 7.5 多子句查询

![image-20220725224015666](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355027.png)

> 应用案例

![image-20220725224028848](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355802.png)

```sql
select job,count(*),avg(sal) as sal_avg from emp
group by job having sal_avg>1000
order by sal_avg desc
limit 0,2;
```

# 8. 统计函数

## 8.1 count

![image-20220725171732347](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355824.png)

> 应用案例

![image-20220725171749139](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355850.png)

说白了`count(*)`和`count(列)`没有本质的区别，就是`count(列)`会排除掉有 null 的数据，假如你使用的`count(name)`就是按照`name`来查询，假如`name`中有 null 就会排除

```sql
select * from student order by math asc; -- 按照数学成绩顺序查询
select * from student order by (math+chinese+english) desc; -- 按照总分逆序查询
select * from student where name='李%' order by math; -- 姓名为李，按照数学顺序来查询

use zjh_db01;
select count(*) from student; -- 统计一个班有多少学生
select count(*) from student where math>90; -- 统计数学成绩大于90的学生
select count(*) from student where (math+chinese+english)>250; -- 统计总分大于250的学生
-- count(*)和count(列)的区别
-- count(*) 返回满足条件的记录的行数
-- count(列) 统计满足条件的某列有多少个，会排除null
create table person
(
    `name` varchar(20),
    id int
);
insert into person values("tom",1);
insert into person values("jack",2);
insert into person values("mary");
insert into person values(null);

select count(*) from person; -- 4
select count(`name`) from person; -- 3
select count(`id`) from person; -- 2
```

## 8.2 sum

![image-20220725173828907](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355878.png)

> 应用案例

![image-20220725174152749](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355901.png)

```sql
select sum(math) from student; -- 统计一个班级数学总成绩
select sum(math),sum(chinese),sum(english) from student; -- 统计数学，英语，语文总成绩
select sum(math+english+chinese) from student; -- 统计所有课总分
select sum(chinese)/count(*) from student -- 统计语文平均分
```

## 8.3 avg

![image-20220725174801982](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355008.png)

> 应用案例

![image-20220725174819533](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355746.png)

```sql
select avg(math) from student; -- 数学平均分
select avg(math+chinese+english) from student; -- 班级总分的平均分
```

## 8.4 max/min

![image-20220725174950638](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355780.png)

> 应用案例

![image-20220725175006013](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355816.png)

```sql
select `name`,max(math+chinese+english) from student; -- 最高分
select `name`,min(math+chinese+english) from student; -- 最低分
```

# 9. 分组统计

![image-20220725175406756](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355845.png)

> 应用案例

![image-20220725175418079](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355871.png)

```sql
select avg(sal),max(sal),deptno from emp group by deptno; -- 每个部门的平均工资和最高工资

-- 显示每个部门的每个岗位的平均工资和最低工资
-- 先按照部门来分，在从分好的部门里面分岗位
select avg(sal),min(sal),deptno,job from emp group by deptno,job;

-- 显示平均工资低于2000的部门号和它的平均工资
select avg(sal) as avg_sal,deptno from emp group by deptno having avg(sal)<2000;
-- 使用别名来处理
select avg(sal) as avg_sal,deptno from emp group by deptno having avg_sal<2000;
```

```sql
-- 创建表
use zjh_db02;
#创建表EMP雇员
CREATE TABLE emp
(
	empno  MEDIUMINT UNSIGNED  NOT NULL  DEFAULT 0, /*编号*/
	ename VARCHAR(20) NOT NULL DEFAULT "", /*名字*/
	job VARCHAR(9) NOT NULL DEFAULT "",/*工作*/
	mgr MEDIUMINT UNSIGNED ,/*上级编号*/
	hiredate DATE NOT NULL,/*入职时间*/
	sal DECIMAL(7,2)  NOT NULL,/*薪水*/
	comm DECIMAL(7,2) ,/*红利*/
	deptno MEDIUMINT UNSIGNED NOT NULL DEFAULT 0 /*部门编号*/
);

INSERT INTO emp VALUES(7369, 'SMITH', 'CLERK', 7902, '1990-12-17', 800.00,NULL , 20),
(7499, 'ALLEN', 'SALESMAN', 7698, '1991-2-20', 1600.00, 300.00, 30),
(7521, 'WARD', 'SALESMAN', 7698, '1991-2-22', 1250.00, 500.00, 30),
(7566, 'JONES', 'MANAGER', 7839, '1991-4-2', 2975.00,NULL,20),
(7654, 'MARTIN', 'SALESMAN', 7698, '1991-9-28',1250.00,1400.00,30),
(7698, 'BLAKE','MANAGER', 7839,'1991-5-1', 2850.00,NULL,30),
(7782, 'CLARK','MANAGER', 7839, '1991-6-9',2450.00,NULL,10),
(7788, 'SCOTT','ANALYST',7566, '1997-4-19',3000.00,NULL,20),
(7839, 'KING','PRESIDENT',NULL,'1991-11-17',5000.00,NULL,10),
(7844, 'TURNER', 'SALESMAN',7698, '1991-9-8', 1500.00, NULL,30),
(7900, 'JAMES','CLERK',7698, '1991-12-3',950.00,NULL,30),
(7902, 'FORD', 'ANALYST',7566,'1991-12-3',3000.00, NULL,20),
(7934,'MILLER','CLERK',7782,'1992-1-23', 1300.00, NULL,10);

#工资级别表
CREATE TABLE salgrade
(
	grade MEDIUMINT UNSIGNED NOT NULL DEFAULT 0, -- 工资级别
	losal DECIMAL(17,2)  NOT NULL, -- 该级别的最低工资
	hisal DECIMAL(17,2)  NOT NULL -- 该级别的最高工资
);

INSERT INTO salgrade VALUES (1,700,1200);
INSERT INTO salgrade VALUES (2,1201,1400);
INSERT INTO salgrade VALUES (3,1401,2000);
INSERT INTO salgrade VALUES (4,2001,3000);
INSERT INTO salgrade VALUES (5,3001,9999);
```

# 10. 字符串函数

![image-20220725182928732](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355919.png)

> 应用案例

```sql
select charset(hiredate) from emp; -- 返回字串字符集
select concat(empno,' is ',ename) from emp; -- 连接字符串
-- 查询o在Hello World里面那个首次出现的位置，dual表示不从那个表中取
select instr("Hello World",'o') from dual;
select instr(ename,'o') from emp; -- 表示在ename里面查找o出现的位置
select ucase(ename) from emp -- 转换为大写
select lcase(ename) from emp -- 转换为小写
select left(ename,2) from emp -- 表示从ename左边取出2个字符
select right(ename,2) from emp -- 表示从ename右边取出2个字符
select length(ename) from emp -- 表示返回字符长度，按字节返回的
select replace("Hello World!","World","Java") from dual; -- 将World替换为Java
select strcmp("Hello World!","Hello Java") from dual; -- 比较大小
select substring("Hello World",2,3) from dual; -- 表示从2开始，截取3个字符
select ltrim(" Hello ") from dual; -- 去除左边空格
select rtrim(" Hello ") from dual; -- 去除右边空格
select trim(" Hello ") from dual -- 去除两边的空格

-- 以首字母小写返回ename
select concat(lcase(left(ename,1)),substring(ename,2)) from emp
```

# 11. 数学函数

![image-20220725185059263](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355647.png)

> 应用案例

```sql
select abs(-12) from dual; -- 绝对值
select least(10,2,3,4,5) from dual -- 返回最小值
select mod(10,3) from dual -- 取模

select ceiling(1.2) from dual -- 向上取整,得到比num大的最小整数,1.2->2
select floor(1.2) from dual -- 向下取整，得到比num小的最大整数,1.2->1
select format(1.24567,3) from dual -- 保留3位小数,四舍五入

select conv(6,10,2) from dual -- 表示把6从10进制转换为2进制
select bin(10) from dual; -- 十进制转换为二进制
select hex(10) from dual -- 转为16进制

select rand() from dual -- 返回随机数,0≤v≤1.0
select rand(3) from dual -- 给rand种子为3,那么只能随机一次，后面就固定了
```

# 12. 日期函数

![image-20220725190411627](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355686.png)

> 1.

![image-20220725190556273](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355763.png)

```sql
use zjh_db02;
create table person
(
	id int,
	birthday date
);
insert into person values(1,current_timestamp); -- 时间戳在实际的使用

select current_date from dual; -- 年月日
select current_time from dual; -- 时分秒
select current_timestamp from dual; -- 年月日，时分秒
```

> 2.

![image-20220725193038304](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355769.png)

下方为应用案例

![image-20220725191134784](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355807.png)

```sql
-- 1.显示所有留言信息，发布日期只显示日期，不用显示时间
select content,date(sendtime) from mes;
-- 2.请查询在5分钟内发布的帖子
select * from mes where DATE_ADD(sendtime,INTERVAL 5 MINUTE) >= now();
select * from mes where DATE_SUB(now(),INTERVAL 5 MINUTE) <= sendtime;
-- 3.请在mysq的sql语句中求出2011-11-11和1990-1-1相差多少天
select datediff('2011-11-11','1990-1-1') from dual
-- 4.请用mysql的sq语句求出你活了多少天
select datediff(current_date,'2001-11-28') from dual
-- 5.如果你能活80岁，求出你还能活多少天
select datediff(date_add('2001-11-18',InTERVAL 80 YEAR),current_date) from dual
```

> 3.

![image-20220725204505324](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355844.png)

```sql
select year(now()) from dual; -- 返回年,2022
select month('2001-11-11') from dual; -- 返回月,11
select day(now()) from dual; -- 返回天,25
select UNIX_TIMESTAMP() from dual; -- 返回的是19770-1-1到现在的秒数
-- 将unix的时间戳转换为年月日 时分秒
select FROM_UNIXTIME(UNIX_TIMESTAMP(),'%Y-%m-%d') from dual -- 转换为年月日
select FROM_UNIXTIME(UNIX_TIMESTAMP(),'%H:%i:%s') from dual -- 转换为时分秒
```

# 13. 系统函数

![image-20220725210238723](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355745.png)

```sql
select USER() from dual; -- 查看登录到mysql的用户和ip
select DATABASE() from dual -- 查看当前数据库的名称
```

# 14. 加密函数

![image-20220725210255130](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355774.png)

```sql
select MD5('zjh20011128') from dual -- 计算出32位的md5
create table person
(
	id int,
	name vachar(32),
	pwd char(32)
)
insert into person values(1,'张三',MD5('1234')),(2,'李四',MD5('9080')); -- 实际运用

-- mysql数据库默认使用这种方式来存储密码
select PASSWORD('zjh') from dual -- 另外一种加密方式
```

# 15. 流程控制函数

![image-20220725212353174](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355831.png)

```sql
-- 就是三元运算符，为true就返回第二个值，为false就返回第三个值
select if(true,'返回为真','返回为假') from dual;


-- 第一个值为空就返回第一个值，第一个值不为空就返回第二个值
select IFNULL('','这是空') from dual;

-- 当when后面的条件为true就是执行返回前面的，否则就返回后面的
select case
	when false
		then 'jack'
		else 'tom' end

-- 当第一个为true就返回jack，否则就执行后面的when，注意第一个when不能有else
select
	case
		when false then 'jack'
		when false then 'tom' else 'mary'
	end;
```

> 应用案例

![image-20220725214216261](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355876.png)

```sql
select ename,comm,IFNULL(comm,0.0) from emp;
-- 判断为null的时候，需要使用is null,而不是=
select ename,comm,if(comm is null,0.0,comm) from emp

select ename,job,
	case
		when job='CLERK' then '职员'
		when job='MANAGER' then '经理'
		when job='SALESMAN' then '销售人员'
		else job
	end as '翻译'
from emp;
```

# 16. 分页查询

```sql
-- 第一页
select * from emp order by empno
	limit 0,3; -- 表示从第1个数据开始，显示3行
-- 第二页
select * from emp order by empno
	limit 3,3; -- 表示从第4个数据开始，显示3行
-- 第三页
select * from emp order by empno
	limit 6,3;
```

# 17. 多表查询

假如我们在多表查询的时候不去限制条件的话，首先是从第一张表中取出一条数据和第二个表的每一行进行组合，所以我们在进行多表查询的时候

```sql
select * from emp,dept;
```

![image-20220726151537011](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355915.png)

![image-20220726114512891](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355953.png)

```sql
-- 显示雇员名，雇员工资及所在的部门的名字
select ename,sal,dname from emp,dept where emp.deptno=dept.deptno;
-- 显示部门号为10的部门号、员工名和工资
select dept.deptno,ename,sal from emp,dept where emp.deptno=dept.deptno and emp.deptno=10;
-- 显示各个员工的姓名，工资，及其工资的级别
select ename,sal,grade from emp,salgrade as g where sal between g.losal and g.hisal;
-- 显示雇员名，雇员工资及所在部门的名字，并按照部门降序
select ename,sal,dname from emp,dept where emp.deptno=dept.deptno order by dept.deptno desc;
```

# 18. 自连接

![image-20220726155801689](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355649.png)

`Smith`的编号是`7369`，它上级的编号是`7902`，那么就是`Ford`，也就是说上级并不在另外一个表中，而是在同一个表中

![image-20220726160239146](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355672.png)

所以这个时候遇到这种情况就需要使用`自连接`来处理，将一个表当作两个表，使用`表别名`来`区分`

```sql
select worker.ename,boss.ename from emp as worker,emp as boss where worker.mgr=boss.empno;
```

# 19. 子查询

![image-20220726162542087](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355693.png)

## 19.1 单行子查询

```sql
-- 显示与Smith同一个部门的所有员工
select * from emp where deptno=(
	-- 先查出SMITH的部门编号
	select deptno from emp where ename='SMITH'
)

-- EXISTS 的作用：子查询返回结果，条件成立，反之不成立
SELECT name FROM department
    WHERE EXISTS (
        SELECT * FROM employee WHERE department.id = employee.department_id
    );
-- NOT EXISTS 来查询所有没有员工的部门
SELECT name FROM department
    WHERE NOT EXISTS (
            SELECT * FROM employee WHERE department.id = employee.department_id
    );
```

## 19.2 多行子查询

```sql
-- 查看与10号部门岗位相同的其他部门的员工，但是查询的结果不能包含10号部门的员工
select ename,job,sal,deptno from emp where job in (
	select distinct job from emp where deptno=10
) and deptno<>10;
```

## 19.3 子查询临时表

```sql
-- 查看各类商品中价格最高的商品
-- temp是子查询的结果作为一个表来查询
select goods_id,temp.cat_id,goods_name,shop_price from ecs_goods,(
	select cat_id,max(shop_price) as max from ecs_goods group by cat_id
) as temp where temp.cat_id=ecs_goods.cat_id and temp.max = ecs_goods.shop_price;
```

整个表大概长这样

![image-20220726175202264](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355726.png)

```sql
-- 查询每个部门工资高于本部门平均工资的人的资料
select * from emp,(
	select deptno,avg(sal) as avg_sal from emp group by deptno
) as temp
where temp.deptno=emp.deptno and emp.sal>temp.avg_sal
order by emp.deptno desc;
-- 查找每个部门工资最高的人
select * from emp,(
	select deptno,max(sal) as max_sal from emp group by deptno
) as temp
where temp.deptno=emp.deptno and emp.sal=temp.max_sal
order by emp.deptno desc;
-- 先查询每个部门的信息和人员数量
select dept.*,c as '人数' from dept,(
	select deptno,count(*) as c from emp group by deptno
) as temp where temp.deptno=dept.deptno;
```

## 19.4 any 和 all

![image-20220726175912221](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355816.png)

`all`表示所有，就按照下面的`sql`来写，就是说`select sal from emp where deptno=30`查询到 30 号部门所有的员工，`sal>all(...)`就是说薪水要大于所有的结果

```sql
select ename,sal,deptno from emp where sal > all(
	select sal from emp where deptno=30
);
-- 或者可以这样写
select ename,sal,deptno from emp where sal > all(
	select max(sal) from emp where deptno=30
);
```

![image-20220726180432963](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355851.png)

`any`表示任意，所以结果就是比 30 号任意一个工资高，那么就是比 30 号最低工资高

```sql
select ename,sal,deptno from emp where sal > any(
	select sal from emp where deptno=30
);
-- 或者可以这样写
select ename,sal,deptno from emp where sal > all(
	select min(sal) from emp where deptno=30
);
```

## 19.3 多列子查询

![image-20220726180712458](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355406.png)

![image-20220726180803730](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355426.png)

```sql
-- 这里的(job,deptno)=(...),就是一一对应来查询的，因为子查询返回的结果就是(job,deptno)
select * from emp where (job,deptno) = (
	select job,deptno from emp where ename='ALLEN'
) and ename <> 'ALLEN';
```

# 20. 表复制和去重

![image-20220726185348015](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355447.png)

```sql
create table emp_copy -- 创建表
(
	id int,
	`name` varchar(32),
	sal double,
	job varchar(32),
	deptno int
);
insert into emp_copy(id,`name`,sal,job,deptno) select empno,ename,sal,job,deptno from emp; -- 讲筛选出来的数据传输给emp_copy

insert into emp_copy select * from emp_copy -- 自我复制，这个是几何倍数增加，一直*2
create table emp_copy1 like emp; -- 将emp表结构复制到semp_copy1

-- 去重emp_copy，因为我们执行了2遍自我复制，肯定有重复的值，所以我们需要去重
-- 就是将一个使用insert into emp_copy2 select distinct * from emp_copy将去重的数据取出，然后移入你想要去重的表就可以了
```

# 21. 合并查询

![image-20220726204753989](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355494.png)

```sql
-- union 和 union all 就是将查询的数据拼在一起
-- union all 不会对记录进行去重
select * from emp where sal>2500 union all select * from emp where job="MANAGER";
-- union 会对记录进行去重操作
select * from emp where sal>2500 union select * from emp where job="MANAGER";
```

# 22. 外连接

![image-20220726205845337](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355544.png)

```sql
-- 使用左外连接，显示所有人的成绩，如果没有成绩就显示为空，但是依然显示这个人
-- 左外连接，表示左边的表完全显示，即便右边的表没有对应的数据
select student.id,`name`,grade from student left join exam on student.id=exam.id;

-- 右外连接，显示所有成绩，如果没有名字匹配就为null
-- 和左外连接是一样的，右边的表显示完全，没有匹配的就为null
select student.id,`name`,grade from student right join exam on student.id=exam.id;

-- 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门名
select dname,ename,job from dept left join emp on emp.deptno=dept.deptno;
```

这个主要是为了多表之间的连接，有下面的几种查询方式

![image-20220907163310838](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355388.png)

> 左连接

左连接就是以`products`表为基础，会全部显示。右边的`brand`表会加在`products`后面，假如`products`没有对应的数据话，就会显示为`null`

![image-20220907211603755](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355409.png)

> 右连接

右连接就是`左连接`相反的，以`brand`为基础

![image-20220907212238163](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355439.png)

> 内连接

这个就是挑选共同的地方，就和`select * from product,brand where product.brand_id = brand.id`显示的结果是一样的，但是`select ...`是将所有的信息都查询出来，然后再将不符合条件的过滤掉。假如你使用的内连接的话，就先过滤不符合条件的数据，然后再连接表。理论上，内连接的方式比`select...`的效率高

![](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355464.png)

> 全连接

![image-20220907214920298](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355493.png)

# 23. 约束

![image-20220726212148569](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355568.png)

## 23.1 主键

![image-20220726212227298](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355420.png)

```sql
create table t1
(
	id int primary key,
	`name` varchar(32),
	email varchar(32)
)
insert into t1 values(1,'jack','123@qq.com');
insert into t1 values(2,'Tom','234@qq.com');
insert into t1 values(2,'xxx','567@qq.com'); -- 报错，因为主键不能重复
```

> 使用细节

1.`primary key`不能重复而且不能为`null`

```sql
insert into t1 values(null,'zjh','234@13.com') -- 主键自带not null，不能为空
```

2.一张表最多只能有一个`主键`，但可以是`复合主键`

```sql
-- 错误的
create table t1
(
	id int primary key,
	`name` varchar(32) primary key,
	email varchar(32)
)

-- 使用复合主键
-- 你设置了复合主键的字段，也就是说要id和name都相同才不满足，如果只是id相同，name不同是不受影响的
create table t1
(
	id int,
	`name` varchar(32),
	email varchar(32)
    primary key(id,'name')
)
insert into t1 values(1,'jack','123@qq.com');
insert into t1 values(1,'Tom','234@qq.com'); -- 正确，因为name不同
insert into t1 values(1,'Tom','567@qq.com'); -- 报错，因为id和name都相同
```

3.主键的指定方式有两种

```sql
-- 直接在字段名后指定：字段名 primakry key
create table t1
(
	`name` varchar(32) primary key,
)

-- 在表定义最后写 primary key(列名)：
create table t1
(
	`name` varchar(32),
    primary key(`name`)
)
```

4.使用`desc`表名，可以看到`primary key`的情况

```sql
desc t1
```

![image-20220726213733388](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355440.png)

## 23.2 unique

![image-20220726213855925](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355456.png)

假如你使用`unique not null`的话，那么效果其实就像是`primary key`

## 23.3 外键

![image-20220726233333124](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355485.png)

大致的示意图，也就是使用外键约束之后的效果图，而且主表必须具有`主键约束`或者`unique约束`，因为`从表`的外键必须链接的字段必须是`唯一`的

![image-20220728104553776](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355514.png)

```sql
create table class
(
	id int primary key,
	`name` varchar(32),
	`add` varchar(32)
);
create table student
(
	id int primary key,
	`name` varchar(32),
	class_id int,
	foreign key (class_id) references class(id) -- 指定的外键关系
);
-- 先创建主表class,然后再取创建从表，并且student的class_id要再主表存在
insert into class values(1,'java','上海'),(2,'php','广州');
insert into student values(101,'张三',1),(102,'李四',2);
```

> 使用细节

1.外键指向的表的字段，要求是`primary key`或者是`unique`

2.表的类型是`innodb`，这样的表才支持外键

3.外键字段的类型要和主键字段的类型**一致**（长度可以不同）

4.外键字段的值，必须在主键字段中**出现过**或者为**null**，前提是外键字段允许为**null**

5.一旦建立主外键的关系，数据不能随意删除了；假如要删除主表的数据，必须要把所有链接到主表的的从表的数据先删除掉，然后才能删除主表的数据

在上文我提到，**假如建立的外键关系，数据不能随意删除**。我们在创建外键的时候是可以修改外键的关联关系。假如我们默认创建的话，就是`Restrict`，该模式下更新和删除某个外键关联的记录就会报错

![image-20220907193410418](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355541.png)

我们就可以按照下面的形式来修改外键的关联属性

```sql
create table student
(
	id int primary key,
	`name` varchar(32),
	class_id int,
    -- 我们使用on update或者on delete的形式来设置
	foreign key (class_id) references class(id) on update cascade on delete set null
);
```

我们设置了`on update`的值为`cascade`，`on delete`的值为`set null`。我们将写了`foreign...`的定为主表的话，那么我们只能更新于主表关联的从表

```sql
update class set id = 3 where id = 1
```

假如我们继续删除操作，假如你操作从表的数据，主表的数据中`class_id`的值就会设置为`null`

```sql
delete from class where id = 1
```

下面就是外键可以设置的值

![image-20220907192238190](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355369.png)

假如不是很理解上面的解释的话，可以理解一个表

![image-20220916224750977](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355392.png)

`buildings`这个表是主表，`rooms`表是依附于`buildings`表的，并且`building_no`作为`rooms`的外键，假如外面需要删除`buildings`表中的数据，所以`rooms`中与`buildings`关联的也需要删除，这个就是`cascade`的效果

参考资料：[MySQL on delete cascade 语句 - MySQL 教程 (yiibai.com)](https://www.yiibai.com/mysql/on-delete-cascade.html)

## 23.4 check

![image-20220728110515059](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355416.png)

```sql
create table t2
(
	id int primary key,
	`name` varchar(32),
	sex varchar(6) check (sex in ('man','woman')),
	sal double check (sal>1000 and sal<2000)
)
-- 我使用的mysql版本是8.0所以可以使用check的校验
insert into t2 values(1,'张三','man',1900); -- 可以添加
insert into t2 values(2,'李四','mid',9000); -- 不通过
```

> 应用案例

![image-20220728111111184](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355447.png)

```sql
create database shop_db;
use shop_db;
create table goods
(
	goods_id int primary key,
	goods_name varchar(64) not null,
	unitprice decimal(10,2) check (unitprice=>1.0 and unitprice<=9999.99),
	category varchar(32) not null,
	provider varchar(32) not null
);
create table customer
(
	customer_id int primary key,
	`name` varchar(32) not null,
	address double not null,
	email varchar(32) unique,
	sex varchar(32) check (sex in ('男','女')),
	card_id long not null
)
create table purchase
(
	order_id int primary key,
	customer_id int not null,
	goods_id int not null,
	nums int unique,
	foreign key (customer_id) references customer(customer_id),
	foreign key (goods_id) references goods(goods_id)
)
```

## 23.5 自增长

![image-20220728114427385](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355474.png)

```sql
create table t3
(
	id int primary key auto_increment, -- 添加自增长
	`name` varchar(32),
	address varchar(32)
)
insert into t3 values(null,'张三','上海');
insert into t3(name) values('李四');
insert into t3(`name`,address) values('王五','北京');
```

> 使用细节

1.一般来说`自增长`是和`primary key`配合使用的

2.自增长也可以`单独使用`，但是需要配合一个`unique`

3 自增长修饰的字段为`整数型`的（虽然小数也可以但是非常非常少这样使用)

4.自增长默认从`1`开始，你也可以通过如下命令修改

```sql
alter table t3 auto_increment=10; -- 修改默认自增长的初始值
```

5.如果你添加数据时，给`自增长`字段（列指定的有值，则以指定的值为准）

# 24. 索引

## 24.1 基础介绍

![image-20220728115620460](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355505.png)

假如我们执行下面得代码，会存入大概 800000 份数据，这个时候数据量会很大

```sql
CREATE TABLE dept( /*部门表*/
deptno MEDIUMINT   UNSIGNED  NOT NULL  DEFAULT 0,
dname VARCHAR(20)  NOT NULL  DEFAULT "",
loc VARCHAR(13) NOT NULL DEFAULT ""
) ;

#创建表EMP雇员
CREATE TABLE emp
(empno  MEDIUMINT UNSIGNED  NOT NULL  DEFAULT 0, /*编号*/
ename VARCHAR(20) NOT NULL DEFAULT "", /*名字*/
job VARCHAR(9) NOT NULL DEFAULT "",/*工作*/
mgr MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,/*上级编号*/
hiredate DATE NOT NULL,/*入职时间*/
sal DECIMAL(7,2)  NOT NULL,/*薪水*/
comm DECIMAL(7,2) NOT NULL,/*红利*/
deptno MEDIUMINT UNSIGNED NOT NULL DEFAULT 0 /*部门编号*/
) ;

#工资级别表
CREATE TABLE salgrade
(
grade MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,
losal DECIMAL(17,2)  NOT NULL,
hisal DECIMAL(17,2)  NOT NULL
);

#测试数据
INSERT INTO salgrade VALUES (1,700,1200);
INSERT INTO salgrade VALUES (2,1201,1400);
INSERT INTO salgrade VALUES (3,1401,2000);
INSERT INTO salgrade VALUES (4,2001,3000);
INSERT INTO salgrade VALUES (5,3001,9999);

SET GLOBAL log_bin_trust_function_creators = 1; -- 假如执行不了下面得脚本，就执行这调语句

delimiter $$
#创建一个函数，名字 rand_string，可以随机返回我指定的个数字符串
create function rand_string(n INT)
returns varchar(255) #该函数会返回一个字符串
begin
#定义了一个变量 chars_str， 类型  varchar(100)
#默认给 chars_str 初始值   'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
 declare chars_str varchar(100) default
   'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ';
 declare return_str varchar(255) default '';
 declare i int default 0;
 while i < n do
    # concat 函数 : 连接函数mysql函数
   set return_str =concat(return_str,substring(chars_str,floor(1+rand()*52),1));
   set i = i + 1;
   end while;
  return return_str;
  end $$
#这里我们又自定了一个函数,返回一个随机的部门号
create function rand_num( )
returns int(5)
begin
declare i int default 0;
set i = floor(10+rand()*500);
return i;
end $$
#创建一个存储过程， 可以添加雇员
create procedure insert_emp(in start int(10),in max_num int(10))
begin
declare i int default 0;
#set autocommit =0 把autocommit设置成0
 #autocommit = 0 含义: 不要自动提交
 set autocommit = 0; #默认不提交sql语句
 repeat
 set i = i + 1;
 #通过前面写的函数随机产生字符串和部门编号，然后加入到emp表
 insert into emp values ((start+i) ,rand_string(6),'SALESMAN',0001,curdate(),2000,400,rand_num());
  until i = max_num
 end repeat;
 #commit整体提交所有sql语句，提高效率
   commit;
end $$

#添加8000000数据
call insert_emp(100001,8000000)$$

#命令结束符，再重新设置为;
delimiter ;
```

这个时候我们可以使用下面得方式来获取数据库中数据存储得位置

```sql
show global variables like "%datadir%";
```

![image-20220729102709376](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355315.png)

我们可以看到`emp.ibd`有`500mb`，数据量很大

![image-20220729102752308](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355332.png)

我们使用这条语句，你会发现查询得时间很长

```sql
select count(*) from emp;
```

假如说我们建立索引的话，就会添加`empno`添加索引，相应得内存也会增加

```sql
create index empno_index on emp(empno);
```

![image-20220729103302514](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355357.png)

我们查询建立了索引得字段`empno`得情况下，查询速度会非常块

```sql
select * from emp where empno=200000; -- 0.006s
```

假如我们不按照索引字段来查询得话，你会发现时间长了很多；也就是说空间换时间，建立了索引得字段查询速度会很快，假如不建立索引查询速度就很慢，但是这也是针对大量数据得情况下，假如是数据量不大得话，就不用处理

```sql
select * from emp where ename="xlLZNP"; -- 6.431s
```

> 索引原理

其实索引的本质就是将表改为二叉树，这样检索的速度会变得非常快

![image-20220729183414503](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355381.png)

> 索引的代价

1.磁盘占用大

2.对**update delete insert**语句效率影响大

> 索引使用情况

![image-20220729212448906](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355418.png)

## 24.2 创建索引

> 索引类型

假如你在创建字段之后，为这个字段设置了`Primary Key`和`Unique`，数据库就默认为他们建立索引，使用这些字段来查询默认是最快的

![image-20220729184418575](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355506.png)

```sql
create table t4
(
	id int,
	`name` varchar(32)
)
create unique index id_index on t4(id); -- 添加唯一索引
create index name_index on t4(`name`); -- 添加普通索引1
alter table t4 add index id_index(id); -- 添加普通索引2

-- 添加主键索引，你设置的主键字段就默认是主键索引
create table t5
(
	id int primary key
)
-- 假如是后续添加主键索引,也就是添加主键
alter table t5 add primary key (id)
```

> 应用案例

![image-20220729211903142](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355301.png)

## 24.3 查询索引

我们还可以使用`show`来查询这个表索引的情况，可以看到`Non_unique`字段，`0`表示是唯一索引，`1`表示不是唯一索引，因为是`Non`，所以双重否定表示肯定

```sql
show indexes from t4;
show index from t4;
show keys from t4;
-- desc只能看到这个字段有索引
desc t4;
```

![image-20220729211116744](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355421.png)

## 24.3 删除索引

```sql
drop index id_index on t4; -- 删除普通索引
alter tables t4 drop primary key; -- 删除主键索引
```

# 25. 事务

## 25.1 基本介绍

事务用于保证数据的一致性，它由一组相关的 dml 语句组成，该组的 dml 语句要么全部成功，要么全部失败。如：转账就要用事务来处理，用以保证数据的**一致性**。

![image-20220729213324856](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355490.png)

但是事务不仅仅是执行一堆`dml`语句，下面还有事务和锁的问题

![image-20220729220053244](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355537.png)

我们还可以开启事务来进行回滚的操作，这样就可以回到执行错误`sql`语句之前，来改正错误

![image-20220729214120890](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355580.png)

## 25.2 基本操作

![image-20220729220046429](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355673.png)

```sql
create table t5
(
	id int,
	`name` varchar(32)
)

-- 开启事务
start transaction;
-- 设置保存点a
savepoint a;
-- 执行dml语句
insert into t5 values(1,'张三');
select * from t5;

-- 设置保存点b
savepoint b;
-- 执行dml语句
insert into t5 values(2,'李四');
select * from t5;

rollback to b; -- 回退到b,相当于没添加记录点b后面的语句
rollback to a; -- 回退到a
rollback; -- 回退所有的事务
commit; -- 会提交，保存点会删除，不能回退了

select * from t5;
```

![image-20220729220212319](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355936.png)

## 25.3 使用细节

1.如果不开始事务，默认情况下，dml 操作是自动提交的，不能回滚

2.如果开始一个事务，你没有创建保存点.你可以执行 rollback,默认就是回退到你事务开始的状态

3.你也可以在这个事务中（还没有提交时），创建多个保存点

4.你可以在事务没有提交前，选择回退到哪个保存点.

5.mysql 的事务机制需要`innodb`的存储引擎还可以使用，`myisam`不好使.

6.开始一个事务`start transaction`或`set autocommit=off`

## 25.4 隔离级别

首先要解决为什么需要**隔离级别**这个东西？可以设想一个场景，**程序 A**和**程序 B**都在操作数据库，同时数据库开启了事务，但是我们可以回想一下**数据库的事务**是什么，是不是就是**保存记录点**，可以**回到记录点**。这个时候程序 A 去操作数据库，程序 B 又在查询数据库，这个时候数据库 B 返回的结果就不是开启事务的那个节点的数据库了，而是程序 A 修改之后的数据库，这肯定和事务的设计是违背的，所以就有了隔离级别

![image-20220730122315039](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355597.png)

下面是不考虑隔离性之后会出现下面的 3 个问题

![image-20220729221205476](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355617.png)

![image-20220729225702893](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355638.png)

## 25.5 隔离演示

![image-20220730105342193](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355671.png)

此时我们打开了 2 个数据库同时操作，相当于演示同时操作的情况

![image-20220730105948351](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355704.png)

```sql
select @@transaction_isolation; -- 查看该数据库的隔离级别
```

![image-20220730105904914](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355504.png)

> Read-uncommited

这个时候我们给一个数据设置隔离级别为`read uncommitted`，我们查询隔离级别表可以知道这种隔离级别，会导致**脏读、不可重复读、幻读**

```sql
set session transaction isolation level read uncommitted; -- 设置隔离级别为read uncommitted
```

并且要注意一个点，就是任何隔离级别的前提是**开启了事务**，你不开启事务都是没用的

我们同时开启事务，一个表的隔离级别是`read-uncommitted`，一个是`repeatable-read`

![image-20220730110634270](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355525.png)

先演示脏读的情况（隔离级别是`read-uncommitted`）

同时开启了事务，但是左边数据库插入了数据，但是并没有提交。右边的数据库接收到了，还能正常显示，这就是**脏读**，但是为什么不能出现这种情况呢？这是因为**数据库 B**开启了**事务**，肯定是想要进行自己的操作，假如**数据库 A**一直在对表进行操作，那么**数据库 B**的数据就会出现不必要的数据

![image-20220730111134912](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355546.png)

我们再来看**不可重复读**，在提交之前我们对数据库中的数据进行**修改**，但是并**没有提交**，但是**数据库 B**可以看到数据的改变

![image-20220730111905043](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355573.png)

再来看**幻读**，在我们提交之后可以看到插入数据中数据的变化

![image-20220730112328058](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355629.png)

这里我们就总结为**脏读和不可重复读**就是未提交，但是可以看到数据库的变化；**幻读**就是已经提交，也可以看到数据库的变化

> Read-commited

我们将隔离级别调整为`read commited`，我们插入数据，但是没有提交，对面是看不到。其实这就是想要的效果，因为数据库 B 开启了事务本质就是想处理开启事务的一瞬间这些表的数据，其他的人的修改操作对他没有任何影响

![image-20220730113155020](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355661.png)

假如我们提交之后，所有数据就可以看的到了

> repeatable-read

我们再来看权限设置为`repeatable read`，我们可以看到插入的效果是看不到的

![image-20220730113827675](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355453.png)

并且提交之后依旧看不到任何变化

![image-20220730114639178](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355478.png)

> Serializable

我们将权限设置为`Serializable`，也就是串行化，这样只能同时操作一个表。我们可以看到下面的`select * from temp`，是不执行的

![image-20220730120135183](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355509.png)

过一段时间另一个正在操作的数据库不**提交**的话，就会一直**阻塞**在这里，直到出现**超时**

![image-20220730130753741](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355547.png)

## 25.6 设置隔离

下面的方式在前面都有显示

![image-20220730135825196](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355583.png)

我们也可以全局修改

![image-20220730140111059](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355735.png)

![image-20220730140136785](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355081.png)

## 25.7 隔离特性

![image-20220730140300105](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355104.png)

# 26. 存储引擎

![image-20220730153238064](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355190.png)

我们可以查看当前数据库支持那些`存储引擎`

```sql
show engines;
```

![image-20220730153628642](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355488.png)

> 主要存储引擎特点

![image-20220730154204040](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355539.png)

![image-20220730154041312](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355012.png)

> 存储引擎演示

```sql
show engines; -- 显示引擎

-- 创建的myisam引擎的数据库
create table t1
(
	id int,
	`name` varchar(32)
) engine myisam;
-- 1.添加速度快 2.不支持外键和事务 3.支持表级锁

-- 创建的myisam引擎的数据库
create table t2
(
	id int,
	`name` varchar(32)
) engine memory;
-- 1.数据存储在内存 2.执行速度快 3.默认支持索引(hash)
-- 退出数据库之后，表结构都在，但是数据不见了

-- 语法为alter table `表名` engine=存储引擎;
alter table t1 engine=inndb -- 修改存储引擎
```

# 27 视图

引出需求

![image-20220730155937216](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355038.png)

说白了就是为了让一些人不能查看表的全部数据，就会出现**视图**，将表的一部分不敏感的数据摘出来让你查看和修改，这也是权限管理的一部分

![image-20220730160656280](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355068.png)

> 基本使用

![image-20220730160930129](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355113.png)

```sql
create view emp_view1 as select empno,ename,job,deptno from emp; -- 创建视图
desc emp_view1; -- 查看视图的结构
alter view emp_view01 as select empno from emp; -- 更新视图
show create view emp_view01; -- 查看创建视图的指令
drop view emp_view01; -- 删除视图
```

> 使用细节

![image-20220730161350799](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355280.png)

> 最佳实践

![image-20220730162127512](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355428.png)

> 应用案例

![image-20220730162425366](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355500.png)

# 28. mysql 管理

## 28.1 用户管理

![image-20220730163517616](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355526.png)

为什么需要 Mysql 用户的管理?因为当我们做项目开发时，可以根据不同的开发人员，赋给他相应的 Mysql 操作权限，所以，Mysql 数据库管理人员(root), 根据需要创建不同的用户，赋给相应的权限，供人员使用

```sql
-- 1. 创建新的用户
-- 解读 (1) 'hsp_edu'@'localhost' 表示用户的完整信息 'hsp_edu' 用户名 'localhost' 登录的IP
-- (2) 123456 密码, 但是注意 存放到 mysql.user表时，是password('123456') 加密后的密码
--     *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9
CREATE USER 'hsp_edu'@'localhost' IDENTIFIED BY '123456'

-- 查询用户
SELECT `host`, `user`, authentication_string  -- 这里是查看主机，用户名，加密后的密码
	FROM mysql.user

-- 2. 删除用户
DROP USER 'hsp_edu'@'localhost'

-- 3. 登录

SET PASSWORD = PASSWORD('123456') -- 修改自己的密码
-- root 用户修改 hsp_edu@localhost 密码, 是可以成功.
SET PASSWORD FOR 'hsp_edu'@'localhost' = PASSWORD('123456') -- 修改别人的密码
alter user 'zjh'@'localhost' identified by 'abc'; -- 新版本使用这个方式来修改
```

我们设置了权限之后，该用户所能操作的和看到的和 root 用户是不一样的

![image-20220731115334864](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355559.png)

## 28.2 权限管理

![image-20220731115930733](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355593.png)

下面是用户权限操作基本语法

![image-20220731120337682](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355628.png)

```sql
-- 有用户得情况下
-- 将select,delete得操作权限给在localhost登录得zjh用户，并且只能操作zjh_db02库下得emp表
grant select,delete on zjh_db02.emp to 'zjh'@'localhost'
grant select,delete on zjh_db02.emp to 'zjh'@'localhost' identified by '123' -- 将密码修改为123

-- 没有这个用户得情况下,创建这个用户，并且赋予权限
grant select,delete on zjh_db02.emp to 'zjhhh'@'localhost' identified by '123'

-- 假如使用*.*得操作，就是指定所有数据库下得所有表
grant select,delete on *.* to 'zjh'@'localhost'
-- 这个就表示zjh_db02下得所有表
grant select,delete on zjh_db02.* to 'zjh'@'localhost'
```

假如权限生效之后也可以回收权限

![image-20220731121137589](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355660.png)

> 应用案例

![image-20220731121650198](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355748.png)

```sql
-- root
-- 1.创建用户
create user 'zjh'@'localhost' identified by '123456';
-- 2.创建库和表
create table person
(
	id int,
	`name` varchar(32)
)
-- 3.给用户赋予权限
grant select,insert on *.* to 'zjh'@'localhost';
-- 4.修改密码
alter user 'zjh'@'localhost' identified by 'abc'; -- 注意新老版本的问题
-- 5.删除用户
drop user 'zjh'@'localhost'
-- 6.收回权限
revoke select,insert on *.* from 'zjh'@'localhost'; -- 收回zjh用户的select和insert权限
revoke all on zjh_db04.person from 'zjh'@'localhost';  -- all就是收回所有的权限

-- zjh
select * from person;
insert into person values(1,'张三');
delete from person where id=1; -- 提示错误，没有权限
```

## 28.3 权限细节

1.在创建用户的时候，如果不指定 Host，则为%，%表示表示所有 IP 都有连接权限，默认就可以远程登录

```sql
create user 'zjh' identified by '123456';
```

2.你也可以这样来指定登录 mysql

```sql
create user'xx'@'192.168.1.%' -- 表示192.168.1开头的ip地址都可以使用
```

3.在删除用户的时候，如果 host 不是%，需要明确指定"用户'@'host 值

```sql
drop user 'zjh' -- 默认就是drop user 'zhj'@'%'
drop user 'zjh'@'12.168.1.%'
```

# 29. 多对多处理

多对多的解决方法就是建立一个中间表来处理

![image-20220907220805884](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355773.png)

下面为`sql`的创建方式

```sql
create table if not exists `students`
(
	id int primary key auto_increment,
	`name` varchar(20) not null,
	age int
)
create table if not exists `courses`
(
	id int primary key auto_increment,
	`name` varchar(20) not null,
	price double not null
)
INSERT INTO `students` (name, age) VALUES('why', 18);
INSERT INTO `students` (name, age) VALUES('tom', 22);
INSERT INTO `students` (name, age) VALUES('lilei', 25);
INSERT INTO `students` (name, age) VALUES('lucy', 16);
INSERT INTO `students` (name, age) VALUES('lily', 20);
INSERT INTO `courses` (name, price) VALUES ('英语', 100);
INSERT INTO `courses` (name, price) VALUES ('语文', 666);
INSERT INTO `courses` (name, price) VALUES ('数学', 888);
INSERT INTO `courses` (name, price) VALUES ('历史', 80);



create table if not exists `students_select_courses`
(
	id int primary key auto_increment,
	student_id int not null,
	course_id int not null,
	foreign key (student_id) REFERENCES students(id) on UPDATE CASCADE,
	foreign key (course_id) REFERENCES courses(id) on UPDATE CASCADE
)

# why 选修了 英文和数学
INSERT INTO `students_select_courses` (student_id, course_id) VALUES (1, 1);
INSERT INTO `students_select_courses` (student_id, course_id) VALUES (1, 3);
# lilei选修了 语文和数学和历史
INSERT INTO `students_select_courses` (student_id, course_id) VALUES (3, 2);
INSERT INTO `students_select_courses` (student_id, course_id) VALUES (3, 3);
INSERT INTO `students_select_courses` (student_id, course_id) VALUES (3, 4);
```

下面是面对这种表关系的基础查询语句的思路

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355793.png" alt="image-20220907221651251" style="zoom:80%;" />

下面为实现的`sql`语句

```sql
# 查询所有的学生选择的所有课程
select s.id,s.name,s.age,ssc.student_id,ssc.course_id,c.name from students s
	join students_select_courses ssc on s.id = ssc.student_id -- 先进行第一波的查询
	-- 查询之后的结果再进行内连接查询
	join courses c on c.id = ssc.course_id
```

![image-20220907222227549](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355825.png)

```sql
# 查询所有的学生选课情况
select s.id,s.name,s.age,ssc.student_id,ssc.course_id,c.name from students s
	left join students_select_courses ssc on s.id = ssc.student_id
	left join courses c on c.id = ssc.course_id
```

![image-20220907223244961](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355839.png)

```sql
# why同学选择了哪些课程
# 这里使用内连接也可以，左连接都可以
select s.id,s.name,s.age,ssc.student_id,ssc.course_id from students s
	left join students_select_courses ssc on s.id = ssc.student_id
	left join courses c on c.id = ssc.course_id
	where s.id = 1
```

![image-20220907223649418](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355871.png)

```sql
# lily同学选择了哪些课程
select s.id,s.name,s.age,ssc.student_id,ssc.course_id from students s
	left join students_select_courses ssc on s.id = ssc.student_id
	left join courses c on c.id = ssc.course_id
	where s.id = 5
```

![image-20220907223749110](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355532.png)

```sql
# 哪些学生是没有选课的
select s.id,s.name,s.age,ssc.student_id,ssc.course_id from students s
	left join students_select_courses ssc on s.id = ssc.student_id
	left join courses c on c.id = ssc.course_id
	where ssc.course_id is null
```

![image-20220907223951521](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355550.png)

```sql
# 查询哪些课程没有被学生选择 - 其实使用这种方式也可以查询出来
select * from courses c
	left join students_select_courses ssc on c.id = ssc.student_id
	where ssc.student_id is null
```

![image-20220907224559696](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355567.png)

# 30. 转化为对象和数组

你在查询的时候会出现一个问题，我们查询到的数据都是一条一条的，但是返回到前端的数据都是`对象`或者`数组`。所以我们需要在`mysql`中进行查询，将其转化为对象或数组的形式

![image-20220908091705837](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355590.png)

可以使用下面的`JSON_OBJECT`函数来进行创建，第一个参数为`key`，第二个参数为`value`。依次循环

![image-20220908094028299](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355630.png)

我们在将刚刚的数据转化为数组，这里必须要使用`group by`来进行了分组，这个在`navicat`是可以正常查询，但是在`Node.js`中的`mysql2`中就会报错

![image-20220908094428191](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355671.png)

# 31. 函数/存储过程

文章参考：[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7237503560735260732)

因为数据库大部分只做存储功能，最好不要将业务逻辑写进去，这里只做了解即可

# 29. mysql 练习

## 29.1 练习 1 P811

答案：D，B，C

![image-20220731140917180](https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032355267.png)

## 29.2 练习 2 P812
