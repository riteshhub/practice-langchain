from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('.data/sample.pdf')

docs = loader.load()
print(type(docs))
print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)