# Real-ESRGAN 超分

照片宽高各放大4倍，分块处理，输出PNG；输入最多150万像素。

本仓库提供独立应用源码及部署脚本，模型版本固定在 `app.json`。源码仓库不含权重；本次准备保存的AutoDL环境已将模型和独立依赖放入系统盘，模型无需在客户首次运行时下载。

## 本次镜像准备状态

2026-11-11已完成系统盘迁移，6006上传、排队、GPU推理和PNG下载通过：321×273输入输出1284×1092，耗时5.34秒。包含模型的应用目录磁盘占用约0.560GB，此数值不是平台保存镜像体积。

代码位于 `/root/autodl-active`，模型位于 `/root/autodl-active/models`，启动命令为 `bash /root/autodl-active/run-service.sh`。6006服务正常，已配置与U2Net恢复测试通过时相同的开机启动机制。镜像 `autodl-realesrgan-20261111`（`image-ee2e3c811c`）已保存就绪，平台体积1.24GB；AutoDL.Art条目已提交，v1审核中。没有为本应用另建镜像复建测试实例。

迁移和保存记录见 [IMAGE_VALIDATION.json](IMAGE_VALIDATION.json)，镜像使用说明见 [IMAGE_README.md](IMAGE_README.md)。[社区条目](https://www.autodl.art/i/zw2029181901/autodl-realesrgan/Real-ESRGAN-Upscale)当前等待平台审核，尚未公开上架。

## 环境与空间

- Ubuntu 22.04，Python 3.11（也允许3.12），每个应用独立虚拟环境。
- 支持CPU或GPU；推荐GPU，分块256像素。建议8GB内存起测。
- 模型约 0.067GB，模型和输出建议预留 2GB；Python/CUDA依赖另计。系统盘建议至少保留15GB安装余量；最终以 `df -h` 为准。
- 许可：BSD-3-Clause（Real-ESRGAN）；Apache-2.0（BasicSR网络结构）。
- [上游项目](https://github.com/xinntao/Real-ESRGAN)。本项目添加中文网页、固定模型下载、部署和检查脚本，上游算法归原作者。

## 独立包部署

以下用于从源码另行安装；使用之后保存就绪的镜像时直接打开6006即可。命令在AutoDL的Linux终端执行，项目仓库为 `zw2029181901/autodl-realesrgan`。

```bash
cd /root
git clone https://github.com/zw2029181901/autodl-realesrgan.git
cd /root/autodl-realesrgan
bash install.sh
# 可在无卡模式完成依赖安装和模型下载；GPU应用实际推理须有卡模式。
.venv/bin/python runtime/prefetch.py --project .
.venv/bin/python runtime/doctor.py --project . --models
bash start.sh
```

若Python不是3.11/3.12，先选择合适的基础镜像，或用 `PYTHON_BIN=/你的Python路径 bash install.sh`。
若PyPI下载慢，可显式使用清华源：`PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple bash install.sh`；PyTorch使用官方独立源。
若Hugging Face不可访问，可自行选择镜像端点：`HF_ENDPOINT=https://hf-mirror.com .venv/bin/python runtime/prefetch.py --project .`。这是下载源选项，不保证可达；仓库及revision不变。

打开实例的自定义服务6006。保持前台启动终端运行，或按 UPLOAD_GUIDE.md 的后台启动方式运行。网页出现后必须完成 SMOKE_TEST.md 的真实任务。
如需密码：`APP_USERNAME=user APP_PASSWORD='自行设置' bash start.sh`。公开镜像保存前不要把自己的密码写进代码或脚本。

## 模型和保存镜像

源码安装时，模型优先放入 `MODEL_ROOT` 指定目录或项目内已有的 `models` 目录，否则使用 `/root/autodl-tmp/autodl-models`。保存镜像只保存系统盘，数据盘模型不会随镜像分发。

本次已将约67MB的Real-ESRGAN权重放入系统盘 `/root/autodl-active/models`，使用离线模式运行；依赖复用基础镜像内的固定PyTorch，不重复安装CUDA框架。每保存一份后核对平台镜像体积及账号合计容量，不能用应用目录大小代替计费体积。

## 验收与发布

看 SMOKE_TEST.md、PUBLICATION.md、IMAGE_README.md 和 IMAGE_VALIDATION.json。本应用已通过独立环境真实HTTP推理与系统盘迁移后的多分块GPU任务。没有为此应用另租测试实例或重复重启；开机机制在U2Net保存镜像的新实例上已验证。本应用镜像已保存、审核已提交；公开状态以平台审核结果为准。
安装会保存 `installed-requirements.txt`，请在云端验收后保留它作为该镜像的依赖记录。没有自动更新依赖或模型的后台任务。
