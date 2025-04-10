新版教程：[尚硅谷丨 2022 版 JavaWeb 教程(全新技术栈,全程实战)\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1AS4y177xJ?p=2&vd_source=2d46cc0fa105788201e3e43d9c83f528)

老版教程[002.尚硅谷*HTML 和 CSS-BS 软件的结构*哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Y7411K7zz/?p=2&spm_id_from=pageDriver&vd_source=2d46cc0fa105788201e3e43d9c83f528)

笔记：[JavaWeb 教程目录 | 代码重工 (gitee.io)](https://heavy_code_industry.gitee.io/code_heavy_industry/pro001-javaweb/lecture/)

# 配置操作

P32 0:00 - 3:50 如何在本项目中复制项目之后，能继续使用这个复制的项目

# 1. 前端网页

可以参考我以前的 HTML + CSS + JavaScript 笔记

# 2. XML

## 2.1 简单介绍

XML 是可扩展语言。主要用于保存数据，并且这些数据有自我描述性；并且该文件可以作为项目的配置文件

```xml
Student{
	id:1,
	name:张三
}

// 假如我们.xml文件就是这样的
<Students>
	<Student>
    	<id>1</id>
        <name>张三</name>
    </Student>
    <Student>
    	<id>2</id>
        <name>李四</name>
    </Student>
</Students>
```

## 2.2 基础语法

下面就是 XML 文件解析

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!--
	version 表示xml文件的版本
	encoding 表示xml文件本身的编码
-->
<books> <!-- books表示多个图书信息 -->
	<book sn="SN123456789"> <!-- book表示图片信息，sn表示图书序列号 -->
    	<name>时间简史</name> <!-- name表示标签书名 -->
        <author>霍金</author> <!-- auther表示作者 -->
        <price>90</price> <!-- price表示价格 -->
    </book>
    <book sn="SN123456700"> <!-- book表示图片信息，sn表示图书序列号 -->
    	<name>时间简史</name> <!-- name表示标签书名 -->
        <author>霍金</author> <!-- auther表示作者 -->
        <price>90</price> <!-- price表示价格 -->
    </book>
</books>
```

当然 xml 文件也可以使用单标签，并且数据必需要使用引号

```xml
<books>
	<book sn="SN123456789" name="时间简史" auther="霍金" price="90" />
</books>
```

当然 XML 文件还有根标记的机制，根标签只能使用一次

```xml
// 其中books标签是根元素，只能出现一次
<books> <!-- books表示多个图书信息 -->
	<book sn="SN123456789"> <!-- book表示图片信息，sn表示图书序列号 -->
    	<name>时间简史</name> <!-- name表示标签书名 -->
        <author>霍金</author> <!-- auther表示作者 -->
        <price>90</price> <!-- price表示价格 -->
    </book>
    <book sn="SN123456700"> <!-- book表示图片信息，sn表示图书序列号 -->
    	<name>时间简史</name> <!-- name表示标签书名 -->
        <author>霍金</author> <!-- auther表示作者 -->
        <price>90</price> <!-- price表示价格 -->
    </book>
</books>

// 这个就会报错
<books></books>
```

我们可以使用`<![CDATA[]]>`来写纯文本标签

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<books>
    <![CDATA[
        这是一个纯文本，不会进行XML文本解析
    ]]>
</books>
```

## 2.3 语法规范

XML 元素必须遵循以下命名规则：

1.名称可以含字母、数字以及其他的字符

2.名称不能以数字或者标点符号开始

3.名称不能以字符“xml”(或者 XML、Xml)开始

4.名称不能包含空格

5.可使用任何名称，没有保留的字词。

## 2.4 XML 解析

其中不管是`HTML`还是`XML`文件都是标记型文档，都可以使用 w3c 组织指定的`DOM`技术来解决

![[00 assets/006af87c5b521451ac8a2b67051acc69_MD5.png]]

我们一般可以使用`dom4j`来解析`XML`文件，但是这种方式已经过时了，所以这里就不去介绍

# 3. Web

## 3.1 CS 和 BS 的差异

**CS**：客户端服务器架构模式

充分利用客户端机器的资源，减轻服务器的负载，一部分安全要求的计算任务存储任务放在客户端执行，不需要将所有计算和存储都在服务器端执行。

**BS**：浏览器服务器架构模式

客户端不需要安装，维护成本低

## 3.2 Tomcat

### 2.2.1 基本介绍

这里我们需要准备`Tomcat`的软件，本质 Tomcat 也是使用 Java 来编写

![image-20220710103854663](image-20220710103854663.png)

```
bin  		//表示可执行文件
conf		//配置文件
lib			//依赖包
logs		//日志文件
temp		//临时文件
webapps		//部署空间
work		//工作目录
```

🎉 注意：假如不能运行记得配置 Java 环境

其实 Tomcat 就像一个 web 容器，我们将网页丢进去，然后进行访问

![[00 assets/799507119ff6b41a3f396435fba0a743_MD5.png]]

### 2.2.2 原始部署

#### 2.2.2.1 webapps 方式

假如我们想使用 Tomcat 来部署我们的网页的话，首先在 webapps 下面新建一个文件夹，这文件夹你叫什么名字都可以，这里我就使用`HelloWorld`

![[00 assets/95ff3fe0bc302852a7fdbdc12ca20f7c_MD5.png]]

我们再来创建`WEB-INF`文件夹，在同目录下创建`index.html`

![[00 assets/01160721c9a182b2a29cbb507233f488_MD5.png]]

我们要使用`startup.bat`来启动`Tomcat`服务

![[00 assets/c1135d650f6e26405bebbda678192c7c_MD5.png]]

我们再使用`http://localhost:8080/HelloWorld`就可以访问了

#### 2.2.2.2 Context 部署

> 方式一

1、我们可以在`server.xml`中配置`Context`属性，`path`为浏览器访问网址，`docBase`为你电脑真实得地址

![[00 assets/de7e89c4dabc2b4530e50e4e1b123a47_MD5.png]]

2、这样也可以进行访问

![[00 assets/8526b46bba11c2f19c88e6b36930ba09_MD5.png]]

> 方式二

![[00 assets/02defa53a5062297fd5f09d6c72b758e_MD5.png]]

1、或者在`conf\Catalina`下面编写一个`xxx.xml`文件，他会自动收录进入，可以减少编写`path`

![[00 assets/35939cccc3bc2c9b325a9dd2d0fb5d34_MD5.png]]

### 2.2.3 IDEA 部署

首先是进入到`Idea专业版`的右上角，点击`编辑配置`，就会进入到编辑配置的页面

![[00 assets/60e23f33ad6fd4225fe4355538ebb7f0_MD5.png]]

我们点击`编辑配置模板`

![[00 assets/913734773fea1917f3054890f4121832_MD5.png]]

选择`Tomcat服务器-本地`，然后点击右边的配置

![[00 assets/5db8785ec565e1b60e5adba8c803aab4_MD5.png]]

然后就会让我们选择主机的那个文件夹里面有`TOmcat服务器`，我们选择下载好的`Tomcat`服务器就可以了

![[00 assets/fd73f8f668028fdcfa36e73c00fdcf05_MD5.png]]

应用完毕之后，点击左上角的`+`号，来添加`Tomcat模板`

![[00 assets/e1cc2cdd9687d2ffb95949e44e8b42c7_MD5.png]]

我们再点击部署，将`Tomcat模板`部署到我们的项目中

![[00 assets/3cf4f173fbb86b16758477755d7cacc9_MD5.png]]

这里的应用程序的上下文就是访问`Html`文件时输入的`Url`

![[00 assets/5d96d8a1d9805ee077ccaa8efc784bc2_MD5.png]]

我们使用下面的配置可以实现热加载

![[00 assets/8ed82d0ec257fdd7feb174f5624560f6_MD5.png]]

我们点击右边的运行就可以看到页面了

![[00 assets/d6cdfa0853d617be9201eb41909a4e41_MD5.png]]

剩下的如何补充`Web`模板，如何`导入项目`，可以参考视频：[20-尚硅谷-Web-在 idea 下新建 javaweb 项目-部署-运行\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1AS4y177xJ?p=20&vd_source=2d46cc0fa105788201e3e43d9c83f528)

# 3. Servlet

## 3.1 基本介绍

> 导入 Servlet

首先我们需要导入`Servlet`包，在`lib`下面的`servlet-api.jar`里面有，我们怎么导入的`JDBC`就怎么导`servlet-api.jar`，在以前的笔记里面有写，这里就不说了

![[00 assets/7f08f86b25494afcd07069c10c70bb7b_MD5.png]]

还有一种方式就是使用`Idea`来导入，我们点击`文件-项目结构-模块-“+”-库`

![[00 assets/e726737a7179a094c47363ab8c9b1471_MD5.png]]

因为我们前面配置了模板，所以直接使用`Tomcat`提供的包就可以了

![[00 assets/848ea4e98a45ab7087b0199a7cd86a91_MD5.png]]

我们就可以看到`JDK1.8`和`Tomcat`的包

![[00 assets/c5a90680448e10fd0721295da3bf9c5d_MD5.png]]

> 基本使用

我们来大致说一下流程，浏览器使用`Http Request`请求`add.html`，用户在浏览器中输入数据并且配置的请求方法是`post`。`action`本质就是一个代号，浏览器叫后端那个程序处理的一个代号，到时候会有一个`.xml`的配置文件来识别，并且执行后面的操作，最后通过`DAO`来将数据存入数据库

![[00 assets/5b020a77a1036a64dfbdcb1142b9cc76_MD5.png]]

1.这是`Html`文件的书写

![[00 assets/8d2507028597235c5aad6aca4f275ff5_MD5.png]]

并且这里就有一个我以前学习`HTML`没有发现的一个小细节，就是`form`标签里面的`input`标签中的`name`就是作为一个`key`存在的，我们在`Servlet`来获取的时候也是使用的这个`key`

![[00 assets/ccf0cbaa4a0a7b0b2af83390f7e8d4eb_MD5.png]]

2.下面就是`AddServlet`的书写了，因为是前端将数据发送过来，所以我们调用`req`对象中的`getParameter`方法来获取数据，并对其进行处理

![[00 assets/7b2b81b76ec1f4b26c4924bd63fe1fc0_MD5.png]]

3.但是这样看可不行，注意到没前端的`action`只是发送了一个代号，所以我们还需要配置这个代号，将它带到指定的`AddServlet`中进行数据的处理，这个时候我们就需要配置`WEB-INF/web.xml`文件了

`servlet-mapping`是一个映射，也就是`url-pattern`对`servlet-name`的映射，当浏览器的主页提交的内容弹窗到`/add`之后就会去配置文件中寻找`/add`是找那个类来处理

![[00 assets/59fdbd5c1de7c5042f2877102c6c32a0_MD5.png]]

我们不仅可以写一个映射，我们也可以写多个映射，这样我们书写不同的`HTML`，请求不同的组件，就可以使用一个`servlet`来解决

![[00 assets/b7ff750b094dac36c91e35559b2cc948_MD5.png]]

4.我们再使用`DAO`来对数据库进行处理，这个在我`Java基础`里面写的很详细，可以参考一下。但是这里会出现很多的问题，遇到问题可以查询，但是有一个万能方法就是将对数据库的`.jar`加入到`Tomcat\lib`下面

![[00 assets/8e8433971d38d8420eaa7e054df053f6_MD5.png]]

🎈：P22 讲了如何导入包，如何添加依赖，假如忘记了可以参考

需要注意一个问题，就是`Tomcat`默认是`GBK`，假如想传输中文的话，就需要设置为`UTF-8`，这样的话就没有乱码问题，并且要将`req.setCharacterEncoding()`放置在获取数据之前

![[00 assets/22e05f6d416449b49397bed492ddceb8_MD5.png]]

## 3.2 Servlet 继承

![[00 assets/b425e3496b177c7a7538c3837a3c3cda_MD5.png]]

## 3.3 实现方法

其实底层主要的方法就`init(),service(),destory()`，其中我们最常用的就是`service()`方法了，我们在`3.1基本介绍`里面使用的就是`doPost`方法，但是`service()`其实更加智能，可以自动识别你请求的方式

![[00 assets/f05cce63bc4ce090a5a7a178a6e9a6af_MD5.png]]

假如说我们正常使用的话和上面的`doPost`是一样的，就是使用这个方法我们就不需要再去分辨是那个网络请求了

![[00 assets/2b7139242252e809ea16f9e68bf46439_MD5.png]]

## 3.4 生命周期

> 生命周期

其实`Servlet`的生命周期就是对应的上面的实现方法`init(),service(),destory()`

![[00 assets/99bb43c3fa3a8c8cd9e4947824b46093_MD5.png]]

大致的生命周期就是**实例化、初始化、服务、销毁**。

销毁时当容器消失的时候，就会去执行**销毁**的操作，而**实例化和初始化**只能执行一次，这就说明都是一个`servlet`来处理，所有的请求都是通过这个`servlet`来处理

![[00 assets/b12e378d730b491a1766904cde8f87fa_MD5.png]]

> laod-on-startup

我们还需要注意一个问题，就是**实例化和初始化**的时机，假如是什么都不去设置的情况下，只有**第一个网络请求**发送的时候才会进行**实例化和初始化**，我们看下图就可以发现

![[00 assets/629042e38351fd7f33320ded247959d2_MD5.png]]

假如说我们去配置`web.xml`就可以实现实例化和初始化提前，但是这么做有什么好处呢？我们一开始不去实例化就加快了启动的速度，但是第一个访问的人的速度就会变慢这是因为时间都用于加载了。但是我们配置之后虽然启动速度变慢了，但是所有的访问速度都是一样的

![[00 assets/d6f3b1fcc0491cd5b17c6d5f56f931ab_MD5.png]]

所以这个时候我们就可以去配置`web.xml`文件，给`servlet`标签添加`laod-on-startup`数字来设置优先级，配置该属性就默认是初始化和实例化优先，这个数字是为了多个`servlet`同时创建的时候使用，**数字越小优先级越高**

![[00 assets/ff907e977f78f831bf5c688bc9efe626_MD5.png]]

> Servlet 是单例的，线程不安全的

Servlet 单例的，每次一个`Servlet`来执行；但是 Servlet 并没有线程锁，所以是线程不安全的

## 3.5 HTTP 协议

可以看我以前笔记，但是还是一些开发的时候没注意到的问题

**请求体的三种情况**

| get  | 没有请求体，但是可以通过 queryString 来处理 |
| :--: | :-----------------------------------------: |
| post |             有请求体，form data             |
| json |      有请求体，request payload（载荷）      |

**HTTP 是无状态**，服务器无法区分这 2 个请求都是一个客户端发来的，还是不同客户端

![[00 assets/cf03e8085bc47066a066f76998f12701_MD5.png]]

## 3.6 会话存储

### 3.6.1 基本介绍

🎈 就是前端领域的话，这里可以参考我以前的`JS`笔记

我们使用会话存储不仅仅是进行**持久化登录**，我们也可以让**服务端**传输`token`来**区分**不同的**客户端**，下面的`Set-Cookie`就是服务器响应的一个特殊的值，并且是只有这个客户端能使用

![[00 assets/bdcef1e1e63ef753c74e52e0f61e4827_MD5.png]]

我们使用`req.getSession()`就是**获取当前会话，没有的话就创建一个返回**。我们就可以看到响应头里面就包含`SessionId`，并且我们可以看右边的输出语句，是不是每次请求发送的 Cookie 都一样，这样的话就可以区分各个客户端了

![[00 assets/9c0fa9f991d42e31cf85ae8665c1219c_MD5.png]]

我们**观察上面图的 Cookie**，第一次发送请求的话是不带`JSESSIONID`，假如是第二次请求就有了

![[00 assets/4a49a5fb28b48cedcea308721022f8c8_MD5.png]]

### 3.6.2 常用 API

这个是 Session 的基本设置

![[00 assets/41035032b595e902d8c57a4683ad74be_MD5.png]]

下面的就是 Session 的**设置、获取、删除**的操作

![[00 assets/8ed82d0ec257fdd7feb174f5624560f6_MD5.png]]

### 3.6.3 Session 作用域

下面就是`Session`的作用域，我们通过一个主机来访问一台服务器，主机会将你设置的 Session 丢到一个公共的内存中，所有的`Servlet`都可以去访问。假如你又有一个客户端就又会创建一个容器将这个客户端的`Session`丢进去，并且这 2 个容器互相不影响

![[00 assets/bf2d45a12f9074bbe9d261d43995d37f_MD5.png]]

这里是 2 个不同的类，也可以看出`Session`并不是保存在一个类中，而是将值存到一个单独的空间。并且我们设置`Session`是通过`setAttribute`，而获取`Session`是通过`getAttribute`

![[00 assets/dea5d80e11817f9b30c13f7875c84d30_MD5.png]]

假如是一个客户端去设置了`Session`之后，然后从`Java`容器中获取，就可以在控制台正常显示

![[00 assets/1945e5198d320be2d7fdadc920bbdb4a_MD5.png]]

这个时候我们更换浏览器（更换客户端），直接去查询，会发现根本查不到。其实这很好理解，因为`HTTP`是无状态的，所以这个 Session 就是这个客户端独有的，假如在服务器内部共享的，这不也分清那个客户端

![[00 assets/c07160ff27b946b38b35739ec7d8ce54_MD5.png]]

## 3.7 服务器内部转发

就是将服务流转给另一个处理程序

![[00 assets/ed9c7da464d8a6eb32c9d59eace33ca9_MD5.png]]

我们使用`req.getRequestDispatcher()`就可以将服务转发给`Test2`

![[00 assets/50ca52fd9551d0883daff8c1d4e06924_MD5.png]]

并且服务器内部转发是发生在服务器的，客户端根本不知道

![[00 assets/335b0d2dcbb7cbcec4df0f37864f4e6f_MD5.png]]

## 3.8 客户端重定向

不仅仅客户端可以使用路由来操作，在服务器端也可以进行响应，告诉客户端如何去响应

![[00 assets/22cc2d2a91978dc06ea4c4ecd2bb33f8_MD5.png]]

下面的方式和上面的服务器内部转发有原理性的区别，所以客户端就会显示改变响应的 url，并且会有 2 个请求，其中用于重定向的请求状态码是 302。

这里使用的是`resp.sendRedirect()`来进行客户端的重定向，注意这里重定向是改变地址来的，所以我们书写`Web.xml`文件的时候，是需要对应`url-pattern`来书写

![[00 assets/d89730531a97e4226d7fe9b673bcc7c8_MD5.png]]

## 3.9 保存作用域

保存作用域有 4 个范围：**page**(页面级别，现在几乎不用)，**request**(一次请求响应的范围)，**session**(一次会话范围)，**application**(整个应用程序范围)

### 3.9.1 request

`request`作用域只在第一次请求中有效

![[00 assets/acb9476bea1dd2cdc7d5901fb8da3ef6_MD5.png]]

下面就是进行的操作，就是在一个`Servlet`中进行设置值的操作，然后让另外一个`Servlet`来读取

![[00 assets/37976086dc690485ea893fb5548680dc_MD5.png]]

结果是**null**，所以可以得出结论：request 的作用域只在一次请求和响应的时候，也就是上图的**请求 1 和响应 1**

![[00 assets/a0e1612763441198a159f7c5a0fac6b9_MD5.png]]

假如我们将重定向换为服务器内部转发会怎么样呢？结果是显而易见的，是**可以**的，因为服务器内部转发本质也是一次请求，所以是可以获取到数据的

![[00 assets/1f7c45381295e5d7167ca82c4c4dceca_MD5.png]]

### 3.9.2 session

可以参考`3.6.3` Session 作用域

这里就梳理结论：作用域为同一客户端

### 3.9.3 application

只要是设置了`application`的情况，不管是你不同的请求还是不同的客户端都可以请求到

![[00 assets/047015086d557177db5ceb12a6f4c59a_MD5.png]]

下面是同一客户端重定向的情况下是可以获取到数据的，那么可以看出`application`的作用域在 Tomcat 开启，假如 Tomcat 关闭就没了

![[00 assets/33acc2fc5f173d8633f83bd04912d55e_MD5.png]]

假如是不同客户端呢？结果也显而易见，是可以的

![[00 assets/bde2c7c1390374c71a6db1dbfb635017_MD5.png]]

## 3.10 路径问题

以前我们使用绝对路径的情况下，我们以`index.html`为基础来引用`login.css`，路径的选择就是`css/index.css`，但是使用这种方式有个缺点就是当层级较深，就不知道自己引入的是什么了。所以整个时候就需要使用到**相对路径**，但是这个相对路径并不是以前指定盘符的相对路径，而是以服务器为主体

![[00 assets/c86e676e9c781ff824fbf42a60e21781_MD5.png]]

以 index.html 为基础： `css/index` -> `http://localhost:8080/pro10/css/index.css`

假如你是使用的`thymeleaf`的情况下，可以使用`th:href="@{/css/index.css}"`来代替上面的`http://...`，因为`@{}`就是代指的`http://...`，里面填入地址就可以了，而且不存在设备迁移的问题

# 4. thymeleaf

## 4.1 基本使用

1.导入`.jar`

![[00 assets/022bed50de1f5ad9c1b4fe3965c73970_MD5.png]]

.我们创建一个`ViewBaseServlet`类

![[00 assets/bde2c7c1390374c71a6db1dbfb635017_MD5.png]]

将下面的代码拷入`ViewBaseServlet`，这个类暂时只需要复制粘贴，以后使用框架都会淘汰

```java
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.WebContext;
import org.thymeleaf.templatemode.TemplateMode;
import org.thymeleaf.templateresolver.ServletContextTemplateResolver;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class ViewBaseServlet extends HttpServlet {

    private TemplateEngine templateEngine;

    @Override
    public void init() throws ServletException {

        // 1.获取ServletContext对象
        ServletContext servletContext = this.getServletContext();

        // 2.创建Thymeleaf解析器对象
        ServletContextTemplateResolver templateResolver = new ServletContextTemplateResolver(servletContext);

        // 3.给解析器对象设置参数
        // ①HTML是默认模式，明确设置是为了代码更容易理解
        templateResolver.setTemplateMode(TemplateMode.HTML);

        // ②设置前缀
        String viewPrefix = servletContext.getInitParameter("view-prefix");

        templateResolver.setPrefix(viewPrefix);

        // ③设置后缀
        String viewSuffix = servletContext.getInitParameter("view-suffix");

        templateResolver.setSuffix(viewSuffix);

        // ④设置缓存过期时间（毫秒）
        templateResolver.setCacheTTLMs(60000L);

        // ⑤设置是否缓存
        templateResolver.setCacheable(true);

        // ⑥设置服务器端编码方式
        templateResolver.setCharacterEncoding("utf-8");

        // 4.创建模板引擎对象
        templateEngine = new TemplateEngine();

        // 5.给模板引擎对象设置模板解析器
        templateEngine.setTemplateResolver(templateResolver);

    }

    protected void processTemplate(String templateName, HttpServletRequest req, HttpServletResponse resp) throws IOException {
        // 1.设置响应体内容类型和字符集
        resp.setContentType("text/html;charset=UTF-8");

        // 2.创建WebContext对象
        WebContext webContext = new WebContext(req, resp, getServletContext());

        // 3.处理模板数据
        templateEngine.process(templateName, webContext, resp.getWriter());
    }
}
```

3.配置`Web.xml`

![[00 assets/20ba5577571a77e3545d18a2bbd5e77b_MD5.png]]

4.创建一个`Servlet`类继承`ViewBaseServlet`，并且在里面写好数据库操作语句，将想要的数据取出来

![[00 assets/334432651dd62cd37b9d16b705d7abe9_MD5.png]]

这里就得出了一个物理视图名称，我们在`web.xml`文件中配置了视图前缀和后缀，在这里就其效果了。这里的`super.processTemplate()`中的`hello`就是逻辑视图，`view-prefix`和`view-suffix`就是作为视图前缀和后缀

![[00 assets/841649921fd82e45642db987834f6704_MD5.png]]

6.这里就是将数据库中的数据通过`DAO`，`Servlet`，`Session`传入到 HTML 中，并且是使用`thymeleaf`来操作 HTML

![[00 assets/7c631f50e41db7098fb805e6e81938ba_MD5.png]]

下面就是展示的效果，其实和 Vue 是差不多的，但是平常前端的页面都是 Vue 是直接操作，这个是通过 Java 代码来操作

![[00 assets/9d0715c1845ae2cdd74dcfaefbc6b164_MD5.png]]

## 4.2 更新功能

1.添加跳转的功能

![[00 assets/3cc34da9f1ea9fe2e3b1a2220065462d_MD5.png]]

2.跳转的功能实现了，但是没有配套的`Servlet`方法，所以我们书写一个`EditServlet`方法，并且识别参数，从数据库中取值，传入 request 作用域中供`thymeleaf`中使用

![[00 assets/22f9d5646d13518d0c253b768689ffe1_MD5.png]]

下面的 id 值，你可以使用`application`来传值，也可以使用`input`一起传值，就是要将 input 设置为隐藏

3.此时我们来编写页面的`thymeleaf`的语法

![[00 assets/b59cd11c8667df7bc4b39e286508cba4_MD5.png]]

这样页面就可以正常显示了

![[00 assets/f235985758c6b7ffbc86862d22e21a81_MD5.png]]

4.我们再来编写`update`的语法逻辑

![[00 assets/5e82cf5b92ce9487bc6c0af467aa8ca6_MD5.png]]

假如我们不事宜客户端重定向的功能赖实现页面的跳转，而是渲染呢？也就是`super.processTemplate("index",req,resp);`，这种方式赖跳转呢？其实它的本质就是`req.getRequestDispatch("index.html").forward(req,resp)`也就是服务器内部转发，这种方式其实不会造成 url 的变化，所以也不会启动`IndexServlet`方法，那么就不会更新里面的数据。

![[00 assets/5b020a77a1036a64dfbdcb1142b9cc76_MD5.png]]

即便里面使用的`Session作用域`但是其实根本没有执行，所以数据就不会更新

![[00 assets/6108649a78207af1f8a00443766c4b50_MD5.png]]

所以这里使用的是客户端重定向的方法来改变的

## 4.3 删除功能

1.我们先在页面中书写删除的按钮的逻辑，这里我们是使用`url`来提示删除

![[00 assets/61629c31920687386b7530c336d67cd5_MD5.png]]

2.我们来编写删除的逻辑

![[00 assets/d261a493a9697ef8c77a03ce8760c1ec_MD5.png]]

然后就可以实现删除的功能，其实逻辑很简单就是常规的`Crud`操作

## 4.4 添加功能

1.我们在主页使得页面跳转到`add.html`

![[00 assets/457e72d30b48202ea21fa2d721505055_MD5.png]]

2.我们来编写`add.html`

![[00 assets/90000abf8412eaf8a68e84634dab4055_MD5.png]]

3.这里编写添加的逻辑功能

![[00 assets/fc40240f04da1c6c4030c2e695546585_MD5.png]]

## 4.5 分页功能

分页功能其实只需要知道：**总数据，每页显示的数据**就可以写了

1.先编写 HTML 文件

![[00 assets/4535735b46476b7e70a4f6305f247d77_MD5.png]]

2.再来编写业务逻辑

![[00 assets/0a6c6ac7d7f5054e1b5c6f310a5d78db_MD5.png]]

其实我这个方式不是很好，我建议使用老师的方式来编写 P37

这里我发现为什么我一开始进入主页需要使用`@WebServlet(/index.html)`了，假如我们要设置为`index`的话

![[00 assets/7c24318a1d0245b902033de97203a651_MD5.png]]

就需要默认打开网页就是`index`，然后再去重定向，使用`Thymeleaf`来渲染`HTML`页面，设置好前后缀

![[00 assets/6108649a78207af1f8a00443766c4b50_MD5.png]]

![[00 assets/eb40170ea3ff022202a149152f382ab3_MD5.png]]

这里来总结一个为什么我一开始不能访问，而必须要使用`index.html`了，因为我一开始默认访问的是`/index.html`，但是我的`@WebServlet`中写的却是`index`，所以检索不到，我一开始就默认 url 为`/index`的话，后面直接`Thymeleaf`就可以跳转过去了

## 4.6 模糊查询

1.完成 index.html

![[00 assets/25f5e5b2df498a976dbf4419b627da7c_MD5.png]]

2.完成业务`IndexServlet`

![[00 assets/101884cc0558e40a01e55c90b33edafc_MD5.png]]

为了方便以后溯源，我将`index.html`和`IndexServlet`的代码都粘贴过来

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .main {
            display: flex;
            justify-content: space-around;
            width: 400px;
            border: 1px solid rebeccapurple;
            margin: 1px;
        }

        .main div {
            height: 20px;
            margin: 10px;

        }

        .main button {
            width: 70px;
            height: 25px;
            margin-top: 5px;
        }

        .main a {
            color: black;
        }

        .AddBtn {
            display: block;
            width: 100px;
            height: 40px;
            border: 1px solid royalblue;
            border-radius: 10px;
            margin: 10px;
            color: black;
            text-decoration: none;
            text-align: center;
            line-height: 40px;
        }
    </style>
</head>
<body>
<form action="index.html" method="post">
    <input type="text" name="oper"  hidden>
    <input type="text" name="keyword" th:value="${session.keyword}"/>
    <input type="submit" value="查询"/>
</form>

<a th:href="@{/add.html}" class="AddBtn">添加数据</a>

<div th:if="${#lists.isEmpty(session.Fruit)}">
    库存为空，暂时没有数据...
</div>
<div th:unless="${#lists.isEmpty(session.Fruit)}"
     th:each="temp:${session.Fruit}" class="main">
    <!--    <div><a th:text="${temp.name}" th:href="@{'/edit?id='+${temp.id}}"></a></div>-->
    <div><a th:text="${temp.name}" th:href="@{/edit(id=${temp.id})}"></a></div>
    <div th:text="${temp.price}"></div>
    <div th:text="${temp.count}"></div>
    <div th:text="${temp.remark}"></div>
    <!--    <button th:onclick="'delFruit('+${temp.id}+')'">删除</button>-->
    <button th:onclick="'delFruit('+${temp.id}+')'">删除</button>
    <script type="text/javascript">
        function delFruit(id) {
            window.location.href = "del?id=" + id;
        }
    </script>
</div>

<div>
    <button th:onclick="ChangeNum(1)" th:disabled="${session.CurrentNum==1}">首页</button>
    <button th:onclick="'ChangeNum('+${session.CurrentNum-1}+')'"
            th:disabled="${session.CurrentNum==1}">上一页
    </button>
    <button th:onclick="'ChangeNum('+${session.CurrentNum+1}+')'"
            th:disabled="${session.CurrentNum==session.PageNum}">下一页
    </button>
    <button th:onclick="'ChangeNum('+${session.PageNum}+')'"
            th:disabled="${session.CurrentNum==session.PageNum}">尾页
    </button>
    <div th:text="'页码:'+${session.CurrentNum}+'/'+${session.PageNum}+
    ' 总数据:'+${session.Total}">
    </div>
</div>
<script type="text/javascript">
    function ChangeNum(Num) {
        window.location.href = "index.html?Num=" + Num;
    }
</script>

</body>
</html>

```

```java
package Servlet;

import DAO.FruitDAO;
import MySsm.ViewBaseServlet;
import domain.Fruit;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.List;

//@WebServlet("/index")
public class IndexServlet extends ViewBaseServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setCharacterEncoding("UTF-8");
        FruitDAO fruitDAO = new FruitDAO();
        HttpSession session = req.getSession();

        String keyword = req.getParameter("keyword");
        String Session_Key = (String) session.getAttribute("keyword");
        if("".equals(keyword)) Session_Key = "";
        if (keyword == null) keyword = "";
        if (Session_Key == null) Session_Key = "";
        if (!(keyword == "" || (keyword.equals(Session_Key)))) {
            Session_Key = keyword;
        }

        String num = req.getParameter("Num");
        if (num == null) num = "1";

        Object o = fruitDAO.queryScalar("select count(*) from fruit where name like ?", "%" + Session_Key + "%");
        int Total = Integer.parseInt(String.valueOf(o));  // 总数据数
        int CurrentNum = Integer.parseInt(num); // 获取当前页
        int SinglePageNum = 5; // 一页展示多少数据
        int PageNum = (Total + SinglePageNum - 1) / SinglePageNum; // 页码

        List<Fruit> inps = fruitDAO.queryMulti("select * from fruit where name like ? limit ?,?"
                , Fruit.class, "%" + Session_Key + "%", (CurrentNum - 1) * SinglePageNum, SinglePageNum);

        session.setAttribute("Fruit", inps);
        session.setAttribute("CurrentNum", CurrentNum);
        session.setAttribute("PageNum", PageNum);
        session.setAttribute("Total", Total);
        session.setAttribute("keyword", Session_Key);


        super.processTemplate("index", req, resp);
    }
}

```

我这个实现的方式有点繁琐，我建议看老师的方法

下面就是一个全新的思路，我们可以多添加一个 input 框来判断从翻页获取的数据，还是查询，这里在 P39 中有详细的解释，这样做的话就将翻页和查询分开。因为**查询需要将输入的值进行存储，而翻页的话就是直接调用存储的 key 值**，这句话是关键

![[00 assets/704ea4a3448a08493bd621de67dfa669_MD5.png]]

假如想要查看所有代码的主体，可以去查看`D:\code\JavaTest4\Test2`下面文件，这个就是这个项目的所有代码

# 5. MVC

## 5.1 基本介绍

首先是介绍一下上面的水果店的主体功能，下面就是主体功能

![[00 assets/32e32796b3ee0e7ec629c3c8f2aa49d9_MD5.png]]

现在我们就使用这种方式来处理，所有的请求发送给`FruitServlet`中，然后在`FruitServlet`中执行各个方法

![[00 assets/60d634cccc6767006056b62ded7fd6d3_MD5.png]]

下面就是`FruitServlet`中的大致实现原理，我们将以前的`IndexServlet、AddServlet...`中的实现都传入到`FruitServlet`中了，单独设置一个`operate`值，专门用来判断执行那个`Servlet`

![[00 assets/cd69ce1df5aba804e247d040e8ca63c9_MD5.png]]

## 5.2 dispatchServlet

1.这里是优化上面的`Switch`，假如`Servlet`中的方法太多的话就会造成`Switch`太多了，所以这个时候就需要使用反射来获取当前对象的所有方法，然后一一对应来执行

![[00 assets/3ed796f4ba6c4b2949c074794e367029_MD5.png]]

# 暂时去 Spring 看看
