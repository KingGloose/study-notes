**视频讲解**：[https://www.bilibili.com/video/BV1FE411P7B3](https://gitee.com/link?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1FE411P7B3)

**视频讲解**：coderwhy 前端系统课 - git

**文章介绍**：[视频同步笔记：狂神聊 Git (qq.com)](https://mp.weixin.qq.com/s/Bf7uVhGiu47uOELjmC5uXQ)

# 1. 基本介绍

## 1.1 版本控制介绍

![[00 assets/baf1972c0a7112ccb533f236bb6eba93_MD5.png]]

![[00 assets/60a502592d5f6f65659523efc65b1768_MD5.png]]

因为一个项目需要多次的迭代，所以我们就需要一个版本控制器

**主流的版本控制器**：Git、SVN、CVS、VSS、TFS

**版本控制分类**：本地版本控制、集中版本控制(SVN)、分布式版本控制(Git)

SVN 的版本否集中在服务器，需要的时候再从服务器中获取

Git 没有中央服务器，每个电脑都是一个完整的版本库

## 1.2 版本控制历史

![[00 assets/83395d307b4db52108654f30bf129af6_MD5.png]]

## 1.3 集中式和分布式版本控制

> 集中式版本控制

![[00 assets/b2c56ab84ce197bf6fbd2bdb0e2ee22c_MD5.png]]

> 分布式版本控制

![[00 assets/1c6b6713b95247f93d3b571720f5eb1b_MD5.jpeg]]

# 2. 基本配置

## 2.1 安装使用

> 下载安装

下载地址：[Git - Downloading Package (git-scm.com)](https://git-scm.com/download/win)（假如下载比较慢的话，可以考虑相应的镜像网站）

> Git Bash、Git CMD、Git GUI 区别

![[00 assets/c8d926b6c32fb2ca38751986e47f9ee3_MD5.png]]

## 2.2 必要配置

> 配置分类

![[00 assets/b5be963d2a3e7d4b7c3b713ada76392a_MD5.png]]

> 配置处理

![[00 assets/f0667b97f631f45c5b457bd8fb30bf4a_MD5.png]]

**查看 Git 配置**

```
git config -l
```

**查看本地的配置** Git\etc\gitconfig

```
git config --system --list
```

**查看当前用户配置的信息** C:\Users\Administrator\ .gitconfig

```
git config --global --list
```

**添加名称和邮箱**

```
git config --global user.name "张三"  #名称
git config --global user.email 2319671152@qq.com   #邮箱
```

# 3. 基本使用

![[00 assets/99d5ce63409a498ebd366c0dd6ac8027_MD5.png]]

> 初始化本地仓库 - 从零开始

1、一开始使用项目得话需要使用`git init`来初始化，这样文件就会多一个`.git`得文件夹

![[00 assets/303ff510311e96430cc34aa9c8345260_MD5.png]]

2、使用`git add .`将文件存入暂缓区中，其中`.`表示所有文件，如果需要存入单个文件得话就可以写`git add index.html`得形式

![[00 assets/a2aaa51638c98b64649a3c031ac937c4_MD5.png]]

3、使用`git commit -m "初始化项目"`来提交项目

![[00 assets/20035a679d36c16e3dffeba33ca61f26_MD5.png]]

4、我们可以使用`git log`来查看仓库日志

![[00 assets/5f014bdf2caa67336a3a670909b78a47_MD5.png]]

如果列表很多的话，可以使用`空格`来看下一段信息，使用`q`来退出当前查看

> 克隆远程仓库 - 从已有得仓库进行处理

使用`git clone xxx`命令对仓库进行克隆

![[00 assets/de37a97161c111f73961fc79ab598e0a_MD5.png]]

# 4. 文件状态

## 4.1 基本概念

版本控制就是对文件的版本控制，要对文件进行修改、提交等操作，首先要知道文件当前在什么状态，不然可能会提交了现在还不想提交的文件，或者要提交的文件没提交上。

- **Untracked**: 未跟踪, 此文件在文件夹中, 但并没有加入到 git 库, 不参与版本控制. 通过 git add 状态变为 Staged.
- **Unmodify**: 文件已经入库, 未修改, 即版本库中的文件快照内容与文件夹中完全一致. 这种类型的文件有两种去处, 如果它被修改, 而变为 Modified. 如果使用 git rm 移出版本库, 则成为 Untracked 文件
- **Modified**: 文件已修改, 仅仅是修改, 并没有进行其他的操作. 这个文件也有两个去处, 通过 git add 可进入暂存 staged 状态, 使用 git checkout 则丢弃修改过, 返回到 unmodify 状态, 这个 git checkout 即从库中取出文件, 覆盖当前修改
- **Staged**: 暂存状态. 执行 git commit 则将修改同步到库中, 这时库中的文件和本地文件又变为一致, 文件为 Unmodify 状态. 执行 git reset HEAD filename 取消暂存, 文件状态为 Modified

![[00 assets/56d9ed6febce302b9b436e83f9276641_MD5.png]]

1、我们使用`git add .`的时候就会将文件设置为`已跟踪状态`

2、如果我们对已经添加到`跟踪状态`的代码进行修改的话，就会变成`modified`状态

![[00 assets/30da4d85736fccbf8c7e905af79dd2f6_MD5.png]]

## 4.2 操作流程

Git 本地有 3 个目录，**工作目录(Working Directory)、暂存区(Stage/index)、资源库(Repository/Git Directory)**，如果加上是远程的**Git 仓库(Remote Directory)**，就是四个目录

<img src="https://knowledge-picture.oss-cn-wuhan-lr.aliyuncs.com/202405032110195.png" alt="屏幕截图 2022-02-20 140601" style="zoom:50%;" />

- Workspace：工作区，就是你平时存放项目代码的地方
- Index / Stage：暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信息
- Repository：仓库区（或本地仓库），就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中 HEAD 指向最新放入仓库的版本
- Remote：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换

![[00 assets/77af0a926a3f6e4b3c8993d780d3ed25_MD5.png]]

> 基本操作流程

其实在工作中就是下面得 2 个命令

![[00 assets/1e919a0735e5b53465564a92e4769538_MD5.jpeg]]

![[00 assets/8c046a0cb67be87620253236f9f651aa_MD5.png]]

## 4.3 查看文件状态

![[00 assets/725cb52a193bcb7fe592b616a5b470f9_MD5.png]]

我们可以使用`git status`来查看文件状态，或者在`vscode`的边栏查看

![[00 assets/3a356dbe5134907e8e857fb5e29a12bf_MD5.png]]

## 4.4 校验和

使用`校验和`得话不仅仅可以作为唯一标识，还可以作为回退版本得标识

![[00 assets/79dee0ba46c16636a3c07fd7fb691dd3_MD5.png]]

![[00 assets/cf55b0836906ab564b67d64efddf6a83_MD5.png]]

> 查看提交历史

![[00 assets/b2d23961edcbb916b0a2152212d3dc02_MD5.png]]

# 5. 忽略文件

在`github`中有开源的忽略文件，直接复制即可。根据项目后续自己修改即可

![[00 assets/513546db0e376c30a46a959df68eacc1_MD5.png]]

在主目录下建立".gitignore"文件，此文件有如下规则：

1. 忽略文件中的空行或以井号（#）开始的行将会被忽略。
2. 可以使用 Linux 通配符。例如：星号（\*）代表任意多个字符，问号（？）代表一个字符，方括号（[abc]）代表可选字符范围，大括号（{string1,string2,...}）代表可选的字符串等。
3. 如果名称的最前面有一个感叹号（!），表示例外规则，将不被忽略。
4. 如果名称的最前面是一个路径分隔符（/），表示要忽略的文件在此目录下，而子目录中的文件不忽略。
5. 如果名称的最后面是一个路径分隔符（/），表示要忽略的是此目录下该名称的子目录，而非文件（默认文件或目录都忽略）。

```
#为注释
*.txt        #忽略所有 .txt结尾的文件,这样的话上传就不会被选中！
!lib.txt     #但lib.txt除外
/temp        #仅忽略项目根目录下的TODO文件,不包括其它目录temp
build/       #忽略build/目录下的所有文件，其实就是前面的/表示往上忽略
doc/*.txt    #会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
```

注意：假如没有.gitignore 的文件的话，是需要全局配置的时候才有

# 6. 版本回退

![[00 assets/f0ef84fe1606fb758a391072c1bd84c9_MD5.png]]

![[00 assets/99ecbb44f9374554fd4d6e70b1d38392_MD5.png]]

如果你想撤回回退得版本，本质其实也是移动`head`指针，按照下面得方式即可

![[00 assets/e0fe0cc4f1a5026d2a733e2a4c9bc03a_MD5.png]]

# 7. 远程仓库

## 7.1 基本介绍

![[00 assets/12f2b5753e371beef6248d25f2feedeb_MD5.png]]

## 7.2 仓库验证

1、我们在`Gitee`创建了一个仓库，但是`Gitee`默认是私有仓库

![[00 assets/95e9ef85cd86b4744c3744b2361c2fd6_MD5.png]]

2、一般自己创建得仓库是私有仓库，所以需要输入自己得信息，但是每次都需要输入自己得信息就太麻烦了。所以就需要一个验证手段来解决这个问题

![[00 assets/1c34f5f8e5f9bc81cfa300fc8158fc31_MD5.png]]

### 7.2.1 HTTP 凭证

![[00 assets/2ee32e9f4ebc2be044910dc57b919a10_MD5.png]]

1、因为我们在安装`Git`得时候都是选择默认得，所以是默认有`Git Credential Manager for Windows`工具，该工具主要是将电脑中得账户和密码进行隐藏

2、我们使用`git commit -a -m "xxx"`存在暂缓区之后

![[00 assets/935a4c11a70fecd58be5326465203fc4_MD5.png]]

在输入`git push`就可以将更新得代码推送过去，并且`-m`后面得注释这里也可以看到

![[00 assets/f07366f010b94bedd36ef02d3fba5535_MD5.png]]

3、如果想要删掉凭证得话，通过下面得设置就可以删掉

![[00 assets/b88716a49fd4764454d2f176190a060b_MD5.png]]

### 7.2.2 SSH 密钥

![[00 assets/fb9051b9a4df50553911b05b30f8de88_MD5.png]]

1、在`Git Bash`中就可以生成密钥

![[00 assets/664c96789476390d566f0d8752d69d1b_MD5.png]]

2、我们根据路径找到下面得文件，将公钥中得文本复制

![[00 assets/484e10c5e3d6b0fab63ebe78de9862ea_MD5.png]]

3、我们将 `公钥` 复制到`Gitee`得个人中心即可，这样每次请求得时候，直接将私钥给服务器与你输入得公钥对比即可，就不需要使用账户和密码存储了

![[00 assets/2fabfcc72d9aa828f500e10e6cbb9a17_MD5.png]]

## 7.3 管理远程服务器

下面所有操作是在`gitee`中来处理得，每个`git`可能处理方式不一样

> 查看远程服务器

![[00 assets/889c2cef75322fafea87f3d75b42218e_MD5.png]]

`origin`表示名称，`url`表示该仓库得地址，`fetch/push`分别表示`获取和发布`得权限

![[00 assets/3b4e389364acacc1ae11a056be584dcc_MD5.png]]

> 操作远程服务器

![[00 assets/a6f3dc0e4dbcc4091cb3385c726c4408_MD5.png]]

1、在前面我们自己手动搭建了一个本地仓库，也就是文件夹`01`。因为是本地仓库得原因，即便我们使用`git remote xxx`连接上了远程仓库，但是不能正常交互

![[00 assets/b2e8fba4b0fd731fb75182fba846c42f_MD5.png]]

我们使用命令`git remote -v`就可以发现没有连接得仓库

![[00 assets/47b6c0e84bd8febb0fa746c8e18f17a4_MD5.png]]

2、所以需要手动添加远程仓库得地址，才能和远程仓库进行连接

![[00 assets/25a040f2bc2590d00e6032c2e7ae23c0_MD5.png]]

![[00 assets/42ace90476c228a27f8e213b81fda93e_MD5.png]]

3、但是只是单纯得添加连接并不行。因为`本地仓库`存在很多得分支，`远程仓库`也存在很多得分支，我们并没有指定本地分支连接得远程仓库分支，所以你使用`git pull/git push`就会报错，所以就需要设置分支

4、其中`git branch --set-upstream-to=origin/master`后面的参数表示`origin`远程仓库，`master`表示远程仓库的分支，这样就设置了上游分支。这步操作只是告诉这个本地仓库它的远程仓库是`origin的master分支`，如果我们直接写`git pull origin master`也是一样的效果

![[00 assets/52e5d708344df8330840e741006f9158_MD5.png]]

4、我们虽然设置了`git branch`解决了`git fetch`得问题，即本地仓库和上游仓库进行连接，文件都能正常下载下来。但是并不能正常合并，因为在`Git 2.9`之后就不允许没有共同`Git`历史得分支进行合并，假如想强行合并得话，就需要使用`git merge --allow-unrelated-histories`

![[00 assets/2b92f77c9d20192e3f7981c9c1f3e791_MD5.png]]

5、这样我们就可以将远程仓库得数据合并下来

![[00 assets/5699f8f91bc6479817a5a2a8d3553430_MD5.png]]

并且这个时候你再来查看日志得话就会发现，里面多了一条`origin/master`

![[00 assets/4cbf67c40c17fd6bdeb5b44be0e9feea_MD5.png]]

## 7.4 push 默认行为

问题：我们在`github`中创建了一个仓库，也是按照`本地仓库`插入到`远程仓库`得操作，但是我得本地仓库默认是`master`，但是现在`github`默认是`main`，所以就会出现下面得冲突，即便我们设置了上游分支也是不行

![[00 assets/48957302548165e185e209613d5ab101_MD5.png]]

1、我们查看`git`文档就可以知道，现在`Git`得默认提交是按照`simple`来处理得

2、其中`simple`表示`推送远程设备上同名的当前分支`。也就是说你本地仓库叫做`master`，那么远程仓库也需要叫`master`。所以上述出现得问题其实就是`git push`默认为`git push origin master:master`了，但是远程仓库并没有`master`所以导致报的错

![[00 assets/c8d45c1cbb5baa438a0cc7b532196e0f_MD5.png]]

3、所以我们将`git push`设置为`upstream`即可，跟随上游分支就行。其中没加`--global`就是局部设置

![[00 assets/c3735c7dfdff054b8aa10112326cea06_MD5.png]]

4、`push.default`还存在`current`，表示按照当前分支来处理，比如当前分支为`dev`，那么`git push`就会按照`dev`来上传，假如远程仓库没有得话，就会在远程仓库创建一个`dev`分支

## 7.5 操作总结

![[00 assets/7438b90acaaea1ad9f4411c8333775ff_MD5.png]]

1、对于远程仓库得使用分为下面得 2 种情况，和 2 种方案，其中`方案二`不是经常使用，只在初始化创建得时候使用

2、一般我们公司开发得时候在使用`git push`之前最好再使用一次`git pull`来获取最新得代码，然后再使用`git push`上传

![[00 assets/2d073dd1b6891aea52ab429554972cdf_MD5.png]]

# 8. 开源协议

1、一般比较大型得项目就是`MIT`协议

![[00 assets/fd2bccbc68eb5321ad18174a13a12929_MD5.png]]

# 9. tag 管理

## 9.1 创建 tag

![[00 assets/ec9e392907e7a08ab6cece9232811b50_MD5.png]]

1、其实就可以理解为`版本管理`，可以看下`Vue`得`tag`处理

![[00 assets/137eaecfa1329460892bd9e63977d3b2_MD5.png]]

2、其中`git tag v1.1 -m "xxx"`中`-m`后面得注释会在`git`中进行显示

![[00 assets/ae6d8fba92ff439ebe2f8cada8d76ec0_MD5.png]]

3、在`push`得时候，只有标注了`tag`才能`push`上去，比如`git push origin --tags`才能在`github`上看到。并且`git push origin v1.1`表示只上传`1.1`得版本，使用`git push origin --tags`就是上传所有得`tag`版本

4、如果需要查看`tag`得话可以使用`git show xxx`，跟上`tag`号。要查看所有得`tag`得话，就用`git tag`来查看

![[00 assets/2e304399714ec096a30dc2abf62d0eab_MD5.png]]

## 9.2 删除 tag

我们删除了`远程仓库`中得`tag`，但是本地仓库得`tag`依然存在

![[00 assets/cdbdebdb54e04b118211a314d24585c2_MD5.png]]

## 9.3 检出 tag

![[00 assets/ef95570a7672588b5a504e54bb147d5f_MD5.png]]

如果需要`检出tag`得话也只是回到了你指定得版本

![[00 assets/a64630d44b35c34de8ee1e42b91e43ef_MD5.png]]

切换`tag`得话，文件夹中得文件也会发生相应得变化

![[00 assets/b63f84b7770617a1331a92555e5f63be_MD5.png]]

你切换了`tag`，但是最好不要做修改。你要修改得话就使用`git switch`，这样就会重新创建一个分支

## 9.4 tag 原理

其实在`tags`文件夹中，就存着每个`tag`对应的文件，使用`git cat-file -p xxx`就可以看到`tag`中存在一个`object 26a4...`的值指向的就是每个`commit`

![[00 assets/f951d62cfe13dbbe5ebd12194939a178_MD5.png]]

其实对应的就是下面这张图，其中详细的解析查看`10.提交对象`

![[00 assets/e5a95453ae0199bbcb39bd2a12d59c4b_MD5.png]]

# 10. 提交对象

![[00 assets/2d3a6cbedc5bab4992d6c21870b4194a_MD5.png]]

1、首先我们使用`git add .`得话就会多出 2 个文件对应得就是`index.html`和`main.js`，这就叫做存入`暂缓区`

![[00 assets/b5c753bee37a3e2f3f481b2bc0609085_MD5.png]]

我们再使用`git commit -m "xxx"`得话，又会多出 2 个文件

![[00 assets/61b3ebe0ac3e4b320be654b3e430b75e_MD5.png]]

2、这个时候我们使用`git cat-file -p xxx`来查看得话就会知道答案，其中`xxx`就是文件计算之后的散列值。根据出来的信息就可以知道其实本质就是一个`树结构+链表`组成了整个`git版本`，详细查看我开始放在上面的图

![[00 assets/a0289b7b6ce10d6415f72ba8860b7eaa_MD5.png]]

3、如果这个时候我们修改`main.js`的话也会同时修改`tree`里面的值，这样就组成了`git`的变化

![[00 assets/026261a46d8700de56b93b431f5ac3c9_MD5.png]]

4、并且`refs/heads`文件夹中的`master`也是一直指向最新的`commit object`

![[00 assets/613079afdf08e576430aa12aed17ae0d_MD5.png]]

# 11. 分支管理

## 11.1 master 分支

其实我们默认创建的仓库就存在一个分支，他就是`master`分支。在`github`现在改成`main`分支了

![[00 assets/ad34751cdb4cfbc08bb8452488ede092_MD5.png]]

## 11.2 创建分支

![[00 assets/ae9286d0c30c9686d0584f405d6b8ae5_MD5.png]]

我们使用`git branch xxx`来创建分支，使用`git checkout xxx`来修改`HEAD`指针

![[00 assets/cc3d2494a76f67e139b89b50b1f386b8_MD5.png]]

![[00 assets/6f0cac4829ca3e990a2937d4f612817b_MD5.png]]

1、我们使用`git checkout`修改了`HEAD`的指向之后对该分支中的代码进行提交就会衍生出一个新的分支

2、我们再使用`git checkout`来切换为原本的分支之后文件也会变为一开始的分支内容

![[00 assets/be6cff280505728255516cc00183fffc_MD5.png]]

3、使用`git checkout -b xxx`就会创建该分支，并且切换为该分支

![[00 assets/8e14fa5bb0a1db8b949cda5ae9d371bd_MD5.png]]

## 11.3 分支作用

![[00 assets/40f66b6def76b8283f92292b4b7a7042_MD5.png]]

![[00 assets/406788c8e3b8072fcad7442312f09a43_MD5.png]]

1、上面论述了`分支`的作用，下面是演示的命令

```bash
// 版本迭代到v1.0.0
$ git init

$ git add .
$ git commit -m "111"

$ git add .
$ git commit -m "222"

$ git add .
$ git commit -m "333"

$ git log --pretty=oneline --graph
* 910e8747f5c4ac7c1f5f9f128357cecc5909d0ac (HEAD -> master) 333
* f65fd6c7164081a791889757f8bae0f729ced6cc 222
* ea7496a6fc5142fdc2356d737f4750f837ba912d 111

$ git tag -a v1.0.0 -m "正式版本1"
```

```bash
// 继续在v1.0.0的基础上迭代更新
$ git add .
$ git commit -m "444"

$ git add .
$ git commit -m "555"

$ git log --pretty=oneline --graph
* f86d7dcca49f2d66237f731b7e9c67a6151c17ba (HEAD -> master) 555
* fe0f732ab994fe3d437c7eb8ea7f6db06e5c9291 444
* 910e8747f5c4ac7c1f5f9f128357cecc5909d0ac (tag: v1.0.0) 333
* f65fd6c7164081a791889757f8bae0f729ced6cc 222
* ea7496a6fc5142fdc2356d737f4750f837ba912d 111
```

```bash
// 切换到v1.0.0的版本，修复bug
$ git checkout v1.0.0

$ git checkout -b hotfix

$ git add .
$ git commit -m "修复bug"

$ git add .
$ git commit -m "修复bug1"
```

2、在使用`git merge hotfix`的时候会出现下面的选项是提醒你代码冲突的，根据情况来处理。该冲突一般很少出现，公司中是分配任务来编写代码的，所以一般很少修改别人的代码

```bash
// 切换分支到master,并且合并分支hotfix到主分支master
$ git checkout master

$ git merge hotfix

$ git add .
$ git commit -m "完全修复v1.0.0的bug"

$ git add .
$ git commit -m "666"

$ git log --pretty=oneline --graph
* 4c0646cfc42838d2fa066dcc4061be701383ecbc (HEAD -> master) 666
*   f36f64d12e7b8310542833b54cb846463320571b 完全修复v1.0.0的bug
|\
| * ef9a9e18656d73ee79c3555c08fe1cb6598c1a8a (hotfix) 修复bug1
| * 1f49e4d2b724a765ecf0ae847451eda0ec169212 修复bug
* | f86d7dcca49f2d66237f731b7e9c67a6151c17ba 555
* | fe0f732ab994fe3d437c7eb8ea7f6db06e5c9291 444
|/
* 910e8747f5c4ac7c1f5f9f128357cecc5909d0ac (tag: v1.0.0) 333
* f65fd6c7164081a791889757f8bae0f729ced6cc 222
* ea7496a6fc5142fdc2356d737f4750f837ba912d 111
```

![[00 assets/cc55510dc2067a9fb9bf2a1684037166_MD5.png]]

3、我们按照`git log --prettty=oneline --graph`来查看的图结构是按照前面的`*`来区分分支的

![[00 assets/3c6fdd879a8d3d8c3edaf4b4b62e7bfc_MD5.png]]

4、使用`git merge hotfix`的时候就会在后面提交的`commit`添加 2 个`parent`指向两条路

![[00 assets/b777ccb4abe005b78bb087f0a40f2996_MD5.png]]

## 11.4 查看删除分支

![[00 assets/da8de1a3156efc51dc947697ee3ad2d7_MD5.png]]

## 11.5 git 工作流

![[00 assets/eb02cb5ad98af50e1f1cc1902faf5687_MD5.png]]

下面为比较常见的分支

![[00 assets/1052216f73162fa96bc46ace12694b45_MD5.png]]

下面为`Vue`中的`Releases`

![[00 assets/05b294e3f8a4b02b332df2e84bb28748_MD5.png]]

## 11.6 远程分支

![[00 assets/faa68e470acfd5f0f5221bc540fe35ed_MD5.png]]

1、其实远程仓库也是一个分支，如果是`github`的话，就叫做`origin/main`，而本地仓库默认是`master`分支。如果是互相操作的话就会存在冲突。

比如下面已经为本地仓库添加了`git remote add "xxx"`远程仓库，但是我们直接`git pull`的话还是不知道找远程仓库的那个分支

![[00 assets/77a3d08424409f2f9e455a9f9eb4a725_MD5.png]]

大致画图的话就是下面的形式，远程仓库的数据已经使用`git fetch origin main`下载下来了，但是本地仓库中的`origin/main分支`却和`master分支`没有建立连接

![[00 assets/ba5d0abed4b3b8f54d14a74a76ccaddf_MD5.png]]

2、所以我们使用`git merge`来合并，因为`origin/main`和`master`分支没有共同的祖先，所以需要使用`git merge --allow-unrelated-histories `来忽略没有共同祖先的问题

![[00 assets/2a1fc187c3cd0bae242458d7ff141536_MD5.png]]

3、但是我们修改了代码想要提交给远程仓库的时候又有问题了，这是因为`push`的默认行为是`simple`，就会使用本地分支的名字`master`来寻找上游分支的`main`，所以就会出现下面的问题

![[00 assets/a1ace135031afd680d0403321fb03107_MD5.png]]

所以需要使用`git config push.default upstream`来修改`push`的默认行为

![[00 assets/f5c877e7b166fb5cb3692a95e6e0b5c9_MD5.png]]

但是上面的方式是在本地仓库的名字和远程仓库的名字不一样的情况来处理的方式，如果简单来处理的话，最好就是再创建一个分支来处理，使用`git checkout --track origin/main`来创建并且跟踪该分支

![[00 assets/e8f96a841315143d67107e5e27cb28c9_MD5.png]]

## 11.7 远程分支管理

![[00 assets/4db5ac5faeb114ea11e8be2be407245a_MD5.png]]

> 推送分支到远程

我们使用`git push origin develop`将`develop`分支推送到远程仓库中

![[00 assets/3b6bbb99b59e524be80a47a8614dccd8_MD5.png]]

如果远程仓库没有的话，就会创建一个`develop分支`

![[00 assets/35f27420d951147d3ad95c97555a8881_MD5.png]]

> 跟踪远程分支

如果我们`git clone xxx`的话是默认使用`main分支`的，使用`git branch`可以发现没有其他分支

![[00 assets/dee7eee8bcd124e65bca17e29e7e6ca4_MD5.png]]

所以需要使用`git checkout develop`来创建并且跟踪该分支。这个操作执行了 3 步，第一步是检查远程是否存在该分支，第二步是在本地创建该分支，第三步是根据远程的`origin/develop`分支

![[00 assets/e29d939314a6ebd187917af31b794b57_MD5.png]]

# 12. rebase

> 使用 rebase

因为后续的开发路线很多，我们使用`git log --pretty=oneline --graph`会看到图结构，这个图结构可能不是很清晰，所以我们可以使用`rebase`来替换`base`

![[00 assets/f7ce49c4b2a472c4cfe991f3fb1c82ec_MD5.png]]

下面就是使用的方式，其实将原本的`C4`移动到`master`分支的后面，切断和`C2`的联系，这样使用`git log xxx`就是线性的

![[00 assets/268111e0b0eea30647846bc9a97e435d_MD5.png]]

也就是将左边的形式改为右边的形式来处理，原本使用`git merge`会单独再创建一个`base`

![[00 assets/fdd64bad5e8f5556a082e5d269b81138_MD5.png]]

并且要注意，要在`develop`的分支下使用`git rebase master`，表示将该分支移动到`master`分支的后面，一定要注意切换分支

![[00 assets/edd69fc51a06db8bc22f9f3464b33e41_MD5.png]]

> rebase 原理

![[00 assets/f0dc06cf519ff2d6e461c609750e691b_MD5.png]]

> rebase 和 merge 选择

![[00 assets/40631625df98f2a1b89bbdb574e0ffe0_MD5.png]]

# 13. Linux 命令

```bash
cd /d/code/git		// cd  	改变目录
cd ..				// cd.. 回退到上一个目录，直接cd进入默认目录
pwd					// pwd  显示当前所在的目录路径
ls 					// ls(ll)   都是列出当前目录中的所有文件，只不过ll(两个ll)列出的内容更为详细

touch 1.txt			// touch	新建一个文件,如touch index.js会在当前目录下新建一个index.js文件
rm 2.txt			// rm 	删除一个文件, rm index.js 就会把index.js文件删除
mkdir 1				// mkdir	新建一个目录,就是新建一个文件夹
rm -r 1				// rm -r	删除一个文件夹, rm -r src 删除src目录
					// rm -rf / 切勿在Linux中尝试！删除电脑中全部文件！

mv 1.txt text		// mv	移动文件, mv index.html src index.html 是我们要移动的文件, src 是目标文件夹,当然, 这样写,必须保证文件和目标文件夹在同一目录下

reset				// reset	重新初始化终端/清屏
clear				// clear 	清屏
history				// history	查看命令历史
help				// help	帮助
exit				// exit 退出

					// #表示注释
```

# 14. 速查表

![[00 assets/e5c18612c8cb387cc1b40303bb4765e7_MD5.png]]


# 问题记录

## 1. git pull 如何如何使用

【直接使用git pull拉代码，被同事狠狠diss了！】 https://www.bilibili.com/video/BV1McyYYtEX4/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b


> 情况一

**问题**：本地记录的是`zjh546`的账号，电脑使用的是`edu`的凭证进行提交，最后的结果是可以提交的。不仅可以提交，而且仓库提交记录中可以显示`zjh546`的信息，这是在`zjh546`的账号没有`私人仓库`授权的情况下，而`edu`账户是有的

**解决**：遇到这样的问题，最好的方式就是回退版本`git reset --hard HEAD^ `，让他回到初始的版本，然后重新用`edu`的账号进行提交

**资料**：代码回滚：[拜托，不要再问我 Git 如何回滚代码 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/137856034#:~:text=想要让Git回退历史，有以下步骤： 使用 git log 命令，查看分支提交历史，确认需要回退的版本 使用 git reset --hard commit_id 命令，进行版本回退,使用 git push origin 命令，推送至远程分支 快捷命令： 回退上个版本：git reset --hard HEAD^)

> 情况二

**问题**：公司中的项目可能需要提交源码，有的是直接`commit`，但是有的是提交`pr`的形式来合并

**解决**：进入到`github`中，`fork`一个新的仓库，然后`clone`你`fork`的仓库，编写之后进行提交，最后在主仓库中的`pr`进行合并对比提交即可

**资料**：pr 操作：[向 GitHub 等远程仓库提交 PR 具体操作 - 掘金 (juejin.cn)](https://juejin.cn/post/7196868559125200952)
