import re

def clean_raw_text(text: str) -> str:
    """
    clean noisy OCR text including spaces, page numbers, headings, fix broken lines, footers.
    """
    # Remove page numbers 
    text = re.sub(r"Page\s*\d+\s*of\s*\d+","", text, flags = re.I)
    text = re.sub(r"Page[- ]?\d+", "", text, flags=re.I)

    # Remove Headers
    text = re.sub(r"(RTU|JECRC|BTECH|EXAM|SECTION|SEMESTER).*", "", text, flags = re.I)

    # Remove extra lines
    text = re.sub(r"\n+", "\n", text)

    # Remove spaces
    text = re.sub(r" +", " ", text)

    #trim White spaces
    text = text.strip()

    return text
