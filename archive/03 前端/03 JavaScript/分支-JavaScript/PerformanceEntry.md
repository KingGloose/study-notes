# 1 基本介绍

1、`PerformanceEntry` 是 Web Performance API 的核心对象，用于**捕获和存储与网页性能相关的各种指标数据**。它提供了标准化的方式记录浏览器在加载资源、执行脚本、渲染页面等过程中的详细性能数据，帮助开发者进行精准的性能分析。

2、每个 `PerformanceEntry` 对象代表一个独立的性能事件（如资源加载、用户自定义标记等），包含以下核心属性：
- `name`：事件标识（如资源 URL 或自定义标记名）
- `entryType`：事件类型（见下文分类）
- `startTime`：事件开始时间（高精度时间戳）
- `duration`：事件持续时长（毫秒）
- 其他类型相关属性（如资源大小、渲染时序等）

3、通过 `entryType` 区分不同性能事件：
   ```typescript
   type EntryType = 
     | 'navigation'   // 页面导航 (PerformanceNavigationTiming)
     | 'resource'     // 资源加载 (PerformanceResourceTiming)
     | 'mark'         // 自定义标记 (PerformanceMark)
     | 'measure'      // 自定义时间区间 (PerformanceMeasure)
     | 'paint'        // 渲染事件 (如 'first-paint')
     | 'longtask'     // 长任务 (Long Tasks API)
     | 'element'      // 元素渲染 (Element Timing API)
     | 'event'        // 事件处理耗时 (Event Timing API)
   ```

# 2 基本使用

1、获取图片/脚本等资源的加载耗时
```javascript
performance.getEntriesByType('resource').forEach(entry => {
	console.log(`${entry.name} 加载耗时: ${entry.duration}ms`);
});
```

2、分析 DNS/TCP/DOM 构建等阶段耗时
 ```javascript
const [navEntry] = performance.getEntriesByType('navigation');
console.log(`DOM 解析耗时: ${navEntry.domComplete - navEntry.domInteractive}ms`);
```

3、测量代码块执行时间
```javascript
performance.mark('calcStart');
// 执行复杂计算...
performance.mark('calcEnd');
performance.measure('calcTime', 'calcStart', 'calcEnd');
     
const measure = performance.getEntriesByName('calcTime')[0];
console.log(`计算耗时: ${measure.duration}ms`);
```


# 3 数据获取方式：

1、主动拉取
```javascript
// 获取所有条目
performance.getEntries();
   
// 按类型过滤
performance.getEntriesByType('paint'); // 获取渲染事件
   
// 按名称过滤
performance.getEntriesByName('https://cdn.example.com/lib.js');
```

2、被动监听，使用 `PerformanceObserver` 实时监控：
```javascript
const observer = new PerformanceObserver(list => {
    list.getEntries().forEach(entry => {
	    if (entry.entryType === 'longtask') {
	        console.warn('长任务阻塞:', entry.duration);
	    }
    });
});
observer.observe({ entryTypes: ['longtask', 'resource'] });
```



