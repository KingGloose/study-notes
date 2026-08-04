# 1. Flutter 项目初始化与移动端工具链

> 来源上下文：2026-08-03，在开发 `player-app`、准备持续维护 Flutter 音乐播放器时学习。
> 当前目标只覆盖 Android、iOS，暂不关注 Web。
> 本页重点记录从前端工程化迁移到 Flutter 时的个人认知变化；命令和工具职责由 AI 结合 Flutter 3.44.8 及官方文档补充。

## 1.1 最重要的认知纠正

### 1.1.1 [用户原理解] Flutter 是一个“大一统的 Web”

这个类比能帮助理解声明式组件、状态驱动 UI 和跨平台代码复用，但会误导对运行时的理解。

### 1.1.2 [AI 补充] Flutter 不是 Web，也不是 WebView

更准确的心智模型是：

> Flutter 是自带 UI Framework、渲染引擎和跨平台工具链的应用运行时。

- React Web 最终交给浏览器 DOM/CSS 和排版引擎渲染。
- Flutter 移动端由 Widget 描述 UI，再由 Flutter Engine 布局、合成并绘制像素。
- Android、iOS 共享的主要是 `lib/` 下的 Dart/Flutter 代码。
- 定位、后台音频、通知、登录等系统能力仍通过插件或原生代码接入。

前端经验仍然非常有用：Widget≈组件、状态驱动重建≈React/Vue 响应式更新、VM Service≈CDP。需要避免的是把 Flutter 当成浏览器环境。

## 1.2 初始化项目

Flutter 官方脚手架是 `flutter create`，对应前端的 `npm create vite`：

```bash
flutter create --empty --platforms=android,ios flutter_lab
```

参数含义：

- `--empty`：生成最小 `main.dart`，不带计数器示例。
- `--platforms=android,ios`：只生成 Android、iOS 宿主工程。
- `flutter_lab`：项目目录和默认 Dart package 名。

也可以在 VS Code 命令面板执行 `Flutter: New Project`；IDE 最终仍调用 `flutter create`。

常见模板：

| 模板 | 用途 | 前端类比 |
| --- | --- | --- |
| `app` | 完整 Flutter 应用，默认模板 | Web App |
| `--empty` | 最小 Flutter 应用 | minimal starter |
| `package` | 可复用 Dart/Flutter 包 | npm package |
| `plugin` | Dart API + Android/iOS 原生实现 | 带 native binding 的包 |
| `module` | 嵌入已有原生 App | 在既有宿主中接入子模块 |

## 1.3 `--platforms` 和平台目录

`--platforms` 决定 `flutter create` 为哪些目标生成宿主工程，不是编译后的代码，也不限制共享 Dart 代码的语法。

```text
flutter_lab/
├── lib/                 Android/iOS 共享 Dart、Flutter 代码
│   └── main.dart        应用入口，类似 src/main.tsx
├── android/             Android 宿主源码与构建配置
├── ios/                 iOS 宿主源码与构建配置
├── test/                Dart/Widget 测试
├── pubspec.yaml         依赖、assets、字体、版本配置
└── build/               编译产物与中间缓存，通常不提交 Git
```

### 1.3.1 `android/` 是什么

它包含 Gradle 配置、`AndroidManifest.xml`、Kotlin/Java 原生入口、权限、签名和平台插件配置。

它由脚手架生成，但属于项目源码：可以修改，通常提交 Git。它不是 APK 反编译后的代码，也不是临时编译目录。

### 1.3.2 `ios/` 是什么

它包含 Xcode 工程、`Info.plist`、Swift/Objective-C 原生入口、权限、签名和平台插件配置。

它同样由脚手架生成、可编辑且通常提交 Git。真正的临时构建内容在 `build/`、Xcode DerivedData 等位置。

### 1.3.3 后续添加平台

在已有项目根目录可以补生成缺少的平台骨架：

```bash
flutter create --platforms=ios .
```

这个命令适合补齐缺失平台或修复脚手架文件；已经人工修改的平台配置仍应先由 Git 保护并检查 diff。

## 1.4 Flutter CLI 的正确定位

### 1.4.1 [用户理解] CLI 基本覆盖开发生命周期

这个方向正确。更精确地说，Flutter CLI 是统一编排入口，而不是替代所有底层工具：

```text
flutter create   创建脚手架
flutter pub      管理 Dart/Flutter 依赖
flutter analyze  静态分析
flutter test     测试
flutter run      编译、安装、启动和调试
flutter build    生成发布产物
flutter devices  发现设备
```

Android 构建时：

```text
Dart/Flutter 源码与 assets
        ↓ Flutter CLI 编译和编排
Android 宿主、Engine、原生插件
        ↓ Gradle 构建与打包
      APK / AAB
        ↓ ADB
 Android 真机或 Emulator
```

iOS 构建时则由 Flutter CLI 调用 Xcode 构建体系；原生插件依赖还可能涉及 Swift Package Manager 或 CocoaPods。

## 1.5 Android Studio、Gradle 与 Logcat

### 1.5.1 Android Studio 不是运行容器

- Android Studio 是 IDE、SDK 管理器、Emulator 管理器和原生调试工具入口。
- App 真正运行在 Android 真机或 Android Emulator 中。
- 可以用 VS Code 写 Flutter，只借助 Android Studio 安装 SDK、创建模拟器或查看原生日志。

### 1.5.2 Gradle 是 Android 构建系统

Gradle 负责处理 Android/Kotlin/Java 依赖、Manifest、资源、构建变体、签名、原生插件，最终打包 APK/AAB。

`flutter build apk` 并没有绕开 Gradle，而是由 Flutter CLI 调用它完成 Android 平台部分。

### 1.5.3 Logcat 是 Android 系统日志

Flutter/Dart 逻辑可以先看 VS Code Debug Console；遇到原生崩溃、权限、后台 Service、通知、音频或插件问题时，需要看 Android Studio Logcat 或 `adb logcat`。

## 1.6 Dart VM Service 与 CDP

### 1.6.1 [用户理解] VM Service 类似 CDP

这个类比成立：二者都是 IDE/调试工具观察和控制运行时的协议入口。

Dart VM Service 可提供：

- 断点、单步执行、变量与调用栈；
- Hot Reload；
- CPU、内存、Isolate 与 Timeline 数据；
- DevTools 和 IDE 调试连接。

边界也要记住：

- VM Service 主要负责 Dart/Flutter 运行时；
- Android 原生层问题看 Logcat/原生调试器；
- iOS 原生层问题看 Xcode/LLDB；
- Release 构建默认不提供完整调试服务。

## 1.7 当前学习环境与选择

[本机实测，2026-08-03]

- Flutter 3.44.8、Dart 3.12.2 可用；
- Android SDK 36、Java 21、Android License 已就绪；
- iOS 所需 Xcode 尚未完整安装，CocoaPods 未安装；
- 学习目标只保留 Android、iOS，不生成 Web 平台；
- 第一个项目建议使用 `--empty --platforms=android,ios`，先掌握共享 Dart/UI，再分别认识两个宿主工程。

## 1.8 相关知识

- [[../前端/前端运行时动态 base 完全指南]]：前端 Vite/Webpack 构建产物与 Flutter 多平台工具链的对照入口。

## 1.9 官方参考

- [Create a new Flutter app](https://docs.flutter.dev/reference/create-new-app)
- [Flutter Android integration](https://docs.flutter.dev/platform-integration/android)
- [Flutter and Dart DevTools](https://docs.flutter.dev/tools/devtools)
- [Android Logcat](https://developer.android.com/tools/logcat)
