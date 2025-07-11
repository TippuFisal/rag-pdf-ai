# 🤖 RAG PDF AI Project

This is a beginner-friendly **Retrieval-Augmented Generation (RAG)** project using **LangChain + Ollama + FastAPI + ChromaDB**, designed to answer questions based on your own PDF content.  

You can ask your PDF anything like a chatbot. For example:  
**"Who is Tippu Fisal Sheriff?"** → it answers from your uploaded PDF!

---

## 📁 Project Structure

RAG_AI_PROJECT/
├── app.py # FastAPI app that handles user questions
├── ingest.py # Script to load & store your PDF as searchable data
├── data/
│ └── tippuabout.pdf # Your custom PDF file
├── db/ # Local vector DB created from PDF content
├── requirements.txt # All required Python packages
└── README.md # This file


## 🛠️ Prerequisites (Do this only once per new system)

### ✅ 1. Install Python 3.10 or newer  
You can download it from: https://www.python.org/downloads/

To verify:

python3 --version

✅ 2. Install Ollama (for running local LLMs like Mistral)

ollama run mistral

brew services restart ollama

✅ 3. Clone this project from GitHub

git clone https://github.com/TippuFisal/rag-pdf-ai.git
cd rag-pdf-ai

✅ 4. Create Virtual Environment & Activate

python3 -m venv venv
source venv/bin/activate

✅ 5. Install Required Python Packages

pip install -r requirements.txt

If requirements.txt not created, run this:

pip install langchain fastapi uvicorn chromadb pypdf2 sentence-transformers

pip freeze > requirements.txt


## 🚀 How to Run the App (After Shutdown or Anytime)


🔹 Step 1: Start Ollama in one terminal

ollama run mistral

🔹 Step 2: Activate your virtual environment

cd rag-pdf-ai
source venv/bin/activate

🔹 Step 3: Ingest your PDF (if changed or new)

python ingest.py


🔹 Step 4: Start the FastAPI server

uvicorn app:app --reload

### Your API is live at:
http://127.0.0.1:8000/docs → you can ask questions here!

### ❓ Sample Questions to Test

{
  "question": "Who is Tippu Fisal Sheriff?"
}







