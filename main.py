import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Loop through all the pages and extract text
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Check if text is found on the page
                text += page_text
        return text

# Example usage:
pdf_file_path = 'databases_2425_1to8-B.pdf'  # Replace with your PDF file path
pdf_text = extract_text_from_pdf(pdf_file_path)
with open("thing3.txt", "w") as f:
    f.write(pdf_text)
print(pdf_text)
