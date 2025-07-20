from diffusers import StableVideoDiffusionPipeline
from PIL import Image
import torch
import imageio

pipe_video = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid",
    torch_dtype=torch.float32
).to("cpu")

pipe_video.enable_attention_slicing()

def resize_image(image, size=(256, 256)):
    return image.resize(size, Image.LANCZOS)

def generate_video(image, filename):
    image = resize_image(image)
    result = pipe_video(
        image,
        decode_chunk_size=2,
        num_inference_steps=10,
        generator=torch.manual_seed(42)
    )
    frames = result.frames[0][:8]
    imageio.mimsave(filename, frames, fps=6)
