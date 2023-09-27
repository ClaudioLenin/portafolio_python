import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torchvision.utils as vutils

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler(DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = 'a dog running in the snow'
image = pipe(prompt, height=512, width=768, num_inference_steps=10).images[0]

# Normalize the image tensor to be between 0 and 1
image = (image - image.min()) / (image.max() - image.min())

# Save the image as a PNG file
vutils.save_image(image, "~/my_images/generated_image.png")