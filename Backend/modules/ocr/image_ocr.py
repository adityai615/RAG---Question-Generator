from paddleocr import PaddleOCR
from PIL import Image, ImageFilter, ImageOps
import uuid
import os

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def preprocessing_image(img: Image.Image) -> Image.Image:
    """
    Improve Image quality before OCR.
    """
    img = img.convert("L")  # Grayscale
    img = ImageOps.autocontrast(img)  # Improve contrast
    img = img.filter(ImageFilter.SHARPEN)  # Sharpen edges
    return img

def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from image using PaddleOCR.predict().
    Returns clean plain text.
    """

    # Step 1: Load and preprocess
    img = Image.open(image_path)
    img = preprocessing_image(img)

    # Step 2: Save to a temp file (avoid overwriting original)
    temp_name = f"temp_{uuid.uuid4().hex}.jpg"
    img.save(temp_name)

    # Step 3: Run OCR
    result = ocr.predict(temp_name)

    # Step 4: Delete temp file
    os.remove(temp_name)

    extracted_text = []

    # Step 5: Extract text
    for line in result:
        for item in line:
            extracted_text.append(item["text"])

    # Step 6: Return clean output
    return "\n".join(extracted_text)
