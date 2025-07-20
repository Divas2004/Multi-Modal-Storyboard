from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    safety_checker=None,
    torch_dtype=torch.float32
).to("cpu")

pipe.enable_attention_slicing()

def generate_storyboard(description):
    styled_prompt = f"{description}, cinematic noir, dramatic lighting, rainy night"
    result = pipe(styled_prompt)
    return result.images[0]
