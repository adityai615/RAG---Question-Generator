import docx
import pdfplumber
import os

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

def read_document(file_path: str):
    """read document content based on file"""
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == '.txt':
        return read_text_file(file_path)
    elif file_extension == '.pdf':
        return read_pdf_file(file_path)
    elif file_extension == '.docx':
        return read_docx_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")
    
    