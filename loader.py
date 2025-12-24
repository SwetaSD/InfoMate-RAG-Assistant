from PyPDF2 import PdfReader
import docx


def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text() or ""
        if page_text.strip():
            text += page_text + "\n"

    return text


def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])


def load_documents(pdf_files, docx_files):
    docs = []

    for pdf in pdf_files:
        text = read_pdf(pdf)
        if text.strip():
            docs.append(text)

    for doc in docx_files:
        text = read_docx(doc)
        if text.strip():
            docs.append(text)

    return docs
