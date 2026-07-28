[Kimi](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Kimi&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJLaW1pIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.AYXQOhQBxjKenVA2u3sMipsi8dZg38zPgw3_qFJs39k&zhida_source=entity) 最近把 Agent 从 Python 转成了 Typescipt 和 [pi-tui](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=pi-tui&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJwaS10dWkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.jfCQjmVc9Be07LiCjjPBmW5wK2Xs7NhH_xEtHfP0tXg&zhida_source=entity) 的 kimi-code 新的 Agent，这个蛮有意思的，为什么 Kimi 要这么做。是跟着 [Claude code](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Claude+code&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJDbGF1ZGUgY29kZSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.Q8YFqn9II4VI14WAnlKZo6w33XyOquwSPlXYaWYCuvs&zhida_source=entity) 的步伐吗？

让我们看一下 Kimi-code 的结构变化

|维度|旧版 [kimi-cli](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=kimi-cli&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJraW1pLWNsaSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.f2aKoehdpKsCNpCewZOmIaw2W2BAKCVAYOCzJuZcRv0&zhida_source=entity)|新版 kimi-code|
|---|---|---|
|语言|Python 3.12+|TypeScript|
|运行时|[CPython](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=CPython&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJDUHl0aG9uIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.DAGZgTLhwrTeWPaRGWRRoGkEypwkA-uzTJ1gVPgTN2k&zhida_source=entity)|Node.js ≥ 24.15.0|
|包管理|uv / pip|[pnpm](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=pnpm&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJwbnBtIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.yeI4UUEqwFgoeOUyQOwLgenUK_M40k-vVJBnFEj_x1g&zhida_source=entity) 10.33.0|
|CLI 框架|Typer|Commander|
|TUI 渲染|Rich + [prompt-toolkit](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=prompt-toolkit&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJwcm9tcHQtdG9vbGtpdCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.rskott6xfhDX7tk8MINEbC62hziW40jTIjGOwDCbmPQ&zhida_source=entity)|pi-tui|
|配置校验|[Pydantic](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Pydantic&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJQeWRhbnRpYyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.7V5AXIho8f1YbWJN1M2Rru0KJxZ-IhTDSRkGupp0qlM&zhida_source=entity) + tomlkit|Zod + smol-toml|
|Lint|—|oxlint|
|构建|PyInstaller|Node.js [SEA](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=SEA&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJTRUEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.Uh84AjYced9lZjFgaRZ5NztlsfHi9MO9zr_-MfJSsT4&zhida_source=entity) + postject|

这种迁移不是"把 Python 文件后缀改成 .ts"那么简单。它涉及核心[抽象层](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%8A%BD%E8%B1%A1%E5%B1%82&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmir3osaHlsYIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.Xc-BVkyD784SbAxXDnUlZWong_-72X6Uc7AoV_GWshU&zhida_source=entity)（LLM 交互、OS 执行环境）的跨语言重写、终端 [UI 框架](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=UI+%E6%A1%86%E6%9E%B6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJVSSDmoYbmnrYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.1juQus51enYx2rlv29in5r9VSdcX3MWD-nIXoctV0mU&zhida_source=entity)的完全替换、以及构建产物的形态变革（从虚拟环境到[单二进制文件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%8D%95%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLljZXkuozov5vliLbmlofku7YiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.HSdp1an2zHrUtWA5orx6zuUNg8Pg6QAksZLg-3k-c7k&zhida_source=entity)）

新版 Kimi Code 打出的第一个卖点是：**"Install with one command: no Node.js setup, [PATH](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=PATH&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJQQVRIIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.Ik8SkEqT9ZIG6mBGNWwno6VPmKZp-IA3THxrrQvhewY&zhida_source=entity) gymnastics, or global module conflicts."**（一行命令安装，无需 Node.js、无需折腾 PATH、无全局模块冲突。）

为什么 kimi 要强调这个

老版 `kimi-cli` 基于 Python，虽然用 `uv` 或 `[pipx](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=pipx&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJwaXB4IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.w_-FB7JnOksBSgHgmm0-5AYxygI58yUbOL4yb9PQSZk&zhida_source=entity)` 安装体验已经不错，但本质上它仍然是一个**解释型语言的包**。用户机器上必须有兼容的 Python 版本，依赖要解析，虚拟环境要隔离，不同平台的 wheels 要匹配。对于想覆盖"所有[开发者](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%BC%80%E5%8F%91%E8%80%85&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLlvIDlj5HogIUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.plf9y3rCCkyn1lLopnIpLEJ3DYzSg-ajcnX4uN7Qylg&zhida_source=entity)"的终端工具来说，这始终是一个摩擦力点

同样，基于 python 的 vllm/sglang 也一直面临版本依赖和适配的“地狱”

Kimi 新版的做法：把 Node.js 和业务代码焊在一起

`kimi-code` 的构建流程藏在 `apps/kimi-code/scripts/native/` 里，分为五步：

1. **tsdown 打包**：用基于 Rolldown 的 tsdown 把整个应用 Tree-shake 并打包成一个 JS Bundle；
2. **SEA Blob 生成**：生成 Node.js 原生 SEA [配置文件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLphY3nva7mlofku7YiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.2qB85F9_B0kEp6gMwRTkOWL4IG5tx8oibd_ePi6ZHLA&zhida_source=entity)，声明入口和要内嵌的静态资源；
3. **postject 注入**：用 `postject` 工具把 JS Bundle 和资源注入到 Node.js [可执行文件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLlj6_miafooYzmlofku7YiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.vGK2-RdZ9GkoOZsBCZx0AajUP4c7FLiaNp2NUoHUQJQ&zhida_source=entity)中；
4. **代码签名**：[macOS](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=macOS&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJtYWNPUyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.nRGI-dyKRPuNc91HAfGXgPqjkYQV5CMuo3PAVtBQwiU&zhida_source=entity) 下用 `codesign` 签名，release 流程支持正式的 Apple 签名；
5. **验证**：确保注入后的二进制能正常启动且签名有效。

**结果是：一个 `kimi` 文件，内部包含了完整的 Node.js 运行时 + 业务代码 + 静态资源。** 用户下载后，chmod +x 就能跑，和 Go/Rust 编译出的单二进制体验完全一致。

SEA 是什么？

Node.js SEA 就是 Node.js 官方提供的一种能力，能把一个 Node.js 项目（包括代码、资源）打包成一个单独的可执行文件，用户不需要安装 Node.js 就能直接运行

SEA 也是达到这种单一二进制文件编译的关键能力

很多人听到"TypeScript 单二进制"会第一反应想到 Bun 的 `bun build --compile`。但 Kimi Code 没有选 Bun，而是选用了 **Node.js 官方 SEA + postject** 的组合。原因可能是：

- **稳定性与可控性**：Node.js SEA 是官方能力，与特定 [Node.js](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=15&q=Node.js&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJOb2RlLmpzIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjE1LCJ6ZF90b2tlbiI6bnVsbH0.rbBNZjyPV7RmEw3PFqp3mgWFBRhflC1lhodh-GOodBs&zhida_source=entity) 版本绑定，长期维护更可控；
- **生态兼容**：不需要用户/CI 额外安装 Bun，降低了[构建链](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%9E%84%E5%BB%BA%E9%93%BE&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmnoTlu7rpk74iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.gghX8Nc9M55WyBaJrqjKIMe9QB6hNKNDmlqcwRxEWro&zhida_source=entity)的复杂度；
- **签名与合规**：macOS 的 notarization 和 codesign 流程对官方 Node.js 二进制更友好。

这可能是因为 Bun 最近被 [Anthropic](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Anthropic&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJBbnRocm9waWMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.AK1O-7YEEttzwng6qNQfj_CSXPl56NmQC-DtwSaC-A0&zhida_source=entity) 收购了，处在剧烈的重构中（从 zig 到 Rust）

还有一个很大的特点，kimi-code 用了 pi-tui，这个是什么？ **`@earendil-works/pi-tui`**，这是一个相对独立的 TUI 框架。Kimi Code 的 README 里专门致谢了 pi-tui 的作者。

从架构上看，pi-tui 的引入解决了几个关键问题：

**第一，渲染模型的区分。** [传统终端](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E4%BC%A0%E7%BB%9F%E7%BB%88%E7%AB%AF&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLkvKDnu5_nu4jnq68iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.pAYUUunH60Hmv4zggAGvS3UrSfUVo4fK2CqcMZu8adk&zhida_source=entity) UI 要么是"全屏应用"（如 [Vim](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Vim&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJWaW0iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.TiGL5agrXr3PXocszLvyoUP8P-gY6VEIRPjDLj9ex3o&zhida_source=entity)），要么是"[流式输出](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%B5%81%E5%BC%8F%E8%BE%93%E5%87%BA&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmtYHlvI_ovpPlh7oiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.SgrGq5_4stCr6kOH26c2n3D8KyAWI4P_2DKsUlnKIas&zhida_source=entity)"（如 `ls -la`）。但 AI Agent 的界面是**两者的混合**：既有流式滚动的对话历史，又有需要固定位置的底部输入区、状态栏、浮动审批弹窗。pi-tui 提供了更灵活的 panel 和 layer系统，让 Agent 的复杂布局不再需要用胶水代码拼凑。

**第二，事件驱动的内部协议。** `apps/kimi-code/src/tui/` 里有一个 `reverse-[rpc](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=rpc&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJycGMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.SqPcywwpH6pS7Ifq--5sqGyhP4zcyzp4MK6cf0s8QQQ&zhida_source=entity)/` 目录，说明 TUI 层与 Agent 核心层是通过类 [RPC](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=RPC&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJSUEMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.LJu0oQbBnVFCegivCi7W1EbM88GzN5FcRi3DraeNeI0&zhida_source=entity) 的消息协议通信的，而不是直接函数调用。这意味着：

- TUI 可以独立于 Agent 核心进行测试；
- 未来如果要支持 GUI 或 Web 版本，可以复用同一套 Agent 核心，只替换前端；
- 流式输出的背压（[backpressure](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=backpressure&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJiYWNrcHJlc3N1cmUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.44qYl6cxUo33NwBCKjDKnNNNtkbgQMwtJib5ErBeXIU&zhida_source=entity)）控制更精细。

**第三，为什么是 pi-tui 而不是 Ink？** Ink 是 [React](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=React&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJSZWFjdCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.bYJxm6qDuqmZl-a7GZeyH6cHKLpzfXftqSNnbG15TDI&zhida_source=entity) 生态里很火的 TUI 框架，但 Kimi Code 没有用它。可能的考量包括：

- Ink 依赖 React 的 reconciler，对于需要极致性能的长会话流式渲染，React 的 diff 开销是负担；
- pi-tui 可能提供了更底层的终端控制原语，方便做自定义的 diff 高亮、[视频帧](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E8%A7%86%E9%A2%91%E5%B8%A7&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLop4bpopHluKciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.hp4rEqkNbdBBbISbZg072sA4w2mOcj2DUCk7SMDjWjY&zhida_source=entity)渲染等 Agent 特有的需求；
- 减少 React 依赖可以显著减小 bundle 体积，这对 SEA 单二进制至关重要。

或者这么说，pi-tui 是针对 agent 设计的，未来的优化和适配会更适合 agent。在 AI [技术栈](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%8A%80%E6%9C%AF%E6%A0%88&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmioDmnK_moIgiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.HL-wUuWH4hBiyXXTKWvJD239keBlYsFy_tuGjAax-_Y&zhida_source=entity)选择上，“喜新厌旧”也是一个合理的选择

如果你只看语言变化，可能会以为 kimi 把以前的代码全扔了。但打开 `packages/` 目录，会发现两个熟悉的名字：**[kosong](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=kosong&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJrb3NvbmciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.U3SMZDVUz_vFoEsOlm9vrXqSaHYGm3SH2qBnJZGSWCs&zhida_source=entity)** 和 **[kaos](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=kaos&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJrYW9zIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.rOjmDiabnPhsaXT0taVv-mtsVbzZ2qCKJemP1iTEcJs&zhida_source=entity)**。

老版 Python 的 `kosong` 是一个内部 PyPI 包，描述为"The LLM abstraction layer for modern AI agent applications"，统一了 [OpenAI](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=OpenAI&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJPcGVuQUkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.9D7zbtr7xtMg0oHWuQwD2zHEFK_HqJvMzlsA-iiPs9Q&zhida_source=entity)、Anthropic、Google GenAI、Vertex AI、[Moonshot API](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Moonshot+API&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJNb29uc2hvdCBBUEkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.EhcmCnef_0T0XVN41tAnFgOsso3j2-8S7SpjiAabT4A&zhida_source=entity) 的调用。

新版的 `@moonshot-ai/kosong` 保留了完全相同的定位，但变成了 TypeScript 包。它依赖：

- `[openai](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=openai&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJvcGVuYWkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.NrS6vNkUq4ZMlVFT4FSk4Alw1qiMeBYlE7lGW7cz6Yk&zhida_source=entity)`（官方 Node SDK）
- `@anthropic-ai/sdk`
- `@google/genai`
- `zod` + `zod-to-json-[schema](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=schema&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJzY2hlbWEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.dQxqTwu1BxDT21OV6XrSbJr_Ov8MRQxvxyFGymft1I4&zhida_source=entity)`（用于工具参数的模式定义与 [JSON Schema](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=JSON+Schema&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJKU09OIFNjaGVtYSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.iNTa59HgmeuA1qnI7kpKT3AGkOqXRsT54bQ9RFCoglY&zhida_source=entity) 转换）

**这不仅仅是翻译，而是利用 TypeScript 的[类型系统](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%B1%BB%E5%9E%8B%E7%B3%BB%E7%BB%9F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLnsbvlnovns7vnu58iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.KXgGfdouf3qZwAMtqKbLRxraBaE1TflDvuL8RZQT_2M&zhida_source=entity)进行了一次重构。** Zod 的 schema 可以直接推导 TypeScript 类型，工具定义、LLM 响应、消息结构的[类型安全](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%B1%BB%E5%9E%8B%E5%AE%89%E5%85%A8&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLnsbvlnovlronlhagiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.CtIC9ZUUOiEwyZ-IwYTIkxk2T3dhkMFnNe3J5IM4Zu8&zhida_source=entity)比 Python 的 Pydantic 更紧密地绑定在[编译期](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%BC%96%E8%AF%91%E6%9C%9F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLnvJbor5HmnJ8iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.nmpabpz_5WBPexpP2wQA8Ajjat8qYJS4vsJzu7ekCHI&zhida_source=entity)

我觉得这是个好东西，可以抽象出来作为 Agent 的一个基础开源组件

老版的 `kaos/pykaos` 提供了"本地/远程 [SSH](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=SSH&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJTU0giLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.YbmHUm860nLz4yPMVw-pRbfEcThJ-i0wNrnwxLa3xA4&zhida_source=entity) 文件和命令执行"的统一抽象。

新版的 `@moonshot-ai/kaos` 直接依赖 `ssh2`，提供了：

- 本地[文件系统](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmlofku7bns7vnu58iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.KiD0m-OUtr2BspjI8sebWwZksk-TmQ2166ZDRVKeJbQ&zhida_source=entity)操作
- 通过 [SSH2](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=SSH2&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJTU0gyIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.BrE9_quPChGMhdHWHuc_6klF7TTqBZ1PmiGoecZai6M&zhida_source=entity) 的远程执行环境
- 统一的接口让 Agent 不需要关心代码运行在本地还是远程服务器上

ssh 怎么实现本地还是远程服务器的统一呢？

实际上，kaos 做了一个抽象。因为 Agent 需要对文件做这些操作：

运行 shell 命令:exec()

文件操作：readText()、writeText()、stat()、glob()

kaos 设计一个 POSIX-like 的[操作系统](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmk43kvZzns7vnu58iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.pCVJwVxZW4Vm3zvIYePWjMCTtu9N2UfeKvGcFYSYrSQ&zhida_source=entity)抽象：

```
exec(...args: string[])           // → SSH exec channel
readText(path: string)            // → SFTP read
writeText(path: string, data)     // → SFTP write
stat(path: string)                // → SFTP stat
iterdir(path: string)             // → SFTP readdir
```

这些操作在 [SSH 协议](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=SSH+%E5%8D%8F%E8%AE%AE&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJTU0gg5Y2P6K6uIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.moE8EN7JtZ-Ya7FNeEpcW9F-AzzM-yj4fiTeLLKGzDM&zhida_source=entity)里都有[原子级](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%8E%9F%E5%AD%90%E7%BA%A7&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLljp_lrZDnuqciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.usQ2Lk_68lLsj9eEH1lumuRxuSR50kMUo7pJ9HR9k-4&zhida_source=entity)对应，不需要额外封装或模拟。比如： • exec("git", "status") 直接[映射](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%98%A0%E5%B0%84&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmmKDlsIQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.IvaMw7wJHT2vuqCxSeDSu-CR-36PqdbHSubKQr-d4bA&zhida_source=entity)到 SSH exec channel • readText("/etc/nginx/nginx.conf") 直接映射到 SFTP open → read → close

通过这种抽象和封装，kaos 就能让 kimi 能操作"任何机器"——你的笔记本、云服务器、[CI runner](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=CI+runner&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJDSSBydW5uZXIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.MEcH0j9SxKOVFSjAH3QMagPbeB8LZ8ziRKWTG6oy3VA&zhida_source=entity)、边缘节点

SSH 协议是最通用的协议，POSIX 文件操作是最通用的文件操作，所以 kaos 的适用性就会很广

kaos 也是一个很好的抽象，可以拿出来做 agent 通用库来使用

`packages/agent-core/src/` 是整个产品最值钱的部分。它的目录结构揭示了 Kimi Code 对"Agent 应该长什么样"的理解：

```
agent-core/src/
├── loop/              # Agent 主循环
│   ├── run-turn.ts    # 单轮执行
│   ├── turn-step.ts   # 单步执行
│   ├── tool-call.ts   # 工具调用
│   ├── tool-scheduler.ts  # 工具调度
│   ├── retry.ts       # 重试逻辑
│   ├── llm.ts         # LLM 流式调用
│   └── events.ts      # 内部事件系统
├── agent/             # Agent 运行时
├── session/           # 会话管理
├── tools/             # 工具实现
│   ├── file/          # 文件操作
│   ├── shell/         # Shell 执行
│   ├── web/           # 网页搜索/抓取
│   ├── background/    # 后台任务
│   ├── agent/         # 子 Agent 调用
│   ├── plan/          # Plan 模式
│   ├── ask-user/      # 用户提问
│   └── skill/         # 技能系统
├── mcp/               # MCP 客户端
├── skill/             # 技能发现与加载
├── rpc/               # Wire / ACP 协议
├── config/            # 配置系统
└── logging/           # 结构化日志
```

这个结构与老版 Python 的 `kimi_cli/soul/` + `kimi_cli/tools/` 几乎一一对应，但 TS 版的模块化更清晰：**loop、tools、session、rpc 是完全独立的[子系统](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%AD%90%E7%B3%BB%E7%BB%9F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLlrZDns7vnu58iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.zegARlmVTRf6o9HiHuayEb_vn-SChbEJB7E8EG1r30A&zhida_source=entity)**，通过事件和接口交互，而不是像 Python 版那样有较多的[隐式耦合](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E9%9A%90%E5%BC%8F%E8%80%A6%E5%90%88&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLpmpDlvI_ogKblkIgiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.K_bNipjttJ1Nz5maK5QLstRq4hZVLvs2ti1G99Jq8Q4&zhida_source=entity)

另外，还有一些边还，例如 tsup 更换为 tsdown；[ESLint](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=ESLint&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJFU0xpbnQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.OJapA2zzW_W-wKELKgXjJWmSKaX8HqvqwUAO5b1ggtw&zhida_source=entity) 换成 oxlint；npm run build 改为SEA标准的build 过程。这些都是工程上加固

尽管语言和技术栈全换了，但 Kimi Code 的"架构 DNA"被完整地保留了下来。

例如 [Wire 协议](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=Wire+%E5%8D%8F%E8%AE%AE&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJXaXJlIOWNj-iuriIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3NTU2MjgyNiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.rA-9a7Hyn0sm2MYH01MruacbuWBEiK6Jz0YprqFPjNs&zhida_source=entity)，解决跨语言的调用。具体工具对比如下：

|工具|Python 版位置|TS 版位置|
|---|---|---|
|ReadFile / WriteFile / StrReplaceFile|tools/file/|tools/file/|
|Glob / Grep|tools/file/|tools/file/|
|Shell|tools/shell/|tools/shell/|
|SearchWeb / FetchURL|tools/web/|tools/web/|
|Agent（子 Agent）|subagents/|tools/agent/|
|TaskList / TaskOutput / TaskStop|tools/background/|tools/background/|
|EnterPlanMode / ExitPlanMode|tools/plan/|tools/plan/|
|AskUserQuestion|tools/ask_user/|tools/ask-user/|
|SetTodoList|tools/todo/|（可能在 tools/ 内）|

这种对齐不是巧合，而是说明团队对"Agent 需要哪些能力"有清晰的共识，重写只是换实现语言，不换产品定义

从这个改变来看，我已经切换了，还没有深度使用。等过一周，可能会有更多的对比出来

但是从这个转换，如此大动干戈啊，为什么要这样做呢，我理解可能有几个原因：

1、简化分发。 通过 Node.js SEA，一个 TypeScript 项目做出了 Go 级别的单二进制分发体验。这打破了"TypeScript/Node.js 不适合做 [CLI 工具](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=CLI+%E5%B7%A5%E5%85%B7&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJDTEkg5bel5YW3IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6Mjc1NTYyODI2LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.EovwXmrmTl7u2756h80uGLFFxVQHYAvE1qVE0arPoWc&zhida_source=entity)"的偏见——关键不在于语言，而在于构建工程。

2、TUI 框架的独立趋势 选 pi-tui 而不是 Ink，说明当 Agent 会话的复杂度超过一定阈值后，通用的 React/[组件化](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%BB%84%E4%BB%B6%E5%8C%96&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLnu4Tku7bljJYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.oh011kfH-tSaCYnM9DshUzLOT9kPciASuZ0BjCBXCgM&zhida_source=entity)模型会成为负担，领域专用的 TUI 框架会更有优势。

3、Agent 内核的语言无关性。

kosong、kaos、Wire 协议、工具集、子 Agent 模型——这些核心抽象从 Python 平移到 TypeScript 后依然成立，说明**AI Agent 的[架构模式](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%9E%B6%E6%9E%84%E6%A8%A1%E5%BC%8F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmnrbmnoTmqKHlvI8iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.hH2Rq1-ubCuIQXqTHY9_-pYyh9v0obKSJoXgCaUhBjk&zhida_source=entity)正在收敛**。语言只是实现层，Agent 的"[操作系统化](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%8C%96&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLmk43kvZzns7vnu5_ljJYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.QZhYgMfE_msL-dtPOAf1L8ZSg6LPE4cD7Z2aQmUeqtw&zhida_source=entity)"（文件、Shell、网络、[子进程](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%AD%90%E8%BF%9B%E7%A8%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLlrZDov5vnqIsiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.UUDIAM1SB3nhtzGsuceFFQ53deV_BfdlBo31u5atOeY&zhida_source=entity)、MCP、技能）才是本质。

对于普通用户来说，这次重写可能只意味着启动快了一点、安装简单了一点。但对于观察终端 Agent 演进的开发者来说，Kimi Code 的这次"换芯"，是一张关于未来 AI Native [终端软件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%BB%88%E7%AB%AF%E8%BD%AF%E4%BB%B6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiLnu4jnq6_ova_ku7YiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.9gh0DGIQXpUhIRsbx8Yf3QYwUTxWqYYu2kVFs_16fbQ&zhida_source=entity)该如何构建的 Kimi 的看法

[Kimi Code](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=8&q=Kimi+Code&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODUzOTU5ODUsInEiOiJLaW1pIENvZGUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzU1NjI4MjYsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6OCwiemRfdG9rZW4iOm51bGx9.lVGBCz7UE5xEoYaMqNSNUQL3DdbgXqf3EoUrBE8Fx0E&zhida_source=entity) 是开源的，而且如果体验下来的工程能力很好。那的确可以按照这个成功实践来构建自己的 Agent。同时 kosong、kaos 、Wire 都是很好的组件，可以拿来复用。最近好几个新的 Agent ，例如 CommanCode、Flue、都是用 TS 构建的。而 Python 由于性能、类型安全、依赖和 TUI 的不足，可能难以支撑终端 Agent 向“真正好用的生产力工具”演进