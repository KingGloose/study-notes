### 一、Loader 的输入
| 输入内容               | 类型/格式            | 说明                                                                 |
|------------------------|----------------------|----------------------------------------------------------------------|
| **源文件内容**          | `string` / `Buffer` | 文件原始内容（例如 `.js` 文件代码、`.css` 文件文本、图片二进制流等） |
| **Loader 上下文**       | `LoaderContext`      | 包含 `resourcePath`（文件路径）、`query`（参数）、`async` 回调等     |
| **Source Map**          | `object`             | 前序 loader 生成的 Source Map（可选）                               |
| **AST 抽象语法树**       | `object`             | 部分 loader 会传递 AST（如 `babel-loader` 之间）                    |

### 二、Loader 的输出
| 输出内容               | 格式要求             | 典型场景示例                                                                 |
|------------------------|----------------------|------------------------------------------------------------------------------|
| **JavaScript 代码**    | `string`             | 将非 JS 资源转换为 JS 模块（如 CSS 转成 `module.exports = "..."`）           |
| **AST 对象**           | `object`             | Babel 等编译型 loader 可传递 AST 给后续 loader                               |
| **二进制 Buffer**       | `Buffer`             | 处理图片、字体等二进制资源时直接返回                                         |
| **Source Map**         | `object`             | 生成转换后的 Source Map（需与输出代码同步）                                   |
| **元数据**             | `object`             | 附加资源依赖、webpack 特性标记等（通过 `this.emitFile` 等 API）               |

### 三、核心处理流程
```javascript
// 伪代码演示 loader 处理过程
module.exports = function(source, map, meta) {
  // 1. 接收输入
  const input = {
    source,   // 文件内容（字符串或 Buffer）
    map,      // 前序 Source Map
    meta      // 前序 loader 的元数据
  };

  // 2. 处理逻辑（示例：将 Markdown 转为 HTML）
  const processedHtml = markdownToHtml(source);
  
  // 3. 返回输出（必须符合 Webpack 要求）
  return [
    `module.exports = ${JSON.stringify(processedHtml)};`, // JavaScript 代码
    generateSourceMap(), // 新 Source Map
    { version: 1, dependencies: [] } // 元数据
  ];
};
```

### 四、不同类型 loader 的输入输出对照表
| Loader 类型       | 输入示例                    | 输出示例                          | 代表 loader          |
|--------------------|-----------------------------|-----------------------------------|----------------------|
| **编译型**         | ES6+ 代码                   | ES5 代码 + Source Map             | `babel-loader`       |
| **转换型**         | Sass 代码                   | CSS 文本 + import 依赖            | `sass-loader`        |
| **资源型**         | 图片二进制流                | Base64 字符串或文件路径           | `url-loader`         |
| **链式型**         | 前序 loader 的处理结果       | 进一步处理后的结果                | `postcss-loader`     |
| **元数据型**       | 原始文件                    | 资源依赖声明                      | `style-loader`       |

### 五、特殊处理模式
1. **异步处理**（处理耗时操作）：
```javascript
module.exports = function(source) {
  const callback = this.async();
  fs.readFile('dictionary.txt', (err, data) => {
    const result = source + '\n// 注入字典: ' + data;
    callback(null, result);
  });
};
```

2. **原始模式**（处理二进制）：
```javascript
module.exports.raw = true; // 声明接收 Buffer
module.exports = function(buffer) {
  return optimizeImage(buffer); // 返回优化后的 Buffer
};
```

3. **Pitching 阶段**（前置拦截）：
```javascript
module.exports.pitch = function(remainingRequest) {
  // 在正式处理前拦截（可跳过后续 loader）
  return 'module.exports = "跳过后续处理";';
};
```

### 六、调试技巧
1. 查看中间结果：
```javascript
// 在 loader 中插入调试输出
console.log('Input source:', source);
console.log('Input map:', map);
```

2. 使用 `loader-runner` 独立测试：
```javascript
const { runLoaders } = require('loader-runner');

runLoaders({
  resource: '/abs/path/to/file.txt',
  loaders: ['/abs/path/to/your-loader.js'],
  context: { /* 模拟 webpack 上下文 */ }
}, (err, result) => {
  console.log('处理结果:', result.result);
  console.log('Source Map:', result.sourceMap);
});
```

---

通过理解 loader 的输入输出机制，可以：
- 更高效地编写自定义 loader
- 合理组合现有 loader 的链式调用
- 精准定位构建过程中的文件处理问题
- 实现高级资源处理逻辑（如动态代码生成、按需编译等）