# 1. Obsidian 插件开发入门(实战索引)

> 给未来的自己:下次再做 Obsidian 插件时,翻这一页就能快速上手,别再重新踩一遍坑。
> 首次实践见 [[Obsidian webview 登录态注入]](Session Bridge 插件),cookie 解密细节见 [[浏览器 Cookie 本地存储与登录态搬运]]。
> 标注:[实测] = 我在 Session Bridge(2026-07,macOS,Obsidian 1.8.10)亲手验证过 / [AI 补充] = 通用知识,细节问 AI 或查官方 docs。
>
> 官方文档:<https://docs.obsidian.md> · 官方模板:`obsidianmd/obsidian-sample-plugin`

---

## 1.1 骨架速查(通用部分,当模板用)

### 1.1.1 三件套 + 分发规则

一个插件运行时**只需要三个文件**放进 `<vault>/.obsidian/plugins/<id>/`:

```
main.js          # esbuild 打包产物(唯一执行入口)
manifest.json    # 元信息:id / name / version / minAppVersion / isDesktopOnly
styles.css       # 可选,插件样式
```

[实测] **社区分发也只发这三个文件**(release 附件)。源码留在 GitHub,`main.js` 不进仓库(靠 gitignore),只作为 release 产物。这条规则直接决定了一个大坑,见 1.2.2。

### 1.1.2 manifest.json 关键字段

```json
{
  "id": "session-bridge",              // 唯一 id,目录名必须和它一致
  "name": "Session Bridge",
  "version": "0.1.0",                  // 语义化版本,tag 名和它一致(不带 v)
  "minAppVersion": "1.8.7",            // 你用到的 API 决定它,lint 会校验
  "description": "...",
  "author": "...",
  "authorUrl": "...",
  "isDesktopOnly": true                // 用了 Node/Electron API 就必须 true
}
```

### 1.1.3 入口:生命周期

```ts
import { Plugin } from "obsidian";

export default class MyPlugin extends Plugin {
  async onload() {
    await this.loadSettings();
    this.addCommand({ id: "...", name: "...", callback: () => {} });
    this.addSettingTab(new MySettingTab(this.app, this));
    this.addRibbonIcon("dice", "tip", () => {});
  }
  onunload() { /* 清理:事件、interval、DOM */ }
}
```

- `loadData()` / `saveData()` 读写 `data.json`(插件设置持久化,自动放进插件目录)。
- 注册的东西(command/event/interval)用 `this.registerXxx` 或在 `onunload` 清,避免泄漏。

### 1.1.4 常用 API 速记

| 要做的事 | API |
|---|---|
| 弹提示 | `new Notice("...", ms)` |
| 加命令 | `this.addCommand({ id, name, callback })` |
| 设置页 | 继承 `PluginSettingTab`,`display()` 里用 `new Setting(el)` |
| 设置项控件 | `.addText / .addToggle / .addDropdown / .addTextArea / .addButton` |
| 读写设置 | `this.loadData()` / `this.saveData()` |
| 界面语言 | `getLanguage()`(需 Obsidian ≥1.8.7) |
| 打开外链 | `window.open(url, "_blank")` |

### 1.1.5 构建配置(esbuild)

官方模板的 `esbuild.config.mjs` 直接用:
- `external: ['obsidian', 'electron', ...builtinModules]` —— 这些运行时提供,不打包
- `format: 'cjs'`,`target: 'es2021'` 左右
- dev 用 `sourcemap: 'inline'` + watch;prod 用 `minify: true`

`package.json` 脚本:`dev`(watch)、`build`(tsc 检查 + 打包)、`lint`。

---

## 1.2 实战经验(这才是这页的价值)

### 1.2.1 [实测] 起项目:一定用官方模板 + 官方 lint

不要手搓脚手架。`obsidianmd/obsidian-sample-plugin`(GitHub "Use this template")自带:
- GitHub Actions:push 自动 build+lint、打 tag 自动发 release
- **`eslint-plugin-obsidianmd`——这套 lint 规则基本等于社区提交审核会查的点**

> 把 `npm run lint` 清成 0 error,过审概率大很多。它会精准抓:`require()` 被禁(要正经 import)、内联 `element.style.xxx` 要移到 CSS class、用了超出 minAppVersion 的 API(如 `getLanguage()` 需 ≥1.8.7)等。这些都是审核真会打回的。

剩下的 warning 里,`display()` deprecated / 建议 `getSettingDefinitions()` 这类是 1.13+ 的前瞻提示,当前版本 `display()` 照常用,不阻塞。

### 1.2.2 [大坑] 插件不能分发原生模块 → 逼你走纯 JS / 系统命令

这是 Obsidian 插件最反直觉的约束:**你不能依赖任何 npm 原生模块**(`.node` 二进制)。因为分发只发三个 JS/JSON/CSS 文件,没渠道带平台相关的二进制;就算硬塞,还要为每个 Electron 版本重编。

后果(我在 Session Bridge 上真遇到):
- 想读 SQLite?`better-sqlite3`/`sqlite3` 都是原生模块 → **用不了**。Node 20(Electron 34)也没内置 `node:sqlite`,Windows 又没系统 `sqlite3` 命令。最后**自己写了 250 行纯 JS 的 SQLite 只读解析器**。
- 想调 Keychain / DPAPI?别装 `keytar`/`win-dpapi` 原生模块。改**调系统命令**:macOS `security`、Windows `powershell` 调 `ProtectedData`。

> **可复用心法**:Obsidian 插件里凡是"需要原生能力"的地方,先想"能不能用①Node 内置模块 ②系统自带命令 ③纯 JS 实现"。三条都走不通再考虑放弃该功能。零运行时依赖不只是洁癖,是这个生态的硬约束,也是过审加分项。

### 1.2.3 [实测] 本地开发调试:软链 + Hot Reload + watch

Obsidian 只从 `vault/.obsidian/plugins/<id>/` 加载,但代码在别处开发。三件套连起来 = 存盘即生效:

```bash
# ① 软链:vault 插件目录 → 开发目录(目录名 = manifest 的 id)
ln -s /path/to/dev/my-plugin  /path/to/vault/.obsidian/plugins/my-plugin

# ② 装 Hot Reload 插件(pjeby/hot-reload,不在商店,从 GitHub 拿 main.js+manifest.json)
#    并在开发目录建一个空标记文件,告诉它监视:
touch /path/to/dev/my-plugin/.hotreload    # 记得 gitignore

# ③ 开 watch,存盘自动重新 build 出 main.js
npm run dev
```

之后循环:**改 .ts → 存盘 → esbuild 自动 build → Hot Reload 自动重载插件 → 直接测**,不用手动开关插件。

调试看日志:Obsidian 里 `Cmd+Opt+I` 开 DevTools,Console 搜你打的日志前缀(如 `[my-plugin]`)。

> 软链 + git 注意:通过软链改的是开发目录的文件,git 正常追踪。但如果 vault 本身被 obsidian-git 自动提交,记得在 vault 的忽略里排除 `.obsidian/plugins/my-plugin`,别把软链提交进知识库仓库。

### 1.2.4 [实测] 访问 Electron / Obsidian 私有能力:灰色地带

有些能力(如操作 Web Viewer 的 session)只能靠 `require('electron').remote`,这是 Obsidian **不公开鼓励**的私有 API,lint 也会提示。现实:核心功能自己也在用同一套(见 [[Obsidian webview 登录态注入]] 1.3.2),不少浏览器类插件也这么干。

> **取舍**:用私有 API 能开源自用、能用 BRAT 装,但**进官方社区市场有被拒风险**。做之前想清楚目标是"自用/小范围"还是"官方上架"。

### 1.2.5 i18n:内置字典 + `getLanguage()`

不必上 i18next 这种库。一个 `Record<Lang, Strings>` 字典 + 一个 `getStrings(setting)` 就够:
- `getLanguage()`(Obsidian ≥1.8.7)读界面语言实现"自动跟随"
- 设置里给个下拉:自动 / en / zh;切换后重绘设置页即可

---

## 1.3 发布全流程(实测走通)

### 1.3.1 版本与产物

- `version` 三处要一致:`manifest.json`、`package.json`、git tag。
- `versions.json` 记录 `版本 → 最低 Obsidian 版本` 的映射(用户升级时判断兼容)。
- **tag 名不带 `v` 前缀**(`0.2.0` 不是 `v0.2.0`),这是 Obsidian 硬规范。

### 1.3.2 [实测] 一键发版脚本

我在 Session Bridge 写了 `release.mjs`(`npm run release -- 0.2.0`),做:改三处版本号 → commit → 打 tag → push 分支和 tag。**push tag 触发官方模板的 release.yml**,自动 build 并创建 release **草稿**(附 main.js/manifest.json/styles.css),再去 Releases 页手动 Publish。

> 首次发版前:GitHub 仓库 Settings → Actions → General 确认 workflow 有写权限(release.yml 需要 `contents: write`)。

### 1.3.3 用户怎么装(写进 README)

- **手动**:从 Releases 下三个文件 → 放进 `<vault>/.obsidian/plugins/<id>/` → 重启启用。
- **BRAT**(`TfTHacker/obsidian42-brat`):输入 `作者/仓库名`,自动装 + 从 release 自动更新。适合还没进官方市场时给别人用。

### 1.3.4 提交官方社区市场

1. 代码公开在 GitHub,根目录有 `manifest.json` + README(讲清用途和用法)。
2. 打 tag 发 release,产物为附件。
3. 去 `obsidianmd/obsidian-releases` 提 PR,在 `community-plugins.json` 加一条(按格式:id/name/author/description/repo),过 PR checklist。
4. 官方人工 review:重点看**依赖(有没有原生模块/可疑包)、安全、有没有用私有 API**。
5. 现在还有个开发者面板(community 站点)管理提交状态。

---

## 1.4 一句话检查清单(下次开工照着过)

- [ ] 用官方模板起,别手搓
- [ ] 需要原生能力?先想 Node 内置 / 系统命令 / 纯 JS,**绝不引原生模块**
- [ ] 软链 + Hot Reload + `npm run dev`,配好再开始写
- [ ] `isDesktopOnly` 按是否用 Node/Electron 设
- [ ] `npm run lint` 清成 0 error(≈过审标准)
- [ ] 用私有 API 了吗?想清楚上不上官方市场
- [ ] 发版:三处版本号一致、tag 不带 v、release 草稿手动 Publish
- [ ] README 写清手动装 + BRAT 装
