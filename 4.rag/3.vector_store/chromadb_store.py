from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

loader = PyPDFLoader('.data/diversified_content.pdf')
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=['\n\n','\n',' ',''] # \n\n : paragraph, \n : next line, ' ' : space, '' : character
)

doc_chunks = splitter.split_documents(documents=docs)

vectore_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    persist_directory="./.chroma_db",
    collection_name="sample"
)

vectore_store.add_documents(documents=doc_chunks)
