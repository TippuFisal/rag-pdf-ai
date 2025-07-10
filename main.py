from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents([text])

def store_embeddings(docs):
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embedding, persist_directory="db")
    db.persist()
    print("✅ Vector DB created successfully")

# Load and process PDF
pdf_path = "data/tippuabout.pdf"  # update file name if needed
text = load_pdf(pdf_path)
chunks = split_text(text)
store_embeddings(chunks)
