# npm 依赖冲突问题(原始资料)

> 来源:Confluence 导出文档 `npm依赖冲突问题.doc`(MHTML),导出时间 2026-07-09。
> 学堂系统接入 zant-ui 富文本组件时的依赖冲突记录。原文文字较简略,关键代码在截图里,已转成文字/代码块。

---

## 问题

> 如果想要用一个对等包依赖与当前包依赖冲突不兼容的库,并且充分评估了接入成本,或许下面的内容能有所帮助。

在学堂系统中接入新改的 zant-ui 的富文本组件时,由于学堂的 antd 版本(v4)和 zant-ui 的版本(v5)不兼容,导致依赖冲突。

### 实际现象

- npm 安装时默认会报错并终止。
- pnpm 通过内容寻址和符号链接去进行包的隔离,非严格模式不会因对等依赖冲突而拒绝安装,仅警告且不影响安装(两个版本共存);**但实际链接还是会链接项目根目录的 antd 版本,而不是 zant-ui 的 node_modules 中的版本**。下面是用 pro-components 的 lock 文件链接的一个例子:

```
'@ant-design/pro-components@3.0.2-0(@types/react@19.2.6)(antd@4.24.16(react-dom@19.2...
  dependencies:
    antd: 4.24.16(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
```

(pro-components 声称依赖 antd,但被解析成了根目录的 antd@4)

---

## AI 建议的可用方案(文档记录的截图)

### 方案 1:使用 pnpm 的严格模式

在 package.json 中配置:
```json
{
  "pnpm": {
    "peerDependencyRules": {
      "strictPeerDependencies": true
    }
  }
}
```
> 这样 pnpm 会拒绝安装,或者强制安装正确的版本。

### 方案 2:使用 pnpm 的 publicHoistPattern
```json
{
  "pnpm": {
    "publicHoistPattern": ["*antd*"]
  }
}
```
> 但这可能不会解决根本问题。

### 方案 3:使用 resolutions 或 overrides 强制版本(pnpm)
```json
{
  "pnpm": {
    "overrides": {
      "@ant-design/pro-components>antd": "^5.27.6"
    }
  }
}
```
> 这样会强制 @ant-design/pro-components 使用 antd@5.x。

### 方案 4:使用 npm/yarn 的 resolutions
```json
{
  "resolutions": {
    "@ant-design/pro-components/antd": "^5.27.6"
  }
}
```

---

## 最终采用的方案(两步组合)

### 1、通过 package.json 的 resolutions 强制保留冲突的版本
```json
{
  "resolutions": {
    "@zz-common/zant-ui/antd": "^5.24.0"
  }
}
```

### 2、通过 chainWebpack 配置控制解析规则(vite 中去查找对应的 babel 配置)
```js
// 为 @zz-common/zant-ui 配置 antd 解析, 使其使用自己的 antd 5.x 版本
const path = require('path')
const zantUiAntdPath = path.resolve(
  __dirname,
  '../node_modules/@zz-common/zant-ui/node_modules/antd'
)
// 使用 NormalModuleReplacementPlugin 替换 zant-ui 中的 antd 引用(包括 antd/xxx 子路径)
const webpack = require('webpack')
config.plugin('ReplaceZantUiAntd').use(webpack.NormalModuleReplacementPlugin, [
  /^antd(\/.*)?$/,
  (resource) => {
    // 如果是从 zant-ui 内部发起的 antd 导入, 使用 zant-ui 自己的 antd
    if (resource.context && resource.context.includes('@zz-common/zant-ui')) {
      const match = resource.request.match(/^antd(\/.*)?$/)
      const subPath = match ? match[1] || '' : ''
      resource.request = zantUiAntdPath + subPath
    }
  },
])
```
