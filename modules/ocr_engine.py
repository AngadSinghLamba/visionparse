"""
ocr_engine.py
-------------
Module to handle OCR processing using EasyOCR or Tesseract.

Functions:
- run_ocr_tesseract(image_path): Extracts text using Tesseract OCR.
- run_ocr_easyocr(image_path): Extracts text using EasyOCR.
- perform_ocr_on_images(image_paths, engine): Applies OCR to each image using the selected engine.
"""

import pytesseract
from PIL import Image
import easyocr

# Initialize EasyOCR reader globally (so it loads only once)
easyocr_reader = easyocr.Reader(['en'], gpu=False)

def run_ocr_tesseract(image_path):
    """
    Runs Tesseract OCR on a given image.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

def run_ocr_easyocr(image_path):
    """
    Runs EasyOCR on a given image.
    """
    results = easyocr_reader.readtext(image_path, detail=0)
    return "\n".join(results)

def perform_ocr_on_images(image_paths, engine="Tesseract"):
    """
    Performs OCR on a list of image paths using the specified engine.
    
    Parameters:
    - image_paths: list of image file paths
    - engine: "Tesseract" or "EasyOCR"
    
    Returns:
    - Combined OCR text from all images
    """
    all_text = []

    for path in image_paths:
        if engine == "Tesseract":
            text = run_ocr_tesseract(path)
        elif engine == "EasyOCR":
            text = run_ocr_easyocr(path)
        else:
            text = ""
        all_text.append(text)

    return "\n\n".join(all_text)
