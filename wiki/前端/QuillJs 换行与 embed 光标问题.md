# 1. QuillJs 换行与 embed 光标问题

> 项目背景:学堂系统富文本组件底层是 QuillJs。回显富文本时遇到 `<br>` 被忽略、单独视频/图片后光标无法定位进编辑器的问题。
> 原始资料:[[../../raw/QuillJs换行bug解决方案-原文.md]]

---

## 1.1 现象

回显一段富文本时,如果内容是「单独一个 video embed」,光标无法定位到编辑器内部,只能选中视频块,进不了编辑状态。

复现最小 delta:

```js
quill.setContents([
  { insert: { video: 'https://.../xxx.mp4' } }
])
```

社区 issue:https://github.com/slab/quill/issues/4424

---

## 1.2 根因(AI 补充)

这个问题的根因**不在「`<br>` 被忽略」这个表象**,而在 Quill 的文档模型:

1. Quill 用 **`\n` 作为块分隔符**,模型里没有「独立 `<br>` 软换行」这个原生概念——换行在 Quill 里是块级的。
2. **Quill 文档必须以 `\n` 结尾。** 上面的 delta 只塞了一个 video embed、后面没有任何文本行,于是「视频后面没有可落脚的编辑行」,光标自然进不去。

所以「`<br>` 被吞」和「光标进不去」其实是同一个模型特性的两个侧面:外部 HTML 里的软换行 `<br>` 进到 Quill 后无处安放,而 embed 后缺少 `\n` 行导致无落脚点。

---

## 1.3 笔记原方案:注册 BrBlot(治标 workaround)

思路:不改底层库,注册一个 `br` 标签的 Blot,让 Quill 不再忽略它。

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
    return { html: "<br />" }
  }
}
```
```tsx
<ReactQuill formats={["br"]} />
```

### 1.3.1 评估结论

**能解决眼前的光标问题,但属于治标,且原代码有一个会直接报错的 bug + 若干副作用。**

- ❌ **`create()` 没有 `return node`。** Parchment 的 `create()` 必须返回 DOM 节点(Quill 拿它挂到文档树)。原代码只创建不返回,渲染到该 blot 就会挂。这段照抄跑不起来——要么记录时漏了 `return node`,要么当时没真正验证过。**用之前必须补 `return node`。**

- ⚠️ **语义拧了。** BlockEmbed 是「视频/图片」这种块级、原子、不可编辑的嵌入体。把 `<br>` 做成 BlockEmbed = 一个换行独占整块、内部不可编辑,和「换行」的轻量语义对不上。更像「塞个占位块让光标有地方待」,而非真正修复换行。

- ⚠️ **存量数据可移植性变差(最要命)。** 注册后 delta 里会出现 `{ insert: { br: {...} } }` 这种私有 format。服务端渲染 / 不认识该 blot 的其他 Quill 实例 / 官方 `getSemanticHTML()` 导出时,这段会无法识别或丢失。等于为了修回显,在存储数据里埋了「只有本项目这套注册逻辑才能正确回显」的私有格式,换环境又坏。

- ⚠️ **两个 Quill 来源混用。** 复现代码 `import Quill from 'quill'`,方案代码 `import { Quill } from 'react-quill-new'`。若项目里存在两份 Quill 实例(版本/引用不一致),`Quill.import('blots/block/embed')` 拿到的基类和实际渲染用的可能不是同一个,会出现「看着注册了但不生效」。需保证**全项目只有一个 Quill 实例来源**。

---

## 1.4 更干净的替代方案(AI 补充)

针对「embed 后光标进不去」这一具体症状,优先在**数据层归一化**,而不是造 blot。

### 1.4.1 方案 A:回显时保证 embed 后有空行

```js
quill.setContents([
  { insert: { video: '...' } },
  { insert: '\n' },   // ← 给光标一个落脚点,delta 以 \n 结尾
])
```

### 1.4.2 方案 B:用 clipboard matcher 把 `<br>` 归一化成 `\n`

```js
import Delta from 'quill-delta'
quill.clipboard.addMatcher('BR', () => new Delta().insert('\n'))
```

这两种做法存下来的 delta 是**标准格式**,换环境、走服务端渲染、用官方 API 导出都不会坏。

---

## 1.5 选型建议

| 真实诉求 | 推荐做法 |
| --- | --- |
| 只是「视频/图片后进不去光标」 | 数据层补 `\n`(1.4.1),最小最稳,无副作用 |
| 需要「HTML 里的 `<br>` 原样无损往返」 | BrBlot 方向对,但必须①补 `return node` ②约定所有读写端走同一套注册,并评估存储兼容性 |

结论:多数场景真实诉求是「能编辑就行」,那么 BrBlot 属于**用偏重的手段解决了一个能轻量解决的问题**。先确认诉求是「无损保留 `<br>`」还是「只要能编辑」,再决定用哪条路。

> 以上评估是「AI 建议」,不是定论。QuillJs 版本演进较快,注册 blot 的 API 细节以实际版本源码为准,最终由主人判断拍板。
