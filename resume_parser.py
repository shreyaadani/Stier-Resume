import pdfplumber
import re

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def split_into_sections(text):
    sections = re.split(r'\n\s*(Skills|Experience|Education|Projects|Certifications)\s*\n', text, flags=re.IGNORECASE)
    parsed = {}
    for i in range(1, len(sections), 2):
        parsed[sections[i].strip().lower()] = sections[i + 1].strip()
    return parsed
