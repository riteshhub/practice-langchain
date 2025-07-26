from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    collection_name="sample",
    persist_directory="./.chroma_db"
)

retriever = vector_store.as_retriever(search_kwargs={'k': 3})

docs = retriever.invoke("What are the most effective strategies individuals can adopt at home to reduce their environmental impact?")

print(docs)