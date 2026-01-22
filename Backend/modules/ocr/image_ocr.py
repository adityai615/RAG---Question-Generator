from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')


def extract_text_from_image(image_path: str) -> str:
    """
    Extracting text from Image using PaddleOCR.
    Return Clean plain text.
    """
    
    # gives the reult in object form as we are using predict, it gives item containing text confidence bbox
    result = ocr.predict(image_path)

    extracted_text = []

    # result -> list of boxes + text
    for line in result:
        for item in line:
            extracted_text.append(item["text"])

            return "/n".join(extracted_text)
