# QuillJs 换行 bug 解决方案(原始资料)

> 来源:Confluence 导出文档 `QuillJs换行bug解决方案.doc`(MHTML 格式),导出时间 2026-07-09。
> 学堂系统富文本组件相关记录,原样保留可追溯。图片未搬运(效果型截图)。

---

## 问题

学堂系统中的富文本组件底层一直是基于 QuillJs 的,但 QuillJs 原生存在一些 Bug,比如换行问题:

回显富文本时,直接忽略了 `<br>` 标签,导致如果回显单独一个视频,光标无法定位到富文本编辑器内部输入。

社区 issue:https://github.com/slab/quill/issues/4424

用底层库 quill.js 复现:

```js
import Quill from 'quill';
import "quill/dist/quill.snow.css";
import { onMounted } from 'vue';

onMounted(() => {
  const quill = new Quill("#app", {
    placeholder: "默认值",
    modules: {
      // toolbar 配置(片段)
      // [{ 'header': [1, 2, false] }],
      // ['image', 'video'],  // 添加视频按钮
    }
  });
  quill.setContents([
    {
      insert: { video: 'https://edu.zhuanstatic.com/video/xxx.mp4?mid=2404' }
    }
  ]);
})
```

现象:换行符被忽略了,导致只能选择视频,无法进入编辑。(原文此处有效果截图)

---

## 方案

直接修改底层原生库还是很费时费力的,于是准备采用一些折中的方案。根据源码的逻辑得出:注册 `br` 标签的 Blot 插件的话,就可以直接跳过忽略的逻辑。

### 具体代码

1、在 Quill 中注册 BrBlot

```ts
import { Quill } from 'react-quill-new'

const BlockEmbed = Quill.import('blots/block/embed')

class BrBlot extends BlockEmbed {
  static blotName = 'br'
  static tagName = 'br'
  static create() {
    const node = super.create()
    // node.innerHTML = "<br />"
  }
  static value(node: HTMLElement) {
    return {
      html: "<br />",
    }
  }
}
BrBlot.blotName = 'br'
BrBlot.tagName = 'br'
```

2、在 formats 中进行注册

```tsx
<ReactQuill
  formats={["br"]}
/>
```
