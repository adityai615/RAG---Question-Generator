import docx
import pdfplumber


def read_text_file(file_path: str):
    """ Read content from a text file"""
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()


def read_pdf_file(file_path: str):
    """ Read content from a pdf file"""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text


def read_docx_file(file_path: str):
    """ Read content from a docx file"""
    doc = docx.Document(file_path)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

