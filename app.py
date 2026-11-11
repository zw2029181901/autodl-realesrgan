import functools
from runtime.common import asset_path, device, guarded, image_rgb, output_path, page_header


@functools.lru_cache(maxsize=1)
def model():
    import torch
    from network import RRDBNet
    net = RRDBNet()
    weights = torch.load(asset_path(), map_location="cpu", weights_only=True)
    net.load_state_dict(weights.get("params_ema", weights.get("params", weights)), strict=True)
    return net.eval().to(device())


@guarded
def upscale(image):
    import numpy as np
    import torch
    from PIL import Image
    image = image_rgb(image, max_pixels=1_500_000)
    # Original checkpoint expects RGB. Tile on device but keep the full output in CPU RAM.
    data = np.asarray(image, dtype=np.float32) / 255.0
    height, width = data.shape[:2]
    result = np.empty((height*4, width*4, 3), dtype=np.uint8)
    tile, border = 256, 32
    net = model()
    with torch.inference_mode():
        for y in range(0, height, tile):
            for x in range(0, width, tile):
                y_end, x_end = min(y+tile, height), min(x+tile, width)
                y0, x0 = max(0, y-border), max(0, x-border)
                y1, x1 = min(height, y_end+border), min(width, x_end+border)
                tensor = torch.from_numpy(data[y0:y1, x0:x1].copy()).permute(2, 0, 1).unsqueeze(0).to(device())
                output = net(tensor).clamp(0, 1)[0].permute(1, 2, 0).cpu().numpy()
                output = np.rint(output*255).astype(np.uint8)
                result[y*4:y_end*4, x*4:x_end*4] = output[(y-y0)*4:(y_end-y0)*4, (x-x0)*4:(x_end-x0)*4]
    destination = output_path(".png")
    Image.fromarray(result).save(destination)
    return str(destination), str(destination)


def build_ui():
    import gradio as gr
    with gr.Blocks(title="Real-ESRGAN 超分") as ui:
        page_header()
        gr.Markdown("输入最多150万像素；输出宽高各放大4倍。适合照片及商品图，不保证恢复真实细节。")
        source = gr.Image(type="pil", label="低分辨率图片")
        button = gr.Button("四倍放大", variant="primary")
        result = gr.Image(label="超分结果")
        file = gr.File(label="下载 PNG")
        button.click(upscale, source, [result, file], api_name="upscale")
    return ui
