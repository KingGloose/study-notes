# 1、Jest

## 1.1 基本介绍

1、Jest 有如下的优势项目，而且还有很多的插件项目

![[00 assets/ba6f131592f20af525aace43d82371f6_MD5.png]]

## 1.2 基本使用

1、如果你运行的话，是不支持 ECMA 的模块导入的，如果使用的 CommonJS 模块倒是正常。所以我们需要做一些额外的操作
2、`npm i jest --dev` 来安装 自动化测试 工具
3、`npm install --save-dev @babel/core @babel/preset-env babel-jest` 安装 babel 来做转换
4、在项目根目录下创建一个名为 .babelrc 的文件，并添加以下内容

```javascript
{
  "presets": ["@babel/preset-env"]
}
```

5、确保你的 package.json 中包含 Jest 的配置，或者创建一个单独的 jest.config.js 文件。在 package.json 中，你可以添加如下配置：

```javascript
// package.json
{
  "jest": {
    "transform": {
      "^.+\\.jsx?$": "babel-jest"
    }
  }
}

// jest.config.js
module.exports = {
  transform: {
    "^.+\\.jsx?$": "babel-jest"
  }
};
```

6、执行 `npx jest` 即可实现测试功能
![[00 assets/69e261b5fe8f8822502e17569dd59ab7_MD5.png]]

## 1.3 基础配置

### 1.3.1 collectCoverage / coverageDirectory

1、`collectCoverage` 这是用于做测试覆盖率，
2、`coverageDirectory` 是测试文件夹，他会将覆盖率报告放在这个填入的文件夹中（coverage）中
![[00 assets/c3e9a1a66891c3477fd90fb43970cb09_MD5.png]]
3、这样我们就有对于的代码覆盖率报告
![[00 assets/2f874d2975b26f3cf30d0355625d2fd3_MD5.png]]

## 1.4 匹配器

> Base

1、`toBe` 的本质就是 `Object.is` 和 `===`，针对对象会比较引用地址
2、`toEqual` 是匹配值相等

> null、undefined

1、`toBeNull` 判断是否为 null
2、`toBeUndefined` 判断是否为 undefined
3、`toBeDefined` 判断是否定义过，和 `toBeUndefined` 正好相反

> true、false

1、`toBeTruthy` 判断是否为 true
2、`toBeFalsy` 判断是否为 false
3、`not` 取反
![[00 assets/50a232676254bfeb934eb759e0fe3038_MD5.png]]

> <、>、>=、<=

1、`toBeGreaterThan` 是 >
2、`toBeLessThan` 是 <
3、`toBeGreaterThanOrEqual` 是 >=
4、`toBeLessThanOrEqual` 是 <=
5、`toBeCloseTo` 判断浮点数字比较，比如：0.1 + 0.2 = 0.3
![[00 assets/c62c9a1aa5a9b67c6f89c63211d823c9_MD5.png]]

> String

1、`toMatch` 是否包含，里面可以直接写字符串或者正则表达式
![[00 assets/eb228db4c5b20028338d6327a94d5e99_MD5.png]]

> Array、Set

1、`toContain` 是否包含
![[00 assets/309fb8284145f7a7f9150a4489e4659e_MD5.png]]

> Error

1、`toThrow` 判断异常
![[00 assets/5763ebaf5ad312acdc30b9c7d7b25d52_MD5.png]]

## 1.5 命令行
