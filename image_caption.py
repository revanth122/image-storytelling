from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

device= "cpu"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image: Image.Image) -> str:
    """
    Transcribe the image into a descriptive caption.
    """
    inputs = processor(image, return_tensors="pt")
    inputs ={
        key: value.to(device) for key, value in inputs.items()
    }

    output = model.generate(**inputs,max_length=50)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption