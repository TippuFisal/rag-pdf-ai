from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from fastapi import FastAPI
from langchain.embeddings import HuggingFaceEmbeddings


app = FastAPI()

# Request schema
class QuestionRequest(BaseModel):
    question: str

# Load vector store once
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="db", embedding_function=embeddings)
retriever = db.as_retriever()

llm = Ollama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# API Endpoint
@app.post("/ask")
def ask_question(data: QuestionRequest):
    query = data.question
    response = qa_chain.run(query)
    return {"answer": response}
