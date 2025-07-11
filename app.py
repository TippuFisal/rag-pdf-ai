from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

# ✅ Load Chroma DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="db", embedding_function=embeddings)
retriever = db.as_retriever()

# ✅ Load LLM and create QA chain
llm = Ollama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.post("/ask")
def ask_question(data: QuestionRequest):
    response = qa_chain.run(data.question)
    return {"answer": response}
