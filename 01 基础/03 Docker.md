**视频讲解**：[web 前端有必要学 docker 吗？0 基础-45 分钟带你学会](https://www.bilibili.com/video/BV1Z84y1a7nM/?spm_id_from=333.337.search-card.all.click&vd_source=2d46cc0fa105788201e3e43d9c83f528)

**文章介绍**：[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7227408739827974199)

# 1. 基本介绍

## 1.1 docker 介绍

1、`docker`能够隔绝物理环境，相当于是之前的虚拟机。而且 docker 内置了很多镜像可供使用。

2、`docker`容器技术以及`docker-compose`容器编排技术能最大限度的保证您的项目在开发环境和生产环境 上的一致表现。

3、要想在`window`、`mac os`中使用`docker`，需要先安装桌面版，其实相当于是在电脑安装了一个`Linux`内核 + `docker`环境。

![[00 assets/0152aa735f5c9e55d83d8e7419fcd0c5_MD5.png]]

4、`Docker` 提供了 `Docker Hub` 镜像仓库，可以把本地镜像 push 到仓库或者从仓库 pull 镜像到本地。

![[00 assets/9ff39b6af5c042d92ffb08864b9d249e_MD5.png]]

5、这里需要补充一条`镜像`和`容器`的关系，`镜像`作为一个软件存在，而`镜像`需要放在`容器`里面才能运行

## 1.2 原理总结

[Nest 通关秘籍 - zxg\_神说要有光 - 掘金小册 (juejin.cn)](https://juejin.cn/book/7226988578700525605/section/7236561244033908773)

1、如何做到各个容器不互相影响，这是结合了`linux`中的`namespace`和`group controller`，一个是隔离，一个控制

2、并且对于`docker`的分层架构中，不同的文件会使用`union fs`来处理

![[00 assets/e0e082c3758fcc4c1f03c04172a20d10_MD5.png]]

3、这样镜像之间的资源可以公用，减少了资源的浪费

![[00 assets/d339b3a7398db90587faec27d8014bb0_MD5.png]]

4、`docker`中的镜像是不能修改的，所以`docker`添加了一个`可写层`，并且使用`volume`挂载卷的方式来做数据持久化存储

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032113721.png" alt="image-20231222110427823" style="zoom: 67%;" />

5、回顾一下 Docker 实现原理的三大基础技术，都是缺一不可的

- Namespace：实现各种资源的隔离
- Control Group：实现容器进程的资源访问限制
- UnionFS：实现容器文件系统的分层存储，镜像合并

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032113736.png" alt="image-20231222110523230" style="zoom:67%;" />

# 2. 基本使用

## 2.1 安装 docker

### 2.1.1 win 安装

1、在`docker`官网下载最新的 `Docker Desktop` 安装，下载地址：https://www.docker.com/

2、如果出现下面的提示就表示`docker`已经安装完成

![[00 assets/8176625e1979797e38e79d5d9ff420c8_MD5.png]]

> WSL2 installations is incomplete

1、`Docker Desktop`启动的时候，有可能弹框提示 `"WSL2 installations is incomplete"` ，这是系统中没有安装`WSL2`内核的原因，打开https://aka.ms/wsl2kernel，在打开的页面中有一 个"**适用于 x64 计算机的 WSL2 Linux 内核更新包**"链接，点击下载，安装。

2、`WSL2 Linux`内核更新包安装后，重启 `Docker Desktop` 即可正常使用。您可在 cmd 或者 PowerShell 命令行中使用`docker`或者`docker-compose`等相关命令了

3、如果您在安装 `WSL2` 的过程中遇到了问题，可能是您的系统版本较低等原因，您可按照 https://aka.ms/wsl2kernel 页面的相关提示更新系统。该 `Docker Desktop` 的安装方法基于 Windows10 的 `WSL2` 如果您的系统没有或者不能安装 `WSL2`，可能不能使用该方法安装`Docker Desktop`。

> Windows Hypervisor is not present

![[00 assets/f598b810b7795764a65d87a5412fbd71_MD5.png]]

1、在 win11 中打开 `启用或关闭window功能` ，看选项中是否有 `hyper-v` ：

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032113405.png" alt="image-20230810154840686" style="zoom: 80%;" />

2、如果没有，则需要运行一个`BAT`脚本，以便激活该功能，将以下代码保存为`bat`文件，然后使用管 理员方式运行。经过大约 5 分钟，自动重启电脑即可：

```bash
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hv.txt
for /f %%i in ('findstr /i . hv.txt 2^>nul') do dism /online /norestart
/add-package:"%SystemRoot%\servicing\Packages\%%i"
del hv.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All
/LimitAccess /ALL
pause
```

> 手机模拟器问题

docker 和手机模拟器只能使用一个，所以这里就需要做一个取舍了

### 2.1.2 mac 安装

无 mac 电脑

## 2.2 部署使用

### 2.2.1 desktop 使用

1、我们需要下载一个镜像，然后使用镜像安装一个容器

2、我们就使用`images`来安装一个`nginx`镜像部署

3、下面的`/usr/share/nginx/html`表示`nginx`的共享地址，这里可以使用`volume 挂载`来共享文件

![[00 assets/bab90b2666815fb593256d54cdf3d3f4_MD5.png]]

4、使用`pull`将镜像拉取下来，就可以创建容器了，下面就是容器的配置

5、`8080`表示端口映射，也就是子系统中的`80`映射到`8080`中

6、`volumes`表示路径映射，我们可以将文件移动到`host path`，这样容器中也存在

![[00 assets/991873f26d24196687fd56c1d160333c_MD5.png]]

7、可以看到有`mount`的标识，标识的文件挂载上去了

![[00 assets/7fca47857ed437a20588bfbd2a5976fa_MD5.png]]

8、直接访问查看即可

![[00 assets/f874f66eadda6caee05a6178c5441718_MD5.png]]

### 2.2.2 命令行使用

1、因为`linux`中可能不存在可视化界面，所以需要使用命令来处理

> docker pull

1、`docker pull nginx:latest`就是下载`nginx`镜像

> docker run

1、因为`windows`中的`docker`是基于`wsl2`实现，所以路径可能存在问题，这里就使用`linux地址`来代替了

`-p` 是端口映射 `-v` 是指定数据卷挂载目录 `-e` 是指定环境变量 `-d` 是后台运行

```bash
docker run --name nginx-test2 -p 80:80 -v /tmp/aaa:/usr/share/nginx/html -e KEY1=VALUE1 -d nginx:latest
```

![[00 assets/991873f26d24196687fd56c1d160333c_MD5.png]]

> docker start / docker rm / docker stop

1、`docker start [name]` 启动一个已经停止的容器

2、`docker rm [name]` 删除一个容器

3、`docker stop [name]` 停止一个容器

> docker ps

1、`docker ps`可以查看现在在运行的`docker`容器

![[00 assets/6f33d097deca374a687ec24bd638553f_MD5.png]]

2、如果想查看所有的`docker`可以使用`docker ps -a`

![[00 assets/8923f44f4f20bfdba746f2ba7b330db5_MD5.png]]

> docker image

1、使用`docker images`可以查看所有的镜像

![[00 assets/b94b89391f71bc3c1f7155158cc81eb9_MD5.png]]

> docker exec

1、使用`docker exec -it [name] /bin/bash`，如果容器名字叫做`nginx-test`的话，就可以输入为`docker exec -it nginx-test /bin/bash`相当于在控制台打开了`docker`的控制台终端

`-i` 是 terminal 交互的方式运行 `-t` 是 tty 终端类型

![[00 assets/3267298b18942d665165e161ec10f8df_MD5.png]]

2、输入`exit`即可退出`docker exec`

![[00 assets/e41a0ea6d8dbd1170d51855e9b1d279d_MD5.png]]

> docker logs

1、使用`docker logs [name]`即可查看对应的`docker log`

![[00 assets/865b9e03bbacf2824b554e4dbe336d67_MD5.png]]

> docker inspect

1、使用`docker inspect`即可查看`docker`中的所有详细参数

![[00 assets/e9961ebf21fe923a29cca487a87cd791_MD5.png]]

> docker volume

1、`docker volume` 可以管理数据卷，这里需要了解`volume`的知识

![[00 assets/e9a3ef7a75ac140ea0aea053d6160f6d_MD5.png]]

# 3. 制作镜像

## 3.1 基本使用

1、使用`docker`可以方便将其他人的项目直接运行，而不需要配置

2、在`dist`目录之上新建一个 `dockerfile` 文件，该文件没有后缀，文件名即为此。我们来编写对应的`dockerfile`

3、`COPY dist /usr/share/nginx/html`，其中`copy`也可以这样编写，将`dist`文件夹下面的内容拷贝到 `/usr/share/nginx/html `目录下面（nginx 的默认项目路径）

![[00 assets/4ac889e266f0daca42c28a9f6479900a_MD5.png]]

4、我们运行`docker build -t aaa:ccc .`即可构建，`aaa` 是镜像名，`ccc` 是镜像的标签。注意后面的`.`不能省略。并且`docker build` 的时候会把构建上下文的所有文件打包发送给 `docker daemon` 来构建镜像

![[00 assets/c4e9044f0d703ecdfac1b5adc0b10bf9_MD5.png]]

5、使用`docker images`即可查看到创建的镜像

![[00 assets/98b9afe45c737b9399eb23616f2ee2ec_MD5.png]]

6、可以看到已经执行了`dockerfile`中的指令

![[00 assets/6509328a63c5defd70163ec68300f37a_MD5.png]]

## 3.2 volume 挂载

> 设置 mount

1、我们在`dockerfile`中添加`volume`标签，将`/app`设置为`volume`

2、我们执行`docker build ...`，因为默认是`dockerfile`，但是我们需要更换的话就是`-f`指定即可

![[00 assets/5bfec41cb57e82a6337becc40e468368_MD5.png]]

3、我们将本地的磁盘路径映射到`/app`中

![[00 assets/cf355bd84c6de929a1d4b3d2b5220908_MD5.png]]

4、可以看到文件已经被挂载进去了

5、但是可以看到`copy`中的数据不见了，这里的`volume`可以这样理解，`volume`只是挂载卷，容器不创建，和本机互通。但是`copy`需要容器中存在才可以

![[00 assets/24755d0ab5530c8a55c7838b296ad68f_MD5.png]]

6、可以看到地址和本机映射了，如果容器删除了数据依旧保存在本机

![[00 assets/ce22a283aecc7b9856562b05f109828a_MD5.png]]

> 不设置 mount

1、这次不去指定`volume`

![[00 assets/901b41c6aa43c7723b7bf030e4aa7ebc_MD5.png]]

2、可以看到文件不一样了，这次没有映射本机地址文件（因为没指定），但是这次`copy`的文件出现了

![[00 assets/b2a86b23d87203be8b7256c3da84be8f_MD5.png]]

并且可以看到这次的`mounts`的地址已经不一样了，这是因为`docker`会在本机中生成一个随机的地址来做存储

![[00 assets/f5d6b3a0f893a6a657ddac645b655aaf_MD5.png]]

3、在`windows`中可以通过这个路径查找到，`\\wsl$\docker-desktop-data\data\docker\volumes`

![[00 assets/65a995cadd68d5d8e9557e8ea8c4b2d6_MD5.png]]

4、这样就算你删了容器，数据也可以在这里找回。设想下，如果你跑了个 mysql 容器，存了很多数据，但是跑容器的时候没指定数据卷。有一天，你把容器删了，所有数据都没了，可不可怕？为了避免这种情况，mysql 的 dockerfile 里是必须声明 volume 的，这样就算你没通过 -v 指定数据卷，将来也可以找回数据。在镜像详情可以看到 mysql 的 dockerfile，确实声明了 volume

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032113756.png" alt="image-20231221235833102" style="zoom:50%;" />

5、这里的挂载`mount`我是这么理解的，如果指定了`mount`的话就会使用指定的地址，如果没指定的话`docker`就会默认随机生成一份，并且在`desktop`中的`volumes`，也就是一个归我们管理，一个归`docker`管理

![[00 assets/dbd13064bbc0e2cf200c39ce0b135522_MD5.png]]

## 3.3 arg/env

目前没找到什么好的实例，这里先留着，但是可以参数使用

## 3.4 cmd/entrypoint

1、表面上 2 个指令没区别，但是`cmd`可以被覆盖，但是`entrypoint`依旧会执行

![[00 assets/34624c23fe063a644bce300f52719903_MD5.png]]

2、借用这个点就可以结合起来，用来做默认值，比如下面的示例，就可以借用`cmd`可覆盖的特性做默认值

![[00 assets/b07a3d018468345315da09ebfc5d70b1_MD5.png]]

## 3.5 copy/add

1、ADD、COPY 都可以用于把目录下的文件复制到容器内的目录下。但是 `ADD` 还可以解压 `tar.gz` 文件。一般情况下，还是用 COPY 居多

![[00 assets/4a1a01632dde6214de717a67cee03b08_MD5.png]]

# 4. 发布 docker

## 4.1 发布

1、发布指令，其实很简单，直接在命令行输入如下命令即可：

```bash
docker push imqdcn/xxx:latest
# docker push 注册用户名/镜像名:tag名
```

2、我们要进行登录，才能发布作品

![[00 assets/f5c99a0cf33584468cbe69f7ab4645da_MD5.png]]

然后通过命令行，运行 docker login 登录，看是否命令行也已经登录成功：

![[00 assets/cc87873e8a3a0dda1b4d88581a19cd54_MD5.png]]

3、如果你的镜像名字在最开始时没起好名或与其他人发布的镜像名有冲突，可以通过如下方式改名：

```bash
docker tag xxx imqdcn/xxx
# 表示将xxx改名为 imqdcn/xxx,你也可以改为任意你喜欢的名字，比如imqdcn/vue3project
```

![[00 assets/e884bfcdb17eeb81f87fac2030aa3e69_MD5.png]]

4、你可以在 `docker-desktop` 通过搜索该镜像名字找到镜像地址，或打开https://hub.docker.com/查找你 发布的镜像：

![[00 assets/a60a8ae13acaea6fe43fa16e88a25f94_MD5.png]]

## 4.2 运行

1、镜像作者发给你 hub 镜像地址后，上面有拉取指令

![[00 assets/bcc8d42ba922e884eb4e0837f038f36f_MD5.png]]

可以在命令行中先通过执行 docker pull 下载到本地

```bash
docker pull imqdcn/xxx
# 如果后面没有写tagname，则使用默认的tagName：latest
```

![[00 assets/ba32d7d8f1440d262050ef2b82ac0127_MD5.png]]

2、运行以上指令，即可在 `docker desktop` 看到该镜像，并可运行该镜像。

![[00 assets/e41a0ea6d8dbd1170d51855e9b1d279d_MD5.png]]

# 5. dockerignore

1、\*.md 就是忽略所有 md 结尾的文件，然后 !README.md 就是其中不包括 README.md

2、node_modules/ 就是忽略 node_modules 下 的所有文件

3、[a-c].txt 是忽略 a.txt、b.txt、c.txt 这三个文件

4、.DS_Store 是 mac 的用于指定目录的图标、背景、字体大小的配置文件，这个一般都要忽略

5、eslint、prettier 的配置文件在构建镜像的时候也用不到

6、语法基本和`.ignore`类似，直接参考即可

```
*.md
!README.md
node_modules/
[a-c].txt
.git/
.DS_Store
.vscode/
.dockerignore
.eslintignore
.eslintrc
.prettierrc
.prettierignore
```

# 6. 多阶段构建

## 6.1 基本使用

1、目前在部署一个`nestjs`的项目，可以发现 src 等目录就不再需要了，构建的时候需要这些，但运行的时候只需要 dist 目录就可以了。把这些文件包含在内，会让镜像体积变大。那怎么办呢？构建两次么？第一次构建出 dist 目录，第二次再构建出跑 dist/main.js 的镜像。那不是要两个 dockerfile？确实需要构建两次，但只需要一个 dockerfile 就可以搞定。这需要用到 dockerfile 的多阶段构建的语法。

![[00 assets/f5e793e2be98357239dcafe182cd3ca8_MD5.png]]

2、我们使用多阶段构建编写`dockerfile`来构建一个新镜像`nest:second`

![[00 assets/42d1aac12de191d761a79cecc7884722_MD5.png]]

3、通过 FROM 继承镜像的时候，给当前镜像指定一个名字，比如 `build-stage`然后第一个镜像执行 build。之后再通过 FROM 继承 node 镜像创建一个新镜像`production-stage`

4、通过 COPY --from-build-stage 从那个镜像内复制 /app/dist 的文件到当前镜像的 /app 下

5、还要把 package.json 也复制过来，然后切到 /app 目录执行 npm install --production 只安装 dependencies 依赖

6、这个生产阶段的镜像就指定容器跑起来执行 node main.js 就好了

```dockerfile
# 构建环境（开发环境）
FROM node:18 as build-stage

WORKDIR /app

COPY ./package.json .

RUN npm config set registry https://registry.npmmirror.com/

RUN npm i

COPY . .

RUN npm run build

# 生产环境
FROM node:18 as production-stage

WORKDIR /app

COPY --from=build-stage /app/dist .
COPY --from=build-stage /app/package.json ./package.json

RUN npm config set registry https://registry.npmmirror.com/

RUN npm install --production

EXPOSE 3000

CMD [ "node", "./main.js" ]
```

7、可以看到小了很多，相比于之前。该多阶段构建会创建多个中间镜像来处理，但是只会选中最终镜像来处理

8、但是为什么需要多个阶段的镜像，为什么不直接使用`rm`来删除？因为在 Docker 构建过程中，虽然可以使用 rm 命令来删除不需要的文件，但这并不意味着这些文件不再占用空间。**Docker 镜像是由多层文件系统组成的，每一条 Dockerfile 指令都会创建一个新的层**。当你在一个层中添加了文件，然后在下一个层中删除这些文件，这些文件仍然会在原来的层中存在，因此它们仍然会占用空间。

![[00 assets/246d81ad6b6749cb71177e6cea100b28_MD5.png]]

9、可是我们用的基础的 linux 镜像比较大，可以换成 `alpine` 的，这是一个 linux 发行版，主打的就是一个体积小

![[00 assets/6255c351713685d956006d3dd624b692_MD5.png]]

## 6.2 多层缓存

1、但是对于为什么`Docker 镜像`是多层的，并且每个指令都会创建一个新层？下面是回答，可以知道`docker`是一个多层架构的

![[00 assets/fa549d4236012ebd14f638172c4c2253_MD5.png]]

2、这里就可以解决一个疑惑，为什么先`copy package.json`，而不是一起`copy`就完了，这就是利用了`docker`的多层缓存

![[00 assets/fb26e7abcb7409cb6accdf92db5a4e61_MD5.png]]

3、因为每条指令都会创建一个`层`，如果一起复制使用，那么只要文件变化就会重新构建，浪费资源

4、因为我们`copy package.json`的时候是一层，`npm i`又是一层，并且`package.json`一般情况不会频繁变化，所以可以单独抽取到前面作为一层，而容易变化的业务文件，就放在后面，这样就可以使用到`package.json`之前的缓存，加快构建速度

![[00 assets/f860333acaa781d87c76693b0e454e9c_MD5.png]]

这样只要业务文件改动就会重新`npm i`，这显然不合理

![[00 assets/9bd871916fbc639d4fa2f61159aa7e32_MD5.png]]

5、尝试之后发现不管构建多少次都没问题，速度很快

![[00 assets/48e4b21d4e49d84f8fd91ba629e623f2_MD5.png]]

现在我们改下 `README.md`，和`package.json`，可以看下速度对比，差距很明显

![[00 assets/6e292cfe683e620edf1064966fcbdeb4_MD5.png]]

6、我们可以知道`docker`是多层的，其实很多的`开发环境`的层是不需要的，所以我们需要多阶段构建，抛弃不需要的层

![[00 assets/96792d6e5c87ffb53e1fd4730f5b373e_MD5.png]]

7、我们在`docker desktop`中就可以看到，这个`nginx`就是`16层`缓存

![[00 assets/db3d12ea1b13c50e9af37103ca30be4d_MD5.png]]
