import os
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ✅ STEP 1: Define folders
folders_to_read = ["data", "books"]  # Add more if needed

# ✅ STEP 2: Load all PDFs
all_docs = []

for folder in folders_to_read:
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            print(f"📄 Reading: {path}")
            loader = PyPDFLoader(path)
            docs = loader.load()
            all_docs.extend(docs)

# ✅ STEP 3: Split documents into chunks
print("✂️ Splitting...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(all_docs)

# ✅ STEP 4: Generate embeddings
print("🧠 Embedding...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(texts, embedding=embeddings, persist_directory="db")
db.persist()

print("✅ All PDFs ingested successfully!")


