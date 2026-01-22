import os
from pdf2image import convert_from_path
from paddleocr import PaddleOCR
from PIL import Image, ImageFilter, ImageOps

def preprocessing_image(img: Image.Image) -> Image.Image:
    """
    Imroving Image quality before ocr 
    """
    img = img.convert("L") #Grayscale
    img = ImageOps.autocontrast(img) #improves contrast
    img = img.filter(ImageFilter.SHARPEN) # Sharpen Edges
    return img


ocr = PaddleOCR(lang='en', use_angle_cls=True)

def extract_text_from_pdf(pdf_path: str, temp_folder="temp_pages") -> str:
    """
    convert PDF to images and extract text from each page using PaddleOCR.
    """

    # PDF -> Images
    pages = convert_from_path(pdf_path, dpi=350)
    os.makedirs(temp_folder, exist_ok=True)

    extracted_text = []

    for i, page in enumerate(pages):

        #preprocess
        page = preprocessing_image(page)

        #save temporary image
        image_path = f"{temp_folder}/page_{i}.jpg"
        page.save(image_path, "JPEG")

        #Run OCR using predict
        result = ocr.predict(image_path)

        # Extract Text
        for line in result:
            for item in line:
                extracted_text.append(item["text"])
    
    # Return clean text
    return "/n".join(extracted_text)            