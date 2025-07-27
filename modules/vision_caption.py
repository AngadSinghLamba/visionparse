"""
vision_caption.py
------------------
This module handles vision-based image captioning using BLIP (default)
or SmolVLM (lightweight alternative). It processes each image and generates
a descriptive caption for use in markdown or QA tasks.

Functions:
- load_blip_model(): Loads the BLIP model.
- load_smolvlm_model(): Loads the SmolVLM model.
- generate_caption_blip(image_path): Generates a caption using BLIP.
- generate_caption_smolvlm(image_path): Generates a caption using SmolVLM.
- generate_captions_bulk(image_paths, model_type): Captions multiple images.
"""

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import os

# Optional: smolVLM (if integrated)
try:
    from transformers import AutoProcessor as SmolProcessor, AutoModelForVision2Seq
    smolvlm_available = True
except ImportError:
    smolvlm_available = False

# Cache BLIP model
blip_processor = None
blip_model = None

def load_blip_model():
    """
    Loads BLIP model and processor if not already loaded.
    """
    global blip_processor, blip_model
    if blip_processor is None or blip_model is None:
        blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption_blip(image_path):
    """
    Generates caption using BLIP model.
    """
    load_blip_model()
    raw_image = Image.open(image_path).convert("RGB")
    inputs = blip_processor(raw_image, return_tensors="pt")
    out = blip_model.generate(**inputs)
    caption = blip_processor.decode(out[0], skip_special_tokens=True)
    return caption

# Optional: Use SmolVLM if lightweight model needed
def generate_caption_smolvlm(image_path):
    """
    Generates caption using SmolVLM model.
    """
    if not smolvlm_available:
        return "SmolVLM not installed."
    
    processor = SmolProcessor.from_pretrained("HuggingFaceTB/SmolVLM-256M-Instruct")
    model = AutoModelForVision2Seq.from_pretrained("HuggingFaceTB/SmolVLM-256M-Instruct")
    image = Image.open(image_path).convert("RGB")
    prompt = "Describe the image in a single sentence."
    inputs = processor(images=image, text=prompt, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, max_new_tokens=50)
    return processor.batch_decode(out, skip_special_tokens=True)[0]

def generate_captions_bulk(image_paths, model_type="BLIP"):
    """
    Processes a list of image paths and returns captions for each.
    
    Parameters:
    - image_paths: List of image file paths
    - model_type: "BLIP" or "SmolVLM"
    
    Returns:
    - Dictionary: {image_filename: caption}
    """
    captions = {}
    for path in image_paths:
        try:
            if model_type == "BLIP":
                caption = generate_caption_blip(path)
            elif model_type == "SmolVLM" and smolvlm_available:
                caption = generate_caption_smolvlm(path)
            else:
                caption = "Unsupported or missing model"
        except Exception as e:
            caption = f"Error: {e}"
        captions[os.path.basename(path)] = caption
    return captions
