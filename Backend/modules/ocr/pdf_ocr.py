import os
from pdf2image import convert_from_path
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en', use_angle_cls=True)

def extract_text_from_pdf(pdf_path: str, temp_folder="temp_pages") -> str:
    """
    convert PDF to images and extract text from each page using PaddleOCR.
    """

    pages = convert_from_path(pdf_path, dpi=350)
    os.makedirs(temp_folder, exist_ok=True)

    extracted_text = []

    for i, page in enumerate(pages):
        image_path = f"{temp_folder}/page_{i}.jpg"
        page.save(image_path, "JPEG")

        #Run OCR using predict
        result = ocr.predict(image_path)

        for line in result:
            for item in line:
                extracted_text.append(item["text"])

    return "/n".join(extracted_text)            