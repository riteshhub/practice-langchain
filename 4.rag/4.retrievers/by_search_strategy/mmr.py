from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

documents = [
        Document(page_content="Dogs are great companions, known for their loyalty and friendliness."),
        Document(page_content="Elephants are intelligent and social animals, known for their memory."),
        Document(page_content="Dogs make wonderful friends, cherished for their affection and unwavering devotion."),
        Document(page_content="Lions are apex predators, living in prides and hunting together."),
        Document(page_content="Cats are independent animal that often enjoy their own space."),
]

# Initialize embeddings and vectorstore
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
vector_store = Chroma.from_documents(documents, embeddings)

# Create a retriever with MMR
# retriever = vector_store.as_retriever(search_kwargs={'k': 2})
retriever = vector_store.as_retriever(search_type='mmr', search_kwargs={'k': 2})

docs = retriever.invoke("What are good pets?")

for doc in docs:
    print(doc.page_content)