# 1、基本介绍

## 1.1 痛点解释

1、类似 `nx、turborepo、lerna` 解决了什么问题？本质就是多 package 得问题，比如在 babel 分为了 `@babel/core、@babel/cli、@babel/parser、@babel/traverse、@babel/generator` 等一系列包
![[00 assets/8462d5257e3523d8c7cf7f5535214bed_MD5.png]]

2、如果每个包单独一个仓库，那就有十多个 git 仓库，这些 git 仓库每个都要单独来一套编译、lint、发包等工程化的工具和配置，重复十多次。工程化部分重复还不是最大的问题，最大的问题还是这三个：
	2.1 一个项目依赖了一个本地还在开发的包，我们会通过 npm link 的方式把这个包 link 到全局，然后再 link 到那个项目的 node_modules 下
	2.2 需要在每个包里执行命令，现在也是要分别进入到不同的目录下来执行十多次。最关键的是有一些包需要根据依赖关系来确定执行命令的先后顺序。6
	2.3 版本更新的时候，要手动更新所有包的版本，如果这个包更新了，那么依赖它的包也要发个新版本才行。

3、那么在项目中使用 `npm link` 的本质如下图
![[00 assets/bff668fa2d308ba5e4bc126927b6917f_MD5.png]]

4、如果是 `monorepos` 工具的话本质结构如下
![[00 assets/67b1ed1933ce60d29fd03e72ebed4ec7_MD5.png]]

5、并且对于 `yarn` 和 `pnpm`， 他们也支持 `workspace:*` 这样查找依赖就是从 workspace 里查找，而不是从 npm 仓库了
![[00 assets/21e7d0a196729c81419c3a86146ade2a_MD5.png]]

6、如果你使用 `monorepos` 另外一个大功能就是执行命令，比如你执行 `lerna run build` 的话，lerna 会按照依赖的拓扑顺序来执行命令，并且合并输出执行结果。比如 remixapp 依赖了 header 和 footer 包，所以先在 footer 和 header 下执行，再在 remixapp 下执行。
![[00 assets/e34e709db30e77c1db47da6575bf0dab_MD5.png]]

7、再就是版本更新操作，可以借助 `changeset` 来实现更新，也可以使用 `lerna` 等工具来实现

## 1.2 简单实现

^f024dc

1、这其实本质就是 monorepo 基本原理 得实现，我们需要在 `zjh-cli（右边）`引入 `zjh-cli-lib（左边）`得代码内容
![[00 assets/d41f63821a3a1d92af4cb72db42ae9f8_MD5.png]]

2、首先我们需要先编写 `zjh-cli-lib` 得内容
![[00 assets/dee0f8123dd98b072d22730e27846622_MD5.png]]
然后使用 `npm link` 来做链接，他会在全局库中做引用
![[00 assets/ef53fca6e056c09fb6ff88ebe6f1a379_MD5.png]]

3、在 `zjh-cli` 中再来执行 `npm link zjh-cli-lib`，然后导入就可以看到了
![[00 assets/077053bba63bb4c8b2216de49d99d716_MD5.png]]

## 1.3 npm link 本质

![[00 assets/88d6b4f224fe391ca025ecdd8da7fdb9_MD5.png]]

针对 `npm link` 的本质就是软链接，可以参考 [[22 Monorepos#^f024dc]]，在全局库中图标的左下角出现了箭头的标识
![[00 assets/6bebd577a812e8b10b6a695a61da79a2_MD5.png]]

# 2. lerna

## 2.1 基本介绍

![[00 assets/7227f4a3f94102d1e3eb4263b50aeee1_MD5.png]]
![[00 assets/f33cf5c63e1d65ebab85f18bb3a79c50_MD5.png]]

具体可以参考，但是针对脚手架来说，多包管理要怎么做，可以参照如下流程
![[00 assets/0f86f46999a495781dc9cfebe1726139_MD5.png]]
![[00 assets/b09a150c0016250bb19c06c7bec4cf56_MD5.png]]
![[00 assets/527b35b6085c2042b70c5321c6d80e01_MD5.png]]

## 2.2 基本使用

因为 lerna 目前已经几乎被 **nx** 所替代，所以暂不做过多的记录

**废弃说明**：[Legacy Package Management | Lerna](https://lerna.js.org/docs/legacy-package-management#migrating-from-lerna-bootstrap-lerna-add-and-lerna-link-in-lerna-v7-and-later) | [Lerna and Nx | Lerna](https://lerna.js.org/docs/lerna-and-nx)

> lerna init

因为版本的变迁，lerna 很多功能都已经交给了包管理工具，我们使用 7+ lerna 会提示让我们自己设置 workspace，这个参考各个包管理工具的实现即可
![[00 assets/5143e3eb059672ff9f6027f1f4c2984a_MD5.png]]

> lerna create

我们输入 `lerna create [name]` 表示创建一个 package，然后依次输入必要内容即可
![[00 assets/07ec89f956e19fb6876edaa4584b4a3e_MD5.png]]

**lerna add、lerna bootstrap、lerna link 已经被废弃了，所以可以使用 npm、yarn、pnpm 来替代**
![[00 assets/8a824b803097b76a9016443baa35c29c_MD5.png]]

> lerna add（被废弃）

在我们使用了 `npm workspace` 之后，在需要引入的库中手动书写引入依赖，再来执行 `npm i`即可实现自动引入
![[00 assets/a831c1e152527081ff0644db779865b0_MD5.png]]
如果是本地开发的话最好使用 `*` 就行，在后续发布的时候会被自动替换为具体的版本号
![[00 assets/80805d7cc879ac8c804ef33a2e28ed76_MD5.png]]

> lerna changed

代表哪些 package 会将被发布
![[00 assets/186f45a67f1009c14a4bded75d49ae98_MD5.png]]

> lerna publish

用于发布该库到 npm，如果你使用的名字为 `@my-cli/core` 那么 `@my-cli` 会作为组织名，而 `core` 是作为包名

> lerna exec shell（执行脚本）

`lerna run build` 会按照依赖的拓扑顺序来执行命令，并且合并输出执行结果
![[00 assets/9b4e599be2f8fd4a97e6b8cadbafc876_MD5.png]]

# 3. yarn + changest

^2bdf54

1、初始化如下的仓库，如果你写了`workspaces`一定要写`private:true`防止根目录被意外发布，`Monorepo` 的根目录本身不是一个可发布的包，它只是一个容器
![[00 assets/4323cb01394267371a05da2b4a53cb3a_MD5.png]]

2、输入 `npm init -w packages/core -y` 就会自动创建 `package.json` 并且在 `package-lock.json` 中建立索引，而且在 `node_modules` 中会有对应的软链接
![[00 assets/f43746f8b4969414c840f740710b8560_MD5.png]]

3、再来输入 `yarn` 来建立索引，如果你修改了 `package.json` 中的 `name` 的话记得再输入一次 `yarn`
![[00 assets/8505612981b1a987e23bca05501177d5_MD5.png]]

4、输入来添加 `yarn workspace @yarn-mono-test/cli add @yarn-mono-test/core@1.0.0`，这里必须指明版本号才会安装本地 packages 下的另一个包为依赖，不然会从 npm 仓库来查找依赖。这是`yarn workspace` 的一个[历史 bug](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyarnpkg%2Fyarn%2Fissues%2F3973 "https://github.com/yarnpkg/yarn/issues/3973")。
![[00 assets/8fb7b1d3ccf65d1a9e91c5bd1692d638_MD5.png]]

5、我们再来打印输出一下是否正确
![[00 assets/ddf25dbc87dd211bed7ef8250694266d_MD5.png]]

6、我们可以在根目录安装库，这样全局几乎都可以使用
![[00 assets/55441281b5c3eddf9b21d4cbe5fedf3e_MD5.png]]
也可以为每个 package 单独安装库 `yarn workspace @yarn-mono-test/cli add chalk commander`
![[00 assets/e5d3c0013464ea4191a0c0f8fb068300_MD5.png]]

7、现在用的 cli、core 的包名太容易冲突了，一般 monorepo 的包都是用 @scope/xxx 的命名方式，比如：`@babel/cli` 来实现
8、后续就是对应的发包流程，我们需要填写`"publishConfig": {"access": "public"}` 来表示为公共的
![[00 assets/c1970a401a17ad2c73a91382471dac42_MD5.png]]

9、因为我们使用 `@scope/xxx` 的模式来发包，那么需要在 npm 中创建自己的组织，再来发布即可
![[00 assets/99845c769d07dbf9dc3ee76bb67a2345_MD5.png]]

10、`yarn workspace @guang-yarn/core run build` 和 `yarn workspaces run build` 分别执行单个 package、每个 package 中得 `scripts` 中得内容
![[00 assets/e9a4c43287738dc78c5207065732cdeb_MD5.png]]

11、我们可以使用 `changeset` 来实现版本控制，在根目录输入 `yarn add --dev -W @changesets/cli prettier-plugin-organize-imports prettier-plugin-packagejson`再输入`npx changeset init`
12、因为 `changeset` 是基于 `git` 来做记录得，所以需要初始化 `git`，并且需要提交
13、我们先输入 `npx changeset add`，changeset 就是一次改动的集合，可能一次改动会涉及到多个 package，多个包的版本更新，这合起来叫做一个 changeset
![[00 assets/4a1fbb6e081842a441ff6a4258b973d6_MD5.png]]
这时你就会发现在 .changeset 下多了一个临时文件记录着这次变更的信息：
![[00 assets/c733c1bbd3005cf6cef0c60f6d1fc9a5_MD5.png]]

14、然后你可以 `npx changeset version` 命令来生成最终的 `CHANGELOG.md` 还有更新版本信息
![[00 assets/0cd4feff8548f55ffb04134f9274cf94_MD5.png]]

15、再输入 `npx changeset publish` 来发送到 `npm`
![[00 assets/4c1eb74a324ffcf4a4315bf277d0998d_MD5.png]]
这个发布还会为 `git` 打上 `tag`，使用 `git tag --list`
![[00 assets/7e1f67a9e45ebda898a8c67aa64f6c31_MD5.png]]

16、如果你使用 `yarn workspace info`可以查看本地的包的依赖关系
![[00 assets/0425a2c28a10754d145a18f5cbd64de6_MD5.png]]

# 4. pnpm + changeset

**目前文章是基于 yarn + changeset 来做得修改 [[22 Monorepos#^2bdf54]]，所以下面只叙述差异点**

1、`workspaces` 编写位置不同，需要单独写一个 `pnpm-workspace.yaml`，这里的 `package.json` 直接使用 `npm init -y` 就行，不需要使用 `npm init -w packages/core -y`
![[00 assets/8daa24def0598b8c10fbdf102edec05f_MD5.png]]

```yaml
packages:
  - 'packages/*'
```

2、使用 `pnpm --filter @pnpm-mono-test/cli add @pnpm-mono-test/core --workspace` 为 `@pnpm-mono-test/cli` 添加 `@pnpm-mono-test/core`
3、其中 `--filter` 指定在哪个包下执行 add 命令，`--workspace` 就是从本地查找
4、这里 `workspace:` 前缀就是`本地的 workspace` 的意思
5、可以看到在 `packages/cli` 包下的 node_modules 多了一个 core 的软链。`yarn workspace` 是放在根目录下，而 pnpm 是放在 workspace 目录下，都可以。node 查找依赖会从当前目录一层层往上查找 node_modules，所以都能找到。可以看到，就是从 `packages/core` 软链过来的：
![[00 assets/e9d172d880fb12e3f474486c72a775b2_MD5.png]]

6、`pnpm add typescript @types/node -w --save-dev` 加上 `-w` 才能在根目录安装依赖

7、使用 `pnpm -r exec npx tsc`，`-r` 是递归的意思
![[00 assets/863bb0a26fdd4c20288fef97a0326af0_MD5.png]]
8、或者使用 `pnpm -r --no-sort npx tsc`，他会按照拓扑顺序执行
![[00 assets/b4ac7ff011ef0e926bfa88625afa905a_MD5.png]]

9、`pnpm --filter @pnpm-mono-cli/cli exec npx tsc --init` 表示在 `@pnpm-mono-cli/cli`下面执行指令

# 5. npm + changeset

1、`workspaces` 步骤和 `yarn` 基本一致
![[00 assets/da705da6289bda2b7de5fd934c294d5b_MD5.png]]

2、使用 `npm i --workspace @npm-mono-cli/cli @npm-mono-cli/core` 来为 `cli` 安装 `core`
3、使用 `npm i --workspace @npm-mono-cli/cli chalk commander` 为 `cli` 安装 `core`、`commander`
![[00 assets/f635238684eb0dfb0e01412231af8f40_MD5.png]]

4、使用 `npm exec --workspaces -- npx tsc` ，`--workspaces` 是所有 workspace 都执行这个命令
5、`npm exec --workspace @npm-mono-cli/cli -- node ./dist/index.js add 1 2` 单独执行命令



# 6、nx

# 7、Turborepo
