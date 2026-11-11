# Real-ESRGAN 超分 发布填写材料

| 字段 | 填写内容 |
|---|---|
| 显示名称 | Real-ESRGAN 超分 |
| GitHub仓库名 | autodl-realesrgan |
| 公开镜像名称 | Real-ESRGAN-Upscale |
| 拟保存镜像名称 | autodl-realesrgan-20261111 |
| 镜像UUID | image-ee2e3c811c |
| 平台镜像体积 | 1.24GB，已就绪 |
| GitHub账号 | zw2029181901 |
| 拟用项目链接 | https://github.com/zw2029181901/autodl-realesrgan |
| AutoDL.Art账号 | 200211（金鳞） |
| 介绍 | 照片宽高各放大4倍，分块处理，输出PNG；输入最多150万像素。 |
| 服务端口 | 6006 |
| 本批导出镜像启动命令 | bash /root/autodl-active/run-service.sh |
| 模型容量 | 约0.067GB；模型及输出预留2GB，依赖另计 |
| 上游 | https://github.com/xinntao/Real-ESRGAN |
| 许可 | BSD-3-Clause（Real-ESRGAN）；Apache-2.0（BasicSR网络结构） |

已完成独立环境真实HTTP任务，以及系统盘迁移后6006的多分块四倍超分，具体见 `IMAGE_VALIDATION.json`。开机启动沿用U2Net镜像恢复验证过的同一机制；本应用未额外重启或创建客户测试实例。平台镜像已保存就绪，已提交AutoDL.Art，详情页显示“v1版本镜像正在审核中”；尚未公开上架。

社区条目：https://www.autodl.art/i/zw2029181901/autodl-realesrgan/Real-ESRGAN-Upscale

原创算法/论文：不勾选，上游模型归原作者。
原创代码：按平台定义如实提交中文界面、部署脚本等增量说明，不因新建自己的仓库就勾选整套模型代码原创。
收益以平台当前审核及结算规则为准；不承诺上架或收益。

本包是独立Gradio应用。发布社区镜像后，是否成为应用广场APP须走平台对应入口与审核；也不会自动变成由AutoDL部署维护的ComfyUI工作流API。
