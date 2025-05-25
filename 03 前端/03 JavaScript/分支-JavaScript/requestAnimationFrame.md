# 1. 基本介绍

![[00 assets/6838ffe01e667bbe007d63f1e6a1fdd4_MD5.png]]

1、下图是表示`requestAnimationFrame`中`1s`绘制`多帧`的演示，这个调用函数的次数和你浏览器的刷新率有关系。这里也可以这样理解，对于浏览器来说，只要屏幕刷新一次就会重绘，也就会调用该函数

2、我电脑的浏览器刷新`144hz`，所以`1s`就会重绘`142帧`

![[00 assets/98bfc9006faf23b200659df6f4b06706_MD5.png]]

3、我们使用`requestAnimationFrame`函数之后，整体动画就趋于稳定

![[00 assets/1ff8312603cbe92ca40089fe9842f2b2_MD5.png]]

# 2. 基本使用

针对该 API 我封装了下述的代码，在回调函数中直接操作动画即可

```javascript
const useAnimationFrame = (animationFn, animationTime = 1000) => {
  // 类型检查
  if (typeof animationFn !== "function") {
    throw new TypeError("animationFn must be a function");
  }
  if (!Number.isSafeInteger(animationTime) || animationTime <= 0) {
    throw new RangeError("animationTime must be a positive integer");
  }

  let isFinish = false;
  const start = () => {
    let startTime = null;
   
    const animation = (currentTime) => {
      if (!startTime) startTime = currentTime;
      const progress = (currentTime - startTime) / animationTime;
     
      if (!isFinish && progress <= 1) {
        animationFn(progress);
        requestAnimationFrame(animation);
      }
    };

    requestAnimationFrame(animation);
  };

  const stop = () => {
    isFinish = true;
  };

  return { start, stop };
};


// 获取DOM元素
const element = document.getElementById("element");
const windowWidth = window.innerWidth;
const windowHeight = window.innerHeight;

// 执行动画
const { start, stop } = useAnimationFrame((progress) => {
  const x = (windowWidth - 100) * progress;
  const y = (windowHeight - 100) * progress;
  element.style.transform = `translate(${x}px, ${y}px)`;
}, 1000);

start();
```
