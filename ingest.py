import os
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 📁 Folders containing PDFs
folders = ["data", "books"]

# 🧠 Load all PDFs
all_docs = []
for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            print(f"📄 Loading: {path}")
            loader = PyPDFLoader(path)
            docs = loader.load()
            all_docs.extend(docs)

# ✂️ Split into chunks
print("✂️ Splitting text...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(all_docs)

# 🔗 Embed and store into vector DB
print("🧠 Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="db")
db.persist()

print("✅ All PDFs processed successfully!")
