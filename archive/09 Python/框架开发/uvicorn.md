### 一句话先说

因为 FastAPI 这类框架需要一个 ASGI 服务器 来“承载”它运行，而 uvicorn 就是目前最主流、性能好、用法简单的 ASGI 服务器，所以用它来启动整个服务。

---

### 具体原因

- 1. FastAPI 不是直接对外提供 HTTP 的“进程”，它只是一个应用对象
    
      # app/main.py 里一般是这样
    
      app = FastAPI()
    

这个 app 只是一个「可调用对象」，要由 ASGI 服务器（比如 uvicorn）来接收网络请求，然后把请求交给 app 处理。

- 2. uvicorn 是专门为 ASGI 设计的高性能服务器

- 基于 uvloop / httptools，性能比传统 WSGI 服务器高很多；

- 天然支持 async/await，和 FastAPI 的异步风格完全匹配。

- 3. 提供很多你自己用 python app.py 难以优雅处理的能力

- 热重载（reload=True）；

- 日志级别控制（log_level）；

- 多进程、多 worker、超时、优雅退出等生产环境能力。

- 4. 官方推荐 & 生态成熟

- FastAPI 官方文档就是以 uvicorn 作为默认启动方式；

- 在部署（docker / k8s / 云服务器）时，大家也几乎都是用 uvicorn（或者 uvicorn+gunicorn）。

---

### 对你这个项目来说

这句：

uvicorn.run(

    "app.main:app",

    host=config.HOST,

    port=config.PORT,

    reload=config.RELOAD,

    log_level=config.LOG_LEVEL.lower(),

)

做的事情就是：

- 用 uvicorn 这个 ASGI 服务器；

- 加载 app.main 模块里的 app 实例；

- 按你的配置（HOST / PORT / RELOAD / LOG_LEVEL）跑起来。

如果你不用 uvicorn，而是直接 python app/main.py，你还要自己写一大堆底层 socket/HTTP/异步调度的代码，相当于重复造一个“半成品的 uvicorn”，得不偿失。