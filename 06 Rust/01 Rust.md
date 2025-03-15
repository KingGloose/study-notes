文章介绍：[Hello, World! - Rust 程序设计语言 中文版 (rustwiki.org)](https://rustwiki.org/zh-CN/book/ch01-02-hello-world.html)

# 1、基本介绍

学就完了，没啥说的

# 2、基本使用

## 2.1 安装环境

1、这里需要安装`rustc`的编译工具，安装完成之后使用`rustc --version`来查看

2、通过 `rustup` 安装 Rust 后，更新到最新版本使用`rustup update`

3、要卸载 `Rust` 和 `rustup`使用`rustup self uninstall`

![[00 assets/a08995424c1d09e0bfb72716f06ae445_MD5.png]]

## 2.2 HelloWorld

1、我们这里编写了一个`Hello World`的程序

2、`fn`表示函数；`main`的作用与`Java`和`C`一致，它始终是每个可执行 Rust 程序中运行的第一个代码；`println!` 表示调用 `Rust宏`，如果改为调用函数，则应该将其输入为 `println`（不含 !）

![[00 assets/24e7829b726d6a891a723baa1d9a70a2_MD5.png]]

3、我们安装了`rust`的话，`cargo`也会一起安装，使用`cargo --version`来查看`cargo`的版本，这个你可以理解为`nodejs`中的`npm`，用于构建大型项目，一般情况也是使用`cargo`来创建新项目

4、其目录和其他很多的前端项目基本一致，src 用于放置代码，`Cargo.toml`用于放置额外的包和一些版本信息

![[00 assets/10bbec694fea78970194ba30b43cffb4_MD5.png]]

5、使用`cargo build`来构建一个`rust`项目，和`npm run build`是一致的，其中`.exe`结尾的就是编译后的程序

![[00 assets/d4aa5293bf0a32a9e13b3365a0b1dc82_MD5.png]]

6、当然也可以使用`cargo build` 构建项目、 `cargo run` 构建并运行项目、 `cargo check` 构建项目但是不生成二进制文件来检查错误。`cargo build --release`用于构建优化后的项目，可以理解为生产环境使用

## 2.3 基本使用

1、下面是一个输入字符，控制台打印的程序

​ 1.1 `let mut str = String::new()`； `let`表示定义一个变量； `mut`表示该变量可变（默认情况是不可变）； `String::new()`表示创建一个`UTF-8 编码的可增长文本`，`new()`是`String`的关联函数；

​ 1.2 `io::stdio()`表示进行`io`操作，上面引入了`std::io`，这里直接使用即可；`read_line` 将用户在标准输入中输入的任何内容都追加到一个字符串中（而不会覆盖其内容），所以它需要字符串作为参数；

​ 1.3 `&`表示引入，这里和`C`基本一致，引入默认是不可变的需要写成 `&mut guess` 来使其可变，而不是 `&guess`

​ 1.4 因为`read_line()`会返回`io::Result`，他是一个枚举类型，因为`Rust`默认安全为主，我们需要编写一个`expect()`来对`IO`错误进行处理，可以理解为必须使用`try { ... } catch(e) { ... }`

​ 1.5 在`print()`中使用`{}`来作为占位使用，把 `{}` 想象成小蟹钳，可以夹住合适的值

​ 1.6 `use std::io`表示引入了`std::io`标准库中的内容，类似`import`

![[00 assets/54d7e348a7e1fd1d459d0bf5641e01cb_MD5.png]]

2、
