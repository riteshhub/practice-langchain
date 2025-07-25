from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('.data/sample.pdf')
docs = loader.load()

text = """
Honey never spoils. Archaeologists have discovered pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=['\n\n','\n',' ',''] # \n\n : paragraph, \n : next line, ' ' : space, '' : character
)

doc_chunks = splitter.split_documents(documents=docs)
text_chunks = splitter.split_text(text=text)

print(f"docs - first chunk data {doc_chunks[0]}")
print(f"docs - first chunk lenght {len(doc_chunks[0].page_content)}")
print(f"text - first text data {text_chunks[0]}")
print(f"text - first text length {len(text_chunks[0])}")