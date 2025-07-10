from PyPDF2 import PdfReader

reader = PdfReader("data/tippuabout.pdf")  # Use your actual PDF file name

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"\n---- Page {i+1} ----\n{text}")