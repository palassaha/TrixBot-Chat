
from PyPDF2 import PdfReader
import re

def extract_pdf_content(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        
    return re.sub(r'\s+', ' ', text).strip()

def save_processed_text(text:str, output_path: str):
    with open(output_path, "w") as f:
        f.write(text)
        
        