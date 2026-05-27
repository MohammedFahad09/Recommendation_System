# import pytesseract
# from PIL import Image

# def extract_text(image):
#     text = pytesseract.image_to_string(Image.open(image))
#     return text.lower()

import pytesseract
from PIL import Image

# 🔥 FIX PATH HERE
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text.lower()