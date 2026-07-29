# 各站点正文选择器与已知坑

按需查阅。**选择器会随站点改版失效**——失效时用 SKILL.md 里的"探选择器"片段重新找，
找到后回来更新本文件（这是知识积累，不是一次性配置）。

---

## 知乎 zhihu.com

需要登录态（纯 HTTP 请求会被 `zse-ck` JS 挑战拦成 403，实测带完整 cookie 也不行），
所以必须走真实浏览器。

| 页面类型 | URL 形态 | 正文选择器（按优先级） |
|----------|----------|------------------------|
| 专栏文章 | `zhuanlan.zhihu.com/p/<id>` | `.Post-RichTextContainer` → `.Post-RichText` |
| 单条回答 | `www.zhihu.com/question/<q>/answer/<a>` | `.QuestionAnswer-content .RichContent-inner` → `.RichContent-inner` |
| 问题页多回答 | `www.zhihu.com/question/<q>` | 遍历 `.List-item`，每项内 `.RichContent-inner` |
| 想法 | `www.zhihu.com/pin/<id>` | `.PinItem-content` |

**坑**：
- 回答默认**折叠**，`.RichContent` 上有 `is-collapsed` 类。先点"阅读全文"
  （`take_snapshot` 找按钮 → `click`）或直接执行
  `() => document.querySelectorAll('.ContentItem-expandButton').forEach(b => b.click())` 再取。
- 问题页是**无限滚动**，只加载前几条回答。需要更多就滚动后再取。
- 公式是 `<img>` 带 LaTeX 在 `alt`/`data-formula` 属性里；想保留公式要单独处理这些属性，
  否则 Markdown 里只剩图片链接。
- 图片有 `data-original`（原图）和 `src`（缩略图）之分，取 `data-original` 更好。
- 付费/盐选内容取不到，属正常，不要尝试绕过。

## 掘金 juejin.cn

- 正文：`#article-root` → `.article-viewer`
- 代码块干净，直接转 Markdown 效果好。

## CSDN blog.csdn.net

- 正文：`#content_views` → `.blog-content-box`
- **坑**：有大量广告/推荐插入正文 DOM，转换后需人工核对；部分文章有"登录后查看全文"遮罩。

## 博客园 cnblogs.com

- 正文：`#cnblogs_post_body`
- 结构干净，转换质量好。

## SegmentFault segmentfault.com

- 正文：`.article__content` → `.fmt`

## 简书 jianshu.com

- 正文：`article` → `.show-content`
- **坑**：有阅读遮罩，可能需要滚动或关闭弹窗。

## 语雀 yuque.com

- 正文：`.ne-viewer-body` → `.lake-content`
- **坑**：编辑器渲染，DOM 层级深且类名带 hash；内容懒加载，长文需滚动到底再取。

## Notion notion.so

- 正文：`.notion-page-content`
- **坑**：虚拟滚动——**只渲染视口内的块**。长页面必须逐屏滚动累积，否则只拿到一部分。

## 微信公众号 mp.weixin.qq.com

**不要用本 skill**——走 `kg-wechat`，那边有图片防盗链处理和公众号专属元信息提取，
且公众号单篇文章纯 HTTP 就能抓，不需要浏览器。

---

## 通用兜底

站点没记录时的顺序：
1. `article` → `main` → `[role="main"]` → `.content` / `#content`
2. 都不中，用 SKILL.md 的"探选择器"片段按文字量排序挑
3. 仍不行 → 可能是 iframe（先 `list_pages` 看有没有子框架）或 Shadow DOM
   （`el.shadowRoot.innerHTML`）

## 更新约定

新站点跑通后，把选择器和踩的坑加到本文件。
**优先记"坑"而不是"选择器"**——选择器容易失效，坑（懒加载/折叠/虚拟滚动/公式处理）
是结构性的，换个选择器还得面对。
