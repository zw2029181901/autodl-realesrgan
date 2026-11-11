# Real-ESRGAN 超分

上传照片或商品图，宽高各放大4倍，下载PNG。输入最多150万像素，采用分块处理。

## 基本环境

Ubuntu 22.04，Python 3.12，PyTorch 2.8.0，CUDA 12.8。支持CPU或GPU；推荐GPU，建议8GB内存起测。

## 使用方法

使用保存就绪的镜像创建并启动实例后，打开“自定义服务6006”，上传图片，点击“四倍放大”，下载PNG。首次任务会初始化模型。

- 项目：https://github.com/zw2029181901/autodl-realesrgan
- 代码：`/root/autodl-active`
- 模型：`/root/autodl-active/models`，权重已包含，无需再次下载。
- 启动：`bash /root/autodl-active/run-service.sh`
- 环境检查：`/root/autodl-active/.venv/bin/python /root/autodl-active/runtime/doctor.py --project /root/autodl-active --models --http`

## 验证记录

RTX3090系统盘环境已完成321×273图片上传、四倍放大及1284×1092 PNG下载，耗时5.34秒。跨分块输出与同模型整图推理的平均通道差值为0.058/255。该结果不代表所有GPU的性能或兼容性保证。

镜像 `autodl-realesrgan-20261111`，UUID `image-ee2e3c811c`，平台显示1.24GB、就绪。社区公开状态以平台审核结果为准。没有为本应用额外执行镜像新实例复建测试；开机配置沿用U2Net保存镜像新实例验证通过的同一机制。完整记录见 `IMAGE_VALIDATION.json`。

模型可能生成原图不存在的细节。许可见项目内 `THIRD_PARTY.md` 和 `licenses`。
