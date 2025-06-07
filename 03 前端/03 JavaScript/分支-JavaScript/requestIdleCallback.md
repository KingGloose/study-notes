[requestIdleCallback - Web API | MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/requestIdleCallback#%E8%AF%AD%E6%B3%95)

这个方法可以允许你在闲时去执行回调，但是他不支持 safari 浏览器

1、`window.requestldleCallback()`方法插入一个函数，这个函数将在浏览器空闲时期被调用
要弄懂`requestIdlecallback`函数，其实最主要的是要清楚，浏览器在一帧里面做了什么？

2、帧：由于现在广泛使用的屏幕都有固定的刷新率（比如最新的一般在60HZ），在两次硬件刷新之间浏览器进行两次重绘是没有意义的只会消耗性能。浏览器会利用这个间隔16ms（1000ms/60）适当地对绘制进行节流：因此16ms就成为页面渲染优化的一个关键时间。在这段时间内，浏览器需要完成如下事情：
- 脚本执行（JavaScript）：脚本造成了需要重绘的改动，比如：增删DOM、请求动画等
- 样式计算（CSS Object Model）：级联地生成每个节点的生效样式
- 布局（Layout）：计算布局，执行渲染算法
- 重绘（Paint）：各层分别进行绘制
- 合成（Composite）：合成各层的染结果Web

3、一帧里事件执行顺序
- 用户事件
	- 阻塞输入事件，如 `wheel`、`touch` 等。
	- 非阻塞输入事件，如 `click`、`keypress` 等
- 宏任务 + 微任务
	- 先执行宏任务
	- 每个宏任务执行完后，会执行宏任务中产生的微任务
	- 如果微任务中还有微任务，那么添加到微任务队列后，继续执行微任务
	- 微任务执行完成后，可能会继续执行另一个宏任务（一帧里可以执行多个宏任务），也可能进入后续渲染阶段
- begin frame
	- window.resize
	- scroll
	- mediaquery changed（媒体查询）
	- animation events（动画事件）
- requestAnimationFrame回调（在每次渲染之前执行，丢帧时不执行）
- 浏览器渲染过程
	- 样式计算
	- 布局
	- 重绘
	- 合成
- requestIdleCallback回调（空闲时间）
![[00 assets/9c61961bedc2b9f08b6f28304ebf0f94_MD5.jpeg]]



