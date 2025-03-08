import fitz  # PyMuPDF

def read_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    
    for page in doc:
        text += page.get_text("text") + "\n"
    
    return text

# Example usage
pdf_path = "example.pdf"  # Replace with your PDF file
pdf_text = read_pdf(pdf_path)
print(pdf_text)
