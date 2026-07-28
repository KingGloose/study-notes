# 从本地 Chrome 历史/书签找内容

解决一类真实场景：**主人记得"之前看过一篇讲 XX 的文章"，但想不起链接在哪。**

脚本读本地 Chrome 的历史库和书签，按关键词模糊匹配。
这是"CLI 做不到、必须写代码"的部分（读 SQLite、跨 profile、避免锁库），所以是脚本而非 CLI 组合。

## 用法

```bash
# 单关键词
python3 scripts/find-history.py "LLM Wiki"

# 多关键词（推荐）：AI 理解主人意图后自行扩展同义词
python3 scripts/find-history.py --keywords 知乎 zhihu 知识库

# 只要看起来像文章的（过滤搜索页/登录页/首页噪声）★ 找内容时基本都该加
python3 scripts/find-history.py --keywords AI Agent --articles-only

# 只要最近 N 天访问过的
python3 scripts/find-history.py --keywords 播客 --days 30 --articles-only

# 其他
--limit N      最多返回几条（默认 10）
--pretty       缩进 JSON
--chrome-home  指定 Chrome 数据目录（默认 macOS 标准路径）
```

输出 JSON：`title` / `url` / `source`(bookmark|history) / `profile` /
`last_visit_time` / `bookmark_path` / `match_score`。

## 怎么用好它（给 AI 的建议）

**1. 主动扩展关键词。** 主人说"那篇讲知识库的知乎"，别只搜"知识库"——
用 `--keywords 知识库 wiki 笔记 knowledge` 提高命中率。脚本本身不做同义词猜测
（原设计的明确决定：硬编码同义词不可扩展），语义扩展是 AI 的活。

**2. 找内容时默认加 `--articles-only`。** 不加会混进大量搜索页、登录页、站点首页。
实测搜"知乎"：不加过滤 8 条里 4 条是噪声，加了之后 3 条全是真文章。

**3. 拿到候选后和主人确认，别自己挑。** 标题相似的很多，让主人认。

**4. 时间是有力线索。** 主人说"上周看的"→ `--days 10`；"很久之前"→ 不限时间但加大 `--limit`。

**5. 结果为空时的降级顺序**：
- 换更短的关键词（`"OA 系统"` → `"OA"`）
- 试 URL 里的词（域名片段）
- 试英文/中文另一种写法
- 都不行就直接问主人要链接，别硬猜

## 隐私边界

- **只在主人要找 URL 时才跑**，不主动扫描历史。
- 只按关键词匹配标题和 URL，**不输出完整历史**。
- 默认最多 10 条。
- 不读 cookie、不写缓存、不上传任何浏览器数据。
- 历史库先复制到临时文件再只读查询（避免 Chrome 运行时锁库），用完即弃。

## 读取范围

```
~/Library/Application Support/Google/Chrome/Default
~/Library/Application Support/Google/Chrome/Profile *
```
读 `Bookmarks`（JSON）和 `History`（SQLite）。

## 匹配规则

- 大小写不敏感；自动去空格（`"OA 系统"` 能匹配 `"OA系统"`）
- 自动分词：`"OA 系统"` → `["oa系统", "oa", "系统"]`，任一命中即算
- 书签优先于历史；同 URL 保留得分高/更近的
- 完整匹配得分 10，部分匹配 5

## 与其他能力的配合

```
主人："之前看过一篇讲 XX 的知乎，帮我找出来沉淀一下"
  → find-history.py 找候选
  → 主人确认是哪篇
  → kg-zhihu（走 kg-browser 读正文）
  → 按 AGENTS.md 沉淀
```

也可用于：找回之前看过的技术博客（→ `kg-doc` 抓网页）、B站视频、播客单集。

## 跨平台

脚本默认 macOS 路径。其他平台用 `--chrome-home` 指定：
- Windows: `%LOCALAPPDATA%\Google\Chrome\User Data`
- Linux: `~/.config/google-chrome`
- **WSL 读 Windows 侧 Chrome**：`--chrome-home "/mnt/c/Users/<你>/AppData/Local/Google/Chrome/User Data"`
  （这个比 remote debugging 好办——只是读文件，不需要网络打通）
